---
url: https://docs.cloud.google.com/security-command-center/docs/respond-compute-engine-threats/
title: Respond to Compute Engine threat findings \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:44:47.113169+00:00
---

# Respond to Compute Engine threat findings  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/respond-compute-engine-threats/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Respond to Compute Engine threat findings Stay organized with collections  Save and categorize content based on your preferences. 

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This document offers informal guidance on how you can respond to findings of suspicious activities in your Compute Engine resources. The recommended steps might not be appropriate for all findings and might impact your operations. Before you take any action, you should investigate the findings; assess the information that you gather; and decide how to respond.

**Note:** The techniques that Security Command Center provides aren't guaranteed to be effective against any previous, current, or future threats that you face. For information about why Security Command Center does not provide official remediation guidance for threats, see [Approach to threat finding remediation](https://docs.cloud.google.com/security-command-center/docs/how-to-investigate-threats#remediating_threats).

## Before you begin

  1. [Review the finding](https://docs.cloud.google.com/security-command-center/docs/how-to-investigate-threats#reviewing_findings). Note the affected Compute Engine instance and the detected principal email and caller IP address (if present). Also review the finding for indicators of compromise (IP, domain, file hash, or signature).
  2. To learn more about the finding that you're investigating, search for the finding in the [Threat findings index](https://docs.cloud.google.com/security-command-center/docs/threat-findings-index).



## General recommendations

  * Contact the owner of the affected resource.
  * Investigate the potentially compromised instance and remove any discovered malware.
  * If necessary, [stop the compromised instance](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance) and replace it with a new instance.
  * For forensic analysis, consider backing up the affected virtual machines and persistent disks. For more information, see [Data protection options](https://docs.cloud.google.com/compute/docs/disks/data-protection) in the Compute Engine documentation.
  * If necessary, delete the VM instance.
  * If the finding includes a principal email and caller IP, review other audit logs associated with that principal or IP address for anomalous activity. If necessary, disable or reduce the privileges of the associated account if it has been compromised.
  * For further investigation, consider using incident response services like [Mandiant](https://docs.cloud.google.com/security/consulting/mandiant-incident-response-services).



In addition, consider the recommendations in the subsequent sections on this page.

## SSH threats

  * Consider disabling SSH access to the VM. For information about disabling SSH keys, see [Restrict SSH keys from VMs](https://docs.cloud.google.com/compute/docs/connect/restrict-ssh-keys). This action can interrupt authorized access to the VM, so consider the needs of your organization before you proceed.
  * Only use SSH authentication with [authorized keys](https://docs.cloud.google.com/compute/docs/instances/ssh).
  * Block malicious IP addresses by [updating firewall rules](https://docs.cloud.google.com/vpc/docs/using-firewalls) or by using [Cloud Armor](https://docs.cloud.google.com/armor/docs/cloud-armor-overview). Consider [enabling Cloud Armor as an integrated service](https://docs.cloud.google.com/security-command-center/docs/how-to-configure-security-command-center#gcp-configure-other-services). Depending on data volume, Cloud Armor costs can be significant. For more information, see [Cloud Armor pricing](https://cloud.google.com/armor/pricing).



## Lateral movements in Compute Engine instances

  * Consider using [Secure Boot](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#secure-boot) for your Compute Engine VM instances.

  * Consider [deleting the potentially compromised service account](https://docs.cloud.google.com/iam/docs/service-accounts-delete-undelete#deleting) and rotate and delete all service account access keys for the potentially compromised project. After deletion, applications that use the service account for authentication lose access. Before proceeding, your security team should identify all impacted applications and work with application owners to ensure business continuity.

  * Work with your security team to identify unfamiliar resources, including Compute Engine instances, snapshots, service accounts, and IAM users. Delete resources not created with authorized accounts.

  * Respond to any notifications from Cloud Customer Care.




## What's next

  * Learn [how to work with threat findings in Security Command Center](https://docs.cloud.google.com/security-command-center/docs/how-to-investigate-threats).
  * Refer to the [Threat findings index](https://docs.cloud.google.com/security-command-center/docs/threat-findings-index).
  * Learn how to [review a finding](https://docs.cloud.google.com/security-command-center/docs/how-to-investigate-threats#reviewing_findings) through the Google Cloud console.
  * Learn about the [services that generate threat findings](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#threats).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
