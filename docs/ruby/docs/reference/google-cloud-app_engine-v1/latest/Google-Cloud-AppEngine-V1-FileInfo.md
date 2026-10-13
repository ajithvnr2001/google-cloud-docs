---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-FileInfo/
title: App Engine Admin V1 API - Class Google::Cloud::AppEngine::V1::FileInfo (v1.8.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:48:23.243567+00:00
---

# App Engine Admin V1 API - Class Google::Cloud::AppEngine::V1::FileInfo (v1.8.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-FileInfo/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  App Engine Admin V1 API - Class Google::Cloud::AppEngine::V1::FileInfo (v1.8.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.2 (latest)  1.8.1  1.7.0  1.6.0  1.5.1  1.4.0  1.3.0  1.2.1  1.1.0  1.0.1  0.10.0  0.9.2  0.8.0  0.7.0  0.6.1  0.5.0  0.4.0  0.3.6 

Reference documentation and code samples for the App Engine Admin V1 API class Google::Cloud::AppEngine::V1::FileInfo.

Single source file that is part of the version to be deployed. Each source file that is deployed must be specified separately.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #mime_type
    
    
    def mime_type() -> ::String

**Returns**

  * (::String) — The MIME type of the file.

Defaults to the value from Google Cloud Storage. 




### #mime_type=
    
    
    def mime_type=(value) -> ::String

**Parameter**

  * **value** (::String) — The MIME type of the file.

Defaults to the value from Google Cloud Storage. 




**Returns**

  * (::String) — The MIME type of the file.

Defaults to the value from Google Cloud Storage. 




### #sha1_sum
    
    
    def sha1_sum() -> ::String

**Returns**

  * (::String) — The SHA1 hash of the file, in hex. 



### #sha1_sum=
    
    
    def sha1_sum=(value) -> ::String

**Parameter**

  * **value** (::String) — The SHA1 hash of the file, in hex. 



**Returns**

  * (::String) — The SHA1 hash of the file, in hex. 



### #source_url
    
    
    def source_url() -> ::String

**Returns**

  * (::String) — URL source to use to fetch this file. Must be a URL to a resource in Google Cloud Storage in the form 'http(s)://storage.googleapis.com/<bucket>/<object>'. 



### #source_url=
    
    
    def source_url=(value) -> ::String

**Parameter**

  * **value** (::String) — URL source to use to fetch this file. Must be a URL to a resource in Google Cloud Storage in the form 'http(s)://storage.googleapis.com/<bucket>/<object>'. 



**Returns**

  * (::String) — URL source to use to fetch this file. Must be a URL to a resource in Google Cloud Storage in the form 'http(s)://storage.googleapis.com/<bucket>/<object>'. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
