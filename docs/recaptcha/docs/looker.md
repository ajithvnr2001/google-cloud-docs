---
url: https://docs.cloud.google.com/recaptcha/docs/looker/
title: Create dashboards with Data Studio \u00a0|\u00a0 Google Cloud Fraud Defense \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:26:03.774698+00:00
---

# Create dashboards with Data Studio  |  Google Cloud Fraud Defense  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recaptcha/docs/looker/

reCAPTCHA is a part of Google Cloud Fraud Defense. For more information, see [Google Cloud Fraud Defense](https://docs.cloud.google.com/security/products/fraud-defense). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Cloud Fraud Defense ](https://docs.cloud.google.com/recaptcha/docs)
  * [ Guides ](https://docs.cloud.google.com/recaptcha/docs/implementation-workflow)



Send feedback 

#  Create dashboards with Data Studio Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to create custom dashboards of your reCAPTCHA [`assessments`](https://docs.cloud.google.com/recaptcha/docs/create-assessment) by exporting [reCAPTCHA platform logs](https://docs.cloud.google.com/recaptcha/docs/platform-logging) to [Data Studio](https://support.google.com/looker-studio/answer/6283323) .

reCAPTCHA provides a Data Studio template that gives you visibility into how reCAPTCHA is helping to protect your site from threats like scraping, account takeovers (ATOs), and payment fraud. All Data Studio charts are customizable. You can share dashboards as reports through email, or as PDF and PNG files.

**Note:** Data Studio custom dashboards are only available when using the `v1` API and not the `v1beta1` API.

## Before you begin

  1. Ensure that you have the following Identity and Access Management role: reCAPTCHA Enterprise Admin (`roles/recaptchaenterprise.admin`).



## Set up Data Studio dashboard

  1. In the Google Cloud console, go to the **reCAPTCHA** page.

[Go to reCAPTCHA](https://console.cloud.google.com/security/recaptcha).

  2. [Enable platform logs](https://docs.cloud.google.com/recaptcha/docs/platform-logging#enable-disable-platform-logs) for [`assessment`](https://docs.cloud.google.com/recaptcha/docs/create-assessment) operations.

  3. [Create a BigQuery sink](https://docs.cloud.google.com/recaptcha/docs/export-logs-bigquery#create-bigquery-sink) to a [new partitioned BigQuery dataset](https://docs.cloud.google.com/logging/docs/export/configure_export_v2#creating_sink).

  4. Open the [Data Studio dashboard template](https://lookerstudio.google.com/c/u/0/reporting/7c61319f-9d41-4996-bf5e-189ae1d8441e/preview).

  5. To use the BigQuery dataset that you created, follow [Data Studio instructions](https://support.google.com/looker-studio/answer/9851950#add).

  6. You can see your copied or saved reports on the [Data Studio home page](https://lookerstudio.google.com).




## Pricing

Review [BigQuery pricing](https://cloud.google.com/bigquery/pricing).

## What's next

  * Review [BigQuery storage](https://docs.cloud.google.com/bigquery/docs/storage_overview).

  * Review [BigQuery analytics](https://docs.cloud.google.com/bigquery/docs/query-overview).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
