import logging
import boto3

logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s')

logging.info('Fat Lambda Params ***STARTED***')

bucketname='stuarts-bucket'
itemname='test.txt'

s3 = boto3.resource('s3')

obj = s3.Object(bucketname, itemname)

logging.info(f'Reading Bucket: {bucketname} File: {itemname}')

body = obj.get()['Body'].read()

logging.info(f'File Contents: {body}')




