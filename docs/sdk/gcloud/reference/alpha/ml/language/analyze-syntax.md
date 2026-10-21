---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/ml/language/analyze-syntax/
title: gcloud alpha ml language analyze-syntax \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:33:55.363035+00:00
---

# gcloud alpha ml language analyze-syntax  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/ml/language/analyze-syntax/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha ml language analyze-syntax Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha ml language analyze-syntax - use Google Cloud Natural Language API to identify linguistic information 
SYNOPSIS
    

`gcloud alpha ml language analyze-syntax` (`--content`=`CONTENT` | `--content-file`=`CONTENT_FILE`) [`--content-type`=`CONTENT_TYPE`; default="plain-text"] [`--encoding-type`=`ENCODING_TYPE`; default="utf8"] [`--language`=`LANGUAGE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Syntactic Analysis extracts linguistic information, breaking up the given text into a series of sentences and tokens (generally, word boundaries), providing further analysis on those tokens. 

Currently English, Spanish, Japanese, Chinese (Simplified and Traditional), French, German, Italian, Korean, and Portuguese are supported. 

EXAMPLES
     To analyze syntax in raw content 'They drink.': 
    
    
    gcloud alpha ml language analyze-syntax --content='They drink'

To analyze syntax in file 'myfile.txt': 
    
    
    gcloud alpha ml language analyze-syntax --content-file='myfile.txt'

To analyze syntax in a remote file 'gs://bucket_name/mycontent.html' for Japanese language using UTF-8 encoding: 
    
    
    gcloud alpha ml language analyze-syntax --content-file='gs://bucket_name/mycontent.html' --content-type=HTML --encoding-type=utf8 --language=ja-JP

REQUIRED FLAGS
    

Exactly one of these must be specified: 

`--content`=`CONTENT`
     Specify input text on the command line. Useful for experiments, or for extremely short text. 
`--content-file`=`CONTENT_FILE`
     Specify a local file or Google Cloud Storage (format `gs://bucket/object`) file path containing the text to be analyzed. More useful for longer text or data output from another system. 
OPTIONAL FLAGS
    

`--content-type`=`CONTENT_TYPE`; default="plain-text"
     Specify the format of the input text. `CONTENT_TYPE` must be one of: `html`, `plain-text`. 
`--encoding-type`=`ENCODING_TYPE`; default="utf8"
     The encoding type used by the API to calculate offsets. If set to `none`, encoding-dependent offsets will be set at -1. This is an optional flag only used for the entity mentions in results, and does not affect how the input is read or analyzed. `ENCODING_TYPE` must be one of: `none`, `utf16`, `utf32`, `utf8`. 
`--language`=`LANGUAGE`
     Specify the language of the input text. If omitted, the server will attempt to auto-detect. Both ISO (such as `en` or `es`) and BCP-47 (such as `en-US` or `ja-JP`) language codes are accepted. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `language/v1beta2` API. The full documentation for this API can be found at: <https://cloud.google.com/natural-language/>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud ml language analyze-syntax](https://docs.cloud.google.com/sdk/gcloud/reference/ml/language/analyze-syntax)
    
    
    [gcloud beta ml language analyze-syntax](https://docs.cloud.google.com/sdk/gcloud/reference/beta/ml/language/analyze-syntax)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
