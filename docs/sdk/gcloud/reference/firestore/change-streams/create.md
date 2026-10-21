---
url: https://docs.cloud.google.com/sdk/gcloud/reference/firestore/change-streams/create/
title: gcloud firestore change-streams create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:36:13.837187+00:00
---

# gcloud firestore change-streams create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/firestore/change-streams/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud firestore change-streams create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud firestore change-streams create - create a Cloud Firestore change stream 
SYNOPSIS
    

`gcloud firestore change-streams create` `CHANGE_STREAM` (`--collection-group-scope`=`COLLECTION_GROUP_ID` | `--database-scope`) [`--database`=`DATABASE`; default="(default)"] [`--retention`=`RETENTION`; default="7d"] [`GCLOUD_WIDE_FLAG …`]
EXAMPLES
     To create a database-scoped change stream named `my-stream` in database `my-db`: 
    
    
    gcloud firestore change-streams create my-stream --database=my-db --database-scope

To create a collection-group-scoped change stream named `my-cg-stream` for collection group `my-cg` in database `my-db` with a retention period of 1 day: 
    
    
    gcloud firestore change-streams create my-cg-stream --database=my-db --collection-group-scope=my-cg --retention=1d

POSITIONAL ARGUMENTS
    

`CHANGE_STREAM`
     The ID of the change stream. 
REQUIRED FLAGS
    

Exactly one of these must be specified: 

`--collection-group-scope`=`COLLECTION_GROUP_ID`
     Create a collection-group-scoped change stream for the specified collection group (e.g., --collection-group-scope=my-collection-group). 
`--database-scope`
     Create a database-scoped change stream. 
OPTIONAL FLAGS
    

`--database`=`DATABASE`; default="(default)"
     The database to operate on. The default value is `(default)`. 

For example, to operate on database `foo`: 
    
    
    gcloud firestore change-streams create --database='foo'

`--retention`=`RETENTION`; default="7d"
     The retention period of the change stream (e.g. 1d, 7d). Must be between 1 and 7 days, in day granularity. Default is 7d. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha firestore change-streams create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/firestore/change-streams/create)
    
    
    [gcloud beta firestore change-streams create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/firestore/change-streams/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
