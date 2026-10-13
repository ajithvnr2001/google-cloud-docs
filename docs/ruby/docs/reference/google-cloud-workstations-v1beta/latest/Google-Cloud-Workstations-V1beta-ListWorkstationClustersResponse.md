---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workstations-v1beta/latest/Google-Cloud-Workstations-V1beta-ListWorkstationClustersResponse/
title: Cloud Workstations V1BETA API - Class Google::Cloud::Workstations::V1beta::ListWorkstationClustersResponse (v0.10.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:51:15.238370+00:00
---

# Cloud Workstations V1BETA API - Class Google::Cloud::Workstations::V1beta::ListWorkstationClustersResponse (v0.10.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workstations-v1beta/latest/Google-Cloud-Workstations-V1beta-ListWorkstationClustersResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Workstations V1BETA API - Class Google::Cloud::Workstations::V1beta::ListWorkstationClustersResponse (v0.10.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.1 (latest)  0.10.0  0.9.0  0.8.1  0.7.1  0.6.0  0.5.1  0.4.1  0.3.0  0.2.0  0.1.3 

Reference documentation and code samples for the Cloud Workstations V1BETA API class Google::Cloud::Workstations::V1beta::ListWorkstationClustersResponse.

Response message for ListWorkstationClusters.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #next_page_token
    
    
    def next_page_token() -> ::String

**Returns**

  * (::String) — Token to retrieve the next page of results, or empty if there are no more results in the list. 



### #next_page_token=
    
    
    def next_page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — Token to retrieve the next page of results, or empty if there are no more results in the list. 



**Returns**

  * (::String) — Token to retrieve the next page of results, or empty if there are no more results in the list. 



### #unreachable
    
    
    def unreachable() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Unreachable resources. 



### #unreachable=
    
    
    def unreachable=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Unreachable resources. 



**Returns**

  * (::Array<::String>) — Unreachable resources. 



### #workstation_clusters
    
    
    def workstation_clusters() -> ::Array<::Google::Cloud::Workstations::V1beta::WorkstationCluster>

**Returns**

  * (::Array<[::Google::Cloud::Workstations::V1beta::WorkstationCluster](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workstations-v1beta/latest/Google-Cloud-Workstations-V1beta-WorkstationCluster)>) — The requested workstation clusters. 



### #workstation_clusters=
    
    
    def workstation_clusters=(value) -> ::Array<::Google::Cloud::Workstations::V1beta::WorkstationCluster>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Workstations::V1beta::WorkstationCluster](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workstations-v1beta/latest/Google-Cloud-Workstations-V1beta-WorkstationCluster)>) — The requested workstation clusters. 



**Returns**

  * (::Array<[::Google::Cloud::Workstations::V1beta::WorkstationCluster](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workstations-v1beta/latest/Google-Cloud-Workstations-V1beta-WorkstationCluster)>) — The requested workstation clusters. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
