---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/vector-search/collections/data-objects/create/
title: gcloud beta vector-search collections data-objects create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:20:59.913987+00:00
---

# gcloud beta vector-search collections data-objects create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/vector-search/collections/data-objects/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta vector-search collections data-objects create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta vector-search collections data-objects create - create a data object 
SYNOPSIS
    

`gcloud beta vector-search collections data-objects create` (`DATA_OBJECT` : `--collection`=`COLLECTION` `--location`=`LOCATION`) [`--data`=`DATA`] [`--etag`=`ETAG`] [`--vectors`=[`VECTORS`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Create a data object. 
EXAMPLES
     To create a data object `my-do-1` in collection `my-collection`, project `my-project` and location `us-central1`, run: 
    
    
    gcloud beta vector-search collections data-objects create my-do-1 --collection=my-collection --location=us-central1 --data='{"director":"Frank
     Darabont","genre":"Drama","title":"The Shawshank
     Redemption","year":1994}' \
        --vectors='{"genre_embedding":{"dense":{"values":[0.4,0.5,0.6,0.\
    7]}},"plot_embedding":{"dense":{"values":[0.1,0.2,0.3]}},"sparse_emb\
    edding":{"sparse":{"indices":[1,5,10],"values":[0.1,0.5,0.21]}}}' \
        --project=my-project

POSITIONAL ARGUMENTS
    

DataObject resource - Identifier. The fully qualified resource name of the dataObject. 

Format: `projects/{project}/locations/{location}/collections/{collection}/dataObjects/{data_object_id}` The data_object_id must be 1-63 characters long, and comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt). The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

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
    

`--data`=`DATA`
     The data of the dataObject. 
`--etag`=`ETAG`
     The etag of the dataObject. 
`--vectors`=[`VECTORS`,…]
     The vectors of the dataObject. 

`KEY`
     Sets `KEY` value. 
`VALUE`
     Sets `VALUE` value. 

`dense`
     A dense vector. 

`values`
     The values of the vector. 
`sparse`
     A sparse vector. 

`indices`
     The corresponding indices for the values. 
`values`
     The values of the vector. 
`values`
     Deprecated: Use `dense` or `sparse` instead. 
`Shorthand Example:`
    
    
    --vectors=string={dense={values=[float]},sparse={indices=[int],values=[float]},values=[float]}

`JSON Example:`
    
    
    --vectors='{"string": {"dense": {"values": [float]}, "sparse": {"indices": [int], "values": [float]}, "values": [float]}}'

`File Example:`
    
    
    --vectors=path_to_file.(yaml|json)

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `vectorsearch/v1beta` API. The full documentation for this API can be found at: <https://docs.cloud.google.com/vertex-ai/docs/vector-search-2/overview>
NOTES
     This command is currently in beta and might change without notice. This variant is also available: 
    
    
    [gcloud vector-search collections data-objects create](https://docs.cloud.google.com/sdk/gcloud/reference/vector-search/collections/data-objects/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
