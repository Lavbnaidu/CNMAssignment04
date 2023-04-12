import sns_module_assignment4
import boto3
import logging
import boto3
from botocore.exceptions import ClientError
import sns_config

sub_name = sns_config.name
sub_email= sns_config.email
# logger config
logger = logging.getLogger()
if __name__ == '__main__':
    logger.info(f'Creating SNS topic {sub_name}...')
    topic = sns_module_assignment4.create_topic(sub_name)
    list_topic = sns_module_assignment4.list_topics()
    user_subs =sns_module_assignment4.subscribe(sub_name,sub_email)
