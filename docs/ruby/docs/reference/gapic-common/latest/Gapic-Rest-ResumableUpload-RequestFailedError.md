---
url: https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-ResumableUpload-RequestFailedError/
title: gapic-common - Class Gapic::Rest::ResumableUpload::RequestFailedError (v1.5.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:47:13.990012+00:00
---

# gapic-common - Class Gapic::Rest::ResumableUpload::RequestFailedError (v1.5.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-ResumableUpload-RequestFailedError/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  gapic-common - Class Gapic::Rest::ResumableUpload::RequestFailedError (v1.5.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.5.1 (latest)  1.5.0  1.4.1  1.3.0  1.2.0  1.1.0  1.0.1  0.26.0  0.25.0  0.24.0 

Reference documentation and code samples for the gapic-common class Gapic::Rest::ResumableUpload::RequestFailedError.

Raised when an HTTP request fails (e.g. transport connection failure, request timeout, or retries exhausted).

## Inherits

  * [Gapic::Common::Error](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Common-Error)



## Includes

  * [Gapic::Rest::ResumableUpload::HasResumeHandle](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-ResumableUpload-HasResumeHandle)



## Methods 

### #cause
    
    
    def cause() -> StandardError, nil

Returns the underlying cause exception.

**Returns**

  * (StandardError, nil) 



### #details
    
    
    def details() -> Object, nil

**Returns**

  * (Object, nil) 



### #headers
    
    
    def headers() -> Object, nil

**Returns**

  * (Object, nil) 



### #initialize
    
    
    def initialize(message = nil, cause: nil, resume_handle: nil, status_code: nil, status: nil, details: nil, headers: nil) -> RequestFailedError

Initializes a new RequestFailedError.

**Parameters**

  * **message** (String, nil) — Error message 
  * **cause** (StandardError, nil) _(defaults to: nil)_ — Underlying cause exception 
  * **resume_handle** (Gapic::Rest::ResumableUpload::ResumeHandle, nil) _(defaults to: nil)_ — Associated resume handle 
  * **status_code** (Integer, nil) _(defaults to: nil)_ — HTTP status code 
  * **status** (String, nil) _(defaults to: nil)_ — Status description 
  * **details** (Object, nil) _(defaults to: nil)_ — Error details 
  * **headers** (Object, nil) _(defaults to: nil)_ — Response headers 



**Returns**

  * ([RequestFailedError](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-ResumableUpload-RequestFailedError)) — a new instance of RequestFailedError 



### #resume_handle
    
    
    def resume_handle() -> Gapic::Rest::ResumableUpload::ResumeHandle, nil

**Returns**

  * (Gapic::Rest::ResumableUpload::ResumeHandle, nil) — Associated resume handle 



### #status
    
    
    def status() -> String, nil

**Returns**

  * (String, nil) 



### #status_code
    
    
    def status_code() -> Integer, nil

**Returns**

  * (Integer, nil) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
