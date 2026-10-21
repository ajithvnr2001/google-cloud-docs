---
url: https://docs.cloud.google.com/monitoring/alerts/snooze/
title: Snooze notifications and alerts \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:44:30.983533+00:00
---

# Snooze notifications and alerts  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/alerts/snooze/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  Snooze notifications and alerts Stay organized with collections  Save and categorize content based on your preferences. 

This document describes snoozes, which let you prevent Cloud Monitoring from creating [alerts](https://docs.cloud.google.com/monitoring/alerts/incidents-events) and issuing notifications during specific time periods. You can create and manage your snoozes by using the Google Cloud console, the Google Cloud CLI, and the Cloud Monitoring API.

## When to snooze alerting policies

[Create a snooze](https://docs.cloud.google.com/monitoring/alerts/manage-snooze) when you want to temporarily prevent alerts from being created and notifications from being sent, or to prevent [repeated notifications](https://docs.cloud.google.com/monitoring/alerts/policies-in-api#send-repeated-notifications) from being sent for an open alert. For example, you might create a snooze in the following situations:

  * You have planned maintenance.
  * You have an escalating outage and you want to prevent further alerts and notifications.



## How snoozes work

When a snooze for an alerting policy is active, Monitoring doesn't send notifications or create alerts for the snoozed alerting policy. When you apply a snooze to a metric-based or SQL-based alerting policy, Monitoring also closes all alerts related to the alerting policy.

You can create a snooze by doing any of the following:

  * To apply the snooze to multiple alerting policies, create it from the **Alerting** page, the gcloud CLI, or the Cloud Monitoring API. You can also choose when the snooze begins and define the snooze duration.

Applying the snooze to multiple alerting policies might be helpful when you you have planned maintenance and need the snooze to begin at a specific time and last for a predetermined duration.

  * To apply a snooze to a specific alert, create the snooze from the **Alert details** page of an open alert. In this case, all snooze fields are preconfigured except the duration.

Applying the snooze from a specific alert might be helpful when you have an escalating outage and need to immediately snooze an alerting policy until related issues have been resolved.




### Components of snoozes

A snooze has the following components:

  * A name. We recommend that you use this field to describe the purpose of the snooze.

  * A period that determines when the snooze is active. It's specified by a start time and a duration. An active snooze prevents Monitoring from creating alerts and issuing notifications for alerting policies that match the criteria of the snooze. Outside the active period, the snooze is inactive. An _inactive_ snooze doesn't affect when alerts are created and notifications are sent.

  * Criteria for the snooze, which includes the following:

    * A list of alerting policies to which the snooze applies.

    * An optional label-based filter that can be used when the snooze applies to a single alerting policy. You define the filter's labels to snooze alerts with matching labels. For example, suppose a filter includes a label for a specific virtual machine (VM) instance ID and that the snooze is active. The alerting policy can still create alerts for all VMs except the one listed in the filter.

A label-based filter can include resource and metric labels. When the alerting policy isn't PromQL-based, the filter can also include metadata labels.




## How snoozes affect alerting policy conditions

The following table describes the relationship between the status of a condition in a single-condition alerting policy and when alerts are created and notifications are sent:

State | Action  
---|---  
Condition isn't met | **Existing behavior** When an alert is open, close it and send alert-closure notifications.  
Condition is met **and**  
Policy isn't associated with an active snooze | **Existing behavior** When an alert doesn't exist, create one and send notifications.  
Condition is met **and**  
**Policy is associated with an active snooze** | 

  * When an alert doesn't exist, don't create one and don't send notifications.
  * When an alert is open, close it and send alert-closure notifications.

  
  
When a snooze is applied to an alerting policy that contains [multiple conditions](https://docs.cloud.google.com/monitoring/alerts/concepts-indepth#condition-combiners), the rules to combine the conditions are enforced first. Next, the rules associated with snoozes are applied.

## How creating a snooze differs from disabling a policy

To prevent notifications from a collection of alerting policies for a short interval, you can manually disable each alerting policy or you can create a snooze:

  * If you choose to manually disable the alerting policies, then you must remember to manually enable each disabled alerting policy at the end of the interval. Also, you can only schedule these actions if you use the Cloud Monitoring API and configure something to issue the API call at a specific time.

  * If you create a snooze, you can schedule the active period, and the snooze can apply to multiple alerting policies. When the snooze is inactive or when an active snooze ends, the alerting policies associated with the snooze behave normally. That is, these alerting policies can create alerts and send notifications.




When you have periodic maintenance windows, for each window, you can manually disable and enable the alerting policies that shouldn't send notifications. However, if you create a snooze for one maintenance window, you can copy that snooze and update the start time and duration of the copy. That is, by creating one snooze and copying it, you can schedule a series of upcoming snoozes for the same collection of alerting policies.

To view a record of when alerting policies are disabled or enabled, you must query the Audit Logs of the Google Cloud project. However, when you create a snooze, that snooze is added to the [historical record of snoozes](https://docs.cloud.google.com/monitoring/alerts/manage-snooze#list) for your Google Cloud project. You can view the historical record, which shows your past, active, and upcoming snoozes, by using the Google Cloud console.

## Restrictions

  * The duration of a snooze must be a single interval that is a multiple of minutes.

  * A snooze can only be applied to 16 alerting policies.

  * The criteria of a snooze can't be modified.

  * When applying a snooze to an alerting policy with a PromQL-based condition, you can't use metadata labels in the filter.




## What's next

  * [Create and manage snoozes](https://docs.cloud.google.com/monitoring/alerts/manage-snooze)
  * [Alerting overview](https://docs.cloud.google.com/monitoring/alerts)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
