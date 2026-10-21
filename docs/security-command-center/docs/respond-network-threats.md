---
url: https://docs.cloud.google.com/security-command-center/docs/respond-network-threats/
title: Respond to network threat findings \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:48:38.499816+00:00
---

# Respond to network threat findings  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/respond-network-threats/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Respond to network threat findings Stay organized with collections  Save and categorize content based on your preferences. 

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This document offers informal guidance on how you can respond to findings of suspicious activities in your network. The recommended steps might not be appropriate for all findings and might impact your operations. Before you take any action, you should investigate the findings; assess the information that you gather; and decide how to respond.

**Note:** The techniques that Security Command Center provides aren't guaranteed to be effective against any previous, current, or future threats that you face. For information about why Security Command Center does not provide official remediation guidance for threats, see [Approach to threat finding remediation](https://docs.cloud.google.com/security-command-center/docs/how-to-investigate-threats#remediating_threats).

## Before you begin

  1. [Review the finding](https://docs.cloud.google.com/security-command-center/docs/how-to-investigate-threats#reviewing_findings). Note the affected resource and the detected network connections. If present, review the indicators of compromise in the finding with threat intelligence from VirusTotal.

  2. To learn more about the finding that you're investigating, search for the finding in the [Threat findings index](https://docs.cloud.google.com/security-command-center/docs/threat-findings-index).




## General recommendations

  * Contact the owner of the affected resource.
  * Investigate the potentially compromised compute resource and remove any discovered malware.
  * If necessary, stop the compromised compute resource.
  * For forensic analysis, consider backing up the affected virtual machines and persistent disks. For more information, see [Data protection options](https://docs.cloud.google.com/compute/docs/disks/data-protection) in the Compute Engine documentation.
  * If necessary, delete the affected compute resource.
  * For further investigation, consider using incident response services like [Mandiant](https://docs.cloud.google.com/security/consulting/mandiant-incident-response-services).



In addition, consider the recommendations in the subsequent sections on this page.

## Malware

  * To track activity and vulnerabilities that allowed the insertion of malware, check audit logs and syslogs associated with the compromised compute resource.
  * Block malicious IP addresses by [updating firewall rules](https://docs.cloud.google.com/vpc/docs/using-firewalls) or by using [Cloud Armor](https://docs.cloud.google.com/armor/docs/cloud-armor-overview). Consider [enabling Cloud Armor as an integrated service](https://docs.cloud.google.com/security-command-center/docs/how-to-configure-security-command-center#gcp-configure-other-services). Depending on data volume, Cloud Armor costs can be significant. For more information, see [Cloud Armor pricing](https://cloud.google.com/armor/pricing).
  * To control access and use of images, use [Shielded VM](https://docs.cloud.google.com/security/shielded-cloud/shielded-vm) and set up [trusted image policies](https://docs.cloud.google.com/compute/docs/images/restricting-image-access).



## Cryptocurrency mining threats

If you determine that the application is a miner application, and its process is still running, terminate the process. Locate the application's executable binary in the compute resource's storage, and delete it.

## What's next

  * Learn [how to work with threat findings in Security Command Center](https://docs.cloud.google.com/security-command-center/docs/how-to-investigate-threats).
  * Refer to the [Threat findings index](https://docs.cloud.google.com/security-command-center/docs/threat-findings-index).
  * Learn how to [review a finding](https://docs.cloud.google.com/security-command-center/docs/how-to-investigate-threats#reviewing_findings) through the Google Cloud console.
  * Learn about the [services that generate threat findings](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#threats).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
