---
url: https://docs.cloud.google.com/sdk/gcloud/reference/gemini/gibq-observability-settings/create/
title: gcloud gemini gibq-observability-settings create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:03:08.476305+00:00
---

# gcloud gemini gibq-observability-settings create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/gemini/gibq-observability-settings/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud gemini gibq-observability-settings create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud gemini gibq-observability-settings create - create gibqObservabilitySettings 
SYNOPSIS
    

`gcloud gemini gibq-observability-settings create` (`GIBQ_OBSERVABILITY_SETTING` : `--location`=`LOCATION`) [`--labels`=[`LABELS`,…]] [`--request-id`=`REQUEST_ID`] [`--conversational-analytics-setting-feedback-enabled` `--conversational-analytics-setting-logging-enabled` `--conversational-analytics-setting-metrics-enabled` `--conversational-analytics-setting-traces-enabled`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Create a gibqObservabilitySetting 
EXAMPLES
     To create the gibqObservabilitySetting, run: 
    
    
    gcloud gemini gibq-observability-settings create

POSITIONAL ARGUMENTS
    

GibqObservabilitySetting resource - Identifier. Name of the resource. Format:projects/{project}/locations/{location}/gibqObservabilitySettings/{gibq_observability_setting} The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `gibq_observability_setting` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`GIBQ_OBSERVABILITY_SETTING`
     ID of the gibqObservabilitySetting or fully qualified identifier for the gibqObservabilitySetting. 

To set the `gibq_observability_setting` attribute: 

  * provide the argument `gibq_observability_setting` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location id of the gibqObservabilitySetting resource. 

To set the `location` attribute: 

  * provide the argument `gibq_observability_setting` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


FLAGS
    

`--labels`=[`LABELS`,…]
     Labels as key value pairs. 

`KEY`
     Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 
`VALUE`
     Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 
`Shorthand Example:`
    
    
    --labels=string=string

`JSON Example:`
    
    
    --labels='{"string": "string"}'

`File Example:`
    
    
    --labels=path_to_file.(yaml|json)

`--request-id`=`REQUEST_ID`
     An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. 

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. 

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 

Message describing Setting for Conversational Analytics. 
`--conversational-analytics-setting-feedback-enabled`
     Whether to enable feedback. 
`--conversational-analytics-setting-logging-enabled`
     Whether to enable logging. 
`--conversational-analytics-setting-metrics-enabled`
     Whether to enable metrics. 
`--conversational-analytics-setting-traces-enabled`
     Whether to enable traces. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `cloudaicompanion/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/gemini>

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
