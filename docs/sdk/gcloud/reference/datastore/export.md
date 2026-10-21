---
url: https://docs.cloud.google.com/sdk/gcloud/reference/datastore/export/
title: gcloud datastore export \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:15:32.814384+00:00
---

# gcloud datastore export  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/datastore/export/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud datastore export Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud datastore export - export Cloud Datastore entities to Google Cloud Storage 
SYNOPSIS
    

`gcloud datastore export` `OUTPUT_URL_PREFIX` [`--async`] [`--kinds`=[`KIND`,…]] [`--namespaces`=[`NAMESPACE`,…]] [`--operation-labels`=[`OPERATION_LABEL`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Export a copy of all or a subset of entities from Google Cloud Datastore to another storage system, such as Google Cloud Storage. Recent updates to entities may not be reflected in the export. The export occurs in the background and its progress can be monitored and managed via the operation commands. The output of an export may only be used once the operation has completed. If an export operation is cancelled before completion then it may leave partial data behind in Google Cloud Storage. 
EXAMPLES
     To export all kinds in the `exampleNs` namespace in the `exampleProject` project to the `exampleBucket`, run: 
    
    
    gcloud datastore export gs://exampleBucket --namespaces='exampleNs' --project='exampleProject'

To export the `exampleKind` and `otherKind` kinds in the `exampleNs` namespace in the `exampleProject` project to the `exampleBucket`, run: 
    
    
    gcloud datastore export gs://exampleBucket --kinds='exampleKind,otherKind' --namespaces='exampleNs' --project='exampleProject'

To export all namespaces and kinds in the currently set project to the `exampleBucket` without waiting for the operation to complete, run: 
    
    
    gcloud datastore export gs://exampleBucket --async

To export the `exampleKind` in all namespaces in the currently set project to the `exampleBucket`, and output the result in JSON, run: 
    
    
    gcloud datastore export gs://exampleBucket --kinds='exampleKind' --format=json

POSITIONAL ARGUMENTS
    

`OUTPUT_URL_PREFIX`
     Location for the export metadata and data files. Must be a valid Google Cloud Storage bucket with an optional path prefix. For example: 
    
    
    gcloud datastore export gs://mybucket/my/path

Will place the export in the `mybucket` bucket in objects prefixed with `my/path`. 

FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--kinds`=[`KIND`,…]
     A list specifying what kinds will be included in the operation. When omitted, all Kinds are included. For example, to operate on only the 'Customer' and 'Order' Kinds: 
    
    
    gcloud datastore export --kinds='Customer','Order'

`--namespaces`=[`NAMESPACE`,…]
     A list specifying what namespaces will be included in the operation. When omitted, all namespaces are included in the operation, including the default namespace. To specify that `only` the default namespace should be operated on, use the special symbol '(default)'. For example, to operate on entities from both the 'customers' and default namespaces: 
    
    
    gcloud datastore export --namespaces='(default)','customers'

`--operation-labels`=[`OPERATION_LABEL`,…]
     A string:string map of custom labels to associate with this operation. For example: 
    
    
    gcloud datastore export --operation-labels=comment='customer orders','sales rep'=pending

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha datastore export](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/datastore/export)
    
    
    [gcloud beta datastore export](https://docs.cloud.google.com/sdk/gcloud/reference/beta/datastore/export)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-30 UTC."],[],[]] 
