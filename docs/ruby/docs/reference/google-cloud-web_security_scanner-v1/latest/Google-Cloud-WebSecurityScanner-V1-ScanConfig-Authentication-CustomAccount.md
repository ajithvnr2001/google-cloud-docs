---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-web_security_scanner-v1/latest/Google-Cloud-WebSecurityScanner-V1-ScanConfig-Authentication-CustomAccount/
title: Web Security Scanner V1 API - Class Google::Cloud::WebSecurityScanner::V1::ScanConfig::Authentication::CustomAccount (v1.6.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:33:07.499087+00:00
---

# Web Security Scanner V1 API - Class Google::Cloud::WebSecurityScanner::V1::ScanConfig::Authentication::CustomAccount (v1.6.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-web_security_scanner-v1/latest/Google-Cloud-WebSecurityScanner-V1-ScanConfig-Authentication-CustomAccount/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Web Security Scanner V1 API - Class Google::Cloud::WebSecurityScanner::V1::ScanConfig::Authentication::CustomAccount (v1.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.6.1 (latest)  1.6.0  1.5.1  1.4.1  1.3.0  1.2.1  1.1.0  1.0.1  0.10.0  0.9.2  0.8.0  0.7.1  0.6.0  0.5.0  0.4.1  0.3.5 

Reference documentation and code samples for the Web Security Scanner V1 API class Google::Cloud::WebSecurityScanner::V1::ScanConfig::Authentication::CustomAccount.

Describes authentication configuration that uses a custom account.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #login_url
    
    
    def login_url() -> ::String

**Returns**

  * (::String) — Required. The login form URL of the website. 



### #login_url=
    
    
    def login_url=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The login form URL of the website. 



**Returns**

  * (::String) — Required. The login form URL of the website. 



### #password
    
    
    def password() -> ::String

**Returns**

  * (::String) — Required. Input only. The password of the custom account. The credential is stored encrypted and not returned in any response nor included in audit logs. 



### #password=
    
    
    def password=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. Input only. The password of the custom account. The credential is stored encrypted and not returned in any response nor included in audit logs. 



**Returns**

  * (::String) — Required. Input only. The password of the custom account. The credential is stored encrypted and not returned in any response nor included in audit logs. 



### #username
    
    
    def username() -> ::String

**Returns**

  * (::String) — Required. The user name of the custom account. 



### #username=
    
    
    def username=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The user name of the custom account. 



**Returns**

  * (::String) — Required. The user name of the custom account. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
