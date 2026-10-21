---
url: https://docs.cloud.google.com/security-command-center/docs/cryptomining-detection-best-practices/
title: Cryptomining detection best practices \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:46:31.763079+00:00
---

# Cryptomining detection best practices  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/cryptomining-detection-best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Cryptomining detection best practices Stay organized with collections  Save and categorize content based on your preferences. 

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This page explains best practices for detecting cryptocurrency mining (cryptomining) attacks on Compute Engine virtual machines (VMs) in your Google Cloud environment.

These best practices also serve as the eligibility requirements for the Google Cloud Cryptomining Protection Program. For more information about the program, see the Security Command Center [Cryptomining Protection Program overview](https://cloud.google.com/security-command-center/cryptomining-protection-program).

## Activate the Premium or Enterprise tier of Security Command Center for your organization

The activation of the Premium tier or Enterprise tier of Security Command Center is a foundational element of detecting cryptomining attacks on Google Cloud.

Two threat detection services of the Premium and Enterprise tiers are critical for detecting cryptomining attacks: Event Threat Detection and VM Threat Detection.

Because cryptomining attacks can occur on any VM in any project within your organization, activating Security Command Center Premium or Enterprise for your entire organization with Event Threat Detection and VM Threat Detection enabled is both a best practice and a requirement of the Security Command Center Cryptomining Protection Program.

For more information, see either [Overview of activating Security Command Center](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview) or [Activate the Security Command Center Enterprise tier](https://docs.cloud.google.com/security-command-center/docs/activate-enterprise-tier).

## Enable key threat detection services on all projects

Enable the Event Threat Detection and VM Threat Detection detection services of Security Command Center on all projects in your organization.

Together, Event Threat Detection and VM Threat Detection detect events that can lead to a cryptomining attack (stage-0 events) and events that indicate an attack is in progress (stage-1 events). The specific events these detection services detect are described in the following sections.

For more information, see the following:

  * [Overview of Event Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview)
  * [Overview of VM Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-vm-threat-detection-overview)



### Enable stage-0 event detection

_Stage-0 events_ are events in your environment that often precede, or are the first step of, common cryptomining attacks.

Event Threat Detection, a detection service available with Security Command Center Premium or Enterprise, generates findings to alert you when it detects certain stage-0 events.

If you can detect and remediate these issues quickly, you can prevent many cryptomining attacks before you incur significant costs.

Event Threat Detection uses the following finding categories to alert you to these events:

  * [Account_Has_Leaked_Credentials](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#anomaly_detection): A finding in this category indicates that a service account key was leaked on GitHub. Acquiring service account credentials is a common precursor to cryptomining attacks.
  * [Evasion: Access from Anonymizing Proxy](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview#rules): A finding in this category indicates that a modification to a Google Cloud service originated from an IP address associated with the Tor network.
  * [Initial Access: Dormant Service Account Action](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview#rules): A finding in this category indicates that a dormant service account took action in your environment. Security Command Center uses Policy Intelligence to detect dormant accounts.



### Enable stage-1 event detection

_Stage-1 events_ are events that indicate that a cryptomining application program is running in your Google Cloud environment.

Both Event Threat Detection and VM Threat Detection generate Security Command Center findings to alert you when they detect certain stage-1 events.

Investigate and remediate these findings immediately to avoid incurring significant costs that are associated with the resource consumption of cryptomining applications.

A finding in any of the following categories indicates that a cryptomining application is running on a VM in one of the projects in your Google Cloud environment:

  * [Execution: Cryptomining YARA Rule](https://docs.cloud.google.com/security-command-center/docs/concepts-vm-threat-detection-overview#cryptocurrency-mining-threat-findings): Findings in this category indicate that VM Threat Detection detected a memory pattern, such as a proof-of-work constant, that is used by a cryptomining application.
  * [Execution: Cryptomining Hash Match](https://docs.cloud.google.com/security-command-center/docs/concepts-vm-threat-detection-overview#cryptocurrency-mining-threat-findings): Findings in this category indicate that VM Threat Detection detected a memory hash that is used by a cryptomining application.
  * [Execution: Combined Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-vm-threat-detection-overview#cryptocurrency-mining-threat-findings): Findings in this category indicate that VM Threat Detection detected both a memory pattern and a memory hash that are used by a cryptomining application.
  * [Malware: Bad IP](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview#rules): Findings in this category indicate that Event Threat Detection detected a connection to, or a lookup of, an IP address that is known to be used by cryptomining applications.
  * [Malware: Bad Domain](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview#rules): Findings in this category indicate that Event Threat Detection detected a connection to, or a lookup of, a domain that is known to be used by cryptomining applications.



## Enable Cloud DNS logging

To detect calls made by cryptomining applications to known bad domains, enable [Cloud DNS Logging](https://docs.cloud.google.com/dns/docs/monitoring#using_logging). Event Threat Detection processes the Cloud DNS logs and generates findings when it detects resolution of a domain that is known to be used for cryptomining pools.

## Integrate your SIEM and SOAR products with Security Command Center

Integrate Security Command Center with your existing security operations tools, such as your SIEM or SOAR products, to triage and respond to the Security Command Center findings for stage-0 and stage-1 events that indicate potential or actual cryptomining attacks.

If your security team does not use a SIEM or SOAR product, the team needs to familiarize themselves with working with Security Command Center findings in the Google Cloud console and how to set up finding notifications and exports by using Pub/Sub or the Security Command Center APIs to route findings for cryptomining attacks effectively.

For the specific findings that you need to export to your security operations tools, see Enable key threat detection services on all projects.

For information about how to integrate SIEM and SOAR products with Security Command Center, see [Setting up SIEM and SOAR integrations](https://docs.cloud.google.com/security-command-center/docs/how-to#setting-up-siem-and-soar-integrations).

For information about setting up finding notifications or exports, see the following information:

  * [Enabling real-time chat notifications](https://docs.cloud.google.com/security-command-center/docs/how-to-enable-real-time-notifications)
  * [Enable finding notifications for Pub/Sub](https://docs.cloud.google.com/security-command-center/docs/how-to-notifications)



## Designate your essential contacts for security notifications

So that your company can respond as quickly as possible to any security notifications from Google, specify to Google Cloud which teams in your company, such as IT security or operations security, should receive security notifications. When you specify a team, you enter its email address in [Essential Contacts](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts).

To ensure reliable delivery of these notifications over time, we strongly encourage teams to configure delivery to a mailing list, group, or other mechanism that ensures consistency of delivery and distribution to the responsible team at your organization. We recommend that you do not specify the email addresses of individuals as essential contacts because communication can be interrupted if the individuals change teams or leave the company.

After setting up your essential contacts, ensure that the email inbox is monitored by your security teams continuously. Continuous monitoring is a critical best practice, because adversaries frequently initiate cryptomining attacks when they expect you to be less vigilant, such as on weekends, holidays, and at night.

Designating your essential contacts for security, and then monitoring the essential contacts email address, are both a best practice and a requirement of the Security Command Center Cryptomining Protection Program.

## Maintain required IAM permissions

Your security teams, and Security Command Center itself, require authorization to access resources in the Google Cloud environment. You manage authentication and authorization by using Identity and Access Management (IAM).

As a best practice and, in the case of Security Command Center, a basic requirement, you need to maintain or preserve the IAM roles and permissions that are required to detect and respond to cryptomining attacks.

For general information about IAM on Google Cloud, see [IAM overview](https://docs.cloud.google.com/iam/docs/overview).

### Authorizations that are required by your security teams

To be able to view Security Command Center findings and respond immediately to a cryptomining attack or other security issue on Google Cloud, the Google Cloud user accounts of your security personnel need to be authorized ahead of time to respond to, remediate, and investigate the issues that might come up.

On Google Cloud, you can manage authentication and authorization by using IAM roles and permissions.

#### Roles required to work with Security Command Center

For information about the IAM roles that users need to work with Security Command Center, see [Access control with IAM](https://docs.cloud.google.com/security-command-center/docs/access-control).

#### Roles required to work with other Google Cloud services

To properly investigate a cryptomining attack, you are likely to need other IAM roles, such as [Compute Engine roles](https://docs.cloud.google.com/compute/docs/access#predefined-compute-engine-roles) that allow you to view and manage the affected VM instance and the applications that are running on it.

Depending on where the investigation of an attack leads, you might need other roles as well, such as [Compute Engine network roles](https://docs.cloud.google.com/compute/docs/access#predefined-compute-engine-roles) or [Cloud Logging roles](https://docs.cloud.google.com/logging/docs/access-control).

You also need the proper IAM permissions to create and manage your Essential Contacts for security. For information about the IAM roles that are required to manage security contacts, see [Required roles](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts#permissions).

### Authorizations that are required by Security Command Center

When you activate Security Command Center, Google Cloud automatically creates a service account that Security Command Center uses for authentication and authorization when running scans and processing logs. During the activation process, you confirm the permissions that are granted to the service account.

Do not remove or modify this service account, its roles, or its permissions.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
