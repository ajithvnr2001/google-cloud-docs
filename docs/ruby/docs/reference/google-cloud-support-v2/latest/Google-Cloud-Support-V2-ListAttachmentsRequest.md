---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-support-v2/latest/Google-Cloud-Support-V2-ListAttachmentsRequest/
title: Google Cloud Support V2 API - Class Google::Cloud::Support::V2::ListAttachmentsRequest (v1.11.3) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:02:57.521672+00:00
---

# Google Cloud Support V2 API - Class Google::Cloud::Support::V2::ListAttachmentsRequest (v1.11.3)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-support-v2/latest/Google-Cloud-Support-V2-ListAttachmentsRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Google Cloud Support V2 API - Class Google::Cloud::Support::V2::ListAttachmentsRequest (v1.11.3) Stay organized with collections  Save and categorize content based on your preferences. 

1.11.3 (latest)  1.11.2  1.10.0  1.9.0  1.8.0  1.7.1  1.6.0  1.5.1  1.4.1  1.3.0  1.2.1  1.1.0  1.0.1  0.4.0  0.3.2  0.2.0  0.1.0 

Reference documentation and code samples for the Google Cloud Support V2 API class Google::Cloud::Support::V2::ListAttachmentsRequest.

The request message for the ListAttachments endpoint.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #page_size
    
    
    def page_size() -> ::Integer

**Returns**

  * (::Integer) — The maximum number of attachments fetched with each request.

If not provided, the default is 10. The maximum page size that will be returned is 100.

The size of each page can be smaller than the requested page size and can include zero. For example, you could request 100 attachments on one page, receive 0, and then on the next page, receive 90. 




### #page_size=
    
    
    def page_size=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — The maximum number of attachments fetched with each request.

If not provided, the default is 10. The maximum page size that will be returned is 100.

The size of each page can be smaller than the requested page size and can include zero. For example, you could request 100 attachments on one page, receive 0, and then on the next page, receive 90. 




**Returns**

  * (::Integer) — The maximum number of attachments fetched with each request.

If not provided, the default is 10. The maximum page size that will be returned is 100.

The size of each page can be smaller than the requested page size and can include zero. For example, you could request 100 attachments on one page, receive 0, and then on the next page, receive 90. 




### #page_token
    
    
    def page_token() -> ::String

**Returns**

  * (::String) — A token identifying the page of results to return. If unspecified, the first page is retrieved. 



### #page_token=
    
    
    def page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — A token identifying the page of results to return. If unspecified, the first page is retrieved. 



**Returns**

  * (::String) — A token identifying the page of results to return. If unspecified, the first page is retrieved. 



### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — Required. The name of the case for which attachments should be listed. 



### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The name of the case for which attachments should be listed. 



**Returns**

  * (::String) — Required. The name of the case for which attachments should be listed. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
