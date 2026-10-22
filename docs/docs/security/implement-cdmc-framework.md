---
url: https://docs.cloud.google.com/docs/security/implement-cdmc-framework/
title: Implement CDMC controls in BigQuery \u00a0|\u00a0 Security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:24:48.062467+00:00
---

# Implement CDMC controls in BigQuery  |  Security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/security/implement-cdmc-framework/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Guides ](https://docs.cloud.google.com/docs/security/overview/whitepaper)



Send feedback 

#  Implement CDMC controls in BigQuery Stay organized with collections  Save and categorize content based on your preferences. 

![A CDMC certification badge.](https://docs.cloud.google.com/static/docs/security/images/cdmc/cdmc-badge.png)

This document describes how to implement the 14 [Cloud Data Management Capabilities (CDMC)](https://edmcouncil.org/frameworks/cdmc/) key controls in a BigQuery data warehouse to help protect and govern sensitive data. Organizations deploy cloud data warehouses to store sensitive information for business analytics, requiring rigorous governance and regulatory compliance.

The CDMC Key Controls Framework was published primarily for cloud service providers and technology providers. The framework describes 14 key controls that providers can implement to let their customers effectively manage and govern sensitive data in the cloud. The controls were written by the CDMC Working Group, with more than 300 professionals participating from more than 100 firms. While writing the framework, the CDMC Working Group considered many of the legal and regulatory requirements that exist.

This BigQuery and Knowledge Catalog reference architecture was assessed and certified against the CDMC Key Controls Framework as a CDMC Certified Cloud Solution. The reference architecture uses various Google Cloud services and features as well as public libraries to implement the CDMC key controls and recommended automation. This document explains how you can implement the key controls to help protect sensitive data in a BigQuery data warehouse.

## Architecture

The following Google Cloud reference architecture aligns with the CDMC Key Controls Framework Test Specifications v1.1.1. The numbers in the diagram represent the key controls that are addressed with Google Cloud services.

![Reference architecture diagram showing Google Cloud services mapped to the 14 CDMC key controls.](https://docs.cloud.google.com/static/docs/security/images/cdmc/cdmc-architecture.svg)

The reference architecture builds on the [secured data warehouse blueprint](https://docs.cloud.google.com/architecture/confidential-data-warehouse-blueprint), which provides an architecture that helps you protect a BigQuery data warehouse that includes sensitive information. In the preceding diagram, projects at the top of the diagram (in gray) are part of the secured data warehouse blueprint. The data governance project (in blue) includes the services that are added to meet the CDMC Key Controls Framework requirements. To implement the CDMC Key Controls Framework, the architecture extends the Data governance project. The Data governance project provides controls such as classification, lifecycle management and data quality management. The project also provides a way to audit the architecture and report on findings.

For sample deployment templates and automation scripts, see the archived [Google Cloud CDMC Reference Architecture](https://github.com/GoogleCloudPlatform/cdmc) open source reference implementation on GitHub.

### Architecture alternative: Decentralized data mesh

The architecture that's described in this document uses a centralized data governance project to monitor and manage a centralized BigQuery data warehouse. If your organization requires a domain-driven model, you can implement the 14 CDMC key controls using a data mesh architecture with federated governance. In this model, individual domains own their data products while CDMC policies, classification standards, and audit reporting are governed centrally.

A data mesh architecture lets you implement the CDMC key controls as follows:

  * **Group logical domains:** Use [data lakes and data zones](https://docs.cloud.google.com/dataplex/docs/build-a-data-mesh-quickstart) to organize data across multiple Google Cloud projects, BigQuery datasets, and Cloud Storage buckets into distinct business domains without moving the data. For lineage and cataloging, use Knowledge Catalog.
  * **Validate data quality:** Define and schedule Knowledge Catalog [auto data quality scans](https://docs.cloud.google.com/dataplex/docs/auto-data-quality-overview) to validate data contracts without relying on a central tagging pipeline.
  * **Manage the data lifecycle:** Configure [BigQuery table partition expiration](https://docs.cloud.google.com/bigquery/docs/managing-partitioned-tables#partition-expiration), [table expiration](https://docs.cloud.google.com/bigquery/docs/managing-tables#updating_a_tables_expiration_time), and [Cloud Storage object lifecycle management](https://docs.cloud.google.com/storage/docs/lifecycle) on domain assets.
  * **Track cross-domain data lineage:** Use [Knowledge Catalog data lineage](https://docs.cloud.google.com/dataplex/docs/about-data-lineage) to track data movement and transformations across domain and project boundaries.
  * **Support hybrid and multi-cloud environments:** Use [BigQuery Omni](https://docs.cloud.google.com/bigquery/docs/omni-introduction) to analyze data in place.



To deploy an enterprise data mesh that integrates the CDMC controls, see [Deploy an enterprise data management and analytics platform](https://docs.cloud.google.com/architecture/blueprints/deploy_enterprise_data_mesh) and the companion [Terraform enterprise data mesh blueprint](https://github.com/googlecloudplatform/terraform-google-enterprise-datamesh). This blueprint implements a federated model by pairing decentralized domain producer and consumer environments with a central data governance project in a shared folder.

## Overview of the CDMC Key Controls Framework

The following table summarizes the [CDMC Key Controls Framework](https://edmcouncil.org/frameworks/cdmc/).

# | CDMC key control | CDMC control requirement  
---|---|---  
1 | Data control compliance | Cloud data management business cases are defined and governed. All data assets that contain sensitive data must be monitored for compliance with the CDMC Key Controls, using metrics and automated notifications.  
2 | Data ownership is established for both migrated and cloud-generated data | The **Ownership** field in a data catalog must be populated for all sensitive data or otherwise reported to a defined workflow.  
3 | Data sourcing and consumption are governed and supported by automation | A register of authoritative data sources and provisioning points must be populated for all data assets that contain sensitive data or otherwise must be reported to a defined workflow.  
4 | Data sovereignty and cross-border data movement are managed | The data sovereignty and cross-border movement of sensitive data must be recorded, audited, and controlled according to defined policy.  
5 | Data catalogs are implemented, used, and interoperable | Cataloging must be automated for all data at the point of creation or ingestion, with consistency across all environments.  
6 | Data classifications are defined and used | Classification must be automated for all data at the point of creation or ingestion and must be always on. Classification is automated for the following:  


  * Personally identifiable information (PII)
  * Information sensitivity classification
  * [Material nonpublic information (MNPI)](https://www.investopedia.com/terms/m/materialinsiderinformation.asp)
  * Client identifiable information
  * Organization-defined classification

  
7 | Data entitlements are managed, enforced, and tracked | This control requires the following:  


  * Entitlements and access for sensitive data must default to creator and owner until explicitly and authoritatively granted.
  * Access must be tracked for all sensitive data.

  
8 | Ethical access, use, and outcomes of data are managed | The data consumption purpose must be provided for all data sharing agreements that involve sensitive data. The purpose must specify the type of data required and, for global organizations, the country or legal entity scope.  
9 | Data is secured, and controls are evidenced | This control requires the following:  


  * Appropriate security controls must be enabled for sensitive data.
  * Security control evidence must be recorded in the data catalog for all sensitive data.

  
10 | A data privacy framework is defined and operational | Data protection impact assessments (DPIAs) must be automatically triggered for all personal data according to its jurisdiction.  
11 | The data lifecycle is planned and managed | Data retention, archiving, and purging must be managed according to a defined retention schedule.  
12 | Data quality is managed | Data quality measurement must be enabled for sensitive data with metrics distributed when available.  
13 | Cost management principles are established and applied | Technical design principles are established and applied. Cost metrics that are directly associated with data use, storage, and movement must be available in the catalog.  
14 | Data provenance and lineage are understood | Data lineage information must be available for all sensitive data. This information must at a minimum include the source from which the data was ingested or in which it was created in a cloud environment.  
  
## 1\. Data control compliance

This control requires that you can verify that all sensitive data is monitored for compliance with this framework using metrics.

The architecture uses metrics that show the extent to which each of the key controls are operational. The architecture also includes dashboards that indicate when the metrics don't meet defined thresholds.

The architecture includes detectors that publish findings and remediation recommendations when data assets don't meet a key control. These findings and recommendations are in JSON format and published to a [Pub/Sub topic](https://docs.cloud.google.com/pubsub/docs/create-topic) for distribution to subscribers. You can integrate your internal service desk or service management tools with the Pub/Sub topic so that incidents are automatically created in your ticketing system.

The architecture uses Dataflow to create an example subscriber to the findings events, which are then stored in a BigQuery instance that runs in the Data Governance project. Using a number of supplied views, you can query the data using BigQuery Studio in the Google Cloud console. You can also create reports using [Data Studio](https://docs.cloud.google.com/looker-studio) or other BigQuery-compatible business intelligence tools. Reports that you can view include the following:

  * Last run findings summary
  * Last run findings detail
  * Last run metadata
  * Last run data assets in scope
  * Last run dataset statistics



The following diagram shows the services that apply to this control.

![The Control 1 architecture components.](https://docs.cloud.google.com/static/docs/security/images/cdmc/cdmc-control1.svg)

To meet the requirements of this control, the architecture uses the following services:

  * Pub/Sub publishes findings.
  * Dataflow loads findings into a BigQuery instance.
  * BigQuery stores the findings data and provides summary views.
  * Data Studio provides dashboards and reports.



The following screenshot shows a sample Data Studio summary dashboard.

![Sample Data Studio summary
dashboard.](https://docs.cloud.google.com/static/docs/security/images/cdmc/cdmc-sample-looker-dashboard.png) The following screenshot shows a sample view of findings by data asset.

![Sample view of findings by data asset.](https://docs.cloud.google.com/static/docs/security/images/cdmc/cdmc-sample-findings.png)

## 2\. Data ownership is established for both migrated and cloud-generated data

To meet the requirements of this control, the architecture automatically reviews the data in the BigQuery data warehouse and adds data classification tags that indicate that owners are identified for all sensitive data.

Knowledge Catalog handles two types of metadata: technical metadata and business metadata. For a given project, Knowledge Catalog automatically catalogs BigQuery datasets, tables, and views and populates the technical metadata. Synchronization between the catalog and data assets is maintained on a near real-time basis.

The architecture uses [Tag Engine](https://github.com/GoogleCloudPlatform/datacatalog-tag-engine/tree/cloud-run) to add the following business metadata tags to a `CDMC controls` tag template in Knowledge Catalog:

  * `is_sensitive`: whether the data asset contains sensitive data (see Control 6 for data classification)
  * `owner_name`: the owner of the data
  * `owner_email`: the email address of the owner



The tags are populated using defaults that are stored in a reference BigQuery table in the Data governance project.

By default, the architecture sets the ownership metadata at the table level, but you can change the architecture so that metadata is set at the column level. For more information, see [Manage aspects and enrich metadata](https://docs.cloud.google.com/dataplex/docs/enrich-entries-metadata).

The following diagram shows the services that apply to this control.

![The Control 2 architecture components.](https://docs.cloud.google.com/static/docs/security/images/cdmc/cdmc-control2.svg)

To meet the requirements of this control, the architecture uses the following services:

  * Two BigQuery data warehouses: one stores the confidential data and the other stores the defaults for data asset ownership.
  * Knowledge Catalog stores ownership metadata through tag templates and tags.
  * Two Cloud Run instances, as follows: 
    * One instance runs Report Engine, which checks whether tags are applied and publishes results.
    * Another instance runs Tag Engine, which tags the data in the secured data warehouse.
  * Pub/Sub publishes findings.



To detect issues related to this control, the architecture checks whether sensitive data is assigned an owner name tag.

## 3\. Data sourcing and consumption are governed and supported by automation

This control requires classification of data assets and a data register of authoritative sources and authorized distributors. The architecture uses Knowledge Catalog to add the `is_authoritative` tag to the `CDMC controls` tag template. This tag defines whether the data asset is authoritative.

Knowledge Catalog catalogs BigQuery datasets, tables, and views with technical metadata and business metadata. Technical metadata is automatically populated and includes the resource URL, which is the location of the provisioning point. Business metadata is defined in the Tag Engine configuration file and includes the `is_authoritative` tag.

During the next scheduled run, Tag Engine populates the `is_authoritative` tag in the `CDMC controls` tag template from default values stored in a reference table in BigQuery.

The following diagram shows the services that apply to this control.

![The Control 3 architecture components.](https://docs.cloud.google.com/static/docs/security/images/cdmc/cdmc-control3.svg)

To meet the requirements of this control, the architecture uses the following services:

  * Two BigQuery data warehouses: one stores the confidential data and the other stores the defaults for the data asset authoritative source.
  * Knowledge Catalog stores authoritative source metadata through tags.
  * Two Cloud Run instances, as follows: 
    * One instance runs Report Engine, which checks whether tags are applied and publishes results.
    * Another instance runs Tag Engine, which tags the data in the secured data warehouse.
  * Pub/Sub publishes findings.



To detect issues related to this control, the architecture checks whether sensitive data is assigned the authoritative source tag.

## 4\. Data sovereignty and cross-border data movement are managed

This control requires the architecture to inspect the data registry for region-specific storage requirements and enforce usage rules. A report describes the geographical location of data assets.

The architecture uses Knowledge Catalog to add the `approved_storage_location` tag to the `CDMC controls` tag template. This tag defines the geographic location that the data asset is permitted to be stored in.

The actual location of the data is stored as technical metadata in BigQuery table details. BigQuery doesn't let administrators change the location of a dataset or table. Instead, if administrators want to change data location, they must [copy the dataset](https://docs.cloud.google.com/bigquery/docs/copying-datasets).

The [resource locations Organization Policy Service constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations) defines the Google Cloud regions that you can store data in. By default, the architecture sets the constraint on the Confidential data project, but you can set the constraint at an organization or folder level if preferred. Tag Engine replicates the permitted locations to the Knowledge Catalog tag template and stores the location in the `approved_storage_location` tag. If you activate Security Command Center Premium tier, and someone updates the resource locations Organization Policy constraint, Security Command Center generates [vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#org-findings) for resources stored outside of the updated policy.

[Access Context Manager](https://docs.cloud.google.com/access-context-manager/docs/overview) defines the geographic location that users must be in before they can access data assets. Using [access levels](https://docs.cloud.google.com/access-context-manager/docs/create-basic-access-level), you can specify which [regions](https://docs.cloud.google.com/access-context-manager/docs/access-level-attributes#regions) the requests can come from. You then [add the access policy](https://docs.cloud.google.com/access-context-manager/docs/create-access-policy) to the VPC Service Controls perimeter for the Confidential data project.

To track data movement, BigQuery maintains a full audit trail for every job and query against each dataset. The audit trail is stored in the BigQuery [Information Schema Jobs](https://docs.cloud.google.com/bigquery/docs/information-schema-jobs) view.

The following diagram shows the services that apply to this control.

![The Control 4 architecture components.](https://docs.cloud.google.com/static/docs/security/images/cdmc/cdmc-control4.svg)

To meet the requirements of this control, the architecture uses the following services:

  * Organization Policy defines and enforces the resource locations constraint.
  * Access Context Manager defines the locations that users can access data from.
  * Two BigQuery data warehouses: one stores the confidential data and the other hosts a remote function which is used to inspect the location policy.
  * Knowledge Catalog stores approved storage locations as tags.
  * Two Cloud Run instances, as follows: 
    * One instance runs Report Engine, which checks whether tags are applied and publishes results.
    * Another instance runs Tag Engine, which tags the data in the secured data warehouse.
  * Pub/Sub publishes findings.
  * Cloud Logging writes the audit logs.
  * Security Command Center reports on any findings related to resource location or data access.



To detect issues related to this control, the architecture includes a finding for whether the approved locations tag includes the location of the sensitive data.

## 5\. Data catalogs are implemented, used, and interoperable

This control requires that a data catalog exists, and that the architecture can scan new and updated assets to add metadata as required.

To meet the requirements of this control, the architecture uses Knowledge Catalog. Knowledge Catalog automatically logs Google Cloud assets, including BigQuery datasets, tables, and views. When you create a new table in BigQuery, Knowledge Catalog automatically registers the new table's technical metadata and schema. When you update a table in BigQuery, Knowledge Catalog updates its entries almost instantaneously.

The following diagram shows the services that apply to this control.

![The Control 5 architecture components.](https://docs.cloud.google.com/static/docs/security/images/cdmc/cdmc-control5.svg)

To meet the requirements of this control, the architecture uses the following services:

  * Two BigQuery data warehouses: one stores the confidential data and the other stores the non-confidential data.
  * Knowledge Catalog stores the technical metadata for tables and fields.



By default, in this architecture, Knowledge Catalog stores technical metadata from BigQuery. If required, you can [integrate Knowledge Catalog with other data sources](https://docs.cloud.google.com/dataplex/docs/ingest-custom-sources).

## 6\. Data classifications are defined and used

This assessment requires that data can be classified based on its sensitivity, such as whether it's PII, identifies clients, or meets some other standard that your organization defines. To meet the requirements of this control, the architecture creates a report of data assets and their sensitivity. You can use this report to verify whether the sensitivity settings are correct. In addition, each new data asset or change to an existing data asset results in an update to the data catalog.

Classifications are stored in the `sensitive_category` tag in the Knowledge Catalog tag template at the table level and the column level. A classification reference table lets you rank the available Sensitive Data Protection [information types](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-infotypes) (infoTypes), with higher rankings for more sensitive content.

To meet the requirements of this control, the architecture uses Sensitive Data Protection, Knowledge Catalog, and Tag Engine to add the following tags to sensitive columns in BigQuery tables:

  * `is_sensitive`: whether the data asset contains sensitive information
  * `sensitive_category`: the category of the data; one of the following: 
    * Sensitive Personal Identifiable Information
    * Personal Identifiable Information
    * Sensitive Personal Information
    * Personal Information
    * Public Information



You can change the data categories to meet your requirements. For example, you can add the Material Non-Public Information (MNPI) classification.

After Sensitive Data Protection [inspects the data](https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-storage), Tag Engine reads the per-asset `DLP results` tables to compile the findings. If a table contains columns with one or more sensitive infoTypes, the most notable infoType is determined and both the sensitive columns and the whole table are tagged as the category that has the highest rank. Tag Engine also assigns a corresponding [policy tag](https://docs.cloud.google.com/bigquery/docs/column-level-security-intro) to the column and assigns the `is_sensitive` boolean tag to the table.

You can use [Cloud Scheduler](https://docs.cloud.google.com/scheduler) to automate the Sensitive Data Protection inspection.

The following diagram shows the services that apply to this control.

![The Control 6 architecture components.](https://docs.cloud.google.com/static/docs/security/images/cdmc/cdmc-control6.svg)

To meet the requirements of this control, the architecture uses the following services:

  * Four BigQuery data warehouses store the following information: 
    * Confidential data
    * Sensitive Data Protection results information
    * Data classification reference data
    * Tag export information
  * Knowledge Catalog stores the classification tags.
  * Sensitive Data Protection inspects assets for sensitive infoTypes.
  * Compute Engine runs the Inspect Datasets script, which triggers a Sensitive Data Protection job for each BigQuery dataset.
  * Two Cloud Run instances, as follows: 
    * One instance runs Report Engine, which checks whether tags are applied and publishes results.
    * Another instance runs Tag Engine, which tags the data in the secured data warehouse.
  * Pub/Sub publishes findings.



To detect issues related to this control, the architecture includes the following findings:

  * Whether sensitive data is assigned a sensitive category tag.
  * Whether sensitive data is assigned a column-level sensitivity type tag.



## 7\. Data entitlements are managed, enforced, and tracked

By default, only creators and owners are assigned entitlements and access to sensitive data. In addition, this control requires that the architecture tracks all access to sensitive data.

To meet the requirements of this control, the architecture uses the `cdmc sensitive data classification` policy tag taxonomy in BigQuery to control access to columns that contain confidential data in BigQuery tables. The taxonomy includes the following policy tags:

  * Sensitive Personal Identifiable Information
  * Personal Identifiable Information
  * Sensitive Personal Information
  * Personal Information



Policy tags let you control who can view sensitive columns in BigQuery tables. The architecture maps these policy tags to sensitivity classifications which were derived from Sensitive Data Protection infoTypes. For example, the `sensitive_personal_identifiable_information` policy tag and the sensitive category maps to infoTypes such as `AGE`, `DATE_OF_BIRTH`, `PHONE_NUMBER`, and `EMAIL_ADDRESS`.

The architecture uses Identity and Access Management (IAM) to manage the groups, users, and service accounts that require access to the data. IAM permissions are granted to a given asset for table-level access. In addition, column-level access based on policy tags enables fine-grained access to sensitive data assets. By default, users don't have access to columns that have defined policy tags.

To help ensure that only authenticated users can access data, Google Cloud uses Cloud Identity, which you can federate with your existing identity providers to authenticate users.

This control also requires that the architecture checks regularly for data assets that don't have entitlements defined. The detector, which is managed by Cloud Scheduler, checks for the following scenarios:

  * A data asset includes a sensitive category, but there isn't a related policy tag.
  * A category doesn't match the policy tag.



When these scenarios happen, the detector generates findings that are published by Pub/Sub, and then are written to the `events` table in BigQuery by Dataflow. You can then distribute the findings to your remediation tool, as described in 1\. Data control compliance.

The following diagram shows the services that apply to this control.

![The Control 7 architecture components.](https://docs.cloud.google.com/static/docs/security/images/cdmc/cdmc-control7.svg)

To meet the requirements of this control, the architecture uses the following services:

  * A BigQuery data warehouse stores the confidential data and the policy tag bindings for fine-grained access controls.
  * IAM manages access.
  * Knowledge Catalog stores the table-level and column-level tags for the sensitive category.
  * Two Cloud Run instances, as follows: 
    * One instance runs Report Engine, which checks whether tags are applied and publishes results.
    * Another instance runs Tag Engine, which tags the data in the secured data warehouse.



To detect issues related to this control, the architecture checks whether sensitive data has a corresponding policy tag.

## 8\. Ethical access, use, and outcomes of data are managed

This control requires the architecture to store data sharing agreements from both the data provider and data consumers, including a list of approved consumption purposes. The consumption purpose for the sensitive data is then mapped to entitlements stored in BigQuery using [query labels](https://docs.cloud.google.com/bigquery/docs/adding-labels#adding-label-to-session). When a consumer queries sensitive data in BigQuery, they must specify a valid purpose which matches their entitlement (for example, `SET @@query_label = "use:3";`).

The architecture uses Knowledge Catalog to add the following tags to the `CDMC controls` tag template. These tags represent the data sharing agreement with the data provider:

  * `approved_use`: the approved use or users of the data asset
  * `sharing_scope_geography`: the list of geographic locations that the data asset can be shared in
  * `sharing_scope_legal_entity`: the list of agreed entities that can share the data asset



A separate BigQuery data warehouse includes the `entitlement_management` dataset with the following tables:

  * `provider_agreement`: the data sharing agreement with the data provider, including the agreed legal entity and geographic scope. This data provides the default values for the `sharing_scope_geography` and `sharing_scope_legal_entity` tags.
  * `consumer_agreement`: the data sharing agreement with the data consumer, including the agreed legal entity and geographic scope. Each agreement is associated with an IAM binding for the data asset.
  * `use_purpose`: the consumption purpose such as the usage description and permitted operations for the data asset.
  * `data_asset`: information about the data asset, such as the asset name and details about the data owner.



To audit data sharing agreements, BigQuery maintains a full audit trail for every job and query against each dataset. The audit trail is stored in the BigQuery [Information Schema Jobs](https://docs.cloud.google.com/bigquery/docs/information-schema-jobs) view. After you associate a query label with a session and run queries inside the session, you can collect audit logs for queries with that query label. For more information, see the [Audit log reference for BigQuery](https://docs.cloud.google.com/bigquery/docs/reference/auditlogs).

The following diagram shows the services that apply to this control.

![The Control 8 architecture components.](https://docs.cloud.google.com/static/docs/security/images/cdmc/cdmc-control8.svg)

To meet the requirements of this control, the architecture uses the following services:

  * Two BigQuery data warehouses: one stores the confidential data and the other stores the entitlement data, which includes the provider and consumer data sharing agreements and the approved usage purpose.
  * Knowledge Catalog stores the provider data sharing agreement information as tags.
  * Two Cloud Run instances, as follows: 
    * One instance runs Report Engine, which checks whether tags are applied and publishes results.
    * Another instance runs Tag Engine, which tags the data in the secured data warehouse.
  * Pub/Sub publishes findings.



To detect issues related to this control, the architecture includes the following findings:

  * Whether there is an entry for a data asset in the `entitlement_management` dataset.
  * Whether an operation is performed on a sensitive table with an expired use case (for example, the `valid_until_date` in the `consumer_agreement` table has passed).
  * Whether an operation is performed on a sensitive table with an incorrect label key.
  * Whether an operation is performed on a sensitive table with either a blank or an unapproved use-case label value.
  * Whether a sensitive table is queried with an unapproved operation method (for example, `SELECT` or `INSERT`).
  * Whether the recorded purpose that the consumer specified when querying the sensitive data matches the data sharing agreement.



## 9\. Data is secured and controls are evidenced

This control requires the implementation of data encryption and de-identification to help protect sensitive data and provide a record of these controls.

This architecture builds on Google default security, which includes [encryption at rest](https://docs.cloud.google.com/docs/security/encryption/default-encryption). In addition, the architecture lets you manage your own keys using customer-managed encryption keys (CMEK). [Cloud Key Management Service](https://docs.cloud.google.com/kms) lets you encrypt your data with software-backed encryption keys or FIPS 140-2 Level 3 validated hardware security modules (HSMs).

The architecture uses column-level [dynamic data masking](https://docs.cloud.google.com/bigquery/docs/column-data-masking-intro) configured through policy tags, and stores confidential data within a separate VPC Service Controls perimeter. You can also add application-level de-identification, which you can implement either on-premises or as part of the data ingestion pipeline.

By default, the architecture implements CMEK encryption with HSMs, but also supports Cloud External Key Manager (Cloud EKM).

The following table describes the example security policy that the architecture implements for the us-central1 region. You can adapt the policy to meet your requirements, including by adding different policies for different regions.

Data sensitivity | Default encryption method | Other permitted encryption methods | Default de-identification method | Other permitted de-identification methods  
---|---|---|---|---  
Public Information | Default Encryption | Any | None | Any  
Sensitive Personal Identifiable Information | CMEK with HSM | EKM | Nullify | SHA-256 Hash or Default Masking Value  
Personal Identifiable Information | CMEK with HSM | EKM | SHA-256 Hash | Nullify or Default Masking Value  
Sensitive Personal Information | CMEK with HSM | EKM | Default Masking Value | SHA-256 Hash or Nullify  
Personal Information | CMEK with HSM | EKM | Default Masking Value | SHA-256 Hash or Nullify  
  
The architecture uses Knowledge Catalog to add the `encryption_method` tag to the table-level `CDMC controls` tag template. The `encryption_method` defines the encryption method that is used by the data asset.

In addition, the architecture creates a `security policy template` tag to identify which de-identification method is applied to a particular field. The architecture uses the `platform_deid_method` which is applied using dynamic data masking. You can add the `app_deid_method`, and can populate it using the Dataflow and Sensitive Data Protection data ingestion pipelines that are included in the secured data warehouse blueprint.

The following diagram shows the services that apply to this control.

![The Control 9 architecture components.](https://docs.cloud.google.com/static/docs/security/images/cdmc/cdmc-control9.svg)

To meet the requirements of this control, the architecture uses the following services:

  * Two optional instances of Dataflow, one performs application-level de-identification and the other performs re-identification.
  * Three BigQuery data warehouses: one stores the confidential data, one stores the non-confidential data, and the third stores the security policy.
  * Knowledge Catalog stores the encryption and de-identification tag templates.
  * Two Cloud Run instances, as follows: 
    * One instance runs Report Engine, which checks whether tags are applied and publishes results.
    * Another instance runs Tag Engine, which tags the data in the secured data warehouse.
  * Pub/Sub publishes findings.



To detect issues related to this control, the architecture includes the following findings:

  * The value for the encryption method tag doesn't match the permitted encryption methods for specified sensitivity and location.
  * A table contains sensitive columns but the Security Policy Template tag contains an invalid platform-level de-identification method.
  * A table contains sensitive columns but the Security Policy Template tag is missing.



## 10\. A data privacy framework is defined and operational

This control requires that the architecture inspects the data catalog and classifications to determine whether you must create a data protection impact assessment (DPIA) report or a privacy impact assessment (PIA) report. Privacy assessments vary significantly between geographies and regulators. To determine whether an impact assessment is required, the architecture must consider the residency of the data, and the residency of the data subject.

The architecture uses Knowledge Catalog to add the following tags to the `Impact assessment` tag template:

  * `subject_locations`: the location of the subjects referred to by the data in this asset.
  * `is_dpia`: whether a data privacy impact assessment (DPIA) was completed for this asset.
  * `is_pia`: whether a privacy impact assessment (PIA) was completed for this asset.
  * `impact_assessment_reports`: external link to where the impact assessment report is stored.
  * `most_recent_assessment`: the date of the most recent impact assessment.
  * `oldest_assessment`: the date of the first impact assessment.



Tag Engine adds these tags to each sensitive data asset, as defined by control 6. The detector validates these tags against a policy table in BigQuery. The policy table defines valid combinations of data residency, subject location, data sensitivity (for example, whether it's PII), and what impact assessment type (either PIA or DPIA) is required.

The following diagram shows the services that apply to this control.

![The Control 10 architecture components.](https://docs.cloud.google.com/static/docs/security/images/cdmc/cdmc-control10.svg)

To meet the requirements of this control, the architecture uses the following services:

  * Four BigQuery data warehouses store the following information: 
    * Confidential data
    * Non-confidential data
    * Impact assessment policy and entitlements timestamps
    * Tag exports that are used for the dashboard
  * Knowledge Catalog stores the impact assessment details in tags within tag templates.
  * Two Cloud Run instances, as follows: 
    * One instance runs Report Engine, which checks whether tags are applied and publishes results.
    * Another instance runs Tag Engine, which tags the data in the secured data warehouse.
  * Pub/Sub publishes findings.



To detect issues related to this control, the architecture includes the following findings:

  * Sensitive data exists without an impact assessment template.
  * Sensitive data exists without a link to a DPIA or PIA report.
  * Tags don't meet the requirements in the policy table.
  * The impact assessment is older than the most recently approved entitlement for the data asset in the consumer agreement table.



## 11\. The data lifecycle is planned and managed

This control requires the ability to inspect all data assets to determine that a data lifecycle policy exists and is adhered to.

The architecture uses Knowledge Catalog to add the following tags to the `CDMC controls` tag template:

  * `retention_period`: the time, in days, to retain the table
  * `expiration_action`: whether to archive or purge the table when the retention period ends



By default, the architecture uses the following retention period and expiration action:

Data category | Retention period, in days | Expiration action  
---|---|---  
Sensitive Personal Identifiable Information | 60 | Purge  
Personal Identifiable Information | 90 | Archive  
Sensitive Personal Information | 180 | Archive  
Personal Information | 180 | Archive  
  
You can use the following options to implement data lifecycle management:

  * Combine BigQuery lifecycle features with serverless orchestration. In this case, the preceding tag values define the governance policy. Cloud Scheduler triggers a serverless workflow using [Workflows](https://docs.cloud.google.com/scheduler/docs/tut-workflows) or [Cloud Run function](https://docs.cloud.google.com/scheduler/docs/tut-gcf-http). This workflow reads the tag metadata and evaluates the expiration action. If the action is purge, the workflow creates a [table snapshot](https://docs.cloud.google.com/bigquery/docs/table-snapshots-intro) with an [expiration time](https://docs.cloud.google.com/bigquery/docs/managing-tables#updating_a_tables_expiration_time) to support soft deletion and recovery, and applies BigQuery [table expiration](https://docs.cloud.google.com/bigquery/docs/managing-tables#updating_a_tables_expiration_time) or [partition expiration](https://docs.cloud.google.com/bigquery/docs/managing-partitioned-tables#partition-expiration) policies to the source table. If the action is archive, the workflow completes the following:

    * [Exports the table data to Cloud Storage](https://docs.cloud.google.com/bigquery/docs/exporting-data) in Parquet format.
    * Registers a BigLake table to support external metadata tagging.
    * Copies the metadata and policy tags from the source table to the BigLake table (or re-applies the tags using Tag Engine).
    * Drops or expires the source table.
  * Deploy [Record Manager](https://github.com/GoogleCloudPlatform/bigquery-record-manager), an open source asset for BigQuery, to purge and archive BigQuery tables based on the preceding tag values and a configuration file. The purging procedure sets an expiration date on a table and creates a snapshot table with an [expiration time](https://docs.cloud.google.com/bigquery/docs/managing-tables#updating_a_tables_expiration_time) that is defined in the Record Manager configuration. By default, the expiration time is 30 days. During the soft-deletion period, you can retrieve the table. The archival procedure creates an external table for each BigQuery table that passes its retention period. The table is stored in Cloud Storage in Parquet format and upgraded to a [BigLake](https://docs.cloud.google.com/bigquery/docs/biglake-intro) table, which lets the external file be tagged with metadata in Knowledge Catalog. Record Manager then drops the source table to complete the archival process.




In both options, after data is archived to Cloud Storage, you can configure [Cloud Storage object lifecycle management](https://docs.cloud.google.com/storage/docs/lifecycle) to automatically transition older files to lower-cost storage classes.

The following diagram shows the services that apply to this control when you use BigQuery lifecycle features.

![The Control 11 architecture components with BigQuery lifecycle
features.](https://docs.cloud.google.com/static/docs/security/images/cdmc/cdmc-control11-new.svg)

To meet the requirements of this control, the architecture uses the following services:

  * Two BigQuery data warehouses: one stores the confidential data, and the other stores the data retention policy.
  * Cloud Storage provides archive storage.
  * Knowledge Catalog stores the retention period and action in tag templates and the tags.
  * Two Cloud Run instances, as follows: 
    * One instance runs Report Engine, which checks whether tags are applied, evaluates tables against the retention policy, and publishes results.
    * Another instance runs Tag Engine, which tags the data in the secured data warehouse based on corporate policy rules stored in the governance data warehouse.
  * Cloud Scheduler triggers the workflow to enact the expiration or archival actions.
  * Workflows or Cloud Run function runs the serverless workflow.
  * Pub/Sub publishes findings.
  * BigLake enables access control and metadata tagging on archived data.



The following diagram shows the services that apply to this control when you use Record Manager.

![The Control 11 architecture components with Record
Manager.](https://docs.cloud.google.com/static/docs/security/images/cdmc/cdmc-control11.svg)

To meet the requirements of this control, the architecture uses the following services:

  * Two BigQuery data warehouses: one stores the confidential data, and the other stores the data retention policy.
  * Two Cloud Storage buckets, one provides archive storage and the other stores records.
  * Knowledge Catalog stores the retention period and action in tag templates and the tags.
  * Three Cloud Run instances, as follows: 
    * One instance runs Report Engine, which checks whether tags are applied and publishes results.
    * Another instance runs Tag Engine, which tags the data in the secured data warehouse.
    * Another instance runs Record Manager, which automates the purging and archiving of BigQuery tables.
  * Pub/Sub publishes findings.



To detect issues related to this control, the architecture includes the following findings:

  * The expiration action for a sensitive asset isn't aligned with the policy for the asset's location.
  * The retention period for a sensitive asset isn't aligned with the policy for the asset's location.
  * Sensitive data exists without a retention period or expiration action tags.



## 12\. Data quality is managed

This control requires the ability to measure the quality of the data based on data profiling or user-defined metrics.

The architecture includes the ability to define data quality rules for either an individual or aggregate value and assign thresholds to a specific table column. It includes tag templates for correctness and completeness. Knowledge Catalog adds the following tags to each tag template:

  * `column_name`: the name of the column that the metric applies to
  * `metric`: the name of the metric or quality rule
  * `rows_validated`: the number of validated rows
  * `success_percentage`: the percentage of values which satisfy this metric
  * `acceptable_threshold`: the acceptable threshold for this metric
  * `meets_threshold`: whether the quality score (the `success_percentage` value) meets the acceptable threshold
  * `most_recent_run`: the most recent time that the metric or quality rule was run



The following diagram shows the services that apply to this control.

![The Control 12 architecture components.](https://docs.cloud.google.com/static/docs/security/images/cdmc/cdmc-control12.svg)

To meet the requirements of this control, the architecture uses the following services:

  * Three BigQuery data warehouses: one stores the sensitive data, one stores the non-sensitive data, and the third stores the quality rule metrics.
  * Knowledge Catalog stores the data quality results in tag templates and tags.
  * Cloud Scheduler defines when Cloud Data Quality Engine runs.
  * Three Cloud Run instances, as follows: 
    * One instance runs Report Engine, which checks whether tags are applied and publishes results.
    * Another instance runs Tag Engine, which tags the data in the secured data warehouse.
    * The third instance runs the [Cloud Data Quality Engine](https://github.com/GoogleCloudPlatform/cloud-data-quality).
  * Cloud Data Quality Engine defines data quality rules and schedules data quality checks for tables and columns.
  * Pub/Sub publishes findings.



A Data Studio dashboard displays the data quality reports for both the table levels and column levels.

To detect issues related to this control, the architecture includes the following findings:

  * Data is sensitive, but no data quality tag templates are applied (correctness and completeness).
  * Data is sensitive but the data quality tag isn't applied to the sensitive column.
  * Data is sensitive, but data quality results aren't within the threshold set in the rule.
  * Data isn't sensitive and data quality results aren't within the threshold that was set by the rule.



As an alternative to the Cloud Data Quality Engine, you can configure [Knowledge Catalog auto data quality](https://docs.cloud.google.com/dataplex/docs/auto-data-quality-overview).

## 13\. Cost management principles are established and applied

This control requires the ability to inspect data assets to confirm cost usage, based on policy requirements and the data architecture. Cost metrics should be comprehensive and not limited to storage use and movement.

The architecture uses Knowledge Catalog to add the following tags to the `cost_metrics` tag template:

  * `total_query_bytes_billed`: total number of query bytes that were billed for this data asset since the start of the current month.
  * `total_storage_bytes_billed`: total number of storage bytes that were billed for this data asset since the start of the current month.
  * `total_bytes_transferred`: sum of bytes transferred cross-region into this data asset.
  * `estimated_query_cost`: estimated query cost, in US dollars, for the data asset for the current month.
  * `estimated_storage_cost`: estimated storage cost, in US dollars, for the data asset for the current month.
  * `estimated_egress_cost`: estimated egress in US dollars for the current month in which data asset was used as a destination table.



The architecture exports pricing information from Cloud Billing to a BigQuery table named `cloud_pricing_export`.

The following diagram shows the services that apply to this control.

![The Control 13 architecture components.](https://docs.cloud.google.com/static/docs/security/images/cdmc/cdmc-control13.svg)

To meet the requirements of this control, the architecture uses the following services:

  * Cloud Billing provides billing information.
  * Knowledge Catalog stores the cost information in tag templates and tags.
  * BigQuery stores the exported pricing information and the query historical job information through its built-in [INFORMATION_SCHEMA](https://docs.cloud.google.com/bigquery/docs/information-schema-intro) view.
  * Two Cloud Run instances, as follows: 
    * One instance runs Report Engine, which checks whether tags are applied and publishes results.
    * Another instance runs Tag Engine, which tags the data in the secured data warehouse.
  * Pub/Sub publishes findings.



To detect issues related to this control, the architecture checks whether sensitive data assets exist without having cost metrics associated with them.

## 14\. Data provenance and lineage are understood

This control requires the ability to inspect the traceability of the data asset from its source and any changes to the data asset lineage.

To maintain information about data provenance and lineage, the architecture uses the [built-in Data Lineage features](https://docs.cloud.google.com/dataplex/docs/about-data-lineage) in Knowledge Catalog. Additionally, the data ingestion scripts define the ultimate source and add the source as an additional node to the data lineage graph.

To meet the requirements of this control, the architecture uses Knowledge Catalog to add the `ultimate_source` tag to the `CDMC controls` tag template. The `ultimate_source` tag defines the source for this data asset.

The following diagram shows the services that apply to this control.

![The Control 14 architecture components.](https://docs.cloud.google.com/static/docs/security/images/cdmc/cdmc-control14.svg)

To meet the requirements of this control, the architecture uses the following services:

  * Two BigQuery data warehouses: one stores the confidential data, and the other stores the ultimate source data.
  * Knowledge Catalog stores the ultimate source in tag templates and tags.
  * Data ingestion scripts load the data from Cloud Storage, define the ultimate source and add the source to the data lineage graph.
  * Two Cloud Run instances, as follows: 
    * One instance runs Report Engine, which checks whether tags are applied and publishes results.
    * Another instance runs Tag Engine, which tags the data in the secured data warehouse.
  * Pub/Sub publishes findings.



To detect issues related to this control, the architecture includes the following checks:

  * Sensitive data is identified with no ultimate source tag.
  * Lineage graph isn't populated for sensitive data assets.



## Tag reference

This section describes the tag templates and tags that this architecture uses to meet the requirements of the CDMC key controls.

### Table-level CDMC control tag templates

The following table lists the tags that are part of the CDMC control tag template and that are applied to tables.

Tag | Tag ID | Applicable key control  
---|---|---  
Approved Storage Location | `approved_storage_location` | 4  
Approved Use | `approved_use` | 8  
Data Owner Email | `data_owner_email` | 2  
Data Owner Name | `data_owner_name` | 2  
Encryption Method | `encryption_method` | 9  
Expiration Action | `expiration_action` | 11  
Is Authoritative | `is_authoritative` | 3  
Is Sensitive | `is_sensitive` | 6  
Sensitive Category | `sensitive_category` | 6  
Sharing Scope Geography | `sharing_scope_geography` | 8  
Sharing Scope Legal Entity | `sharing_scope_legal_entity` | 8  
Retention Period | `retention_period` | 11  
Ultimate Source | `ultimate_source` | 14  
  
### Impact Assessment tag template

The following table lists the tags that are part of the Impact Assessment tag template and that are applied to tables.

Tag | Tag ID | Applicable key control  
---|---|---  
Subject Locations | `subject_locations` | 10  
Is DPIA Impact Assessment | `is_dpia` | 10  
Is PIA Impact Assessment | `is_pia` | 10  
Impact Assessment Reports | `impact_assessment_reports` | 10  
Most Recent Impact Assessment | `most_recent_assessment` | 10  
Oldest Impact Assessment | `oldest_assessment` | 10  
  
### Cost Metrics tag template

The following table lists the tags that are part of the Cost Metrics tag template and that are applied to tables.

Tag | Tag ID | Applicable key control  
---|---|---  
Estimated Query Cost | `estimated_query_cost` | 13  
Estimated Storage Cost | `estimated_storage_cost` | 13  
Estimated Egress Cost | `estimated_egress_cost` | 13  
Total Query Bytes Billed | `total_query_bytes_billed` | 13  
Total Storage Bytes Billed | `total_storage_bytes_billed` | 13  
Total Bytes Transferred | `total_bytes_transferred` | 13  
  
### Data Sensitivity tag template

The following table lists the tags that are part of the Data Sensitivity tag template and that are applied to fields.

Tag | Tag ID | Applicable key control  
---|---|---  
Sensitive Field | `sensitive_field` | 6  
Sensitive Type | `sensitive_category` | 6  
  
### Security Policy tag template

The following table lists the tags that are part of the Security Policy tag template and that are applied to fields.

Tag | Tag ID | Applicable key control  
---|---|---  
Application De-Identification Method | `app_deid_method` | 9  
Platform De-Identification Method | `platform_deid_method` | 9  
  
### Data Quality tag templates

The following table lists the tags that are part of the Completeness and Correctness Data Quality tag templates and that are applied to fields.

Tag | Tag ID | Applicable key control  
---|---|---  
Acceptable Threshold | `acceptable_threshold` | 12  
Column Name | `column_name` | 12  
Meets Threshold | `meets_threshold` | 12  
Metric | `metric` | 12  
Most Recent Run | `most_recent_run` | 12  
Rows Validated | `rows_validated` | 12  
Success Percentage | `success_percentage` | 12  
  
### Field-level CDMC policy tags

The following table lists the policy tags that are part of the CDMC Sensitive Data Classification policy tag taxonomy and that are applied to fields. These policy tags restrict field-level access and enable platform level data de-identification.

Data Classification | Tag Name | Applicable key control  
---|---|---  
Personal Identifiable Information | `personal_identifiable_information` | 7  
Personal Information | `personal_information` | 7  
Sensitive Personal Identifiable Information | `sensitive_personal_identifiable_information` | 7  
Sensitive Personal Information | `sensitive_personal_data` | 7  
  
### Prepopulated technical metadata

The following table lists the technical metadata that is synchronized by default in Knowledge Catalog for all BigQuery data assets.

Metadata | Applicable key control  
---|---  
Asset Type | —  
Creation Time | —  
Expiration Time | 11  
Location | 4  
Resource URL | 3  
  
## What's next

  * Learn more about the [CDMC framework](https://edmcouncil.org/frameworks/cdmc/) on the EDM Council website.
  * Read about the security controls used by the [secured data warehouse blueprint](https://docs.cloud.google.com/architecture/confidential-data-warehouse-blueprint).
  * Track training data provenance and pipeline transformations for AI and machine learning workloads with [Knowledge Catalog data lineage](https://docs.cloud.google.com/dataplex/docs/about-data-lineage).
  * Learn more about [Tag Engine](https://github.com/GoogleCloudPlatform/datacatalog-tag-engine/tree/cloud-run).
  * Review sample automation scripts in the archived [Google Cloud CDMC Reference Architecture](https://github.com/GoogleCloudPlatform/cdmc) repository on GitHub.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
