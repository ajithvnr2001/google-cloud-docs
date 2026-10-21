---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/region/
title: Regionalization and data residency \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:22:26.657737+00:00
---

# Regionalization and data residency  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/region/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  Regionalization and data residency Stay organized with collections  Save and categorize content based on your preferences. 

Customer Experience Agent Studio provides [data residency (DRZ)](https://cloud.google.com/blog/products/identity-security/meet-data-residency-requirements-with-google-cloud) to keep your [data-at-rest](https://en.wikipedia.org/wiki/Data_at_rest) physically within a specified geographical region or location. When you specify a region, your data-at-rest is not stored outside that region. Pricing is the same for all regions.

Specifying a region is particularly helpful in the following use cases:

  * Your system has regulatory or policy requirements that govern where your data must reside.
  * Your network latencies might be improved when the data is in the same region as your customers.



## Available regions

Region ID | Description  
---|---  
`us` | Multi-region data centers in the United States.  
`eu` | Multi-region data centers in the European Union. Agent data in the EU multi-region is not stored in the EUROPE-WEST2 (London) or EUROPE-WEST6 (Zürich) regions.  
  
## Available features for regional serving

All features are available in all supported regions.

## ML processing

Machine learning (ML) processing occurs within the specific region or multi-region where the request is made. For the details on data residency support for each model and region, see [Gemini Enterprise Agent Platform - Data residency](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/data-residency#ml_processing).

The following models supported by CX Agent Studio are not mentioned on the Gemini Enterprise Agent Platform page, but the ML processing still occurs within your selected region or multi-region:

  * gemini-3.1-flash-live



## Data-at-rest

All Customer Experience Agent Studio developer user and end-user data is included in data-at-rest. For example:

  * Callback Code
  * Tool Code and Configurations
  * Agent Instructions and Prompts
  * Application Variables
  * Conversation History



## Specify a region using the API

To use regionalization you must specify a region for every API request.

Required fields:

  * Provide the region ID for the `location` URL path or resource parameter.



## Cloud Logging

See the [Cloud Logging documentation](https://docs.cloud.google.com/logging/docs) to control the region where your logs are stored.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
