---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.TagTemplateOrBuilder
title: Interface TagTemplateOrBuilder (1.101.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:24:06.560379+00:00
---

# Interface TagTemplateOrBuilder (1.101.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.TagTemplateOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface TagTemplateOrBuilder (1.101.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.101.0 (latest)  1.100.0  1.99.0  1.97.0  1.94.0  1.93.0  1.91.0  1.89.0  1.88.0  1.87.0  1.86.0  1.84.0  1.82.0  1.81.0  1.80.0  1.79.0  1.78.0  1.76.0  1.74.0  1.73.0  1.70.0  1.69.0  1.68.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.60.0  1.59.0  1.58.0  1.57.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.48.0  1.47.0  1.46.0  1.45.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.36.0  1.35.0  1.34.0  1.33.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.5  1.8.4  1.7.2  1.6.2  1.5.4 
    
    
    public interface TagTemplateOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### containsFields(String key)
    
    
    public abstract boolean containsFields(String key)

Required. Map of tag template field IDs to the settings for the field. This map is an exhaustive list of the allowed fields. This map must contain at least one field and at most 500 fields.

The keys to this map are tag template field IDs. Field IDs can contain letters (both uppercase and lowercase), numbers (0-9) and underscores (_). Field IDs must be at least 1 character long and at most 64 characters long. Field IDs must start with a letter or underscore.

` map<string, .google.cloud.datacatalog.v1beta1.TagTemplateField> fields = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getDataplexTransferStatus()
    
    
    public abstract TagTemplate.DataplexTransferStatus getDataplexTransferStatus()

Output only. Transfer status of the TagTemplate

` .google.cloud.datacatalog.v1beta1.TagTemplate.DataplexTransferStatus dataplex_transfer_status = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TagTemplate.DataplexTransferStatus](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.TagTemplate.DataplexTransferStatus)` | The dataplexTransferStatus.  
  
### getDataplexTransferStatusValue()
    
    
    public abstract int getDataplexTransferStatusValue()

Output only. Transfer status of the TagTemplate

` .google.cloud.datacatalog.v1beta1.TagTemplate.DataplexTransferStatus dataplex_transfer_status = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for dataplexTransferStatus.  
  
### getDisplayName()
    
    
    public abstract String getDisplayName()

The display name for this template. Defaults to an empty string.

`string display_name = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The displayName.  
  
### getDisplayNameBytes()
    
    
    public abstract ByteString getDisplayNameBytes()

The display name for this template. Defaults to an empty string.

`string display_name = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for displayName.  
  
### getFields() (deprecated)
    
    
    public abstract Map<String,TagTemplateField> getFields()

Use [#getFieldsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.TagTemplateOrBuilder#com_google_cloud_datacatalog_v1beta1_TagTemplateOrBuilder_getFieldsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[TagTemplateField](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.TagTemplateField)>` |   
  
### getFieldsCount()
    
    
    public abstract int getFieldsCount()

Required. Map of tag template field IDs to the settings for the field. This map is an exhaustive list of the allowed fields. This map must contain at least one field and at most 500 fields.

The keys to this map are tag template field IDs. Field IDs can contain letters (both uppercase and lowercase), numbers (0-9) and underscores (_). Field IDs must be at least 1 character long and at most 64 characters long. Field IDs must start with a letter or underscore.

` map<string, .google.cloud.datacatalog.v1beta1.TagTemplateField> fields = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getFieldsMap()
    
    
    public abstract Map<String,TagTemplateField> getFieldsMap()

Required. Map of tag template field IDs to the settings for the field. This map is an exhaustive list of the allowed fields. This map must contain at least one field and at most 500 fields.

The keys to this map are tag template field IDs. Field IDs can contain letters (both uppercase and lowercase), numbers (0-9) and underscores (_). Field IDs must be at least 1 character long and at most 64 characters long. Field IDs must start with a letter or underscore.

` map<string, .google.cloud.datacatalog.v1beta1.TagTemplateField> fields = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[TagTemplateField](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.TagTemplateField)>` |   
  
### getFieldsOrDefault(String key, TagTemplateField defaultValue)
    
    
    public abstract TagTemplateField getFieldsOrDefault(String key, TagTemplateField defaultValue)

Required. Map of tag template field IDs to the settings for the field. This map is an exhaustive list of the allowed fields. This map must contain at least one field and at most 500 fields.

The keys to this map are tag template field IDs. Field IDs can contain letters (both uppercase and lowercase), numbers (0-9) and underscores (_). Field IDs must be at least 1 character long and at most 64 characters long. Field IDs must start with a letter or underscore.

` map<string, .google.cloud.datacatalog.v1beta1.TagTemplateField> fields = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[TagTemplateField](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.TagTemplateField)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TagTemplateField](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.TagTemplateField)` |   
  
### getFieldsOrThrow(String key)
    
    
    public abstract TagTemplateField getFieldsOrThrow(String key)

Required. Map of tag template field IDs to the settings for the field. This map is an exhaustive list of the allowed fields. This map must contain at least one field and at most 500 fields.

The keys to this map are tag template field IDs. Field IDs can contain letters (both uppercase and lowercase), numbers (0-9) and underscores (_). Field IDs must be at least 1 character long and at most 64 characters long. Field IDs must start with a letter or underscore.

` map<string, .google.cloud.datacatalog.v1beta1.TagTemplateField> fields = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TagTemplateField](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.TagTemplateField)` |   
  
### getName()
    
    
    public abstract String getName()

Identifier. The resource name of the tag template in URL format. Example:

  * projects/{project_id}/locations/{location}/tagTemplates/{tag_template_id}

Note that this TagTemplate and its child resources may not actually be stored in the location in this name.




`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Identifier. The resource name of the tag template in URL format. Example:

  * projects/{project_id}/locations/{location}/tagTemplates/{tag_template_id}

Note that this TagTemplate and its child resources may not actually be stored in the location in this name.




`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-04 UTC."],[],[]] 
