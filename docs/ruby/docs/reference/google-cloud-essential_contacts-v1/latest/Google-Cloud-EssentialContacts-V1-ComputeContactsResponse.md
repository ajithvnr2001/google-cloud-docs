---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-essential_contacts-v1/latest/Google-Cloud-EssentialContacts-V1-ComputeContactsResponse/
title: Essential Contacts V1 API - Class Google::Cloud::EssentialContacts::V1::ComputeContactsResponse (v1.7.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:10:36.627347+00:00
---

# Essential Contacts V1 API - Class Google::Cloud::EssentialContacts::V1::ComputeContactsResponse (v1.7.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-essential_contacts-v1/latest/Google-Cloud-EssentialContacts-V1-ComputeContactsResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Essential Contacts V1 API - Class Google::Cloud::EssentialContacts::V1::ComputeContactsResponse (v1.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.7.1 (latest)  1.7.0  1.6.1  1.5.0  1.4.1  1.3.0  1.2.1  1.1.0  1.0.2  0.7.0  0.6.2  0.5.0  0.4.1  0.3.0  0.2.0  0.1.4 

Reference documentation and code samples for the Essential Contacts V1 API class Google::Cloud::EssentialContacts::V1::ComputeContactsResponse.

Response message for the ComputeContacts method.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #contacts
    
    
    def contacts() -> ::Array<::Google::Cloud::EssentialContacts::V1::Contact>

**Returns**

  * (::Array<[::Google::Cloud::EssentialContacts::V1::Contact](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-essential_contacts-v1/latest/Google-Cloud-EssentialContacts-V1-Contact)>) — All contacts for the resource that are subscribed to the specified notification categories, including contacts inherited from any parent resources. 



### #contacts=
    
    
    def contacts=(value) -> ::Array<::Google::Cloud::EssentialContacts::V1::Contact>

**Parameter**

  * **value** (::Array<[::Google::Cloud::EssentialContacts::V1::Contact](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-essential_contacts-v1/latest/Google-Cloud-EssentialContacts-V1-Contact)>) — All contacts for the resource that are subscribed to the specified notification categories, including contacts inherited from any parent resources. 



**Returns**

  * (::Array<[::Google::Cloud::EssentialContacts::V1::Contact](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-essential_contacts-v1/latest/Google-Cloud-EssentialContacts-V1-Contact)>) — All contacts for the resource that are subscribed to the specified notification categories, including contacts inherited from any parent resources. 



### #next_page_token
    
    
    def next_page_token() -> ::String

**Returns**

  * (::String) — If there are more results than those appearing in this response, then `next_page_token` is included. To get the next set of results, call this method again using the value of `next_page_token` as `page_token` and the rest of the parameters the same as the original request. 



### #next_page_token=
    
    
    def next_page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — If there are more results than those appearing in this response, then `next_page_token` is included. To get the next set of results, call this method again using the value of `next_page_token` as `page_token` and the rest of the parameters the same as the original request. 



**Returns**

  * (::String) — If there are more results than those appearing in this response, then `next_page_token` is included. To get the next set of results, call this method again using the value of `next_page_token` as `page_token` and the rest of the parameters the same as the original request. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
