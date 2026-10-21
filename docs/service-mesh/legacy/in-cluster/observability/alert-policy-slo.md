---
url: https://docs.cloud.google.com/service-mesh/legacy/in-cluster/observability/alert-policy-slo/
title: Creating an alerting policy for an SLO \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:49:36.180186+00:00
---

# Creating an alerting policy for an SLO  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/legacy/in-cluster/observability/alert-policy-slo/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Creating an alerting policy for an SLO

This page describes how to create an alerting policy in Cloud Monitoring for a service level objective (SLO) that you create in Cloud Service Mesh.

For an introduction to SLOs, see the [Service level objectives overview](https://docs.cloud.google.com/service-mesh/legacy/in-cluster/observability/slo-overview).

Cloud Monitoring can trigger an alert when a Service is on track to violate an SLO. You can create an alerting policy based on the rate of consumption of your [error budget](https://docs.cloud.google.com/service-mesh/legacy/in-cluster/observability/design-slo#error_budgets). All alerts on error budgets have the same basic condition: a specified percentage of the error budget for the [compliance period](https://docs.cloud.google.com/service-mesh/legacy/in-cluster/observability/design-slo#compliance_periods) is consumed in a lookback period, which is a time period, such as the previous 60 minutes. When you create the alerting policy, Cloud Service Mesh automatically sets most of the conditions for the alert based on the settings in the SLO. You specify the lookback period and the consumption percentage.

Determining what values you should set for the lookback period and consumption percentage might take some trial and error. You could use the default lookback period of 60 minutes as a starting point. To determine the consumption percentage, monitor the service behavior to see what percentage of the total error budget (over the compliance period) was consumed in the previous 60 minutes. You want to set the consumption percentage so that you don't burn more error budget in the lookback period than you can afford, but you don't want to set off an alert unnecessarily.

For example, suppose you created an SLO with the following name: `95% < 300ms Latency in Calendar Week`

With this SLO, only 5% of the total number of requests in a week can have a latency > 300ms. Hitting or exceeding 5% consumes your total error budget. If you set the lookback period to one hour, each lookback period is `1/168` of your compliance period (there are 168 hours in a week). To calculate the hourly consumption percentage that doesn't exceed the total error budget for the week: `5%` ÷ `168` ≈ `0.03%`

Because latency for your Service can fluctuate depending on load or other conditions, setting 0.03% as the consumption percentage might trigger unnecessary alerts. You could start with a value twice that, or 0.06%, then monitor your Service and adjust the value as needed.

## Before you begin

[Create an SLO](https://docs.cloud.google.com/service-mesh/legacy/in-cluster/observability/create-slo) for one of your Services.

## Creating an alerting policy on an SLO

  1. Go to the **Health** tab for a service:

     1. In the Google Cloud console, go to **Cloud Service Mesh**.

[Go to Cloud Service Mesh](https://console.cloud.google.com/kubernetes/services)

     2. Select the Google Cloud project from the drop-down list on the menu bar.

     3. Click the service that you want to create an alerting policy for.

     4. In the left navigation bar, click **Health**.

  2. Click the SLO that you want to create an alerting policy for.

  3. In the **Current Status of SLO** section on the right, click the **Create Alerting Policy** link.

The **Add condition** dialog displays. Cloud Service Mesh automatically populates the **SLO Burn Rate** condition based on the settings in the SLO. You configure the **SLO Burn Rate** condition so that you get an alert when the SLO's error budget is declining too rapidly. You want to make sure that you get an alert before the SLO is out of error budget.

![Screenshot of the Cloud Monitoring add condition dialog box.](https://docs.cloud.google.com/service-mesh/legacy/in-cluster/images/alerting-condition.png)

  4. Configure the condition:

     1. To name the condition, click the **Suggested title** link to use the name based on your SLO, or enter a name for the condition.
     2. In the **Target** section, enter the lookback period in the **Lookback Duration** field, or use the default value.
     3. In the **Configuration** section, enter the consumption percentage in the **Threshold** field.
     4. Click **Save**. The **Create new alerting policy** window displays.
  5. Configure the alerting policy:

     1. Enter a policy name.
     2. The condition is automatically populated, but you can optionally add another condition.
     3. If the alerting policy has only one condition, then leave the **Policy triggers** field at the default value of **Any condition is met**.
     4. Optionally, configure the **Notifications** and **Documentation** sections. See [Managing alerting policies](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui) for more information.
     5. Click **Save**. The **Policy details** page is displayed.
     6. To go back to the **Cloud Service Mesh** dashboard, click the **Navigation menu** _dehaze_ and go to **Anthos** > **Services**.



## What's next

  * Learn more about alerting from Site Reliability Engineering at Google:

    * [Site Reliability Engineering](https://sre.google/sre-book/practical-alerting/)
    * [The Site Reliability Workbook](https://sre.google/workbook/alerting-on-slos/)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
