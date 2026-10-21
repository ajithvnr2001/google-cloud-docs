---
url: https://docs.cloud.google.com/model-armor/data-residency/
title: Data residency and endpoints \u00a0|\u00a0 Model Armor \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:05:42.173461+00:00
---

# Data residency and endpoints  |  Model Armor  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/model-armor/data-residency/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Model Armor ](https://docs.cloud.google.com/model-armor)
  * [ Guides ](https://docs.cloud.google.com/model-armor/overview)



Send feedback 

#  Data residency and endpoints Stay organized with collections  Save and categorize content based on your preferences. 

This document explains when data residency is enforced in each location where Model Armor is available. Data residency lets you specify a geographic region where your data is stored and processed, which helps ensure that your data remains in that location. Model Armor helps provide control over where your data is handled, supporting compliance with various regulations.

Model Armor processes the following types of data:

  * **Core data** : The primary data that Model Armor processes, most relevant to data residency, which includes prompts, responses, and input files. Model Armor processes core data but doesn't store it at rest. For more information, see [Data handling and storage](https://docs.cloud.google.com/model-armor/overview#data-handling).

  * **Configuration data** : Template and floor setting configurations such as rules, filters, and thresholds that Model Armor uses to scan prompts and responses. Model Armor processes and stores configuration data at rest.




## Data residency enforcement for templates

This section indicates the data residency controls enforced by Model Armor templates for each supported Google Cloud location. Model Armor maintains data residency at the jurisdiction level, for example, a specific country like India, or a multi-region like `eu`.

**Note:** The information in this section also applies to all Model Armor [integrations](https://docs.cloud.google.com/model-armor/integrations)—except for the integration with Google and Google Cloud MCP servers, which doesn't support Model Armor templates.

Model Armor works in the following regions and multi-regions. However, by default, Model Armor has limited feature support in some regions to maintain strict data residency, including in-jurisdiction data processing. For information about the regions with full and limited support, see [Feature availability by region](https://docs.cloud.google.com/model-armor/feature-availability-by-region).

If you must use a limited-support region but you want to prioritize comprehensive security filtering over strict data residency, you can [disable data residency enforcement](https://docs.cloud.google.com/model-armor/manage-templates#set-data-residency-compliance) in your Model Armor template.

Region/multi-region | Jurisdiction | At rest | In use | In transit | Feature support1  
---|---|---|---|---|---  
`asia-northeast1` | [Japan](https://docs.cloud.google.com/assured-workloads/docs/control-packages/japan-data-boundary) | Yes | Yes | Yes | [Limited support](https://docs.cloud.google.com/model-armor/feature-availability-by-region#limited-support)  
`asia-northeast3` | [South Korea](https://docs.cloud.google.com/assured-workloads/docs/control-packages/south-korea-data-boundary) | Yes | Yes | Yes | [Limited support](https://docs.cloud.google.com/model-armor/feature-availability-by-region#limited-support)  
`asia-south1` | [India](https://docs.cloud.google.com/assured-workloads/docs/control-packages/india-data-boundary) | Yes | Yes | Yes | [Limited support](https://docs.cloud.google.com/model-armor/feature-availability-by-region#limited-support)  
`asia-southeast1` | [Singapore](https://docs.cloud.google.com/assured-workloads/docs/control-packages/singapore-data-boundary) | Yes | Yes | Yes | [Limited support](https://docs.cloud.google.com/model-armor/feature-availability-by-region#limited-support)  
`australia-southeast2` | [Australia](https://docs.cloud.google.com/assured-workloads/docs/control-packages/australia-data-boundary) | Yes | Yes | Yes | [Limited support](https://docs.cloud.google.com/model-armor/feature-availability-by-region#limited-support)  
`eu` | [European Union](https://docs.cloud.google.com/assured-workloads/docs/control-packages/eu-data-boundary) | Yes | Yes | Yes | [Full support](https://docs.cloud.google.com/model-armor/feature-availability-by-region#full-support)  
`europe-southwest1` | [European Union](https://docs.cloud.google.com/assured-workloads/docs/control-packages/eu-data-boundary) | Yes | Yes | Yes | [Full support](https://docs.cloud.google.com/model-armor/feature-availability-by-region#full-support)  
`europe-west1` | [European Union](https://docs.cloud.google.com/assured-workloads/docs/control-packages/eu-data-boundary) | Yes | Yes | Yes | [Full support](https://docs.cloud.google.com/model-armor/feature-availability-by-region#full-support)  
`europe-west2` | [United Kingdom](https://docs.cloud.google.com/assured-workloads/docs/control-packages/uk-data-boundary) | Yes | Yes | Yes | [Limited support](https://docs.cloud.google.com/model-armor/feature-availability-by-region#limited-support)  
`europe-west3` | [European Union](https://docs.cloud.google.com/assured-workloads/docs/control-packages/eu-data-boundary) | Yes | Yes | Yes | [Full support](https://docs.cloud.google.com/model-armor/feature-availability-by-region#full-support)  
`europe-west4` | [European Union](https://docs.cloud.google.com/assured-workloads/docs/control-packages/eu-data-boundary) | Yes | Yes | Yes | [Full support](https://docs.cloud.google.com/model-armor/feature-availability-by-region#full-support)  
`europe-west9` | [European Union](https://docs.cloud.google.com/assured-workloads/docs/control-packages/eu-data-boundary) | Yes | Yes | Yes | [Full support](https://docs.cloud.google.com/model-armor/feature-availability-by-region#full-support)  
`northamerica-northeast2` | [Canada](https://docs.cloud.google.com/assured-workloads/docs/control-packages/canada-data-boundary) | Yes | Yes | Yes | [Limited support](https://docs.cloud.google.com/model-armor/feature-availability-by-region#limited-support)  
`us` | [United States](https://docs.cloud.google.com/assured-workloads/docs/control-packages/us-data-boundary) | Yes | Yes | Yes | [Full support](https://docs.cloud.google.com/model-armor/feature-availability-by-region#full-support)  
`us-central1` | [United States](https://docs.cloud.google.com/assured-workloads/docs/control-packages/us-data-boundary) | Yes | Yes | Yes | [Full support](https://docs.cloud.google.com/model-armor/feature-availability-by-region#full-support)  
`us-east1` | [United States](https://docs.cloud.google.com/assured-workloads/docs/control-packages/us-data-boundary) | Yes | Yes | Yes | [Full support](https://docs.cloud.google.com/model-armor/feature-availability-by-region#full-support)  
`us-east4` | [United States](https://docs.cloud.google.com/assured-workloads/docs/control-packages/us-data-boundary) | Yes | Yes | Yes | [Full support](https://docs.cloud.google.com/model-armor/feature-availability-by-region#full-support)  
`us-west1` | [United States](https://docs.cloud.google.com/assured-workloads/docs/control-packages/us-data-boundary) | Yes | Yes | Yes | [Full support](https://docs.cloud.google.com/model-armor/feature-availability-by-region#full-support)  
  
1The **Feature support** column is relevant only to Model Armor configurations that use templates. For Model Armor configurations that use floor settings, all features are available but data residency enforcement for data in use and in transit varies by location.

The **Jurisdiction** column indicates the geographical boundary (for example, a country or a multi-region like `eu` or `us`) within which Model Armor ensures data residency compliance for the supported states (at rest, in use, and in transit) as indicated in the table.

The **Region/multi-region** column lists the specific Google Cloud region or multi-region identifier.

When data residency is enforced for a region in Model Armor, it helps ensure that data remains within a specified jurisdiction while in at least one of the following states:

  * **At rest** : Stored data remains within the specific Google Cloud region listed.

  * **In use** and **In transit** : Data residency enforcement for these states within the specified jurisdiction depends on the values in the **In use** and **In transit** columns:

    * **Yes** : Data residency is enforced for the _In use_ and _In transit_ states within the listed jurisdiction. This means that the data remains within the boundaries of the listed jurisdiction while being processed or transmitted (not necessarily within that single region).
    * **No** : Data residency is not enforced for the _In use_ and _In transit_ states within the listed jurisdiction. This means that the data might be processed or transmitted outside of the jurisdiction.

**Note:** For Assured Workloads, Model Armor maintains data residency within the selected jurisdiction for [supported locations](https://docs.cloud.google.com/model-armor/locations) for data in use. For more information, see [Assured Workloads Service Specific Terms](https://cloud.google.com/terms/service-terms#37).

## Data residency for Model Armor integrations using floor settings

The following sections explain how data residency is enforced for Model Armor floor settings across integrations.

### Integration with Gemini Enterprise Agent Platform

If you use floor settings for the [Agent Platform integration](https://docs.cloud.google.com/model-armor/model-armor-vertex-integration), all Model Armor features are available in the following locations. However, data residency enforcement for data in use and in transit varies by region.

**Note:** Floor settings for the Agent Platform integration don't apply to requests sent to Agent Platform [multi-regional endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/locations#multi-region_endpoints), such as `aiplatform.us.rep.googleapis.com` or `aiplatform.eu.rep.googleapis.com`.

#### Show supported regions

Region | Jurisdiction | At rest | In use | In transit  
---|---|---|---|---  
`asia-northeast1` |  [Japan](https://docs.cloud.google.com/assured-workloads/docs/control-packages/japan-data-boundary) | Yes | No | No  
`asia-northeast3` |  [South Korea](https://docs.cloud.google.com/assured-workloads/docs/control-packages/south-korea-data-boundary) | Yes | No | No  
`asia-south1` |  [India](https://docs.cloud.google.com/assured-workloads/docs/control-packages/india-data-boundary) | Yes | No | No  
`asia-southeast1` |  [Singapore](https://docs.cloud.google.com/assured-workloads/docs/control-packages/singapore-data-boundary) | Yes | No | No  
`australia-southeast2` |  [Australia](https://docs.cloud.google.com/assured-workloads/docs/control-packages/australia-data-boundary) | Yes | No | No  
`europe-southwest1` |  [European Union](https://docs.cloud.google.com/assured-workloads/docs/control-packages/eu-data-boundary) | Yes | Yes | Yes  
`europe-west1` |  [European Union](https://docs.cloud.google.com/assured-workloads/docs/control-packages/eu-data-boundary) | Yes | Yes | Yes  
`europe-west2` |  [United Kingdom](https://docs.cloud.google.com/assured-workloads/docs/control-packages/uk-data-boundary) | Yes | No | No  
`europe-west3` |  [European Union](https://docs.cloud.google.com/assured-workloads/docs/control-packages/eu-data-boundary) | Yes | Yes | Yes  
`europe-west4` |  [European Union](https://docs.cloud.google.com/assured-workloads/docs/control-packages/eu-data-boundary) | Yes | Yes | Yes  
`europe-west9` |  [European Union](https://docs.cloud.google.com/assured-workloads/docs/control-packages/eu-data-boundary) | Yes | Yes | Yes  
`northamerica-northeast2` |  [Canada](https://docs.cloud.google.com/assured-workloads/docs/control-packages/canada-data-boundary) | Yes | No | No  
`us-central1` |  [United States](https://docs.cloud.google.com/assured-workloads/docs/control-packages/us-data-boundary) | Yes | Yes | Yes  
`us-east1` |  [United States](https://docs.cloud.google.com/assured-workloads/docs/control-packages/us-data-boundary) | Yes | Yes | Yes  
`us-east4` |  [United States](https://docs.cloud.google.com/assured-workloads/docs/control-packages/us-data-boundary) | Yes | Yes | Yes  
`us-west1` |  [United States](https://docs.cloud.google.com/assured-workloads/docs/control-packages/us-data-boundary) | Yes | Yes | Yes  
  
### Integration with Google and Google Cloud MCP servers

Model Armor is a regionalized service, but it's not available in every Google Cloud region where Google and Google Cloud MCP servers operate. If you [enable Model Armor for an MCP-supported service](https://docs.cloud.google.com/model-armor/model-armor-mcp-google-cloud-integration) in a jurisdiction where Model Armor isn't present, Model Armor is called depending on whether the MCP-supported service uses _cross-jurisdictional routing_ or _data residency compliant routing_.

#### Google and Google Cloud MCP servers with cross-jurisdictional routing

For [Google and Google Cloud MCP servers](https://docs.cloud.google.com/model-armor/model-armor-mcp-google-cloud-integration) with [cross-jurisdictional routing](https://docs.cloud.google.com/mcp/model-armor-supported-products#cross-jurisdictional-routing), Model Armor is always called if enabled. Cross-jurisdictional calls might impact data residency compliance for in-use and in-transit data.

To see which Google and Google Cloud MCP servers use cross-jurisdictional routing, see [Products with Model Armor support](https://docs.cloud.google.com/mcp/model-armor-supported-products#products-with-ma-support).

#### Google and Google Cloud MCP servers with data residency compliant routing

For Google and Google Cloud MCP servers with [data residency compliant routing](https://docs.cloud.google.com/mcp/model-armor-supported-products#drz-compliant), Model Armor can be called in any region or multi-region within the European Union and the United States jurisdictions. Data residency is enforced for data at rest, in use, and in transit.

To see which Google and Google Cloud MCP servers use data residency compliant routing, see [Products with Model Armor support](https://docs.cloud.google.com/mcp/model-armor-supported-products#products-with-ma-support).

## Regional and multi-regional endpoints

Regional and multi-regional endpoints provide access to resources in a specific location. When you use a regional or multi-regional endpoint, your request is routed directly to the endpoint's location.

Each regional or multi-regional endpoint uses the following format:

`modelarmor.LOCATION.rep.googleapis.com`

Replace `LOCATION` with a supported Model Armor region or multi-region.

To create, update, or use templates to sanitize content, you must use a regional or multi-regional endpoint that matches the template's location.

Regional and multi-regional Model Armor endpoints don't support managing floor settings.

For general information about using regional and multi-regional endpoints, see [Google Cloud API endpoint overview](https://docs.cloud.google.com/docs/security/compliance/endpoints).

### VPC network requirements

To access Model Armor regional endpoints from within a VPC network, you must [create a Private Service Connect endpoint](https://docs.cloud.google.com/vpc/docs/access-regional-google-apis-endpoints#create-regional-endpoint) to the Model Armor APIs. This is required to prevent certificate errors when regional endpoints are accessed using Private Google Access or VPC Service Controls. For more information, see [Troubleshoot Model Armor issues](https://docs.cloud.google.com/model-armor/troubleshooting#ma-certificate-error) and [About accessing regional endpoints through Private Service Connect endpoints](https://docs.cloud.google.com/vpc/docs/about-accessing-regional-google-apis-endpoints).

## Global endpoint

The global endpoint (`modelarmor.googleapis.com`) is supported only for managing [Model Armor floor settings](https://docs.cloud.google.com/model-armor/configure-floor-settings).

The global Model Armor endpoint doesn't support managing Model Armor templates or sanitizing prompts and responses.

For general information about global endpoints, see [Google Cloud API endpoint overview](https://docs.cloud.google.com/docs/security/compliance/endpoints).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-12 UTC."],[],[]] 
