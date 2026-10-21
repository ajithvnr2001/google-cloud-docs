---
url: https://docs.cloud.google.com/model-armor/model-armor-apigee-integration/
title: Integrate Model Armor with Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:49:15.231424+00:00
---

# Integrate Model Armor with Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/model-armor/model-armor-apigee-integration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Model Armor ](https://docs.cloud.google.com/model-armor)
  * [ Guides ](https://docs.cloud.google.com/model-armor/overview)



Send feedback 

#  Integrate Model Armor with Apigee Stay organized with collections  Save and categorize content based on your preferences. 

You can enhance the security of your AI applications by integrating Model Armor with [Apigee](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee). By using Apigee as an API gateway in front of your AI applications, you can use the capabilities of Model Armor to screen and sanitize both the inputs sent to your application and the responses received.

## Overview

You can integrate Model Armor policies into your Apigee API proxies to provide enhanced control and protection for your AI applications. For example, you can use Apigee to enforce token-level quotas to limit a user or application to a maximum number of tokens per day. Use [`LLMTokenQuota`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/llm-token-quota-policy) and [`PromptTokenLimit`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/prompt-token-limit-policy) for precise control over token usage. These policies help manage costs, stop abuse, and stabilize traffic by preventing sudden spikes in consumption.

## Limitations

Consider the following limitations when integrating Model Armor with Apigee:

  * [Regional availability](https://docs.cloud.google.com/model-armor/data-residency#data-residency-enforced): Model Armor isn't available in all regions. Ensure that Apigee and Model Armor are configured in the same region. Although it is possible to configure Apigee and Model Armor in different regions, using different regions might introduce additional latency due to cross-region network traversal. For optimal performance, configure them in the exact same region.
  * [Quota](https://docs.cloud.google.com/model-armor/quotas): High volume traffic may require a quota increase for Model Armor. To request an adjustment, see [Request a quota adjustment](https://docs.cloud.google.com/docs/quotas/view-manage#requesting_higher_quota). If you need more than the default quota, contact [Cloud Customer Care](https://cloud.google.com/support-hub). For information on quotas related to Model Armor integrations with other services, see [Manage quota](https://docs.cloud.google.com/model-armor/integrations#manage-quota).
  * Token limits: Model Armor has [token limits](https://docs.cloud.google.com/model-armor/quotas#token_system_limits) for processing prompts and responses, which vary by filter. Content exceeding these limits might not be fully scanned.



## Before you begin

  * [Enable the Model Armor API](https://docs.cloud.google.com/model-armor/manage-templates#enable-apis) in your project.
  * [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project).
  * Confirm that you have an [Intermediate or Comprehensive environment](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/environments-overview#environment-types) available in your Apigee instance. You can deploy Model Armor policies in Intermediate and Comprehensive environments.
  * Confirm that you have an [active Apigee organization provisioned](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/provisioning-intro).
  * To create and use Model Armor policies with Apigee, you must have specific roles. For the required roles, see [Apigee roles](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee).

  * [Set the Model Armor regional endpoint](https://docs.cloud.google.com/model-armor/manage-templates#gcloud).

  * [Create a Model Armor template](https://docs.cloud.google.com/model-armor/manage-templates).




## How it works

The integration uses two main Apigee policies:

  * `SanitizeUserPrompt`: Add this policy to the request flow of your API proxy. It intercepts all incoming requests and sends them to Model Armor for inspection before they reach your AI application. For more information, see [`SanitizeUserPrompt` policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/sanitize-user-prompt-policy).
  * `SanitizeModelResponse`: Add this policy to the response flow. It intercepts the response from the AI application and sends it to Model Armor for inspection before sending the response to the client. For more information, see [`SanitizeModelResponse` policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/sanitize-llm-response-policy).



Model Armor evaluates the content against the rules defined in your active Model Armor template. Based on the findings and the [enforcement type](https://docs.cloud.google.com/model-armor/overview#define-enforcement-type) set, Apigee allows, blocks, or redacts the request or response. If the request or response is redacted, extract the redacted data using [flow variables](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/sanitize-user-prompt-policy#flowvariables) and pass it to the LLM.

To get started, use the built-in **Proxy with Model Armor** proxy template in the Apigee console. This template automatically adds optional `SanitizeUserPrompt` and `SanitizeModelResponse` configurations.

## Create an Apigee API proxy with Model Armor policies

  1. [Create a service account to deploy the API proxy](https://docs.cloud.google.com/apigee/docs/api-platform/tutorials/using-model-armor-policies#create-service-account).
  2. [Create an Apigee API proxy](https://docs.cloud.google.com/apigee/docs/api-platform/tutorials/using-model-armor-policies#create-an-apigee-api-proxy).
  3. [Edit the `SanitizeUserPrompt` and `SanitizeModelResponse` XML](https://docs.cloud.google.com/apigee/docs/api-platform/tutorials/using-model-armor-policies#edit-the-sanitizeuserprompt-and-sanitizemodelresponse-xml). You must edit the XML of these policies for Model Armor to work.
  4. [Add Google authentication to the API proxy](https://docs.cloud.google.com/apigee/docs/api-platform/tutorials/using-model-armor-policies#add-auth).
  5. [Deploy the API proxy](https://docs.cloud.google.com/apigee/docs/api-platform/tutorials/using-model-armor-policies#deploy-api-proxy).
  6. [Test the Model Armor policies](https://docs.cloud.google.com/apigee/docs/api-platform/tutorials/using-model-armor-policies#test-the-model-armor-policies).



For more details on configuration and usage, see [Get started with Apigee Model Armor policies](https://docs.cloud.google.com/apigee/docs/api-platform/tutorials/using-model-armor-policies).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
