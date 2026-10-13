---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-developer_connect-v1/latest/Google-Cloud-DeveloperConnect-V1-GitHubEnterpriseConfig/
title: Developer Connect V1 API - Class Google::Cloud::DeveloperConnect::V1::GitHubEnterpriseConfig (v1.7.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:52:07.057942+00:00
---

# Developer Connect V1 API - Class Google::Cloud::DeveloperConnect::V1::GitHubEnterpriseConfig (v1.7.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-developer_connect-v1/latest/Google-Cloud-DeveloperConnect-V1-GitHubEnterpriseConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Developer Connect V1 API - Class Google::Cloud::DeveloperConnect::V1::GitHubEnterpriseConfig (v1.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.7.1 (latest)  1.7.0  1.6.0  1.5.0  1.4.1  1.3.0  1.2.0  1.1.0  1.0.1  0.5.0  0.4.0  0.3.0  0.2.0  0.1.1 

Reference documentation and code samples for the Developer Connect V1 API class Google::Cloud::DeveloperConnect::V1::GitHubEnterpriseConfig.

Configuration for connections to an instance of GitHub Enterprise.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #app_id
    
    
    def app_id() -> ::Integer

**Returns**

  * (::Integer) — Optional. ID of the GitHub App created from the manifest. 



### #app_id=
    
    
    def app_id=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. ID of the GitHub App created from the manifest. 



**Returns**

  * (::Integer) — Optional. ID of the GitHub App created from the manifest. 



### #app_installation_id
    
    
    def app_installation_id() -> ::Integer

**Returns**

  * (::Integer) — Optional. ID of the installation of the GitHub App. 



### #app_installation_id=
    
    
    def app_installation_id=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. ID of the installation of the GitHub App. 



**Returns**

  * (::Integer) — Optional. ID of the installation of the GitHub App. 



### #app_slug
    
    
    def app_slug() -> ::String

**Returns**

  * (::String) — Output only. The URL-friendly name of the GitHub App. 



### #host_uri
    
    
    def host_uri() -> ::String

**Returns**

  * (::String) — Required. The URI of the GitHub Enterprise host this connection is for. 



### #host_uri=
    
    
    def host_uri=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The URI of the GitHub Enterprise host this connection is for. 



**Returns**

  * (::String) — Required. The URI of the GitHub Enterprise host this connection is for. 



### #installation_uri
    
    
    def installation_uri() -> ::String

**Returns**

  * (::String) — Output only. The URI to navigate to in order to manage the installation associated with this GitHubEnterpriseConfig. 



### #organization
    
    
    def organization() -> ::String

**Returns**

  * (::String) — Optional. Immutable. GitHub Enterprise organization in which the GitHub App is created. 



### #organization=
    
    
    def organization=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Immutable. GitHub Enterprise organization in which the GitHub App is created. 



**Returns**

  * (::String) — Optional. Immutable. GitHub Enterprise organization in which the GitHub App is created. 



### #private_key_secret_version
    
    
    def private_key_secret_version() -> ::String

**Returns**

  * (::String) — Optional. SecretManager resource containing the private key of the GitHub App, formatted as `projects/*/secrets/*/versions/*` or `projects/*/locations/*/secrets/*/versions/*` (if regional secrets are supported in that location). 



### #private_key_secret_version=
    
    
    def private_key_secret_version=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. SecretManager resource containing the private key of the GitHub App, formatted as `projects/*/secrets/*/versions/*` or `projects/*/locations/*/secrets/*/versions/*` (if regional secrets are supported in that location). 



**Returns**

  * (::String) — Optional. SecretManager resource containing the private key of the GitHub App, formatted as `projects/*/secrets/*/versions/*` or `projects/*/locations/*/secrets/*/versions/*` (if regional secrets are supported in that location). 



### #server_version
    
    
    def server_version() -> ::String

**Returns**

  * (::String) — Output only. GitHub Enterprise version installed at the host_uri. 



### #service_directory_config
    
    
    def service_directory_config() -> ::Google::Cloud::DeveloperConnect::V1::ServiceDirectoryConfig

**Returns**

  * ([::Google::Cloud::DeveloperConnect::V1::ServiceDirectoryConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-developer_connect-v1/latest/Google-Cloud-DeveloperConnect-V1-ServiceDirectoryConfig)) — Optional. Configuration for using Service Directory to privately connect to a GitHub Enterprise server. This should only be set if the GitHub Enterprise server is hosted on-premises and not reachable by public internet. If this field is left empty, calls to the GitHub Enterprise server will be made over the public internet. 



### #service_directory_config=
    
    
    def service_directory_config=(value) -> ::Google::Cloud::DeveloperConnect::V1::ServiceDirectoryConfig

**Parameter**

  * **value** ([::Google::Cloud::DeveloperConnect::V1::ServiceDirectoryConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-developer_connect-v1/latest/Google-Cloud-DeveloperConnect-V1-ServiceDirectoryConfig)) — Optional. Configuration for using Service Directory to privately connect to a GitHub Enterprise server. This should only be set if the GitHub Enterprise server is hosted on-premises and not reachable by public internet. If this field is left empty, calls to the GitHub Enterprise server will be made over the public internet. 



**Returns**

  * ([::Google::Cloud::DeveloperConnect::V1::ServiceDirectoryConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-developer_connect-v1/latest/Google-Cloud-DeveloperConnect-V1-ServiceDirectoryConfig)) — Optional. Configuration for using Service Directory to privately connect to a GitHub Enterprise server. This should only be set if the GitHub Enterprise server is hosted on-premises and not reachable by public internet. If this field is left empty, calls to the GitHub Enterprise server will be made over the public internet. 



### #ssl_ca_certificate
    
    
    def ssl_ca_certificate() -> ::String

**Returns**

  * (::String) — Optional. SSL certificate to use for requests to GitHub Enterprise. 



### #ssl_ca_certificate=
    
    
    def ssl_ca_certificate=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. SSL certificate to use for requests to GitHub Enterprise. 



**Returns**

  * (::String) — Optional. SSL certificate to use for requests to GitHub Enterprise. 



### #webhook_secret_secret_version
    
    
    def webhook_secret_secret_version() -> ::String

**Returns**

  * (::String) — Optional. SecretManager resource containing the webhook secret of the GitHub App, formatted as `projects/*/secrets/*/versions/*` or `projects/*/locations/*/secrets/*/versions/*` (if regional secrets are supported in that location). 



### #webhook_secret_secret_version=
    
    
    def webhook_secret_secret_version=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. SecretManager resource containing the webhook secret of the GitHub App, formatted as `projects/*/secrets/*/versions/*` or `projects/*/locations/*/secrets/*/versions/*` (if regional secrets are supported in that location). 



**Returns**

  * (::String) — Optional. SecretManager resource containing the webhook secret of the GitHub App, formatted as `projects/*/secrets/*/versions/*` or `projects/*/locations/*/secrets/*/versions/*` (if regional secrets are supported in that location). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
