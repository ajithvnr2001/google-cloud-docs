---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Api-DotnetSettings/
title: Dataflow V1beta3 API - Class Google::Api::DotnetSettings (v0.17.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:51:53.642032+00:00
---

# Dataflow V1beta3 API - Class Google::Api::DotnetSettings (v0.17.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Api-DotnetSettings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Dataflow V1beta3 API - Class Google::Api::DotnetSettings (v0.17.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.17.1 (latest)  0.17.0  0.16.0  0.15.0  0.14.1  0.13.1  0.12.1  0.11.0  0.10.0  0.9.1  0.8.2  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.4 

Reference documentation and code samples for the Dataflow V1beta3 API class Google::Api::DotnetSettings.

Settings for Dotnet client libraries.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #common
    
    
    def common() -> ::Google::Api::CommonLanguageSettings

**Returns**

  * ([::Google::Api::CommonLanguageSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Api-CommonLanguageSettings)) — Some settings. 



### #common=
    
    
    def common=(value) -> ::Google::Api::CommonLanguageSettings

**Parameter**

  * **value** ([::Google::Api::CommonLanguageSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Api-CommonLanguageSettings)) — Some settings. 



**Returns**

  * ([::Google::Api::CommonLanguageSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Api-CommonLanguageSettings)) — Some settings. 



### #forced_namespace_aliases
    
    
    def forced_namespace_aliases() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Namespaces which must be aliased in snippets due to a known (but non-generator-predictable) naming collision 



### #forced_namespace_aliases=
    
    
    def forced_namespace_aliases=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Namespaces which must be aliased in snippets due to a known (but non-generator-predictable) naming collision 



**Returns**

  * (::Array<::String>) — Namespaces which must be aliased in snippets due to a known (but non-generator-predictable) naming collision 



### #handwritten_signatures
    
    
    def handwritten_signatures() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Method signatures (in the form "service.method(signature)") which are provided separately, so shouldn't be generated. Snippets _calling_ these methods are still generated, however. 



### #handwritten_signatures=
    
    
    def handwritten_signatures=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Method signatures (in the form "service.method(signature)") which are provided separately, so shouldn't be generated. Snippets _calling_ these methods are still generated, however. 



**Returns**

  * (::Array<::String>) — Method signatures (in the form "service.method(signature)") which are provided separately, so shouldn't be generated. Snippets _calling_ these methods are still generated, however. 



### #ignored_resources
    
    
    def ignored_resources() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — List of full resource types to ignore during generation. This is typically used for API-specific Location resources, which should be handled by the generator as if they were actually the common Location resources. Example entry: "documentai.googleapis.com/Location" 



### #ignored_resources=
    
    
    def ignored_resources=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — List of full resource types to ignore during generation. This is typically used for API-specific Location resources, which should be handled by the generator as if they were actually the common Location resources. Example entry: "documentai.googleapis.com/Location" 



**Returns**

  * (::Array<::String>) — List of full resource types to ignore during generation. This is typically used for API-specific Location resources, which should be handled by the generator as if they were actually the common Location resources. Example entry: "documentai.googleapis.com/Location" 



### #renamed_resources
    
    
    def renamed_resources() -> ::Google::Protobuf::Map{::String => ::String}

**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Map from full resource types to the effective short name for the resource. This is used when otherwise resource named from different services would cause naming collisions. Example entry: "datalabeling.googleapis.com/Dataset": "DataLabelingDataset" 



### #renamed_resources=
    
    
    def renamed_resources=(value) -> ::Google::Protobuf::Map{::String => ::String}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::String}) — Map from full resource types to the effective short name for the resource. This is used when otherwise resource named from different services would cause naming collisions. Example entry: "datalabeling.googleapis.com/Dataset": "DataLabelingDataset" 



**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Map from full resource types to the effective short name for the resource. This is used when otherwise resource named from different services would cause naming collisions. Example entry: "datalabeling.googleapis.com/Dataset": "DataLabelingDataset" 



### #renamed_services
    
    
    def renamed_services() -> ::Google::Protobuf::Map{::String => ::String}

**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Map from original service names to renamed versions. This is used when the default generated types would cause a naming conflict. (Neither name is fully-qualified.) Example: Subscriber to SubscriberServiceApi. 



### #renamed_services=
    
    
    def renamed_services=(value) -> ::Google::Protobuf::Map{::String => ::String}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::String}) — Map from original service names to renamed versions. This is used when the default generated types would cause a naming conflict. (Neither name is fully-qualified.) Example: Subscriber to SubscriberServiceApi. 



**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Map from original service names to renamed versions. This is used when the default generated types would cause a naming conflict. (Neither name is fully-qualified.) Example: Subscriber to SubscriberServiceApi. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
