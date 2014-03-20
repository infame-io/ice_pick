"""
ice_pick.filters.operations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module contains a set of constants that can be used as operation
filters. All the constants are based on AWS definitions.

Copyright 2014 Demand Media.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""


A = 'A'
AAAA = 'AAAA'
ANY = 'ANY'
ASSOCIATE_ADDRESS = 'AssociateAddress'
ASSOCIATED_ADDRESS_VPC = 'AssociateAddressVPC'
BATCH_PUT_ATTRIBUTES = 'BatchPutAttributes'
CNAME = 'CNAME'
COMMITED_THROUGHPUT = 'CommittedThroughput'
COMPLETE_MULTIPART_UPLOAD = 'CompleteMultipartUpload'
COPY_OBJECT = 'CopyObject'
COPY_OBJECT_GET = 'CopyObjectGet'
CREATE = 'Create'
CREATE_BUCKET = 'CreateBucket'
CREATE_CACHE_CLUSTER_0001 = 'CreateCacheCluster:0001'
CREATE_CACHE_CLUSTER_0002 = 'CreateCacheCluster:0002'
CREATE_DB_INSTANCE = 'CreateDBInstance'
CREATE_DB_INSTANCE_0002 = 'CreateDBInstance:0002'
CREATE_DOMAIN = 'CreateDomain'
CREATE_SNAPSHOT = 'CreateSnapshot'
CREATE_TOPIC = 'CreateTopic'
CREATE_VOLUME = 'CreateVolume'
CREATE_VOLUME_P_IOPS = 'CreateVolume-P-IOPS'
CREATE_VPN_CONNECTION = 'CreateVpnConnection'
DATA_PIPELINE = 'datapipeline'
DELETE_ARCHIVE = 'DeleteArchive'
DELETE_BUCKET = 'DeleteBucket'
DELETE_MESSAGE = 'DeleteMessage'
DELETE_OBJECT = 'DeleteObject'
DESCRIBE_JOB = 'DescribeJob'
DESCRIBE_TABLE = 'DescribeTable'
DESCRIBE_VAULT = 'DescribeVault'
EBS_IO_READ = 'EBS:IO-Read'
EBS_IO_WRITE = 'EBS:IO-Write'
GET = 'GET'
GET_JOB_OUTPUT = 'GetJobOutput'
GET_METRIC_STATISTICS = 'GetMetricStatistics'
GET_OBJECT = 'GetObject'
GET_QUEUE_ATTRIBUTE = 'GetQueueAttributes'
GET_TOPIC_ATTRIBUTE = 'GetTopicAttributes'
GET_VAULT_NOTIFICATION = 'GetVaultNotifications'
GLACIER_OBJECT_OVERHEAD = 'GlacierObjectOverhead'
GLACIER_S3_OBJECT_OVERHEAD = 'GlacierS3ObjectOverhead'
GLACIER_STORAGE = 'GlacierStorage'
HEAD = 'HEAD'
HEAD_BUCKET = 'HeadBucket'
HEAD_OBJECT = 'HeadObject'
HOSTED_ZONE = 'HostedZone'
HOURLY = 'Hourly'
INITIATE_JOB = 'InitiateJob'
INITIATE_MULTIPART_UPLOAD = 'InitiateMultipartUpload'
INTER_ZONE_IN = 'InterZone-In'
INTER_ZONE_OUT = 'InterZone-Out'
LIST = 'List'
LIST_ALL_MY_BUCKETS = 'ListAllMyBuckets'
LIST_BUCKET = 'ListBucket'
LIST_BUCKET_VERSIONS = 'ListBucketVersions'
LIST_DOMAINS = 'ListDomains'
LIST_JOBS = 'ListJobs'
LIST_METRICS = 'ListMetrics'
LIST_MULTIPART_UPLOADS = 'ListMultipartUploads'
LIST_PARTS = 'ListParts'
LIST_PLATFORM_APPLICATIONS = 'ListPlatformApplications'
LIST_SUBSCRIPTIONS = 'ListSubscriptions'
LIST_SUBSCRIPTIONS_BY_TOPIC = 'ListSubscriptionsByTopic'
LIST_TABLES = 'ListTables'
LIST_TOPICS = 'ListTopics'
LIST_VAULTS = 'ListVaults'
LOAD_BALANCING = 'LoadBalancing'
LOAD_BALANCING_PUBLIC_IP_IN = 'LoadBalancing-PublicIP-In'
LOAD_BALANCING_PUBLIC_IP_OUT = 'LoadBalancing-PublicIP-Out'
MX = 'MX'
METRIC_STORAGE = 'MetricStorage'
NS = 'NS'
NOT_APPLICABLE = 'Not Applicable'
NOTIFICATION = 'Notification'
ONDEMAND_INSTANCES = 'OndemandInstances'
PTR = 'PTR'
PREFLIGHT_REQUEST = 'PreflightRequest'
PUBLIC_IP_IN = 'PublicIP-In'
PUBLIC_IP_OUT = 'PublicIP-Out'
PUBLISH = 'Publish'
PUT_ITEM = 'PutItem'
PUT_METRIC_DATA = 'PutMetricData'
PUT_OBJECT = 'PutObject'
PUT_REQUEST = 'PutRequest'
READ_ACL = 'ReadACL'
READ_BUCKET_CORS = 'ReadBucketCors'
READ_BUCKET_LIFECYCLE = 'ReadBucketLifecycle'
READ_BUCKET_POLICY = 'ReadBucketPolicy'
READ_BUCKET_WEBSITE = 'ReadBucketWebsite'
READ_COST_ALLOWCATION = 'ReadCostAllocation'
READ_LOCATION = 'ReadLocation'
READ_LOG_PROPS = 'ReadLogProps'
READ_NOTIFICATION_PROPS = 'ReadNotificationProps'
READ_REQUEST_PAYMENT_PROPS = 'ReadRequestPaymentProps'
READ_VERSIONING_PROPS = 'ReadVersioningProps'
RECEIVE = 'Receive'
REDUCED_REDUNDANCY_STORAGE = 'ReducedRedundancyStorage'
RESERVED_INSTANCES = 'ReservedInstances'
RUN_INSTANCES = 'RunInstances'
RUN_INSTANCES_S0001 = 'RunInstances:S0001'
RUN_INSTANCES_S0006 = 'RunInstances:S0006'
RUN_INSTANCES_S0007 = 'RunInstances:S0007'
S3_GLACIER_TRANSITION = 'S3-GlacierTransition'
SHARD_HOUR_STORAGE = 'shardHourStorage'
SOA = 'SOA'
SPF = 'SPF'
SRV = 'SRV'
SSL_CERT_CUSTOM = 'SSL-Cert-Custom'
SELECT_GET = 'SelectGet'
SEND = 'Send'
SEND_EMAIL = 'SendEmail'
SEND_RAW_EMAIL = 'SendRawEmail'
SET_QUEUE_ATTRIBUTE = 'SetQueueAttributes'
SET_TOPIC_ATTRIBUTE = 'SetTopicAttributes'
STANDARD_STORAGE = 'StandardStorage'
STORAGE = 'Storage'
SUBSCRIBE = 'Subscribe'
SUBSCRIPTION_CONFIRMATION = 'SubscriptionConfirmation'
TXT = 'TXT'
UNSUPPORTED = 'UNSUPPORTED'
UNKNOWN = 'Unknown'
UNKNOWN_ACTION = 'UnknownAction'
UPLOAD_ARCHIVE = 'UploadArchive'
UPLOAD_MULTIPART_PART = 'UploadMultipartPart'
UPLOAD_PART = 'UploadPart'
URL_INFO = 'UrlInfo'
WEBSITE_GET_OBJECT = 'WebsiteGetObject'
WEBSITE_HEAD_OBJECT = 'WebsiteHeadObject'
WRITE_ACL = 'WriteACL'
WRITE_BUCKET_LIFECYCLE = 'WriteBucketLifecycle'
WRITE_BUCKET_POLICY = 'WriteBucketPolicy'
WRITE_BUCKET_WEBSITE = 'WriteBucketWebsite'
WRITE_LOG_PROPS = 'WriteLogProps'
WRITE_VERSIONING_PROPS = 'WriteVersioningProps'
