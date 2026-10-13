---
url: https://docs.cloud.google.com/cortex/docs/solution-samples/supplier-spend-analysis/
title: Supplier Spend Analysis \u00a0|\u00a0 Google Cloud Cortex Framework \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:48:02.764757+00:00
---

# Supplier Spend Analysis  |  Google Cloud Cortex Framework  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cortex/docs/solution-samples/supplier-spend-analysis/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Google Cloud Cortex Framework ](https://docs.cloud.google.com/cortex/docs)
  * [ Version 7 Guides ](https://docs.cloud.google.com/cortex/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Supplier Spend Analysis

This consumption data product sample provides an example on how to accelerate insights into supplier spend position using SAP ERP or SAP BDC sourced data.

With it you can:

  * Optimize total spend by material type and track country concentration.
  * Understand hidden purchasing patterns to maximize procurement value.
  * Use AI to uncover new insights.



## Reference architecture

A high level reference architecture provides an overview of the source specific data products required to feed this use case.

[ ![Consumption data product sample reference
architecture for Cortex Framework](https://docs.cloud.google.com/static/cortex/docs/images/supplier_spend_analysis.png)](https://docs.cloud.google.com/static/cortex/docs/images/supplier_spend_analysis.png)

**Figure 1**. Supplier Spend Analysis consumption data product sample reference architecture for Cortex Framework.

## Required data products

If building on top of SAP ERP sourced data the following [Cortex Framework data products](https://docs.cloud.google.com/cortex/docs/data-product#data_source_specific_data_products_for_sap_erp) are required:

  * Vendors
  * Purchasing Documents
  * Purchasing Organizational Structure
  * Materials



If building on top of SAP BDC sourced data the following [BDC data products](https://api.sap.com/dataproducts) are required:

  * Purchase Order (tables: `purchaseorder`, `purchaseorderitem`, and `purchaseorderscheduleline`)
  * Supplier
  * Purchasing Organization
  * Procurement Configuration Data



## Enable data product in Google Cloud Google Cloud Cortex Framework

To deploy the Supplier Spend Analysis data product, you must enable it in your `config/config.yaml` file by registering the data product module under `data.modules.products`.

For detailed information on configuring `config/config.yaml`, see the [Deployment](https://docs.cloud.google.com/cortex/docs/deployment) and [Deployment configuration](https://docs.cloud.google.com/cortex/docs/deployment-configuration) documentation.

### SAP ERP Sourced Data Product

To enable the SAP ERP conformed data product, add the following configuration under the `products:` section, ensuring all dependent foundation data products are also configured and enabled:
    
    
    data:
      modules:
        products:
          # Enabled Supplier Spend Analysis sample (SAP ERP version)
          - moduleId: sap_supplier_spend_analysis_sample
            modulePath: cortex_samples.sap.products.supplier_spend_analysis
            enabled: true # If using configuration file based on config.yaml.example, please the `enabled` flag is set to `true`
            dataTargetId: product_target
            dependencyBindings:
              sapMaterials: sap_materials
              sapPurchasingDocuments: sap_purchasing_documents
              sapPurchasingOrganizationalStructure: sap_purchasing_organizational_structure
              sapVendors: sap_vendors
    

### SAP BDC Sourced Data Product

To enable the SAP BDC conformed data product, ensure that your external data catalog is registered under `data.modules.catalogs`, and add the following configuration:
    
    
    data:
      modules:
        products:
          # Enabled Supplier Spend Analysis sample (SAP BDC version)
          - moduleId: sap_bdc_supplier_spend_analysis_sample
            modulePath: cortex_samples.sap_bdc.products.supplier_spend_analysis
            enabled: true # If using configuration file based on config.yaml.example, please the `enabled` flag is set to `true`
            dataTargetId: product_target
            dependencyBindings:
              sapBdcSupplier: sap_bdc_catalog
              sapBdcProcurementConfigurationData: sap_bdc_catalog
              sapBdcPurchasingOrganization: sap_bdc_catalog
              sapBdcPurchaseOrder: sap_bdc_catalog
    

## Entity Relationship Diagrams

The following Entity Relationship (ER) diagrams outline the structure of the data product views and their relationships with source and associated foundation tables.

### SAP ERP Supplier Spend Analysis ER Diagram

[ ![SAP ERP Supplier Spend Analysis ER Diagram](https://docs.cloud.google.com/static/cortex/docs/images/supplier_spend_analysis_er.png)](https://docs.cloud.google.com/static/cortex/docs/images/supplier_spend_analysis_er.png)

**Figure 2**. Supplier Spend Analysis conformed data product SAP ERP ER diagram for Cortex Framework.

### SAP BDC Supplier Spend Analysis ER Diagram

[ ![SAP BDC Supplier Spend Analysis ER Diagram](https://docs.cloud.google.com/static/cortex/docs/images/supplier_spend_analysis_bdc_er.png)](https://docs.cloud.google.com/static/cortex/docs/images/supplier_spend_analysis_bdc_er.png)

**Figure 3**. Supplier Spend Analysis conformed data product SAP BDC ER diagram for Cortex Framework.

## Source code

The source code for this Sales Performance consumption data product sample, can be found in the repository:

  * [SAP ERP](https://github.com/GoogleCloudPlatform/cortex-framework/tree/main/src/data_modules/cortex_samples/sap/products/supplier_spend_analysis) or in your local source code using the path `src/data_modules/cortex_samples/sap/products/supplier_spend_analysis`
  * [SAP BDC](https://github.com/GoogleCloudPlatform/cortex-framework/tree/main/src/data_modules/cortex_samples/sap_bdc/products/supplier_spend_analysis) or in your local source code using the path `src/data_modules/cortex_samples/sap_bdc/products/supplier_spend_analysis`



## Enable AI agents

After creating your Sales Performance Insights data model in BigQuery, you may be interested in [building a custom data agent](https://docs.cloud.google.com/bigquery/docs/create-data-agents). This lets you query sales trends and performance metrics directly using natural language, bypassing the need for complex SQL.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
