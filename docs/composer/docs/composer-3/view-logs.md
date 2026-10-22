---
url: https://docs.cloud.google.com/composer/docs/composer-3/view-logs/
title: View Airflow logs \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:08:32.158412+00:00
---

# View Airflow logs  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-3/view-logs/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 3 Guides ](https://docs.cloud.google.com/composer/docs/composer-3/composer-overview)



Send feedback 

#  View Airflow logs Stay organized with collections  Save and categorize content based on your preferences. 

**Managed Airflow (Gen 3)** | [Managed Airflow (Gen 2)](https://docs.cloud.google.com/composer/docs/composer-2/view-logs "View this page for Managed Airflow \(Gen 2\)") | [Managed Airflow (Legacy Gen 1)](https://docs.cloud.google.com/composer/docs/composer-1/view-logs "View this page for Managed Airflow \(Legacy Gen 1\)")

This page describes how to access and view Apache Airflow logs for Managed Service for Apache Airflow.

## About log types

Managed Service for Apache Airflow has the following Airflow logs:

  * Streaming logs. These logs contain Airflow task logs, as well as logs of Airflow components of your environment, such as Airflow schedulers and workers.

To learn about Cloud Logging and Cloud Monitoring for your Managed Airflow environment, see [Monitor environments](https://docs.cloud.google.com/composer/docs/composer-3/monitor-environments).

  * Managed Service for Apache Airflow generates [audit logs](https://docs.cloud.google.com/logging/docs/audit), such as Admin Activity logs. For more information, see [View audit logs](https://docs.cloud.google.com/composer/docs/composer-3/audit-logging).




## Before you begin

  * Managed Airflow (Gen 3) environments **don't save Airflow task logs to the environment's bucket**. As an alternative, you can [configure a sink](https://docs.cloud.google.com/logging/docs/export/configure_export_v2) in Cloud Logging to route logs to any of the supported locations.

For an example of routing environment logs to a Cloud Storage bucket, see [Restrict locations for Managed Airflow logs](https://docs.cloud.google.com/composer/docs/composer-3/configure-resource-location-restrictions#restrict-logs-location).

**Important:** If you use a sink to route logs, we recommend to **keep environment logs in Cloud Logging** as well as in the configured location. If you use the provided example, skip the last step and don't add an exclusion for Cloud Logging.



## View streaming logs

To view streaming logs in Cloud Logging:

###  Console 

  1. In the Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  2. In the list of environments, click the name of your environment. The **Environment details** page opens.

  3. Go to the **Logs** tab.




## View streaming logs in Cloud Logging

To view streaming logs in Cloud Logging:

###  Console 

  1. In the Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  2. In the list of environments, locate your environment.

  3. in the **Logs** column, click the **Logs** link.




## What's next

  * [Monitor environments](https://docs.cloud.google.com/composer/docs/composer-3/monitor-environments)
  * [Managed Service for Apache Airflow audit logging](https://docs.cloud.google.com/composer/docs/composer-3/audit-logging)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
