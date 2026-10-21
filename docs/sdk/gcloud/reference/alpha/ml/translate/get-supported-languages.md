---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/ml/translate/get-supported-languages/
title: gcloud alpha ml translate get-supported-languages \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:47:22.539353+00:00
---

# gcloud alpha ml translate get-supported-languages  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/ml/translate/get-supported-languages/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha ml translate get-supported-languages Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha ml translate get-supported-languages - returns a list of supported languages for translation 
SYNOPSIS
    

`gcloud alpha ml translate get-supported-languages` [`--display-language-code`=`DISPLAY_LANGUAGE_CODE`] [`--model`=`MODEL`] [`--zone`=`ZONE`; default="global"] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` List supported languages for translation. 
EXAMPLES
     The following command lists supported languages. 
    
    
    gcloud alpha ml translate get-supported-languages --zone=global

FLAGS
    

`--display-language-code`=`DISPLAY_LANGUAGE_CODE`
     The language to use to return localized, human-readable name of supported languages. If missing, then display names aren't returned in the response. 
`--model`=`MODEL`
     Get supported languages of specified model. 

Authorization requires one or more of the following Google IAM permissions on the specified resource model: 
    
    
    cloudtranslate.generalModels.get
    
    
    automl.models.get

Defaults to 'general/base'. 

Usage: 
    
    
    AutoML models: '--model=TRL321456789'
    
    
    General models: '--model=general/nmt'

`--zone`=`ZONE`; default="global"
     Location to make calls. Non-global location is required for requests using AutoML models. Currently, only 'us-central1' is supported as a non-global location. Defaults to 'global'. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `translate/v3beta1` API. The full documentation for this API can be found at: <https://cloud.google.com/translate/docs/quickstarts>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud beta ml translate get-supported-languages](https://docs.cloud.google.com/sdk/gcloud/reference/beta/ml/translate/get-supported-languages)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
