---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-ListEntityTypesResponse/
title: Dialogflow V2 API - Class Google::Cloud::Dialogflow::V2::ListEntityTypesResponse (v1.18.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:29:02.337005+00:00
---

# Dialogflow V2 API - Class Google::Cloud::Dialogflow::V2::ListEntityTypesResponse (v1.18.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-ListEntityTypesResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Dialogflow V2 API - Class Google::Cloud::Dialogflow::V2::ListEntityTypesResponse (v1.18.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.18.0 (latest)  1.17.1  1.16.1  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.10.1  1.9.1  1.8.0  1.7.0  1.6.0  1.5.0  1.4.1  1.3.0  1.2.0  1.1.1  1.0.0  0.34.0  0.33.0  0.32.2  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.2  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.1  0.16.0  0.15.2  0.14.0  0.13.0  0.12.0 

Reference documentation and code samples for the Dialogflow V2 API class Google::Cloud::Dialogflow::V2::ListEntityTypesResponse.

The response message for [EntityTypes.ListEntityTypes](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-EntityTypes-Client#Google__Cloud__Dialogflow__V2__EntityTypes__Client_list_entity_types_instance_ "Google::Cloud::Dialogflow::V2::EntityTypes::Client#list_entity_types \(method\)").

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #entity_types
    
    
    def entity_types() -> ::Array<::Google::Cloud::Dialogflow::V2::EntityType>

**Returns**

  * (::Array<[::Google::Cloud::Dialogflow::V2::EntityType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-EntityType)>) — The list of agent entity types. There will be a maximum number of items returned based on the page_size field in the request. 



### #entity_types=
    
    
    def entity_types=(value) -> ::Array<::Google::Cloud::Dialogflow::V2::EntityType>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Dialogflow::V2::EntityType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-EntityType)>) — The list of agent entity types. There will be a maximum number of items returned based on the page_size field in the request. 



**Returns**

  * (::Array<[::Google::Cloud::Dialogflow::V2::EntityType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-EntityType)>) — The list of agent entity types. There will be a maximum number of items returned based on the page_size field in the request. 



### #next_page_token
    
    
    def next_page_token() -> ::String

**Returns**

  * (::String) — Token to retrieve the next page of results, or empty if there are no more results in the list. 



### #next_page_token=
    
    
    def next_page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — Token to retrieve the next page of results, or empty if there are no more results in the list. 



**Returns**

  * (::String) — Token to retrieve the next page of results, or empty if there are no more results in the list. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
