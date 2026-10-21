---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/ai-platform/models/create/
title: gcloud beta ai-platform models create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:25:43.757925+00:00
---

# gcloud beta ai-platform models create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/ai-platform/models/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta ai-platform models create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta ai-platform models create - create a new AI Platform model 
SYNOPSIS
    

`gcloud beta ai-platform models create` `MODEL` [`--description`=`DESCRIPTION`] [`--enable-console-logging`] [`--enable-logging`] [`--labels`=[`KEY`=`VALUE`,…]] [`--region`=`REGION` | `--regions`=`REGION`,[`REGION`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Create a new AI Platform model. 
POSITIONAL ARGUMENTS
    

`MODEL`
     Name of the model. 
FLAGS
    

`--description`=`DESCRIPTION`
     Description of the model. 
`--enable-console-logging`
     If set, enables StackDriver Logging of stderr and stdout streams for online prediction. These logs are more verbose than the standard access logs and can be helpful for debugging. 
`--enable-logging`
     If set, enables StackDriver Logging for online prediction. These logs are like standard server access logs, containing information such as timestamps and latency for each request. 
`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

At most one of these can be specified: 

`--region`=`REGION`
     Google Cloud region of the regional endpoint to use for this command. 

If you specify this flag, do not specify `--regions`. 

If you specify `--region=global`, the model will be deployed to 'us-central1' by default using the global endpoint. Please use `--regions` only if you want to change the region where the model will be deployed against the global endpoint. 

If both flags are unspecified and you don't set ``ai_platform/region``, you will be prompted for region of the regional endpoint. 

Learn more about regional endpoints and see a list of available regions: <https://cloud.google.com/ai-platform/prediction/docs/regional-endpoints>

`REGION` must be one of: `global`, `asia-east1`, `asia-northeast1`, `asia-southeast1`, `australia-southeast1`, `europe-west1`, `europe-west2`, `europe-west3`, `europe-west4`, `northamerica-northeast1`, `us-central1`, `us-east1`, `us-east4`, `us-west1`. 

`--regions`=`REGION`,[`REGION`,…]
     The Google Cloud region where the model will be deployed (currently only a single region is supported) against the global endpoint. 

If you specify this flag, do not specify `--region`. 

Defaults to 'us-central1' while using the global endpoint. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud ai-platform models create](https://docs.cloud.google.com/sdk/gcloud/reference/ai-platform/models/create)
    
    
    [gcloud alpha ai-platform models create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/models/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
