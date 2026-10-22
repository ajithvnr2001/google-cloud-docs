---
url: https://docs.cloud.google.com/network-intelligence-center/docs/firewall-insights/how-to/configure-observation-period/
title: Set up observation period and refresh cycle \u00a0|\u00a0 Network Intelligence Center - Firewall Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:14:19.553631+00:00
---

# Set up observation period and refresh cycle  |  Network Intelligence Center - Firewall Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/firewall-insights/how-to/configure-observation-period/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Firewall Insights ](https://docs.cloud.google.com/network-intelligence-center/docs/firewall-insights)
  * [ Guides ](https://docs.cloud.google.com/network-intelligence-center/docs/firewall-insights/how-to/using-firewall-insights)



Send feedback 

#  Set up observation period and refresh cycle Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to configure an observation period and a refresh cycle in Firewall Insights.

For an overview of the available insights, see [Firewall Insights categories and states](https://docs.cloud.google.com/network-intelligence-center/docs/firewall-insights/concepts/insights-categories-states).

For a list of firewall usage metrics, see [View Firewall Insights metrics](https://docs.cloud.google.com/network-intelligence-center/docs/firewall-insights/how-to/view-metrics).

## Required roles and permissions

To get the permission that you need to configure observation period and refresh cycle, ask your administrator to grant you the [Firewall Recommender Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/recommender#recommender.firewallAdmin) (`roles/recommender.firewallAdmin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the `recommender.computeFirewallInsightTypeConfigs.update` permission, which is required to configure observation period and refresh cycle. 

You might also be able to get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Configure observation period

For some insights, you can configure an _observation period_ —the time interval the insight covers. For example, you can configure the observation period for overly permissive and `deny` rule insights. The default observation window is six weeks, and you can configure the observation period between seven days to one year. 

For example, if you set the observation period for `deny` rule insights to two months, when you review the list of `deny` rules with hits after the observation period, Firewall Insights shows you only those that had hits during the past two months. Suppose you later change the observation period to one month; Firewall Insights might identify a different number of rules because it would analyze a shorter time interval.

When reviewing insights and configuring observation periods, be aware of the following:

  * When you configure the observation period for `deny` rules with hits, Firewall Insights updates the insight results immediately.

  * When you update the observation period for overly permissive rule insights, Firewall Insights can take up to 48 hours to update existing results. In the interim, the observation period for existing results matches the previously configured observation period.

  * For overly permissive insights, if the insight identified no firewall rules, Firewall Insights does not display the observation period to identify the insights used.

  * Shadowed rule insights do not have an observation period because they do not evaluate historical data. Shadowed rule analysis evaluates your existing firewall rule configuration every 24 hours.

  * Traffic log data from the last 24 hours might not be included when generating insights.




###  Console 

Configure an observation period:

  1. In the Google Cloud console, go to the **Firewall Insights** page.

[Go to Firewall Insights](https://console.cloud.google.com/net-intelligence/firewalls)

  2. Click **Configuration**.

  3. Click **Observation period**.

  4. As appropriate, set the **Observation period** drop-down list to the appropriate time for each of the following:

     * **Overly permissive rule insights**

     * **Deny rule insights**




###  API 

To set the observation period for `deny` rules with hits, you must use the Google Cloud console. However, you can use the Recommender API to set the observation period for overly permissive rule insights. You can also use the API to enable insights and to retrieve configuration details.

To set the observation period for overly permissive rules insights, use the [`updateConfig` method](https://docs.cloud.google.com/recommender/docs/reference/rest/v1beta1/projects.locations.insightTypes/updateConfig).

To use the `updateConfig` method, set values for all of its parameters. Also specify whether shadowed rule insights and overly permissive rule insights are enabled or disabled.

To make this type of update, use the following request.
    
    
      PATCH https://recommender.googleapis.com/v1beta1/projects/PROJECT_ID/locations/global/insightTypes/google.compute.firewall.Insight/config
      {
        "name": "projects/PROJECT_ID/locations/global/insightTypes/google.compute.firewall.Insight/config",
          "insightTypeGenerationConfig": {
            "params": {
              "observation_period": "OBSERVATION_PERIOD_OVERLY_PERMISSIVE",
              "enable_shadowed_rule_insights": ENABLEMENT_SHADOWED,
              "enable_overly_permissive_rule_insights": ENABLEMENT_OVERLY_PERMISSIVE
             }
           },
        "etag": "\"ETAG\"",
      }
    

Replace the following values:

  * PROJECT_ID: the ID of your project
  * OBSERVATION_PERIOD_OVERLY_PERMISSIVE: the time, in seconds, of the observation period for overly permissive rules insights
  * ENABLEMENT_SHADOWED: a boolean value that represents whether shadowed rule insights are enabled
  * ENABLEMENT_OVERLY_PERMISSIVE: a boolean value that represents whether overly permissive rule insights are enabled
  * ETAG: the [IAM policy etag](https://docs.cloud.google.com/iam/docs/policies) value; to retrieve the etag value, use the `getConfig` method, as described in the following section



#### Example
    
    
      PATCH https://recommender.googleapis.com/v1beta1/projects/PROJECT_ID/locations/global/insightTypes/google.compute.firewall.Insight/config
      {
        "name": "projects/PROJECT_ID/locations/global/insightTypes/google.compute.firewall.Insight/config",
          "insightTypeGenerationConfig": {
            "params": {
              "observation_period": "604800s",
              "enable_shadowed_rule_insights": true,
              "enable_overly_permissive_rule_insights": true
             }
           },
        "etag": "\"ETAG\"",
      }
    

####  Retrieve configuration details

To retrieve details about how Firewall Insights is configured, use the [`getConfig` method](https://docs.cloud.google.com/recommender/docs/reference/rest/v1beta1/projects.locations.insightTypes/getConfig) as shown in the following example. 
    
    
      GET https://recommender.googleapis.com/v1beta1/projects/PROJECT_ID/locations/global/insightTypes/google.compute.firewall.Insight/config
    

## Schedule a custom refresh cycle

Set up a refresh cycle to generate shadowed rule insights for your project.

You can schedule the refresh cycle to begin on a specified date and customize the cycle frequency. The default cycle frequency is one day (24 hours).

###  Console 

Configure a custom refresh cycle for insights:

  1. In the Google Cloud console, go to the **Firewall Insights** page.

[Go to Firewall Insights](https://console.cloud.google.com/net-intelligence/firewalls)

  2. Click **Configuration**.

  3. Click **Enablement**.

  4. To enable shadowed rule insights, click the toggle.

  5. In the **Start on** field, enter a date from which the custom refresh cycle starts.

  6. In the **Repeat every** field, select the frequency for the refresh cycle starting from the cycle start date:

     * **day** : every 24 hours
     * **week** : every week on the days you select
     * **month** : every month
     * **quarter** : every quarter

The new insight generation schedule takes effect 24 hours after saving changes to the schedule.




## What's next

  * [View and understand Firewall Insights](https://docs.cloud.google.com/network-intelligence-center/docs/firewall-insights/how-to/view-understand-insights)
  * [Review and optimize firewall rules](https://docs.cloud.google.com/network-intelligence-center/docs/firewall-insights/how-to/review-optimize)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
