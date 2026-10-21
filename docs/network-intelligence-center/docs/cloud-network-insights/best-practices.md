---
url: https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/best-practices/
title: Best practices for Cloud Network Insights \u00a0|\u00a0 Network Intelligence Center - Cloud Network Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:29:22.530540+00:00
---

# Best practices for Cloud Network Insights  |  Network Intelligence Center - Cloud Network Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Cloud Network Insights ](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights)
  * [ Guides ](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/overview)



#  Best practices for Cloud Network Insights Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the best practices for monitoring your networks with Cloud Network Insights.

## Enable in a dedicated Google Cloud project

While you can enable Cloud Network Insights in any Google Cloud project, we recommend creating a new, dedicated project for enabling Cloud Network Insights. You can monitor other Google Cloud projects by deploying a Monitoring Point to them.

We don't recommend adding a Monitoring Point to the project with Cloud Network Insights enabled.

## Deploy to the location you want to monitor

We recommend deploying one Monitoring Point to each location you want to monitor, such as on-premises networks, data centers, or Google Cloud regions.

In addition, what you want to monitor determines where you deploy Monitoring Points. For example, if you want to monitor the user experience for a web app, deploy a Monitoring Point in the same network environment. The closer you can get to deploying in the same subnet, location, VLAN, etc., the more closely you can monitor the user experience.

Learn more about [deployment Best Practices from AppNeta](https://techdocs.broadcom.com/us/en/ca-enterprise-software/it-operations-management/appneta-for-google-cloud-network-insights/GA/appliance-overview/appliance-where.html).

## Deploy a single-purpose container or VM first

Before deploying a Monitoring Point, deploy one of the following to the network that includes the application you want to monitor.

  * A container on a VM
  * A container on Google Kubernetes Engine
  * VM on KVM
  * VM on VmWare



Then install the Monitoring Point on the fresh container or VM.

We don't recommend installing a Monitoring Point directly with the workload you want to monitor. This isolates the Monitoring Point from other applications, preventing resource contention and ensuring more reliable monitoring results.

## Use multiple severities when creating alarm rules

When creating alarm rules, define multiple rules for the same metric. With multiple levels, you can create different notifications.

For example, create an alarm rule with a Minor severity level in AppNeta and a second alarm rule with a Major severity level. You can then create notifications that send information for the Minor alert to a chat and the information for the Major alert to a pager.

For more alarm best practices, see the [AppNeta documentation](https://techdocs.broadcom.com/us/en/ca-enterprise-software/it-operations-management/appneta-for-google-cloud-network-insights/GA/alarms-set-up/alarms-best-practices.html).

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
