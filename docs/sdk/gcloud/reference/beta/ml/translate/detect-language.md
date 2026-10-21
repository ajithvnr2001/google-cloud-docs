---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/ml/translate/detect-language/
title: gcloud beta ml translate detect-language \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:38:59.279183+00:00
---

# gcloud beta ml translate detect-language  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/ml/translate/detect-language/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta ml translate detect-language Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta ml translate detect-language - use the Google Cloud Translation API to detect languages 
SYNOPSIS
    

`gcloud beta ml translate detect-language` (`--content`=`CONTENT` | `--content-file`=`CONTENT_FILE`) [`--mime-type`=`MIME_TYPE`] [`--model`=`MODEL`] [`--zone`=`ZONE`; default="global"] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Detects the language of text in a request. 
EXAMPLES
     The following command detects the language of 'What beautiful weather!' 
    
    
    gcloud beta ml translate detect-language --content='What beautiful weather!' --zone=us-central1

REQUIRED FLAGS
    

Contents group. 

Exactly one of these must be specified: 

`--content`=`CONTENT`
     Content of the input in string format. 
`--content-file`=`CONTENT_FILE`
     Specify a local file path with content. 
OPTIONAL FLAGS
    

`--mime-type`=`MIME_TYPE`
     Format of the source text, for example, 'text/html', 'text/plain'. Defaults to 'text/html'. 
`--model`=`MODEL`
     Language detection model to be used. If not specified, the default (language-detection/default) model is used. Authorization requires the following Google IAM permission on the specified resource model: 
    
    
    cloudtranslate.languageDetectionModels.predict

`--zone`=`ZONE`; default="global"
     Location to make calls. Non-global location is required for requests using AutoML models. Currently, only 'us-central1' is supported as a non-global location. Defaults to 'global'. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `translate/v3` API. The full documentation for this API can be found at: <https://cloud.google.com/translate/docs/quickstarts>
NOTES
     This command is currently in beta and might change without notice. This variant is also available: 
    
    
    [gcloud alpha ml translate detect-language](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/ml/translate/detect-language)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
