---
url: https://docs.cloud.google.com/network-intelligence-center/docs/firewall-insights/support/troubleshooting/
title: Troubleshoot Firewall Insights \u00a0|\u00a0 Network Intelligence Center - Firewall Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:56:13.157127+00:00
---

# Troubleshoot Firewall Insights  |  Network Intelligence Center - Firewall Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/firewall-insights/support/troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Firewall Insights ](https://docs.cloud.google.com/network-intelligence-center/docs/firewall-insights)
  * [ Guides ](https://docs.cloud.google.com/network-intelligence-center/docs/firewall-insights/how-to/using-firewall-insights)



Send feedback 

#  Troubleshoot Firewall Insights Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to troubleshoot common issues with Firewall Insights.

## You do not see insights

In general, if you do not see insights, you should review the [Enable APIs and features](https://docs.cloud.google.com/network-intelligence-center/docs/firewall-insights/how-to/enable-api-features) page and ensure that you didn't miss an essential setup step. The following sections describe specific cases in more detail.

### You're not seeing insights about overly permissive rules or `deny` rules

If you can't see any insights about overly permissive rules or `deny` rules, you might need to do one of the following:

  * [Enable the Firewall Insights API](https://docs.cloud.google.com/network-intelligence-center/docs/firewall-insights/how-to/enable-api-features#enabling-api)
  * [Enable Firewall Rules Logging](https://docs.cloud.google.com/vpc/docs/using-firewall-rules-logging#enable)
  * [Enable overly permissive rule insights](https://docs.cloud.google.com/network-intelligence-center/docs/firewall-insights/how-to/enable-api-features#enabling-insights)



### You're not seeing any shadowed firewall rules

If you're unable to see any shadowed firewall rules, you might need to do one of the following:

  * [Enable the Firewall Insights API](https://docs.cloud.google.com/network-intelligence-center/docs/firewall-insights/how-to/enable-api-features#enabling-api)
  * [Enable shadowed rule insights](https://docs.cloud.google.com/network-intelligence-center/docs/firewall-insights/how-to/enable-api-features#enabling-insights)



You must enable the Firewall Insights API because it allows the Firewall Insights service to check the settings of your network, firewall, and virtual machine (VM) instances.

### You're not seeing metrics

In some cases, you might be unable to see Firewall Insights metrics. In this case, you might need to do one of the following:

  * [Enable the Firewall Insights API](https://docs.cloud.google.com/network-intelligence-center/docs/firewall-insights/how-to/enable-api-features#enabling-api)
  * [Enable Firewall Rules Logging](https://docs.cloud.google.com/vpc/docs/using-firewall-rules-logging#enable)



## Machine learning predictions don't appear

After you have enabled overly permissive insights, the machine learning model training and deployment take a few days. Therefore, it might take up to a week for predictions to be available.

## Firewall Insights still doesn't work

After you use all of the preceding solutions and still don't see firewall usage metrics or insights in your projects, make sure that you have permission to use Firewall Insights.

If you still have issues, contact [Support](https://docs.cloud.google.com/network-intelligence-center/docs/firewall-insights/support/getting-support). They will contact the Firewall Insights team to help resolve your issue.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
