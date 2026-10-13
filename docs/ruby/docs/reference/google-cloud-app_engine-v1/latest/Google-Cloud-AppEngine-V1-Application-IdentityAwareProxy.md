---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-Application-IdentityAwareProxy/
title: App Engine Admin V1 API - Class Google::Cloud::AppEngine::V1::Application::IdentityAwareProxy (v1.8.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:48:10.418384+00:00
---

# App Engine Admin V1 API - Class Google::Cloud::AppEngine::V1::Application::IdentityAwareProxy (v1.8.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-Application-IdentityAwareProxy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  App Engine Admin V1 API - Class Google::Cloud::AppEngine::V1::Application::IdentityAwareProxy (v1.8.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.2 (latest)  1.8.1  1.7.0  1.6.0  1.5.1  1.4.0  1.3.0  1.2.1  1.1.0  1.0.1  0.10.0  0.9.2  0.8.0  0.7.0  0.6.1  0.5.0  0.4.0  0.3.6 

Reference documentation and code samples for the App Engine Admin V1 API class Google::Cloud::AppEngine::V1::Application::IdentityAwareProxy.

Identity-Aware Proxy

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #enabled
    
    
    def enabled() -> ::Boolean

**Returns**

  * (::Boolean) — Whether the serving infrastructure will authenticate and authorize all incoming requests.

If true, the `oauth2_client_id` and `oauth2_client_secret` fields must be non-empty. 




### #enabled=
    
    
    def enabled=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Whether the serving infrastructure will authenticate and authorize all incoming requests.

If true, the `oauth2_client_id` and `oauth2_client_secret` fields must be non-empty. 




**Returns**

  * (::Boolean) — Whether the serving infrastructure will authenticate and authorize all incoming requests.

If true, the `oauth2_client_id` and `oauth2_client_secret` fields must be non-empty. 




### #oauth2_client_id
    
    
    def oauth2_client_id() -> ::String

**Returns**

  * (::String) — OAuth2 client ID to use for the authentication flow. 



### #oauth2_client_id=
    
    
    def oauth2_client_id=(value) -> ::String

**Parameter**

  * **value** (::String) — OAuth2 client ID to use for the authentication flow. 



**Returns**

  * (::String) — OAuth2 client ID to use for the authentication flow. 



### #oauth2_client_secret
    
    
    def oauth2_client_secret() -> ::String

**Returns**

  * (::String) — OAuth2 client secret to use for the authentication flow.

For security reasons, this value cannot be retrieved via the API. Instead, the SHA-256 hash of the value is returned in the `oauth2_client_secret_sha256` field. 




### #oauth2_client_secret=
    
    
    def oauth2_client_secret=(value) -> ::String

**Parameter**

  * **value** (::String) — OAuth2 client secret to use for the authentication flow.

For security reasons, this value cannot be retrieved via the API. Instead, the SHA-256 hash of the value is returned in the `oauth2_client_secret_sha256` field. 




**Returns**

  * (::String) — OAuth2 client secret to use for the authentication flow.

For security reasons, this value cannot be retrieved via the API. Instead, the SHA-256 hash of the value is returned in the `oauth2_client_secret_sha256` field. 




### #oauth2_client_secret_sha256
    
    
    def oauth2_client_secret_sha256() -> ::String

**Returns**

  * (::String) — Hex-encoded SHA-256 hash of the client secret. 



### #oauth2_client_secret_sha256=
    
    
    def oauth2_client_secret_sha256=(value) -> ::String

**Parameter**

  * **value** (::String) — Hex-encoded SHA-256 hash of the client secret. 



**Returns**

  * (::String) — Hex-encoded SHA-256 hash of the client secret. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
