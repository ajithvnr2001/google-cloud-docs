---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/firestore/import/
title: gcloud alpha firestore import \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:34:45.310738+00:00
---

# gcloud alpha firestore import  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/firestore/import/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha firestore import Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha firestore import - import Cloud Firestore documents from Google Cloud Storage 
SYNOPSIS
    

`gcloud alpha firestore import` `INPUT_URI_PREFIX` [`--async`] [`--collection-ids`=[`COLLECTION_GROUP_IDS`,…]] [`--database`=`DATABASE`; default="(default)"] [`--namespace-ids`=[`NAMESPACE_IDS`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` import Cloud Firestore documents from Google Cloud Storage. 
EXAMPLES
     To import all collection groups from `mybucket/my/path`, run: 
    
    
    gcloud alpha firestore import gs://mybucket/my/path

To import a specific set of collections groups asynchronously, run: 
    
    
    gcloud alpha firestore import gs://mybucket/my/path --collection-ids='specific collection group1','specific
     collection group2' --async

To import all collection groups from certain namespace, run: 
    
    
    gcloud alpha firestore import gs://mybucket/my/path --namespace-ids='specific namespace id'

POSITIONAL ARGUMENTS
    

`INPUT_URI_PREFIX`
     Location of the import files. 

This location is the 'output_uri_prefix' field of a previous export, and can be found via the 'gcloud alpha firestore operations describe' command. 

FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--collection-ids`=[`COLLECTION_GROUP_IDS`,…]
     List specifying which collection groups will be included in the operation. When omitted, all collection groups are included. 

For example, to operate on only the `customers` and `orders` collections groups: 
    
    
    gcloud alpha firestore import --collection-ids='customers','orders'

`--database`=`DATABASE`; default="(default)"
     The database to operate on. The default value is `(default)`. 

For example, to operate on database `foo`: 
    
    
    gcloud alpha firestore import --database='foo'

`--namespace-ids`=[`NAMESPACE_IDS`,…]
     List specifying which namespaces will be included in the operation. When omitted, all namespaces are included. 

This is only supported for Datastore Mode databases. 

For example, to operate on only the `customers` and `orders` namespaces: 
    
    
    gcloud alpha firestore import --namespaces-ids='customers','orders'

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud firestore import](https://docs.cloud.google.com/sdk/gcloud/reference/firestore/import)
    
    
    [gcloud beta firestore import](https://docs.cloud.google.com/sdk/gcloud/reference/beta/firestore/import)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
