---
url: https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-UpgradeOccurrence/
title: Grafeas V1 API - Class Grafeas::V1::UpgradeOccurrence (v1.10.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:11:37.471081+00:00
---

# Grafeas V1 API - Class Grafeas::V1::UpgradeOccurrence (v1.10.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-UpgradeOccurrence/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Grafeas V1 API - Class Grafeas::V1::UpgradeOccurrence (v1.10.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.10.1 (latest)  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.1  1.4.0  1.3.1  1.2.0  1.1.1  1.0.0  0.16.1  0.15.0  0.14.2  0.13.0  0.12.1  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.1  0.5.0  0.4.0  0.3.1 

Reference documentation and code samples for the Grafeas V1 API class Grafeas::V1::UpgradeOccurrence.

An Upgrade Occurrence represents that a specific resource_url could install a specific upgrade. This presence is supplied via local sources (i.e. it is present in the mirror and the running system has noticed its availability). For Windows, both distribution and windows_update contain information for the Windows update.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #distribution
    
    
    def distribution() -> ::Grafeas::V1::UpgradeDistribution

**Returns**

  * ([::Grafeas::V1::UpgradeDistribution](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-UpgradeDistribution)) — Metadata about the upgrade for available for the specific operating system for the resource_url. This allows efficient filtering, as well as making it easier to use the occurrence. 



### #distribution=
    
    
    def distribution=(value) -> ::Grafeas::V1::UpgradeDistribution

**Parameter**

  * **value** ([::Grafeas::V1::UpgradeDistribution](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-UpgradeDistribution)) — Metadata about the upgrade for available for the specific operating system for the resource_url. This allows efficient filtering, as well as making it easier to use the occurrence. 



**Returns**

  * ([::Grafeas::V1::UpgradeDistribution](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-UpgradeDistribution)) — Metadata about the upgrade for available for the specific operating system for the resource_url. This allows efficient filtering, as well as making it easier to use the occurrence. 



### #package
    
    
    def package() -> ::String

**Returns**

  * (::String) — Required for non-Windows OS. The package this Upgrade is for. 



### #package=
    
    
    def package=(value) -> ::String

**Parameter**

  * **value** (::String) — Required for non-Windows OS. The package this Upgrade is for. 



**Returns**

  * (::String) — Required for non-Windows OS. The package this Upgrade is for. 



### #parsed_version
    
    
    def parsed_version() -> ::Grafeas::V1::Version

**Returns**

  * ([::Grafeas::V1::Version](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-Version)) — Required for non-Windows OS. The version of the package in a machine + human readable form. 



### #parsed_version=
    
    
    def parsed_version=(value) -> ::Grafeas::V1::Version

**Parameter**

  * **value** ([::Grafeas::V1::Version](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-Version)) — Required for non-Windows OS. The version of the package in a machine + human readable form. 



**Returns**

  * ([::Grafeas::V1::Version](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-Version)) — Required for non-Windows OS. The version of the package in a machine + human readable form. 



### #windows_update
    
    
    def windows_update() -> ::Grafeas::V1::WindowsUpdate

**Returns**

  * ([::Grafeas::V1::WindowsUpdate](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-WindowsUpdate)) — Required for Windows OS. Represents the metadata about the Windows update. 



### #windows_update=
    
    
    def windows_update=(value) -> ::Grafeas::V1::WindowsUpdate

**Parameter**

  * **value** ([::Grafeas::V1::WindowsUpdate](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-WindowsUpdate)) — Required for Windows OS. Represents the metadata about the Windows update. 



**Returns**

  * ([::Grafeas::V1::WindowsUpdate](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-WindowsUpdate)) — Required for Windows OS. Represents the metadata about the Windows update. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
