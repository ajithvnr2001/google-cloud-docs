---
url: https://docs.cloud.google.com/sdk/gcloud/reference/data-catalog/search/
title: gcloud data-catalog search \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:13:00.056833+00:00
---

# gcloud data-catalog search  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/data-catalog/search/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud data-catalog search Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud data-catalog search - search Data Catalog for resources that match a query 
SYNOPSIS
    

`gcloud data-catalog search` `QUERY` (`--include-gcp-public-datasets` `--include-organization-ids`=[`ORGANIZATION`,…] `--include-project-ids`=[`PROJECT`,…] `--restricted-locations`=[`LOCATION`,…]) [`--limit`=`LIMIT`] [`--order-by`=`ORDER_BY`] [`--page-size`=`PAGE_SIZE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(DEPRECATED)` This command is deprecated. Please use `[gcloud dataplex entries search](https://docs.cloud.google.com/sdk/gcloud/reference/dataplex/entries/search)` instead. 

Search Data Catalog for resources that match a query. 

EXAMPLES
     To search project 'my-project' for Data Catalog resources that match the simple predicate 'foo': 
    
    
    gcloud data-catalog search 'foo' --include-project-ids=my-project

To search organization '1234' for Data Catalog resources that match entities whose names match the predicate 'foo': 
    
    
    gcloud data-catalog search 'name:foo' --include-organization-ids=1234

POSITIONAL ARGUMENTS
    

`QUERY`
     Query string in search query syntax in Data Catalog. For more information, see: <https://cloud.google.com/data-catalog/docs/how-to/search-reference>
REQUIRED FLAGS
    

Scope. Control the scope of the search. 

At least one of these must be specified: 

`--include-gcp-public-datasets`
     If True, include Google Cloud Platform public datasets in the search results. 
`--include-organization-ids`=[`ORGANIZATION`,…]
     List of Cloud Organization IDs to include in the search. 
`--include-project-ids`=[`PROJECT`,…]
     List of Cloud Project IDs to include in the search. 
`--restricted-locations`=[`LOCATION`,…]
     List of locations to search within. 
LIST COMMAND FLAGS
    

`--limit`=`LIMIT`
     Maximum number of resources to list. The default is `unlimited`. 
`--order-by`=`ORDER_BY`
     Specifies the ordering of results. Defaults to 'relevance'. 

Currently supported case-sensitive choices are: 

  * relevance 
  * last_access_timestamp [asc|desc]: defaults to descending. 
  * last_modified_timestamp [asc|desc]: defaults to descending. 



To order by last modified timestamp ascending, specify: `--order-by="last_modified_timestamp desc"`. 

`--page-size`=`PAGE_SIZE`
     Some services group resource list output into pages. This flag specifies the maximum number of resources per page. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha data-catalog search](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/data-catalog/search)
    
    
    [gcloud beta data-catalog search](https://docs.cloud.google.com/sdk/gcloud/reference/beta/data-catalog/search)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
