---
url: https://docs.cloud.google.com/model-armor/release-notes/
title: Model Armor release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:39:28.719483+00:00
---

# Model Armor release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/model-armor/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Model Armor ](https://docs.cloud.google.com/model-armor)
  * [ Resources ](https://docs.cloud.google.com/model-armor/resources)



Send feedback 

#  Model Armor release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page contains release notes for features and updates to Model Armor. You can periodically check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/modelarmor-release-notes.xml) directly. 

## October 21, 2026

Feature

You can use custom organization policies to ensure that all new or updated Model Armor `Template` resources enforce required filters, like responsible AI or prompt injection and jailbreak detection. This feature is generally available ([GA](https://cloud.google.com/products#product-launch-stages)). For more information, see [Use custom organization policies](https://docs.cloud.google.com/model-armor/access-control/custom-constraints).

## October 09, 2026

Feature

Model Armor includes enhanced prompt injection and jailbreak protection for Workspace data. This capability improves detection accuracy and minimizes false positives when screening Workspace content, such as emails, documents, and files.

This capability is available on multi-region endpoints in the US (`us`) and EU (`eu`) for templates and floor setting configured with [filter version](https://docs.cloud.google.com/model-armor/set-filter-version) `v3` or later, including the `Stable` and `Latest` aliases.

## September 28, 2026

Feature

Template-specific exclusion rules are available in [Preview](https://cloud.google.com/products#product-launch-stages). This feature lets you configure dictionary (word and phrase lists) and regular expression rules to mitigate false-positive detections for prompt injection and jailbreak detection and responsible AI filters.

For more information, see [Configure template-specific exclusion rules](https://docs.cloud.google.com/model-armor/configure-exclusion-rules).

## September 24, 2026

Feature

You can use the following filters in Melbourne (`australia-southeast2`) with [data residency enforcement enabled](https://docs.cloud.google.com/model-armor/manage-templates#set-data-residency-compliance):

  * Prompt injection and jailbreak detection
  * Responsible AI



For information about available Model Armor features for each region, see [Supported features by region](https://docs.cloud.google.com/model-armor/feature-availability-by-region#supported-by-region).

## September 18, 2026

Feature

Filter version `v4` is available and set as the default for the `Latest` alias. Filter version `v3` is promoted to the `Stable` alias in all supported regions except the following:

  * In `asia-northeast3`, `v1` remains the `Stable` version.
  * In `australia-southeast2`, `v3` becomes the `Stable` version on September 25, 2026.



If your templates use the `Stable` alias, they automatically upgrade to `v3` when `v3` becomes `Stable` in that region.

Filter versions `v1` (except in `asia-northeast3`, and starting September 25, 2026 in `australia-southeast2`) and `v2` transition to `Legacy` status and retire on December 17, 2026. If your templates are explicitly configured with `v1` or `v2` in regions where those versions are in `Legacy` status, you must migrate them to `v3` or the `Stable` alias before December 17, 2026.

For more information, see [Version release timeline](https://docs.cloud.google.com/model-armor/set-filter-version#release-timeline) and [Model Armor filter version history](https://docs.cloud.google.com/model-armor/version-history#release-history).

## September 04, 2026

Feature

**Clarification: August 5, 2026 release note for Melbourne and Seoul**

In Melbourne (`australia-southeast2`) and Seoul (`asia-northeast3`), only the Sensitive Data Protection filter is supported when data residency is enforced. To use other Model Armor features in these regions, [disable data residency enforcement in the template](https://docs.cloud.google.com/model-armor/manage-templates#set-data-residency-compliance).

For information about available Model Armor features for each region, see [Supported features by region](https://docs.cloud.google.com/model-armor/feature-availability-by-region#supported-by-region).

## September 02, 2026

Feature

Filter version `v3` will be promoted to the `Stable` alias on or before September 25, 2026. On the same date, filter versions `v1` and `v2` transition to `Legacy` status and retire on November 29, 2026.

If your templates use the `Stable` alias, they will automatically upgrade to `v3` when it is promoted. If your templates use explicit version numbers (`v1` or `v2`), migrate them to `v3` or the `Stable` alias before November 29, 2026.

For more information, see [Set the filter version for a template](https://docs.cloud.google.com/model-armor/set-filter-version#release-timeline).

## August 27, 2026

Feature

You can disable data residency enforcement for in-use and in-transit data in Model Armor templates. Disabling data residency enforcement allows cross-jurisdictional routing to enable Model Armor features that are otherwise unavailable in [limited-support regions](https://docs.cloud.google.com/model-armor/feature-availability-by-region#limited-support). Data at rest remains compliant with data residency requirements.

For more information, see [Set data residency compliance](https://docs.cloud.google.com/model-armor/manage-templates#set-data-residency-compliance) and [Data residency and endpoints](https://docs.cloud.google.com/model-armor/data-residency).

## August 25, 2026

Feature

Model Armor supports screening prompts and responses up to 65,536 tokens (262,144 characters) for prompt injection and jailbreak detection, responsible AI, and child sexual abuse material (CSAM) filters. Model Armor scans only the first 256 URLs found in prompts and responses.

For more information, see [Token system limits](https://docs.cloud.google.com/model-armor/quotas#token-limits).

## August 05, 2026

Feature

Model Armor supports data residency compliance for in-use and in-transit data in the following regions:

  * Melbourne (`australia-southeast2`)
  * Seoul (`asia-northeast3`)



To maintain data residency compliance, these regions have [limited feature support](https://docs.cloud.google.com/model-armor/feature-availability-by-region#limited-support). For more information about data residency enforcement in Model Armor, see [Data residency and endpoints](https://docs.cloud.google.com/model-armor/data-residency).

For information about available Model Armor features for each region when using templates, see [Supported features by region](https://docs.cloud.google.com/model-armor/feature-availability-by-region#supported-by-region).

A clarification for this release note is provided in the September 4, 2026 release note.

## August 03, 2026

Feature

Filter version `v3` will be promoted to the `Stable` alias on August 31, 2026. On the same date, filter versions `v1` and `v2` transition to `Legacy` status and retire on November 29, 2026.

If your templates use the `Stable` alias, they automatically upgrade to `v3` on August 31, 2026. If your templates use explicit version numbers (`v1` or `v2`), migrate them to `v3` or `Stable` before November 29, 2026. For more information, see [Set the filter version for a template](https://docs.cloud.google.com/model-armor/set-filter-version#release-timeline).

## July 20, 2026

Feature

The responsible AI safety filter for the hate speech, harassment, sexually explicit, and dangerous content categories has been upgraded to improve detection accuracy and reduce the rate of false positives.

## July 10, 2026

Feature

Streaming sanitization for text is generally available ([GA](https://cloud.google.com/products#product-launch-stages)). For more information, see [Sanitize streaming text prompts](https://docs.cloud.google.com/model-armor/sanitize-prompts-responses#sanitize-streaming).

## July 08, 2026

Feature

Model Armor supports data residency in-use and in-transit compliance in Japan (`asia-northeast1`) and the United Kingdom (`europe-west2`). These regions have [limited feature support](https://docs.cloud.google.com/model-armor/feature-availability-by-region#limited-support). For more information, see [Data residency](https://docs.cloud.google.com/model-armor/data-residency).

## July 01, 2026

Feature

You can select the modality (text, images, or both) when [creating a Model Armor template](https://docs.cloud.google.com/model-armor/manage-templates#create-ma-template) in the Google Cloud console. Image modality is supported in the `us` and `eu` multi-regions. This feature is in [Preview](https://cloud.google.com/products#product-launch-stages). For more information, see [Image screening](https://docs.cloud.google.com/model-armor/overview#image-screening).

## June 25, 2026

Feature

Model Armor supports screening images within prompts and responses. This feature extends Model Armor's protection capabilities to multimodal inputs, helping you detect and mitigate risks associated with image content in your AI applications. This feature is in [Preview](https://cloud.google.com/products#product-launch-stages). For more information, see [Image screening](https://docs.cloud.google.com/model-armor/overview#image-screening).

## June 24, 2026

Feature

You can enable Model Armor on an Agent Gateway resource to apply your organization's content security guardrails to prompts and responses that pass through the gateway. This feature is generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

For more information, see [Integrate Model Armor with Agent Gateway](https://docs.cloud.google.com/model-armor/model-armor-agent-gateway-integration).

## June 22, 2026

Feature

Model Armor supports data residency in-use compliance in Singapore (`asia-southeast1`). This region has [limited feature support](https://docs.cloud.google.com/model-armor/feature-availability-by-region#limited-support). Filter version `v3` under the `Latest` alias is available in `asia-southeast1` and it includes an updated prompt injection and jailbreak detection filter to improve accuracy and reduce false positives. For more information, see [Data residency](https://docs.cloud.google.com/model-armor/data-residency).

## June 16, 2026

Feature

Filter version `v3` under the `Latest` alias is available in `asia-south1` and `northamerica-northeast2`. This version includes an updated prompt injection and jailbreak detection filter to improve accuracy and reduce false positives.

## June 08, 2026

Feature

Model Armor supports data residency in-use compliance in Mumbai (`asia-south1`) and Toronto (`northamerica-northeast2`). This compliance lets you meet regional data locality requirements when using Model Armor in these regions. For more information, see [Data residency](https://docs.cloud.google.com/model-armor/data-residency).

## May 25, 2026

Feature

Model Armor supports multiple filter versions, allowing you to choose the version that best suits your needs for stability and access to the latest features. You can configure versions within your templates using version numbers or aliases such as `Latest`, `Stable`, and `Legacy`. For more information, see [Set the filter version for a template](https://docs.cloud.google.com/model-armor/set-filter-version).

A new filter version, `v3`, is available under the `Latest` alias. `v3` features an updated prompt injection and jailbreak detection filter. This new model has been trained to:

  * Significantly reduce false positives.
  * Provide improved detection and mitigation against various attack vectors.



## May 12, 2026

Feature

Model Armor supports streaming sanitization for text. You can process user prompts and model responses more efficiently for large inputs and low-latency scenarios by sending text to the Model Armor API as a stream of chunks. This feature is in [Preview](https://cloud.google.com/products#product-launch-stages). For more information, see [Sanitize streaming text prompts](https://docs.cloud.google.com/model-armor/sanitize-prompts-responses#sanitize-streaming).

## April 22, 2026

Feature

Model Armor is available in Gemini Enterprise Agent Platform and integrates with Agent Gateway to provide enhanced security and governance for your AI agent interactions. This integration lets you enforce Model Armor's AI safety and security policies directly on gateway traffic.

To screen AI agents for content security risks and block violations, [configure Model Armor on the gateways that govern your agents](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/configure-model-armor). You can then do the following:

  * [Monitor content security insights](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/monitor-content-security) from Model Armor on the Agent Platform **Security** page in the Google Cloud console.
  * [View Model Armor trace spans](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/view-model-armor-spans).



This feature is in [Preview](https://cloud.google.com/products#product-launch-stages). For more information, see [Integrate with Agent Gateway](https://docs.cloud.google.com/model-armor/model-armor-agent-gateway-integration).

Feature

[Model Armor integration with Google and Google Cloud MCP servers](https://docs.cloud.google.com/model-armor/model-armor-mcp-google-cloud-integration) is in [General Availability](https://cloud.google.com/products#product-launch-stages).

## April 10, 2026

Change

The level of detail provided in the `virusDetails` field of the Antivirus filter scan results has been updated. To enhance security and align with data handling policies, responses no longer include specific names of security vendors or threat signatures. Instead, generalized placeholders are used when a threat is detected. This change does not affect the efficacy of the Antivirus filter's detection capabilities.

## April 06, 2026

Change

Model Armor is [FedRAMP High](https://cloud.google.com/security/compliance/fedramp) compliant.

Feature

Model Armor can sanitize data passed in as rich documents that have specific metadata labels. To use this feature, [create a custom metadata label infoType](https://docs.cloud.google.com/sensitive-data-protection/docs/create-custom-infotypes-metadata-labels) in Sensitive Data Protection. Use the custom infoType in an [advanced Sensitive Data Protection configuration](https://docs.cloud.google.com/model-armor/sanitize-prompts-responses#advanced_sdp_configuration) in your Model Armor template.

## March 31, 2026

Change

[Prompt injection and jailbreak detection](https://docs.cloud.google.com/model-armor/overview#ma-prompt-injection) was improved to reduce the rate of false positives and false negatives.

## March 27, 2026

Change

Model Armor is available in the following regions:

  * `asia-northeast1` (Japan)
  * `asia-northeast3` (South Korea)
  * `europe-southwest1` (Madrid)
  * `europe-west9` (Paris)
  * `northamerica-northeast2` (Canada)



For more information, see [Locations](https://docs.cloud.google.com/model-armor/locations).

## March 26, 2026

Change

The [malicious URL detection](https://docs.cloud.google.com/model-armor/overview#ma-malicious-url-detection) and [responsible AI safety](https://docs.cloud.google.com/model-armor/overview#ma-responsible-ai-safety-categories) filters are fixed to improve detection accuracy and reduce the rate of false positives.

## March 06, 2026

Change

Model Armor is available in the `australia-southeast2` (Melbourne) region. For more information, see [Model Armor Locations](https://docs.cloud.google.com/model-armor/locations).

## March 05, 2026

Change

For non-English requests, the translation process was enhanced to improve service availability and processing efficiency.

## February 27, 2026

Change

The behavior of multi-language detection for text prompts and model responses has changed.

Previously, if you [specified the source language in your sanitization request](https://docs.cloud.google.com/model-armor/sanitize-prompts-responses#sanitize-prompts-multi-lang), Model Armor compared the specified language with the automatically detected language. If the specified and detected languages differed, Model Armor skipped the request.

With this change, if you specify the source language, Model Armor uses that language to evaluate the request. It no longer attempts to automatically detect the language.

## February 10, 2026

Change

The error messages returned by the Sensitive Data Protection detector have been modified to exclude internal details. If a transient or internal quota error occurs, you will receive the message: `Error occurred while processing sensitive data detection. Please try again`.

## January 30, 2026

Change

The [prompt injection and jailbreak detection](https://docs.cloud.google.com/model-armor/overview#ma-prompt-injection) filter for the Mumbai (`asia-south1`) and Singapore (`asia-southeast1`) regions is upgraded to improve detection accuracy and reduce the rate of false positives.

## December 15, 2025

Feature

You can [configure Model Armor floor settings](https://docs.cloud.google.com/model-armor/configure-floor-settings) for Google-managed Model Context Protocol (MCP) servers to define baseline safety and security filters. This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).

You can also [configure Cloud Logging for sanitization operations](https://docs.cloud.google.com/model-armor/configure-logging#configure-logging-floor-settings). The Model Armor floor settings perform these operations on traffic to and from Google-managed MCP servers and Gemini Enterprise Agent Platform models.

## December 10, 2025

Feature

You can configure Model Armor to enhance the security of your agentic AI applications that interact with Google Cloud Model Context Protocol (MCP) servers. This feature is in [Preview](https://cloud.google.com/products#product-launch-stages). For configuration details, see [Model Armor integration with Google Cloud MCP servers](https://docs.cloud.google.com/model-armor/model-armor-mcp-google-cloud-integration).

## December 04, 2025

Feature

[The monitoring dashboard](https://docs.cloud.google.com/model-armor/monitoring-dashboard) is available in [General Availability](https://cloud.google.com/products#product-launch-stages).

## December 03, 2025

Feature

[Model Armor integration with Gemini Enterprise Agent Platform](https://docs.cloud.google.com/model-armor/model-armor-vertex-integration) is available in [General Availability](https://cloud.google.com/products#product-launch-stages).

## November 10, 2025

Feature

Model Armor is available in the following regions:

  * `europe-west1` (Belgium)
  * `europe-west2` (London)
  * `europe-west3` (Frankfurt)
  * `asia-south1` (Mumbai)



For more information, see [Locations](https://docs.cloud.google.com/model-armor/locations).

## September 27, 2025

Feature

Model Armor limits the maximum input size for files and text to 4 MB, automatically skipping any content that exceeds this threshold.

## September 23, 2025

Feature

The upgraded model for the prompt injection and jailbreak detection filter is available in EU multi-region. This model has improved detection rates across several attack vectors, including the following:

  * Do Anything Now prompts
  * System instruction manipulation
  * Unauthorized action execution
  * Sensitive information retrieval



## September 16, 2025

Feature

Model Armor is integrated with Gemini Enterprise to provide greater insights and enhanced security of your agent interactions by default. This feature is available in [General Availability](https://cloud.google.com/products#product-launch-stages). For more information, see [Integration with Gemini Enterprise](https://docs.cloud.google.com/model-armor/model-armor-agentspace-integration).

## September 15, 2025

Feature

Model Armor integration with Google Kubernetes Engine is available in [General Availability](https://cloud.google.com/products#product-launch-stages).

## September 08, 2025

Feature

The Model Armor monitoring dashboard provides a centralized view to track interactions and violations within your projects. This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages). For more information, see [View the monitoring dashboard](https://docs.cloud.google.com/model-armor/monitoring-dashboard).

## July 29, 2025

Feature

Model Armor and Gemini Enterprise Agent Platform integration

Model Armor integrates with Gemini Enterprise Agent Platform, providing a default security configuration for all new prediction endpoints. This feature is in [Preview](https://cloud.google.com/products#product-launch-stages). For more information, see [Integration with Gemini Enterprise Agent Platform](https://docs.cloud.google.com/model-armor/model-armor-vertex-integration).

Feature

You can use Terraform to manage Model Armor floor settings and templates. This helps reduce manual overhead with Model Armor deployments. For more information, see [Terraform resources for Model Armor](https://docs.cloud.google.com/security-command-center/docs/terraform#resources).

Change

Model Armor supports the `asia-southeast1` location. For information about supported locations, see [Locations](https://docs.cloud.google.com/model-armor/locations).

## July 28, 2025

Feature

Model Armor filter updates

  * The prompt injection and jailbreak detection filter now supports 10,000 tokens.
  * For the Sensitive Data Protection filter, `SKIP_DETECTION` is returned if the prompt or response exceeds the token limit.
  * For all other filters, if the prompt or response exceeds the token limit, `MATCH_FOUND` is returned if malicious content is found, and `SKIP_DETECTION` is returned if no malicious content is found.



## June 19, 2025

Feature

The prompt injection and jailbreak detection filter in Model Armor flags more threats across various attack vectors, and offers an improved detection rate for high-confidence malicious prompts. This filter is available in `us-east1`.

## June 08, 2025

Feature

Model Armor supports screening text in the following document types for malicious content:

  * DOCX, DOCM, DOTX, DOTM documents
  * PPTX, PPTM, POTX, POT presentations
  * XLSX, XLSM, XLTX, XLTM spreadsheets
  * Multi-language support for Model Armor filters



Feature

The Responsible AI and prompt injection and jailbreak detection filters are tested in English, Spanish, French, Italian, Portuguese, German, Chinese (Mandarin), Japanese, and Korean. These filters can work in other languages, but the quality of results might vary. For more information, see [Languages supported](https://docs.cloud.google.com/model-armor/overview#languages-supported).

## May 28, 2025

Change

  * Model Armor supports multi-regional endpoints. For more information, see [Locations](https://docs.cloud.google.com/model-armor/locations).
  * All Model Armor filters support up to 2,000 tokens.



## April 09, 2025

Feature

Model Armor enforces security policies uniformly on generative AI inference traffic using a traffic extension. This applies to all application load balancers, including Google Kubernetes Engine Inference Gateway. This feature is in [Preview](https://cloud.google.com/products#product-launch-stages). For more information, see [Integration with Google Kubernetes Engine](https://docs.cloud.google.com/model-armor/model-armor-gke-integration).

## March 21, 2025

Change

The [prompt injection and jailbreak detection](https://docs.cloud.google.com/model-armor/overview#ma-prompt-injection) filter in Model Armor is upgraded with increased efficacy and higher model quality scores.

## February 03, 2025

Feature

Model Armor is a Google Cloud service that lets you to apply content safety and content security controls to LLM prompts and responses to mitigate risks such as sensitive data leakage, prompt injection, and offensive content. For more information, see [Overview](https://docs.cloud.google.com/model-armor/overview).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
