---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/vector-search/collections/data-objects/aggregate/
title: gcloud beta vector-search collections data-objects aggregate \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:20:59.004358+00:00
---

# gcloud beta vector-search collections data-objects aggregate  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/vector-search/collections/data-objects/aggregate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta vector-search collections data-objects aggregate Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta vector-search collections data-objects aggregate - aggregate data objects 
SYNOPSIS
    

`gcloud beta vector-search collections data-objects aggregate` `--aggregation-method`=`AGGREGATION_METHOD` `--collection`=`COLLECTION` `--location`=`LOCATION` [`--json-filter`=`JSON_FILTER`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Aggregate data objects. 
EXAMPLES
     To aggregate data objects from collection `my-collection` in location `us-central1` in project `my-project` with aggregation method `COUNT`, run: 
    
    
    gcloud beta vector-search collections data-objects aggregate --collection=my-collection --location=us-central1 --aggregation-method=count --project=my-project

REQUIRED FLAGS
    

`--aggregation-method`=`AGGREGATION_METHOD`
     The aggregation method to apply to the query. `AGGREGATION_METHOD` must be (only one value is supported): 

`count`
     Count the number of data objects that match the filter. 
`--collection`=`COLLECTION`
     The collection to aggregate data objects from. 
`--location`=`LOCATION`
     Location of the collection. 
OPTIONAL FLAGS
    

`--json-filter`=`JSON_FILTER`
     A filter expression in JSON format to apply to the aggregate, e.g. `'{"genre": {"$eq": "sci-fi"}}'`. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. This variant is also available: 
    
    
    [gcloud vector-search collections data-objects aggregate](https://docs.cloud.google.com/sdk/gcloud/reference/vector-search/collections/data-objects/aggregate)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
