---
url: https://docs.cloud.google.com/network-intelligence-center/docs/firewall-insights/how-to/enable-api-features/
title: Enable APIs and features \u00a0|\u00a0 Network Intelligence Center - Firewall Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:35:58.081740+00:00
---

# Enable APIs and features  |  Network Intelligence Center - Firewall Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/firewall-insights/how-to/enable-api-features/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Firewall Insights ](https://docs.cloud.google.com/network-intelligence-center/docs/firewall-insights)
  * [ Guides ](https://docs.cloud.google.com/network-intelligence-center/docs/firewall-insights/how-to/using-firewall-insights)



Send feedback 

#  Enable APIs and features Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to enable the APIs and features required to use Firewall Insights.

Before using Firewall Insights, select a project, ensure that you have the required roles and permissions, and then complete the required setup tasks. For more information about the first two steps, see [Roles and permissions](https://docs.cloud.google.com/network-intelligence-center/docs/firewall-insights/concepts/roles-permissions).

The setup tasks vary based on the metrics and insights that you want to use. For details, see the following table.

Task | All metrics | Shadowed rule insights | Overly permissive rule insights | Deny rules with hits  
---|---|---|---|---  
Enable the Firewall Insights API | ✔ | ✔ | ✔ | ✔  
Enable Firewall Rules Logging | ✔ |  | ✔ | ✔  
Enable the Recommender API |  | ✔ | ✔ |   
Enable this type of insight |  | ✔ | ✔ |   
Configure an observation period |  |  | ✔ | ✔  
Schedule a custom refresh cycle |  | ✔ |  |    
The following sections describe how to enable the APIs and features.

## Enable the Firewall Insights API

Before performing any tasks using Firewall Insights, you must enable the Firewall Insights API.  To enable the API, you can use the following steps or the [Google Cloud console API Library](https://console.cloud.google.com/apis/library?project=_), described in [Enabling APIs](https://docs.cloud.google.com/apis/docs/getting-started#enabling_apis) in the Cloud APIs documentation.

###  Console 

  1. In the Google Cloud console, go to the **Firewall Insights** page. [Go to Firewall Insights](https://console.cloud.google.com/net-intelligence/firewalls)
  2. On the **Firewall Insights API** page, click **Enable**.



###  gcloud 

Use the following command:
    
    
    gcloud services enable firewallinsights.googleapis.com
    

## Enable Firewall Rules Logging

If you want to view any of the following, you must [enable Firewall Rules Logging](https://docs.cloud.google.com/vpc/docs/using-firewall-rules-logging#enable):

  * Metrics about firewall rules
  * Insights about overly permissive rules or `deny` rules; these insights are known collectively as _log-based insights_

Firewall Insights produces metrics and log-based insights only for those rules that have logging enabled. For more information, see the [Firewall Rules Logging overview](https://docs.cloud.google.com/vpc/docs/firewall-rules-logging).

## Enable the Recommender API

Enable the Recommender API to do the following:

  * Use shadowed rule insights
  * Use overly permissive rule insights
  * Retrieve any data by making API calls or by using the Google Cloud CLI



###  Console 

  1. In the Google Cloud console, go to the **Enable access to API** page. [Enable access to API](https://console.cloud.google.com/apis/enableflow?apiid=recommender.googleapis.com&_ga=2.158401658.1767111083.1627410912-1550826818.1627403508)
  2. Make sure that the correct project is selected, and then click **Next**.
  3. Click **Enable**.



###  gcloud 

Use the following command:
    
    
    gcloud services enable recommender.googleapis.com
    

## Enable shadowed rule or overly permissive rule insights

Firewall Insights does not generate shadowed or overly permissive rule insights unless you actively enable these features on the Firewall Insights page. After you enable either feature, you might have to wait up to 48 hours to see the generated insights. When you create or update a firewall rule, you might have to wait up to ten days to see [machine learning predictions](https://docs.cloud.google.com/network-intelligence-center/docs/firewall-insights/concepts/insights-categories-states#machine-learning-predictions) for overly permissive rule insights. In the meantime, you can view insights based on data gathered from [Firewall Rules Logging](https://docs.cloud.google.com/vpc/docs/firewall-rules-logging). **Note:** If you enable these features and decide to disable them later, consider downloading the insights that Firewall Insights has generated. If you disable either feature, Firewall Insights does not save the insights previously generated for your project, even if you enable the feature later.

###  Console 

  1. In the Google Cloud console, go to the **Firewall Insights** page. [Go to Firewall Insights](https://console.cloud.google.com/net-intelligence/firewalls)
  2. Click **Configuration**.
  3. Click **Enablement**.
  4. As appropriate, move the slider to **Enabled** or **Disabled** for one or both of the following:
     * **Shadowed rule insights**
     * **Overly permissive rule insights**



###  API 

You can use the Recommender API to enable or disable shadowed rule insights and overly permissive rule insights. You can also use the API to set the observation period for overly permissive rule insights and retrieve configuration details. To enable shadowed rule insights and overly permissive rule insights, use the [`updateConfig` method](https://docs.cloud.google.com/recommender/docs/reference/rest/v1beta1/projects.locations.insightTypes/updateConfig). To use the `updateConfig` method, you must set values for all of its parameters. When you enable or disable insights, you must also configure the observation period for overly permissive insights. To make this type of update, use the following request.
    
    
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
    

## Configure an observation period

For some insights, you can configure an observation period, or the time interval that the insight covers. For more information, see [Configure observation period](https://docs.cloud.google.com/network-intelligence-center/docs/firewall-insights/how-to/configure-observation-period#observation-period) in _Set up observation period and refresh cycle_.

## Schedule a custom refresh cycle

You can set up a refresh cycle to generate shadowed rule insights for your project. For more information, see [Schedule a custom refresh cycle](https://docs.cloud.google.com/network-intelligence-center/docs/firewall-insights/how-to/configure-observation-period#insight-schedule) in _Set up observation period and refresh cycle_.

## What's next

  * [Firewall Insights categories and states](https://docs.cloud.google.com/network-intelligence-center/docs/firewall-insights/concepts/insights-categories-states)
  * [View and understand Firewall Insights](https://docs.cloud.google.com/network-intelligence-center/docs/firewall-insights/how-to/view-understand-insights)

Send feedback  Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates. Last updated 2026-10-22 UTC. Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
