---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CheckCloudIdentityAccountsExistRequest/
title: Cloud Channel V1 API - Class Google::Cloud::Channel::V1::CheckCloudIdentityAccountsExistRequest (v2.6.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:49:08.677656+00:00
---

# Cloud Channel V1 API - Class Google::Cloud::Channel::V1::CheckCloudIdentityAccountsExistRequest (v2.6.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CheckCloudIdentityAccountsExistRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Channel V1 API - Class Google::Cloud::Channel::V1::CheckCloudIdentityAccountsExistRequest (v2.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.6.1 (latest)  2.6.0  2.5.0  2.4.1  2.3.0  2.2.1  2.1.0  2.0.1  1.3.0  1.2.0  1.1.0  1.0.1  0.24.0  0.23.2  0.22.1  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.5 

Reference documentation and code samples for the Cloud Channel V1 API class Google::Cloud::Channel::V1::CheckCloudIdentityAccountsExistRequest.

Request message for [CloudChannelService.CheckCloudIdentityAccountsExist](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CloudChannelService-Client#Google__Cloud__Channel__V1__CloudChannelService__Client_check_cloud_identity_accounts_exist_instance_ "Google::Cloud::Channel::V1::CloudChannelService::Client#check_cloud_identity_accounts_exist \(method\)").

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #domain
    
    
    def domain() -> ::String

**Returns**

  * (::String) — Required. Domain to fetch for Cloud Identity account customers, including domain and team customers. For team customers, please use the domain for their emails. 



### #domain=
    
    
    def domain=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. Domain to fetch for Cloud Identity account customers, including domain and team customers. For team customers, please use the domain for their emails. 



**Returns**

  * (::String) — Required. Domain to fetch for Cloud Identity account customers, including domain and team customers. For team customers, please use the domain for their emails. 



### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — Required. The reseller account's resource name. Parent uses the format: accounts/{account_id} 



### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The reseller account's resource name. Parent uses the format: accounts/{account_id} 



**Returns**

  * (::String) — Required. The reseller account's resource name. Parent uses the format: accounts/{account_id} 



### #primary_admin_email
    
    
    def primary_admin_email() -> ::String

**Returns**

  * (::String) — Optional. Primary admin email to fetch for Cloud Identity account team customer. 



### #primary_admin_email=
    
    
    def primary_admin_email=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Primary admin email to fetch for Cloud Identity account team customer. 



**Returns**

  * (::String) — Optional. Primary admin email to fetch for Cloud Identity account team customer. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
