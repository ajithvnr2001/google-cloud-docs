---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/alloydb/clusters/export/
title: gcloud alpha alloydb clusters export \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:03:47.688582+00:00
---

# gcloud alpha alloydb clusters export  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/alloydb/clusters/export/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha alloydb clusters export Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha alloydb clusters export - export data from an AlloyDB cluster to Google Cloud Storage 
SYNOPSIS
    

`gcloud alpha alloydb clusters export` `CLUSTER` `--database`=`DATABASE` `--gcs-uri`=`GCS_URI` `--region`=`REGION` ([`--csv` `--select-query`=`SELECT_QUERY` : `--escape-character`=`ESCAPE_CHARACTER` `--field-delimiter`=`FIELD_DELIMITER` `--quote-character`=`QUOTE_CHARACTER`] | [`--sql` : `--schema-only` `--tables`=`TABLES` [`--clean-target-objects` : `--if-exist-target-objects`]]) [`--async`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Export data from an AlloyDB cluster to Google Cloud Storage. 
EXAMPLES
     To export a cluster, run: 
    
    
    gcloud alpha alloydb clusters export my-cluster --region=us-central1 --database=my-database --gcs-uri=gs://my-bucket/my-export-file-path --csv --select-query="SELECT * FROM my-table"

POSITIONAL ARGUMENTS
    

`CLUSTER`
     AlloyDB cluster ID 
REQUIRED FLAGS
    

`--database`=`DATABASE`
     Database name. 
Destination URI where the file needs to be exported. 

This must be specified. 

`--gcs-uri`=`GCS_URI`
     Path to the Google Cloud Storage file to which export has to be done. 
`--region`=`REGION`
     Regional location (e.g. `asia-east1`, `us-east1`). See the full list of regions at <https://cloud.google.com/sql/docs/instance-locations>. 
Export options for the cluster. 

Exactly one of these must be specified: 

CSV export options for the cluster. 
`--csv`
     Specifies destination file type. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--select-query`=`SELECT_QUERY`
     Select query to be used for export. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--escape-character`=`ESCAPE_CHARACTER`
     Escape character to be used for export. 
`--field-delimiter`=`FIELD_DELIMITER`
     Field delimiter to be used for export. 
`--quote-character`=`QUOTE_CHARACTER`
     Quote character to be used for export. 
SQL export options for the cluster. 
`--sql`
     Specifies destination file type. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--schema-only`
     Export only schema of the database. 
`--tables`=`TABLES`
     Comma-separated list of table names which need to be exported. 
SQL export options to clean target objects. 
`--clean-target-objects`
     If true, output commands to DROP all the dumped database objects prior to outputting the commands for creating them. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--if-exist-target-objects`
     If true, use DROP … IF EXISTS commands to check for the object's existence before dropping it in clean_target_objects mode. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud alloydb clusters export](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/clusters/export)
    
    
    [gcloud beta alloydb clusters export](https://docs.cloud.google.com/sdk/gcloud/reference/beta/alloydb/clusters/export)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
