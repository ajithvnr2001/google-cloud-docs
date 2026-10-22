---
url: https://docs.cloud.google.com/agent-registry/locations/
title: Agent Registry locations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:38:22.693789+00:00
---

# Agent Registry locations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/agent-registry/locations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Registry ](https://docs.cloud.google.com/agent-registry)
  * [ Resources ](https://docs.cloud.google.com/agent-registry/resources)



Send feedback 

#  Agent Registry locations Stay organized with collections  Save and categorize content based on your preferences. 

Agent Registry is available in the following regions and global locations. For more information about regions and zones, see [Geography and regions](https://docs.cloud.google.com/docs/geography-and-regions).

## Governance scope across regional and global locations

When deploying and governing agentic architectures across Agent Registry, Agent Gateway, and IAM, consider the following location and scoping rules:

  * **Google-managed MCP servers** : Built-in Google-managed MCP servers, associated with enabled Google and Google Cloud APIs, are automatically registered in the `global` location. Looking up a Google-managed server in a regional location returns an error.
  * **Regional gateways governing global MCP servers** : An Agent Gateway deployed in a regional location, such as `us-central1`, can govern and route traffic to `global` MCP servers. The gateway registry lookup filter queries both regional and `global` records.
  * **Egress policy bindings** : Identity-Aware Proxy egress authorization bindings for Google-managed MCP servers must be applied at the `global` location, matching the server's registration location, even when the calling agent sends traffic through a regional gateway.
  * **Registration locations** : You must manually register agents, MCP servers, and endpoints, and create bindings, in a supported regional location or the `global` location. For details on multi-region support, see Multi-regions.
  * **Regional alignment for policy enforcement** : If you configure Model Armor policy filters on Agent Gateway, all resources must reside in the same region.



## Global

You can register and discover resources without a specific geographic restriction by using the `global` location.

All resources in Agent Registry are supported in the `global` location.

## Multi-regions

In supported [multi-regions](https://docs.cloud.google.com/architecture/deployment-archetypes/multiregional), you can discover automatically registered agentic components and register or discover standalone [skills](https://docs.cloud.google.com/agent-registry/concepts#skill).

Manual registration of agents, MCP servers, or endpoints, and the creation of bindings, are only supported in regional locations or the `global` location. Those operations aren't supported in multi-region locations.

The following table lists the multi-regions where Agent Registry is available.

Region description | Region name  
---|---  
United States | `us`  
Europe | `eu`  
  
## Americas

The following table lists the regions in the Americas where Agent Registry is available.

Region description | Region name  
---|---  
Iowa | `us-central1`  
South Carolina | `us-east1`  
Northern Virginia | `us-east4`  
Columbus | `us-east5`  
Dallas | `us-south1`  
Oregon | `us-west1`  
Los Angeles | `us-west2`  
Montréal | `northamerica-northeast1`  
Toronto | `northamerica-northeast2`  
Mexico | `northamerica-south1`  
São Paulo | `southamerica-east1`  
Santiago | `southamerica-west1`  
  
## Asia Pacific

The following table lists the regions in Asia Pacific where Agent Registry is available.

Region description | Region name  
---|---  
Taiwan | `asia-east1`  
Hong Kong | `asia-east2`  
Tokyo | `asia-northeast1`  
Osaka | `asia-northeast2`  
Seoul | `asia-northeast3`  
Mumbai | `asia-south1`  
Delhi | `asia-south2`  
Singapore | `asia-southeast1`  
Jakarta | `asia-southeast2`  
Kuala Lumpur | `asia-southeast3`  
Sydney | `australia-southeast1`  
Melbourne | `australia-southeast2`  
  
## Europe

The following table lists the regions in Europe where Agent Registry is available.

Region description | Region name  
---|---  
Warsaw | `europe-central2`  
Finland | `europe-north1`  
Sweden | `europe-north2`  
Madrid | `europe-southwest1`  
Belgium | `europe-west1`  
London | `europe-west2`  
Frankfurt | `europe-west3`  
Netherlands | `europe-west4`  
Zurich | `europe-west6`  
Milan | `europe-west8`  
Paris | `europe-west9`  
Berlin | `europe-west10`  
Turin | `europe-west12`  
  
## Middle East

The following table lists the regions in the Middle East where Agent Registry is available.

Region description | Region name  
---|---  
Doha | `me-central1`  
Dammam | `me-central2`  
Tel Aviv | `me-west1`  
  
## Africa

The following table lists the regions in Africa where Agent Registry is available.

Region description | Region name  
---|---  
Johannesburg | `africa-south1`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
