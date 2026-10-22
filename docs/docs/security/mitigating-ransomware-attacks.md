---
url: https://docs.cloud.google.com/docs/security/mitigating-ransomware-attacks/
title: Mitigate ransomware attacks using Google Cloud \u00a0|\u00a0 Security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:23:39.432828+00:00
---

# Mitigate ransomware attacks using Google Cloud  |  Security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/security/mitigating-ransomware-attacks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Guides ](https://docs.cloud.google.com/docs/security/overview/whitepaper)



Send feedback 

#  Mitigate ransomware attacks using Google Cloud Stay organized with collections  Save and categorize content based on your preferences. 

Ransomware is code created by a third party to infiltrate your systems and hijack, encrypt, or steal data. To help you mitigate ransomware attacks, Google Cloud provides you with controls for identifying, protecting, detecting, responding to, and recovering from attacks. These controls help you accomplish the following:

  * Assess your risk.
  * Protect your business from threats.
  * Maintain continuous operations.
  * Enable rapid response and recovery.



This document is intended for security architects and administrators. It describes the ransomware attack sequence and how Google Cloud can help your organization mitigate the effects of ransomware attacks.

## Ransomware attack sequence

Ransomware attacks can start as mass campaigns looking for potential vulnerabilities or as directed campaigns. A directed campaign starts with identification and reconnaissance, where an attacker determines which organizations are vulnerable and what attack vector to use.

There are many ransomware attack vectors. The most common vectors are phishing emails with malicious URLs or exploiting an exposed software vulnerability. This software vulnerability can be in the software that your organization uses, or a vulnerability that exists in your software supply chain. Ransomware attackers target organizations, their supply chain, and their customers.

When the initial attack is successful, the ransomware installs itself and contacts the command and control server to retrieve the encryption keys. As ransomware spreads throughout the network, it can infect resources, encrypt data using the keys that it retrieved, and exfiltrate data. Attackers demand a ransom, typically in cryptocurrency, from the organization so that they can get the decryption key.

The following diagram summarizes the typical ransomware attack sequence, from identification and reconnaissance to data exfiltration and ransom demand.

![The ransomware attack sequence.](https://docs.cloud.google.com/static/docs/security/images/ransomware-attack-sequence.svg)

Ransomware is often difficult to detect. It's critical, therefore, that you put in place prevention, monitoring, and detection capabilities, and that your organization is ready to respond swiftly when someone discovers an attack.

## Security and resiliency controls in Google Cloud

Google Cloud includes built-in security and resiliency controls to help protect customers against ransomware attacks. These controls include the following:

  * Global infrastructure designed with security throughout the information-processing lifecycle
  * Built-in detective features for Google Cloud products and services, such as monitoring, threat detection, data loss prevention, and access controls
  * Built-in preventive controls, such as Assured Workloads
  * High availability with regional clusters and global load balancers
  * Built-in backup, with scalable services
  * Automation capabilities using Infrastructure as Code and configuration guardrails



[Google Threat Intelligence](https://cloud.google.com/security/products/threat-intelligence), [VirusTotal](https://www.virustotal.com/gui/intelligence-overview), and [ Mandiant Digital Threat Monitoring](https://cloud.google.com/security/products/digital-threat-monitoring) track and respond to many types of malware, including ransomware, across Google infrastructure and products. Google Threat Intelligence is a team of threat researchers that develop threat intelligence for Google Cloud products. VirusTotal is a malware database and visualization solution that provides you with a better understanding of how malware operates within your enterprise. Mandiant Digital Threat Monitoring and other Mandiant services provide threat research, consultation, and incident response support.

For more information about built-in security controls, see the [Google security overview](https://docs.cloud.google.com/docs/security/overview/whitepaper) and [Google infrastructure security design overview](https://docs.cloud.google.com/docs/security/infrastructure/design).

## Security and resiliency controls in Google Workspace, Chrome browser, and Chromebooks

In addition to the controls within Google Cloud, other Google products like Google Workspace, Google Chrome browser, and [Chromebooks](https://www.google.com/chromebook/dr/shop/) include security controls that can help protect your organization against ransomware attacks. For example, Google products provide security controls that allow remote workers to access resources from anywhere, based on their identity and context (such as location or IP address).

As described in the Ransomware attack sequence section, email is a key vector for many ransomware attacks. It can be exploited to phish credentials for fraudulent network access and to distribute ransomware binaries directly. [Advanced phishing and malware protection](https://support.google.com/a/answer/9157861) in Gmail provides controls to quarantine emails, defends against dangerous attachment types, and helps protect users from inbound spoofing emails. [Security Sandbox](https://support.google.com/a/answer/7676854?ref_topic=9974692) is designed to detect the presence of previously unknown malware in attachments.

Chrome browser includes [Google Safe Browsing](https://safebrowsing.google.com/), which is designed to provide warnings to users when they attempt to access an infected or malicious site. [Sandboxes](https://privacysandbox.com/) and [site isolation](http://www.chromium.org/Home/chromium-security/site-isolation) help protect against the spread of malicious code within different processes on the same tab. [Password protection](https://support.google.com/chrome/answer/10311524#zippy=%2Chow-password-protection-works) is designed to provide alerts when a corporate password is being used on a personal account, and checks whether any of the user's saved passwords have been compromised in an online breach. In this scenario, the browser prompts the user to change their password.

The following [Chromebook features](https://chromeenterprise.google/solutions/secure-browsing/) help to protect against phishing and ransomware attacks:

  * **Read-only operating system ([Chrome OS](https://chromeos.google/)):** This system is designed to update constantly and invisibly. Chrome OS helps protect against the most recent vulnerabilities and includes controls that help ensure that applications and extensions can't modify it.
  * **Sandboxing:** Each application runs in an isolated environment, so one harmful application can't easily infect other applications.
  * **Verified boot:** While the Chromebook is booting, it is designed to check that the system hasn't been modified.
  * **[Safe Browsing](https://support.google.com/chrome/answer/13844634):** Chrome periodically downloads the most recent Safe Browsing list of unsafe sites. It is designed to check the URLs of each site that a user visits and checks each file that a user downloads against this list.
  * **Google security chips:** These chips help protect the operating system from malicious tampering.



To help reduce your organization's attack surface, consider Chromebooks for users who work primarily in a browser.

## Best practices for mitigating ransomware attacks on Google Cloud

To protect your enterprise resources and data from ransomware attacks, you must put multi-layered controls in place across your on-premises and cloud environments.

The following sections describe best practices to help your organization identify, prevent, detect, and respond to ransomware attacks on Google Cloud.

### Identify your risks and assets

Consider the following best practices to identify your risks and assets in Google Cloud:

  * [Maintain an inventory of your resources in Google Cloud](https://docs.cloud.google.com/docs/security/security-best-practices-catalog/secure-enterprise-foundations#maintain-an-inventory-of-your-resources-in-google-cloud).
  * [Use audit logs](https://docs.cloud.google.com/docs/security/security-best-practices-catalog/secure-enterprise-foundations#use-audit-logs).
  * Use [attack path simulations](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn) in Security Command Center Premium to assess your current risk profile.
  * Consider cyber insurance options available through the [Risk Protection Program](https://cloud.google.com/security/products/risk-protection-program).
  * [Enable Sensitive Data Protection for data inspection](https://docs.cloud.google.com/docs/security/security-best-practices-catalog/data-management#enable-sensitive-data-protection-for-data-inspection).



### Control access to your resources and data

Consider the following best practices to limit access to Google Cloud resources and data:

  * [Analyze and refine Identity and Access Management (IAM) permissions regularly](https://docs.cloud.google.com/docs/security/security-best-practices-catalog/secure-enterprise-foundations#analyze-and-refine-iam-permissions-regularly).

  * [Use Workload Identity Federation](https://docs.cloud.google.com/docs/security/security-best-practices-catalog/secure-enterprise-foundations#use-workload-identity-federation).

  * [Enable multi-factor authentication for all Google Accounts and Cloud Identity users](https://docs.cloud.google.com/docs/security/security-best-practices-catalog/secure-enterprise-foundations#enable-multi-factor-authentication-for-all-google-accounts-and-cloud-identity-users).

  * [Enable two-step verification for super admin accounts](https://docs.cloud.google.com/docs/security/security-best-practices-catalog/secure-enterprise-foundations#enable-two-step-verification-for-super-admin-accounts).




For more best practices on protecting service accounts, see [Best practices for using service accounts](https://docs.cloud.google.com/iam/docs/best-practices-service-accounts).

### Protect critical data

Consider the following best practices to help protect your sensitive data:

  * Configure redundancy (N+2) on the cloud storage option that you use to store your data. If you use Cloud Storage, consider the following:

    * [Ensure Cloud Storage bucket retention policy uses Bucket Lock](https://docs.cloud.google.com/docs/security/security-best-practices-catalog/data-management#ensure-cloud-storage-bucket-retention-policy-uses-bucket-lock).
    * [Enforce versioning for Cloud Storage buckets](https://docs.cloud.google.com/docs/security/security-best-practices-catalog/data-management#enforce-versioning-for-cloud-storage-buckets).
  * [Implement and test database backups](https://docs.cloud.google.com/docs/security/security-best-practices-catalog/data-management#implement-and-test-database-backups).

  * [Implement a backup and disaster recovery strategy](https://docs.cloud.google.com/docs/security/security-best-practices-catalog/infrastructure#implement-a-backup-and-disaster-recovery-strategy).

  * [Rotate service account keys](https://docs.cloud.google.com/docs/security/security-best-practices-catalog/secure-enterprise-foundations#rotate-service-account-keys).

  * [Monitor key-related activities](https://docs.cloud.google.com/docs/security/security-best-practices-catalog/secure-enterprise-foundations#monitor-key-related-activities).




### Secure network and infrastructure

Consider the following best practices to help secure your network and infrastructure:

  * [Use Infrastructure as Code for secure baselines](https://docs.cloud.google.com/docs/security/security-best-practices-catalog/secure-enterprise-foundations#use-infrastructure-as-code-for-secure-baselines).
  * [Enable VPC Service Controls](https://docs.cloud.google.com/docs/security/security-best-practices-catalog/secure-enterprise-foundations#enable-vpc-service-controls).
  * [Secure hybrid connections using Cloud VPN or Cloud Interconnect](https://docs.cloud.google.com/docs/security/security-best-practices-catalog/secure-enterprise-foundations#use-cloud-vpn-or-cloud-interconnect-in-hybrid-environments).
  * Use [Cloud Load Balancing](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview) with [firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls).
  * Implement [restrictive organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints) such as the following:

    * [Disable root access on Agent Platform Workbench user-managed notebooks and instances](https://docs.cloud.google.com/docs/security/security-best-practices-catalog/tools-inference#disable-root-access-on-agent-platform-workbench-user-managed-notebooks-and-instances).
    * [Restrict Cloud SQL public IP addresses](https://docs.cloud.google.com/docs/security/security-best-practices-catalog/data-management#restrict-cloud-sql-public-ip-addresses).
    * [Disable VM serial port access](https://docs.cloud.google.com/docs/security/security-best-practices-catalog/infrastructure#disable-vm-serial-port-access).
    * [Enable Shielded VM features](https://docs.cloud.google.com/docs/security/security-best-practices-catalog/infrastructure#enable-shielded-vm-features).



### Protect your workloads

Consider the following best practices to help protect your workloads:

  * Integrate security into every phase of your software development lifecycle. For Google Kubernetes Engine (GKE) workloads, implement [software supply chain security](https://docs.cloud.google.com/software-supply-chain-security/docs/overview), including trusted builds and application isolation.
  * [Restrict traffic among pods](https://docs.cloud.google.com/docs/security/security-best-practices-catalog/infrastructure#restrict-traffic-among-pods).
  * Use [Cloud Build](https://docs.cloud.google.com/build/docs/overview) with [On-Demand Scanning](https://docs.cloud.google.com/artifact-analysis/docs/ods-cloudbuild) to perform vulnerability scanning before code commits.
  * [Configure vulnerability scanning for artifacts](https://docs.cloud.google.com/docs/security/security-best-practices-catalog/agents-applications#configure-vulnerability-scanning-for-artifacts).
  * [Enforce Binary Authorization](https://docs.cloud.google.com/docs/security/security-best-practices-catalog/infrastructure#enforce-binary-authorization).
  * [Use Google Cloud Armor policies](https://docs.cloud.google.com/docs/security/security-best-practices-catalog/secure-enterprise-foundations#use-cloud-armor-policies).
  * [Keep GKE clusters up-to-date](https://docs.cloud.google.com/docs/security/security-best-practices-catalog/infrastructure#keep-gke-clusters-up-to-date).



### Detect attacks

Consider the following best practices to help you detect attacks:

  * Use [Cloud Logging](https://docs.cloud.google.com/logging/docs/overview) to manage and analyze the logs from your services in Google Cloud and [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview) to measure the performance of your service and resources.
  * [Enable Security Command Center at the organization level](https://docs.cloud.google.com/docs/security/security-best-practices-catalog/secure-enterprise-foundations#enable-security-command-center-at-the-organization-level).
  * For runtime threat detection of VM and containerized workloads, use [Wiz Defend](https://www.wiz.io/products/wiz-defend) with Wiz Runtime Sensor to detect and respond to active threats.
  * For deep security analysis and threat hunting, [integrate with Google Security Operations](https://cloud.google.com/security/products/security-operations).



### Plan for incidents

  * Complete [business continuity](https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns-and-practices/business-continuity-patterns) and [disaster recovery plans](https://docs.cloud.google.com/architecture/dr-scenarios-planning-guide).

  * Create a ransomware incident response playbook, and perform tabletop exercises. Regularly practice recovery procedures to help ensure readiness and identify gaps.

  * Understand your obligations for reporting attacks to authorities and include relevant contact information in your playbook.




## Respond to and recover from attacks

When you detect a ransomware attack, activate your incident response plan. After you confirm that the incident isn't a false positive and that it affects your Google Cloud services, open a [P1 support case](https://docs.cloud.google.com/support/docs/procedures#create_a_support_case). [Cloud Customer Care](https://cloud.google.com/support-hub) responds as documented in the [Google Cloud: Technical Support Services Guidelines](https://cloud.google.com/terms/tssg/).

After you activate your plan, gather the team within your organization that needs to be involved in your incident coordination and resolution processes. Ensure that these tools and processes are in place to investigate and resolve the incident.

Follow your incident response plan to remove the ransomware and restore your environment to a healthy state. Depending on the severity of the attack and the security controls that you have enabled, your plan can include activities such as the following:

  * Quarantining infected systems.
  * Restoring from healthy backups.
  * Restoring your infrastructure to a previously known good state using your CI/CD pipeline.
  * Verifying that the vulnerability was removed.
  * Patching all systems that might be vulnerable to a similar attack.
  * Implementing the controls that you require to avoid a similar attack.



As you progress through your response process, continue to monitor your Google support ticket. Customer Care takes appropriate actions within Google Cloud to contain, eradicate, and (if possible) recover your environment.

Inform Customer Care when your incident is resolved and your environment is restored. If one is scheduled, participate in a joint retrospective with your Google representative.

Ensure that you capture any lessons learned from the incident, and set in place the controls that you require to avoid a similar attack. Depending on the nature of the attack, you could consider the following actions:

  * Write detection rules and alerts that would automatically trigger should the attack occur again.
  * Update your incident response playbook to include any lessons learned.
  * Improve your security posture based on your retrospective findings.



## What's next

  * Contact [Mandiant consultants for a cyber defense assessment](https://cloud.google.com/security/consulting/mandiant-cyber-defense-assessment).
  * Review the [security best practices catalog](https://docs.cloud.google.com/docs/security/security-best-practices-catalog) for additional best practices.
  * For information on how Google manages incidents, see [Data incident response process](https://docs.cloud.google.com/docs/security/incident-response).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
