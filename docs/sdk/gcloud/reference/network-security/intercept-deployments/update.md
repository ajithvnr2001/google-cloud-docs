---
url: https://docs.cloud.google.com/sdk/gcloud/reference/network-security/intercept-deployments/update/
title: gcloud network-security intercept-deployments update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:35:24.625399+00:00
---

# gcloud network-security intercept-deployments update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/network-security/intercept-deployments/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud network-security intercept-deployments update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud network-security intercept-deployments update - update an Intercept Deployment 
SYNOPSIS
    

`gcloud network-security intercept-deployments update` (`INTERCEPT_DEPLOYMENT` : `--location`=`LOCATION`) [`--async`] [`--description`=`DESCRIPTION`] [`--max-wait`=`MAX_WAIT`; default="20m"] [`--update-labels`=[`KEY`=`VALUE`,…]] [`--clear-labels` | `--remove-labels`=[`KEY`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Update an intercept deployment. Check the progress of deployment update by using `[gcloud network-security intercept-deployments list](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/intercept-deployments/list)`. 

For examples refer to the EXAMPLES section below. 

EXAMPLES
     To update labels k1 and k2, run: 
    
    
    gcloud network-security intercept-deployments update my-deployment --project=my-project --location=us-central1-a --update-labels=k1=v1,k2=v2

To remove labels k3 and k4, run: 
    
    
    gcloud network-security intercept-deployments update my-deployment --project=my-project --location=us-central1-a --remove-labels=k3,k4

To clear all labels from the intercept deployment, run: 
    
    
    gcloud network-security intercept-deployments update my-deploymen --project=my-project --location=us-central1-a --clear-labels

To update description to 'new description', run: 
    
    
    gcloud network-security intercept-deployments update my-deploymen --project=my-project --location=us-central1-a --description="new description"

POSITIONAL ARGUMENTS
    

Intercept deployment resource - Intercept Deployment. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `INTERCEPT_DEPLOYMENT` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`INTERCEPT_DEPLOYMENT`
     ID of the intercept deployment or fully qualified identifier for the intercept deployment. 

To set the `deployment-id` attribute: 

  * provide the argument `INTERCEPT_DEPLOYMENT` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     Location of the intercept deployment. 

To set the `location` attribute: 

  * provide the argument `INTERCEPT_DEPLOYMENT` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. The default is `True`. Enabled by default, use `--no-async` to disable. 
`--description`=`DESCRIPTION`
     Description of the deployment. 
`--max-wait`=`MAX_WAIT`; default="20m"
     Time to synchronously wait for the operation to complete, after which the operation continues asynchronously. Ignored if --no-async isn't specified. See $ [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes) for information on time formats. 
`--update-labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to update. If a label exists, its value is modified. Otherwise, a new label is created. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

At most one of these can be specified: 

`--clear-labels`
     Remove all labels. If `--update-labels` is also specified then `--clear-labels` is applied first. 

For example, to remove all labels: 
    
    
    gcloud network-security intercept-deployments update --clear-labels

To remove all existing labels and create two new labels, ``foo`` and ``baz``: 
    
    
    gcloud network-security intercept-deployments update --clear-labels --update-labels foo=bar,baz=qux

`--remove-labels`=[`KEY`,…]
     List of label keys to remove. If a label does not exist it is silently ignored. If `--update-labels` is also specified then `--update-labels` is applied first. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha network-security intercept-deployments update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/network-security/intercept-deployments/update)
    
    
    [gcloud beta network-security intercept-deployments update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security/intercept-deployments/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
