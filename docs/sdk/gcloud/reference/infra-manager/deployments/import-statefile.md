---
url: https://docs.cloud.google.com/sdk/gcloud/reference/infra-manager/deployments/import-statefile/
title: gcloud infra-manager deployments import-statefile \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:17:23.664820+00:00
---

# gcloud infra-manager deployments import-statefile  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/infra-manager/deployments/import-statefile/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud infra-manager deployments import-statefile Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud infra-manager deployments import-statefile - import a terraform state file 
SYNOPSIS
    

`gcloud infra-manager deployments import-statefile` (`DEPLOYMENT` : `--location`=`LOCATION`) `--lock-id`=`LOCK_ID` [`--file`=`FILE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     This command generates a signed url to upload a terraform state file. 
EXAMPLES
     Import state file for `my-deployment` with lock-id `1658343229583347`: 
    
    
    gcloud infra-manager deployments import-statefile projects/p1/locations/us-central1/deployments/my-deployment --lock-id=1658343229583347

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


REQUIRED FLAGS
    

`--lock-id`=`LOCK_ID`
     Lock ID of the lock file to verify person importing owns lock. 
OPTIONAL FLAGS
    

`--file`=`FILE`
     File path for importing statefile into a deployment. It specifies the local file path of an existing Terraform statefile to directly upload for a deployment. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
