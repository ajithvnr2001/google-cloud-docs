---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/apigee/apis/delete/
title: gcloud beta apigee apis delete \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:31:21.412115+00:00
---

# gcloud beta apigee apis delete  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/apigee/apis/delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta apigee apis delete Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta apigee apis delete - delete an Apigee API proxy 
SYNOPSIS
    

`gcloud beta apigee apis delete` (`API` : `--organization`=`ORGANIZATION`) [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Delete an Apigee API proxy. 

`gcloud beta apigee apis delete` deletes an API proxy and all of its revisions. 

The API proxy must not have any deployed revisions. To undeploy a revision, run `[gcloud beta apigee apis undeploy](https://docs.cloud.google.com/sdk/gcloud/reference/beta/apigee/apis/undeploy)`. Deleting an API proxy cannot be undone. 

EXAMPLES
     To delete an API proxy called ``my-proxy`` given that its matching Cloud Platform project has been set in gcloud settings, run: 
    
    
    gcloud beta apigee apis delete my-proxy

To delete an API proxy called ``my-proxy`` in an organization called ``my-org``, run: 
    
    
    gcloud beta apigee apis delete my-proxy --organization=my-org

To delete an API proxy called ``my-proxy`` without prompting for confirmation, run: 
    
    
    gcloud beta apigee apis delete my-proxy --quiet

To delete an API proxy called ``my-proxy`` and print the deleted proxy as a JSON object, run: 
    
    
    gcloud beta apigee apis delete my-proxy --format=json

POSITIONAL ARGUMENTS
    

API proxy resource - API proxy to be deleted. To get a list of available API proxies, run `[gcloud beta apigee apis list](https://docs.cloud.google.com/sdk/gcloud/reference/beta/apigee/apis/list)`. The arguments in this group can be used to specify the attributes of this resource. 

This must be specified. 

`API`
     ID of the API proxy or fully qualified identifier for the API proxy. 

To set the `api` attribute: 

  * provide the argument `API` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--organization`=`ORGANIZATION`
     Apigee organization containing the API proxy. If unspecified, the Cloud Platform project's associated organization will be used. 

To set the `organization` attribute: 

  * provide the argument `API` on the command line with a fully specified name; 
  * provide the argument `--organization` on the command line; 
  * set the property [project] or provide the argument [--project] on the command line, using a Cloud Platform project with an associated Apigee organization. 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud apigee apis delete](https://docs.cloud.google.com/sdk/gcloud/reference/apigee/apis/delete)
    
    
    [gcloud alpha apigee apis delete](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/apigee/apis/delete)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
