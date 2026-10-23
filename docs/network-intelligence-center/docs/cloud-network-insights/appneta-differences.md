---
url: https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/appneta-differences/
title: Differences between Google Cloud and AppNeta \u00a0|\u00a0 Network Intelligence Center - Cloud Network Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:37:18.256413+00:00
---

# Differences between Google Cloud and AppNeta  |  Network Intelligence Center - Cloud Network Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/appneta-differences/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Cloud Network Insights ](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights)
  * [ Guides ](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/overview)



#  Differences between Google Cloud and AppNeta Stay organized with collections  Save and categorize content based on your preferences. 

This page describes key differences between Google Cloud and AppNeta by Broadcom.

If you already have an AppNeta instance as part of your network monitoring implementation, you can't combine your current AppNeta monitoring solution with Cloud Network Insights. Cloud Network Insights is associated with a unique AppNeta instance and can't be associated with a different instance.

## Differences in identity and access management

Google's [Identity and Access Management](https://docs.cloud.google.com/iam/docs/overview) is used to grant roles in AppNeta. Roles and permissions granted in Google Cloud automatically map and grant roles in your AppNeta instance.

The following table lists the [predefined Google Cloud roles and permissions](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/access-control) that grant the corresponding AppNeta roles. Users can be granted either the Google Cloud role or the permission.

**Predefined Google Cloud Role and Permissions** | **AppNeta Role**  
---|---  
Cloud Network Insights Admin  
(`roles/networkmanagement.CloudNetworkInsightsAdmin`) **Permissions** :

  * `productrequirementsservice.requirements.record`
  * `networkmanagement.googleapis.com/providers.create`

| Admin  
Cloud Network Insights Editor  
(`roles/networkmanagement.CloudNetworkInsightsEditor`) **Permissions** : `networkmanagement.providers.create` | Editor  
Cloud Network Insights Viewer  
(`roles/networkmanagement.CloudNetworkInsightsViewer`) **Permissions** : `networkmanagement.providers.list` | Viewer  
  
## Differences between alarms and alerts

In Cloud Network Insights, AppNeta uses alarms and alarm rules to generate events and logs that are sent to [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview). Those logs can then be used to create [alerts and notifications](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/set-up-alerts) in Cloud Network Insights.

Some of Google Cloud's logs and AppNeta's logs are different. The following table maps the difference between alarm log severity.

**Google** | **AppNeta**  
---|---  
Notice | Warning  
Warning | Minor  
Error | Major  
Critical | Critical  
  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
