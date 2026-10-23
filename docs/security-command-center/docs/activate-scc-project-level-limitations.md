---
url: https://docs.cloud.google.com/security-command-center/docs/activate-scc-project-level-limitations/
title: Features available with project-level activations \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:53:21.412527+00:00
---

# Features available with project-level activations  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/activate-scc-project-level-limitations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Features available with project-level activations Stay organized with collections  Save and categorize content based on your preferences. 

Standard-legacy, Standard, and Premium [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

Security Command Center project-level activations let you manage security findings within an individual project. However, some detection services and finding categories require access beyond a single project's scope. Activating the [Standard tier](https://cloud.google.com/security-command-center/pricing) at the parent organization level turns on certain cross-project features, while other organization-wide capabilities require an organization-level activation of the Premium tier.

## Features you can enable by activating the Standard tier in the parent organization

This section lists the features that you can enable for a project-level activation of Security Command Center Premium by activating Security Command Center Standard tier in the parent organization.

### Security Health Analytics findings

To enable the following finding categories for a project-level activation of Security Command Center Premium, activate Security Command Center Standard tier in the parent organization, which enables the finding for all projects in the organization:

  * `MFA not enforced`
  * `Public log bucket`



You can enable the following Premium tier finding categories in project-level activations of Security Command Center Premium by activating the Standard tier in the parent organization:

  * `Audit config not monitored`
  * `Bucket IAM not monitored`
  * `Cluster private Google access disabled`
  * `CUSTOM_ORG_POLICY_VIOLATION`
  * `Custom role not monitored`
  * `Default network`
  * `DNS logging disabled`
  * `Egress deny rule not set`
  * `Firewall not monitored`
  * `HTTP load balancer`
  * `KMS project has owner`
  * `Legacy network`
  * `Locked retention policy not set`
  * `Log not exported`
  * `Network not monitored`
  * `Object versioning disabled`
  * `Org policy Confidential VM policy`
  * `Org policy location restriction`
  * `OS login disabled`
  * `Owner not monitored`
  * `Pod security policy disabled`
  * `Route not monitored`
  * `SQL instance not monitored`
  * `Too many KMS users`
  * `Weak SSL policy`



For the complete list of Security Health Analytics findings, see [Vulnerabilities findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#security-health-analytics-detectors).

### Event Threat Detection findings

You can enable the following Premium tier finding categories in project-level activations of Security Command Center Premium by activating Security Command Center Standard in the parent organization:

  * `Exfiltration: BigQuery data extraction`
  * `Exfiltration: CloudSQL data exfiltration`



For a complete list of Event Threat Detection finding categories, see [Event Threat Detection rules](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview#rules).

### Integrated Google Cloud services

To enable the publication of findings from the following integrated Google Cloud services in a project-level activation of Security Command Center Premium, activate the Standard tier in the parent organization, which enables the services for all projects in the organization:

  * [Sensitive Data Protection](https://cloud.google.com/security/products/dlp)
  * [Google Cloud Armor](https://docs.cloud.google.com/armor/docs/cloud-armor-overview)
  * [ Anomaly Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#anomaly_detection)
  * [Google Security Operations](https://docs.cloud.google.com/chronicle)



You can enable the publication of findings from the following integrated Premium-tier Google Cloud service in project-level Premium-tier activations by activating Security Command Center Standard in the parent organization:

  * [VM Manager](https://docs.cloud.google.com/compute/docs/vm-manager)



### Integrations with third-party services

You can enable the publication of findings from [third-party services](https://docs.cloud.google.com/security-command-center/docs/how-to-configure-security-command-center#third-party-source) in project-level activations by activating Security Command Center Standard tier in the parent organization.

## Features unavailable with project-level Premium-tier activations

Features listed in this section are Premium-tier features that require an organization-level activation of Security Command Center Premium. These features are not available with project-level Premium-tier activations.

### Security Health Analytics finding categories unavailable with project-level activations

The following Security Health Analytics findings require organization-level activations of Security Command Center Premium:

  * `Audit logging disabled`
  * `KMS role separation`
  * `Redis role used on org`
  * `Service account role separation`



For the complete list of Security Health Analytics findings, see [Vulnerabilities findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#security-health-analytics-detectors).

### Event Threat Detection finding categories unavailable with project-level activations

The following Event Threat Detection findings require organization-level activations of Security Command Center Premium:

  * `Defense evasion: modify VPC service control`
  * `Initial access: account disabled hijacked`
  * `Initial access: disabled password leak`
  * `Initial access: government based attack`
  * `Initial access: suspicious login blocked`
  * `Persistence: new geography`
  * `Persistence: new user agent`
  * `Persistence: SSO enablement toggle`
  * `Persistence: SSO settings changed`
  * `Persistence: strong authentication disabled`
  * `Persistence: two step verification disabled`
  * `Privilege escalation: external member added to privileged group`
  * `Privilege escalation: privileged group opened to public`
  * `Privilege escalation: sensitive role granted to hybrid group`
  * `Privilege escalation: suspicious cross-project permission use`
  * `Privilege escalation: suspicious token generation`



For a complete list of Event Threat Detection finding categories, see [Event Threat Detection rules](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview#rules).

### Sensitive Actions Service finding categories unavailable with project-level activations

The following Sensitive Actions Service findings require organization-level activations of Security Command Center Premium:

  * `Defense Evasion: Organization Policy Changed`
  * `Defense Evasion: Remove Billing Admin`
  * `Persistence: Add Sensitive Role`



For a complete list of Sensitive Actions Service finding categories, see [Sensitive Actions Service findings](https://docs.cloud.google.com/security-command-center/docs/concepts-sensitive-actions-overview#findings).

### Attack path simulations

Attack path simulations, a Premium-tier feature, are not available with project-level activations of Security Command Center. Attack path simulations generate [attack exposure scores](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn#attack_exposure_scores) and [attack paths](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn#attack_paths) for vulnerability and misconfiguration findings.

### Graph search

Graph search, a Premium-tier feature, isn't available with project-level activations of Security Command Center. [Graph search](https://docs.cloud.google.com/security-command-center/docs/graph-search) lets you explore the security graph by creating custom queries to help pinpoint potential security concerns in your environment.

### Security posture

Security posture management, a Premium-tier feature, isn't available with project-level activations of Security Command Center. The [security posture service](https://docs.cloud.google.com/security-command-center/docs/security-posture-overview) lets you define, assess, and monitor the overall status of your security in Google Cloud.

### Data residency

[Data residency](https://docs.cloud.google.com/security-command-center/docs/data-residency-support) isn't supported with project-level activations of Security Command Center. Data residency lets you configure the location where some Security Command Center data is kept when it's at rest, in use, and in transit.

### Artifact Registry vulnerability assessment

To use Artifact Registry vulnerability assessment, you must activate Security Command Center at the organization level.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
