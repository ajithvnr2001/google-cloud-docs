---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1beta/latest/Google-Cloud-NetworkConnectivity-V1beta-AutoAccept/
title: Network Connectivity V1BETA API - Class Google::Cloud::NetworkConnectivity::V1beta::AutoAccept (v0.3.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:48:21.376600+00:00
---

# Network Connectivity V1BETA API - Class Google::Cloud::NetworkConnectivity::V1beta::AutoAccept (v0.3.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1beta/latest/Google-Cloud-NetworkConnectivity-V1beta-AutoAccept/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Network Connectivity V1BETA API - Class Google::Cloud::NetworkConnectivity::V1beta::AutoAccept (v0.3.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.3.2 (latest)  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Network Connectivity V1BETA API class Google::Cloud::NetworkConnectivity::V1beta::AutoAccept.

The auto-accept setting for a group controls whether proposed spokes are automatically attached to the hub. If auto-accept is enabled, the spoke immediately is attached to the hub and becomes part of the group. In this case, the new spoke is in the ACTIVE state. If auto-accept is disabled, the spoke goes to the INACTIVE state, and it must be reviewed and accepted by a hub administrator.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #auto_accept_projects
    
    
    def auto_accept_projects() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Optional. A list of project ids or project numbers for which you want to enable auto-accept. The auto-accept setting is applied to spokes being created or updated in these projects. 



### #auto_accept_projects=
    
    
    def auto_accept_projects=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Optional. A list of project ids or project numbers for which you want to enable auto-accept. The auto-accept setting is applied to spokes being created or updated in these projects. 



**Returns**

  * (::Array<::String>) — Optional. A list of project ids or project numbers for which you want to enable auto-accept. The auto-accept setting is applied to spokes being created or updated in these projects. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
