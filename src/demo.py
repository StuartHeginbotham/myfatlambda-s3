import logging
import sys
import boto3

logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s')
bucketname='stuarts-bucket'
itemname='test.txt'
s3 = boto3.resource('s3')
obj = s3.Object(bucketname, itemname)

logging.info('Fat Lambda Params ***STARTED***')

logging.info(f'reading bucket {bucketname} file {itemname}')

body = obj.get()['Body'].read()

logging.info(f'{body}')


#try:
#    logging.info(f'Fat Lambda started, param is: {sys.argv[1]}')
#except:
#    logging.info(f'Fat Lambda started but no input paramter supplied')

