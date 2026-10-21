---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/ai-platform/explain/
title: gcloud beta ai-platform explain \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:25:43.047113+00:00
---

# gcloud beta ai-platform explain  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/ai-platform/explain/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta ai-platform explain Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta ai-platform explain - run AI Platform explanation 
SYNOPSIS
    

`gcloud beta ai-platform explain` `--model`=`MODEL` (`--json-instances`=`JSON_INSTANCES` | `--json-request`=`JSON_REQUEST` | `--text-instances`=`TEXT_INSTANCES`) [`--region`=`REGION`] [`--version`=`VERSION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` `gcloud beta ai-platform explain` sends an explain request to AI Platform for the given instances. This command will read up to 100 instances, though the service itself will accept instances up to the payload limit size (currently, 1.5MB). 
EXAMPLES
     To get explanations for an AI Platform version model with the version 'version' and with the name 'model-name', run: 
    
    
    gcloud beta ai-platform explain explain --model=model-name --version=version --json-instances=instances.json

REQUIRED FLAGS
    

`--model`=`MODEL`
     Name of the model. 
Exactly one of these must be specified: 

`--json-instances`=`JSON_INSTANCES`
     Path to a local file from which instances are read. Instances are in JSON format; newline delimited. 

An example of the JSON instances file: 
    
    
    {"images": [0.0, …, 0.1], "key": 3}
    {"images": [0.0, …, 0.1], "key": 2}
    …

This flag accepts "-" for stdin. 

`--json-request`=`JSON_REQUEST`
     Path to a local file containing the body of JSON request. 

An example of a JSON request: 
    
    
    {
      "instances": [
        {"x": [1, 2], "y": [3, 4]},
        {"x": [-1, -2], "y": [-3, -4]}
      ]
    }

This flag accepts "-" for stdin. 

`--text-instances`=`TEXT_INSTANCES`
     Path to a local file from which instances are read. Instances are in UTF-8 encoded text format; newline delimited. 

An example of the text instances file: 
    
    
    107,4.9,2.5,4.5,1.7
    100,5.7,2.8,4.1,1.3
    …

This flag accepts "-" for stdin. 

OPTIONAL FLAGS
    

`--region`=`REGION`
     Google Cloud region of the regional endpoint to use for this command. For the global endpoint, the region needs to be specified as `global`. 

Learn more about regional endpoints and see a list of available regions: <https://cloud.google.com/ai-platform/prediction/docs/regional-endpoints>

`REGION` must be one of: `global`, `asia-east1`, `asia-northeast1`, `asia-southeast1`, `australia-southeast1`, `europe-west1`, `europe-west2`, `europe-west3`, `europe-west4`, `northamerica-northeast1`, `us-central1`, `us-east1`, `us-east4`, `us-west1`. 

`--version`=`VERSION`
     Model version to be used. 

If unspecified, the default version of the model will be used. To list model versions run 
    
    
    [gcloud beta ai-platform versions list](https://docs.cloud.google.com/sdk/gcloud/reference/beta/ai-platform/versions/list)

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. This variant is also available: 
    
    
    [gcloud alpha ai-platform explain](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/explain)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
