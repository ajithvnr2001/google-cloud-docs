---
url: https://docs.cloud.google.com/sdk/gcloud/reference/infra-manager/deployments/export-statefile/
title: gcloud infra-manager deployments export-statefile \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:27:05.177750+00:00
---

# gcloud infra-manager deployments export-statefile  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/infra-manager/deployments/export-statefile/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud infra-manager deployments export-statefile Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud infra-manager deployments export-statefile - export a terraform state file 
SYNOPSIS
    

`gcloud infra-manager deployments export-statefile` (`DEPLOYMENT` : `--location`=`LOCATION`) [`--draft`] [`--file`=`FILE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     This command generates a signed url to download a terraform state file. 
EXAMPLES
     Export state file for `my-deployment`: 
    
    
    gcloud infra-manager deployments export-statefile projects/p1/locations/us-central1/deployments/my-deployment

POSITIONAL ARGUMENTS
    

Deployment resource - the deployment to be used as parent. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `DEPLOYMENT` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`DEPLOYMENT`
     ID of the deployment or fully qualified identifier for the deployment. 

To set the `deployment` attribute: 

  * provide the argument `DEPLOYMENT` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The Cloud location for the deployment. 

To set the `location` attribute: 

  * provide the argument `DEPLOYMENT` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `infra-manager/location`. 


FLAGS
    

`--draft`
     If this flag is set to true, the exported deployment state file will be the draft state 
`--file`=`FILE`
     File name for statefile. It is optional and it specifies the filename or complete path for the downloaded statefile. If only a file path is provided, the statefile will be downloaded as "statefile" within that directory. If a filename is included, the statefile will be downloaded with that name. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
