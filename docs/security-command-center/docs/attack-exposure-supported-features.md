---
url: https://docs.cloud.google.com/security-command-center/docs/attack-exposure-supported-features/
title: Risk Engine feature support \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:39:34.624978+00:00
---

# Risk Engine feature support  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/attack-exposure-supported-features/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Risk Engine feature support Stay organized with collections  Save and categorize content based on your preferences. 

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (requires [organization-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation)) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This page describes the services and findings that the Security Command Center Risk Engine feature supports and the supportability limits it is subject to.

Risk Engine generates attack exposure scores and attack path simulations for the following:

  * Supported finding categories in the `External exposure` ([Preview](https://cloud.google.com/products/#product-launch-stages)), `Misconfiguration`, and `Vulnerability` [finding classes](https://docs.cloud.google.com/security-command-center/docs/finding-classes).
  * `Toxic combination` class findings.
  * `Chokepoint` class findings.
  * Resource instances of supported resource types that you designate as high value. For more information, see Resource types supported in high-value resource sets.



Security Command Center can provide attack exposure scores and attack path visualizations for multiple cloud service provider platforms. Detector support differs for each cloud service provider. Risk Engine depends on external exposure, vulnerability, and misconfiguration detectors that are specific to each cloud service provider. The following sections describe the supported resources for each cloud service provider.

  * Google Cloud
  * Amazon Web Services (AWS)
  * Microsoft Azure



## Organization-level support only

The attack path simulations that Risk Engine uses to generate the attack exposure scores and attack paths require Security Command Center to be activated at the [organization level](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation). Attack path simulations are not supported with [project-level activations](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#project-level-activation-overview) of Security Command Center.

To view attack paths, your Google Cloud console view must be set to your organization. If you select a project or folder view in the Google Cloud console, you can see attack exposure scores, but you cannot see the attack paths.

## Required roles

Attack paths are associated with specific components of Security Command Center, like findings and high-value resources. To view Security Command Center attack paths, you must have the correct IAM roles to let you view each of your Security Command Center resources.

To get the permissions that you need to view attack paths, ask your administrator to grant you the following IAM roles on your organization: 

  * [Security Center Attack Paths Reader ](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.attackPathsViewer) (`roles/securitycenter.attackPathsViewer`)
  * View attack paths generated from findings and issues (for example, toxic combinations and chokepoints): [Security Center Findings Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.findingsViewer) (`roles/securitycenter.findingsViewer`) 
  * Allow access to attack paths for high-value resources: 
    * [Security Center Assets Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.assetsViewer) (`roles/securitycenter.assetsViewer`)
    * [Security Center Valued Resources Reader ](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.valuedResourcesViewer) (`roles/securitycenter.valuedResourcesViewer`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Size limits for organizations

For attack path simulations, Risk Engine limits the number of active assets and active findings that an organization can contain.

If an organization exceeds the limits shown in the following table, attack path simulations don't run.

Type of limit  | Usage limit  
---|---  
Maximum number of active findings | 250,000,000  
Maximum number of active assets | 26,000,000  
  
If the assets, findings, or both in your organization are approaching these limits or exceed them, contact Cloud Customer Care to request an evaluation of your organization for a possible increase.

## High-value resource set limits

A high-value resource set supports only certain resource types and can contain only a certain number of resource instances.

  * A high-value resource set for a cloud service provider platform can contain up to 1,000 resource instances.

  * You can create up to 100 resource value configurations per organization on Google Cloud.




## User interface support

You can work with attack exposure scores in either the Google Cloud console, the Security Operations console, or the Security Command Center API.

You can work with attack exposure scores and attack paths for toxic combination cases in the Security Operations console only.

You can create resource value configurations either on the **Attack path simulations** tab of the Security Command Center **Settings** page in the Google Cloud console, or through the [Security Command Center API](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1/organizations.resourceValueConfigs).

## Google Cloud support

The following sections describe Risk Engine support for Google Cloud.

### Google Cloud services supported by Risk Engine

The simulations that Risk Engine runs can include the following Google Cloud services:

  * Artifact Registry
  * BigQuery
  * Cloud Build
  * Cloud Run
  * Cloud Run functions
  * Managed Service for Apache Spark
  * Cloud Key Management Service
  * Cloud Load Balancing
  * Cloud NAT
  * Cloud Router
  * Cloud SQL
  * Cloud Storage
  * Compute Engine
  * Google Kubernetes Engine
  * Identity and Access Management
  * Resource Manager
  * Gemini Enterprise Agent Platform
  * Virtual Private Cloud, including subnets, firewall configurations and service control perimeters



### Google Cloud resource types supported in high-value resource sets

You can add only the following types of Google Cloud resources to a high-value resource set:

  * `aiplatform.googleapis.com/Dataset`
  * `aiplatform.googleapis.com/Featurestore`
  * `aiplatform.googleapis.com/MetadataStore`
  * `aiplatform.googleapis.com/Model`
  * `aiplatform.googleapis.com/ReasoningEngine`
  * `aiplatform.googleapis.com/TrainingPipeline`
  * `artifactregistry.googleapis.com/Repository`
  * `bigquery.googleapis.com/Dataset`
  * `cloudbuild.googleapis.com/BitbucketServerConfig`
  * `cloudbuild.googleapis.com/BuildTrigger`
  * `cloudbuild.googleapis.com/Connection`
  * `cloudbuild.googleapis.com/GithubEnterpriseConfig`
  * `cloudbuild.googleapis.com/Repository`
  * `cloudbuild.googleapis.com/WorkerPool`
  * `cloudfunctions.googleapis.com/CloudFunction`
  * `compute.googleapis.com/Instance`
  * `container.googleapis.com/Cluster`
  * `dataproc.googleapis.com/Cluster`
  * `dataproc.googleapis.com/Job`
  * `run.googleapis.com/Job`
  * `run.googleapis.com/Service`
  * `spanner.googleapis.com/Instance`
  * `sqladmin.googleapis.com/Instance`
  * `storage.googleapis.com/Bucket`



### Google Cloud resource types supported with data-sensitivity classifications

Attack path simulations can automatically set priority values based on data-sensitivity classifications from [Sensitive Data Protection discovery](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles) for only the following data resource types:

  * `aiplatform.googleapis.com/Dataset`
  * `bigquery.googleapis.com/Dataset`
  * `sqladmin.googleapis.com/Instance`
  * `storage.googleapis.com/Bucket`



### Supported finding categories

Attack path simulations generate attack exposure scores and attack paths for only the Security Command Center finding categories from the Security Command Center detection services that are listed in this section.

#### Risk Engine findings

The toxic combination and chokepoint findings categories that are generated by Risk Engine support attack exposure scores.

#### External Exposure findings

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Attack path simulations support the `EXTERNALLY_EXPOSED_VM_INSTANCE` [External Exposure finding category](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#external-exposure-findings), which identifies Compute Engine or GKE resources with a direct public IP address that allows host OS access. For more information about this service, see [Detect exposed resources](https://docs.cloud.google.com/security-command-center/docs/detect-external-exposure).

#### Vulnerability Assessment for Google Cloud findings

Attack path simulations support the following [Vulnerability Assessment for Google Cloud](https://docs.cloud.google.com/security-command-center/docs/vulnerability-assessment-google-cloud) finding categories:

  * `GCE OS vulnerability`
  * `GCE Software vulnerability`
  * `GKE OS vulnerability`
  * `GKE Software vulnerability`



#### GKE Security Posture findings

Attach path simulations support the following [GKE Security Posture](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#gke-security-posture-dashboard) finding categories:

  * `GKE runtime OS vulnerability`



#### Mandiant Attack Surface Management findings

Attack path simulations support the following [Mandiant Attack Surface Management](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#vulnerabilities) finding categories:

  * `Software vulnerability`



#### VM Manager findings

The `OS Vulnerability` finding category that is generated by [VM Manager](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#vm_manager) supports attack exposure scores.

### Pub/Sub notification support

Changes to attack exposure scores cannot be used as a trigger for notifications to Pub/Sub.

Also, findings sent to Pub/Sub when the findings are created don't include an attack exposure score because they are sent before a score can be calculated.

## AWS support

Security Command Center can calculate attack exposure scores and attack path visualizations for your resources on AWS.

### AWS services supported by Risk Engine

The simulations can include the following AWS services:

  * Identity and Access Management (IAM)
  * Security Token Service (STS)
  * Simple Storage Service (S3)
  * Web Application Firewall (WAFv2)
  * Elastic Compute Cloud (EC2)
  * Elastic Load Balancing (ELB & ELBv2)
  * Relational Database Service (RDS)
  * Key Management Service (KMS)
  * Elastic Container Registry (ECR)
  * Elastic Container Service (ECS)
  * ApiGateway & ApiGatewayv2
  * Organizations (Account Management Service)
  * CloudFront
  * AutoScaling
  * Lambda
  * DynamoDB



### AWS resource types supported in high-value resource sets

You can add only the following types of AWS resources to a high-value resource set:

  * DynamoDB table
  * EC2 instance
  * Lambda function
  * RDS DBCluster
  * RDS DBInstance
  * S3 bucket



### AWS resource types supported with data-sensitivity classifications

Attack path simulations can automatically set priority values based on data-sensitivity classifications from [Sensitive Data Protection discovery](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles) for only the following AWS data resource types:

  * Amazon S3 bucket



### Finding support in Security Health Analytics for AWS

Risk Engine provides scores and attack path visualizations for the following Security Health Analytics finding categories:

  * Access keys rotated 90 days less
  * Credentials unused 45 days greater disabled
  * Default security group VPC restricts all traffic
  * EC2 instance no public IP
  * IAM password policy
  * IAM password policy prevents password reuse
  * IAM password policy requires minimum length 14 greater
  * IAM user unused credentials check
  * IAM users receive permissions groups
  * KMS cmk not scheduled for deletion
  * MFA delete enabled S3 buckets
  * MFA enabled root user account
  * Multi factor authentication MFA enabled all IAM users console
  * No root user account access key exists
  * No security groups allow ingress 0 remote server administration
  * No security groups allow ingress 0 0 0 0 remote server administration
  * One active access key available any single IAM user
  * Public access given RDS instance
  * Restricted common ports
  * Restricted SSH
  * Rotation customer created CMKS enabled
  * Rotation customer created symmetric CMKS enabled
  * S3 buckets configured block public access bucket settings
  * S3 bucket policy set deny HTTP requests
  * S3 default encryption KMS
  * VPC default security group closed



### Vulnerability Assessment for Amazon Web Services findings

The `Software vulnerability` finding category that is generated by [EC2 Vulnerability Assessment](https://docs.cloud.google.com/security-command-center/docs/vulnerability-assessment-aws-overview) supports attack exposure scores.

## Azure support

Risk Engine can generate attack exposure scores and attack path visualizations for your resources on Microsoft Azure.

After you [establish a connection to Azure](https://docs.cloud.google.com/security-command-center/docs/connect-scc-to-azure), you can designate Azure high-value resources by creating resource value configurations, as you would for resources on Google Cloud and AWS. For instructions, see section [Define and manage your high-value resource set](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-define-high-value-resource-set).

Before you create your first resource value configuration for Azure, Security Command Center uses a default high-value resource set that is specific to the cloud service provider.

Security Command Center runs simulations for a cloud platform that are independent of simulations run for other cloud platforms.

### Azure services supported by Risk Engine

The attack path simulations can include the following Azure services:

  * App Service
  * Azure Kubernetes Service (AKS)
  * Virtual Network
  * Container Registry
  * Cosmos DB
  * Functions
  * Key Vault
  * MySQL database
  * Network security groups
  * PostgreSQL database
  * Role-Based Access Control (RBAC)
  * Service Bus
  * SQL Database
  * Storage Account
  * Virtual Machine Scale Sets
  * Virtual Machines



### Azure resource types you can specify in high-value resource sets

You can add only the following types of Azure resources to a high-value resource set:

  * Microsoft.Compute/virtualMachines 
    * Linux VM
    * Windows VM
  * Microsoft.ContainerService/managedClusters 
    * Kubernetes Cluster
  * Microsoft.DBforMySQL/flexibleServers/databases 
    * MySQL Database
  * Microsoft.DBforPostgreSQL/flexibleServers/databases 
    * PostgreSQL Database
  * Microsoft.DocumentDB/databaseAccounts 
    * Cosmos DB Account
  * Microsoft.Sql/servers/databases 
    * SQL Database
  * Microsoft.Storage/storageAccounts 
    * Storage Account
  * Microsoft.Web/sites 
    * App Service
    * Function App



### Azure resources included in the default high-value resource set

The following are resources included in the default high-value resource set:

  * Microsoft.Compute/virtualMachines 
    * Linux VM
    * Windows VM
  * Microsoft.DBforPostgreSQL/flexibleServers/databases 
    * PostgreSQL Database
  * Microsoft.DBforMySQL/flexibleServers/databases 
    * MySQL Database
  * Microsoft.DocumentDB/databaseAccounts 
    * Cosmos DB Account
  * Microsoft.Sql/servers/databases 
    * SQL Database
  * Microsoft.Storage/storageAccounts 
    * Storage Account
  * Microsoft.Web/sites 
    * App Service
    * Function App



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
