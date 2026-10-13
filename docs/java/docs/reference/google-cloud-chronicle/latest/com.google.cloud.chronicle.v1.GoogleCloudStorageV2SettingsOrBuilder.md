---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.GoogleCloudStorageV2SettingsOrBuilder
title: Interface GoogleCloudStorageV2SettingsOrBuilder (0.37.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:34:20.506465+00:00
---

# Interface GoogleCloudStorageV2SettingsOrBuilder (0.37.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.GoogleCloudStorageV2SettingsOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface GoogleCloudStorageV2SettingsOrBuilder (0.37.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.37.0 (latest)  0.33.0  0.32.0  0.31.0  0.29.0  0.26.0  0.25.0  0.23.0  0.21.0  0.20.0  0.19.0  0.18.0  0.16.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.6.0  0.5.0  0.2.0  0.1.0 
    
    
    public interface GoogleCloudStorageV2SettingsOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getBucketUri()
    
    
    public abstract String getBucketUri()

Required. Google Cloud Storage Bucket URI for the feed.

`string bucket_uri = 1 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The bucketUri.  
  
### getBucketUriBytes()
    
    
    public abstract ByteString getBucketUriBytes()

Required. Google Cloud Storage Bucket URI for the feed.

`string bucket_uri = 1 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for bucketUri.  
  
### getChronicleServiceAccount()
    
    
    public abstract String getChronicleServiceAccount()

Output only. SA that will read data, this is Storage Transfer Service SA of Customer's Tenancy Project.

`string chronicle_service_account = 3 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The chronicleServiceAccount.  
  
### getChronicleServiceAccountBytes()
    
    
    public abstract ByteString getChronicleServiceAccountBytes()

Output only. SA that will read data, this is Storage Transfer Service SA of Customer's Tenancy Project.

`string chronicle_service_account = 3 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for chronicleServiceAccount.  
  
### getIncludePrefixes(int index)
    
    
    public abstract String getIncludePrefixes(int index)

Optional. Optional list of object prefixes to include.

`repeated string include_prefixes = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The includePrefixes at the given index.  
  
### getIncludePrefixesBytes(int index)
    
    
    public abstract ByteString getIncludePrefixesBytes(int index)

Optional. Optional list of object prefixes to include.

`repeated string include_prefixes = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the includePrefixes at the given index.  
  
### getIncludePrefixesCount()
    
    
    public abstract int getIncludePrefixesCount()

Optional. Optional list of object prefixes to include.

`repeated string include_prefixes = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of includePrefixes.  
  
### getIncludePrefixesList()
    
    
    public abstract List<String> getIncludePrefixesList()

Optional. Optional list of object prefixes to include.

`repeated string include_prefixes = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the includePrefixes.  
  
### getMaxLookbackDays()
    
    
    public abstract int getMaxLookbackDays()

Optional. Maximum File Age to ingest in days.

`int32 max_lookback_days = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The maxLookbackDays.  
  
### getSourceDeletionOption()
    
    
    public abstract SourceDeletionOptionV2 getSourceDeletionOption()

Optional. Source deletion option determines if the data from the source is to be deleted after ingestion.

` .google.cloud.chronicle.v1.SourceDeletionOptionV2 source_deletion_option = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[SourceDeletionOptionV2](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.SourceDeletionOptionV2)` | The sourceDeletionOption.  
  
### getSourceDeletionOptionValue()
    
    
    public abstract int getSourceDeletionOptionValue()

Optional. Source deletion option determines if the data from the source is to be deleted after ingestion.

` .google.cloud.chronicle.v1.SourceDeletionOptionV2 source_deletion_option = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for sourceDeletionOption.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
