---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.DataExchangeOrBuilder
title: Interface DataExchangeOrBuilder (0.96.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:38:21.808655+00:00
---

# Interface DataExchangeOrBuilder (0.96.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.DataExchangeOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface DataExchangeOrBuilder (0.96.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.96.0 (latest)  0.92.0  0.91.0  0.90.0  0.88.0  0.85.0  0.84.0  0.82.0  0.80.0  0.79.0  0.78.0  0.77.0  0.75.0  0.73.0  0.72.0  0.71.0  0.70.0  0.69.0  0.67.0  0.65.0  0.64.0  0.61.0  0.60.0  0.59.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface DataExchangeOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getDescription()
    
    
    public abstract String getDescription()

Optional. Description of the data exchange. The description must not contain Unicode non-characters as well as C0 and C1 control codes except tabs (HT), new lines (LF), carriage returns (CR), and page breaks (FF). Default value is an empty string. Max length: 2000 bytes.

`string description = 3 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The description.  
  
### getDescriptionBytes()
    
    
    public abstract ByteString getDescriptionBytes()

Optional. Description of the data exchange. The description must not contain Unicode non-characters as well as C0 and C1 control codes except tabs (HT), new lines (LF), carriage returns (CR), and page breaks (FF). Default value is an empty string. Max length: 2000 bytes.

`string description = 3 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for description.  
  
### getDiscoveryType()
    
    
    public abstract DiscoveryType getDiscoveryType()

Optional. Type of discovery on the discovery page for all the listings under this exchange. Updating this field also updates (overwrites) the discovery_type field for all the listings under this exchange.

` optional .google.cloud.bigquery.analyticshub.v1.DiscoveryType discovery_type = 9 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[DiscoveryType](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.DiscoveryType)` | The discoveryType.  
  
### getDiscoveryTypeValue()
    
    
    public abstract int getDiscoveryTypeValue()

Optional. Type of discovery on the discovery page for all the listings under this exchange. Updating this field also updates (overwrites) the discovery_type field for all the listings under this exchange.

` optional .google.cloud.bigquery.analyticshub.v1.DiscoveryType discovery_type = 9 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for discoveryType.  
  
### getDisplayName()
    
    
    public abstract String getDisplayName()

Required. Human-readable display name of the data exchange. The display name must contain only Unicode letters, numbers (0-9), underscores (_), dashes (-), spaces ( ), ampersands (&) and must not start or end with spaces. Default value is an empty string. Max length: 63 bytes.

`string display_name = 2 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The displayName.  
  
### getDisplayNameBytes()
    
    
    public abstract ByteString getDisplayNameBytes()

Required. Human-readable display name of the data exchange. The display name must contain only Unicode letters, numbers (0-9), underscores (_), dashes (-), spaces ( ), ampersands (&) and must not start or end with spaces. Default value is an empty string. Max length: 63 bytes.

`string display_name = 2 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for displayName.  
  
### getDocumentation()
    
    
    public abstract String getDocumentation()

Optional. Documentation describing the data exchange.

`string documentation = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The documentation.  
  
### getDocumentationBytes()
    
    
    public abstract ByteString getDocumentationBytes()

Optional. Documentation describing the data exchange.

`string documentation = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for documentation.  
  
### getIcon()
    
    
    public abstract ByteString getIcon()

Optional. Base64 encoded image representing the data exchange. Max Size: 3.0MiB Expected image dimensions are 512x512 pixels, however the API only performs validation on size of the encoded data. Note: For byte fields, the content of the fields are base64-encoded (which increases the size of the data by 33-36%) when using JSON on the wire.

`bytes icon = 7 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The icon.  
  
### getListingCount()
    
    
    public abstract int getListingCount()

Output only. Number of listings contained in the data exchange.

`int32 listing_count = 6 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The listingCount.  
  
### getLogLinkedDatasetQueryUserEmail()
    
    
    public abstract boolean getLogLinkedDatasetQueryUserEmail()

Optional. By default, false. If true, the DataExchange has an email sharing mandate enabled.

` optional bool log_linked_dataset_query_user_email = 10 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The logLinkedDatasetQueryUserEmail.  
  
### getName()
    
    
    public abstract String getName()

Output only. The resource name of the data exchange. e.g. `projects/myproject/locations/us/dataExchanges/123`.

`string name = 1 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Output only. The resource name of the data exchange. e.g. `projects/myproject/locations/us/dataExchanges/123`.

`string name = 1 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getPrimaryContact()
    
    
    public abstract String getPrimaryContact()

Optional. Email or URL of the primary point of contact of the data exchange. Max Length: 1000 bytes.

`string primary_contact = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The primaryContact.  
  
### getPrimaryContactBytes()
    
    
    public abstract ByteString getPrimaryContactBytes()

Optional. Email or URL of the primary point of contact of the data exchange. Max Length: 1000 bytes.

`string primary_contact = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for primaryContact.  
  
### getSharingEnvironmentConfig()
    
    
    public abstract SharingEnvironmentConfig getSharingEnvironmentConfig()

Optional. Configurable data sharing environment option for a data exchange.

` .google.cloud.bigquery.analyticshub.v1.SharingEnvironmentConfig sharing_environment_config = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[SharingEnvironmentConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.SharingEnvironmentConfig)` | The sharingEnvironmentConfig.  
  
### getSharingEnvironmentConfigOrBuilder()
    
    
    public abstract SharingEnvironmentConfigOrBuilder getSharingEnvironmentConfigOrBuilder()

Optional. Configurable data sharing environment option for a data exchange.

` .google.cloud.bigquery.analyticshub.v1.SharingEnvironmentConfig sharing_environment_config = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[SharingEnvironmentConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.SharingEnvironmentConfigOrBuilder)` |   
  
### hasDiscoveryType()
    
    
    public abstract boolean hasDiscoveryType()

Optional. Type of discovery on the discovery page for all the listings under this exchange. Updating this field also updates (overwrites) the discovery_type field for all the listings under this exchange.

` optional .google.cloud.bigquery.analyticshub.v1.DiscoveryType discovery_type = 9 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the discoveryType field is set.  
  
### hasLogLinkedDatasetQueryUserEmail()
    
    
    public abstract boolean hasLogLinkedDatasetQueryUserEmail()

Optional. By default, false. If true, the DataExchange has an email sharing mandate enabled.

` optional bool log_linked_dataset_query_user_email = 10 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the logLinkedDatasetQueryUserEmail field is set.  
  
### hasSharingEnvironmentConfig()
    
    
    public abstract boolean hasSharingEnvironmentConfig()

Optional. Configurable data sharing environment option for a data exchange.

` .google.cloud.bigquery.analyticshub.v1.SharingEnvironmentConfig sharing_environment_config = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the sharingEnvironmentConfig field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
