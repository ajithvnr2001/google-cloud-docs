---
url: https://docs.cloud.google.com/docs/security/compliance/hipaa/
title: HIPAA compliance on Google Cloud and Google Workspace \u00a0|\u00a0 Security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:22:41.936936+00:00
---

# HIPAA compliance on Google Cloud and Google Workspace  |  Security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/security/compliance/hipaa/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Guides ](https://docs.cloud.google.com/docs/security/overview/whitepaper)



Send feedback 

#  HIPAA compliance on Google Cloud and Google Workspace Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how Google Cloud and Google Workspace support the Health Insurance Portability and Accountability Act (HIPAA) and how you can configure Google Cloud to help meet your HIPAA responsibilities. This guide is intended for security officers, compliance officers, IT administrators, and other employees who are responsible for HIPAA implementation and compliance on Google Cloud and Google Workspace.

## Shared responsibility

The U.S. Department of Health and Human Services (HHS) doesn't offer a certification program for HIPAA compliance. Complying with HIPAA is a shared responsibility between you and Google.

HIPAA requires compliance with the [Security Rule](https://www.hhs.gov/hipaa/for-professionals/security/index.html), the [Privacy Rule](https://www.hhs.gov/hipaa/for-professionals/privacy/index.html), and the [Breach Notification Rule](https://www.hhs.gov/hipaa/for-professionals/breach-notification/index.html). Google Cloud and Google Workspace support HIPAA compliance within the scope of a Business Associate Agreement, but ultimately you are responsible for evaluating your own HIPAA compliance.

Google enters into Business Associate Agreements as necessary under HIPAA.

**Note:** Any capitalized terms that are used but not defined in this document are based on the [definitions in HIPAA](https://www.hhs.gov/hipaa/for-professionals/index.html). In this document, _Protected Health Information (PHI)_ means the PHI that Google receives from a Covered Entity.

### Customer responsibilities

You must determine the following:

  * Whether you are a Covered Entity or a Business Associate of a Covered Entity.
  * Whether you require a [Business Associate Agreement](https://cloud.google.com/terms/hipaa-baa) with Google.



Google provides infrastructure security controls that are designed to support your HIPAA requirements for the storage and processing of PHI. You're responsible for ensuring that your environment and applications that you build on Google Cloud are properly configured and secured according to HIPAA requirements. For more information, see [Shared fate](https://cloud.google.com/security/shared-fate).

For information about Google's approach to security and data protection, see the [Google security overview](https://docs.cloud.google.com/docs/security/overview/whitepaper) and [Google infrastructure security design overview](https://docs.cloud.google.com/docs/security/infrastructure/design).

## Google Cloud features and pricing

The HIPAA BAA for Google Cloud includes the entire Google Cloud infrastructure, not only a subset of Google Cloud. As a result, you aren't restricted to a specific region and you can use multi-regional service redundancy. You can also use [Spot VMs](https://cloud.google.com/solutions/spot-vms) to reduce costs.

Google also offers HIPAA-regulated customers the same services at the same [pricing](https://cloud.google.com/pricing) that is available to all customers, including [sustained use discounts](https://docs.cloud.google.com/compute/docs/sustained-use-discounts).

## Google Cloud supported services

_Last updated: 2025-09-17_

The [Google Cloud BAA](https://cloud.google.com/terms/hipaa-baa) includes Google Cloud's entire infrastructure (all regions, all zones, all network paths, all points of presence), and the following products:

  * Access Approval
  * Access Context Manager
  * Access Transparency
  * Agent Assist for Google Cloud Contact Center as a Service (CCaaS)
  * Agent Search on Gemini Enterprise Agent Platform [1]
  * AI Platform Training and Prediction
  * AlloyDB for PostgreSQL
  * Antigravity in Gemini Enterprise
  * API Gateway [2]
  * Apigee
  * App Engine
  * Application Integration [3]
  * Artifact Analysis
  * Artifact Registry [4]
  * Assured Workloads
  * Audit Manager
  * AutoML Natural Language
  * AutoML Tables
  * AutoML Translation
  * AutoML Video
  * AutoML Vision
  * Backup and DR Service
  * Backup for GKE
  * Bare Metal Solution
  * Batch
  * BigQuery
  * BigQuery Data Transfer Service
  * BigQuery Omni
  * Bigtable
  * Binary Authorization
  * Certificate Authority Service
  * Certificate Manager
  * Cloud Asset Inventory
  * Cloud Build [5]
  * Cloud CDN [6]
  * Cloud Data Fusion
  * Cloud Deploy
  * Cloud Deployment Manager
  * Cloud DNS
  * Cloud Endpoints
  * Cloud Healthcare API
  * Cloud HSM (Hardware Security Module)
  * Cloud Identity
  * Cloud Interconnect
  * Cloud Intrusion Detection System (Cloud IDS)
  * Cloud Key Management Service [7]
  * Cloud Life Sciences
  * Cloud Load Balancing
  * Cloud Logging [8]
  * Cloud Monitoring [9]
  * Cloud NAT
  * Cloud Natural Language API
  * Cloud Profiler
  * Cloud Resource Manager API
  * Cloud Router
  * Cloud Run
  * Cloud Run functions
  * Cloud Scheduler
  * Cloud Service Mesh
  * Cloud Shell
  * Cloud Source Repositories
  * Cloud SQL
  * Cloud Storage [10]
  * Cloud Tasks
  * Cloud Trace
  * Cloud Translation
  * Cloud Vision
  * Cloud VPN
  * Cloud Workstations
  * Cluster Director
  * Colab Enterprise
  * Compute Engine
  * Connect
  * Container Registry [11]
  * Conversational Agents [12]
  * Customer Experience Agent Studio
  * Customer Experience Insights
  * Cyber Insurance Hub
  * Data Catalog
  * Data Studio [13]
  * Database Migration Service [14]
  * Dataflow
  * Dataform
  * Datastream
  * Document AI
  * Document AI Warehouse
  * Eventarc
  * Filestore [15]
  * Firestore
  * Firestore in Datastore mode (Datastore) [16]
  * Gemini Code Assist
  * Gemini Enterprise
  * Gemini Enterprise Agent Platform
  * Gemini Enterprise for Customer Experience
  * Gemini in BigQuery
  * Gemini in Colab Enterprise
  * Gemini Notebook Enterprise
  * Generative AI on Agent Platform
  * Google Cloud Armor
  * Google Cloud console
  * Google Cloud Contact Center as a Service
  * Google Cloud Fraud Defense [17]
  * Google Cloud Identity-Aware Proxy (IAP)
  * Google Cloud Managed Lustre
  * Google Cloud Managed Service for Apache Kafka
  * Google Cloud NetApp Volumes
  * Google Cloud VMware Engine [18]
  * Google Distributed Cloud connected [19]
  * Google Kubernetes Engine
  * Google Kubernetes Engine (GKE) Enterprise edition Config Management
  * Google Kubernetes Engine (GKE) Hub
  * Healthcare Data Engine
  * Identity and Access Management (IAM) [21]
  * Identity Platform [22]
  * Infrastructure Manager
  * Integration Connectors [23]
  * Key Access Justifications
  * Knative serving
  * Knowledge Catalog [24]
  * Looker (Google Cloud core) [25]
  * Looker (original) [26]
  * Managed Service for Apache Airflow
  * Managed Service for Apache Spark
  * Managed Service for Microsoft Active Directory (AD)
  * Memorystore
  * Model Armor
  * Network Connectivity Center
  * Network Service Tiers
  * Persistent Disk
  * Pub/Sub
  * Secret Manager [27]
  * Secure Source Manager
  * Security Command Center
  * Sensitive Data Protection [28]
  * Service Directory
  * Spanner
  * Speech-to-Text [29]
  * Storage Transfer Service
  * Text-to-Speech
  * Traffic Director API
  * Transfer Appliance
  * Vertex AI Workbench instances
  * Video Intelligence API
  * Virtual Private Cloud (VPC)
  * VPC Service Controls
  * Web Security Scanner
  * Workflows



## Google SecOps supported services

The following Google SecOps services[20] are supported by the BAA:

  * Google Security Operations SIEM
  * Google Security Operations SOAR
  * Mandiant Digital Threat Monitoring
  * Mandiant Security Validation



## Google Workspace supported services

_Last updated: 2025-08-31_

The following Google Workspace services are included in the Google Cloud BAA:

  * AppSheet
  * Cloud Identity Management
  * Gemini App (excluding Gemini in Google Chrome)
  * Gemini in Google Workspace
  * Gemini Mac App
  * Gmail
  * Google Apps Script
  * Google Calendar
  * Google Chat
  * Google Cloud Search
  * Google Drive (including Google Docs, Google Forms, Google Photos, Google Sheets, Google Slides, and Google Vids)
  * Google Groups
  * Google Keep
  * Google Meet
  * Google Sites
  * Google Tasks
  * Google Vault (if applicable)
  * Google Voice (managed users only)



For information about HIPAA compliance for Google Workspace, see [HIPAA compliance for Google Workspace](https://support.google.com/a/answer/3407054).

## Best practices for Google Cloud

Implement the best practices in this section to help meet your HIPAA obligations.

### General Google Cloud best practices

Implement the following best practices:

  * Enter in to a Google Cloud BAA. For instructions, see the [Privacy compliance and records for Google Cloud](https://support.google.com/cloud/answer/6329727) to review and accept the BAA.
  * [Disable unsupported Google Cloud services](https://docs.cloud.google.com/service-usage/docs/enable-disable#disabling) when working with PHI. If you can't disable a service, you must not use it for PHI.
  * Don't use pre-GA offerings as defined in the [Service Specific Terms](https://cloud.google.com/terms/service-terms) with PHI, unless expressly noted otherwise in a notice or other terms of the offering.
  * When creating or updating resources, avoid including PHI or security credentials in resource metadata, because logs might capture that information. Audit logs never include resource data contents or query results, but they might capture resource metadata.



### Identity, security, and encryption

The following table describes best practices and limitations for identity, security, and encryption services.

Supported product | Best practices and limitations  
---|---  
Cloud KMS |  Determine whether your organization has encryption requirements beyond what's required by the HIPAA Security Rule. Customer content is [encrypted at rest on Google Cloud](https://docs.cloud.google.com/docs/security/encryption/default-encryption). If you have additional encryption requirements, use [Cloud KMS](https://docs.cloud.google.com/docs/security/key-management-deep-dive).   
Identity and Access Management |  Use [IAM best practices](https://docs.cloud.google.com/iam/docs/using-iam-securely) when configuring who has access to your project. In particular, because service accounts can be used to access resources, tightly control access to those service accounts and service account keys.   
Identity Platform | 

  * Only store the minimum data needed to provide authentication and authorization for your application or service. When creating a user in Identity Platform, the only required attribute is an email address or a phone number. If you must store PHI, use a general-purpose database solution in Google Cloud. 
  * Don't store PHI in optional or custom attributes, such as display names or photo URLs. If you must store PHI, use a general-purpose database solution in Google Cloud. 
  * Don't transmit PHI from [federated external identity providers (IdPs)](https://docs.cloud.google.com/architecture/identity/overview-google-authentication#external_identities) to Identity Platform in tokens, claims, assertions or through any other mechanism. 
  * Don't synchronize PHI from external identity systems to Identity Platform. Google makes no assertions or guarantees as to the security of this information in transit or upon receipt by the third party. 
  * Don't use anonymous accounts when interacting with, managing, or storing PHI. 
  * Don't use Identity Platform SDKs and client libraries when interacting with, managing, or storing PHI. As this code runs outside of Identity Platform, Google makes no assertions or guarantees as to the security of information outside of the Identity Platform service, such as on an end-user's device. 

  
Secret Manager |  When storing secrets in Secret Manager, review and follow the [Secret Manager best practices](https://docs.cloud.google.com/secret-manager/docs/best-practices).   
  
### Logging, monitoring, and data protection

The following table describes best practices and limitations for logging, monitoring, and data protection services.

Supported product | Best practices and limitations  
---|---  
Logging | 

  * Configure [audit log export destinations](https://docs.cloud.google.com/logging/docs/export/configure_export_v2). Export audit logs to Cloud Storage for long-term archival and to BigQuery for any analytical, monitoring, and forensic needs. Configure appropriate access controls for those destinations. 
  * Configure [log access controls](https://docs.cloud.google.com/logging/docs/access-control). Users with the [Logs Viewer role (`roles/logging.viewer`)](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewer) can access Admin Activity audit logs, and users with the [Private Logs Viewer role (`roles/logging.privateLogViewer`)](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.privateLogViewer) can access Data Access audit logs. 
  * Regularly review audit logs to ensure security and compliance with requirements. For large-scale log analysis, use BigQuery or a [SIEM platform](https://cloud.google.com/discover/what-is-siem) to demonstrate compliance through log analysis. 

  
Monitoring | 

  * Don't store PHI in metadata such as metric labels, VM labels, GKE resource annotations, or dashboard titles or content. Anyone with the appropriate IAM permissions can view your monitoring console or use the Cloud Monitoring API to see this data. 
  * Don't place PHI in alerting configurations (for example, in display names or documentation) which can be sent to alert recipients. 

  
Google SecOps |  Don't use the following services or features: 

  * Third-party services other than services that are provided by a Google Affiliate or a cloud-based infrastructure provider. 
  * On-demand analyst support.
  * Non-Google services, software, or hardware that's provided to Google personnel in connection with a Mandiant Consulting Services engagement. 
  * API integration tools that aren't secure.

  
Sensitive Data Protection  |  When configuring Sensitive Data Protection jobs, ensure that any output data is written to storage targets configured as part of your secure environment.   
  
### Storage and databases

The following table describes best practices and limitations for storage and database services.

Supported product | Best practices and limitations  
---|---  
Cloud Storage |  Enable [Object Versioning](https://docs.cloud.google.com/storage/docs/object-versioning) to help preserve historical archives and recover objects after accidental deletion.   
Database Migration Service |  Use Private IP connectivity methods to avoid exposing a database containing PHI to the internet.   
Filestore | 

  * Use [IP-based access control](https://docs.cloud.google.com/filestore/docs/access-control#ip-based_access_control) to restrict which Compute Engine VMs and GKE clusters can access the Filestore instance. 
  * Use [Filestore backups](https://docs.cloud.google.com/filestore/docs/backup-restore) to recover data after accidental deletion. 

  
Datastore |  When creating or configuring indexes, encrypt PHI, security credentials, or other sensitive data before using the data as an entity key, indexed property key, or indexed property value. For more information, see [Datastore indexes](https://docs.cloud.google.com/datastore/docs/concepts/indexes).   
  
### Data analytics and business intelligence

The following table describes best practices and limitations for data analytics and business intelligence services.

Supported product | Best practices and limitations  
---|---  
Data Studio |  You must opt in to have Data Studio governed under your Google Cloud Agreement.   
Knowledge Catalog  |  Don't include PHI or PII in the values of the `google.cloud.datacatalog.lineage.v1.Process.attributes` and `google.cloud.datacatalog.lineage.v1.Run.attributes` fields.   
Looker (Google Cloud core) | 

  * Ensure that administrators review the security configurations for third-party applications and integrations as well as any corresponding security and privacy documentation from the third-party application. 
  * When creating structured queries, avoid including or storing PHI in the business logic that configures those queries. 

  
  
### AI, machine learning, and conversational agents

The following table describes best practices and limitations for AI, machine learning, and conversational agent services.

Supported product | Best practices and limitations  
---|---  
Agent Search on Gemini Enterprise Agent Platform  |  Use regional APIs and resource locations for PHI.  
Conversational Agents |  Don't include PHI or security credentials in your agent definition, including intents, training phrases, and entities.   
Speech-to-Text |  If you have entered into a BAA with Google that covers any PHI obligations under HIPAA, don't opt in to [data logging](https://docs.cloud.google.com/speech-to-text/docs/v1/data-logging).   
  
### Application development, integration, and networking

The following table describes best practices and limitations for application development, integration, and networking services.

Supported product | Best practices and limitations  
---|---  
API Gateway |  Don't include PHI or PII in the headers.  
Application Integration and Integration Connectors  | 

  * Don't include PII, PHI, or other sensitive information in the [`IntegrationParameter`](https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/IntegrationParameter), the name field in [`projects.locations.connections`](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.connections), or the configuration settings in the `Connection` resource. This information can get logged. 
  * Configure [access control for logs](https://docs.cloud.google.com/logging/docs/access-control) if the requested payload contains sensitive data. 

  
Cloud Build |  Don't include PHI in build configuration files, source control files, or other build artifacts.   
Cloud CDN |  Don't request caching of PHI. To prevent caching, see [Prevent caching](https://docs.cloud.google.com/cdn/docs/caching#preventing-caching).   
Fraud Defense |  Don't include PHI in URIs or actions.  
  
### Compute, containers, and hybrid infrastructure

The following table describes best practices and limitations for compute, containers, and hybrid infrastructure services.

Supported product | Best practices and limitations  
---|---  
Artifact Registry |  Artifact Registry encrypts data in repositories using Google default encryption or [customer-managed encryption keys](https://docs.cloud.google.com/artifact-registry/docs/cmek) (CMEK). Metadata, such as artifact names, is encrypted with Google default encryption. This metadata can appear in logs and is visible to any user account with the [Artifact Registry Reader role (`roles/artifactregistry.reader`)](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.reader) or [Artifact Registry Viewer role (`roles/artifactregistry.viewer`)](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.viewer). To help prevent unauthorized access to PHI, see [Control access and protect artifacts](https://docs.cloud.google.com/artifact-registry/docs/protect-artifacts).   
Container Registry |  Container Registry encrypts data in the storage buckets of your registries using Google default encryption or [CMEK](https://docs.cloud.google.com/container-registry/docs/using-encryption-keys). To help prevent unauthorized access to PHI, see [Best practices for securing containers](https://docs.cloud.google.com/container-registry/docs/container-best-practices).   
VMware Engine |  Retain application-level access logs for an appropriate period to meet HIPAA requirements.   
Distributed Cloud connected  |  When deploying [Distributed Cloud connected](https://docs.cloud.google.com/distributed-cloud/docs), you're responsible for certain security aspects, particularly physical security. To help secure your deployment, see [Physical security best practices](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/security#physical).   
  
### Looker (original)

The following table describes best practices and limitations for Looker when deployed in a hosted environment by Google.

Item | Best practices and limitations  
---|---  
Excluded services |  Don't use the following services, which aren't supported by the BAA:

  * Any third-party services (including [Excluded services](https://cloud.google.com/terms/looker/privacy/lookeroriginal-subprocessors)) other than services provided by a Google affiliate or a cloud-based infrastructure provider. 
  * Any API integration tool that isn't secure. 

  
Access controls |  Consider the following when implementing access controls:

  * Use the `access filter` parameter with user attributes to apply row, column, or field level data security by user or user group.
  * Minimize data access for your users by limiting administrator, developer, and SQL runner access privileges. 
  * Create a process that helps prevent sharing of PHI with excluded services and Google personnel, including technical support teams using support access or professional services teams during an engagement. 
  * Set up API usage between Google and your vendor or other third parties in a secure way. 

  
Data sharing |  Consider the following when sharing data:

  * Don't share PHI or instruct Google to share PHI with a third party unless a BAA is in place with the third party. 
  * Don't share PHI using email. Configure Looker to redirect email recipients to the Looker instance where the recipients must log in to access PHI or related sensitive content. 
  * Create processes that help ensure PHI isn't attached to or sent using any technical support chat functionality. 
  * Store cache query results for only the minimum time necessary for the datasets and use cases. 
  * Restrict when users can create public links. 
  * Create and maintain logs when you permit a third party to use aggregated PHI. 

  
Secure configuration |  Consider the following when configuring security:

  * Implement industry-standard methods of authenticating users such as two-factor authentication or SAML-supported SSO. If a user uses SSO, restrict the `login_special_email` permission to a maximum of two users. 
  * Apply dataset security in the Looker model. 
  * At least quarterly, audit all users, groups, permissions, roles, API keys, public links, and additional access controls, sharing, and security configuration. 

  
Database security controls |  Consider the following when configuring database security controls:

  * When granting access to your databases, follow the principle of least privilege to the database and its information. 
  * Ensure that all connections to the database are encrypted in transit and use a tunnel server for any SSH tunnel connection. 
  * Use an allow list to restrict external access to permit only Google-specific IP addresses. 
  * Configure your database rights so that Google doesn't have write access or administrative access to your databases. 

  
  
## What's next

  * Learn more about Google's security in the [Google security overview](https://docs.cloud.google.com/docs/security/overview/whitepaper) and the [Google infrastructure security design overview](https://docs.cloud.google.com/docs/security/infrastructure/design).
  * Review [HHS Health Information Privacy (HIPAA)](https://www.hhs.gov/hipaa/).
  * Review the [HHS guidance on HIPAA compliance and cloud computing](https://www.hhs.gov/hipaa/for-professionals/special-topics/cloud-computing/index.html).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
