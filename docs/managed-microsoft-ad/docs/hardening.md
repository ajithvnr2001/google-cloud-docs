---
url: https://docs.cloud.google.com/managed-microsoft-ad/docs/hardening/
title: About security hardening \u00a0|\u00a0 Managed Service for Microsoft Active Directory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:38:21.295214+00:00
---

# About security hardening  |  Managed Service for Microsoft Active Directory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-microsoft-ad/docs/hardening/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Managed Microsoft AD ](https://docs.cloud.google.com/managed-microsoft-ad/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-microsoft-ad/docs/overview)



Send feedback 

#  About security hardening Stay organized with collections  Save and categorize content based on your preferences. 

This topic explains the various measures that we take to harden Managed Service for Microsoft Active Directory and minimize security vulnerabilities.

## No public internet access

To improve security, Managed Microsoft AD is not exposed to the public internet. Managed Microsoft AD makes all connections through private IP from authorized networks:

  * Hosting: Managed Microsoft AD hosts every VM that runs Active Directory in their own [VPC](https://docs.cloud.google.com/vpc/docs), which isolates users from each other.

  * Connecting: You can use authorized networks to connect to Managed Microsoft AD through private IP. Managed Microsoft AD handles the [VPC peering](https://docs.cloud.google.com/vpc/docs/vpc-peering) for these connections.

  * Patching: Managed Microsoft AD applies Windows patches to the Managed Microsoft AD VMs without using public internet access. For more information about how Managed Microsoft AD handles patching, see [Patching](https://docs.cloud.google.com/managed-microsoft-ad/docs/hardening#patching).




## Shielded VM

[Shielded VMs](https://docs.cloud.google.com/security/shielded-cloud/shielded-vm) are virtual machines (VMs) hardened by a set of security controls that help defend against rootkits and bootkits. Shielded VM's features protect all Managed Microsoft AD VMs at no additional cost.

## OS image

Managed Microsoft AD VMs are seeded from the [public Compute Engine Windows Server 2019 image](https://docs.cloud.google.com/compute/docs/images). These images have [Shielded VM](https://docs.cloud.google.com/security/shielded-cloud/shielded-vm) features enabled and are optimized for running on Compute Engine infrastructure.

## Microsoft security baselines

In addition to the security measures provided by Managed Microsoft AD, you can also opt in for applying Microsoft security baselines on your Managed Microsoft AD VMs. These baselines are industry-standard security configuration settings that Managed Microsoft AD can apply on your Managed Microsoft AD instances and domain controllers.

We recommend that you review these baselines and test them on your development or staging Managed Microsoft AD instances before opting to apply on the production instances. You can [contact support](https://docs.cloud.google.com/managed-microsoft-ad/docs/get-support) to learn more about these baselines or to opt in for applying these settings.

## Security monitoring and protection

We use the operating system's built-in antivirus to protect the Managed Microsoft AD instances against virus and malwares. The antivirus scans your Managed Microsoft AD VMs and detects security threats, such as viruses, malware, and spyware. The antivirus then logs these security events which we analyze and remediate if required.

## Patching

Microsoft releases bug fixes, security updates, and feature improvements on a regular basis. These patches are crucial to keep your domain controllers up to date and safe.

Managed Microsoft AD tests all these patches before applying them on your domain controllers. During testing, Managed Microsoft AD validates customer use cases, availability, security, and reliability. After a patch passes these tests, Managed Microsoft AD applies it on your domain controllers.

### Availability during patching

While applying the patches and updates, the Active Directory domain remains available. However, you can't perform any mutate operations on these domains, such as extending the schema, updating the domain, and connecting with SQL Server or Cloud SQL. Also, Managed Microsoft AD doesn't apply patches to domains for which you have already initiated mutate operations until the operation is complete.

Managed Microsoft AD ensures that there are at least two domain controllers running per region for a domain in different availability zones. Managed Microsoft AD updates one domain controller at a time. For each domain controller update, Managed Microsoft AD adds and promotes a new domain controller, with the latest validated patch. After the new domain controller reaches a healthy state, Managed Microsoft AD demotes the existing domain controller. The new domain controller comes into use when Managed Microsoft AD promotes it. The old domain controller stops serving requests after Managed Microsoft AD demotes it. This process ensures that there are at least two domain controllers running in each region at any time.

To ensure that your applications can reach the active domain controller, the applications can use the Windows DC locator service. This enables your applications to reconnect with the new domain controllers during the automated patching process.

### Patching schedule

We have the objective of testing and applying patches on all Managed Microsoft AD domain controllers within 21 business days of when Microsoft releases a monthly patch for Windows Server. However, we prioritize and apply critical security vulnerability patches that Microsoft releases for domain controllers within 15 business days.

## Credential rotation and encryption

Managed Microsoft AD uses several methods to protect credentials. Managed Microsoft AD frequently rotates credentials and encrypts them using industry-standard techniques. Credentials created for managing AD are never shared between instances. Only a smaller-sized support team and automated systems can access these credentials. Managed Microsoft AD destroys these credentials when it deletes the instance.

## Restricted production access

Managed Microsoft AD employs multiple systems and processes to ensure that Google Cloud engineers have minimal access to the Managed Microsoft AD domain. Only a small number of on-call engineers have access to production data. They access production environment only to perform a recovery on a domain or advanced troubleshooting. These accesses require a validated justification before they can proceed, and then Managed Microsoft AD logs and audits them internally. Managed Microsoft AD automates most accesses such that they cannot access AD data. In rare scenarios, there might be a need for on-call engineers to remotely access domain controllers. In these cases, the remote accesses use [Identity-Aware Proxy (IAP)](https://docs.cloud.google.com/iap/docs/concepts-overview), not the public internet.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
