---
url: https://docs.cloud.google.com/sdk/gcloud/reference/iap/settings/get/
title: gcloud iap settings get \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:14:18.409610+00:00
---

# gcloud iap settings get  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/iap/settings/get/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud iap settings get Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud iap settings get - get the setting for an IAP resource 
SYNOPSIS
    

`gcloud iap settings get` [`--folder`=`FOLDER` `--organization`=`ORGANIZATION` `--project`=`PROJECT` `--region`=`REGION` `--resource-type`=`RESOURCE_TYPE` `--service`=`SERVICE` `--version`=`VERSION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Get the setting for an IAP resource. 
EXAMPLES
     To get the IAP setting for the resources within an organization, run: 
    
    
    gcloud iap settings get --organization=ORGANIZATION_ID

To get the IAP setting for the resources within a folder, run: 
    
    
    gcloud iap settings get --folder=FOLDER_ID

To get the IAP setting for the resources within a project, run: 
    
    
    gcloud iap settings get --project=PROJECT_ID

To get the IAP setting for web type resources within a project, run: 
    
    
    gcloud iap settings get --project=PROJECT_ID --resource-type=iap_web

To get the IAP setting for all app engine services within a project, run: 
    
    
    gcloud iap settings get --project=PROJECT_ID --resource-type=app-engine

To get the IAP setting for an app engine service within a project, run: 
    
    
    gcloud iap settings get --project=PROJECT_ID --resource-type=app-engine --service=SERVICE_ID

To get the IAP setting for an app engine service version within a project, run: 
    
    
    gcloud iap settings get --project=PROJECT_ID --resource-type=app-engine --service=SERVICE_ID --version=VERSION_ID

To get the IAP setting for all backend services within a project, run: 
    
    
    gcloud iap settings get --project=PROJECT_ID --resource-type=backend-services

To get the IAP setting for a backend service within a project, run: 
    
    
    gcloud iap settings get --project=PROJECT_ID --resource-type=backend-services --service=SERVICE_ID

To get the IAP setting for a regional backend service within a project, run: 
    
    
    gcloud iap settings get --project=PROJECT_ID --resource-type=backend-services --service=SERVICE_ID --region=REGION_ID

To get the IAP setting for all forwarding rules within a project, run: 
    
    
    gcloud iap settings get --project=PROJECT_ID --resource-type=forwarding-rule

To get the IAP setting for a forwarding rule within a project, run: 
    
    
    gcloud iap settings get --project=PROJECT_ID --resource-type=forwarding-rule --service=SERVICE_ID

To get the IAP setting for a regional forwarding rule within a project, run: 
    
    
    gcloud iap settings get --project=PROJECT_ID --resource-type=forwarding-rule --service=SERVICE_ID --region=REGION_ID

To get the IAP setting for all Cloud Run services within a region of a project, run: 
    
    
    gcloud iap settings get --project=PROJECT_ID --resource-type=cloud-run --region=REGION_ID

To get the IAP setting for a Cloud Run service within a project, run: 
    
    
    gcloud iap settings get --project=PROJECT_ID --resource-type=cloud-run --region=REGION_ID --service=SERVICE_ID

FLAGS
    

`--folder`=`FOLDER`
     Folder ID. 
`--organization`=`ORGANIZATION`
     Organization ID. 
`--project`=`PROJECT`
     Project ID. 
`--region`=`REGION`
     Region name. Not applicable for `app-engine`. Required when `resource-type=compute` and regional scoped. Not applicable for global scoped compute. Required when `resource-type=cloud-run`. 
`--resource-type`=`RESOURCE_TYPE`
     Resource type of the IAP resource. For Backend Services, you can use both `compute` and `backend-services` as resource type. `RESOURCE_TYPE` must be one of: `app-engine`, `iap_web`, `compute`, `organization`, `folder`, `backend-services`, `forwarding-rule`, `cloud-run`. 
`--service`=`SERVICE`
     Service name. Optional when `resource-type` is `compute` or `app-engine`. 
`--version`=`VERSION`
     Version name. Not applicable for `compute`. Optional when `resource-type=app-engine`. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha iap settings get](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/iap/settings/get)
    
    
    [gcloud beta iap settings get](https://docs.cloud.google.com/sdk/gcloud/reference/beta/iap/settings/get)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
