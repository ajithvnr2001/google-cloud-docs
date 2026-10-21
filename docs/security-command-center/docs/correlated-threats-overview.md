---
url: https://docs.cloud.google.com/security-command-center/docs/correlated-threats-overview/
title: Correlated Threats overview \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:46:47.182368+00:00
---

# Correlated Threats overview  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/correlated-threats-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Correlated Threats overview Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

The Correlated Threats feature in Security Command Center helps you uncover critical active threats in your environment. Correlated Threats outputs a set of related threat findings and provides in-depth explanations about these findings, which you can then use to prioritize, understand, and respond to these threats.

Security teams often experience alert fatigue from managing an overwhelming number of threat findings. This situation can lead to missed or delayed responses. These teams require prioritized and relevant information quickly to identify post-exploit activity.

Correlated Threats help by aggregating multiple related threat findings into an issue. This aggregation helps provide higher confidence detections that you can act on. Correlated Threats generates an issue, which represents a series of related malicious activities.

This feature offers several benefits:

  * Reduces alert fatigue by consolidating numerous findings into critical issues.
  * Enhances detection fidelity by combining multiple signals, helping to increase confidence in detecting malicious activity.
  * Provides a visualization of the attack chain, showing how events connect to help form a complete attack story. This approach helps you anticipate adversary moves and quickly identify compromised assets.
  * Highlights critical threats and provides clear recommendations, helping you prioritize and accelerate your response.



## How Correlated Threats work

The Correlated Threats feature uses a rules engine to identify and group related security findings.

The rules engine queries the security graph with predefined Correlated Threats queries. The engine then creates issues when a pattern is identified. Security Command Center manages the lifecycle of these issues.

## Issue lifecycle

An issue remains active for 14 days after the first threat finding if you don't set the state to `INACTIVE`. This time period cannot be changed. Correlated Threats automatically set the issue state to `INACTIVE` if the underlying resources, such as VMs or Google Kubernetes Engine nodes, are deleted.

## Scan frequency

Security Command Center processes Correlated Threat rules hourly.

## Correlated Threats rules

Correlated Threats help to identify various multi-stage attack patterns across cloud resources. The following table defines the available Correlated Threats rules.

Filter this table:  Rule | Description  
---|---  
Multiple correlated threat signals of cryptocurrency mining software |  Look for multiple distinct signals of malicious software coming from Google Cloud virtual machines, including Compute Engine VMs and Google Kubernetes Engine (GKE) nodes (and their Pods). Examples include the following:

  * VM Threat Detection detects a cryptocurrency program and Event Threat Detection detects connections to cryptocurrency IP addresses or domains from the same VM.
  * Container Threat Detection detects a program that is using the cryptocurrency mining stratum protocol and Event Threat Detection detects a connection to a cryptocurrency mining IP address from the same Google Kubernetes Engine node.

  
Multiple correlated threat signals of malicious software |  Look for multiple distinct signals of malicious software coming from Google Cloud virtual machines, including Compute Engine VMs and GKE nodes (and their Pods) or Agent Runtime. Examples include the following:

  * Container Threat Detection detects if both a malicious binary and a malicious Python script are running in the same Pod.
  * Event Threat Detection detects a VM that is connecting to a malware IP address, and VM Threat Detection detects malware on the disk in the same VM.
  * Agent Platform Threat Detection detects a Malicious URL and a Reverse Shell from the same AI Agent.

  
Potentially compromised GCP account lateral movement to compromised compute resource |  Look for evidence of suspicious calls to compute APIs (Compute Engine or GKE) that modify a VM or Pod. The rule then correlates that activity with malicious activity that originates from the compute resource within a short period. Attackers commonly use this lateral movement pattern. This rule indicates that the VM or Pod is likely compromised. This rule also indicates that the Google Cloud account (either user or service account) may be the cause of the malicious activity. Examples include the following:

  * Event Threat Detection detects that a user added a new SSH key to a Compute Engine instance, and VM Threat Detection detects a cryptocurrency miner running on the same instance.
  * Event Threat Detection detects that a service account accessed an instance using the Compute Engine API from the Tor network, and Event Threat Detection detects connections to a malicious IP address from the same instance.
  * Event Threat Detection detects that a user created a privileged container and Container Threat Detection detects that the container accessed sensitive files on the GKE node from the same Pod.

  
  
## Investigate Correlated Threats

The following sections describe how to investigate Correlated Threats issues. For information about how to view and remediate issues created by Correlated Threats rules, see [Manage and remediate issues](https://docs.cloud.google.com/security-command-center/docs/issues-manage-remediate).

### Reception

You receive a Correlated Threats issue through Security Command Center. This issue indicates that the system detected and grouped multiple suspicious findings. You recognize this issue as high priority, because it is marked as an **Active threat**. The correlation of multiple signals indicates a true positive that warrants immediate focus. For more information, see [Manage and remediate issues](https://docs.cloud.google.com/security-command-center/docs/issues-manage-remediate).

### Deconstruction

Open the issue to see its parts. Within the issue details view, you can expand a section to see the individual findings. For example, if a harmful script runs on a GKE node and then connects to a malicious IP address, both events appear together. Check the details of each finding, such as when it happened, what processes were involved, the malicious IP addresses, and where the detection came from. This information indicates that the events are potentially related and explains the attack's technical details. A chronological view shows the sequence of events. The system maps these details to MITRE ATT&CK attack chain stages and presents them on an attack chain visualization. This feature gives you immediate context on the attack stage.

### Scope identification

Determine the extent of the threat. Check contextual information about the correlated events, such as the affected asset and its project or cluster context. The platform correlates issues by resource, using unique identifiers to tie events to the same node. This shows the impacted asset. Verify if other assets show similar signs. Note the identities involved, such as the service account or user that ran the malicious script. This scoped view helps you focus on affected systems and confirms whether the incident is localized or widespread.

### Next actions

The system marks Correlated Threat issues with a critical severity. You can find recommended actions in the **How to fix** views. Contain the impacted asset, for example, by isolating or shutting down the affected GKE node. Follow recommendations, such as blocking the known malicious IP at the firewall or cloud VPC level. The recommended actions help you respond faster, contain the incident, and initiate a focused investigation. For more information about investigating threats, see [How to investigate threats](https://docs.cloud.google.com/security-command-center/docs/how-to-investigate-threats).

## What's next

  * [Threat detection in Security Command Center](https://docs.cloud.google.com/security-command-center/docs/overview-threats)
  * [Container Threat Detection overview](https://docs.cloud.google.com/security-command-center/docs/concepts-container-threat-detection-overview)
  * [Event Threat Detection overview](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview)
  * [Virtual Machine Threat Detection overview](https://docs.cloud.google.com/security-command-center/docs/concepts-vm-threat-detection-overview)
  * [Manage and remediate issues](https://docs.cloud.google.com/security-command-center/docs/issues-manage-remediate)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
