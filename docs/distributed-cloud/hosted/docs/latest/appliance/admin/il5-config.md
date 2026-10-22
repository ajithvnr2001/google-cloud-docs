---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/il5-config/
title: Google Distributed Cloud air-gapped appliance IL5 configuration \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:57:16.563763+00:00
---

# Google Distributed Cloud air-gapped appliance IL5 configuration  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/il5-config/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Google Distributed Cloud air-gapped appliance IL5 configuration Stay organized with collections  Save and categorize content based on your preferences. 

Google Cloud supports the Department of Defense and partner organizations that must meet IL5 data requirements in Google Cloud US regions. Google Distributed Cloud (GDC) air-gapped appliance must meet IL5 requirements defined in the [US Department of Defense (DoD) Cloud Computing Security Requirements Guide (SRG)](https://public.cyber.mil/dccs/dccs-documents/). The configuration guidance provided on this page helps regulated customers deploy IL5 regulated workloads on Google Distributed Cloud air-gapped appliance. This document also addresses how to configure GDC air-gapped appliance to work with Google Cloud's Assured Workloads service, the [IL5 Software Defined Community Cloud](https://cloud.google.com/blog/products/identity-security/software-defined-community-cloud-new-way-goveGoogle%20Cloudrnment-cloud#:%7E:text=A%20community%20cloud%20is%20defined,policy%2C%20and%20compliance%20considerations).

## GDC air-gapped appliance impact level 5 configuration approach

Unlike an enterprise cloud platform, DoD customers have sole custody of their appliance's physical hardware and the data stored on it. The appliance is also a single-tenant platform, which achieves both Compute and Storage Isolation in accordance with [SRG Section 5.2.2.3](https://public.cyber.mil/dccs/dccs-documents/) and [SRG Section 5.2.4.1](https://public.cyber.mil/dccs/dccs-documents/).

When using Google Cloud in a connected mode, customers must also ensure that their Google Cloud environment is configured for IL5 by leveraging Assured Workloads.

## Stay in compliance

GDC air-gapped appliance customers should operate their deployed units in accordance with IL5 guidelines.

## Access and authorization

**Manage the identity provider** : Department of Defense customers have two options for configuring an identity provider:

  1. Use the pre-installed Keycloak identity provider and configure Keycloak to be compliant. Google provides a [detailed overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/keycloak-compliance) of all settings that must be configured by DoD customers in accordance with their policies and the DoD SRG, such as password policies, two factor authentication, certificate management, login attempt thresholds, audit logging, and initial administrator account management.
  2. Integrate with an existing [identity provider](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/iam/connect-identity) and configure it to be compliant with government policies and DoD SRG requirements.



**[Grant and revoke access](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/iam/set-up-role-bindings)** : Department of Defense customers must manage access to clusters within their appliances as well as cloud workloads. Customers are also responsible for periodic access reviews for user accounts.

  * [Manage access to clusters](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/iam/set-up-role-bindings): Department of Defense customers are responsible for managing IO/PA/AO access to clusters.
  * [Manage access to project resources](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/iam/role-bindings): Department of Defense customers are responsible for managing PA/AO access to project resources.



**[Manage service identities](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/iam/service-identity)** : Department of Defense customers must securely manage service identities and follow the principle of least privilege for all service accounts by only granting the minimum roles required to function. Customers are also responsible for periodic access reviews for service accounts.

**Rotate credentials and certificates** : Customers are responsible for rotating default credentials and certificates, rotating credentials and certificates periodically, and rotating credentials and certificates when compromise is suspected. This includes but is not limited to: [network appliances](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/rotate-cert), [object storage keys](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/object-storage-key-rotation), [TLS certificates](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/storage-cert-rotation), [disk encryption keys](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/disk-encryption-key-rotation), and [storage authentication keys](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/storage-auth-key-rotation).

## Storage and encryption

**Customer-Managed Encryption Keys (CMEK)** : Customers are responsible for managing the keys for the appliance's Linux Unified Key Setup (LUKS) based [disk encryption](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/boot-disk-encryption) by leveraging the Yubikeys provided. Customers are required to remove the Yubikeys for transport, label them in accordance with their classification, and ship them separately.

**Storage volume utilization** : Customers are responsible for monitoring the storage utilization of their appliances, to include audit log storage. Appliances have limited onboard storage, so it's important to monitor when a [data transfer](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/transfer-data) to a data center is required.

## Logging

GDC air-gapped appliance provides multiple [logging sources](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform-application/pa-ao-operations/audited-components) out of the box to meet compliance requirements. Customers are responsible for centralized storage, managing log retention, and periodic log reviews.

**[Set up a central log server](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/set-up-central-logs-server)** : Customers must set up a central log server for long-term retention. Google strongly recommends writing logs to a WORM storage bucket in the customer's IL5 Google Cloud or IL6 GDC air-gapped data center organization to ensure logs are available if an appliance is lost, damaged, or destroyed. The appliance also has limited onboard storage that might not be sufficient for long-term storage requirements. Offboarding logs periodically requires some connectivity to occur, which might vary in availability depending on operational needs or organizational policy.

**[Back up audit logs](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/audit-backup-restore)** : Customers must back up audit logs to ensure recovery and reconstitution can occur following any catastrophic failure.

**[Set up logging for log transfer jobs](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/transfer-data#optional_define_a_loggingtarget_to_see_logs_in_loki)** : Customers must set up logs and alerts for log transfer jobs. This ensures that customers are notified when a log transfer fails.

**[Create custom alert rules](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/create-alert-rules)** : Customers should set up custom alert rules for organizationally-defined indicators of compromise.

**Query and view[logs](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/query-and-view-logs)** and **[alerts](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/query-and-view-alerts)** : Customers are required to periodically review logs and alerts. Customers can use the appliance's monitoring capability or by leveraging their own SIEM solution from the centralized log server. Customers should set up [dashboards](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/create-dashboards) for ease of use and to more readily identify organizational-defined indicators of compromise.

## Networking

**[Configure the firewall](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/firewall)** (initial setup): Customers must configure the appliance firewall during initial setup to ensure that source and destination communications are explicitly allowed where required. The default policy won't permit any external communication.

**[NTP](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/setup#external-ntp)** : (initial setup) Customers must configure appliances to use an approved DoD time source. Internally, the appliance switch is the time reference. The switch must reference a time source on the customer's network.

**[Manage internal network compliance](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/rotate-cert)** : Rotate certificates and credentials every 90 days.

**[Configure network policies for VM workloads](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/connect-to-vm/network-policy)** : Google provides a default network policy that is deny-by-default within projects and VM workloads. Customers are responsible for configuring network policies to exercise least privilege in their environment.

**Session Termination** : The appliance [terminates sessions automatically](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/iam/sign-in#session-inactivity-logout) after 15 minutes.

## Vulnerability management (patching and scanning)

**[Update and patch the appliance](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/update-patch)** : Update on a monthly basis or as-needed for Google-issued advisories. Customers must provide Google with a security point of contact for these advisories as a part of Task Order onboarding.

**[Scanning](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/nessus-scans)** : Google scans a reference device in order to detect vulnerabilities and provide customers patches on a monthly basis. Customers are responsible for scanning their appliances in their environments to ensure patches succeed and for situational awareness of vulnerabilities in their environment.

## Media protection

**Media Marking** : Customers are responsible for labeling the appliance and output devices at the appropriate classification level. Google ships unclassified units with unclassified drives and blank Yubikeys. Customers must apply labels to indicate if a unit is intended for use with Controlled Unclassified Information, Secret Information, or other caveats.

**Media Handling** : Customers are responsible for maintaining custody of all protected information to include media access, use, storage, transport, and downgrading. Customers have sole control over physical access to appliances and media. When Yubikeys are used, customers should treat the keys at the same level of classification as the appliance. While in transit, the Yubikeys must be removed from the appliance and stored or shipped separately.

**Media Sanitization** : Customers are responsible for media sanitization, to include removal and sanitization or destruction of drives as necessary. Customers must remove drives and Yubikeys prior to shipping appliance units back to Google for maintenance. If drives are removed, the same media handling expectations previously outlined apply until the drives are sanitized or destroyed.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
