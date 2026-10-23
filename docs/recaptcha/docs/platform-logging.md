---
url: https://docs.cloud.google.com/recaptcha/docs/platform-logging/
title: Working with platform logs \u00a0|\u00a0 Google Cloud Fraud Defense \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T05:43:54.214642+00:00
---

# Working with platform logs  |  Google Cloud Fraud Defense  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recaptcha/docs/platform-logging/

reCAPTCHA is a part of Google Cloud Fraud Defense. For more information, see [Google Cloud Fraud Defense](https://docs.cloud.google.com/security/products/fraud-defense). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Cloud Fraud Defense ](https://docs.cloud.google.com/recaptcha/docs)
  * [ Guides ](https://docs.cloud.google.com/recaptcha/docs/implementation-workflow)



Send feedback 

#  Working with platform logs Stay organized with collections  Save and categorize content based on your preferences. 

This document shows you how to enable or disable platform logs that are created by reCAPTCHA as part of Cloud Logging. For more information about platform logs, see [Google Cloud platform logs](https://docs.cloud.google.com/logging/docs/api/platform-logs).

You can enable platform logging for reCAPTCHA specifically for the following operations:

  * [`Assessment`](https://docs.cloud.google.com/recaptcha/docs/reference/rest/v1/projects.assessments#Assessment) response from [`projects.assessments.create`](https://docs.cloud.google.com/recaptcha/docs/reference/rest/v1/projects.assessments/create)

  * [`AnnotateAssessmentRequest`](https://docs.cloud.google.com/recaptcha/docs/reference/rpc/google.cloud.recaptchaenterprise.v1#google.cloud.recaptchaenterprise.v1.AnnotateAssessmentRequest) request to [`projects.assessments.annotate`](https://docs.cloud.google.com/recaptcha/docs/reference/rest/v1/projects.assessments/annotate)




Platform logging is available only when using the v1 API ([`CreateAssessment`](https://docs.cloud.google.com/recaptcha/docs/reference/rest/v1/projects.assessments#Assessment) and [`AnnotateAssessment`](https://docs.cloud.google.com/recaptcha/docs/reference/rest/v1/projects.assessments/annotate)) and not with the `v1beta1` API or the `SiteVerify` API.

**Note:** The PII data for Fraud Prevention is not displayed in the platform logs.

## Enable or disable platform logs

To enable or disable platform logs, do the following:

  1. In the Google Cloud console, go to the **Google Cloud Fraud Defense** page.

[Go to Google Cloud Fraud Defense](https://console.cloud.google.com/security/recaptcha)

  2. Verify that the name of your project appears in the resource selector at the top of the page.

If you don't see the name of your project, click the resource selector, then select your project. See [identifying projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) for help finding the project name, ID, or number.

  3. Click **settings Settings**.

![](https://docs.cloud.google.com/static/recaptcha/images/settings-button.png)

  4. In the **Platform logging** card, click **Configure**.

![](https://docs.cloud.google.com/static/recaptcha/images/platform-logging-card.png)

  5. To enable or disable platform logs for [assessment](https://docs.cloud.google.com/recaptcha/docs/create-assessment) and [annotation](https://docs.cloud.google.com/recaptcha/docs/annotate-assessment) operations, click the respective toggles in the **Platform logging** pane.

![](https://docs.cloud.google.com/static/recaptcha/images/platform-logging-subtask.png)

  6. Click **Save** to complete.




For more information about viewing, routing, and storing platform logs, see [Managing logs](https://docs.cloud.google.com/logging/docs/api/platform-logs#managing-logs).

You can export reCAPTCHA platform logs to BigQuery using a log sink in Logs Router. For more information, see [Export logs to BigQuery](https://docs.cloud.google.com/recaptcha/docs/export-logs-bigquery).

You can enable the collection of reCAPTCHA platform logs in Google Security Operations for analysis. For more information, see [Collect reCAPTCHA logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/collect-gcp-recaptcha-logs).

## Pricing

For information on logs pricing, see [Logging pricing](https://cloud.google.com/stackdriver/pricing#logging-costs).

**Note:** To avoid potentially redundant billing for logs, ensure that `DATA_WRITE` audit logs are not enabled for reCAPTCHA. For more information, see [audit logging](https://docs.cloud.google.com/recaptcha/docs/audit-logging).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
