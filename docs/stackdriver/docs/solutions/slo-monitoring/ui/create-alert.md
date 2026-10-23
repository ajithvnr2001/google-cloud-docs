---
url: https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/ui/create-alert/
title: Creating an alerting policy \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:32:33.220908+00:00
---

# Creating an alerting policy  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/ui/create-alert/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  Creating an alerting policy Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to create an alerting policy to monitor the error budget of an SLO associated with a service. To monitor the error budget for your SLO, you can create one or more alerting policies for the SLO. The purpose of the alerting policy is to warn you when the service is consuming the error budget too quickly.

You can have up to 2,000 alerting policies in a metrics scope.

For general information on SLO-based alerting policies, see [Alerting on your burn rate](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/alerting-on-budget-burn-rate).

To create an alerting policy for an SLO associated with a service, start by doing the following:

  * On the **Services Overview** page, click the name of the service for which you want to create an alerting policy.

  * In the **Current status** pane, locate the entry for the SLO you want to monitor. Click _notifications_ **Create SLO alert**.

![Option to create an alerting policy from the service dashboard.](https://docs.cloud.google.com/static/stackdriver/docs/solutions/slo-monitoring/images/svcmon-msvc-alert1.png)




Clicking **Create SLO alert** takes to you the condition editor for a SLO-based alerting policy.

## Creating the condition

When you click **Create SLO alert** , an in-context pane, **Set SLO alert conditions** , opens for creating a SLO-based condition for an alerting policy. The following screenshot shows an example:

![Pre-populated values in an SLO-based alert condition.](https://docs.cloud.google.com/static/stackdriver/docs/solutions/slo-monitoring/images/svcmon-alert-condition.png)

Because you clicked **Create SLO alert** from a specific SLO in a specific service, the configuration pane is pre-populated with best-practice values for your SLO. The value of the **Target** field is the SLO for which you are creating the alerting policy.

The condition must have a name. The **Display name** field is pre-populated with a suggestion based on the configuration of the SLO. You can change this value by clicking on the text box.

The **Lookback duration** field specifies how far back in time to retrieve the burn-rate data. This value is also used as the evaluation period for calculating the error-budget consumption. This field has a default value, but you can change it. See [Alerting policies and lookback periods](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/alerting-on-budget-burn-rate#alert-lookbacks) for more information.

The **Burn rate threshold** field specifies the rate of error-budget consumption for which you want to be notified. This field has a default value, but you can change it. Set this value so that, as long as the rate of error-budget consumption stays below this threshold, you will not exhaust your error budget during the SLO compliance period.

The condition describes the behavior of the alerting policy, and SLOs often have two, a “fast burn” and a “slow burn” policy. For more information, see [Types of error-budget alerts](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/alerting-on-budget-burn-rate#burn-rates).

When you are satisfied with the condition, click **Next** to proceed to the next pane, **Who should be notified?**

## Setting up notifications

In this step, you specify notification channels for the alerting policy. Notification channels tell Cloud Monitoring how to notify you that the alerting policy has fired. This step is optional:

![Specify whom to notify of the problem and how.](https://docs.cloud.google.com/static/stackdriver/docs/solutions/slo-monitoring/images/svcmon-alert-notification.png)

After selecting a notification channel or deciding to skip the step, click **Next** to proceed to the next pane, **What are the steps to fix the issue?**

## Setting up documentation

In this step, you can provide information that is included in notifications. This documentation can describe the alerting policy and provide troubleshooting information to the recipient of the notification.

![Add information to help responders address the problem.](https://docs.cloud.google.com/static/stackdriver/docs/solutions/slo-monitoring/images/svcmon-alert-doc.png)

Documentation is optional but strongly recommended. This information can help guide the troubleshooting process once an alert has fired.

When you are satisfied with the documentation, click **Save** to finish the creation of the alerting policy.

Notification channels and documentation are standard parts of an alerting policy in Cloud Monitoring; for more information about them, see the general documentation for [Creating an alerting policy](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui#create-policy).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
