---
url: https://docs.cloud.google.com/cortex/docs/source-system-integration/sap-bdc/
title: Integrate and synchronize SAP Business Data Cloud data products with Cortex Framework using Lakehouse runtime catalog. \u00a0|\u00a0 Google Cloud Cortex Framework \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:23:52.979338+00:00
---

# Integrate and synchronize SAP Business Data Cloud data products with Cortex Framework using Lakehouse runtime catalog.  |  Google Cloud Cortex Framework  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cortex/docs/source-system-integration/sap-bdc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Google Cloud Cortex Framework ](https://docs.cloud.google.com/cortex/docs)
  * [ Version 7 Guides ](https://docs.cloud.google.com/cortex/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate and synchronize SAP Business Data Cloud data products with Cortex Framework using Lakehouse runtime catalog.

This document describes how to connect Cortex Framework to **SAP Business Data Cloud** using the Lakehouse runtime catalog integration.

By combining Google Cloud SAP Delta Sharing with the BigQuery Lakehouse runtime catalog federation connection, Cortex Framework can query any data products managed inside SAP BDC directly in BigQuery with zero copy overhead, and reference them in custom downstream analytical data products. The key components of this integration are:

  1. **Federated Querying** : Data products published in SAP BDC are exposed using secure Delta Sharing endpoints. BigQuery federates queries to these endpoints using the Google Cloud Lakehouse runtime catalog connection.
  2. **Catalog Registration** : In Cortex Framework you register the SAP BDC catalog using a module of type `delta_share` under `data.modules.catalogs` in `config/config.yaml`.
  3. **Google Cloud Cortex Framework data products bindings** : Downstream custom data products reference BDC catalog tables by binding their input dependencies to the specific Delta Sharing share and table IDs in the format `{catalog_id}.{share_id}.{table_name}`.



## Prerequisites for SAP BDC

Before configuring the connection in Cortex Framework you must complete the following steps in Google Cloud and SAP:

  * **Configure Google Cloud Lakehouse runtime catalog** : Set up the BigQuery Lakehouse runtime catalog connection in your Google Cloud Project leveraging Google Cloud [Delta Sharing](https://docs.cloud.google.com/lakehouse/docs/set-up-cross-cloud-lakehouse-sap-bdc) for SAP Business Data Cloud.
  * **Retrieve Share IDs** : [Locate and list the Delta Sharing `shareId` values](https://docs.cloud.google.com/lakehouse/docs/query-sap-data) (for example, `customer_v1_he2_100_p8123` or `salesorder_v1_he2_100_p8124`) published by the connected SAP BDC tenant.



## Configuration example

The following example configuration registers an SAP BDC catalog and uses its shares to compute a custom sales performance data product:
    
    
    buildEnvironment:
      buildProjectId: YOUR_BUILD_PROJECT_ID
    
    data:
      bigQueryLocation: europe-west3
      namespaces:
        - name: cortex
          path: ../src/data_modules/cortex
        - name: cortex_samples
          path: ../src/data_modules/cortex_samples
      datasets:
        - id: sap_bdc_data_products
          projectId: YOUR_TARGET_PROJECT_ID
          datasetId: sap_bdc_data_products
    
      modules:
        # 1. Register the SAP BDC Lakehouse runtime catalog connection (using lakehouse_delta_share type)
        catalogs:
          - id: sap_bdc_catalog
            type: lakehouse_delta_share
            enabled: true
            bindsNamespaces: [sap_bdc]
            connectionSettings:
              catalogId: sap_bdc_catalog
              projectId: YOUR_CATALOG_PROJECT_ID
              location: europe-west3
              shares:
                - shareId: customer_v1_he2_100_p8123
                - shareId: salesorder_v1_he2_100_p8124
    
        # 2. Reference the catalog shares in downstream products
        products:
          - moduleId: sap_bdc_sales_performance
            modulePath: cortex_samples.sap_bdc.products.sales_performance
            dependencyBindings:
              # Bind logical dependencies directly to the catalog shares and tables
              sapBdcCustomer: sap_bdc_catalog.customer_v1_he2_100_p8123.customer
              sapBdcSalesOrder: sap_bdc_catalog.salesorder_v1_he2_100_p8124.salesorder
            dataTargetId: sap_bdc_data_products
    

For parameter reference, refer to [Deployment configuration](https://docs.cloud.google.com/cortex/docs/deployment-configuration#data_modules_catalogs) section for data catalog module type.

When a custom data product relies on Lakehouse runtime catalog tables, configure its input dependencies in `config/config.yaml` using the catalog path syntax:

`dependencyBindings:` `{logical_input_name}: {catalog_id}.{share_id}.{table_name}`

Where:

  * `{catalog_id}` matches the catalog `id` property under `data.modules.catalogs`.
  * `{share_id}` matches one of the declared catalog `shareId` strings.
  * `{table_name}` matches the physical table name exposed inside that share.



## Downstream Dataform dependency binding

During compilation (`cortex-build`) Cortex Framework reads the catalog metadata and automatically translates the dependency bindings into fully qualified BigQuery federated table names.

In your custom data product definitions (for example, `.js` or `.sqlx` files) reference the conformed SAP BDC sources:
    
    
    // Example JS definition referencing SAP BDC inputs
    const moduleConfig = config.product[moduleContext.moduleId];
    const customerSource = moduleConfig.sources.sapBdcCustomer;
    const salesOrderSource = moduleConfig.sources.sapBdcSalesOrder;
    
    publish("custom_sales_performance", {
      type: "table",
    }).query(
      (ctx) => `
        SELECT
          cust.customer_id,
          orders.sales_order_id,
          orders.amount
        FROM ${ctx.ref(customerSource.datasetId, customerSource.tableName)} AS cust
        JOIN ${ctx.ref(salesOrderSource.datasetId, salesOrderSource.tableName)} AS orders
          ON cust.customer_id = orders.customer_id
      `
    );
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
