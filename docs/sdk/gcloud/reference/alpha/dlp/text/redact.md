---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dlp/text/redact/
title: gcloud alpha dlp text redact \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:43:44.207643+00:00
---

# gcloud alpha dlp text redact  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dlp/text/redact/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha dlp text redact Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha dlp text redact - redact potentially sensitive data from text content 
SYNOPSIS
    

`gcloud alpha dlp text redact` `--info-types`=[`INFOTYPE`,…] (`--content`=`CONTENT` | `--content-file`=`PATH_TO_FILE`) (`--remove-findings` | `--replace-with-info-type` | `--replacement-text`=`REPLACEMENT_TEXT`) [`--min-likelihood`=`MIN_LIKELIHOOD`; default="possible"] [`--output-file`=`OUTPUT_FILE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Redacts potentially sensitive data from text content. 
EXAMPLES
     To redact email addresses from a file named my-data.csv and write the redacted contents to my-redacted-data.csv, run: 
    
    
    gcloud alpha dlp text redact --info-types EMAIL_ADDRESS --replace-with-info-type --content-file my-data.csv --output-file my-redacted-data.csv

REQUIRED FLAGS
    

`--info-types`=[`INFOTYPE`,…]
     Which infoTypes to scan input for. The values must correspond to infoType values found in documentation. For more information about valid infoTypes, see [infoTypes Reference](https://cloud.google.com/dlp/docs/infotypes-reference)
Exactly one of these must be specified: 

`--content`=`CONTENT`
     Text content to redact sensitive data from. 
`--content-file`=`PATH_TO_FILE`
     Text file to scan for sensitive data to redact. Can also be a CSV file specifying tabular data. For CSV files, up to 50,000 values per request are allowed. To read from stdin pass '-' as the file name. Use a full or relative path to a local file containing the value of content_file. 
Exactly one of these must be specified: 

`--remove-findings`
     If specified, all sensitive data will be removed, instead of replaced. 
`--replace-with-info-type`
     If specified, all sensitive data will be replaced with its infoType. For example, 'email:guest@example.com' would become 'email:[EMAIL_ADDRESS]'. 
`--replacement-text`=`REPLACEMENT_TEXT`
     Text to replace each sensitive data finding with. 
OPTIONAL FLAGS
    

`--min-likelihood`=`MIN_LIKELIHOOD`; default="possible"
     Only return findings equal to or above this threshold. `MIN_LIKELIHOOD` must be one of: `likely`, `possible`, `unlikely`, `very-likely`, `very-unlikely`. 
`--output-file`=`OUTPUT_FILE`
     Path to the file to write redacted contents to. 
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
