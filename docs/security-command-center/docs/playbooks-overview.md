---
url: https://docs.cloud.google.com/security-command-center/docs/playbooks-overview/
title: Playbooks overview \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:14:16.989876+00:00
---

# Playbooks overview  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/playbooks-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Playbooks overview Stay organized with collections  Save and categorize content based on your preferences. 

Enterprise (Deprecated) [service tier](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This document provides an overview of the playbooks available to you in the Enterprise tier of Security Command Center.

## Overview

In Security Command Center, use playbooks to explore and enrich [alerts](https://docs.cloud.google.com/security-command-center/docs/working-with-alerts), obtain more information about findings, get recommendations about excess permissions in your organization, and automate responses to threats, vulnerabilities, and misconfigurations. When you integrate with ticketing systems, playbooks help you focus on relevant posture findings while ensuring the synchronization between cases and tickets.

The Enterprise tier of Security Command Center provides you with the following playbooks:

  * Threat response playbooks: 
    * **AWS Threat Response Playbook**
    * **Azure Threat Response Playbook**
    * **GCP Threat Response Playbook**
    * **Google Cloud – Execution – Binary or Library Loaded Executed**
    * **Google Cloud – Execution – Cryptomining**
    * **Google Cloud – Execution – Malicious URL Script or Shell Process**
    * **Google Cloud – Malware – Indicators**
    * **Google Cloud – Persistence – IAM Anomalous Grant**
    * **Google Cloud – Persistence – Suspicious Behaviour**
  * Posture findings playbooks: 
    * **Posture – Toxic Combination Playbook**
    * **Posture Findings – Generic**
    * **Posture Findings – Generic – VM Manager** (disabled by default)
    * **Posture Findings With Jira** (disabled by default)
    * **Posture Findings With ServiceNow** (disabled by default)
  * Playbook for handling the IAM recommendations: 
    * **IAM Recommender Response** (disabled by default)



The playbooks disabled by default are optional and require you to enable them manually before using them.

On the **Cases** Security Operations console page, findings become _case alerts_. Alerts trigger attached playbooks to execute the configured set of actions for retrieving as much information about alerts as possible, remediating the threat, and, depending on the playbook type, provide the required information to create tickets or manage the toxic combinations and IAM recommendations.

## Threat response playbooks

You can execute the threat response playbooks to analyze threats, enrich findings using different sources, and suggest and apply a remediation response. Threat response playbooks use multiple services like Google SecOps, Security Command Center, Cloud Asset Inventory, and products like VirusTotal and Mandiant Threat Intelligence to help you obtain as much context about threats as possible. The playbooks can help you understand whether the threat in the environment is a true positive or a false positive and what is the optimal response for it.

To ensure that the threat response playbooks provide you with the full information about threats, see [Advanced configuration for threat management](https://docs.cloud.google.com/security-command-center/docs/advanced-configuration-threat-management).

The **GCP Threat Response Playbook** playbook executes a generic response to threats that originate from Google Cloud.

The **AWS Threat Response Playbook** playbook executes a generic response to threats that originate from Amazon Web Services.

The **Azure Threat Response Playbook** playbook executes a generic response to threats that originate from Microsoft Azure. To remediate threats, the playbook enriches the information from Microsoft Entra ID and supports responding to emails.

The **Google Cloud – Malware – Indicators** playbook can help you respond to malware-related threats and enrich the indicators of compromise (IoC) and impacted resources. As part of the remediation, the playbook suggests that you stop a suspicious instance or disable a service account.

The **Google Cloud – Execution – Binary or Library Loaded Executed** playbook can help you handle a suspicious new binary or library in a container. After enriching the information about the container and the associated service account, the playbook sends an email to an assigned security analyst for further remediation.

The **Google Cloud – Execution – Binary or Library Loaded Executed** playbook works with the following findings:

  * Added Binary Executed
  * Added Library Loaded
  * Execution: Added Malicious Binary Executed
  * Execution: Added Malicious Library Loaded
  * Execution: Built in Malicious Binary Executed
  * Execution: Modified Malicious Binary Executed
  * Execution: Modified Malicious Library Loaded



For more information about the findings that the playbook focuses on, see [Container Threat Detection overview](https://docs.cloud.google.com/security-command-center/docs/concepts-container-threat-detection-overview).

The **Google Cloud – Execution – Cryptomining** playbook can help you detect cryptocurrency mining threats in Google Cloud, enrich information about impacted assets and service accounts, investigate the activity detected on related resources for vulnerabilities and misconfigurations. As a threat response, the playbook suggests that you stop an impacted compute instance or disable a service account.

The **Google Cloud – Execution – Malicious URL Script or Shell Process** playbook can help you handle a suspicious activity in a container and perform a dedicated resource enrichment. As a threat response, the playbook sends email to an assigned security analyst.

The **Google Cloud – Execution – Malicious URL Script or Shell Process** playbook works with the following findings:

  * Malicious Script Executed
  * Malicious URL Observed
  * Reverse Shell
  * Unexpected Child Shell



For more information about the findings that the playbook focuses on, see [Container Threat Detection overview](https://docs.cloud.google.com/security-command-center/docs/concepts-container-threat-detection-overview).

The **Google Cloud – Malware – Indicators** playbook can help you handle the malware-related threats detected by Security Command Center and investigate the potentially compromised instances.

The **Google Cloud – Persistence – IAM Anomalous Grant** playbook can help you investigate an identity or a service account that granted suspicious permissions to a principal along with the set of granted permissions, and identify the principal in question. As a threat response, the playbook suggests that you disable a suspicious service account or, if it's not a service account that is associated with a finding but a user, sends email to an assigned security analyst for further remediation.

For more information about the rules used in the playbook, see [Container Threat Detection overview](https://docs.cloud.google.com/security-command-center/docs/findings/threats/iam-anomalous-grant).

The **Google Cloud – Persistence – Suspicious Behaviour** playbook can help you handle the specific subsets of suspicious user-related behavior like signing in using a new API method. As a threat response, the playbook sends email to an assigned security analyst for further remediation.

For more information about the rules used in the playbook, see [Overview of Event Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview#rules).

## Posture findings playbooks

Use the posture findings playbooks to analyze the multicloud posture findings, enrich them using the Security Command Center and Cloud Asset Inventory, and highlight the received relevant information in the [Case Overview tab](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/whats-on-the-case-overview-tab). The posture findings playbooks ensure that the synchronization for findings and cases works as expected.

The **Posture – Toxic Combination Playbook** playbook can help you enrich toxic combinations and set the necessary information like case tags that Security Command Center requires to track and process the toxic combinations and related findings.

The **Posture Findings – Generic – VM Manager** playbook is a lightweight version of the **Posture Findings – Generic** playbook that doesn't contain Cloud Asset Inventory enrichment steps and only works for the VM Manager findings.

By default, only the **Posture Findings – Generic** playbook is enabled. If you integrate with Jira or ServiceNow, disable the **Posture Findings – Generic** playbook and enable the one that is relevant for your ticketing system. To learn more about configuring Jira or ServiceNow, see [Integrate Security Command Center Enterprise with ticketing systems](https://docs.cloud.google.com/security-command-center/docs/integrate-ticketing-systems).

In addition to investigating and enriching posture findings, the **Posture Findings With Jira** and **Posture Findings With ServiceNow** playbooks ensure that the resource owner value (email address) stated in a finding is valid and assignable in the respective ticketing system. Optional posture findings playbooks collect information required to create new tickets and update existing tickets when new alerts are ingested into existing cases.

## Playbook for handling the IAM recommendations

Use the **IAM Recommender Response** playbook to automatically address and apply the recommendations suggested by the IAM recommender. This playbook provides no enrichment and doesn't create tickets even when you have integrated with a ticketing system.

For more details about enabling and using the **IAM Recommender Response** playbook, see [Automate IAM recommendations using playbooks](https://docs.cloud.google.com/security-command-center/docs/automate-recommendations-playbook).

## What's next?

To learn more about playbooks, refer to the following pages in the Google SecOps documentation:

  * [What's on the Playbook's page?](https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/whats-on-the-playbooks-screen)
  * [Use flows in playbooks](https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/using-flows-in-playbooks)
  * [Use actions in playbooks](https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/using-actions-in-playbooks)
  * [Work with playbook blocks](https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/working-with-playbook-blocks)
  * [Attach playbooks to an alert](https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/attaching-playbooks-to-an-alert)
  * [Assign actions and playbook blocks](https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/assign-actions-and-playbook-blocks)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
