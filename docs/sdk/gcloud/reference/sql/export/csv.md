---
url: https://docs.cloud.google.com/sdk/gcloud/reference/sql/export/csv/
title: gcloud sql export csv \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:39:36.927155+00:00
---

# gcloud sql export csv  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/sql/export/csv/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud sql export csv Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud sql export csv - exports data from a Cloud SQL instance to a CSV file 
SYNOPSIS
    

`gcloud sql export csv` `INSTANCE` `URI` `--query`=`QUERY` [`--async`] [`--database`=`DATABASE`,[`DATABASE`,…], `-d` `DATABASE`,[`DATABASE`,…]] [`--escape`=`ESCAPE`] [`--fields-terminated-by`=`FIELDS_TERMINATED_BY`] [`--lines-terminated-by`=`LINES_TERMINATED_BY`] [`--offload`] [`--quote`=`QUOTE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Exports data from a Cloud SQL instance to a Google Cloud Storage bucket as a plain text file with one line per row and comma-separated fields. 
POSITIONAL ARGUMENTS
    

`INSTANCE`
     Cloud SQL instance ID. 
`URI`
     The path to the file in Google Cloud Storage where the export will be stored. The URI is in the form gs://bucketName/fileName. If the file already exists, the operation fails. If the filename ends with .gz, the contents are compressed. 
REQUIRED FLAGS
    

`--query`=`QUERY`
     A SQL SELECT query (e.g., SELECT * FROM table) that specifies the data to export. WARNING: While in-transit, the query might be processed in intermediate locations other than the location of the target instance. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--database`=`DATABASE`,[`DATABASE`,…], `-d` `DATABASE`,[`DATABASE`,…]
     Database(s) from which the export is made. Information on requirements can be found here: <https://cloud.google.com/sql/docs/mysql/admin-api/v1beta4/instances/export#exportContext.databases>
`--escape`=`ESCAPE`
     Specifies the character that should appear before a data character that needs to be escaped. The value of this argument has to be a character in Hex ASCII Code. For example, "22" represents double quotes. This flag is only available for MySQL and Postgres. If this flag is not provided, double quotes character will be used as the default value. 
`--fields-terminated-by`=`FIELDS_TERMINATED_BY`
     Specifies the character that splits column values. The value of this argument has to be a character in Hex ASCII Code. For example, "2C" represents a comma. This flag is only available for MySQL and Postgres. If this flag is not provided, a comma character will be used as the default value. 
`--lines-terminated-by`=`LINES_TERMINATED_BY`
     Specifies the character that split line records. The value of this argument has to be a character in Hex ASCII Code. For example, "0A" represents a new line. This flag is only available for MySQL. If this flag is not provided, a new line character will be used as the default value. 
`--offload`
     Offload an export to a temporary instance. Doing so reduces strain on source instances and allows other operations to be performed while the export is in progress. 
`--quote`=`QUOTE`
     Specifies the character that encloses values from columns that have string data type. The value of this argument has to be a character in Hex ASCII Code. For example, "22" represents double quotes. This flag is only available for MySQL and Postgres. If this flag is not provided, double quotes character will be used as the default value. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha sql export csv](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/sql/export/csv)
    
    
    [gcloud beta sql export csv](https://docs.cloud.google.com/sdk/gcloud/reference/beta/sql/export/csv)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
