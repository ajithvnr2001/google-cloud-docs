---
url: https://docs.cloud.google.com/compute/docs/monitor-security-risks-console/
title: Monitor security risks with Security Command Center \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:27:16.105590+00:00
---

# Monitor security risks with Security Command Center  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/monitor-security-risks-console/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Monitor security risks with Security Command Center Stay organized with collections  Save and categorize content based on your preferences. 

[Security Command Center](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview) helps you prevent, detect, and respond to security risks across Google Cloud and other cloud providers. When you enable Security Command Center, you can use the Google Cloud console to view the highest-priority security risks that affect your Compute Engine resources. 

This document explains how to activate Security Command Center and view the dashboard that it provides for your Compute Engine resources. 

## Activate Security Command Center

To analyze your Compute Engine resources with Security Command Center, you must [activate Security Command Center](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview). This section explains the service tiers that Security Command Center offers and explains how to activate the Standard or Premium tier in your project. 

### Service tiers

When you activate Security Command Center, you choose which [service tier](https://docs.cloud.google.com/security-command-center/docs/service-tiers) to activate: 

  * **Standard**. Enables basic scanning for risks and misconfigurations. Applies to your Google Cloud resources. 
  * **Premium**. Provides enhanced scanning for risks, vulnerabilities, and misconfigurations, as well as security posture management, attack paths, threat detection, and compliance monitoring. Applies to your Google Cloud resources. 
  * **Enterprise**. Offers a complete cloud-native application protection platform (CNAPP) solution, including automated case management and remediation playbooks. Applies to your Google Cloud resources, as well as resources hosted by other cloud providers. 



You can use the Standard tier at no additional charge. To learn about pricing for the Premium and Enterprise tiers, see [Security Command Center pricing](https://docs.cloud.google.com/security-command-center/pricing). 

**Note** : This page explains how to activate the Standard or Premium service tier for your project. Some Security Command Center features require you to [activate the Enterprise tier](https://docs.cloud.google.com/security-command-center/docs/activate-enterprise-tier) or [activate the Standard or Premium tier](https://docs.cloud.google.com/security-command-center/docs/activate-scc-for-an-organization) for your entire organization. 

### Activate Security Command Center in your project

To activate the Security Command Center Standard or Premium tier in your project, do the following: 

  1. In the Google Cloud console, go to **Compute Engine Overview**.

[Go to Compute Engine Overview](https://console.cloud.google.com/projectselector2/compute/overview?supportedpurview=project)

  2. Look for a pane titled **Sample security findings**. 

This pane shows examples of the types of security findings that you might see after you enable Security Command Center. These examples don't represent actual security issues in your project. 

If you see a pane titled **Top security findings** , then Security Command Center is already activated. You can skip the remaining steps. 

  3. In the **Sample security findings** pane, click **Turn on security scanning for free**. The activation pane opens. 
  4. Optional: To choose a different service tier, find the service tier that you want to enable, and then click **Select** for that tier. 
  5. Click **Enable**. 



After you activate Security Command Center, it starts to analyze, or scan, your resources for Compute Engine and other Google Cloud services. This initial scan is [usually complete within minutes or hours](https://docs.cloud.google.com/security-command-center/docs/concepts-scan-latency-overview#scan_latency). 

## Review high-priority security risks

After Security Command Center [completes an initial scan](https://docs.cloud.google.com/security-command-center/docs/concepts-scan-latency-overview#scan_latency) of your Compute Engine resources, you can review high-priority _findings_ for your resources in the Google Cloud console. Each finding represents a security risk. 

To review high-priority findings for your Compute Engine resources, do the following: 

  1. In the Google Cloud console, go to **Compute Engine Overview**. 

[Go to Compute Engine Overview](https://console.cloud.google.com/projectselector2/compute/overview?supportedpurview=project)

  2. Find the **Top security findings** pane. This pane lists the most important types of findings that affect your Compute Engine resources. 

     * To view a specific subset of high-priority findings, select **By resource type** or **By category** , and then select the resource type or category that you want to view. 
     * To view all of your findings, click arrow_forward **View all findings**. 



## Get an overview of other risks

In addition to an overview of high-priority risks, you can use the Google Cloud console to view other types of security risks that affect your Compute Engine resources. 

To get an overview of these additional risks, in the Google Cloud console, go to **Security Risk Overview**. 

[Go to Security Risk Overview](https://console.cloud.google.com/projectselector2/compute/security?supportedpurview=project)

This page shows the following information: 

Top security findings
    

This table lists the most important types of findings that affect your Compute Engine resources. 

All vulnerability findings over time
    

This chart shows the total number of Security Command Center findings over time for your Compute Engine instances. Findings are categorized by severity. 

To change the date range, click the list, and then select a new value. 

Top CVE findings on your virtual machines
    

This heatmap shows the number of Common Vulnerabilities and Exposures (CVEs) that affect your Compute Engine instances, grouped by the potential impact and exploitability of each CVE. 

Top CVE findings
    

This table lists the most severe CVEs that affect your Compute Engine instances, including the exploitability and impact of each CVE. 

Boost your security knowledge
    

This pane provides links to more information about Security Command Center and strategies for mitigating vulnerabilities. 

To get more details, click the links in each pane. 

## What's next

  * [Security Command Center overview](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)
  * [Security Command Center service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)
  * [Security Command Center pricing](https://docs.cloud.google.com/security-command-center/pricing)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
