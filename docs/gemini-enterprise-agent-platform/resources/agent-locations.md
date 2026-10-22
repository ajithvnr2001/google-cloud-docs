---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/agent-locations/
title: Supported locations for agents in Agent Platform \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:41:32.062720+00:00
---

# Supported locations for agents in Agent Platform  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/agent-locations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)



Send feedback 

#  Supported locations for agents in Agent Platform Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the supported locations for Google agents and agent infrastructure features in Gemini Enterprise Agent Platform.

Supported locations for agent infrastructure features provide [data-at-rest residency](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/data-residency#data-at-rest) for your data (including agent source code, deployment packages, session history, memory bank entries, and metadata) in the selected location. When an agent invokes foundation models or generative AI services, ML processing support is governed by the [location and endpoint](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/locations) configured for that model.

For more information about regions and zones, see [Geography and regions](https://docs.cloud.google.com/docs/geography-and-regions).

The following agent infrastructure features are supported in the zones, regions, and multi-regions listed in the table:

  * [Runtime](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/runtime)
  * [Sessions](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/sessions)
  * [Agent Platform Memory Bank](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/memory-bank)
  * [Sandboxes](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/sandbox) ([Code Execution](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/sandbox/code-execution-overview), [shell execution](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/sandbox/shell-sandbox-quickstart), [Computer Use](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/sandbox/computer-use), and [custom container images](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/sandbox/custom-containers))
  * [Agent Gateway](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/agent-gateway-runtime-deploy)

Region | Location | Supported versions  
---|---|---  
`us-east1` | South Carolina | `v1` is supported for GA features. `v1beta1` is supported for Preview features.  
`us-east4` | Northern Virginia | `v1` is supported for GA features. `v1beta1` is supported for Preview features.  
`us-west1` | Oregon | `v1` is supported for GA features. `v1beta1` is supported for Preview features.  
`us-central1` | Iowa | `v1` is supported for GA features. `v1beta1` is supported for Preview features.  
`europe-west1` | Belgium | `v1` is supported for GA features. `v1beta1` is supported for Preview features.  
`europe-west2` | London | `v1` is supported for GA features. `v1beta1` is supported for Preview features.  
`europe-west3` | Frankfurt | `v1` is supported for GA features. `v1beta1` is supported for Preview features.  
`europe-west4` | Netherlands | `v1` is supported for GA features. `v1beta1` is supported for Preview features.  
`europe-west6` | Zurich | `v1` is supported for GA features. `v1beta1` is supported for Preview features.  
`europe-west8` | Milan | `v1` is supported for GA features. `v1beta1` is supported for Preview features.  
`europe-southwest1` | Madrid | `v1` is supported for GA features. `v1beta1` is supported for Preview features.  
`asia-east1` | Taiwan | `v1` is supported for GA features. `v1beta1` is supported for Preview features.  
`asia-east2†` | Hong Kong | `v1` is supported for GA features. `v1beta1` is supported for Preview features.  
`asia-northeast1` | Tokyo | `v1` is supported for GA features. `v1beta1` is supported for Preview features.  
`asia-northeast3†` | Seoul | `v1` is supported for GA features. `v1beta1` is supported for Preview features.  
`asia-south1` | Mumbai | `v1` is supported for GA features. `v1beta1` is supported for Preview features.  
`asia-southeast1` | Singapore | `v1` is supported for GA features. `v1beta1` is supported for Preview features.  
`asia-southeast2*†` | Jakarta | `v1` is supported for GA features. `v1beta1` is supported for Preview features.  
`australia-southeast2*` | Melbourne | `v1` is supported for GA features. `v1beta1` is supported for Preview features.  
`me-west1` | Tel Aviv | `v1` is supported for GA features. `v1beta1` is supported for Preview features.  
`northamerica-northeast1` | Montréal | `v1` is supported for GA features. `v1beta1` is supported for Preview features.  
`northamerica-northeast2*` | Toronto | `v1` is supported for GA features. `v1beta1` is supported for Preview features.  
`southamerica-east1` | São Paulo | `v1` is supported for GA features. `v1beta1` is supported for Preview features.  
  
* Memory Bank is not supported in this region.

† Agent Gateway is not supported in this region.

## Multi-regional and global endpoints

[Memory Bank](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/memory-bank), [Sessions](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/sessions), [Runtime](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/runtime), and [Code Execution](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/sandbox/code-execution-overview) support multi-regional endpoints. Memory Bank and Sessions also support global endpoints. For global requests, set your location to `global`. For multi-regional requests, set your location to `us` or `eu`.

**Note:** You can't use CMEK if your Memory Bank or Sessions is configured to use the global endpoint. Cloud Key Management Service requires encryption keys to reside within a fixed geographic data residency boundary. Because the global region lacks a physical geographic boundary, it is barred from encrypting localized regional or multi-regional resources.**Note:** You can't use CMEK if your Runtime is configured to use a multi-regional endpoint.

### Supported agents

Usage of the global endpoint is supported for the following Google agents.

  * [CodeMender](https://docs.cloud.google.com/gemini-enterprise-agent-platform/agents/codemender) (Preview) 
  * [Gemini Deep Research Agent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/agents/google/deep-research) (Preview) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
