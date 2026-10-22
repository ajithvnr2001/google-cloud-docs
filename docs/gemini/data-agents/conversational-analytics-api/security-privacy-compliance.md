---
url: https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/security-privacy-compliance/
title: Security, privacy, risk, and compliance for the Conversational Analytics API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:50:54.058124+00:00
---

# Security, privacy, risk, and compliance for the Conversational Analytics API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/security-privacy-compliance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Data Agents ](https://docs.cloud.google.com/gemini/data-agents)
  * [ Conversational Analytics API ](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/overview)



Send feedback 

#  Security, privacy, risk, and compliance for the Conversational Analytics API Stay organized with collections  Save and categorize content based on your preferences. 

This document provides an overview of various controls that support the security of the Conversational Analytics API on Google Cloud and links to further information on how to configure the controls. Security controls such as network security options, policies, and access management can help you address your business risks and meet the privacy and regulatory requirements that apply to your business. 

The security, privacy, risk, and compliance for the Conversational Analytics API use a [shared responsibility](https://docs.cloud.google.com/architecture/framework/security/shared-responsibility-shared-fate) model. For example, because the Conversational Analytics API is a fully-managed service, Google secures and manages the infrastructure that the Conversational Analytics API and other Google Cloud services run on, and provides you with the capabilities that help you manage access to your services and resources. For more information about how we secure the infrastructure, see the [Google infrastructure security design overview](https://docs.cloud.google.com/docs/security/infrastructure/design). 

As part of the Gemini for Google Cloud family of products, the Conversational Analytics API follows Google's commitments for data privacy and usage. For more information, see [how Gemini for Google Cloud uses your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance) and [certifications and security for Gemini for Google Cloud](https://docs.cloud.google.com/gemini/docs/discover/certifications).

The Conversational Analytics API includes security controls to help mitigate risks such as prompt injection. Because large language model (LLM) security is a rapidly evolving field, these defense mechanisms are continuously updated to help safeguard data agent interactions.

As an early-stage technology, Gemini for Google Cloud products can generate output that seems plausible but is factually incorrect. We recommend that you validate all output from Gemini for Google Cloud products before you use it. For more information, see [Gemini for Google Cloud and responsible AI](https://docs.cloud.google.com/gemini/docs/discover/responsible-ai).

## Provisioned services

the Conversational Analytics API uses the following APIs:

  * [`geminidataanalytics.googleapis.com`](https://docs.cloud.google.com/gemini/data-agents/reference/rest)
  * [`cloudaicompanion.googleapis.com`](https://docs.cloud.google.com/gemini/docs/api/reference/rest)



To get started, see [Enable the Conversational Analytics API](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/enable-the-api).

## Authentication for Google Cloud management

Administrators and developers who create and manage the Conversational Analytics API instances must authenticate to Google Cloud to verify their identity and access privileges. You must set up each user with a [user account that is managed](https://docs.cloud.google.com/architecture/identity/overview-google-authentication#google_for_organizations) by Cloud Identity, Google Workspace, or an [identity provider that you've federated](https://docs.cloud.google.com/architecture/identity/best-practices-for-federating) with Cloud Identity or Google Workspace. For more information, see [Overview of Google identity management](https://docs.cloud.google.com/architecture/identity/overview-google-authentication). 

After you create the user accounts, implement security best practices such as [single sign-on](https://docs.cloud.google.com/architecture/identity/single-sign-on) and [2-step verification](https://support.google.com/a/answer/175197). 

To use the Conversational Analytics API, you must authenticate to Google Cloud. Depending on your data sources, you might also need to provide separate credentials to authorize the agent to access the underlying data. For more information, see [Authenticate and connect to a data source](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/authentication).

## Identity and Access Management

To manage Identity and Access Management (IAM) roles at scale for your administrators and developers, consider creating separate [functional groups](https://docs.cloud.google.com/architecture/identity/overview-google-authentication#group) for your various user roles and applications. Grant the IAM roles or permissions that are required to manage the Conversational Analytics API to your groups. When you assign roles to your groups, follow the principle of least privilege and other [IAM security best practices](https://docs.cloud.google.com/iam/docs/using-iam-securely). For more information, see [Best practices for using Google Groups](https://docs.cloud.google.com/iam/docs/groups-best-practices). 

For more information about setting up IAM, see [IAM overview](https://docs.cloud.google.com/iam/docs/overview). 

IAM controls access to Conversational Analytics API resources, such as agents and conversations. Access to the underlying data that an agent queries is controlled by permissions on the data source itself. For more information, see [Conversational Analytics API access control with IAM](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/access-control).

## Conversational Analytics API service accounts

When you enable the Conversational Analytics API, Google creates service accounts for you. A [service account](https://docs.cloud.google.com/iam/docs/service-account-overview) is a special type of non-interactive Google Account that's typically used by an application or compute workload, such as a Compute Engine instance, rather than a person. Applications use service accounts to access Google APIs.

### Service agents

To enable the Conversational Analytics API to access your resources on your behalf, Google Cloud creates a special service account known as a [service agent](https://docs.cloud.google.com/iam/docs/service-account-types#service-agents).

the Conversational Analytics API uses the following Conversational Analytics API service agents:

  * `service-PROJECT_NUMBER@gcp-sa-geminidataanalytics.iam.gserviceaccount.com`
  * `service-PROJECT_NUMBER@gcp-sa-cloudaicompanion.iam.gserviceaccount.com`



## Policies for the Conversational Analytics API

## Network security

By default, Google applies default protections to data in transit for all Google Cloud services, including the Conversational Analytics API instances that are running on Google Cloud. For more information about default network protections, see [Encryption in transit](https://docs.cloud.google.com/docs/security/encryption-in-transit). 

If required by your organization, you can configure additional security controls to further protect traffic on the Google Cloud network and traffic between the Google Cloud network and your corporate network. Consider the following: 

  * The Conversational Analytics API supports [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview). VPC Service Controls let you control the movement of data in Google services and set up context-based perimeter security. For more information on setting up VPC Service Controls, see [Configure perimeter security with VPC Service Controls](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/vpc-sc). 
  * In Google Cloud, consider using [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc) as your network topology. Shared VPC provides centralized network configuration management while maintaining separation of environments. 



For more information about network security best practices, see [Implement zero trust](https://docs.cloud.google.com/architecture/framework/security/implement-zero-trust) and [Decide the network design for your Google Cloud landing zone](https://docs.cloud.google.com/architecture/landing-zones/decide-network-design). 

## Data protection and privacy

The Conversational Analytics API encrypts your data that is stored in Google Cloud using [default encryption](https://docs.cloud.google.com/docs/security/encryption/default-encryption). Example data includes the following:

  * Data agent configuration (system instructions and example queries)
  * Data agent context (staging and published context)
  * Conversation messages and state history



This data can only be accessed by the Conversational Analytics API instances.

You can enable [customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/cmek) to encrypt your data at rest. With CMEK, keys are stored in Cloud Key Management Service (Cloud KMS) as software-protected keys or hardware-protected keys with Cloud HSM, but they are managed by you. To provision encryption keys automatically, you can enable [Cloud KMS Autokey](https://docs.cloud.google.com/kms/docs/autokey-overview). When you enable Autokey, a developer can request a key from Cloud KMS, and the service agent provisions a key that matches the developer's intent. With Cloud KMS Autokey, keys are available on demand, are consistent, and follow industry-standard practices.

### Where data is processed

The Conversational Analytics API supports [data residency](https://cloud.google.com/terms/data-residency) for data that is stored on Google Cloud. Data residency lets you choose the regions that you want your data to be stored in using the [Resource Location Restriction policy constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). You can use [Cloud Asset Inventory](https://docs.cloud.google.com/asset-inventory/docs/asset-inventory-overview) to verify the location of the Conversational Analytics API resources.

### Data privacy

To help protect the privacy of your data, the Conversational Analytics API conforms to the [Common Privacy Principles](https://cloud.google.com/privacy/common-privacy-principles).

The Conversational Analytics API acts as a data processor for Customer Data. Google also acts as a data controller for information such as billing and account management and abuse detections. For more information, see [Google Cloud Privacy Notice](https://cloud.google.com/terms/cloud-privacy-notice).

## Audit logging

The Conversational Analytics API writes the following types of audit logs:

  * **Admin Activity audit logs** : Includes `ADMIN WRITE` operations that write metadata or configuration information.

  * **Data Access audit logs** : Includes `ADMIN READ` operations that read metadata or configuration information. Also includes `DATA READ` and `DATA WRITE` operations that read or write user-provided data.




For more information, see [Audit logging](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/audit-logging).

## Access transparency

You can use [Access Approval](https://docs.cloud.google.com/assured-workloads/access-approval/docs/overview) and [Access Transparency](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/overview) to control access to the Conversational Analytics API instances by Google personnel who support the service. Access Approval lets you approve or dismiss requests for access by Google employees. Access Transparency logs offer near real-time insight when Google Cloud administrators access the resources.

## Monitoring and incident response

You can use a variety of tools to help you monitor the performance and security of the Conversational Analytics API. Consider the following:

  * Logs Explorer to view and analyze event logs and create [custom metrics](https://docs.cloud.google.com/logging/docs/logs-based-metrics) and alerts.
  * Use the Cloud Monitoring dashboard to monitor the performance of the Conversational Analytics API. 
  * Deploy [cloud controls and frameworks](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-apply-framework) in Security Command Center to detect vulnerabilities and threats to the Conversational Analytics API (such as privilege escalations). You can set up alerts and [playbooks](https://docs.cloud.google.com/security-command-center/docs/playbooks-overview) for your security operations center (SOC) analysts so that they can respond to findings.



## What's next

  * Use [Google Threat Intelligence](https://cloud.google.com/security/products/threat-intelligence) to track external threats that apply to your business.
  * Learn how to [authenticate to the Conversational Analytics API](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/authentication).
  * Learn about [access control](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/access-control) for the Conversational Analytics API.
  * Learn how to [protect resources with customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/cmek).
  * Learn how to [view and manage audit logs](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/audit-logging).
  * Learn how to [configure a service perimeter with VPC Service Controls](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/vpc-sc).
  * Learn how to [apply organization policy constraints](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/organization-policies).
  * Learn about [data residency and supported regions](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/data-residency).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
