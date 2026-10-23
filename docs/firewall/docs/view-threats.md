---
url: https://docs.cloud.google.com/firewall/docs/view-threats/
title: View threats \u00a0|\u00a0 Cloud Next Generation Firewall \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:13:11.361279+00:00
---

# View threats  |  Cloud Next Generation Firewall  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firewall/docs/view-threats/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NGFW ](https://docs.cloud.google.com/firewall/docs)
  * [ Guides ](https://docs.cloud.google.com/firewall/docs/about-firewalls)



Send feedback 

#  View threats Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to view threats detected by the firewall endpoint for the intercepted traffic by using the Google Cloud console.

Firewall endpoints perform signature-based threat detection and prevention on the intercepted traffic from your virtual machine (VM) instances. Cloud Next Generation Firewall (Cloud NGFW) provides default threat signatures, supported threat severity levels, and threat overrides that you use to identify malicious activity and prevent network attacks. Use the **Threat** page to view threats detected in your network during a specific timeframe.

To view a summary of the threats observed during a specific period in your network, go to the Cloud NGFW [Dashboard](https://console.cloud.google.com/net-security/firewall-manager/dashboard/cards).

To learn more about threats, see [Threat signatures overview](https://docs.cloud.google.com/firewall/docs/about-threats).

## Roles and permissions

To get permissions that you need to view the threat page, ask your administrator to grant you the necessary Identity and Access Management (IAM) roles on your organization. For more information about granting roles, see [Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## View threats

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your organization.

**Permissions**

  * `networksecurity.securityProfiles.create`



**Roles**

  * Compute Network Admin (`roles/compute.networkAdmin`) 



###  Console 

  1. In the Google Cloud console, go to the **Threats** page.

[Go to Threats](https://console.cloud.google.com/net-security/threats/list)

  2. If necessary, select your Google Cloud project.

  3. Select the timeframe for which you want to view the threats detected. You can select the duration from 1 hour to 30 days. Threats detected during the selected timeframe are displayed.

  4. Optional: To further refine the listed threats, select one or more of the following filters:

     * Severity
     * Alert time on
     * Alert time before
     * Alert time after
     * Threat name
     * Threat type
  5. To view logs for a specific threat, click **View audit log** next to the threat name. The Cloud Logging page appears that displays the detailed logs for the selected threat. To understand the threat log structure, see [Threat logs](https://docs.cloud.google.com/firewall/docs/threat_logs).




## What's next

  * [Create and manage threat prevention security profiles](https://docs.cloud.google.com/firewall/docs/configure-security-profiles)
  * [Create and manage security profile groups](https://docs.cloud.google.com/firewall/docs/configure-security-profile-groups)
  * [Create and manage firewall endpoints](https://docs.cloud.google.com/firewall/docs/configure-firewall-endpoints)
  * [Create and manage firewall endpoint associations](https://docs.cloud.google.com/firewall/docs/configure-firewall-endpoint-associations)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
