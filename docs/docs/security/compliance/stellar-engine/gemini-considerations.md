---
url: https://docs.cloud.google.com/docs/security/compliance/stellar-engine/gemini-considerations/
title: Security standards for Gemini \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:08:17.930258+00:00
---

# Security standards for Gemini  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/security/compliance/stellar-engine/gemini-considerations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Guides ](https://docs.cloud.google.com/docs/security/overview/whitepaper)



Send feedback 

#  Security standards for Gemini Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the security standards and guardrails for deploying [Gemini for Google Cloud](https://docs.cloud.google.com/gemini/docs) and [Gemini for Government](https://docs.cloud.google.com/docs/security/compliance/deploy-gemini-gov). These standards help you align with public-sector frameworks such as FedRAMP High and DoD IL5.

Although Stellar Engine automates foundational landing zone deployments, you must enforce specific guardrails for sensitive AI workloads to maintain sovereignty, prevent configuration drift, and mitigate AI-specific vulnerabilities.

## Prerequisites

To help ensure a secure deployment lifecycle, adhere to the following prerequisites before initiating infrastructure provisioning:

  * **Infrastructure as code (IaC) enforcement:** Eliminate manual configurations in the Google Cloud console. Implement all environment changes, remediation actions, and adjustments using automated CI/CD pipelines to help prevent configuration drift.
  * **Official repository use:** Use the official [Stellar Engine repositories](https://github.com/google/stellar-engine). Unverified forks or custom variations might introduce security regressions.
  * **[Security Command Center Premium](https://docs.cloud.google.com/security-command-center/docs):** Activate Security Command Center Premium across all folders to enable continuous threat detection and compliance monitoring.



### Root environment lockdown

To satisfy FedRAMP High and DoD IL5 frameworks, enforce the following strict controls at the folder and organization levels:

  * **Dual-folder architecture:** segregate resources using at least two dedicated folders that are governed by [Assured Workloads](https://docs.cloud.google.com/assured-workloads/docs); one for FedRAMP High and one for FedRAMP Moderate or IL5.
  * **Resource residency:** lock resource residency to pre-agreed US regions (for example, `us-east4`).
  * **Organizational policy constraint:** enable the following constraints to restrict access: 
    * [`iam.allowedPolicyMemberDomains`](https://docs.cloud.google.com/organization-policy/restrict-domains): restrict to authorized agency domains.
    * [`compute.vmExternalIpAccess`](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-static-external-ip-address#disableexternalip): prevent public IP assignments on VM instances.
    * [`compute.restrictVpcPeering`](https://docs.cloud.google.com/organization-policy/reference/org-policy-constraints): minimize lateral traversal risks; route spoke traffic through centralized hubs.
    * [`vertexai.allowedModels`](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/control-model-access): restrict access to authorized models (for example, to prevent the ingestion of unapproved external or partner models).
  * **Context-aware access:** require [Identity-Aware Proxy (IAP)](https://docs.cloud.google.com/iap/docs) to verify the user's identity and their device security posture (using Access Context Manager) before routing traffic to the Gemini application layer.



## Secure networking

Deployments must enforce a hub-and-spoke topology that's governed by [Network Connectivity Center](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center) rather than flat peering. Hub-and-spoke topology has the following benefits:

  * **Traffic segregation:** isolate traffic across specialized VPCs (for example, `vpc-trust` for internal routing, `vpc-mgmt` for appliance management, and `vpc-untrust`).
  * **Boundary protection:** direct traffic through specialized inspection VPCs equipped with clustered next-generation firewalls (NGFW) to sanitize ingress and egress traffic.
  * **Lateral insulation:** configure NCC hubs to ensure that spoke networks that serve application data cannot communicate directly with one another, eliminating lateral movement vectors.



## Application guardrails

To help protect the application layer and backing models from typical injection or exfiltration risks, implement the following:

  * **Private load balancing:** expose frontend applications using a regional external Application Load Balancer only, ensuring they are never directly accessible from the internet.
  * **[IAP](https://docs.cloud.google.com/iap/docs):** enforce strict identity and device posture verification before routing traffic to the Gemini application layer.
  * **[Model Armor](https://docs.cloud.google.com/model-armor/overview):** enable Model Armor for all backing models that run on Gemini Enterprise Agent Platform. Model Armor is required to enforce runtime payload safety, satisfy content compliance, and mitigate prompt injection vulnerabilities.



## Data protection and auditing

To help protect sovereign workloads, you can implement the following centralized auditing and immutability features:

  * **Data classification scheme:** integrate with your data classification scheme to optimize control placement.
  * **VPC Service Controls perimeters:** implement VPC Service Controls perimeters around sensitive data processing and storage environments to help prevent data exfiltration. Perimeters are mandatory for DoD IL5.
  * **KMS separation of duties:** enforce strict separation of duties for cryptographic keys. Ensure that security administrators who manage the Cloud Key Management Service key rings in the Stage 3 Security project don't have Identity and Access Management permissions to decrypt the data.
  * **Hierarchical log sinks:** forward organization-level telemetry into structured sinks that are dedicated to:

    * Admin Activity and Data Access Audit Logs
    * [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs) events
    * Google Workspace and login events
    * CIS Compliance Telemetry

Ensure that users cannot bypass telemetry forwarding.

  * **SIEM ingestion:** route logs using [Pub/Sub](https://docs.cloud.google.com/pubsub/docs) topics to specialized administrative projects where the logs flow into immutable storage repositories.

  * **Anomaly detection:** analyze events using SecOps tools like [Google Security Operations](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview) to detect violations such as abnormal API bursts to Agent Platform.

  * **Cross-tool harmonization:** integrate telemetry with [Google Threat Intelligence](https://docs.cloud.google.com/threat-intelligence), [Wiz Security Graph](https://www.wiz.io/lp/wiz-security-graph), or third-party tools to identify shadow AI endpoints or toxic configurations.

  * **Automated remediation using SOAR:** use SOAR playbooks to enable real-time defenses, such as isolating rogue model endpoints or disabling compromised tokens.




## Monitoring and AI security

Maintain observability and automated defense pipelines using the following features:

  * **API usage monitoring:** create alerts for surge detection on core LLM functions (for example, `serviceruntime.googleapis.com/api/request_count`).
  * **Hierarchical log sinks for AI:** configure hierarchical log sinks to capture AI-specific events, such as abnormal API call volume bursts to `aiplatform.googleapis.com` or [impossible travel violations](https://en.wikipedia.org/wiki/Security_information_and_event_management#Impossible_travel) by AI service accounts. Ensure that these logs flow into an immutable storage repository (for example, [BigQuery](https://docs.cloud.google.com/bigquery/docs)) that's accessible by the agency SIEM.
  * **Secure AI Framework (SAIF) alignment:** connect telemetry to the following four SAIF pillars: 
    * **Strong foundations:** validate [IAM](https://docs.cloud.google.com/iam/docs) permissions and [Cloud KMS](https://docs.cloud.google.com/kms/docs) status.
    * **Detection extensions:** track prompt injections and rogue endpoints using log filtering.
    * **Automated defenses:** use automation to quarantine or reject anomalous payloads.
    * **Platform harmonization:** act on threat intelligence (from Google Threat Intelligence or Wiz security findings).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
