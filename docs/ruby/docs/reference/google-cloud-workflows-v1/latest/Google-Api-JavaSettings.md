---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workflows-v1/latest/Google-Api-JavaSettings/
title: Workflows V1 API - Class Google::Api::JavaSettings (v2.6.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:28:51.174386+00:00
---

# Workflows V1 API - Class Google::Api::JavaSettings (v2.6.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workflows-v1/latest/Google-Api-JavaSettings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Workflows V1 API - Class Google::Api::JavaSettings (v2.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.6.1 (latest)  2.6.0  2.5.1  2.4.1  2.3.0  2.2.0  2.1.1  2.0.0  1.2.0  1.1.0  1.0.2  0.8.0  0.7.2  0.6.0  0.5.0  0.4.1  0.3.0  0.2.0  0.1.5 

Reference documentation and code samples for the Workflows V1 API class Google::Api::JavaSettings.

Settings for Java client libraries.

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

  * ([::Google::Api::CommonLanguageSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workflows-v1/latest/Google-Api-CommonLanguageSettings)) — Some settings. 



### #common=
    
    
    def common=(value) -> ::Google::Api::CommonLanguageSettings

**Parameter**

  * **value** ([::Google::Api::CommonLanguageSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workflows-v1/latest/Google-Api-CommonLanguageSettings)) — Some settings. 



**Returns**

  * ([::Google::Api::CommonLanguageSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workflows-v1/latest/Google-Api-CommonLanguageSettings)) — Some settings. 



### #library_package
    
    
    def library_package() -> ::String

**Returns**

  * (::String) — 

The package name to use in Java. Clobbers the java_package option set in the protobuf. This should be used **only** by APIs who have already set the language_settings.java.package_name" field in gapic.yaml. API teams should use the protobuf java_package option where possible.

Example of a YAML configuration::
        
        publishing:
          library_settings:
            java_settings:
              library_package: com.google.cloud.pubsub.v1
        




### #library_package=
    
    
    def library_package=(value) -> ::String

**Parameter**

  * **value** (::String) — 

The package name to use in Java. Clobbers the java_package option set in the protobuf. This should be used **only** by APIs who have already set the language_settings.java.package_name" field in gapic.yaml. API teams should use the protobuf java_package option where possible.

Example of a YAML configuration::
        
        publishing:
          library_settings:
            java_settings:
              library_package: com.google.cloud.pubsub.v1
        




**Returns**

  * (::String) — 

The package name to use in Java. Clobbers the java_package option set in the protobuf. This should be used **only** by APIs who have already set the language_settings.java.package_name" field in gapic.yaml. API teams should use the protobuf java_package option where possible.

Example of a YAML configuration::
        
        publishing:
          library_settings:
            java_settings:
              library_package: com.google.cloud.pubsub.v1
        




### #service_class_names
    
    
    def service_class_names() -> ::Google::Protobuf::Map{::String => ::String}

**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — 

Configure the Java class name to use instead of the service's for its corresponding generated GAPIC client. Keys are fully-qualified service names as they appear in the protobuf (including the full the language_settings.java.interface_names" field in gapic.yaml. API teams should otherwise use the service name as it appears in the protobuf.

Example of a YAML configuration::
        
        publishing:
          java_settings:
            service_class_names:
              - google.pubsub.v1.Publisher: TopicAdmin
              - google.pubsub.v1.Subscriber: SubscriptionAdmin
        




### #service_class_names=
    
    
    def service_class_names=(value) -> ::Google::Protobuf::Map{::String => ::String}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::String}) — 

Configure the Java class name to use instead of the service's for its corresponding generated GAPIC client. Keys are fully-qualified service names as they appear in the protobuf (including the full the language_settings.java.interface_names" field in gapic.yaml. API teams should otherwise use the service name as it appears in the protobuf.

Example of a YAML configuration::
        
        publishing:
          java_settings:
            service_class_names:
              - google.pubsub.v1.Publisher: TopicAdmin
              - google.pubsub.v1.Subscriber: SubscriptionAdmin
        




**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — 

Configure the Java class name to use instead of the service's for its corresponding generated GAPIC client. Keys are fully-qualified service names as they appear in the protobuf (including the full the language_settings.java.interface_names" field in gapic.yaml. API teams should otherwise use the service name as it appears in the protobuf.

Example of a YAML configuration::
        
        publishing:
          java_settings:
            service_class_names:
              - google.pubsub.v1.Publisher: TopicAdmin
              - google.pubsub.v1.Subscriber: SubscriptionAdmin
        




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
