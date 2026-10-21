---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/apigee/deployments/describe/
title: gcloud beta apigee deployments describe \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:31:23.302557+00:00
---

# gcloud beta apigee deployments describe  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/apigee/deployments/describe/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta apigee deployments describe Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta apigee deployments describe - describe an Apigee API proxy deployment 
SYNOPSIS
    

`gcloud beta apigee deployments describe` [[`REVISION`] `--api`=`API` `--environment`=`ENVIRONMENT` `--organization`=`ORGANIZATION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Describe an Apigee API proxy deployment. 

`gcloud beta apigee deployments describe` retrieves the status of a specific API proxy's deployment to a specific environment. 

EXAMPLES
     To get the status of a deployment in the active Cloud Platform project, which deploys ``my-proxy`` into the ``prod`` environment, run: 
    
    
    gcloud beta apigee deployments describe --api=my-proxy --environment=prod

To get the status of that deployment as a JSON object, run: 
    
    
    gcloud beta apigee deployments describe --api=my-proxy --environment=prod --format=json

To get the status of a deployment in an organization called ``my-org``, which deploys version 3 of the proxy ``my-proxy`` into the ``test`` environment, run: 
    
    
    gcloud beta apigee deployments describe 3 --organization=my-org --environment=test --api=my-proxy

POSITIONAL ARGUMENTS
    

Revision resource - API proxy revision and environment of the deployment to be described. To get a list of deployed proxies and their environments, run: 
    
    
    [gcloud beta apigee deployments list](https://docs.cloud.google.com/sdk/gcloud/reference/beta/apigee/deployments/list)

REVISION can either be a positive revision number, or the special value ``auto``, which will choose whichever revision of API is currently deployed in ENVIRONMENT, or return an error if more than one revision is deployed. 

If REVISION is unspecified, the default is ``auto``. 
    
    
    The arguments in this group can be used to specify the attributes of this resource.

[`REVISION`]
     ID of the revision or fully qualified identifier for the revision. 

To set the `revision` attribute: 

  * provide the argument `REVISION` on the command line; 
  * leave the argument unspecified for it to be chosen automatically. 


`--api`=`API`
     Deployed API proxy. 

To set the `api` attribute: 

  * provide the argument `REVISION` on the command line with a fully specified name; 
  * leave the argument unspecified for it to be chosen automatically with a fully specified name; 
  * provide the argument `--api` on the command line. 


`--environment`=`ENVIRONMENT`
     Environment in which the proxy was deployed. 

To set the `environment` attribute: 

  * provide the argument `REVISION` on the command line with a fully specified name; 
  * leave the argument unspecified for it to be chosen automatically with a fully specified name; 
  * provide the argument `--environment` on the command line. 


`--organization`=`ORGANIZATION`
     Apigee Organization of the proxy and environment. If unspecified, the Cloud Platform project's associated organization will be used. 

To set the `organization` attribute: 

  * provide the argument `REVISION` on the command line with a fully specified name; 
  * leave the argument unspecified for it to be chosen automatically with a fully specified name; 
  * provide the argument `--organization` on the command line; 
  * set the property [project] or provide the argument [--project] on the command line, using a Cloud Platform project with an associated Apigee organization. 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud apigee deployments describe](https://docs.cloud.google.com/sdk/gcloud/reference/apigee/deployments/describe)
    
    
    [gcloud alpha apigee deployments describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/apigee/deployments/describe)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
