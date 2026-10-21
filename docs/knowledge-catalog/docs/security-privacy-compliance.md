---
url: https://docs.cloud.google.com/knowledge-catalog/docs/security-privacy-compliance/
title: Security, privacy, risk, and compliance for Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:37:26.459766+00:00
---

# Security, privacy, risk, and compliance for Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/security-privacy-compliance/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  Security, privacy, risk, and compliance for Knowledge Catalog Stay organized with collections  Save and categorize content based on your preferences. 

This document provides an overview of various controls that support the security of Knowledge Catalog on Google Cloud and links to further information on how to configure the controls. Security controls such as network security options, policies, and access management can help you address your business risks and meet the privacy and regulatory requirements that apply to your business. 

The security, privacy, risk, and compliance for Knowledge Catalog use a [shared responsibility](https://docs.cloud.google.com/architecture/framework/security/shared-responsibility-shared-fate) model. For example, because Knowledge Catalog is a fully-managed service, Google secures and manages the infrastructure that Knowledge Catalog and other Google Cloud services run on, and provides you with the capabilities that help you manage access to your services and resources. For more information about how we secure the infrastructure, see the [Google infrastructure security design overview](https://docs.cloud.google.com/docs/security/infrastructure/design). 

Knowledge Catalog security controls let you protect catalog metadata, including entry groups, entries, aspects, and business glossaries. You can configure access controls, organization policies, network perimeters, and customer-managed encryption keys to govern catalog resources and meet data residency requirements. 

## Provisioned services

Knowledge Catalog uses the following APIs:

  * [`dataplex.googleapis.com`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest)
  * [`datalineage.googleapis.com`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/data-lineage/rest)



To get started, see [Enable Knowledge Catalog](https://docs.cloud.google.com/knowledge-catalog/docs/enable-api).

## Authentication for Google Cloud management

Administrators and developers who create and manage Knowledge Catalog instances must authenticate to Google Cloud to verify their identity and access privileges. You must set up each user with a [user account that is managed](https://docs.cloud.google.com/architecture/identity/overview-google-authentication#google_for_organizations) by Cloud Identity, Google Workspace, or an [identity provider that you've federated](https://docs.cloud.google.com/architecture/identity/best-practices-for-federating) with Cloud Identity or Google Workspace. For more information, see [Overview of Google identity management](https://docs.cloud.google.com/architecture/identity/overview-google-authentication). 

After you create the user accounts, implement security best practices such as [single sign-on](https://docs.cloud.google.com/architecture/identity/single-sign-on) and [2-step verification](https://support.google.com/a/answer/175197). 

## Authentication for Google Cloud resource access

[Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation) lets you use your external identity provider (IdP) to authenticate your workforce users so that they can access Google Cloud resources. Use Workforce Identity Federation when users require programmatic access to your Google Cloud resources and you store your users' credentials in IdPs that support OpenID Connect (OIDC) or Security Assertion Markup Language (SAML).

[Workload Identity Federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation) lets you use your external IdP to grant your on-premises or multi-cloud workloads access to Google Cloud resources, without using a service account key. You can use identity federation with IdPs such as Amazon Web Services (AWS), Microsoft Entra ID, GitHub, or Okta.

For more information about Knowledge Catalog support for identity federation, see [Federated identity supported services](https://docs.cloud.google.com/iam/docs/federated-identity-supported-services).

For more information about authentication in Google Cloud, see [Authentication](https://docs.cloud.google.com/iam/docs/authentication).

## Identity and Access Management

To manage Identity and Access Management (IAM) roles at scale for your administrators and developers, consider creating separate [functional groups](https://docs.cloud.google.com/architecture/identity/overview-google-authentication#group) for your various user roles and applications. Grant the IAM roles or permissions that are required to manage Knowledge Catalog to your groups. When you assign roles to your groups, follow the principle of least privilege and other [IAM security best practices](https://docs.cloud.google.com/iam/docs/using-iam-securely). For more information, see [Best practices for using Google Groups](https://docs.cloud.google.com/iam/docs/groups-best-practices). 

For more information about using IAM with Knowledge Catalog, see [Manage access with IAM](https://docs.cloud.google.com/knowledge-catalog/docs/iam-and-access-control). For more information about setting up IAM, see [IAM overview](https://docs.cloud.google.com/iam/docs/overview). 

You can grant predefined and custom roles for Knowledge Catalog resources such as entry groups and entries.

## Knowledge Catalog service accounts

When you enable Knowledge Catalog, Google creates service accounts for you. A [service account](https://docs.cloud.google.com/iam/docs/service-account-overview) is a special type of non-interactive Google Account that's typically used by an application or compute workload, such as a Compute Engine instance, rather than a person. Applications use service accounts to access Google APIs.

### Service agents

To enable Knowledge Catalog to access your resources on your behalf, Google Cloud creates a special service account known as a [service agent](https://docs.cloud.google.com/iam/docs/service-account-types#service-agents).

Knowledge Catalog uses the following Knowledge Catalog service agents:

  * `service-PROJECT_NUMBER@gcp-sa-dataplex.iam.gserviceaccount.com`
  * `service-org-ORGANIZATION_NUMBER@gcp-sa-dataplex.iam.gserviceaccount.com`
  * `service-org-ORGANIZATION_NUMBER@gcp-sa-dataplex-cmek.iam.gserviceaccount.com`
  * `service-PROJECT_NUMBER@gcp-sa-datalineage.iam.gserviceaccount.com`



For more information about Knowledge Catalog service agents, see [Manage access with IAM](https://docs.cloud.google.com/knowledge-catalog/docs/iam-and-access-control#service-agent).

## Policies for Knowledge Catalog

The predefined organization policies that apply to Knowledge Catalog include the following:

  * Resource location restriction (`constraints/gcp.resourceLocations`)
  * Restrict which projects can supply Cloud KMS keys for CMEK (`constraints/gcp.restrictCmekCryptoKeyProjects`)
  * Restrict which services can create resources without CMEK (`constraints/gcp.restrictNonCmekServices`)
  * Restrict endpoint usage (`constraints/gcp.restrictEndpointUsage`)
  * Restrict resource service usage (`constraints/gcp.restrictServiceUsage`)
  * Restrict TLS cipher suites (`constraints/gcp.restrictTLSCipherSuites`)



You can use custom organization policies to configure restrictions on Knowledge Catalog at a project, folder, or organization level. For more information, see [Creating and managing custom constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-custom-constraints). 

For more information about organization policies, see [Manage Knowledge Catalog resources using custom constraints](https://docs.cloud.google.com/knowledge-catalog/docs/dataplex-custom-constraints).

## Network security

By default, Google applies default protections to data in transit for all Google Cloud services, including Knowledge Catalog instances that are running on Google Cloud. For more information about default network protections, see [Encryption in transit](https://docs.cloud.google.com/docs/security/encryption-in-transit). 

If required by your organization, you can configure additional security controls to further protect traffic on the Google Cloud network and traffic between the Google Cloud network and your corporate network. Consider the following: 

  * Knowledge Catalog supports [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview). VPC Service Controls let you control the movement of data in Google services and set up context-based perimeter security. 
  * In Google Cloud, consider using [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc) as your network topology. Shared VPC provides centralized network configuration management while maintaining separation of environments. 



For more information about network security best practices, see [Implement zero trust](https://docs.cloud.google.com/architecture/framework/security/implement-zero-trust) and [Decide the network design for your Google Cloud landing zone](https://docs.cloud.google.com/architecture/landing-zones/decide-network-design). 

## Data protection and privacy

Knowledge Catalog encrypts your data that is stored in Google Cloud using [default encryption](https://docs.cloud.google.com/docs/security/encryption/default-encryption). Example data includes the following:

  * Entry group and entry names
  * Tag and aspect definitions
  * Metadata attributes, descriptions, and tags
  * Business glossary terms and relationships



This data can only be accessed by Knowledge Catalog instances.

You can enable [customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/knowledge-catalog/docs/cmek) to encrypt your data at rest. With CMEK, keys are stored in Cloud Key Management Service (Cloud KMS) as software-protected keys or hardware-protected keys with Cloud HSM, but they are managed by you. To provision encryption keys automatically, you can enable [Cloud KMS Autokey](https://docs.cloud.google.com/kms/docs/autokey-overview). When you enable Autokey, a developer can request a key from Cloud KMS, and the service agent provisions a key that matches the developer's intent. With Cloud KMS Autokey, keys are available on demand, are consistent, and follow industry-standard practices.

In addition, Knowledge Catalog supports Cloud External Key Manager (Cloud EKM), which lets you store your keys in an external key manager outside of Google Cloud. For more information, see [Enable customer-managed encryption keys](https://docs.cloud.google.com/knowledge-catalog/docs/cmek).

### Where data is processed

Knowledge Catalog supports [data residency](https://cloud.google.com/terms/data-residency) for data that is stored on Google Cloud. Data residency lets you choose the regions that you want your data to be stored in using the [Resource Location Restriction policy constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). You can use [Cloud Asset Inventory](https://docs.cloud.google.com/asset-inventory/docs/asset-inventory-overview) to verify the location of Knowledge Catalog resources.

If you require data residency for data in use, you can configure Assured Workloads. For more information, see [Assured Workloads and data residency](https://docs.cloud.google.com/assured-workloads/docs/data-residency).

### Data privacy

To help protect the privacy of your data, Knowledge Catalog conforms to the [Common Privacy Principles](https://cloud.google.com/privacy/common-privacy-principles).

Knowledge Catalog acts as a data processor for Customer Data. Google also acts as a data controller for information such as billing and account management and abuse detections. For more information, see [Google Cloud Privacy Notice](https://cloud.google.com/terms/cloud-privacy-notice).

## Audit logging

Knowledge Catalog writes the following types of audit logs:

  * **Admin Activity audit logs** : Includes `ADMIN WRITE` operations that write metadata or configuration information.

  * **Data Access audit logs** : Includes `ADMIN READ` operations that read metadata or configuration information. Also includes `DATA READ` and `DATA WRITE` operations that read or write user-provided data.




For more information, see [Audit logging](https://docs.cloud.google.com/knowledge-catalog/docs/audit-logging).

## Access transparency

You can use [Access Approval](https://docs.cloud.google.com/assured-workloads/access-approval/docs/overview) and [Access Transparency](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/overview) to control access to Knowledge Catalog instances by Google personnel who support the service. Access Approval lets you approve or dismiss requests for access by Google employees. Access Transparency logs offer near real-time insight when Google Cloud administrators access the resources.

## Monitoring and incident response

You can use a variety of tools to help you monitor the performance and security of Knowledge Catalog. Consider the following:

  * Logs Explorer to view and analyze event logs and create [custom metrics](https://docs.cloud.google.com/logging/docs/logs-based-metrics) and alerts.
  * Use the Cloud Monitoring dashboard to monitor the performance of Knowledge Catalog. For more information, see [Monitor Knowledge Catalog](https://docs.cloud.google.com/knowledge-catalog/docs/monitoring).
  * Deploy [cloud controls and frameworks](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-apply-framework) in Security Command Center to detect vulnerabilities and threats to Knowledge Catalog (such as privilege escalations). You can set up alerts and [playbooks](https://docs.cloud.google.com/security-command-center/docs/playbooks-overview) for your security operations center (SOC) analysts so that they can respond to findings.



## Certifications and compliance

Meeting your regulatory requirements is a [shared responsibility](https://docs.cloud.google.com/architecture/framework/security/shared-responsibility-shared-fate) between you and Google.

Knowledge Catalog has received a variety of certifications, including the following:

  * ISO 27001
  * SOC 2
  * FedRAMP
  * DoD IL5
  * ITAR



For more information about Google Cloud compliance with different regulatory frameworks and certifications, see the [compliance resource center](https://cloud.google.com/security/compliance).

Knowledge Catalog also supports Assured Workloads (subject to the limitations of each [control package](https://docs.cloud.google.com/assured-workloads/docs/control-packages)), which lets you apply controls to specific folders in your Google organization that support regulatory, regional, or sovereign requirements. For more information, see [Supported products by control package](https://docs.cloud.google.com/assured-workloads/docs/supported-products).

## What's next

  * Use [Terraform to deploy Knowledge Catalog](https://docs.cloud.google.com/knowledge-catalog/docs/terraform).
  * Use [Google Threat Intelligence](https://cloud.google.com/security/products/threat-intelligence) to track external threats that apply to your business.
  * Learn how to [manage access](https://docs.cloud.google.com/knowledge-catalog/docs/iam-and-access-control) in Knowledge Catalog.
  * Learn how to configure [customer-managed encryption keys](https://docs.cloud.google.com/knowledge-catalog/docs/cmek) in Knowledge Catalog.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
