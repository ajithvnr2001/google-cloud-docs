---
url: https://docs.cloud.google.com/security-command-center/docs/overview-threats/
title: Threat detection in Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:48:19.466928+00:00
---

# Threat detection in Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/overview-threats/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Threat detection in Security Command Center Stay organized with collections  Save and categorize content based on your preferences. 

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (some features require [organization-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation))

This document describes Security Command Center features that help you detect and investigate threats to your cloud environment.

## Architectural overview

Security Command Center provides threat detection through a multi-layered approach to address security gaps in your environment. Log-based, agentless, and runtime detectors monitor your cloud resources and detect potentially malicious activity in near real time. These detectors report these incidents as findings with assigned severity levels.

Security Command Center provides the threat findings in a central platform along with other security findings to give you a high-level view of your overall security posture. To help you triage the findings, Security Command Center groups any closely related threats into Correlated Threats issues.

The following diagram illustrates the threat detection process of Security Command Center.

![Architecture for Security Command Center threat detection.](https://docs.cloud.google.com/static/security-command-center/images/threats-overview-diagram.svg)

**Note:** Some threat detectors are disabled by default. To enable or disable threat detection services or modules, see [Configure Security Command Center services](https://docs.cloud.google.com/security-command-center/docs/how-to-configure-security-command-center).

## Layers of threat detection

Security Command Center organizes threat detection into three primary layers to help address gaps in your security posture: log-based detection, agentless detection, and runtime detection.

### Log-based detection

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

Security Command Center can continuously monitor and analyze log streams for your organization or projects to identify suspicious patterns, known indicators of compromise (IoCs), and sensitive actions.

[Event Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview) and [Sensitive Actions Service](https://docs.cloud.google.com/security-command-center/docs/concepts-sensitive-actions-overview) provide log-based detection.

#### Log-based detection of threats

Event Threat Detection can detect attacks across various Google Cloud services and [resource categories](https://docs.cloud.google.com/security-command-center/docs/threat-findings-index), including identity-based attacks and unauthorized service usage. Event Threat Detection monitors the following:

  * The Cloud Logging stream for your organization and projects, like API call and action entries that create, read, or modify the resources' configuration or metadata. Examples include the following:

    * [Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit) (Admin Activity, Data Access, and System Event logs)
    * [VPC Flow Logs](https://docs.cloud.google.com/vpc/docs/flow-logs)
    * [Cloud DNS logs](https://docs.cloud.google.com/dns/docs/monitoring)
    * [Foundational log sources](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview#foundational_log_sources)
  * [Audit logs for Google Workspace](https://docs.cloud.google.com/logging/docs/audit/gsuite-audit-logging), which track user sign-ins to your domain and actions performed on your Google Workspace Admin Console.




For a complete list of Event Threat Detection detectors and the logs that they analyze, see [Event Threat Detection rules](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview#rules).

You might need to enable the collection of specific logs if required by your organization. For more information, see [Log types and activation requirements](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview#log_types).

##### Sensitive data enrichment

Event Threat Detection is integrated with Sensitive Data Protection to enrich sensitive resource findings. If you have [enabled Sensitive Data Protection discovery scans](https://docs.cloud.google.com/security-command-center/docs/activate-sensitive-data-discovery), Event Threat Detection can use the sensitivity metadata of your BigQuery and Cloud Storage resources to adjust findings by updating finding categories and upgrading finding severity. For more information, see [Sensitive data enrichment](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview#sdp-enrichment).

#### Log-based detection of sensitive actions

Sensitive Actions Service monitors [Admin Activity audit logs](https://docs.cloud.google.com/logging/docs/audit#admin-activity) to detect sensitive actions that might be damaging to your business if taken by a malicious actor. For a complete list of Sensitive Actions Service detectors, see [Sensitive Actions Service findings](https://docs.cloud.google.com/security-command-center/docs/concepts-sensitive-actions-overview#findings).

### Agentless detection

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

Agentless detection scans your Compute Engine virtual machines from the hypervisor to identify malicious applications running on your virtual machine (VM) instances, such as cryptocurrency mining tools and kernel-mode rootkits.

Agentless detection operates from outside the guest VM instance and doesn't require guest agents, special guest OS configurations, or network connectivity within the guest. You don't need to install, manage, or update software in a fleet of VMs. Because agentless detection operates outside the VM instance, it remains undetectable to malware residing inside the VM and doesn't consume CPU cycles or memory.

[Virtual Machine Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-vm-threat-detection-overview) provides agentless detection. For a complete list of VM Threat Detection detectors, see [Virtual Machine Threat Detection findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vm-threat-detection-overview#findings).

### Runtime detection

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

Runtime detection addresses threats that emerge after deployment in dynamic environments. It continuously monitors and assesses activity, changes, and remote access attempts within running containers and serverless applications to identify common runtime attacks. Examples of these attacks include reverse shells, container escapes, and the execution of malicious programs.

The following services provide runtime detection:

  * [Container Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-container-threat-detection-overview) uses kernel-level instrumentation to collect and assess behavior in the guest kernel of GKE nodes.
  * [Cloud Run Threat Detection](https://docs.cloud.google.com/security-command-center/docs/cloud-run-threat-detection-overview) monitors supported Cloud Run resources.
  * [Agent Platform Threat Detection](https://docs.cloud.google.com/security-command-center/docs/agent-engine-threat-detection-overview) ([Preview](https://cloud.google.com/products/#product-launch-stages)) monitors agentic workloads that are deployed to Agent Runtime.



## Resource category and detection matrix

The following table shows the categories of resources that Security Command Center can monitor, example detections, and the available detection layers.

**Resource category** | **Example threats detected** | **Detection layers**  
---|---|---  
**AI** | Agent-initiated data exfiltration, malicious script executed in an agentic workload | Runtime, log-based  
**Amazon EC2** | Malicious file on disk | Agentless  
**Backup and DR** | Unauthorized deletion of backups and DR hosts | Log-based  
**BigQuery** | Data exfiltration | Log-based  
**Cloud Run** | Reverse shells, execution of reconnaissance tools, use of cryptomining commands | Runtime, log-based  
**Cloud Storage** | Modifications in the IP filtering configuration for a bucket | Log-based  
**Compute Engine** | Cryptomining, kernel-mode rootkits, modified boot disk persistence | Agentless, log-based  
**Database** | Data exfiltration, superuser modifications to user tables | Log-based  
**Google Kubernetes Engine** | Malicious binary execution, container escape, launch of privileged containers | Runtime, log-based  
**Google Workspace** | Password leaks, suspicious login patterns | Log-based  
**Identity and Access Management** | Anomalous role grants, sensitive policy changes, access from Tor | Log-based  
**Network** | Malware DNS queries, connections to known cryptomining IP addresses | Log-based  
  
## Sources of threat intelligence

Security Command Center uses threat intelligence from [Google Threat Intelligence](https://cloud.google.com/security/products/threat-intelligence): a high-fidelity intelligence suite that gathers billions of signals from across Google's global products and services. Google Threat Intelligence identifies known malicious indicators like malicious signatures, file hashes, and addresses and offers the following benefits:

  * **Fidelity and precision:** Minimizes false positives by focusing on active and verified threats.
  * **Continuous improvement:** Uses frontline intelligence from real-world incident response investigations, global telemetry, internal intelligence, and crowdsourced context on potentially malicious files, URLs, and domains to continuously improve coverage. To enhance its intelligence gathering, it also uses various techniques, such as decoy systems (also known as [_honeypots_](https://en.wikipedia.org/wiki/Honeypot_\(computing\))).



## Threat prioritization

To help you identify the most critical threats that require immediate attention, Security Command Center assigns a [severity level](https://docs.cloud.google.com/security-command-center/docs/finding-severity-classifications) to each finding.

In addition, the [Correlated Threats](https://docs.cloud.google.com/security-command-center/docs/correlated-threats-overview) feature consolidates multiple related findings into a single [issue](https://docs.cloud.google.com/security-command-center/docs/issues-overview) to provide higher-confidence detections of post-exploit activity. The Correlated Threats feature also visualizes the attack chain and shows how events connect to form a complete attack story. This attack chain helps you anticipate adversary moves, identify compromised assets, highlight critical threats, get clear response recommendations, and accelerate your response.

## Built-in threat detection services

This section provides a summary of the built-in detection services in Security Command Center. These services use different scanning techniques and operate at different layers to detect threats in your cloud environment.

  * [Agent Platform Threat Detection](https://docs.cloud.google.com/security-command-center/docs/agent-engine-threat-detection-overview) ([Preview](https://cloud.google.com/products/#product-launch-stages)) monitors the state of AI agents that are deployed to [Agent Runtime](https://docs.cloud.google.com/agent-builder/agent-engine/overview) Runtime to detect common runtime attacks. Available for Premium and Enterprise (Deprecated) service tiers.

  * [Anomaly Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#anomaly_detection) uses behavior signals from outside your system to detect security anomalies in your service accounts, such as potential leaked credentials. Available for Standard-legacy, Standard, Premium, and Enterprise (Deprecated) service tiers.

  * [Cloud Run Threat Detection](https://docs.cloud.google.com/security-command-center/docs/cloud-run-threat-detection-overview) monitors the state of supported Cloud Run resources to detect common runtime attacks. Available for Premium and Enterprise (Deprecated) service tiers.

  * [Container Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-container-threat-detection-overview) generates findings by collecting and analyzing low-level observed behavior in the guest kernel of containers. Available for Premium and Enterprise (Deprecated) service tiers.

  * [Event Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview) produces security findings by matching events in your Cloud Logging log streams to known indicators of compromise (IoCs), identifying known adversarial techniques, and detecting behavioral anomalies. Available for Premium and Enterprise (Deprecated) service tiers.

  * [Sensitive Actions Service](https://docs.cloud.google.com/security-command-center/docs/concepts-sensitive-actions-overview) detects when actions are taken in your Google Cloud organization, folders, and projects that might be damaging to your business if they're taken by a malicious actor. Available for Standard-legacy, Standard, Premium, and Enterprise (Deprecated) service tiers.

  * [Virtual Machine Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-vm-threat-detection-overview) scans Compute Engine projects and VM instances to detect potentially malicious applications running in VMs, such as cryptocurrency mining software and kernel-mode rootkits. Available for Premium and Enterprise (Deprecated) service tiers.




These detection services generate findings in Security Command Center. For the Premium and Enterprise (Deprecated) service tiers (requires organization-level activation), you can also configure [continuous exports to Cloud Logging](https://docs.cloud.google.com/security-command-center/docs/export-cloud-logging).

## Enable threat detection

For the Premium and Enterprise (Deprecated) service tiers, many threat detection services are enabled by default. To enable or disable a built-in service, see [Configure Security Command Center services](https://docs.cloud.google.com/security-command-center/docs/how-to-configure-security-command-center).

You might need to enable the collection of specific logs if required by your organization. For more information, see [Log types and activation requirements](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview#log_types).

## Work with threat detection services

To work with the built-in threat detection services, see the following:

  * [Use Agent Platform Threat Detection](https://docs.cloud.google.com/security-command-center/docs/use-agent-engine-threat-detection)
  * [Use Cloud Run Threat Detection](https://docs.cloud.google.com/security-command-center/docs/use-cloud-run-threat-detection)
  * [Use Container Threat Detection](https://docs.cloud.google.com/security-command-center/docs/how-to-use-container-threat-detection)
  * [Use Event Threat Detection](https://docs.cloud.google.com/security-command-center/docs/how-to-use-event-threat-detection)
  * [Use Sensitive Actions Service](https://docs.cloud.google.com/security-command-center/docs/how-to-use-sensitive-actions)
  * [Use Virtual Machine Threat Detection](https://docs.cloud.google.com/security-command-center/docs/how-to-use-vm-threat-detection)



## Send feedback

To send feedback on the threat detection features of Security Command Center, see [Send feedback through the Google Cloud console](https://docs.cloud.google.com/security-command-center/docs/optimize-security-command-center#send-feedback-console).

## What's next

  * [Review the complete list of all threat finding types](https://docs.cloud.google.com/security-command-center/docs/threat-findings-index).
  * [Investigate and respond to a threat finding](https://docs.cloud.google.com/security-command-center/docs/how-to-investigate-threats).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
