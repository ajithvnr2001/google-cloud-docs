---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-CreateLakeRequest/
title: Dataplex V1 API - Class Google::Cloud::Dataplex::V1::CreateLakeRequest (v2.10.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:53:16.231883+00:00
---

# Dataplex V1 API - Class Google::Cloud::Dataplex::V1::CreateLakeRequest (v2.10.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-CreateLakeRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Dataplex V1 API - Class Google::Cloud::Dataplex::V1::CreateLakeRequest (v2.10.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.10.1 (latest)  2.10.0  2.9.0  2.8.1  2.7.0  2.6.1  2.5.0  2.4.1  2.3.1  2.2.0  2.1.0  2.0.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.1  0.23.0  0.22.0  0.21.1  0.20.0  0.19.0  0.18.2  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.1  0.9.0  0.8.0  0.7.0  0.6.1  0.5.1  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Dataplex V1 API class Google::Cloud::Dataplex::V1::CreateLakeRequest.

Create lake request.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #lake
    
    
    def lake() -> ::Google::Cloud::Dataplex::V1::Lake

**Returns**

  * ([::Google::Cloud::Dataplex::V1::Lake](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-Lake)) — Required. Lake resource 



### #lake=
    
    
    def lake=(value) -> ::Google::Cloud::Dataplex::V1::Lake

**Parameter**

  * **value** ([::Google::Cloud::Dataplex::V1::Lake](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-Lake)) — Required. Lake resource 



**Returns**

  * ([::Google::Cloud::Dataplex::V1::Lake](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-Lake)) — Required. Lake resource 



### #lake_id
    
    
    def lake_id() -> ::String

**Returns**

  * (::String) — 

Required. Lake identifier. This ID will be used to generate names such as database and dataset names when publishing metadata to Hive Metastore and BigQuery.

    * Must contain only lowercase letters, numbers and hyphens.
    * Must start with a letter.
    * Must end with a number or a letter.
    * Must be between 1-63 characters.
    * Must be unique within the customer project / location.



### #lake_id=
    
    
    def lake_id=(value) -> ::String

**Parameter**

  * **value** (::String) — 

Required. Lake identifier. This ID will be used to generate names such as database and dataset names when publishing metadata to Hive Metastore and BigQuery.

    * Must contain only lowercase letters, numbers and hyphens.
    * Must start with a letter.
    * Must end with a number or a letter.
    * Must be between 1-63 characters.
    * Must be unique within the customer project / location.



**Returns**

  * (::String) — 

Required. Lake identifier. This ID will be used to generate names such as database and dataset names when publishing metadata to Hive Metastore and BigQuery.

    * Must contain only lowercase letters, numbers and hyphens.
    * Must start with a letter.
    * Must end with a number or a letter.
    * Must be between 1-63 characters.
    * Must be unique within the customer project / location.



### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — Required. The resource name of the lake location, of the form: projects/{project_number}/locations/{location_id} where `location_id` refers to a Google Cloud region. 



### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The resource name of the lake location, of the form: projects/{project_number}/locations/{location_id} where `location_id` refers to a Google Cloud region. 



**Returns**

  * (::String) — Required. The resource name of the lake location, of the form: projects/{project_number}/locations/{location_id} where `location_id` refers to a Google Cloud region. 



### #validate_only
    
    
    def validate_only() -> ::Boolean

**Returns**

  * (::Boolean) — Optional. Only validate the request, but do not perform mutations. The default is false. 



### #validate_only=
    
    
    def validate_only=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Optional. Only validate the request, but do not perform mutations. The default is false. 



**Returns**

  * (::Boolean) — Optional. Only validate the request, but do not perform mutations. The default is false. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
