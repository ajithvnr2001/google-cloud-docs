---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-ApiConfigHandler/
title: App Engine Admin V1 API - Class Google::Cloud::AppEngine::V1::ApiConfigHandler (v1.8.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:48:09.727977+00:00
---

# App Engine Admin V1 API - Class Google::Cloud::AppEngine::V1::ApiConfigHandler (v1.8.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-ApiConfigHandler/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  App Engine Admin V1 API - Class Google::Cloud::AppEngine::V1::ApiConfigHandler (v1.8.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.2 (latest)  1.8.1  1.7.0  1.6.0  1.5.1  1.4.0  1.3.0  1.2.1  1.1.0  1.0.1  0.10.0  0.9.2  0.8.0  0.7.0  0.6.1  0.5.0  0.4.0  0.3.6 

Reference documentation and code samples for the App Engine Admin V1 API class Google::Cloud::AppEngine::V1::ApiConfigHandler.

[Google Cloud Endpoints](https://cloud.google.com/appengine/docs/python/endpoints/) configuration for API handlers.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #auth_fail_action
    
    
    def auth_fail_action() -> ::Google::Cloud::AppEngine::V1::AuthFailAction

**Returns**

  * ([::Google::Cloud::AppEngine::V1::AuthFailAction](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-AuthFailAction)) — Action to take when users access resources that require authentication. Defaults to `redirect`. 



### #auth_fail_action=
    
    
    def auth_fail_action=(value) -> ::Google::Cloud::AppEngine::V1::AuthFailAction

**Parameter**

  * **value** ([::Google::Cloud::AppEngine::V1::AuthFailAction](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-AuthFailAction)) — Action to take when users access resources that require authentication. Defaults to `redirect`. 



**Returns**

  * ([::Google::Cloud::AppEngine::V1::AuthFailAction](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-AuthFailAction)) — Action to take when users access resources that require authentication. Defaults to `redirect`. 



### #login
    
    
    def login() -> ::Google::Cloud::AppEngine::V1::LoginRequirement

**Returns**

  * ([::Google::Cloud::AppEngine::V1::LoginRequirement](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-LoginRequirement)) — Level of login required to access this resource. Defaults to `optional`. 



### #login=
    
    
    def login=(value) -> ::Google::Cloud::AppEngine::V1::LoginRequirement

**Parameter**

  * **value** ([::Google::Cloud::AppEngine::V1::LoginRequirement](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-LoginRequirement)) — Level of login required to access this resource. Defaults to `optional`. 



**Returns**

  * ([::Google::Cloud::AppEngine::V1::LoginRequirement](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-LoginRequirement)) — Level of login required to access this resource. Defaults to `optional`. 



### #script
    
    
    def script() -> ::String

**Returns**

  * (::String) — Path to the script from the application root directory. 



### #script=
    
    
    def script=(value) -> ::String

**Parameter**

  * **value** (::String) — Path to the script from the application root directory. 



**Returns**

  * (::String) — Path to the script from the application root directory. 



### #security_level
    
    
    def security_level() -> ::Google::Cloud::AppEngine::V1::SecurityLevel

**Returns**

  * ([::Google::Cloud::AppEngine::V1::SecurityLevel](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-SecurityLevel)) — Security (HTTPS) enforcement for this URL. 



### #security_level=
    
    
    def security_level=(value) -> ::Google::Cloud::AppEngine::V1::SecurityLevel

**Parameter**

  * **value** ([::Google::Cloud::AppEngine::V1::SecurityLevel](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-SecurityLevel)) — Security (HTTPS) enforcement for this URL. 



**Returns**

  * ([::Google::Cloud::AppEngine::V1::SecurityLevel](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-SecurityLevel)) — Security (HTTPS) enforcement for this URL. 



### #url
    
    
    def url() -> ::String

**Returns**

  * (::String) — URL to serve the endpoint at. 



### #url=
    
    
    def url=(value) -> ::String

**Parameter**

  * **value** (::String) — URL to serve the endpoint at. 



**Returns**

  * (::String) — URL to serve the endpoint at. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
