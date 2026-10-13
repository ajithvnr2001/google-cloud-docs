---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Api-PhpSettings/
title: Cloud Vision V1 API - Class Google::Api::PhpSettings (v1.7.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:05:24.474929+00:00
---

# Cloud Vision V1 API - Class Google::Api::PhpSettings (v1.7.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Api-PhpSettings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Vision V1 API - Class Google::Api::PhpSettings (v1.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.7.1 (latest)  1.7.0  1.6.0  1.5.1  1.4.0  1.3.1  1.2.1  1.1.0  1.0.1  0.15.0  0.14.0  0.13.2  0.12.0  0.11.1  0.10.0  0.9.0  0.8.0  0.7.0  0.6.4 

Reference documentation and code samples for the Cloud Vision V1 API class Google::Api::PhpSettings.

Settings for Php client libraries.

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

  * ([::Google::Api::CommonLanguageSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Api-CommonLanguageSettings)) — Some settings. 



### #common=
    
    
    def common=(value) -> ::Google::Api::CommonLanguageSettings

**Parameter**

  * **value** ([::Google::Api::CommonLanguageSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Api-CommonLanguageSettings)) — Some settings. 



**Returns**

  * ([::Google::Api::CommonLanguageSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Api-CommonLanguageSettings)) — Some settings. 



### #library_package
    
    
    def library_package() -> ::String

**Returns**

  * (::String) — 

The package name to use in Php. Clobbers the php_namespace option set in the protobuf. This should be used **only** by APIs who have already set the language_settings.php.package_name" field in gapic.yaml. API teams should use the protobuf php_namespace option where possible.

Example of a YAML configuration::
        
        publishing:
          library_settings:
            php_settings:
              library_package: Google\Cloud\PubSub\V1
        




### #library_package=
    
    
    def library_package=(value) -> ::String

**Parameter**

  * **value** (::String) — 

The package name to use in Php. Clobbers the php_namespace option set in the protobuf. This should be used **only** by APIs who have already set the language_settings.php.package_name" field in gapic.yaml. API teams should use the protobuf php_namespace option where possible.

Example of a YAML configuration::
        
        publishing:
          library_settings:
            php_settings:
              library_package: Google\Cloud\PubSub\V1
        




**Returns**

  * (::String) — 

The package name to use in Php. Clobbers the php_namespace option set in the protobuf. This should be used **only** by APIs who have already set the language_settings.php.package_name" field in gapic.yaml. API teams should use the protobuf php_namespace option where possible.

Example of a YAML configuration::
        
        publishing:
          library_settings:
            php_settings:
              library_package: Google\Cloud\PubSub\V1
        




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
