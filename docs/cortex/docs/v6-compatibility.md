---
url: https://docs.cloud.google.com/cortex/docs/v6-compatibility/
title: Cortex Framework v6 compatibility \u00a0|\u00a0 Google Cloud Cortex Framework \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:23:27.196642+00:00
---

# Cortex Framework v6 compatibility  |  Google Cloud Cortex Framework  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cortex/docs/v6-compatibility/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Google Cloud Cortex Framework ](https://docs.cloud.google.com/cortex/docs)
  * [ Version 7 Guides ](https://docs.cloud.google.com/cortex/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Cortex Framework v6 compatibility

The v6 compatibility content provides a schema-compatible layer for Cortex Framework v6 workloads within the Cortex Framework v7 architecture. This lets you migrate to Cortex Framework v7 without breaking existing analytics assets, such as Looker dashboards or LookML semantic models.

## Supported data sources

The framework provides v6 compatibility content for SAP ECC and SAP S/4HANA data sources.

## How it works

The v6 compatibility content acts as an adapter between the v7 data models and your legacy reporting assets:

  * **Schema-compatible views** : Expose reporting view names, columns, and casing exactly as they appeared in Cortex Framework (v6).
  * **Target isolation** : Isolates compatibility views from the core Cortex Framework tables by deploying them within a separate namespace (`cortex_v6_compatibility`) and a dedicated BigQuery target dataset.



## Deploy the compatibility content

To deploy the Cortex Framework v6 compatibility content, complete the following steps:

  * Configure a dedicated BigQuery target dataset.
  * Enable the v6 compatibility modules in the `config.yaml` file.
  * Run the Google Cloud Cortex Framework build and deployment scripts.
  * Execute the Dataform pipelines.



### Dedicated target dataset

You must deploy the v6 compatibility content to a separate BigQuery dataset. This prevents namespace shadowing and physical table collisions, because many tables used by the compatibility content share identical physical names (such as `cost_centers`, `profit_centers`, `billing`, and `deliveries`) with the Cortex Framework v7 core tables.

To create the dedicated BigQuery dataset, add the `cortex_v6_compatibility_target` to you `config.yaml` file:
    
    
    data:
      datasets:
        - id: product_target
          projectId: YOUR_TARGET_PROJECT_ID
          datasetId: prod_sap_dataproducts # Core v7 tables
        - id: cortex_v6_compatibility_target
          projectId: YOUR_TARGET_PROJECT_ID
          datasetId: prod_sap_cortex6 # Compatibility v6 tables
    

### Configure Cortex Framework

To register and activate the compatibility layer in your `config.yaml` file, you must complete the following tasks:

  * Set up the dedicated target dataset.
  * Register the compatibility namespace.
  * Set the enabled attribute to `true` for all of the following Cortex Framework v6 compatibility modules:

  * `sap_cortex_v6_compatibility_master_data`

  * `sap_cortex_v6_compatibility_accounts_payable`

  * `sap_cortex_v6_compatibility_finance`

  * `sap_cortex_v6_compatibility_inventory`

  * `sap_cortex_v6_compatibility_purchasing`

  * `sap_cortex_v6_compatibility_sales`




The following example demonstrates the configuration changes necessary to enable the `sap_cortex_v6_compatibility_inventory`:
    
    
    data:
      datasets:
        - id: cortex_v6_compatibility_target
          projectId: YOUR_TARGET_PROJECT_ID
          datasetId: prod_sap_cortex6
    
      namespaces:
        - name: cortex_v6_compatibility
          path: ../src/data_modules/cortex_v6_compatibility
    
      modules:
        products:
          - moduleId: sap_cortex_v6_compatibility_inventory
            modulePath: cortex_v6_compatibility.sap.products.inventory
            enabled: true # If using configuration file based on config.yaml.example, ensure the `enabled` flag is set to `true`
            syncToKc: false
            dependencyBindings:
              sapModule: erp
              sapMasterData: sap_cortex_v6_compatibility_master_data
              sapSales: sap_cortex_v6_compatibility_sales
            dataTargetId: cortex_v6_compatibility_target
            moduleSettings:
              targetCurrencies: ['USD']
              rateType: 'M'
              languages: ['E']
    
    #    You must ensure the `enabled` flag is set to `true` for all of the listed dependent modules. In this example:
    #   `sap_cortex_v6_compatibility_master_data`
    #   `sap_cortex_v6_compatibility_sales`
    
    

### Operational requirements

We strongly recommend enabling all Cortex Framework v6 compatibility modules at the same time. The compatibility content contains cross-module dependencies (for example, billing views depend on master data tables, and inventory snapshotting views depend on calendar dimensions). Enabling them together prevents dependency errors in Dataform.

Inventory snapshots

You must configure and execute the inventory snapshot tables (`stock_weekly_snapshots` and `stock_monthly_snapshots`) as incremental tables. In Cortex Framework v6, inventory snapshots calculate a running cumulative total of stock quantities and values:

  1. **Initial Run** : The tables process the entire history of movement transactions to establish the starting stock levels.
  2. **Subsequent Runs** : Dataform processes only the movements posted since the last snapshot execution, adding them to the previous period's cumulative totals.



If you run these tables in full-refresh (non-incremental) mode, they recalculate the entire movement history from scratch on every run. This approach is highly inefficient, expensive, and can cause incorrect cumulative calculations if the source tables contain date gaps. Keep the materialization type for these tables set to incremental (the default configuration).

### Build and deploy the compatibility content

To build and deploy the compatibility content, follow the instructions in the [Deployment](https://docs.cloud.google.com/cortex/docs/deployment) and [Post-deployment](https://docs.cloud.google.com/cortex/docs/post-deployment-steps) documentation.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
