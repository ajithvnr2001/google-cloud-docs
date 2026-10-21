---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/apigee/apis/undeploy/
title: gcloud beta apigee apis undeploy \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:31:21.717538+00:00
---

# gcloud beta apigee apis undeploy  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/apigee/apis/undeploy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta apigee apis undeploy Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta apigee apis undeploy - undeploy an Apigee API proxy from an environment 
SYNOPSIS
    

`gcloud beta apigee apis undeploy` [[`REVISION`] `--api`=`API` `--environment`=`ENVIRONMENT` `--organization`=`ORGANIZATION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Undeploy an Apigee API proxy from an environment. 
EXAMPLES
     To undeploy an API proxy called ``my-api`` from the ``test`` environment of the active Cloud Platform project, run: 
    
    
    gcloud beta apigee apis undeploy --environment=test --api=my-api

To undeploy revision 3 of an `my-api` from the `test` environment of the organization named ``test-org``, run: 
    
    
    gcloud beta apigee apis undeploy 3 --organization=test-org --environment=test --api=my-api

POSITIONAL ARGUMENTS
    

Revision resource - API proxy revision to be undeployed and environment from which it should be removed. 

Revisions can either be a positive revision number, or the special value ``auto``, which will undeploy whatever revision is currently deployed. If revision is unspecified, the default is ``auto``. The arguments in this group can be used to specify the attributes of this resource. 

[`REVISION`]
     ID of the revision or fully qualified identifier for the revision. 

To set the `revision` attribute: 

  * provide the argument `REVISION` on the command line; 
  * leave the argument unspecified for it to be chosen automatically. 


`--api`=`API`
     API proxy to be undeployed. Must currently be deployed. To get a list of available deployed proxies, run `gcloud beta apigee deployments list --environment=ENV`. 

To set the `api` attribute: 

  * provide the argument `REVISION` on the command line with a fully specified name; 
  * leave the argument unspecified for it to be chosen automatically with a fully specified name; 
  * provide the argument `--api` on the command line. 


`--environment`=`ENVIRONMENT`
     Environment from which to undeploy the API proxy. To get a list of available environments, run `[gcloud beta apigee environments list](https://docs.cloud.google.com/sdk/gcloud/reference/beta/apigee/environments/list)`. 

To set the `environment` attribute: 

  * provide the argument `REVISION` on the command line with a fully specified name; 
  * leave the argument unspecified for it to be chosen automatically with a fully specified name; 
  * provide the argument `--environment` on the command line. 


`--organization`=`ORGANIZATION`
     Apigee organization of the proxy and environment. 

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
    
    
    [gcloud apigee apis undeploy](https://docs.cloud.google.com/sdk/gcloud/reference/apigee/apis/undeploy)
    
    
    [gcloud alpha apigee apis undeploy](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/apigee/apis/undeploy)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
