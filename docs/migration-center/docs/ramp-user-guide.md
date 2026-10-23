---
url: https://docs.cloud.google.com/migration-center/docs/ramp-user-guide/
title: RaMP user guide \u00a0|\u00a0 Migration Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:54:22.337933+00:00
---

# RaMP user guide  |  Migration Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migration-center/docs/ramp-user-guide/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migration Center ](https://docs.cloud.google.com/migration-center/docs)
  * [ Resources ](https://docs.cloud.google.com/migration-center/docs/release-notes)



Send feedback 

#  RaMP user guide Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the steps required to qualify for RaMP incentives, how rewards are calculated, and the rules for managing the migration journey and the limitations that apply to RaMP incentives.

**Note:** Terms used but not defined on this page have the meaning given to them in the [RaMP Terms](https://cloud.google.com/terms/ramp) or RaMP Agreement, as applicable.

## Qualify for RaMP incentives

To qualify for RaMP incentives, prepare the environment and tag the workloads. The following sections describe the necessary steps.

### Complete a RaMP assessment

To begin the RaMP incentives journey, a customer must undergo a data-driven RaMP assessment to formally qualify for a RaMP Agreement. This assessment identifies eligible RaMP workloads and validates the Projected Annual Run Rate as defined in the [RaMP terms](https://cloud.google.com/terms/ramp). The estimated _Projected Annual Run Rate_ must be at least $60,000 USD per workload to qualify for RaMP.

To start your RaMP assessment, [try our free migration assessment](https://cloud.google.com/resources/migration-assessment-offer) or contact your [Google Cloud account team](https://cloud.google.com/contact).

### Sign a RaMP Agreement

After a RaMP assessment is complete, a RaMP Agreement must be signed and the identified RaMP workloads (which can be one or more workloads) must be tagged to qualify for any RaMP incentives.

### RaMP Workload

A RaMP workload is a collection of resources within a Google Cloud project that function together to achieve a business outcome and drive spend on Google Cloud. The following are Workload Types that can earn incentives:

Workload type | Workload type details  
---|---  
**Analytics** | An Analytics Workload refers to the migration of new Data Lake and Data Warehouse environments from on-premises (e.g., Teradata, Cloudera) and cloud platforms (e.g., Snowflake, Redshift, Databricks) to BigQuery or Managed Service for Apache Spark on Google Cloud.  
**Database** | A Database Workload refers to the migration of any database from any source environment (on-premise or another cloud) to any managed first-party Google Cloud database products on Google Cloud—including: 

  * [Cloud SQL](https://cloud.google.com/sql) (Postgres, MySQL, SQL Server)
  * [AlloyDB for PostgreSQL](https://cloud.google.com/products/alloydb)
  * [AlloyDB Omni](https://cloud.google.com/alloydb/omni)
  * [Spanner](https://cloud.google.com/spanner)
  * Spanner Omni
  * [Bigtable](https://cloud.google.com/bigtable)
  * [Memorystore](https://cloud.google.com/memorystore)
  * [Firestore](https://cloud.google.com/products/firestore)

  
**Modern infrastructure**  
(Google Kubernetes Engine (GKE), Cloud Run, Arm or Axion) | A Modern Infrastructure Workload refers to the deployment of workloads on Google Cloud utilizing GKE, Cloud Run, or Arm or Axion.  
**Oracle** | An Oracle Workload refers to the deployment of Oracle Databases alongside custom or first-party Oracle applications (E-Business Suite, PeopleSoft, JD Edwards, Siebel, Hyperion, ATG Web Commerce, or Fusion Middleware) on Compute Engine within Google Cloud.  
**SAP** | An SAP Workload refers to the migration of SAP HANA, S/4HANA, BW/4HANA, Business One, or other qualified SAP apps and databases to Google Cloud.  
**VMware** | A VMware workload refers to the deployment of VMware VMs on Google Cloud sourced from on-premises, colocation, or other VMware clouds. These VMs must reside on Google Cloud VMware Engine or, if replatformed, Compute Engine or GKE, provided at least 75% of the source scope are VMware VMs.  
**Windows** | A Windows Workload refers to any application or server environment running on a Windows Server OS that is deployed and hosted on Google Cloud (on Compute Engine or VMware Engine).  
**General** | A General Workload refers to any other RaMP-eligible application, dataset, service, or IT process that can be effectively migrated or refactored to run on Google Cloud (some service exclusions may apply).  
  
These Workload Types are identified as part of the RaMP assessment and receive a unique Workload ID number in the RaMP Agreement.

### Tag RaMP Workloads

Tagging is the primary mechanism for identifying and tracking workloads by applying the provided **RaMP Agreement ID** number and **Workload ID** number that is bound to the customer's Google Cloud resources.

Workload tagging is required for Google to calculate and disburse RaMP incentives. The customer is responsible for ensuring tags are applied accurately and timely. Google cannot perform retroactive adjustments. Failure to appropriately tag workloads will result in the forfeiture of RaMP incentives for that period.

For more information about tagging RaMP workloads, see [RaMP workload tagging guide](https://docs.cloud.google.com/migration-center/docs/ramp-workload-tagging).

### Workload exclusivity

To prevent incentive duplication, RaMP enforces the following strict exclusivity rules across workloads:

  * A single, defined workload can reside in exactly one RaMP Agreement.
  * A workload cannot be split or shared across multiple RaMP Agreements.
  * If a workload is inadvertently included in a second RaMP Agreement, the original RaMP Agreement takes precedence.



### Additional RaMP Agreements and billing account best practices

RaMP enables the customer to have more than one active RaMP Agreement at the same time under the same primary billing account (as the customer plans different workloads and completes different RaMP assessments over time, including entering into a new RaMP Agreement for a different Workload Type).

The primary billing account is the main account where consumption is tracked for RaMP incentive eligibility. Only the eligible consumption occurring under this billing account earns RaMP-related Google Cloud credits.

## Calculate RaMP incentives

RaMP incentives are calculated based on factors including eligible spending and workload type. The following sections explain how incentives are calculated.

### Incremental eligible spend for incentives

Google Cloud Services Credits and Partner Services Funds are earned from spend on the [RaMP 2026 SKU Group](https://cloud.google.com/skus/sku-groups/ramp-2026). Offerings that are not eligible for RaMP incentives from incremental spend include Google Cloud Marketplace offerings, Google Cloud Support (including Technical Support Services or TSS), subscriptions, GPUs, Archival Storage, and Google Distributed Cloud.

### Funds to support migrate and modernize

The following incentive types are available to help support migration and modernization needs: Google Cloud Consulting Services Funds and Training and Implementation Services Funds as well as Partner Services Funds.

For General Workload Types, each workload is eligible for the lesser of 20% of the Projected Annual Run Rate and $2M USD. For specialized Workload Types (for example, VMware) a higher Projected Annual Run Rate percentage is available. Projected Annual Run Rate only includes eligible incremental spend.

For more information, see [RaMP Terms](https://cloud.google.com/terms/ramp).

### Funds to support deployment

Google Cloud Service Credits are available to support Deployments.

For General Workload Types, each workload is eligible for 25% of the incremental eligible spend, capped at the lesser of 30% of Projected Annual Run Rate and $3M USD. For specialized Workload Types (for example, Oracle) a higher Projected Annual Run Rate percentage is available.

For more information, see [RaMP Terms](https://cloud.google.com/terms/ramp).

While the preceding information determines the maximum amount of Google Cloud Service Credits available for each unique Workload ID, additional requirements to earn quarterly Google Cloud Services Credits include:

  * **Total account growth:** To qualify for incentives during the RaMP contract period, you must meet the following requirements: 
    * Tag workloads: Tag projects with the applicable Workload ID. Google might withhold incentives for improper tagging.
    * Demonstrate account growth: Establish overall account growth. Google reserves the right to review your spend to verify this growth.
    * Generate incremental spend: Pre-existing spend is ineligible for incentives. You cannot transfer pre-existing spend to a new workload to earn incentives. Google might withhold incentives if it reasonably suspects ineligible spend.
  * **High watermark:** Defined as the highest total TTM spend recorded over any four consecutive quarters during the agreement. You must surpass this watermark to qualify for new incentives after a dip. Google only pays credits if your workloads show continuous, uninterrupted growth throughout the agreement.



For example:

  * **Year 1:** Your spend grows → You receive incentives.
  * **Year 2:** Your spend dips significantly → No incentives are paid.
  * **Year 3:** Your spend grows compared to Year 2, but remains lower than your Year 1 peak → No incentives are paid.



#### Full case scenario: Calculating Google Cloud Service Credits

A customer signs a RaMP Agreement for $1,000,000 USD General Workload Type Projected Annual Run Rate on Jan 1, 2026.

They begin the migration right away, and spend $100,000 USD in Q2 2026, $150,000 USD in Q3 2026, $200,000 USD in Q4 2026, and $250,000 USD in Q1 2027, reaching the steady state. They continue spending $250,000 USD per each quarter of 2027.

#### Incentives

The customer receives **Partner Services Funds (PSF)** equaling 20% of the workload Annual Run Rate, so $200,000 USD, paid upon meeting the PSF payout requirements.

The customer also receives Google Cloud Service Credits, equal to 25% of the incremental eligible spend each quarter, so the total Google Cloud Service Credit amount is $250,000 USD (see table below).

Total incentives that the customer received from PSF and Google Cloud Service Credit is $450,000 USD.

The following table shows the quarterly eligible spend, incremental eligible spend, and resulting Google Cloud Service Credits from 2026 to 2028:

Year | Metric | Q1 | Q2 | Q3 | Q4 | Total per year  
---|---|---|---|---|---|---  
**2026** | Google Cloud Eligible spend | $0 | $100,000 | $150,000 | $200,000 | $450,000  
Incremental Eligible spend | $0 | $100,000 | $150,000 | $200,000 | $450,000  
**Google Cloud Service Credits** | $0 | $25,000 | $37,500 | $50,000 | $112,500  
**2027** | Google Cloud Eligible spend | $250,000 | $250,000 | $250,000 | $250,000 | $1,000,000  
Incremental Eligible spend | $250,000 | $150,000 | $100,000 | $50,000 | $550,000  
**Google Cloud Service Credits** | **$62,500** | **$37,500** | **$25,000** | **$12,500** | **$137,500**  
**2028** | Google Cloud Eligible spend | $250,000 | $250,000 | $250,000 | $250,000 | $1,000,000  
Incremental Eligible spend | $0 | $0 | $0 | $0 | $0  
**Google Cloud Service Credits** | $0 | $0 | $0 | $0 | $0  
  
## Incentive disbursement and restrictions

After incentives are calculated, they are applied according to a specific schedule and are subject to certain restrictions. The following sections provide details on the disbursement process and applicable limitations.

### Disbursement to Designated Accounts

For each RaMP Agreement, RaMP incentives will be applied towards fees from tagged workloads on the customer's primary billing account. To monitor your progress toward credit milestones and view accumulated spend, see [Track the status of your conditional incentives](https://docs.cloud.google.com/billing/docs/how-to/incentives-program-tracker).

### Payout Schedule: Google Cloud Services Credits

Disbursement will be within 45 days of each calendar quarter-end beginning with the quarter-end falling on June 30, 2026. For clarity, this means the first set of earned Google Cloud Service Credits for RaMP Agreements executed through June 30, 2026 would be deposited into the primary invoiced billing account (or, as applicable, the primary sub-account associated with the Relevant Customer) by August 15, 2026.

### Payout Schedule: Partner Services Funds

Disbursement is tied to both statements of work completion and consumption milestones from incremental eligible spend on the RaMP 2026 SKU group.

## Training and Implementation Services Funds; Google Cloud Consulting Services Funds

For Google Cloud Consulting services, RaMP incentives are issued using an Order Form for eligible, registered workloads. These incentives can be applied to partially or fully fund the project, as defined in the Statement of Work (SOW).

## Additional RaMP Incentive Information

**Expiration:** If a workload is not fully migrated before the RaMP Agreement expiration, all future incentives for that workload growth are void.

**Rollover** : Workloads where migration work has started cannot be rolled over into a new RaMP Agreement

## What's next

  * [RaMP workload tagging guide](https://docs.cloud.google.com/migration-center/docs/ramp-workload-tagging)
  * [Track the status of your conditional incentives](https://docs.cloud.google.com/billing/docs/how-to/incentives-program-tracker)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
