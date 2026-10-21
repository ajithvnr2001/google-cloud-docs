---
url: https://docs.cloud.google.com/recaptcha/docs/billing-information/
title: Billing information \u00a0|\u00a0 Google Cloud Fraud Defense \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:50:33.470314+00:00
---

# Billing information  |  Google Cloud Fraud Defense  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recaptcha/docs/billing-information/

reCAPTCHA is a part of Google Cloud Fraud Defense. For more information, see [Google Cloud Fraud Defense](https://docs.cloud.google.com/security/products/fraud-defense). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Cloud Fraud Defense ](https://docs.cloud.google.com/recaptcha/docs)
  * [ Resources ](https://docs.cloud.google.com/recaptcha/docs/resources)



Send feedback 

#  Billing information Stay organized with collections  Save and categorize content based on your preferences. 

This document describes billing for Google Cloud Fraud Defense.

## Fraud Defense tiers

Understand the Fraud Defense tiers so that you can adjust your tier to better adapt to your needs.

### Essentials

  * **Eligibility:** Automatically applied to new keys in Google Cloud projects without billing enabled.

  * **Cost:** Free.

  * **Usage Limit:** Up to 10,000 assessments per calendar month per organization. The limit aggregates use across all accounts and all sites.

  * **Features:** [Basic](https://docs.cloud.google.com/recaptcha/docs/compare-tiers) feature set.

  * **Beyond Limit:** Requests return a [`Resource Exhausted (429)`](https://docs.cloud.google.com/recaptcha/docs/quotas#quota_limit) quota error after your organization exceeds 10,000 cumulative assessments across all accounts and sites within a calendar month.




### Premium

  * **Eligibility:** Automatically applied when you enable billing on your Google Cloud project.

  * **Cost:** The cost is as follows:

    * **0–10,000 assessments per calendar month:** Free per organization (aggregates use across all accounts and all sites).
    * **10,001–100,000 assessments per month:** $8 flat fee.
    * **Over 100,000 assessments per month:** $0.001 per assessment ($1.00 per 1,000 assessments).
  * **Features:** Access to an advanced set of features, even within the free assessment range.




### Free monthly allowance and usage across tiers

The free 10,000 assessments are per organization per calendar month. The limit aggregates use across all accounts and all sites. The limit includes assessment traffic across all keys, web pages, and mobile applications within your individual Google Cloud accounts and Google Cloud projects, regardless of whether your projects use the Essentials plan or the Premium plan.

The following rules apply when your cumulative monthly usage reaches 10,000 assessments across your organization:

  * **Essentials projects (no billing account attached):** After your organization reaches 10,000 cumulative assessments across all accounts and sites in a calendar month, any further `CreateAssessment` requests in an Essentials project return a `Resource Exhausted (429)` quota error until the quota resets on the first day of the next calendar month.
  * **Premium projects (billing account attached):** After your organization reaches 10,000 cumulative assessments in a calendar month, any further requests in your projects remain active without interruption and are billed according to Premium tier pricing ($8 flat fee for assessments 10,001 through 100,000, and $0.001 per assessment thereafter).



#### Examples of monthly usage calculation

The following scenarios illustrate how the 10,000 free monthly assessments apply across your projects and sites:

  * **Example 1: Multiple projects sharing the free monthly allowance.** If you use multiple projects (`Project A` and `Project B`) without billing enabled to protect your sites or applications, those projects share a single 10,000 free monthly assessment limit. If `Project A` processes 7,000 assessments and `Project B` processes 3,000 assessments in the same calendar month, your cumulative usage reaches the 10,000-assessment limit. Both projects remain within the free allowance for that month and process requests normally without errors.

  * **Example 2: Essentials projects exceeding the shared free limit.** If your projects (`Project A` and `Project B`) process more than 10,000 cumulative assessments across your sites in a calendar month while billing remains disabled, requests after the 10,000th assessment return a quota error. To process additional assessments in those projects during that calendar month without errors, you must [enable billing](https://docs.cloud.google.com/billing/docs/how-to/modify-project#enable_billing_for_an_existing_project) on `Project A` and `Project B` to upgrade the projects to the Premium tier.

  * **Example 3: A Premium project exceeding the free monthly allowance.** If you have a Premium project (`Project A`) with billing enabled and process 25,000 assessments across your accounts and sites in a calendar month, the first 10,000 assessments are free under the monthly allowance. The remaining 15,000 assessments are billed on your Cloud Billing invoice under Premium tier rates ($8 flat fee).




### Verifying assessment volume and quota limits

To monitor your monthly billable assessment volume across your projects and check whether you are approaching the 10,000 free monthly allowance, use the following tools:

  * **Billing reports:** To view your total billable assessment volume and cost trends across your organization, see [View your billing reports and cost trends](https://docs.cloud.google.com/billing/docs/how-to/reports).
  * **Usage dashboard:** To view a breakdown of billed assessments over the last 30 days, check the feature usage dashboard on the Fraud Defense home page in the Google Cloud console.



To debug API traffic or check for `RESOURCE_EXHAUSTED` status codes, you can still use [platform logs](https://docs.cloud.google.com/recaptcha/docs/platform-logging) in Cloud Logging and [quota metrics](https://docs.cloud.google.com/recaptcha/docs/quotas).

### Enterprise

If you're a high-volume user, [contact Sales](https://inthecloud.withgoogle.com/security-ups/contact.html) to discuss an Enterprise subscription with volume discounts.

After an Enterprise subscription is activated on your billing account, projects linked to the account will automatically gain access to [Enterprise features](https://docs.cloud.google.com/recaptcha/docs/compare-tiers) within 1 hour.

## When to enable billing

To enable and use Fraud Defense on Google Cloud, you don't need to enable billing for your Google Cloud project. However, you need to enable billing for your Google Cloud project in the following scenarios:

  * You expect to exceed the free monthly allowance of Fraud Defense, which is 10,000 assessments per calendar month across your organization. For more information about the free monthly allowance, see [Pricing](https://cloud.google.com/security/products/recaptcha#pricing).

  * You're about to exceed the free monthly allowance of Fraud Defense and you want to continue using Fraud Defense to protect your website or mobile application.

You'll receive email notifications to enable billing when you're approaching the free monthly allowance and when you exceed it. Enabling the billing account before you exceed the free monthly allowance helps to keep you and your users safe from fraudulent activities, spam, and abuse.

If you don't enable billing for your Google Cloud project, Fraud Defense returns an error for any new request after you reach the free monthly allowance.

  * You want access to features that are exclusive to Fraud Defense Premium and Enterprise tiers. Enabling billing is required for those features even if you expect your usage to be within the free monthly allowance.




To learn how to enable billing for your project, see [Enable billing for a project](https://docs.cloud.google.com/billing/docs/how-to/modify-project#enable_billing_for_a_project).

## Downgrading tiers

If your project is downgraded to a lower tier, you lose access to features exclusive to the higher tier. This can happen due to an expired subscription or a billing issue.

For detailed information about what happens during a downgrade, how to avoid it, and how it impacts your integration, see [Understand tier downgrades](https://docs.cloud.google.com/recaptcha/docs/downgrades).

## Billing resources

Use the following resources to get help with billing questions:

  * To view billing reports, see [View your billing reports and cost trends](https://docs.cloud.google.com/billing/docs/how-to/reports).

  * To learn more about billing, read the [Cloud Billing documentation](https://docs.cloud.google.com/billing/docs).

  * To resolve billing concerns, use the [Google Cloud Billing Troubleshooter](https://support.google.com/cloud/troubleshooter/7279311?&ref_topic=6288636).

  * To request help with billing questions, contact [Cloud Billing Support](https://docs.cloud.google.com/support/billing).

  * To change or disable billing on a project, go to the **Billing** page in the Google Cloud console. For more information, see [Modify a project's billing settings](https://docs.cloud.google.com/billing/docs/how-to/modify-project).

**Caution:** When you disable billing for a project, you also disable all product resources in that project.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
