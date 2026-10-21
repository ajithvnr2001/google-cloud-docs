---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/sql/import/csv/
title: gcloud alpha sql import csv \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:26:02.983822+00:00
---

# gcloud alpha sql import csv  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/sql/import/csv/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha sql import csv Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha sql import csv - imports data into a Cloud SQL instance from a CSV file 
SYNOPSIS
    

`gcloud alpha sql import csv` `INSTANCE` `URI` `--database`=`DATABASE`, `-d` `DATABASE` `--table`=`TABLE` [`--async`] [`--columns`=`COLUMNS`,[`COLUMNS`,…]] [`--escape`=`ESCAPE`] [`--fields-terminated-by`=`FIELDS_TERMINATED_BY`] [`--lines-terminated-by`=`LINES_TERMINATED_BY`] [`--quote`=`QUOTE`] [`--user`=`USER`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Imports data into a Cloud SQL instance from a plain text file in a Google Cloud Storage bucket with one line per row and comma-separated fields. 
POSITIONAL ARGUMENTS
    

`INSTANCE`
     Cloud SQL instance ID. 
`URI`
     Path to the CSV file in Google Cloud Storage from which the import is made. The URI is in the form `gs://bucketName/fileName`. Compressed gzip files (.gz) are also supported. 
REQUIRED FLAGS
    

`--database`=`DATABASE`, `-d` `DATABASE`
     The database (for example, guestbook) to which the import is made. 
`--table`=`TABLE`
     The database table to import csv file into. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--columns`=`COLUMNS`,[`COLUMNS`,…]
     The columns to import from csv file. These correspond to actual database columns to import. If not set, all columns from csv file are imported to corresponding database columns. 
`--escape`=`ESCAPE`
     Specifies the character that should appear before a data character that needs to be escaped. The value of this argument has to be a character in Hex ASCII Code. For example, "22" represents double quotes. This flag is only available for MySQL and Postgres. If this flag is not provided, double quotes character will be used as the default value. 
`--fields-terminated-by`=`FIELDS_TERMINATED_BY`
     Specifies the character that splits column values. The value of this argument has to be a character in Hex ASCII Code. For example, "2C" represents a comma. This flag is only available for MySQL and Postgres. If this flag is not provided, a comma character will be used as the default value. 
`--lines-terminated-by`=`LINES_TERMINATED_BY`
     Specifies the character that split line records. The value of this argument has to be a character in Hex ASCII Code. For example, "0A" represents a new line. This flag is only available for MySQL. If this flag is not provided, a new line character will be used as the default value. 
`--quote`=`QUOTE`
     Specifies the character that encloses values from columns that have string data type. The value of this argument has to be a character in Hex ASCII Code. For example, "22" represents double quotes. This flag is only available for MySQL and Postgres. If this flag is not provided, double quotes character will be used as the default value. 
`--user`=`USER`
     PostgreSQL user for this import operation. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud sql import csv](https://docs.cloud.google.com/sdk/gcloud/reference/sql/import/csv)
    
    
    [gcloud beta sql import csv](https://docs.cloud.google.com/sdk/gcloud/reference/beta/sql/import/csv)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
