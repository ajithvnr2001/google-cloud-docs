---
url: https://docs.cloud.google.com/model-armor/feature-availability-by-region/
title: Feature availability for templates by region \u00a0|\u00a0 Model Armor \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:55:56.139795+00:00
---

# Feature availability for templates by region  |  Model Armor  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/model-armor/feature-availability-by-region/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Model Armor ](https://docs.cloud.google.com/model-armor)
  * [ Guides ](https://docs.cloud.google.com/model-armor/overview)



Send feedback 

#  Feature availability for templates by region Stay organized with collections  Save and categorize content based on your preferences. 

Model Armor feature availability varies by region due to dependencies on services that could process data outside the location. As a result, some regions have limited feature support when you configure Model Armor using templates in order to maintain strict data residency. This page provides a breakdown of supported features across all available regions.

**Note:** For Model Armor configurations that use floor settings, all features are available, but data residency enforcement for data in use and in transit varies by region.

## Full-support regions

If you create a Model Armor template in a full-support region, you have access to all of the following filters. All underlying dependency services are available in the jurisdictional boundary.

  * [Prompt injection and jailbreak detection](https://docs.cloud.google.com/model-armor/overview#ma-prompt-injection)
  * [ Responsible AI](https://docs.cloud.google.com/model-armor/overview#ma-responsible-ai-safety-categories)
  * [ Sensitive Data Protection](https://docs.cloud.google.com/model-armor/overview#ma-sensitive-data-prot)
  * [ Malicious URL detection](https://docs.cloud.google.com/model-armor/overview#ma-malicious-url-detection)
  * Child sexual abuse material (CSAM) detection
  * [Multi-language detection](https://docs.cloud.google.com/model-armor/overview#languages-supported)
  * Antivirus scanning



The following table shows the locations with full feature support. The **Jurisdiction** column indicates the geographical boundary (for example, a country or a multi-region like `eu` or `us`) within which Model Armor ensures data residency compliance for the supported states (at rest, in use, and in transit) as indicated in the table.

The **Region/multi-region** column lists the specific Google Cloud region or multi-region identifier.

When data residency is enforced for a region in Model Armor, it helps ensure that data remains within a specified jurisdiction while in at least one of the following states:

  * **At rest** : Stored data remains within the specific Google Cloud region listed.

  * **In use** and **In transit** : Data residency enforcement for these states within the specified jurisdiction depends on the values in the **In use** and **In transit** columns:

    * **Yes** : Data residency is enforced for the _In use_ and _In transit_ states within the listed jurisdiction. This means that the data remains within the boundaries of the listed jurisdiction while being processed or transmitted (not necessarily within that single region).
    * **No** : Data residency is not enforced for the _In use_ and _In transit_ states within the listed jurisdiction. This means that the data might be processed or transmitted outside of the jurisdiction.

**Note:** For Assured Workloads, Model Armor maintains data residency within the selected jurisdiction for [supported locations](https://docs.cloud.google.com/model-armor/locations) for data in use. For more information, see [Assured Workloads Service Specific Terms](https://cloud.google.com/terms/service-terms#37).Region/multi-region | Jurisdiction | At rest | In use | In transit  
---|---|---|---|---  
`eu` |  [European Union](https://docs.cloud.google.com/assured-workloads/docs/control-packages/eu-data-boundary) | Yes | Yes | Yes  
`europe-southwest1` |  [European Union](https://docs.cloud.google.com/assured-workloads/docs/control-packages/eu-data-boundary) | Yes | Yes | Yes  
`europe-west1` |  [European Union](https://docs.cloud.google.com/assured-workloads/docs/control-packages/eu-data-boundary) | Yes | Yes | Yes  
`europe-west3` |  [European Union](https://docs.cloud.google.com/assured-workloads/docs/control-packages/eu-data-boundary) | Yes | Yes | Yes  
`europe-west4` |  [European Union](https://docs.cloud.google.com/assured-workloads/docs/control-packages/eu-data-boundary) | Yes | Yes | Yes  
`europe-west9` |  [European Union](https://docs.cloud.google.com/assured-workloads/docs/control-packages/eu-data-boundary) | Yes | Yes | Yes  
`us` |  [United States](https://docs.cloud.google.com/assured-workloads/docs/control-packages/us-data-boundary) | Yes | Yes | Yes  
`us-central1` |  [United States](https://docs.cloud.google.com/assured-workloads/docs/control-packages/us-data-boundary) | Yes | Yes | Yes  
`us-east1` |  [United States](https://docs.cloud.google.com/assured-workloads/docs/control-packages/us-data-boundary) | Yes | Yes | Yes  
`us-east4` |  [United States](https://docs.cloud.google.com/assured-workloads/docs/control-packages/us-data-boundary) | Yes | Yes | Yes  
`us-west1` |  [United States](https://docs.cloud.google.com/assured-workloads/docs/control-packages/us-data-boundary) | Yes | Yes | Yes  
  
For a list of features that are available for each region or multi-region, see Supported features by region in this document.

## Limited-support regions

By default, if you create a Model Armor template in a limited-support region and your template has [data residency compliance enabled](https://docs.cloud.google.com/model-armor/manage-templates#set-data-residency-compliance), some Model Armor features are unavailable because they rely on services that might process data outside the [jurisdiction of your chosen Model Armor region](https://docs.cloud.google.com/model-armor/data-residency#data-residency-enforced).

If you must use a limited-support region but you want to prioritize comprehensive security filtering over strict data residency, you can [disable data residency enforcement](https://docs.cloud.google.com/model-armor/manage-templates#set-data-residency-compliance) for in-use and in-transit data in your Model Armor template.

The following are the regions with limited feature support:

Region/multi-region | Jurisdiction | At rest | In use | In transit  
---|---|---|---|---  
`asia-northeast1` |  [Japan](https://docs.cloud.google.com/assured-workloads/docs/control-packages/japan-data-boundary) | Yes | Yes | Yes  
`asia-northeast3` |  [South Korea](https://docs.cloud.google.com/assured-workloads/docs/control-packages/south-korea-data-boundary) | Yes | Yes | Yes  
`asia-south1` |  [India](https://docs.cloud.google.com/assured-workloads/docs/control-packages/india-data-boundary) | Yes | Yes | Yes  
`asia-southeast1` |  [Singapore](https://docs.cloud.google.com/assured-workloads/docs/control-packages/singapore-data-boundary) | Yes | Yes | Yes  
`australia-southeast2` |  [Australia](https://docs.cloud.google.com/assured-workloads/docs/control-packages/australia-data-boundary) | Yes | Yes | Yes  
`europe-west2` |  [United Kingdom](https://docs.cloud.google.com/assured-workloads/docs/control-packages/uk-data-boundary) | Yes | Yes | Yes  
`northamerica-northeast2` |  [Canada](https://docs.cloud.google.com/assured-workloads/docs/control-packages/canada-data-boundary) | Yes | Yes | Yes  
  
For a list of features that are available for each region or multi-region, see Supported features by region in this document.

## Supported features by region

This section shows the regional capabilities and supported filters for each region or multi-region when you configure Model Armor using a template that has [data residency enforcement enabled](https://docs.cloud.google.com/model-armor/manage-templates#set-data-residency-compliance).

Region/multi-region | Supported filters | Multi-language detection | CSAM support | Image support | Antivirus scanning  
---|---|---|---|---|---  
`asia-northeast1` | 

  * Responsible AI
  * Sensitive Data Protection
  * Prompt injection and jailbreak

| No | No | No | No  
`asia-northeast3` | 

  * Sensitive Data Protection

| No | No | No | No  
`asia-south1` | 

  * Responsible AI
  * Sensitive Data Protection
  * Prompt injection and jailbreak

| No | No | No | No  
`asia-southeast1` | 

  * Responsible AI
  * Sensitive Data Protection
  * Prompt injection and jailbreak

| No | No | No | No  
`australia-southeast2` | 

  * Responsible AI
  * Sensitive Data Protection
  * Prompt injection and jailbreak

| No | No | No | No  
`eu` | 

  * Responsible AI
  * Sensitive Data Protection
  * Prompt injection and jailbreak
  * Malicious URL

| Yes | Yes | Yes | Yes  
`europe-southwest1` | 

  * Responsible AI
  * Sensitive Data Protection
  * Prompt injection and jailbreak
  * Malicious URL

| Yes | Yes | No | Yes  
`europe-west1` | 

  * Responsible AI
  * Sensitive Data Protection
  * Prompt injection and jailbreak
  * Malicious URL

| Yes | Yes | No | Yes  
`europe-west2` | 

  * Responsible AI
  * Sensitive Data Protection
  * Prompt injection and jailbreak

| No | No | No | No  
`europe-west3` | 

  * Responsible AI
  * Sensitive Data Protection
  * Prompt injection and jailbreak
  * Malicious URL

| Yes | Yes | No | Yes  
`europe-west4` | 

  * Responsible AI
  * Sensitive Data Protection
  * Prompt injection and jailbreak
  * Malicious URL

| Yes | Yes | No | Yes  
`europe-west9` | 

  * Responsible AI
  * Sensitive Data Protection
  * Prompt injection and jailbreak
  * Malicious URL

| Yes | Yes | No | Yes  
`northamerica-northeast2` | 

  * Responsible AI
  * Sensitive Data Protection
  * Prompt injection and jailbreak

| No | No | No | No  
`us` | 

  * Responsible AI
  * Sensitive Data Protection
  * Prompt injection and jailbreak
  * Malicious URL

| Yes | Yes | Yes | Yes  
`us-central1` | 

  * Responsible AI
  * Sensitive Data Protection
  * Prompt injection and jailbreak
  * Malicious URL

| Yes | Yes | No | Yes  
`us-east1` | 

  * Responsible AI
  * Sensitive Data Protection
  * Prompt injection and jailbreak
  * Malicious URL

| Yes | Yes | No | Yes  
`us-east4` | 

  * Responsible AI
  * Sensitive Data Protection
  * Prompt injection and jailbreak
  * Malicious URL

| Yes | Yes | No | Yes  
`us-east7` | 

  * Responsible AI
  * Sensitive Data Protection
  * Prompt injection and jailbreak
  * Malicious URL

| Yes | Yes | No | Yes  
`us-west1` | 

  * Responsible AI
  * Sensitive Data Protection
  * Prompt injection and jailbreak
  * Malicious URL

| Yes | Yes | No | Yes  
`global` | 

  * Responsible AI
  * Sensitive Data Protection
  * Prompt injection and jailbreak
  * Malicious URL

| Yes | Yes | Yes | Yes  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
