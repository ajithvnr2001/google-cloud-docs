---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-OsConfig-V1-Inventory-WindowsApplication/
title: Cloud Asset V1 API - Class Google::Cloud::OsConfig::V1::Inventory::WindowsApplication (v1.9.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:09:25.552503+00:00
---

# Cloud Asset V1 API - Class Google::Cloud::OsConfig::V1::Inventory::WindowsApplication (v1.9.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-OsConfig-V1-Inventory-WindowsApplication/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Asset V1 API - Class Google::Cloud::OsConfig::V1::Inventory::WindowsApplication (v1.9.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.9.1 (latest)  1.9.0  1.8.0  1.7.0  1.6.1  1.5.0  1.4.1  1.3.1  1.2.0  1.1.0  1.0.2  0.32.0  0.31.0  0.30.0  0.29.3  0.28.1  0.27.0  0.26.1  0.25.0  0.24.0  0.23.0  0.22.0  0.21.1  0.20.1  0.19.0  0.18.0  0.17.3 

Reference documentation and code samples for the Cloud Asset V1 API class Google::Cloud::OsConfig::V1::Inventory::WindowsApplication.

Contains information about a Windows application that is retrieved from the Windows Registry. For more information about these fields, see: <https://docs.microsoft.com/en-us/windows/win32/msi/uninstall-registry-key>

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #display_name
    
    
    def display_name() -> ::String

**Returns**

  * (::String) — The name of the application or product. 



### #display_name=
    
    
    def display_name=(value) -> ::String

**Parameter**

  * **value** (::String) — The name of the application or product. 



**Returns**

  * (::String) — The name of the application or product. 



### #display_version
    
    
    def display_version() -> ::String

**Returns**

  * (::String) — The version of the product or application in string format. 



### #display_version=
    
    
    def display_version=(value) -> ::String

**Parameter**

  * **value** (::String) — The version of the product or application in string format. 



**Returns**

  * (::String) — The version of the product or application in string format. 



### #help_link
    
    
    def help_link() -> ::String

**Returns**

  * (::String) — The internet address for technical support. 



### #help_link=
    
    
    def help_link=(value) -> ::String

**Parameter**

  * **value** (::String) — The internet address for technical support. 



**Returns**

  * (::String) — The internet address for technical support. 



### #install_date
    
    
    def install_date() -> ::Google::Type::Date

**Returns**

  * ([::Google::Type::Date](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Type-Date)) — The last time this product received service. The value of this property is replaced each time a patch is applied or removed from the product or the command-line option is used to repair the product. 



### #install_date=
    
    
    def install_date=(value) -> ::Google::Type::Date

**Parameter**

  * **value** ([::Google::Type::Date](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Type-Date)) — The last time this product received service. The value of this property is replaced each time a patch is applied or removed from the product or the command-line option is used to repair the product. 



**Returns**

  * ([::Google::Type::Date](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Type-Date)) — The last time this product received service. The value of this property is replaced each time a patch is applied or removed from the product or the command-line option is used to repair the product. 



### #publisher
    
    
    def publisher() -> ::String

**Returns**

  * (::String) — The name of the manufacturer for the product or application. 



### #publisher=
    
    
    def publisher=(value) -> ::String

**Parameter**

  * **value** (::String) — The name of the manufacturer for the product or application. 



**Returns**

  * (::String) — The name of the manufacturer for the product or application. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
