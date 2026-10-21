---
url: https://docs.cloud.google.com/sdk/gcloud/reference/firestore/export/
title: gcloud firestore export \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:44:30.875565+00:00
---

# gcloud firestore export  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/firestore/export/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud firestore export Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud firestore export - export Cloud Firestore documents to Google Cloud Storage 
SYNOPSIS
    

`gcloud firestore export` `OUTPUT_URI_PREFIX` [`--async`] [`--collection-ids`=[`COLLECTION_GROUP_IDS`,…]] [`--database`=`DATABASE`; default="(default)"] [`--namespace-ids`=[`NAMESPACE_IDS`,…]] [`--snapshot-time`=`SNAPSHOT_TIME`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     export Cloud Firestore documents to Google Cloud Storage. 
EXAMPLES
     To export all collection groups to `mybucket` in objects prefixed with `my/path`, run: 
    
    
    gcloud firestore export gs://mybucket/my/path

To export a specific set of collections groups asynchronously, run: 
    
    
    gcloud firestore export gs://mybucket/my/path --collection-ids='specific collection group1','specific
     collection group2' --async

To export all collection groups from certain namespace, run: 
    
    
    gcloud firestore export gs://mybucket/my/path --namespace-ids='specific namespace id'

To export from a snapshot at '2023-05-26T10:20:00.00Z', run: 
    
    
    gcloud firestore export gs://mybucket/my/path --snapshot-time='2023-05-26T10:20:00.00Z'

POSITIONAL ARGUMENTS
    

`OUTPUT_URI_PREFIX`
     Location where the export files will be stored. Must be a valid Google Cloud Storage bucket with an optional path prefix. 

For example: 
    
    
    gcloud firestore export gs://mybucket/my/path

Will place the export in the `mybucket` bucket in objects prefixed with `my/path`. 

FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--collection-ids`=[`COLLECTION_GROUP_IDS`,…]
     List specifying which collection groups will be included in the operation. When omitted, all collection groups are included. 

For example, to operate on only the `customers` and `orders` collections groups: 
    
    
    gcloud firestore export --collection-ids='customers','orders'

`--database`=`DATABASE`; default="(default)"
     The database to operate on. The default value is `(default)`. 

For example, to operate on database `foo`: 
    
    
    gcloud firestore export --database='foo'

`--namespace-ids`=[`NAMESPACE_IDS`,…]
     List specifying which namespaces will be included in the operation. When omitted, all namespaces are included. 

This is only supported for Datastore Mode databases. 

For example, to operate on only the `customers` and `orders` namespaces: 
    
    
    gcloud firestore export --namespaces-ids='customers','orders'

`--snapshot-time`=`SNAPSHOT_TIME`
     The version of the database to export. 

The timestamp must be in the past, rounded to the minute and not older than `earliestVersionTime`. If specified, then the exported documents will represent a consistent view of the database at the provided time. Otherwise, there are no guarantees about the consistency of the exported documents. 

For example, to operate on snapshot time `2023-05-26T10:20:00.00Z`: 
    
    
    gcloud firestore export --snapshot-time='2023-05-26T10:20:00.00Z'

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha firestore export](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/firestore/export)
    
    
    [gcloud beta firestore export](https://docs.cloud.google.com/sdk/gcloud/reference/beta/firestore/export)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
