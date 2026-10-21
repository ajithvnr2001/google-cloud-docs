---
url: https://docs.cloud.google.com/sdk/gcloud/reference/biglake/hive/databases/create/
title: gcloud biglake hive databases create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:45:29.532925+00:00
---

# gcloud biglake hive databases create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/biglake/hive/databases/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud biglake hive databases create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud biglake hive databases create - creates a BigLake Hive database 
SYNOPSIS
    

`gcloud biglake hive databases create` (`DATABASE` : `--catalog`=`CATALOG`) [`--description`=`DESCRIPTION`] [`--location-uri`=`LOCATION_URI`] [`--parameters`=[`KEY`=`VALUE`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Creates a BigLake Hive database. 
EXAMPLES
     To create a BigLake Hive database named `my-database` in catalog `my-catalog`, run: 
    
    
    gcloud biglake hive databases create my-database --catalog=my-catalog

To create a BigLake Hive database named `my-database` in catalog `my-catalog`, with bucket `gs://my-bucket`, parameters `key1=value1,key2=value2` and description `My new database`, run: 
    
    
    gcloud biglake hive databases create my-database --catalog=my-catalog --location-uri=gs://my-bucket --description="My new database" --parameters=key1=value1,key2=value2

POSITIONAL ARGUMENTS
    

Hive database resource - The Hive Database to create. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `database` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`DATABASE`
     ID of the hive_database or fully qualified identifier for the hive_database. 

To set the `database` attribute: 

  * provide the argument `database` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--catalog`=`CATALOG`
     Name of the Hive catalog to use. To set the `catalog` attribute: 

  * provide the argument `database` on the command line with a fully specified name; 
  * provide the argument `--catalog` on the command line. 


FLAGS
    

`--description`=`DESCRIPTION`
     Description of the Hive database. 
`--location-uri`=`LOCATION_URI`
     The Cloud Storage location path where the database data will be stored. Format: gs://bucket/path/to/database 
`--parameters`=[`KEY`=`VALUE`,…]
     Additional parameters associated with the database. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `biglake/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/bigquery/>
NOTES
     These variants are also available: 
    
    
    [gcloud alpha biglake hive databases create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/biglake/hive/databases/create)
    
    
    [gcloud beta biglake hive databases create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/biglake/hive/databases/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
