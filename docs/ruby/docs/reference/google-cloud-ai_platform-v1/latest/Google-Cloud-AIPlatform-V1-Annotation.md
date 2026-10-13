---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Annotation/
title: Vertex AI V1 API - Class Google::Cloud::AIPlatform::V1::Annotation (v1.49.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:07:35.126414+00:00
---

# Vertex AI V1 API - Class Google::Cloud::AIPlatform::V1::Annotation (v1.49.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Annotation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Vertex AI V1 API - Class Google::Cloud::AIPlatform::V1::Annotation (v1.49.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.49.0 (latest)  1.48.0  1.47.1  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.1  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.1  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.64.0  0.63.0  0.62.0  0.61.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.1  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Vertex AI V1 API class Google::Cloud::AIPlatform::V1::Annotation.

Used to assign specific AnnotationSpec to a particular area of a DataItem or the whole part of the DataItem.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #annotation_source
    
    
    def annotation_source() -> ::Google::Cloud::AIPlatform::V1::UserActionReference

**Returns**

  * ([::Google::Cloud::AIPlatform::V1::UserActionReference](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-UserActionReference)) — Output only. The source of the Annotation. 



### #create_time
    
    
    def create_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Protobuf-Timestamp)) — Output only. Timestamp when this Annotation was created. 



### #etag
    
    
    def etag() -> ::String

**Returns**

  * (::String) — Optional. Used to perform consistent read-modify-write updates. If not set, a blind "overwrite" update happens. 



### #etag=
    
    
    def etag=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Used to perform consistent read-modify-write updates. If not set, a blind "overwrite" update happens. 



**Returns**

  * (::String) — Optional. Used to perform consistent read-modify-write updates. If not set, a blind "overwrite" update happens. 



### #labels
    
    
    def labels() -> ::Google::Protobuf::Map{::String => ::String}

**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — 

Optional. The labels with user-defined metadata to organize your Annotations.

Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. No more than 64 user labels can be associated with one Annotation(System labels are excluded).

See https://goo.gl/xmQnxf for more information and examples of labels. System reserved label keys are prefixed with "aiplatform.googleapis.com/" and are immutable. Following system labels exist for each Annotation:

    * "aiplatform.googleapis.com/annotation_set_name": optional, name of the UI's annotation set this Annotation belongs to. If not set, the Annotation is not visible in the UI.

    * "aiplatform.googleapis.com/payload_schema": output only, its value is the [payload_schema's][google.cloud.aiplatform.v1.Annotation.payload_schema_uri] title.




### #labels=
    
    
    def labels=(value) -> ::Google::Protobuf::Map{::String => ::String}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::String}) — 

Optional. The labels with user-defined metadata to organize your Annotations.

Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. No more than 64 user labels can be associated with one Annotation(System labels are excluded).

See https://goo.gl/xmQnxf for more information and examples of labels. System reserved label keys are prefixed with "aiplatform.googleapis.com/" and are immutable. Following system labels exist for each Annotation:

    * "aiplatform.googleapis.com/annotation_set_name": optional, name of the UI's annotation set this Annotation belongs to. If not set, the Annotation is not visible in the UI.

    * "aiplatform.googleapis.com/payload_schema": output only, its value is the [payload_schema's][google.cloud.aiplatform.v1.Annotation.payload_schema_uri] title.




**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — 

Optional. The labels with user-defined metadata to organize your Annotations.

Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. No more than 64 user labels can be associated with one Annotation(System labels are excluded).

See https://goo.gl/xmQnxf for more information and examples of labels. System reserved label keys are prefixed with "aiplatform.googleapis.com/" and are immutable. Following system labels exist for each Annotation:

    * "aiplatform.googleapis.com/annotation_set_name": optional, name of the UI's annotation set this Annotation belongs to. If not set, the Annotation is not visible in the UI.

    * "aiplatform.googleapis.com/payload_schema": output only, its value is the [payload_schema's][google.cloud.aiplatform.v1.Annotation.payload_schema_uri] title.




### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Output only. Resource name of the Annotation. 



### #payload
    
    
    def payload() -> ::Google::Protobuf::Value

**Returns**

  * ([::Google::Protobuf::Value](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Protobuf-Value)) — Required. The schema of the payload can be found in [payload_schema](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Annotation#Google__Cloud__AIPlatform__V1__Annotation_payload_schema_uri_instance_ "Google::Cloud::AIPlatform::V1::Annotation#payload_schema_uri \(method\)"). 



### #payload=
    
    
    def payload=(value) -> ::Google::Protobuf::Value

**Parameter**

  * **value** ([::Google::Protobuf::Value](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Protobuf-Value)) — Required. The schema of the payload can be found in [payload_schema](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Annotation#Google__Cloud__AIPlatform__V1__Annotation_payload_schema_uri_instance_ "Google::Cloud::AIPlatform::V1::Annotation#payload_schema_uri \(method\)"). 



**Returns**

  * ([::Google::Protobuf::Value](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Protobuf-Value)) — Required. The schema of the payload can be found in [payload_schema](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Annotation#Google__Cloud__AIPlatform__V1__Annotation_payload_schema_uri_instance_ "Google::Cloud::AIPlatform::V1::Annotation#payload_schema_uri \(method\)"). 



### #payload_schema_uri
    
    
    def payload_schema_uri() -> ::String

**Returns**

  * (::String) — Required. Google Cloud Storage URI points to a YAML file describing [payload](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Annotation#Google__Cloud__AIPlatform__V1__Annotation_payload_instance_ "Google::Cloud::AIPlatform::V1::Annotation#payload \(method\)"). The schema is defined as an [OpenAPI 3.0.2 Schema Object](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.2.md#schemaObject). The schema files that can be used here are found in gs://google-cloud-aiplatform/schema/dataset/annotation/, note that the chosen schema must be consistent with the parent Dataset's [metadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Dataset#Google__Cloud__AIPlatform__V1__Dataset_metadata_schema_uri_instance_ "Google::Cloud::AIPlatform::V1::Dataset#metadata_schema_uri \(method\)"). 



### #payload_schema_uri=
    
    
    def payload_schema_uri=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. Google Cloud Storage URI points to a YAML file describing [payload](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Annotation#Google__Cloud__AIPlatform__V1__Annotation_payload_instance_ "Google::Cloud::AIPlatform::V1::Annotation#payload \(method\)"). The schema is defined as an [OpenAPI 3.0.2 Schema Object](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.2.md#schemaObject). The schema files that can be used here are found in gs://google-cloud-aiplatform/schema/dataset/annotation/, note that the chosen schema must be consistent with the parent Dataset's [metadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Dataset#Google__Cloud__AIPlatform__V1__Dataset_metadata_schema_uri_instance_ "Google::Cloud::AIPlatform::V1::Dataset#metadata_schema_uri \(method\)"). 



**Returns**

  * (::String) — Required. Google Cloud Storage URI points to a YAML file describing [payload](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Annotation#Google__Cloud__AIPlatform__V1__Annotation_payload_instance_ "Google::Cloud::AIPlatform::V1::Annotation#payload \(method\)"). The schema is defined as an [OpenAPI 3.0.2 Schema Object](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.2.md#schemaObject). The schema files that can be used here are found in gs://google-cloud-aiplatform/schema/dataset/annotation/, note that the chosen schema must be consistent with the parent Dataset's [metadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Dataset#Google__Cloud__AIPlatform__V1__Dataset_metadata_schema_uri_instance_ "Google::Cloud::AIPlatform::V1::Dataset#metadata_schema_uri \(method\)"). 



### #update_time
    
    
    def update_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Protobuf-Timestamp)) — Output only. Timestamp when this Annotation was last updated. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
