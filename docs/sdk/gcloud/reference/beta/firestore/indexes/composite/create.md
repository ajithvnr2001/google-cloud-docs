---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/firestore/indexes/composite/create/
title: gcloud beta firestore indexes composite create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:16:58.956460+00:00
---

# gcloud beta firestore indexes composite create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/firestore/indexes/composite/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta firestore indexes composite create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta firestore indexes composite create - create a new composite index 
SYNOPSIS
    

`gcloud beta firestore indexes composite create` `--field-config`=[`array-config`=`ARRAY-CONFIG`],[`field-path`=`FIELD-PATH`],[`order`=`ORDER`],[`search-config`=`SEARCH-CONFIG`],[`vector-config`=`VECTOR-CONFIG`] (`--collection-group`=`COLLECTION_GROUP` : `--database`=`DATABASE`) [`--api-scope`=`API_SCOPE`; default="any-api"] [`--async`] [`--density`=`DENSITY`] [`--multikey`] [`--query-scope`=`QUERY_SCOPE`; default="collection"] [`--search-index-options`=[`text-language`=`TEXT-LANGUAGE`],[`text-language-override-field-path`=`TEXT-LANGUAGE-OVERRIDE-FIELD-PATH`]] [`--unique`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Create a new composite index. 
EXAMPLES
     The following command creates a composite index with fields ``user_id`` (in descending order) followed by ``timestamp`` (in descending order) in the ``Events`` collection group. 
    
    
    gcloud beta firestore indexes composite create --collection-group=Events --field-config=field-path=user-id,order=descending --field-config=field-path=timestamp,order=descending
    
    
    gcloud beta firestore indexes composite create --database=(default) --collection-group=Events --field-config=field-path=user-id,order=descending --field-config=field-path=timestamp,order=descending

REQUIRED FLAGS
    

`--field-config`=[`array-config`=`ARRAY-CONFIG`],[`field-path`=`FIELD-PATH`],[`order`=`ORDER`],[`search-config`=`SEARCH-CONFIG`],[`vector-config`=`VECTOR-CONFIG`]
     Required, Configuration for an index field. 

`array-config`
     Specifies the configuration for an array field. The only valid option is 'contains'. Exactly one of 'order', 'array-config', or 'vector-config' must be specified. 
`field-path`
     Required, specifies the field path (e.g. address.city). 
`order`
     Specifies the order. Valid options are 'ascending', 'descending'. Exactly one of 'order', 'array-config', or 'vector-config' must be specified. 
`search-config`
     Specifies the configuration for a search field. An index definition must contain either only 'search-config' fields or only non 'search-config' fields. 

The following shorthand aliases are supported instead of a full 'search-config': 

  * `TEXT_TOKENIZED_MATCH_GLOBALLY`: Tokenized text search with global matching. 
  * `GEO_POINT`: Geo search. 



Examples: 

With alias: 
    
    
    --field-config=field-path=title,search-config=TEXT_TOKENIZED_MATCH_GLOBALLY

Text search: 
    
    
    --field-config=field-path=title,search-config='{"text-spec": {"index-specs": [{"index-type": "tokenized", "match-type": "match-globally"}]}}'

Geo search: 
    
    
    --field-config=field-path=location,search-config='{"geo-spec": {"geo-json-indexing-disabled": true}}'

With file: 
    
    
    --field-config=field-path=text,search-config='/path/to/configs/search-config.json'

For complex configurations, it is recommended to use a file. 

`geo-spec`
     Optional. The specification for building a geo search index for a field. 

`geo-json-indexing-disabled`
     Optional. Disables geoJSON indexing for the field. By default, geoJSON points are indexed. 
`text-spec`
     Optional. The specification for building a text search index for a field. 

`index-specs`
     Optional. Array of specifications for how the field should be indexed. 

`index-type`
     Required. How to index the text field value. 
`match-type`
     Required. How to match the text field value. 
`vector-config`
     Specifies the configuration for a vector field. Exactly one of 'order', 'array-config', or 'vector-config' must be specified. 

`dimension`
     Required, sets `dimension` value. 
`flat`
     Sets `flat` value. 
`Shorthand Example:`
    
    
    --field-config=array-config=string,field-path=string,order=string,search-config=geo-spec={geo-json-indexing-disabled=boolean},text-spec={index-specs=[{index-type=string,match-type=string}]},vector-config={dimension=int,flat} --field-config=array-config=string,field-path=string,order=string,search-config=geo-spec={geo-json-indexing-disabled=boolean},text-spec={index-specs=[{index-type=string,match-type=string}]},vector-config={dimension=int,flat}

`JSON Example:`
    
    
    --field-config='[{"array-config": "string", "field-path": "string", "order": "string", "search-config": {"geo-spec": {"geo-json-indexing-disabled": boolean}, "text-spec": {"index-specs": [{"index-type": "string", "match-type": "string"}]}}, "vector-config": {"dimension": int, "flat": {}}}]'

`File Example:`
    
    
    --field-config=path_to_file.(yaml|json)

Collection group resource - Collection group of the index. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--collection-group` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`--collection-group`=`COLLECTION_GROUP`
     ID of the collection group or fully qualified identifier for the collection group. 

To set the `collection-group` attribute: 

  * provide the argument `--collection-group` on the command line. 



This flag argument must be specified if any of the other arguments in this group are specified. 

`--database`=`DATABASE`
     Database of the collection group. 

To set the `database` attribute: 

  * provide the argument `--collection-group` on the command line with a fully specified name; 
  * provide the argument `--database` on the command line; 
  * the default value of argument [--database] is `(default)`. 


OPTIONAL FLAGS
    

`--api-scope`=`API_SCOPE`; default="any-api"
     Api scope the index applies to. `API_SCOPE` must be one of: `any-api`, `datastore-mode-api`, `mongodb-compatible-api`. 
`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--density`=`DENSITY`
     Density of the index. `DENSITY` must be one of: `dense`, `density-unspecified`, `sparse-all`, `sparse-any`. 
`--multikey`
     Optional. Whether the index is multikey. By default, the index is not multikey. For non-multikey indexes, none of the paths in the index definition reach or traverse an array, except via an explicit array index. For multikey indexes, at most one of the paths in the index definition reach or traverse an array, except via an explicit array index. Violations will result in errors. Note this field only applies to index with 'mongodb-compatible-api' ApiScope. 
`--query-scope`=`QUERY_SCOPE`; default="collection"
     Query scope the index applies to. `QUERY_SCOPE` must be one of: `collection`, `collection-group`, `collection-recursive`, `query-scope-unspecified`. 
`--search-index-options`=[`text-language`=`TEXT-LANGUAGE`],[`text-language-override-field-path`=`TEXT-LANGUAGE-OVERRIDE-FIELD-PATH`]
     Optional. Configuration options for search indexes. 

`text-language`
     Optional. The language to use for text search indexes. Used as the default language if not overridden at the document level by specifying the 'text-language-override-field-path'. The language is specified as a BCP 47 language code. For indexes with 'mongodb-compatible-api' ApiScope: If unspecified, the default language is English. For indexes with 'any-api' ApiScope: If unspecified, the default behavior is autodetect. 
`text-language-override-field-path`
     Optional. The field in the document that specifies which language to use for that specific document. If unspecified, the language is taken from the 'language' document field if it exists or from 'text-language' if it does not. 
`Shorthand Example:`
    
    
    --search-index-options=text-language=string,text-language-override-field-path=string

`JSON Example:`
    
    
    --search-index-options='{"text-language": "string", "text-language-override-field-path": "string"}'

`File Example:`
    
    
    --search-index-options=path_to_file.(yaml|json)

`--unique`
     Optional. Whether it is an unique index. Unique index ensures all values for the indexed field(s) are unique across documents. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the firestore/v1 API. 

The index specification can be found at: <https://firebase.google.com/docs/firestore/reference/rpc/google.firestore.admin.v1#index_1>

The full API documentation can be found at: <https://cloud.google.com/firestore>

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud firestore indexes composite create](https://docs.cloud.google.com/sdk/gcloud/reference/firestore/indexes/composite/create)
    
    
    [gcloud alpha firestore indexes composite create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/firestore/indexes/composite/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-26 UTC."],[],[]] 
