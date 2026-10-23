---
url: https://docs.cloud.google.com/agent-registry/locations/
title: Agent Registry locations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:51:51.805036+00:00
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

Agent Registry lets you register and discover agentic components in specific Google Cloud regions or in the `global` location to meet your latency, availability, and data residency requirements. Choosing the appropriate regional or global location scopes component discovery and gateway routing across your [governance project](https://docs.cloud.google.com/agent-registry/overview#governance-project) and workloads. For more information about regions and zones, see [Geography and regions](https://docs.cloud.google.com/docs/geography-and-regions).

## Governance scope across regional and global locations

When deploying and governing agentic architectures across Agent Registry, Agent Gateway, and Identity and Access Management (IAM), consider the following location and scoping rules:

  * **Google and Google Cloud remote MCP servers** : when Agent Registry automatically registers a [Google or Google Cloud remote MCP server](https://docs.cloud.google.com/mcp/supported-products) for an enabled API, it creates the `McpServer` resource only in the `global` location, not in individual regions such as `us-central1`. If the service provides regional endpoints (REPs), such as `https://SERVICE.REGION.rep.googleapis.com/mcp`, Agent Registry lists those regional URLs in the `interfaces` field of that single `global` `McpServer` resource: 
    * **Use`global` for automatically registered servers**: specify the `global` location when you query the server in Agent Registry with `--location=global` or apply Identity-Aware Proxy (IAP) policies to it with `--region=global`. If you specify a region such as `us-central1`, the command returns a `NOT_FOUND` error because no regional `McpServer` resource exists there by default.
    * **Register in a region for data residency** : if you need to keep registry metadata in a specific region, deploy custom MCP servers to regional [Cloud Run](https://docs.cloud.google.com/agent-registry/register-mcp-servers#cloud-run-mcp) or [Google Kubernetes Engine (GKE)](https://docs.cloud.google.com/agent-registry/register-mcp-servers#gke-mcp) runtimes, or [manually register](https://docs.cloud.google.com/agent-registry/register-mcp-servers#register-external-servers) the MCP server and its regional endpoint URL in that region, and then apply your IAP policy in that same region. When Agent Gateway resolves a target URL, regional registry entries take precedence over `global` entries. For troubleshooting information, see [Remote MCP server not found in a regional location](https://docs.cloud.google.com/agent-registry/troubleshooting#remote-mcp-server-regional-location).
  * **Regional gateways governing global MCP servers** : an Agent Gateway deployed in a regional location, such as `us-central1`, can govern and route traffic to `global` MCP servers. The gateway registry lookup filter queries both regional and `global` resources.
  * **Egress policy bindings** : apply IAP egress authorization bindings in the same location where the target resource is registered in Agent Registry: 
    * For automatically registered Google and Google Cloud remote MCP servers, apply the binding in `global` with `--region=global`, even when the calling agent sends traffic through a regional gateway.
    * For resources registered in a specific region, apply the binding in that region. For troubleshooting information, see [Resource entity not found error when managing IAP policies](https://docs.cloud.google.com/agent-registry/troubleshooting#resource-entity-not-found).
  * **Registration locations** : you must manually register agents, MCP servers, and endpoints, and create bindings, in a supported regional location or the `global` location. For details on multi-region support, see Multi-regions.
  * **Regional alignment for policy enforcement** : if you configure [Model Armor policy filters](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/configure-model-armor) on Agent Gateway, the gateway, the Model Armor templates, and the authorization extension and policy must reside in the same region. Because Model Armor inspects request and response payloads at the regional gateway, the gateway can still inspect and govern traffic routed to MCP servers registered in the `global` location as well as regional destinations. For troubleshooting information, see [Region mismatch errors when configuring Model Armor on Agent Gateway](https://docs.cloud.google.com/agent-registry/troubleshooting#model-armor-region-mismatch).
  * **Organization policy location restrictions** : if your organization has specific requirements for the geographic location of resources, your organization policy might include [resource location constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations) (`constraints/gcp.resourceLocations`). Agent Registry enforces those constraints when you create regional `Service`, `Binding`, `Skill`, or `SkillRevision` resources. Organization policy compliance isn't enforced retroactively, so applying a resource location constraint doesn't affect existing Agent Registry resources or updates to those resources. For more information, see [Services that support restricting resource locations](https://docs.cloud.google.com/organization-policy/reference/restrict-locations-supported-services#agent-registry).



## Global

You can register and discover resources without a specific geographic restriction by using the `global` location.

All resources in Agent Registry are supported in the `global` location.

## Multi-regions

In supported [multi-regions](https://docs.cloud.google.com/architecture/deployment-archetypes/multiregional), you can discover [automatically registered](https://docs.cloud.google.com/agent-registry/component-lifecycle-and-discovery#automatic-registration) agents and MCP servers from [Gemini Enterprise](https://docs.cloud.google.com/gemini/enterprise/docs) and register or discover standalone [skills](https://docs.cloud.google.com/agent-registry/skills-architecture).

Manual registration of agents, MCP servers, or endpoints, and the creation of bindings, are only supported in regional locations or the `global` location. Those operations aren't supported in multi-region locations. For troubleshooting information, see [Manual registration or binding creation fails in a multi-region location](https://docs.cloud.google.com/agent-registry/troubleshooting#multi-region-unsupported-operation).

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

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
