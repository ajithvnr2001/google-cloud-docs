---
url: https://docs.cloud.google.com/data-fusion/docs/how-to/sap-order-to-cash-accelerator/
title: SAP Order to Cash accelerator \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:43.464769+00:00
---

# SAP Order to Cash accelerator  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/how-to/sap-order-to-cash-accelerator/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  SAP Order to Cash accelerator Stay organized with collections  Save and categorize content based on your preferences. 

The SAP accelerator for the [order to cash](https://en.wikipedia.org/wiki/Order_to_cash) process is a sample implementation of the [SAP Table Batch Source](https://cloud.google.com/data-fusion/docs/how-to/use-sap-batch-source-plugin) feature in Cloud Data Fusion. The accelerator helps you get started when you create your end-to-end order to cash process and analytics. It includes sample Cloud Data Fusion pipelines that you can configure to perform the following tasks:

  * Connect to your SAP data source.
  * Perform transformations on your data in Cloud Data Fusion.
  * Store your data in BigQuery.
  * Set up analytics in Looker. This includes dashboards and an ML model, where you can define the key performance indicators (KPIs) for your order to cash process.



This guide describes the sample implementation, and how you can get started with your configurations.

The accelerator is available in Cloud Data Fusion environments running in version 6.3.0 and above.

## Before you begin

  1. [ Sign in](https://accounts.google.com/Login) to your Google Account.

If you don't already have one, [ sign up for a new account](https://accounts.google.com/SignUp).

  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Cloud Data Fusion and BigQuery APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=datafusion.googleapis.com,bigquery.googleapis.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Cloud Data Fusion and BigQuery APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=datafusion.googleapis.com,bigquery.googleapis.com)

  8. Download the [SAP Table Batch Source](https://docs.cloud.google.com/data-fusion/docs/how-to/use-sap-batch-source-plugin).
  9. You must have access to a Looker instance and have the marketplace [labs feature](https://docs.looker.com/admin-options/settings/labs) turned on to install the Looker Block. You can [request a free trial](https://looker.com/demo/free-trial) to get access to an instance.



### Required skills

Setting up the SAP Order to Cash accelerator requires the following skills:

  * Expertise in SAP on-premises ERP systems and configuration
  * Familiarity with the [Cloud Data Fusion](https://docs.cloud.google.com/data-fusion/docs)
  * Familiarity with [BigQuery](https://docs.cloud.google.com/bigquery)
  * Familiarity with [Looker](https://looker.com/)
  * Familiarity with [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs/service-accounts) service accounts and access control
  * Familiarity with data analytics, including writing SQL queries
  * Familiarity with [Kimball's dimensional data model](https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/star-schema-olap-cube/)



### Required users

The configurations described on this page require changes in your SAP system and in Google Cloud. You need to work with the following users of those systems to perform the configurations:

**User type** | **Description**  
---|---  
SAP admin | Administrator for your SAP system who can access the SAP service site for downloading software.  
SAP user | An SAP user who is authorized to connect to an SAP system.  
GCP admin | Administrator who controls IAM access for your organization, who creates and deploys service accounts and grants permissions for Cloud Data Fusion, BigQuery, and Looker.  
Cloud Data Fusion user | Users who are authorized to design and run data pipelines in Cloud Data Fusion.  
BigQuery Data Owner | Users who are authorized to create, view, and modify BigQuery datasets.  
Looker Developer | These users can install the Looker Block through the [Marketplace](https://docs.looker.com/data-modeling/marketplace). They must have `develop`, `manage_model`, and `deploy` permissions.  
  
### Required IAM roles

In the accelerator's sample implementation, the following IAM roles are required. You might need additional roles if your project relies on other Google Cloud services.

  * BigQuery Admin ([`roles/bigquery.admin`](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery))
  * BigQuery Data Owner ([`roles/bigquery.dataOwner`](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery))
  * Storage Object Viewer ([`roles/storage.objectViewer`](https://docs.cloud.google.com/iam/docs/roles-permissions/storage))
  * Cloud Data Fusion Runner ([`roles/datafusion.runner`](https://docs.cloud.google.com/data-fusion/docs/access-control#roles)) needs to be granted to the Managed Service for Apache Spark service account



## Process overview

You can implement the accelerator in your project with the following steps:

  1. [Configure the SAP ERP system](https://docs.cloud.google.com/data-fusion/docs/how-to/use-sap-batch-source-plugin#configure-sap-erp) and [install the SAP transport](https://docs.cloud.google.com/data-fusion/docs/how-to/use-sap-batch-source-plugin#install-sap-transport) provided.
  2. [Set up your Cloud Data Fusion environment to use the SAP Table Batch Source plugin](https://docs.cloud.google.com/data-fusion/docs/how-to/use-sap-batch-source-plugin#set-up-data-fusion).
  3. [Create datasets in BigQuery](https://docs.cloud.google.com/bigquery/docs/datasets). The accelerator provides sample datasets for staging, dimensional, and fact tables.
  4. Configure the sample Cloud Data Fusion pipelines from the accelerator to integrate your SAP data.
  5. From the Cloud Data Fusion Hub, deploy the pipelines associated with the order to cash analytics process. These pipelines must be configured correctly to create the BigQuery dataset.
  6. Connect Looker to the BigQuery project.
  7. Install and deploy the Looker Block.



For more information, see [Using the SAP Table Batch Source plugin](https://docs.cloud.google.com/data-fusion/docs/how-to/use-sap-batch-source-plugin).

## Sample datasets in BigQuery

In the sample implementation in this accelerator, the following datasets are created in BigQuery.

**Dataset name** | **Description**  
---|---  
`sap_cdf_staging` | Contains all the tables from the SAP Source system as identified for that business process.  
`sap_cdf_dimension` | Contains the key dimension entities like Customer Dimension and Material Dimension.  
`sap_cdf_fact` | Contains the fact tables generated from the pipeline.  
  
## Sample pipelines in Cloud Data Fusion

**Note:** A table is a collection of records inside a dataset in BigQuery. A pipeline is the series of ETL functions that exist to move data between a source and a destination (such as a BigQuery table).

Sample pipelines for this accelerator are available in the Cloud Data Fusion Hub.

To get the sample pipelines from the Hub:

  1. Go to your instance: 
     1. In the Google Cloud console, go to the Cloud Data Fusion page.

     2. To open the instance in the Cloud Data Fusion Studio, click **Instances** , and then click **View instance**.

[Go to Instances](https://console.cloud.google.com/data-fusion/locations/-/instances)

  2. Click **Hub**.
  3. Select the **SAP** tab.
  4. Select **Pipelines**. A page of sample pipelines opens.
  5. Select the desired pipelines to download them.



Each of the pipelines contains macros that you can configure to run in your environment.

**Note:** Changing the SQL macros is non-trivial. For example, a change to the target schema also requires changes to the data loading and Looker configurations.

There are three types of sample pipelines:

  * **Staging layer pipelines** : The staging dataset in this type of pipeline is a direct mapping to the original source table in SAP. The sample staging layer pipelines have names that refer to the SAP source table and the BigQuery target table. For example, a pipeline named KNA1_Customer_Master refers to the SAP Source Table (`KNA1`) and BigQuery target table (`CustomerMaster`).
  * **Dimension layer pipelines** : The dimension layer dataset in this type of pipeline is a curated and refined version of the staging dataset that creates the dimension and facts needed for the analysis. The sample pipelines have names that refer to the target entity in the target BigQuery dataset. For example, a pipeline called customer_dimension refers to the Customer Dimension entity in the BigQuery dataset `sap_cdf_fact`.
  * **Fact layer pipelines** : The fact layer dataset is a curated and refined version of the staging dataset that creates the facts that are necessary for the analysis. These sample pipelines have names that refer to the target entity in the target BigQuery dataset. For example, a pipeline called sales_order_fact delivers curated data to the Sales Order Fact entity in the corresponding BigQuery dataset `sap_cdf_fact`.



The following sections summarize how to get the pipelines to work in your environment.

## Configure staging layer pipelines

There are two configuration steps for the staging pipelines:

  1. Configure the source SAP system.
  2. Configure the target BigQuery dataset and table.



### Parameters for the SAP Table Batch Source plugin

The SAP Table Batch Source plugin reads the content of an SAP table or view. The accelerator provides the following macros, which you can modify to control your SAP connections centrally.

Macro name | Description | Example  
---|---|---  
`${SAP Client}` | SAP client to use | `100`  
`${SAP Language}` | SAP logon language | `EN`  
`${SAP Application Server Host}` | SAP server name or IP address | `10.132.0.47`  
`${SAP System Number}` | SAP system number | `00`  
`${secure(saplogonusername)}` | SAP User name | For more information, see [Using Secure Keys](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/801767425/Using+Secure+Keys).  
`${secure(saplogonpassword)}` | SAP user password | For more information, see [Using Secure Keys](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/801767425/Using+Secure+Keys).  
`${Number of Rows to Fetch}` | Used to limit the number of extracted records. | `100000`  
  
For more information, see [Configuring the plugin](https://docs.cloud.google.com/data-fusion/docs/how-to/use-sap-batch-source-plugin#plugin-configuration).

### Parameters for the BigQuery target

The accelerator provides the following macros for BigQuery targets.

**BigQuery target connector configuration**

Macro name | Description | Example  
---|---|---  
`${ProjectID}` | The project ID where the BigQuery dataset has been created. | `sap_adaptor`  
`${Dataset}` | Target dataset | `sap_cdf_staging`  
  
### Sample pipelines used for order to cash KPIs

The following key business entities in the order to cash process correspond with sample pipelines in the accelerator. These pipelines deliver the data that powers the analytics about these entities.

Key business entities | Corresponding sample pipeline name  
---|---  
A `Customer` might be a person or an entity with whom the organization does business. These three SAP source tables capture details about the customer as they pertain to the business. Information from these tables contributes to the `customer_dimension` in the `sap_cdf_dimension` dataset.  |  KNA1_CustomerMaster  
KNVV_CustomerSales  
KNVP_CustomerPartnerFunction   
`Material` is the commodity that is traded between the enterprise and its customers. Information from these SAP source tables contributes to the material_dimension in the `sap_cdf_dimension` dataset.  |  MARA_MaterialMaster  
MARD_MaterialStorageLocation   
The **order management** sub-process of the order to cash process (when your system receives an order from the customer).  |  VBAK_SalesDocumentHeader  
VBAP_SalesDocumentItem  
VBEP_SalesDocumentSchedule   
The **order fulfillment and shipping** sub-processes.  |  LIKP_DeliveryHeader  
LIPS_DeliveryItem   
The **invoicing and customer payments** sub-processes (when the customer receives an invoice).  |  VBRK_BillingHeader  
VBRP_BillingLineItem   
The **accounts receivable and reporting sub-processes**(when the payment is logged in your system).  |  ACDOCA_UniversalJournalItem   
  
### All Cloud Data Fusion staging pipelines

The following Cloud Data Fusion staging pipeline samples are available in the accelerator:

  * KNA1_CustomerMaster
  * KNVV_CustomerSales
  * KNVP_CustomerPartnerFunction
  * MARA_MaterialMaster
  * MARD_MaterialStorageLocation
  * VBAK_SalesDocumentHeader
  * VBAP_SalesDocumentItem
  * VBEP_SalesDocumentSchedule
  * LIKP_DeliveryHeader
  * LIPS_DeliveryItem
  * ACDOCA_UniversalJournalItem
  * VBRK_BillingHeader
  * VBRP_BillingLineItem
  * BSEG_AccountDocumentItem
  * BSID_AccDocCustOpenItem
  * BSAD_AccDocCustCloseItem
  * T001_CompanyCodes
  * T006A_UnitOfMeasure
  * T024D_MRPControllers
  * T042ZT_PaymentMethodText
  * T189T_PriceListCategory
  * TCURC_CurrencyCodes
  * TCURT_CurrencyCodesText
  * TCURW_ExchangeRateType
  * TINCT_CustomerIncotermsText
  * TVAKT_SalesDocumentType
  * TVAPT_SalesDocumentItemCategory
  * TVFST_BillingBlockReasonText
  * TVLST_DeliveryBlockText
  * TVTWT_DistributionChannelText
  * MAKT_MaterialDescription
  * T005T_CountryNames
  * T005U_RegionText
  * TVAST_SalesDocBlockReasonText
  * T077X_AccountGroupName
  * T134T_MaterialTypeDescription
  * T023T_MaterialGroupDescription
  * TSPAT_SalesDivisionText
  * TVKOV_DistributionChannel
  * TVTA_SalesArea
  * TVKOT_SalesOrgText
  * TVAUT_SalesDocumentOrderText
  * TVSBT_ShippingConditionText
  * TVAG_SalesDocRejectionReasons
  * TVAGT_SalesDocRejectionReasonDescription



## Configure dimensional layer pipelines

You can extract KPIs from source SAP tables. To prepare the data for analysis, organize the data in the source table to match the BigQuery table's schema structure.

The accelerator creates the following four sample tables:

Table name  | Table description   
---|---  
customer_dimension | Curated list* of Customers and their associated facts such as customer classification, customer hierarchy, and customer sales-related information.  
material_dimension | Curated list of Materials and associated facts such as SKU number, product hierarchy, and classification.  
sales_order_fact | Curated list of sales information such as order types, order status visibility, ordered quantity, and order value. These fields are typically aggregated to generate order management KPIs such as Open Orders, Confirmed Orders, Rejected Orders, and Billed Orders.  
revenue_fact | Detailed accounting information generated by the Sale of the Material to Customers. Derived from the Accounting tables, this fact table contains information that can provide insights through Revenue KPIs including Gross Sales, Net Sales Before Discount, Net Sales After Discount, or Trends.   
  
*In this context, the curated list comes from business logic that gets applied to the selected list of columns.

The accelerator builds the dimensional layer of the BigQuery dataset using SQL scripts, which you can modify for your project. For example, you can adapt these scripts to add more columns to the target BigQuery dataset entities.

### Transformation to star schema: BigQuery executor pipeline names

The following BigQuery executor pipelines in Cloud Data Fusion load data into dimension and fact tables:

### All dimensional transformation pipelines:

  * `customer_dimension`
  * `material_dimension`
  * `sales_order_fact`
  * `revenue_fact`



#### BigQuery executor configuration

Macro name | Example  
---|---  
`${ProjectID}` | `sap_adaptor`  
`${StagingDatasetName}` | `sap_cdf_staging`  
`${TargetDatasetName}` | `sap_cdf_dimension`  
  
## Connect Looker to the BigQuery project

To connect Looker to BigQuery, see the Looker documentation about [BigQuery connections](https://docs.looker.com/setup-and-management/database-config/google-bigquery).

### Install the block

**Note:** You need access to a Looker instance to install and use this block.

You can access the [SAP Looker Block](https://github.com/llooker/sap_data_fusion_block) on GitHub.

The [Looker Block](https://docs.looker.com/data-modeling/looker-blocks) installs a pre-configured [LookML](https://docs.looker.com/data-modeling/learning-lookml/what-is-lookml) model with two [Explore](https://docs.looker.com/exploring-data/exploring-data) environments and two dashboards.

## What's next

  * Learn more about [Cloud Data Fusion](https://docs.cloud.google.com/data-fusion/docs).
  * Learn more about [SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud).
  * Learn more about [BigQuery](https://docs.cloud.google.com/bigquery).
  * Learn more about [Looker Blocks](https://docs.cloud.google.com/looker).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
