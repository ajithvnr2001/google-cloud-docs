---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/certificate/
title: Third-party service certificates in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:04:00.127127+00:00
---

# Third-party service certificates in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/certificate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Third-party service certificates in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

This page explains how to add and manage third-party certificates used by Backup and DR.

Backup and DR can connect to the external endpoint of a third-party service only if the endpoint has a valid certificate issued by a public Public Certificate Authority (CA) associated to it. If the endpoint doesn't have a certificate, you need to add one to it.

A certificate is validated either through certificate revocation lists (CRL) or Online Certificate Status Protocol (OCSP). If the CRL or OCSP endpoints are not reachable, the certificate is treated as valid and an event is generated. You can track these events on the **Monitor** > **Events** page.

## Before you begin

Allow egress connection from the backup/recovery appliance to the OCSP or CRL endpoints of the certificate using [Cloud NAT](https://docs.cloud.google.com/nat/docs/set-up-manage-network-address-translation). By default, Cloud NAT has access to all the primary and secondary IP ranges of all subnets in the region of a Virtual Private Cloud (VPC) network. To limit Cloud NAT access to only the subnet where the appliance is deployed, see [Specify subnet ranges for NAT](https://docs.cloud.google.com/nat/docs/set-up-manage-network-address-translation#specify_subnet_ranges_for_nat).

## IAM roles and permissions

The following permissions are required for third-party certificate operations:

  * `backupdr.managementServers.manageSystem` and `backupdr.managementServers.viewSystem` for adding or deleting certificates
  * `backupdr.managementServers.viewSystem` for viewing certificates



## Add a certificate

You can add a private CA issued or self-signed certificate to a third-party service endpoint using the **Manage** > **Certificates** page. For example, if a vCenter is using a private CA or self-signed certificate, you need to add the certificate to the appliance management console.

Use the following instructions to add a third-party certificate:

  1. In the appliance management console, click **Manage** > **Certificates**.
  2. Click **Add Certificate**.
  3. You can add the certificate in either ways:

     * Copy the certificate and paste it in the **Certificate** box.
     * Click **Choose File** and upload the certificate.
  4. Click **Upload**.




## Delete a certificate

Use the following instructions to delete a certificate:

  1. Click **Manage** > **Certificates**.
  2. Right-click the certificate that you want to remove and select **Delete**.
  3. Click **Delete** in the confirmation dialog.



## What's next

  * [Add vCenter and ESX server hosts](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/add-vcenter-host)
  * [Discover and protect VMware VMs](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/discover-and-protect-vms)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
