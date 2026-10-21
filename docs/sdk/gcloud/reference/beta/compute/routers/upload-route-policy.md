---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/routers/upload-route-policy/
title: gcloud beta compute routers upload-route-policy \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T11:35:15.164587+00:00
---

# gcloud beta compute routers upload-route-policy  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/routers/upload-route-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta compute routers upload-route-policy Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta compute routers upload-route-policy - upload a route policy into a Compute Engine router 
SYNOPSIS
    

`gcloud beta compute routers upload-route-policy` `NAME` `--file-name`=`FILE_NAME` [`--file-format`=`FILE_FORMAT`] [`--policy-name`=`POLICY_NAME`] [`--region`=`REGION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` `gcloud beta compute routers upload-route-policy` uploads a route policy into a Compute Engine router. 
EXAMPLES
     To upload a route policy `my-import-policy` from a file `my-import-policy.yaml` into a router `my-router` in region `us-central1`, run: 
    
    
    gcloud beta compute routers upload-route-policy my-router --region=us-central1 --policy-name=my-import-policy --file-name=my-import-policy.yaml"

POSITIONAL ARGUMENTS
    

`NAME`
     Name of the router to upload. 
REQUIRED FLAGS
    

`--file-name`=`FILE_NAME`
     Local path to the file defining the policy 
OPTIONAL FLAGS
    

`--file-format`=`FILE_FORMAT`
     Format of the file passed to --file-name. `FILE_FORMAT` must be one of: `json`, `yaml`. 
`--policy-name`=`POLICY_NAME`
     Name of the route policy to add/replace. 
`--region`=`REGION`
     Region of the router to upload. If not specified, you might be prompted to select a region (interactive mode only). 

To avoid prompting when this flag is omitted, you can set the ``compute/region`` property: 
    
    
    [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) compute/region REGION

A list of regions can be fetched by running: 
    
    
    [gcloud compute regions list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/regions/list)

To unset the property, run: 
    
    
    [gcloud config unset](https://docs.cloud.google.com/sdk/gcloud/reference/config/unset) compute/region

Alternatively, the region can be stored in the environment variable ``CLOUDSDK_COMPUTE_REGION``. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud compute routers upload-route-policy](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/upload-route-policy)
    
    
    [gcloud alpha compute routers upload-route-policy](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/routers/upload-route-policy)
    
    
    [gcloud preview compute routers upload-route-policy](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/routers/upload-route-policy)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
