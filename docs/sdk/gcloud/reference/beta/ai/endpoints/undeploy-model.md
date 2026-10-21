---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints/undeploy-model/
title: gcloud beta ai endpoints undeploy-model \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:11:14.475474+00:00
---

# gcloud beta ai endpoints undeploy-model  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints/undeploy-model/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta ai endpoints undeploy-model Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta ai endpoints undeploy-model - undeploy a model from an existing Vertex AI endpoint 
SYNOPSIS
    

`gcloud beta ai endpoints undeploy-model` (`ENDPOINT` : `--region`=`REGION`) `--deployed-model-id`=`DEPLOYED_MODEL_ID` [`--traffic-split`=[`DEPLOYED_MODEL_ID`=`VALUE`,…]] [`GCLOUD_WIDE_FLAG …`]
EXAMPLES
     To undeploy a model ``456`` from an endpoint ``123`` under project ``example`` in region ``us-central1``, run: 
    
    
    gcloud beta ai endpoints undeploy-model 123 --project=example --region=us-central1 --deployed-model-id=456

POSITIONAL ARGUMENTS
    

Endpoint resource - The endpoint to undeploy a model from. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `endpoint` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`ENDPOINT`
     ID of the endpoint or fully qualified identifier for the endpoint. 

To set the `name` attribute: 

  * provide the argument `endpoint` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--region`=`REGION`
     Cloud region for the endpoint. 

To set the `region` attribute: 

  * provide the argument `endpoint` on the command line with a fully specified name; 
  * provide the argument `--region` on the command line; 
  * set the property `ai/region`; 
  * choose one from the prompted list of available regions. 


REQUIRED FLAGS
    

`--deployed-model-id`=`DEPLOYED_MODEL_ID`
     Id of the deployed model. 
OPTIONAL FLAGS
    

`--traffic-split`=[`DEPLOYED_MODEL_ID`=`VALUE`,…]
     List of pairs of deployed model id and value to set as traffic split. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud ai endpoints undeploy-model](https://docs.cloud.google.com/sdk/gcloud/reference/ai/endpoints/undeploy-model)
    
    
    [gcloud alpha ai endpoints undeploy-model](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/ai/endpoints/undeploy-model)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
