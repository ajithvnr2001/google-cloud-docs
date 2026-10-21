---
url: https://docs.cloud.google.com/docs/security/bps-for-protecting-against-cryptocurrency-attacks/
title: Mitigate cryptocurrency mining attacks on Google Cloud \u00a0|\u00a0 Security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:04:39.250815+00:00
---

# Mitigate cryptocurrency mining attacks on Google Cloud  |  Security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/security/bps-for-protecting-against-cryptocurrency-attacks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Guides ](https://docs.cloud.google.com/docs/security/overview/whitepaper)



Send feedback 

#  Mitigate cryptocurrency mining attacks on Google Cloud Stay organized with collections  Save and categorize content based on your preferences. 

Cryptocurrency mining (also known as _bitcoin mining_) is the process used to create new cryptocoins and verify transactions. Cryptocurrency mining attacks occur when attackers who gain access to your environment exploit your resources to run their own mining operations at your expense.

The [H1 2026 Cloud Threat Horizons Report](https://cloud.google.com/security/report/resources/cloud-threat-horizons-report-h1-2026) warns that the window between vulnerability disclosure and active exploitation has collapsed from weeks to just days. Threat actors can move from initial entry to secondary payload deployment in less than an hour, and use large language models (LLMs) to automate credential harvesting in under 72 hours. Cryptocurrency mining can rapidly increase costs, and a cryptocurrency mining attack can cause a much larger bill than you expected. Because costs can add up quickly, you must put in place protective, detective, and mitigation measures to protect your organization.

This document is intended for security architects and administrators. It describes the best practices that you can take to help protect your Google Cloud resources from cryptocurrency mining attacks and to help mitigate the impact should an attack occur.

For information about how to respond to cryptocurrency mining alerts, see [Respond to abuse notifications and warnings](https://docs.cloud.google.com/docs/security/respond-to-abuse-misuse).

## Identify your threat vectors

To determine your organization's exposure to cryptocurrency mining attacks, you must identify the threat vectors that apply to your organization.

The H1 2026 Cloud Threat Horizons Report indicates that most attackers exploit vulnerabilities such as the following:

  * Vulnerabilities in third-party or user-managed software
  * Weak, absent, or compromised credentials
  * Cloud or application misconfigurations
  * Identity and token abuse (such as OAuth token or OpenID Connect theft)



In addition, you can subscribe to and review the following documents for a list of threat vectors:

  * Your government's cybersecurity advisories
  * [Google Cloud security bulletins](https://cloud.google.com/support/bulletins)
  * [Compute Engine security bulletins](https://docs.cloud.google.com/compute/docs/security-bulletins)
  * The security bulletins for the third-party applications that you are running in Google Cloud
  * Important [Google Cloud notifications](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts)



After you identify the threat vectors that apply to you, you can use the remaining best practices in this document to help address them.

## Protect accounts and account credentials

Attackers can exploit unguarded or mismanaged accounts to gain access to your Google Cloud resources. Google Cloud includes different options that you can configure to manage accounts and groups. Consider the following:

  * [Enable multi-factor authentication for all Google Accounts and Cloud Identity users](https://docs.cloud.google.com/docs/security/security-best-practices-catalog/secure-enterprise-foundations#enable-multi-factor-authentication-for-all-google-accounts-and-cloud-identity-users)

  * [Enable two-step verification for super admin accounts](https://docs.cloud.google.com/docs/security/security-best-practices-catalog/secure-enterprise-foundations#enable-two-step-verification-for-super-admin-accounts)

  * [Analyze and refine Identity and Access Management (IAM) permissions regularly](https://docs.cloud.google.com/docs/security/security-best-practices-catalog/secure-enterprise-foundations#analyze-and-refine-iam-permissions-regularly)

  * [Audit high-risk changes to IAM](https://docs.cloud.google.com/docs/security/security-best-practices-catalog/secure-enterprise-foundations#audit-high-risk-changes-to-iam)

  * [Restrict authorized principals](https://docs.cloud.google.com/docs/security/security-best-practices-catalog/secure-enterprise-foundations#restrict-authorized-principals)

  * [Share audit logs from Cloud Identity](https://docs.cloud.google.com/docs/security/security-best-practices-catalog/secure-enterprise-foundations#share-audit-logs-from-cloud-identity)

  * [Restrict external members in groups](https://docs.cloud.google.com/docs/security/security-best-practices-catalog/secure-enterprise-foundations#restrict-external-members-in-groups)

  * [Use Workload Identity Federation](https://docs.cloud.google.com/docs/security/security-best-practices-catalog/secure-enterprise-foundations#use-workload-identity-federation)

  * [Deactivate accounts and reset permissions when offboarding](https://docs.cloud.google.com/docs/security/security-best-practices-catalog/secure-enterprise-foundations#deactivate-accounts-and-reset-permissions-when-offboarding)

  * [Monitor group logs](https://docs.cloud.google.com/docs/security/security-best-practices-catalog/secure-enterprise-foundations#monitor-group-logs)

  * [Enforce strict OAuth 2.0 API scope limits](https://knowledge.workspace.google.com/admin/apps/control-which-apps-access-google-workspace-data)

  * [Audit third-party permissions](https://knowledge.workspace.google.com/admin/reports/oauth-log-events) and [configure alerts for high-risk events](https://developers.google.com/apps-script/guides/admin/monitor-restrict-oauth-scopes) (for example, a user authorizes an unverified application)




## Reduce internet exposure to your Compute Engine and GKE resources

Reducing internet exposure means that your attackers have fewer opportunities to find and exploit vulnerabilities. This section describes the best practices that help protect your Compute Engine VMs and your Google Kubernetes Engine (GKE) clusters from internet exposure.

### Restrict external traffic

To restrict external traffic, consider the following:

  * [Restrict external IP addresses on VMs](https://docs.cloud.google.com/docs/security/security-best-practices-catalog/infrastructure#restrict-external-ip-addresses-on-vms)

  * [Disable IPv6 unless required](https://docs.cloud.google.com/docs/security/security-best-practices-catalog/secure-enterprise-foundations#disable-ipv6-unless-required)

  * [Restrict control plane access](https://docs.cloud.google.com/docs/security/security-best-practices-catalog/infrastructure#restrict-control-plane-access)

  * [Restrict outbound traffic](https://docs.cloud.google.com/docs/security/security-best-practices-catalog/secure-enterprise-foundations#restrict-outbound-traffic)

  * [Use GKE Autopilot](https://docs.cloud.google.com/docs/security/security-best-practices-catalog/infrastructure#use-gke-autopilot)

  * [Limit inbound access to SSH and RDP ports](https://docs.cloud.google.com/docs/security/security-best-practices-catalog/secure-enterprise-foundations#limit-inbound-access-to-ssh-and-rdp-ports)




For more information about restricting external traffic, such as configuring Cloud NAT to allow outgoing communications for VMs without an external IP address or using a proxy load balancer for incoming communications, see [Securely connecting to VM instances](https://cloud.google.com/solutions/connecting-securely).

### Control access to services

To control access to services, consider the following:

  * [Enable VPC Service Controls](https://docs.cloud.google.com/docs/security/security-best-practices-catalog/secure-enterprise-foundations#enable-vpc-service-controls)

  * [Configure Context-Aware Access for Google consoles](https://docs.cloud.google.com/docs/security/security-best-practices-catalog/secure-enterprise-foundations#configure-context-aware-access-for-google-consoles)

  * Set up zero trust security with [Chrome Enterprise Premium](https://docs.cloud.google.com/chrome-enterprise-premium/docs/overview) to enable [threat and data protection](https://support.google.com/a/answer/10104463) and [access controls](https://docs.cloud.google.com/chrome-enterprise-premium/docs/access-protection)




## Secure your Compute Engine and GKE resources

Cryptocurrency mining requires compute resources. This section describes the best practices that help you secure your Compute Engine and GKE resources.

### Secure your VM images

To help secure your VM images, consider the following:

  * [Enable Shielded VM features](https://docs.cloud.google.com/docs/security/security-best-practices-catalog/infrastructure#enable-shielded-vm-features)

  * [Configure trusted image policies](https://docs.cloud.google.com/docs/security/security-best-practices-catalog/infrastructure#configure-trusted-image-policies)

  * [Use base images](https://docs.cloud.google.com/docs/security/security-best-practices-catalog/infrastructure#use-base-images)

  * [Enforce OS Login for VMs](https://docs.cloud.google.com/docs/security/security-best-practices-catalog/infrastructure#enforce-os-login-for-vms)




### Restrict service accounts

To help restrict service accounts, consider the following:

  * [Disable automatic IAM grants for default service accounts](https://docs.cloud.google.com/docs/security/security-best-practices-catalog/secure-enterprise-foundations#disable-automatic-iam-grants-for-default-service-accounts)

  * [Block the creation of external service account keys](https://docs.cloud.google.com/docs/security/security-best-practices-catalog/secure-enterprise-foundations#block-the-creation-of-external-service-account-keys)

  * [Use Workload Identity Federation](https://docs.cloud.google.com/docs/security/security-best-practices-catalog/secure-enterprise-foundations#use-workload-identity-federation)

  * [Use Workload Identity Federation for GKE](https://docs.cloud.google.com/docs/security/security-best-practices-catalog/infrastructure#use-workload-identity-federation-for-gke)

  * [Monitor usage patterns for service accounts and service account keys](https://docs.cloud.google.com/docs/security/security-best-practices-catalog/secure-enterprise-foundations#monitor-usage-patterns-for-service-accounts-and-service-account-keys)




For more best practices that help secure service accounts, see [Best practices for working with service accounts](https://docs.cloud.google.com/iam/docs/best-practices-service-accounts).

### Monitor and patch VMs and containers

To start a cryptocurrency mining attack, attackers often exploit misconfigurations and software vulnerabilities to gain access to Compute Engine and GKE resources.

To monitor and patch VMs and containers, consider the following:

  * [Scan containers for vulnerabilities](https://docs.cloud.google.com/docs/security/security-best-practices-catalog/infrastructure#scan-containers-for-vulnerabilities)

  * [Use Patch to upgrade VM instances](https://docs.cloud.google.com/docs/security/security-best-practices-catalog/infrastructure#use-patch-to-upgrade-vm-instances)

  * [Keep GKE clusters up to date](https://docs.cloud.google.com/docs/security/security-best-practices-catalog/infrastructure#keep-gke-clusters-up-to-date)

  * [Use Google Cloud Armor policies](https://docs.cloud.google.com/docs/security/security-best-practices-catalog/secure-enterprise-foundations#use-cloud-armor-policies)




## Secure your supply chain

Continuous integration and continuous delivery (CI/CD) provides a mechanism for getting your latest functionality to your customers quickly. To help prevent cryptocurrency mining attacks against your pipeline, perform code analysis and monitor your pipeline for malicious attacks.

Consider the following:

  * Implement [Supply-chain Levels for Software Artifacts (SLSA)](https://slsa.dev) guidelines to track and verify the provenance of build artifacts. Verifying provenance helps you compile untampered code from authorized pipelines.

  * [Enforce Binary Authorization](https://docs.cloud.google.com/docs/security/security-best-practices-catalog/infrastructure#enforce-binary-authorization).




For information on setting up a secure supply chain with GKE, see [Software supply chain security](https://docs.cloud.google.com/software-supply-chain-security/docs/overview).

## Manage secrets and keys

A key attack vector for unauthorized cryptocurrency mining attacks is insecure or leaked secrets. This section describes the best practices that you can use to help protect your secrets and encryption keys.

Consider the following:

  * [Rotate encryption keys every 90 days](https://docs.cloud.google.com/docs/security/security-best-practices-catalog/secure-enterprise-foundations#rotate-encryption-key-every-90-days).

  * [Set up automatic secret rotation](https://docs.cloud.google.com/docs/security/security-best-practices-catalog/secure-enterprise-foundations#set-up-automatic-secret-rotation).

  * [Rotate service account keys](https://docs.cloud.google.com/docs/security/security-best-practices-catalog/secure-enterprise-foundations#rotate-service-account-keys).

  * If at all possible, don't download encryption keys or other secrets, including service account keys.

  * If you are using GitHub or another public repository, implement tools such as [secret scanning](https://docs.github.com/en/code-security/secret-scanning/about-secret-scanning), which warns you about exposed secrets in your GitHub repositories.

  * Don't hard-code secrets in your applications. Use secret management solutions such as [Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview) and [HashiCorp Vault](https://www.vaultproject.io/) to store your secrets, rotate them regularly, and apply least privilege.




## Detect anomalous activity

To monitor for anomalous activity, configure Google Cloud and third-party monitoring tools and set up alerts. Consider the following:

  * [Monitor billing anomalies](https://docs.cloud.google.com/docs/security/security-best-practices-catalog/secure-enterprise-foundations#monitor-billing-anomalies)

  * [Configure billing alerts](https://docs.cloud.google.com/docs/security/security-best-practices-catalog/secure-enterprise-foundations#configure-billing-alerts)

  * [Enable auditing of administrator activity](https://docs.cloud.google.com/docs/security/security-best-practices-catalog/secure-enterprise-foundations#enable-auditing-of-administrator-activity)

  * [Enable Security Command Center at the organization level](https://docs.cloud.google.com/docs/security/security-best-practices-catalog/secure-enterprise-foundations#enable-security-command-center-at-the-organization-level)

  * [Inspect network traffic using Cloud Intrusion Detection System (Cloud IDS)](https://docs.cloud.google.com/docs/security/security-best-practices-catalog/secure-enterprise-foundations#inspect-network-traffic-using-cloud-ids)

  * [Enable Data Access audit logs](https://docs.cloud.google.com/docs/security/security-best-practices-catalog/secure-enterprise-foundations#enable-data-access-audit-logs)

  * Monitor for bulk API activity such as mass Cloud Storage downloads, BigQuery exports, and anomalous data movement (for example, monitor the `storage.objects.get`, `storage.objects.list`, and `jobservice.insert` methods)

  * Monitor for export jobs that target public Cloud Storage buckets or unfamiliar Google Cloud projects that are outside your organization (for example, [Exfiltration: BigQuery Data Extraction](https://docs.cloud.google.com/security-command-center/docs/findings/threats/big-query-exfil-to-cloud-storage))




### Participate in the Security Command Center Cryptomining Protection Program

If you are a Security Command Center Premium customer and use Compute Engine, you can participate in the [Security Command Center Cryptomining Protection Program](https://cloud.google.com/security-command-center/cryptomining-protection-program). This program lets you defray the Compute Engine VM costs related to undetected and unauthorized cryptomining attacks in your Compute Engine VM environment. You must implement the [cryptomining detection best practices](https://docs.cloud.google.com/security-command-center/docs/cryptomining-detection-best-practices), some of which overlap with the other best practices that are described on this page.

## Update your incident response plan

Ensure that your incident response plan and your playbooks provide prescriptive guidance for how your organization responds to cryptocurrency mining attacks. For example, ensure that your plan includes the following:

  * How to file a [support case](https://cloud.google.com/support/docs/procedures#create_a_support_case) with Cloud Customer Care and contact your [Google technical account manager (TAM)](https://cloud.google.com/tam). If you don't have a support account, review the available [support plans](https://cloud.google.com/support) and create one.
  * How to tell the difference between legitimate [high performance computing (HPC)](https://cloud.google.com/solutions/hpc) workloads and cryptocurrency mining attacks. For example, you can tag which projects have HPC enabled, and set up alerts for unexpected cost increases.
  * How to deal with [compromised Google Cloud credentials](https://docs.cloud.google.com/docs/security/compromised-credentials).
  * How to quarantine infected systems and restore from healthy backups.
  * Who in your organization must be notified to investigate and respond to the attack.
  * What information needs to be logged for your retrospective activities.
  * How to verify that your remediation activities effectively removed the mining activities and addressed the initial vulnerability that led to the attack.
  * How to respond to an alert sent from Customer Care. For more information, see [Policy violations FAQ](https://support.google.com/cloud/answer/7002354).



For more information, see [Respond to and recover from attacks](https://docs.cloud.google.com/docs/security/mitigating-ransomware-attacks#respond-to-recover-from-attacks).

## Implement a disaster recovery plan

To prepare for a cryptocurrency mining attack, complete [business continuity](https://cloud.google.com/solutions/security-and-resilience) and [disaster recovery plans](https://docs.cloud.google.com/architecture/dr-scenarios-planning-guide), create an incident response playbook, and perform tabletop exercises.

If unauthorized cryptocurrency mining occurs, ensure that you can address the threat vector that caused the initial breach and that you can reconstruct your environment from a known good state. Your disaster recovery plan must define what a known good state is so that the attacker can't repeatedly use the same vulnerabilities to exploit your resources.

## What's next

  * Find more security best practices in the [Google Cloud security best practices catalog](https://docs.cloud.google.com/docs/security/security-best-practices-catalog).
  * [Protect against ransomware attacks](https://docs.cloud.google.com/docs/security/mitigating-ransomware-attacks).
  * Deploy a secure baseline in Google Cloud, as described in the [Google Cloud enterprise foundations blueprint](https://docs.cloud.google.com/architecture/blueprints/security-foundations).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
