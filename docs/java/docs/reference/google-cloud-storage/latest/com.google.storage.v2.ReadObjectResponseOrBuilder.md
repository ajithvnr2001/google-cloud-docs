---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.v2.ReadObjectResponseOrBuilder
title: Interface ReadObjectResponseOrBuilder (2.75.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:43:34.476887+00:00
---

# Interface ReadObjectResponseOrBuilder (2.75.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.v2.ReadObjectResponseOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ReadObjectResponseOrBuilder (2.75.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.75.0 (latest)  2.71.0  2.70.0  2.69.0  2.67.0  2.64.0  2.63.0  2.62.1  2.60.0  2.59.0  2.58.1  2.57.0  2.56.0  2.55.0  2.54.0  2.53.3  2.52.3  2.50.0  2.49.0  2.48.2  2.47.0  2.46.0  2.45.0  2.44.1  2.43.2  2.42.0  2.41.0  2.40.1  2.39.0  2.38.0  2.37.0  2.36.1  2.34.0  2.33.0  2.32.1  2.30.1  2.29.1  2.28.0  2.27.1  2.24.0  2.23.0  2.22.6  2.21.0  2.20.2  2.19.0  2.18.0  2.17.2  2.16.0  2.15.1  2.14.0  2.13.1  2.12.0  2.11.3  2.10.0  2.9.3  2.8.1  2.7.1  2.6.1  2.5.1  2.4.5  2.3.0  2.2.3  2.1.10 
    
    
    public interface ReadObjectResponseOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getChecksummedData()
    
    
    public abstract ChecksummedData getChecksummedData()

A portion of the data for the object. The service might leave `data` empty for any given `ReadResponse`. This enables the service to inform the client that the request is still live while it is running an operation to generate more data.

`.google.storage.v2.ChecksummedData checksummed_data = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ChecksummedData](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.v2.ChecksummedData)` | The checksummedData.  
  
### getChecksummedDataOrBuilder()
    
    
    public abstract ChecksummedDataOrBuilder getChecksummedDataOrBuilder()

A portion of the data for the object. The service might leave `data` empty for any given `ReadResponse`. This enables the service to inform the client that the request is still live while it is running an operation to generate more data.

`.google.storage.v2.ChecksummedData checksummed_data = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ChecksummedDataOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.v2.ChecksummedDataOrBuilder)` |   
  
### getContentRange()
    
    
    public abstract ContentRange getContentRange()

If `read_offset` and or `read_limit` is specified on the `ReadObjectRequest`, `ContentRange` is populated on the first `ReadObjectResponse` message of the read stream.

`.google.storage.v2.ContentRange content_range = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ContentRange](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.v2.ContentRange)` | The contentRange.  
  
### getContentRangeOrBuilder()
    
    
    public abstract ContentRangeOrBuilder getContentRangeOrBuilder()

If `read_offset` and or `read_limit` is specified on the `ReadObjectRequest`, `ContentRange` is populated on the first `ReadObjectResponse` message of the read stream.

`.google.storage.v2.ContentRange content_range = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ContentRangeOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.v2.ContentRangeOrBuilder)` |   
  
### getMetadata()
    
    
    public abstract Object getMetadata()

Metadata of the object whose media is being returned. Only populated in the first response in the stream.

`.google.storage.v2.Object metadata = 4;`

**Returns**  
---  
**Type** | **Description**  
`[Object](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.v2.Object)` | The metadata.  
  
### getMetadataOrBuilder()
    
    
    public abstract ObjectOrBuilder getMetadataOrBuilder()

Metadata of the object whose media is being returned. Only populated in the first response in the stream.

`.google.storage.v2.Object metadata = 4;`

**Returns**  
---  
**Type** | **Description**  
`[ObjectOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.v2.ObjectOrBuilder)` |   
  
### getObjectChecksums()
    
    
    public abstract ObjectChecksums getObjectChecksums()

The checksums of the complete object. If the object is downloaded in full, the client should compute one of these checksums over the downloaded object and compare it against the value provided here.

`.google.storage.v2.ObjectChecksums object_checksums = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ObjectChecksums](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.v2.ObjectChecksums)` | The objectChecksums.  
  
### getObjectChecksumsOrBuilder()
    
    
    public abstract ObjectChecksumsOrBuilder getObjectChecksumsOrBuilder()

The checksums of the complete object. If the object is downloaded in full, the client should compute one of these checksums over the downloaded object and compare it against the value provided here.

`.google.storage.v2.ObjectChecksums object_checksums = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ObjectChecksumsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.v2.ObjectChecksumsOrBuilder)` |   
  
### hasChecksummedData()
    
    
    public abstract boolean hasChecksummedData()

A portion of the data for the object. The service might leave `data` empty for any given `ReadResponse`. This enables the service to inform the client that the request is still live while it is running an operation to generate more data.

`.google.storage.v2.ChecksummedData checksummed_data = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the checksummedData field is set.  
  
### hasContentRange()
    
    
    public abstract boolean hasContentRange()

If `read_offset` and or `read_limit` is specified on the `ReadObjectRequest`, `ContentRange` is populated on the first `ReadObjectResponse` message of the read stream.

`.google.storage.v2.ContentRange content_range = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the contentRange field is set.  
  
### hasMetadata()
    
    
    public abstract boolean hasMetadata()

Metadata of the object whose media is being returned. Only populated in the first response in the stream.

`.google.storage.v2.Object metadata = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the metadata field is set.  
  
### hasObjectChecksums()
    
    
    public abstract boolean hasObjectChecksums()

The checksums of the complete object. If the object is downloaded in full, the client should compute one of these checksums over the downloaded object and compare it against the value provided here.

`.google.storage.v2.ObjectChecksums object_checksums = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the objectChecksums field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
