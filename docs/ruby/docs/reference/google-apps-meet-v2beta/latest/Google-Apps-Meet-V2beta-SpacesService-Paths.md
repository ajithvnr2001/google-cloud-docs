---
url: https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-SpacesService-Paths/
title: Google Meet V2BETA API - Module Google::Apps::Meet::V2beta::SpacesService::Paths (v0.12.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:46:31.908282+00:00
---

# Google Meet V2BETA API - Module Google::Apps::Meet::V2beta::SpacesService::Paths (v0.12.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-SpacesService-Paths/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Google Meet V2BETA API - Module Google::Apps::Meet::V2beta::SpacesService::Paths (v0.12.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.12.0 (latest)  0.11.1  0.10.0  0.9.0  0.8.1  0.7.0  0.6.1  0.5.0  0.4.0  0.3.2  0.2.2  0.1.0 

Reference documentation and code samples for the Google Meet V2BETA API module Google::Apps::Meet::V2beta::SpacesService::Paths.

Path helper methods for the SpacesService API.

## Extended By

  * [Google::Apps::Meet::V2beta::SpacesService::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-SpacesService-Paths)



## Included In

  * [Google::Apps::Meet::V2beta::SpacesService::Client](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-SpacesService-Client)
  * [Google::Apps::Meet::V2beta::SpacesService::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-SpacesService-Paths)
  * [Google::Apps::Meet::V2beta::SpacesService::Rest::Client](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-SpacesService-Rest-Client)



## Methods 

### #conference_record_path
    
    
    def conference_record_path(conference_record:) -> ::String

Create a fully-qualified ConferenceRecord resource string.

The resource will be in the following format:

`conferenceRecords/{conference_record}`

**Parameter**

  * **conference_record** (String) 



**Returns**

  * (::String) 



### #member_path
    
    
    def member_path(space:, member:) -> ::String

Create a fully-qualified Member resource string.

The resource will be in the following format:

`spaces/{space}/members/{member}`

**Parameters**

  * **space** (String) 
  * **member** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #space_path
    
    
    def space_path(space:) -> ::String

Create a fully-qualified Space resource string.

The resource will be in the following format:

`spaces/{space}`

**Parameter**

  * **space** (String) 



**Returns**

  * (::String) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
