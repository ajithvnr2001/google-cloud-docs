---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v2/latest/Google-Cloud-Build-V2-GitLabConfig/
title: Cloud Build V2 API - Class Google::Cloud::Build::V2::GitLabConfig (v0.14.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:16:17.328750+00:00
---

# Cloud Build V2 API - Class Google::Cloud::Build::V2::GitLabConfig (v0.14.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v2/latest/Google-Cloud-Build-V2-GitLabConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Build V2 API - Class Google::Cloud::Build::V2::GitLabConfig (v0.14.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.14.2 (latest)  0.14.1  0.13.0  0.12.1  0.11.0  0.10.0  0.9.1  0.8.0  0.7.2  0.6.0  0.5.2  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Cloud Build V2 API class Google::Cloud::Build::V2::GitLabConfig.

Configuration for connections to gitlab.com or an instance of GitLab Enterprise.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #authorizer_credential
    
    
    def authorizer_credential() -> ::Google::Cloud::Build::V2::UserCredential

**Returns**

  * ([::Google::Cloud::Build::V2::UserCredential](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v2/latest/Google-Cloud-Build-V2-UserCredential)) — Required. A GitLab personal access token with the `api` scope access. 



### #authorizer_credential=
    
    
    def authorizer_credential=(value) -> ::Google::Cloud::Build::V2::UserCredential

**Parameter**

  * **value** ([::Google::Cloud::Build::V2::UserCredential](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v2/latest/Google-Cloud-Build-V2-UserCredential)) — Required. A GitLab personal access token with the `api` scope access. 



**Returns**

  * ([::Google::Cloud::Build::V2::UserCredential](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v2/latest/Google-Cloud-Build-V2-UserCredential)) — Required. A GitLab personal access token with the `api` scope access. 



### #host_uri
    
    
    def host_uri() -> ::String

**Returns**

  * (::String) — The URI of the GitLab Enterprise host this connection is for. If not specified, the default value is https://gitlab.com. 



### #host_uri=
    
    
    def host_uri=(value) -> ::String

**Parameter**

  * **value** (::String) — The URI of the GitLab Enterprise host this connection is for. If not specified, the default value is https://gitlab.com. 



**Returns**

  * (::String) — The URI of the GitLab Enterprise host this connection is for. If not specified, the default value is https://gitlab.com. 



### #read_authorizer_credential
    
    
    def read_authorizer_credential() -> ::Google::Cloud::Build::V2::UserCredential

**Returns**

  * ([::Google::Cloud::Build::V2::UserCredential](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v2/latest/Google-Cloud-Build-V2-UserCredential)) — Required. A GitLab personal access token with the minimum `read_api` scope access. 



### #read_authorizer_credential=
    
    
    def read_authorizer_credential=(value) -> ::Google::Cloud::Build::V2::UserCredential

**Parameter**

  * **value** ([::Google::Cloud::Build::V2::UserCredential](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v2/latest/Google-Cloud-Build-V2-UserCredential)) — Required. A GitLab personal access token with the minimum `read_api` scope access. 



**Returns**

  * ([::Google::Cloud::Build::V2::UserCredential](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v2/latest/Google-Cloud-Build-V2-UserCredential)) — Required. A GitLab personal access token with the minimum `read_api` scope access. 



### #server_version
    
    
    def server_version() -> ::String

**Returns**

  * (::String) — Output only. Version of the GitLab Enterprise server running on the `host_uri`. 



### #service_directory_config
    
    
    def service_directory_config() -> ::Google::Cloud::Build::V2::ServiceDirectoryConfig

**Returns**

  * ([::Google::Cloud::Build::V2::ServiceDirectoryConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v2/latest/Google-Cloud-Build-V2-ServiceDirectoryConfig)) — Configuration for using Service Directory to privately connect to a GitLab Enterprise server. This should only be set if the GitLab Enterprise server is hosted on-premises and not reachable by public internet. If this field is left empty, calls to the GitLab Enterprise server will be made over the public internet. 



### #service_directory_config=
    
    
    def service_directory_config=(value) -> ::Google::Cloud::Build::V2::ServiceDirectoryConfig

**Parameter**

  * **value** ([::Google::Cloud::Build::V2::ServiceDirectoryConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v2/latest/Google-Cloud-Build-V2-ServiceDirectoryConfig)) — Configuration for using Service Directory to privately connect to a GitLab Enterprise server. This should only be set if the GitLab Enterprise server is hosted on-premises and not reachable by public internet. If this field is left empty, calls to the GitLab Enterprise server will be made over the public internet. 



**Returns**

  * ([::Google::Cloud::Build::V2::ServiceDirectoryConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v2/latest/Google-Cloud-Build-V2-ServiceDirectoryConfig)) — Configuration for using Service Directory to privately connect to a GitLab Enterprise server. This should only be set if the GitLab Enterprise server is hosted on-premises and not reachable by public internet. If this field is left empty, calls to the GitLab Enterprise server will be made over the public internet. 



### #ssl_ca
    
    
    def ssl_ca() -> ::String

**Returns**

  * (::String) — SSL certificate to use for requests to GitLab Enterprise. 



### #ssl_ca=
    
    
    def ssl_ca=(value) -> ::String

**Parameter**

  * **value** (::String) — SSL certificate to use for requests to GitLab Enterprise. 



**Returns**

  * (::String) — SSL certificate to use for requests to GitLab Enterprise. 



### #webhook_secret_secret_version
    
    
    def webhook_secret_secret_version() -> ::String

**Returns**

  * (::String) — Required. Immutable. SecretManager resource containing the webhook secret of a GitLab Enterprise project, formatted as `projects/*/secrets/*/versions/*`. 



### #webhook_secret_secret_version=
    
    
    def webhook_secret_secret_version=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. Immutable. SecretManager resource containing the webhook secret of a GitLab Enterprise project, formatted as `projects/*/secrets/*/versions/*`. 



**Returns**

  * (::String) — Required. Immutable. SecretManager resource containing the webhook secret of a GitLab Enterprise project, formatted as `projects/*/secrets/*/versions/*`. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
