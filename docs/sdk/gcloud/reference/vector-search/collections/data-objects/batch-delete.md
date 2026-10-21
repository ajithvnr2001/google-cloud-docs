---
url: https://docs.cloud.google.com/sdk/gcloud/reference/vector-search/collections/data-objects/batch-delete/
title: gcloud vector-search collections data-objects batch-delete \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:59:38.007135+00:00
---

# gcloud vector-search collections data-objects batch-delete  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/vector-search/collections/data-objects/batch-delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud vector-search collections data-objects batch-delete Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud vector-search collections data-objects batch-delete - delete a batch of data objects 
SYNOPSIS
    

`gcloud vector-search collections data-objects batch-delete` `--requests`=[`etag`=`ETAG`],[`name`=`NAME`] (`--collection`=`COLLECTION` : `--location`=`LOCATION`) [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Delete a batch of data objects. 
EXAMPLES
     To delete a batch of data objects in collection `my-collection`, project `my-project` and location `us-central1`, run: 
    
    
    gcloud vector-search collections data-objects batch-delete --collection=my-collection --location=us-central1 --requests='[{"name":"projects/my-project/locations/us-central1/collections/my-collection/dataObjects/my-do-b1"},{"name":"projects/my-project/locations/us-central1/collections/my-collection/dataObjects/my-do-b2"}]' --project=my-project

REQUIRED FLAGS
    

`--requests`=[`etag`=`ETAG`],[`name`=`NAME`]
     Required, The request message specifying the resources to delete. A maximum of 1000 DataObjects can be deleted in a batch. 

`etag`
     The current etag of the DataObject. If an etag is provided and does not match the current etag of the DataObject, deletion will be blocked and an ABORTED error will be returned. 
`name`
     The name of the DataObject resource to be deleted. Format: `projects/{project}/locations/{location}/collections/{collection}/dataObjects/{dataObject}`. 
`Shorthand Example:`
    
    
    --requests=etag=string,name=string --requests=etag=string,name=string

`JSON Example:`
    
    
    --requests='[{"etag": "string", "name": "string"}]'

`File Example:`
    
    
    --requests=path_to_file.(yaml|json)

Collection resource - The resource name of the Collection to delete the DataObjects in. Format: `projects/{project}/locations/{location}/collections/{collection}`. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--collection` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`--collection`=`COLLECTION`
     ID of the collection or fully qualified identifier for the collection. 

To set the `collection` attribute: 

  * provide the argument `--collection` on the command line. 



This flag argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location id of the collection resource. 

To set the `location` attribute: 

  * provide the argument `--collection` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `vectorsearch/v1` API. The full documentation for this API can be found at: <https://docs.cloud.google.com/vertex-ai/docs/vector-search-2/overview>
NOTES
     This variant is also available: 
    
    
    [gcloud beta vector-search collections data-objects batch-delete](https://docs.cloud.google.com/sdk/gcloud/reference/beta/vector-search/collections/data-objects/batch-delete)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
