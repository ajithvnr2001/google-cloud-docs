---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataplex/metadata-jobs/create/
title: gcloud alpha dataplex metadata-jobs create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:17:50.082505+00:00
---

# gcloud alpha dataplex metadata-jobs create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataplex/metadata-jobs/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha dataplex metadata-jobs create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha dataplex metadata-jobs create - create a Dataplex Metadata Job 
SYNOPSIS
    

`gcloud alpha dataplex metadata-jobs create` [[`METADATA_JOB`] `--location`=`LOCATION`] `--type`=`TYPE` (`--export-output-path`=`EXPORT_OUTPUT_PATH` ((`--export-entry-groups`=[`EXPORT_ENTRY_GROUPS`,…] | `--export-organization-level`=`EXPORT_ORGANIZATION_LEVEL` | `--export-projects`=[`EXPORT_PROJECTS`,…]) : `--export-aspect-types`=[`EXPORT_ASPECT_TYPES`,…] `--export-entry-types`=[`EXPORT_ENTRY_TYPES`,…]) | [`--import-aspect-sync-mode`=`IMPORT_ASPECT_SYNC_MODE` `--import-entry-sync-mode`=`IMPORT_ENTRY_SYNC_MODE` `--import-source-storage-uri`=`IMPORT_SOURCE_STORAGE_URI` (`--import-aspect-types`=[`IMPORT_ASPECT_TYPES`,…] `--import-entry-groups`=[`IMPORT_ENTRY_GROUPS`,…] `--import-entry-link-types`=[`IMPORT_ENTRY_LINK_TYPES`,…] `--import-entry-types`=[`IMPORT_ENTRY_TYPES`,…] `--import-glossaries`=[`IMPORT_GLOSSARIES`,…] `--import-referenced-entry-scopes`=[`IMPORT_REFERENCED_ENTRY_SCOPES`,…]) : `--import-log-level`=`IMPORT_LOG_LEVEL` `--import-source-create-time`=`IMPORT_SOURCE_CREATE_TIME`]) [`--async`] [`--labels`=[`KEY`=`VALUE`,…]] [`--validate-only`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` A metadata job represents a long running job on Dataplex Catalog metadata entries. Some operations include importing and exporting metadata into entry groups through the usage of entry types and aspect types. 

The Metadata Job ID will be used to identify each configuration run. The Metadata Job id must follow these rules: 

  * Must contain only lowercase letters, numbers, and hyphens. 
  * Must start with a letter. 
  * Must end with a number or a letter. 
  * Must be between 1-63 characters. 
  * Must be unique within the customer project / location. 


EXAMPLES
     To create a Dataplex Metadata Job with type `IMPORT` and name `my-metadata-job` in location `us-central1` with additional parameters, run: 
    
    
    gcloud alpha dataplex metadata-jobs create my-metadata-job --location=us-central --project=test-project --type=import --import-source-storage-uri=gs://test-storage/ --import-source-create-time="2019-01-23T12:34:56.123456789Z" --import-entry-sync-mode=FULL --import-aspect-sync-mode=INCREMENTAL --import-log-level="debug" --import-entry-groups=projects/test-project/locations/us-central1/entryGroups/eg1 --import-entry-types="projects/test-project/locations/us-central1/entryTypes/et1", "projects/test-project/locations/us-central1/entryTypes/et2" --import-aspect-types="projects/test-project/locations/us-central1/aspectTypes/at1", "projects/test-project/locations/us-central1/aspectTypes/at2"

To create a Dataplex Metadata Job with type `EXPORT` and name `my-metadata-job` in location `us-central1` with additional parameters, run: 
    
    
    gcloud alpha dataplex metadata-jobs create my-metadata-job --location=us-central --project=test-project --type=export --export-output-path=gs://test-storage/ --export-entry-groups=projects/test-project/locations/us-central1/entryGroups/eg1 --export-entry-types="projects/test-project/locations/us-central1/entryTypes/et1", "projects/test-project/locations/us-central1/entryTypes/et2" --export-aspect-types="projects/test-project/locations/us-central1/aspectTypes/at1", "projects/test-project/locations/us-central1/aspectTypes/at2"

POSITIONAL ARGUMENTS
    

Metadata job resource - Arguments and flags that define the Dataplex metdata job you want to create. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `metadata_job` on the command line with a fully specified name; 
  * job ID is optional and will be generated if not specified with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 


[`METADATA_JOB`]
     ID of the metadata job or fully qualified identifier for the metadata job. 

To set the `metadata_job` attribute: 

  * provide the argument `metadata_job` on the command line; 
  * job ID is optional and will be generated if not specified. 


`--location`=`LOCATION`
     The location of the Dataplex resource. 

To set the `location` attribute: 

  * provide the argument `metadata_job` on the command line with a fully specified name; 
  * job ID is optional and will be generated if not specified with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `dataplex/location`. 


REQUIRED FLAGS
    

`--type`=`TYPE`
     Type. `TYPE` must be one of: 

`EXPORT`
     A Metadata Export Job will export entries and aspects from the declared Dataplex scope to the specified Cloud Storage location. 
`IMPORT`
     A Metadata Import Job will ingest, update, or delete entries and aspects into the declared Dataplex entry group. 
Settings for metadata job operation. 

Exactly one of these must be specified: 

Settings for metadata export job operation. 
`--export-output-path`=`EXPORT_OUTPUT_PATH`
     The Cloud Storage location to export metadata to. 

This flag argument must be specified if any of the other arguments in this group are specified. 

A boundary on the scope of impact that the metadata export job can have. 

At least one of these must be specified: 

`--export-aspect-types`=[`EXPORT_ASPECT_TYPES`,…]
     The list of aspect types to export metadata from. 
`--export-entry-types`=[`EXPORT_ENTRY_TYPES`,…]
     The list of entry types to export metadata from. 
The scope of resources to export metadata from. 

Exactly one of these must be specified: 

`--export-entry-groups`=[`EXPORT_ENTRY_GROUPS`,…]
     The list of entry groups to export metadata from. 
`--export-organization-level`=`EXPORT_ORGANIZATION_LEVEL`
     Whether to export metadata at the organization level. 
`--export-projects`=[`EXPORT_PROJECTS`,…]
     The list of projects to export metadata from. 
Settings for metadata import job operation. 
`--import-aspect-sync-mode`=`IMPORT_ASPECT_SYNC_MODE`
     Type. `IMPORT_ASPECT_SYNC_MODE` must be one of: 

`FULL`
     All resources in the job's scope are modified. If a resource exists in Dataplex but isn't included in the metadata import file, the resource is deleted when you run the metadata job. Use this mode to perform a full sync of the set of entries in the job scope. 
`INCREMENTAL`
     Only the entries and aspects that are explicitly included in the metadata import file are modified. Use this mode to modify a subset of resources while leaving unreferenced resources unchanged. 
This flag argument must be specified if any of the other arguments in this group are specified. 
`--import-entry-sync-mode`=`IMPORT_ENTRY_SYNC_MODE`
     Type. `IMPORT_ENTRY_SYNC_MODE` must be one of: 

`FULL`
     All resources in the job's scope are modified. If a resource exists in Dataplex but isn't included in the metadata import file, the resource is deleted when you run the metadata job. Use this mode to perform a full sync of the set of entries in the job scope. 
`INCREMENTAL`
     Only the entries and aspects that are explicitly included in the metadata import file are modified. Use this mode to modify a subset of resources while leaving unreferenced resources unchanged. 
This flag argument must be specified if any of the other arguments in this group are specified. 
`--import-source-storage-uri`=`IMPORT_SOURCE_STORAGE_URI`
     The Dataplex source storage URI to import metadata from. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--import-log-level`=`IMPORT_LOG_LEVEL`
     Type. `IMPORT_LOG_LEVEL` must be one of: 

`DEBUG`
     Debug-level logging. Captures detailed logs for each import item. Use debug-level logging to troubleshoot issues with specific import items. For example, use debug-level logging to identify resources that are missing from the job scope, entries or aspects that don't conform to the associated entry type or aspect type, or other misconfigurations with the metadata import file.. 
`INFO`
     Info-level logging. Captures logs at the overall job level. Includes aggregate logs about import items, but doesn't specify which import item has an error.. 
`--import-source-create-time`=`IMPORT_SOURCE_CREATE_TIME`
     Time at which the event took place. See `$ [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes)` for information on supported time formats. 
A boundary on the scope of impact that the metadata import job can have. 

At least one of these must be specified: 

`--import-aspect-types`=[`IMPORT_ASPECT_TYPES`,…]
     The list of aspect types to import metadata jobs into. 
`--import-entry-groups`=[`IMPORT_ENTRY_GROUPS`,…]
     The list of entry groups to import metadata jobs into. 
`--import-entry-link-types`=[`IMPORT_ENTRY_LINK_TYPES`,…]
     The list of entry link types to import metadata jobs into. 
`--import-entry-types`=[`IMPORT_ENTRY_TYPES`,…]
     The list of entry types to import metadata jobs into. 
`--import-glossaries`=[`IMPORT_GLOSSARIES`,…]
     The list of glossaries to import metadata jobs into. 
`--import-referenced-entry-scopes`=[`IMPORT_REFERENCED_ENTRY_SCOPES`,…]
     The list of referenced entry scopes to import metadata jobs into. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

`--validate-only`
     Validate the create action, but don't actually perform it. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud dataplex metadata-jobs create](https://docs.cloud.google.com/sdk/gcloud/reference/dataplex/metadata-jobs/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
