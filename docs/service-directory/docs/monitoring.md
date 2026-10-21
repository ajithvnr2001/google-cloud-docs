---
url: https://docs.cloud.google.com/service-directory/docs/monitoring/
title: View logs and metrics \u00a0|\u00a0 Service Directory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:49:10.313688+00:00
---

# View logs and metrics  |  Service Directory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-directory/docs/monitoring/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Service Directory ](https://docs.cloud.google.com/service-directory/docs)
  * [ Guides ](https://docs.cloud.google.com/service-directory/docs/overview)



Send feedback 

#  View logs and metrics Stay organized with collections  Save and categorize content based on your preferences. 

You can use [Cloud Monitoring](https://docs.cloud.google.com/monitoring) and [Cloud Logging](https://docs.cloud.google.com/logging) with Service Directory.

## Monitor

Monitoring lets you create dashboards or set up alerts. You can access it by visiting [Monitoring](https://app.google.stackdriver.com/) in Google Cloud console. To view basic monitoring metrics (request count, size, and latency), go to the **Metrics Explorer** and filter by `resource_type:consumed_api` and `service:servicedirectory.googleapis.com`.

## View logs

Service Directory produces audit logs that you can view through Logging.

### Audit logs

[Audit logs](https://docs.cloud.google.com/logging/docs/audit) can help you answer the questions "Who did what, where, and when?". Service Directory writes two types of audit logs: **admin activity** and **data access**. Admin activity logs are always enabled and apply to the following Service Directory operations:

  * CreateNamespace
  * UpdateNamespace
  * DeleteNamespace
  * SetIamPolicy



All other Service Directory operations are considered data access logs and are not enabled by default. Data access logs are also subject to Logging pricing and quota, whereas neither applies to admin activity logs. To enable data access logging, see [Configuring Data Access logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access#config-console).

To see these logs in [Logging](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface#getting_started), select `Service Directory Namespace` from the **Resource** drop-down menu and `cloudaudit.googleapis.com/activity` or `cloudaudit.googleapis.com/data_access`, as appropriate, from the **Logs** drop-down.

## What's next

  * To get a thorough understanding of Monitoring, see the [Monitoring documentation](https://docs.cloud.google.com/monitoring/docs).
  * To find solutions for common issues that you might encounter when using Service Directory, see [Troubleshooting](https://docs.cloud.google.com/service-directory/docs/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
