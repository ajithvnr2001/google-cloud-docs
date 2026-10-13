---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vmware_engine-v1/latest/Google-Api-MethodSettings/
title: Google Cloud VMware Engine V1 API - Class Google::Api::MethodSettings (v1.5.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:44:42.771791+00:00
---

# Google Cloud VMware Engine V1 API - Class Google::Api::MethodSettings (v1.5.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vmware_engine-v1/latest/Google-Api-MethodSettings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Google Cloud VMware Engine V1 API - Class Google::Api::MethodSettings (v1.5.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.5.2 (latest)  1.5.1  1.4.1  1.3.1  1.2.0  1.1.0  1.0.1  0.11.0  0.10.0  0.9.2  0.8.0  0.7.1  0.6.1  0.5.0  0.4.0  0.3.1  0.2.0  0.1.1 

Reference documentation and code samples for the Google Cloud VMware Engine V1 API class Google::Api::MethodSettings.

Describes the generator configuration for a method.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #auto_populated_fields
    
    
    def auto_populated_fields() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — 

List of top-level fields of the request message, that should be automatically populated by the client libraries based on their (google.api.field_info).format. Currently supported format: UUID4.

Example of a YAML configuration:
        
        publishing:
          method_settings:
          - selector: google.example.v1.ExampleService.CreateExample
            auto_populated_fields:
            - request_id
        




### #auto_populated_fields=
    
    
    def auto_populated_fields=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — 

List of top-level fields of the request message, that should be automatically populated by the client libraries based on their (google.api.field_info).format. Currently supported format: UUID4.

Example of a YAML configuration:
        
        publishing:
          method_settings:
          - selector: google.example.v1.ExampleService.CreateExample
            auto_populated_fields:
            - request_id
        




**Returns**

  * (::Array<::String>) — 

List of top-level fields of the request message, that should be automatically populated by the client libraries based on their (google.api.field_info).format. Currently supported format: UUID4.

Example of a YAML configuration:
        
        publishing:
          method_settings:
          - selector: google.example.v1.ExampleService.CreateExample
            auto_populated_fields:
            - request_id
        




### #batching
    
    
    def batching() -> ::Google::Api::BatchingConfigProto

**Returns**

  * ([::Google::Api::BatchingConfigProto](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vmware_engine-v1/latest/Google-Api-BatchingConfigProto)) — 

Batching configuration for an API method in client libraries.

Example of a YAML configuration:
        
        publishing:
          method_settings:
          - selector: google.example.v1.ExampleService.BatchCreateExample
            batching:
              element_count_threshold: 1000
              request_byte_threshold: 100000000
              delay_threshold_millis: 10
        




### #batching=
    
    
    def batching=(value) -> ::Google::Api::BatchingConfigProto

**Parameter**

  * **value** ([::Google::Api::BatchingConfigProto](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vmware_engine-v1/latest/Google-Api-BatchingConfigProto)) — 

Batching configuration for an API method in client libraries.

Example of a YAML configuration:
        
        publishing:
          method_settings:
          - selector: google.example.v1.ExampleService.BatchCreateExample
            batching:
              element_count_threshold: 1000
              request_byte_threshold: 100000000
              delay_threshold_millis: 10
        




**Returns**

  * ([::Google::Api::BatchingConfigProto](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vmware_engine-v1/latest/Google-Api-BatchingConfigProto)) — 

Batching configuration for an API method in client libraries.

Example of a YAML configuration:
        
        publishing:
          method_settings:
          - selector: google.example.v1.ExampleService.BatchCreateExample
            batching:
              element_count_threshold: 1000
              request_byte_threshold: 100000000
              delay_threshold_millis: 10
        




### #long_running
    
    
    def long_running() -> ::Google::Api::MethodSettings::LongRunning

**Returns**

  * ([::Google::Api::MethodSettings::LongRunning](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vmware_engine-v1/latest/Google-Api-MethodSettings-LongRunning)) — 

Describes settings to use for long-running operations when generating API methods for RPCs. Complements RPCs that use the annotations in google/longrunning/operations.proto.

Example of a YAML configuration::
        
        publishing:
          method_settings:
          - selector: google.cloud.speech.v2.Speech.BatchRecognize
            long_running:
              initial_poll_delay: 60s # 1 minute
              poll_delay_multiplier: 1.5
              max_poll_delay: 360s # 6 minutes
              total_poll_timeout: 54000s # 90 minutes
        




### #long_running=
    
    
    def long_running=(value) -> ::Google::Api::MethodSettings::LongRunning

**Parameter**

  * **value** ([::Google::Api::MethodSettings::LongRunning](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vmware_engine-v1/latest/Google-Api-MethodSettings-LongRunning)) — 

Describes settings to use for long-running operations when generating API methods for RPCs. Complements RPCs that use the annotations in google/longrunning/operations.proto.

Example of a YAML configuration::
        
        publishing:
          method_settings:
          - selector: google.cloud.speech.v2.Speech.BatchRecognize
            long_running:
              initial_poll_delay: 60s # 1 minute
              poll_delay_multiplier: 1.5
              max_poll_delay: 360s # 6 minutes
              total_poll_timeout: 54000s # 90 minutes
        




**Returns**

  * ([::Google::Api::MethodSettings::LongRunning](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vmware_engine-v1/latest/Google-Api-MethodSettings-LongRunning)) — 

Describes settings to use for long-running operations when generating API methods for RPCs. Complements RPCs that use the annotations in google/longrunning/operations.proto.

Example of a YAML configuration::
        
        publishing:
          method_settings:
          - selector: google.cloud.speech.v2.Speech.BatchRecognize
            long_running:
              initial_poll_delay: 60s # 1 minute
              poll_delay_multiplier: 1.5
              max_poll_delay: 360s # 6 minutes
              total_poll_timeout: 54000s # 90 minutes
        




### #selector
    
    
    def selector() -> ::String

**Returns**

  * (::String) — 

The fully qualified name of the method, for which the options below apply. This is used to find the method to apply the options.

Example:
        
        publishing:
          method_settings:
          - selector: google.storage.control.v2.StorageControl.CreateFolder
            # method settings for CreateFolder...
        




### #selector=
    
    
    def selector=(value) -> ::String

**Parameter**

  * **value** (::String) — 

The fully qualified name of the method, for which the options below apply. This is used to find the method to apply the options.

Example:
        
        publishing:
          method_settings:
          - selector: google.storage.control.v2.StorageControl.CreateFolder
            # method settings for CreateFolder...
        




**Returns**

  * (::String) — 

The fully qualified name of the method, for which the options below apply. This is used to find the method to apply the options.

Example:
        
        publishing:
          method_settings:
          - selector: google.storage.control.v2.StorageControl.CreateFolder
            # method settings for CreateFolder...
        




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
