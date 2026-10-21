---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/alloydb/clusters/import/
title: gcloud alpha alloydb clusters import \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:45:21.367190+00:00
---

# gcloud alpha alloydb clusters import  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/alloydb/clusters/import/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha alloydb clusters import Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha alloydb clusters import - import data to an AlloyDB cluster from Google Cloud Storage 
SYNOPSIS
    

`gcloud alpha alloydb clusters import` `CLUSTER` `--gcs-uri`=`GCS_URI` `--region`=`REGION` (`--sql` | [`--csv` `--table`=`TABLE` : `--columns`=`COLUMNS` `--escape-character`=`ESCAPE_CHARACTER` `--field-delimiter`=`FIELD_DELIMITER` `--quote-character`=`QUOTE_CHARACTER`]) [`--async`] [`--database`=`DATABASE`] [`--user`=`USER`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Import data to an AlloyDB cluster from Google Cloud Storage. 
EXAMPLES
     To import data into a cluster, run: 
    
    
    gcloud alpha alloydb clusters import my-cluster --region=us-central1 --database=my-database --gcs-uri=gs://my-bucket/source-file-path --sql --user=my-user"

POSITIONAL ARGUMENTS
    

`CLUSTER`
     AlloyDB cluster ID 
REQUIRED FLAGS
    

URI of the source file for import. 

This must be specified. 

`--gcs-uri`=`GCS_URI`
     Path to the Google Cloud Storage file from which import has to be done. 
`--region`=`REGION`
     Regional location (e.g. `asia-east1`, `us-east1`). See the full list of regions at <https://cloud.google.com/sql/docs/instance-locations>. 
Import options for the cluster. 

Exactly one of these must be specified: 

SQL import options for the cluster. 
`--sql`
     Specify source file type. 
CSV import options for the cluster. 
`--csv`
     Specify source file type. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--table`=`TABLE`
     Table name to which the data has to be imported. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--columns`=`COLUMNS`
     Comma-separated list of column names to be used for import. 
`--escape-character`=`ESCAPE_CHARACTER`
     Escape character in the source file. 
`--field-delimiter`=`FIELD_DELIMITER`
     Field delimiter in the source file. 
`--quote-character`=`QUOTE_CHARACTER`
     Quote character in the source file. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--database`=`DATABASE`
     Database name. 
`--user`=`USER`
     Database user for the import. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud alloydb clusters import](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/clusters/import)
    
    
    [gcloud beta alloydb clusters import](https://docs.cloud.google.com/sdk/gcloud/reference/beta/alloydb/clusters/import)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
