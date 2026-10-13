---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-ExportEntityTypesRequest/
title: Dialogflow CX V3 API - Class Google::Cloud::Dialogflow::CX::V3::ExportEntityTypesRequest (v1.12.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:20:49.586159+00:00
---

# Dialogflow CX V3 API - Class Google::Cloud::Dialogflow::CX::V3::ExportEntityTypesRequest (v1.12.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-ExportEntityTypesRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Dialogflow CX V3 API - Class Google::Cloud::Dialogflow::CX::V3::ExportEntityTypesRequest (v1.12.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.12.2 (latest)  1.12.1  1.11.0  1.10.1  1.9.0  1.8.0  1.7.0  1.6.1  1.5.0  1.4.0  1.3.0  1.2.0  1.1.1  1.0.0  0.26.0  0.25.0  0.24.2  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.1  0.14.0  0.13.0  0.12.0  0.11.0  0.10.2  0.9.0  0.8.1  0.7.1  0.6.0  0.5.0  0.4.0 

Reference documentation and code samples for the Dialogflow CX V3 API class Google::Cloud::Dialogflow::CX::V3::ExportEntityTypesRequest.

The request message for [EntityTypes.ExportEntityTypes](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-EntityTypes-Client#Google__Cloud__Dialogflow__CX__V3__EntityTypes__Client_export_entity_types_instance_ "Google::Cloud::Dialogflow::CX::V3::EntityTypes::Client#export_entity_types \(method\)").

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #data_format
    
    
    def data_format() -> ::Google::Cloud::Dialogflow::CX::V3::ExportEntityTypesRequest::DataFormat

**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::ExportEntityTypesRequest::DataFormat](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-ExportEntityTypesRequest-DataFormat)) — Optional. The data format of the exported entity types. If not specified, `BLOB` is assumed. 



### #data_format=
    
    
    def data_format=(value) -> ::Google::Cloud::Dialogflow::CX::V3::ExportEntityTypesRequest::DataFormat

**Parameter**

  * **value** ([::Google::Cloud::Dialogflow::CX::V3::ExportEntityTypesRequest::DataFormat](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-ExportEntityTypesRequest-DataFormat)) — Optional. The data format of the exported entity types. If not specified, `BLOB` is assumed. 



**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::ExportEntityTypesRequest::DataFormat](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-ExportEntityTypesRequest-DataFormat)) — Optional. The data format of the exported entity types. If not specified, `BLOB` is assumed. 



### #entity_types
    
    
    def entity_types() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Required. The name of the entity types to export. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/entityTypes/<EntityTypeID>`. 



### #entity_types=
    
    
    def entity_types=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Required. The name of the entity types to export. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/entityTypes/<EntityTypeID>`. 



**Returns**

  * (::Array<::String>) — Required. The name of the entity types to export. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/entityTypes/<EntityTypeID>`. 



### #entity_types_content_inline
    
    
    def entity_types_content_inline() -> ::Boolean

**Returns**

  * (::Boolean) — Optional. The option to return the serialized entity types inline.

Note: The following fields are mutually exclusive: `entity_types_content_inline`, `entity_types_uri`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #entity_types_content_inline=
    
    
    def entity_types_content_inline=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Optional. The option to return the serialized entity types inline.

Note: The following fields are mutually exclusive: `entity_types_content_inline`, `entity_types_uri`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * (::Boolean) — Optional. The option to return the serialized entity types inline.

Note: The following fields are mutually exclusive: `entity_types_content_inline`, `entity_types_uri`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #entity_types_uri
    
    
    def entity_types_uri() -> ::String

**Returns**

  * (::String) — Optional. The [Google Cloud Storage](https://cloud.google.com/storage/docs/) URI to export the entity types to. The format of this URI must be `gs://<bucket-name>/<object-name>`.

Dialogflow performs a write operation for the Cloud Storage object on the caller's behalf, so your request authentication must have write permissions for the object. For more information, see [Dialogflow access control](https://cloud.google.com/dialogflow/cx/docs/concept/access-control#storage).

Note: The following fields are mutually exclusive: `entity_types_uri`, `entity_types_content_inline`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #entity_types_uri=
    
    
    def entity_types_uri=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The [Google Cloud Storage](https://cloud.google.com/storage/docs/) URI to export the entity types to. The format of this URI must be `gs://<bucket-name>/<object-name>`.

Dialogflow performs a write operation for the Cloud Storage object on the caller's behalf, so your request authentication must have write permissions for the object. For more information, see [Dialogflow access control](https://cloud.google.com/dialogflow/cx/docs/concept/access-control#storage).

Note: The following fields are mutually exclusive: `entity_types_uri`, `entity_types_content_inline`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * (::String) — Optional. The [Google Cloud Storage](https://cloud.google.com/storage/docs/) URI to export the entity types to. The format of this URI must be `gs://<bucket-name>/<object-name>`.

Dialogflow performs a write operation for the Cloud Storage object on the caller's behalf, so your request authentication must have write permissions for the object. For more information, see [Dialogflow access control](https://cloud.google.com/dialogflow/cx/docs/concept/access-control#storage).

Note: The following fields are mutually exclusive: `entity_types_uri`, `entity_types_content_inline`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #language_code
    
    
    def language_code() -> ::String

**Returns**

  * (::String) — Optional. The language to retrieve the entity type for. The following fields are language dependent:

    * `EntityType.entities.value`
    * `EntityType.entities.synonyms`
    * `EntityType.excluded_phrases.value`

If not specified, all language dependent fields will be retrieved. [Many languages](https://cloud.google.com/dialogflow/docs/reference/language) are supported. Note: languages must be enabled in the agent before they can be used. 




### #language_code=
    
    
    def language_code=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The language to retrieve the entity type for. The following fields are language dependent:

    * `EntityType.entities.value`
    * `EntityType.entities.synonyms`
    * `EntityType.excluded_phrases.value`

If not specified, all language dependent fields will be retrieved. [Many languages](https://cloud.google.com/dialogflow/docs/reference/language) are supported. Note: languages must be enabled in the agent before they can be used. 




**Returns**

  * (::String) — Optional. The language to retrieve the entity type for. The following fields are language dependent:

    * `EntityType.entities.value`
    * `EntityType.entities.synonyms`
    * `EntityType.excluded_phrases.value`

If not specified, all language dependent fields will be retrieved. [Many languages](https://cloud.google.com/dialogflow/docs/reference/language) are supported. Note: languages must be enabled in the agent before they can be used. 




### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — Required. The name of the parent agent to export entity types. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>`. 



### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The name of the parent agent to export entity types. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>`. 



**Returns**

  * (::String) — Required. The name of the parent agent to export entity types. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>`. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
