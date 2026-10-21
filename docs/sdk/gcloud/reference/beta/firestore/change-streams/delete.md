---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/firestore/change-streams/delete/
title: gcloud beta firestore change-streams delete \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:16:56.505259+00:00
---

# gcloud beta firestore change-streams delete  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/firestore/change-streams/delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta firestore change-streams delete Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta firestore change-streams delete - delete a Cloud Firestore change stream 
SYNOPSIS
    

`gcloud beta firestore change-streams delete` `CHANGE_STREAM` `--database`=`DATABASE` [`--etag`=`ETAG`] [`GCLOUD_WIDE_FLAG …`]
EXAMPLES
     To delete a change stream named `my-stream` in database `my-db`: 
    
    
    gcloud beta firestore change-streams delete my-stream --database=my-db

POSITIONAL ARGUMENTS
    

`CHANGE_STREAM`
     The ID of the change stream. 
REQUIRED FLAGS
    

`--database`=`DATABASE`
     The database to operate on. 

For example, to operate on database `foo`: 
    
    
    gcloud beta firestore change-streams delete --database='foo'

OPTIONAL FLAGS
    

`--etag`=`ETAG`
     The current etag of the change stream. If an etag is provided and does not match the current etag of the change stream, deletion will be blocked and a FAILED_PRECONDITION error will be returned. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud firestore change-streams delete](https://docs.cloud.google.com/sdk/gcloud/reference/firestore/change-streams/delete)
    
    
    [gcloud alpha firestore change-streams delete](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/firestore/change-streams/delete)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
