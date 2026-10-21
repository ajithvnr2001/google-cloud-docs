---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/project-info/set-default-service-account/
title: gcloud alpha compute project-info set-default-service-account \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T11:28:45.484256+00:00
---

# gcloud alpha compute project-info set-default-service-account  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/project-info/set-default-service-account/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha compute project-info set-default-service-account Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha compute project-info set-default-service-account - set the default service account on the project 
SYNOPSIS
    

`gcloud alpha compute project-info set-default-service-account` [`--service-account`=`SERVICE_ACCOUNT` | `--no-service-account`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` `gcloud alpha compute project-info set-default-service-account` is used to configure the default service account on project. 

The project's default service account is used when a new instance is created unless a custom service account is set via --scopes or --no-scopes. Existing instances are not affected. 

For example, 
    
    
    gcloud alpha compute project-info set-default-service-account --service-account=example@developers.gserviceaccount.com
    [gcloud compute instances create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create) instance-name

will set the project's default service account as example@developers.gserviceaccount.com. The instance created will have example@developers.gserviceaccount.com as the service account associated with because no service account email was specified in the "instances create" command. 

To remove the default service account from the project, issue the command: 
    
    
    gcloud alpha compute project-info set-default-service-account --no-service-account

The required permission to execute this command is `compute.projects.setDefaultServiceAccount`. If needed, you can include this permission, or choose any of the following preexisting IAM roles that contain this particular permission: 

  * Owner 
  * Editor 
  * Compute Admin 


FLAGS
    

At most one of these can be specified: 

`--service-account`=`SERVICE_ACCOUNT`
     The email address of the service account that will be set as the default service account for all newly created instances in the project. 

To set the default service account to example@project.iam.gserviceaccount.com: 
    
    
    gcloud alpha compute project-info set-default-service-account --service-account example@project.iam.gserviceaccount.com

`--no-service-account`
     Sets the default service account on the project as no service account. This causes newly created instances to not run as a service account by default. 

To set the default service account as no service account, specify this flag: 
    
    
    gcloud alpha compute project-info set-default-service-account --no-service-account

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
