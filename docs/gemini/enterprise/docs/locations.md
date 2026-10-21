---
url: https://docs.cloud.google.com/gemini/enterprise/docs/locations/
title: Data residency for Gemini Enterprise Standard and Plus Editions and Gemini Notebook Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:16:08.340193+00:00
---

# Data residency for Gemini Enterprise Standard and Plus Editions and Gemini Notebook Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/locations/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Resources ](https://docs.cloud.google.com/gemini/enterprise/docs/resources)



Send feedback 

#  Data residency for Gemini Enterprise Standard and Plus Editions and Gemini Notebook Enterprise Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the locations where Gemini Enterprise and Gemini Notebook Enterprise are available, along with their data residency commitments for at-rest storage (at-rest DRZ) and artificial intelligence (AI) or machine learning processing (MLP).

Gemini Enterprise and Gemini Notebook Enterprise support **at-rest DRZ** in the multi-regions and in-country regions listed on this page, subject to limitations.

If you don't have security, or regulatory reasons to locate your customer data in the `us` or `eu` multi-regions or the in-country regions with respect to at-rest DRZ or MLP, Google recommends that you choose the `global` location. This is because the `global` location provides better end-user response times, the latest model versions, and the most up-to-date features. See Limitations for multi-regions and in-country regions.

## Multi-regions

The following tables list the multi-regions where Gemini Enterprise and Gemini Notebook Enterprise are available.

### Gemini Enterprise multi-regions

The following table lists the multi-regions where Gemini Enterprise is available.

Multi-region description | Multi-region name  
---|---  
API availability in the European Union | `eu`  
API availability in the United States | `us`  
  
For Gemini Enterprise, MLP, such as training, prediction, and model tuning, occurs within the `us` multi-region when requests are made to regionally-available APIs in the US, or within the `eu` multi-region when requests are made to regionally-available APIs in Europe, subject to the limitations outlined below.

### Gemini Notebook Enterprise multi-regions

The following table lists the multi-regions where Gemini Notebook Enterprise is available.

Multi-region description | Multi-region name  
---|---  
API availability in the European Union | `eu`  
API availability in the United States | `us`  
  
For more information on the limitations, see Limitations for multi-regions and in-country regions.

## In-country regions

Using these locations is in GA with allowlist. To get access to these locations for use with Gemini Enterprise or Gemini Notebook Enterprise, contact your Google account team.

The following table lists the in-country regions and multi-regions where Gemini Enterprise and Gemini Notebook Enterprise are available.

In-country description | In-country name  
---|---  
API availability in Canada | `ca`  
API availability in India | `in`  
API availability in Japan | `asia-northeast1`  
API availability in Singapore | `sg`  
API availability in the United Kingdom | `europe-west2`  
  
These locations provide at-rest DRZ within the specified location. These in-country locations may be more constrained and have limitations similar to the `us` and `eu` multi-regions.

## Specify a multi-region for your data store

To confine your Customer Data to at-rest DRZ in the `us` or `eu` multi-region, follow these steps:

  1. If you create the data store through the Google Cloud console, then choose **us (multiple regions in the United States)** or **eu (multiple regions in the European Union)** when you pick your app location.

For more information, see [Create an app](https://docs.cloud.google.com/gemini/enterprise/docs/create-app).

  2. For API calls, replace `global-discoveryengine` or `discoveryengine` with `eu-discoveryengine` or `us-discoveryengine`, and replace `global` with `eu` or `us`. The following table shows examples of the API paths:

EU multi-region  
---  
           
         https://**eu-** discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/**eu** /…  
  
US multi-region  
           
         https://**us-** discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/**us** /…  
  
Global multi-region (Two equivalent endpoints)  
With the `global` endpoint prefix:  
           
         https://**global-** discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/**global** /…  
  
Without the `global` endpoint prefix:  
           
         https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/**global** /…  
  
  3. For Gemini Notebook Enterprise, ensure the user is licensed and is using a notebook in the selected region.

  4. Review the limitations associated with using a specific multi-region.




## Limitations for multi-regions and in-country regions

The following features of Gemini Enterprise that are supported globally may have limitations for certain multi-regions and in-country regions:

### Gemini Enterprise limitations

Feature | US/EU multi-regions | In-country regions (CA, IN, JP, SG, UK) | Notes  
---|---|---|---  
**Gemini Enterprise base functionality** | 

  * At-rest DRZ and MLP supported.

| 

  * Status - GA with allowlist.
  * At-rest DRZ and MLP supported.

|  Includes access-controlled data, blended search, Workspace search, people search, core search infrastructure, Assistant, answer generation, ingested and federated connectors, document understanding, analytics, frontend, Canvas, Agent Registry, Workflow Builder, custom Agents and Agent Engine Platform.  
**Gemini 4 Argon** | 

  * At-rest DRZ and MLP supported.

| 

  * Only available in the `global` region.

|  Gemini 4 Argon is turned off by default in the Gemini Enterprise app. Beginning October 27, 2026, the model toggle defaults to on. For AI developer tools, Gemini 4 Argon is enabled by default for licensed users when default model selection is active. If a custom model list is configured, an administrator must manually select Gemini 4 Argon.  To manage availability, administrators can use the **Gemini 4 Argon** toggle in the Gemini Enterprise app or configure access under **Antigravity authorized models**. For more information, see [Manage features on the web app](https://docs.cloud.google.com/gemini/enterprise/docs/manage-web-app-features) and [Configure AI developer tools settings](https://docs.cloud.google.com/gemini/enterprise/docs/ai-developer-tools-settings).  CA, IN, JP, SG, and UK regions don't offer the Gemini 4 Argon model. For unsupported in-country regions, you must confirm the warning dialog to route traffic to the `global` endpoint.   
**Gemini 3.1 Pro** | 

  * At-rest DRZ and MLP supported in: `US`.
  * At-rest DRZ not supported in: `EU`.
  * MLP not supported in: `EU`.

| 

  * At-rest DRZ not supported.
  * MLP not supported.

|  Gemini 3.1 Pro in Gemini Enterprise is in Limited Availability. For AI developer tools, Gemini 3.1 Pro (Preview) is enabled by default for licensed users when default model selection is active. If a custom model list is configured, an administrator must manually select Gemini 3.1 Pro.  To manage availability, administrators can use the **Gemini 3.1 Pro** toggle in the Gemini Enterprise app or configure access under **Antigravity authorized models**. For more information, see [Manage features on the web app](https://docs.cloud.google.com/gemini/enterprise/docs/manage-web-app-features), [Limited availability of Gemini 3.1 Pro](https://docs.cloud.google.com/gemini/enterprise/docs/known-limitations#using-gemini-3-preview), and [Configure AI developer tools settings](https://docs.cloud.google.com/gemini/enterprise/docs/ai-developer-tools-settings).   
**Gemini 3.8 Flash** | 

  * At-rest DRZ and MLP supported.

| 

  * **SG, UK:** At-rest DRZ and MLP supported.

|  Gemini 3.8 Flash is enabled by default in the `global`, `us`, and `eu` regions and in the SG and UK in-country regions. Administrators can turn on or turn off the **Gemini 3.8 Flash** toggle in the Gemini Enterprise app. For more information, see [Manage features on the web app](https://docs.cloud.google.com/gemini/enterprise/docs/manage-web-app-features) and [Configure AI developer tools settings](https://docs.cloud.google.com/gemini/enterprise/docs/ai-developer-tools-settings).  CA, IN, and JP regions don't offer the 3.8 Flash model. For unsupported in-country regions, you must confirm the warning dialog to route traffic to the `global` endpoint.   
**Anthropic model - Claude Opus 5.5** | 

  * At-rest DRZ and MLP supported.

| 

  * Not available.

|  In the Gemini Enterprise app, Claude Opus 5.5 is supported in the `global`, `us`, and `eu` regions. To make Claude Opus 5.5 available to users in the Gemini Enterprise app, administrators must turn on the **Claude Opus 5.5** toggle in the **Enable third-party models** section. For more information, see [Enable third-party models](https://docs.cloud.google.com/gemini/enterprise/docs/manage-web-app-features#enable-third-party-models).  To see the list of countries and regions that the model is supported in, see [Supported countries and regions](https://www.anthropic.com/supported-countries) in the Anthropic documentation.  For model details, see the [Claude Opus 5.5](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/claude/opus-5-5) model card.   
**Anthropic model - Claude Sonnet 5.5** | 

  * At-rest DRZ and MLP supported.

| 

  * Not available.

|  In the Gemini Enterprise app, Claude Sonnet 5.5 is supported in the `global`, `us`, and `eu` regions. To make Claude Sonnet 5.5 available to users in the Gemini Enterprise app, administrators must turn on the **Claude Sonnet 5.5** toggle in the **Enable third-party models** section. For more information, see [Enable third-party models](https://docs.cloud.google.com/gemini/enterprise/docs/manage-web-app-features#enable-third-party-models).  To see the list of countries and regions that the model is supported in, see [Supported countries and regions](https://www.anthropic.com/supported-countries) in the Anthropic documentation.  For model details, see the [Claude Sonnet 5.5](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/claude/sonnet-5-5) model card.   
**Gemini 3.7 Flash** | 

  * At-rest DRZ and MLP supported.

| 

  * Only available in the `global` region.

|  Gemini 3.7 Flash is turned off by default in the Gemini Enterprise app. For AI developer tools, Gemini 3.7 Flash is enabled by default for licensed users when default model selection is active. If a custom model list is configured, an administrator must manually select Gemini 3.7 Flash.  To manage availability, administrators can use the **Gemini 3.7 Flash** toggle in the Gemini Enterprise app or configure access under **Antigravity authorized models**. For more information, see [Manage features on the web app](https://docs.cloud.google.com/gemini/enterprise/docs/manage-web-app-features) and [Configure AI developer tools settings](https://docs.cloud.google.com/gemini/enterprise/docs/ai-developer-tools-settings).  For unsupported in-country regions, you must confirm the warning dialog to route traffic to the `global` endpoint.   
**Gemini 3.6 Flash** | 

  * At-rest DRZ and MLP supported.

| 

  * Only available in the `global` region.

|  Gemini 3.6 Flash is turned off by default in the Gemini Enterprise app. For AI developer tools, Gemini 3.6 Flash is enabled by default for licensed users when default model selection is active. If a custom model list is configured, an administrator must manually select Gemini 3.6 Flash.  To manage availability, administrators can use the **Gemini 3.6 Flash** toggle in the Gemini Enterprise app or configure access under **Antigravity authorized models**. For more information, see [Manage features on the web app](https://docs.cloud.google.com/gemini/enterprise/docs/manage-web-app-features) and [Configure AI developer tools settings](https://docs.cloud.google.com/gemini/enterprise/docs/ai-developer-tools-settings).  For unsupported in-country regions, you must confirm the warning dialog to route traffic to the `global` endpoint.   
**Gemini 3.5 Flash** | 

  * At-rest DRZ and MLP supported.

| 

  * At-rest DRZ and MLP supported.

|   
**Gemini 2.5 Pro** | 

  * At-rest DRZ and MLP supported.

| 

  * At-rest DRZ not supported.
  * MLP not supported.

|  In-country regions (CA, JP, IN, SG, UK) don't offer the 2.5 Pro model.  Gemini 2.5 Pro is turned on by default in the `global`, `us`, and `eu` regions. Administrators can turn off the **Gemini 2.5 Pro** toggle to make the model unavailable to users in the Gemini Enterprise app. For more information, see [Manage features on the web app](https://docs.cloud.google.com/gemini/enterprise/docs/manage-web-app-features).  For unsupported in-country regions, you must confirm the warning dialog to route traffic to the `global` endpoint.   
**Model Armor** | 

  * At-rest DRZ and MLP supported.

| 

  * At-rest DRZ supported.
  * MLP supported.

| Model Armor is also not available in the global region. Previously created Model Armor templates in CA, IN, JP, SG, and UK continue to call out-of-region to avoid breaking changes for customers.   
**CMEK** | 

  * At-rest DRZ and MLP supported.

| 

  * At-rest DRZ and MLP supported.

|  CMEK is also not available in the global region. For more information, see [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/gemini/enterprise/docs/cmek). To use this security feature, you must choose either the US multi-region or the EU multi-region.   
**Autocomplete** | 

  * At-rest DRZ and MLP supported, but tail match suggestions and advanced document data mode features can't be used.

| 

  * At-rest DRZ and MLP supported, but tail match suggestions and advanced document data mode features can't be used.

|  Tail match suggestions and advanced document data mode are only available in `global`. For more information, see [Configure autocomplete](https://docs.cloud.google.com/gemini/enterprise/docs/configure-autocomplete).   
**Dynamic facets** | 

  * Only available in the `global` region.

| 

  * Only available in the `global` region.

|  Even if a field is set to **Dynamic Facetable** , Gemini Enterprise doesn't generate dynamic facets in these locations.   
**Grounding with Google Search** | 

  * Only available in the `global` region.

| 

  * Only available in the `global` region.

|  The Grounding with Google Search feature has several additional limitations, which are described further in the Grounding with Google Search Service [Specific Terms](https://cloud.google.com/terms/service-terms) and in the [Gemini Enterprise Agent Platform product documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/grounding/grounding-with-google-search) pages. Notably, Grounding with Google Search temporarily logs certain pieces of Customer Data as part of providing this feature.   
**Web Grounding for Enterprise** | 

  * At-rest DRZ supported.
  * MLP supported.

| 

  * At-rest DRZ not supported.
  * MLP not supported.

| Grounding features are turned on by default for US/EU.  
**Gemini 3.1 Flash image (Nano Banana 2)** | 

  * At-rest DRZ and MLP supported.

| 

  * Only available in the `global` region.

|  To make Gemini 3.1 Flash image available to users in the Gemini Enterprise app, administrators must turn on the **Gemini 3.1 Flash image** toggle. For more information, see [Manage features on the web app](https://docs.cloud.google.com/gemini/enterprise/docs/manage-web-app-features).   
**Gemini 3 Pro image (Nano Banana Pro)** | 

  * Only available in the `global` region.

| 

  * Only available in the `global` region.

|  To make Gemini 3 Pro image available to users in the Gemini Enterprise app, administrators must turn on the **Gemini 3 Pro image** toggle. For more information, see [Manage features on the web app](https://docs.cloud.google.com/gemini/enterprise/docs/manage-web-app-features).  For unsupported in-country, US, and EU regions, you must confirm the warning dialog to route traffic to the `global` endpoint.   
**Gemini 2.5 Flash image** | 

  * At-rest DRZ and MLP supported.

| 

  * At-rest DRZ not supported.
  * MLP not supported.

|  The system defaults to this model if an administrator doesn't select an image model.   
**Video generation** | 

  * Only available in the `global` region.

| 

  * Only available in the `global` region.

|   
**AI developer tools** | 

  * Follows the data residency (at-rest DRZ) and machine learning processing (MLP) commitments of the selected model. For details, see the model's entry in this table. 

| 

  * At-rest DRZ not supported.
  * MLP not supported.

|  Includes Antigravity app, Antigravity CLI, Antigravity for IDEs, and Android Studio. If a model isn't available in your region, select a supported model or region listed in this table.  AI developer tools also support third-party models: **Anthropic models - Claude Opus 5.5 and Claude Sonnet 5.5**. Inference is available in the `global`, `us`, and `eu` locations (in-country regions aren't supported). Third-party models are turned off by default and require administrator opt-in. For more information, see [Configure AI developer tools settings](https://docs.cloud.google.com/gemini/enterprise/docs/ai-developer-tools-settings#enable-third-party-models).   
  
### Gemini Notebook Enterprise limitations

The following features of Gemini Notebook Enterprise are supported globally but may have limitations for certain multi-regions and in-country regions:

**Note:** Machine learning processing (MLP) is supported for base functionality in the US and EU multi-regions. It is not supported for other features or in in-country regions.Feature | US/EU multi-regions | In-country regions (CA, IN, JP, SG, UK) | Notes  
---|---|---|---  
**Base functionality** | 

  * At-rest DRZ supported.
  * MLP supported.

| 

  * At-rest DRZ supported.
  * MLP supported.

|  Includes adding sources to generate embeddings and interacting with them to query, chat, or generate summaries.   
**Gemini Notebook Content Studio** | 

  * At-rest DRZ supported.
  * MLP not supported.

| 

  * Not available.
  * MLP not supported.

|  Content Studio includes audio overviews, slide decks, infographics, and video overviews.   
**Discover Sources** | 

  * At-rest DRZ not supported.
  * MLP not supported.

| 

  * At-rest DRZ not supported.
  * MLP not supported.

|  Discover Sources is powered by Grounding with Google Search. The Grounding with Google Search feature has several additional limitations, which are described further in the Grounding with Google Search Service [Specific Terms](https://cloud.google.com/terms/service-terms) and in the [Gemini Enterprise Agent Platform product documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/grounding/grounding-with-google-search) pages. Notably, Grounding with Google Search temporarily logs certain pieces of customer data as part of providing this feature.   
  
### Agent Runtime limitations

The following features of Agent Runtime are supported globally but may have limitations for certain multi-regions and in-country regions:

Feature | US/EU multi-regions | In-country regions (CA, IN, JP, SG, UK)  
---|---|---  
**Memory Bank and Sessions** | 

  * At-rest DRZ supported.

| 

  * At-rest DRZ supported.

  
**Runtime** | 

  * At-rest DRZ supported.

| 

  * At-rest DRZ supported.

  
**Code execution** | 

  * At-rest DRZ supported in **US**.
  * At-rest DRZ not supported in **EU**.

| 

  * At-rest DRZ not supported.

  
  
### AlphaEvolve limitations

AlphaEvolve features are supported globally but may have limitations for certain multi-regions and in-country regions.

Feature | US/EU multi-regions | In-country regions (CA, IN, JP, SG, UK)  
---|---|---  
**Base functionality (with Gemini 4 Argon)** | At-rest DRZ supported. | At-rest DRZ not supported.  
MLP supported. | MLP not supported.  
**Base functionality (with Gemini 3.8 Flash)** | At-rest DRZ supported. | At-rest DRZ not supported.  
MLP supported. | MLP not supported.  
**Base functionality (with Gemini 3.7 Flash)** | At-rest DRZ supported. | At-rest DRZ not supported.  
MLP supported. | MLP not supported.  
**Base functionality (with Gemini 3.5 Flash)** | At-rest DRZ supported. | At-rest DRZ not supported.  
MLP supported. | MLP not supported.  
**Base functionality (with Gemini 3.1 Pro)** | At-rest DRZ supported. | At-rest DRZ not supported.  
MLP not supported. | MLP not supported.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
