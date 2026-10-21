---
url: https://docs.cloud.google.com/cortex/docs/extensibility-guide-data-foundation/
title: Data foundation module creation \u00a0|\u00a0 Google Cloud Cortex Framework \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:49:39.988752+00:00
---

# Data foundation module creation  |  Google Cloud Cortex Framework  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cortex/docs/extensibility-guide-data-foundation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Google Cloud Cortex Framework ](https://docs.cloud.google.com/cortex/docs)
  * [ Version 7 Guides ](https://docs.cloud.google.com/cortex/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Data foundation module creation

While Cortex Framework provides out-of-the-box [data foundation](https://docs.cloud.google.com/cortex/docs/data-foundation) modules for enterprise ERP systems such as SAP (`cortex.sap`), you can also create new custom data foundation modules within a [custom namespace](https://docs.cloud.google.com/cortex/docs/extensibility-guide-namespaces). This lets you define custom build behaviors and extend support to a new source system. These can include database management systems like PostgreSQL, MySQL, etc. that replicate their raw data into BigQuery.

This guide walks you through an end-to-end example of creating a new data foundation module for a **Customer Service Ticketing System** whose data (`customers`, `tickets`, `ticketlogitem` tables) has been replicated from a PostgreSQL database into a raw BigQuery dataset named `ticketing_data_raw`.

When creating a custom [data foundation](https://docs.cloud.google.com/cortex/docs/data-foundation) module, we recommend using a dedicated [custom namespace](https://docs.cloud.google.com/cortex/docs/extensibility-guide-namespaces) to improve lifecycle management by separating extensions and customizations from Cortex Framework artifacts.

**Note:** If you only want to process additional standard or custom tables, you do **not** need to create a custom module. Instead, you can [configure standard module to run multiple instances with its own table settings](https://docs.cloud.google.com/cortex/docs/deployment-configuration#add-table-to-data-foundation).

## Example scenario overview

In this walkthrough, we will:

  1. Create a dedicated custom namespace `ticketing` to isolate the data foundation assets.
  2. Define a new data foundation module of path `ticketing.ticketing.foundations.ticketing_system`.
  3. Configure table settings (`table_settings.default.yaml`) for the `customers`, `tickets`, and `ticketlogitem` tables.
  4. Create column and field-level metadata annotations for each table.
  5. Register the raw data source (`ticketing_data_raw`), the target conformed dataset (`data_foundation_ticketing`), and the new foundation module in `config/config.yaml`.



## Module folder and file structure

All physical files for your new data foundation module reside inside your custom namespace under `src/data_modules/`. The following table and directory tree outline where to place each file:
    
    
    config/
    └── config.yaml                                           # Global configuration & module registration
    src/data_modules/ticketing/ticketing/foundations/ticketing_system/
    ├── manifest.yaml                                         # Declares module category, type, and builder
    ├── table_settings.default.yaml                           # Table materialization, bigQueryLabels, dataformTags, and layouts
    ├── builder.py                                            # (Optional) Custom Dataform generator class for this module
    └── annotations/                                          # Field and column-level schema descriptions
        ├── customers.yaml
        ├── tickets.yaml
        └── ticketlogitem.yaml
    

**Important: Before starting, ensure the source tables you plan to process exists in the[raw layer](https://docs.cloud.google.com/cortex/docs/overview#raw_layer) dataset.**

File or directory path | Purpose and description  
---|---  
`config/config.yaml` | Registers the `ticketing` namespace, the PostgreSQL raw data source, the target BigQuery dataset, and the foundation module instance.  
`src/data_modules/ticketing/ticketing/foundations/ticketing_system/manifest.yaml` | Declares the module metadata, display name, category (e.g., `foundation`), module type (e.g., `generic`), and the generator builder class used during compilation.  
`src/data_modules/ticketing/ticketing/foundations/ticketing_system/table_settings.default.yaml` | Configures which source tables from `ticketing_data_raw` should be conformed, along with BigQuery optimization dataformTags, bigQueryLabels, partition details, and cluster details.  
`src/data_modules/ticketing/ticketing/foundations/ticketing_system/annotations/*.yaml` | Contains rich YAML metadata describing table and field definitions. These are automatically merged into the compiled Dataform definitions so descriptions persist in BigQuery table metadata.  
`src/data_modules/ticketing/ticketing/foundations/ticketing_system/builder.py` | _Optional._ If your source database requires custom data cleaning or dialect-specific SQL transformations during compilation, you can define a module-level builder class here.  
  
## Step 1: Register the namespace, data source, and target in `config.yaml`

Before creating the physical files, open your deployment configuration file (`config/config.yaml`) and declare the custom namespace, the raw PostgreSQL source dataset, and the destination dataset where conformed tables will be created:
    
    
    data:
      namespaces:
        - name: cortex
          path: ../src/data_modules/cortex
        - name: ticketing                              # <-- Name of custom namespace
          path: ../src/data_modules/ticketing          # <-- Points to subdirectory under 'src/data_modules/'
    
      datasets:
        - id: ticketing_data_raw                       # <-- Unique source ID
          projectId: "source_project_id"
          datasetId: ticketing_data_raw                # <-- Raw dataset containing PostgreSQL replication tables
        - id: data_foundation_ticketing                # <-- Unique target ID
          projectId: "target_project_id"
          datasetId: data_foundation_ticketing         # <-- Target dataset for conformed foundation tables
    

## Step 2: Register the data foundation module in `config.yaml`

Under the `data.modules.foundations` section of `config/config.yaml`, register the new data foundation module instance, linking the data source (`ticketing_data_raw`) to the data target (`data_foundation_ticketing`):
    
    
    data:
      modules:
        foundations:
          - moduleId: ticketing_foundation
            modulePath: ticketing.ticketing.foundations.ticketing_system   # Format: {namespace}.{systemtype}.{module_type:foundations}.{subsystemtype}
            dataSourceId: ticketing_data_raw
            dataTargetId: data_foundation_ticketing
            # Custom table settings file relative to 'config/' directory
            # Recommended path: '{namespace_dir}/{system_type}/foundations/{system_sub_type}/table_settings.yaml'
            # If omitted, defaults to "../src/data_modules/ticketing/ticketing/foundations/ticketing_system/table_settings.default.yaml"
            tableSettings: "ticketing/ticketing/foundations/ticketing_system/table_settings.yaml"
    

## Step 3: Create the module manifest file

Create the manifest file declaring your module metadata: `src/data_modules/ticketing/ticketing/foundations/ticketing_system/manifest.yaml`.
    
    
    displayName: Ticketing System Data Foundation
    description: Conformed foundation tables for PostgreSQL raw ticketing database.
    category: foundation
    type: generic
    builder: ticketing_foundation
    

**Note:** The `builder:` parameter instructs Cortex Framework which compiler class to use when generating Dataform `.sqlx` or `.js` definitions. If you register a custom builder (see Step 6), specify its key here.

## Step 4: Create the table settings file (`table_settings.default.yaml`)

Create the default table configuration file `src/data_modules/ticketing/ticketing/foundations/ticketing_system/table_settings.default.yaml`. This file defines how the replicated PostgreSQL tables (`customers`, `tickets`, `ticketlogitem`) are materialized, partitioned, and clustered within BigQuery:
    
    
    common:
      - source:
          tableName: customers
        target:
          bigQueryLabels:
            - key: data_class
              value: master
          dataformTags: [ticketing, foundation, masterdata]
          clusterDetails:
            columns: [customer_id]
    
      - source:
          tableName: tickets
        target:
          bigQueryLabels:
            - key: data_class
              value: transactional
          dataformTags: [ticketing, foundation, transactional]
          partitionDetails:
            column: created_at
            partitionType: time
            timeGrain: day
          clusterDetails:
            columns: [ticket_id, customer_id]
    
      - source:
          tableName: ticketlogitem
        target:
          bigQueryLabels:
            - key: data_class
              value: transactional
          dataformTags: [ticketing, foundation, transactional]
          partitionDetails:
            column: log_timestamp
            partitionType: time
            timeGrain: day
          clusterDetails:
            columns: [ticket_id, log_id]
    

## Step 5: Create field-level metadata annotations

To ensure your conformed tables contain clear documentation in BigQuery, create an annotation YAML file for each table inside `src/data_modules/ticketing/ticketing/foundations/ticketing_system/annotations/`. The filename must exactly match the source table name.

### `annotations/customers.yaml`
    
    
    description: "Customer master data conformed from PostgreSQL raw ticketing database."
    fields:
      - name: "customer_id"
        description: "Unique customer identifier, PK"
      - name: "email"
        description: "Primary email address associated with the customer"
      - name: "full_name"
        description: "Customer full name or account contact name"
      - name: "created_at"
        description: "Timestamp when the customer record was originally created in PostgreSQL"
    

### `annotations/tickets.yaml`
    
    
    description: "Customer service tickets conformed from PostgreSQL raw ticketing database."
    fields:
      - name: "ticket_id"
        description: "Unique ticket identifier, PK"
      - name: "customer_id"
        description: "Foreign key referencing customers.customer_id"
      - name: "subject"
        description: "Summary or subject line of the customer inquiry"
      - name: "status"
        description: "Current ticket lifecycle status (e.g., OPEN, IN_PROGRESS, RESOLVED, CLOSED)"
      - name: "priority"
        description: "Priority severity level (e.g., LOW, MEDIUM, HIGH, URGENT)"
      - name: "created_at"
        description: "Timestamp when the ticket was created"
      - name: "updated_at"
        description: "Timestamp when the ticket was last modified"
    

### `annotations/ticketlogitem.yaml`
    
    
    description: "Audit log history and activity events for customer service tickets."
    fields:
      - name: "log_id"
        description: "Unique log event identifier, PK"
      - name: "ticket_id"
        description: "Foreign key referencing tickets.ticket_id"
      - name: "action"
        description: "Action or event performed on the ticket"
      - name: "description"
        description: "Notes and description on performed events on the ticket"
      - name: "performed_by"
        description: "User, agent, or automated system that performed the action"
      - name: "log_timestamp"
        description: "Exact timestamp when the activity log event occurred"
    

## Step 6: (Optional) Define a custom foundation builder

If your PostgreSQL data foundation requires logic during compilation (such as automatic data type casting, timestamp conversion, or data cleaning rules across all tables), you can define a custom builder scoped to this module.

Create `src/data_modules/ticketing/ticketing/foundations/ticketing_system/builder.py`:
    
    
    import logging
    import pathlib
    import yaml
    from common.builders.base import FoundationBuilder, Source
    from common.registry import builder_registry
    from common.schemas import config_schema, manifest_schema
    
    logger = logging.getLogger(__name__)
    
    @builder_registry.register("ticketing_foundation")
    class TicketingFoundationBuilder(FoundationBuilder[config_schema.BaseModuleConfig]):
        """Custom Dataform generator for PostgreSQL ticketing data foundation."""
    
        def build(
            self,
            *,
            module_id: str,
            module_config: config_schema.BaseModuleConfig,
            global_config: config_schema.GlobalConfig,
            manifest: manifest_schema.ManifestConfig,
            base_dir: pathlib.Path,
            annotations_dir: pathlib.Path,
            output_dir: pathlib.Path,
            module_dir_name: str,
            sources_registry: set[Source],
            table_settings_file: pathlib.Path | None = None,
            required_tables: set[str] | None = None,
        ) -> None:
            logger.info("Building ticketing data foundation for module: %s", module_id)
            
            # 1. Load table settings
            if not table_settings_file or not table_settings_file.exists():
                logger.warning("No valid table settings found for %s", module_id)
                return
    
            with open(table_settings_file, encoding="utf-8") as f:
                settings = yaml.safe_load(f) or {}
    
            tables = settings.get("common", [])
            source_config = global_config.get_data_source(module_config.data_source_id)
            target_dataset = global_config.get_data_target(module_config.data_target_id)
    
            # 2. Generate Dataform .sqlx files for each table
            for table_item in tables:
                source_table = table_item["source"]["tableName"]
                if required_tables and source_table not in required_tables and not table_item.get("deployAlways"):
                    continue
    
                # Register source table for centralized source generation
                sources_registry.add(Source(source_config.project_id, source_config.dataset_id, source_table))
    
                # Retrieve labels if configured
                bigquery_config = {}
                if "bigQueryLabels" in table_item["target"]:
                    labels_dict = {label["key"]: label["value"] for label in table_item["target"]["bigQueryLabels"]}
                    bigquery_config["labels"] = labels_dict
    
                dataform_tags = table_item["target"].get("dataformTags", ["ticketing", "foundation"])
    
                sqlx_content = f"""config {{
      type: "table",
      schema: "{target_dataset.dataset_id}",
      name: "{source_table}",
      tags: {dataform_tags}"""
                
                if bigquery_config:
                    sqlx_content += f",\n  bigquery: {bigquery_config}"
                    
                sqlx_content += f"""
    }}
    
    SELECT *
    FROM `${{source_config.project_id}}.${{source_config.dataset_id}}.{source_table}`
    """
                out_file = output_dir / f"{source_table}.sqlx"
                out_file.write_text(sqlx_content, encoding="utf-8")
                logger.info("Generated %s", out_file)
    

**Note:** When `builder.py` is placed directly inside the module directory, Cortex Framework dynamically discovers and loads it without requiring global python package registration.

## Verification of new foundation module

To verify and deploy your newly created data foundation module:

  1. Execute the Cortex Framework build and deploy script: `bash uv run cortex-build-and-deploy --config "config/config.yaml"`
  2. Check that the Dataform compilation succeeded without errors and that `.sqlx` scripts were generated for `customers`, `tickets`, and `ticketlogitem`.
  3. Follow the [Post deployment steps](https://docs.cloud.google.com/cortex/docs/post-deployment-steps) to run your Dataform pipeline actions and verify the conformed records inside your `data_foundation_ticketing` dataset in BigQuery.



To verify that the custom data foundation module compiles and deploys successfully, refer to the [Verification](https://docs.cloud.google.com/cortex/docs/extensibility-guide-data-product#verification-of-custom-namespace-extension) section in the data product extensibility page.

* * *

  * Previous step: [Setting up a custom namespace](https://docs.cloud.google.com/cortex/docs/extensibility-guide-namespaces)
  * Next step: [Data product module creation](https://docs.cloud.google.com/cortex/docs/extensibility-guide-data-product)
  * Back to [Overview](https://docs.cloud.google.com/cortex/docs/extensibility-guide)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
