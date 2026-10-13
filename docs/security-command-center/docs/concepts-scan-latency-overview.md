---
url: https://docs.cloud.google.com/security-command-center/docs/concepts-scan-latency-overview/
title: When to expect findings in Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:13:48.834978+00:00
---

# When to expect findings in Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/concepts-scan-latency-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  When to expect findings in Security Command Center Stay organized with collections  Save and categorize content based on your preferences. 

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This page provides an overview of the activation process that takes place when you enable Security Command Center. It aims to answer common questions:

  * What happens when Security Command Center is enabled?
  * Why is there a delay before the first scans start?
  * What is the expected runtime for the first scans and ongoing scans?
  * How will changing resources and settings impact performance?



## Overview

When you first enable Security Command Center, an activation process must complete before Security Command Center can start scanning your resources. Then the scans must complete before you see a complete set of findings for your Google Cloud environment.

How long the activation process and scans take to complete depends on a number of factors, including the number of assets and resources in your environment and whether Security Command Center is activated at the [organization level](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation) or the [project level](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#project-level-activation-overview).

With organization-level activations, Security Command Center must repeat certain steps of the activation process for each project in the organization. Depending on the number of projects in an organization, the time required for the activation process can range from minutes to hours. For organizations with more than 100,000 projects, a lot of resources in each project, and other complicating factors, enablement and initial scans can take up to 24 hours or more to complete.

With project-level activations of Security Command Center, the activation process is much faster, because the process is limited to the single project in which Security Command Center is activated.

The factors that can introduce latency in starting scans, processing changes to settings, and the runtime of scans are discussed in the following sections.

## Latency in onboarding

Before scans start, Security Command Center discovers and indexes your resources.

Indexed services include App Engine, BigQuery, Cloud SQL, Cloud Storage, Compute Engine, Identity and Access Management, and Google Kubernetes Engine.

For project-level activations of Security Command Center, the discovery and indexing is limited to the single project in which Security Command Center is activated.

For organization-level activations, Security Command Center discovers and indexes resources across your organization.

During this onboarding process, two critical steps take place.

### Asset scan

Security Command Center conducts an initial asset scan to identify the total number, location, and state of projects, folders, files, clusters, identities, access policies, enrolled users, and other resources. This process is usually completed within minutes.

### API activation

As resources are discovered, Security Command Center enables parts of Google Cloud that are needed for Security Health Analytics, Event Threat Detection, Container Threat Detection, and Web Security Scanner to operate. Some detection services require specific APIs to be enabled on protected projects to function.

When you activate Security Command Center at the project level, API activation usually takes less than a minute.

With organization-level activations, Security Command Center iterates through all of the projects that you select for scanning to enable the necessary APIs.

The number of projects in an organization largely determines the length of the onboarding and enablement processes. Because APIs must be activated for projects one by one, API activation is usually the most time-consuming task, particularly for organizations with more than 100,000 projects.

The time needed to enable services across projects scales linearly. That means, generally, it takes twice as long to enable services and security settings in an organization with 30,000 projects as it does for one with 15,000 projects.

For an organization with 100,000 projects, onboarding and enablement of the Premium and Enterprise (Deprecated) service tiers should be completed in under five hours. Your time can vary depending on many factors, including the number of projects or containers that you are using and the number of Security Command Center services that you choose to enable.

## Initial scan latency

When you set up Security Command Center, you decide which built-in and integrated services to enable, and select the Google Cloud resources that you want to have analyzed, or scanned, for threats and vulnerabilities. As APIs are activated for projects, selected services begin their scans. The duration of these scans also depends on the number of projects in an organization.

Findings from built-in services are available as initial scans are completed. Services experience latency as described in the following sections.

  * **Agent Platform Threat Detection** ([Preview](https://cloud.google.com/products/#product-launch-stages)) has the following latencies: 
    * Activation latency of up to 3.5 hours for newly onboarded projects or organizations.
    * Detection latency of minutes.
  * **Agent Platform Vulnerability Assessment** ([Preview](https://cloud.google.com/products/#product-launch-stages)) scans new and updated Agent Platform instances and container images during deployment. Findings appear in Security Command Center shortly after being detected. Scans run continuously to identify new findings and changes to findings.
  * **Cloud Run Threat Detection** has the following latencies: 
    * Activation latency of up to 3.5 hours for newly onboarded projects or organizations.
    * Detection latency of minutes.
  * **Compliance Manager** : See [Compliance Manager scan latency for detective controls](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-overview#cm-scan-latency).
  * **Container Threat Detection** has the following latencies: 
    * Activation latency of up to 3.5 hours for newly onboarded projects or organizations.
    * Activation latency of minutes for newly created clusters.
    * Detection latency of minutes for threats in clusters that have been activated.
  * **Event Threat Detection** activation occurs within seconds for built-in detectors. For new or updated custom detectors, it can take up to 15 minutes for your changes to take effect. In practice, it typically takes less than 5 minutes.

For built-in and custom detectors, detection latencies are generally less than 15 minutes from the time a log is written to when a finding is available in Security Command Center.

  * **External Exposure** ([Preview](https://cloud.google.com/products/#product-launch-stages)) scans can take up to 12 hours to start after the service is enabled.

  * **Issues** data for the Security Command Center Premium and Enterprise tiers can take approximately 6 hours to appear.

  * Security graph data for the Security Command Center Premium and Enterprise tiers can take approximately 2 hours to appear.

  * **Security Health Analytics** : See [Security Health Analytics scan latency](https://docs.cloud.google.com/security-command-center/docs/concepts-security-health-analytics#sha-scan-latency).

  * Sensitive Data Protection: See [Sensitive Data Protection scan latency](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#sdp-scan-latency).

  * **VM Threat Detection** has an activation latency of up to 48 hours for newly onboarded organizations. For projects, the activation latency is up to 15 minutes.

  * **Vulnerability Assessment for Google Cloud** : See [Findings generated by Vulnerability Assessment for Google Cloud](https://docs.cloud.google.com/security-command-center/docs/vulnerability-assessment-google-cloud#findings) for information about the frequency of scans after it is enabled.

  * **Vulnerability Assessment for Amazon Web Services (AWS)** begins scanning the resources in an AWS account approximately 15 minutes after the required CloudFormation template is first deployed in the account. When a software vulnerability is detected in the AWS account, the corresponding finding becomes available in Security Command Center approximately 10 minutes later.

How long it takes to complete a scan depends on the number of EC2 instances. Typically, a scan of a single EC2 instance takes less than 5 minutes.

  * **Web Security Scanner** scans can take up to 24 hours to start after the service is enabled and run weekly after the first scan.

  * **Data Security Posture Management (DSPM)** scans can take up to 24 hours to start after the service is enabled.

  * VM Manager: For information, see [Asset scan settings](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#vm_manager) column.




Security Command Center runs error detectors, which detect configuration errors related to Security Command Center and its services. These error detectors are activated by default and can't be deactivated. Detection latencies vary depending on the error detector. For more information, see [Security Command Center errors](https://docs.cloud.google.com/security-command-center/docs/concepts-scc-errors).

The IAM roles for Security Command Center can be granted at the organization, folder, or project level. Your ability to view, edit, create, or update findings, assets, and security sources depends on the level that you're granted access for. To learn more about Security Command Center roles, see [Access control](https://docs.cloud.google.com/security-command-center/docs/access-control). 

### Viewing preliminary findings

You might see some findings in the Google Cloud console while initial scans are taking place but before the onboarding process is complete. Preliminary findings are accurate and actionable, but they are not comprehensive. Using these findings for a compliance assessment within the first 24 hours is not recommended. 

## Subsequent scans

Changes made within your organization or project, such as moving resources or, for organization-level activations, adding new folders and projects, usually won't significantly impact resource discovery time or the runtime of scans. However, some scans proceed on set schedules, which determine how quickly Security Command Center detects changes.

  * **Agent Platform Threat Detection** ([Preview](https://cloud.google.com/products/#product-launch-stages)) uses a watcher process to collect event information while the agentic workload is running. The watcher process can take up to one minute to start and collect information.
  * **Agent Platform Vulnerability Assessment** ([Preview](https://cloud.google.com/products/#product-launch-stages)) scans Agent Platform instances and container images continuously to identify new findings and changes to existing findings.
  * **Attack path simulations** : For information, see the Attack path simulations section.
  * **Cloud Run Threat Detection** uses a watcher process to collect container and event information for the complete duration of a Cloud Run workload. The watcher process can take up to one minute to start and collect information.
  * **External Exposure** ([Preview](https://cloud.google.com/products/#product-launch-stages)) runs batch scans approximately every 12 hours.
  * **Event Threat Detection and Container Threat Detection** : these services run in real time when they are turned on and immediately detect new or changed resources, such as clusters, buckets, or logs, in enabled projects.
  * **Security Health Analytics** : For information about scan types, see [Security Health Analytics scan types](https://docs.cloud.google.com/security-command-center/docs/concepts-security-health-analytics#sha-scan-types). For information about detection latency, see [ Security Health Analytics subsequent scans](https://docs.cloud.google.com/security-command-center/docs/concepts-security-health-analytics#detection_latency).
  * Sensitive Data Protection: See [Sensitive Data Protection scan latency](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#sdp-scan-latency).
  * **VM Threat Detection** : For memory scanning, VM Threat Detection scans each VM instance immediately after the instance is created. In addition, VM Threat Detection scans each VM instance every 30 minutes. 
    * For cryptocurrency mining detection, VM Threat Detection generates one finding per process, per VM, per day. Each finding includes only the threats associated with the process that is identified by the finding. If VM Threat Detection finds threats but can't associate them with any process, then, for each VM, VM Threat Detection groups all of the unassociated threats into a single finding that it generates once per 24-hour period. For any threats that persist longer than 24 hours, VM Threat Detection generates new findings once every 24 hours. 
    * For kernel-mode rootkit detection, VM Threat Detection generates one finding per category, per VM, every three days. 

For persistent disk scanning, which detects the presence of known malware, VM Threat Detection scans each VM instance at least daily. 

  * **Vulnerability Assessment for AWS** runs scans three times a day. How long it takes to complete a scan depends on the number of EC2 instances. Typically, a scan of a single EC2 instance takes less than 5 minutes.

When a software vulnerability is detected in an AWS account, the corresponding finding becomes available in Security Command Center approximately 10 minutes later.

  * **Web Security Scanner** : Web Security Scanner runs weekly, on the same day as the initial scan. Because it runs weekly, Web Security Scanner won't detect changes in real time. If you move a resource or alter an application, the change might not be detected for up to a week. You can run [on-demand scans](https://docs.cloud.google.com/security-command-center/docs/how-to-use-web-security-scanner#on-demand_scans) to check new or changed resources between scheduled scans.

  * **DSPM** : Findings that are generated by DSPM show up in near real time on the DSPM dashboard.

  * VM Manager: For information, see the [Asset scan settings](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#vm_manager) column.




Security Command Center error detectors run periodically in batch mode. Batch scanning frequencies vary depending on the error detector. For more information, see [Security Command Center errors](https://docs.cloud.google.com/security-command-center/docs/concepts-scc-errors).

### Attack path simulations

Attack path simulations run every six hours, approximately. As your Google Cloud organization grows in size or complexity, the time between intervals can increase.

When you first activate Security Command Center, the attack path simulations use a default high-value resource set, which focuses on a subset of the supported resource types found in your organization. For more information, refer to the [list of supported resource types.](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn#default-high-value-resource-set)

When you start defining your own high-value resource set by creating a resource value configuration, you might see the time between simulation intervals drop if the number of resource instances in your high-value resource set is significantly lower than the default set.

## Correlated Threats

For information about when to expect issues generated by Correlated Threats, see [Scan frequency](https://docs.cloud.google.com/security-command-center/docs/correlated-threats-overview#rule-frequency).

## What's next

  * Learn about [using Security Command Center in the Google Cloud console](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-command-center).
  * Learn about [detection services](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
