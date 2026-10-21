---
url: https://docs.cloud.google.com/sdk/gcloud/reference/design-center/spaces/applications/deploy/
title: gcloud design-center spaces applications deploy \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:17:59.490772+00:00
---

# gcloud design-center spaces applications deploy  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/design-center/spaces/applications/deploy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud design-center spaces applications deploy Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud design-center spaces applications deploy - deploy an application 
SYNOPSIS
    

`gcloud design-center spaces applications deploy` (`APPLICATION` : `--location`=`LOCATION` `--space`=`SPACE`) [`--async`] [`--create-sa`] [`--replace`] [`--service-account`=`SERVICE_ACCOUNT`] [`--worker-pool`=`WORKER_POOL`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Deploy an application in a space. 
EXAMPLES
     To deploy the application my-application in space my-space, project my-project and location us-central1, run: 
    
    
    gcloud design-center spaces applications deploy my-application --space=my-space --project=my-project --location=us-central1

Or run: 
    
    
    gcloud design-center spaces applications deploy projects/my-project/locations/us-central1/spaces/my-space/applications/my-application

To deploy the application my-application in space my-space, project my-project and location us-central1 and replace the existing deployment, run: 
    
    
    gcloud design-center spaces applications deploy my-application --space=my-space --project=my-project --location=us-central1 --replace

To deploy the application my-application in space my-space, project my-project and location us-central1 using a worker pool projects/my-project/locations/us-central1/workerPools/my-worker-pool, run: 
    
    
    gcloud design-center spaces applications deploy my-application --space=my-space --project=my-project --location=us-central1 --worker-pool=projects/my-project/locations/us-central1/workerPools/my-worker-pool

To deploy the application my-application and create a new service account for the deployment, run: 
    
    
    gcloud design-center spaces applications deploy my-application --space=my-space --project=my-project --location=us-central1 --create-sa

To deploy the application my-application and create a new service account and create a specific service account for the deployment, run: 
    
    
    gcloud design-center spaces applications deploy my-application --space=my-space --project=my-project --location=us-central1 --create-sa --service-account=my-service-account@my-project.iam.gserviceaccount.com

To deploy the application my-application and use a specific service account for the deployment, run: 
    
    
    gcloud design-center spaces applications deploy my-application --space=my-space --project=my-project --location=us-central1 --service-account=projects/my-project/serviceAccounts/my-service-account@my-project.iam.gserviceaccount.com

To deploy the application my-application in space my-space, project my-project and location us-central1 asynchronously, run: 
    
    
    gcloud design-center spaces applications deploy my-application --space=my-space --project=my-project --location=us-central1 --async

POSITIONAL ARGUMENTS
    

Application resource - The application to deploy IaC. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `APPLICATION` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`APPLICATION`
     ID of the application or fully qualified identifier for the application. 

To set the `application` attribute: 

  * provide the argument `APPLICATION` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The Cloud location for the application. 

To set the `location` attribute: 

  * provide the argument `APPLICATION` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


`--space`=`SPACE`
     The ID of the space. 

To set the `space` attribute: 

  * provide the argument `APPLICATION` on the command line with a fully specified name; 
  * provide the argument `--space` on the command line. 


FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--create-sa`
     Create a new service account for the deployment. 
`--replace`
     Flag to update the existing deployment. If not set or false, deploy will fail if application state is in the DEPLOYED state. 
`--service-account`=`SERVICE_ACCOUNT`
     The service account to use for this deployment. 

  * If provided, this service account will be used to execute the deployment process, taking precedence over any service_account specified on the Application resource. 
  * The caller must have the "iam.serviceAccounts.actAs" permission on this service account. 
  * If this field is omitted, the system will use the "service_account" defined within the Application resource. 
  * If this field is omitted with --create-sa flag, the system will create a new and unique service_account and use it for the deployment. 
  * We recommend that you provide a service account here or on the Application resource. If you don't provide a service account, the deployment will fail. 
  * If the `--create-sa` flag is also provided, this value is the ID of a new service account to be created (e.g., `my-new-sa`). 



Format: `projects/{PROJECT}/serviceAccounts/{EMAIL_ADDRESS}` (when not using `--create-sa`) 

`--worker-pool`=`WORKER_POOL`
     The user-specified Worker Pool resource in which the Cloud Build job will execute. Format: projects/{project}/locations/{location}/workerPools/{workerPoolId} If this flag is omitted, the worker pool already defined on the application will be used. If no worker pool is defined on the application, the default Cloud Build worker pool is used. The worker pool must exist in the same region as the application. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This variant is also available: 
    
    
    [gcloud alpha design-center spaces applications deploy](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/design-center/spaces/applications/deploy)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
