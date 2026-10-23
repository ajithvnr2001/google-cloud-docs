---
url: https://docs.cloud.google.com/monitoring/alerts/monitor-resource-group/
title: Create alerting policy that monitors a resource group \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:37:28.061656+00:00
---

# Create alerting policy that monitors a resource group  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/alerts/monitor-resource-group/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  Create alerting policy that monitors a resource group Stay organized with collections  Save and categorize content based on your preferences. 

Alerting policies in Cloud Monitoring let you monitor a metric for a [resource group](https://docs.cloud.google.com/monitoring/groups), which is a dynamic collection of resources that match criteria that you define. When you create an alerting policy that monitors a resource group, the alerting policy automatically monitors new resources that match the group criteria. For example, if your resource group includes production Compute Engine virtual machine (VM) instances, then the alerting policy monitors any new production VM that you add.

This content does not apply to log-based alerting policies. For information about log-based alerting policies, which notify you when a particular message appears in your logs, see [Monitoring your logs](https://docs.cloud.google.com/logging/docs/alerting/monitoring-logs). 

## Before you begin

  1. To get the permissions that you need to create and modify alerting policies by using the Google Cloud console, ask your administrator to grant you the [Monitoring Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.editor) (`roles/monitoring.editor`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For more information about Cloud Monitoring roles, see [Control access with Identity and Access Management](https://docs.cloud.google.com/monitoring/access-control).

  2. Ensure that you're familiar with the general concepts of alerting policies. For information about these topics, see [Alerting overview](https://docs.cloud.google.com/monitoring/alerts).

  3. Configure the notification channels that you want to use to receive any alerts. For redundancy purposes, we also recommend that you create multiple types of notification channels. For information about these steps, see [Create and manage notification channels](https://docs.cloud.google.com/monitoring/support/notification-options).

  4. Configure the [resource group](https://docs.cloud.google.com/monitoring/groups) that you want to monitor.




## Create alerting policy

To create an alerting policy that monitors a resource-group by using the Cloud Monitoring API, the filter expression must specify a `group.id`. For an example of a JSON file that specifies this field, see [Group-aggregate policy](https://docs.cloud.google.com/monitoring/alerts/policies-in-json#json-group-aggr).

To create an alerting policy that monitors a resource-group by using the Google Cloud console, do the following:

  1. In the Google Cloud console, go to the _notifications_ **Alerting** page: 

[Go to **Alerting**](https://console.cloud.google.com/monitoring/alerting)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Select **Create policy**.
  3. Expand the **Select a metric** menu and select the metric type that you want to monitor.

  4. Restrict the resources to those in a Monitoring group:

     1. Click **Add Filter** and select **Group**.
     2. Expand _arrow_drop_down_ **Value** and select the group name.
     3. Click **Done**.

You can't modify the group while the group is being used by an alerting policy.

  5. Complete the alerting policy. You must configure the condition trigger, notifications, documentation, and policy name, and then click **Create policy**.




For more information about the settings in an alerting policy, see [Create metric-threshold alerting policies](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
