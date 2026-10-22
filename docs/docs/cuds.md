---
url: https://docs.cloud.google.com/docs/cuds/
title: Committed use discounts \u00a0|\u00a0 Get started \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:12:54.910437+00:00
---

# Committed use discounts  |  Get started  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/cuds/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Get started ](https://docs.cloud.google.com/docs/get-started)
  * [ Guides ](https://docs.cloud.google.com/docs/overview)



Send feedback 

#  Committed use discounts Stay organized with collections  Save and categorize content based on your preferences. 

This document provides information about committed use discounts (CUDs) for Google Cloud and how they apply for various services.

**Note** : This document discusses some spend-based committed use discounts (CUDs) that automatically migrate to a new consumption model, which leverages discounts rather than credits. The migration date is indicated by a notification in the Google Cloud console Billing Overview page. For more information about the improvements, the affected CUDs, and any required actions on your part, see [Spend-based CUDs](https://docs.cloud.google.com/docs/cuds-multiprice). 

CUDs provide discounted prices for eligible Google Cloud resources in exchange for purchasing committed use contracts (also known as commitments). When you purchase Google Cloud commitments, you commit to either using a minimum level of resources or spending a minimum amount, for a term duration of one or three years.

CUDs for Google Cloud are broadly available as spend-based or resource-based CUDs and cover a wide range of services and resources. You can choose the type of commitment that you want to purchase depending on the service that you use and whether you have predictable or unpredictable resource needs.

## Spend-based commitments

Spend-based CUDs provide a discount in exchange for your commitment to spend a minimum amount for any of the services listed in this section. The discount applies to the set of eligible resources for each service and the commitment term is one or three years.

With standard spend-based CUDs, you receive discounted rates until your hourly spend on eligible resources and services meets your hourly committed spend amount. With Flexible Savings Plans, your commitment is measured over a monthly entitlement window. Any overage usage that takes your spend amount over your committed amount is charged at the on-demand rate.

Spend-based CUDs apply to eligible usage in any projects that the Cloud Billing account pays for.

Depending on the Google Cloud service that you use, you can purchase spend-based commitments in one of the following ways:

  * Compute flexible commitments
  * Flexible Savings Plans
  * Service-specific spend-based commitments



### Compute flexible commitments

Compute flexible commitments are ideal for scenarios where you have predictable Google Cloud spend needs that span usage beyond a single service. You can purchase a single flexible commitment to cover your eligible spend across the following services. See these links for details:

  * [CUDs documentation for Compute Engine](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview)
  * [CUDs documentation for GKE](https://docs.cloud.google.com/kubernetes-engine/cud)
  * [CUDs documentation for Cloud Run](https://docs.cloud.google.com/run/cud)



### Flexible Savings Plans

Flexible Savings Plans (FSPs) provide cross-product spend-based discounts for eligible Google Cloud workloads, such as generative AI models and product offerings across first-party, open-source, and participating third-party models. Unlike standard spend-based CUDs that evaluate usage against an hourly entitlement window, FSPs evaluate usage over a **monthly entitlement window** , providing flexibility for workloads with variable or spiky usage patterns.

For details, see [Flexible Savings Plans](https://docs.cloud.google.com/docs/cuds-flexible-savings-plans).

### Service-specific spend-based commitments

These commitments are ideal for scenarios where you have predictable spend needs within a Google Cloud service. You purchase these commitments separately for each Google Cloud service, and CUDs from these commitments apply only to spend within that service. Service-specific spend-based CUDs are available for the following Google Cloud services. Some commitments from this list are no longer available for purchase, but Google supports any existing, active commitments until they expire.

  * AlloyDB for PostgreSQL
  * Backup and DR Service
  * BigQuery
  * Bigtable
  * Dataflow
  * Firestore
  * Spanner
  * Cloud SQL
  * Google Cloud Managed Service for Apache Kafka
  * Google Cloud NetApp Volumes
  * Google Cloud VMware Engine
  * Memorystore
  * Backup for GKE _(no longer available for purchase)_
  * Cloud Run _(no longer available for purchase)_
  * Google Kubernetes Engine (Autopilot) _(no longer available for purchase)_



#### AlloyDB for PostgreSQL

AlloyDB for PostgreSQL committed use discounts are spend-based CUDs that apply to all AlloyDB for PostgreSQL instance vCPU and memory usage. The discount applies to AlloyDB for PostgreSQL instances in any project or region that is associated with a single Cloud Billing account.

AlloyDB for PostgreSQL commitments _don't apply_ to storage, backup, and network egress.

For current rates, see [AlloyDB for PostgreSQL pricing](https://cloud.google.com/alloydb/pricing#cpu-mem-pricing).

#### Backup and DR Service

[Backup and DR (for VMware Engine) committed use discounts](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/cud) apply to the combined node usage in a region. This gives you low, predictable costs, without the need to make any manual changes or updates yourself. They apply to VMware Engine backups in the regions where the service is available and to which you have committed.

[Backup and DR (for protecting Oracle databases into a backup vault) committed use discounts](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/cud) apply to aggregate Oracle database protection into backup vault usage. This gives you low, predictable costs, without the need to make any manual changes or updates yourself. This flexibility saves you time and helps you to save more by achieving high utilization rates across your commitments.

For current rates, see [Backup and DR pricing](https://cloud.google.com/backup-disaster-recovery/pricing).

#### Backup for GKE (no longer available for purchase)

**Note:** Backup for GKE service-specific commitments are no longer available for purchase. Google supports any existing and active commitments until they expire.

[Backup for GKE committed use discounts](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/cud) are spend-based CUDs that apply to Backup for GKE backup management, that is Pods per plan in a region. Committed use discounts don't apply to backup storage (GiB) or inter-region data transfer (GiB).

For current rates, see [Backup for GKE CUDs pricing](https://cloud.google.com/kubernetes-engine/pricing#backup-for-gke).

#### BigQuery

[BigQuery CUDs](https://docs.cloud.google.com/bigquery/docs/bigquery-cud) provide discounted prices in exchange for your commitment to use BigQuery PAYG compute capacity for a one- or three-year term, with the commitment fee billed monthly. BigQuery CUDs apply to all compute types.

For current rates, see [BigQuery pricing](https://cloud.google.com/bigquery/pricing).

#### Bigtable

As a Bigtable customer, you can purchase a commitment to receive a committed use discount on the price of Bigtable nodes. The discount applies to nodes in any project or region that is associated with a single Cloud Billing account. The discount does not apply to the cost of storage, backup storage, or network egress. For details, see [ Bigtable committed use discounts](https://docs.cloud.google.com/bigtable/docs/cuds). For current rates, see [ Bigtable pricing](https://cloud.google.com/bigtable/pricing).

#### Cloud Run (no longer available for purchase)

**Note:** Cloud Run service-specific commitments are no longer available for purchase. Google supports any existing and active commitments until they expire. If you want new commitments for this service, then purchase Compute flexible commitments instead.

[Cloud Run committed use discounts](https://docs.cloud.google.com/run/cud) apply to all aggregated Cloud Run CPU, memory, and request usage in a region, giving you low, predictable costs when your code is running in one of the supported container ecosystems. Cloud Run commitments _don't apply_ to networking changes.

For current rates, see the [Cloud Run pricing details](https://cloud.google.com/run/pricing#tables).

#### Dataflow

[Dataflow committed use discounts](https://docs.cloud.google.com/dataflow/docs/cuds) apply to your spending on the Dataflow compute capacity used by streaming jobs across projects. The discount applies to any eligible usage in Dataflow projects associated with the Cloud Billing account used to purchase the commitment, regardless of instance configuration or region. All CUDs apply to both regional and multi-region configurations.

The discount doesn't apply to the cost of worker CPU and memory for batch and FlexRS jobs, Dataflow Shuffle data processed, Data Compute Units (DCUs) for batch jobs, Persistent Disk storage, Cloud GPUs, snapshots, and confidential VMs.

For current rates and other details, see [Dataflow pricing](https://cloud.google.com/dataflow/pricing).

#### Firestore

As a Firestore customer, you can purchase a commitment to receive a committed use discount on the price of Firestore Read/Write/Delete operations. The discount applies to Read/Write/Delete operations in any project or region that is associated with a single Cloud Billing account. The discount doesn't apply to any other Firestore resource. For details, see [Firestore committed use discounts](https://docs.cloud.google.com/firestore/docs/cuds).

For current rates, see [Firestore pricing](https://cloud.google.com/firestore/pricing).

#### Spanner

[Spanner committed use discounts](https://docs.cloud.google.com/spanner/docs/cuds) apply to all Spanner compute capacity associated with a single Cloud Billing account, regardless of region. This includes all instances in all projects, whether configured as single-region or multi-region instances.

Spanner CUDs _don't apply_ to Spanner storage, backup, or network egress.

For current rates and other details, see [Spanner pricing](https://cloud.google.com/spanner/pricing).

#### Cloud SQL

[Cloud SQL committed use discounts](https://docs.cloud.google.com/sql/cud) provide you the flexibility to use any machine shapes with the supported Cloud SQL database engines, without having to modify your commitments. They apply to all Cloud SQL database instance vCPU and memory usage for the service in the region you purchased the commitments, _except_ shared CPU machine types (such as db-f1-micro and db-g1-small). The commitments apply to usage from all supported database engines, such as MySQL, PostgreSQL, and SQL Server.

Cloud SQL commitments _don't apply_ to persistent disk snapshots, storage, IP addresses, network egress, or licensing.

For current rates, see [Cloud SQL pricing](https://cloud.google.com/sql/pricing).

#### Google Cloud Managed Service for Apache Kafka

[Managed Service for Apache Kafka committed use discounts (CUDs)](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/cuds) are discounts that apply to the Kafka compute (vCPU and RAM) costs for running Managed Service for Apache Kafka clusters across projects. You can apply the CUDs to any Managed Service for Apache Kafka project that is associated with the Cloud Billing account used to purchase the commitment. You can apply CUDs to any available region. You can't apply the Managed Service for Apache Kafka CUDs to the cost of storage, networking or Private Service Connect.

For current rates and other details, see [Managed Service for Apache Kafka pricing](https://cloud.google.com/managed-service-for-apache-kafka/pricing).

#### Google Cloud NetApp Volumes

[Google Cloud NetApp Volumes committed use discounts](https://docs.cloud.google.com/netapp/volumes/docs/cuds) apply to the aggregate storage capacity on Flex, Standard, Premium, and Extreme service levels and regions at your billing account level. CUDs can keep your storage costs low when you have predictable storage needs. NetApp Volumes CUDs are'nt available for volume replications and backups.

For current rates, see [NetApp Volumes pricing](https://docs.cloud.google.com/netapp/volumes/pricing).

#### Google Cloud VMware Engine

[VMware Engine committed use discounts](https://docs.cloud.google.com/vmware-engine/docs/cud) apply to aggregate VMware Engine node usage in a region, giving you low, predictable costs, without the need to make any manual changes or updates yourself. They apply to VMware Engine node CPU and memory usage in the regions where the service is available and you have committed.

Current rates and supported regions for Google Cloud VMware Engine CUDs are detailed on the [VMware Engine pricing page](https://cloud.google.com/vmware-engine/pricing).

#### Google Kubernetes Engine (Autopilot) (no longer available for purchase)

**Note:** Google Kubernetes Engine (Autopilot) service-specific commitments are no longer available for purchase. Google supports any existing and active commitments until they expire. If you want new commitments for this service, then purchase Compute flexible commitments instead.

[Google Kubernetes Engine (Autopilot Mode) committed use discounts](https://docs.cloud.google.com/kubernetes-engine/cud) apply to all Autopilot Pod workload vCPU, memory, and ephemeral storage usage in the region in which you have purchased commitments. Google Kubernetes Engine (Autopilot Mode) CUDs don't apply to the cluster management fee or to GKE Standard mode compute nodes.

For current rates, see the [Google Kubernetes Engine pricing details](https://cloud.google.com/kubernetes-engine/pricing#autopilot_mode).

#### Memorystore

Memorystore CUDs apply to Memorystore for Valkey, Memorystore for Redis Cluster, Memorystore for Redis, and Memorystore for Memcached usage. A Memorystore CUD gives you the flexibility to use Valkey, Redis Cluster, Redis, or Memcached instance spending toward a commitment on a single Cloud Billing account.

Memorystore commitments _don't apply_ to Cloud Storage storage for backups, persistence, network egress, or Memorystore for Redis M1 capacity tier instances (less than 5 GB).

For current rates, see the following pages:

  * [Memorystore for Valkey committed use discounts](https://docs.cloud.google.com/memorystore/docs/valkey/cuds)
  * [Memorystore for Redis Cluster committed use discounts](https://docs.cloud.google.com/memorystore/docs/cluster/cuds)
  * [Memorystore for Redis committed use discounts](https://docs.cloud.google.com/memorystore/docs/redis/cuds)
  * [Memorystore for Memcached committed use discounts](https://docs.cloud.google.com/memorystore/docs/memcached/cuds)



## Resource-based commitments

Resource-based CUDs are available only for Compute Engine. [Compute Engine resource-based CUDs](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts) provide discounts in exchange for committing to using a minimum amount of Compute Engine resources in a specific region. These CUDs are ideal when you have predictable resource needs. You can purchase Compute Engine resource-based commitments for the following hardware, software, and block storage resources for a duration of up to six years:

  * vCPUs
  * Memory
  * GPUs
  * Local SSD disks
  * Sole-tenant nodes
  * Operating system (OS) licenses
  * Hyperdisk Exapools



Commitments for hardware resources, commitments for OS licenses, and commitments for block storage remain distinct from one another. You can't purchase a single commitment that covers resources from multiple categories.

For current rates, see [VM instance pricing](https://docs.cloud.google.com/compute/vm-instance-pricing#general-purpose_machine_type_family).

## Spend-based versus resource-based commitments

The following table demonstrates the differences between spend-based and resource-based CUDs, using Compute Engine as the example service.

Spend-based CUDs | Resource-based CUDs  
---|---  
**Spend-based** commitments for Compute Engine are purchased and measured in terms of the dollars per hour of equivalent discount spend. | **Resource-based** commitments for Compute Engine are purchased and measured in terms of the numbers of the underlying resource types.  
**Spend-based** commitments are purchased from your Cloud Billing account; they apply to eligible usage in any projects paid for by that Cloud Billing account.  |  **Resource-based** commitments are purchased in the context of an individual project, rather than that of a Cloud Billing account. The commitments are tied to the project where they were purchased. However, the CUDs can apply to the specific project or be shared across all projects linked to the Cloud Billing account, depending on your [CUD sharing configuration](https://docs.cloud.google.com/compute/docs/committed-use-discounts/share-resource-cuds-across-projects#cud-scope-configuration). You can enable or disable [ CUD sharing](https://docs.cloud.google.com/compute/docs/committed-use-discounts/share-resource-cuds-across-projects) for your Cloud Billing account at any time.  You can change the Cloud Billing account that pays for the project where you purchased the resource-based commitments. [ Learn about how moving a project affects CUD sharing and attribution settings](https://docs.cloud.google.com/compute/docs/committed-use-discounts/share-resource-cuds-across-projects#moving-project-billing-account).   
  
## CUDs summary

The following table summarizes the differences between resource-based CUDs and spend-based CUDs.

| Resource-based CUDs | Spend-based CUDs  
---|---|---  
**Products covered** | [Compute Engine](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview) | **Compute Flexible CUDs**  


  * [Cloud Run](https://docs.cloud.google.com/run/cud)
  * [Compute Engine](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview)
  * [Google Kubernetes Engine](https://docs.cloud.google.com/kubernetes-engine/cud)

**Flexible Savings Plans**  


  * [Gemini Enterprise](https://docs.cloud.google.com/docs/cuds-flexible-savings-plans)

**Service-specific spend-based commitments**

  * AlloyDB for PostgreSQL
  * Backup and DR Service
  * Bigtable
  * Cloud SQL
  * Dataflow
  * Firestore
  * Google Cloud NetApp Volumes
  * Google Cloud VMware Engine
  * Memorystore
  * Spanner
  * Backup for GKE _(no longer available for purchase)_
  * Cloud Run _(no longer available for purchase)_
  * Google Kubernetes Engine (Autopilot) _(no longer available for purchase)_

  
**Purchase unit** | 

  * Resource-based (available for vCPUs, memory, Local SSD disks, and Cloud GPUs).
  * You commit to purchasing a minimum amount of eligible resources.

| 

  * **Standard spend-based CUDs:** Measured in dollars per hour (for example, $100/hour) of equivalent discount spend. For Compute Engine, eligible spend covers vCPUs, memory, and Local SSD disks for applicable machine series. For G2 and G4 machine series only, Cloud GPUs are also supported.
  * **Flexible Savings Plans:** Measured in dollars per month (for example, $1,000/month) across a monthly entitlement window.

  
**Scope** | 

  * These CUDs can apply to a specific project or be shared across all projects linked to the Cloud Billing account, depending on your [ CUD sharing configuration](https://docs.cloud.google.com/compute/docs/committed-use-discounts/share-resource-cuds-across-projects#cud-scope-configuration).

| 

  * You can buy spend-based commitments measured in dollars per hour or dollars per month of equivalent discount spend. You buy these commitments at the billing account level and they apply to eligible usage in any project linked to that billing account, across all regions.

  
**Discount of on-demand rate** |  [Compute Engine](https://cloud.google.com/compute/all-pricing) |  Pricing for CUDs is unique for each Google Cloud product:  


  * AlloyDB for PostgreSQL
  * Backup and DR Service
  * Backup for GKE
  * Bigtable
  * Cloud Run
  * Cloud SQL
  * [Compute Engine](https://cloud.google.com/compute/all-pricing)
  * Dataflow
  * Firestore
  * [Gemini Enterprise (Flexible Savings Plans)](https://docs.cloud.google.com/docs/cuds-flexible-savings-plans)
  * Google Cloud NetApp Volumes
  * Google Cloud VMware Engine
  * Google Kubernetes Engine (Autopilot)
  * Memorystore
  * Spanner

  
**Regional eligibility** | Applies to a specific region. | Depending on the service, CUDs can apply to a specific region or all regions.  
**Attribution** | Supports proportional and prioritized attribution. | Supports proportional attribution only.  
  
## View your commitments and discounts

To view your spend-based and resource-based CUDs in the **Committed use discounts (CUDs)** page, complete the following steps:

  1. In the Google Cloud console, open the **Committed use discounts (CUDs)** page for **Billing**.

[Go to Committed use discounts (CUDs)](https://console.cloud.google.com/billing/reports/commitments)

  2. At the prompt, choose the Cloud Billing account for which you want to view commitments.




The **Committed use discounts (CUDs)** page displays a list of all the commitments, across services, that are associated with your Cloud Billing account.

The page provides two levels of detail (**Aggregated view** and **Instance view**) to help you manage your commitments. For more information about these views, see [View your commitments](https://docs.cloud.google.com/billing/docs/how-to/cuds-list-overview).

On this page, you can view which of your commitments are expiring in the next 30 days. You can also specify your _resource-based_ commitments to automatically renew at the end of their ongoing terms by changing the setting in the **Auto-renew** column in the Aggregated view, or in the details panel in the Instance view.

For information about viewing _spend-based_ CUDs, see [Viewing spend-based commitments](https://docs.cloud.google.com/billing/docs/how-to/cuds-list-overview).

For information about viewing _resource-based_ CUDs, see [Viewing resource-based commitments](https://docs.cloud.google.com/compute/docs/committed-use-discounts/view-resource-based-commitments).

## Pricing for commitments

You are billed a monthly fee for the commitments you purchase. This fee is calculated when you purchase the commitments, based on the list price on the date you made the purchase. This monthly fee applies to your purchased commitments for the entire duration of the commitment period. Future changes to the list prices don't affect your commitment fee during the commitment period.

To understand how your commitment fees and credits are applied to your Cloud Billing account and projects, see [Attribution of committed use discount fees and credits](https://docs.cloud.google.com/docs/cuds-attribution).

Pricing for CUDs is unique for each Google Cloud product:

  * [Backup and DR Service](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/cud#cud_pricing)
  * [Bigtable CUD pricing](https://docs.cloud.google.com/bigtable/docs/cuds#pricing)
  * [Cloud SQL pricing](https://cloud.google.com/sql/pricing/)
  * [Firestore CUD pricing](https://docs.cloud.google.com/firestore/docs/cuds#pricing)
  * [Spanner CUD pricing](https://docs.cloud.google.com/spanner/docs/cuds#pricing)
  * [Compute Engine pricing](https://docs.cloud.google.com/compute/vm-instance-pricing#committed_use)
  * [Google Cloud VMware Engine pricing](https://cloud.google.com/vmware-engine/pricing/)
  * [Memorystore for Memcached CUD pricing](https://docs.cloud.google.com/memorystore/docs/memcached/cuds#pricing)
  * [Memorystore for Redis CUD pricing](https://docs.cloud.google.com/memorystore/docs/redis/cuds#pricing)
  * [Backup for GKE (no longer available for purchase)](https://cloud.google.com/kubernetes-engine/pricing#backup-for-gke)
  * [Cloud Run (no longer available for purchase)](https://cloud.google.com/run/pricing#tables)
  * [Google Kubernetes Engine (Autopilot Mode) (no longer available for purchase)](https://cloud.google.com/kubernetes-engine/pricing#autopilot_mode)



## Purchase commitments

To purchase _spend-based_ commitments, see [Purchasing spend-based commitments](https://docs.cloud.google.com/docs/cuds-multiprice#steps_to_purchase).

To purchase _resource-based_ commitments for Compute Engine, see one of the following, depending on your use case:

  * [Purchase hardware commitments without attached reservations](https://docs.cloud.google.com/compute/docs/committed-use-discounts/purchase-commitments)
  * [Purchase hardware commitments with attached reservations](https://docs.cloud.google.com/compute/docs/committed-use-discounts/purchase-commitments-with-reservations)
  * [Purchase software commitments for OS licenses](https://docs.cloud.google.com/compute/docs/committed-use-discounts/purchase-license-commitments)
  * [Purchase block storage commitments for Exapools](https://docs.cloud.google.com/compute/docs/committed-use-discounts/purchase-block-storage-commitments)



## Related topics

  * Learn about [spend-based committed use discounts](https://docs.cloud.google.com/docs/cuds-multiprice).
  * Learn about [Flexible Savings Plans](https://docs.cloud.google.com/docs/cuds-flexible-savings-plans).
  * Learn more about [resource-based CUDs for Compute Engine](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts).
  * Learn how to [view your CUDs reports](https://docs.cloud.google.com/billing/docs/how-to/cud-analysis).
  * Learn how to [view your Cloud Billing reports and cost trends](https://docs.cloud.google.com/billing/docs/how-to/reports#credits).
  * [Understand your savings with cost breakdown reports](https://docs.cloud.google.com/billing/docs/how-to/cost-breakdown).
  * Learn how to [export Cloud Billing data to BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery).
  * Learn how to [view your cost and payment history](https://docs.cloud.google.com/billing/docs/how-to/view-history).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
