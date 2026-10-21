---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/metastore/services/migrations/start/
title: gcloud alpha metastore services migrations start \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:10:55.861307+00:00
---

# gcloud alpha metastore services migrations start  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/metastore/services/migrations/start/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha metastore services migrations start Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha metastore services migrations start - start the migration from a Dataproc Metastore service to Lakehouse runtime catalog(s)
SYNOPSIS
    

`gcloud alpha metastore services migrations start` (`SERVICE` : `--location`=`LOCATION`) [`--async`] [`--conflict-policy`=`CONFLICT_POLICY`] [`--dry-run`] [`--migration-execution-id`=`MIGRATION_EXECUTION_ID`] [`--mode`=`MODE`; default="backfill"] [`--report-path`=`REPORT_PATH`] [`--hive-catalog`=`HIVE_CATALOG` : `--hive-databases`=[`HIVE_DATABASES`,…]] [`--iceberg-catalog`=`ICEBERG_CATALOG` : `--iceberg-namespaces`=[`ICEBERG_NAMESPACES`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Start the migration from a Dataproc Metastore service to Lakehouse runtime catalog(s). 

If run asynchronously with `--async`, exits after printing the operation name that can be used to poll the status of the migration operation via: 
    
    
    gcloud metastore operations describe

EXAMPLES
     To start a one-shot backfill migration for service `my-service` to a target Hive catalog: 
    
    
    gcloud alpha metastore services migrations start my-service --location=us-central1 --mode=backfill --hive-catalog=projects/my-project/catalogs/my-hive-catalog

To start a migration with specific Hive databases and Iceberg namespaces: 
    
    
    gcloud alpha metastore services migrations start my-service --location=us-central1 --mode=backfill --hive-catalog=projects/my-project/catalogs/my-hive-catalog --hive-databases=db1,db2 --iceberg-catalog=projects/my-project/catalogs/my-iceberg-catalog --iceberg-namespaces=ns1,ns2

To run a dry-run migration without applying changes: 
    
    
    gcloud alpha metastore services migrations start my-service --location=us-central1 --dry-run --hive-catalog=projects/my-project/catalogs/my-hive-catalog

POSITIONAL ARGUMENTS
    

Service resource - Dataproc Metastore service to start the migration on. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `service` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`SERVICE`
     ID of the service or fully qualified identifier for the service. 

To set the `service` attribute: 

  * provide the argument `service` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location of the Dataproc Metastore service. 

If not specified, will use `default` metastore/location. To set the `location` attribute: 

  * provide the argument `service` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `metastore/location`. 


FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--conflict-policy`=`CONFLICT_POLICY`
     Policy to handle conflicts when migrating resources, defaults to SKIP if not specified. `CONFLICT_POLICY` must be one of: 

`overwrite`
     Update resources that already exist in the target catalog. 
`skip`
     Skip migrating resources that already exist in the target catalog. 
`--dry-run`
     If true, performs discovery of requested resources and analysis against the target catalog to come up with a plan for each resource (e.g. Create, Update, Skip, etc.). No metadata is actually migrated. 
`--migration-execution-id`=`MIGRATION_EXECUTION_ID`
     ID to use for the migration execution, which will become the final component of the migration execution's resource name. If not specified, a UUID will be generated. 

This value must be between 2 and 63 characters long inclusive, begin with a letter, end with a letter or number, and valid characters are [a-z0-9-]. 

`--mode`=`MODE`; default="backfill"
     Execution mode of the migration. `MODE` must be one of: 

`backfill`
     Performs the metadata migration of requested resources. The migration completes once the backfill is finished. 
`incremental-sync`
     Performs the initial backfill, then transitions to an incremental synchronization state to replicate ongoing source writes. Requires an explicit CompleteMigration or CancelMigration call to end the migration. Note: Supported only for Iceberg migrations. 
`--report-path`=`REPORT_PATH`
     Cloud Storage path where the backfill / dry run report should be written. If not provided, the report will be generated in the service's artifacts bucket. Format: "gs://path/to/folder". 
Configuration for migrating Hive tables to a BigLake Hive catalog. 
`--hive-catalog`=`HIVE_CATALOG`
     Target catalog for migrated databases and tables. Format: "projects/{project_id_or_number}/catalogs/{catalog_id}" 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--hive-databases`=[`HIVE_DATABASES`,…]
     Comma-separated list of databases to migrate to the Hive catalog. Defaults to `*` (migrate all databases). Note: If Iceberg tables exist in these databases, they will only be migrated if `--iceberg-catalog` is also specified. 
Configuration for migrating Iceberg tables to a BigLake Iceberg REST catalog. 
`--iceberg-catalog`=`ICEBERG_CATALOG`
     Target catalog for migrated Iceberg metadata. Format: "projects/{project_id_or_number}/catalogs/{catalog_id}" 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--iceberg-namespaces`=[`ICEBERG_NAMESPACES`,…]
     Comma-separated list of namespaces to migrate to the Iceberg REST catalog. Defaults to `*` (migrate all namespaces). Note: If Hive tables exist in these namespaces, they will only be migrated if `--hive-catalog` is also specified. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `metastore/v1alpha` API. The full documentation for this API can be found at: <https://cloud.google.com/dataproc-metastore/docs>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud metastore services migrations start](https://docs.cloud.google.com/sdk/gcloud/reference/metastore/services/migrations/start)
    
    
    [gcloud beta metastore services migrations start](https://docs.cloud.google.com/sdk/gcloud/reference/beta/metastore/services/migrations/start)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-09 UTC."],[],[]] 
