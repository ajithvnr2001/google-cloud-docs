---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataplex/dbt/metadata-jobs/create/
title: gcloud alpha dataplex dbt metadata-jobs create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:17:38.519788+00:00
---

# gcloud alpha dataplex dbt metadata-jobs create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataplex/dbt/metadata-jobs/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha dataplex dbt metadata-jobs create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha dataplex dbt metadata-jobs create - transform dbt-core artifacts and import them into Dataplex Catalog 
SYNOPSIS
    

`gcloud alpha dataplex dbt metadata-jobs create` [[`METADATA_JOB`] `--location`=`LOCATION`] `--storage-uri`=`STORAGE_URI` [`--artifacts-path`=`ARTIFACTS_PATH`; default="."] [`--aspects-only`] [`--async`] [`--entry-group`=`ENTRY_GROUP`; default="dbt-metadata-ingestion"] [`--no-include-entry-links`] [`--skip-bigquery-link`] [`--validate-only`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` This command reads the JSON artifacts produced by dbt-core (manifest.json, catalog.json, run_results.json, sources.json) from a local directory or a Cloud Storage folder, transforms them into the Dataplex metadata import format, uploads the result to Cloud Storage, and triggers a Dataplex metadata import job that ingests the metadata into the Knowledge Catalog. 

One chain of dbt commands, run from the dbt project root against a single profile and target, produces an artifact set that fills every field this command imports. On dbt-core 2.x and Fusion: 
    
    
    dbt source freshness; dbt build; dbt parse --write-catalog

On dbt-core 1.x, where `dbt parse` writes no catalog and `dbt docs generate` still does: 
    
    
    dbt source freshness; dbt build; dbt docs generate --no-compile

Separate the commands with `;` rather than `&&`: `dbt build` exits non-zero when a test fails, and a run with failing tests is exactly the one whose verdicts are worth importing. Whatever the chain omits is omitted from the import too -- without catalog.json columns arrive untyped and tables carry no row or byte counts, without run_results.json tests carry no verdict and models no compiled SQL, and without sources.json sources carry no freshness. 

Only the entry group that receives the dbt entries must exist in the caller's project beforehand. The caller must also be able to USE the dbt connector types (dataplex.aspectTypes.use / the dbt-connector-types alternate-use permission). 

Unless `--aspects-only` is passed, the import is a FULL sync of the dbt contents of the entry group: any dbt entry in the entry group that this run's artifacts do not describe is DELETED. Give each dbt project its own entry group. Two dbt projects importing their own artifacts into one shared entry group will each delete the other's entries on every run. 

The Metadata Job ID identifies the import run and, if provided, must: 

  * Contain only lowercase letters, numbers, and hyphens. 
  * Start with a letter and end with a number or a letter. 
  * Be 1-63 characters and unique within the project / location. 


EXAMPLES
     To transform the dbt artifacts in the current directory and import them into entry group `dbt-metadata-ingestion` in project `my-project`, location `us-central1`, run: 
    
    
    gcloud alpha dataplex dbt metadata-jobs create my-dbt-import --project=my-project --location=us-central1 --artifacts-path=. --entry-group=dbt-metadata-ingestion --storage-uri=gs://my-bucket/dbt-imports/

The artifacts may also be read from Cloud Storage, e.g. when they are published there by a dbt CI job: 
    
    
    gcloud alpha dataplex dbt metadata-jobs create my-dbt-import --project=my-project --location=us-central1 --artifacts-path=gs://my-bucket/dbt-artifacts/ --entry-group=dbt-metadata-ingestion --storage-uri=gs://my-bucket/dbt-imports/

To only build and upload the JSONL and validate the job without ingesting, add `--validate-only`. 

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
    

`--storage-uri`=`STORAGE_URI`
     Cloud Storage URI prefix (gs://bucket/path/) the transformed JSONL is uploaded to and the import job reads from. The caller must have write access and the Dataplex service agent must have read access. 
OPTIONAL FLAGS
    

`--artifacts-path`=`ARTIFACTS_PATH`; default="."
     Path to the dbt-core artifacts: a local directory, or a Cloud Storage folder (`gs://bucket/folder/`) they were published to. May point at the dbt project root (the `target/` subdirectory is detected automatically) or directly at the directory containing manifest.json. manifest.json is required; catalog.json, run_results.json and sources.json are read if present. Defaults to the current working directory. 
`--aspects-only`
     Update only the metadata this dbt run observed, and leave the rest of the entry group untouched. No entry is created, deleted or re-parented, and an aspect whose dbt artifact was absent from this run keeps the value a previous run gave it. An aspects-only run emits no entry links, so `--include-entry-links` has no effect here. 

Use this for routine ingestion, after whichever dbt command your pipeline already runs: `dbt build`, `dbt test`, `dbt source freshness`, or a `--select`-narrowed rebuild. It is safe to run repeatedly and from several jobs. 

Omit it when the set of dbt resources itself changed (a model added, renamed or deleted), since only a full run creates and prunes entries. A full run also refreshes display names, descriptions, labels and the entry hierarchy, which this flag leaves alone; and because a full run must write every entry's required aspects, run it from as complete an artifact set as your pipeline can produce. 

The first ingestion into an entry group must be a full run: there are no entries to attach aspects to yet. 

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--entry-group`=`ENTRY_GROUP`; default="dbt-metadata-ingestion"
     Short ID of the entry group that receives the dbt entries. Must already exist in the project / location. Use a separate entry group per dbt project: without `--aspects-only`, a run deletes the dbt entries in this entry group that its own artifacts do not describe. 
`--include-entry-links`
     Also emit EntryLink records capturing dbt relationships: `reference` where one resource describes or uses another (a test, a semantic model, a metric, a macro the project defines and a node calls, or the physical BigQuery table a node writes), and `schema-join` for joinable columns declared by a dbt `relationships` test. 

Enabled by default, use `--no-include-entry-links` to disable. 

`--skip-bigquery-link`
     Skip physical `reference` links (dbt node -> physical BigQuery table entry). Otherwise a `reference` link is emitted for each materialized dbt node (model/seed/snapshot) whose BigQuery dataset lives in the import location (`--location`); links can only reference @bigquery entries in that same region, so datasets in another region are skipped automatically. Use this flag when the BigQuery tables are not cataloged in Dataplex. 
`--validate-only`
     Build and upload the JSONL and validate the metadata job, but don't actually ingest. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud dataplex dbt metadata-jobs create](https://docs.cloud.google.com/sdk/gcloud/reference/dataplex/dbt/metadata-jobs/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-29 UTC."],[],[]] 
