---
url: https://docs.cloud.google.com/architecture/blueprints/deploy_enterprise_data_mesh/
title: Deploy an enterprise data management and analytics platform \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:38:11.055218+00:00
---

# Deploy an enterprise data management and analytics platform  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/blueprints/deploy_enterprise_data_mesh/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Deploy an enterprise data management and analytics platform Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2025-04-04 UTC

An enterprise data management and analytics platform provides an enclave where you can store, analyze, and manipulate sensitive information while maintaining security controls. You can use the _enterprise data mesh architecture_ to deploy a platform on Google Cloud for data management and analytics. The architecture is designed to work in a hybrid environment, where Google Cloud components interact with your existing on-premises components and operating processes.

The enterprise data mesh architecture includes the following:

  * A [GitHub repository](https://github.com/googlecloudplatform/terraform-google-enterprise-datamesh) that contains a set of Terraform configurations, scripts, and code to build the following: 
    * A governance project that lets you use Google's [implementation of the Cloud Data Management Capabilities (CDMS) Key Controls Framework](https://docs.cloud.google.com/docs/security/implement-cdmc-framework).
    * A data platform example that supports interactive and production workflows.
    * A producer environment within the data platform that supports multiple data domains. Data domains are logical groupings of data elements.
    * A consumer environment within the data platform that supports multiple consumer projects.
    * A data transfer service that uses Workload Identity Federation and the [Tink](https://developers.google.com/tink) encryption library to help you transfer data into Google Cloud in a secure manner.
    * A data domain example that contains ingestion, non-confidential, and confidential projects.
    * An example of a data access system that lets data consumers request access to data sets and data owners grant access to those data sets. The example also includes a workflow manager that changes the IAM permissions of those data sets accordingly.
  * A guide to the architecture, design, security controls, and operational processes that you use this architecture to implement (this document).



The enterprise data mesh architecture is designed to be compatible with the [enterprise foundations blueprint](https://docs.cloud.google.com/architecture/blueprints/security-foundations). The enterprise foundations blueprint provides a number of base-level services that this architecture relies on, such as [VPC networks](https://docs.cloud.google.com/vpc/docs/vpc) and logging. You can deploy this architecture without deploying the enterprise foundations blueprint if your Google Cloud environment provides the [necessary functionality](https://docs.cloud.google.com/architecture/blueprints/security-foundations/summary).

This document is intended for cloud architects, data scientists, data engineers, and security architects who can use the architecture to build and deploy comprehensive data services on Google Cloud. This document assumes that you are familiar with the concepts of [data meshes](https://docs.cloud.google.com/architecture/data-mesh), Google Cloud data services, and the Google Cloud implementation of the CDMC framework.

## Architecture

The enterprise data mesh architecture takes a layered approach to provide the capabilities that enable data ingestion, data processing, and governance. The architecture is intended to be deployed and controlled through a CI/CD workflow. The following diagram shows how the data layer that is deployed by this architecture relates to other layers in your environment.

![Data mesh architecture.](https://docs.cloud.google.com/static/architecture/images/data-mesh-architecture/data-mesh-architecture.svg)

This diagram includes the following:

  * [Google Cloud infrastructure](https://cloud.google.com/infrastructure) provides security capabilities such as [encryption at rest](https://docs.cloud.google.com/docs/security/encryption/default-encryption) and [encryption in transit](https://docs.cloud.google.com/docs/security/encryption-in-transit), as well as basic building blocks such as compute and storage.
  * The enterprise foundation provides a baseline of resources such as identity, networking, logging, monitoring, and deployment systems that enable you to adopt Google Cloud for your data workloads.
  * The data layer provides various capabilities such as data ingestion, data storage, data access control, data governance, data monitoring, and data sharing.
  * The application layer represents various different applications that use the data layer assets.
  * CI/CD provides the tools to automate the provision, configuration, management, and deployment of infrastructure, workflows, and software components. These components help you ensure consistent, reliable, and auditable deployments; minimize manual errors; and accelerate the overall development cycle.



To show how the data environment is used, the architecture includes a sample data workflow. The sample data workflow takes you through the following processes: data governance, data ingestion, data processing, data sharing, and data consumption.

### Key architectural decisions

The following table summarizes the high-level decisions of the architecture.

Decision area | Decision  
---|---  
**Google Cloud architecture**  
Resource hierarchy | The architecture uses the [resource hierarchy](https://docs.cloud.google.com/architecture/blueprints/security-foundations/organization-structure) from the enterprise foundations blueprint.  
Networking | The architecture includes an example data transfer service that uses [Workload Identity Federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation) and a Tink library.  
Roles and IAM permissions | The architecture includes segmented data producer roles, data consumer roles, data governance roles, and data platform roles.  
**Common data services**  
Metadata | The architecture uses Knowledge Catalog to manage data metadata.  
Central policy management | To manage policies, the architecture uses Google Cloud's implementation of the CDMC framework.  
Data access management | To control access to data, the architecture includes an independent process that requires data consumers to request access to data assets from the data owner.  
Data quality | The architecture uses the [Cloud Data Quality Engine](https://github.com/GoogleCloudPlatform/cloud-data-quality) to define and run data quality rules on specified table columns, measuring data quality based on metrics like correctness and completeness.  
Data security | The architecture uses tagging, encryption, masking, tokenization, and IAM controls to provide data security.  
**Data domain**  
Data environments | The architecture includes three environments. Two environments (non-production and production) are operational environments that are driven by pipelines. One environment (development) is an interactive environment.  
Data owners | Data owners ingest, process, expose, and grant access to data assets.  
Data consumers | Data consumers request access to data assets.  
**Onboarding and operations**  
Pipelines | The architecture uses the following pipelines to deploy resources:

  * Foundation pipeline
  * Infrastructure pipeline
  * Artifact pipelines
  * Service Catalog pipeline

  
Repositories | Each pipeline uses a separate repository to enable segregation of responsibility.  
Process flow | The process requires that changes to the production environment include a submitter and an approver.  
**Cloud operations** |   
Data product scorecards | The [Report Engine](https://github.com/GoogleCloudPlatform/cdmc/blob/main/report-engine/README.md) generates data product scorecards.  
Cloud Logging | The architecture uses the [logging infrastructure](https://docs.cloud.google.com/architecture/blueprints/security-foundations/detective-controls#centralized-logging) from the enterprise foundations blueprint.  
Cloud Monitoring | The architecture uses the monitoring infrastructure from the enterprise foundations blueprint.  
  
### Identity: Mapping roles to groups

The data mesh leverages the enterprise foundations blueprint's existing identity lifecycle management, authorization, and authentication architecture. Users are not assigned roles directly; instead groups are the primary method of assigning roles and permission in IAM. IAM roles and permissions are assigned during project creation through the foundation pipeline.

The data mesh associates groups with one of four key areas: [infrastructure](https://docs.cloud.google.com/architecture/data-mesh#central_self-service_data_infrastructure_platform_team), [data governance](https://docs.cloud.google.com/architecture/data-mesh#central_data_governance_team), [domain-based data producers](https://docs.cloud.google.com/architecture/data-mesh#data_domain-based_producer_team), and [domain-based consumers](https://docs.cloud.google.com/architecture/data-mesh#data_domain-based_consumer_teams).

The permission scopes for these groups are the following:

  * The infrastructure group's permission scope is the data mesh as a whole.
  * The data governance groups' permission scope is the data governance project.
  * Domain-based producers and consumers permissions are scoped to their data domain.



The following tables show the various roles used in this data mesh implementation and their associated permissions.

#### Infrastructure

Group | Description | Roles  
---|---|---  
`data-mesh-ops@example.com` | Overall administrators of the data mesh | `roles/owner` (data platform)  
  
#### Data governance

Group | Description | Roles  
---|---|---  
`gcp-dm-governance-admins@example.com` | Administrators of the data governance project | `roles/owner` on the data governance project  
`gcp-dm-governance-developers@example.com` | Developers who build and maintain the data governance components | Multiple roles on the data governance project, including `roles/viewer`, BigQuery roles, and Knowledge Catalog roles  
`gcp-dm-governance-data-readers@example.com` | Readers of data governance information | `roles/viewer`  
`gcp-dm-governance-security-administrator@example.com` | Security administrators of the governance project | `roles/orgpolicy.policyAdmin` and `roles/iam.securityReviewer`  
`gcp-dm-governance-tag-template-users@example.com` | Group with permission to use aspect types | `roles/dataplex.aspectTypeUser`  
`gcp-dm-governance-tag-users@example.com` | Group with permission to use aspect types and add aspects | `roles/dataplex.aspectTypeUser` and `roles/dataplex.catalogEditor`  
`gcp-dm-governance-scc-notifications@example.com` | Service account group for Security Command Center notifications | None. This is a group for membership, and a service account is created with this name, which has the necessary permissions.  
  
#### Domain-based data producers

Group | Description | Roles  
---|---|---  
`gcp-dm-{data_domain_name}-admins@example.com` | Administrators of a specific data domain | `roles/owner` on the data domain project  
`gcp-dm-{data_domain_name}-developers@example.com` | Developers who build and maintain data products within a data domain | Multiple roles on the data domain project, including `roles/viewer`, BigQuery roles, and Cloud Storage roles  
`gcp-dm-{data_domain_name}-data-readers@example.com` | Readers of the data domain information | `roles/viewer`  
`gcp-dm-{data_domain_name}-metadata-editors@{var.domain}` | Editors of Knowledge Catalog entries | Roles to edit Knowledge Catalog entries  
`gcp-dm-{data_domain_name}-data-stewards@example.com` | Data stewards for the data domain | Roles to manage metadata and data governance aspects  
  
#### Domain-based data consumers

Group | Description | Roles  
---|---|---  
`gcp-dm-consumer-{project_name}-admins@example.com` | Administrators of a specific consumer project | `roles/owner` on consumer project  
`gcp-dm-consumer-{project_name}-developers@example.com` | Developers working within a consumer project | Multiple roles on the consumer project, including `roles/viewer` and BigQuery roles  
`gcp-dm-consumer-{project_name}-data-readers@example.com` | Readers of the consumer project information | `roles/viewer`  
  
## Organization structure

To differentiate between production operations and production data, the architecture uses different environments to develop and release workflows. Production operations include the governance, traceability, and repeatability of a workflow and the auditability of the results of the workflow. Production data refers to possibly sensitive data that you need to run your organization. All environments are designed to have security controls that let you ingest and operate your data.

To help data scientists and engineers, the architecture includes an interactive environment, where developers can work with the environment directly and add services through a curated catalog of solutions. Operational environments are driven through pipelines which have codified architecture and configuration.

This architecture uses the organizational structure of the enterprise foundations blueprint as a basis for deploying data workloads. The following diagram shows the top-level folders and projects used in the enterprise data mesh architecture.

![Data mesh organization structure.](https://docs.cloud.google.com/static/architecture/images/data-mesh-architecture/data-mesh-org-structure.svg)

The following table describes the top-level folders and projects that are part of the architecture.

Folder | Component | Description  
---|---|---  
`common` | `prj-c-artifact-pipeline` | Contains the deployment pipeline that's used to build out the code artifacts of the architecture.  
| `prj-c-service-catalog` | Contains the infrastructure used by the Service Catalog to deploy resources in the interactive environment.  
| `prj-c-datagovernance` | Contains all the resources used by Google Cloud's implementation of the CDMC framework.  
`development` | `fldr-d-dataplatform` | Contains the projects and resources of the data platform for developing use cases in interactive mode.  
`non-production` | `fldr-n-dataplatform` | Contains the projects and resources of the data platform for testing use cases that you want to deploy in an operational environment.  
`production` | `fldr-p-dataplatform` | Contains the projects and resources of the data platform for deployment into production.  
  
### Data platform folder

The data platform folder contains all the data plane components and some of the CDMC resources. In addition, the data platform folder and the data governance project contain the CDMC resources. The following diagram shows the folders and projects that are deployed in the data platform folder.

![The data platform folder](https://docs.cloud.google.com/static/architecture/images/data-mesh-architecture/data-mesh-data-platform.svg)

Each data platform folder includes an environment folder (production, non-production, and development). The following table describes the folders within each data platform folder.

Folders | Description  
---|---  
Producers | Contains the data domains.  
Consumers | Contains the consumer projects.  
Data domain | Contains the projects associated with a particular domain.  
  
### Producers folder

Each producers folder includes one or more data domains. A data domain refers to a logical grouping of data elements that share a common meaning, purpose, or business context. Data domains let you categorize and organize data assets within an organization. The following diagram shows the structure of a data domain. The architecture deploys projects in the data platform folder for each environment.

![The producers folder.](https://docs.cloud.google.com/static/architecture/images/data-mesh-architecture/data-mesh-producers.svg)

The following table describes the projects that are deployed in the data platform folder for each environment.

Project | Description  
---|---  
Ingestion | The ingestion project ingests data into the data domain. The architecture provides examples of how you can stream data into BigQuery, Cloud Storage, and Pub/Sub. The ingestion project also contains examples of Dataflow and Managed Service for Apache Airflow that you can use to orchestrate the transformation and movement of ingested data.  
Non-confidential | The non-confidential project contains data that has been de-identified. You can mask, containerize, encrypt, tokenize, or obfuscate data. Use policy tags to control how the data is presented.  
Confidential | The confidential project contains plaintext data. You can control access through IAM permissions.  
  
### Consumer folder

The consumer folder contains consumer projects. Consumer projects provide a mechanism to segment data users based on their required trust boundary. Each project is assigned to a separate user group and the group is assigned access to the required data assets on a project-by-project basis. You can use the consumer project to collect, analyze, and augment the data for the group.

### Common folder

The common folder contains the services that are used by different environments and projects. This section describes the capabilities that are added to the common folder to enable the enterprise data mesh.

#### CDMC architecture

The architecture uses the CDMC architecture for data governance. The data governance functions reside in the data governance project in the common folder. The following diagram shows the components of the CDMC architecture. The numbers in the diagram represent the key controls that are addressed with Google Cloud services.

![The CDMC architecture.](https://docs.cloud.google.com/static/docs/security/images/cdmc/cdmc-architecture.svg)

The following table describes the components of the CDMC architecture that the enterprise data mesh architecture uses.

CDMC component | Google Cloud service | Description  
---|---|---  
**Access and lifecycle components**  
Key management | Cloud KMS | A service that securely manages encryption keys that protect sensitive data.  
Record Manager | Cloud Run | An application that maintains comprehensive logs and records of data processing activities, ensuring organizations can track and audit data usage.  
Archiving policy | BigQuery | A BigQuery table that contains the storage policy for data.  
Entitlements | BigQuery | A BigQuery table that stores information about who can access sensitive data. This table ensures that only authorized users can access specific data based on their roles and privileges.  
**Scanning components**  
Data loss | Sensitive Data Protection | Service used to inspect assets for sensitive data.  
DLP findings | BigQuery | A BigQuery table that catalogs data classifications within the data platform.  
Policies | BigQuery | A BigQuery table that contains consistent data governance practices (for example, data access types).  
Billing export | BigQuery | A table that stores cost information that is [exported from Cloud Billing](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery#setup) to enable the analysis of cost metrics that are associated with data assets.  
Cloud Data Quality Engine | Cloud Run | An application that runs data quality checks for tables and columns.  
Data quality findings | BigQuery | A BigQuery table that records identified discrepancies between the defined data quality rules and the actual quality of the data assets.  
**Reporting components**  
Scheduler | Cloud Scheduler | A service that controls when the Cloud Data Quality Engine runs and when the Sensitive Data Protection inspection occurs.  
Report Engine | Cloud Run | An application that generates reports that help track and measure adherence to the CDMC framework's controls.  
Findings and assets | BigQuery and Pub/Sub | A BigQuery report of discrepancies or inconsistencies in data management controls, such as missing aspects, incorrect classifications, or non-compliant storage locations.  
Tag exports | BigQuery | A BigQuery table that contains extracted aspect information from Knowledge Catalog.  
**Other components**  
Policy management | Organization Policy Service | A service that defines and enforces restrictions on where data can be stored geographically.  
Attribute-based access policies | Access Context Manager | A service that defines and enforces granular, attribute-based access policies so that only authorized users from permitted locations and devices can access sensitive information.  
Metadata | Knowledge Catalog | A service that stores metadata information about the tables that are in use in the data mesh.  
Tag Engine | Cloud Run | An application that adds aspects to BigQuery table entries in Knowledge Catalog.  
CDMC reports | Data Studio | Dashboards that let your analysts view reports that were generated by the CDMC architecture engines.  
  
#### CDMC implementation

The following table describes how the architecture implements the key controls in the CDMC framework.

CDMC control requirement | Implementation  
---|---  
[Data control compliance](https://docs.cloud.google.com/docs/security/implement-cdmc-framework#control-1) | The Report Engine detects non-compliant data assets through and publishes findings to a Pub/Sub topic. These findings are also loaded into BigQuery for reporting using Data Studio.  
[Data ownership is established for both migrated and cloud-generated data](https://docs.cloud.google.com/docs/security/implement-cdmc-framework#2_data_ownership_is_established_for_both_migrated_and_cloud-generated_data) | Knowledge Catalog automatically captures technical metadata from BigQuery. Tag Engine applies business metadata aspects like owner name and sensitivity level from a reference table, which helps ensure that all sensitive data is annotated with owner information for compliance. This automated process helps provide data governance and compliance by identifying and labeling sensitive data with the appropriate owner information.  
[Data sourcing and consumption are governed and supported by automation](https://docs.cloud.google.com/docs/security/implement-cdmc-framework#3_data_sourcing_and_consumption_are_governed_and_supported_by_automation) | Knowledge Catalog classifies data assets by annotating them with an aspect that includes an `is_authoritative` flag when they are an authoritative source. Knowledge Catalog automatically stores the information, along with the technical metadata, in a data register. The Report Engine and the Tag Engine can validate and report the data register of authoritative sources using Pub/Sub.  
[Data sovereignty and cross-border data movement are managed](https://docs.cloud.google.com/docs/security/implement-cdmc-framework#4_data_sovereignty_and_cross-border_data_movement_are_managed) | [Organization Policy Service](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview) defines permitted storage regions for data assets and [Access Context Manager](https://docs.cloud.google.com/access-context-manager/docs/overview) restricts access based on user location. Knowledge Catalog stores the approved storage locations as metadata aspects. Report Engine compares these aspects against the actual location of the data assets in BigQuery and publishes any discrepancies as findings using Pub/Sub. Security Command Center provides an additional layer of monitoring by generating vulnerability findings if data is stored or accessed outside the defined policies.  
[Data catalogs are implemented, used, and interoperable](https://docs.cloud.google.com/docs/security/implement-cdmc-framework#5_data_catalogs_are_implemented_used_and_interoperable) | Knowledge Catalog stores and updates the technical metadata for all BigQuery data assets, effectively creating a continuously synchronized data catalog. Knowledge Catalog ensures that any new or modified tables and views are immediately added to the catalog, maintaining an up-to-date inventory of data assets.  
[Data classifications are defined and used](https://docs.cloud.google.com/docs/security/implement-cdmc-framework#control-6) | [Sensitive Data Protection](https://docs.cloud.google.com/sensitive-data-protection/docs) inspects BigQuery data and identifies sensitive information types. These findings are then ranked based on a classification reference table, and the highest sensitivity level is assigned as an aspect in Knowledge Catalog at the column and table levels. Tag Engine manages this process by updating Knowledge Catalog with sensitivity aspects whenever new data assets are added or existing ones are modified. This process ensures a constantly updated classification of data based on sensitivity, which you can monitor and report on using Pub/Sub and integrated reporting tools.  
[Data entitlements are managed, enforced, and tracked](https://docs.cloud.google.com/docs/security/implement-cdmc-framework#7_data_entitlements_are_managed_enforced_and_tracked) | BigQuery [policy tags](https://docs.cloud.google.com/bigquery/docs/column-level-security-intro) control access to sensitive data at the column level, ensuring only authorized users can access specific data based on their assigned policy tag. IAM manages overall access to the data warehouse, while Knowledge Catalog stores sensitivity classifications. Regular checks are performed to ensure all sensitive data has corresponding policy tags, with any discrepancies reported using Pub/Sub for remediation.  
[Ethical access, use, and outcomes of data are managed](https://docs.cloud.google.com/docs/security/implement-cdmc-framework#8_ethical_access_use_and_outcomes_of_data_are_managed) | Data sharing agreements for both providers and consumers are stored in a dedicated BigQuery data warehouse to control consumption purposes. Knowledge Catalog labels data assets with the provider agreement information, while consumer agreements are linked to IAM bindings for access control. Query labels enforce consumption purposes, requiring consumers to specify a valid purpose when querying sensitive data, which is validated against their entitlements in BigQuery. An audit trail in BigQuery tracks all data access and ensures compliance with the data sharing agreements.  
[Data is secured, and controls are evidenced](https://docs.cloud.google.com/docs/security/implement-cdmc-framework#9_data_is_secured_and_controls_are_evidenced) | Google's default encryption at rest helps protect data that is stored on disk. Cloud KMS supports customer-managed encryption keys (CMEK) for enhanced key management. BigQuery implements column-level dynamic data masking for de-identification and supports application-level de-identification during data ingestion. Knowledge Catalog stores metadata aspects for encryption and de-identification techniques that are applied to data assets. Automated checks ensure that the encryption and de-identification methods align with predefined security policies, with any discrepancies that are reported as findings using Pub/Sub.  
[A data privacy framework is defined and operational](https://docs.cloud.google.com/docs/security/implement-cdmc-framework#10_a_data_privacy_framework_is_defined_and_operational) | Knowledge Catalog annotates sensitive data assets with aspects containing relevant information for impact assessment, such as subject location and assessment report links. Tag Engine applies these aspects based on data sensitivity and a policy table in BigQuery, which defines the assessment requirements based on data and subject residency. This automated process allows for continuous monitoring and reporting of compliance with impact assessment requirements, ensuring that data protection impact assessments (DPIAs) or protection impact assessment (PIAs) are conducted when necessary.  
[The data lifecycle is planned and managed](https://docs.cloud.google.com/docs/security/implement-cdmc-framework#11_the_data_lifecycle_is_planned_and_managed) | Knowledge Catalog labels data assets with retention policies, specifying retention periods and expiration actions (such as archive or purge). Record Manager automates the enforcement of these policies by purging or archiving BigQuery tables based on the defined aspects. This enforcement ensures adherence to the data lifecycle policies and maintains compliance with data retention requirements, with any discrepancies detected and reported using Pub/Sub.  
[Data quality is managed](https://docs.cloud.google.com/docs/security/implement-cdmc-framework#12_data_quality_is_managed) | The Cloud Data Quality Engine defines and runs data quality rules on specified table columns, measuring data quality based on metrics like correctness and completeness. Results from these checks, including success percentages and thresholds, are stored as aspects in Knowledge Catalog. Storing these results allows for continuous monitoring and reporting of data quality, with any issues or deviations from acceptable thresholds published as findings using Pub/Sub.  
[Cost management principles are established and applied](https://docs.cloud.google.com/docs/security/implement-cdmc-framework#13_cost_management_principles_are_established_and_applied) | Knowledge Catalog stores cost-related metrics for data assets, such as query costs, storage costs, and data egress costs, which are calculated using billing information exported from Cloud Billing to BigQuery. Storing cost-related metrics allows for comprehensive cost tracking and analysis, ensuring adherence to cost policies and efficient resource utilization, with any anomalies reported using Pub/Sub.  
[Data provenance and lineage are understood](https://docs.cloud.google.com/docs/security/implement-cdmc-framework#14_data_provenance_and_lineage_are_understood) | Knowledge Catalog's built-in data lineage features track the provenance and lineage of data assets, visually representing the flow of data. Additionally, data ingestion scripts identify and record the original source of the data as an aspect in Knowledge Catalog, enhancing the traceability of data back to its origin.  
  
## Data access management

The architecture's access to data is controlled through an independent process which separates operational control (for example, running Dataflow jobs) from data access control. A user's access to a Google Cloud service is defined by an environmental or operational concern and is provisioned and approved by a cloud engineering group. A user's access to Google Cloud data assets (for example, a BigQuery table) is a privacy, regulatory, or governance concern and is subject to an access agreement between the producing and consuming parties and controlled through the following processes. The following diagram shows how data access is provisioned through the interaction of different software components.

![Data access management](https://docs.cloud.google.com/static/architecture/images/data-mesh-architecture/data-mesh-data-access.svg)

As shown in the previous diagram, onboarding of data accesses is handled by the following processes:

  * Cloud data assets are collected and inventoried by Knowledge Catalog.
  * The workflow manager retrieves the data assets from Knowledge Catalog.
  * Data owners are onboarded to workflow manager.



The operation of the data access management is as follows:

  1. A data consumer makes a request for a specific asset.
  2. The data owner of the asset is alerted to the request.
  3. The data owner approves or rejects the request.
  4. If the request is approved, the workflow manager passes the group, asset, and associated tag to the IAM mapper.
  5. The IAM mapper translates the workflow manager tags into IAM permissions, and gives the specified group IAM permissions for the data asset.
  6. When a user wants to access the data asset, IAM evaluates access to the Google Cloud asset based on the permissions of the group.
  7. If permitted, the user accesses the data asset.



## Networking

The data security process initiates at the source application, which might reside on-premises or in another environment external to the target Google Cloud project. Before any network transfer occurs, this application uses Workload Identity Federation to securely authenticate itself to Google Cloud APIs. Using these credentials, it interacts with Cloud KMS to obtain or wrap the necessary keys and then employs the Tink library to perform initial encryption and de-identification on the sensitive data payload according to predefined templates.

After the data payload is protected, the payload must be securely transferred into the Google Cloud ingestion project. For on-premise applications, you can use Cloud Interconnect or potentially Cloud VPN. Within the Google Cloud network, use Private Service Connect to route the data towards the ingestion endpoint within the target project's VPC network. Private Service Connect lets the source application connect to Google APIs using private IP addresses, ensuring traffic isn't exposed to the internet.

The entire network path and the target ingestion services (Cloud Storage, BigQuery, and Pub/Sub) within the ingestion project are secured by a VPC Service Controls perimeter. This perimeter enforces a security boundary, ensuring that the protected data originating from the source can only be ingested into the authorized Google Cloud services within that specific project.

## Logging

This architecture uses the [Cloud Logging](https://docs.cloud.google.com/architecture/blueprints/security-foundations/detective-controls#centralized-logging) capabilities that are provided by the enterprise foundations blueprint.

## Pipelines

The enterprise data mesh architecture uses a series of pipelines to provision the infrastructure, orchestration, data sets, data pipelines, and application components. The architecture's resource deployment pipelines use Terraform as the infrastructure as code (IaC) tool and Cloud Build as the CI/CD service to deploy the Terraform configurations into the architecture environment. The following diagram shows the relationship between the pipelines.

![Pipeline relationships](https://docs.cloud.google.com/static/architecture/images/data-mesh-architecture/data-mesh-pipelines.svg)

The foundation pipeline and the infrastructure pipeline are part of the enterprise foundations blueprint. The following table describes the purpose of the pipelines and the resources that they provision.

Pipeline | Provisioned by | Resources  
---|---|---  
Foundation pipeline | Bootstrap | 

  * Data platform folder and subfolders
  * Common projects
  * Infrastructure pipeline service account
  * Cloud Build trigger for the Infrastructure pipeline
  * Shared VPC
  * VPC Service Control perimeter

  
Infrastructure pipeline | Foundation pipeline | 

  * Consumer projects
  * Service Catalog service account
  * The Cloud Build trigger for the Service Catalog pipeline
  * Artifact pipeline service account
  * The Cloud Build trigger for the artifact pipeline

  
Service Catalog pipeline | Infrastructure pipeline | 

  * Resources deployed in the Service Catalog bucket

  
Artifact pipelines | Infrastructure pipeline | Artifact pipelines produce the various containers and other components of the codebase used by the data mesh.  
  
Each pipeline has its own set of repositories that it pulls code and configuration files from. Each repository has a separation of duties where submitters and approvals of operational code deployments are the responsibilities of different groups.

### Interactive deployment through Service Catalog

Interactive environments are the development environment within the architecture and exist under the development folder. The main interface for the interactive environment is Service Catalog, which lets developers use preconfigured templates to instantiate Google services. These preconfigured templates are known as _service templates_. Service templates help you to enforce your security posture, such as making CMEK encryption mandatory, and also prevents your users from having direct access to Google APIs.

The following diagram shows the components of the interactive environment and how data scientists deploy resources.

![Interactive environment with Service Catalog.](https://docs.cloud.google.com/static/architecture/images/data-mesh-architecture/data-mesh-service-catalog.svg)

To deploy resources using the Service Catalog, the following steps occur:

  1. The MLOps engineer puts a Terraform resource template for Google Cloud into a Git repository.
  2. The Git Commit command triggers a Cloud Build pipeline.
  3. Cloud Build copies the template and any associated configuration files to Cloud Storage.
  4. The MLOps engineer sets up the Service Catalog solutions and Service Catalog manually. The engineer then shares the Service Catalog with a service project in the interactive environment.
  5. The data scientist selects a resource from the Service Catalog.
  6. Service Catalog deploys the template into the interactive environment.
  7. The resource pulls any necessary configuration scripts.
  8. The data scientist interacts with the resources.



### Artifact pipelines

The data ingestion process uses Managed Airflow and Dataflow to orchestrate the movement and transformation of data within the data domain. The artifact pipeline builds all necessary resources for data ingestion and moves the resources to the appropriate location for the services to access them. The artifact pipeline creates the container artifacts that the orchestrator uses.

## Security controls

The enterprise data mesh architecture uses a layered defense-in-depth security model that includes default Google Cloud capabilities, Google Cloud services, and security capabilities that are configured through the enterprise foundations blueprint. The following diagram shows the layering of the various security controls for the architecture.

![Security controls in the data mesh architecture.](https://docs.cloud.google.com/static/architecture/images/data-mesh-architecture/data-mesh-security-controls.svg)

The following table describes the security controls that are associated with the resources in each layer.

Layer | Resource | Security control  
---|---|---  
CDMC framework | Google Cloud CDMC implementation | Provides a governance framework that helps secure, manage and control your data assets. See [CDMC Key Controls Framework](https://docs.cloud.google.com/docs/security/implement-cdmc-framework#overview_of_the_cdmc_key_controls_framework) for more information.  
Deployment | Infrastructure pipeline | Provides a series of pipelines that deploy infrastructure, build containers, and create data pipelines. The use of pipelines allows for auditability, traceability, and repeatability.  
Artifact pipeline | Deploys various components not deployed by the infrastructure pipeline.  
Terraform templates | Builds out the system infrastructure.  
Open Policy Agent | Helps ensure that the platform conforms to selected policies.  
Network | Private Service Connect | Provides data exfiltration protections around the architecture resources at the API layer and the IP layer. Lets you communicate with Google Cloud APIs using private IP addresses so that you can avoid exposing traffic to the internet.  
VPC network with private IP addresses | Helps remove exposure to internet-facing threats.  
VPC Service Controls | Helps protect sensitive resources against data exfiltration.  
Firewall | Helps protect the VPC network against unauthorized access.  
Access management | Access Context Manager | Controls who can access what resources and helps prevent unauthorized use of your resources.  
Workload Identity Federation | Removes the need for external credentials to transfer data onto the platform from on-premises environments.  
Knowledge Catalog | Provides an index of assets available to users.  
IAM | Provides fine-grained access.  
Encryption | Cloud KMS | Lets you manage your encryption keys and secrets, and help protect your data through encryption at rest and encryption in transit.  
Secrets Manager | Provides a secret store for pipelines that are controlled by IAM.  
Encryption at rest | By default, Google Cloud encrypts data at rest.  
Encryption in transit | By default, Google Cloud encrypts [data in transit](https://docs.cloud.google.com/docs/security/encryption-in-transit).  
Detective | Security Command Center | Helps you to detect misconfigurations and malicious activity in your Google Cloud organization.  
Continuous architecture | Continually checks your Google Cloud organization against a series of OPA policies that you have defined.  
IAM Recommender | Analyzes user permissions and provides suggestions about reducing permissions to help enforce the principle of least privilege.  
Firewall Insights | Analyzes firewall rules, identifies overly-permissive firewall rules, and suggests more restrictive firewalls to help strengthen your overall security posture.  
Cloud Logging | Provides visibility into system activity and helps enable the detection of anomalies and malicious activity.  
Cloud Monitoring | Tracks key signals and events that can help identify suspicious activity.  
Preventative | Organization Policy | Lets you control and restrict actions within your Google Cloud organization.  
  
## Workflows

The following sections outline the data producer workflow and data consumer workflow, ensuring appropriate access controls based on data sensitivity and user roles.

### Data producer workflow

The following diagram shows how data is protected as it is transferred to BigQuery.

![Data producer workflow](https://docs.cloud.google.com/static/architecture/images/data-mesh-architecture/data-mesh-process-flow.svg)

The workflow for data transfer is the following:

  1. An application that is integrated with Workload Identity Federation uses Cloud KMS to decrypt a wrapped encryption key.
  2. The application uses the Tink library to de-identify or encrypt the data using a template.
  3. The application transfers data to the ingestion project in Google Cloud.
  4. The data arrives in Cloud Storage, BigQuery, or Pub/Sub.
  5. In the ingestion project, the data is decrypted or re-identified using a template.
  6. The decrypted data is encrypted or masked based on another de-identification template, then placed in the non-confidential project. Aspects and policy tags are applied by Tag Engine as appropriate.
  7. Data from the non-confidential project is transferred over to the confidential project and re-identified.



The following data access is permitted:

  * Users who have access to the confidential project can access all the raw plaintext data.
  * Users who have access to the non-confidential project can access masked, tokenized, or encrypted data based on the policy tags associated with the data and their permissions.



### Data consumer workflow

The following steps describe how a consumer can access data that is stored in BigQuery.

  1. The data consumer searches for data assets using Knowledge Catalog.
  2. After the consumer finds the assets that they are looking for, the data consumer requests access to the data assets.
  3. The data owner decides whether to provide access to the assets.
  4. If the consumer obtains access, the consumer can use a notebook and the Solution Catalog to create an environment in which they can analyze and transform the data assets.



## Bringing it all together

The [GitHub repository](https://github.com/GoogleCloudPlatform/terraform-google-enterprise-datamesh) provides you with detailed instructions on deploying the data mesh on Google Cloud after you deployed the enterprise foundation. The process to deploy the architecture involves modifying your existing infrastructure repositories and deploying new data mesh specific components.

Complete the following:

  1. Complete all prerequisites, including the following: 
     1. Install [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install), [Terraform](https://docs.cloud.google.com/docs/terraform/install-configure-terraform), [Tink](https://developers.google.com/tink/getting-started), [Java](https://www.java.com/en/download/manual.jsp), and [Go](https://go.dev/doc/install).
     2. Deploy the [enterprise foundations blueprint (v4.1)](https://github.com/terraform-google-modules/terraform-example-foundation).
     3. Maintain the following local repositories: 
        * `gcp-data-mesh-foundations`
        * `gcp-bootstrap`
        * `gcp-environments`
        * `gcp-networks`
        * `gcp-org`
        * `gcp-projects`
  2. Modify the existing foundation blueprint and then deploy the data mesh applications. For each item, complete the following: 
     1. In your target repository, check out the `Plan` branch.
     2. To add data mesh components, copy the relevant files and directories from `gcp-data-mesh-foundations` into the appropriate foundation directory. Overwrite files when required.
     3. Update the data mesh variables, roles, and settings in the Terraform files (for example, `*.tfvars` and `*.tf`). Set the GitHub tokens as environment variables.
     4. Perform the Terraform initialize, plan, and apply operations on each repository.
     5. Commit your changes, push the code to your remote repository, create pull requests and merge to your development, nonproduction, and production environments.



## What's next

  * Read about the [architecture and functions in a data mesh](https://docs.cloud.google.com/architecture/data-mesh).
  * [Import data from Google Cloud into a secured BigQuery data warehouse](https://docs.cloud.google.com/architecture/blueprints/confidential-data-warehouse-blueprint).
  * [Implement the CDMC key controls framework in a BigQuery data warehouse](https://docs.cloud.google.com/docs/security/implement-cdmc-framework).
  * Read about the [enterprise foundations blueprint](https://docs.cloud.google.com/architecture/blueprints/security-foundations).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-04-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-04-04 UTC."],[],[]] 
