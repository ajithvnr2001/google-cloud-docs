---
url: https://docs.cloud.google.com/cortex/docs/extensibility-guide-data-product/
title: Data product module creation \u00a0|\u00a0 Google Cloud Cortex Framework \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:36:57.712144+00:00
---

# Data product module creation  |  Google Cloud Cortex Framework  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cortex/docs/extensibility-guide-data-product/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Google Cloud Cortex Framework ](https://docs.cloud.google.com/cortex/docs)
  * [ Version 7 Guides ](https://docs.cloud.google.com/cortex/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Data product module creation

To define your own business logic and analytical models, create a custom [data product](https://docs.cloud.google.com/cortex/docs/data-product) module. This lets you run calculations on your foundation tables or upstream data products and package the results into deployable datasets.

**Note:** You can follow the manual configuration instructions, or use pre-packaged AI skills to autonomously scaffold and verify your modules. For details on AI-assisted workflows, see [Agentic creation of data products](https://docs.cloud.google.com/cortex/docs/extensibility-guide-agentic-data-product-creation).

## Prerequisites

We recommend creating custom data product modules in a dedicated [custom namespace](https://docs.cloud.google.com/cortex/docs/extensibility-guide-namespaces) for better lifecycle management. Also, ensure the source table you plan to use exists in the [data foundation](https://docs.cloud.google.com/cortex/docs/extensibility-guide-data-foundation) dataset.

## Creation of a data product module

Data product module definition requires these steps:

  * Registration of the data product module within the `config/config.yaml` file, by extending the `data.modules.products` list with entry:


    
    
    data:
      # Configuration for data foundation and product modules.
      modules:
        # List of data product modules.
        products:
            # Recommended naming for product_module_id:
            # custom_namespace_product_name
          - moduleId:  product_module_id
            # Path of the data product (namespaced).
            modulePath:  custom_namespace.system_type.products.product_name
            # Map of module dependencies.
            dependencyBindings:
              sapModule: erp
              sapModuleCustNS:  foundation_module_id
            # Reference to the target dataset ID.
            dataTargetId: product_target
            # Whether the module is enabled.
            # enabled: true
            # Whether the foundation is external (does not create target dataset).
            # external: false
            # Custom table settings file, relative to 'config/' file directory
            # Recommended path: '{custom_namespace}/{system_type}/products/{product_name}/table_settings.yaml'
            # If omitted, defaults to '../src/data_modules/{custom_namespace}/{system_type}/products/{product_name}/table_settings.default.yaml'
            # tableSettings: "{custom_namespace}/{system_type}/products/{product_name}/table_settings.yaml"
            
    

  * Creation of default [`tableSettings` file](https://docs.cloud.google.com/cortex/docs/deployment-configuration#config-table-settings-yaml) (e.g. `src/data_modules/custom_namespace/system_type/products/product_name/table_settings.default.yaml`). 



This YAML controls [table configurations](https://docs.cloud.google.com/cortex/docs/deployment-configuration#config-table-settings-yaml) like materializations and BigQuery optimization details:
    
    
    common:
      custom_sales_summary:
        materializationType: "table"
        bigQueryLabels:
          - key: data_class
            value: transactional
        dataformTags: ["custom", "sales", "reporting"]
        partitionDetails:
          column: "created_date"
          partitionType: "date"
          timeGrain: "day"
        clusterDetails:
          columns:
            - "customer_id"
    

  * Creation of annotation file



The annotation file `tablename.yaml` is created for each data product output artifacts (table, view) and describes columns and fields in YAML format. During compilation, the builder automatically searches for annotations within the product's `annotations/` folder (e.g. `src/data_modules/custom_namespace/system_type/products/product_name/annotations/custom_sales_summary.yaml`), merges these strings directly into the output Dataform schema definitions so they are preserved in BigQuery table metadata.

An annotation `src/data_modules/custom_namespace/system_type/products/product_name/annotations/tablename.yaml` file has the format:
    
    
    description: "Description of the table or view purpose"
    fields:
      - name: "customer_id"                     # column name
        description: "Customer identifier"      # column description
      - name: "column2"
        description: "Description of Column 2"
      - name: "column3"
        description: "Description of Column 3"
    

  * Create a `manifest.yaml` file in your data product folder `src/data_modules/custom_namespace/system_type/products/product_name/`, maintaining the type, category, tables and module dependencies. The manifest file follows this format:


    
    
    displayName: Sales Performance Summary
    description: Sales performance analytical data product.
    category: product
    type: generic
    builder: sap_product     # Automatically resolves to the global SapProductBuilder fallback
    dependencies:
      sapModule:
        modulePath: cortex.sap.foundations.sap
        supportedVersions:
          - ecc
          - s4
    

## Data product module example

The steps to implement the `flights_usd` data product in the namespace: `sap_bookingdatamodel` of the [flights example](https://docs.cloud.google.com/cortex/docs/extensibility-guide#example_scenario) are:

  * Registration of the data product module within the `config/config.yaml` file, by extending the `data.modules.products` list with entry:


    
    
    data:
      modules:
        products:
          - moduleId: sap_bookingdatamodel_flights_usd
            modulePath: sap_bookingdatamodel.sap.products.flights_usd
            dependencyBindings:
              sapModule: erp
              sapModuleCustNS: sap_bookingdatamodel
            dataTargetId: product_target
    

  * As next, create `src/data_modules/sap_bookingdatamodel/sap/products/flights_usd/manifest.yaml` with the content


    
    
    displayName: Flights USD
    description: Flight scheduling and pricing USD data product.
    category: product
    type: generic
    dependencies:
      sapModule:
        modulePath: cortex.sap.foundations.sap
        supportedVersions:
          - ecc
          - s4
        tables:
          common:
            - tcurr
      sapModuleCustNS:
        # Type of the dependent Module.
        # use cortex.sap.foundations.sap if you followed "Configure multiple instances of a data foundation module"
        # https://docs.cloud.google.com/cortex/docs/deployment-configuration#multiple-data-foundation-instances
        modulePath: cortex.sap.foundations.sap
        # use sap_bookingdatamodel.sap.foundations.sap if you are connecting to custom-data foundation module:
        # https://docs.cloud.google.com/cortex/docs/extensibility-guide-data-foundation
        #modulePath: sap_bookingdatamodel.sap.foundations.sap
        supportedVersions:
          - ecc
          - s4
        tables:
          common:
            - sflight
    builder: sap_product
    

  * In the next step, create the referenced [table settings](https://docs.cloud.google.com/cortex/docs/deployment-configuration#config-table-settings-yaml) file to configure the schema and metadata of the output tables or views in BigQuery.



In the used example, create: `src/data_modules/sap_bookingdatamodel/sap/products/flights_usd/table_settings.default.yaml` with the content:
    
    
    ecc:
      flights_usd:
        materializationType: incremental
        bigQueryLabels:
          - key: data_class
            value: transactional
        dataformTags: [sap, dataproduct, masterdata]
    s4:
      flights_usd:
        materializationType: incremental
        bigQueryLabels:
          - key: data_class
            value: transactional
        dataformTags: [sap, dataproduct, masterdata]
    
    

  * Create annotations for data product tables to enrich the storage schema with descriptions.



In the used example, create file: `src/data_modules/sap_bookingdatamodel/sap/products/flights_usd/annotations/flights_usd.yaml` with the content:
    
    
    description: "Flight scheduling and pricing information, including currency conversion to USD."
    fields:
      - name: "client_mandt"
        description: "Client (Mandant), PK"
      - name: "airline_code_carrid"
        description: "Airline Carrier ID, PK"
      - name: "flight_connection_number_connid"
        description: "Flight Number, PK"
      - name: "flight_date_fldate"
        description: "Flight Date"
      - name: "price_usd"
        description: "Price in USD"
      - name: "price"
        description: "Price in local currency"
      - name: "currency"
        description: "Local currency"
    

  * The business logic of the data product is stored in `js` or `sqlx` files.

**Note:** For data products with differences in logic for different dialects (e.g., SAP ECC and S/4HANA), use subfolders `ecc` and `s4` of the `definitions` folder.**Note:** Files created inside the local module's `definitions/` folder are compiled by `cortex-build` and synced into the remote Dataform workspace during deployment. If you need to add custom code directly inside the remote Dataform workspace using the Google Cloud console without creating a module in source control, place your files inside `definitions/custom/` in the Dataform remote repository. Any unmanaged files in Dataform remote repository outside of `definitions/custom/` will be overwritten or deleted on the next deployment run (`cortex-deploy`).

In given example create `src/data_modules/sap_bookingdatamodel/sap/products/flights_usd/definitions/flights_usd.js` file with the content:
    
    
    // ___MODULE_CONTEXT___
    // ___TABLE_CONFIG___
    
    const moduleConfig = config.product[moduleContext.moduleId];
    const sapModuleConfigDatasetId = moduleConfig.sources.sapModule.datasetId;
    const sapModuleCustNSConfigDatasetId = moduleConfig.sources.sapModuleCustNS.datasetId;
    
    const materializationType = tableConfig.materializationType || "incremental";
    
    const incremental = require("includes/cortex/incremental.js");
    const publish_config = require("includes/cortex/publish_config.js");
    
    const publishConfig = publish_config.getPublishConfig(
       materializationType,
       tableConfig,
       moduleConfig,
       [
           "client_mandt",
           "airline_code_carrid",
           "flight_connection_number_connid",
           "flight_date_fldate"
       ]
    );
    
    publish("flight_usd", publishConfig).query(
       (ctx) => `
    WITH flight_base AS (
       SELECT
           mandt,
           carrid,
           connid,
           fldate,
           price,
           currency,
           -- Convert flight date string (YYYYMMDD) to an integer to calculate SAP's inverted date key
           CAST(99999999 - CAST(fldate AS INT64) AS STRING) AS inverted_fldate
       FROM   ${ctx.ref(sapModuleCustNSConfigDatasetId, 'sflight')} AS flight
    ),
    ranked_exchange_rates AS (
       SELECT
           f.mandt,
           f.carrid,
           f.connid,
           f.fldate,
           f.price,
           f.currency,
           t.ukurs,
           -- Window function to grab the closest historical exchange rate
           ROW_NUMBER() OVER (
               PARTITION BY f.mandt, f.carrid, f.connid, f.fldate
               ORDER BY t.gdatu ASC
           ) AS latest_rate_rank
       FROM flight_base f
       LEFT JOIN ${ctx.ref(sapModuleConfigDatasetId, 'tcurr')} AS t
         ON f.mandt = t.mandt
        AND t.kurst = 'M'       -- 'M' is the standard SAP default for average exchange rates
        AND t.fcurr = f.currency
        AND t.tcurr = 'USD'
        -- Chronological (rate_date <= flight_date) translates to (t.gdatu >= inverted_fldate)
        AND t.gdatu >= f.inverted_fldate
    )
    
    SELECT
       client_mandt,
       airline_code_carrid,
       flight_connection_number_connid,
       flight_date_fldate,
       price,
       currency,
       price_usd,
       CURRENT_TIMESTAMP() AS bq_loaded_at
    FROM (
      SELECT
        mandt              AS client_mandt,
        carrid             AS airline_code_carrid,
        connid             AS flight_connection_number_connid,
        PARSE_TIMESTAMP('%Y%m%d', fldate) AS flight_date_fldate,
        price              AS price,
        currency           AS currency,
        -- Currency Conversion Logic
        CASE
           WHEN currency = 'USD' THEN price
           WHEN ukurs IS NULL   THEN NULL -- Handles cases where no exchange rate is found
           -- If UKURS is negative, it's an indirect quotation (1 USD = X Local) -> Divide
           WHEN ukurs < 0       THEN ROUND(price / ABS(ukurs), 2)
           -- If UKURS is positive, it's a direct quotation (1 Local = X USD) -> Multiply
           ELSE ROUND(price * ukurs, 2)
         END AS price_usd
      FROM ranked_exchange_rates
      WHERE latest_rate_rank = 1
    )
    ${incremental.getWhere(ctx, ["flight_date_fldate"])}
    `
    );
    
    

## Verification of custom namespace extension

To verify the successful creation of Google Cloud Cortex Framework data product modules, follow these steps:

  * Execute [Cortex Framework deployment](https://docs.cloud.google.com/cortex/docs/deployment#execute_deployment) referencing the updated `config.yaml` file. 
  * Follow the [Post deployment steps](https://docs.cloud.google.com/cortex/docs/post-deployment-steps) to execute the Dataform actions and verify the results in BigQuery



* * *

  * Previous step: [Data foundation module creation](https://docs.cloud.google.com/cortex/docs/extensibility-guide-data-foundation)
  * Next step: [Post deployment steps](https://docs.cloud.google.com/cortex/docs/post-deployment-steps)
  * Back to [Overview](https://docs.cloud.google.com/cortex/docs/extensibility-guide)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
