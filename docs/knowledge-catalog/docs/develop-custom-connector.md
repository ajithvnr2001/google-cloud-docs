---
url: https://docs.cloud.google.com/knowledge-catalog/docs/develop-custom-connector/
title: Develop a custom connector for metadata import \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:37:29.436165+00:00
---

# Develop a custom connector for metadata import  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/develop-custom-connector/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  Develop a custom connector for metadata import Stay organized with collections  Save and categorize content based on your preferences. 

Custom connectors let you extract metadata from third-party data sources, such as MySQL, SQL Server, and Oracle. You can then import this metadata into Knowledge Catalog (formerly Dataplex Universal Catalog) through a [managed connectivity pipeline](https://docs.cloud.google.com/knowledge-catalog/docs/managed-connectivity-overview). Building a custom connector helps you catalog, search, and govern assets from data sources that don't have a prebuilt connector.

You can use the PySpark reference template and example Python connector for Oracle Database Express Edition (XE) on this page as a starting point to build your own connector.

## How connectors work

A connector extracts metadata from a third-party data source, transforms the metadata to Knowledge Catalog `ImportItem` format, and generates metadata import files that can be imported by Knowledge Catalog.

The connector is a part of a managed connectivity pipeline. A managed connectivity pipeline is an orchestrated workflow that you use to import Knowledge Catalog metadata. The managed connectivity pipeline runs the connector and performs other tasks in the import workflow, such as running a metadata import job and capturing logs.

The managed connectivity pipeline runs the connector by using a [Managed Service for Apache Spark](https://docs.cloud.google.com/dataproc-serverless/docs/overview) batch job. Managed Service for Apache Spark provides a serverless Spark execution environment. Although you can build a connector that doesn't use Spark, we recommend that you use Spark because it can improve the performance of your connector. You can develop connectors by using Python, Java, Scala, or R.

### Connector requirements

The connector has the following requirements:

  * The connector must be an Artifact Registry image that can be run on Managed Service for Apache Spark.
  * The connector must generate metadata files in a format that can be imported by a Knowledge Catalog metadata import job (the `metadataJobs.create` API method). For detailed requirements, see [Metadata import file](https://docs.cloud.google.com/knowledge-catalog/docs/import-metadata#metadata-import-file).
  * The connector must accept the following command-line arguments to receive information from the pipeline:

Command-line argument | Value that pipeline provides  
---|---  
`target_project_id` | PROJECT_ID  
`target_location_id` | REGION  
`target_entry_group_id` | ENTRY_GROUP_ID  
`output_bucket` | CLOUD_STORAGE_BUCKET_ID  
`output_folder` | FOLDER_ID  
  
The connector uses these arguments to generate metadata in a target entry group `projects/PROJECT_ID/locations/REGION/entryGroups/ENTRY_GROUP_ID`, and to write to a Cloud Storage bucket `gs://CLOUD_STORAGE_BUCKET_ID/FOLDER_ID`. Each execution of the pipeline creates a new folder FOLDER_ID in bucket CLOUD_STORAGE_BUCKET_ID. The connector should write metadata import files to this folder.




The pipeline templates support PySpark connectors. The templates assume that the driver ([`mainPythonFileUri`](https://docs.cloud.google.com/dataproc-serverless/docs/reference/rest/v1/projects.locations.batches#pysparkbatch)) is a local file on the connector image named `main.py`. You can modify the pipeline templates for other scenarios, such as a Spark connector, a different driver URI, or other options.

Here's how you use PySpark to create an import item in the metadata import file.
    
    
    """PySpark schemas for the data."""
    entry_source_schema = StructType([
          StructField("display_name", StringType()),
          StructField("source", StringType())])
    
    aspect_schema = MapType(StringType(),
                            StructType([
                                StructField("aspect_type", StringType()),
                                StructField("data", StructType([
                                ]))
                              ])
                            )
    
    entry_schema = StructType([
      StructField("name", StringType()),
      StructField("entry_type", StringType()),
      StructField("fully_qualified_name", StringType()),
      StructField("parent_entry", StringType()),
      StructField("entry_source", entry_source_schema),
      StructField("aspects", aspect_schema)
    ])
    
    import_item_schema = StructType([
      StructField("entry", entry_schema),
      StructField("aspect_keys", ArrayType(StringType())),
      StructField("update_mask", ArrayType(StringType()))
    ])
    

## Before you begin

The example on this page uses a Python connector for Oracle Database Express Edition (XE) and assumes that you're familiar with Python and PySpark.

Review the following information:

  * [Knowledge Catalog metadata concepts](https://docs.cloud.google.com/knowledge-catalog/docs/metadata-overview)
  * Documentation about [metadata import jobs](https://docs.cloud.google.com/knowledge-catalog/docs/import-metadata)



Do the following things. Create all resources in the same Google Cloud location.

  1. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  2. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  3. Enable the Dataplex, Dataproc, Workflows, and Artifact Registry APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable dataplex.googleapis.com dataproc.googleapis.com workflows.googleapis.com artifactregistry.googleapis.com

  4. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  5. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  6. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  7. Grant roles to your user account. Run the following command once for each of the following IAM roles: `roles/resourcemanager.projectCreator, roles/billing.projectManager, roles/serviceusage.admin, roles/iam.serviceAccountCreator, roles/iam.securityAdmin, roles/storage.admin, roles/artifactregistry.writer, roles/dataplex.entryGroupOwner, roles/dataplex.entryOwner, roles/dataplex.aspectTypeOwner`
         
         gcloud projects add-iam-policy-binding PROJECT_ID --member="user:USER_IDENTIFIER" --role=ROLE

Replace the following:

     * `PROJECT_ID`: Your project ID.
     * `USER_IDENTIFIER`: The identifier for your user account. For example, `myemail@example.com`. 
     * `ROLE`: The IAM role that you grant to your user account.

  8. Set up authentication:

     1. Ensure that you have the Create Service Accounts IAM role (`roles/iam.serviceAccountCreator`) and the Project IAM Admin role (`roles/resourcemanager.projectIamAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
     2. Create the service account: 
            
            gcloud iam service-accounts create SERVICE_ACCOUNT_NAME

Replace `SERVICE_ACCOUNT_NAME` with a name for the service account. 

     3. Grant the `roles/owner` IAM role to the service account: 
            
            gcloud projects add-iam-policy-binding PROJECT_ID --member="serviceAccount:SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com" --role=roles/owner

Replace the following: 

        * `SERVICE_ACCOUNT_NAME`: the name of the service account
        * `PROJECT_ID`: the project ID where you created the service account
**Note** : The `--role` flag affects which resources the service account can access in your project. You can revoke these roles or grant additional roles later. In production environments, do not grant the Owner, Editor, or Viewer roles. Instead, grant a [predefined role](https://docs.cloud.google.com/iam/docs/understanding-roles#predefined_roles) or [custom role](https://docs.cloud.google.com/iam/docs/understanding-custom-roles) that meets your needs. 
  9. [Create a Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/creating-buckets) to store the metadata import files.

  10. Create the following metadata resources in the same project.

**Note:** This document assumes all the resources are in the same project for simplicity. If you want to create resources different projects, you can adjust the sample code. 

For example values, see the Example metadata resources for an Oracle source section of this document.

     1. [Create an entry group](https://docs.cloud.google.com/knowledge-catalog/docs/ingest-custom-sources#create-entry-group).
     2. [Create custom aspect types](https://docs.cloud.google.com/knowledge-catalog/docs/enrich-entries-metadata#create-aspect-type) for the entries that you want to import. Use the naming convention `SOURCE`-`ENTITY_TO_IMPORT`.

For example, for an Oracle database, create an aspect type named `oracle-database`.

Optionally, you can create additional aspect types to store other information.

     3. [Create custom entry types](https://docs.cloud.google.com/knowledge-catalog/docs/ingest-custom-sources#create-entry-type) for the resources that you want to import, and assign the relevant aspect types to them. Use the naming convention `SOURCE`-`ENTITY_TO_IMPORT`.

For example, for an Oracle database, create an entry type named `oracle-database`. Link it to the aspect type that is named `oracle-database`.

  11. Ensure that your third-party source is accessible from your Google Cloud project. For more information, see [Managed Service for Apache Spark network configuration](https://docs.cloud.google.com/dataproc-serverless/docs/concepts/network).



## Create a basic Python connector

The example basic Python connector creates top-level entries for an Oracle data source by using the Knowledge Catalog client library classes. Then, you provide the values for the entry fields.

The connector creates a metadata import file with the following entries:

  * An `instance` entry, with entry type `projects/PROJECT_ID/locations/LOCATION/entryTypes/oracle-instance`. This entry represents an Oracle Database XE system.
  * A `database` entry, which represents a database inside the Oracle Database XE system.

**Note:** This basic example lets you create the metadata import file without a connection to Oracle Database XE. To extract metadata in production, you need to set up a connection to your data source so that the connector can read data from it.

To build a basic Python connector, do the following:

  1. Clone the [`cloud-dataplex` repository](https://github.com/GoogleCloudPlatform/cloud-dataplex).

  2. Set up a local environment. We recommend that you use a virtual environment.
         
         mkdir venv
         python -m venv venv/
         source venv/bin/activate
         

Use the [active](https://devguide.python.org/developer-workflow/development-cycle/index.html#in-development-main-branch) or [maintenance](https://devguide.python.org/developer-workflow/development-cycle/index.html#maintenance-branches) versions of Python. Python versions 3.7 and later are supported.

  3. Create a Python project.

  4. Install requirements:
         
         pip install -r requirements.txt
         

The following requirements are installed:
         
         google-cloud-dataplex==2.2.2
         google-cloud-storage
         google-cloud-secret-manager
         

  5. Add a `main.py` pipeline file on the root of the project.
         
         from src import bootstrap
         
         
         if __name__ == '__main__':
             bootstrap.run()
         

When deploying your code to Managed Service for Apache Spark, the `main.py` file serves as the entry point for execution. We recommend that you minimize the amount of information that is stored in the `main.py` file; use this file to call functions and classes that are defined within your connector, such as the `src/bootstrap.py` class.

  6. Create a `src` folder to store the majority of the logic for your connector.

  7. Update the `src/cmd_reader.py` file with a Python class to accept command-line arguments. You can use the [argeparse](https://docs.python.org/3/library/argparse.html#module-argparse) module to do this.
         
         """Command line reader."""
         import argparse
         
         
         def read_args():
             """Reads arguments from the command line."""
             parser = argparse.ArgumentParser()
         
             # Dataplex arguments
             parser.add_argument("--target_project_id", type=str, required=True,
                 help="The name of the target Google Cloud project to import the metadata into.")
             parser.add_argument("--target_location_id", type=str, required=True,
                 help="The target Google Cloud location where the metadata will be imported into.")
             parser.add_argument("--target_entry_group_id", type=str, required=True,
                 help="The ID of the entry group to import metadata into. "
                      "The metadata will be imported into entry group with the following"
                      "full resource name: projects/${target_project_id}/"
                      "locations/${target_location_id}/entryGroups/${target_entry_group_id}.")
         
             # Oracle arguments
             parser.add_argument("--host_port", type=str, required=True,
                 help="Oracle host and port number separated by the colon (:).")
             parser.add_argument("--user", type=str, required=True, help="Oracle User.")
             parser.add_argument("--password-secret", type=str, required=True,
                 help="Secret resource name in the Secret Manager for the Oracle password.")
             parser.add_argument("--database", type=str, required=True,
                 help="Source Oracle database.")
         
             # Google Cloud Storage arguments
             # It is assumed that the bucket is in the same region as the entry group
             parser.add_argument("--output_bucket", type=str, required=True,
                 help="The Cloud Storage bucket to write the generated metadata import file.")
             parser.add_argument("--output_folder", type=str, required=True,
                 help="A folder in the Cloud Storage bucket, to write the generated metadata import files.")
         
             return vars(parser.parse_known_args()[0])
         

In production environments, we recommend that you store the password in [Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview).

  8. Update the `src/constants.py` file with code to create constants.
         
         """Constants that are used in the different files."""
         import enum
         
         SOURCE_TYPE = "oracle"
         
         # Symbols for replacement
         FORBIDDEN = "#"
         ALLOWED = "!"
         
         
         class EntryType(enum.Enum):
             """Types of Oracle entries."""
             INSTANCE: str = "projects/{project}/locations/{location}/entryTypes/oracle-instance"
             DATABASE: str = "projects/{project}/locations/{location}/entryTypes/oracle-database"
             DB_SCHEMA: str = "projects/{project}/locations/{location}/entryTypes/oracle-schema"
             TABLE: str = "projects/{project}/locations/{location}/entryTypes/oracle-table"
             VIEW: str = "projects/{project}/locations/{location}/entryTypes/oracle-view"
         

  9. Update the `src/name_builder.py` file with methods to build the metadata resources that you want the connector to create for your Oracle resources. Use the conventions that are described in the Example metadata resources for an Oracle source section of this document.
         
         """Builds Dataplex hierarchy identifiers."""
         from typing import Dict
         from src.constants import EntryType, SOURCE_TYPE
         
         
         # Oracle cluster users start with C## prefix, but Dataplex doesn't accept #.
         # In that case in names it is changed to C!!, and escaped with backticks in FQNs
         FORBIDDEN_SYMBOL = "#"
         ALLOWED_SYMBOL = "!"
         
         
         def create_fqn(config: Dict[str, str], entry_type: EntryType,
                        schema_name: str = "", table_name: str = ""):
             """Creates a fully qualified name or Dataplex v1 hierarchy name."""
             if FORBIDDEN_SYMBOL in schema_name:
                 schema_name = f"`{schema_name}`"
         
             if entry_type == EntryType.INSTANCE:
                 # Requires backticks to escape column
                 return f"{SOURCE_TYPE}:`{config['host_port']}`"
             if entry_type == EntryType.DATABASE:
                 instance = create_fqn(config, EntryType.INSTANCE)
                 return f"{instance}.{config['database']}"
             if entry_type == EntryType.DB_SCHEMA:
                 database = create_fqn(config, EntryType.DATABASE)
                 return f"{database}.{schema_name}"
             if entry_type in [EntryType.TABLE, EntryType.VIEW]:
                 database = create_fqn(config, EntryType.DATABASE)
                 return f"{database}.{schema_name}.{table_name}"
             return ""
         
         
         def create_name(config: Dict[str, str], entry_type: EntryType,
                         schema_name: str = "", table_name: str = ""):
             """Creates a Dataplex v2 hierarchy name."""
             if FORBIDDEN_SYMBOL in schema_name:
                 schema_name = schema_name.replace(FORBIDDEN_SYMBOL, ALLOWED_SYMBOL)
             if entry_type == EntryType.INSTANCE:
                 name_prefix = (
                     f"projects/{config['target_project_id']}/"
                     f"locations/{config['target_location_id']}/"
                     f"entryGroups/{config['target_entry_group_id']}/"
                     f"entries/"
                 )
                 return name_prefix + config["host_port"].replace(":", "@")
             if entry_type == EntryType.DATABASE:
                 instance = create_name(config, EntryType.INSTANCE)
                 return f"{instance}/databases/{config['database']}"
             if entry_type == EntryType.DB_SCHEMA:
                 database = create_name(config, EntryType.DATABASE)
                 return f"{database}/database_schemas/{schema_name}"
             if entry_type == EntryType.TABLE:
                 db_schema = create_name(config, EntryType.DB_SCHEMA, schema_name)
                 return f"{db_schema}/tables/{table_name}"
             if entry_type == EntryType.VIEW:
                 db_schema = create_name(config, EntryType.DB_SCHEMA, schema_name)
                 return f"{db_schema}/views/{table_name}"
             return ""
         
         
         def create_parent_name(config: Dict[str, str], entry_type: EntryType,
                                parent_name: str = ""):
             """Generates a Dataplex v2 name of the parent."""
             if entry_type == EntryType.DATABASE:
                 return create_name(config, EntryType.INSTANCE)
             if entry_type == EntryType.DB_SCHEMA:
                 return create_name(config, EntryType.DATABASE)
             if entry_type == EntryType.TABLE:
                 return create_name(config, EntryType.DB_SCHEMA, parent_name)
             return ""
         
         
         def create_entry_aspect_name(config: Dict[str, str], entry_type: EntryType):
             """Generates an entry aspect name."""
             last_segment = entry_type.value.split("/")[-1]
             return f"{config['target_project_id']}.{config['target_location_id']}.{last_segment}"
         

Because the `name_builder.py` file is used for both the Python core code and the PySpark core code, we recommend that you write the methods as pure functions, instead of as members of a class.

  10. Update the `src/top_entry_builder.py` file with code to fill the top-level entries with data.
         
         """Non-Spark approach for building the entries."""
         import dataclasses
         import json
         from typing import List, Dict
         
         import proto
         from google.cloud import [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest)
         
         from src.constants import [EntryType](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.EntryType.html)
         from src import name_builder as nb
         
         
         @dataclasses.dataclass(slots=True)
         class ImportItem:
             """A template class for Import API."""
         
             entry: [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[Entry](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.Entry.html) = dataclasses.field(default_factory=[dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[Entry](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.Entry.html))
             aspect_keys: List[str] = dataclasses.field(default_factory=list)
             update_mask: List[str] = dataclasses.field(default_factory=list)
         
         
         def _dict_factory(data: object):
             """Factory function required for converting Entry dataclass to dict."""
         
             def convert(obj: object):
                 if isinstance(obj, proto.Message):
                     return proto.Message.to_dict(obj)
                 return obj
         
             return dict((k, convert(v)) for k, v in data)
         
         
         def _create_entry(config: Dict[str, str], entry_type: EntryType):
             """Creates an entry based on a Dataplex library."""
             entry = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[Entry](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.Entry.html)()
             entry.name = nb.create_name(config, entry_type)
             entry.entry_type = entry_type.value.format(
                 project=config["target_project_id"], location=config["target_location_id"]
             )
             entry.fully_qualified_name = nb.create_fqn(config, entry_type)
             entry.parent_entry = nb.create_parent_name(config, entry_type)
         
             aspect_key = nb.create_entry_aspect_name(config, entry_type)
         
             # Add mandatory aspect
             entry_aspect = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[Aspect](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.Aspect.html)()
             entry_aspect.aspect_type = aspect_key
             entry_aspect.data = {}
             entry.aspects[aspect_key] = entry_aspect
         
             return entry
         
         
         def _entry_to_import_item(entry: [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[Entry](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.Entry.html)):
             """Packs entry to import item, accepted by the API,"""
             import_item = ImportItem()
             import_item.entry = entry
             import_item.aspect_keys = list(entry.aspects.keys())
             import_item.update_mask = "aspects"
         
             return import_item
         
         
         def create(config, entry_type: EntryType):
             """Creates an entry, packs it to Import Item and converts to json."""
             import_item = _entry_to_import_item(_create_entry(config, entry_type))
             return json.dumps(dataclasses.asdict(import_item, dict_factory=_dict_factory))
         

  11. Update the `src/bootstrap.py` file with code to generate the metadata import file and run the connector.
         
         """The entrypoint of a pipeline."""
         from typing import Dict
         
         from src.constants import EntryType
         from src import cmd_reader
         from src import secret_manager
         from src import entry_builder
         from src import gcs_uploader
         from src import top_entry_builder
         from src.oracle_connector import OracleConnector
         
         
         FILENAME = "output.jsonl"
         
         
         def write_jsonl(output_file, json_strings):
             """Writes a list of string to the file in JSONL format."""
         
             # For simplicity, dataset is written into the one file. But it is not
             # mandatory, and the order doesn't matter for Import API.
             # The PySpark itself could dump entries into many smaller JSONL files.
             # Due to performance, it's recommended to dump to many smaller files.
             for string in json_strings:
                 output_file.write(string + "\n")
         
         
         def process_dataset(
             connector: OracleConnector,
             config: Dict[str, str],
             schema_name: str,
             entry_type: EntryType,
         ):
             """Builds dataset and converts it to jsonl."""
             df_raw = connector.get_dataset(schema_name, entry_type)
             df = entry_builder.build_dataset(config, df_raw, schema_name, entry_type)
             return df.toJSON().collect()
         
         
         def run():
             """Runs a pipeline."""
             config = cmd_reader.read_args()
             config["password"] = secret_manager.get_password(config["password_secret"])
             connector = OracleConnector(config)
         
             with open(FILENAME, "w", encoding="utf-8") as file:
                 # Write top entries that don't require connection to the database
                 file.writelines(top_entry_builder.create(config, EntryType.INSTANCE))
                 file.writelines("\n")
                 file.writelines(top_entry_builder.create(config, EntryType.DATABASE))
         
                 # Get schemas, write them and collect to the list
                 df_raw_schemas = connector.get_db_schemas()
                 schemas = [schema.USERNAME for schema in df_raw_schemas.select("USERNAME").collect()]
                 schemas_json = entry_builder.build_schemas(config, df_raw_schemas).toJSON().collect()
         
                 write_jsonl(file, schemas_json)
         
                 # Ingest tables and views for every schema in a list
                 for schema in schemas:
                     print(f"Processing tables for {schema}")
                     tables_json = process_dataset(connector, config, schema, EntryType.TABLE)
                     write_jsonl(file, tables_json)
                     print(f"Processing views for {schema}")
                     views_json = process_dataset(connector, config, schema, EntryType.VIEW)
                     write_jsonl(file, views_json)
         
             gcs_uploader.upload(config, FILENAME)
         

  12. Run the code locally.

A metadata import file named `output.jsonl` is returned. The file has two lines, each representing an import item. The managed connectivity pipeline reads this file when running the metadata import job.

  13. Optional: Extend the previous example to use the Knowledge Catalog client library classes to create import items for tables, schemas, and views. You can also run the Python example on Managed Service for Apache Spark.

We recommend that you create a connector that uses Spark (and runs on Managed Service for Apache Spark), because it can improve the performance of your connector.




## Create a PySpark connector

This example is based on the [PySpark DataFrame API](https://spark.apache.org/docs/latest/api/python/getting_started/quickstart_df.html). You can install PySpark SQL and run it locally before running on Managed Service for Apache Spark. If you install and run PySpark locally, install the PySpark library by using pip, but you don't need to install a local Spark cluster.

For performance reasons, this example doesn't use predefined classes from the PySpark library. Instead, the example creates DataFrames, converts the DataFrames into JSON entries, and then writes the output into a metadata import file in JSON Lines format that can be imported into Knowledge Catalog.

To build a connector using PySpark, do the following:

  1. Clone the [`cloud-dataplex` repository](https://github.com/GoogleCloudPlatform/cloud-dataplex).

  2. Install PySpark:
         
         pip install pyspark
         

  3. Install requirements:
         
         pip install -r requirements.txt
         

The following requirements are installed:
         
         google-cloud-dataplex==2.2.2
         google-cloud-storage
         google-cloud-secret-manager
         

  4. Update the `oracle_connector.py` file with code to read data from an Oracle data source and return DataFrames.
         
         """Reads Oracle using PySpark."""
         from typing import Dict
         from pyspark.sql import SparkSession, DataFrame
         
         from src.constants import EntryType
         
         
         SPARK_JAR_PATH = "/opt/spark/jars/ojdbc11.jar"
         
         
         class OracleConnector:
             """Reads data from Oracle and returns Spark Dataframes."""
         
             def __init__(self, config: Dict[str, str]):
                 # PySpark entrypoint
                 self._spark = SparkSession.builder.appName("OracleIngestor") \
                     .config("spark.jars", SPARK_JAR_PATH) \
                     .getOrCreate()
         
                 self._config = config
                 self._url = f"jdbc:oracle:thin:@{config['host_port']}:{config['database']}"
         
             def _execute(self, query: str) -> DataFrame:
                 """A generic method to execute any query."""
                 return self._spark.read.format("jdbc") \
                     .option("driver", "oracle.jdbc.OracleDriver") \
                     .option("url", self._url) \
                     .option("query", query) \
                     .option("user", self._config["user"]) \
                     .option("password", self._config["password"]) \
                     .load()
         
             def get_db_schemas(self) -> DataFrame:
                 """In Oracle, schemas are usernames."""
                 query = "SELECT username FROM dba_users"
                 return self._execute(query)
         
             def _get_columns(self, schema_name: str, object_type: str) -> str:
                 """Gets a list of columns in tables or views in a batch."""
                 # Every line here is a column that belongs to the table or to the view.
                 # This SQL gets data from ALL the tables in a given schema.
                 return (f"SELECT col.TABLE_NAME, col.COLUMN_NAME, "
                         f"col.DATA_TYPE, col.NULLABLE "
                         f"FROM all_tab_columns col "
                         f"INNER JOIN DBA_OBJECTS tab "
                         f"ON tab.OBJECT_NAME = col.TABLE_NAME "
                         f"WHERE tab.OWNER = '{schema_name}' "
                         f"AND tab.OBJECT_TYPE = '{object_type}'")
         
             def get_dataset(self, schema_name: str, entry_type: EntryType):
                 """Gets data for a table or a view."""
                 # Dataset means that these entities can contain end user data.
                 short_type = entry_type.name  # table or view, or the title of enum value
                 query = self._get_columns(schema_name, short_type)
                 return self._execute(query)
         

Add SQL queries to return the metadata that you want to import. The queries need to return the following information:

     * Database schemas
     * Tables that belong to these schemas
     * Columns that belong to these tables, including the column name, column data type, and whether the column is nullable or required

All of the columns of all the tables and views are stored in the same system table. You can select columns with the `_get_columns` method. Depending on the parameters that you provide, you can select columns for the tables or for the views separately.

Note the following:

     * In Oracle, a database schema is owned by a database user and has the same name as that user.
     * Schema objects are logical structures that are created by users. Objects such as tables or indexes can hold data, and objects such as views or synonyms consist of only a definition.
     * The `ojdbc11.jar` file contains the [Oracle JDBC driver](https://www.oracle.com/database/technologies/appdev/jdbc-downloads.html).
  5. Update the `src/entry_builder.py` file with shared methods for applying Spark transformations.
         
         """Creates entries with PySpark."""
         import pyspark.sql.functions as F
         from pyspark.sql.types import StringType
         
         from src.constants import EntryType, SOURCE_TYPE
         from src import name_builder as nb
         
         
         @F.udf(returnType=StringType())
         def choose_metadata_type_udf(data_type: str):
             """Choose the metadata type based on Oracle native type."""
             if data_type.startswith("NUMBER") or data_type in ["FLOAT", "LONG"]:
                 return "NUMBER"
             if data_type.startswith("VARCHAR") or data_type.startswith("NVARCHAR2"):
                 return "STRING"
             if data_type == "DATE":
                 return "DATETIME"
             return "OTHER"
         
         
         def create_entry_source(column):
             """Create Entry Source segment."""
             return F.named_struct(F.lit("display_name"),
                                   column,
                                   F.lit("system"),
                                   F.lit(SOURCE_TYPE))
         
         
         def create_entry_aspect(entry_aspect_name):
             """Create aspect with general information (usually it is empty)."""
             return F.create_map(
                 F.lit(entry_aspect_name),
                 F.named_struct(
                     F.lit("aspect_type"),
                     F.lit(entry_aspect_name),
                     F.lit("data"),
                     F.create_map()
                     )
                 )
         
         
         def convert_to_import_items(df, aspect_keys):
             """Convert entries to import items."""
             entry_columns = ["name", "fully_qualified_name", "parent_entry",
                              "entry_source", "aspects", "entry_type"]
         
             # Puts entry to "entry" key, a list of keys from aspects in "aspects_keys"
             # and "aspects" string in "update_mask"
             return df.withColumn("entry", F.struct(entry_columns)) \
               .withColumn("aspect_keys", F.array([F.lit(key) for key in aspect_keys])) \
               .withColumn("update_mask", F.array(F.lit("aspects"))) \
               .drop(*entry_columns)
         
         
         def build_schemas(config, df_raw_schemas):
             """Create a dataframe with database schemas from the list of usernames.
             Args:
                 df_raw_schemas - a dataframe with only one column called USERNAME
             Returns:
                 A dataframe with Dataplex-readable schemas.
             """
             entry_type = EntryType.DB_SCHEMA
             entry_aspect_name = nb.create_entry_aspect_name(config, entry_type)
         
             # For schema, parent name is the name of the database
             parent_name =  nb.create_parent_name(config, entry_type)
         
             # Create user-defined function.
             create_name_udf = F.udf(lambda x: nb.create_name(config, entry_type, x),
                                     StringType())
             create_fqn_udf = F.udf(lambda x: nb.create_fqn(config, entry_type, x),
                                    StringType())
         
             # Fills the missed project and location into the entry type string
             full_entry_type = entry_type.value.format(
                 project=config["target_project_id"],
                 location=config["target_location_id"])
         
             # Converts a list of schema names to the Dataplex-compatible form
             column = F.col("USERNAME")
             df = df_raw_schemas.withColumn("name", create_name_udf(column)) \
               .withColumn("fully_qualified_name", create_fqn_udf(column)) \
               .withColumn("parent_entry", F.lit(parent_name)) \
               .withColumn("entry_type", F.lit(full_entry_type)) \
               .withColumn("entry_source", create_entry_source(column)) \
               .withColumn("aspects", create_entry_aspect(entry_aspect_name)) \
             .drop(column)
         
             df = convert_to_import_items(df, [entry_aspect_name])
             return df
         
         
         def build_dataset(config, df_raw, db_schema, entry_type):
             """Build table entries from a flat list of columns.
             Args:
                 df_raw - a plain dataframe with TABLE_NAME, COLUMN_NAME, DATA_TYPE,
                          and NULLABLE columns
                 db_schema - parent database schema
                 entry_type - entry type: table or view
             Returns:
                 A dataframe with Dataplex-readable data of tables of views.
             """
             schema_key = "dataplex-types.global.schema"
         
             # The transformation below does the following
             # 1. Alters NULLABLE content from Y/N to NULLABLE/REQUIRED
             # 2. Renames NULLABLE to mode
             # 3. Renames DATA_TYPE to dataType
             # 4. Creates metadataType column based on dataType column
             # 5. Renames COLUMN_NAME to name
             df = df_raw \
               .withColumn("mode", F.when(F.col("NULLABLE") == 'Y', "NULLABLE").otherwise("REQUIRED")) \
               .drop("NULLABLE") \
               .withColumnRenamed("DATA_TYPE", "dataType") \
               .withColumn("metadataType", choose_metadata_type_udf("dataType")) \
               .withColumnRenamed("COLUMN_NAME", "name")
         
             # The transformation below aggregate fields, denormalizing the table
             # TABLE_NAME becomes top-level filed, and the rest is put into
             # the array type called "fields"
             aspect_columns = ["name", "mode", "dataType", "metadataType"]
             df = df.withColumn("columns", F.struct(aspect_columns))\
               .groupby('TABLE_NAME') \
               .agg(F.collect_list("columns").alias("fields"))
         
             # Create nested structured called aspects.
             # Fields are becoming a part of a `schema` struct
             # There is also an entry_aspect that is repeats entry_type as aspect_type
             entry_aspect_name = nb.create_entry_aspect_name(config, entry_type)
             df = df.withColumn("schema",
                                F.create_map(F.lit(schema_key),
                                             F.named_struct(
                                                 F.lit("aspect_type"),
                                                 F.lit(schema_key),
                                                 F.lit("data"),
                                                 F.create_map(F.lit("fields"),
                                                              F.col("fields")))
                                             )
                                )\
               .withColumn("entry_aspect", create_entry_aspect(entry_aspect_name)) \
             .drop("fields")
         
             # Merge separate aspect columns into the one map called 'aspects'
             df = df.select(F.col("TABLE_NAME"),
                            F.map_concat("schema", "entry_aspect").alias("aspects"))
         
             # Define user-defined functions to fill the general information
             # and hierarchy names
             create_name_udf = F.udf(lambda x: nb.create_name(config, entry_type,
                                                              db_schema, x),
                                     StringType())
         
             create_fqn_udf = F.udf(lambda x: nb.create_fqn(config, entry_type,
                                                            db_schema, x), StringType())
         
             parent_name = nb.create_parent_name(config, entry_type, db_schema)
             full_entry_type = entry_type.value.format(
                 project=config["target_project_id"],
                 location=config["target_location_id"])
         
             # Fill the top-level fields
             column = F.col("TABLE_NAME")
             df = df.withColumn("name", create_name_udf(column)) \
               .withColumn("fully_qualified_name", create_fqn_udf(column)) \
               .withColumn("entry_type", F.lit(full_entry_type)) \
               .withColumn("parent_entry", F.lit(parent_name)) \
               .withColumn("entry_source", create_entry_source(column)) \
             .drop(column)
         
             df = convert_to_import_items(df, [schema_key, entry_aspect_name])
             return df
         

Note the following:

     * The methods build the metadata resources that the connector creates for your Oracle resources. Use the conventions that are described in the Example metadata resources for an Oracle source section of this document.
     * The `convert_to_import_items` method applies to schemas, tables, and views. Ensure that the output of the connector is one or more import items that can be processed by the [`metadataJobs.create` method](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.metadataJobs/create), not individual entries.
     * Even in a view, the column is called `TABLE_NAME`.
  6. Update the `bootstrap.py` file with code to generate the metadata import file and run the connector.
         
         """The entrypoint of a pipeline."""
         from typing import Dict
         
         from src.constants import EntryType
         from src import cmd_reader
         from src import secret_manager
         from src import entry_builder
         from src import gcs_uploader
         from src import top_entry_builder
         from src.oracle_connector import OracleConnector
         
         
         FILENAME = "output.jsonl"
         
         
         def write_jsonl(output_file, json_strings):
             """Writes a list of string to the file in JSONL format."""
         
             # For simplicity, dataset is written into the one file. But it is not
             # mandatory, and the order doesn't matter for Import API.
             # The PySpark itself could dump entries into many smaller JSONL files.
             # Due to performance, it's recommended to dump to many smaller files.
             for string in json_strings:
                 output_file.write(string + "\n")
         
         
         def process_dataset(
             connector: OracleConnector,
             config: Dict[str, str],
             schema_name: str,
             entry_type: EntryType,
         ):
             """Builds dataset and converts it to jsonl."""
             df_raw = connector.get_dataset(schema_name, entry_type)
             df = entry_builder.build_dataset(config, df_raw, schema_name, entry_type)
             return df.toJSON().collect()
         
         
         def run():
             """Runs a pipeline."""
             config = cmd_reader.read_args()
             config["password"] = secret_manager.get_password(config["password_secret"])
             connector = OracleConnector(config)
         
             with open(FILENAME, "w", encoding="utf-8") as file:
                 # Write top entries that don't require connection to the database
                 file.writelines(top_entry_builder.create(config, EntryType.INSTANCE))
                 file.writelines("\n")
                 file.writelines(top_entry_builder.create(config, EntryType.DATABASE))
         
                 # Get schemas, write them and collect to the list
                 df_raw_schemas = connector.get_db_schemas()
                 schemas = [schema.USERNAME for schema in df_raw_schemas.select("USERNAME").collect()]
                 schemas_json = entry_builder.build_schemas(config, df_raw_schemas).toJSON().collect()
         
                 write_jsonl(file, schemas_json)
         
                 # Ingest tables and views for every schema in a list
                 for schema in schemas:
                     print(f"Processing tables for {schema}")
                     tables_json = process_dataset(connector, config, schema, EntryType.TABLE)
                     write_jsonl(file, tables_json)
                     print(f"Processing views for {schema}")
                     views_json = process_dataset(connector, config, schema, EntryType.VIEW)
                     write_jsonl(file, views_json)
         
             gcs_uploader.upload(config, FILENAME)
         

This example saves the metadata import file as a single JSON Lines file. You can use PySpark tools such as the `DataFrameWriter` class to output batches of JSON in parallel.

The connector can write entries to the metadata import file in any order.

  7. Update the `gcs_uploader.py` file with code to upload the metadata import file to a Cloud Storage bucket.
         
         """Sends files to GCP storage."""
         from typing import Dict
         from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
         
         
         def upload(config: Dict[str, str], filename: str):
             """Uploads a file to GCP bucket."""
             client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
             bucket = client.[get_bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_get_bucket)(config["output_bucket"])
             folder = config["output_folder"]
         
             blob = bucket.blob(f"{folder}/{filename}")
             blob.[upload_from_filename](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_filename)(filename)
         

  8. Build the connector image.

If your connector contains multiple files, or if you want to use libraries that aren't included in the default Docker image, you must use a [custom container](https://docs.cloud.google.com/dataproc-serverless/docs/guides/custom-containers). Managed Service for Apache Spark runs workloads within Docker containers. Create a custom Docker image of the connector and store the image in [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/overview). Managed Service for Apache Spark reads the image from Artifact Registry.

**Note:** If the connector contains only one file, you can send the job to Managed Service for Apache Spark directly. Skip this step.

     1. Create a Dockerfile:
            
            FROM debian:11-slim
            
            ENV DEBIAN_FRONTEND=noninteractive
            
            RUN apt update && apt install -y procps tini
            RUN apt install -y wget
            
            ENV SPARK_EXTRA_JARS_DIR=/opt/spark/jars/
            RUN mkdir -p "${SPARK_EXTRA_JARS_DIR}"
            COPY ojdbc11.jar "${SPARK_EXTRA_JARS_DIR}"
            
            ENV CONDA_HOME=/opt/miniconda3
            ENV PYSPARK_PYTHON=${CONDA_HOME}/bin/python
            ENV PATH=${CONDA_HOME}/bin:${PATH}
            RUN wget https://repo.anaconda.com/miniconda/Miniconda3-py311_24.9.2-0-Linux-x86_64.sh
            
            RUN bash Miniconda3-py310_23.3.1-0-Linux-x86_64.sh -b -p /opt/miniconda3 \
              && ${CONDA_HOME}/bin/conda config --system --set always_yes True \
              && ${CONDA_HOME}/bin/conda config --system --set auto_update_conda False \
              && ${CONDA_HOME}/bin/conda config --system --prepend channels conda-forge \
              && ${CONDA_HOME}/bin/conda config --system --set channel_priority strict
            
            RUN ${CONDA_HOME}/bin/conda install mamba -n base -c conda-forge \
                && ${CONDA_HOME}/bin/mamba install \
                  conda \
                  google-cloud-dataproc \
                  google-cloud-logging \
                  google-cloud-monitoring \
                  google-cloud-storage
            
            RUN apt update && apt install -y git
            COPY requirements.txt .
            RUN python -m pip install -r requirements.txt
            
            ENV PYTHONPATH=/opt/python/packages
            RUN mkdir -p "${PYTHONPATH}/src/"
            COPY src/ "${PYTHONPATH}/src/"
            COPY main.py .
            
            RUN groupadd -g 1099 spark
            RUN useradd -u 1099 -g 1099 -d /home/spark -m spark
            USER spark

Use Conda as your package manager. Managed Service for Apache Spark mounts `pyspark` into the container at runtime, so you don't need to install PySpark dependencies in your custom container image.

     2. Build the custom container image and push it to Artifact Registry.
            
            #!/bin/bash
            
            IMAGE=oracle-pyspark:0.0.1
            PROJECT=<PROJECT_ID>
            
            
            REPO_IMAGE=us-central1-docker.pkg.dev/${PROJECT}/docker-repo/oracle-pyspark
            
            docker build -t "${IMAGE}" .
            
            # Tag and push to GCP container registry
            gcloud config set project ${PROJECT}
            gcloud auth configure-docker us-central1-docker.pkg.dev
            docker tag "${IMAGE}" "${REPO_IMAGE}"
            docker push "${REPO_IMAGE}"
            

Because one image can have multiple names, you can use the Docker tag to assign an alias to the image.

  9. Run the connector on Managed Service for Apache Spark. To submit a PySpark batch job using the custom container image, run the [`gcloud dataproc batches submit pyspark` command](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/pyspark).
         
         gcloud dataproc batches submit pyspark main.py --project=PROJECT \
             --region=REGION --batch=BATCH_ID \
             --container-image=CUSTOM_CONTAINER_IMAGE \
             --service-account=SERVICE_ACCOUNT_NAME \
             --jars=PATH_TO_JAR_FILES \
             --properties=PYSPARK_PROPERTIES \
             -- PIPELINE_ARGUMENTS
         

Note the following:

     * The JAR files are drivers for Spark. To read from Oracle, MySQL, or Postgres, you must provide Apache Spark a specific package. The package can be located in Cloud Storage or inside the container. If the JAR file is inside the container, the path is similar to `file:///path/to/file/driver.jar`. In this example, the path to the JAR file is `/opt/spark/jars/`.
     * PIPELINE_ARGUMENTS are the command-line arguments for the connector.

The connector extracts metadata from the Oracle database, generates a metadata import file, and saves the metadata import file to a Cloud Storage bucket.

  10. To manually import the metadata in the metadata import file into Knowledge Catalog, run a metadata job. Use the [`metadataJobs.create` method](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.metadataJobs/create).

     1. In the command line, add environment variables and create an alias for the curl command.
            
            PROJECT_ID=PROJECT
            LOCATION_ID=LOCATION
            DATAPLEX_API=dataplex.googleapis.com/v1/projects/$PROJECT_ID/locations/$LOCATION_ID
            alias gcurl='curl -H "Authorization: Bearer $(gcloud auth print-access-token)" -H "Content-Type: application/json"'
            

     2. Call the API method, passing the entry types and aspect types that you want to import.
            
            gcurl https://${DATAPLEX_API}/metadataJobs?metadata_job_id="JOB_ID" -d "$(cat <<EOF
            {
              "type": "IMPORT",
              "import_spec": {
                "source_storage_uri": "gs://BUCKET/FOLDER/",
                "entry_sync_mode": "FULL",
                "aspect_sync_mode": "INCREMENTAL",
                "scope": {
                  "entry_groups": ["projects/PROJECT/locations/LOCATION/entryGroups/ENTRY_GROUP_ID"],
                  "entry_types": [
                    "projects/PROJECT/locations/LOCATION/entryTypes/oracle-instance",
                    "projects/PROJECT/locations/LOCATION/entryTypes/oracle-database",
                    "projects/PROJECT/locations/LOCATION/entryTypes/oracle-schema",
                    "projects/PROJECT/locations/LOCATION/entryTypes/oracle-table",
                    "projects/PROJECT/locations/LOCATION/entryTypes/oracle-view"],
            
                  "aspect_types": [
                    "projects/PROJECT/locations/LOCATION/aspectTypes/oracle-instance",
                    "projects/dataplex-types/locations/global/aspectTypes/schema",
                    "projects/PROJECT/locations/LOCATION/aspectTypes/oracle-database",
                    "projects/PROJECT/locations/LOCATION/aspectTypes/oracle-schema",
                    "projects/PROJECT/locations/LOCATION/aspectTypes/oracle-table",
                    "projects/PROJECT/locations/LOCATION/aspectTypes/oracle-view"],
                  },
                },
              }
            EOF
            )"
            

The `schema` aspect type is a global aspect type that is defined by Knowledge Catalog.

Note that the format that you use for aspect type names when calling the API method is different from the format that you use in the connector code.

     3. Optional: Use Cloud Logging to view logs for the metadata job. For more information, see [Monitor Knowledge Catalog logs](https://docs.cloud.google.com/knowledge-catalog/docs/logging).




## Set up pipeline orchestration

The previous sections showed how to build an example connector and run the connector manually.

In a production environment, you run the connector as part of a managed connectivity pipeline, by using an orchestration platform like Workflows.

  1. To run a managed connectivity pipeline with the example connector, follow the [steps to import metadata using Workflows](https://docs.cloud.google.com/knowledge-catalog/docs/import-using-workflows-custom-source). Do these things:

     * Create the workflow in the same Google Cloud location as the connector.
     * In the workflow definition file, update the `submit_pyspark_extract_job` function with the following code to extract data from the Oracle database using the connector that you created.
           
           - submit_pyspark_extract_job:
               call: http.post
               args:
                 url: ${"https://dataproc.googleapis.com/v1/projects/" + args.TARGET_PROJECT_ID + "/locations/" + args.CLOUD_REGION + "/batches"}
                 auth:
                   type: OAuth2
                   scopes: "https://www.googleapis.com/auth/cloud-platform"
                 headers:
                   Content-Type: "application/json"
                 query:
                   batchId: ${WORKFLOW_ID}
                 body:
                   pysparkBatch:
                     mainPythonFileUri: file:///main.py
                     jars: file:///opt/spark/jars/ojdbc11.jar
                     args:
                       - ${"--host_port=" + args.ORACLE_HOST_PORT}
                       - ${"--user=" + args.ORACLE_USER}
                       - ${"--password=" + args.ORACLE_PASSWORD}
                       - ${"--database=" + args.ORACLE_DATABASE}
                       - ${"--project=" + args.TARGET_PROJECT_ID}
                       - ${"--location=" + args.CLOUD_REGION}
                       - ${"--entry_group=" + args.TARGET_ENTRY_GROUP_ID}
                       - ${"--bucket=" + args.CLOUD_STORAGE_BUCKET_ID}
                       - ${"--folder=" + WORKFLOW_ID}
                   runtimeConfig:
                     version: "2.0"
                     containerImage: "us-central1-docker.pkg.dev/PROJECT/REPOSITORY/oracle-pyspark"
                   environmentConfig:
                     executionConfig:
                         serviceAccount: ${args.SERVICE_ACCOUNT}
               result: RESPONSE_MESSAGE
           

     * In the workflow definition file, update the `submit_import_job` function with the following code to import the entries. The function calls the `metadataJobs.create` API method to run a metadata import job.
           
           - submit_import_job:
               call: http.post
               args:
                 url: ${"https://dataplex.googleapis.com/v1/projects/" + args.TARGET_PROJECT_ID + "/locations/" + args.CLOUD_REGION + "/metadataJobs?metadata_job_id=" + WORKFLOW_ID}
                 auth:
                   type: OAuth2
                   scopes: "https://www.googleapis.com/auth/cloud-platform"
                 body:
                   type: IMPORT
                   import_spec:
                     source_storage_uri: ${"gs://" + args.CLOUD_STORAGE_BUCKET_ID + "/" + WORKFLOW_ID + "/"}
                     entry_sync_mode: FULL
                     aspect_sync_mode: INCREMENTAL
                     scope:
                       entry_groups:
                         - ${"projects/" + args.TARGET_PROJECT_ID + "/locations/" + args.CLOUD_REGION + "/entryGroups/"+args.TARGET_ENTRY_GROUP_ID}
                       entry_types:
                         -"projects/PROJECT/locations/LOCATION/entryTypes/oracle-instance"
                         -"projects/PROJECT/locations/LOCATION/entryTypes/oracle-database"
                         -"projects/PROJECT/locations/LOCATION/entryTypes/oracle-schema"
                         -"projects/PROJECT/locations/LOCATION/entryTypes/oracle-table"
                         -"projects/PROJECT/locations/LOCATION/entryTypes/oracle-view"
                       aspect_types:
                         -"projects/PROJECT/locations/LOCATION/aspectTypes/oracle-instance"
                         -"projects/dataplex-types/locations/global/aspectTypes/schema"
                         -"projects/PROJECT/locations/LOCATION/aspectTypes/oracle-database"
                         -"projects/PROJECT/locations/LOCATION/aspectTypes/oracle-schema"
                         -"projects/PROJECT/locations/LOCATION/aspectTypes/oracle-table"
                         -"projects/PROJECT/locations/LOCATION/aspectTypes/oracle-view"
               result: IMPORT_JOB_RESPONSE
           

Provide the same entry types and aspect types that you included when you called the API method manually. Note that there isn't a comma at the end of each string.

     * When you execute the workflow, provide the following runtime arguments:
           
           {
             "CLOUD_REGION": "us-central1",
             "ORACLE_USER": "system",
             "ORACLE_HOST_PORT": "x.x.x.x:1521",
             "ORACLE_DATABASE": "xe",
             "ADDITIONAL_CONNECTOR_ARGS": [],
           }
           

  2. Optional: Use Cloud Logging to view logs for the managed connectivity pipeline. The log payload includes a link to the logs for the Managed Service for Apache Spark batch job and the metadata import job, as relevant. For more information, see [View workflow logs](https://docs.cloud.google.com/workflows/docs/log-workflow#viewing-logs).

  3. Optional: To improve the security, performance, and functionality of your managed connectivity pipeline, consider doing the following things:

     1. [Use Secret Manager](https://docs.cloud.google.com/secret-manager/docs/creating-and-accessing-secrets) to store the credentials for your third-party data source.
     2. Use PySpark to write the JSON Lines output into multiple metadata import files in parallel.
     3. Use a prefix to split big files (more than 100 MB) into smaller files.
     4. Add more custom aspects that capture additional business and technical metadata from your source.



## Example metadata resources for an Oracle source

The example connector extracts metadata from an Oracle database and maps the metadata to corresponding Knowledge Catalog metadata resources.

### Hierarchy considerations

Every system in Knowledge Catalog has a root entry that is the parent entry for the system. Usually the root entry has an `instance` entry type. The following table shows the example hierarchy of entry types and aspect types for an Oracle system. For example, the `oracle-database` entry type is linked to an aspect type that is also named `oracle-database`.

Entry type ID | Description | Linked aspect type ID  
---|---|---  
`oracle-instance` | The root of the imported system. | `oracle-instance`  
`oracle-database` | The Oracle database. | `oracle-database`  
`oracle-schema` | The database schema. | `oracle-schema`  
`oracle-table` | A table. |  `oracle-table` `schema`  
`oracle-view` | A view. |  `oracle-view` `schema`  
  
The `schema` aspect type is a global aspect type that is defined by Knowledge Catalog. It contains a description of the fields in a table, view, or other entity that has columns. The `oracle-schema` custom aspect type contains the name of the Oracle database schema.

**Note:**

  * You can use a different name for the root entry if it's relevant for your system. For example, you can name the root entry for an Apache Kafka system as `cluster`.
  * Depending on the system, you might have only schemas or databases. For many relational database management systems, "schema" and "database" are synonyms. To reduce the number of entry types in the hierarchy, consider choosing one term to use for all similar resources.



### Example import item fields

The connector should use the following conventions for Oracle resources.

  * **Fully qualified names** : fully qualified names for Oracle resources use the following naming template. Forbidden characters are escaped with backticks.

Resource | Template | Example  
---|---|---  
Instance |  `SOURCE`:`ADDRESS` Use the host and port number or the domain name of the system. | `oracle:`localhost:1521`` or `oracle:`myinstance.com``  
Database | `SOURCE`:`ADDRESS`.`DATABASE` | `oracle:`localhost:1521`.xe`  
Schema | `SOURCE`:`ADDRESS`.`DATABASE`.`SCHEMA` | `oracle:`localhost:1521`.xe.sys`  
Table | `SOURCE`:`ADDRESS`.`DATABASE`.`SCHEMA`.`TABLE_NAME` | `oracle:`localhost:1521`.xe.sys.orders`  
View | `SOURCE`:`ADDRESS`.`DATABASE`.`SCHEMA`.`VIEW_NAME` | `oracle:`localhost:1521`.xe.sys.orders_view`  
  * **Entry names or entry IDs** : entries for Oracle resources use the following naming template. Forbidden characters are replaced with a permitted character. Resources use the prefix `projects/PROJECT/locations/LOCATION/entryGroups/ENTRY_GROUP/entries`.

Resource | Template | Example  
---|---|---  
Instance | `PREFIX`/`HOST_PORT` | `projects/example-project/locations/us-central1/entryGroups/oracle-prod/entries/10.1.1.1@1521`  
Database | `PREFIX`/`HOST_PORT`/databases/`DATABASE` | `projects/example-project/locations/us-central1/entryGroups/oracle-prod/entries/10.1.1.1@1521/databases/xe`  
Schema | `PREFIX`/`HOST_PORT`/databases/`DATABASE`/database_schemas/`SCHEMA` | `projects/example-project/locations/us-central1/entryGroups/oracle-prod/entries/10.1.1.1@1521/databases/xe/database_schemas/sys`  
Table | `PREFIX`/`HOST_PORT`/databases/`DATABASE`/database_schemas/`SCHEMA`/tables/`TABLE` | `projects/example-project/locations/us-central1/entryGroups/oracle-prod/entries/10.1.1.1@1521/databases/xe/database_schemas/sys/tables/orders`  
View | `PREFIX`/`HOST_PORT`/databases/`DATABASE`/database_schemas/`SCHEMA`/views/`VIEW` | `projects/example-project/locations/us-central1/entryGroups/oracle-prod/entries/10.1.1.1@1521/databases/xe/database_schemas/sys/views/orders_view`  
  * **Parent entries** : if an entry isn't a root entry for the system, the entry can have a parent entry field that describes its position in the hierarchy. The field should contain the name of the parent entry. We recommend that you generate this value.

The following table shows the parent entries for Oracle resources.

Entry | Parent entry  
---|---  
Instance | `""` (empty string)  
Database | Instance name  
Schema | Database name  
Table | Schema name  
View | Schema name  
  * **Aspect map** : the aspect map must contain at least one aspect that describes the entity to import. Here's an example aspect map for an Oracle table.
        
        "example-project.us-central1.oracle-table": {
            "aspect_type": "example-project.us-central1.oracle-table",
            "path": "",
            "data": {}
         },

You can find predefined aspect types (like `schema`) that define the table or view structure in the `dataplex-types` project, in the `global` location.

  * **Aspect keys** : aspect keys use the naming format PROJECT.LOCATION.ASPECT_TYPE. The following table shows example aspect keys for Oracle resources.

Entry | Example aspect key  
---|---  
Instance | `example-project.us-central1.oracle-instance`  
Database | `example-project.us-central1.oracle-database`  
Schema | `example-project.us-central1.oracle-schema`  
Table | `example-project.us-central1.oracle-table`  
View | `example-project.us-central1.oracle-view`  



## What's next

  * [Import metadata using Workflows](https://docs.cloud.google.com/knowledge-catalog/docs/import-using-workflows-custom-source)
  * [About metadata management in Knowledge Catalog](https://docs.cloud.google.com/knowledge-catalog/docs/metadata-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
