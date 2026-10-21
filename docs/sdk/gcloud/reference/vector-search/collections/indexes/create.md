---
url: https://docs.cloud.google.com/sdk/gcloud/reference/vector-search/collections/indexes/create/
title: gcloud vector-search collections indexes create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:55:24.297850+00:00
---

# gcloud vector-search collections indexes create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/vector-search/collections/indexes/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud vector-search collections indexes create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud vector-search collections indexes create - create an index 
SYNOPSIS
    

`gcloud vector-search collections indexes create` (`INDEX` : `--collection`=`COLLECTION` `--location`=`LOCATION`) `--index-field`=`INDEX_FIELD` [`--async`] [`--dense-scann-feature-norm-type`=`DENSE_SCANN_FEATURE_NORM_TYPE`] [`--description`=`DESCRIPTION`] [`--display-name`=`DISPLAY_NAME`] [`--distance-metric`=`DISTANCE_METRIC`] [`--filter-fields`=[`FILTER_FIELDS`,…]] [`--labels`=[`LABELS`,…]] [`--request-id`=`REQUEST_ID`] [`--store-fields`=[`STORE_FIELDS`,…]] [`--dedicated-infrastructure-mode`=`DEDICATED_INFRASTRUCTURE_MODE` `--dedicated-infrastructure-autoscaling-spec-max-replica-count`=`DEDICATED_INFRASTRUCTURE_AUTOSCALING_SPEC_MAX_REPLICA_COUNT` `--dedicated-infrastructure-autoscaling-spec-min-replica-count`=`DEDICATED_INFRASTRUCTURE_AUTOSCALING_SPEC_MIN_REPLICA_COUNT`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Create an index. 
EXAMPLES
     To create an index `my-index` on field `my-embedding-field` for collection `my-collection` in project `my-project` and location `us-central1`, run: 
    
    
    gcloud vector-search collections indexes create my-index --collection=my-collection --location=us-central1 --index-field='my-embedding-field' --display-name='My Index' --project=my-project

To create an index `my-index-2` on field `my-embedding-field` for collection `my-collection` in project `my-project` and location `us-central1`, with filter fields `genre` and `year` and store fields `title`, run: 
    
    
    gcloud vector-search collections indexes create my-index-2 --collection=my-collection --location=us-central1 --index-field='my-embedding-field' --display-name='My Index 2' --filter-fields=genre,year --store-fields=title --project=my-project

POSITIONAL ARGUMENTS
    

Index resource - Identifier. name of resource The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `index` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`INDEX`
     ID of the index or fully qualified identifier for the index. 

To set the `index` attribute: 

  * provide the argument `index` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--collection`=`COLLECTION`
     The collection id of the index resource. 

To set the `collection` attribute: 

  * provide the argument `index` on the command line with a fully specified name; 
  * provide the argument `--collection` on the command line. 


`--location`=`LOCATION`
     The location id of the index resource. 

To set the `location` attribute: 

  * provide the argument `index` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


REQUIRED FLAGS
    

`--index-field`=`INDEX_FIELD`
     The collection schema field to index. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
Arguments for the index type. 
Dense ScaNN index configuration. 
`--dense-scann-feature-norm-type`=`DENSE_SCANN_FEATURE_NORM_TYPE`
     Feature norm type. `DENSE_SCANN_FEATURE_NORM_TYPE` must be one of: 

`none`
     No norm applied. 
`unit-l2-norm`
     Unit L2 norm. 
`--description`=`DESCRIPTION`
     User-specified description of the index 
`--display-name`=`DISPLAY_NAME`
     User-specified display name of the index 
`--distance-metric`=`DISTANCE_METRIC`
     Distance metric used for indexing. If not specified, will default to DOT_PRODUCT. `DISTANCE_METRIC` must be one of: 

`cosine-distance`
     Cosine distance metric. 
`dot-product`
     Dot product distance metric. 
`--filter-fields`=[`FILTER_FIELDS`,…]
     The fields to push into the index to enable fast ANN inline filtering. 
`--labels`=[`LABELS`,…]
     Labels as key value pairs. 

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

`--request-id`=`REQUEST_ID`
     An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. 

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. 

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 

`--store-fields`=[`STORE_FIELDS`,…]
     The fields to push into the index to enable inline data retrieval. 
Arguments for the infra type. 
Represents dedicated infrastructure for the index. 
Arguments for the mode. 
`--dedicated-infrastructure-mode`=`DEDICATED_INFRASTRUCTURE_MODE`
     Mode of the dedicated infrastructure. `DEDICATED_INFRASTRUCTURE_MODE` must be one of: 

`performance-optimized`
     This is Performance optimized on E2 or equivalent family. 
`storage-optimized`
     This is storage optimized variation. 
Specification for autoscaling. 
`--dedicated-infrastructure-autoscaling-spec-max-replica-count`=`DEDICATED_INFRASTRUCTURE_AUTOSCALING_SPEC_MAX_REPLICA_COUNT`
     The maximum number of replicas. Must be >= `min_replica_count` and <= `1000`. For the v1beta version, if not set or set to `0`, defaults to the greater of `min_replica_count` and `5`. For all other versions, if not set or set to `0`, defaults to the greater of `min_replica_count` and `2`. 
`--dedicated-infrastructure-autoscaling-spec-min-replica-count`=`DEDICATED_INFRASTRUCTURE_AUTOSCALING_SPEC_MIN_REPLICA_COUNT`
     The minimum number of replicas. If not set or set to `0`, defaults to `2`. Must be >= `1` and <= `1000`. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `vectorsearch/v1` API. The full documentation for this API can be found at: <https://docs.cloud.google.com/vertex-ai/docs/vector-search-2/overview>
NOTES
     This variant is also available: 
    
    
    [gcloud beta vector-search collections indexes create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/vector-search/collections/indexes/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
