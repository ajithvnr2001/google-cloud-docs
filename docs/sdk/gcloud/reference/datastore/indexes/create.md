---
url: https://docs.cloud.google.com/sdk/gcloud/reference/datastore/indexes/create/
title: gcloud datastore indexes create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:52:00.765499+00:00
---

# gcloud datastore indexes create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/datastore/indexes/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud datastore indexes create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud datastore indexes create - create new datastore indexes based on your local index configuration 
SYNOPSIS
    

`gcloud datastore indexes create` `INDEX_FILE` [`--database`=`DATABASE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Create new datastore indexes based on your local index configuration. Any indexes in your index file that do not exist will be created. 
EXAMPLES
     To create new indexes based on your local configuration, run: 
    
    
    gcloud datastore indexes create ~/myapp/index.yaml

Detailed information about index configuration can be found at the [index.yaml reference](https://cloud.google.com/datastore/docs/tools/indexconfig). 

POSITIONAL ARGUMENTS
    

`INDEX_FILE`
     The path to your `index.yaml` file. For a detailed look into defining your `index.yaml` file, refer to this configuration guide: <https://cloud.google.com/datastore/docs/tools/indexconfig#Datastore_About_index_yaml>
FLAGS
    

`--database`=`DATABASE`
     The database to operate on. If not specified, the CLI refers the `(default)` database by default. 

For example, to operate on database `testdb`: 
    
    
    gcloud datastore indexes create --database='testdb'

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha datastore indexes create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/datastore/indexes/create)
    
    
    [gcloud beta datastore indexes create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/datastore/indexes/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
