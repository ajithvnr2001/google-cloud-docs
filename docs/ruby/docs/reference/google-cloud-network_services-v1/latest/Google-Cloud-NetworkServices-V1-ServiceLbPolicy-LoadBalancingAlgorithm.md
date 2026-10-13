---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_services-v1/latest/Google-Cloud-NetworkServices-V1-ServiceLbPolicy-LoadBalancingAlgorithm/
title: Network Services V1 API - Module Google::Cloud::NetworkServices::V1::ServiceLbPolicy::LoadBalancingAlgorithm (v2.12.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:08:32.412258+00:00
---

# Network Services V1 API - Module Google::Cloud::NetworkServices::V1::ServiceLbPolicy::LoadBalancingAlgorithm (v2.12.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_services-v1/latest/Google-Cloud-NetworkServices-V1-ServiceLbPolicy-LoadBalancingAlgorithm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Network Services V1 API - Module Google::Cloud::NetworkServices::V1::ServiceLbPolicy::LoadBalancingAlgorithm (v2.12.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.12.0 (latest)  2.11.0  2.10.1  2.9.0  2.8.0  2.7.0  2.6.1  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.1  1.2.0  1.1.0  1.0.1  0.2.0  0.1.0 

Reference documentation and code samples for the Network Services V1 API module Google::Cloud::NetworkServices::V1::ServiceLbPolicy::LoadBalancingAlgorithm.

The global load balancing algorithm to be used.

## Constants 

### LOAD_BALANCING_ALGORITHM_UNSPECIFIED

**value:** 0  
The type of the loadbalancing algorithm is unspecified.

### SPRAY_TO_WORLD

**value:** 3  
Balance traffic across all backends across the world proportionally based on capacity.

### SPRAY_TO_REGION

**value:** 4  
Direct traffic to the nearest region with endpoints and capacity before spilling over to other regions and spread the traffic from each client to all the MIGs/NEGs in a region.

### WATERFALL_BY_REGION

**value:** 5  
Direct traffic to the nearest region with endpoints and capacity before spilling over to other regions. All MIGs/NEGs within a region are evenly loaded but each client might not spread the traffic to all the MIGs/NEGs in the region.

### WATERFALL_BY_ZONE

**value:** 6  
Attempt to keep traffic in a single zone closest to the client, before spilling over to other zones.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-03 UTC."],[],[]] 
