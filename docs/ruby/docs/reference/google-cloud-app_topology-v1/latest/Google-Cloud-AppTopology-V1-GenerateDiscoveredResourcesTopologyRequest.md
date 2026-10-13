---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_topology-v1/latest/Google-Cloud-AppTopology-V1-GenerateDiscoveredResourcesTopologyRequest/
title: App Topology V1 API - Class Google::Cloud::AppTopology::V1::GenerateDiscoveredResourcesTopologyRequest (v0.1.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:03:55.776419+00:00
---

# App Topology V1 API - Class Google::Cloud::AppTopology::V1::GenerateDiscoveredResourcesTopologyRequest (v0.1.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_topology-v1/latest/Google-Cloud-AppTopology-V1-GenerateDiscoveredResourcesTopologyRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  App Topology V1 API - Class Google::Cloud::AppTopology::V1::GenerateDiscoveredResourcesTopologyRequest (v0.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

Reference documentation and code samples for the App Topology V1 API class Google::Cloud::AppTopology::V1::GenerateDiscoveredResourcesTopologyRequest.

Request for GenerateDiscoveredResourcesTopology.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #filter
    
    
    def filter() -> ::Google::Cloud::AppTopology::V1::GraphPattern

**Returns**

  * ([::Google::Cloud::AppTopology::V1::GraphPattern](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_topology-v1/latest/Google-Cloud-AppTopology-V1-GraphPattern)) — Filters for the topology nodes and edges; Detail format see GraphPattern proto. A separate 'LookupSchema' method will be added that will return the necessary information to be able to construct these filters. 



### #filter=
    
    
    def filter=(value) -> ::Google::Cloud::AppTopology::V1::GraphPattern

**Parameter**

  * **value** ([::Google::Cloud::AppTopology::V1::GraphPattern](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_topology-v1/latest/Google-Cloud-AppTopology-V1-GraphPattern)) — Filters for the topology nodes and edges; Detail format see GraphPattern proto. A separate 'LookupSchema' method will be added that will return the necessary information to be able to construct these filters. 



**Returns**

  * ([::Google::Cloud::AppTopology::V1::GraphPattern](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_topology-v1/latest/Google-Cloud-AppTopology-V1-GraphPattern)) — Filters for the topology nodes and edges; Detail format see GraphPattern proto. A separate 'LookupSchema' method will be added that will return the necessary information to be able to construct these filters. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Required. The project to query discoverable resources on. Expected format: `projects/{project}/locations/{location}/discoveredResourcesTopology`. Only `global` location is supported. 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The project to query discoverable resources on. Expected format: `projects/{project}/locations/{location}/discoveredResourcesTopology`. Only `global` location is supported. 



**Returns**

  * (::String) — Required. The project to query discoverable resources on. Expected format: `projects/{project}/locations/{location}/discoveredResourcesTopology`. Only `global` location is supported. 



### #topology_domains
    
    
    def topology_domains() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Required. The full resource name of the domain of the app topology. Format: `projects/{project}/locations/{location}/domains/{domain}` Caller must have apptopology.domains.get permission on each of the domains. 



### #topology_domains=
    
    
    def topology_domains=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Required. The full resource name of the domain of the app topology. Format: `projects/{project}/locations/{location}/domains/{domain}` Caller must have apptopology.domains.get permission on each of the domains. 



**Returns**

  * (::Array<::String>) — Required. The full resource name of the domain of the app topology. Format: `projects/{project}/locations/{location}/domains/{domain}` Caller must have apptopology.domains.get permission on each of the domains. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
