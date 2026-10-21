---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/model-armor/templates/sanitize-user-prompt/
title: gcloud beta model-armor templates sanitize-user-prompt \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T20:44:44.595045+00:00
---

# gcloud beta model-armor templates sanitize-user-prompt  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/model-armor/templates/sanitize-user-prompt/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta model-armor templates sanitize-user-prompt Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta model-armor templates sanitize-user-prompt - sanitize User Prompt 
SYNOPSIS
    

`gcloud beta model-armor templates sanitize-user-prompt` (`TEMPLATE` : `--location`=`LOCATION`) [`--multi-language-detection-metadata-enable`] [`--multi-language-detection-metadata-source`=`MULTI_LANGUAGE_DETECTION_METADATA_SOURCE`] [`--user-prompt-data-text`=`USER_PROMPT_DATA_TEXT` | `--byte-item-data-type`=`BYTE_ITEM_DATA_TYPE` (`--byte-item-data`=`BYTE_ITEM_DATA` | `--byte-item-data-from-file`=`PATH_TO_FILE`)] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Sanitizes a user prompt. 
EXAMPLES
     To sanitize a user prompt, run: 
    
    
    gcloud beta model-armor templates sanitize-user-prompt my-template --location=us-central1 --user-prompt-data="test-user-prompt"

POSITIONAL ARGUMENTS
    

Template resource - Represents resource name of template e.g. name=projects/sample-project/locations/us-central1/templates/templ01 The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `template` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`TEMPLATE`
     ID of the template or fully qualified identifier for the template. 

To set the `template` attribute: 

  * provide the argument `template` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location id of the template resource. 

To set the `location` attribute: 

  * provide the argument `template` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


FLAGS
    

`--multi-language-detection-metadata-enable`
     Enable detection of multi-language prompts and responses. 
`--multi-language-detection-metadata-source`=`MULTI_LANGUAGE_DETECTION_METADATA_SOURCE`
     Optional Source language of the user prompt. 

If multi-language detection is enabled but language is not set in that case we would automatically detect the source language. 

Arguments for the data item. 

At most one of these can be specified: 

`--user-prompt-data-text`=`USER_PROMPT_DATA_TEXT`
     Plaintext string data for sanitization. 
Or at least one of these can be specified: 

Represents Byte Data item. 
`--byte-item-data-type`=`BYTE_ITEM_DATA_TYPE`
     The type of byte data. `BYTE_ITEM_DATA_TYPE` must be one of: 

`csv`
     CSV 
`excel-document`
     XLSX, XLSM, XLTX, XLYM 
`pdf`
     PDF 
`plaintext-utf8`
     plain text 
`powerpoint-document`
     PPTX, PPTM, POTX, POTM, POT 
`txt`
     TXT 
`word-document`
     DOCX, DOCM, DOTX, DOTM 
This flag argument must be specified if any of the other arguments in this group are specified. 
Exactly one of these must be specified: 

`--byte-item-data`=`BYTE_ITEM_DATA`
     Bytes Data 
`--byte-item-data-from-file`=`PATH_TO_FILE`
     Bytes Data. Use a full or relative path to a local file containing the value of byte_item_data. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `modelarmor/v1beta` API. The full documentation for this API can be found at: <https://cloud.google.com/security-command-center/docs/model-armor-overview>
NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud model-armor templates sanitize-user-prompt](https://docs.cloud.google.com/sdk/gcloud/reference/model-armor/templates/sanitize-user-prompt)
    
    
    [gcloud alpha model-armor templates sanitize-user-prompt](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/model-armor/templates/sanitize-user-prompt)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
