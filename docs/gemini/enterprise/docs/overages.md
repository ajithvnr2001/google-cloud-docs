---
url: https://docs.cloud.google.com/gemini/enterprise/docs/overages/
title: Quotas and overages (Legacy) \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T23:32:27.747745+00:00
---

# Quotas and overages (Legacy)  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/overages/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)



Send feedback 

#  Quotas and overages (Legacy) Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** The quotas and overages on this page apply to you if you received the email with the subject line _[Billing Update] New Gemini Enterprise overage billing controls launching August 17, 2026_. If you didn't receive the email, see [Quotas and overages](https://docs.cloud.google.com/gemini/enterprise/docs/quotas-and-overages).

Your subscription entitles you to certain quotas across product features.

With the exception of storage and data indexing, quotas are pooled across users in the same edition within a project and location. All users with licenses for a specific edition share a single combined limit per project and location for every product feature with a quota. This total, or pooled, quota is calculated by multiplying the number of user licenses for that edition by the per-user quota.

#### Use case 1: Multiple editions in one project and location

If you have users with different editions in the same project and location, quota pools are maintained separately for each edition except for storage and data indexing:

  * **Standard feature quotas:** Quotas are pooled separately by edition in each project and location. For example, if a project and location has 100 Standard edition licenses and 50 Plus edition licenses, your Standard edition users share a pool of 16,000 Assistant queries per day (100 licenses × 160 queries), and your Plus edition users share a separate pool of 10,000 queries per day (50 licenses × 200 queries). These feature quota pools don't combine across editions.
  * **Storage and data indexing:** Quotas are pooled across all users in a given project and location, regardless of edition. For example, if a project and location has 100 Standard edition licenses (30 GiB per user) and 50 Plus edition licenses (75 GiB per user), there is a single combined storage pool of 6,750 GiB per month ((100 × 30 GiB) + (50 × 75 GiB)) shared by all users in that project and location across all editions.



#### Use case 2: Quota pooling within a single edition

Within an edition's quota pool, the following rules apply. For example, if you have 10 Standard edition licenses, your users share a total pooled quota of 1,600 queries per day (10 licenses x 160 queries):

  * The 10 Standard edition users share a combined pool of 1,600 queries for the day.
  * One power user can use 500 queries, leaving 1,100 queries for the remaining users in that edition.
  * Individual usage isn't capped at the per-user limit; all users in the edition draw from their edition's shared pool until it is depleted.



## Quotas for Standard and Plus editions

For information about quotas across Gemini Enterprise Standard and Plus editions, see the following table:

| Gemini Enterprise Standard | Gemini Enterprise Plus  
---|---|---  
Quotas | Pooled or unpooled | Pooled across users within the edition per project and location | Pooled across users within the edition per project and location  
Product | Storage + data indexing | 30 GiB | 75 GiB  
Assistant | 160 queries per day | 200 queries per day  
No-code agent building tools - create | 1 agent per day | 10 agents per day  
No-Code agent building tools - use | Based on underlying agent actions  
Video generation | 2 video generation requests per day | 3 video generation requests per day  
Image generation | 5 images per day | 10 images per day  
General purpose agents made by Google | Gemini Notebook - use | Gemini Notebook Enterprise limits1 | Gemini Notebook Enterprise limits1  
Gemini Notebook - create & publish | Gemini Notebook Enterprise limits1 | Gemini Notebook Enterprise limits1  
Deep Research | 3 per day | 10 per day  
  
1 For information about Gemini Notebook Enterprise usage limits, see the [Gemini Notebook Enterprise documentation](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/overview#usage-limits).

## Quotas for EDU and EDU Pro editions

For information about quotas across Gemini Enterprise EDU and EDU Pro editions, see the following table:

| Gemini Enterprise EDU | Gemini Enterprise EDU Pro  
---|---|---  
Quotas (Pooled or Unpooled) | Pooled across users within the edition per project and location | Pooled across users within the edition per project and location  
Product | Storage + data indexing | 5 GiB | 50 GiB  
Assistant2 | 40 queries per day | 200 queries per day  
No-code agent building tools - Create | 1 agent per day | 10 agents per day  
No-code agent building tools - use | Based on underlying agent actions  
Video generation | 1 video generation requests per day | 3 video generation requests per day  
Image generation | 2 images per day | 10 images per day  
General purpose agents made by Google | Gemini Notebook - use | Gemini Notebook Enterprise limits1 | Gemini Notebook Enterprise limits1  
Gemini Notebook - create & publish | Gemini Notebook Enterprise limits1 | Gemini Notebook Enterprise limits1  
Deep Research | 1 per day | 10 per day  
Security and compliance | Model Armor | Same quota as the assistant | Same quota as the assistant  
  
1 For information about Gemini Notebook Enterprise usage limits, see the [Gemini Notebook Enterprise documentation](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/overview#usage-limits).

2 This includes the usage of Google Search and Web Grounding.

## Quotas for Frontline editions

For information about quotas across Gemini Enterprise Frontline Starter and Worker, see the following table:

| Gemini Frontline Starter | Gemini Frontline Worker  
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
Security and Compliance | Model Armor | Same quota as the assistant |   
  
1 For information about Gemini Notebook Enterprise usage limits, see the [Gemini Notebook Enterprise documentation](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/overview#usage-limits).

2 Subject to abuse-preventative usage limits only.

## Quotas for Emerging Markets editions

For information about quotas across Gemini Enterprise Emerging Markets editions, see the following table:

| Gemini Enterprise Emerging Markets | Gemini Enterprise Emerging Markets EDU and governments  
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
Gemini Notebook Enterprise - create & publish | Gemini Notebook Enterprise limits1 | n/a  
Deep Research | 1 per day | n/a  
Idea Generation | n/a | n/a  
Security and Compliance | Model Armor | Same quota as the assistant | Same quota as the assistant  
  
1 For information about Gemini Notebook Enterprise usage limits, see the [Gemini Notebook Enterprise documentation](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/overview#usage-limits).

2Subject to abuse-preventative usage limits only.

## Overages

For information about overages in Gemini Enterprise, see the following table.

**Note:** Overages are the same across all editions of Gemini Enterprise. To prevent unexpected overage charges, [set a monthly spend limit](https://docs.cloud.google.com/gemini/enterprise/docs/configure-overages#set-spend-limit).**Note:** Usage that exceeds the quota for `storage + data indexing` automatically incurs overage charges. For all other features, exceeding the pooled quota limit restricts functionality. When a limit is reached, you will get the option to either enable overages to pay for them, or keep the feature restricted to the available quota. |  | Gemini Enterprise  
Quota units | Gemini Enterprise  
Add-on Overage Charges  
---|---|---|---  
Quotas (Pooled or Unpooled) | Pooled across users within the edition per project and location | Pooled across users within the edition per project and location  
Product | Storage + data indexing | GiB | $5 per GiB per mo  
Assistant | Queries per day | $0.10 per query  
No-code agent building tools - create | Agents per day | n/a  
No-code agent building tools - use | Based on underlying agent actions | Based on underlying agent actions  
Video generation | seconds per day | $0.40 per second  
Image generation | images per day | $0.02 per image generation  
General purpose OOTB agents | Gemini Notebook Enterprise - use | Gemini Notebook Enterprise limits1 | n/a  
Gemini Notebook Enterprise - create & publish | queries per day | n/a  
Deep Research | queries per day | $4.00 per query  
  
1 For information about Gemini Notebook Enterprise usage limits, see the [Gemini Notebook Enterprise documentation](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/overview#usage-limits).

## AI developer tools

For information about AI developer tools quotas and overages across supported Gemini Enterprise editions, see the following table.

Prices are listed in US Dollars (USD). If you pay in a currency other than USD, the prices listed in your currency on [Cloud Platform SKUs](https://cloud.google.com/skus/) apply.

| Gemini Enterprise Standard | Gemini Enterprise Plus | Add-on overage charges  
---|---|---|---  
AI developer tools1 |  Included Antigravity, Antigravity for IDEs, and Android Studio credits  | $10 credit per user per month2 | $15 credit per user per month2 | [Agent Platform prices](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing#cost-of-building-and-deploying-ai-models-in-agent-platform)  
  
1 AI developer tools are available only for [invoiced Cloud Billing accounts](https://docs.cloud.google.com/billing/docs/concepts#billing_account_types), including accounts with a free-trial subscription.

2 Although quotas are listed as a monthly per-user amount, Gemini Enterprise enforces them on a rolling seven-day basis as a shared pool. Gemini Enterprise calculates your project's weekly quota by dividing the monthly per-user value by four and multiplying it by your project's total licensed seats, including free-trial seats. Any user in your edition can draw from this shared weekly pool. Unused quota doesn't roll over to the next week.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
