---
url: https://docs.cloud.google.com/vmware-engine/docs/concepts-security/
title: VMware Engine security overview \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:13.963555+00:00
---

# VMware Engine security overview  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/concepts-security/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/vmware-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# VMware Engine security overview

This page describes the security features VMware Engine uses to help keep your data and environment secure. For a detailed list of what you, the customer are responsible for and what Google is responsible for, see [VMware Engine shared responsibility model](https://docs.cloud.google.com/vmware-engine/docs/shared-responsibility).

## Dedicated hardware

As part of the VMware Engine service, all customers get dedicated bare metal hosts with local attached disks that are physically isolated from other hardware. An ESXi hypervisor with vSAN runs on every node. The nodes are managed through customer dedicated VMware vCenter and NSX. Not sharing hardware between tenants provides an additional layer of isolation and security protection.

## Data security

Customers keep control and ownership of their data. Stewardship of customer data is the responsibility of the customer.

### Data protection for data at rest and data in transit within internal networks

Data at rest in the private cloud environment can be encrypted using vSAN software based encryption. vSAN encryption relies on external Key Management Solutions to store encryption keys.

VMware Engine enables vSAN data at rest encryption by default for any new private clouds deployed, with key management infrastructure managed by Google as part of the service. For details related to the default encryption model, see [About vSAN encryption](https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/howto-vsan-encryption#gmek).

To help decide between Google-managed or customer-managed encryption keys, see [Choose a key management solution](https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/howto-vsan-encryption#choose-solution). If you want to manage encryption keys yourself, you can use [Customer-Managed Encryption Keys (CMEK)](https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/howto-vsan-encryption#cmek). Alternatively, you can deploy external key management infrastructure from a validated KMS provider and configure it as a key provider in vCenter. For more information, see [External KMS](https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/howto-vsan-encryption#supported-vendors).

For data in transit, we expect applications to encrypt their network communication within internal network segments. vSphere supports encryption of data over the wire for vMotion traffic.

### Data protection for data that is required to move through public networks

To protect data that moves through public networks, you can create IPsec and SSL VPN tunnels for your private clouds. Common encryption methods are supported, including 128-byte and 256-byte AES. Data in transit (including authentication, administrative access, and customer data) is encrypted with standard encryption mechanisms (SSH, TLS 1.2, and Secure RDP). Communication that transports sensitive information uses the standard encryption mechanisms.

### Secure disposal

If your service expires or is terminated, you are responsible for removing or deleting your data. Google will cooperate with you to delete or return all customer data as provided in the customer agreement, except to the extent that Google is required by applicable law to retain some or all of the personal data. If necessary to retain any personal data, Google will archive the data and implement reasonable measures to prevent the customer data from any further processing.

#### Erasure of customer data

Every time a VMware Engine node is taken out of a customer-provisioned VMware cluster, the drives are erased to remove all customer data present on the disk. This erasure is performed after the following actions:

  * deletion of a VMware Engine private cloud
  * deletion of a cluster within a private cloud
  * automated and manual removal of a node from a cluster



#### Hardware end of life

At the end of life of hardware, VMware Engine decommissions the servers and takes them out of the production network. At that point, the drives are physically destroyed according to Google security guidelines. This destruction is in addition to the disk erasure described previously.

### Data location

Your application data is located in the region you selected during the private cloud creation. The service does not change the location of the data on its own without specific customer action or trigger (for example, user-configured replication to a private cloud in a different Google Cloud region). However, if your use case requires, you can deploy your workloads across regions and configure replication and data migration between regions.

### Data backups

VMware Engine does not back up or archive customer application data that resides within VMware virtual machines. VMware Engine periodically backs up vCenter and NSX configuration. Prior to backup, all data is encrypted at the source management server (for example, vCenter) using VMware APIs. The encrypted backup data is transported and stored in Cloud Storage buckets.

## Network security

Google Cloud VMware Engine relies on layers of network security.

### Edge security

The Google Cloud VMware Engine service runs within Google Cloud under the baseline network security provided by Google Cloud. This applies to both the VMware Engine application and the dedicated and private VMware environment. Google Cloud provides built-in protection against distributed denial-of-service (DDoS) attacks. VMware Engine also follows the defense-in-depth strategy for helping to secure the network edge by implementing security controls like firewall rules and NAT.

### Segmentation

VMware Engine has logically separate Layer 2 networks that restrict access to your own internal networks in your private cloud environment. You can further protect your private cloud networks by using a firewall. The Google Cloud console lets you define rules for EW and NS network traffic controls for all network traffic, including intra-private cloud traffic, inter-private cloud traffic, general traffic to the internet, and network traffic to the on-premises environment.

## Vulnerability and patch management

Google is responsible for periodic security patching of managed VMware software (ESXi, vCenter, and NSX).

## Identity and Access Management

You can authenticate to Google Cloud console from Google Cloud using SSO. You grant access to users to access Google Cloud console using [IAM roles and permissions](https://docs.cloud.google.com/vmware-engine/docs/iam).

By default, VMware Engine creates a user account for you in the vCenter local domain of the private cloud. You can add new local users or configure the vCenter to use an existing identity source. For this, add either an existing on-premises identity source or a new identity source within the private cloud.

The default user has sufficient privileges to perform necessary day-to-day vCenter operations of the vCenter within the private cloud, but they don't have full administrator access to vCenter. If administrator access is temporarily required, you can elevate your privileges for a limited period of time while you complete the administrator tasks.

Some third-party tools and products used with your private cloud might require a user to have administrative privileges in vSphere. When you create a private cloud, VMware Engine also creates [solution user accounts](https://docs.cloud.google.com/vmware-engine/docs/vmware-platform/howto-solution-user-accounts) with administrative privileges that you can use with the third-party tools and products.

## Compliance

Google Cloud remains committed to continually expand our coverage against the most important compliance standards. VMware Engine has achieved [ISO/IEC 27001](https://docs.cloud.google.com/security/compliance/iso-27001), [27017](https://docs.cloud.google.com/security/compliance/iso-27017), [27018](https://docs.cloud.google.com/security/compliance/iso-27018); [PCI-DSS](https://docs.cloud.google.com/security/compliance/pci-dss); [SOC 1](https://docs.cloud.google.com/security/compliance/soc-1), [SOC 2](https://docs.cloud.google.com/security/compliance/soc-2), and [SOC 3](https://docs.cloud.google.com/security/compliance/soc-3) compliance certifications, among others. Further, Google Cloud Business Associate Agreement (BAA) also covers VMware Engine.

For assistance with auditing, contact your account representative for the latest ISO certificates, SOC reports, and self assessments.

## What's next

  * Learn more about the [VMware Engine security shared responsibility model](https://docs.cloud.google.com/vmware-engine/docs/shared-responsibility).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
