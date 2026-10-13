---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1/latest/Google-Cloud-Datastream-V1-DestinationConfig/
title: Datastream V1 API - Class Google::Cloud::Datastream::V1::DestinationConfig (v1.7.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:22:04.212686+00:00
---

# Datastream V1 API - Class Google::Cloud::Datastream::V1::DestinationConfig (v1.7.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1/latest/Google-Cloud-Datastream-V1-DestinationConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Datastream V1 API - Class Google::Cloud::Datastream::V1::DestinationConfig (v1.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.7.1 (latest)  1.7.0  1.6.0  1.5.1  1.4.0  1.3.0  1.2.1  1.1.1  1.0.0  0.13.0  0.12.0  0.11.0  0.10.1  0.9.2  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Datastream V1 API class Google::Cloud::Datastream::V1::DestinationConfig.

The configuration of the stream destination.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #bigquery_destination_config
    
    
    def bigquery_destination_config() -> ::Google::Cloud::Datastream::V1::BigQueryDestinationConfig

**Returns**

  * ([::Google::Cloud::Datastream::V1::BigQueryDestinationConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1/latest/Google-Cloud-Datastream-V1-BigQueryDestinationConfig)) — BigQuery destination configuration.

Note: The following fields are mutually exclusive: `bigquery_destination_config`, `gcs_destination_config`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #bigquery_destination_config=
    
    
    def bigquery_destination_config=(value) -> ::Google::Cloud::Datastream::V1::BigQueryDestinationConfig

**Parameter**

  * **value** ([::Google::Cloud::Datastream::V1::BigQueryDestinationConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1/latest/Google-Cloud-Datastream-V1-BigQueryDestinationConfig)) — BigQuery destination configuration.

Note: The following fields are mutually exclusive: `bigquery_destination_config`, `gcs_destination_config`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Datastream::V1::BigQueryDestinationConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1/latest/Google-Cloud-Datastream-V1-BigQueryDestinationConfig)) — BigQuery destination configuration.

Note: The following fields are mutually exclusive: `bigquery_destination_config`, `gcs_destination_config`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #destination_connection_profile
    
    
    def destination_connection_profile() -> ::String

**Returns**

  * (::String) — Required. Destination connection profile resource. Format: `projects/{project}/locations/{location}/connectionProfiles/{name}`



### #destination_connection_profile=
    
    
    def destination_connection_profile=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. Destination connection profile resource. Format: `projects/{project}/locations/{location}/connectionProfiles/{name}`



**Returns**

  * (::String) — Required. Destination connection profile resource. Format: `projects/{project}/locations/{location}/connectionProfiles/{name}`



### #gcs_destination_config
    
    
    def gcs_destination_config() -> ::Google::Cloud::Datastream::V1::GcsDestinationConfig

**Returns**

  * ([::Google::Cloud::Datastream::V1::GcsDestinationConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1/latest/Google-Cloud-Datastream-V1-GcsDestinationConfig)) — A configuration for how data should be loaded to Cloud Storage.

Note: The following fields are mutually exclusive: `gcs_destination_config`, `bigquery_destination_config`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #gcs_destination_config=
    
    
    def gcs_destination_config=(value) -> ::Google::Cloud::Datastream::V1::GcsDestinationConfig

**Parameter**

  * **value** ([::Google::Cloud::Datastream::V1::GcsDestinationConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1/latest/Google-Cloud-Datastream-V1-GcsDestinationConfig)) — A configuration for how data should be loaded to Cloud Storage.

Note: The following fields are mutually exclusive: `gcs_destination_config`, `bigquery_destination_config`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Datastream::V1::GcsDestinationConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1/latest/Google-Cloud-Datastream-V1-GcsDestinationConfig)) — A configuration for how data should be loaded to Cloud Storage.

Note: The following fields are mutually exclusive: `gcs_destination_config`, `bigquery_destination_config`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
