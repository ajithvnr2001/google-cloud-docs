---
url: https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-Error/
title: gapic-common - Class Gapic::Rest::Error (v1.5.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:47:12.816106+00:00
---

# gapic-common - Class Gapic::Rest::Error (v1.5.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-Error/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  gapic-common - Class Gapic::Rest::Error (v1.5.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.5.1 (latest)  1.5.0  1.4.1  1.3.0  1.2.0  1.1.0  1.0.1  0.26.0  0.25.0  0.24.0 

Reference documentation and code samples for the gapic-common class Gapic::Rest::Error.

Gapic REST exception class

## Inherits

  * [Gapic::Common::Error](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Common-Error)



## Methods 

### .wrap_faraday_error
    
    
    def self.wrap_faraday_error(err) -> Gapic::Rest::Error

This creates a new error message wrapping the Faraday's one. Additionally it tries to parse and set a detailed message and an error code from from the Google Cloud's response body

**Parameter**

  * **err** (Faraday::Error) — the Faraday error to wrap 



**Returns**

  * ([Gapic::Rest::Error](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-Error)) 



### #details
    
    
    def details() -> Object, nil

**Aliases**

  * [#status_details](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-Error#Gapic__Rest__Error_status_details_instance_)



**Returns**

  * (Object, nil) — the details as parsed from the response body 



### #header
    
    
    def header() -> Object, nil

**Alias Of** : [#headers](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-Error#Gapic__Rest__Error_headers_instance_)

The Cloud error wrapper expect to see a `header` property

**Returns**

  * (Object, nil) — the headers of the REST error 



### #headers
    
    
    def headers() -> Object, nil

**Aliases**

  * [#header](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-Error#Gapic__Rest__Error_header_instance_)



**Returns**

  * (Object, nil) — the headers of the REST error 



### #initialize
    
    
    def initialize(message, status_code, status: nil, details: nil, headers: nil) -> Error

**Parameters**

  * **message** (String, nil) — error message 
  * **status_code** (Integer, nil) — HTTP status code of this error 
  * **status** (String, nil) _(defaults to: nil)_ — The text representation of status as parsed from the response body 
  * **details** (Object, nil) _(defaults to: nil)_ — Details data of this error 
  * **headers** (Object, nil) _(defaults to: nil)_ — Http headers data of this error 



**Returns**

  * ([Error](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-Error)) — a new instance of Error 



### #status
    
    
    def status() -> Object, nil

**Returns**

  * (Object, nil) — the text representation of status as parsed from the response body 



### #status_code
    
    
    def status_code() -> Integer, nil

**Returns**

  * (Integer, nil) — the http status code for the error 



### #status_details
    
    
    def status_details() -> Object, nil

**Alias Of** : [#details](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-Error#Gapic__Rest__Error_details_instance_)

The Cloud error wrapper expect to see a `status_details` property

**Returns**

  * (Object, nil) — the details as parsed from the response body 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
