---
url: https://docs.cloud.google.com/migration-center/docs/migration-modernization-tools/
title: Migration tools \u00a0|\u00a0 Migration Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:38:25.718241+00:00
---

# Migration tools  |  Migration Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migration-center/docs/migration-modernization-tools/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migration Center ](https://docs.cloud.google.com/migration-center/docs)
  * [ Guides ](https://docs.cloud.google.com/migration-center/docs/migration-center-overview)



Send feedback 

#  Migration tools Stay organized with collections  Save and categorize content based on your preferences. 

Migration tools are at the center of migration execution. They allow you to move your existing workloads to Google Cloud and to take advantage of Google Cloud managed services when you modernize your infrastructure.

This document presents the main tools that Google Cloud professional service teams use during migration projects.

## Google Cloud tools

This table presents some of the migration tools available in Google Cloud.

**Strategy** | **Tools** | **Source** | **Destination** | **Description**  
---|---|---|---|---  
**Lift and shift** | [Migrate to Virtual Machines](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0) | 

  * On-premises VMware VMs


  * VMs from other cloud environments

| Compute Engine  
| Tool to migrate virtual machines from on-premises and cloud environments to Google Cloud.  
  
[VMware HCX](https://docs.cloud.google.com/vmware-engine/docs/workloads/howto-migrate-vms-using-hcx) | 

  * On-premises VMware VMs


  * VMware VMs running in alternate clouds

| Google Cloud VMware Engine | Tool to migrate virtual machines (VMs) from on-premises environments to Google Cloud VMware Engine. VMware HCX abstracts vSphere-based on-premises and cloud resources and presents them to applications as one continuous resource, creating a hybrid infrastructure.  
**Replatform** | [Migrate to Containers](https://docs.cloud.google.com/migrate/containers/docs) | [On-premises physical servers, VMs, GKE](https://docs.cloud.google.com/migrate/containers/docs/m2c-cli/compatible-components) | [GKE, Autopilot, GKE Enterprise, Cloud Run](https://docs.cloud.google.com/migrate/containers/docs/getting-started) | Tool used to convert VM-based workloads into containers in Google Kubernetes Engine (GKE) or GKE Enterprise. Workloads can be migrated from VMs running on either VMware on-premises, AWS, Azure, or Compute Engine, giving the flexibility to containerize the existing workloads with ease.  
[Datastream](https://docs.cloud.google.com/datastream/docs/overview) | PostgreSQL (including AlloyDB for PostgreSQL and AlloyDB Omni), MySQL, SQL Server, Oracle | Cloud Storage, BigQuery | This tool is a serverless change data capture (CDC) and replication service that lets you synchronize data reliably, and with minimal latency. It provides seamless replication of data from operational databases into BigQuery, and supports writing the change event stream into Cloud Storage. You can also integrate Datastream with Dataflow templates to build custom workflows for loading data into destinations such as Cloud SQL and Spanner.  
[Database Migration Service](https://docs.cloud.google.com/database-migration/docs/overview) | PostgreSQL, MySQL, SQL Server, Oracle | Cloud SQL, AlloyDB for PostgreSQL | This tool is a serverless service that helps migrate PostgreSQL workloads into Cloud SQL and AlloyDB for PostgreSQL, MySQL and SQL Server workloads into Cloud SQL, and Oracle workloads into Cloud SQL for PostgreSQL or AlloyDB for PostgreSQL. Database Migration Service streamlines networking workflows, manages the initial snapshot and ongoing replication, and provides a status of the migration operations.  
**Refactor** | [BigQuery Data Transfer Service](https://docs.cloud.google.com/bigquery/docs/dts-introduction) | Teradata, Amazon RedShift | BigQuery | This tool automates data movement from software-as-a-service apps to BigQuery on a scheduled, managed basis.  
  
Based on the nature of the workloads that you want to migrate, you might want to integrate other tools with your migration tools architecture. The following list includes additional migration tools:

  * [Storage Transfer Service](https://docs.cloud.google.com/storage-transfer) lets you bring data to Cloud Storage from other cloud providers, online resources, or local data (for example: S3, Blob, Data Lake, on-premises file systems).
  * [Transfer Appliance](https://docs.cloud.google.com/transfer-appliance) is a hardware appliance you can use to migrate large volumes of data (recommended for data that exceeds 20 TBs and up to 1 petabyte) to Google Cloud without disrupting business operations.
  * [Image Import](https://docs.cloud.google.com/compute/docs/import/importing-virtual-disks) lets you to import virtual disks in your on-premises environment with software and configurations that you need (a.k.a. golden disks or golden images) into Google Cloud and uses the resulting image to create virtual machines. The tool supports most virtual disk file formats, including VMDK and VHD.



## Third-party tools

The following list includes third-party migration tools. The list is meant as a reference only, and doesn't represent a statement of support by Google.

  * [RackWare Management Module (RMM)](https://console.cloud.google.com/marketplace/browse?q=rackware) is a fully-automated enterprise-grade migration solution that lets you migrate physical and virtual servers from any data center or public cloud into Google Cloud. It is listed in Google Cloud Marketplace, and you can purchase a license in two ways:

    * Within the Cloud Marketplace, by selecting [RackWare Cloud Migration SaaS and API](https://console.cloud.google.com/marketplace/product/rackware-public/rackware-cloud-migration-saas).
    * Directly from RackWare, by selecting [RackWare Cloud Migration Virtual Machine](https://console.cloud.google.com/marketplace/product/rackware-public/rackware-cloud-migration-virtual-machine).
  * [SUREedge](https://console.cloud.google.com/marketplace/product/persistent-mp-public/sureedge-migrator-byol) is a tool that lets you migrate physical and virtual environments to Google Cloud when Migrate to Virtual Machines might not be a fit, for example for on-premises non-vSphere virtualized environments.

  * [Data Validation Tool](https://github.com/GoogleCloudPlatform/professional-services-data-validator) is an open sourced Python CLI tool based on the Ibis framework that compares heterogeneous data source tables with multi-leveled validation functions. Data validation is a critical step in a Data Warehouse, Database or Data Lake migration project.

  * [HarbourBridge: Spanner Evaluation and Migration](https://github.com/cloudspannerecosystem/harbourbridge) is a standalone open source tool for Spanner evaluation and migration, using data from an existing PostgreSQL, MySQL, SQL Server, Oracle or DynamoDB database.

  * [HBase Tools](https://github.com/googleapis/java-bigtable-hbase/tree/bigtable-1.x/bigtable-hbase-1.x-parent/bigtable-hbase-1.x-tools) help HBase users with migrations to Bigtable.

  * [Migrate Hive tables to BigQuery](https://github.com/GoogleCloudPlatform/professional-services/tree/main/tools/hive-bigquery) framework migrates data from Hive to BigQuery using Cloud SQL to keep track of the migration progress.




## Build and deploy automation and CI/CD tools

The automation of building and deployment within a CI/CD framework is an essential part of the migration process.

[Cloud Build](https://docs.cloud.google.com/build) is a service that executes your builds on Google Cloud. Cloud Build can import source code from Cloud Storage, Cloud Source Repositories, GitHub, or Bitbucket, execute a build to your specifications, and produce artifacts such as Docker containers or Java archives.

[Artifact Registry](https://docs.cloud.google.com/artifact-registry) provides a single location for managing packages and Docker container images. It integrates with CI/CD tools and Google Cloud runtime environments so that you can manage the full artifact lifecycle.

[Cloud Deploy](https://docs.cloud.google.com/deploy) is a managed service that automates delivery of your applications to a series of target environments in a defined promotion sequence.

If you have containerized applications, you can deploy them with [Kubernetes](https://kubernetes.io/) and managed services such as [Google Kubernetes Engine](https://docs.cloud.google.com/kubernetes-engine). To deploy into a serverless environment, you can use tools such as [App Engine flexible environment](https://docs.cloud.google.com/appengine/docs/flexible), [Cloud Run functions](https://docs.cloud.google.com/functions), and [Cloud Run](https://docs.cloud.google.com/run).

## Testing tools

As you migrate workloads to Google Cloud, you need to test these workloads for specific functional and non-functional scenarios with a view to measure and mitigate the impact on functionality, integration, security, performance, and availability.

The choice of testing tools depends on several factors, such as the following:

  * Compatibility with technology stacks of workloads
  * Degree of test automation
  * Integration with CI/CD framework
  * Defect logging and management
  * Test project and program management



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
