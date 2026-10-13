---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dlp/images/redact/
title: gcloud alpha dlp images redact \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:54:16.439800+00:00
---

# gcloud alpha dlp images redact  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dlp/images/redact/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha dlp images redact Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha dlp images redact - redact potentially sensitive data from image content 
SYNOPSIS
    

`gcloud alpha dlp images redact` `IMAGE` [`--include-quote`] [`--info-types`=[`INFOTYPE`,…]] [`--min-likelihood`=`MIN_LIKELIHOOD`; default="possible"] [`--output-file`=`OUTPUT_FILE`] [`--redact-all-text`] [`--redact-color`=`REDACT_COLOR`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Redact potentially sensitive data from image content. 
EXAMPLES
     To redact phone numbers from an image named my-image.jpg and write the redacted image to my-redacted-image.jpg, run: 
    
    
    gcloud alpha dlp images redact my-image.jpg --info-types PHONE_NUMBER --output-file my-redacted-image.jpg

POSITIONAL ARGUMENTS
    

`IMAGE`
     Image file to search for sensitive info. The file type must be one of PNG, JPEG, SVG, or BMP. 
FLAGS
    

`--include-quote`
     If True, a contextual quote from the data that triggered a finding is included in the response. Even if the content is not text, it may be converted to a textual representation in the response. For example, given the input value 'My phone number is (415) 555-0890' and a search for the infoType PHONE_NUMBER, the contextual quote would be '(415) 555-0890.' 
`--info-types`=[`INFOTYPE`,…]
     Which infoTypes to scan input for. The values must correspond to infoType values found in documentation. For more information about valid infoTypes, see [infoTypes Reference](https://cloud.google.com/dlp/docs/infotypes-reference)
`--min-likelihood`=`MIN_LIKELIHOOD`; default="possible"
     Only return findings equal to or above this threshold. `MIN_LIKELIHOOD` must be one of: `likely`, `possible`, `unlikely`, `very-likely`, `very-unlikely`. 
`--output-file`=`OUTPUT_FILE`
     Path to the file to write redacted contents to. 
`--redact-all-text`
     If specified, all text info in the image will be removed, whether it is detected as sensitive or not. 
`--redact-color`=`REDACT_COLOR`
     The color to use when redacting content from an image. If not specified, the default value is black. Colors should be specified as a string of `r,g,b` float values in the interval [0,1] representing the amount of red, green, and blue in the color, respectively. For example, `black = 0,0,0`, `red = 1.0,0,0`, `white = 1.0,1.0,1.0`, and so on. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `dlp/v2` API. The full documentation for this API can be found at: <https://cloud.google.com/sensitive-data-protection/docs/>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
