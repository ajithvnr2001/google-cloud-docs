---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-data_transfer-v1/latest/Google-Cloud-Bigquery-DataTransfer-V1-CheckValidCredsRequest/
title: BigQuery Data Transfer Service V1 API - Class Google::Cloud::Bigquery::DataTransfer::V1::CheckValidCredsRequest (v1.7.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:37:44.047739+00:00
---

# BigQuery Data Transfer Service V1 API - Class Google::Cloud::Bigquery::DataTransfer::V1::CheckValidCredsRequest (v1.7.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-data_transfer-v1/latest/Google-Cloud-Bigquery-DataTransfer-V1-CheckValidCredsRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  BigQuery Data Transfer Service V1 API - Class Google::Cloud::Bigquery::DataTransfer::V1::CheckValidCredsRequest (v1.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.7.1 (latest)  1.7.0  1.6.0  1.5.1  1.4.1  1.3.1  1.2.0  1.1.0  1.0.3  0.14.2  0.13.1  0.12.2  0.11.0  0.10.0  0.9.0  0.8.0  0.7.1  0.6.1  0.5.1  0.4.6 

Reference documentation and code samples for the BigQuery Data Transfer Service V1 API class Google::Cloud::Bigquery::DataTransfer::V1::CheckValidCredsRequest.

A request to determine whether the user has valid credentials. This method is used to limit the number of OAuth popups in the user interface. The user id is inferred from the API call context. If the data source has the Google+ authorization type, this method returns false, as it cannot be determined whether the credentials are already valid merely based on the user id.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Required. The data source in the form: `projects/{project_id}/dataSources/{data_source_id}` or `projects/{project_id}/locations/{location_id}/dataSources/{data_source_id}`. 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The data source in the form: `projects/{project_id}/dataSources/{data_source_id}` or `projects/{project_id}/locations/{location_id}/dataSources/{data_source_id}`. 



**Returns**

  * (::String) — Required. The data source in the form: `projects/{project_id}/dataSources/{data_source_id}` or `projects/{project_id}/locations/{location_id}/dataSources/{data_source_id}`. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
