---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/gemini/cloud-assist/investigations/update/
title: gcloud beta gemini cloud-assist investigations update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:40:46.826038+00:00
---

# gcloud beta gemini cloud-assist investigations update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/gemini/cloud-assist/investigations/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta gemini cloud-assist investigations update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta gemini cloud-assist investigations update - update an existing investigation 
SYNOPSIS
    

`gcloud beta gemini cloud-assist investigations update` `INVESTIGATION` [`--issue`=`ISSUE`] [`--end-time`=`END_TIME` | `--clear-end-time`] [`--resources`=[`RESOURCE`,…] | `--clear-resources`] [`--start-time`=`START_TIME` | `--clear-start-time`] [`--title`=`TITLE` | `--clear-title`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Shows metadata for the investigation after updating. 

This command can fail for the following reasons: 

  * The investigation ID doesn't exist. 
  * The active account does not have permission to update the investigation. 
  * The investigation is currently running. 


EXAMPLES
     The following command updates title, text description, resources, and start time of the existing investigation with the name`example-foo-bar-1`: 
    
    
    gcloud beta gemini cloud-assist investigations update example-foo-bar-1 --title="Example Investigation" --issue="I have a problem" --start-time=2025-07-10

`
POSITIONAL ARGUMENTS
    

Investigation resource - The investigation name to update. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `investigation` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `investigation` on the command line with a fully specified name; 
  * The default is `global`. 



This must be specified. 

`INVESTIGATION`
     ID of the investigation or fully qualified identifier for the investigation. 

To set the `investigation` attribute: 

  * provide the argument `investigation` on the command line. 


FLAGS
    

`--issue`=`ISSUE`
     A description of the issue you are investigating, or an error log. 
At most one of these can be specified: 

`--end-time`=`END_TIME`
     The estimated end time of the issue you are investigating. 
`--clear-end-time`
     Clear the end time of the investigation. 
At most one of these can be specified: 

`--resources`=[`RESOURCE`,…]
     A list of resources relevant to the investigation 
`--clear-resources`
     Clear the resources of the investigation. 
At most one of these can be specified: 

`--start-time`=`START_TIME`
     The estimated start time of the issue you are investigating. 
`--clear-start-time`
     Clear the start time of the investigation. 
At most one of these can be specified: 

`--title`=`TITLE`
     The desired title of the resulting investigation. 
`--clear-title`
     Clear the title of the investigation. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
