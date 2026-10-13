---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/bq/translation/translate-batch/
title: gcloud alpha bq translation translate-batch \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:43:50.570606+00:00
---

# gcloud alpha bq translation translate-batch  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/bq/translation/translate-batch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha bq translation translate-batch Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha bq translation translate-batch - translates a batch of SQL queries 
SYNOPSIS
    

`gcloud alpha bq translation translate-batch` `--location`=`LOCATION` `--source-dialect`=`SOURCE_DIALECT` `--target-dialect`=`TARGET_DIALECT` `--target-gcs-path`=`TARGET_GCS_PATH` [`--async`] [`--enable-ai-suggestion`] [`--endpoint-mode`=`ENDPOINT_MODE`] [`--source-gcs-files`=[`FILE_URI`,…]] [`--source-gcs-uris`=[`URI`,…]] [`--source-local-dirs`=[`LOCAL_DIR`=`CLOUD_STORAGE_URI`,…]] [`--source-local-files`=[`LOCAL_FILE`=`CLOUD_STORAGE_FILE_URI`,…]] [`--target-types`=[`TARGET_TYPE`,…]] [`GCLOUD_WIDE_FLAG …`]
EXAMPLES
     To translate a batch of Teradata queries in Cloud Storage in location `us-central1`, run: 
    
    
    gcloud alpha bq translation translate-batch --source-dialect=teradata --target-dialect=bigquery --location=us-central1 --source-gcs-uris=gs://my-bucket/queries/ --target-gcs-path=gs://my-bucket/output/

To upload queries from a local directory and translate them, run: 
    
    
    gcloud alpha bq translation translate-batch --source-dialect=teradata --target-dialect=bigquery --location=us-central1 --source-local-dirs=./queries=gs://my-bucket/queries/ --target-gcs-path=gs://my-bucket/output/

REQUIRED FLAGS
    

`--location`=`LOCATION`
     The location to execute the migration workflow. 
`--source-dialect`=`SOURCE_DIALECT`
     The dialect of the source SQL files. 
`--target-dialect`=`TARGET_DIALECT`
     The dialect of the target SQL files. 
`--target-gcs-path`=`TARGET_GCS_PATH`
     The Cloud Storage directory URI where the translated output will be written. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--enable-ai-suggestion`
     Enable AI suggestion to improve translation quality. 
`--endpoint-mode`=`ENDPOINT_MODE`
     Specifies endpoint mode for a given command. Regional endpoints provide enhanced data residency and reliability by ensuring your request is handled entirely within the specified Google Cloud region. This differs from global endpoints, which may process parts of the request outside the target region. Overrides the default `regional/endpoint_mode` property value for this command invocation. `ENDPOINT_MODE` must be one of: 

`global`
     (Default) Use global rather than regional endpoints. 
`regional`
     Only use regional endpoints. An error will be raised if a regional endpoint is not available for a given command. 
`regional-preferred`
     Use regional endpoints when available, otherwise use global endpoints. Recommended for most users. 
`--source-gcs-files`=[`FILE_URI`,…]
     List of Cloud Storage URIs pointing to individual source files or additional files. Note: these files must not be located within the directory specified by \--source-gcs-uris, or an error will occur. 
`--source-gcs-uris`=[`URI`,…]
     List of Cloud Storage URI prefixes containing multiple source SQL files. 
`--source-local-dirs`=[`LOCAL_DIR`=`CLOUD_STORAGE_URI`,…]
     Map of local directories to their corresponding Cloud Storage URIs (e.g., local_dir=gs://bucket/path). The local directories will be uploaded to the specified Cloud Storage URIs before translation, and those Cloud Storage URIs will be automatically included in the translation job. 
`--source-local-files`=[`LOCAL_FILE`=`CLOUD_STORAGE_FILE_URI`,…]
     Map of local files to their corresponding Cloud Storage URIs (e.g., local_file=gs://bucket/path/file.sql). The local files will be uploaded to the specified Cloud Storage URIs before translation, and those Cloud Storage URIs will be automatically included in the translation job. 
`--target-types`=[`TARGET_TYPE`,…]
     List of output types to generate. Supported values include `sql` to translate SQL files, and `metadata` to translate metadata ZIP files into DDL statements and table mappings. Specify both to translate SQL files and metadata ZIP files in a single job, instead of running a separate `[gcloud alpha bq translation translate-metadata](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/bq/translation/translate-metadata)` command. Defaults to `sql`. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

REGIONAL ENDPOINTS
     This command supports regional endpoints. To use regional endpoints for this command, use the `--endpoint-mode=regional-preferred` flag. To use regional endpoints by default, run `$ [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) regional/endpoint_mode regional-preferred`. 
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-29 UTC."],[],[]] 
