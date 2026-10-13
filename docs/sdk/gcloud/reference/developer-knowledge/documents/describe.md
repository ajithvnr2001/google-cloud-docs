---
url: https://docs.cloud.google.com/sdk/gcloud/reference/developer-knowledge/documents/describe/
title: gcloud developer-knowledge documents describe \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:50:36.840371+00:00
---

# gcloud developer-knowledge documents describe  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/developer-knowledge/documents/describe/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud developer-knowledge documents describe Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud developer-knowledge documents describe - retrieve a single document with its full Markdown content 
SYNOPSIS
    

`gcloud developer-knowledge documents describe` `NAME` [`--view`=`VIEW`; default="content"] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Retrieve a single document and metadata based on its resource name/URI. 
EXAMPLES
     To retrieve the full Markdown content along with the metadata of a document, run: 
    
    
    gcloud developer-knowledge documents describe documents/docs.cloud.google.com/storage/docs/creating-buckets

To retrieve only the basic metadata (like title and data source) of a specific document, run: 
    
    
    gcloud developer-knowledge documents describe documents/docs.cloud.google.com/storage/docs/creating-buckets --view=basic

To retrieve the complete document record, including all available backend fields, metadata, and full Markdown content, run: 
    
    
    gcloud developer-knowledge documents describe documents/docs.cloud.google.com/storage/docs/creating-buckets --view=full

POSITIONAL ARGUMENTS
    

`NAME`
     The resource name of the document to retrieve. Format: `documents/{uri_without_scheme}` (e.g., `documents/docs.cloud.google.com/storage/docs/creating-buckets`). 
FLAGS
    

`--view`=`VIEW`; default="content"
     Specify which fields of the document are included in the response. `VIEW` must be one of: 

`basic`
     Include basic metadata fields (e.g., URI, data source, title). 
`content`
     Include basic fields and the Markdown content. 
`full`
     Include all document fields. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `developerknowledge/v1` API. The full documentation for this API can be found at: <https://developers.google.com/knowledge>
NOTES
     These variants are also available: 
    
    
    [gcloud alpha developer-knowledge documents describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/developer-knowledge/documents/describe)
    
    
    [gcloud beta developer-knowledge documents describe](https://docs.cloud.google.com/sdk/gcloud/reference/beta/developer-knowledge/documents/describe)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-22 UTC."],[],[]] 
