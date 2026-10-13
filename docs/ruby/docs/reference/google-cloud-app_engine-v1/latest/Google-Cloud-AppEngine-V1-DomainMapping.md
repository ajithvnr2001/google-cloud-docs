---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-DomainMapping/
title: App Engine Admin V1 API - Class Google::Cloud::AppEngine::V1::DomainMapping (v1.8.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:48:19.723261+00:00
---

# App Engine Admin V1 API - Class Google::Cloud::AppEngine::V1::DomainMapping (v1.8.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-DomainMapping/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  App Engine Admin V1 API - Class Google::Cloud::AppEngine::V1::DomainMapping (v1.8.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.2 (latest)  1.8.1  1.7.0  1.6.0  1.5.1  1.4.0  1.3.0  1.2.1  1.1.0  1.0.1  0.10.0  0.9.2  0.8.0  0.7.0  0.6.1  0.5.0  0.4.0  0.3.6 

Reference documentation and code samples for the App Engine Admin V1 API class Google::Cloud::AppEngine::V1::DomainMapping.

A domain serving an App Engine application.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #id
    
    
    def id() -> ::String

**Returns**

  * (::String) — Relative name of the domain serving the application. Example: `example.com`. 



### #id=
    
    
    def id=(value) -> ::String

**Parameter**

  * **value** (::String) — Relative name of the domain serving the application. Example: `example.com`. 



**Returns**

  * (::String) — Relative name of the domain serving the application. Example: `example.com`. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Full path to the `DomainMapping` resource in the API. Example: `apps/myapp/domainMapping/example.com`. 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Full path to the `DomainMapping` resource in the API. Example: `apps/myapp/domainMapping/example.com`. 



**Returns**

  * (::String) — Full path to the `DomainMapping` resource in the API. Example: `apps/myapp/domainMapping/example.com`. 



### #resource_records
    
    
    def resource_records() -> ::Array<::Google::Cloud::AppEngine::V1::ResourceRecord>

**Returns**

  * (::Array<[::Google::Cloud::AppEngine::V1::ResourceRecord](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-ResourceRecord)>) — The resource records required to configure this domain mapping. These records must be added to the domain's DNS configuration in order to serve the application via this domain mapping. 



### #resource_records=
    
    
    def resource_records=(value) -> ::Array<::Google::Cloud::AppEngine::V1::ResourceRecord>

**Parameter**

  * **value** (::Array<[::Google::Cloud::AppEngine::V1::ResourceRecord](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-ResourceRecord)>) — The resource records required to configure this domain mapping. These records must be added to the domain's DNS configuration in order to serve the application via this domain mapping. 



**Returns**

  * (::Array<[::Google::Cloud::AppEngine::V1::ResourceRecord](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-ResourceRecord)>) — The resource records required to configure this domain mapping. These records must be added to the domain's DNS configuration in order to serve the application via this domain mapping. 



### #ssl_settings
    
    
    def ssl_settings() -> ::Google::Cloud::AppEngine::V1::SslSettings

**Returns**

  * ([::Google::Cloud::AppEngine::V1::SslSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-SslSettings)) — SSL configuration for this domain. If unconfigured, this domain will not serve with SSL. 



### #ssl_settings=
    
    
    def ssl_settings=(value) -> ::Google::Cloud::AppEngine::V1::SslSettings

**Parameter**

  * **value** ([::Google::Cloud::AppEngine::V1::SslSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-SslSettings)) — SSL configuration for this domain. If unconfigured, this domain will not serve with SSL. 



**Returns**

  * ([::Google::Cloud::AppEngine::V1::SslSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-SslSettings)) — SSL configuration for this domain. If unconfigured, this domain will not serve with SSL. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
