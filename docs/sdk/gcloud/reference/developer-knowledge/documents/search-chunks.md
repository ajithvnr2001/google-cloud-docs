---
url: https://docs.cloud.google.com/sdk/gcloud/reference/developer-knowledge/documents/search-chunks/
title: gcloud developer-knowledge documents search-chunks \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:00:38.487365+00:00
---

# gcloud developer-knowledge documents search-chunks  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/developer-knowledge/documents/search-chunks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud developer-knowledge documents search-chunks Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud developer-knowledge documents search-chunks - search for developer knowledge across Google's developer documentation 
SYNOPSIS
    

`gcloud developer-knowledge documents search-chunks` `--query`=`QUERY` [`--query-filter`=`QUERY_FILTER`] [`--filter`=`EXPRESSION`] [`--limit`=`LIMIT`; default=5] [`--page-size`=`PAGE_SIZE`] [`--sort-by`=[`FIELD`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Search for developer knowledge across Google's developer documentation. Return DocumentChunks based on the user's query. 

There may be many chunks from the same Document. To retrieve full documents, use `[gcloud alpha developer-knowledge documents describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/developer-knowledge/documents/describe)` with the DocumentChunk.parent returned in the search-chunks results. 

EXAMPLES
     To search for document chunks answering a query: 
    
    
    gcloud developer-knowledge documents search-chunks --query="How to create a Cloud Storage bucket?"

To search for document chunks filtered by data source: 
    
    
    gcloud developer-knowledge documents search-chunks --query="Cloud Functions deployment" --query-filter='data_source = "docs.cloud.google.com"'

To search with custom pagination: 
    
    
    gcloud developer-knowledge documents search-chunks --query="Compute Engine instances" --page-size=10 --limit=20

REQUIRED FLAGS
    

`--query`=`QUERY`
     Raw query string provided by the user, such as "How to create a Cloud Storage bucket?". 
FLAGS
    

`--query-filter`=`QUERY_FILTER`
     Apply a strict filter to the search results. Supported filter fields: `data_source`, `update_time`, `uri`. Example: `data_source = "docs.cloud.google.com"`. 
LIST COMMAND FLAGS
    

`--filter`=`EXPRESSION`
     Apply a Boolean filter `EXPRESSION` to each resource item to be listed. If the expression evaluates `True`, then that item is listed. For more details and examples of filter expressions, run $ [gcloud topic filters](https://docs.cloud.google.com/sdk/gcloud/reference/topic/filters). This flag interacts with other flags that are applied in this order: `--flatten`, `--sort-by`, `--filter`, `--limit`. 
`--limit`=`LIMIT`; default=5
     Maximum number of resources to list. The default is `5`. This flag interacts with other flags that are applied in this order: `--flatten`, `--sort-by`, `--filter`, `--limit`. 
`--page-size`=`PAGE_SIZE`
     Some services group resource list output into pages. This flag specifies the maximum number of resources per page. The default is determined by the service if it supports paging, otherwise it is `unlimited` (no paging). Paging may be applied before or after `--filter` and `--limit` depending on the service. 
`--sort-by`=[`FIELD`,…]
     Comma-separated list of resource field key names to sort by. The default order is ascending. Prefix a field with ``~´´ for descending order on that field. This flag interacts with other flags that are applied in this order: `--flatten`, `--sort-by`, `--filter`, `--limit`. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the developerknowledge API. The full documentation for this API can be found at: <https://developers.google.com/knowledge>
GUIDANCE
     When searching for information, use `search-chunks` first to discover relevant document chunks, and then use `describe` on the chunk's parent to retrieve the full document if necessary. 
NOTES
     These variants are also available: 
    
    
    [gcloud alpha developer-knowledge documents search-chunks](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/developer-knowledge/documents/search-chunks)
    
    
    [gcloud beta developer-knowledge documents search-chunks](https://docs.cloud.google.com/sdk/gcloud/reference/beta/developer-knowledge/documents/search-chunks)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-22 UTC."],[],[]] 
