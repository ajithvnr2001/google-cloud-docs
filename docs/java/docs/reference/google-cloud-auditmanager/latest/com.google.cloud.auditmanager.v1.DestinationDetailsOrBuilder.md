---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-auditmanager/latest/com.google.cloud.auditmanager.v1.DestinationDetailsOrBuilder
title: Interface DestinationDetailsOrBuilder (0.17.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:20:40.680941+00:00
---

# Interface DestinationDetailsOrBuilder (0.17.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-auditmanager/latest/com.google.cloud.auditmanager.v1.DestinationDetailsOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface DestinationDetailsOrBuilder (0.17.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.17.0 (latest)  0.13.0  0.12.0  0.11.0  0.9.0  0.6.0  0.5.0  0.3.0  0.1.0 
    
    
    public interface DestinationDetailsOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getDestinationCase()
    
    
    public abstract DestinationDetails.DestinationCase getDestinationCase()

**Returns**  
---  
**Type** | **Description**  
`[DestinationDetails.DestinationCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-auditmanager/latest/com.google.cloud.auditmanager.v1.DestinationDetails.DestinationCase)` |   
  
### getGcsBucketUri()
    
    
    public abstract String getGcsBucketUri()

URI for the Cloud Storage bucket, in the format `gs://{bucket_name}`.

`string gcs_bucket_uri = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The gcsBucketUri.  
  
### getGcsBucketUriBytes()
    
    
    public abstract ByteString getGcsBucketUriBytes()

URI for the Cloud Storage bucket, in the format `gs://{bucket_name}`.

`string gcs_bucket_uri = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for gcsBucketUri.  
  
### hasGcsBucketUri()
    
    
    public abstract boolean hasGcsBucketUri()

URI for the Cloud Storage bucket, in the format `gs://{bucket_name}`.

`string gcs_bucket_uri = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the gcsBucketUri field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
