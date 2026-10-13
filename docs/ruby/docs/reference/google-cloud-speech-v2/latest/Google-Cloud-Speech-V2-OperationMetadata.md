---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-speech-v2/latest/Google-Cloud-Speech-V2-OperationMetadata/
title: Cloud Speech-to-Text V2 API - Class Google::Cloud::Speech::V2::OperationMetadata (v1.8.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:16:38.524757+00:00
---

# Cloud Speech-to-Text V2 API - Class Google::Cloud::Speech::V2::OperationMetadata (v1.8.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-speech-v2/latest/Google-Cloud-Speech-V2-OperationMetadata/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Speech-to-Text V2 API - Class Google::Cloud::Speech::V2::OperationMetadata (v1.8.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.1 (latest)  1.8.0  1.7.1  1.6.0  1.5.0  1.4.1  1.3.0  1.2.1  1.1.0  1.0.1  0.16.0  0.15.0  0.14.0  0.13.1  0.12.0  0.11.0  0.10.0  0.9.2  0.8.0  0.7.0  0.6.0  0.5.1  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Cloud Speech-to-Text V2 API class Google::Cloud::Speech::V2::OperationMetadata.

Represents the metadata of a long-running operation.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #batch_recognize_metadata
    
    
    def batch_recognize_metadata() -> ::Google::Cloud::Speech::V2::BatchRecognizeMetadata

**Returns**

  * ([::Google::Cloud::Speech::V2::BatchRecognizeMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-speech-v2/latest/Google-Cloud-Speech-V2-BatchRecognizeMetadata)) — Metadata specific to the BatchRecognize method. 



### #batch_recognize_metadata=
    
    
    def batch_recognize_metadata=(value) -> ::Google::Cloud::Speech::V2::BatchRecognizeMetadata

**Parameter**

  * **value** ([::Google::Cloud::Speech::V2::BatchRecognizeMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-speech-v2/latest/Google-Cloud-Speech-V2-BatchRecognizeMetadata)) — Metadata specific to the BatchRecognize method. 



**Returns**

  * ([::Google::Cloud::Speech::V2::BatchRecognizeMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-speech-v2/latest/Google-Cloud-Speech-V2-BatchRecognizeMetadata)) — Metadata specific to the BatchRecognize method. 



### #batch_recognize_request
    
    
    def batch_recognize_request() -> ::Google::Cloud::Speech::V2::BatchRecognizeRequest

**Returns**

  * ([::Google::Cloud::Speech::V2::BatchRecognizeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-speech-v2/latest/Google-Cloud-Speech-V2-BatchRecognizeRequest)) — The BatchRecognizeRequest that spawned the Operation.

Note: The following fields are mutually exclusive: `batch_recognize_request`, `create_recognizer_request`, `update_recognizer_request`, `delete_recognizer_request`, `undelete_recognizer_request`, `create_custom_class_request`, `update_custom_class_request`, `delete_custom_class_request`, `undelete_custom_class_request`, `create_phrase_set_request`, `update_phrase_set_request`, `delete_phrase_set_request`, `undelete_phrase_set_request`, `update_config_request`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #batch_recognize_request=
    
    
    def batch_recognize_request=(value) -> ::Google::Cloud::Speech::V2::BatchRecognizeRequest

**Parameter**

  * **value** ([::Google::Cloud::Speech::V2::BatchRecognizeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-speech-v2/latest/Google-Cloud-Speech-V2-BatchRecognizeRequest)) — The BatchRecognizeRequest that spawned the Operation.

Note: The following fields are mutually exclusive: `batch_recognize_request`, `create_recognizer_request`, `update_recognizer_request`, `delete_recognizer_request`, `undelete_recognizer_request`, `create_custom_class_request`, `update_custom_class_request`, `delete_custom_class_request`, `undelete_custom_class_request`, `create_phrase_set_request`, `update_phrase_set_request`, `delete_phrase_set_request`, `undelete_phrase_set_request`, `update_config_request`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Speech::V2::BatchRecognizeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-speech-v2/latest/Google-Cloud-Speech-V2-BatchRecognizeRequest)) — The BatchRecognizeRequest that spawned the Operation.

Note: The following fields are mutually exclusive: `batch_recognize_request`, `create_recognizer_request`, `update_recognizer_request`, `delete_recognizer_request`, `undelete_recognizer_request`, `create_custom_class_request`, `update_custom_class_request`, `delete_custom_class_request`, `undelete_custom_class_request`, `create_phrase_set_request`, `update_phrase_set_request`, `delete_phrase_set_request`, `undelete_phrase_set_request`, `update_config_request`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #create_custom_class_request
    
    
    def create_custom_class_request() -> ::Google::Cloud::Speech::V2::CreateCustomClassRequest

**Returns**

  * ([::Google::Cloud::Speech::V2::CreateCustomClassRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-speech-v2/latest/Google-Cloud-Speech-V2-CreateCustomClassRequest)) — The CreateCustomClassRequest that spawned the Operation.

Note: The following fields are mutually exclusive: `create_custom_class_request`, `batch_recognize_request`, `create_recognizer_request`, `update_recognizer_request`, `delete_recognizer_request`, `undelete_recognizer_request`, `update_custom_class_request`, `delete_custom_class_request`, `undelete_custom_class_request`, `create_phrase_set_request`, `update_phrase_set_request`, `delete_phrase_set_request`, `undelete_phrase_set_request`, `update_config_request`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #create_custom_class_request=
    
    
    def create_custom_class_request=(value) -> ::Google::Cloud::Speech::V2::CreateCustomClassRequest

**Parameter**

  * **value** ([::Google::Cloud::Speech::V2::CreateCustomClassRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-speech-v2/latest/Google-Cloud-Speech-V2-CreateCustomClassRequest)) — The CreateCustomClassRequest that spawned the Operation.

Note: The following fields are mutually exclusive: `create_custom_class_request`, `batch_recognize_request`, `create_recognizer_request`, `update_recognizer_request`, `delete_recognizer_request`, `undelete_recognizer_request`, `update_custom_class_request`, `delete_custom_class_request`, `undelete_custom_class_request`, `create_phrase_set_request`, `update_phrase_set_request`, `delete_phrase_set_request`, `undelete_phrase_set_request`, `update_config_request`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Speech::V2::CreateCustomClassRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-speech-v2/latest/Google-Cloud-Speech-V2-CreateCustomClassRequest)) — The CreateCustomClassRequest that spawned the Operation.

Note: The following fields are mutually exclusive: `create_custom_class_request`, `batch_recognize_request`, `create_recognizer_request`, `update_recognizer_request`, `delete_recognizer_request`, `undelete_recognizer_request`, `update_custom_class_request`, `delete_custom_class_request`, `undelete_custom_class_request`, `create_phrase_set_request`, `update_phrase_set_request`, `delete_phrase_set_request`, `undelete_phrase_set_request`, `update_config_request`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #create_phrase_set_request
    
    
    def create_phrase_set_request() -> ::Google::Cloud::Speech::V2::CreatePhraseSetRequest

**Returns**

  * ([::Google::Cloud::Speech::V2::CreatePhraseSetRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-speech-v2/latest/Google-Cloud-Speech-V2-CreatePhraseSetRequest)) — The CreatePhraseSetRequest that spawned the Operation.

Note: The following fields are mutually exclusive: `create_phrase_set_request`, `batch_recognize_request`, `create_recognizer_request`, `update_recognizer_request`, `delete_recognizer_request`, `undelete_recognizer_request`, `create_custom_class_request`, `update_custom_class_request`, `delete_custom_class_request`, `undelete_custom_class_request`, `update_phrase_set_request`, `delete_phrase_set_request`, `undelete_phrase_set_request`, `update_config_request`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #create_phrase_set_request=
    
    
    def create_phrase_set_request=(value) -> ::Google::Cloud::Speech::V2::CreatePhraseSetRequest

**Parameter**

  * **value** ([::Google::Cloud::Speech::V2::CreatePhraseSetRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-speech-v2/latest/Google-Cloud-Speech-V2-CreatePhraseSetRequest)) — The CreatePhraseSetRequest that spawned the Operation.

Note: The following fields are mutually exclusive: `create_phrase_set_request`, `batch_recognize_request`, `create_recognizer_request`, `update_recognizer_request`, `delete_recognizer_request`, `undelete_recognizer_request`, `create_custom_class_request`, `update_custom_class_request`, `delete_custom_class_request`, `undelete_custom_class_request`, `update_phrase_set_request`, `delete_phrase_set_request`, `undelete_phrase_set_request`, `update_config_request`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Speech::V2::CreatePhraseSetRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-speech-v2/latest/Google-Cloud-Speech-V2-CreatePhraseSetRequest)) — The CreatePhraseSetRequest that spawned the Operation.

Note: The following fields are mutually exclusive: `create_phrase_set_request`, `batch_recognize_request`, `create_recognizer_request`, `update_recognizer_request`, `delete_recognizer_request`, `undelete_recognizer_request`, `create_custom_class_request`, `update_custom_class_request`, `delete_custom_class_request`, `undelete_custom_class_request`, `update_phrase_set_request`, `delete_phrase_set_request`, `undelete_phrase_set_request`, `update_config_request`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #create_recognizer_request
    
    
    def create_recognizer_request() -> ::Google::Cloud::Speech::V2::CreateRecognizerRequest

**Returns**

  * ([::Google::Cloud::Speech::V2::CreateRecognizerRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-speech-v2/latest/Google-Cloud-Speech-V2-CreateRecognizerRequest)) — The CreateRecognizerRequest that spawned the Operation.

Note: The following fields are mutually exclusive: `create_recognizer_request`, `batch_recognize_request`, `update_recognizer_request`, `delete_recognizer_request`, `undelete_recognizer_request`, `create_custom_class_request`, `update_custom_class_request`, `delete_custom_class_request`, `undelete_custom_class_request`, `create_phrase_set_request`, `update_phrase_set_request`, `delete_phrase_set_request`, `undelete_phrase_set_request`, `update_config_request`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #create_recognizer_request=
    
    
    def create_recognizer_request=(value) -> ::Google::Cloud::Speech::V2::CreateRecognizerRequest

**Parameter**

  * **value** ([::Google::Cloud::Speech::V2::CreateRecognizerRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-speech-v2/latest/Google-Cloud-Speech-V2-CreateRecognizerRequest)) — The CreateRecognizerRequest that spawned the Operation.

Note: The following fields are mutually exclusive: `create_recognizer_request`, `batch_recognize_request`, `update_recognizer_request`, `delete_recognizer_request`, `undelete_recognizer_request`, `create_custom_class_request`, `update_custom_class_request`, `delete_custom_class_request`, `undelete_custom_class_request`, `create_phrase_set_request`, `update_phrase_set_request`, `delete_phrase_set_request`, `undelete_phrase_set_request`, `update_config_request`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Speech::V2::CreateRecognizerRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-speech-v2/latest/Google-Cloud-Speech-V2-CreateRecognizerRequest)) — The CreateRecognizerRequest that spawned the Operation.

Note: The following fields are mutually exclusive: `create_recognizer_request`, `batch_recognize_request`, `update_recognizer_request`, `delete_recognizer_request`, `undelete_recognizer_request`, `create_custom_class_request`, `update_custom_class_request`, `delete_custom_class_request`, `undelete_custom_class_request`, `create_phrase_set_request`, `update_phrase_set_request`, `delete_phrase_set_request`, `undelete_phrase_set_request`, `update_config_request`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #create_time
    
    
    def create_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-speech-v2/latest/Google-Protobuf-Timestamp)) — The time the operation was created. 



### #create_time=
    
    
    def create_time=(value) -> ::Google::Protobuf::Timestamp

**Parameter**

  * **value** ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-speech-v2/latest/Google-Protobuf-Timestamp)) — The time the operation was created. 



**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-speech-v2/latest/Google-Protobuf-Timestamp)) — The time the operation was created. 



### #delete_custom_class_request
    
    
    def delete_custom_class_request() -> ::Google::Cloud::Speech::V2::DeleteCustomClassRequest

**Returns**

  * ([::Google::Cloud::Speech::V2::DeleteCustomClassRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-speech-v2/latest/Google-Cloud-Speech-V2-DeleteCustomClassRequest)) — The DeleteCustomClassRequest that spawned the Operation.

Note: The following fields are mutually exclusive: `delete_custom_class_request`, `batch_recognize_request`, `create_recognizer_request`, `update_recognizer_request`, `delete_recognizer_request`, `undelete_recognizer_request`, `create_custom_class_request`, `update_custom_class_request`, `undelete_custom_class_request`, `create_phrase_set_request`, `update_phrase_set_request`, `delete_phrase_set_request`, `undelete_phrase_set_request`, `update_config_request`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #delete_custom_class_request=
    
    
    def delete_custom_class_request=(value) -> ::Google::Cloud::Speech::V2::DeleteCustomClassRequest

**Parameter**

  * **value** ([::Google::Cloud::Speech::V2::DeleteCustomClassRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-speech-v2/latest/Google-Cloud-Speech-V2-DeleteCustomClassRequest)) — The DeleteCustomClassRequest that spawned the Operation.

Note: The following fields are mutually exclusive: `delete_custom_class_request`, `batch_recognize_request`, `create_recognizer_request`, `update_recognizer_request`, `delete_recognizer_request`, `undelete_recognizer_request`, `create_custom_class_request`, `update_custom_class_request`, `undelete_custom_class_request`, `create_phrase_set_request`, `update_phrase_set_request`, `delete_phrase_set_request`, `undelete_phrase_set_request`, `update_config_request`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Speech::V2::DeleteCustomClassRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-speech-v2/latest/Google-Cloud-Speech-V2-DeleteCustomClassRequest)) — The DeleteCustomClassRequest that spawned the Operation.

Note: The following fields are mutually exclusive: `delete_custom_class_request`, `batch_recognize_request`, `create_recognizer_request`, `update_recognizer_request`, `delete_recognizer_request`, `undelete_recognizer_request`, `create_custom_class_request`, `update_custom_class_request`, `undelete_custom_class_request`, `create_phrase_set_request`, `update_phrase_set_request`, `delete_phrase_set_request`, `undelete_phrase_set_request`, `update_config_request`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #delete_phrase_set_request
    
    
    def delete_phrase_set_request() -> ::Google::Cloud::Speech::V2::DeletePhraseSetRequest

**Returns**

  * ([::Google::Cloud::Speech::V2::DeletePhraseSetRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-speech-v2/latest/Google-Cloud-Speech-V2-DeletePhraseSetRequest)) — The DeletePhraseSetRequest that spawned the Operation.

Note: The following fields are mutually exclusive: `delete_phrase_set_request`, `batch_recognize_request`, `create_recognizer_request`, `update_recognizer_request`, `delete_recognizer_request`, `undelete_recognizer_request`, `create_custom_class_request`, `update_custom_class_request`, `delete_custom_class_request`, `undelete_custom_class_request`, `create_phrase_set_request`, `update_phrase_set_request`, `undelete_phrase_set_request`, `update_config_request`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #delete_phrase_set_request=
    
    
    def delete_phrase_set_request=(value) -> ::Google::Cloud::Speech::V2::DeletePhraseSetRequest

**Parameter**

  * **value** ([::Google::Cloud::Speech::V2::DeletePhraseSetRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-speech-v2/latest/Google-Cloud-Speech-V2-DeletePhraseSetRequest)) — The DeletePhraseSetRequest that spawned the Operation.

Note: The following fields are mutually exclusive: `delete_phrase_set_request`, `batch_recognize_request`, `create_recognizer_request`, `update_recognizer_request`, `delete_recognizer_request`, `undelete_recognizer_request`, `create_custom_class_request`, `update_custom_class_request`, `delete_custom_class_request`, `undelete_custom_class_request`, `create_phrase_set_request`, `update_phrase_set_request`, `undelete_phrase_set_request`, `update_config_request`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Speech::V2::DeletePhraseSetRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-speech-v2/latest/Google-Cloud-Speech-V2-DeletePhraseSetRequest)) — The DeletePhraseSetRequest that spawned the Operation.

Note: The following fields are mutually exclusive: `delete_phrase_set_request`, `batch_recognize_request`, `create_recognizer_request`, `update_recognizer_request`, `delete_recognizer_request`, `undelete_recognizer_request`, `create_custom_class_request`, `update_custom_class_request`, `delete_custom_class_request`, `undelete_custom_class_request`, `create_phrase_set_request`, `update_phrase_set_request`, `undelete_phrase_set_request`, `update_config_request`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #delete_recognizer_request
    
    
    def delete_recognizer_request() -> ::Google::Cloud::Speech::V2::DeleteRecognizerRequest

**Returns**

  * ([::Google::Cloud::Speech::V2::DeleteRecognizerRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-speech-v2/latest/Google-Cloud-Speech-V2-DeleteRecognizerRequest)) — The DeleteRecognizerRequest that spawned the Operation.

Note: The following fields are mutually exclusive: `delete_recognizer_request`, `batch_recognize_request`, `create_recognizer_request`, `update_recognizer_request`, `undelete_recognizer_request`, `create_custom_class_request`, `update_custom_class_request`, `delete_custom_class_request`, `undelete_custom_class_request`, `create_phrase_set_request`, `update_phrase_set_request`, `delete_phrase_set_request`, `undelete_phrase_set_request`, `update_config_request`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #delete_recognizer_request=
    
    
    def delete_recognizer_request=(value) -> ::Google::Cloud::Speech::V2::DeleteRecognizerRequest

**Parameter**

  * **value** ([::Google::Cloud::Speech::V2::DeleteRecognizerRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-speech-v2/latest/Google-Cloud-Speech-V2-DeleteRecognizerRequest)) — The DeleteRecognizerRequest that spawned the Operation.

Note: The following fields are mutually exclusive: `delete_recognizer_request`, `batch_recognize_request`, `create_recognizer_request`, `update_recognizer_request`, `undelete_recognizer_request`, `create_custom_class_request`, `update_custom_class_request`, `delete_custom_class_request`, `undelete_custom_class_request`, `create_phrase_set_request`, `update_phrase_set_request`, `delete_phrase_set_request`, `undelete_phrase_set_request`, `update_config_request`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Speech::V2::DeleteRecognizerRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-speech-v2/latest/Google-Cloud-Speech-V2-DeleteRecognizerRequest)) — The DeleteRecognizerRequest that spawned the Operation.

Note: The following fields are mutually exclusive: `delete_recognizer_request`, `batch_recognize_request`, `create_recognizer_request`, `update_recognizer_request`, `undelete_recognizer_request`, `create_custom_class_request`, `update_custom_class_request`, `delete_custom_class_request`, `undelete_custom_class_request`, `create_phrase_set_request`, `update_phrase_set_request`, `delete_phrase_set_request`, `undelete_phrase_set_request`, `update_config_request`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #kms_key_name
    
    
    def kms_key_name() -> ::String

**Returns**

  * (::String) — The [KMS key name](https://cloud.google.com/kms/docs/resource-hierarchy#keys) with which the content of the Operation is encrypted. The expected format is `projects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}`. 



### #kms_key_name=
    
    
    def kms_key_name=(value) -> ::String

**Parameter**

  * **value** (::String) — The [KMS key name](https://cloud.google.com/kms/docs/resource-hierarchy#keys) with which the content of the Operation is encrypted. The expected format is `projects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}`. 



**Returns**

  * (::String) — The [KMS key name](https://cloud.google.com/kms/docs/resource-hierarchy#keys) with which the content of the Operation is encrypted. The expected format is `projects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}`. 



### #kms_key_version_name
    
    
    def kms_key_version_name() -> ::String

**Returns**

  * (::String) — The [KMS key version name](https://cloud.google.com/kms/docs/resource-hierarchy#key_versions) with which content of the Operation is encrypted. The expected format is `projects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}/cryptoKeyVersions/{crypto_key_version}`. 



### #kms_key_version_name=
    
    
    def kms_key_version_name=(value) -> ::String

**Parameter**

  * **value** (::String) — The [KMS key version name](https://cloud.google.com/kms/docs/resource-hierarchy#key_versions) with which content of the Operation is encrypted. The expected format is `projects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}/cryptoKeyVersions/{crypto_key_version}`. 



**Returns**

  * (::String) — The [KMS key version name](https://cloud.google.com/kms/docs/resource-hierarchy#key_versions) with which content of the Operation is encrypted. The expected format is `projects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}/cryptoKeyVersions/{crypto_key_version}`. 



### #method
    
    
    def method() -> ::String

**Returns**

  * (::String) — The method that triggered the operation. 



### #method=
    
    
    def method=(value) -> ::String

**Parameter**

  * **value** (::String) — The method that triggered the operation. 



**Returns**

  * (::String) — The method that triggered the operation. 



### #progress_percent
    
    
    def progress_percent() -> ::Integer

**Returns**

  * (::Integer) — The percent progress of the Operation. Values can range from 0-100. If the value is 100, then the operation is finished. 



### #progress_percent=
    
    
    def progress_percent=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — The percent progress of the Operation. Values can range from 0-100. If the value is 100, then the operation is finished. 



**Returns**

  * (::Integer) — The percent progress of the Operation. Values can range from 0-100. If the value is 100, then the operation is finished. 



### #resource
    
    
    def resource() -> ::String

**Returns**

  * (::String) — The resource path for the target of the operation. 



### #resource=
    
    
    def resource=(value) -> ::String

**Parameter**

  * **value** (::String) — The resource path for the target of the operation. 



**Returns**

  * (::String) — The resource path for the target of the operation. 



### #undelete_custom_class_request
    
    
    def undelete_custom_class_request() -> ::Google::Cloud::Speech::V2::UndeleteCustomClassRequest

**Returns**

  * ([::Google::Cloud::Speech::V2::UndeleteCustomClassRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-speech-v2/latest/Google-Cloud-Speech-V2-UndeleteCustomClassRequest)) — The UndeleteCustomClassRequest that spawned the Operation.

Note: The following fields are mutually exclusive: `undelete_custom_class_request`, `batch_recognize_request`, `create_recognizer_request`, `update_recognizer_request`, `delete_recognizer_request`, `undelete_recognizer_request`, `create_custom_class_request`, `update_custom_class_request`, `delete_custom_class_request`, `create_phrase_set_request`, `update_phrase_set_request`, `delete_phrase_set_request`, `undelete_phrase_set_request`, `update_config_request`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #undelete_custom_class_request=
    
    
    def undelete_custom_class_request=(value) -> ::Google::Cloud::Speech::V2::UndeleteCustomClassRequest

**Parameter**

  * **value** ([::Google::Cloud::Speech::V2::UndeleteCustomClassRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-speech-v2/latest/Google-Cloud-Speech-V2-UndeleteCustomClassRequest)) — The UndeleteCustomClassRequest that spawned the Operation.

Note: The following fields are mutually exclusive: `undelete_custom_class_request`, `batch_recognize_request`, `create_recognizer_request`, `update_recognizer_request`, `delete_recognizer_request`, `undelete_recognizer_request`, `create_custom_class_request`, `update_custom_class_request`, `delete_custom_class_request`, `create_phrase_set_request`, `update_phrase_set_request`, `delete_phrase_set_request`, `undelete_phrase_set_request`, `update_config_request`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Speech::V2::UndeleteCustomClassRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-speech-v2/latest/Google-Cloud-Speech-V2-UndeleteCustomClassRequest)) — The UndeleteCustomClassRequest that spawned the Operation.

Note: The following fields are mutually exclusive: `undelete_custom_class_request`, `batch_recognize_request`, `create_recognizer_request`, `update_recognizer_request`, `delete_recognizer_request`, `undelete_recognizer_request`, `create_custom_class_request`, `update_custom_class_request`, `delete_custom_class_request`, `create_phrase_set_request`, `update_phrase_set_request`, `delete_phrase_set_request`, `undelete_phrase_set_request`, `update_config_request`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #undelete_phrase_set_request
    
    
    def undelete_phrase_set_request() -> ::Google::Cloud::Speech::V2::UndeletePhraseSetRequest

**Returns**

  * ([::Google::Cloud::Speech::V2::UndeletePhraseSetRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-speech-v2/latest/Google-Cloud-Speech-V2-UndeletePhraseSetRequest)) — The UndeletePhraseSetRequest that spawned the Operation.

Note: The following fields are mutually exclusive: `undelete_phrase_set_request`, `batch_recognize_request`, `create_recognizer_request`, `update_recognizer_request`, `delete_recognizer_request`, `undelete_recognizer_request`, `create_custom_class_request`, `update_custom_class_request`, `delete_custom_class_request`, `undelete_custom_class_request`, `create_phrase_set_request`, `update_phrase_set_request`, `delete_phrase_set_request`, `update_config_request`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #undelete_phrase_set_request=
    
    
    def undelete_phrase_set_request=(value) -> ::Google::Cloud::Speech::V2::UndeletePhraseSetRequest

**Parameter**

  * **value** ([::Google::Cloud::Speech::V2::UndeletePhraseSetRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-speech-v2/latest/Google-Cloud-Speech-V2-UndeletePhraseSetRequest)) — The UndeletePhraseSetRequest that spawned the Operation.

Note: The following fields are mutually exclusive: `undelete_phrase_set_request`, `batch_recognize_request`, `create_recognizer_request`, `update_recognizer_request`, `delete_recognizer_request`, `undelete_recognizer_request`, `create_custom_class_request`, `update_custom_class_request`, `delete_custom_class_request`, `undelete_custom_class_request`, `create_phrase_set_request`, `update_phrase_set_request`, `delete_phrase_set_request`, `update_config_request`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Speech::V2::UndeletePhraseSetRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-speech-v2/latest/Google-Cloud-Speech-V2-UndeletePhraseSetRequest)) — The UndeletePhraseSetRequest that spawned the Operation.

Note: The following fields are mutually exclusive: `undelete_phrase_set_request`, `batch_recognize_request`, `create_recognizer_request`, `update_recognizer_request`, `delete_recognizer_request`, `undelete_recognizer_request`, `create_custom_class_request`, `update_custom_class_request`, `delete_custom_class_request`, `undelete_custom_class_request`, `create_phrase_set_request`, `update_phrase_set_request`, `delete_phrase_set_request`, `update_config_request`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #undelete_recognizer_request
    
    
    def undelete_recognizer_request() -> ::Google::Cloud::Speech::V2::UndeleteRecognizerRequest

**Returns**

  * ([::Google::Cloud::Speech::V2::UndeleteRecognizerRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-speech-v2/latest/Google-Cloud-Speech-V2-UndeleteRecognizerRequest)) — The UndeleteRecognizerRequest that spawned the Operation.

Note: The following fields are mutually exclusive: `undelete_recognizer_request`, `batch_recognize_request`, `create_recognizer_request`, `update_recognizer_request`, `delete_recognizer_request`, `create_custom_class_request`, `update_custom_class_request`, `delete_custom_class_request`, `undelete_custom_class_request`, `create_phrase_set_request`, `update_phrase_set_request`, `delete_phrase_set_request`, `undelete_phrase_set_request`, `update_config_request`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #undelete_recognizer_request=
    
    
    def undelete_recognizer_request=(value) -> ::Google::Cloud::Speech::V2::UndeleteRecognizerRequest

**Parameter**

  * **value** ([::Google::Cloud::Speech::V2::UndeleteRecognizerRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-speech-v2/latest/Google-Cloud-Speech-V2-UndeleteRecognizerRequest)) — The UndeleteRecognizerRequest that spawned the Operation.

Note: The following fields are mutually exclusive: `undelete_recognizer_request`, `batch_recognize_request`, `create_recognizer_request`, `update_recognizer_request`, `delete_recognizer_request`, `create_custom_class_request`, `update_custom_class_request`, `delete_custom_class_request`, `undelete_custom_class_request`, `create_phrase_set_request`, `update_phrase_set_request`, `delete_phrase_set_request`, `undelete_phrase_set_request`, `update_config_request`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Speech::V2::UndeleteRecognizerRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-speech-v2/latest/Google-Cloud-Speech-V2-UndeleteRecognizerRequest)) — The UndeleteRecognizerRequest that spawned the Operation.

Note: The following fields are mutually exclusive: `undelete_recognizer_request`, `batch_recognize_request`, `create_recognizer_request`, `update_recognizer_request`, `delete_recognizer_request`, `create_custom_class_request`, `update_custom_class_request`, `delete_custom_class_request`, `undelete_custom_class_request`, `create_phrase_set_request`, `update_phrase_set_request`, `delete_phrase_set_request`, `undelete_phrase_set_request`, `update_config_request`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #update_config_request
    
    
    def update_config_request() -> ::Google::Cloud::Speech::V2::UpdateConfigRequest

**Returns**

  * ([::Google::Cloud::Speech::V2::UpdateConfigRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-speech-v2/latest/Google-Cloud-Speech-V2-UpdateConfigRequest)) — The UpdateConfigRequest that spawned the Operation.

Note: The following fields are mutually exclusive: `update_config_request`, `batch_recognize_request`, `create_recognizer_request`, `update_recognizer_request`, `delete_recognizer_request`, `undelete_recognizer_request`, `create_custom_class_request`, `update_custom_class_request`, `delete_custom_class_request`, `undelete_custom_class_request`, `create_phrase_set_request`, `update_phrase_set_request`, `delete_phrase_set_request`, `undelete_phrase_set_request`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #update_config_request=
    
    
    def update_config_request=(value) -> ::Google::Cloud::Speech::V2::UpdateConfigRequest

**Parameter**

  * **value** ([::Google::Cloud::Speech::V2::UpdateConfigRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-speech-v2/latest/Google-Cloud-Speech-V2-UpdateConfigRequest)) — The UpdateConfigRequest that spawned the Operation.

Note: The following fields are mutually exclusive: `update_config_request`, `batch_recognize_request`, `create_recognizer_request`, `update_recognizer_request`, `delete_recognizer_request`, `undelete_recognizer_request`, `create_custom_class_request`, `update_custom_class_request`, `delete_custom_class_request`, `undelete_custom_class_request`, `create_phrase_set_request`, `update_phrase_set_request`, `delete_phrase_set_request`, `undelete_phrase_set_request`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Speech::V2::UpdateConfigRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-speech-v2/latest/Google-Cloud-Speech-V2-UpdateConfigRequest)) — The UpdateConfigRequest that spawned the Operation.

Note: The following fields are mutually exclusive: `update_config_request`, `batch_recognize_request`, `create_recognizer_request`, `update_recognizer_request`, `delete_recognizer_request`, `undelete_recognizer_request`, `create_custom_class_request`, `update_custom_class_request`, `delete_custom_class_request`, `undelete_custom_class_request`, `create_phrase_set_request`, `update_phrase_set_request`, `delete_phrase_set_request`, `undelete_phrase_set_request`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #update_custom_class_request
    
    
    def update_custom_class_request() -> ::Google::Cloud::Speech::V2::UpdateCustomClassRequest

**Returns**

  * ([::Google::Cloud::Speech::V2::UpdateCustomClassRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-speech-v2/latest/Google-Cloud-Speech-V2-UpdateCustomClassRequest)) — The UpdateCustomClassRequest that spawned the Operation.

Note: The following fields are mutually exclusive: `update_custom_class_request`, `batch_recognize_request`, `create_recognizer_request`, `update_recognizer_request`, `delete_recognizer_request`, `undelete_recognizer_request`, `create_custom_class_request`, `delete_custom_class_request`, `undelete_custom_class_request`, `create_phrase_set_request`, `update_phrase_set_request`, `delete_phrase_set_request`, `undelete_phrase_set_request`, `update_config_request`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #update_custom_class_request=
    
    
    def update_custom_class_request=(value) -> ::Google::Cloud::Speech::V2::UpdateCustomClassRequest

**Parameter**

  * **value** ([::Google::Cloud::Speech::V2::UpdateCustomClassRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-speech-v2/latest/Google-Cloud-Speech-V2-UpdateCustomClassRequest)) — The UpdateCustomClassRequest that spawned the Operation.

Note: The following fields are mutually exclusive: `update_custom_class_request`, `batch_recognize_request`, `create_recognizer_request`, `update_recognizer_request`, `delete_recognizer_request`, `undelete_recognizer_request`, `create_custom_class_request`, `delete_custom_class_request`, `undelete_custom_class_request`, `create_phrase_set_request`, `update_phrase_set_request`, `delete_phrase_set_request`, `undelete_phrase_set_request`, `update_config_request`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Speech::V2::UpdateCustomClassRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-speech-v2/latest/Google-Cloud-Speech-V2-UpdateCustomClassRequest)) — The UpdateCustomClassRequest that spawned the Operation.

Note: The following fields are mutually exclusive: `update_custom_class_request`, `batch_recognize_request`, `create_recognizer_request`, `update_recognizer_request`, `delete_recognizer_request`, `undelete_recognizer_request`, `create_custom_class_request`, `delete_custom_class_request`, `undelete_custom_class_request`, `create_phrase_set_request`, `update_phrase_set_request`, `delete_phrase_set_request`, `undelete_phrase_set_request`, `update_config_request`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #update_phrase_set_request
    
    
    def update_phrase_set_request() -> ::Google::Cloud::Speech::V2::UpdatePhraseSetRequest

**Returns**

  * ([::Google::Cloud::Speech::V2::UpdatePhraseSetRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-speech-v2/latest/Google-Cloud-Speech-V2-UpdatePhraseSetRequest)) — The UpdatePhraseSetRequest that spawned the Operation.

Note: The following fields are mutually exclusive: `update_phrase_set_request`, `batch_recognize_request`, `create_recognizer_request`, `update_recognizer_request`, `delete_recognizer_request`, `undelete_recognizer_request`, `create_custom_class_request`, `update_custom_class_request`, `delete_custom_class_request`, `undelete_custom_class_request`, `create_phrase_set_request`, `delete_phrase_set_request`, `undelete_phrase_set_request`, `update_config_request`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #update_phrase_set_request=
    
    
    def update_phrase_set_request=(value) -> ::Google::Cloud::Speech::V2::UpdatePhraseSetRequest

**Parameter**

  * **value** ([::Google::Cloud::Speech::V2::UpdatePhraseSetRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-speech-v2/latest/Google-Cloud-Speech-V2-UpdatePhraseSetRequest)) — The UpdatePhraseSetRequest that spawned the Operation.

Note: The following fields are mutually exclusive: `update_phrase_set_request`, `batch_recognize_request`, `create_recognizer_request`, `update_recognizer_request`, `delete_recognizer_request`, `undelete_recognizer_request`, `create_custom_class_request`, `update_custom_class_request`, `delete_custom_class_request`, `undelete_custom_class_request`, `create_phrase_set_request`, `delete_phrase_set_request`, `undelete_phrase_set_request`, `update_config_request`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Speech::V2::UpdatePhraseSetRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-speech-v2/latest/Google-Cloud-Speech-V2-UpdatePhraseSetRequest)) — The UpdatePhraseSetRequest that spawned the Operation.

Note: The following fields are mutually exclusive: `update_phrase_set_request`, `batch_recognize_request`, `create_recognizer_request`, `update_recognizer_request`, `delete_recognizer_request`, `undelete_recognizer_request`, `create_custom_class_request`, `update_custom_class_request`, `delete_custom_class_request`, `undelete_custom_class_request`, `create_phrase_set_request`, `delete_phrase_set_request`, `undelete_phrase_set_request`, `update_config_request`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #update_recognizer_request
    
    
    def update_recognizer_request() -> ::Google::Cloud::Speech::V2::UpdateRecognizerRequest

**Returns**

  * ([::Google::Cloud::Speech::V2::UpdateRecognizerRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-speech-v2/latest/Google-Cloud-Speech-V2-UpdateRecognizerRequest)) — The UpdateRecognizerRequest that spawned the Operation.

Note: The following fields are mutually exclusive: `update_recognizer_request`, `batch_recognize_request`, `create_recognizer_request`, `delete_recognizer_request`, `undelete_recognizer_request`, `create_custom_class_request`, `update_custom_class_request`, `delete_custom_class_request`, `undelete_custom_class_request`, `create_phrase_set_request`, `update_phrase_set_request`, `delete_phrase_set_request`, `undelete_phrase_set_request`, `update_config_request`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #update_recognizer_request=
    
    
    def update_recognizer_request=(value) -> ::Google::Cloud::Speech::V2::UpdateRecognizerRequest

**Parameter**

  * **value** ([::Google::Cloud::Speech::V2::UpdateRecognizerRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-speech-v2/latest/Google-Cloud-Speech-V2-UpdateRecognizerRequest)) — The UpdateRecognizerRequest that spawned the Operation.

Note: The following fields are mutually exclusive: `update_recognizer_request`, `batch_recognize_request`, `create_recognizer_request`, `delete_recognizer_request`, `undelete_recognizer_request`, `create_custom_class_request`, `update_custom_class_request`, `delete_custom_class_request`, `undelete_custom_class_request`, `create_phrase_set_request`, `update_phrase_set_request`, `delete_phrase_set_request`, `undelete_phrase_set_request`, `update_config_request`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Speech::V2::UpdateRecognizerRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-speech-v2/latest/Google-Cloud-Speech-V2-UpdateRecognizerRequest)) — The UpdateRecognizerRequest that spawned the Operation.

Note: The following fields are mutually exclusive: `update_recognizer_request`, `batch_recognize_request`, `create_recognizer_request`, `delete_recognizer_request`, `undelete_recognizer_request`, `create_custom_class_request`, `update_custom_class_request`, `delete_custom_class_request`, `undelete_custom_class_request`, `create_phrase_set_request`, `update_phrase_set_request`, `delete_phrase_set_request`, `undelete_phrase_set_request`, `update_config_request`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #update_time
    
    
    def update_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-speech-v2/latest/Google-Protobuf-Timestamp)) — The time the operation was last updated. 



### #update_time=
    
    
    def update_time=(value) -> ::Google::Protobuf::Timestamp

**Parameter**

  * **value** ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-speech-v2/latest/Google-Protobuf-Timestamp)) — The time the operation was last updated. 



**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-speech-v2/latest/Google-Protobuf-Timestamp)) — The time the operation was last updated. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
