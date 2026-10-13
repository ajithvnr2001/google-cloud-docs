---
url: https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs/reference/hardware/rest/v1alpha/HardwareConfig/
title: HardwareConfig \u00a0|\u00a0 Google Distributed Cloud connected, version 1.9.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:32:17.515505+00:00
---

# HardwareConfig  |  Google Distributed Cloud connected, version 1.9.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs/reference/hardware/rest/v1alpha/HardwareConfig/

Select versionkeyboard_arrow_down

  * [ 1.13.0 ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs)
  * [ 1.12.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs)
  * [ 1.11.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs)
  * [ 1.10.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs)
  * [ 1.9.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs)
  * [ 1.8.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs)
  * [ 1.7.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.1/docs)
  * [ 1.7.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.0/docs)
  * [ 1.6.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs)
  * [ 1.6.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs)
  * [ 1.5.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.5.1/docs)

For version information, see the [Distributed Cloud connected release notes](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/release-notes). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Connected ](https://docs.cloud.google.com/distributed-cloud/connected)
  * [ 1.9.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs/apis)



Send feedback 

#  HardwareConfig Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Configuration for GDC hardware.

JSON representation  
---  
      
    
    {
      "sku": string,
      "powerSupply": enum ([PowerSupply](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs/reference/hardware/rest/v1alpha/PowerSupply)),
      "subscriptionDurationMonths": integer
    }  
  
Fields  
---  
`sku` |  `string` Required. Reference to the SKU for this hardware. This can point to a specific SKU revision in the form of `resourceName@revisionId` as defined in [AIP-162](https://google.aip.dev/162). If no revisionId is specified, it refers to the latest revision.  
`powerSupply` |  `enum (`[PowerSupply](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs/reference/hardware/rest/v1alpha/PowerSupply)`)` Required. Power supply type for this hardware.  
`subscriptionDurationMonths` |  `integer` Optional. Subscription duration for the hardware in months.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-24 UTC."],[],[]] 
