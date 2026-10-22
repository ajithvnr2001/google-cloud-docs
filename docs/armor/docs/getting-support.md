---
url: https://docs.cloud.google.com/armor/docs/getting-support/
title: Getting support \u00a0|\u00a0 Google Cloud Armor \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:37:56.521755+00:00
---

# Getting support  |  Google Cloud Armor  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/armor/docs/getting-support/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Google Cloud Armor ](https://docs.cloud.google.com/armor/docs)
  * [ Support ](https://docs.cloud.google.com/armor/docs/support)



Send feedback 

#  Getting support Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the support options available for Google Cloud Armor. Use these resources to resolve technical issues, request proactive assistance, and connect with other users.

Before you begin, note the following prerequisites:

  * To receive formal technical support, you must have an active Google Cloud support package. For more information, see [Cloud Customer Care](https://docs.cloud.google.com/support).
  * To get support during an active distributed denial-of-service (DDoS) attack, your support package must be [eligible for DDoS response support](https://docs.cloud.google.com/armor/docs/armor-enterprise-overview#ddos-response-support).



## Get a Google support package

If you have an eligible support package, you can request a DDoS posture review or get support during an active DDoS attack. The following sections describe how to submit these support cases.

### Request a DDoS posture review

To request a DDoS posture review, complete the following steps:

  1. In the Google Cloud console, go to the **Support** page.

[Go to Support](https://console.cloud.google.com/support/cases)

  2. Select the project for which you would like to open a DDoS Response case.

  3. Select **Cases**.

  4. Click **Create Case**.

  5. See the following table, then complete the required fields and submit the form. The table provides a template to help facilitate DDoS support cases. For each topic in the **Topic** column, provide the information as described in the **Information** column:


Topic | Information  
---|---  
Case title | Google Cloud Armor DDoS posture review  
Case priority | P4  
Organization name | The name of your organization  
Organization ID | The ID number of your organization  
Critical projects | The names and project IDs of the projects that you want the support team to review  
  
### Get support for a DDoS case

If your infrastructure is under active attack, you can open a support case for assistance with the attack. For customers who aren't eligible for [DDoS response support](https://docs.cloud.google.com/armor/docs/armor-enterprise-overview#ddos-response-support), the Cloud Customer Care team provides assistance during active DDoS attacks on a best-effort basis including rule debugging and addressing specific concerns with existing policies. The Cloud Customer Care team isn't able to provide general recommendations about policy settings nor can they optimize your service's protection against active attacks.

To open a DDoS response case, complete the following steps:

  1. In the Google Cloud console, go to the **Support** page.

[Go to Support](https://console.cloud.google.com/support/cases)

  2. Select the project for which you would like to open a DDoS Response case.

  3. Select **Cases**.

  4. Click **Create Case**.

  5. See the following table, then complete the required fields and submit the form. The table provides a template to help facilitate DDoS support cases. For each topic in the **Topic** column, provide the information as described in the **Information** column:


Topic | Information  
---|---  
Case title | DDoS attack on FrontEndResourceName  
Case priority | One of the following: 

  * P1 for an active DDoS attack
  * P2 for any urgent proactive support
  * P3 for non-urgent proactive or post-attack support

  
Case summary | Provide a short summary of the active or expected attack. The information that you provide helps us respond more quickly and comprehensively. Highlight the following key areas:

  * Is your service running in a degraded state, or is it completely unusable?
  * Has the attack had an impact on internal resources or only frontend access?
  * If there is an impact on internal resources, what types of resources are affected?

  
Project ID | The project name under attack  
Project number | The project number under attack  
Type of resource under attack | One of the following: 

  * Application Load Balancer
  * Classic Application Load Balancer
  * Regional external passthrough Network Load Balancer
  * VM + external IP address

  
**Resource information:** Forwarding rule nameFrontend IP address |    
The name of the forwarding rule under attack The external IP address of the resource under attack  
**Attack information:** Attack stateAttack start time Attack end timeCurrent attack QPS |    
Future, active, intermittent, or stopped As accurate as possible, ideally in Pacific or UTC As accurate as possible, ideally in Pacific or UTC As accurate as possible, in thousands of queries per second  
Service information (optional, but more information is better)  
Peak attack QPS | As accurate as possible, in thousands of queries per second  
Normal QPS (approximate) | As accurate as possible, in thousands of queries per second  
Normal bandwidth (approximate) | As accurate as possible, in Mb/Gb/Tb per second  
Normal latency (approximate) | As accurate as possible, in milliseconds  
Current latency | As accurate as possible, in milliseconds  
Baseline and current backend resource utilization | Resource utilization information for any relevant internal services, such as: 

  * CPU
  * Memory
  * Disk
  * Database latency or other performance metrics

  
  
## Get support from the community

You can get support from the community through various channels.

### Ask a question on Stack Overflow

Ask a question about Cloud Armor on [Stack Overflow](http://stackoverflow.com/questions/tagged/google-cloud-armor). Use the tag `google-cloud-armor` for questions about Cloud Armor. This tag not only receives responses from the Stack Overflow community, but also from Google engineers, who monitor the tag and offer unofficial support.

### Discuss Cloud Armor

Visit the Google Cloud [Slack community](https://googlecloud-community.slack.com/) to discuss Cloud Armor and other Google Cloud products. If you haven't already joined, [use this form to sign up](https://join.slack.com/t/googlecloud-community/shared_invite/zt-3icuwfdvq-eq_58LqmOoCNc16mpZcaNA). 

## File bugs or feature requests

From the Cloud Armor documentation, click **Send feedback** near the top right of the page or at the bottom of the page. This opens a feedback form. Your comments are reviewed by the Cloud Armor team.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
