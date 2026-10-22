---
url: https://docs.cloud.google.com/cortex/docs/release-notes/
title: Google Cloud Cortex Framework release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:45:11.354751+00:00
---

# Google Cloud Cortex Framework release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cortex/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Google Cloud Cortex Framework ](https://docs.cloud.google.com/cortex/docs)
  * [ Resources ](https://docs.cloud.google.com/cortex/docs/resources-v7)



Send feedback 

#  Google Cloud Cortex Framework release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Google Cloud Cortex Framework. Check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionalities.

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/cortex-release-notes.xml) directly. 

## September 02, 2026

Announcement

### Release 7.0.6

Fixed

  * Added support for logical SAP table remapping in SAP Data Foundation.
  * Added `custom/` directory scaffolding across all developer skills for local extensions.



## September 01, 2026

Announcement

### Release 7.0.5

Fixed

  * Removed obsolete review items checklist from tests.



## August 26, 2026

Announcement

### Release 7.0.4

Fixed

  * Removed unused dependencies (pandas, pytest-bigquery-mock) and lockfile cleanup.



## August 14, 2026

Announcement

### Release 7.0.3

Fixed

  * Resolved an issue where `SapBdcProductBuilder` incorrectly enforced SAP-versioned sections (ecc, s4, common) in `table_settings`.



## August 11, 2026

Announcement

### Release 7.0.2

Fixed

  * Resolved security vulnerabilities in transitive dependencies by updating the following corresponding direct dependencies: `google-auth`, `google-cloud-bigquery`, `google-cloud-dataform`, `google-cloud-resource-manager`, `google-cloud-service-usage` and `google-cloud-storage`.



## August 07, 2026

Announcement

### Release 7.0.1

Fixed

  * Resolved an issue where running the [`uv run cortex-build`](https://docs.cloud.google.com/cortex/docs/uv-run-cortex-build) command in Windows PowerShell or Windows Command Prompt resulted in a `Could not auto-import local builder` warning and an `Invalid builder type NoneType for category ...` error.

  * Improved Dataform quota management in [`uv run cortex-deploy`](https://docs.cloud.google.com/cortex/docs/uv-run-cortex-deploy) script.




## July 30, 2026

Announcement

### Release 7.0.0-GA (General Availability)

**Note: Important upgrade considerations for Version 7**

  * **Upgrading from v6:** Because v7 is a new major version it implies breaking changes with no automatic migration path. For v6 customers looking to adopt v7, we provide [v6 compatibility content for SAP reporting.](https://docs.cloud.google.com/cortex/docs/v6-compatibility)
  * **Upgrading from a v7 Preview:** Due to configuration model improvements, you must recreate your configuration files and re-deploy



Feature

Google Cloud Cortex Framework version 7 is now generally available. Version 7 introduces a modular deployment architecture, simplified data orchestration via [Dataform](https://cloud.google.com/dataform/docs), and AI-ready data products with [BigQuery](https://cloud.google.com/bigquery/docs) and [Knowledge Catalog](https://cloud.google.com/products/knowledge-catalog) integration. This enables enterprises to build, extend, and deploy data assets and pipelines for advanced analytics and agentic use cases with less risk, complexity, and cost.

**New features and enhancements**

_additional to those released in preview_

AI, discovery, and governance:

  * **[New agentic data product builder skills](https://docs.cloud.google.com/cortex/docs/agentic-skills-for-data-product-building)** : Automate the creation and customization of data products using natural language.
  * **[New Knowledge Catalog integration](https://docs.cloud.google.com/cortex/docs/knowledge-catalog)** : Automatically synchronize deployed Cortex Framework data products and enriched metadata directly into Knowledge Catalog for discovery and governance.



Expanded data product content and integrations:

  * **[New data products available for SAP ERP](https://docs.cloud.google.com/cortex/docs/data-product#available_data_products)** : Access an expanded number of Cortex Framework delivered data products for SAP ECC and SAP S/4HANA.
  * **[New support for SAP Business Data Cloud data products](https://docs.cloud.google.com/cortex/docs/source-system-integration/sap-bdc)** : Register your SAP BDC data products with Cortex Framework for expanded use case opportunities on top.
  * **[New solution samples features](https://docs.cloud.google.com/cortex/docs/solution-samples/overview)** : Consumption data product samples for SAP ERP and SAP BDC can now be easily deployed on top of Cortex Framework managed data products.
  * **[New v6 compatibility for SAP reporting](https://docs.cloud.google.com/cortex/docs/v6-compatibility)** : Provides an option to use Cortex Framework version 6 delivered SAP BigQuery data models within the version 7 architecture to support customers looking to migrate while continuing to use v6 delivered Looker reports.



Supportability and operations: 

  * **[New observability features](https://docs.cloud.google.com/cortex/docs/observability)** : Enhanced error reporting and pipeline monitoring. 
  * **[New environment management and operations features](https://docs.cloud.google.com/cortex/docs/deployment)** : Gain deeper control over deployments with the option to provide compilation overrides that integrate cleanly with Dataform release configurations.



Change

Google Cloud Cortex Framework version 7 includes [telemetry](https://docs.cloud.google.com/cortex/docs/telemetry) to capture anonymized deployment statistics. This data helps the solution build team focus on improving modules with high adoption. Telemetry is enabled by default, but you can opt out at any time.

## June 25, 2026

Announcement

### Release 7.0.0-preview.2.1 (Public Preview)

**Note:** Due configuration structure change, upgrade to v7.0.0 GA and later require recreation of configuration files.

Fixed

Resolved a path resolution issue affecting `table_settings.yaml` in the configuration.

## June 24, 2026

Announcement

### Release 7.0.0-preview.2 (Public Preview)

**Note:** Due configuration structure change, upgrade to v7.0.0 GA and later require recreation of configuration files.

Feature

  * **[Data products for SAP ERP](https://docs.cloud.google.com/cortex/docs/data-product)** : Additional data product accelerators including: accounting documents, accounts payable, accounts receivable, addresses, agency business settlement documents, billing documents, business partners, condition contracts, controlling areas and cost elements, cost and profit centers, currency conversion, financial statement structure & versions, fiscal year variants, fixed assets, general ledger accounts, global settings, plants and storage, project structure, units of measurement, universal journal, and vendor invoices.
  * **[Extensibility guide](https://docs.cloud.google.com/cortex/docs/extensibility-guide)** : Documentation explaining how to customize and extend Cortex Framework, organized by three steps: [Custom namespace setup](https://docs.cloud.google.com/cortex/docs/extensibility-guide-namespaces), [Data foundation module creation](https://docs.cloud.google.com/cortex/docs/extensibility-guide-data-foundation), and [Data product module creation](https://docs.cloud.google.com/cortex/docs/extensibility-guide-data-product).



## April 30, 2026

Announcement

### Release 7.0.0-preview.1 (Public Preview)

**Note:** Due configuration structure change, upgrade to v7.0.0 GA and later require recreation of configuration files.

Feature

Cortex Framework **version 7** introduces a highly modular deployment architecture, simplified data orchestration via [Dataform](https://docs.cloud.google.com/dataform/docs), and enhanced support for the next generation of AI-ready data products with [BigQuery](https://docs.cloud.google.com/bigquery/docs) \- enabling enterprises to build, extend, and deploy robust data models and pipelines for advanced analytics and AI/agentic use cases. To request access to the GitHub repository, see [Request access](https://docs.cloud.google.com/cortex/docs/request-access).

  * **Key architecture features**

    * **Modular deployment and smart dependency resolution** : Deploy exactly what you need. Simply select the desired data products, and the framework will automatically identify, retrieve, and transform the necessary tables to the data foundation layer, ensuring no unnecessary data is processed. Easily add custom fields or logic without breaking standard models.
    * **Native dependency graph generation** : Automatically handle the order of operations for complex data models, ensuring prerequisite tables are ready before deploying data foundations and data products.
    * **Bring your own CDC (External data foundation)** : A flexible architecture allows you to bypass built-in Change Data Capture processing and connect your own existing CDC pipelines directly to the foundation layer.
    * **Serverless BigQuery-native execution** : Orchestration relies entirely on Google Cloud Dataform, enabling easy data transformation and processing using version-controlled SQL. No standing compute clusters or Airflow VMs are required, minimizing infrastructure overhead.
    * **Incremental loading** : Native, incremental loading configurations ensure highly efficient processing of large enterprise datasets. Significantly reduce BigQuery processing time and costs by processing only new or changed data since the last execution.
    * **High data fidelity & semantics**: Features dynamic discovery and ingestion of custom fields, robust semantic mapping (e.g. translating cryptic table names to business-friendly terms), AI-ready metadata, and advanced logic handling (e.g. integrating the SAP TCURX table for exact currency decimal shifts).
    * **Multi-system SAP support** : Built-in dynamic dependency resolution and logic differentiation allows seamless compilation and parallel deployment for both SAP ECC and SAP S/4HANA source systems. Seamlessly bring in data from multiple SAP ERP systems.
    * **Extensibility framework** : Maintain a clean separation between your custom data products and Cortex Data Products using namespaces. This ensures you can benefit from the latest Cortex updates without impacting your custom work.
  * **Data product accelerators**

BigQuery based [data product accelerators for SAP ERP](https://docs.cloud.google.com/cortex/docs/data-product#data_source_specific_data_products_for_sap_erp) (SAP ECC and S/4HANA), purpose-built for AI-readiness with agent-friendly metadata included for all data model and field-level descriptions.

  * **Solution samples for SAP ERP or SAP BDC**

Solution reference architectures and code snippets for demonstrating how to build use cases on top of Cortex Framework data products to address particular business needs.

    * **[Sales Performance Insights](https://docs.cloud.google.com/cortex/docs/sales-performance-insights)** : How to accelerate insights into sales performance health using SAP ERP or SAP BDC sourced data.
    * **[Supplier Spend Analysis](https://docs.cloud.google.com/cortex/docs/supplier-spend-analysis)** : How to accelerate insights into supplier spend position using SAP ERP or SAP BDC sourced data.



## February 27, 2026

Announcement

### Release 6.3.4

Fixed

  * **Airflow v3 support** : 
    * All Composer DAGs generated by new deployments are now compatible with Airflow v3.
    * Airflow v2 is still supported. However, consider [planning for migration](https://airflow.apache.org/docs/apache-airflow/stable/installation/upgrading_to_airflow3.html) as [it will soon reach end-of-life](https://www.astronomer.io/airflow-2-eol/).
  * **SAP:**
    * SAP CDC scripts now support custom tables containing forward slashes (`/`) in their names. Existing deployments are not affected.
    * Added optional `adrt` table to SAP CDC table list.
  * **Cortex for Marketing:**
    * Meta API is now upgraded from v21 to v25. For field name changes, see [changelog](https://developers.facebook.com/docs/marketing-api/marketing-api-changelog/).
  * **Minor fixes:**
    * Migrated Cloud SDK to `gcloud storage` CLI.
    * Fixed for line breaks in DAG packages import.
    * Improved error handling for target bucket access verification.



## December 17, 2025

Deprecated

  * **SAP** : Cortex's Data Mesh functionality has been deprecated. This change is prompted by the evolution of Google Cloud data management services. The Data Mesh solution was built using Data Catalog for metadata management, which is now being replaced by the more advanced [Dataplex Universal Catalog](https://docs.cloud.google.com/dataplex/docs/introduction). Dataplex Universal Catalog provides a unified API, enhanced metadata capabilities, and new features for a more comprehensive data governance experience. For existing Cortex Framework users who have implemented the Data Mesh feature, we recommend transitioning to Dataplex Universal Catalog to ensure continued support and access to the latest features. For a detailed migration guide, see [Transition to Dataplex Universal Catalog](https://cloud.google.com/dataplex/docs/transition-to-dataplex-catalog).



Change

  * **SAP** : The column `DUMMY_SDDOCPARTNER_INCL_EEW_PS` has been removed from _SalesOrderPartnerFunction_ (ECC and S/4) as it is a non-standard column not used for reporting.



Fixed

  * **SAP** : Added support for future dates to `currency_conversion`.
  * **Cloud Build Image** : Updated gcloud SDK to v541 and Python library dependencies used during Cloud Build deployment.
  * **Composer DAG** : Corrected propagation of location parameterization.
  * **Cortex for Marketing** : Updated references to Google Ads API v22.



Announcement

### Release 6.3.3

## September 19, 2025

Announcement

### Release 6.3.2

Change

  * **1-Click Deployer** : 1-Click deployer now deploys the [Sustainability](https://docs.cloud.google.com/cortex/docs/dun-and-bradstreet) module when SAP ECC or S/4 is selected.
  * **SAP** : 
    * The CDC script now considers the `L` flag alongside `I` and `U` when determining which records are updated in the raw dataset. This is to account for situations where the pipeline is somehow re-configured after data load, but the CDC dataset can still be reused to avoid re-processing existing data.
    * Column names in `StockInHand` views (ECC and S/4) for `MATNR` and `WERKS` have been aligned with other views to be `MaterialNumber_MATNR` and `Plant_WERKS`. Previous column names `ArticleNumber_MATNR` and `Site_WERKS` still exist for compatibility reasons, but will be removed in a future release. Customers are advised to change their upstream consumption assets accordingly.
    * Column names in `SalesOrders_V2` views (ECC and S/4) for `ERDAT` and `ERZET` have been aligned to new names `SalesDocumentCreationDate_ERDAT`, `SalesOrderItemCreationDate_ERDAT`, `SalesOrderCreationTime_ERZET` and `SalesDocumentItemCreationTime_ERZET` to account for the correct granularity of their source table (either `VBAP` or `VBAK`) . Previous column names `CreationDate_ERDAT` and `CreationTime_ERZET` still exist for compatibility reasons, but will eventually be removed in a future release. Customers are advised to change their upstream consumption assets accordingly. Also, Sales Order Item level calendar dimensions are now added by default.
    * Column names in `Deliveries` view for `VGBEL`, `VGPOS`, and `XBLNR` are updated to `InternalReferenceDocumentNumber_VGBEL`, `InternalReferenceDocumentItem_VGPOS` `ExternalReferenceDocumentNumber_XBLNR` for more clarity. Previous column names `SalesOrderNumber_VGBEL`, `SalesOrderItem_VGPOS`, and `ReferenceDocumentNumber_XBLNR` still exist for compatibility reasons, but will eventually be removed in a future release. Customers are advised to change their upstream consumption assets accordingly. 
    * Sales Order Item level calendar dimensions are now added by default.
    * In `AccountingDocuments` view as well as the downstream `AccountingDocumentsReceivables` views, `DoubtfulReceivables`, and `DaysInArrear` metrics are now positive instead of negative to align with [official SAP guidelines](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/3cb1182b4a184bdd93f8d62e3f1f0741/39a73b581aee2160e10000000a44147b.html).
    * `SalesFulfillment` and `SalesFulfillment_PerOrder` views are updated to use `SalesOrders_V2` instead of `SalesOrders` view as their upstream source for both ECC and S/4. The view signatures are unchanged.
    * ERD for both [ECC](https://docs.cloud.google.com/cortex/docs/operational-sap#sap-ecc) and [S/4](https://docs.cloud.google.com/cortex/docs/operational-sap#sap-s4-hana) have been cleaned up and updated based on the latest changes.
  * **Marketing** : Cortex for Meridian reporting views adapted to TikTok, Meta, and YouTube (DV360) to focus on top of the funnel marketing campaigns. Search Ads data is skipped from aggregates as higher quality data is now available from Marketing Mix Modeling (MMM) Data Platform.



Issue

  * **Oracle** builds may time out when using a private worker pool created with default parameters.



Deprecated

  * **SAP** : The views `GLDocumentsHdr` and `RegionsMD` are now removed as they are no longer relevant.



Fixed

  * **SAP** : 
    * `Qty` field data type in `StockInHand` views (ECC and S/4) has been changed from `STRING` to `NUMERIC`.
    * Currency conversion and currency decimal shift in `PurchaseDocuments_Flow` views (ECC and S/4) now align with the logic implemented in all other SAP reporting views.
    * Fixed incorrect GR quantity caused by an incorrect `JOIN` condition.
    * Removed an excessive `LEFT JOIN` in the Unit of Measure Function and View Utility code to avoid possible duplicate rows.
    * Cleaned up unnecessary date casting and `ORDER BY` clauses in some views to improve performance.
  * **Salesforce (SFDC):**
    * Currency conversion logic is now updated to account for possible source currency fields that are not corporate currency in the objects (for example, `Opportunities`).
    * Updated ERD to include proper linkage to calendar dimension.



## May 14, 2025

Announcement

### Release 6.3.1

Issue

  * Oracle builds may time out when using a private worker pool created with default parameters.



Fixed

  * Resolved inconsistencies between the standard and Cortex for Meridian Quickstart demos related to Cloud Build Service Account behavior.
  * The Quickstart demo now automatically enables the Data Catalog API during its execution.



Change

  * A dedicated Cortex-specific Cloud Build Service Account will now be automatically created during the deployment process for both the standard Quickstart demo and the Cortex for Meridian Quickstart demo.
  * When executing `gcloud builds submit` command for Cortex Framework deployments, the `_BUILD_ACCOUNT` parameter is now required. If you are updating an existing deployment, ensure you provide the appropriate build account in the following format: `_BUILD_ACCOUNT='projects/SOURCE_PROJECT/serviceAccounts/SERVICE_ACCOUNT@SOURCE_PROJECT.iam.gserviceaccount.com'`.



## April 22, 2025

Fixed

  * Resolved duplicate entries from `VendorsMD`
  * Fixed DATE_ADD overflow issue in`InventoryByPlant`.
  * Fixed mislabeled columns in `AccountingDocumentsReceivable`.
  * Addressed JSON parsing errors related to FLOAT numbers in Meta Raw to DAG Change Data Capture (CDC).
  * Fixed a typo in the `LeadsCaptureConversions` Salesforce (SFDC) reporting table: `LeadFirstResponeDatestamp` corrected to `LeadFirstResponseDatestamp`.



Deprecated

  * CATGAP has been deprecated.
  * SAP Machine Learning (ML) models have been deprecated.



Feature

  * [**Task Dependent DAGs**](https://docs.cloud.google.com/cortex/docs/optional-step-task-dependent-dags): 
    * Provided out-of-the-box, recommended DAGs and task dependencies for SAP ECC/S4 reporting.
    * Enabled the creation and deployment of customized task-dependent reporting settings for all data sources.



Change

### Release 6.3

Feature

  * **[Cortex for Meridian](https://docs.cloud.google.com/cortex/docs/meridian)**. 
    * Cortex Framework for [Meridian](https://developers.google.com/meridian), Google's open-source Marketing Mix Modeling (MMM) tool (v1.0.5), delivers ready data models and automation of Meridian Model execution using Google Cloud tools like Colab Enterprise and Cloud Workflows.
    * This integration empowers users to make data-driven marketing decisions by providing accurate campaign performance measurement and budget optimization.
    * Cortex for Meridian simplifies the pre-modeling process by gathering and transforming data from core Cortex Framework data sources, including: 
      * [Cross Media & Product Connected Insights](https://docs.cloud.google.com/cortex/docs/marketing-cross-media)
      * [SAP (ECC and S/4 HANA)](https://docs.cloud.google.com/cortex/docs/operational-sap)
      * [Oracle EBS](https://docs.cloud.google.com/cortex/docs/operational-oracle-ebs)



## March 04, 2025

Deprecated

The following standalone accelerators and samples are removed from Cortex Framework:

  * Demand Sensing
  * AppLayer
  * CATGAP
  * SAP ML Model samples



Change

  * Minor refactoring for Data Mesh configuration specs code, which are now moved to the `/src/common/py_libs` directory.



Feature

_New Data Sources_

  * **Marketing:[Cross Media & Product Connected Insights](https://docs.cloud.google.com/cortex/docs/marketing-cross-media)**. Understand the effectiveness of marketing campaigns running across media platforms such as Google Ads, YouTube (with DV360), Meta, and TikTok for product and product category sales performance with the power of Gemini Flash 2.0. Access the [Looker Block for Cross Media](https://docs.cloud.google.com/cortex/docs/looker-block-cross-media) with sample dashboards for further analytics.
  * **[Cortex Common Dimensions](https://docs.cloud.google.com/cortex/docs/optional-step-common-dimensions)** : Newly added utility views and tables created within the Data Foundation to enable advanced use cases across different data sources, such as Cross Media & Product Connected Insights. Currently Country, Product Hierarchy and Currency Conversion are available.



Announcement

### Release 6.2

Fixed

  * SAP CDC Deployer now provides detailed error messages on failure.
  * SAP Reporting - Fixing abundant join condition in `PurchaseDocuments_Flow` view.
  * For all DAGs, BigQuery execution now happens in the same location as the dataset.
  * 1-click deployer usability fixes for CM360 and SFMC bucket names.



## January 28, 2025

Libraries

Updated the Cortex libraries for Meta to use v21.0 of the [Meta Marketing API](https://developers.facebook.com/docs/marketing-apis/).

## December 19, 2024

Announcement

### Release 6.1

Feature

  * **SAP Annotations** : All SAP Reporting views and fields are now fully annotated with functional descriptions and business context. [Deploy Data Mesh](https://docs.cloud.google.com/cortex/docs/datamesh#deploying_the_data_mesh) to take advantage of this feature.



Change

  * **Google Ads Campaign Daily Aggregates view has been redesigned** : 
    * The `CampaignDailyAggByUserCountry` view is now removed.
    * Relevant information is now integrated into the `CampaignDailyAgg` view.
  * **SAP Financial Model Initial Load** : The Financial Model's initial load has been separated into a dedicated DAG for better organization.
  * **SAP Inventory Module** : Removed "Preview" tag.



Deprecated

  * **SAP Hierarchy Reader** : As announced in the previous release notes, the `hier_reader` code has been fully deprecated. Relevant `SAMPLE` scripts have been updated to use the new hierarchy reader DAG output tables.
  * **SAP Fiscal and Currency functions** : As announced in the previous release notes, these functions have been removed. Please use the relevant tables (`currency_conversion`, `currency_decimal`, and `fiscal_date_dim`) instead.



Issue

  * [**Google Trends DAG**](https://docs.cloud.google.com/cortex/docs/optional-step-external-datasets): The Google Trends API calls issued by this DAG [may intermittently fail](https://github.com/GeneralMills/pytrends/issues/561). If this happens, try rerunning the DAG.
  * **1-click deployer:** The 1-click deployer for Oracle EBS currently requires manual naming. Autoname mode is not yet supported.



Fixed

  * **SAP Currency Decimal Fix** : Fixed a decimal precision issue for SAP currency data.
  * **Minor JOIN Condition Issue** : Fixed a JOIN condition in SAP Billings view comments.
  * **1-Click Deployer** : 
    * Fixed an issue with incorrect default Google Analytics 4 CDC dataset setting.
    * Updated to use different output bucket names for SFMC and CM360. 
  * **K9 Deployer** : Fixed the issue where temporary files were copied to the tmp* directory in the target bucket and not removed.
  * **Minor Fixes** : Addressed other minor issues related to dependency, configuration handling, Python library requirements, and DAG steps.



## October 21, 2024

Change

### Release 6.0.1

  * Quickstart demo updates for permissions with legacy accounts.
  * CATGAP Python library vulnerability updates.



## September 30, 2024

Announcement

### Release 6.0

Change

_GitHub Submodules_

Submodules are officially removed. Workloads have been migrated as follows:

**Previous Submodule** | **New Directory**  
---|---  
[cortex-dag-generator](https://www.github.com/GoogleCloudPlatform/cortex-dag-generator) | [cortex-data-foundation/tree/main/src/SAP/SAP_CDC](https://github.com/GoogleCloudPlatform/cortex-data-foundation/tree/main/src/SAP/SAP_CDC)  
[cortex-ml-models](https://www.github.com/GoogleCloudPlatform/cortex-ml-models) | [cortex-data-foundation/tree/main/src/SAP/SAP_ML_MODELS](https://github.com/GoogleCloudPlatform/cortex-data-foundation/tree/main/src/SAP/SAP_ML_MODELS)  
[cortex-reporting](https://www.github.com/GoogleCloudPlatform/cortex-reporting) | [cortex-data-foundation/tree/main/src/SAP/SAP_REPORTING](https://github.com/GoogleCloudPlatform/cortex-data-foundation/tree/main/src/SAP/SAP_REPORTING)  
[cortex-salesforce](https://www.github.com/GoogleCloudPlatform/cortex-salesforce) | [cortex-data-foundation/tree/main/src/SFDC](https://github.com/GoogleCloudPlatform/cortex-data-foundation/tree/main/src/SFDC)  
[cortex-marketing](https://www.github.com/GoogleCloudPlatform/cortex-marketing) | [cortex-data-foundation/tree/main/src/marketing](https://github.com/GoogleCloudPlatform/cortex-data-foundation/tree/main/src/marketing)  
  
**Note** : As announced in release 5.4, workload specific repositories will continue to receive code updates for at least one more release.

Feature

_New Cloud Build features support_

Added support for the following Cloud Build features:

  * [Private worker pools](https://docs.cloud.google.com/cortex/docs/optional-step-cloud-build-features#build_with_a_private_worker_pool): Run Cortex Framework deployment builds in your Cloud Build private worker pool.
  * [Regional builds](https://docs.cloud.google.com/cortex/docs/optional-step-cloud-build-features#build_in_a_specific_region): Specify a region for Cortex Framework deployment builds.
  * [User-specified service accounts](https://docs.cloud.google.com/cortex/docs/optional-step-cloud-build-features#deployment_with_user_created_service_account): Run Cortex Framework deployment builds with a specific service account instead of the Cloud Build default.



Issue

_Known issues and limitations_

  * Data Mesh deployments where only column descriptions are deployed require Data Catalog API to be enabled. This will be patched in a future release.
  * Local K9 for SAP produces a temporary folder (tmp*) in the target bucket for DAGs. Please, remove it manually. There is no impact in the execution.



Change

_SAP_

  * **SAP Raw to CDC DAG** : Rewrote logic and became less costly with about 25% improvement in performance.
  * **Fiscal dimension** : All views now use the new Fiscal Dimension instead of function. ECC/S4 specific Fiscal Functions are now removed as announced in v3.1. Fiscal functions will be removed in the next version.
  * **Future deprecation** : Legacy `Currency_Conversion` and `Currency_Decimal` functions will be deprecated in the next version. Join the views `currency_conversion` and `currency_decimal` instead.
  * **Finance** : New views for FSV, Cost, and Profit center hierarchy that supersedes the old `hier_reader` local k9, which will be removed in the next version. For more information, see [Cortex Framework: integration with SAP](https://docs.cloud.google.com/cortex/docs/operational-sap).
  * Improved `SalesStatus_Items` and S/4 `Billing` logic.
  * **Inventory** : Moved the following views and functions from `src/SAP/SAP_REPORTING/local_k9/inventory_snapshots` to `src/SAP/SAP_REPORTING/{SAP_FLAVOR}`; and renamed them to make the structure more logical and succinct. Also added notes and instructions on this module in the [Cortex Framework: integration with SAP](https://docs.cloud.google.com/cortex/docs/operational-sap) . There isn't any content or logic change.

    * From `00_stock_characteristics_config` to `StockCharacteristicsConfig`.
    * From `00_slow_moving_threshold` to `SlowMovingThreshold`.
    * From `0_{weekly|monthly}_inventory_aggregation.sql` to `Aggregate{Weekly|Monthly}Inventory`.
    * From `stock_weekly_snapshots_inventory_aggregation_update` to `UpdateMonthlyInventoryAggregation`.
    * From `01_stock_{weekly|monthly}_snapshots` to `Update{Weekly|Monthly}StockSnapshots`.



Feature

_New Data Sources_

  * **Marketing:[YouTube (with DV360)](https://docs.cloud.google.com/cortex/docs/marketing-dv360)**. Get comprehensive overview of your campaign spend, performance and audience targeting with actionable insights for paid media campaigns on YouTube purchased in DV360 platform. Access the [Looker Block for YouTube (with DV360)](https://docs.cloud.google.com/cortex/docs/looker-block-youtube) with sample dashboards for faster data analysis and exploration.

  * **Marketing:[Google Analytics 4 (GA4)](https://docs.cloud.google.com/cortex/docs/marketing-google-analytics)**. Understand website engagement and purchases using page views, time spent, call to action ratios, average purchases, lifetime value over time, traffic volumes, and success rates for defined conversion.

  * **[Oracle EBS](https://docs.cloud.google.com/cortex/docs/operational-oracle-ebs)** : Measure and understand Order to Cash operational metrics around sales performance, order status, order fulfillment, invoicing, and receivables with new BigQuery integration templates and data models. Access the [Looker Block for Oracle EBS](https://docs.cloud.google.com/cortex/docs/looker-block-oracle-ebs) with sample dashboards for further analytics.




Change

_Data Mesh_

  * Added support for annotations on nested fields.
  * Removed inherited default values for lake regions and zone location types. These values need to be provided if deploying lakes and zones.



Announcement

_New documentation page_

  * Cortex documentation is now live! READMEs in GitHub have been deprecated and relocated to [Google Cloud Cortex Framework documentation](https://docs.cloud.google.com/cortex/docs).



Fixed

_Misc Technical Notes_

  * Upgraded Google Ads API from v15 to v17.1. For field name changes, see [Google Ads API upgrade notes](https://developers.google.com/google-ads/api/docs/upgrade).
  * Moved deployment configs for Language and Currency to workload specific sections. This affects SAP and Oracle EBS data sources.
  * Officially dropped Airflow v1 support.
  * Adding test harness support for new BigQuery regions `africa-south1` and `europe-west10.`
  * Deployer log verbosity reduced by 75% for reporting deployment steps across all workloads.
  * Cloud Composer (Airflow) DAGs now use current python and BigQuery operators in place of deprecated `airflow.operators.python_operator` and `airflow.contrib.operators.bigquery_operator` operators.
  * Patched multiple Python library vulnerabilities.
  * Deprecated Credly badging.



## June 21, 2024

Change

### Release 5.4.2

This release changes the **Cloud Build default service account behavior** , and now it has one of the two types of service accounts by default: 

  * The legacy Cloud Build service account (`project-number@cloudbuild.gserviceaccount.com`).
  * The project's compute service account (`project-number-compute@developer.gserviceaccount.com`). 



Consequently, the [Quickstart demo deployment](https://cloud.google.com/solutions/cortex/docs/get-started) is updated to use either default service account. For more information, see [Cloud Build Service Account Change](https://docs.cloud.google.com/build/docs/cloud-build-service-account-updates).

## May 15, 2024

Change

### Release 5.4.1

  * Realigned table schema directory location for Google Ads, CM360 and TikTok, by moving it from `src/marketing/src/SOURCE/src/table_schema` to `src/marketing/src/SOURCE/config/table_schema` matching other marketing sources.
  * Reporting table refresh operation is now atomic, which ensures data is available in reporting during table refresh.



_Google Ads_

  * Renamed `Keywords` view to `KeywordStats`.
  * Added new reporting views to support campaign level metrics by country (`CampaignStats`, `CampaignStatsByUserCountry`, `GeoTargetConstant`), and new experimental views (`CampaignDailyAgg`, `CampaignDailyAggByUserCountry)`.
  * Enabled auto discovery for all accessible customer IDs. Therefore `login_customer_id` no longer needs to be explicitly specified in the Secret Manager configuration. 
  * Improved readability for raw view queries.



_Meta_

  * Updated source raw request specification format to YAML. Required fields can now be specified in a readable format.
  * Maximum load days and per request delay can be configured in `src/marketing/src/Meta/src/raw/pipelines/config.ini`.
  * Added table annotations for reporting views.
  * Fixed a bug for source raw load date range, causing data to be backfilled multiple times in edge cases.
  * Included performance optimizations of the hierarchy flattener code for SAP Finance Financial Statement Version, Profit Center, and Cost Center hierarchies.



_K9_

  * Converted scores to `INTEGER` type from `STRING` based on source definition. Sustainability views are now GA.
  * Holiday Calendar updated to correctly load data for most recent years.
  * Added support for [polymorphic fields](https://developer.salesforce.com/docs/atlas.en-us.soql_sosl.meta/soql_sosl/sforce_api_calls_soql_relationships_and_polymorph_keys.htm) to Salesforce Sales Cloud (SFDC).
  * SFDC encoding text is now configurable in `src/SFDC/src/raw_dag_generator/dependencies/config.ini`. Default value is UTF-8.



_Repository READMEs_

  * Moved SAP and Salesforce Sales Cloud (SFDC) content from main README to their respective README files.
  * Added Google BigQuery Connector for SAP configuration considerations to the [README_SAP](https://github.com/GoogleCloudPlatform/cortex-data-foundation/blob/main/README_SAP.md#prerequisites-for-sap-replication).



## March 09, 2024

Change

### Release 5.4

_Plan migration_

  * Cortex Framework employs multiple submodule repositories, however the [Cortex Data Foundation repository](https://github.com/GoogleCloudPlatform/cortex-data-foundation/tree/main) would no longer contain submodules.
  * Cloud Composer 1 is entering in [post-maintenance mode](https://docs.cloud.google.com/composer/docs/how-to/managing/creating), and Cortex support for Airflow 1 and Cloud Composer 1 is ending. Plan to upgrade to Airflow 2 and Cloud Composer 2. For more information, see [Migrate environments to Cloud Composer 2](https://docs.cloud.google.com/composer/docs/migrate-composer-2-snapshots-af-2).



_Marketing_

  * **New Meta data source** : Measure and understand [Meta (Facebook and Instagram)](https://www.facebook.com/business) paid media campaign performance with new BigQuery integration templates, data models, and a [Looker Semantic Model](https://github.com/looker-open-source/block-cortex-meta) with sample dashboards for further analytics. 
  * **New Salesforce Marketing Cloud (SFMC) data source** : Measure and understand [SFMC](https://www.salesforce.com/eu/products/marketing-cloud/platform/) email marketing campaign performance with new BigQuery integration templates, data models, and [Looker Semantic Model](https://github.com/looker-open-source/block-cortex-sfmc) with sample dashboards for further analytics.
  * Support for Google Ads API updated to [v15](https://ads-developers.googleblog.com/2023/10/announcing-v15-of-google-ads-api.html).



_SAP Finance_

  * Added New Profit and Loss view (`ProfitAndLoss`) that shows company's revenues, expenses, and profits. Also demonstrating Financial Statement Version (FSV), cost-center, and profit-center hierarchy.
  * Added sample Financial Income Statement Dashboards for Profit and Loss view to the [Looker Semantic Model for Cortex SAP Framework](https://github.com/looker-open-source/block-cortex-sap/blob/main/RELEASE_NOTES.md).
  * Hierarchy flattener for profit-center and cost-center hierarchy.
  * Improved performance and optimization to the `financial_statements` code, which significantly decreases execution time and resources required for `FinancialStatement` and `BalanceSheet` views.



_K9 - Sustainability_

  * Added Intelligent ESG data for Sustainability analysis utilizing Dun and Bradstreet sourced data with [Sustainability Looker Studio Dashboard](https://lookerstudio.google.com/c/reporting/cab436f2-ff83-4cfa-b7e4-e99b9fd9a8d0/page/p_wa5lq4dsfd) samples. This feature is experimental. The data model is subject to change in subsequent releases.



_Other changes_

  * Now obtain and share a Credly Digital Badge after a successful deployment of Cortex Framework.
  * Salesforce (SFDC): Added Line of Business Catalog tags for Data Mesh annotations.
  * Updated Cortex Data Foundation principal [README](https://github.com/GoogleCloudPlatform/cortex-data-foundation/blob/main/README.md). This simplifies searches for deployment content and data sources separately. [SAP](https://github.com/GoogleCloudPlatform/cortex-data-foundation/blob/main/README_SAP.md), [SFDC](https://github.com/GoogleCloudPlatform/cortex-data-foundation/blob/main/README_SFDC.md), and [Marketing](https://github.com/GoogleCloudPlatform/cortex-data-foundation/blob/main/README_Marketing.md) workloads have separate pages now.
  * Updated `DAG ApacheBeam[gcp]` version requirements to 2.53.0. New test harness regions added: `me-central1` and `me-west1`. Addressed a variety of vulnerabilities in Python library versions.
  * Known Issues And Limitations from previous release are still in effect.
  * It's expected that only the company code `C006` balances in the SAP Finance test harness data.



## January 19, 2024

Fixed

### Release 5.3.1

  * Fixed race condition and numbering sorting that leads to Cloud Build sequence bypass (`SAP_REPORTING/common/materializer/generate_build_files.py`).
  * Experimental preview of hierarchy flattener and base view for P&L Report. These artifacts are subject to change to include further optimizations, but provide a preview of an upcoming feature.



## January 04, 2024

Change

### Release 5.3

  * New experimental functionality to deploy Data Mesh definitions leveraging Data Catalog, Dataplex and BigQuery. Current functionality includes definitions for lakes, zones, access policies, and other exciting features. By default, configuration only creates descriptions in BigQuery and doesn't require any additional configuration.
  * Experimental Balance Sheet report with financial statement version flattening is available. Due to potential performance issues, the underlying data processing pipeline is under development for optimization and would be improved in a future release based on user input. Review CDC settings, as ACDOCA, BSEG and BKPF have modified clustering and partition settings.
  * New persisted and optimized fiscal time dimension.
  * Google Ads ingestion pipeline upgrade to Google Ads API version 15.
  * Minor modifications to marketing ingestion pipelines for LiveRamp: streamlined imports for Python libraries.
  * Directory `external_dags` for SAP was converted into local K9.
  * Modification on `AccountsPayable` for S4 to match invoice based on reference.



_Known issues and limitations_

  * Local K9 for SAP produces a temporary folder (`tmp`) in the target bucket for DAGS. Remove it manually. There is no impact in the execution.
  * Nested fields aren't supported yet by Data Mesh annotations. They would be incorporated in a follow-up release.
  * It's expected that data in the test harness for finance doesn't zero out in the balance sheet because it is incomplete.



## November 20, 2023

Fixed

### Release 5.2.1

  * Performance improvements for SAP Inventory. Updated `InventoryByPlant` and `InventoryKeyMetrics` for ECC and S4 to reduce memory processing requirements. Updated partitions and clusters for `StockMonthlySnapshots` and `StockWeeklySnapshot`.
  * Increasing Cloud Build timeout for SAP reporting deployment and Data Foundation deployer.



## September 28, 2023

Change

### Release 5.2

  * **LiveRamp for Marketing** : New integration templates and data models to enable identity resolution by integrating with [LiveRamp](https://docs.liveramp.com/identity/en/identity-resolution.html).
  * **SAP Reusable DAGs** are now deployed via the K9 deployment mechanism so they now behave like other cross-workload DAGs. This applies to all DAGs in the [`external_dag`](https://github.com/GoogleCloudPlatform/cortex-reporting/tree/cca3c1c86047d5ea387c50dc5e4eccdb27141775/external_dag) directory. These DAGs no longer search for SQL files from `bq_data_replication` directory. If you have modified the SQLs for them, follow these steps to migrate: 
    1. Back up any SQL file(s) you have modified from `gs://<your_airflow_bucket>/data/bq_data_replication`.
    2. If any of the relevant DAG(s) are running, pause them in Airflow.
    3. Deploy Cortex Data Foundations v5.2.
    4. Copy your modified SQL file into the deployment directory, which by default is `gs://<your_deployment_bucket>/dags/sap/reporting/<dag_name>`.
    5. Copy `/dags` directory from the deployment bucket into your Airflow bucket. Then, wait for Airflow to refresh, and unpause the DAGs in Airflow.
    6. Remove migrated files from `gs://<your_airflow_bucket>/data/bq_data_replication`.
  * **Metadata for SAP and TikTok:** New experimental annotations feature for SAP artifacts. The deployer now creates views with descriptions for views and their fields.
  * **Support for new regions** : New supported regions incorporated into the test harness.
  * Fix for set hierarchy reader in SAP, generating a node with no associated main data for the header.



## August 28, 2023

Change

### Release 5.1

  * New TikTok for Marketing: New integration templates and data models for TikTok to measure paid media campaign performance insights, through impressions and reach. 
  * Placeholders for [K9 views](https://github.com/GoogleCloudPlatform/cortex-data-foundation#configure-k9-deployments) are now created for each workload.
  * New experimental feature to help gather necessary data to request support after a failed deployment. This feature gathers the logs and the configuration to be sent to [`cortex-support@google.com`](mailto:cortex-support@google.com).
  * Added option to calculate doubtful receivables and days in arrear as positive amount in AccountingDocuments. 
  * Pull [request #9](https://github.com/GoogleCloudPlatform/cortex-reporting/pull/9) from SAP Reporting, adding safe divide for Fill rate Percent.



## August 03, 2023

Fixed

### Release 5.0.1

  * Enhanced validation of permissions and assets existence as the first step in deployment. The former `Mando Checker` is now executed at the beginning of the validation process. The deployer attempts to create, write and delete temporary files and datasets in the targets to validate permissions.
  * Minor tweaks and some image refreshes in the Cortex Data Foundation README.
  * Move pre-processing or post-processing K9 configuration to individual manifests to simplify execution.
  * Test harness: Restore behavior to ignore a table in Raw if it exists, and it has no records, and `testData` is set to `True`.
  * Materializer: Restore behavior to attempt to build all views sequentially when `turbo mode` is set to `False`.



## July 14, 2023

Change

### Release 5.0

  * [Cortex for Marketing](https://github.com/GoogleCloudPlatform/cortex-marketing), has been added to the Data Foundation. For more information, see the Entity Relationship Diagram (ERD) in the [docs](https://github.com/GoogleCloudPlatform/cortex-data-foundation/tree/main/docs) folder.
  * Created quickstart demo deployment.
  * K9 cross-workload and source reusable models.
  * Optional materialization and performance optimization enabled for all modules and views. This impacts the SQL templates previously containing a `CREATE` statement. Check the new default configurations as this attempts to replace some views with tables. 
  * [CATGAP](https://github.com/GoogleCloudPlatform/cortex-data-foundation/tree/main/src/k9/src/catgap) has moved to K9. The deployment is disabled by default.
  * The test harness data has now moved from buckets into BigQuery datasets available in all relevant regions. Test harness data isn't provided with any warranty of quality, but this change simplifies and speeds up the deployment for those exploring the framework.
  * Substitutions are removed, except for Logs in Cloud Storage bucket. Configuration files are now normalized into `config.json`. Legacy Dotenv files have been removed.
  * DeployCDC is now specific to each workload.
  * GenerateExtraData is now removed, the control of this deployment is owned by K9.



_SAP_

  * SAP-specific DAGs, like currency conversion, inventory management or hierarchy reader, were moved to the reporting module and are executed by default.
  * Configured [reporting configuration for materialization](https://github.com/GoogleCloudPlatform/cortex-reporting/blob/main/reporting_settings_ecc.yaml) to improve match customer expectations, but it might not apply to your business at all.
  * UNION deployment logic has been removed, but supported views continue to have the UNION template until further notice.
  * The reporting module relies on the time dimension deployment in K9, it can be executed manually if deploying from the [cortex-reporting submodule](https://github.com/GoogleCloudPlatform/cortex-reporting/).



_Salesforce_

  * New currency conversion for Salesforce. Since these are optional components for Salesforce deployments, they can be created through the placeholder settings. If you don't have the currency types and conversion in Salesforce, comment out or remove the calls in `SFDC/config/ingestion_settings.yaml`. The configuration in `cdc_placeholder_settings.yaml` now takes care of the dependencies in the reporting views.
  * The reporting module relies on the time dimension deployment in K9, it can be executed manually if deploying from the [Salesforce submodule](https://github.com/GoogleCloudPlatform/cortex-salesforce).



_Known issues and limitations_

  * SAP Reporting and Salesforce Reporting requires execution of K9 pre-processing if used as a separate submodule.
  * ML Models repository still allows for substitutions.
  * CM360 and Ads integration scripts are in `Experimental` mode while we gather early feedback from customers on usage. 
  * Google Ads DAG is supported on Airflow v2 only.



## April 01, 2023

Change

### Release 4.2

  * **New Supply Chain and Finance views** : These views support KPIs for Inventory management, Vendor Performance, Accounts Payable and Spend Analysis. The new objects are: 
    * **Reusable DAG scripts for inventory snapshots** (`SAP_CDC/external_dag/inventory_snapshots`): Initializer and periodic update for weekly and monthly inventory snapshots and aggregations, slow moving threshold, and stock characteristic configuration. Review for `CORTEX-CUSTOMER` comments for potential updates needed for custom thresholds and material movements. These scripts are in `PREVIEW` and would be moved into another structure in deployment in the next major release. These scripts fill the base tables and need to be scheduled for the reporting views to function properly.
    * **New views for reporting** : `AccountsPayableOverview, DaysPayableOutstanding, InventoryByPlant, InventoryKeyMetrics, MaterialLedger, MaterialMovementTypesMD MaterialsBatchMD, POScheduleLine, PurchaseDocumentsHistory, SalesOrderStatus, SlowMovingThreshold, StockCharacteristicsConfig, StockInHand, StockMonthlySnapshots, and StockWeeklySnapshots`.
    * **New overview views** : `VendorLeadTimeOverview` and `VendorPerformanceOverview`. These views show the reporting logic used in Looker in case you want to replicate them in another tool or a microservice. These views aren't deployed by default.
  * **Materializer preview** : By default, the new views that require a lot of computation are now deployed as materializing DAGs.
  * **Cortex Analytics Templates - Google Ads Pipelines (CATGAP)** : This new experimental feature uses Natural Language Processing Machine Learning models to intelligently map product categories from Google Ads to SAP's product hierarchy. For more information, see [CATGAP](https://github.com/GoogleCloudPlatform/cortex-data-foundation/tree/main/src/k9/src/catgap) for details and further setup.
  * Reporting views that expect parameters from currencies in `config/config.json` now produce the same result as many times as currencies are set as targets. Check for `CORTEX-CUSTOMER` comments for specific guidance if you deploy the data foundation with more than one currency.
  * Parameters that control runtime (for example, `DEPLOY_SAP`, `DEPLOY_SFDC`, `DEPLOY_CDC`, and `TEST_DATA`) are now read from the `config` file. These are still defaulted in `cloudbuild.yaml` substitutions. If you want to use the values in the file, the [substitutions section in `cloudbuild.yaml`](https://github.com/GoogleCloudPlatform/cortex-data-foundation/blob/main/cloudbuild.yaml#L107) needs to be commented out. Substitutions from the command line would be phased out.
  * Compatibility for Airflow v1 and v2 updated for `currency_conversion` DAG.
  * Addressing [SFDC Issue #2](https://github.com/GoogleCloudPlatform/cortex-salesforce/issues/2).



_Known Issues and Limitations_

  * If using the SAP Reporting submodule as standalone for deployment, `sap_config.json` needs to be manually generated from `config.env` for the materializer to read as input. Dotenv files would be removed in the next major release, and this would be addressed for SAP submodules.
  * New views aren't released for `UNION` mode.



## February 17, 2023

Change

### Release 4.1

  * More options for Salesforce integration with provided scripts or external tools: End-to-end integration from Salesforce APIs (provided out-of-the-box), structure mapping with no change data capture processing and optional CDC and mapping generation scripts.
  * Option for `sequential` deployment (`TURBO=false`) for SFDC incorporated.
  * Salesforce integration now updates the RAW tables with changes, merging changes on landing. This removes the need for additional CDC processing. Deltas are captured using SystemModstamp provided by Salesforce APIs.
  * `IsArchived` flag is removed from CDC processing for Salesforce.
  * Errors originating from _gsutil_ steps in `cloudbuild.sfdc.yaml` not finding files to copy are now caught and surfaced gracefully.
  * Removing some `substitution` defaults (for example, `LOCATION`) from `cloudbuild.yaml` file so all configurations are either passed from the command line or read from `config/config.json`. These parameters would be removed from substitution defaults in future releases.
  * Detecting version for Airflow in DAG templates to use updated libraries for Airflow v2 in SAP and Salesforce. This removes some deprecation warnings, but it might need additional libraries installed in your Airflow instance.
  * Fix for test harness data not loading in an intended location when the location isn't passed as a substitution.
  * Checking existence of DAG-generated files before attempting to copy with `gsutil` to avoid errors.
  * Structure of RAW landed tables has changed to not require additional DAG processing. Review the documentation about mapping and use of the new extraction process before upgrading to avoid disruption.



## January 16, 2023

Change

### Release 4.0

  * New [Salesforce](https://github.com/GoogleCloudPlatform/cortex-salesforce) data source. The module includes optional integration and CDC scripts and reporting views. For more information, see the [Entity Relationship Diagram](https://github.com/GoogleCloudPlatform/cortex-data-foundation/blob/main/images/erd_sfdc.png) for a list of tables and views and the [Looker repository](https://github.com/looker-open-source/block-cortex-salesforce) for sample dashboards.
  * New configuration file (`config/config.json`) for deployment parameters. We maintain backward compatibility with the existing `gcloud builds submit` command parameters. Enhanced parameters like `SAP UNION` datasets and those for Salesforce, can be configured in `config.json`. This file format replaces the `.env` format for `SAP_REPORTING` in the next releases.
  * New preview models for SAP Finance: `AccountingDocumentsReceivable, AccountsPayable, AccountsPayableTurnover, CashDiscountUtilization, CurrencyConversion` (exposing table processed by DAG), `VendorPerformance, and VendorConfig` (dependant on TVARVC values). 
  * New split views for SAP Order-To-Cash: `SalesOrderPricing` and `PricingConditions`. For more information, see the updated [Looker reports](https://github.com/looker-open-source/block-cortex-sap) to make use of the split models.



_Known issues and limitations_

  * Salesforce integration DAGs have been tested in Airflow 1.0 and Airflow 2.0. They might require library updates or use of backwards compatible libraries to be tested and confirmed in the next release.
  * Finance views for SAP are good candidates for partial or total materialization. Check BigQuery's execution details to identify opportunities to create materialization processes and further optimizations that fit your data best.



## November 27, 2022

Change

### Release 3.1

  * New configurable partitioning and clustering on deployment of CDC landing tables and scripts. See example in [`cdc_settings.yaml`](https://github.com/GoogleCloudPlatform/cortex-dag-generator/blob/main/cdc_settings.yaml).
  * New date dimension generated from external DAGs through `_GEN_EXT=true` to allow for more flexibility in reporting. This table has been incorporated into views `POSchedule, MaterialsValuation, PurchaseDocuments, Deliveries, Billing, SalesOrderScheduleLine, AccountingDocuments, InvoiceDocuments_Flow, POOrderHistory, and SalesOrders_V2`. The structure of the table is generated without data if `_GEN_EXT=false`. If you don't want to execute the generation of other DAGs for external sources, remove them from the list in the generation script.
  * Performance improvements to `AccountingDocuments, InvoiceDocuments_Flow,Billing, Deliveries, MaterialsValuation, PurchaseDocuments, POOrderHistory, and SalesOrders_V2` when using currency conversion generated from DAG materializing results (see `CORTEX-CUSTOMER` tags and differences when merging).
  * New preview views modularizing functionality from SalesOrders_V2: `OneTouchOrder, SalesOrderHeaderStatus, SalesOrderScheduleLine, SalesOrderPartnerFunction, and SalesOrderDetails_SAMPLE`.
  * Replacing `ECC` or `S4` specific functions with non-specific (for example, `fiscal_Case_ecc` or `fiscal_case_s4` now is `fiscal_case`). SQL flavor-specific functions would be commented out from generation in the next release.



## September 07, 2022

Change

### Release 3.0

  * New submodule structure. All SAP-related submodules have been moved under the directory `src/SAP/`. 
  * Submodules now execute independently. SAP's ML Models and SAP Reporting submodules now have their own YAML file for independent execution.
  * New experimental `UNION` logic available if your SAP ECC and S/4 systems don't share the same MANDT. All views are now moved to `/ecc` or `/s4` respectively. This alters the templates of all of the views and requires two sets of datasets (for example, one `raw landing` for ECC, one for S/4). These datasets can be passed to the deployment in the file `sap_config.env`.
  * SAP Reporting can now be deployed using a configuration file (`sap_config.env`) instead of parameters from the `gcloud builds submit --substitutions` command. Parameters received from the substitutions override configurations in the file to maintain backwards compatibility. This affects all the `cloudbuild.yaml` files.
  * New simplified view for Sales Orders (`_SalesOrders_V2_`) with less underlying joins for use cases that don't require them.
  * New experimental views for a collaboration with [C3.ai](https://c3.ai/). These views are considered `experimental` as we increase the functionality around and on top of them in collaboration with C3.ai. Experimental views are flagged with an `## EXPERIMENTAL` comment.
  * Turbo mode for SAP Reporting: The file `sap_config.env` contains a variable called `TURBO`. If set to `true`, the `cloudbuild.yaml` file is generated dynamically from the dependencies file. This reduces the deployment time.
  * Candidates for enhancement points within the code, that is portions where customers should consider incorporating changes or applying extensions, are flagged with a comment `## CORTEX-CUSTOMER`.
  * Templatized currency and language for views that require the values to be hardcoded for better performance. 
  * New non-changing views created as tables by default. Sources that are unlikely to ever change (for example, material document types, valuation areas) are now created as tables, instead of views, by default. 
  * Added the following new views: `WeatherDaily, SalesOrders_V2, DeliveryBlockingReasonsMD, BillingBlockingReasonsMD, StorageLocationsMD, PurchaseDocumentTypesMD, MovementTypesMD, ReasonForMovementTypesMD, SpecialStocksMD, PurchasingOrganizationsMD, BatchesMD, MaterialPlantsMD, ProductionOrders, PurchasingGroupsMD, MaterialsValuation, MaterialsMovement, MaterialTypesMD, BillOfMaterialsMD, DivisionsMD, and ValuationAreasMD`.
  * Added new DAG for currency conversion and currency decimal shifting. 
  * When test data is set to true, the dynamically generated `MERGE` operation now copies the test data from the raw landing dataset into the CDC dataset. Test data in CDC dataset isn't copied as it is from the raw landing. Test data is still meant to provide a base for specific demo scenarios and isn't guaranteed to be a reliable source with any quality or referential integrity.
  * Started marking releases with tags. This release is [v3.0](https://github.com/GoogleCloudPlatform/cortex-data-foundation/releases/tag/v3.0)
  * Views for ECC are now matched in S4. 
  * New guide with [recommendations for upgrades](https://github.com/GoogleCloudPlatform/cortex-data-foundation/blob/main/docs/upgrade_recommendations/upgrade_recommendations.md).



## August 15, 2022

Change

### Release 2.2

  * New external datasets available: Holidays, Weather, Trends and product hierarchy flattener to feed the Trends search terms.
  * Region-specific deployments with test data are now possible. For more information about supported regions and limitations of regional datasets in BigQuery, see [BigQuery locations](https://docs.cloud.google.com/bigquery/docs/locations).
  * Addressing records with the same key and operation flag sent more than once in different chunks into raw landing.
  * Escaping of table and column names in DAG and real-time view generation to avoid issues with reserved words ([Issue #7](https://github.com/GoogleCloudPlatform/cortex-data-foundation/issues/7)).
  * Minor tweak to CustomersMD: Coalesce address between customer main data and latest record in ADRC.
  * Minor correction to OrderToCash: Use CDC dataset as source for VBRP.



_Known issues_

  * Analytics hub supports regions in the EU and US . For more information, see [Analytics hub introduction](https://docs.cloud.google.com/bigquery/docs/analytics-hub-introduction). If deploying the Weather DAG in a specific location where the source linked datasets aren't available, you might need to resort to another source for weather data or create a scheduled query to feed a copy in the same location, and use a transfer service to copy the records into a table in the desired location.



## May 01, 2022

Change

### Release 2.1.1

  * Fixed AddressesMD date format to `9999-12-31`.
  * Merged original 800 and 200 demo client tables into test harness for ECC (now it has both 800 and 100). This client was mostly used for demos.
  * Commenting out deployment of Product Recommender ML model as it requires specific reservations and a sample dataset that is only offered in the US region.
  * Addressing [Issue #4](https://github.com/GoogleCloudPlatform/cortex-data-foundation/issues/4).
  * Ignoring `.INCLUDE` when generating DAGs and Runtime views.
  * Fixed RUNTIME view logic generation affecting keys with deletion.
  * New Looker blocks available replacing the older blocks.



## March 01, 2022

Change

### Release 2.1

_Features and improvements_

  * Templatized deployment and SQL Flavour for views, `setting.yaml` file and test harness to deploy either ECC or S4: 
    1. New split source of data with `MANDT = 050` for ECC and `MANDT = 100` for S/4. These populates automatically based on the `_SQL_FLAVOUR` parameter in the build (default to `ECC`).
    2. Original dataset from ECC and S/4 mixed still present in the source bucket (`MANDT = 800`).
    3. The following views would be adapted to S/4 with source tables in a next minor release: `FixedAssets, SDStatus_Items, GLDocumentsHdr, BSID and BSAD implementations, InvoiceDocuments_flow,DeliveriesStatus_PerSalesOrg, SalesFulfillment_perOrder, SalesFulfillment, and UoMUsage_SAMPLE`.
  * Additional views for ECC and S/4 with Accounts Receivables and On-Time/In-Full analysis: `Billing, OrderToCas, and AccountingDocumentsReceivable`.
  * Additional helper functions for currency conversion.
  * Additional function for Due Date calculation for discounts.
  * New helper function for Fiscal period.
  * Renamed CDC parameters to match Reporting and ML Models.
  * SAP Reporting now has a SQL Flavour switch to correctly deploy S4 or ECC based on the `_SQL_FLAVOUR` parameter. Possible values are `ECC` or `S4`.
  * Enhanced reporting and calculation logics in: `Deliveries`, `PurchaseDocuments` and `SalesOrders`.
  * Reduced CDC deployment copy step by 80% implementing multithreaded copy.
  * Optimized overall build time when Cloud Build has the container cached, improving overall deployment time by 50%.



_Bug Fixes_

  * Fix for Runtime views not generated from `settings.yaml`.
  * Deployment dependencies causing errors on view creation.



_Known issues_

  * Hierarchy flattener not configured to find sets in new test data.
  * `.INCLUDE` in some tables in some versions of S/4 is known to be marked as key, which results in invalid SQLs in DAG generation. Recommendation as of now is to clear the _keyflag_ field in the offending `.INCLUDE` entry in the replicated `DD03L` table in BigQuery when generating the DAG. 



_New_

  * [Cortex Application Layer](https://console.cloud.google.com/marketplace/product/cortex-public/cloud-cortex-application-layer): Google Marketplace offering showcasing how to consume the Cortex Data Foundation in your own cloud-native applications.
  * [Looker Blocks](https://github.com/looker-open-source/block-cortex-sap) dashboards for Orders Fulfillment, Order Snapshot, Order Details, Sales Performance, Billing, and Pricing.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
