---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.IngestionDataSourceSettings.AwsKinesisOrBuilder
title: Interface IngestionDataSourceSettings.AwsKinesisOrBuilder (1.157.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:25:47.785302+00:00
---

# Interface IngestionDataSourceSettings.AwsKinesisOrBuilder (1.157.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.IngestionDataSourceSettings.AwsKinesisOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface IngestionDataSourceSettings.AwsKinesisOrBuilder (1.157.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.157.0 (latest)  1.153.0  1.152.0  1.151.0  1.150.1  1.149.0  1.148.0  1.147.0  1.145.0  1.143.1  1.142.0  1.141.5  1.140.2  1.139.4  1.138.0  1.137.1  1.136.1  1.135.0  1.134.2  1.133.1  1.132.2  1.131.0  1.130.0  1.129.6  1.127.3  1.126.6  1.125.13  1.123.18  1.122.2  1.121.1  1.120.24  1.119.1  1.118.0  1.117.0  1.116.4  1.115.5 
    
    
    public static interface IngestionDataSourceSettings.AwsKinesisOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAwsRoleArn()
    
    
    public abstract String getAwsRoleArn()

Required. AWS role ARN to be used for Federated Identity authentication with Kinesis. Check the Pub/Sub docs for how to set up this role and the required permissions that need to be attached to it.

`string aws_role_arn = 4 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The awsRoleArn.  
  
### getAwsRoleArnBytes()
    
    
    public abstract ByteString getAwsRoleArnBytes()

Required. AWS role ARN to be used for Federated Identity authentication with Kinesis. Check the Pub/Sub docs for how to set up this role and the required permissions that need to be attached to it.

`string aws_role_arn = 4 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for awsRoleArn.  
  
### getConsumerArn()
    
    
    public abstract String getConsumerArn()

Required. The Kinesis consumer ARN to used for ingestion in Enhanced Fan-Out mode. The consumer must be already created and ready to be used.

`string consumer_arn = 3 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The consumerArn.  
  
### getConsumerArnBytes()
    
    
    public abstract ByteString getConsumerArnBytes()

Required. The Kinesis consumer ARN to used for ingestion in Enhanced Fan-Out mode. The consumer must be already created and ready to be used.

`string consumer_arn = 3 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for consumerArn.  
  
### getGcpServiceAccount()
    
    
    public abstract String getGcpServiceAccount()

Required. The GCP service account to be used for Federated Identity authentication with Kinesis (via a `AssumeRoleWithWebIdentity` call for the provided role). The `aws_role_arn` must be set up with `accounts.google.com:sub` equals to this service account number.

`string gcp_service_account = 5 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The gcpServiceAccount.  
  
### getGcpServiceAccountBytes()
    
    
    public abstract ByteString getGcpServiceAccountBytes()

Required. The GCP service account to be used for Federated Identity authentication with Kinesis (via a `AssumeRoleWithWebIdentity` call for the provided role). The `aws_role_arn` must be set up with `accounts.google.com:sub` equals to this service account number.

`string gcp_service_account = 5 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for gcpServiceAccount.  
  
### getState()
    
    
    public abstract IngestionDataSourceSettings.AwsKinesis.State getState()

Output only. An output-only field that indicates the state of the Kinesis ingestion source.

` .google.pubsub.v1.IngestionDataSourceSettings.AwsKinesis.State state = 1 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[IngestionDataSourceSettings.AwsKinesis.State](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.IngestionDataSourceSettings.AwsKinesis.State)` | The state.  
  
### getStateValue()
    
    
    public abstract int getStateValue()

Output only. An output-only field that indicates the state of the Kinesis ingestion source.

` .google.pubsub.v1.IngestionDataSourceSettings.AwsKinesis.State state = 1 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for state.  
  
### getStreamArn()
    
    
    public abstract String getStreamArn()

Required. The Kinesis stream ARN to ingest data from.

`string stream_arn = 2 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The streamArn.  
  
### getStreamArnBytes()
    
    
    public abstract ByteString getStreamArnBytes()

Required. The Kinesis stream ARN to ingest data from.

`string stream_arn = 2 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for streamArn.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
