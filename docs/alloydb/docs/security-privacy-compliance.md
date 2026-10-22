---
url: https://docs.cloud.google.com/alloydb/docs/security-privacy-compliance/
title: Security, privacy, risk, and compliance for AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:30:06.904870+00:00
---

# Security, privacy, risk, and compliance for AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/security-privacy-compliance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Security, privacy, risk, and compliance for AlloyDB for PostgreSQL Stay organized with collections  Save and categorize content based on your preferences. 

This document provides an overview of various controls that support the security of AlloyDB for PostgreSQL on Google Cloud and links to further information on how to configure the controls. Security controls such as network security options, policies, and access management can also help you address your business risks and meet the privacy and regulatory requirements that apply to your business.

The security, privacy, risk, and compliance for AlloyDB for PostgreSQL use a [shared responsibility](https://docs.cloud.google.com/architecture/framework/security/shared-responsibility-shared-fate) model. For example, Google secures the infrastructure that AlloyDB for PostgreSQL and other Google Cloud services run on, and provides you with the capabilities that help you manage access to your services and resources. For more information about how we secure the infrastructure, see the [Google infrastructure security design overview](https://docs.cloud.google.com/docs/security/infrastructure/design).

## AlloyDB architecture

The following diagram shows the components of the AlloyDB architecture.

![AlloyDB architecture.](https://docs.cloud.google.com/static/alloydb/images/alloydb-architecture.svg)

The components include the following:

  * AlloyDB instances deploy across multiple zones to enable high availability and resiliency.
  * An application in Google Cloud or in another environment that connects to the primary instance of AlloyDB. The diagram shows the application running in the same Google Cloud project as AlloyDB, though you can also run the application in another project in your Google Cloud organization.
  * In a hybrid environment, [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview) or [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview) can provide access to resources on your corporate network.
  * A service perimeter that is created using [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview). VPC Service Controls lets you control the movement of data between Google services or resources and set up context-based perimeter security.



For information about the AlloyDB endpoint, see [AlloyDB API](https://docs.cloud.google.com/alloydb/docs/reference/rest). By default, this endpoint is not a publicly routable endpoint and can't receive inbound traffic from public networks. To enable AlloyDB instances to receive inbound traffic over public networks, see [Connect using public IP](https://docs.cloud.google.com/alloydb/docs/connect-public-ip).

For information about AlloyDB connectors, see Application connectivity.

## Provisioned services

When you get started with AlloyDB, you enable the following APIs:

  * [`alloydb.googleapis.com`](https://docs.cloud.google.com/alloydb/docs/reference/rest)
  * [`compute.googleapis.com`](https://docs.cloud.google.com/compute/docs/reference/rest/v1)
  * [`cloudresourcemanager.googleapis.com`](https://docs.cloud.google.com/resource-manager/reference/rest)
  * [`servicenetworking.googleapis.com`](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest)



For more information, see [Quickstart: Create and connect to a database](https://docs.cloud.google.com/alloydb/docs/quickstart/create-and-connect).

## Authentication for Google Cloud management

Administrators and developers who create and manage AlloyDB instances must authenticate to Google Cloud to verify their identity and access privileges. You must set up each user with a [user account that is managed](https://docs.cloud.google.com/architecture/identity/overview-google-authentication#google_for_organizations) by Cloud Identity, Google Workspace, or an [identity provider that you've federated](https://docs.cloud.google.com/architecture/identity/best-practices-for-federating) with Cloud Identity or Google Workspace. For more information, see [Overview of identity and access management](https://docs.cloud.google.com/architecture/identity).

After you create the user accounts, implement security best practices such as [single sign-on](https://docs.cloud.google.com/architecture/identity/single-sign-on) and [2-step verification](https://support.google.com/a/answer/175197). For more authentication best practices, see [Manage identity and access](https://docs.cloud.google.com/architecture/framework/security/identity-access).

## Identity and Access Management

To manage Identity and Access Management (IAM) roles at scale for your administrators and developers, consider creating separate [functional groups](https://docs.cloud.google.com/architecture/identity/overview-google-authentication#group) for your various database user roles and applications. Grant the IAM roles or permissions that are required to manage AlloyDB to your groups. When you assign roles to your groups, follow the principle of least privilege and other [IAM security best practices](https://docs.cloud.google.com/iam/docs/using-iam-securely). For more information, see [Best practices for using Google Groups](https://docs.cloud.google.com/iam/docs/groups-best-practices).

For more information about setting up IAM, see [IAM overview](https://docs.cloud.google.com/iam/docs/overview).

When clients use IAM database authentication to access AlloyDB, you can also use IAM to control their access to AlloyDB. For more information about the IAM roles that are required for AlloyDB, see [IAM roles and permissions for AlloyDB](https://docs.cloud.google.com/alloydb/docs/reference/iam-roles-permissions).

If you use the Auth Proxy or the Language Connectors (as described in Application connectivity), you can use IAM to control which application workloads can connect to AlloyDB. For more information about using IAM with the Auth Proxy, see [Choose the IAM principal and prepare it for authorization](https://docs.cloud.google.com/alloydb/docs/auth-proxy/connect#iam-principal). To use automatic IAM authentication with the AlloyDB Language Connectors, see [Manage IAM authentication](https://docs.cloud.google.com/alloydb/docs/manage-iam-authn).

## Default service accounts and service agents

A [service account](https://docs.cloud.google.com/iam/docs/service-account-overview) is a special type of non-interactive Google Account intended to represent a non-human user that needs to authenticate and be authorized to access data in Google APIs. Because AlloyDB is a fully-managed service, Google manages your AlloyDB service account on your behalf. When you enable AlloyDB, an AlloyDB service account is created for your project (`service-PROJECT_NUMBER-gcp-sa-alloydb-iam.gserviceaccount.com`). AlloyDB resources such as the PostgreSQL server use this service account to run.

[Service agents](https://docs.cloud.google.com/iam/docs/service-account-types#service-agents) are the IAM roles and permissions that some Google Cloud services use so that they can access your resources and act on your behalf. The managed AlloyDB service account uses the IAM privileges of the [AlloyDB service agent](https://docs.cloud.google.com/iam/docs/service-agents).

## Policies for AlloyDB

The predefined organization policies that apply to AlloyDB define whether AlloyDB can use [customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/alloydb/docs/cmek) to encrypt your data. Configure AlloyDB to use CMEK if your regulatory obligations require you to have greater control over the keys used to encrypt AlloyDB data at rest. The policies include the following:

  * Restrict which services can create resources without CMEK (`constraints/gcp.restrictNonCmekServices`)
  * Restrict which projects can supply Cloud KMS CryptoKeys for CMEK (`constraints/gcp.restrictCmekCryptoKeyProjects`)



For more information, see [Use predefined organization policies](https://docs.cloud.google.com/alloydb/docs/alloydb-predefined-constraints).

You can use custom organization policies to configure restrictions on AlloyDB at a project, folder, or organization level. If you enable public IP addresses, we recommend that you configure a custom policy constraint to enforce who can use the public IP address. To refine your policies, you can add AlloyDB instance fields (for example, enable public IP address or enable outbound public IP address) to the policy. For more information, see [Use custom organization policies](https://docs.cloud.google.com/alloydb/docs/alloydb-custom-constraints).

## Network security

By default, Google applies default protections to data in transit for all Google Cloud services, including AlloyDB instances that are running on Google Cloud. For more information about default network protections, see [Encryption in transit](https://docs.cloud.google.com/docs/security/encryption-in-transit).

AlloyDB supports TLS 1.3 encryption for communication between the database instance and clients. AlloyDB automatically generates the server certificate for this connection. To use client certificates for mutual authentication, you must configure an AlloyDB Language Connector (which uses mTLS authentication) or the AlloyDB Auth Proxy.

If required by your organization, you can configure additional security controls to further protect traffic on the Google Cloud network and traffic between the Google Cloud network and your corporate network. Consider the following:

  * AlloyDB supports [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview). VPC Service Controls let you control the movement of data in Google services and set up context-based perimeter security. For more information on setting up VPC Service Controls, see [Configure VPC Service Controls](https://docs.cloud.google.com/alloydb/docs/vpc-sc/configure-vpc-service-controls).

    * If you enable public IP addresses, use AlloyDB Language Connectors and a custom organization policy to control who has access to AlloyDB instances.
  * In Google Cloud, consider [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc) as your network topology. Shared VPC provides centralized network configuration management while maintaining separation of environments.

  * Use Cloud VPN or Cloud Interconnect to maximize security and reliability for the connection between your corporate network and Google Cloud. For more information, see [Choosing a Network Connectivity product](https://docs.cloud.google.com/network-connectivity/docs/how-to/choose-product).




For more information about network security best practices, see [Implement zero trust](https://docs.cloud.google.com/architecture/framework/security/implement-zero-trust) and [Decide the network design for your Google Cloud landing zone](https://docs.cloud.google.com/architecture/landing-zones/decide-network-design).

## Application connectivity

You can secure the connection between applications and AlloyDB using the following methods:

  * The [AlloyDB Auth Proxy](https://docs.cloud.google.com/alloydb/docs/auth-proxy/overview) or the [AlloyDB Language Connector](https://docs.cloud.google.com/alloydb/docs/language-connectors-overview), to configure a secure TCP tunnel to the AlloyDB instance.
  * Database authentication.
  * [Serverless VPC Access](https://docs.cloud.google.com/vpc/docs/serverless-vpc-access) to connect AlloyDB directly with Cloud Run.
  * [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect) or [private services access](https://docs.cloud.google.com/alloydb/docs/about-private-services-access) to connect to an application in another VPC on Google Cloud using the AlloyDB private IP address. Use this method to keep traffic in Google Cloud. If you want to use Private Service Connect, you must configure Private Service Connect when you create the AlloyDB database cluster.



The following diagram shows the connectivity options.

![AlloyDB connectivity options.](https://docs.cloud.google.com/static/alloydb/images/alloydb-app-connectors.svg)

For more information about options for setting up connections to services without an external IP address, see [Private access options for services](https://docs.cloud.google.com/vpc/docs/private-access-options).

### Database authentication

AlloyDB provides the following authentication methods for database clients:

  * Built-in database authentication using a username and password. Authorization is determined using `GRANT` or `REVOKE` statements. For more information, see [Manage AlloyDB user roles](https://docs.cloud.google.com/alloydb/docs/database-users/about).
  * IAM authentication using IAM principals such as users and service accounts. The AlloyDB Language Connectors can automate the process for IAM authentication. For more information, see the [AlloyDB Language Connectors overview](https://docs.cloud.google.com/alloydb/docs/language-connectors-overview). IAM authentication has the following benefits: 
    * **Unified access control** : IAM centralizes access control across all Google Cloud resources, including databases. Unified access control means consistent policies and easier user and role management.
    * **Reduced credential management** : Users don't need separate database passwords. IAM authentication uses their existing Google Account credentials.
    * **Short-lived tokens** : IAM authentication uses short-lived access tokens, reducing the risk of leaked passwords or compromised credentials.



### Connectors

You can use the [AlloyDB Auth Proxy](https://docs.cloud.google.com/alloydb/docs/auth-proxy/overview) or an [AlloyDB Language Connector](https://docs.cloud.google.com/alloydb/docs/language-connectors-overview) to configure an encrypted connection to the database client. The AlloyDB Auth Proxy is a client-side proxy that transparently upgrades non-TLS connections to TLS 1.3 connections. The Language Connectors are client libraries that connect to a proxy server on the AlloyDB cluster. Both connectors use IAM to authorize the connection and protect the connection using mTLS. Optionally, you can configure passwordless authentication instead of IAM authentication.

If you use the Auth Proxy, review the [Best practices for using the AlloyDB Auth Proxy](https://docs.cloud.google.com/alloydb/docs/auth-proxy/best-practices).

## Data protection and privacy

This section describes how AlloyDB protects your data and privacy of that data.

AlloyDB encrypts your data that is stored in your cluster (for example, the instance name, instance configuration, table contents, row names, and custom functions) using [default encryption](https://docs.cloud.google.com/docs/security/encryption/default-encryption). This data can only be accessed by AlloyDB instances.

You can enable [customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/alloydb/docs/cmek) to encrypt your cluster data at rest. With CMEK, keys are stored in Cloud KMS as software-protected keys or hardware-protected keys (with Cloud HSM), but they are managed by you. To provision encryption keys automatically, you can enable [Cloud KMS Autokey](https://docs.cloud.google.com/kms/docs/autokey-overview). When you enable Autokey, a developer can request a key from Cloud KMS, and the service agent provisions a key that matches the developer's intent. With Cloud KMS Autokey, keys are available on demand, are consistent, and follow industry-standard practices.

In addition, AlloyDB supports [Cloud External Key Manager (Cloud EKM)](https://docs.cloud.google.com/alloydb/docs/cmek#ekm), which lets you store your keys in an external key manager outside of Google Cloud. If you are using Cloud EKM, [Key Access Justifications](https://docs.cloud.google.com/assured-workloads/key-access-justifications/docs/overview) adds a field to your Cloud EKM requests that lets you view the reason for each request. With select external key management partners, you can automatically approve or deny these requests, based on the justification.

### Where data is processed

AlloyDB supports [data residency](https://cloud.google.com/terms/data-residency) for that data that is stored in your cluster. Data residency lets you choose the regions that you want your data to be stored in using the [Resource Location Restriction policy constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). You can use [Cloud Asset Inventory](https://docs.cloud.google.com/asset-inventory/docs/asset-inventory-overview) to verify the location of AlloyDB resources.

If you require data residency for data in use, you can configure Assured Workloads. For more information, see [Assured Workloads and data residency](https://docs.cloud.google.com/assured-workloads/docs/data-residency).

### Data privacy

To help protect the privacy of your data, AlloyDB conforms to the [Common Privacy Principles](https://cloud.google.com/privacy/common-privacy-principles).

AlloyDB acts as a data processor for Customer Data. Google also acts as a data controller for information such as billing and account management and abuse detections. For more information, see [Google Cloud Privacy Notice](https://cloud.google.com/terms/cloud-privacy-notice).

## Audit logging

AlloyDB writes the following types of audit logs:

  * **Admin Activity audit logs** : Includes `ADMIN WRITE` operations that write metadata or configuration information.
  * **Data Access audit logs** : Includes `ADMIN READ` operations that read metadata or configuration information. Also includes `DATA READ` and `DATA WRITE` operations that read or write user-provided data.
  * **System Event audit logs** : Identifies automated Google Cloud actions that modify the configuration of resources.



For more information, see [AlloyDB audit logging](https://docs.cloud.google.com/alloydb/docs/audit-logging).

In addition, to meet regulatory requirements, you can use the [pgAudit extension](https://docs.cloud.google.com/alloydb/docs/pgaudit/about) to enable an audit trail of database commands. pgAudit extension logs include details on what commands were performed, when the commands were performed, and who performed the commands.

## Access transparency

You can use Access Approval and Access Transparency to control access to AlloyDB instances by Google personnel who support the service. Access Approval lets you approve or dismiss requests for access by Google employees. Access Transparency logs offer near real-time insight when Google Cloud administrators access the resources.

## Monitoring and incident response

You can use a variety of tools to help you monitor the performance and security of AlloyDB. Consider the following:

  * Use Logs Explorer to view and analyze event logs and create [custom metrics](https://cloud.google.com/blog/products/databases/creating-custom-log-based-metrics-for-postgresql-and-alloydb/) and alerts.
  * Use the AlloyDB system insights dashboard or Cloud Monitoring dashboard to monitor the performance of AlloyDB instances. For more information, see [Monitor instances](https://docs.cloud.google.com/alloydb/docs/monitor-instance).
  * Enable the [pgAudit](https://docs.cloud.google.com/alloydb/docs/pgaudit/about) extension to audit AlloyDB operations (such as commands and queries performed on an AlloyDB instance). These logs include PostgreSQL database logs and container logs for dataplane agents.
  * Configure Security Command Center to detect [SQL vulnerabilities](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#sql-findings) and [threats](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview) to AlloyDB (such as privilege escalations). You can set up alerts and [playbooks](https://docs.cloud.google.com/security-command-center/docs/playbooks-overview) for your security operations center (SOC) analysts so that they can respond to findings.



## Certifications and compliance

Meeting your regulatory requirements is a [shared responsibility](https://docs.cloud.google.com/architecture/framework/security/shared-responsibility-shared-fate) between you and Google.

AlloyDB has received many certifications, including the following:

  * [International Organization for Standardization (ISO) 27001](https://cloud.google.com/security/compliance/iso-27001), [ISO 27017](https://cloud.google.com/security/compliance/iso-27017), [ISO 27018](https://cloud.google.com/security/compliance/iso-27018), [ISO 27701](https://cloud.google.com/security/compliance/iso-27701)
  * [Service and Organization Controls (SOC) 1](https://cloud.google.com/security/compliance/soc-1), [SOC 2](https://cloud.google.com/security/compliance/soc-2), [SOC 3](https://cloud.google.com/security/compliance/soc-3)
  * [Payment Card Industry Data Security Standards (PCI DSS)](https://cloud.google.com/security/compliance/pci-dss)
  * [Health Insurance Portability and Accountability Act (HIPAA)](https://cloud.google.com/security/compliance/hipaa)



For more information about Google Cloud compliance with different regulatory frameworks and certifications, see the [compliance resource center](https://cloud.google.com/compliance).

AlloyDB also supports Assured Workloads, which lets you apply controls to specific folders in your Google organization that support regulatory, regional, or sovereign requirements. For more information, see [Supported products by control package](https://docs.cloud.google.com/assured-workloads/docs/supported-products).

## What's next

  * [Configure resiliency with clusters](https://docs.cloud.google.com/alloydb/docs/cluster-create).
  * [Enable backups](https://docs.cloud.google.com/alloydb/docs/backup/overview).
  * Use [Terraform to deploy AlloyDB](https://github.com/GoogleCloudPlatform/terraform-google-alloy-db).
  * Use [Google Threat Intelligence](https://cloud.google.com/security/products/threat-intelligence) to track external threats that apply to your business.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
