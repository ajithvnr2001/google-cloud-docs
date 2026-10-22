---
url: https://docs.cloud.google.com/composer/docs/composer-3/enable-saving-logs-to-environment-bucket/
title: Enable saving logs to the environment's bucket \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:02:49.007721+00:00
---

# Enable saving logs to the environment's bucket  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-3/enable-saving-logs-to-environment-bucket/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 3 Guides ](https://docs.cloud.google.com/composer/docs/composer-3/composer-overview)



Send feedback 

#  Enable saving logs to the environment's bucket Stay organized with collections  Save and categorize content based on your preferences. 

**Managed Airflow (Gen 3)** | [Managed Airflow (Gen 2)](https://docs.cloud.google.com/composer/docs/composer-2/enable-saving-logs-to-environment-bucket "View this page for Managed Airflow \(Gen 2\)") | Managed Airflow (Legacy Gen 1)

Managed Airflow (Gen 3) environments **don't save Airflow task logs to the environment's bucket**. As an alternative, you can [configure a sink](https://docs.cloud.google.com/logging/docs/export/configure_export_v2) in Cloud Logging to route logs to any of the supported locations.

For an example of routing environment logs to a Cloud Storage bucket, see [Restrict locations for Managed Airflow logs](https://docs.cloud.google.com/composer/docs/composer-3/configure-resource-location-restrictions#restrict-logs-location).

**Important:** If you use a sink to route logs, we recommend to **keep environment logs in Cloud Logging** as well as in the configured location. If you use the provided example, skip the last step and don't add an exclusion for Cloud Logging.

## What's next

  * [View logs](https://docs.cloud.google.com/composer/docs/composer-3/view-logs)
  * [Monitor environments](https://docs.cloud.google.com/composer/docs/composer-3/monitor-environments)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
