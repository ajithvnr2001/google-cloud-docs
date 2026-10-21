---
url: https://docs.cloud.google.com/cortex/docs/solution-samples/sales-performance-insights/
title: Sales Performance Insights \u00a0|\u00a0 Google Cloud Cortex Framework \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:36:58.980633+00:00
---

# Sales Performance Insights  |  Google Cloud Cortex Framework  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cortex/docs/solution-samples/sales-performance-insights/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Google Cloud Cortex Framework ](https://docs.cloud.google.com/cortex/docs)
  * [ Version 7 Guides ](https://docs.cloud.google.com/cortex/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Sales Performance Insights

This consumption data product sample provides an example on how to accelerate insights into sales performance health using SAP ERP or SAP BDC sourced data.

With it you can:

  * Optimize revenue by product, region, and sales organization.
  * Track performance across distribution channels and divisions.
  * Use AI to uncover fulfillment bottlenecks or on-time delivery trends that impact revenue and costs.



## Reference architecture

A high level reference architecture provides an overview of the source specific data products required to feed this use case.

[ ![Sales Performance Insights consumption data product sample reference architecture for Cortex Framework](https://docs.cloud.google.com/static/cortex/docs/images/sales_performance_solution_sample.png)](https://docs.cloud.google.com/static/cortex/docs/images/sales_performance_solution_sample.png)

**Figure 1**. Sales Performance Insights consumption data product sample reference architecture for Cortex Framework.

## Required data products

If building on top of SAP ERP sourced data the following [Cortex Framework data products](https://docs.cloud.google.com/cortex/docs/data-product#data_source_specific_data_products_for_sap_erp) are required:

  * Customers
  * Delivery Documents
  * Sales Documents
  * Sales Organizational Structure
  * Materials



If building on top of SAP BDC sourced data the following [BDC data products](https://api.sap.com/dataproducts) are required:

  * Customer
  * Sales Order



## Enable data product in Google Cloud Google Cloud Cortex Framework

To deploy the Sales Performance Insights data product, you must enable it in your `config/config.yaml` file by registering the data product module under `data.modules.products`.

For detailed information on configuring `config/config.yaml`, see the [Deployment](https://docs.cloud.google.com/cortex/docs/deployment) and [Deployment configuration](https://docs.cloud.google.com/cortex/docs/deployment-configuration) documentation.

### SAP ERP Sourced Data Product

To enable the SAP ERP conformed data product, add the following configuration under the `products:` section, ensuring all dependent foundation data products are also configured and enabled:
    
    
    data:
      modules:
        products:
          # Enabled Sales Performance sample (SAP ERP version)
          - moduleId: sap_sales_performance_sample
            modulePath: cortex_samples.sap.products.sales_performance
            enabled: true # If using configuration file based on config.yaml.example, please the `enabled` flag is set to `true`
            dataTargetId: product_target
            dependencyBindings:
              sapCustomers: sap_customers
              sapSalesDocuments: sap_sales_documents
              sapDeliveryDocuments: sap_delivery_documents
              sapSalesOrganizationalStructure: sap_sales_organizational_structure
              sapMaterials: sap_materials
    

### SAP BDC Sourced Data Product

To enable the SAP BDC conformed data product, ensure that your external data catalog module is registered under `data.modules.catalogs` as described in the [data catatalog documentation](https://docs.cloud.google.com/cortex/docs/data-catalog), and add the following configuration:
    
    
    data:
      modules:
        products:
          # Enabled Sales Performance sample (SAP BDC version)
          - moduleId: sap_bdc_sales_performance_sample
            modulePath: cortex_samples.sap_bdc.products.sales_performance
            enabled: true # If using configuration file based on config.yaml.example, please the `enabled` flag is set to `true`
            dataTargetId: product_target
            dependencyBindings:
              sapBdcCustomer: sap_bdc_catalog
              sapBdcSalesOrder: sap_bdc_catalog
    

## Entity Relationship Diagrams

The following Entity Relationship (ER) diagrams outline the structure of the data product views and their relationships with source and associated foundation tables.

### SAP ERP Sales Performance ER Diagram

[ ![SAP ERP Sales Performance ER Diagram](https://docs.cloud.google.com/static/cortex/docs/images/sales_performance_er.png)](https://docs.cloud.google.com/static/cortex/docs/images/sales_performance_er.png)

**Figure 2**. Sales Performance Insights consumption data product SAP ERP ER diagram for Cortex Framework.

### SAP BDC Sales Performance ER Diagram

[ ![SAP BDC Sales Performance ER Diagram](https://docs.cloud.google.com/static/cortex/docs/images/sales_performance_bdc_er.png)](https://docs.cloud.google.com/static/cortex/docs/images/sales_performance_bdc_er.png)

**Figure 3**. Sales Performance Insights consumption data product SAP BDC ER diagram for Cortex Framework.

## Source code

The source code for this Sales Performance consumption data product sample, can be found in the repository:

  * [SAP ERP](https://github.com/GoogleCloudPlatform/cortex-framework/tree/main/src/data_modules/cortex_samples/sap/products/sales_performance) or in your local source code using the path `src/data_modules/cortex_samples/sap/products/sales_performance`
  * [SAP BDC](https://github.com/GoogleCloudPlatform/cortex-framework/tree/main/src/data_modules/cortex_samples/sap_bdc/products/sales_performance) or in your local source code using the path `src/data_modules/cortex_samples/sap_bdc/products/sales_performance`



## Enable AI agents

After creating your Sales Performance Insights data model in BigQuery, you may be interested in [building a custom data agent](https://docs.cloud.google.com/bigquery/docs/create-data-agents). This lets you query sales trends and performance metrics directly using natural language, bypassing the need for complex SQL.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
