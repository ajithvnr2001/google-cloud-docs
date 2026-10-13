---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1/latest/Google-Cloud-Datastream-V1-GcsDestinationConfig/
title: Datastream V1 API - Class Google::Cloud::Datastream::V1::GcsDestinationConfig (v1.7.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:11:51.009342+00:00
---

# Datastream V1 API - Class Google::Cloud::Datastream::V1::GcsDestinationConfig (v1.7.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1/latest/Google-Cloud-Datastream-V1-GcsDestinationConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Datastream V1 API - Class Google::Cloud::Datastream::V1::GcsDestinationConfig (v1.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.7.1 (latest)  1.7.0  1.6.0  1.5.1  1.4.0  1.3.0  1.2.1  1.1.1  1.0.0  0.13.0  0.12.0  0.11.0  0.10.1  0.9.2  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Datastream V1 API class Google::Cloud::Datastream::V1::GcsDestinationConfig.

Google Cloud Storage destination configuration

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #avro_file_format
    
    
    def avro_file_format() -> ::Google::Cloud::Datastream::V1::AvroFileFormat

**Returns**

  * ([::Google::Cloud::Datastream::V1::AvroFileFormat](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1/latest/Google-Cloud-Datastream-V1-AvroFileFormat)) — AVRO file format configuration.

Note: The following fields are mutually exclusive: `avro_file_format`, `json_file_format`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #avro_file_format=
    
    
    def avro_file_format=(value) -> ::Google::Cloud::Datastream::V1::AvroFileFormat

**Parameter**

  * **value** ([::Google::Cloud::Datastream::V1::AvroFileFormat](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1/latest/Google-Cloud-Datastream-V1-AvroFileFormat)) — AVRO file format configuration.

Note: The following fields are mutually exclusive: `avro_file_format`, `json_file_format`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Datastream::V1::AvroFileFormat](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1/latest/Google-Cloud-Datastream-V1-AvroFileFormat)) — AVRO file format configuration.

Note: The following fields are mutually exclusive: `avro_file_format`, `json_file_format`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #file_rotation_interval
    
    
    def file_rotation_interval() -> ::Google::Protobuf::Duration

**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1/latest/Google-Protobuf-Duration)) — The maximum duration for which new events are added before a file is closed and a new file is created. Values within the range of 15-60 seconds are allowed. 



### #file_rotation_interval=
    
    
    def file_rotation_interval=(value) -> ::Google::Protobuf::Duration

**Parameter**

  * **value** ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1/latest/Google-Protobuf-Duration)) — The maximum duration for which new events are added before a file is closed and a new file is created. Values within the range of 15-60 seconds are allowed. 



**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1/latest/Google-Protobuf-Duration)) — The maximum duration for which new events are added before a file is closed and a new file is created. Values within the range of 15-60 seconds are allowed. 



### #file_rotation_mb
    
    
    def file_rotation_mb() -> ::Integer

**Returns**

  * (::Integer) — The maximum file size to be saved in the bucket. 



### #file_rotation_mb=
    
    
    def file_rotation_mb=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — The maximum file size to be saved in the bucket. 



**Returns**

  * (::Integer) — The maximum file size to be saved in the bucket. 



### #json_file_format
    
    
    def json_file_format() -> ::Google::Cloud::Datastream::V1::JsonFileFormat

**Returns**

  * ([::Google::Cloud::Datastream::V1::JsonFileFormat](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1/latest/Google-Cloud-Datastream-V1-JsonFileFormat)) — JSON file format configuration.

Note: The following fields are mutually exclusive: `json_file_format`, `avro_file_format`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #json_file_format=
    
    
    def json_file_format=(value) -> ::Google::Cloud::Datastream::V1::JsonFileFormat

**Parameter**

  * **value** ([::Google::Cloud::Datastream::V1::JsonFileFormat](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1/latest/Google-Cloud-Datastream-V1-JsonFileFormat)) — JSON file format configuration.

Note: The following fields are mutually exclusive: `json_file_format`, `avro_file_format`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Datastream::V1::JsonFileFormat](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1/latest/Google-Cloud-Datastream-V1-JsonFileFormat)) — JSON file format configuration.

Note: The following fields are mutually exclusive: `json_file_format`, `avro_file_format`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #path
    
    
    def path() -> ::String

**Returns**

  * (::String) — Path inside the Cloud Storage bucket to write data to. 



### #path=
    
    
    def path=(value) -> ::String

**Parameter**

  * **value** (::String) — Path inside the Cloud Storage bucket to write data to. 



**Returns**

  * (::String) — Path inside the Cloud Storage bucket to write data to. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
