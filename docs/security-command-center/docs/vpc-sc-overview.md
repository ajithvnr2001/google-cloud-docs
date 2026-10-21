---
url: https://docs.cloud.google.com/security-command-center/docs/vpc-sc-overview/
title: Overview of VPC Service Controls and Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:48:50.064179+00:00
---

# Overview of VPC Service Controls and Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/vpc-sc-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Overview of VPC Service Controls and Security Command Center Stay organized with collections  Save and categorize content based on your preferences. 

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

[VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) improves your security posture by providing service-level perimeters around Google Cloud resources to prevent data exfiltration.

When your organization protects resources inside a service perimeter, Security Command Center services need appropriate [ingress or egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/configuring-ingress-egress-policies) to scan resources, monitor log streams, and export findings across perimeter boundaries.

If your VPC Service Controls perimeters restrict access of the [Security Center Service Agent](https://docs.cloud.google.com/security-command-center/docs/access-control-org#service-agent) some parts of Security Command Center might not work properly, including threat detection services such as Event Threat Detection and continuous finding exports. To help prevent configuration errors and missing detections, ensure that ingress and egress policies grant the Security Center Service Agent access to required APIs.

If Security Health Analytics detects that perimeter restrictions block scanning or services, it generates a [`VPC Service Controls Restriction` (`VPC_SC_RESTRICTION`)](https://docs.cloud.google.com/security-command-center/docs/how-to-remediate-scc-errors#vpc_service_controls_restriction) error finding.

## Supported services and configuration guides

The following table lists Security Command Center services and capabilities that support VPC Service Controls service perimeters and links to guides that explain how to configure perimeter access.

Service or feature | Configuration guide  
---|---  
**Security Health Analytics** |  [Scanning projects protected by a service perimeter](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-health-analytics#service-perimeter)  
**Event Threat Detection** |  [Allow Event Threat Detection to access VPC Service Controls perimeters](https://docs.cloud.google.com/security-command-center/docs/etd-allow-access-vpcsc)  
**Virtual Machine Threat Detection** |  [Allow VM Threat Detection to access VPC Service Controls perimeters](https://docs.cloud.google.com/security-command-center/docs/vmtd-allow-access-vpcsc)  
**Container Threat Detection** |  [Scan projects protected by a service perimeter](https://docs.cloud.google.com/security-command-center/docs/how-to-use-container-threat-detection#service-perimeter)  
**Mandiant Attack Surface Management** |  [Use Mandiant Attack Surface Management with VPC Service Controls](https://docs.cloud.google.com/security-command-center/docs/asm-allow-access-vpcsc)  
**Vulnerability Assessment for Google Cloud** |  [Allow Vulnerability Assessment for Google Cloud to access VPC Service Controls perimeters](https://docs.cloud.google.com/security-command-center/docs/vulnerability-assessment-google-cloud-vpcsc)  
**Compliance Manager** |  [Use Compliance Manager with VPC Service Controls](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-configure-vpc-sc)  
**Assured Open Source Software** |  [Configure Assured Open Source Software (Assured OSS) support for VPC Service Controls](https://docs.cloud.google.com/security-command-center/docs/aoss-configure-support-for-vpc-sc)  
**Finding notifications to Pub/Sub** |  [Grant perimeter access for finding notifications](https://docs.cloud.google.com/security-command-center/docs/how-to-notifications#grant-perimeter-access)  
**Continuous exports to BigQuery** |  [Grant perimeter access for BigQuery exports](https://docs.cloud.google.com/security-command-center/docs/how-to-analyze-findings-in-big-query#grant-perimeter-access)  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
