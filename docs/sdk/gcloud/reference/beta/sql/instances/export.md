---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/sql/instances/export/
title: gcloud beta sql instances export \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:07:05.089532+00:00
---

# gcloud beta sql instances export  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/sql/instances/export/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta sql instances export Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta sql instances export - exports data from a Cloud SQL instance 
SYNOPSIS
    

`gcloud beta sql instances export` `INSTANCE` `URI` [`--async`] [`--database`=`DATABASE`,[`DATABASE`,…], `-d` `DATABASE`,[`DATABASE`,…]] [`--table`=`TABLE`,[`TABLE`,…], `-t` `TABLE`,[`TABLE`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` `(DEPRECATED)` Exports data from a Cloud SQL instance. 

This command is deprecated and will be removed in version 205.0.0. Use `[gcloud sql export sql](https://docs.cloud.google.com/sdk/gcloud/reference/sql/export/sql)` instead. 

Exports data from a Cloud SQL instance to a Google Cloud Storage bucket as a MySQL dump file. 

POSITIONAL ARGUMENTS
    

`INSTANCE`
     Cloud SQL instance ID. 
`URI`
     The path to the file in Google Cloud Storage where the export will be stored. The URI is in the form gs://bucketName/fileName. If the file already exists, the operation fails. If the filename ends with .gz, the contents are compressed. 
FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--database`=`DATABASE`,[`DATABASE`,…], `-d` `DATABASE`,[`DATABASE`,…]
     Database(s) from which the export is made. Information on requirements can be found here: <https://cloud.google.com/sql/docs/mysql/admin-api/v1beta4/instances/export#exportContext.databases>
`--table`=`TABLE`,[`TABLE`,…], `-t` `TABLE`,[`TABLE`,…]
     Tables to export from the specified database. If you specify tables, specify one and only one database. For Postgres instances, only one table can be exported at a time. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud sql instances export](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/export)
    
    
    [gcloud alpha sql instances export](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/sql/instances/export)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
