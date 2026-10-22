---
url: https://docs.cloud.google.com/architecture/framework/security/meet-regulatory-compliance-and-privacy-needs/
title: Meet regulatory, compliance, and privacy needs \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:09:11.580600+00:00
---

# Meet regulatory, compliance, and privacy needs  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/framework/security/meet-regulatory-compliance-and-privacy-needs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Meet regulatory, compliance, and privacy needs Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2025-02-05 UTC

This principle in the security pillar of the [Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework) helps you identify and meet regulatory, compliance, and privacy requirements for cloud deployments. These requirements influence many of the decisions that you need to make about the security controls that must be used for your workloads in Google Cloud.

## Principle overview

Meeting regulatory, compliance, and privacy needs is an unavoidable challenge for all businesses. Cloud regulatory requirements depend on several factors, including the following:

  * The laws and regulations that apply to your organization's physical locations
  * The laws and regulations that apply to your customers' physical locations
  * Your industry's regulatory requirements



Privacy regulations define how you can obtain, process, store, and manage your users' data. You own your own data, including the data that you receive from your users. Therefore, many privacy controls are your responsibility, including controls for cookies, session management, and obtaining user permission.

The recommendations to implement this principle are grouped within the following sections:

  * Recommendations to address organizational risks
  * Recommendations to address regulatory and compliance obligations
  * Recommendations to manage your data sovereignty
  * Recommendations to address privacy requirements



## Recommendations to address organizational risks

This section provides recommendations to help you identify and address risks to your organization.

### Identify risks to your organization

This recommendation is relevant to the following [focus area](https://docs.cloud.google.com/architecture/framework/security#focus_areas_of_cloud_security): Cloud governance, risk, and compliance.

Before you create and deploy resources on Google Cloud, complete a risk assessment. This assessment should determine the security features that you need to meet your internal security requirements and external regulatory requirements.

Your risk assessment provides you with a catalog of organization-specific risks, and informs you about your organization's capability to detect and counteract security threats. You must perform a risk analysis immediately after deployment and whenever there are changes in your business needs, regulatory requirements, or threats to your organization.

As mentioned in the [Implement security by design](https://docs.cloud.google.com/architecture/framework/security/implement-security-by-design) principle, your security risks in a cloud environment differ from on-premises risks. This difference is due to the shared responsibility model in the cloud, which varies by service (IaaS, PaaS, or SaaS) and your usage. Use a cloud-specific risk assessment framework like the [Cloud Controls Matrix (CCM)](https://cloudsecurityalliance.org/research/cloud-controls-matrix/). Use threat modeling, like [OWASP application threat modeling](https://owasp.org/www-project-threat-modeling/), to identify and address vulnerabilities. For expert help with risk assessments, contact your Google account representative or consult Google Cloud's [partner directory](https://cloud.google.com/find-a-partner).

After you catalog your risks, you must determine how to address them—that is, whether you want to accept, avoid, transfer, or mitigate the risks. For mitigation controls that you can implement, see the next section about mitigating your risks.

### Mitigate your risks

This recommendation is relevant to the following [focus area](https://docs.cloud.google.com/architecture/framework/security#focus_areas_of_cloud_security): Cloud governance, risk, and compliance.

When you adopt new public cloud services, you can mitigate risks by using technical controls, contractual protections, and third-party verifications or attestations.

_Technical controls_ are features and technologies that you use to protect your environment. These include built-in cloud security controls like firewalls and logging. Technical controls can also include using third-party tools to reinforce or support your security strategy. There are two categories of technical controls:

  * You can implement Google Cloud's security controls to help you mitigate the risks that apply to your environment. For example, you can secure the connection between your on-premises networks and your cloud networks by using [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview) and [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview).
  * Google has robust internal controls and auditing to protect against insider access to customer data. Our audit logs provide you with near real-time logs of [Google administrator access](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/overview) on Google Cloud.



_Contractual protections_ refer to the legal commitments made by us regarding Google Cloud services. Google is committed to maintaining and expanding our compliance portfolio. The [Cloud Data Processing Addendum (CDPA)](https://cloud.google.com/terms/data-processing-addendum) describes our commitments with regard to the processing and security of your data. The CDPA also outlines the access controls that limit Google support engineers' access to customers' environments, and it describes our rigorous logging and approval process. We recommend that you review Google Cloud's contractual controls with your legal and regulatory experts, and verify that they meet your requirements. If you need more information, [contact your technical account representative](https://cloud.google.com/contact).

_Third-party verifications or attestations_ refer to having a third-party vendor audit the cloud provider to ensure that the provider meets compliance requirements. For example, to learn about Google Cloud attestations with regard to the ISO/IEC 27017 guidelines, see [ISO/IEC 27017 - Compliance](https://cloud.google.com/security/compliance/iso-27017). To view the current Google Cloud certifications and letters of attestation, see [Compliance resource center](https://cloud.google.com/security/compliance/).

## Recommendations to address regulatory and compliance obligations

A typical compliance journey has three stages: assessment, gap remediation, and continual monitoring. This section provides recommendations that you can use during each of these stages.

### Assess your compliance needs

This recommendation is relevant to the following [focus area](https://docs.cloud.google.com/architecture/framework/security#focus_areas_of_cloud_security): Cloud governance, risk, and compliance.

Compliance assessment starts with a thorough review of all of your regulatory obligations and how your business is implementing them. To help you with your assessment of Google Cloud services, use the [Compliance resource center](https://cloud.google.com/security/compliance). This site provides information about the following:

  * Service support for various regulations
  * Google Cloud certifications and attestations



To better understand the compliance lifecycle at Google and how your requirements can be met, you can [contact sales](https://cloud.google.com/support-hub) to request help from a Google compliance specialist. Or, you can contact your Google Cloud account manager to request a compliance workshop.

For more information about tools and resources that you can use to manage security and compliance for Google Cloud workloads, see [Assuring Compliance in the Cloud](https://services.google.com/fh/files/misc/assuringcompliance_in_the_cloud.pdf).

### Automate implementation of compliance requirements

This recommendation is relevant to the following [focus area](https://docs.cloud.google.com/architecture/framework/security#focus_areas_of_cloud_security): Cloud governance, risk, and compliance.

To help you stay in compliance with changing regulations, determine whether you can automate how you implement compliance requirements. You can use both compliance-focused capabilities that Google Cloud provides and blueprints that use recommended configurations for a particular compliance regime.

[Assured Workloads](https://docs.cloud.google.com/assured-workloads) builds on the controls within Google Cloud to help you meet your compliance obligations. Assured Workloads lets you do the following:

  * Select your compliance regime. Then, the tool automatically sets the baseline personnel access controls for the selected regime.
  * Set the location for your data by using organization policies so that your data at rest and your resources remain only in that [region](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones).
  * Select the key-management option (such as the key rotation period) that best meets your security and compliance requirements.
  * Select the access criteria for Google support personnel to meet certain regulatory requirements such as FedRAMP Moderate. For example, you can select whether Google support personnel have completed the appropriate background checks.
  * Use Google-owned and Google-managed encryption keys that are FIPS-140-2 compliant and support FedRAMP Moderate compliance. For an added layer of control and for the separation of duties, you can use customer-managed encryption keys (CMEK). For more information about keys, see [Encrypt data at rest and in transit](https://docs.cloud.google.com/architecture/framework/security/implement-security-by-design#encrypt_data_at_rest_and_in_transit).



In addition to Assured Workloads, you can use Google Cloud blueprints that are relevant to your compliance regime. You can modify these blueprints to incorporate your security policies into your infrastructure deployments.

To help you build an environment that supports your compliance requirements, Google's blueprints and solution guides include recommended configurations and provide Terraform modules. The following table lists blueprints that address security and alignment with compliance requirements.

Requirement | Blueprints and solution guides  
---|---  
FedRAMP | 

  * [Google Cloud FedRAMP implementation guide](https://docs.cloud.google.com/docs/security/compliance/fedramp-implementation-guide)
  * [Setting up a FedRAMP Aligned Three-Tier Workload on Google Cloud](https://services.google.com/fh/files/misc/fedramp_aligned_workload_solution_guide.pdf)

  
HIPAA | 

  * [Protecting healthcare data on Google Cloud](https://services.google.com/fh/files/misc/protecting_healthcare_data_on_google_cloud_wp.pdf)
  * [Setting up a HIPAA-aligned workload using Data Protection Toolkit](https://services.google.com/fh/files/misc/hipaa_technical_solution_guide.pdf)

  
  
### Monitor your compliance

This recommendation is relevant to the following [focus areas](https://docs.cloud.google.com/architecture/framework/security#focus_areas_of_cloud_security):

  * Cloud governance, risk, and compliance
  * Logging, monitoring, and auditing



Most regulations require that you monitor particular activities, which include access-related activities. To help with your monitoring, you can use the following:

  * [Access Transparency](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/overview): View near real-time logs when Google Cloud administrators access your content.
  * [Firewall Rules Logging](https://docs.cloud.google.com/vpc/docs/firewall-rules-logging): Record TCP and UDP connections inside a VPC network for any rules that you create. These logs can be useful for auditing network access or for providing early warning that the network is being used in an unapproved manner.
  * [VPC Flow Logs](https://docs.cloud.google.com/vpc/docs/using-flow-logs): Record network traffic flows that are sent or received by VM instances.
  * [Security Command Center Premium](https://docs.cloud.google.com/security-command-center/docs/compliance-management): Monitor for compliance with various standards.
  * [OSSEC](https://ossec.github.io/index.html) (or another open source tool): Log the activity of individuals who have administrator access to your environment.
  * [Key Access Justifications](https://docs.cloud.google.com/assured-workloads/key-access-justifications/docs/overview): View the reasons for a key-access request.
  * [Security Command Center notifications](https://docs.cloud.google.com/security-command-center/docs/how-to-notifications): Get alerts when noncompliance issues occur. For example, get alerts when users disable two-step verification or when service accounts are over-privileged. You can also set up automatic remediation for specific notifications.



## Recommendations to manage your data sovereignty

This recommendation is relevant to the following [focus area](https://docs.cloud.google.com/architecture/framework/security#focus_areas_of_cloud_security): Cloud governance, risk, and compliance.

Data sovereignty provides you with a mechanism to prevent Google from accessing your data. You approve access only for provider behaviors that you agree are necessary. For example, you can manage your data sovereignty in the following ways:

  * Store and manage [encryption keys](https://docs.cloud.google.com/kms/docs/ekm) outside the cloud.
  * Grant access to these keys based on detailed [access justifications](https://docs.cloud.google.com/assured-workloads/key-access-justifications/docs/overview).
  * [Protect data in use](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/confidential-vm-overview) by using Confidential Computing.



### Manage your operational sovereignty

This recommendation is relevant to the following [focus area](https://docs.cloud.google.com/architecture/framework/security#focus_areas_of_cloud_security): Cloud governance, risk, and compliance.

Operational sovereignty provides you with assurances that Google personnel can't compromise your workloads. For example, you can manage operational sovereignty in the following ways:

  * [Restrict the deployment](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations) of new resources to specific provider regions.
  * [Limit Google personnel access](https://docs.cloud.google.com/assured-workloads/docs/personnel-access-data-controls) based on predefined attributes such as their citizenship or geographic location.



### Manage software sovereignty

This recommendation is relevant to the following [focus area](https://docs.cloud.google.com/architecture/framework/security#focus_areas_of_cloud_security): Cloud governance, risk, and compliance.

Software sovereignty provides you with assurances that you can control the availability of your workloads and run them wherever you want. Also, you can have this control without being dependent or locked in with a single cloud provider. Software sovereignty includes the ability to survive events that require you to quickly change where your workloads are deployed and what level of outside connection is allowed.

For example, to help you manage your software sovereignty, Google Cloud supports [hybrid and multicloud deployments](https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns-and-practices). If you choose on-premises deployments for data sovereignty reasons, [Google Distributed Cloud](https://docs.cloud.google.com/distributed-cloud) is a combination of hardware and software that brings Google Cloud into your data center.

## Recommendations to address privacy requirements

Google Cloud includes the following controls that promote privacy:

  * Default encryption of all data when it's at rest, when it's in transit, and while it's being processed.
  * Safeguards against insider access.
  * Support for numerous privacy regulations.



The following recommendations address additional controls that you can implement. For more information, see [Privacy Resource Center](https://cloud.google.com/privacy).

### Control data residency

This recommendation is relevant to the following [focus area](https://docs.cloud.google.com/architecture/framework/security#focus_areas_of_cloud_security): Cloud governance, risk, and compliance.

Data residency describes where your data is stored at rest. Data residency requirements vary based on system design objectives, industry regulatory concerns, national law, tax implications, and even culture.

Controlling data residency starts with the following:

  * Understand your data type and its location.
  * Determine what risks exist for your data and which laws and regulations apply.
  * Control where your data is stored or where it goes.



To help you comply with data residency requirements, Google Cloud lets you control where your data is stored, how it's accessed, and how it's processed. You can use [resource location policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations) to restrict where resources are created and to limit where data is replicated between regions. You can use the location property of a resource to identify where the service is deployed and who maintains it. For more information, see [Resource locations supported services](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations-supported-services).

### Classify your confidential data

This recommendation is relevant to the following [focus area](https://docs.cloud.google.com/architecture/framework/security#focus_areas_of_cloud_security): Data security.

You must define what data is confidential, and then ensure that the confidential data is properly protected. Confidential data can include credit card numbers, addresses, phone numbers, and other personally identifiable information (PII). Using [Sensitive Data Protection](https://docs.cloud.google.com/sensitive-data-protection), you can set up appropriate classifications. You can then tag and tokenize your data before you store it in Google Cloud. Additionally, Knowledge Catalog offers a [catalog](https://docs.cloud.google.com/dataplex/docs/catalog-overview) service that provides a platform for storing, managing, and accessing your metadata. For more information and an example of data classification and de-identification, see [De-identification and re-identification of PII using Sensitive Data Protection](https://docs.cloud.google.com/architecture/de-identification-re-identification-pii-using-cloud-dlp).

### Lock down access to sensitive data

This recommendation is relevant to the following [focus areas](https://docs.cloud.google.com/architecture/framework/security#focus_areas_of_cloud_security):

  * Data security
  * Identity and access management



Place sensitive data in its own service perimeter by using [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview). VPC Service Controls improves your ability to mitigate the risk of unauthorized copying or transferring of data (data exfiltration) from Google-managed services. With VPC Service Controls, you configure security perimeters around the resources of your Google-managed services to control the movement of data across the perimeter. Set [Google Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs) access controls for that data. Configure [multifactor authentication (MFA)](https://support.google.com/cloudidentity/answer/175197) for all users who require access to sensitive data.

[ Previous arrow_back  Use AI for security  ](https://docs.cloud.google.com/architecture/framework/security/use-ai-for-security)

[ Next Shared responsibility and shared fate  arrow_forward  ](https://docs.cloud.google.com/architecture/framework/security/shared-responsibility-shared-fate)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-02-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-02-05 UTC."],[],[]] 
