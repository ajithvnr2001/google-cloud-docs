---
url: https://docs.cloud.google.com/identity-platform/docs/recaptcha-metrics/
title: Monitor reCAPTCHA metrics \u00a0|\u00a0 Identity Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:49:23.443648+00:00
---

# Monitor reCAPTCHA metrics  |  Identity Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity-platform/docs/recaptcha-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Identity Platform ](https://docs.cloud.google.com/identity-platform/docs)
  * [ Guides ](https://docs.cloud.google.com/identity-platform/docs/how-to)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Monitor reCAPTCHA metrics

This document describes the reCAPTCHA metrics that your Identity Platform emits as a result of the Identity Platform integration with the reCAPTCHA Enterprise API and how to view them with Cloud Monitoring.

## reCAPTCHA metrics

After you [set up the Identity Platform integration with the reCAPTCHA Enterprise API](https://docs.cloud.google.com/identity-platform/docs/recaptcha-enterprise), and optionally, [enable reCAPTCHA SMS defense](https://docs.cloud.google.com/identity-platform/docs/recaptcha-tfp), you can monitor the reCAPTCHA metrics your project emits to ensure that your authentication flows are protected. If reCAPTCHA key provisioning fails or if required service accounts weren't created, reCAPTCHA authentication fails open.

If you've enabled reCAPTCHA bot protection or reCAPTCHA SMS defense in audit mode, monitoring the reCAPTCHA metrics will help you determine if you can enable enforcement. You should consider the following before enabling enforcement:

  * If the majority of recent requests have valid tokens and the ratio of `PASSED` to `FAILED_AUDIT` or `FAILED_ENFORCE` verdicts is acceptable for your business case, consider enabling enforcement.
  * If a majority of the recent requests are likely from outdated clients, consider waiting for more users to update their app before enabling enforcement. Enforcing Identity Platform integration with the reCAPTCHA Enterprise API breaks prior app versions that are not integrated with reCAPTCHA.



To ensure that the integration features are working as intended, you can examine the following metrics your project emits to Cloud Monitoring.

### `identitytoolkit.googleapis.com/recaptcha/verdict_count`

This metric tracks the different verdicts returned by reCAPTCHA. A verdict is generated if a token is present. You can filter on the following verdicts:

  * `PASSED`: Indicates that a given request is allowed when enforcement is enabled.
  * `FAILED_AUDIT`: Indicates that a given request is denied when reCAPTCHA audit mode is enabled.
  * `FAILED_ENFORCE`: Indicates that a given request is denied when reCAPTCHA enforcement mode is enabled.
  * `CLIENT_TYPE_MISSING`: Indicates that a given request has a missing client type when reCAPTCHA enforcement is enabled. This error typically occurs if a request was sent using an outdated client SDK version that does not have reCAPTCHA support.
  * `KEYS_MISSING`: Indicates that a given request can't be verified because Identity Platform can't retrieve valid reCAPTCHA keys when reCAPTCHA enforcement is enabled.



To modify your score ranges to change the ratio of passed-to-failed verdicts, see [Enable reCAPTCHA bot protection](https://docs.cloud.google.com/identity-platform/docs/recaptcha-enterprise#enable).

### `identitytoolkit.googleapis.com/recaptcha/token_count`

This metric tracks the number and status of reCAPTCHA tokens received by the Identity Platform backend. You can filter on the following statuses:

  * `VALID`: Indicates that the reCAPTCHA token passed in is valid.
  * `EXPIRED`: Indicates that the reCAPTCHA token passed in has expired. An expired token might indicate client network issues or abuse.
  * `DUPLICATE`: Indicates that the reCAPTCHA token passed in is a duplicate. A duplicate token might indicate client network issues or abuse.
  * `INVALID`: Indicates that the reCAPTCHA token passed in is invalid. An invalid token might indicate abuse.
  * `MISSING`: Indicates that the reCAPTCHA token doesn't exist in the given request. Missing tokens might indicate an outdated client app.
  * `UNCHECKED`: Indicates that the reCAPTCHA token was not checked due to `CLIENT_TYPE_MISSING` or `KEYS_MISSING` verdicts.



If your app rolled out successfully to users, you will see traffic with valid tokens. The number of valid tokens is likely proportional to the number of users who are using your updated app.

### `identitytoolkit.googleapis.com/recaptcha/risk_scores`

This metric tracks the reCAPTCHA score distribution. This can help you define the optimal score ranges for your bot protection configuration.

### `identitytoolkit.googleapis.com/recaptcha/sms_tf_risk_scores`

This metric tracks the reCAPTCHA SMS defense risk score distribution for a particular Identity Platform project. This can help you define the optimal score ranges for your reCAPTCHA SMS defense configuration.

## View reCAPTCHA metrics

To view the reCAPTCHA metrics with Cloud Monitoring, do the following:

  1. In the Google Cloud console, go to the **Metrics explorer** page.

[Go to Metrics explorer](https://console.cloud.google.com/monitoring/metrics-explorer)

  2. From **Select a metric** , enter **Identity Toolkit Tenant**. If you are using multi-tenancy, you can view metrics for each tenant, as well as the parent project, by leaving `tenant_name` empty.




## What's next

  * Learn how to [troubleshoot common issues](https://docs.cloud.google.com/identity-platform/docs/recaptcha-troubleshooting) with the reCAPTCHA integration.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
