---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataplex/entries/search/
title: gcloud alpha dataplex entries search \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:17:40.672211+00:00
---

# gcloud alpha dataplex entries search  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataplex/entries/search/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha dataplex entries search Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha dataplex entries search - searches for Dataplex entries 
SYNOPSIS
    

`gcloud alpha dataplex entries search` `QUERY` `--project`=`PROJECT` [`--limit`=`LIMIT`] [`--order-by`=`ORDER_BY`] [`--page-size`=`PAGE_SIZE`] [`--scope`=`SCOPE`] [`--semantic-search`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Searches for entries matching given query and scope. 
EXAMPLES
     To search project 'my-project' for Dataplex resources that match the simple predicate 'foo': 
    
    
    gcloud alpha dataplex entries search 'foo' --project=my-project

POSITIONAL ARGUMENTS
    

`QUERY`
     The query against which entries in scope should be matched. 
REQUIRED FLAGS
    

`--project`=`PROJECT`
     The project to which the request should be attributed. 
OPTIONAL FLAGS
    

`--limit`=`LIMIT`
     Maximum number of resources. 
`--order-by`=`ORDER_BY`
     Specifies the ordering of results, currently supported case-sensitive choices are: 

  * `title [asc|desc]`, defaults to ascending if not specified. 


`--page-size`=`PAGE_SIZE`
     Maximum number of resources per page. No more than 500. 
`--scope`=`SCOPE`
     The scope under which the search should be operating. Should either be organizations/<org_id> or projects/<project_ref>. If left unspecified, it will default to the organization where the project is located. 
`--semantic-search`
     Specifies whether the search should understand the meaning and intent behind the query, rather than just matching keywords. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `dataplex/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/dataplex/docs>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud dataplex entries search](https://docs.cloud.google.com/sdk/gcloud/reference/dataplex/entries/search)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
