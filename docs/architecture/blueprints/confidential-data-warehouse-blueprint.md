---
url: https://docs.cloud.google.com/architecture/blueprints/confidential-data-warehouse-blueprint/
title: Import data into a secured BigQuery data warehouse \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:38:11.476426+00:00
---

# Import data into a secured BigQuery data warehouse  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/blueprints/confidential-data-warehouse-blueprint/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Import data into a secured BigQuery data warehouse Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2025-06-15 UTC

Many organizations deploy data warehouses that store sensitive data so that they can analyze the data for a variety of business purposes. This document is intended for data engineers and security administrators who deploy and secure data warehouses using BigQuery. It's part of a blueprint that includes the following:

  * Two GitHub repositories ([`terraform-google-secured-data-warehouse`](https://github.com/GoogleCloudPlatform/terraform-google-secured-data-warehouse) and [`terraform-google-secured-data-warehouse-onprem-ingest`](https://github.com/GoogleCloudPlatform/terraform-google-secured-data-warehouse-onprem-ingest)) that contain Terraform configurations and scripts. The Terraform configuration sets up a Google Cloud environment in Google Cloud for a data warehouse that stores confidential data.
  * A guide to the architecture, design, and security controls of this blueprint (this document).
  * A [walkthrough](https://console.cloud.google.com/?walkthrough_id=security--secured-data-warehouse-simple-example) that deploys a sample environment.



This document discusses the following:

  * The architecture and Google Cloud services that you can use to help secure a data warehouse in a production environment.
  * Best practices for importing data into BigQuery from an external network such as an on-premises environment.
  * Best practices for data governance when creating, deploying, and operating a data warehouse in Google Cloud, including the following:

    * data [de-identification](https://docs.cloud.google.com/sensitive-data-protection/docs/classification-redaction)

    * differential handling of confidential data

    * column-level encryption

    * column-level access controls




This document assumes that you have already configured a foundational set of security controls as described in the [enterprise foundations blueprint](https://docs.cloud.google.com/architecture/security-foundations). It helps you to layer additional controls onto your existing security controls to help protect confidential data in a data warehouse.

## Data warehouse use cases

The blueprint supports the following use cases:

  * Use the [`terraform-google-secured-data-warehouse`](https://github.com/GoogleCloudPlatform/terraform-google-secured-data-warehouse) repository to import data from Google Cloud into a BigQuery data warehouse
  * Use the [`terraform-google-secured-data-warehouse-onprem-ingest`](https://github.com/GoogleCloudPlatform/terraform-google-secured-data-warehouse-onprem-ingest) repository to import data from an on-premises environment or another cloud into a BigQuery data warehouse



## Overview

Data warehouses such as [BigQuery](https://docs.cloud.google.com/bigquery/docs/introduction) let businesses analyze their business data for insights. Analysts access the business data that is stored in data warehouses to create insights. If your data warehouse includes confidential data, you must take measures to preserve the security, confidentiality, integrity, and availability of the business data while it is stored, while it is in transit, or while it is being analyzed. In this blueprint, you do the following:

  * When importing data from external data sources, encrypt your data that's located outside of Google Cloud (for example, in an on-premises environment) and import it into Google Cloud.
  * Configure controls that help secure access to confidential data.
  * Configure controls that help secure the data pipeline.
  * Configure an appropriate separation of duties for different personas.
  * When importing data from other sources located in Google Cloud (also known as _internal data sources_), set up templates to find and de-identify confidential data.
  * Set up appropriate security controls and logging to help protect confidential data.
  * Use data classification, policy tags, dynamic data masking, and column-level encryption to restrict access to specific columns in the data warehouse.



## Architecture

To create a confidential data warehouse, you need to import data securely and then store the data in a VPC Service Controls perimeter.

### Architecture when importing data from Google Cloud

The following image shows how ingested data is categorized, de-identified, and stored when you import source data from Google Cloud using the `terraform-google-secured-data-warehouse` repository. It also shows how you can re-identify confidential data on demand for analysis.

![The sensitive data warehouse architecture for internal sources.](https://docs.cloud.google.com/static/architecture/blueprints/images/confidential-data-warehouse-blueprint/sdwv1-architecture.svg)

### Architecture when importing data from external sources

The following image shows how data is ingested and stored when you import data from an on-premises environment or another cloud into a BigQuery warehouse using the `terraform-google-secured-data-warehouse-onprem-ingest` repository.

![The sensitive data warehouse architecture for external networks.](https://docs.cloud.google.com/static/architecture/blueprints/images/confidential-data-warehouse-blueprint/sdwv2-architecture.svg)

### Google Cloud services and features

The architectures use a combination of the following Google Cloud services and features:

Service or feature | Description  
---|---  
[BigQuery](https://docs.cloud.google.com/bigquery/docs/introduction) | Applicable to both internal and external data sources. However, different storage options exist, as follows:

  * When importing data from Google Cloud, BigQuery stores the confidential data in the confidential data perimeter.
  * When importing data from an external source, BigQuery stores the encrypted data and the wrapped encryption key in separate tables.

BigQuery uses various security controls to help protect content, including [access controls](https://docs.cloud.google.com/bigquery/docs/access-control), [column-level security](https://docs.cloud.google.com/bigquery/docs/column-level-security-intro) for confidential data, and [data encryption](https://docs.cloud.google.com/bigquery/docs/customer-managed-encryption).  
Cloud Key Management Service (Cloud KMS) with [Cloud HSM](https://docs.cloud.google.com/kms/docs/hsm) | Applicable to both internal and external sources. However, an additional use case for external data sources exists.Cloud HSM is a cloud-based hardware security module (HSM) service that hosts the key encryption key (KEK). When importing data from an external source, you use Cloud HSM to generate the encryption key that you use to encrypt the data in your network before sending it to Google Cloud.  
[Cloud Logging](https://docs.cloud.google.com/logging/docs) | Applicable to both internal and external sources.Cloud Logging collects all the logs from Google Cloud services for storage and retrieval by your analysis and investigation tools.  
[Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview) | Applicable to both internal and external sources.Cloud Monitoring collects and stores performance information and metrics about Google Cloud services.  
[Cloud Run functions](https://docs.cloud.google.com/run/docs/functions-with-run) | Applicable for external data sources only.Cloud Run functions is triggered by Cloud Storage and writes the data that Cloud Storage uploads to the ingestion bucket into BigQuery.  
[Cloud Storage](https://docs.cloud.google.com/storage/docs/introduction) and [Pub/Sub](https://docs.cloud.google.com/pubsub/docs/overview) | Applicable to both internal and external sources.Cloud Storage and Pub/Sub receive data as follows:

  * **Cloud Storage:** receives and stores batch data. By default, Cloud Storage uses TLS to encrypt data in transit and AES-256 to encrypt data in storage. The encryption key is a [customer-managed encryption key (CMEK)](https://docs.cloud.google.com/kms/docs/cmek). For more information about encryption, see [Data encryption options](https://docs.cloud.google.com/storage/docs/encryption). You can help to secure access to Cloud Storage buckets using security controls such as Identity and Access Management, access control lists (ACLs), and policy documents. For more information about supported access controls, see [Overview of access control](https://docs.cloud.google.com/storage/docs/access-control).


  * **Pub/Sub:** receives and stores streaming data before de-identification. Pub/Sub uses [authentication](https://docs.cloud.google.com/pubsub/docs/authentication), [access controls](https://docs.cloud.google.com/pubsub/docs/access-control), and [message-level encryption](https://docs.cloud.google.com/pubsub/docs/encryption#using-cmek) with a CMEK to protect your data.

  
[Data Profiler for BigQuery](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles) | Applicable to both internal and external sources.Data Profiler for BigQuery automatically scans for sensitive data in all BigQuery tables and columns across the entire organization, including all folders and projects.  
[Dataflow](https://docs.cloud.google.com/dataflow/docs/overview) pipelines | Applicable to both internal and external sources; however, different pipelines exist.Dataflow pipelines import data, as follows:

  * When importing data from Google Cloud, two Dataflow pipelines de-identify and re-identify confidential data. The first pipeline de-identifies confidential data using [pseudonymization](https://docs.cloud.google.com/sensitive-data-protection/docs/pseudonymization). The second pipeline re-identifies confidential data when authorized users require access.
  * When importing data from an external source, one Dataflow pipeline writes streaming data into BigQuery.

  
[Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/introduction) | Applicable to both internal and external sources.Knowledge Catalog automatically categorizes confidential data with metadata, also known as [policy tags](https://docs.cloud.google.com/bigquery/docs/column-level-security-intro), during ingestion. Knowledge Catalog also uses metadata to manage access to confidential data. To control access to data within the data warehouse, you apply policy tags to columns that include confidential data.  
[Dedicated Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/dedicated-overview) | Applicable for external data sources only.Dedicated Interconnect lets you move data between your network and Google Cloud. You can use another connectivity option, as described in [Choosing a Network Connectivity product](https://docs.cloud.google.com/network-connectivity/docs/how-to/choose-product).  
[IAM](https://docs.cloud.google.com/iam/docs/overview) and [Resource Manager](https://docs.cloud.google.com/resource-manager/docs/manage-google-cloud-resources) | Applicable to both internal and external sources.Identity and Access Management (IAM) and Resource Manager restrict access and segment resources. The access controls and resource hierarchy follow the principle of least privilege.  
[Security Command Center](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview) | Applicable to both internal and external sources.Security Command Center monitors and reviews security findings from across your Google Cloud environment in a central location.  
[Sensitive Data Protection](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview) | Applicable to both internal and external sources; however, different scans occur.Sensitive Data Protection scans data, as follows:

  * When importing data from Google Cloud, Sensitive Data Protection de-identifies confidential data during ingestion. Sensitive Data Protection de-identifies structured and unstructured data based on the infoTypes or records that are detected.
  * When importing data from an external source, Sensitive Data Protection scans data that is stored in BigQuery to find any sensitive data that isn't protected. For more information, see [Using Sensitive Data Protection to scan BigQuery data](https://docs.cloud.google.com/bigquery/docs/scan-with-dlp).

  
[VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) | Applicable to both internal and external sources; however, different perimeters exist.VPC Service Controls creates security perimeters that isolate services and resources by setting up authorization, access controls, and [secure data exchange](https://docs.cloud.google.com/vpc-service-controls/docs/secure-data-exchange). The perimeters are as follows:

  * A data ingestion perimeter accepts incoming data (in batch or stream) and de-identifies it. A separate landing zone helps to protect the rest of your workloads from incoming data.
  * When importing data from Google Cloud, a confidential data perimeter can re-identify the confidential data and store it in a restricted area.
  * When importing external data, a data perimeter isolates the encryption data from other workloads.
  * A governance perimeter stores the encryption keys and defines what is considered confidential data.

These perimeters are designed to protect incoming content, isolate confidential data by setting up additional access controls and monitoring, and separate your governance from the actual data in the warehouse. Your governance includes key management, data catalog management, and logging.  
  
## Organization structure

You group your organization's resources so that you can manage them and separate your testing environments from your production environment. Resource Manager lets you logically group resources by project, folder, and organization.

The following diagrams show you a resource hierarchy with folders that represent different environments such as bootstrap, common, production, non-production (or staging), and development. You deploy most of the projects in the architecture into the production folder and the data governance project in the common folder, which is used for governance.

### Organization structure when importing data from Google Cloud

The following diagram shows the organization structure when importing data from Google Cloud using the `terraform-google-secured-data-warehouse` repository.

![The resource hierarchy for a sensitive data warehouse for internal sources.](https://docs.cloud.google.com/static/architecture/blueprints/images/confidential-data-warehouse-blueprint/sdwv1-structure.svg)

### Organization structure when importing data from external sources

The following diagram shows the organization structure when importing data from an external source using the `terraform-google-secured-data-warehouse-onprem-ingest` repository.

![The resource hierarchy for a sensitive data warehouse for external sources.](https://docs.cloud.google.com/static/architecture/blueprints/images/confidential-data-warehouse-blueprint/sdwv2-structure.svg)

### Folders

You use folders to isolate your production environment and governance services from your non-production and testing environments. The following table describes the folders from the enterprise foundations blueprint that are used by this architecture.

Folder | Description  
---|---  
Bootstrap | Contains resources required to deploy the enterprise foundations blueprint.  
Common | Contains centralized services for the organization, such as the Data governance project.  
Production | Contains projects that have cloud resources that have been tested and are ready to use. In this architecture, the Production folder contains the Data ingestion project and data-related projects.  
Non-production | Contains projects that have cloud resources that are being tested and staged for release. In this architecture, the Non-production folder contains the Data ingestion project and data-related projects.  
Development | Contains projects that have cloud resources that are being developed. In this architecture, the Development folder contains the Data ingestion project and data-related projects.  
  
You can change the names of these folders to align with your organization's folder structure, but we recommend that you maintain a similar structure. For more information, see the [enterprise foundations blueprint](https://docs.cloud.google.com/architecture/security-foundations).

### Projects

You isolate parts of your environment using projects. The following table describes the projects that are needed within the organization. You create these projects when you run the Terraform code. You can change the names of these projects, but we recommend that you maintain a similar project structure.

Project | Description  
---|---  
Data ingestion | Common project for both internal and external sources.Contains services that are required in order to receive data and de-identify confidential data.  
Data governance | Common project for both internal and external sources.Contains services that provide key management, logging, and data cataloging capabilities.  
Non-confidential data | Project for internal sources only.Contains services that are required in order to store data that has been de-identified.  
Confidential data | Project for internal sources only.Contains services that are required in order to store and re-identify confidential data.  
Data | Project for external sources only.Contains services that are required to store data.  
  
In addition to these projects, your environment must also include a project that hosts a Dataflow [Flex Template](https://docs.cloud.google.com/dataflow/docs/guides/templates/using-flex-templates) job. The Flex Template job is required for the streaming data pipeline.

## Mapping roles and groups to projects

You must give different user groups in your organization access to the projects that make up the confidential data warehouse. The following sections describe the architecture recommendations for user groups and role assignments in the projects that you create. You can customize the groups to match your organization's existing structure, but we recommend that you maintain a similar segregation of duties and role assignment.

### Data analyst group

Data analysts analyze the data in the warehouse. In the `terraform-google-secured-data-warehouse-onprem-ingest` repository, this group can view data after it has been loaded into the data warehouse and perform the same operations as the Encrypted data viewer group.

The following table describes the group's roles in different projects for the `terraform-google-secured-data-warehouse` repository (internal data sources only).

Project mapping | Roles  
---|---  
Data ingestion | 

  * [Dataflow Developer (`roles/dataflow.developer`)](https://docs.cloud.google.com/dataflow/docs/concepts/access-control#dataflow.developer)
  * [Dataflow Viewer (`roles/dataflow.viewer`)](https://docs.cloud.google.com/dataflow/docs/concepts/access-control#dataflow.viewer)
  * [Logs Viewer (`roles/logging.viewer`)](https://docs.cloud.google.com/logging/docs/access-control#logging.viewer)

Additional role for data analysts that require access to confidential data:

  * [Fine-Grained Reader (`roles/datacatalog.categoryFineGrainedReader`)](https://docs.cloud.google.com/bigquery/docs/column-level-security#fine_grained_reader)

  
Confidential data | 

  * [BigQuery Data Viewer (`roles/bigquery.dataViewer`)](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.dataViewer)
  * [BigQuery Job User (`roles/bigquery.jobUser`)](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.jobUser)
  * [BigQuery User (`roles/bigquery.user`)](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.user)
  * [Dataflow Developer (`roles/dataflow.developer`)](https://docs.cloud.google.com/dataflow/docs/concepts/access-control#dataflow.developer)
  * [Dataflow Viewer (`roles/dataflow.viewer`)](https://docs.cloud.google.com/dataflow/docs/concepts/access-control#dataflow.viewer)
  * [Logs Viewer (`roles/logging.viewer`)](https://docs.cloud.google.com/logging/docs/access-control#logging.viewer)

  
Non-confidential data | 

  * [BigQuery Data Viewer (`roles/bigquery.dataViewer`)](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.dataViewer)
  * [BigQuery Job User (`roles/bigquery.jobUser`)](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.jobUser)
  * [BigQuery User (`roles/bigquery.user`)](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.user)
  * [Logs Viewer (`roles/logging.viewer`)](https://docs.cloud.google.com/logging/docs/access-control#logging.viewer)

  
  
The following table describes the group's roles in different projects for the `terraform-google-secured-data-warehouse-onprem-ingest` repository (external data sources only).

Scope of assignment | Roles  
---|---  
Data ingestion project | 

  * [Dataflow Developer (`roles/dataflow.developer`)](https://docs.cloud.google.com/dataflow/docs/concepts/access-control#dataflow.developer)
  * [Dataflow Viewer (`roles/dataflow.viewer`)](https://docs.cloud.google.com/dataflow/docs/concepts/access-control#dataflow.viewer)
  * [Logs Viewer (`roles/logging.viewer`)](https://docs.cloud.google.com/logging/docs/access-control#logging.viewer)

  
Data project | 

  * [BigQuery Data Viewer (`roles/bigquery.dataViewer`)](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.dataViewer)
  * [BigQuery Job User (`roles/bigquery.jobUser`)](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.jobUser)
  * [BigQuery User (`roles/bigquery.user`)](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.user)
  * [Dataflow Developer (`roles/dataflow.developer`)](https://docs.cloud.google.com/dataflow/docs/concepts/access-control#dataflow.developer)
  * [Dataflow Viewer (`roles/dataflow.viewer`)](https://docs.cloud.google.com/dataflow/docs/concepts/access-control#dataflow.viewer)
  * [DLP Administrator (`roles/dlp.admin`)](https://docs.cloud.google.com/sensitive-data-protection/docs/iam-roles#dlp.admin)
  * [Logs Viewer (`roles/logging.viewer`)](https://docs.cloud.google.com/logging/docs/access-control#logging.viewer)

  
Data policy level | [Masked Reader (`roles/bigquerydatapolicy.maskedReader`)](https://docs.cloud.google.com/bigquery/docs/access-control#bigquerydatapolicy.maskedReader)  
  
### Encrypted data viewer group (external sources only)

The Encrypted data viewer group in the `terraform-google-secured-data-warehouse-onprem-ingest` repository can view encrypted data from BigQuery reporting tables through Data Studio and other reporting tools, such as SAP Business Objects. The encrypted data viewer group can't view cleartext data from encrypted columns.

This group requires the [BigQuery User (`roles/bigquery.jobUser`)](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.jobUser) role in the Data project. This group also requires the [Masked Reader (`roles/bigquerydatapolicy.maskedReader`)](https://docs.cloud.google.com/bigquery/docs/access-control#bigquerydatapolicy.maskedReader) role at the data policy level.

### Plaintext reader group (external sources only)

The Plaintext reader group in the `terraform-google-secured-data-warehouse-onprem-ingest` repository has the required permission to call the decryption user-defined function (UDF) to view plaintext data and the additional permission to read unmasked data.

This group requires the following roles in the Data project:

  * [BigQuery User (`roles/bigquery.user`)](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.user)
  * [BigQuery User (`roles/bigquery.jobUser`)](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.jobUser)
  * [Cloud KMS Viewer (`roles/cloudkms.viewer`)](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles#cloudkms.viewer)



In addition, this group requires the [Fine-Grained Reader (`roles/datacatalog.categoryFineGrainedReader`)](https://docs.cloud.google.com/bigquery/docs/column-level-security#fine_grained_reader) role at the Knowledge Catalog level.

### Data engineer group

Data engineers set up and maintain the data pipeline and warehouse.

The following table describes the group's roles in different projects for the `terraform-google-secured-data-warehouse` repository.

Scope of assignment | Roles  
---|---  
Data ingestion project | 

  * [Cloud Build Editor (`roles/cloudbuild.builds.editor`)](https://docs.cloud.google.com/build/docs/iam-roles-permissions#predefined_roles)
  * [Cloud KMS Viewer (`roles/cloudkms.viewer`)](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles#cloudkms.viewer)
  * [Composer User (`roles/composer.user`)](https://docs.cloud.google.com/composer/docs/composer-3/access-control#composer.user)
  * [Compute Network User (`roles/compute.networkUser`)](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkUser)
  * [Dataflow Admin (`roles/dataflow.admin`)](https://docs.cloud.google.com/dataflow/docs/concepts/access-control#dataflow.admin)
  * [Logs Viewer (`roles/logging.viewer`)](https://docs.cloud.google.com/logging/docs/access-control#logging.viewer)

  
Confidential data project | 

  * [BigQuery Data Editor (`roles/bigquery.dataEditor`)](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.dataEditor)
  * [BigQuery Job User (`roles/bigquery.jobUser`)](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.jobUser)
  * [Cloud Build Editor (`roles/cloudbuild.builds.editor`)](https://docs.cloud.google.com/build/docs/iam-roles-permissions#predefined_roles)
  * [Cloud KMS Viewer (`roles/cloudkms.viewer`)](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles#cloudkms.viewer)
  * [Compute Network User (`roles/compute.networkUser`)](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkUser)
  * [Dataflow Admin (`roles/dataflow.admin`)](https://docs.cloud.google.com/dataflow/docs/concepts/access-control#dataflow.admin)
  * [Logs Viewer (`roles/logging.viewer`)](https://docs.cloud.google.com/logging/docs/access-control#logging.viewer)

  
Non-confidential data project | 

  * [BigQuery Data Editor (`roles/bigquery.dataEditor`)](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.dataEditor)
  * [BigQuery Job User (`roles/bigquery.jobUser`)](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.jobUser)
  * [Cloud KMS Viewer (`roles/cloudkms.viewer`)](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles#cloudkms.viewer)
  * [Logs Viewer (`roles/logging.viewer`)](https://docs.cloud.google.com/logging/docs/access-control#logging.viewer)

  
  
The following table describes the group's roles in different projects for the `terraform-google-secured-data-warehouse-onprem-ingest` repository.

Scope of assignment | Roles  
---|---  
Data ingestion project | 

  * [Cloud Build Editor (`roles/cloudbuild.builds.editor`)](https://docs.cloud.google.com/build/docs/iam-roles-permissions#predefined_roles)
  * [Cloud KMS Viewer (`roles/cloudkms.viewer`)](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles#cloudkms.viewer)
  * [Composer User (`roles/composer.user`)](https://docs.cloud.google.com/composer/docs/composer-3/access-control#composer.user)
  * [Compute Network User (`roles/compute.networkUser`)](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkUser)
  * [Dataflow Admin (`roles/dataflow.admin`)](https://docs.cloud.google.com/dataflow/docs/concepts/access-control#dataflow.admin)
  * [Logs Viewer (`roles/logging.viewer`)](https://docs.cloud.google.com/logging/docs/access-control#logging.viewer)

  
Data project | 

  * [BigQuery Data Editor (`roles/bigquery.dataEditor`)](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.dataEditor)
  * [BigQuery Job User (`roles/bigquery.jobUser`)](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.jobUser)
  * [Cloud Build Editor (`roles/cloudbuild.builds.editor`)](https://docs.cloud.google.com/build/docs/iam-roles-permissions#predefined_roles)
  * [Cloud KMS Viewer (`roles/cloudkms.viewer`)](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles#cloudkms.viewer)
  * [Compute Network User (`roles/compute.networkUser`)](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkUser)
  * [Dataflow Admin (`roles/dataflow.admin`)](https://docs.cloud.google.com/dataflow/docs/concepts/access-control#dataflow.admin)
  * [DLP Administrator (`roles/dlp.admin`)](https://docs.cloud.google.com/sensitive-data-protection/docs/iam-roles#dlp.admin)
  * [Logs Viewer (`roles/logging.viewer`)](https://docs.cloud.google.com/logging/docs/access-control#logging.viewer)

  
  
### Network administrator group

Network administrators configure the network. Typically, they are members of the networking team.

Network administrators require the following roles at the organization level:

  * [Compute Admin (`roles/compute.networkAdmin`)](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkAdmin)
  * [Logs Viewer (`roles/logging.viewer`)](https://docs.cloud.google.com/logging/docs/access-control#logging.viewer)



### Security administrator group

Security administrators administer security controls such as access, keys, firewall rules, VPC Service Controls, and the Security Command Center.

Security administrators require the following roles at the organization level:

  * [Access Context Manager Admin (`roles/accesscontextmanager.policyAdmin`)](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.policyAdmin)
  * [Cloud Asset Viewer (`roles/cloudasset.viewer`)](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudasset#cloudasset.viewer)
  * [Cloud KMS Admin (`roles/cloudkms.admin`)](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles#cloudkms.admin)
  * [Compute Security Admin (`roles/compute.securityAdmin`)](https://docs.cloud.google.com/compute/docs/access/iam#compute.securityAdmin)
  * [Data Catalog Admin (`roles/datacatalog.admin`)](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.admin)
  * [DLP Administrator (`roles/dlp.admin`)](https://docs.cloud.google.com/sensitive-data-protection/docs/iam-roles#dlp.admin)
  * [Logging Admin (`roles/logging.admin`)](https://docs.cloud.google.com/logging/docs/access-control#logging.admin)
  * [Organization Administrator (`roles/orgpolicy.policyAdmin`)](https://docs.cloud.google.com/resource-manager/docs/access-control-org#resourcemanager.organizationAdmin)
  * [Security Admin (`roles/iam.securityAdmin`)](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin)



### Security analyst group

Security analysts monitor and respond to security incidents and Sensitive Data Protection findings.

Security analysts require the following roles at the organization level:

  * [Access Context Manager Reader (`roles/accesscontextmanager.policyReader`)](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.policyReader)
  * [Compute Network Viewer (`roles/compute.networkViewer`)](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkViewer)
  * [Data Catalog Viewer (`roles/datacatalog.viewer`)](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.viewer)
  * [Cloud KMS Viewer (`roles/cloudkms.viewer`)](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles#cloudkms.viewer)
  * [Logs Viewer (`roles/logging.viewer`)](https://docs.cloud.google.com/logging/docs/access-control#logging.viewer)
  * [Organization Policy Viewer (`roles/orgpolicy.policyViewer`)](https://docs.cloud.google.com/iam/docs/roles-permissions/orgpolicy#orgpolicy.policyViewer)
  * [Security Center Admin Viewer (`roles/securitycenter.adminViewer`)](https://docs.cloud.google.com/security-command-center/docs/access-control-org#securitycenter.adminViewer)
  * [Security Center Findings Editor (`roles/securitycenter.findingsEditor`)](https://docs.cloud.google.com/security-command-center/docs/access-control-org#securitycenter.findingsEditor)
  * One of the following Security Command Center roles: 
    * [Security Center Findings Bulk Mute Editor (`roles/securitycenter.findingsBulkMuteEditor`)](https://docs.cloud.google.com/security-command-center/docs/access-control-org#securitycenter.findingsBulkMuteEditor)
    * [Security Center Finders Mute Setter (`roles/securitycenter.findingsMuteSetter`)](https://docs.cloud.google.com/security-command-center/docs/access-control-org#securitycenter.findingsMuteSetter)
    * [Security Center Findings State Setter (`roles/securitycenter.findingsStateSetter`)](https://docs.cloud.google.com/security-command-center/docs/access-control-org#securitycenter.findingsStateSetter)



### Example group access flows for external sources

The following sections describe access flows for two groups when importing data from external sources using the `terraform-google-secured-data-warehouse-onprem-ingest` repository.

#### Access flow for Encrypted data viewer group

The following diagram shows what occurs when a user from the Encrypted data viewer group tries to access encrypted data in BigQuery.

![The flow for the encrypted data viewer group.](https://docs.cloud.google.com/static/architecture/blueprints/images/confidential-data-warehouse-blueprint/sdwv2-encrypted-data-access.svg)

The steps to access data in BigQuery are as follows:

  1. The Encrypted data viewer executes the following query on BigQuery to access confidential data:
         
         SELECT ssn, pan FROM cc_card_table
         

  2. BigQuery verifies access as follows:

     * The user is authenticated using valid, unexpired Google Cloud credentials.
     * The user identity and the IP address that the request originated from are part of the allowlist in the access level or ingress rule on the VPC Service Controls perimeter.
     * IAM verifies that the user has the appropriate roles and is authorized to access selected encrypted columns on the BigQuery table.



BigQuery returns the confidential data in encrypted format.

#### Access flow for Plaintext reader group

The following diagram shows what occurs when a user from the Plaintext reader group tries to access encrypted data in BigQuery.

![The flow for the plaintext reader group.](https://docs.cloud.google.com/static/architecture/blueprints/images/confidential-data-warehouse-blueprint/sdwv2-plaintext-reader.svg)

The steps to access data in BigQuery are as follows:

  1. The Plaintext reader executes the following query on BigQuery to access confidential data in decrypted format:
         
         SELECT decrypt_ssn(ssn) FROM cc_card_table
         

  2. BigQuery calls the decrypt [user-defined function (UDF)](https://docs.cloud.google.com/bigquery/docs/user-defined-functions) within the query to access protected columns.

  3. Access is verified as follows:

     * IAM verifies that the user has appropriate roles and is authorized to access the decrypt UDF on BigQuery.
     * The UDF retrieves the wrapped data encryption key (DEK) that was used to protect sensitive data columns.
  4. The decrypt UDF calls the key encryption key (KEK) in Cloud HSM to unwrap the DEK. The decrypt UDF uses the [BigQuery AEAD decrypt function](https://docs.cloud.google.com/bigquery/docs/aead-encryption-concepts#decryption) to decrypt the sensitive data columns.

  5. The user is granted access to the plaintext data in the sensitive data columns.




## Common security controls

The following sections describe the controls that apply to both internal and external sources.

### Data ingestion controls

To create your data warehouse, you must transfer data from another Google Cloud source (for example, a data lake), your on-premises environment, or another cloud. You can use one of the following options to transfer your data into the data warehouse on BigQuery:

  * A batch job that uses Cloud Storage.
  * A streaming job that uses Pub/Sub.



To help protect data during ingestion, you can use client-side encryption, firewall rules, and access level policies. The ingestion process is sometimes referred to as an [extract, transform, load (ETL) process](https://cloud.google.com/learn/what-is-etl).

### Network and firewall rules

[Virtual Private Cloud (VPC) firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls) control the flow of data into the perimeters. You create firewall rules that deny all egress, except for specific TCP port 443 connections from the `restricted.googleapis.com` special domain names. The `restricted.googleapis.com` domain has the following benefits:

  * It helps reduce your network attack surface by using Private Google Access when workloads communicate to Google APIs and services.
  * It ensures that you only use services that support VPC Service Controls.



For more information, see [Configuring Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access).

When using the `terraform-google-secured-data-warehouse` repository, you must configure separate subnets for each Dataflow job. Separate subnets ensure that data that is being de-identified is properly separated from data that is being re-identified.

The data pipeline requires you to open TCP ports in the firewall, as defined in the `dataflow_firewall.tf` file in the respective repositories. For more information, see [Configuring internet access and firewall rules](https://docs.cloud.google.com/dataflow/docs/guides/routes-firewall).

To deny resources the ability to use external IP addresses, the [Define allowed external IPs for VM instances (`compute.vmExternalIpAccess`)](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints#:%7E:text=compute.vmExternalIpAccess) organization policy is set to deny all.

### Perimeter controls

As shown in the architecture diagram, you place the resources for the data warehouse into separate perimeters. To enable services in different perimeters to share data, you create [perimeter bridges](https://docs.cloud.google.com/vpc-service-controls/docs/share-across-perimeters).

Perimeter bridges let protected services make requests for resources outside of their perimeter. These bridges make the following connections for the `terraform-google-secured-data-warehouse` repository:

  * They connect the data ingestion project to the governance project so that de-identification can take place during ingestion.
  * They connect the non-confidential data project and the confidential data project so that confidential data can be re-identified when a data analyst requests it.
  * They connect the confidential project to the data governance project so that re-identification can take place when a data analyst requests it.



These bridges make the following connections for the `terraform-google-secured-data-warehouse-onprem-ingest` repository:

  * They connect the Data ingestion project to the Data project so that data can be ingested into BigQuery.
  * They connect the Data project to the Data governance project so that Sensitive Data Protection can scan BigQuery for unprotected confidential data.
  * They connect the Data ingestion project to the Data governance project for access to logging, monitoring, and encryption keys.



In addition to perimeter bridges, you use [egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules) to let resources protected by service perimeters access resources that are outside the perimeter. In this solution, you configure egress rules to obtain the external Dataflow Flex Template jobs that are located in Cloud Storage in an external project. For more information, see [Access a Google Cloud resource outside the perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/secure-data-exchange#allow_access_to_a_google_cloud_resource_outside_the_perimeter).

### Access policy

To help ensure that only specific identities (user or service) can access resources and data, you enable IAM groups and roles.

To help ensure that only specific sources can access your projects, you enable an [access policy](https://docs.cloud.google.com/access-context-manager/docs/overview) for your Google organization. We recommend that you create an access policy that specifies the allowed IP address range for requests and only allows requests from specific users or service accounts. For more information, see [Access level attributes](https://docs.cloud.google.com/access-context-manager/docs/access-level-attributes).

### Service accounts and access controls

Service accounts are identities that Google Cloud can use to run API requests on your behalf. Service accounts ensure that user identities don't have direct access to services. To permit separation of duties, you create service accounts with different roles for specific purposes. These service accounts are defined in the `data-ingestion` module and the `confidential-data` module in each architecture.

For the `terraform-google-secured-data-warehouse` repository, the service accounts are as follows:

  * A Dataflow controller service account for the Dataflow pipeline that de-identifies confidential data.
  * A Dataflow controller service account for the Dataflow pipeline that re-identifies confidential data.
  * A Cloud Storage service account to ingest data from a batch file.
  * A Pub/Sub service account to ingest data from a streaming service.
  * A Cloud Scheduler service account to run the batch Dataflow job that creates the Dataflow pipeline.



The following table lists the roles that are assigned to each service account:

Service Account | Name | Project | Roles  
---|---|---|---  
Dataflow controllerThis account is used for de-identification. | `sa-dataflow-controller` | Data ingestion | 

  * [BigQuery Admin `roles/bigquery.admin`](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.admin)
  * [Cloud KMS Admin (`roles/cloudkms.admin`)](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles#cloudkms.admin)
  * [Cloud KMS CryptoKey Decrypter (`roles/cloudkms.cryptoKeyDecrypter`)](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles#cloudkms.cryptoKeyDecrypter)
  * [Compute Viewer (`roles/compute.viewer`)](https://docs.cloud.google.com/compute/docs/access/iam#compute.viewer)
  * [Dataflow Worker (`roles/dataflow.worker`)](https://docs.cloud.google.com/dataflow/docs/concepts/access-control#dataflow.worker)
  * [DLP Administrator (`roles/dlp.admin`)](https://docs.cloud.google.com/sensitive-data-protection/docs/iam-roles#dlp.admin)
  * [Pub/Sub Subscriber (`roles/pubsub.subscriber`)](https://docs.cloud.google.com/pubsub/docs/access-control#pubsub.subscriber)
  * [Storage Admin (`roles/storage.admin`)](https://docs.cloud.google.com/storage/docs/access-control/iam-roles#storage.admin)
  * [Dataflow Service Agent (`roles/dataflow.serviceAgent`)](https://docs.cloud.google.com/dataflow/docs/concepts/security-and-permissions#df-service-account)

  
Dataflow controllerThis account is used for re-identification. | `sa-dataflow-controller-reid` | Confidential data | 

  * [BigQuery Admin `roles/bigquery.admin`](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.admin)
  * [Cloud KMS Admin (`roles/cloudkms.admin`)](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles#cloudkms.admin)
  * [Cloud KMS CryptoKey Decrypter (`roles/cloudkms.cryptoKeyDecrypter`)](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles#cloudkms.cryptoKeyDecrypter)
  * [Compute Viewer (`roles/compute.viewer`)](https://docs.cloud.google.com/compute/docs/access/iam#compute.viewer)
  * [Dataflow Worker (`roles/dataflow.worker`)](https://docs.cloud.google.com/dataflow/docs/concepts/access-control#dataflow.worker)
  * [DLP Administrator (`roles/dlp.admin`)](https://docs.cloud.google.com/sensitive-data-protection/docs/iam-roles#dlp.admin)
  * [Pub/Sub Subscriber (`roles/pubsub.subscriber`)](https://docs.cloud.google.com/pubsub/docs/access-control#pubsub.subscriber)
  * [Storage Admin (`roles/storage.admin`)](https://docs.cloud.google.com/storage/docs/access-control/iam-roles#storage.admin)
  * [Dataflow Service Agent (`roles/dataflow.serviceAgent`)](https://docs.cloud.google.com/dataflow/docs/concepts/security-and-permissions#df-service-account)

  
Cloud Storage | `sa-storage-writer` | Data ingestion | 

  * [Storage Object Creator (`roles/storage.objectCreator`)](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectCreator")
  * [Storage Object Viewer (`roles/storage.ObjectViewer`)](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectViewer)

  
Pub/Sub | `sa-pubsub-writer` | Data ingestion | 

  * [Pub/Sub Publisher (`roles/pubsub.publisher`)](https://docs.cloud.google.com/pubsub/docs/access-control#pubsub.publisher)
  * [Pub/Sub Subscriber (`roles/pubsub.subscriber`)](https://docs.cloud.google.com/pubsub/docs/access-control#pubsub.subscriber)

  
Cloud Scheduler | `sa-scheduler-controller` | Data ingestion | 

  * [Compute Viewer (`roles/compute.viewer`)](https://docs.cloud.google.com/compute/docs/access/iam#compute.viewer)
  * [Dataflow Developer (`roles/dataflow.developer`)](https://docs.cloud.google.com/dataflow/docs/concepts/access-control#dataflow.developer)

  
  
For the `terraform-google-secured-data-warehouse-onprem-ingest` repository, the service accounts are as follows:

  * Cloud Storage service account runs the automated batch data upload process to the ingestion storage bucket.
  * Pub/Sub service account enables streaming of data to Pub/Sub service.
  * Dataflow controller service account is used by the Dataflow pipeline to transform and write data from Pub/Sub to BigQuery.
  * Cloud Run functions service account writes subsequent batch data uploaded from Cloud Storage to BigQuery.
  * Storage Upload service account allows the ETL pipeline to create objects.
  * Pub/Sub Write service Account lets the ETL pipeline write data to Pub/Sub.



The following table lists the roles that are assigned to each service account:

Name | Roles | Scope of Assignment  
---|---|---  
Dataflow controller service account | 

  * [BigQuery Data Editor (`roles/bigquery.dataEditor`)](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.dataEditor)
  * [BigQuery Job User (`roles/bigquery.jobUser`)](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.jobUser)
  * [Dataflow Developer (`roles/dataflow.developer`)](https://docs.cloud.google.com/dataflow/docs/concepts/access-control#dataflow.developer)
  * [Dataflow Worker (`roles/dataflow.worker`)](https://docs.cloud.google.com/dataflow/docs/concepts/access-control#dataflow.worker)
  * [Pub/Sub Editor (`roles/pubsub.editor`)](https://docs.cloud.google.com/pubsub/docs/access-control#pubsub.editor)
  * [Pub/Sub Subscriber (`roles/pubsub.subscriber`)](https://docs.cloud.google.com/pubsub/docs/access-control#pubsub.subscriber)
  * [Service Usage Consumer (`roles/serviceusage.serviceUsageConsumer`)](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageConsumer)
  * [Storage Object Viewer (`roles/storage.ObjectViewer`)](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectViewer)

| Data ingestion project  
| 

  * [BigQuery Data Editor (`roles/bigquery.dataEditor`)](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.dataEditor)
  * [BigQuery Metadata Viewer (`roles/bigquery.metadataViewer`)](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.metadataViewer)

| Data project  
| 

  * [DLP Inspect Findings Reader (`roles/dlp.deidentifyTemplatesReader`)](https://docs.cloud.google.com/sensitive-data-protection/docs/iam-roles#dlp.inspectFindingsReader)
  * [DLP Inspect Templates Editor (`roles/dlp.inspectTemplatesReader`)](https://docs.cloud.google.com/sensitive-data-protection/docs/iam-roles#dlp.inspectTemplatesEditor)
  * [DLP User (`roles/dlp.user`)](https://docs.cloud.google.com/sensitive-data-protection/docs/iam-roles#dlp.user)

| Data governance  
Cloud Run functions service account | 

  * [BigQuery Data Editor (`roles/bigquery.dataEditor`)](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.dataEditor)
  * [BigQuery Job User (`roles/bigquery.jobUser`)](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.jobUser)
  * [Cloud Run Invoker (`roles/run.invoker`)](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.invoker)
  * [Eventarc Event Receiver (`roles/eventarc.eventReceiver`)](https://docs.cloud.google.com/iam/docs/roles-permissions/eventarc#eventarc.eventReceiver)

| Data ingestion project  
| 

  * [BigQuery Data Editor (`roles/bigquery.dataEditor`)](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.dataEditor)
  * [BigQuery Metadata Viewer (`roles/bigquery.metadataViewer`)](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.metadataViewer)

| Data project  
Storage Upload service account | 

  * [Storage Object Creator (`roles/storage.objectCreator`)](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectCreator")
  * [Storage Object Viewer (`roles/storage.ObjectViewer`)](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectViewer)

| Data ingestion Project  
Pub/Sub Write service account | 

  * [Pub/Sub Publisher (`roles/pubsub.publisher`)](https://docs.cloud.google.com/pubsub/docs/access-control#pubsub.publisher)
  * [Pub/Sub Subscriber (`roles/pubsub.subscriber`)](https://docs.cloud.google.com/pubsub/docs/access-control#pubsub.subscriber)

| Data ingestion Project  
  
### Organizational policies

This architecture includes the organization policy constraints that the enterprise foundations blueprint uses and adds additional constraints. For more information about the constraints that the enterprise foundations blueprint uses, see [Organization policy constraints](https://docs.cloud.google.com/architecture/security-foundations/preventative-controls#organization-policy).

The following table describes the additional organizational policy [constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints) that are defined in the `org_policies` module for the respective repositories:

Policy | Constraint name | Recommended value  
---|---|---  
[Restrict resource deployments](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations) to specific physical locations. For additional values, see [Value groups](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations#value_groups). | `gcp.resourceLocations` | One of the following:`in:us-locations``in:eu-locations``in:asia-locations`  
[Disable service account creation](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_service_account_creation) | `iam.disableServiceAccountCreation` | `true`  
[Enable OS Login for VMs created in the project](https://docs.cloud.google.com/compute/docs/oslogin/set-up-oslogin). | `compute.requireOsLogin` | `true`  
[Restrict new forwarding](https://docs.cloud.google.com/compute/docs/protocol-forwarding#enforcing_protocol_forwarding_settings_across_a_project_folder_or_organization) rules to be internal only, based on IP address. | `compute.restrictProtocolForwardingCreationForTypes` | `INTERNAL`  
[Define the set of Shared VPC subnetworks](https://docs.cloud.google.com/vpc/docs/provisioning-shared-vpc#constrain_which_subnets_in_the_host_project_that_a_service_project_can_use) that Compute Engine resources can use. | `compute.restrictSharedVpcSubnetworks` | `projects//regions//s ubnetworks/`.Replace with the resource ID of the private subnet that you want the architecture to use.  
[Disable serial port output logging](https://docs.cloud.google.com/compute/docs/troubleshooting/viewing-serial-port-output) to Cloud Logging. | `compute.disableSerialPortLogging` | `true`  
[Require CMEK protection](https://docs.cloud.google.com/kms/docs/cmek-org-policy#require-cmek) (`terraform-google-secured-data-warehouse-onprem-ingest` only) | `gcp.restrictNonCmekServices` | `bigquery.googleapis.com`  
Disable service account key creation (`terraform-google-secured-data-warehouse-onprem-ingest only`) | `disableServiceAccountKeyCreation` | true  
[Enable OS Login for VMs created in the project](https://docs.cloud.google.com/compute/docs/oslogin/set-up-oslogin) (`terraform-google-secured-data-warehouse-onprem-ingest only`) | `compute.requireOsLogin` | true  
[Disable automatic role grants to default service account](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_service_account_default_grants) (`terraform-google-secured-data-warehouse-onprem-ingest only`) | `automaticIamGrantsForDefaultServiceAccounts` | true  
Allowed ingress settings (Cloud Run functions) (`terraform-google-secured-data-warehouse-onprem-ingest only`) | `cloudfunctions.allowedIngressSettings` | `ALLOW_INTERNAL_AND_GCLB`  
  
## Security controls for external data sources

The following sections describe the controls that apply to ingesting data from external sources.

### Encrypted connection to Google Cloud

When importing data from external sources, you can use Cloud VPN or Cloud Interconnect to protect all data that flows between Google Cloud and your environment. This enterprise architecture recommends Dedicated Interconnect, because it provides a direct connection and high throughput, which are important if you're streaming a lot of data.

To permit access to Google Cloud from your environment, you must define allowlisted IP addresses in the access levels policy rules.

### Client-side encryption

Before you move your sensitive data into Google Cloud, encrypt your data locally to help protect it at rest and in transit. You can use the [Tink](https://developers.google.com/tink) encryption library, or you can use other encryption libraries. The Tink encryption library is compatible with [BigQuery AEAD encryption](https://docs.cloud.google.com/bigquery/docs/column-key-encrypt), which the architecture uses to decrypt column-level encrypted data after the data is imported.

The Tink encryption library uses DEKs that you can generate locally or from [Cloud HSM](https://docs.cloud.google.com/kms/docs/generate-random#generating_random_bytes). To wrap or protect the DEK, you can use a KEK that is generated in Cloud HSM. The KEK is a [symmetric CMEK](https://docs.cloud.google.com/kms/docs/cmek) encryption keyset that is stored securely in Cloud HSM and managed using IAM roles and permissions.

During ingestion, both the wrapped DEK and the data are stored in BigQuery. BigQuery includes two tables: one for the data and the other for the wrapped DEK. When analysts need to view confidential data, BigQuery can use [AEAD decryption](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/aead-encryption-concepts) to unwrap the DEK with the KEK and decrypt the protected column.

Also, client-side encryption using Tink further protects your data by encrypting sensitive data columns in BigQuery. The architecture uses the following Cloud HSM encryption keys:

  * A CMEK key for the ingestion process that's also used by Pub/Sub, Dataflow pipeline for streaming, Cloud Storage batch upload, and Cloud Run functions artifacts for subsequent batch uploads.
  * The cryptographic key wrapped by Cloud HSM for the data encrypted on your network using Tink.
  * CMEK key for the BigQuery warehouse in the Data project.



You specify the CMEK location, which determines the geographical location that the key is stored and is made available for access. You must ensure that your CMEK is in the same location as your resources. By default, the CMEK is rotated every 30 days.

If your organization's compliance obligations require that you manage your own keys externally from Google Cloud, you can enable [Cloud External Key Manager](https://docs.cloud.google.com/kms/docs/ekm). If you use external keys, you're responsible for key management activities, including key rotation.

### Dynamic data masking

To help with sharing and applying data access policies at scale, you can configure [dynamic data masking](https://docs.cloud.google.com/bigquery/docs/column-data-masking-intro). Dynamic data masking lets existing queries automatically mask column data using the following criteria:

  * The masking rules that are applied to the column at query runtime.
  * The roles that are assigned to the user who is running the query. To access unmasked column data, the data analyst must have the [Fine-Grained Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/datacatalog#datacatalog.categoryFineGrainedReader) role.



To define access for columns in BigQuery, you create [policy tags](https://docs.cloud.google.com/bigquery/docs/best-practices-policy-tags). For example, the taxonomy created in the [standalone example](https://github.com/GoogleCloudPlatform/terraform-google-secured-data-warehouse-onprem-ingest/tree/main/examples/standalone) creates the `1_Sensitive` policy tag for columns that include data that cannot be made public, such as the credit limit. The default data masking rule is applied to these columns to hide the value of the column.

Anything that isn't tagged is available to all users who have access to the data warehouse. These access controls ensure that, even after the data is written to BigQuery, the data in sensitive fields still cannot be read until access is explicitly granted to the user.

### Column-level encryption and decryption

[Column-level encryption](https://docs.cloud.google.com/bigquery/docs/column-key-encrypt) lets you encrypt data in BigQuery at a more granular level. Instead of encrypting an entire table, you select the columns that contain sensitive data within BigQuery, and only those columns are encrypted. BigQuery uses [AEAD encryption and decryption](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/aead_encryption_functions) functions that create the keysets that contain the keys for encryption and decryption. These keys are then used to encrypt and decrypt individual values in a table, and rotate keys within a keyset. Column-level encryption provides dual-access control on encrypted data in BigQuery, because the user must have permissions to both the table and the encryption key to read data in cleartext.

### Data profiler for BigQuery with Sensitive Data Protection

[Data profiler](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles) lets you identify the locations of sensitive and high risk data in BigQuery tables. Data profiler automatically scans and analyzes all BigQuery tables and columns across the entire organization, including all folders and projects. Data profiler then outputs metrics such as the predicted [infoTypes](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-infotypes), the assessed data risk and sensitivity levels, and metadata about your tables. Using these insights, you can make informed decisions about how you protect, share, and use your data.

## Security controls for internal data sources

The following sections describe the controls that apply to ingesting data from Google Cloud sources.

### Key management and encryption for ingestion

Both ingestion options (Cloud Storage or Pub/Sub) use Cloud HSM to manage the CMEK. You use the CMEK keys to help protect your data during ingestion. Sensitive Data Protection further protects your data by encrypting confidential data, using the detectors that you configure.

To ingest data, you use the following encryption keys:

  * A CMEK key for the ingestion process that's also used by the Dataflow pipeline and the Pub/Sub service.
  * The cryptographic key [wrapped](https://docs.cloud.google.com/sensitive-data-protection/docs/create-wrapped-key) by Cloud HSM for the data de-identification process using Sensitive Data Protection.
  * Two CMEK keys, one for the BigQuery warehouse in the non-confidential data project, and the other for the warehouse in the confidential data project. For more information, see [Key management](https://docs.cloud.google.com/bigquery/docs/customer-managed-encryption#dataset_default_key).



You specify the [CMEK location](https://docs.cloud.google.com/kms/docs/locations), which determines the geographical location that the key is stored and is made available for access. You must ensure that your CMEK is in the same location as your resources. By default, the CMEK is rotated every 30 days.

If your organization's compliance obligations require that you manage your own keys externally from Google Cloud, you can enable [Cloud EKM](https://docs.cloud.google.com/kms/docs/ekm). If you use external keys, you are responsible for key management activities, including key rotation.

### Data de-identification

You use Sensitive Data Protection to de-identify your structured and unstructured data during the ingestion phase. For structured data, you use [record transformations](https://docs.cloud.google.com/sensitive-data-protection/docs/deidentify-sensitive-data#record_transformations) based on fields to de-identify data. For an example of this approach, see the [`/examples/de_identification_template/`](https://github.com/GoogleCloudPlatform/terraform-google-secured-data-warehouse/tree/main/examples/de-identification-template) folder. This example checks structured data for any credit card numbers and card PINs. For unstructured data, you use [information types](https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference) to de-identify data.

To de-identify data that is tagged as confidential, you use Sensitive Data Protection and a Dataflow pipeline to tokenize it. This pipeline takes data from Cloud Storage, processes it, and then sends it to the BigQuery data warehouse.

For more information about the data de-identification process, see [data governance](https://github.com/GoogleCloudPlatform/terraform-google-secured-data-warehouse/tree/main/modules/data-governance).

### Column-level access controls

To help protect confidential data, you use [access controls for specific columns](https://docs.cloud.google.com/bigquery/docs/column-level-security-intro) in the BigQuery warehouse. In order to access the data in these columns, a data analyst must have the Fine-Grained Reader role.

To define access for columns in BigQuery, you create policy tags. For example, the `taxonomy.tf` file in the [`bigquery-confidential-data` example](https://github.com/GoogleCloudPlatform/terraform-google-secured-data-warehouse/tree/a4267570f86ff9cb417e122140b4cff6cb85facf/examples/bigquery-confidential-data) module creates the following tags:

  * A `3_Confidential` policy tag for columns that include very sensitive information, such as credit card numbers. Users who have access to this tag also have access to columns that are tagged with the `2_Private` or `1_Sensitive` policy tags.
  * A `2_Private` policy tag for columns that include sensitive personal identifiable information (PII), such as a person's first name. Users who have access to this tag also have access to columns that are tagged with the `1_Sensitive` policy tag. Users don't have access to columns that are tagged with the `3_Confidential` policy tag.
  * A `1_Sensitive` policy tag for columns that include data that cannot be made public, such as the credit limit. Users who have access to this tag don't have access to columns that are tagged with the `2_Private` or `3_Confidential` policy tags.



Anything that is not tagged is available to all users who have access to the data warehouse.

These access controls ensure that, even after the data is re-identified, the data still cannot be read until access is explicitly granted to the user.

**Note** : You can use the default definitions to run the examples. For more best practices, see [Best practices for using policy tags in BigQuery](https://docs.cloud.google.com/bigquery/docs/best-practices-policy-tags).

### Service accounts with limited roles

You must limit access to the confidential data project so that only authorized users can view the confidential data. To do so, you create a service account with the [Service Account User (`roles/iam.serviceAccountUser`)](https://docs.cloud.google.com/iam/docs/service-account-permissions#user-role) role that authorized users must impersonate. [Service Account impersonation](https://docs.cloud.google.com/iam/docs/impersonating-service-accounts) helps users to use service accounts without downloading the service account keys, which improves the overall security of your project. Impersonation creates a short-term token that authorized users who have the [Service Account Token Creator (`roles/iam.serviceAccountTokenCreator`)](https://docs.cloud.google.com/iam/docs/service-account-permissions#token-creator-role) role are allowed to download.

### Key management and encryption for storage and re-identification

You manage separate CMEK keys for your confidential data so that you can re-identity the data. You use Cloud HSM to protect your keys. To re-identify your data, use the following keys:

  * A CMEK key that the Dataflow pipeline uses for the re-identification process.
  * The original cryptographic key that Sensitive Data Protection uses to de-identify your data.
  * A CMEK key for the BigQuery warehouse in the confidential data project.



As mentioned in Key management and encryption for ingestion, you can specify the CMEK location and rotation periods. You can use Cloud EKM if it is required by your organization.

## Operations

You can enable logging and [Security Command Center Premium or Enterprise tier features](https://docs.cloud.google.com/security-command-center/docs/service-tiers) such as Security Health Analytics and Event Threat Detection. These controls help you to do the following:

  * Monitor who is accessing your data.
  * Ensure that proper auditing is put in place.
  * Generate findings for misconfigured cloud resources
  * Support the ability of your incident management and operations teams to respond to issues that might occur.



### Access Transparency

[Access Transparency](https://cloud.google.com/security/products/access-transparency) provides you with real-time notification when [Google personnel](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/overview#google-personnel-access) require access to your data. Access Transparency logs are generated whenever a human accesses content, and only Google personnel with valid business justifications (for example, a support case) can obtain access.

### Logging

To help you to meet auditing requirements and get insight into your projects, you configure the [Google Cloud Observability](https://cloud.google.com/products/operations) with data logs for services you want to track. The `centralized-logging` module in the repositories configures the following best practices:

  * [Creating an aggregated log sink](https://docs.cloud.google.com/logging/docs/export/aggregated_sinks) across all projects.
  * Storing your logs in the appropriate [region](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones).
  * Adding CMEK keys to your logging sink.



For all services within the projects, your logs must include information about data reads and writes, and information about what administrators read. For additional logging best practices, see [Detective controls](https://docs.cloud.google.com/architecture/security-foundations/detective-controls).

### Alerts and monitoring

After you deploy the architecture, you can set up alerts to notify your security operations center (SOC) that a security incident might be occurring. For example, you can use alerts to let your security analyst know when an IAM permission has changed. For more information about configuring Security Command Center alerts, see [Setting up finding notifications](https://docs.cloud.google.com/security-command-center/docs/how-to-notifications). For additional alerts that aren't published by Security Command Center, you can set up [alerts](https://docs.cloud.google.com/monitoring/alerts) with Cloud Monitoring.

## Additional security considerations

In addition to the security controls described in this document, you should review and manage the security and risk in key areas that overlap and interact with your use of this solution. These include the following:

  * The security of the code that you use to configure, deploy, and run Dataflow jobs and Cloud Run functions.
  * The data classification taxonomy that you use with this solution.
  * Generation and management of encryption keys.
  * The content, quality, and security of the datasets that you store and analyze in the data warehouse.
  * The overall environment in which you deploy the solution, including the following: 
    * The design, segmentation, and security of networks that you connect to this solution.
    * The security and governance of your organization's IAM controls.
    * The authentication and authorization settings for the actors to whom you grant access to the infrastructure that's part of this solution, and who have access to the data that's stored and managed in that infrastructure.



## Bringing it all together

To implement the architecture described in this document, do the following:

  1. Determine whether you will deploy the architecture with the enterprise foundations blueprint or on its own. If you choose not to deploy the enterprise foundations blueprint, ensure that your environment has a similar security baseline in place.
  2. For importing data from external sources, set up a [Dedicated Interconnect connection](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/dedicated-overview) with your network.
  3. Review the [`terraform-google-secured-data-warehouse` README](https://github.com/GoogleCloudPlatform/terraform-google-secured-data-warehouse) or [`terraform-google-secured-data-warehouse-onprem-ingest` README](https://github.com/GoogleCloudPlatform/terraform-google-secured-data-warehouse-onprem-ingest) and ensure that you meet all the prerequisites.
  4. Verify that your user identity has the [Service Account User (`roles/iam.serviceAccountUser`)](https://docs.cloud.google.com/iam/docs/service-account-permissions#user-role) and [Service Account Token Creator (`roles/iam.serviceAccountTokenCreator`)](https://docs.cloud.google.com/iam/docs/service-account-permissions#token-creator-role) roles for your organization's development folder, as described in Organization structure. If you don't have a folder that you use for testing, [create a folder](https://docs.cloud.google.com/resource-manager/docs/creating-managing-folders#creating-folders) and [configure access](https://docs.cloud.google.com/resource-manager/docs/creating-managing-folders#configuring_access_to_folders).

  5. Record your billing account ID, organization's display name, folder ID for your test or demo folder, and the email addresses for the following [user groups](https://docs.cloud.google.com/architecture/secured-data-warehouse-blueprint-onprem#mapping-roles-and-groups):

     * Data analysts
     * Encrypted data viewer
     * Plaintext reader
     * Data engineers
     * Network administrators
     * Security administrators
     * Security analysts
  6. Create the projects. For a list of APIs that you must enable, see the README.

  7. Create the service account for Terraform and assign the appropriate roles for all projects.

  8. Set up the Access Control Policy.

  9. For Google Cloud data sources using the `terraform-google-secured-data-warehouse` repository, in your testing environment, deploy the [walkthrough](https://console.cloud.google.com/?walkthrough_id=security--secured-data-warehouse-simple-example) to see the solution in action. As part of your testing process, consider the following:

     1. Add your own sample data into the BigQuery warehouse.
     2. Work with a data analyst in your enterprise to test their access to the confidential data and whether they can interact with the data from BigQuery in the way that they would expect.
  10. For external data sources using the `terraform-google-secured-data-warehouse-onprem-ingest` repository, in your testing environment, deploy the solution:

     1. Clone and run the Terraform scripts to set up an environment in Google Cloud.
     2. [Install the Tink encryption library](https://developers.google.com/tink/install-tinkey) on your network.

     3. [Set up Application Default Credentials](https://docs.cloud.google.com/docs/authentication/provide-credentials-adc) so that you can run the Tink library on your network.

     4. [Create encryption keys](https://docs.cloud.google.com/kms/docs/create-encryption-keys) with Cloud KMS.

     5. [Generate encrypted keysets](https://developers.google.com/tink/generate-encrypted-keyset) with Tink.

     6. Encrypt data with Tink using one of the following methods:

        * Using [deterministic encryption](https://developers.google.com/tink/deterministic-encryption).
        * Using a [helper script with sample data](https://github.com/GoogleCloudPlatform/terraform-google-secured-data-warehouse-onprem-ingest/tree/main/examples/standalone/helpers).
     7. Upload encrypted data to BigQuery using streaming or batch uploads.

  11. For external data sources, verify that authorized users can read unencrypted data from BigQuery using the BigQuery AEAD decrypt function. For example, run the following create decryption function:

Run the create view query:
         
         CREATE OR REPLACE VIEW `{project_id}.{bigquery_dataset}.decryption_view` AS
         
         SELECT
          Card_Type_Code,
          Issuing_Bank,
          Card_Number,
          `bigquery_dataset.decrypt`(Card_Number) AS Card_Number_Decrypted
         FROM `project_id.dataset.table_name`
         

Run the select query from view:
         
         SELECT
           Card_Type_Code,
           Issuing_Bank,
           Card_Number,
           Card_Number_Decrypted
         FROM
         `{project_id}.{bigquery_dataset}.decrypted_view`
         

For additional queries and use cases, see [Column-level encryption with Cloud KMS](https://docs.cloud.google.com/bigquery/docs/column-key-encrypt#use_cases).

  12. Use Security Command Center to scan the newly created projects against your [compliance requirements](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings).

  13. Deploy the architecture into your production environment.




## What's next

  * Review the [enterprise foundations blueprint](https://docs.cloud.google.com/architecture/security-foundations) for a baseline secure environment.
  * To see the details of the architecture, read the [Terraform configuration README](https://github.com/GoogleCloudPlatform/terraform-google-secured-data-warehouse) for internal data sources (`terraform-google-secured-data-warehouse` repository) or read the [Terraform configuration README](https://github.com/GoogleCloudPlatform/terraform-google-secured-data-warehouse-onprem-ingest) for external data sources ( `terraform-google-secured-data-warehouse-onprem-ingest` repository).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-15 UTC."],[],[]] 
