---
url: https://docs.cloud.google.com/security-command-center/docs/ciem-overview/
title: Overview of Cloud Infrastructure Entitlement Management \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:39:34.676638+00:00
---

# Overview of Cloud Infrastructure Entitlement Management  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/ciem-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Overview of Cloud Infrastructure Entitlement Management Stay organized with collections  Save and categorize content based on your preferences. 

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

With Security Command Center's Cloud Infrastructure Entitlement Management (CIEM) capabilities, you can manage which identities have access to which resources in your deployments on multiple cloud platforms and mitigate potential vulnerabilities that result from misconfigurations.

Security Command Center's CIEM capabilities provide a comprehensive view of the security of your identity and access configuration. Specifically, the following CIEM features help you identify misconfigurations and enforce the principle of least privilege:

  * Detection of potential identity and access misconfigurations in your deployments on multiple cloud platforms, including Google Cloud, Amazon Web Services (AWS), and Microsoft Azure ([Preview](https://cloud.google.com/products#product-launch-stages)).
  * Identification of vulnerability findings that provide insight into the roles that are granted to principals in your Google Cloud, AWS, and Microsoft Azure ([Preview](https://cloud.google.com/products#product-launch-stages)) environments. This includes federated identities from other identity providers—like Entra ID (Azure AD), Okta, and on-premises Active Directory—for Google Cloud and AWS IAM Identity Center.
  * Guidance on how to remediate misconfigurations, such as removing permissions from a principal with excess permissions.
  * Case management to efficiently track misconfiguration remediation efforts using cases in Security Command Center Enterprise or other ticket management systems.



## Manage identity and access security issues with CIEM

The following sections describe the CIEM capabilities that help you manage identity and access misconfigurations.

### Quick access to identity and access findings

Security issues often arise due to undetected identity and access misconfigurations such as highly privileged principals, dormant identities, unrotated service account keys, and a lack of multifactor authentication.

CIEM generates findings that help alert you to potential identity and access security issues across your cloud environments. Many different Security Command Center services (such as IAM recommender, Security Health Analytics, and CIEM) produce the identity and access findings that are considered part of Security Command Center's CIEM capabilities. For example, the CIEM detection service itself produces a subset of identity and access findings for AWS and Microsoft Azure ([Preview](https://cloud.google.com/products#product-launch-stages)) that alert you to highly privileged roles, groups, and users.

On the Standard and Standard-legacy tiers, CIEM provides recommendations for Google Cloud [basic roles](https://docs.cloud.google.com/iam/docs/roles-overview#basic) only. For details, see the [IAM recommender features](https://docs.cloud.google.com/policy-intelligence/docs/billing-questions#pricing).

To learn how to investigate identity and access findings to understand your identity and access security, see [Investigate identity and access findings](https://docs.cloud.google.com/security-command-center/docs/ciem-identity-access-findings).

### Discovery of federated identities' permissions

CIEM helps provide a more granular view of the security of your identity and access configurations by providing insight into the permissions of federated identities from other identity providers, such as Entra ID (Azure AD), Okta, and on-premises Active Directory. CIEM helps identity federated identities with roles that have excess permissions on your Google Cloud resources. Cloud Infrastructure Entitlement Management can also be used with AWS IAM Identity Center to expose vulnerabilities in federated identities on AWS resources.

You can view offending access grants and recommended remediations directly from the Security Command Center **Findings** page. For more information on offending access grants in findings, see [Offending access grants](https://docs.cloud.google.com/security-command-center/docs/ciem-identity-access-findings#offending-access).

Google Cloud IAM lets you investigate the permissions of principals from other identity providers on the [IAM page](https://console.cloud.google.com/iam-admin) in the Google Cloud console.

### Remediation and tracking using cases

Enterprise (Deprecated) [service tier](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

Security teams working with multicloud infrastructure often struggle to remediate identity and access misconfigurations at scale. Security Command Center provides you with remediation guidance through case management, response playbooks, and security operations capabilities.

To learn more about reviewing findings cases, see [Review cases for identity and access issues](https://docs.cloud.google.com/security-command-center/docs/ciem-identity-access-cases).

## What's next

  * Learn how to [enable the CIEM detection service](https://docs.cloud.google.com/security-command-center/docs/ciem-enable-service).
  * Learn how to [investigate identity and access findings](https://docs.cloud.google.com/security-command-center/docs/ciem-identity-access-findings).
  * Learn how to [review cases for identity and access issues](https://docs.cloud.google.com/security-command-center/docs/ciem-identity-access-cases).
  * Learn more about the [IAM recommender functionality](https://docs.cloud.google.com/policy-intelligence/docs/role-recommendations-overview) that powers CIEM.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
