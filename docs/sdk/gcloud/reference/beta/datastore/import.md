---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/datastore/import/
title: gcloud beta datastore import \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:18:47.311367+00:00
---

# gcloud beta datastore import  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/datastore/import/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta datastore import Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta datastore import - import Cloud Datastore entities from Google Cloud Storage 
SYNOPSIS
    

`gcloud beta datastore import` `INPUT_URL` [`--async`] [`--kinds`=[`KIND`,…]] [`--namespaces`=[`NAMESPACE`,…]] [`--operation-labels`=[`OPERATION_LABEL`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Imports entities into Google Cloud Datastore. Existing entities with the same key are overwritten. The import occurs in the background and its progress can be monitored and managed via the Operation resource that is created. If an Import operation is cancelled, it is possible that a subset of the data has already been imported to Cloud Datastore. This data will not be removed. 
EXAMPLES
     To import all data exported to the output URL `gs://exampleBucket/exampleExport/exampleExport.overall_export_metadata`, run: 
    
    
    gcloud beta datastore import gs://exampleBucket/exampleExport/exampleExport.overall_export_metadata

To import all data exported to the output URL `gs://exampleBucket/exampleExport/exampleExport.overall_export_metadata` without waiting for the operation to complete, run: 
    
    
    gcloud beta datastore import gs://exampleBucket/exampleExport/exampleExport.overall_export_metadata --async

To import only the `exampleKind` from the data exported to the output URL `gs://exampleBucket/exampleExport/exampleExport.overall_export_metadata`, run: 
    
    
    gcloud beta datastore import gs://exampleBucket/exampleExport/exampleExport.overall_export_metadata --kinds='exampleKind'

POSITIONAL ARGUMENTS
    

`INPUT_URL`
     Location of the import metadata. Must be a valid Google Cloud Storage object. The file extension is 'overall_export_metadata'. 

This location is the 'output_url' field of a previous export, and can be found via the 'operations describe' command. 

FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--kinds`=[`KIND`,…]
     A list specifying what kinds will be included in the operation. When omitted, all Kinds are included. For example, to operate on only the 'Customer' and 'Order' Kinds: 
    
    
    gcloud beta datastore import --kinds='Customer','Order'

`--namespaces`=[`NAMESPACE`,…]
     A list specifying what namespaces will be included in the operation. When omitted, all namespaces are included in the operation, including the default namespace. To specify that `only` the default namespace should be operated on, use the special symbol '(default)'. For example, to operate on entities from both the 'customers' and default namespaces: 
    
    
    gcloud beta datastore import --namespaces='(default)','customers'

`--operation-labels`=[`OPERATION_LABEL`,…]
     A string:string map of custom labels to associate with this operation. For example: 
    
    
    gcloud beta datastore import --operation-labels=comment='customer orders','sales rep'=pending

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud datastore import](https://docs.cloud.google.com/sdk/gcloud/reference/datastore/import)
    
    
    [gcloud alpha datastore import](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/datastore/import)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
