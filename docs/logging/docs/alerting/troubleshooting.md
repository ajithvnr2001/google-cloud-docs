---
url: https://docs.cloud.google.com/logging/docs/alerting/troubleshooting/
title: Troubleshoot log-based alerting policies \u00a0|\u00a0 Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:18:38.483024+00:00
---

# Troubleshoot log-based alerting policies  |  Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/alerting/troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Guides ](https://docs.cloud.google.com/logging/docs/overview)



Send feedback 

#  Troubleshoot log-based alerting policies Stay organized with collections  Save and categorize content based on your preferences. 

This document provides troubleshooting information for using log-based alerting policies. The content on this page doesn't apply to alerting policies that monitor metric data—including log-based metrics—or SQL query results.

## No matching logs are available

**This entry applies only to log-based alerting policies. It doesn't apply to alerting policies that monitor metric data—including log-based metrics—or SQL query results**.

When you test your filter for a log-based alerting policy, no logs are returned. Check the following common errors:

  * You are trying to filter on excluded logs. Log-based alerting policies operate only on included logs.

  * You are trying to filter by log buckets, or for other Google Cloud resources such as Cloud Billing accounts or organizations. Log-based alerting policies operate at Google Cloud project level.

  * Your query is too restrictive. 

Check that your field names and regular expressions are correct. You can use the **Query** pane in Logs Explorer or the **Preview logs** button in the alert-configuration interface to help validate the query. For information about creating queries, see [Logging query language](https://docs.cloud.google.com/logging/docs/view/logging-query-language).




## Alerting policy isn't working

You've created a log-based alerting policy, but it isn't working as you expected. For example:

### Cloud Monitoring isn't sending notifications for the alerting policy

**This entry applies only to log-based alerting policies. It doesn't apply to alerting policies that monitor metric data—including log-based metrics—or SQL query results**.

To resolve this failure, do the following:

  * View the most recent notification from your alerting policy to determine if the policy has reached the limit of 20 notifications per day.

  * View your alerting policy and make sure that it isn't extracting the `timestamp` label. Extraction of this label prevents the alerting policy from creating alerts and sending notifications.

  * View and, if necessary, reduce the minimum time between notifications.




### Cloud Monitoring isn't creating alerts

**This entry applies only to log-based alerting policies. It doesn't apply to alerting policies that monitor metric data—including log-based metrics—or SQL query results**.

To resolve this failure, do the following:

  * View your alerting policy and make sure that it isn't extracting the `timestamp` label. Extraction of this label prevents the alerting policy from creating alerts and sending notifications.

  * A log-based alerting policy can create a maximum of 2 new alerts per minute. If your alerting policy extracts labels, then this limit might prevent creating some alerts.

  * Go to the **Alerts** page in Cloud Monitoring and filter the table by policy name. The results show the current and past alerts:

    * If there are no alerts, then verify that the query used is finding matching logs. 

Check that your field names and regular expressions are correct. You can use the **Query** pane in Logs Explorer or the **Preview logs** button in the alert-configuration interface to help validate the query. For information about creating queries, see [Logging query language](https://docs.cloud.google.com/logging/docs/view/logging-query-language).

    * If there are past alerts but no recent ones for the current day, then you might have reached the limit of 20 alerts per day. View the most recent notification from your alerting policy to determine whether the limit has been reached. Note that this daily limit resets at a random time, rather than at a fixed time like midnight.




### Cloud Monitoring creates too many alerts

**This entry applies only to log-based alerting policies. It doesn't apply to alerting policies that monitor metric data—including log-based metrics—or SQL query results**.

If you are receiving more alerts than you expect, then refine the query in the alerting policy to make it more restrictive. 

Check that your field names and regular expressions are correct. You can use the **Query** pane in Logs Explorer or the **Preview logs** button in the alert-configuration interface to help validate the query. For information about creating queries, see [Logging query language](https://docs.cloud.google.com/logging/docs/view/logging-query-language).

## Alerts aren't closing

**This entry applies only to log-based alerting policies. It doesn't apply to alerting policies that monitor metric data—including log-based metrics—or SQL query results**.

If you don't close an alert, then Cloud Logging closes the alert after the autoclose duration for the alerting policy has passed. The default autoclose duration is 7 days, but you can set it to any value between 30 minutes and 7 days. You can also manually close alerts at any time, as described in [Closing alerts](https://docs.cloud.google.com/logging/docs/alerting/log-based-incidents#closing).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
