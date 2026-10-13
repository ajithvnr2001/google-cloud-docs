---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Api-Publishing/
title: Cloud Channel V1 API - Class Google::Api::Publishing (v2.6.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:49:05.180581+00:00
---

# Cloud Channel V1 API - Class Google::Api::Publishing (v2.6.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Api-Publishing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Channel V1 API - Class Google::Api::Publishing (v2.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.6.1 (latest)  2.6.0  2.5.0  2.4.1  2.3.0  2.2.1  2.1.0  2.0.1  1.3.0  1.2.0  1.1.0  1.0.1  0.24.0  0.23.2  0.22.1  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.5 

Reference documentation and code samples for the Cloud Channel V1 API class Google::Api::Publishing.

This message configures the settings for publishing [Google Cloud Client libraries](https://cloud.google.com/apis/docs/cloud-client-libraries) generated from the service config.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #api_short_name
    
    
    def api_short_name() -> ::String

**Returns**

  * (::String) — Used as a tracking tag when collecting data about the APIs developer relations artifacts like docs, packages delivered to package managers, etc. Example: "speech". 



### #api_short_name=
    
    
    def api_short_name=(value) -> ::String

**Parameter**

  * **value** (::String) — Used as a tracking tag when collecting data about the APIs developer relations artifacts like docs, packages delivered to package managers, etc. Example: "speech". 



**Returns**

  * (::String) — Used as a tracking tag when collecting data about the APIs developer relations artifacts like docs, packages delivered to package managers, etc. Example: "speech". 



### #codeowner_github_teams
    
    
    def codeowner_github_teams() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — GitHub teams to be added to CODEOWNERS in the directory in GitHub containing source code for the client libraries for this API. 



### #codeowner_github_teams=
    
    
    def codeowner_github_teams=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — GitHub teams to be added to CODEOWNERS in the directory in GitHub containing source code for the client libraries for this API. 



**Returns**

  * (::Array<::String>) — GitHub teams to be added to CODEOWNERS in the directory in GitHub containing source code for the client libraries for this API. 



### #doc_tag_prefix
    
    
    def doc_tag_prefix() -> ::String

**Returns**

  * (::String) — A prefix used in sample code when demarking regions to be included in documentation. 



### #doc_tag_prefix=
    
    
    def doc_tag_prefix=(value) -> ::String

**Parameter**

  * **value** (::String) — A prefix used in sample code when demarking regions to be included in documentation. 



**Returns**

  * (::String) — A prefix used in sample code when demarking regions to be included in documentation. 



### #documentation_uri
    
    
    def documentation_uri() -> ::String

**Returns**

  * (::String) — Link to product home page. Example: https://cloud.google.com/asset-inventory/docs/overview 



### #documentation_uri=
    
    
    def documentation_uri=(value) -> ::String

**Parameter**

  * **value** (::String) — Link to product home page. Example: https://cloud.google.com/asset-inventory/docs/overview 



**Returns**

  * (::String) — Link to product home page. Example: https://cloud.google.com/asset-inventory/docs/overview 



### #github_label
    
    
    def github_label() -> ::String

**Returns**

  * (::String) — GitHub label to apply to issues and pull requests opened for this API. 



### #github_label=
    
    
    def github_label=(value) -> ::String

**Parameter**

  * **value** (::String) — GitHub label to apply to issues and pull requests opened for this API. 



**Returns**

  * (::String) — GitHub label to apply to issues and pull requests opened for this API. 



### #library_settings
    
    
    def library_settings() -> ::Array<::Google::Api::ClientLibrarySettings>

**Returns**

  * (::Array<[::Google::Api::ClientLibrarySettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Api-ClientLibrarySettings)>) — Client library settings. If the same version string appears multiple times in this list, then the last one wins. Settings from earlier settings with the same version string are discarded. 



### #library_settings=
    
    
    def library_settings=(value) -> ::Array<::Google::Api::ClientLibrarySettings>

**Parameter**

  * **value** (::Array<[::Google::Api::ClientLibrarySettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Api-ClientLibrarySettings)>) — Client library settings. If the same version string appears multiple times in this list, then the last one wins. Settings from earlier settings with the same version string are discarded. 



**Returns**

  * (::Array<[::Google::Api::ClientLibrarySettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Api-ClientLibrarySettings)>) — Client library settings. If the same version string appears multiple times in this list, then the last one wins. Settings from earlier settings with the same version string are discarded. 



### #method_settings
    
    
    def method_settings() -> ::Array<::Google::Api::MethodSettings>

**Returns**

  * (::Array<[::Google::Api::MethodSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Api-MethodSettings)>) — A list of API method settings, e.g. the behavior for methods that use the long-running operation pattern. 



### #method_settings=
    
    
    def method_settings=(value) -> ::Array<::Google::Api::MethodSettings>

**Parameter**

  * **value** (::Array<[::Google::Api::MethodSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Api-MethodSettings)>) — A list of API method settings, e.g. the behavior for methods that use the long-running operation pattern. 



**Returns**

  * (::Array<[::Google::Api::MethodSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Api-MethodSettings)>) — A list of API method settings, e.g. the behavior for methods that use the long-running operation pattern. 



### #new_issue_uri
    
    
    def new_issue_uri() -> ::String

**Returns**

  * (::String) — Link to a _public_ URI where users can report issues. Example: https://issuetracker.google.com/issues/new?component=190865&template=1161103 



### #new_issue_uri=
    
    
    def new_issue_uri=(value) -> ::String

**Parameter**

  * **value** (::String) — Link to a _public_ URI where users can report issues. Example: https://issuetracker.google.com/issues/new?component=190865&template=1161103 



**Returns**

  * (::String) — Link to a _public_ URI where users can report issues. Example: https://issuetracker.google.com/issues/new?component=190865&template=1161103 



### #organization
    
    
    def organization() -> ::Google::Api::ClientLibraryOrganization

**Returns**

  * ([::Google::Api::ClientLibraryOrganization](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Api-ClientLibraryOrganization)) — For whom the client library is being published. 



### #organization=
    
    
    def organization=(value) -> ::Google::Api::ClientLibraryOrganization

**Parameter**

  * **value** ([::Google::Api::ClientLibraryOrganization](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Api-ClientLibraryOrganization)) — For whom the client library is being published. 



**Returns**

  * ([::Google::Api::ClientLibraryOrganization](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Api-ClientLibraryOrganization)) — For whom the client library is being published. 



### #proto_reference_documentation_uri
    
    
    def proto_reference_documentation_uri() -> ::String

**Returns**

  * (::String) — Optional link to proto reference documentation. Example: https://cloud.google.com/pubsub/lite/docs/reference/rpc 



### #proto_reference_documentation_uri=
    
    
    def proto_reference_documentation_uri=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional link to proto reference documentation. Example: https://cloud.google.com/pubsub/lite/docs/reference/rpc 



**Returns**

  * (::String) — Optional link to proto reference documentation. Example: https://cloud.google.com/pubsub/lite/docs/reference/rpc 



### #rest_reference_documentation_uri
    
    
    def rest_reference_documentation_uri() -> ::String

**Returns**

  * (::String) — Optional link to REST reference documentation. Example: https://cloud.google.com/pubsub/lite/docs/reference/rest 



### #rest_reference_documentation_uri=
    
    
    def rest_reference_documentation_uri=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional link to REST reference documentation. Example: https://cloud.google.com/pubsub/lite/docs/reference/rest 



**Returns**

  * (::String) — Optional link to REST reference documentation. Example: https://cloud.google.com/pubsub/lite/docs/reference/rest 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
