---
url: https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-ResumableUpload-BadResponseError/
title: gapic-common - Class Gapic::Rest::ResumableUpload::BadResponseError (v1.5.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:47:14.068561+00:00
---

# gapic-common - Class Gapic::Rest::ResumableUpload::BadResponseError (v1.5.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-ResumableUpload-BadResponseError/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  gapic-common - Class Gapic::Rest::ResumableUpload::BadResponseError (v1.5.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.5.1 (latest)  1.5.0  1.4.1  1.3.0  1.2.0  1.1.0  1.0.1  0.26.0  0.25.0  0.24.0 

Reference documentation and code samples for the gapic-common class Gapic::Rest::ResumableUpload::BadResponseError.

Raised when an unrecoverable HTTP response is received.

## Inherits

  * [Gapic::Rest::Error](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-Error)



## Includes

  * [Gapic::Rest::ResumableUpload::HasResumeHandle](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-ResumableUpload-HasResumeHandle)



## Methods 

### #initialize
    
    
    def initialize(message = nil, status_code = nil, status: nil, details: nil, headers: nil, response_body: nil, resume_handle: nil) -> BadResponseError

Initializes a new BadResponseError.

**Parameters**

  * **message** (String, nil) — Error message 
  * **status_code** (Integer, nil) — HTTP status code 
  * **status** (String, nil) _(defaults to: nil)_ — Status description 
  * **details** (Object, nil) _(defaults to: nil)_ — Error details 
  * **headers** (Object, nil) _(defaults to: nil)_ — Response headers 
  * **response_body** (String, nil) _(defaults to: nil)_ — Response body 
  * **resume_handle** (Gapic::Rest::ResumableUpload::ResumeHandle, nil) _(defaults to: nil)_ — Associated resume handle 



**Returns**

  * ([BadResponseError](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-ResumableUpload-BadResponseError)) — a new instance of BadResponseError 



### #response_body
    
    
    def response_body() -> String, nil

**Returns**

  * (String, nil) — Response body from backend 



### #resume_handle
    
    
    def resume_handle() -> Gapic::Rest::ResumableUpload::ResumeHandle, nil

**Returns**

  * (Gapic::Rest::ResumableUpload::ResumeHandle, nil) — Associated resume handle 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
