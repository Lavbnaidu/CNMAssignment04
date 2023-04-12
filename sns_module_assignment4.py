import boto3
import json
import logging
import sns_config
from botocore.exceptions import ClientError
logger = logging.getLogger()

sns_client = boto3.client('sns', region_name="us-east-1")
sub_name = sns_config.name
sub_email= sns_config.email
def create_topic(name):
    """
    Creates a SNS notification topic.
    """
    try:
        topic = sns_client.create_topic(Name=sub_name)
        logger.info(f'Created SNS topic {sub_name}.')
    except ClientError:
        logger.exception(f'Could not create SNS topic {sub_name}.')
        raise
    else:
        return topic

def list_topics():
    """
    Lists all SNS notification topics using paginator.
    """
    try:
        paginator = sns_client.get_paginator('list_topics')
        # creating a PageIterator from the paginator
        page_iterator = paginator.paginate().build_full_result()
        topics_list = []
        # loop through each page from page_iterator
        for page in page_iterator['Topics']:
            topics_list.append(page['TopicArn'])
    except ClientError:
        logger.exception(f'Could not list SNS topics.')
        raise
    else:
        return topics_list
    
# Create email subscription
def subscribe(topic):
    subscription = sns_client.subscribe(TopicArn=topic, Protocol="email", Endpoint=sub_email)
    publishing = sns_config.publish(TopicArn=topic, 
            Message="message text", 
            Subject="subject used in emails only")
