---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/vector-search/collections/data-objects/delete/
title: gcloud beta vector-search collections data-objects delete \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:21:00.005441+00:00
---

# gcloud beta vector-search collections data-objects delete  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/vector-search/collections/data-objects/delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta vector-search collections data-objects delete Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta vector-search collections data-objects delete - delete a data object 
SYNOPSIS
    

`gcloud beta vector-search collections data-objects delete` (`DATA_OBJECT` : `--collection`=`COLLECTION` `--location`=`LOCATION`) [`--etag`=`ETAG`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Delete a data object. 
EXAMPLES
     To delete a data object `my-do-1` from collection `my-collection`, project `my-project` and location `us-central1`, run: 
    
    
    gcloud beta vector-search collections data-objects delete my-do-1 --collection=my-collection --location=us-central1 --project=my-project

POSITIONAL ARGUMENTS
    

DataObject resource - The name of the DataObject resource to be deleted. Format: `projects/{project}/locations/{location}/collections/{collection}/dataObjects/{dataObject}` The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `data_object` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`DATA_OBJECT`
     ID of the dataObject or fully qualified identifier for the dataObject. 

To set the `data_object` attribute: 

  * provide the argument `data_object` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--collection`=`COLLECTION`
     The collection id of the dataObject resource. 

To set the `collection` attribute: 

  * provide the argument `data_object` on the command line with a fully specified name; 
  * provide the argument `--collection` on the command line. 


`--location`=`LOCATION`
     The location id of the dataObject resource. 

To set the `location` attribute: 

  * provide the argument `data_object` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


FLAGS
    

`--etag`=`ETAG`
     The current etag of the DataObject. If an etag is provided and does not match the current etag of the DataObject, deletion will be blocked and an ABORTED error will be returned. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `vectorsearch/v1beta` API. The full documentation for this API can be found at: <https://docs.cloud.google.com/vertex-ai/docs/vector-search-2/overview>
NOTES
     This command is currently in beta and might change without notice. This variant is also available: 
    
    
    [gcloud vector-search collections data-objects delete](https://docs.cloud.google.com/sdk/gcloud/reference/vector-search/collections/data-objects/delete)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
