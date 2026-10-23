---
url: https://docs.cloud.google.com/gemini/enterprise/docs/security-overview/
title: Gemini Enterprise security overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:55:39.687018+00:00
---

# Gemini Enterprise security overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/security-overview/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Gemini Enterprise security overview Stay organized with collections  Save and categorize content based on your preferences. 

Google helps organizations secure their cloud environment, protect their data, and comply with industry regulations. For general information about security across all of Google Cloud, see [Google Cloud security overview](https://docs.cloud.google.com/docs/security/overview/whitepaper).

## End user security configurations

Managing your Identity and Access Management (IAM) settings within Gemini Enterprise is crucial for security. The resources listed in this section help you understand the permissions and access controls in Gemini Enterprise:

  * [Identity and permissions](https://docs.cloud.google.com/gemini/enterprise/docs/identity)
  * [Set up external identities](https://docs.cloud.google.com/gemini/enterprise/docs/identity-mapping)
  * [Authenticate to Gemini Enterprise API](https://docs.cloud.google.com/gemini/enterprise/docs/authentication)
  * [Access control with IAM](https://docs.cloud.google.com/gemini/enterprise/docs/access-control)



The following authentication frameworks are supported:

  * [Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation)

**Note:** When you send data to Gemini Enterprise using a third-party connector, we recommend using Workforce Identity Federation (WIF).
  * [Google Identity](https://developers.google.com/identity)

  * [Workload Identity Federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation)




## Gemini Enterprise data security

Protecting your data from threats, breaches, and identity theft is important. Gemini Enterprise has the following security measures in place:

  * Gemini Enterprise is integrated with [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products).
  * Default data encryption with [Customer Managed Encryption Keys (CMEK)](https://docs.cloud.google.com/gemini/enterprise/docs/cmek).

Gemini Enterprise also supports External key manager (EKM) or hardware security module (HSM). For information about the limitations that apply to CMEK and EKM, see [Limitations of Cloud Key Management Service in Gemini Enterprise](https://docs.cloud.google.com/gemini/enterprise/docs/cmek#limitations).




## Gemini Enterprise compliance

Data compliance involves meeting legal and regulatory requirements for handling personal and sensitive information. It governs data collection, storage, usage, and security to ensure privacy and protection.

The resources listed in this section provide information to help you maintain data transparency and compliance:

  * [Enable access transparency](https://docs.cloud.google.com/gemini/enterprise/docs/access-transparency)
  * [Audit logging](https://docs.cloud.google.com/gemini/enterprise/docs/audit-logging)
  * [Gemini Enterprise locations](https://docs.cloud.google.com/gemini/enterprise/docs/locations)
  * [Compliance certifications and security controls](https://docs.cloud.google.com/gemini/enterprise/docs/compliance-security-controls)
  * Gemini Enterprise deletes user-requested data within 60 days. For more information, see [Data deletion on Google Cloud](https://docs.cloud.google.com/docs/security/deletion).



## Workforce Identity Federation and pool administrators

If you use Workforce Identity Federation to authenticate your users, you grant the IAM Workforce Identity Pool Admin (`roles/iam.workforcePoolAdmin`) and IAM Workforce Pool Editor (`roles/iam.workforcePoolEditor`) IAM roles to some of your administrators. These roles can modify workforce pool attribute mappings. Incorrect changes, whether intentional or accidental, risk enabling user impersonation, which can lead to unauthorized document access and actions.

For this reason, we recommend the following:

  * Only grant these workforce pool roles to trusted administrators who absolutely require them.

  * Use [Privileged Access Manager](https://docs.cloud.google.com/iam/docs/pam-permissions-and-setup) to set up entitlements for these roles and to audit their use.

  * Integrate Workforce Identity Federation audit logs into your security monitoring solution (for example, SIEM) to quickly detect and alert on any changes to attribute mappings or unauthorized access attempts.




## Required Google Cloud APIs

To begin using Gemini Enterprise, the following APIs must be enabled:

  * Gemini Enterprise Agent Platform API
  * Discovery Engine API
  * Cloud Storage API
  * Identity and Access Management (IAM) API



For more information on getting started with Gemini Enterprise, see the [Before you begin](https://docs.cloud.google.com/gemini/enterprise/docs/quickstart-gemini-enterprise#before-you-begin) section.

To disable the Gemini Enterprise (Discovery Engine) API, see [Turn off Gemini Enterprise](https://docs.cloud.google.com/gemini/enterprise/docs/turn-off-gemini-enterprise).

## Third-party connectors and public endpoints

Third-party connectors interact with public endpoints outside Google's network; for example, endpoints for a third-party's API for polling data or a webhook URL for real-time synchronization. Because VPC Service Controls are designed to govern Google Cloud services, they don't inherently block or secure traffic to these external, non-Google endpoints.

To mitigate, Gemini Enterprise makes sure that your egress traffic is secured by granular VPC Firewall rules, which restrict outbound connections to only the Fully Qualified Domain Names (FQDNs) of the external service you provide.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
