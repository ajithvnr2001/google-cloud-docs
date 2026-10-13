---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1beta3/latest/Google-Cloud-DocumentAI-V1beta3-Document-Entity/
title: Document AI V1beta3 API - Class Google::Cloud::DocumentAI::V1beta3::Document::Entity (v0.49.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:29:37.815837+00:00
---

# Document AI V1beta3 API - Class Google::Cloud::DocumentAI::V1beta3::Document::Entity (v0.49.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1beta3/latest/Google-Cloud-DocumentAI-V1beta3-Document-Entity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Document AI V1beta3 API - Class Google::Cloud::DocumentAI::V1beta3::Document::Entity (v0.49.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.49.1 (latest)  0.49.0  0.48.1  0.47.0  0.46.2  0.45.0  0.44.0  0.43.1  0.42.0  0.41.0  0.40.0  0.39.1  0.38.0  0.37.0  0.36.1  0.35.0  0.34.0  0.33.1  0.32.0  0.31.0  0.30.2  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.4 

Reference documentation and code samples for the Document AI V1beta3 API class Google::Cloud::DocumentAI::V1beta3::Document::Entity.

An entity that could be a phrase in the text or a property that belongs to the document. It is a known entity type, such as a person, an organization, or location.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #confidence
    
    
    def confidence() -> ::Float

**Returns**

  * (::Float) — Optional. Confidence of detected Schema entity. Range `[0, 1]`. 



### #confidence=
    
    
    def confidence=(value) -> ::Float

**Parameter**

  * **value** (::Float) — Optional. Confidence of detected Schema entity. Range `[0, 1]`. 



**Returns**

  * (::Float) — Optional. Confidence of detected Schema entity. Range `[0, 1]`. 



### #id
    
    
    def id() -> ::String

**Returns**

  * (::String) — Optional. Canonical id. This will be a unique value in the entity list for this document. 



### #id=
    
    
    def id=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Canonical id. This will be a unique value in the entity list for this document. 



**Returns**

  * (::String) — Optional. Canonical id. This will be a unique value in the entity list for this document. 



### #mention_id
    
    
    def mention_id() -> ::String

**Returns**

  * (::String) — Optional. Deprecated. Use `id` field instead. 



### #mention_id=
    
    
    def mention_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Deprecated. Use `id` field instead. 



**Returns**

  * (::String) — Optional. Deprecated. Use `id` field instead. 



### #mention_text
    
    
    def mention_text() -> ::String

**Returns**

  * (::String) — Optional. Text value of the entity, for example, `1600 Amphitheatre Pkwy`. 



### #mention_text=
    
    
    def mention_text=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Text value of the entity, for example, `1600 Amphitheatre Pkwy`. 



**Returns**

  * (::String) — Optional. Text value of the entity, for example, `1600 Amphitheatre Pkwy`. 



### #method
    
    
    def method() -> ::Google::Cloud::DocumentAI::V1beta3::Document::Entity::Method

**Returns**

  * ([::Google::Cloud::DocumentAI::V1beta3::Document::Entity::Method](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1beta3/latest/Google-Cloud-DocumentAI-V1beta3-Document-Entity-Method)) — Optional. Specifies how the entity's value is obtained. 



### #method=
    
    
    def method=(value) -> ::Google::Cloud::DocumentAI::V1beta3::Document::Entity::Method

**Parameter**

  * **value** ([::Google::Cloud::DocumentAI::V1beta3::Document::Entity::Method](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1beta3/latest/Google-Cloud-DocumentAI-V1beta3-Document-Entity-Method)) — Optional. Specifies how the entity's value is obtained. 



**Returns**

  * ([::Google::Cloud::DocumentAI::V1beta3::Document::Entity::Method](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1beta3/latest/Google-Cloud-DocumentAI-V1beta3-Document-Entity-Method)) — Optional. Specifies how the entity's value is obtained. 



### #normalized_value
    
    
    def normalized_value() -> ::Google::Cloud::DocumentAI::V1beta3::Document::Entity::NormalizedValue

**Returns**

  * ([::Google::Cloud::DocumentAI::V1beta3::Document::Entity::NormalizedValue](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1beta3/latest/Google-Cloud-DocumentAI-V1beta3-Document-Entity-NormalizedValue)) — Optional. Normalized entity value. Absent if the extracted value could not be converted or the type (for example, address) is not supported for certain parsers. This field is also only populated for certain supported document types. 



### #normalized_value=
    
    
    def normalized_value=(value) -> ::Google::Cloud::DocumentAI::V1beta3::Document::Entity::NormalizedValue

**Parameter**

  * **value** ([::Google::Cloud::DocumentAI::V1beta3::Document::Entity::NormalizedValue](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1beta3/latest/Google-Cloud-DocumentAI-V1beta3-Document-Entity-NormalizedValue)) — Optional. Normalized entity value. Absent if the extracted value could not be converted or the type (for example, address) is not supported for certain parsers. This field is also only populated for certain supported document types. 



**Returns**

  * ([::Google::Cloud::DocumentAI::V1beta3::Document::Entity::NormalizedValue](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1beta3/latest/Google-Cloud-DocumentAI-V1beta3-Document-Entity-NormalizedValue)) — Optional. Normalized entity value. Absent if the extracted value could not be converted or the type (for example, address) is not supported for certain parsers. This field is also only populated for certain supported document types. 



### #page_anchor
    
    
    def page_anchor() -> ::Google::Cloud::DocumentAI::V1beta3::Document::PageAnchor

**Returns**

  * ([::Google::Cloud::DocumentAI::V1beta3::Document::PageAnchor](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1beta3/latest/Google-Cloud-DocumentAI-V1beta3-Document-PageAnchor)) — Optional. Represents the provenance of this entity wrt. the location on the page where it was found. 



### #page_anchor=
    
    
    def page_anchor=(value) -> ::Google::Cloud::DocumentAI::V1beta3::Document::PageAnchor

**Parameter**

  * **value** ([::Google::Cloud::DocumentAI::V1beta3::Document::PageAnchor](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1beta3/latest/Google-Cloud-DocumentAI-V1beta3-Document-PageAnchor)) — Optional. Represents the provenance of this entity wrt. the location on the page where it was found. 



**Returns**

  * ([::Google::Cloud::DocumentAI::V1beta3::Document::PageAnchor](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1beta3/latest/Google-Cloud-DocumentAI-V1beta3-Document-PageAnchor)) — Optional. Represents the provenance of this entity wrt. the location on the page where it was found. 



### #properties
    
    
    def properties() -> ::Array<::Google::Cloud::DocumentAI::V1beta3::Document::Entity>

**Returns**

  * (::Array<[::Google::Cloud::DocumentAI::V1beta3::Document::Entity](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1beta3/latest/Google-Cloud-DocumentAI-V1beta3-Document-Entity)>) — Optional. Entities can be nested to form a hierarchical data structure representing the content in the document. 



### #properties=
    
    
    def properties=(value) -> ::Array<::Google::Cloud::DocumentAI::V1beta3::Document::Entity>

**Parameter**

  * **value** (::Array<[::Google::Cloud::DocumentAI::V1beta3::Document::Entity](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1beta3/latest/Google-Cloud-DocumentAI-V1beta3-Document-Entity)>) — Optional. Entities can be nested to form a hierarchical data structure representing the content in the document. 



**Returns**

  * (::Array<[::Google::Cloud::DocumentAI::V1beta3::Document::Entity](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1beta3/latest/Google-Cloud-DocumentAI-V1beta3-Document-Entity)>) — Optional. Entities can be nested to form a hierarchical data structure representing the content in the document. 



### #provenance
    
    
    def provenance() -> ::Google::Cloud::DocumentAI::V1beta3::Document::Provenance

**Returns**

  * ([::Google::Cloud::DocumentAI::V1beta3::Document::Provenance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1beta3/latest/Google-Cloud-DocumentAI-V1beta3-Document-Provenance)) — Optional. The history of this annotation. 



### #provenance=
    
    
    def provenance=(value) -> ::Google::Cloud::DocumentAI::V1beta3::Document::Provenance

**Parameter**

  * **value** ([::Google::Cloud::DocumentAI::V1beta3::Document::Provenance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1beta3/latest/Google-Cloud-DocumentAI-V1beta3-Document-Provenance)) — Optional. The history of this annotation. 



**Returns**

  * ([::Google::Cloud::DocumentAI::V1beta3::Document::Provenance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1beta3/latest/Google-Cloud-DocumentAI-V1beta3-Document-Provenance)) — Optional. The history of this annotation. 



### #redacted
    
    
    def redacted() -> ::Boolean

**Returns**

  * (::Boolean) — Optional. Whether the entity will be redacted for de-identification purposes. 



### #redacted=
    
    
    def redacted=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Optional. Whether the entity will be redacted for de-identification purposes. 



**Returns**

  * (::Boolean) — Optional. Whether the entity will be redacted for de-identification purposes. 



### #text_anchor
    
    
    def text_anchor() -> ::Google::Cloud::DocumentAI::V1beta3::Document::TextAnchor

**Returns**

  * ([::Google::Cloud::DocumentAI::V1beta3::Document::TextAnchor](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1beta3/latest/Google-Cloud-DocumentAI-V1beta3-Document-TextAnchor)) — Optional. Provenance of the entity. Text anchor indexing into the [Document.text](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1beta3/latest/Google-Cloud-DocumentAI-V1beta3-Document#Google__Cloud__DocumentAI__V1beta3__Document_text_instance_ "Google::Cloud::DocumentAI::V1beta3::Document#text \(method\)"). 



### #text_anchor=
    
    
    def text_anchor=(value) -> ::Google::Cloud::DocumentAI::V1beta3::Document::TextAnchor

**Parameter**

  * **value** ([::Google::Cloud::DocumentAI::V1beta3::Document::TextAnchor](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1beta3/latest/Google-Cloud-DocumentAI-V1beta3-Document-TextAnchor)) — Optional. Provenance of the entity. Text anchor indexing into the [Document.text](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1beta3/latest/Google-Cloud-DocumentAI-V1beta3-Document#Google__Cloud__DocumentAI__V1beta3__Document_text_instance_ "Google::Cloud::DocumentAI::V1beta3::Document#text \(method\)"). 



**Returns**

  * ([::Google::Cloud::DocumentAI::V1beta3::Document::TextAnchor](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1beta3/latest/Google-Cloud-DocumentAI-V1beta3-Document-TextAnchor)) — Optional. Provenance of the entity. Text anchor indexing into the [Document.text](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1beta3/latest/Google-Cloud-DocumentAI-V1beta3-Document#Google__Cloud__DocumentAI__V1beta3__Document_text_instance_ "Google::Cloud::DocumentAI::V1beta3::Document#text \(method\)"). 



### #type
    
    
    def type() -> ::String

**Returns**

  * (::String) — Required. Entity type from a schema, for example, `Address`. 



### #type=
    
    
    def type=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. Entity type from a schema, for example, `Address`. 



**Returns**

  * (::String) — Required. Entity type from a schema, for example, `Address`. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
