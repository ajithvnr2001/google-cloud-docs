---
url: https://docs.cloud.google.com/gemini/enterprise/docs/quotas-and-overages/
title: Quotas and overages \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:25:07.608783+00:00
---

# Quotas and overages  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/quotas-and-overages/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Resources ](https://docs.cloud.google.com/gemini/enterprise/docs/resources)



Send feedback 

#  Quotas and overages Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** The quotas and overages on this page don't apply to users who received the email with the subject line _[Billing Update] New Gemini Enterprise overage billing controls launching August 17, 2026_. If you received this email, see [Quotas and overages (Legacy)](https://docs.cloud.google.com/gemini/enterprise/docs/overages).

Your subscription entitles you to certain quotas across product features. If you have a pay-as-you-go subscription, there are no feature quota limits; you pay for what you use. For seat-based subscriptions, unlike other Google Cloud services, Gemini Enterprise feature quotas don't require manual increase requests; they're automatically adjusted based on the number of licenses or seats in your subscription, including free-trial subscriptions.

**Note:** Google Cloud products that use the Discovery Engine API, including Agent Search and Gemini Enterprise, share the technical rate and allocation quotas listed on this page. However, license-based feature quotas apply only to Gemini Enterprise and aren't shared with Agent Search.**Note:** As a Discovery Engine administrator, you can view pooled quota usage. For more information, see [View the pooled quota usage](https://docs.cloud.google.com/gemini/enterprise/docs/feature-usage#view-quota-usage).

## Feature and edition-based quotas

Except for storage and data indexing, feature quotas are pooled across users in the same edition within a project and location. Storage and data indexing quota is pooled per project and location across all users, but it is not segmented by the edition—all editions share a single storage and data indexing pool. For all other feature quotas, users with licenses for a specific edition share a single combined limit per project and location.

For detailed system limits, subagent depth constraints, file upload thresholds, and sharing member caps that apply to custom agents, see [Workflow Builder quotas and limits](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/quotas-and-limits).

#### Use case 1: Multiple editions in one project and location

If you have users with different editions in the same project and location, quota pools are maintained separately for each edition except for storage and data indexing:

  * **Standard feature quotas:** Quotas are pooled separately by edition in each project and location. For example, if a project and location has 100 Standard edition licenses and 50 Plus edition licenses, your Standard edition users share a pool of 16,000 Assistant queries per day (100 licenses × 160 queries), and your Plus edition users share a separate pool of 10,000 queries per day (50 licenses × 200 queries). These feature quota pools don't combine across editions.
  * **Storage and data indexing:** Quotas are pooled per project and location across all users, regardless of edition. For example, if a project and location has 100 Standard edition licenses (30 GiB per user) and 50 Plus edition licenses (75 GiB per user), there is a single combined storage pool of 6,750 GiB ((100 × 30 GiB) + (50 × 75 GiB)) shared by all users in that project and location across all editions.



#### Use case 2: Quota pooling within a single edition

Within an edition's quota pool, the following rules apply. For example, if you have 10 Standard edition licenses, your users share a total pooled quota of 1,600 queries per day (10 licenses × 160 queries):

  * The 10 Standard edition users share a combined pool of 1,600 queries for the day.
  * One power user can use 500 queries, leaving 1,100 queries for the remaining users in that edition.
  * Individual usage isn't capped at the per-user limit; all users in the edition draw from their edition's shared pool until it is depleted.



### Quota reset times

Pooled quotas reset on the following schedule:

Feature | Reset schedule  
---|---  
All features except AI developer tools | Daily at midnight Pacific Time (PT)  
[AI developer tools](https://docs.cloud.google.com/gemini/enterprise/docs/ai-developer-tools-overview) |  Every seven days, starting from when a prompt or request is first sent to an AI developer tool.   
  
For example, if a user in your project sends the first prompt using Antigravity on Wednesday at 2 PM Pacific Time (PT), the seven-day quota cycle starts at that time, and the AI developer tools quota resets the following Wednesday at 2 PM PT.   
  
### Quotas for Standard and Plus editions

**Note:** When your project reaches its pooled feature quota for Standard or Plus editions, you can enable overages to allow uninterrupted usage at pay-as-you-go rates.

For information about quotas across Gemini Enterprise Standard and Plus editions, see the following table:

| Gemini Enterprise Standard | Gemini Enterprise Plus  
---|---|---  
Quotas | Pooled or unpooled | Pooled across users within the edition per project and location | Pooled across users within the edition per project and location  
Product | Storage + data indexing | 30 GiB | 75 GiB  
Assistant | 160 queries per day | 200 queries per day  
No-code agent building tools - create4 | 1 agent per day | 10 agents per day  
No-Code agent building tools - use | Based on underlying agent actions4  
Video generation | 2 video generation requests per day | 3 video generation requests per day  
Image generation | 5 images per day | 10 images per day  
General purpose agents made by Google | Gemini Notebook - use | Gemini Notebook Enterprise limits1 | Gemini Notebook Enterprise limits1  
Gemini Notebook - create & publish | Gemini Notebook Enterprise limits1 | Gemini Notebook Enterprise limits1  
Deep Research | 3 per day | 10 per day  
AI developer tools2 |  Included Google Antigravity, Antigravity for IDEs, and Android Studio credits  |  $10 credit per user per month3 |  $15 credit per user per month3  
  
1 For information about Gemini Notebook Enterprise usage limits, see the [Gemini Notebook Enterprise documentation](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/overview#usage-limits).

2 AI developer tools are available only for [invoiced Cloud Billing accounts](https://docs.cloud.google.com/billing/docs/concepts#billing_account_types), including accounts with a free-trial subscription.

3 Although quotas are listed as a monthly per-user amount, Gemini Enterprise enforces them on a rolling seven-day basis as a shared pool. Gemini Enterprise calculates your project's weekly quota by dividing the monthly per-user value by four and multiplying it by your project's total licensed seats, including free-trial seats. Any user in your edition can draw from this shared weekly pool. Unused quota doesn't roll over to the next week.

4 Daily creation quotas apply to both creating custom agents in Workflow Builder and registering external or custom agents (such as A2A, ADK, or Dialogflow agents) in an app. Each registration in an engine or app consumes 1 creation quota unit. For detailed agent creation limits, registration quotas across multi-app architectures, subagent depth constraints, file upload thresholds, and sharing member caps, see [Workflow Builder quotas and limits](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/quotas-and-limits#creation-quotas).

### Quotas and pricing for the Pay-as-you-go edition

**Note:** To subscribe to the Gemini Enterprise Pay-as-you-go edition, your project must be linked to an [invoiced Cloud Billing account](https://docs.cloud.google.com/billing/docs/concepts#billing_account_types) that receives an active monthly invoice.

The Gemini Enterprise Pay-as-you-go edition has no feature quota limits, as you pay for what you use. To get started, you need to have an invoiced Cloud Billing account and purchase a subscription to the Pay-as-you-go edition. For more information, see [Cloud Billing account types](https://docs.cloud.google.com/billing/docs/concepts#billing_account_types) and [Get subscriptions and assign licenses](https://docs.cloud.google.com/gemini/enterprise/docs/licenses#about-subscriptions).

The following table lists the rates and pricing for this edition:

#### Pay-as-you-go charges for features

Prices are listed in US Dollars (USD). If you pay in a currency other than USD, the prices listed in your currency on [Cloud Platform SKUs](https://cloud.google.com/skus/) apply. Charges are subject to a variable support fee depending on the support service. For more information on the support services, see [Compare support services](https://docs.cloud.google.com/support/docs/overview#compare-support).

| Gemini Enterprise  
Pay-as-you-go charges  
---|---  
Foundational engagement layer | Storage + data indexing | $5 per GiB per month  
Assistant - Gemini models | [Agent Platform prices](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing#cost-of-building-and-deploying-ai-models-in-agent-platform)  
Assistant - Claude models | Claude pricing  
No-code agent building tools - create | n/a  
No-code agent building tools - use | [Agent Platform prices](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing#cost-of-building-and-deploying-ai-models-in-agent-platform)  
Video generation | [Agent Platform prices](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing#cost-of-building-and-deploying-ai-models-in-agent-platform)  
Image generation | [Agent Platform prices](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing#cost-of-building-and-deploying-ai-models-in-agent-platform)  
General purpose agents made by Google | Deep Research | [Agent Platform prices](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing#cost-of-building-and-deploying-ai-models-in-agent-platform)  
AI developer tools1 |  Gemini models  | [Agent Platform prices](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing#cost-of-building-and-deploying-ai-models-in-agent-platform)  
Claude models  | Claude pricing  
  
1 AI developer tools are available only for [invoiced Cloud Billing accounts](https://docs.cloud.google.com/billing/docs/concepts#billing_account_types), including accounts with a free-trial subscription.

#### Claude pricing

Pay-as-you-go charges for Claude models apply as defined in the following table: **Note:** Claude model pricing and discounts in the Gemini Enterprise app are distinct from pricing procured through Google Cloud Marketplace.

### Global

Model | Type | Model price (/1M tokens)  
=< 200K input tokens | Model price (/1M tokens)  
> 200K input tokens  
---|---|---|---  
Claude Opus 5.5 | Input | $4.00 | $4.00  
Output | $20.00 | $20.00  
5m Cache Write | $5.00 | $5.00  
1h Cache Write | $8.00 | $8.00  
Cache Hit | $0.20 | $0.20  
Claude Sonnet 5.5 | Input | $2.00 | $2.00  
Output | $10.00 | $10.00  
5m Cache Write | $2.50 | $2.50  
1h Cache Write | $4.00 | $4.00  
Cache Hit | $0.20 | $0.20  
  
### US Multi-Region (US)

Model | Type | Model price (/1M tokens)  
=< 200K input tokens | Model price (/1M tokens)  
> 200K input tokens  
---|---|---|---  
Claude Opus 5.5 | Input | $4.40 | $4.40  
Output | $22.00 | $22.00  
5m Cache Write | $5.50 | $5.50  
1h Cache Write | $8.80 | $8.80  
Cache Hit | $0.22 | $0.22  
Claude Sonnet 5.5 | Input | $2.20 | $2.20  
Output | $11.00 | $11.00  
5m Cache Write | $2.75 | $2.75  
1h Cache Write | $4.40 | $4.40  
Cache Hit | $0.22 | $0.22  
  
### EU Multi-Region (EU)

Model | Type | Model price (/1M tokens)  
=< 200K input tokens | Model price (/1M tokens)  
> 200K input tokens  
---|---|---|---  
Claude Opus 5.5 | Input | $4.40 | $4.40  
Output | $22.00 | $22.00  
5m Cache Write | $5.50 | $5.50  
1h Cache Write | $8.80 | $8.80  
Cache Hit | $0.22 | $0.22  
Claude Sonnet 5.5 | Input | $2.20 | $2.20  
Output | $11.00 | $11.00  
5m Cache Write | $2.75 | $2.75  
1h Cache Write | $4.40 | $4.40  
Cache Hit | $0.22 | $0.22  
  
### Quotas for EDU and EDU Pro editions

**Note:** When your project reaches its pooled feature quota for EDU or EDU Pro editions, you can enable overages to allow uninterrupted usage at pay-as-you-go rates.

For information about quotas across Gemini Enterprise EDU and EDU Pro editions, see the following table:

| Gemini Enterprise EDU | Gemini Enterprise EDU Pro  
---|---|---  
Quotas (Pooled or Unpooled) | Pooled across users within the edition per project and location | Pooled across users within the edition per project and location  
Product | Storage + data indexing | 5 GiB | 50 GiB  
Assistant2 | 40 queries per day | 200 queries per day  
No-code agent building tools - Create | 1 agent per day | 10 agents per day  
No-Code agent building tools - use | Based on underlying agent actions  
Video generation | 1 video generation requests per day | 3 video generation requests per day  
Image generation | 2 images per day | 10 images per day  
General purpose agents made by Google | Gemini Notebook - use | Gemini Notebook Enterprise limits1 | Gemini Notebook Enterprise limits1  
Gemini Notebook - create & publish | Gemini Notebook Enterprise limits1 | Gemini Notebook Enterprise limits1  
Deep Research | 1 per day | 10 per day  
Security and compliance | Model Armor | Same quota as the assistant | Same quota as the assistant  
  
1 For information about Gemini Notebook Enterprise usage limits, see the [Gemini Notebook Enterprise documentation](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/overview#usage-limits).

2 This includes the usage of Google Search and Web Grounding.

### Quotas for Frontline editions

**Note:** When your project reaches its pooled feature quota for Frontline editions, you can enable overages to allow uninterrupted usage at pay-as-you-go rates.

For information about quotas across Gemini Enterprise Frontline Starter and Worker, see the following table:

| Gemini Enterprise Frontline Starter | Gemini Enterprise Frontline Worker  
---|---|---  
Quotas (Pooled or Unpooled) | Pooled across users within the edition per project and location | Pooled across users within the edition per project and location  
Product | Storage + data indexing | 2 GiB | 2 GiB  
Search | Abuse preventative only2 |   
Assistant | 20 queries per day | 40 queries per day  
No-code agent building tools - create | n/a | n/a  
No-Code agent building tools - use | Based on underlying agent actions  
Video generation | n/a | 1 video generation request per day  
Image generation | n/a | 2 images per day  
General-purpose agents made by Google | Gemini Notebook - use | Gemini Notebook Enterprise limits1 | Gemini Notebook Enterprise limits1  
Gemini Notebook - create & publish | n/a | n/a  
Deep Research | n/a | 1 per day  
Security and Compliance | Model Armor | Equivalent to assistant quota |   
  
1 For information about Gemini Notebook Enterprise usage limits, see the [Gemini Notebook Enterprise documentation](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/overview#usage-limits).

2Subject to abuse-preventative usage limits only.

### Quotas for Emerging Market editions

**Note:** When your project reaches its pooled feature quota for Emerging Market editions, you can enable overages to allow uninterrupted usage at pay-as-you-go rates.

For information about quotas across Gemini Enterprise Emerging Market editions, see the following table:

| Gemini Enterprise Standard Emerging Market | Gemini Enterprise Emerging Market EDU and governments  
---|---|---  
Quotas (Pooled or Unpooled) | Pooled across users within the edition per project and location | Pooled across users within the edition per project and location  
Product | Storage + data indexing | 10 GiB | 3 GiB  
Search | Abuse preventative only2 | 5 queries per day  
Assistant | 40 queries per day | 5 queries per day, individual only  
No-code agent building tools - create | 1 agent per day | 1 agent per day  
No-Code agent building tools - use | Based on underlying agent actions  
Video generation | n/a | n/a  
Image generation | n/a | 1 image per day  
General-purpose agents made by Google | Gemini Notebook Enterprise - use | Gemini Notebook Enterprise limits1 | n/a  
Gemini Notebook - create & publish | Gemini Notebook Enterprise limits1 | n/a  
Deep Research | 1 per day | n/a  
AI developer tools |  Includes Antigravity, Antigravity for IDEs, and Android Studio  | Doesn't include default quotas3 | n/a  
Security and Compliance | Model Armor | Same quota as the assistant | Same quota as the assistant  
  
1 For information about Gemini Notebook Enterprise usage limits, see the [Gemini Notebook Enterprise documentation](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/overview#usage-limits).

2Subject to abuse-preventative usage limits only.

3AI developer tools don't include bundled quota in the Standard Emerging Market edition.

## API and system quotas

This section lists the technical infrastructure quotas and system limits for Discovery Engine API resources used by Gemini Enterprise. System limits are fixed values that cannot be changed.

### Allocation quotas

The following table lists the allocation quotas for Discovery Engine API. These quotas don't reset over time. Instead, they're released when you release the resource.

Google Cloud uses quotas to help ensure fairness and reduce spikes in resource use and availability. A quota restricts how much of a Google Cloud resource your Google Cloud project can use. Quotas apply to a range of resource types, including hardware, software, and network components. For example, quotas can restrict the number of API calls to a service, the number of load balancers used concurrently by your project, or the number of projects that you can create. Quotas protect the community of Google Cloud users by preventing the overloading of services. Quotas also help you to manage your own Google Cloud resources.

The Cloud Quotas system does the following:

  * Monitors your consumption of Google Cloud products and services
  * Restricts your consumption of those resources
  * Provides a way to [request changes to the quota value](https://docs.cloud.google.com/docs/quotas/help/request_increase) and [automate quota adjustments](https://docs.cloud.google.com/docs/quotas/quota-adjuster)



In most cases, when you attempt to consume more of a resource than its quota allows, the system blocks access to the resource, and the task that you're trying to perform fails.

Quotas generally apply at the Google Cloud project level. Your use of a resource in one project doesn't affect your available quota in another project. Within a Google Cloud project, quotas are shared across all applications and IP addresses. 

For more information, see the [Cloud Quotas overview](https://docs.cloud.google.com/docs/quotas/overview). 

Quota | Value  
---|---  
Total number of data stores per project | 1001  
Total number of engines per project | 1502  
Regional number of data stores per project per location (Global, US, EU) | 100  
Regional number of documents per project per location (Global, US, EU) | 10,000,000  
Regional number of engines per project per location (Global, US, EU) | 150  
  
1 Due to a technical limitation, the maximum quota for data stores is 500 per project. If you need more data stores, use new projects.   
Each entity in a data store is counted as a data store instance and, therefore, counts toward this quota. For example, a data store with three entities counts as three data stores against your quota.

2 Due to a technical limitation, the maximum quota for engines is 500 per project. If you need more engines, use new projects. 

**Note:** The number of data stores, documents, and engines across all locations can't exceed the total per-project quota for that resource. For example, if you already have 60 data stores in the `eu` multi-region and 40 in the `us` multi-region, you can't create another data store because the overall data store quota for the project is 100.

### Rate quotas

The following rate quotas apply to Discovery Engine API requests.

There are also _system limits_ on Gemini Enterprise resources. System limits can't be changed. 

Quota | Value  
---|---  
Complete query requests per minute per project | 300  
Regional search requests per minute per project per location (Global, US, EU) | 300  
  
## Pay-as-you-go usage above quota

Feature usage is restricted when you exceed the feature quotas of your Gemini Enterprise edition. To avoid interruptions, a Gemini Enterprise administrator can turn on the **Pay-as-you-go usage above quota** setting. Pay-as-you-go usage above quota is available only if your project has an [invoiced Cloud Billing account](https://docs.cloud.google.com/billing/docs/concepts#billing_account_types) and at least one active, non-free-trial subscription. Free-trial subscriptions include the base pooled quotas for their edition, including AI developer tools credits, but aren't eligible for overages. To verify your account type, see [Find out your Cloud Billing account type and charging cycle](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle#view-your-charging-cycle).

**Note:** Claude models are available only with pay-as-you-go usage. Ensure that you have turned on **Pay-as-you-go usage above quota** for all editions where you turn on Claude models for your end users.

Pay-as-you-go charges apply as defined in the following table for all license-based editions (Standard, Plus, Frontline, EDU, and Emerging Market editions).

If you have a Pay-as-you-go subscription, you pay for usage at the Pay-as-you-go rates listed in the following table.

**Note:** Usage that exceeds the quota for **storage + data indexing** automatically incurs overage charges. Because storage and data indexing quota is pooled per project and location across all editions, any usage exceeding the single shared pool for the project and location incurs overage charges. You pay storage and data indexing overage charges prorated by the duration you store the data. For example, if you store 30 GiB of excess data for one day in a 30-day month, you pay $5 (30 GiB / 30 days × $5 per GiB per month).

### Pay-as-you-go charges for features above quota

Prices are listed in US Dollars (USD). If you pay in a currency other than USD, the prices listed in your currency on [Cloud Platform SKUs](https://cloud.google.com/skus/) apply. Charges are subject to a variable support fee depending on the support service. For more information on the support services, see [Compare support services](https://docs.cloud.google.com/support/docs/overview#compare-support).

| Gemini Enterprise  
Quota units | Gemini Enterprise  
Pay-as-you-go charges  
---|---|---  
Quotas (Pooled or Unpooled) | Pooled across users within the edition per project and location | Pooled across users within the edition per project and location  
Foundational engagement layer | Storage + data indexing | GiB | $5 per GiB per month  
Assistant - Gemini models | Queries per day | [Agent Platform prices](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing#cost-of-building-and-deploying-ai-models-in-agent-platform)  
Assistant - Claude models | n/a - only available through Pay-as-you-go above quota charges. | Claude pricing  
No-code agent building tools - create | Agents per day | n/a  
No-code agent building tools - use | Based on underlying agent actions | [Agent Platform prices](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing#cost-of-building-and-deploying-ai-models-in-agent-platform)  
Video generation | Video generation requests per day | [Agent Platform prices](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing#cost-of-building-and-deploying-ai-models-in-agent-platform)  
Image generation | Images per day | [Agent Platform prices](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing#cost-of-building-and-deploying-ai-models-in-agent-platform)  
General purpose agents made by Google | Gemini Notebook Enterprise - use | Gemini Notebook Enterprise limits1 | n/a  
Gemini Notebook Enterprise - create & publish | Gemini Notebook Enterprise limits1 | n/a  
Deep Research | Queries per day | [Agent Platform prices](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing#cost-of-building-and-deploying-ai-models-in-agent-platform)  
AI developer tools2 |  Gemini models  | Dollars per month3 in credits for Antigravity, Antigravity for IDEs, and Android Studio | [Agent Platform prices](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing#cost-of-building-and-deploying-ai-models-in-agent-platform)  
Claude models  | n/a - only available through Pay-as-you-go above quota charges. | Claude pricing  
1 For information about Gemini Notebook Enterprise usage limits, see the [Gemini Notebook Enterprise documentation](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/overview#usage-limits). 

2 AI developer tools are available only for [invoiced Cloud Billing accounts](https://docs.cloud.google.com/billing/docs/concepts#billing_account_types), including accounts with a free-trial subscription.

3 Although quotas are listed as a monthly per-user amount, Gemini Enterprise enforces them on a rolling seven-day basis as a shared pool. Gemini Enterprise calculates your project's weekly quota by dividing the monthly per-user value by four and multiplying it by your project's total licensed seats, including free-trial seats. Any user in your edition can draw from this shared weekly pool. Unused quota doesn't roll over to the next week. 

### Claude pricing

Claude models are available on the Gemini Enterprise app only with pay-as-you-go usage. Ensure that you have turned on **Pay-as-you-go usage above quota** for all editions where you want to enable Claude models.

Pay-as-you-go charges for Claude models apply as defined in the following table: **Note:** Claude model pricing and discounts in the Gemini Enterprise app are distinct from pricing procured through Google Cloud Marketplace.

### Global

Model | Type | Model price (/1M tokens)  
=< 200K input tokens | Model price (/1M tokens)  
> 200K input tokens  
---|---|---|---  
Claude Opus 5.5 | Input | $4.00 | $4.00  
Output | $20.00 | $20.00  
5m Cache Write | $5.00 | $5.00  
1h Cache Write | $8.00 | $8.00  
Cache Hit | $0.20 | $0.20  
Claude Sonnet 5.5 | Input | $2.00 | $2.00  
Output | $10.00 | $10.00  
5m Cache Write | $2.50 | $2.50  
1h Cache Write | $4.00 | $4.00  
Cache Hit | $0.20 | $0.20  
  
### US Multi-Region (US)

Model | Type | Model price (/1M tokens)  
=< 200K input tokens | Model price (/1M tokens)  
> 200K input tokens  
---|---|---|---  
Claude Opus 5.5 | Input | $4.40 | $4.40  
Output | $22.00 | $22.00  
5m Cache Write | $5.50 | $5.50  
1h Cache Write | $8.80 | $8.80  
Cache Hit | $0.22 | $0.22  
Claude Sonnet 5.5 | Input | $2.20 | $2.20  
Output | $11.00 | $11.00  
5m Cache Write | $2.75 | $2.75  
1h Cache Write | $4.40 | $4.40  
Cache Hit | $0.22 | $0.22  
  
### EU Multi-Region (EU)

Model | Type | Model price (/1M tokens)  
=< 200K input tokens | Model price (/1M tokens)  
> 200K input tokens  
---|---|---|---  
Claude Opus 5.5 | Input | $4.40 | $4.40  
Output | $22.00 | $22.00  
5m Cache Write | $5.50 | $5.50  
1h Cache Write | $8.80 | $8.80  
Cache Hit | $0.22 | $0.22  
Claude Sonnet 5.5 | Input | $2.20 | $2.20  
Output | $11.00 | $11.00  
5m Cache Write | $2.75 | $2.75  
1h Cache Write | $4.40 | $4.40  
Cache Hit | $0.22 | $0.22  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
