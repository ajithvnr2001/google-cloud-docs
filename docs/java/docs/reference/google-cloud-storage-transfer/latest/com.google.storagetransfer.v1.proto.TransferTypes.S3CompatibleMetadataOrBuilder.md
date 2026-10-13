---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.S3CompatibleMetadataOrBuilder
title: Interface TransferTypes.S3CompatibleMetadataOrBuilder (1.99.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:39:19.085614+00:00
---

# Interface TransferTypes.S3CompatibleMetadataOrBuilder (1.99.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.S3CompatibleMetadataOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface TransferTypes.S3CompatibleMetadataOrBuilder (1.99.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.99.0 (latest)  1.95.0  1.94.0  1.93.0  1.91.0  1.88.0  1.87.0  1.85.0  1.83.0  1.82.0  1.80.0  1.78.0  1.76.0  1.75.0  1.74.0  1.73.0  1.72.0  1.70.0  1.68.0  1.67.0  1.64.0  1.63.0  1.62.0  1.60.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.49.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.37.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.0.4 
    
    
    public static interface TransferTypes.S3CompatibleMetadataOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAuthMethod()
    
    
    public abstract TransferTypes.S3CompatibleMetadata.AuthMethod getAuthMethod()

Specifies the authentication and authorization method used by the storage service. When not specified, Transfer Service will attempt to determine right auth method to use.

`.google.storagetransfer.v1.S3CompatibleMetadata.AuthMethod auth_method = 1;`

**Returns**  
---  
**Type** | **Description**  
`[TransferTypes.S3CompatibleMetadata.AuthMethod](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.S3CompatibleMetadata.AuthMethod)` | The authMethod.  
  
### getAuthMethodValue()
    
    
    public abstract int getAuthMethodValue()

Specifies the authentication and authorization method used by the storage service. When not specified, Transfer Service will attempt to determine right auth method to use.

`.google.storagetransfer.v1.S3CompatibleMetadata.AuthMethod auth_method = 1;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for authMethod.  
  
### getListApi()
    
    
    public abstract TransferTypes.S3CompatibleMetadata.ListApi getListApi()

The Listing API to use for discovering objects. When not specified, Transfer Service will attempt to determine the right API to use.

`.google.storagetransfer.v1.S3CompatibleMetadata.ListApi list_api = 4;`

**Returns**  
---  
**Type** | **Description**  
`[TransferTypes.S3CompatibleMetadata.ListApi](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.S3CompatibleMetadata.ListApi)` | The listApi.  
  
### getListApiValue()
    
    
    public abstract int getListApiValue()

The Listing API to use for discovering objects. When not specified, Transfer Service will attempt to determine the right API to use.

`.google.storagetransfer.v1.S3CompatibleMetadata.ListApi list_api = 4;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for listApi.  
  
### getProtocol()
    
    
    public abstract TransferTypes.S3CompatibleMetadata.NetworkProtocol getProtocol()

Specifies the network protocol of the agent. When not specified, the default value of NetworkProtocol NETWORK_PROTOCOL_HTTPS is used.

`.google.storagetransfer.v1.S3CompatibleMetadata.NetworkProtocol protocol = 3;`

**Returns**  
---  
**Type** | **Description**  
`[TransferTypes.S3CompatibleMetadata.NetworkProtocol](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.S3CompatibleMetadata.NetworkProtocol)` | The protocol.  
  
### getProtocolValue()
    
    
    public abstract int getProtocolValue()

Specifies the network protocol of the agent. When not specified, the default value of NetworkProtocol NETWORK_PROTOCOL_HTTPS is used.

`.google.storagetransfer.v1.S3CompatibleMetadata.NetworkProtocol protocol = 3;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for protocol.  
  
### getRequestModel()
    
    
    public abstract TransferTypes.S3CompatibleMetadata.RequestModel getRequestModel()

Specifies the API request model used to call the storage service. When not specified, the default value of RequestModel REQUEST_MODEL_VIRTUAL_HOSTED_STYLE is used.

`.google.storagetransfer.v1.S3CompatibleMetadata.RequestModel request_model = 2;`

**Returns**  
---  
**Type** | **Description**  
`[TransferTypes.S3CompatibleMetadata.RequestModel](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.S3CompatibleMetadata.RequestModel)` | The requestModel.  
  
### getRequestModelValue()
    
    
    public abstract int getRequestModelValue()

Specifies the API request model used to call the storage service. When not specified, the default value of RequestModel REQUEST_MODEL_VIRTUAL_HOSTED_STYLE is used.

`.google.storagetransfer.v1.S3CompatibleMetadata.RequestModel request_model = 2;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for requestModel.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
