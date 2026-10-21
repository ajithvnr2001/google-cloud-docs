---
url: https://docs.cloud.google.com/sdk/gcloud/reference/workspace-add-ons/deployments/replace/
title: gcloud workspace-add-ons deployments replace \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:23:25.655161+00:00
---

# gcloud workspace-add-ons deployments replace  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/workspace-add-ons/deployments/replace/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud workspace-add-ons deployments replace Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud workspace-add-ons deployments replace - replace a Google Workspace Add-ons deployment 
SYNOPSIS
    

`gcloud workspace-add-ons deployments replace` `DEPLOYMENT` (`--deployment-file`=`DEPLOYMENT_FILE` | `--deployment-object`=`DEPLOYMENT_OBJECT`) [`--etag`=`ETAG`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Replace a Google Workspace Add-ons deployment 
EXAMPLES
     To replace an deployment called `my-deployment` with the deployment file, run: 
    
    
    gcloud workspace-add-ons deployments replace my-deployment --deployment-file=my-deployment.json

To replace an deployment called `my-deployment` with the deployment object, run: 
    
    
    gcloud workspace-add-ons deployments replace my-deployment --deployment-object=my-deployment-string

POSITIONAL ARGUMENTS
    

Deployment resource - Google Workspace Add-ons deployment to replace This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `deployment` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`DEPLOYMENT`
     ID of the deployment or fully qualified identifier for the deployment. 

To set the `deployment` attribute: 

  * provide the argument `deployment` on the command line. 


REQUIRED FLAGS
    

Exactly one of these must be specified: 

`--deployment-file`=`DEPLOYMENT_FILE`
     path to the deployment file 
`--deployment-object`=`DEPLOYMENT_OBJECT`
     json string of the deploymentObject 
OPTIONAL FLAGS
    

`--etag`=`ETAG`
     etag of the deployment file 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `gsuiteaddons/v1` API. The full documentation for this API can be found at: <https://developers.google.com/workspace/add-ons/guides/alternate-runtimes>

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
