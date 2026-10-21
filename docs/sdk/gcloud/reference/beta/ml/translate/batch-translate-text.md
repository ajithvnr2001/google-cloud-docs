---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/ml/translate/batch-translate-text/
title: gcloud beta ml translate batch-translate-text \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:38:59.024143+00:00
---

# gcloud beta ml translate batch-translate-text  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/ml/translate/batch-translate-text/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta ml translate batch-translate-text Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta ml translate batch-translate-text - translates a large volume of text in asynchronous batch mode 
SYNOPSIS
    

`gcloud beta ml translate batch-translate-text` `--destination`=`DESTINATION` `--source`=[`FILE_PATH`[=`FILE_TYPE`],…] `--source-language`=`SOURCE_LANGUAGE` `--target-language-codes`=[`TARGET_LANGUAGE_CODES`,…] [`--glossaries`=[`KEY`=`VALUE`,…]] [`--models`=[`KEY`=`VALUE`,…]] [`--zone`=`ZONE`; default="global"] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Translates a large volume of text in asynchronous batch mode. This command provides real-time output as the inputs are being processed. 
EXAMPLES
     The following command translates 'input.txt' file into French and Spanish: 
    
    
    gcloud beta ml translate batch-translate-text --source=gs://input.txt=text/plain --zone=us-central1 --target-language-codes=fr-CA,es-ES --source-language=en-US --models=fr-CA=TRL321456,es-ES=general/base --destination=gs://output

REQUIRED FLAGS
    

`--destination`=`DESTINATION`
     Location to which the results should be written. Must be a Google Cloud Storage URI. 
`--source`=[`FILE_PATH`[=`FILE_TYPE`],…]
     Comma-separated list of entries of the form FILE_PATH[=FILE_TYPE] specifying source files and files types for the translation. FILE_PATH must be a Google Cloud Storage URI. FILE_TYPE defaults to 'text/html' if not present. Possible FILE_TYPES are 'text/html', 'text/plain'. 

Usage: 

'--source gs://input/input.txt=text/plain,gs://input/my.html=text/html' 

`--source-language`=`SOURCE_LANGUAGE`
     Source language code of the text. 
`--target-language-codes`=[`TARGET_LANGUAGE_CODES`,…]
     The languages to which the text is to be translated. Specify up to 10 language codes here. 
OPTIONAL FLAGS
    

`--glossaries`=[`KEY`=`VALUE`,…]
     Glossaries to be applied for translation. Comma-separated dictionary where map's key is target language code, map's value is glossary name. 
`--models`=[`KEY`=`VALUE`,…]
     Models to use for translation. Comma-separated dictionary where map's key is target language code, map's value is model name. Value can be a built-in general model, or an AutoML Translation model. 

Usage: 

'--models es-ES=TRL321456789,en-US=general/nmt' 

`--zone`=`ZONE`; default="global"
     Location to make calls. Non-global location is required for requests using AutoML models. Currently, only 'us-central1' is supported as a non-global location. Defaults to 'global'. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `translate/v3` API. The full documentation for this API can be found at: <https://cloud.google.com/translate/docs/quickstarts>
NOTES
     This command is currently in beta and might change without notice. This variant is also available: 
    
    
    [gcloud alpha ml translate batch-translate-text](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/ml/translate/batch-translate-text)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
