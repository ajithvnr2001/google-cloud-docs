---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/ml/language/classify-text/
title: gcloud beta ml language classify-text \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:22:33.677524+00:00
---

# gcloud beta ml language classify-text  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/ml/language/classify-text/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta ml language classify-text Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta ml language classify-text - classifies input document into categories 
SYNOPSIS
    

`gcloud beta ml language classify-text` (`--content`=`CONTENT` | `--content-file`=`CONTENT_FILE`) [`--content-type`=`CONTENT_TYPE`; default="plain-text"] [`--language`=`LANGUAGE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Classifies input document into categories. Returns a list of categories representing the document. Only the most relevant categories a document are returned e.g. if `/Science` and `/Science/Astronomy` both apply to a document, then only the `/Science/Astronomy` category is returned, as it is the more specific result. 

Currently only English is supported for this feature. 

EXAMPLES
     To classify text in raw content 'Long Political Text.': 
    
    
    gcloud beta ml language classify-text --content='Long Political Text.'

To classify text in file 'myfile.txt': 
    
    
    gcloud beta ml language classify-text --content-file='myfile.txt'

To classify text in a remote file 'gs://bucket_name/mycontent.html' for Japanese language: 
    
    
    gcloud beta ml language classify-text --content-file='gs://bucket_name/mycontent.html' --content-type=HTML --language=ja-JP

REQUIRED FLAGS
    

Exactly one of these must be specified: 

`--content`=`CONTENT`
     Specify input text on the command line. Useful for experiments, or for extremely short text. 
`--content-file`=`CONTENT_FILE`
     Specify a local file or Google Cloud Storage (format `gs://bucket/object`) file path containing the text to be analyzed. More useful for longer text or data output from another system. 
OPTIONAL FLAGS
    

`--content-type`=`CONTENT_TYPE`; default="plain-text"
     Specify the format of the input text. `CONTENT_TYPE` must be one of: `html`, `plain-text`. 
`--language`=`LANGUAGE`
     Specify the language of the input text. If omitted, the server will attempt to auto-detect. Both ISO (such as `en` or `es`) and BCP-47 (such as `en-US` or `ja-JP`) language codes are accepted. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `language/v1beta2` API. The full documentation for this API can be found at: <https://cloud.google.com/natural-language/>
NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud ml language classify-text](https://docs.cloud.google.com/sdk/gcloud/reference/ml/language/classify-text)
    
    
    [gcloud alpha ml language classify-text](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/ml/language/classify-text)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
