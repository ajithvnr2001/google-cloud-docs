---
url: https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas/best-practices-reporting/
title: Best practices for usage reporting \u00a0|\u00a0 Google Cloud Marketplace Partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:26.935203+00:00
---

# Best practices for usage reporting  |  Google Cloud Marketplace Partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas/best-practices-reporting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Partners ](https://docs.cloud.google.com/marketplace/docs/partners)
  * [ Develop ](https://docs.cloud.google.com/marketplace/docs/partners/develop)



Send feedback 

#  Best practices for usage reporting Stay organized with collections  Save and categorize content based on your preferences. 

To ensure that your customers are billed correctly, when you [report usage to Google](https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas/configure-usage-reports), such as user operation or resource utilization, keep in mind the following best practices.

## Report usage at time of occurrence

Delays in usage reporting degrade your customers' cost management experience and might not be reflected in partner reports. Service providers must report usage within one hour of the usage being generated.

If you need more time to report usage, contact your partner engineer.

## Report usage after an entitlement is canceled

If you have unreported usage after an entitlement is canceled, you can still report it with a timestamp that reflects the actual time when the usage was generated. The timestamp must be before the entitlement was canceled. Report this usage within one hour. Do not report any usage as new usage after the entitlement ends.

## Report usage at the end of the month

The one hour reporting window applies to the month-end cutoff deadline. To ensure that usage is reported on the current month's invoice, report the usage by 1 AM, US and Canadian Pacific Time (UTC-7 or UTC-8) the following day.

For example, for a September invoice, report the usage by October 1st, 1 AM, US and Canadian Pacific Time (UTC-7 or UTC-8).

If you report the usage later in the day, it might not be included in the current month invoice.

## Remediation for customer actions that prevent reporting usage at the time of occurrence

If you can't report usage, or if the service or billing is disabled for an extended time, we recommend that you provide the customer a grace period to restore the service.

We recommend not exceeding 30 days. During this grace period, consider doing the following:

  * Degrade the provided service. For example, switch the customer to a free tier, or start to reject calls.
  * Continue collecting the usage log while the service is disabled. We recommend collecting the usage with the charge breakdown by, at most, a one hour window so it can be replayed after the service is enabled.
  * When the service is enabled, you must report the usage collected while the service was disabled as actual usage with the time the data was collected. You must also resume your normal usage reporting.



For Kubernetes apps, if usage reports fail during the app's startup, we recommend that your app stop itself, so that your customers get immediate feedback and can resolve the issue.

[ Next Best practices for usage labeling  arrow_forward  ](https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas/best-practices-labeling)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
