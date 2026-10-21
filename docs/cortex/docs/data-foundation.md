---
url: https://docs.cloud.google.com/cortex/docs/data-foundation/
title: Data foundation overview \u00a0|\u00a0 Google Cloud Cortex Framework \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:45:02.388344+00:00
---

# Data foundation overview  |  Google Cloud Cortex Framework  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cortex/docs/data-foundation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Google Cloud Cortex Framework ](https://docs.cloud.google.com/cortex/docs)
  * [ Version 7 Guides ](https://docs.cloud.google.com/cortex/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Data foundation overview

The Cortex Framework [data foundation layer](https://docs.cloud.google.com/cortex/docs/overview#data_foundation_layer) serves as a standardized, clean representation of the latest records from your source systems. It bridges the gap between raw replicated enterprise systems of record and high-value analytical consumption data by providing reusable, high-fidelity tables and views inside BigQuery.

While the data foundation layer feeds the [data product layer](https://docs.cloud.google.com/cortex/docs/overview#data_product_layer), it can be used entirely on its own and includes the following functionality:

  * **Independent deployment** : Organizations looking to establish a clean, conformed, and standardized operational datastore (ODS) inside BigQuery can deploy just the [data foundation module(s)](https://docs.cloud.google.com/cortex/docs/overview#data_modules). You don't need to deploy the data product layer to use the data foundation. 
  * **Direct consumption** : Standalone data foundation tables serve as a centralized, highly optimized source of truth that can directly power existing enterprise data mesh architectures, custom downstream ETL pipelines, third-party BI tools, custom ML models, and independent AI agents without dependencies on Cortex Framework delivered data products.
  * **High extensibility** : The framework recognizes and adds custom table columns (for example 'Z' or 'Y' prefixed columns) automatically during build and compilation of the foundation module. Extending with additional tables (custom tables, or standard tables not included in the foundation) is possible with minimal effort.



## Supported data sources

The data foundation layer supports raw replicated data from SAP ERP systems, including:

  * [SAP ECC](https://docs.cloud.google.com/cortex/docs/source-system-integration/sap-erp)
  * [SAP S/4HANA](https://docs.cloud.google.com/cortex/docs/source-system-integration/sap-erp)



For more information, see documentation for [Source system integration](https://docs.cloud.google.com/cortex/docs/source-system-integration/sap-erp).

## Core capabilities

The primary purpose of this layer is to standardize, cleanse, and conform raw source data into high-fidelity tables using the following methods: 

  * **Schema shielding** : Raw transactional schemas such as those from SAP frequently change and are difficult to navigate. The foundation layer shields downstream consumers from raw table complexities and underlying schema alterations by providing stable, standardized target structures.
  * **Business-ready metadata and annotations** : To help business users understand technical data models, the data foundation layer uses an extensive library of annotations (`src/data_modules/{namespace}/{system}/data_foundation/{foundation_name}/annotations/`). During the build process, the framework enriches technical source system columns with human-readable business descriptions in BigQuery table metadata (for example, translating an SAP columns like `bukrs` into `Company Code`). This rich metadata makes tables immediately usable for business analysts, BI dashboards, and enterprise AI agents.
  * **Dynamic schema adaptation** : Supports dynamic table schemas. It automatically ingests and propagates custom fields (such as `Z*` or `Y*` fields in SAP, or custom attributes in other sources) from the [raw layer](https://docs.cloud.google.com/cortex/docs/overview#raw_layer) without requiring manual code changes to the underlying SQL models.
  * **Automated data conforming and deduplication** : Whether raw data arrives as change logs or full snapshots, the foundation layer automatically handles deduplication, data type casting, and state reconstruction. This ensures you always query the accurate, current state of every record.



## CDC versus non-CDC sources

For pipelines managed natively by Cortex Framework, configuration is applied at the individual table level. You can configure how each table is processed based on whether the raw source data arrives as incremental change logs or full table snapshots. For example, individual tables in an otherwise CDC source can be declared as `isCdc: false` to treat them as snapshot tables:

  * **CDC-enabled sources** : For raw data replicated as change data capture logs (containing operation flags and timestamps, such as inserts, updates, and deletes from tools like [BigQuery Connector for SAP](https://docs.cloud.google.com/sap/docs/bq-connector/latest/all-guides) or [BigQuery Toolkit for SAP](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-toolkit-for-sap-overview)), Cortex Framework generates dedicated Dataform pipelines that incrementally process raw logs into a persisted, continuously updated "latest state" conformed table.
  * **Non-CDC (full snapshot/batch) sources** : For sources that do not provide CDC change logs, or where tables are periodically replicated as full extracts, Cortex Framework instructs the pipeline to process the data as complete table snapshots without CDC state reconstruction logic (see `isCdc` configuration attribute in data foundation, [table-settings configuration](https://docs.cloud.google.com/cortex/docs/deployment-configuration#source_settings)).



## External data foundations

In addition to managing CDC processing natively at the individual table level, Cortex Framework provides the architectural flexibility to integrate with existing external data foundations at the entire foundation level. The entire foundation can be declared as external, in which case Cortex Framework assumes the entire CDC processing has already been performed:

  * **Cortex-managed data foundation** : Cortex Framework builds and orchestrates the Dataform transformation pipelines, reading from your raw landing zone and materializing conformed tables in your target foundation dataset.
  * **External data foundation** : If your enterprise already uses an external replication tool, third-party pipeline, or pre-established semantic layer that performs CDC reconstruction and data cleaning outside of Cortex Framework, you can register it as an external data foundation (see `external` flag in [data module foundation setting](https://docs.cloud.google.com/cortex/docs/deployment-configuration#data_modules_foundations). When configured as external, Cortex Framework bypasses generating built-in foundation transformation pipelines and instead points downstream data products directly to your existing target dataset. 



## Data foundation configurability options

While global and module-level configurations are managed in the `config.yaml` file, granular **table-level** options are configured through a source-specific `table_settings.yaml` file (for SAP systems it build of `common`, `ecc`, and `s4` sections, for detailed information see: [Deployment, Table-settings configuration style for SAP ERP](https://docs.cloud.google.com/cortex/docs/deployment-configuration#data-foundation-style-sap-erp)). This file gives you control over materialization options, deployment optimization, and BigQuery performance features for individual tables, all without writing or modifying SQL code.

  * **[Dynamic dependency resolution](https://docs.cloud.google.com/cortex/docs/deployment-configuration#dynamic-dependency-resolution)** : By default (`deployAlways: false`), Cortex Framework optimizes the deployment footprint and execution cost by only deploying and compiling data foundation layer tables that are actively required as dependencies by enabled downstream data products. To override this optimization and force a foundation table to always be deployed (which is particularly useful when running the data foundation standalone or for custom downstream workloads), set `deployAlways: true`.
  * **Ingestion mode** : Controls whether the table is processed using incremental CDC state reconstruction or full snapshot processing.
  * **Target naming and tags** : Customize the target conformed table name and attach arbitrary metadata tags (e.g., `[sap, finance, hourly]`) directly to Dataform actions to enable selective pipeline runs (`dataform run --tags ...`).
  * **Clustering details** : Colocate related data by sorting storage blocks across up to four alphanumeric columns (e.g., `bukrs`, `gjahr`). Clustering significantly improves query performance and reduces data scan costs for queries filtering or joining on these columns.
  * **Partitioning details** : Segment large historical tables by time (`time` or `DATE` with `timeGrain: day | month | year`) or integer ranges (`integer`). Partitioning prevents full table scans when queries request specific date ranges or ID intervals.



## Extending the data foundation

To extend the data foundation layer with additional tables, you have multiple options: 

  * [Use the agentic data product builder](https://docs.cloud.google.com/cortex/docs/agentic-skills-for-data-product-building)
  * [Add a table manually](https://docs.cloud.google.com/cortex/docs/deployment-configuration#add-table-to-data-foundation)
  * For higher-complexity extensions: Create an additional instance of the data foundation module or build a customized module using the extensibility framework. For more information, see [Creating a new data foundation module](https://docs.cloud.google.com/cortex/docs/extensibility-guide-data-foundation).



## Available data foundation tables

The following table lists the tables included in the Cortex Framework data foundation layer and related details.

Line of business | SAP module | Table name | Description | Supported sources | Dataform tags | Partition details | Cluster details  
---|---|---|---|---|---|---|---  
SAP ECC | SAP S/4HANA  
Finance | CO | bpge | Budget Values (Overall) | ✅ | ✅ | finance, sap_co, daily |  |   
bpja | Budget Values (Annual) | ✅ | ✅ | finance, sap_co, daily |  |   
bpvg | Document Line Items | ✅ | ✅ | finance, sap_co, daily |  |   
cepc | Profit Center Master Data Table | ✅ | ✅ | finance, sap_co, daily |  |   
cepct | Texts for Profit Center Master Data | ✅ | ✅ | finance, sap_co, daily |  |   
ckmlcr | Material Ledger: Period Totals Records Values | ✅ | ✅ | finance, sap_co, daily |  |   
ckmlhd | Material Ledger: Header Record | ✅ | ✅ | finance, sap_co, daily |  |   
cobk | Controlling Object: Document Header | ✅ | ✅ | finance, controlling, daily |  |   
coep | Controlling Object: Line Items (By Period) | ✅ | ✅ | finance, controlling, daily |  |   
cooi | Commitments Management: Line Items | ✅ | ✅ | finance, controlling, daily |  |   
cosp | Controlling Object: Cost Totals for External Postings | ✅ | ✅ | finance, controlling, daily |  |   
coss | Controlling Object: Cost Totals for Internal Postings | ✅ | ✅ | finance, controlling, daily |  |   
cskb | Cost Elements (Controlling Area-Dependent Data) | ✅ | ✅ | finance, sap_co, daily |  |   
csks | Cost Center Master Record | ✅ | ✅ | finance, sap_co, daily |  |   
cskt | Cost Center Texts | ✅ | ✅ | finance, sap_co, daily |  |   
csku | Cost Element Texts | ✅ | ✅ | finance, sap_co, daily |  |   
jest | Individual Object Status | ✅ | ✅ | finance, sap_co, daily |  |   
sethanahier0101 | Hierarchy table for Cost Center Groups |  | ✅ | finance, sap_co, monthly |  |   
sethanahier0106 | Hierarchy table for Profit Center Groups |  | ✅ | finance, sap_co, monthly |  |   
setheader | Set Header and Directory | ✅ | ✅ | finance, sap_co, monthly |  |   
setheadert | Short Description of Sets | ✅ | ✅ | finance, sap_co, monthly |  |   
setleaf | Values in Sets | ✅ | ✅ | finance, sap_co, monthly |  |   
setnode | Lower-Level Sets in Sets | ✅ | ✅ | finance, sap_co, monthly |  |   
tj02t | System Status Texts | ✅ | ✅ | finance, sap_co, yearly |  |   
tka01 | Controlling Areas | ✅ | ✅ | finance, sap_co, yearly |  |   
tka02 | Controlling Area Assignment | ✅ | ✅ | finance, sap_co, yearly |  |   
FI | acdoca | Universal Journal Entry Line Items |  | ✅ | finance, sap_fi, hourly |  | rclnt, rbukrs  
acdocu | Group Journal Entries |  | ✅ | finance, sap_fi, hourly |  |   
adr6 | Email Addresses (Business Address Services) | ✅ | ✅ | finance, sap_fi, daily |  |   
adrc | Addresses (Business Address Services) | ✅ | ✅ | finance, sap_fi, daily |  |   
adrct | Address Texts (Business Address Services) | ✅ | ✅ | finance, sap_fi, daily |  |   
anek | Asset Posting Document Header | ✅ |  | finance, sap_fi, daily |  |   
anep | Asset Line Items | ✅ |  | finance, sap_fi, daily |  |   
ankt | Asset Classes: Description | ✅ | ✅ | finance, sap_fi, hourly |  |   
anla | Asset Master Record Segment | ✅ | ✅ | finance, sap_fi, hourly |  |   
anlb | Depreciation Terms | ✅ | ✅ | finance, sap_fi, hourly |  |   
anlc | Asset Value Record: Year | ✅ |  | finance, sap_fi, yearly |  |   
anlh | Main Asset Number | ✅ | ✅ | finance, sap_fi, hourly |  |   
anlz | Time-Dependent Asset Allocations | ✅ | ✅ | finance, sap_fi, hourly |  |   
atras | Treasury Rates Table | ✅ | ✅ | finance, sap_fi, daily |  |   
bkpf | Accounting Document Header | ✅ | ✅ | finance, sap_fi, hourly | budat (time/day) | bukrs, gjahr  
bsad | Generated Table for View | ✅ |  | finance, sap_fi, hourly |  |   
bsak | Generated Table for View | ✅ |  | finance, sap_fi, hourly |  |   
bseg | Accounting Document Segment | ✅ | ✅ | finance, sap_fi, hourly |  | mandt, bukrs, gjahr  
bsid | Generated Table for View | ✅ |  | finance, sap_fi, hourly |  |   
bsik | Generated Table for View | ✅ |  | finance, sap_fi, hourly |  |   
but000 | Bp: General Data I | ✅ | ✅ | finance, sap_fi, daily |  |   
but020 | Bp: Addresses | ✅ | ✅ | finance, sap_fi, daily |  |   
but0bk | Bp: Bank Details | ✅ | ✅ | finance, sap_fi, daily |  |   
faat_doc_it | Asset Accounting: Statistical Line Items |  | ✅ | finance, sap_fi, daily |  |   
faat_plan_values | Asset Values: Planned Values and Revaluations |  | ✅ | finance, sap_fi, daily |  |   
faat_ydda | Asset Values: Year-Dependent Data |  | ✅ | finance, sap_fi, yearly |  |   
fagl_011pc | Fin Statement Version: Items in Financial Statement Version | ✅ | ✅ | finance, sap_fi, monthly |  |   
fagl_011qt | Fin Statement Structure: Text for Fin Statement Items | ✅ | ✅ | finance, sap_fi, monthly |  |   
fagl_011zc | Fin Statement Version: Assignment of Fs Items to G/L Accts | ✅ | ✅ | finance, sap_fi, monthly |  |   
faglflexa | General Ledger: Actual Line Items | ✅ |  | finance, sap_fi, hourly |  |   
fincs_ref_vers_r | Reference Version Relation |  | ✅ | finance, sap_fi, yearly |  |   
finsc_ld_cmp | CompCode-Dependent Settings for Univ. Journal Entry Ledger |  | ✅ | finance, sap_fi, daily |  |   
finsc_ledger | Universal Journal Entry Ledger |  | ✅ | finance, sap_fi, yearly |  |   
finsc_ledger_rep | Unified Journal Entry Ledger (Auxiliary table for Reporting) |  | ✅ | finance, sap_fi, daily |  |   
finsc_ledger_t | Universal Journal Entry Ledger Text |  | ✅ | finance, sap_fi, yearly |  |   
ska1 | G/L Account Master (Chart of Accounts) | ✅ | ✅ | finance, sap_fi, daily |  |   
skat | G/L Account Master Record (Chart of Accounts: Description) | ✅ | ✅ | finance, sap_fi, daily |  |   
t001 | Company Codes | ✅ | ✅ | finance, sap_fi, once |  |   
t002 | Language Keys (Component Bc-I18) | ✅ | ✅ | finance, sap_fi, once |  |   
t002t | Language Key Texts | ✅ | ✅ | finance, sap_fi, once |  |   
t005 | Countries | ✅ | ✅ | finance, sap_fi, yearly |  |   
t005k | Communication: Country Dialling Code | ✅ | ✅ | configuration, yearly |  |   
t005s | Taxes: Region (Province) Key | ✅ | ✅ | configuration, yearly |  |   
t005t | Country Names | ✅ | ✅ | configuration, yearly |  |   
t005u | Taxes: Region Key: Texts | ✅ | ✅ | configuration, yearly |  |   
t009 | Fiscal Year Variants | ✅ | ✅ | configuration, once |  |   
t009b | Fiscal Year Variant Periods | ✅ | ✅ | configuration, once |  |   
t090nat | Depreciation Key Texts | ✅ | ✅ | finance, sap_fi, hourly |  |   
t093b | Company Code Settings for Depreciation Area | ✅ | ✅ | finance, sap_fi, hourly |  |   
t093c | Company Code Settings for Asset Accounting | ✅ | ✅ | finance, sap_fi, hourly |  |   
t093t | Depreciation Area Texts | ✅ | ✅ | finance, sap_fi, hourly |  |   
t095t | Name of Account Determination | ✅ | ✅ | finance, sap_fi, hourly |  |   
t098t | Reason for Manual Valuation Description | ✅ | ✅ | finance, sap_fi, hourly |  |   
t881 | Ledger Master | ✅ | ✅ | finance, sap_fi, once |  |   
t881t | Fi-Sl Ledger Text | ✅ | ✅ | finance, sap_fi, once |  |   
tabw | Asset Transaction Types | ✅ | ✅ | finance, sap_fi, daily |  |   
tabwh | Asset Transaction Type Group Texts | ✅ | ✅ | finance, sap_fi, daily |  |   
tabwt | Asset Transaction Type Texts | ✅ | ✅ | finance, sap_fi, daily |  |   
tcurc | Currency Codes | ✅ | ✅ | finance, sap_fi, once |  |   
tcurf | Conversion Factors | ✅ | ✅ | finance, sap_fi, once |  |   
tcurr | Exchange Rates | ✅ | ✅ | finance, sap_fi, daily |  |   
tcurt | Currency Code Names | ✅ | ✅ | finance, sap_fi, daily |  |   
tcurx | Decimal Places in Currencies | ✅ | ✅ | finance, sap_fi, daily |  |   
tf200 | Consolidation Versions |  | ✅ | finance, sap_fi, yearly |  |   
tf201 | Versions: Name |  | ✅ | finance, sap_fi, yearly |  |   
tvarvc | Table of Variant Variables (Client-Specific) | ✅ | ✅ | finance, sap_fi, daily |  |   
vwpanla | Asset Master for Securities | ✅ | ✅ | finance, sap_fi, daily |  |   
FSCM | fdsb | Cash Management and Forecast Summary Records | ✅ |  | finance, sap_fscm, hourly |  |   
fqm_flow | One Exposure From Operations |  | ✅ | finance, sap_fscm, hourly |  |   
PS | prhi | Work Breakdown Structure, Edges (Hierarchy Pointer) | ✅ | ✅ | finance, sap_ps, hourly |  |   
proj | Project Definition | ✅ | ✅ | finance, sap_ps, hourly |  |   
prps | WBS Element Master Data | ✅ | ✅ | finance, sap_ps, hourly |  |   
prte | Scheduling Data for Project Item | ✅ | ✅ | finance, sap_ps, hourly |  |   
rpsco | Project info database: Costs, revenues, finances | ✅ | ✅ | finance, sap_ps, daily |  |   
TRM | vtbfha | Financial Transaction (Vtbfha) | ✅ | ✅ | finance, sap_trm, hourly |  |   
vtbfhapo | Transaction Flow (Vtbfhapo) | ✅ | ✅ | finance, sap_trm, hourly |  |   
vtbfhazu | Transaction Activity (Vtbfhazu) | ✅ | ✅ | finance, sap_trm, hourly |  |   
vtvbar | Npvs of Otc Transactions (Vtvbar) | ✅ | ✅ | finance, sap_trm, hourly |  |   
HR | HCM | hrrp_directory | Hierarchy directory |  | ✅ | hr, sap_hcm, monthly |  |   
hrrp_node | Hierarchy node |  | ✅ | hr, sap_hcm, monthly |  |   
hrrp_nodet | Hierarchy node texts |  | ✅ | hr, sap_hcm, monthly |  |   
IT | BASIS | dd01l | Domains | ✅ | ✅ | it, sap_basis, once |  |   
dd03l | Table Fields | ✅ | ✅ | it, sap_basis, once |  |   
dd04t | R/3 Dd: Data Element Texts | ✅ | ✅ | it, sap_basis, once |  |   
dd07l | Domain Values | ✅ | ✅ | it, sap_basis, once |  |   
dd07t | Dd: Texts for Domain Fixed Values (Language-Dependent) | ✅ | ✅ | it, sap_basis, once |  |   
dd08l | Relationship Definitions | ✅ | ✅ | it, sap_basis, once |  |   
Manufacturing | PP | afko | Order Header Data PP Orders | ✅ | ✅ | manufacturing, sap_pp, hourly |  |   
afpo | Order Item | ✅ | ✅ | manufacturing, sap_pp, hourly |  |   
aufk | Order Master Data | ✅ | ✅ | manufacturing, sap_pp, hourly |  |   
mast | Material to Bom Link | ✅ | ✅ | manufacturing, sap_pp, monthly |  |   
stas | Boms - Item Selection | ✅ | ✅ | manufacturing, sap_pp, monthly |  |   
stko | Bom Header | ✅ | ✅ | manufacturing, sap_pp, monthly |  |   
stpo | Bom Item | ✅ | ✅ | manufacturing, sap_pp, monthly |  |   
Sales | SD | kna1 | General Data in Customer Master | ✅ | ✅ | sales, sap_sd, daily |  |   
konv | Conditions (Transaction Data) | ✅ |  | sales, sap_sd, daily | kdatu (time/day) | stunr  
prcd_elements | Pricing Elements |  | ✅ | sales, sap_sd, hourly |  |   
t179 | Materials: Product Hierarchies | ✅ | ✅ | sales, sap_sd, once |  |   
t179t | Materials: Product Hierarchies: Texts | ✅ | ✅ | sales, sap_sd, once |  |   
tspa | Organizational Unit: Sales Divisions | ✅ | ✅ | sales, sap_sd, yearly |  |   
tspat | Organizational Unit: Sales Divisions: Texts | ✅ | ✅ | sales, sap_sd, yearly |  |   
tvfst | Billing : Blocking Reason Texts | ✅ | ✅ | sales, sap_sd, yearly |  |   
tvko | Organizational Unit: Sales Organizations | ✅ | ✅ | sales, sap_sd, yearly |  |   
tvkot | Organizational Unit: Sales Organizations: Texts | ✅ | ✅ | sales, sap_sd, yearly |  |   
tvlst | Deliveries: Blocking Reasons/Scope: Texts | ✅ | ✅ | sales, sap_sd, yearly |  |   
tvtw | Organizational Unit: Distribution Channels | ✅ | ✅ | sales, sap_sd, yearly |  |   
tvtwt | Organizational Unit: Distribution Channels: Texts | ✅ | ✅ | sales, sap_sd, yearly |  |   
vbak | Sales Document: Header Data | ✅ | ✅ | sales, sap_sd, hourly | audat (time/day) | vkorg  
vbap | Sales Document: Item Data | ✅ | ✅ | sales, sap_sd, hourly |  | werks, lgort  
vbep | Sales Document: Schedule Line Data | ✅ | ✅ | sales, sap_sd, hourly |  |   
vbfa | Sales Document Flow | ✅ | ✅ | sales, sap_sd, hourly |  |   
vbpa | Sales Document: Partner | ✅ | ✅ | sales, sap_sd, hourly |  |   
vbrk | Billing Document: Header Data | ✅ | ✅ | sales, sap_sd, hourly |  |   
vbrp | Billing Document: Item Data | ✅ | ✅ | sales, sap_sd, hourly |  |   
vbuk | Sales Document: Header Status and Administrative Data | ✅ |  | sales, sap_sd, hourly |  |   
vbup | Sales Document: Item Status | ✅ |  | sales, sap_sd, hourly |  |   
wb2_d_bvdetail | Ccs: Detailed Statement for Settlement | ✅ | ✅ | sales, sap_sd, daily |  |   
wb2_d_settl_cal | Rebates: Settlement Calendar | ✅ | ✅ | sales, sap_sd, daily |  |   
wbrk | Agency Settlement Document: Header | ✅ | ✅ | sales, sap_sd, hourly |  |   
wbrp | Agency Settlement Document: Item | ✅ | ✅ | sales, sap_sd, hourly |  |   
wcocoh | Condition Contract: Header | ✅ | ✅ | sales, sap_sd, daily |  |   
wcocoi | Condition Contract: Item | ✅ | ✅ | sales, sap_sd, daily |  |   
Supply Chain | LE | likp | SD Document: Delivery Header Data | ✅ | ✅ | supply_chain, sap_le, hourly | erdat (time/month) | vkorg  
lips | SD Document: Delivery: Item Data | ✅ | ✅ | supply_chain, sap_le, hourly | erdat (time/month) |   
MM | ekbe | Purchasing Document History (Ekbe) | ✅ | ✅ | supply_chain, sap_mm, hourly | budat (time/day) | mandt, vgabe, ebeln, bwart  
ekes | Vendor Confirmations (Ekes) | ✅ | ✅ | supply_chain, sap_mm, hourly |  |   
eket | Scheduling Agreement Schedule Lines | ✅ | ✅ | supply_chain, sap_mm, hourly | eindt (time/day) | mandt, ebeln  
ekkn | Account Assignment in Purchasing Document (Ekkn) | ✅ | ✅ | supply_chain, sap_mm, hourly |  |   
ekko | Purchasing Document Header | ✅ | ✅ | supply_chain, sap_mm, hourly | bedat (time/day) | mandt, ebeln  
ekpo | Purchasing Document Item | ✅ | ✅ | supply_chain, sap_mm, hourly | aedat (time/day) | mandt, ebeln  
lfa1 | Vendor Master (General Section) | ✅ | ✅ | supply_chain, sap_mm, daily |  |   
makt | Material Descriptions | ✅ | ✅ | supply_chain, sap_mm, daily |  | spras  
mara | General Material Data | ✅ | ✅ | supply_chain, sap_mm, daily |  |   
marc | Plant Data for Material | ✅ | ✅ | supply_chain, sap_mm, hourly |  |   
mard | Storage Location Data for Material | ✅ | ✅ | supply_chain, sap_mm, hourly |  |   
matdoc | Material Documents |  | ✅ | supply_chain, sap_mm, hourly |  |   
mbew | Material Valuation | ✅ | ✅ | supply_chain, sap_mm, daily |  |   
mbewh | Material Valuation: History | ✅ | ✅ | supply_chain, sap_mm, daily |  |   
mch1 | Batches (If Batch Management Cross-Plant) | ✅ | ✅ | supply_chain, sap_mm, daily |  |   
mcha | Batches | ✅ | ✅ | supply_chain, sap_mm, daily |  |   
mchb | Batch Stocks | ✅ | ✅ | supply_chain, sap_mm, daily |  |   
mkol | Special Stocks From Vendor | ✅ | ✅ | supply_chain, sap_mm, weekly |  |   
mseg | Document Segment: Material | ✅ |  | supply_chain, sap_mm, hourly |  |   
msfd | Sales Order Stock with Vendor | ✅ |  | supply_chain, sap_mm, weekly |  |   
mska | Sales Order Stock | ✅ | ✅ | supply_chain, sap_mm, weekly |  |   
msku | Special Stocks with Customer | ✅ | ✅ | supply_chain, sap_mm, weekly |  |   
mslb | Special Stocks with Vendor | ✅ | ✅ | supply_chain, sap_mm, weekly |  |   
rbco | Document Item, Incoming Invoice, Account Assignment | ✅ | ✅ | supply_chain, sap_mm, hourly |  |   
rbkp | Document Header: Invoice Receipt | ✅ | ✅ | supply_chain, sap_mm, hourly |  |   
rseg | Document Item: Incoming Invoice | ✅ | ✅ | supply_chain, sap_mm, hourly |  |   
t001k | Valuation Area | ✅ | ✅ | supply_chain, sap_mm, once |  |   
t001l | Storage Locations | ✅ | ✅ | supply_chain, sap_mm, once |  |   
t001w | Plants/Branches | ✅ | ✅ | supply_chain, sap_mm, once |  |   
t006 | Units of Measurement | ✅ | ✅ | supply_chain, sap_mm, yearly |  |   
t006a | Assign Internal to Language-Dependent Unit | ✅ | ✅ | configuration, once |  |   
t006t | Dimension Texts | ✅ | ✅ | configuration, once |  |   
t023 | Material Groups | ✅ | ✅ | supply_chain, sap_mm, once |  |   
t023t | Material Group Descriptions | ✅ | ✅ | supply_chain, sap_mm, once |  |   
t024 | Purchasing Groups | ✅ | ✅ | supply_chain, sap_mm, once |  |   
t024e | Purchasing Organizations | ✅ | ✅ | supply_chain, sap_mm, once |  |   
t134 | Material Types | ✅ | ✅ | supply_chain, sap_mm, once |  |   
t134t | Material Type Descriptions | ✅ | ✅ | supply_chain, sap_mm, once |  |   
t148t | Special Stock Descriptions | ✅ | ✅ | supply_chain, sap_mm, once |  |   
t156 | Movement Type | ✅ | ✅ | supply_chain, sap_mm, once |  |   
t156t | Movement Type Text | ✅ | ✅ | configuration, once |  |   
t157e | Text Table: Reason for Movement | ✅ | ✅ | configuration, once |  |   
t161 | Purchasing Document Types (T161) | ✅ | ✅ | supply_chain, sap_mm, once |  |   
t161t | Texts for Purchasing Document Types | ✅ | ✅ | supply_chain, sap_mm, once |  |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
