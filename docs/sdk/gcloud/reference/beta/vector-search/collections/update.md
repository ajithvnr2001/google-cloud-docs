---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/vector-search/collections/update/
title: gcloud beta vector-search collections update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:12:06.225393+00:00
---

# gcloud beta vector-search collections update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/vector-search/collections/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta vector-search collections update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta vector-search collections update - update a collection 
SYNOPSIS
    

`gcloud beta vector-search collections update` (`COLLECTION` : `--location`=`LOCATION`) [`--async`] [`--data-schema`=`DATA_SCHEMA`] [`--description`=`DESCRIPTION`] [`--display-name`=`DISPLAY_NAME`] [`--request-id`=`REQUEST_ID`] [`--schema`=`SCHEMA`] [`--labels`=[`LABELS`,…] | `--update-labels`=[`UPDATE_LABELS`,…] `--clear-labels` | `--remove-labels`=`REMOVE_LABELS`] [`--vector-schema`=[`VECTOR_SCHEMA`,…] | `--update-vector-schema`=[`UPDATE_VECTOR_SCHEMA`,…] `--clear-vector-schema` | `--remove-vector-schema`=`REMOVE_VECTOR_SCHEMA`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Update a collection. 
EXAMPLES
     To update a collection `my-collection` in project `my-project` and location `us-central1`, run: 
    
    
    gcloud beta vector-search collections update my-collection --location=us-central1 --display-name='My Updated Collection' --project=my-project

POSITIONAL ARGUMENTS
    

Collection resource - Identifier. name of resource The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `collection` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`COLLECTION`
     ID of the collection or fully qualified identifier for the collection. 

To set the `collection` attribute: 

  * provide the argument `collection` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location id of the collection resource. 

To set the `location` attribute: 

  * provide the argument `collection` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--data-schema`=`DATA_SCHEMA`
     JSON Schema for data. Field names must contain only alphanumeric characters, underscores, and hyphens. The schema must be compliant with [JSON Schema Draft 7](https://json-schema.org/draft-07/schema). 
`--description`=`DESCRIPTION`
     User-specified description of the collection 
`--display-name`=`DISPLAY_NAME`
     User-specified display name of the collection 
`--request-id`=`REQUEST_ID`
     An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. 

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. 

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 

`--schema`=`SCHEMA`
     Deprecated: JSON Schema for data. Please use data_schema instead. 
Update labels. 

At most one of these can be specified: 

`--labels`=[`LABELS`,…]
     Set labels to new value. Labels as key value pairs. 

`KEY`
     Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 
`VALUE`
     Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 
`Shorthand Example:`
    
    
    --labels=string=string

`JSON Example:`
    
    
    --labels='{"string": "string"}'

`File Example:`
    
    
    --labels=path_to_file.(yaml|json)

Or at least one of these can be specified: 

`--update-labels`=[`UPDATE_LABELS`,…]
     Update labels value or add key value pair. Labels as key value pairs. 

`KEY`
     Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 
`VALUE`
     Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 
`Shorthand Example:`
    
    
    --update-labels=string=string

`JSON Example:`
    
    
    --update-labels='{"string": "string"}'

`File Example:`
    
    
    --update-labels=path_to_file.(yaml|json)

At most one of these can be specified: 

`--clear-labels`
     Clear labels value and set to empty map. 
`--remove-labels`=`REMOVE_LABELS`
     Remove existing value from map labels. Sets `remove_labels` value. `Shorthand Example:`
    
    
    --remove-labels=string,string

`JSON Example:`
    
    
    --remove-labels=["string"]

`File Example:`
    
    
    --remove-labels=path_to_file.(yaml|json)

Update vector_schema. 

At most one of these can be specified: 

`--vector-schema`=[`VECTOR_SCHEMA`,…]
     Set vector_schema to new value. Schema for vector fields. Only vector fields in this schema will be searchable. Field names must contain only alphanumeric characters, underscores, and hyphens. 

`KEY`
     Sets `KEY` value. 
`VALUE`
     Sets `VALUE` value. 

`denseVector`
     Dense vector field. 

`dimensions`
     Dimensionality of the vector field. 
`vertexEmbeddingConfig`
     Configuration for generating embeddings for the vector field. If not specified, the embedding field must be populated in the DataObject. 

`modelId`
     Required: ID of the embedding model to use. See <https://cloud.google.com/vertex-ai/generative-ai/docs/learn/models#embeddings-models> for the list of supported models. 
`taskType`
     Required: Task type for the embeddings. 
`textTemplate`
     Required: Text template for the input to the model. The template must contain one or more references to fields in the DataObject, e.g.: "Movie Title: {title} \---- Movie Plot: {plot}". 
`sparseVector`
     Sparse vector field. 
`Shorthand Example:`
    
    
    --vector-schema=string={denseVector={dimensions=int,vertexEmbeddingConfig={modelId=string,taskType=string,textTemplate=string}},sparseVector}

`JSON Example:`
    
    
    --vector-schema='{"string": {"denseVector": {"dimensions": int, "vertexEmbeddingConfig": {"modelId": "string", "taskType": "string", "textTemplate": "string"}}, "sparseVector": {}}}'

`File Example:`
    
    
    --vector-schema=path_to_file.(yaml|json)

Or at least one of these can be specified: 

`--update-vector-schema`=[`UPDATE_VECTOR_SCHEMA`,…]
     Update vector_schema value or add key value pair. Schema for vector fields. Only vector fields in this schema will be searchable. Field names must contain only alphanumeric characters, underscores, and hyphens. 

`KEY`
     Sets `KEY` value. 
`VALUE`
     Sets `VALUE` value. 

`denseVector`
     Dense vector field. 

`dimensions`
     Dimensionality of the vector field. 
`vertexEmbeddingConfig`
     Configuration for generating embeddings for the vector field. If not specified, the embedding field must be populated in the DataObject. 

`modelId`
     Required: ID of the embedding model to use. See <https://cloud.google.com/vertex-ai/generative-ai/docs/learn/models#embeddings-models> for the list of supported models. 
`taskType`
     Required: Task type for the embeddings. 
`textTemplate`
     Required: Text template for the input to the model. The template must contain one or more references to fields in the DataObject, e.g.: "Movie Title: {title} \---- Movie Plot: {plot}". 
`sparseVector`
     Sparse vector field. 
`Shorthand Example:`
    
    
    --update-vector-schema=string={denseVector={dimensions=int,vertexEmbeddingConfig={modelId=string,taskType=string,textTemplate=string}},sparseVector}

`JSON Example:`
    
    
    --update-vector-schema='{"string": {"denseVector": {"dimensions": int, "vertexEmbeddingConfig": {"modelId": "string", "taskType": "string", "textTemplate": "string"}}, "sparseVector": {}}}'

`File Example:`
    
    
    --update-vector-schema=path_to_file.(yaml|json)

At most one of these can be specified: 

`--clear-vector-schema`
     Clear vector_schema value and set to empty map. 
`--remove-vector-schema`=`REMOVE_VECTOR_SCHEMA`
     Remove existing value from map vector_schema. Sets `remove_vector_schema` value. `Shorthand Example:`
    
    
    --remove-vector-schema=string,string

`JSON Example:`
    
    
    --remove-vector-schema=["string"]

`File Example:`
    
    
    --remove-vector-schema=path_to_file.(yaml|json)

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `vectorsearch/v1beta` API. The full documentation for this API can be found at: <https://docs.cloud.google.com/vertex-ai/docs/vector-search-2/overview>
NOTES
     This command is currently in beta and might change without notice. This variant is also available: 
    
    
    [gcloud vector-search collections update](https://docs.cloud.google.com/sdk/gcloud/reference/vector-search/collections/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
