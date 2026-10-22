---
url: https://docs.cloud.google.com/compute/docs/instance-groups/disabling-and-enabling-health-state-change-logs/
title: Disabling and enabling health state change logs \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:07:47.829077+00:00
---

# Disabling and enabling health state change logs  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instance-groups/disabling-and-enabling-health-state-change-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Disabling and enabling health state change logs Stay organized with collections  Save and categorize content based on your preferences. 

By default, Compute Engine logs health state changes of your managed instance group when you configure application-based [health check](https://docs.cloud.google.com/compute/docs/instance-groups/autohealing-instances-in-migs#setting_up_an_autohealing_policy) for the group. However, you can disable the logs if you want to reduce the logging costs or don't have any specific requirement to log the health state changes.

For logs of load balancer health checks, see [load balancer's health check logging](https://docs.cloud.google.com/load-balancing/docs/health-check-logging).

## Before you begin

  * Read the [Logs exclusion](https://docs.cloud.google.com/logging/docs/exclusions) documentation.
  * Review the [Cloud Logging pricing](https://docs.cloud.google.com/stackdriver/pricing).



## Disabling health state change logs

To disable the health state change logs, use the [Logs exclusions](https://docs.cloud.google.com/logging/docs/exclusions) to create an exclusion filter that discards the logs.

###  Console 

  1. Go to the **Logs Router** page in the Google Cloud console.

[Go to Logs Router](https://console.cloud.google.com/logs/router)

  2. In the `_Default` logging bucket row, click the _more_vert_ menu and then select **Edit sink**.

  3. In the **Choose logs to filter out of sink** section, click **Add exclusion**.

  4. In the **Exclusion filter name** field, specify a name for your filter.

  5. Build the following exclusion filter:
         
         logName="projects/PROJECT_ID/logs/compute.googleapis.com%2Finstance_group_manager_events" AND
         jsonPayload.instanceHealthStateChange:"*"
         

  6. To save the changes, click **Update sink**.

After you save the changes, Compute Engine begins to filter out the instance health state change logs. To learn more, see [Managing sinks](https://docs.cloud.google.com/logging/docs/export/configure_export_v2#managing_sinks) and [Creating exclusion filters](https://docs.cloud.google.com/logging/docs/exclusions#create-filter-existing).




## Enabling health state change logs

You can enable any previously disabled instance health state change logs or remove the exclusion filter that you added earlier to disable the logs.

###  Console 

To enable health state change logging, do the following:

  1. Go to the **Logs Router** page in the Google Cloud console.

[Go to Logs Router](https://console.cloud.google.com/logs/router)

  2. In the `_Default` logging bucket row, click the _more_vert_ menu and then select **Edit sink**.

  3. In the **Choose logs to filter out of sink** section, click **Disable** next to the exclusion filter that filters out instance health state change logs. You can also **Delete** the exclusion filter if you no longer need it.

**Note:** Check all your exclusion filters because the same log entries could be targeted by more than one filter.
  4. Click **Update sink** to save the changes.

After you save the changes, Compute Engine begins to log the health state changes. For more information about log entries, see [Format of log entries](https://docs.cloud.google.com/compute/docs/instance-groups/monitoring-managed-instance-health-state-changes#what_is_logged).




To learn more, see [Managing sinks](https://docs.cloud.google.com/logging/docs/export/configure_export_v2#managing_sinks) and [Removing exclusions](https://docs.cloud.google.com/logging/docs/exclusions#stopping-resource).

## What's next

  * [Monitoring managed instance health state changes](https://docs.cloud.google.com/compute/docs/instance-groups/monitoring-managed-instance-health-state-changes)
  * [What makes a good autohealing health check](https://docs.cloud.google.com/compute/docs/instance-groups/autohealing-instances-in-migs#what_makes_a_good_autohealing_health_check).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
