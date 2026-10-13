---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-OidcToken/
title: Cloud Tasks V2 API - Class Google::Cloud::Tasks::V2::OidcToken (v1.7.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:25:45.375650+00:00
---

# Cloud Tasks V2 API - Class Google::Cloud::Tasks::V2::OidcToken (v1.7.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-OidcToken/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Tasks V2 API - Class Google::Cloud::Tasks::V2::OidcToken (v1.7.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.7.0 (latest)  1.6.1  1.5.0  1.4.1  1.3.0  1.2.1  1.1.0  1.0.1  0.11.0  0.10.2  0.9.0  0.8.2  0.7.0  0.6.0  0.5.0  0.4.6 

Reference documentation and code samples for the Cloud Tasks V2 API class Google::Cloud::Tasks::V2::OidcToken.

Contains information needed for generating an [OpenID Connect token](https://developers.google.com/identity/protocols/OpenIDConnect). This type of authorization can be used for many scenarios, including calling Cloud Run, or endpoints where you intend to validate the token yourself.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #audience
    
    
    def audience() -> ::String

**Returns**

  * (::String) — Audience to be used when generating OIDC token. If not specified, the URI specified in target will be used. 



### #audience=
    
    
    def audience=(value) -> ::String

**Parameter**

  * **value** (::String) — Audience to be used when generating OIDC token. If not specified, the URI specified in target will be used. 



**Returns**

  * (::String) — Audience to be used when generating OIDC token. If not specified, the URI specified in target will be used. 



### #service_account_email
    
    
    def service_account_email() -> ::String

**Returns**

  * (::String) — [Service account email](https://cloud.google.com/iam/docs/service-accounts) to be used for generating OIDC token. The service account must be within the same project as the queue. The caller must have iam.serviceAccounts.actAs permission for the service account. 



### #service_account_email=
    
    
    def service_account_email=(value) -> ::String

**Parameter**

  * **value** (::String) — [Service account email](https://cloud.google.com/iam/docs/service-accounts) to be used for generating OIDC token. The service account must be within the same project as the queue. The caller must have iam.serviceAccounts.actAs permission for the service account. 



**Returns**

  * (::String) — [Service account email](https://cloud.google.com/iam/docs/service-accounts) to be used for generating OIDC token. The service account must be within the same project as the queue. The caller must have iam.serviceAccounts.actAs permission for the service account. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
