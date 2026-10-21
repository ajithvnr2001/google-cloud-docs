---
url: https://docs.cloud.google.com/security-command-center/docs/predefined-detection-rules/
title: Predefined detection rules \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:48:47.741929+00:00
---

# Predefined detection rules  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/predefined-detection-rules/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Reference ](https://docs.cloud.google.com/security-command-center/docs/vulnerability-findings-index)



Send feedback 

#  Predefined detection rules Stay organized with collections  Save and categorize content based on your preferences. 

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (requires [organization-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation)) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

Security Command Center provides built-in detection rules to identify threats, vulnerabilities, and misconfigurations across your cloud environment. This document describes the predefined rules for the security graph and correlated threats.

For information about rules and findings from other built-in services, see [Event Threat Detection rules](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview#rules) and [VM Threat Detection findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vm-threat-detection-overview#findings).

## Predefined security graph rules

The security graph uses nodes to identify cloud resources like assets, identities, applications, and data. Edges in the graph represent risk relationships between these resources according to detection rules. When a relationship risk is discovered, the security graph generates an issue.

Security Command Center uses predefined security graph rules to identify issues that might potentially compromise your resources.

The following table defines these rules. For information about how to investigate issues, see [Manage and remediate issues](https://docs.cloud.google.com/security-command-center/docs/issues-manage-remediate).

Filter this table:  Rule | Description  
---|---  
GCE Instance: High-risk CVE, access to high value resource via SA impersonation  |  A high-risk CVE has been detected on a [Compute Engine](https://docs.cloud.google.com/compute/docs/overview) instance that can impersonate a service account (SA) with access to a critical resource. This vulnerability increases the risk of privilege escalation and unauthorized access to sensitive data or systems.   
GCE Instance: High-risk CVE, access to resource with sensitive data via SA impersonation  |  A Compute Engine instance with a high-risk CVE has access to a resource containing sensitive data using service account (SA) impersonation. This vulnerability increases the risk of unauthorized data access, privilege escalation, and potential data breaches.   
GCE Instance: High-risk CVE, direct access to high value resource  |  A Compute Engine instance with a high-risk CVE has direct access to a high-value resource, increasing the likelihood of exploitation, unauthorized access, and data compromise.   
GCE Instance: High-risk CVE, direct access to resource with sensitive data  |  A Compute Engine instance with a high-risk CVE has direct access to a resource containing sensitive data. This vulnerability increases the risk of unauthorized access, data breaches, and privilege escalation.   
Externally Exposed GCE Instance: High-risk CVE, exploit available  |  A Compute Engine instance is externally exposed and affected by a high-risk CVE with a known exploit. This significantly increases the risk of remote attacks, unauthorized access, and system compromise.   
GCE Instance: High-risk CVE, ability to impersonate SA  |  A Compute Engine instance is affected by a high-risk CVE and has the ability to impersonate another service account (SA). This significantly increases the risk of privilege escalation, unauthorized access, and potential compromise of critical cloud resources.   
GCE Instance: High-risk CVE, excessive direct permissions  |  A Compute Engine instance with a high-risk CVE has direct excessive permissions on another resource, increasing the risk of unauthorized access, privilege escalation, and resource compromise.   
GCE Instance: High-risk CVE, excessive permissions via SA impersonation  |  A Compute Engine instance with a high-risk CVE has excessive permissions on another resource through service account (SA) impersonation, increasing the risk of privilege escalation and unauthorized access.   
Externally Exposed GKE Workload: High-risk CVE, exploit available  |  A GKE workload is externally exposed and affected by a high-risk CVE with a known exploit. This significantly increases the risk of remote attacks, unauthorized access, and system compromise.   
GKE Node Pool: High-risk Bulletin, access to high value resource via SA impersonation  |  A GKE node pool has the ability to impersonate a service account (SA) that grants access to a high-value resource. This increases the risk of privilege escalation, unauthorized access, and data compromise.   
GKE Node Pool: High-risk Bulletin, access to resource with sensitive data via SA impersonation  |  A GKE node pool has the ability to impersonate a service account (SA) that grants access to a resource containing sensitive data. This increases the risk of unauthorized access, data breaches, and privilege escalation.   
GKE Node Pool: High-risk Bulletin, direct access to high value resource  |  A GKE node pool has direct access to a high-value resource, increasing the risk of unauthorized access, privilege escalation, and potential data compromise.   
GKE Node Pool: High-risk Bulletin, direct access to resource with sensitive data  |  A GKE node pool has direct access to a resource containing sensitive data, increasing the risk of unauthorized access, data breaches, and privilege escalation.   
Externally Exposed GKE Node Pool: High-risk Bulletin  |  A GKE node pool is externally exposed and affected by a high-risk CVE. This significantly increases the risk of remote attacks, unauthorized access, and system compromise.   
GKE Node Pool: High-risk Bulletin, ability to impersonate SA  |  There is a high-risk bulletin on a GKE node pool that has permissions to impersonate another service account (SA), increasing the risk of privilege escalation and unauthorized access to critical resources.   
GKE Node Pool: High-risk Bulletin, excessive direct permissions  |  There is a high-risk bulletin on a GKE node pool that has excessive permissions on another resource, granting it unintended access. This increases the risk of privilege escalation, unauthorized access, and data exposure.   
GKE Node Pool: High-risk Bulletin, excessive permissions via SA impersonation  |  There is a high-risk bulletin on a GKE node pool that has excessive permissions on another resource through service account (SA) impersonation, increasing the risk of privilege escalation and unauthorized access.   
Service account with unrotated key has excessive permissions  |  A service account is using a long-lived, unrotated key with excessive permissions, increasing the risk of credential compromise, unauthorized access, and privilege escalation.   
Service account with user-managed key has excessive permissions  |  A service account with user-managed keys and excessive permissions, which increases the risk of credential leakage and privilege escalation.   
Externally exposed GKE Workload vulnerable to CVE-2025-49844 (exploit available, critical remote code execution in Redis)  |  Identifies externally exposed GKE workloads running Redis that are vulnerable to CVE-2025-49844, a critical remote code execution flaw with a known exploit.   
Externally exposed GCE Instance vulnerable to CVE-2025-49844 (exploit available, critical remote code execution in Redis)  |  Identifies externally exposed GCE instances running Redis that are vulnerable to CVE-2025-49844, a critical remote code execution flaw with a known exploit.   
Externally exposed GKE Workload vulnerable to CVE-2025-32433 (critical RCE in Erlang SSH)  |  Identifies externally exposed GKE workloads running Erlang SSH that are vulnerable to CVE-2025-32433, a critical remote code execution flaw actively exploited by attackers.   
Externally exposed GCE Instance vulnerable to CVE-2025-32433 (critical RCE in Erlang SSH)  |  Identifies externally exposed GCE instances running Erlang SSH that are vulnerable to CVE-2025-32433, a critical remote code execution flaw actively exploited by attackers.   
Externally exposed GKE Workload vulnerable to CVE-2023-46604 (critical RCE in Apache ActiveMQ, exploited in the wild)  |  Identifies externally exposed GKE workloads running Apache ActiveMQ vulnerable to CVE-2023-46604, a critical remote code execution flaw in the OpenWire protocol actively exploited by attackers.   
Externally exposed GCE Instance vulnerable to CVE-2023-46604 (critical RCE in Apache ActiveMQ, exploited in the wild)  |  Identifies externally exposed GCE instances running Apache ActiveMQ vulnerable to CVE-2023-46604, a critical remote code execution flaw in the OpenWire protocol actively exploited by attackers.   
GCE Instance vulnerable to CVE-2025-32463 (Sudo) with known exploit  |  Identifies GCE instances vulnerable to CVE-2025-32463, a local privilege escalation flaw in Sudo with a known exploit.   
GCE Instance vulnerable to Critical Nvidia Container Toolkit CVE (CVE-2025-23266)  |  Identifies GCE instances using GPU workloads vulnerable to CVE-2025-23266, a critical privilege escalation flaw in the NVIDIA Container Toolkit.   
Externally exposed GCE Instance vulnerable to high risk CVE-2025-59287 (exploited in the wild, critical remote code execution in WSUS)  |  Identifies externally exposed GCE instances running Windows WSUS that are vulnerable to CVE-2025-59287, a critical remote code execution flaw actively exploited by attackers.   
Vertex AI Workbench: High-risk CVE  |  A high-risk CVE has been detected on a Gemini Enterprise Agent Platform Workbench instance. This vulnerability increases the risk of unauthorized access to the development environment, potentially exposing training data and model source code to exfiltration.   
Vertex AI Workbench: High-risk CVE, excessive permissions  |  A Vertex AI Workbench instance with a high-risk CVE is using an overprivileged service account. This combination allows attackers to exploit the vulnerability to escalate privileges and compromise other cloud resources.   
Agent Runtime: High-risk CVE, SA identity with access to high value resource via SA impersonation  |  A high-risk CVE has been detected on an AI Agent deployed to Agent Runtime that can impersonate a service account with access to a critical resource. This vulnerability increases the risk of privilege escalation and unauthorized access to sensitive data or systems.   
Agent Runtime: High-risk CVE, SA identity with access to resource with sensitive data via SA impersonation  |  An AI Agent deployed to Agent Runtime with a high-risk CVE has access to a resource containing sensitive data via service account (SA) impersonation. This vulnerability increases the risk of unauthorized data access, privilege escalation, and potential data breaches.   
Agent Runtime: High-risk CVE, SA identity with direct access to high value resource  |  An AI Agent deployed to Agent Runtime with a high-risk CVE has direct access to a high-value resource, increasing the likelihood of exploitation, unauthorized access, and data compromise.   
Agent Runtime: High-risk CVE, SA identity with direct access to resource with sensitive data  |  An AI Agent deployed to Agent Runtime with a high-risk CVE has direct access to a resource containing sensitive data. This vulnerability increases the risk of unauthorized access, data breaches, and privilege escalation.   
Agent Runtime: High-risk CVE, SA identity with excessive direct permissions  |  An AI Agent deployed to Agent Runtime with a high-risk CVE has direct excessive permissions on another resource, increasing the risk of unauthorized access, privilege escalation, and resource compromise.   
Agent Runtime: High-risk CVE, SA identity with excessive permissions via SA impersonation  |  An AI Agent deployed to Agent Runtime with a high-risk CVE has excessive permissions on another resource through service account (SA) impersonation, increasing the risk of privilege escalation and unauthorized access.   
Agent Runtime: High-risk CVE, SA identity with ability to impersonate SA  |  An AI Agent deployed to Agent Runtime with a high-risk CVE has the ability to impersonate another service account. This significantly increases the risk of privilege escalation, unauthorized access, and potential compromise of critical cloud resources.   
Cloud Storage Bucket: Publicly exposed bucket used for Agent Runtime deployment  |  A publicly exposed Cloud Storage Bucket was used to deploy AI Agent to Agent Runtime. This increases the risk of agent code leakage and agent poisoning.   
  
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

  
  
## What's next

  * [Manage and remediate issues](https://docs.cloud.google.com/security-command-center/docs/issues-manage-remediate)
  * [Investigate Correlated Threats](https://docs.cloud.google.com/security-command-center/docs/correlated-threats-overview#investigate-correlated-threats)
  * [Event Threat Detection rules](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview#rules)
  * [VM Threat Detection findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vm-threat-detection-overview#findings)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
