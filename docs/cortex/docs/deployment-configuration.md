---
url: https://docs.cloud.google.com/cortex/docs/deployment-configuration/
title: Deployment configuration \u00a0|\u00a0 Google Cloud Cortex Framework \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:22:21.281444+00:00
---

# Deployment configuration  |  Google Cloud Cortex Framework  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cortex/docs/deployment-configuration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Google Cloud Cortex Framework ](https://docs.cloud.google.com/cortex/docs)
  * [ Version 7 Guides ](https://docs.cloud.google.com/cortex/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Deployment configuration

This page explains the deployment configuration options for Cortex Framework across the following areas:

  * **Deployment configurations (`config/config.yaml`)**: Defines global variables, build environments, and module mapping (data foundation and data product targets).
  * **Table configurations (`table_settings.yaml`)**: Module-specific performance and schema specifications, outlining how base tables are compiled and conformed in BigQuery.



This page also provides **How-to guides** with step-by-step instructions for common deployment use cases and scenarios.

## Configuration file: `config/config.yaml`

The `config/config.yaml` file — typically initialized from the `config/config.yaml.example` template — serves as the primary configuration for the Cortex Framework deployment. The configuration is divided into these structural blocks:

  1. **Build environment (`buildEnvironment`)**: Governs the build orchestration layer, specifying the central Google Cloud project where intermediate metadata calculations, database validations, and schema lookups are billed and executed.
  2. **Data (`data`)**: Governs the logical data architecture. This block configures dataset locations, namespace boundaries, connection details for raw ingestion sources, destination datasets, and registers the data module instances (`foundations`, `catalogs`, and `products`).
  3. **Deployment (`deployment`)**: Configures physical target system deployments. It specifies the Dataform repository details (project ID, location, repository name, and development workspace) where compiled SQLX/JS transformation pipelines are deployed.



The following sections provide a detailed breakdown of each block.

### Build environment

The build environment project is the project that gets billed for build actions, such as BigQuery jobs reading `DD03L`.
    
    
    buildEnvironment:
      buildProjectId: YOUR_BUILD_PROJECT_ID
    

The following table describes the build environment parameters.

Parameter | Meaning | Default value | Description  
---|---|---|---  
`buildEnvironment.buildProjectId` | Build project ID | `YOUR_BUILD_PROJECT_ID` | Google Cloud Project ID where build operations are executed.  
  
### Data section overview

The `data:` section of the configuration file defines your data sources, targets, and the specific modules for the data foundation and data products. Its general structure is as follows:
    
    
    data:
       # Geographic location for BigQuery datasets (for example: US, EU, us-central1)
       # For full list see: https://docs.cloud.google.com/cortex/docs/supported-locations
      bigQueryLocation: US
      # List of namespaces for data foundation and product modules.
      namespaces:
        - name: cortex
          path: ../src/data_modules/cortex
      # List of datasets mapping.
      datasets:
        - ...
    
      # Configuration for data foundation, data product, and external catalog modules.
      modules:
        # List of foundation modules.
        foundations:
        - ... 
        # List of external catalog modules.
        catalogs:
        - ...
        # List of data product modules.
        products:
        - ...
    

### Data: BigQuery location

Defines the location of the BigQuery source and target datasets.

Parameter | Meaning | Default value | Description  
---|---|---|---  
`data.bigQueryLocation` | BigQuery Location | `US` | BigQuery dataset location (for example, `US`, `us-central1`, or `europe-west1`).   
  
### Data: Cortex namespace

Defines Cortex Framework namespace.

Parameter | Meaning | Default value | Description  
---|---|---|---  
`data.namespaces.name` | Namespace name | - | Cortex Framework namespace name. For example, `cortex`.  
`data.namespaces.path` | Namespace path | - | Cortex Framework namespace path for subdirectories used within src and config folder. For example, `cortex`.  
  
### Data: BigQuery sources and target datasets

The list of datasets defines the inbound raw data connection points and outbound storage locations for the framework. Each dataset registers a unique identifier mapped to a specific Google Cloud project and BigQuery dataset.

Datasets are referenced from the modules using their unique ID.
    
    
    # Dataset mapping
    datasets:
      - id: sap_raw
        projectId: YOUR_SOURCE_PROJECT_ID
        datasetId: cortex_sap_raw
      - id: sap_foundation
        projectId: YOUR_TARGET_PROJECT_ID
        datasetId: cortex7_sap_data_foundation
    

The following table describes the dataset mapping parameters.

Parameter | Meaning | Default value | Description  
---|---|---|---  
`data.datasets.id` | Dataset ID | `-` | Defines a unique identifier for the dataset (e.g., `sap_raw` or `sap_foundation`).  
`data.datasets.projectId` | Project ID | `-` | References the Google Cloud Project ID hosting the dataset.  
`data.datasets.datasetId` | BigQuery Dataset ID | `-` | References the actual BigQuery dataset name.  
  
### Data: Modules

The modules define the structure and components of the Dataform data pipelines.

### Data: Modules: Foundations

This section configures the [data foundation layer](https://docs.cloud.google.com/cortex/docs/data-foundation) modules that process data from the raw layer into standardized latest records representation of the source data. In case the source provides a view on the latest records directly, or such transformations are performed by the source system connector, the module can be configured as an external data foundation source.
    
    
    modules:
      # List of foundation modules.
      foundations:
        # Unique identifier for the module instance.
        - moduleId: erp
          # Path of the module format: {namespace}.{systemtype:sap}.{module_type:foundations}.{subsystemtype:sap}, for example, cortex.sap.foundations.sap.
          modulePath: cortex.sap.foundations.sap
          # Reference to the source dataset ID.
          dataSourceId: sap_raw
          # Reference to the target dataset ID.
          dataTargetId: sap_foundation
          # Module-specific configuration settings.
          moduleSettings:
            # SAP version (for example, ecc, s4).
            sapVersion: ecc
            # SAP client number.
            mandt: "100"
          # Whether the module is enabled.
          enabled: true
          # Whether the foundation is external (does not create target dataset).
          external: false
          # Custom table settings file, relative to 'config/' file directory
          # Recommended path: '{namespace_dir}/{system_type}/foundations/{system_sub_type}/table_settings.yaml' (e.g. 'cortex/sap/foundations/sap/table_settings.yaml')
          # Default path: '../src/data_modules/{namespace_dir}/{system_type}/foundations/{system_sub_type}/table_settings.default.yaml'
          tableSettings: "custom_table_settings.yaml"
    

The following table describes the data foundation modules parameters for `modules.foundations` configuration.

Parameter | Meaning | Default value | Description  
---|---|---|---  
`moduleId` | Module Identifier | `erp` | Unique identifier for a specific data foundation transformation module instance.  
`modulePath` | Module Path | `cortex.sap.foundations.sap` | Defines the namespaced path to the module, business logic or template applied. Format: {namespace}.{systemtype:sap}.{module_type:foundations}.{subsystemtype:sap} (for example, `cortex.sap.foundations.sap`).  
`dataSourceId` | Source Link | `sap_raw` | References the 'id' from the `data.datasets` list to pull data from.  
`dataTargetId` | Target Link | `sap_foundation` | References the 'id' from the `data.datasets` list to push data to.  
`moduleSettings.sapVersion` | SAP System Version | `ecc` | Applicable for SAP data sources only. Determines source-specific logic for `ecc` (ECC) or `s4` (S/4HANA) systems.  
`moduleSettings.mandt` | SAP Client (Mandant) | `100` | Applicable for SAP data sources only. The 3-digit SAP client identifier used to filter data rows.  
`enabled` | Module enablement | `true` | Specifies whether the module is enabled.  
`external` | External foundation | `false` | Specifies whether the foundation is external (does not create target dataset).  
`tableSettings` | Table settings | `src/data_modules/{namespace_dir}/{system_type}/foundations/{system_sub_type}/table_settings.default.yaml` | Path to custom Table settings configuration file, relative to this config file.  
**Recommended path** : relative to `config/` directory: '{namespace_dir}/{system_type}/foundations/{system_sub_type}/table_settings.yaml'  
**Default path** : '../src/data_modules/{namespace_dir}/{system_type}/foundations/{system_sub_type}/table_settings.default.yaml'   
  
### Data: Modules: Catalogs

External lakehouse catalogs allow Cortex Framework to ingest external tables from BigLake Delta Sharing catalogs and shares without physical manifests.
    
    
    modules:
      # List of external catalog modules.
      catalogs:
        # Unique identifier for the catalog.
        - id: sap_bdc_catalog
          # Type of the catalog.
          type: lakehouse_delta_share
          # Logical namespace prefixes bound by this catalog.
          bindsNamespaces: [sap_bdc]
          # Connection settings for the catalog.
          connectionSettings:
            # Unique identifier for the catalog.
            catalogId: sap_bdc_catalog
            # Unique identifier for the project hosting the catalog.
            projectId: sap_bdc_delta_share
            # Geographic region location for the catalog.
            location: europe-west3
            # List of shares to import.
            shares:
              - shareId: customer_v1_he2_100_p8123
              - shareId: salesorder_v1_he2_100_p8124
          # Whether the catalog is enabled.
          # enabled: true
    

The following table describes the external catalog configuration parameters.

Parameter | Meaning | Default value | Description  
---|---|---|---  
`id` | Catalog Identifier | - | Unique identifier for a specific external catalog module instance.  
`type` | Catalog Type | `lakehouse_delta_share` | Type of the catalog. Supports `lakehouse_delta_share`.  
`bindsNamespaces` | Namespaces Bound | - | A list of logical namespace prefixes bound by this catalog (e.g., `[sap_bdc]`).  
`connectionSettings.catalogId` | Physical Catalog ID | - | Physical catalog ID. Typically same as module ID.  
`connectionSettings.projectId` | Project ID | - | The Google Cloud Project ID where the catalog connection is managed.  
`connectionSettings.location` | Location | - | The geographic region location for the catalog.  
`connectionSettings.shares` | Shares | - | List of Delta Sharing shares to import. Each share must contain a `shareId`.  
`enabled` | Catalog Enablement | `true` | Specifies whether the catalog is enabled.  
  
### Data: Modules: Products

Data product modules define the aggregations, calculations, and joins necessary to transform raw data into insights that fulfill specific business use cases.

The configuration of the data products allows setting of unique ID, definition of dependencies as well as reference of the data foundation module and target dataset where the results will be stored into.

Detailed configuration of given data products is defined within files referenced by the key: `tableSettings`.
    
    
    modules:
      # List of data product modules.
      products:
        # Unique identifier for the data product instance.
        - moduleId: sap_purchasing_organizational_structure
          # Path of the data product (namespaced).
          modulePath: cortex.sap.products.purchasing_organizational_structure
          # Map of module dependencies.
          dependencyBindings:
            sapModule: erp
          # Reference to the target dataset ID.
          dataTargetId: product_target
          # Whether the module is enabled.
          enabled: true
          # Whether this data product is synced to the Knowledge Catalog. Defaults to true.
          syncToKc: true
    
          # Custom table settings file, relative to 'config/' file directory
          # Recommended path: '{namespace_dir}/{system_type}/products/{product_name}/table_settings.yaml'
          # If omitted, defaults to '../src/data_modules/{namespace_dir}/{system_type}/products/{product_name}/table_settings.default.yaml'
          # tableSettings: "custom_dataproduct_table_settings.yaml"
    

The following table describes the data product modules parameters for `modules.products` configuration.

Parameter | Meaning | Default value | Description  
---|---|---|---  
`moduleId` | Module Identifier | - | Unique identifier for a specific transformation module instance.  
`modulePath` | Module Path | - | Defines the namespaced path to the module, business logic or template applied, format: {namespace}.{systemtype:sap}.{module_type:products}.{dataproduct_name}, for example, `cortex.sap.products.purchasing_organizational_structure`, defined in `src/data_modules/{namespace_dir}/{system_type}/products/{product_name}` folder.  
`dataTargetId` | Target Link | `product_target` | References the 'id' from the targets list to push data to.  
`dependencyBindings` | Upstream Dependency | `sapModule: erp` | Specifies mappings for satisfying module dependencies. For example, mapping `sapModule` to `erp`.  
`enabled` | Module enablement | `true` | Specifies whether the module is enabled.  
`syncToKc` | Knowledge Catalog synchronisation | `true` | Whether this data product is synced to the Knowledge Catalog.  
`tableSettings` | Table settings | `src/data_modules/{namespace_dir}/{system_type}/products/{product_name}/table_settings.default.yaml` | Path to custom Table settings configuration file, relative to this config file.  
**Recommended path** : relative to `config/` directory: '{namespace_dir}/{system_type}/products/{product_name}/table_settings.yaml'  
**Default path** : '../src/data_modules/{namespace_dir}/{system_type}/products/{product_name}/table_settings.default.yaml'   
  
### Deployment environment

Cortex Framework uses Dataform to orchestrate SQL transformations within BigQuery. The `deployment:` block defines the Dataform configuration, responsible for the execution of the data pipelines, including the repository project, location, repository name, and the Dataform workspace name.
    
    
    deployment:
      targets:
        - type: dataform
          enabled: true
          targetSettings:
            repositoryProjectId: YOUR_REPO_PROJECT_ID
            repositoryRegion: us-central1
            repositoryName: cortex-repository
            workspaceName: dev
            # serviceAccount: "example@example.com"
    

The following table describes the deployment targets location parameters (`deployment.targets:`).

Parameter | Meaning | Default Value | Description  
---|---|---|---  
`type` | Deployment type | `dataform` | Type of the deployment targets.  
`enabled` | Enabled/ Disabled | `true` | Specifies if given deployment target is enabled or disabled.  
`targetSettings.repositoryProjectId` | Repository project ID | `YOUR_REPO_PROJECT_ID` | The Google Cloud Project ID where the Dataform repository is managed.  
`targetSettings.repositoryRegion` | Repository region | `us-central1` | The Google Cloud region for the Dataform repository (for example, `us-central1` or `europe-west1`).  
`targetSettings.repositoryName` | Repository name | `cortex-repository` | The specific name of the Dataform repository.  
`targetSettings.workspaceName` | Workspace name | `dev` | The specific Dataform workspace used for the deployment cycle.  
`targetSettings.serviceAccount` | Service account email | `-` | Default service account email for Dataform repository execution.  
  
* * *

## Configuration file: `table_settings.yaml`

This guide explains how to use `table_settings.yaml` file to configure data foundation and data product tables in Google Cloud Cortex Framework.

The data module specific `table_settings.yaml` file controls how raw source tables are conformed and how analytical data models are materialized within BigQuery. Using this file, you can configure tags, materialization strategies, and advanced BigQuery performance features like partitioning or clustering.

### Dynamic dependency resolution

By default, Cortex Framework optimizes deployment footprint and execution time by only deploying and compiling the foundation tables that are required as dependencies of your enabled data products. If a table configured in `table_settings.yaml` does not have any active downstream data products depending on it, it is omitted from deployment. 

To override this optimization and force the deployment of a foundation table, you can set the `deployAlways` attribute to `true` (see Data foundation style parameter reference).

In Google Cloud Cortex Framework, each module (foundation or product) can be assigned a specific table settings file in the [deployment configuration file](https://docs.cloud.google.com/cortex/docs/deployment-configuration): `config/config.yaml` using the `tableSettings` property.

### Configuration paths

  * **Custom settings (Recommended):** To customize table behaviors, copy the default file to your configuration directory, modify it, and reference its path in `config/config.yaml`. The recommended paths to use (relative to `config/` directory), are: 
    * **Foundation modules:** `namespace_dir/system_type/foundations/system_sub_type/custom_table_settings.yaml` (e.g., `config/cortex/sap/foundations/sap/table_settings.yaml`)
    * **Product modules:** `namespace_dir/system_type/products/product_name/custom_table_settings.yaml` (e.g., `config/cortex/sap/products/accounting_documents/table_settings.yaml`)
  * **Default fallback:** If `tableSettings` is omitted, the framework automatically falls back to: 
    * **Foundation modules:** `../src/data_modules/namespace_dir/system_type/foundations/system_sub_type/table_settings.default.yaml`
    * **Product modules:** `../src/data_modules/namespace_dir/system_type/products/product_name/table_settings.default.yaml`



* * *

### Configuration styles

There are two distinct schema styles for `table_settings.yaml` depending on the category of the module:

  1. **Data Foundation Style:** List-based mapping that defines the source-to-target schema relationships, CDC (Change Data Capture) handling, and BigQuery layout. Notice that the **data foundation table-settings** layout is source system specific.

  2. **Data Product Style:** Map-based mapping (dictionary) that defines how analytical views or tables are materialized (e.g., as views, tables, or incremental tables) and optimized.




Both styles support three root-level sections to segregate configurations by source system version (primarily used for SAP Data Foundation and SAP-dependent products):

  * `ecc`: Settings applied only when deploying an SAP ECC source system.
  * `s4`: Settings applied only when deploying an SAP S/4HANA source system.
  * `common`: Settings applied regardless of the SAP version (used for conformed or universal settings).



* * *

### Data foundation style for SAP ERP

In a data foundation module for SAP ERP source systems, the `table_settings.yaml` file is structured as a list of table items under the `ecc`, `s4`, and `common` keys. Each item maps a raw source table to a conformed target table and configures its BigQuery settings.

#### YAML syntax example
    
    
    common:
      - source:
          tableName: raw_custom_bkpf
          sapTableName: bkpf
          isCdc: true
        target:
          tableName: bkpf # Optional: defaults to source tableName if omitted
          bigQueryLabels:
            - key: data_class
              value: transactional
            - key: line_of_business
              value: finance
          dataformTags: [sap, common, finance, hourly]
          clusterDetails:
            columns: [bukrs, gjahr]
          partitionDetails:
            column: budat
            partitionType: time
            timeGrain: day
        deployAlways: false
    

#### Parameter reference

Parameter | Type | Required | Default / Example | Description  
---|---|---|---|---  
`[].source` | `object` | Yes | `[]` | Describes the table in the data foundation inbound source system (e.g. `sap_raw`). See source settings.  
`[].target` | `object` | Yes | `[]` | Describes the target table in the data foundation datasets (e.g. `sap_data_foundation`). See target settings.  
`ecc` | `s4` | `common` | `string` | No | `[]` | Source system version or dialect.  
`[].deployAlways` | `boolean` | No | `false` | If `true`, the table is always deployed and built, even if optimization rules might otherwise skip it. See also Dynamic dependency resolution  
  
##### Source settings

Defines the raw inbound table characteristics.

Parameter | Type | Required | Default / Example | Description  
---|---|---|---|---  
`tableName` | `string` | **Yes** | `-` | The name of the raw source table in BigQuery (case-insensitive) as it is imported by the connector from the source system .  
`sapTableName` | `string` | No | `-` | The SAP table name (case-insensitive) as defined in the source system metadata tables (e.g. `DD03L`). If defined, this parameter is used as name for the corresponding data foundation table.  
`isCdc` | `boolean` | No | `true` | Indicates if the source table contains Change Data Capture (CDC) logs. • `true` (default): The framework processes CDC logs (using record timestamps and operation flags) to reconstruct the latest conformed state. • `false`: The table is processed as a full snapshot.  
  
##### Target settings

Defines the output conformed table layout in the target dataset.

Parameter | Type | Required | Default / Example | Description  
---|---|---|---|---  
`tableName` | `string` | No | *(Same as source)* | The name of the target conformed table to be created. If omitted, the framework defaults to the source `tableName`.  
`dataformTags` | `array[string]` | No | `[sap, finance]` | A list of metadata tags attached to the conformed action in Dataform. These are arbitrary strings and not needed to be pre-registered or defined in other configurations; they can be used immediately to filter pipeline executions (e.g., using `dataform run --tags ...`).  
`bigQueryLabels` | `array[map]` | No | `-` | A list of key-value pairs representing BigQuery labels to apply to the target table (for example, key: `data_class`, value: `transactional`).  
`clusterDetails` | `map` | No | — | Optional. BigQuery clustering configuration. See Clustering details.  
`partitionDetails` | `map` | No | — | Optional. BigQuery partitioning configuration. See Partitioning details.  
  
* * *

### Data product style

In a data product module, the `table_settings.yaml` file (`ProductTableSettings` block) is structured as a dictionary (map) under the `ecc`, `s4`, and `common` root keys. The keys of this dictionary represent the target analytical table or view names (case-insensitive), and each value is a **Product TableItem** (`ProductTableItem`) configuration block that defines materialization strategies, table enablement, and performance optimizations.

#### YAML syntax example
    
    
    common:
      currency_conversion:
        materializationType: table
        bigQueryLabels:
          - key: data_class
            value: transactional
          - key: line_of_business
            value: finance
        dataformTags: [sap, dataproduct, common]
        enabled: true
        retentionDays: 365 # Custom parameter passed to Dataform context
    s4:
      customers:
        materializationType: incremental
        bigQueryLabels:
          - key: data_class
            value: master
        dataformTags: [sap, dataproduct, masterdata]
        enabled: true
        clusterDetails:
          columns: [mandt, ktokd]
        partitionDetails:
          column: erdat
          partitionType: time
          timeGrain: day
    

#### Parameter reference

Parameter | Type | Required | Default / Example | Description  
---|---|---|---|---  
`ecc` | `s4` | `common` | `map` | No | `{}` | A map of target analytical assets (tables or views) to their `ProductTableItem` configuration descriptors.  
`[table_name]` | `map` | No | `{}` | The **Product Table Item** descriptor schema block configuring a specific analytical asset.  
`[table_name].enabled` | `boolean` | No | `true` | Controls whether the analytical table or view (`[table_name]`) is active and included when building the Dataform workspace. • `true` (default): The table definition is processed, enriched with `table_config` properties, and copied to the Dataform output directory. • `false`: The table definition is skipped during build (`SapProductBuilder` logs and omits it). The table or view won't be copied or built into Dataform, effectively excluding it from deployment without deleting the source definition files.  
`[table_name].materializationType` | `string` | No | `incremental` | How the analytical asset is built in BigQuery. **Allowed Values:**

  * `incremental` (default): Processes only new or updated records since the last run. Recommended for large transactional datasets to save cost.
  * `table`: Completely rebuilds the table from scratch on every run.
  * `view`: Deploys the asset as a BigQuery SQL view (virtual table).

  
`[table_name].dataformTags` | `array[string]` | No | `[sap, dataproduct]` | Metadata tags attached to the analytical asset in Dataform. These are arbitrary strings and don't need to be pre-registered; they can be used immediately for selective pipeline runs (for example, using `dataform run --tags ...`).  
`[table_name].bigQueryLabels` | `array[map]` | No | `-` | A list of key-value pairs representing BigQuery labels to apply to the target analytical asset (for example, key: `data_class`, value: `master`).  
`[table_name].clusterDetails` | `map` | No | — | Optional. BigQuery clustering configuration. See Clustering details.  
`[table_name].partitionDetails` | `map` | No | — | Optional. BigQuery partitioning configuration. See Partitioning details.  
**Note:** Unlike the data foundation style, the data product style supports **arbitrary custom parameters** in its YAML definition. These extra parameters are safely passed down into the SQL compilation context and can be read by custom Dataform macros and scripts. **Note:** During the build process, `SapProductBuilder` merges the `common` dictionary with the active SAP dialect dictionary (`ecc` or `s4`). If a table name exists in both `common` and the active dialect dictionary (`ecc` or `s4`), the dialect-specific `ProductTableItem` overrides the `common` configuration. Table name lookup when matching dictionary keys against definition files (`*.js` or `*.sqlx`) is case-insensitive. 

* * *

### Advanced BigQuery configurations

Both styles share the same structure for optimizing BigQuery storage and query performance through **Clustering** and **Partitioning**.

* * *

#### Clustering details

Clustering co-locates data based on the values in specific columns. BigQuery sorts the data within each storage block using these columns, which dramatically speeds up queries that filter (`WHERE`) or join (`JOIN`) on them.
    
    
    clusterDetails:
      columns: [bukrs, gjahr]
    

##### Parameter reference

Parameter | Type | Required | Example | Description  
---|---|---|---|---  
`columns` | `array[string]` | **Yes** | `[bukrs, gjahr]` | An ordered list of up to four column names to cluster the table by. **Constraint:** Columns must be alphanumeric and contain underscores only. The order of columns in the list determines the sorting hierarchy.  
  
* * *

#### Partitioning details

Partitioning divides a large table into smaller, physical segments based on the values of a date, timestamp, or integer column. This prevents BigQuery from scanning the entire table when a query only requests a specific range of days, months, or IDs.
    
    
    partitionDetails:
      column: budat
      partitionType: time
      timeGrain: day
    

##### Parameter reference

Parameter | Type | Required | Example | Description  
---|---|---|---|---  
`column` | `string` | **Yes** | `budat` | The column name used to partition the table. Must be alphanumeric and underscores only. The column type must match the `partitionType`.  
`partitionType` | `string` | **Yes** | `time` | The partitioning strategy. **Allowed Values:**

  * `time`: Partitions by a time-unit (Date, Timestamp, or Datetime column).
  * `DATE`: Partitions explicitly by a Date column.
  * `integer`: Partitions by an integer range.

  
`timeGrain` | `string` | No | `day` | **Required if`partitionType` is `time` or `DATE`.** Defines the granularity of the time partitions. **Allowed Values:** `hour`, `day`, `month`, `year` (case-insensitive).  
`rangeStart` | `integer` | No | `1` | **Required if`partitionType` is `integer`.** The start value of the first partition (inclusive).  
`rangeEnd` | `integer` | No | `1000` | **Required if`partitionType` is `integer`.** The end value of the last partition (exclusive).  
`rangeInterval` | `integer` | No | `10` | **Required if`partitionType` is `integer`.** The width of each partition interval.  
**Important:** If you configure `partitionType: integer`, you **must** specify all three range parameters (`rangeStart`, `rangeEnd`, and `rangeInterval`) to define the segment bounds. 

* * *

## Examples

The following examples show configuration templates for both data foundation and data product modules, outlining how to customize target tables, optimize storage layout in BigQuery, and configure materialization types.

### 1\. Custom data foundation table settings example

This example shows how to configure a foundation layer with clustered and partitioned transactional tables (like `bseg` and `ekbe`) alongside standard data tables:
    
    
    # ==============================================================================
    # S/4HANA-Specific Tables
    # ==============================================================================
    s4:
      # ACDOCA is a massive table in S/4HANA; clustering is vital
      - source:
          tableName: acdoca
        target:
          bigQueryLabels:
            - key: data_class
              value: transactional
          dataformTags: [sap, s4, finance, transactional, hourly]
          clusterDetails:
            columns: [rclnt, rbukrs, gjahr]
    
    # ==============================================================================
    # ECC-Specific Tables
    # ==============================================================================
    ecc:
      - source:
          tableName: faglflexa
        target:
          bigQueryLabels:
            - key: data_class
              value: transactional
          dataformTags: [sap, ecc, finance, transactional, hourly]
    
    # ==============================================================================
    # Common Tables (ECC & S/4HANA)
    # ==============================================================================
    common:
      # Financial document header (partitioned by posting date)
      - source:
          tableName: bkpf
          isCdc: true
        target:
          bigQueryLabels:
            - key: data_class
              value: transactional
          dataformTags: [sap, common, finance, hourly]
          clusterDetails:
            columns: [bukrs, gjahr]
          partitionDetails:
            column: budat
            partitionType: time
            timeGrain: day
    
      # Purchasing document items (partitioned by creation date)
      - source:
          tableName: ekpo
        target:
          bigQueryLabels:
            - key: data_class
              value: transactional
          dataformTags: [sap, common, logistics, purchasing, hourly]
          clusterDetails:
            columns: [mandt, ebeln]
          partitionDetails:
            column: aedat
            partitionType: time
            timeGrain: month
    
      # Standard master data table (no partitioning/clustering needed)
      - source:
          tableName: lfa1
        target:
          bigQueryLabels:
            - key: data_class
              value: master
          dataformTags: [sap, common, masterdata, vendor, daily]
    

### 2\. Custom data product table settings example

This example shows how to configure materialization types for downstream analytical data products. We set transactional `sales_documents` as incremental to optimize build performance and save costs, while non-transactional data tables like `customers` are built as standard tables:
    
    
    # settings applied for both ECC and S/4HANA pipelines
    common:
      # Transactional data product - incremental build
      sales_documents:
        materializationType: incremental
        bigQueryLabels:
          - key: data_class
            value: transactional
        dataformTags: [sap, dataproduct, sales, transactional]
        clusterDetails:
          columns: [vkorg, vbeln]
        partitionDetails:
          column: audat
          partitionType: time
          timeGrain: day
    
      # Master data product - full table rebuild
      customers:
        materializationType: table
        bigQueryLabels:
          - key: data_class
            value: master
        dataformTags: [sap, dataproduct, masterdata]
        clusterDetails:
          columns: [mandt, ktokd]
    
      # Aggregated reporting view - virtual view
      sales_performance_summary:
        materializationType: view
        bigQueryLabels:
          - key: data_class
            value: transactional
        dataformTags: [sap, dataproduct, sales, reporting]
    

## How-to guides

This section provides step-by-step guides for common configuration tasks and custom deployment scenarios.

### Customize table scope in a data foundation module

To add or remove tables within an existing data foundation module without creating new modules or running separate pipeline instances:

  * Copy the default `table_settings.default.yaml` configurations into your workspace config directory (for example, `config/cortex/sap/foundations/sap/custom_table_settings.yaml`).
  * In your new file, add your custom tables or remove unused standard tables under the `ecc`, `s4`, or `common` keys as required:


    
    
    common:
      - source:
          tableName: custom_table_name
        target:
          dataformTags: [custom_tag]
    

  * Update `config/config.yaml` to reference the path of your custom table settings under the module's `tableSettings` property:


    
    
    data:
      modules:
        foundations:
          - moduleId: erp
            modulePath: cortex.sap.foundations.sap
            # Custom table settings file, relative to configuration file directory
            # Recommended path: '{namespace_dir}/{system_type}/foundations/{system_sub_type}/table_settings.yaml'
            tableSettings: 'cortex/sap/foundations/sap/custom_table_settings.yaml'
    

  * To enrich the table schema of the additional table with annotations (table and column descriptions), create an annotation file in the namespace of the data foundation module you are using. In this example, based on `modulePath: cortex.sap.foundations.sap`, the path to store your annotation file `custom_table_name.yaml` is `src/data_modules/cortex/sap/foundations/sap/annotations`. The format of the annotation files is described in the [extensibility guide for data foundation](https://docs.cloud.google.com/cortex/docs/extensibility-guide-data-foundation#step_5_create_field-level_metadata_annotations).



### Configure multiple instances of a data foundation module

To deploy two or more separate pipeline instances of the same module type (for example, supporting multiple SAP instances, to segment tables, isolate environments, or target different target datasets).

**Before you begin** :

  * Ensure the source tables exist in your source raw dataset.
  * When working with SAP data foundation modules, verify that the metadata table `DD03L` contains columns and descriptor information for the custom tables you intend to ingest. See [SAP ERP requirements](https://docs.cloud.google.com/cortex/docs/source-system-integration/sap-erp) for details.



**Instructions** :

  * In the `config/config.yaml` file, add target configurations under `data.targets` to define target datasets for each pipeline instance:


    
    
    data:
      targets:
        - id: data_foundation_core
          projectId: target_project_id
          datasetId: data_foundation_sap_core
        - id: data_foundation_custom
          projectId: target_project_id
          datasetId: data_foundation_sap_custom
    

  * Define multiple instances of the module under the `data.modules.foundations` list. Give each instance a unique `moduleId`, its own target dataset IDs, and optionally `tableSettings` configuration:


    
    
    data:
      modules:
        foundations:
          # Core SAP ERP foundation module instance
          - moduleId: erp_core
            modulePath: cortex.sap.foundations.sap
            dataSourceId: sap_raw
            dataTargetId: data_foundation_core
            # If omitted, defaults to "../src/data_modules/{namespace_dir}/{system_type}/foundations/{system_sub_type}/table_settings.default.yaml"
            # tableSettings: "../src/data_modules/cortex/sap/foundations/sap/table_settings.default.yaml"
          # Custom tables pipeline instance
          - moduleId: erp_custom
            modulePath: cortex.sap.foundations.sap
            dataSourceId: sap_raw
            dataTargetId: data_foundation_custom
            # Custom table settings file, relative to configuration file directory
            # Recommended path: '{namespace_dir}/{system_type}/foundations/{system_sub_type}/table_settings.yaml'
            tableSettings: "cortex/sap/foundations/sap/custom_datafoundation_table_settings.yaml"
    

  * Create the `config/cortex/data_foundation/sap/custom_datafoundation_table_settings.yaml` file specifying the custom scope. E.g.:


    
    
    common:
      - source:
          tableName: custom_sap_table_name
        target:
          dataformTags: [sap, s4, hourly]
          clusterDetails:
            columns: [carrid, connid]
          partitionDetails:
            column: fldate
            partitionType: time
            timeGrain: day
    

  * To enrich the table schema of the additional table with annotations (table and column descriptions), create an annotation file in the namespace of the data foundation module you are using. In this example, based on `modulePath: cortex.sap.foundations.sap`, the path to store your annotation file `custom_table_name.yaml` is `src/data_modules/cortex/sap/foundations/sap/annotations`. The format of the annotation files is described in the [extensibility guide for data foundation](https://docs.cloud.google.com/cortex/docs/extensibility-guide-data-foundation#step_5_create_field-level_metadata_annotations).

  * Apply the changes by running the deployment script (`uv run cortex-build-and-deploy`), then execute the Dataform actions as described in [Post-deployment steps](https://docs.cloud.google.com/cortex/docs/post-deployment-steps).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
