---
url: https://docs.cloud.google.com/sdk/gcloud/reference/apigee/apis/deploy/
title: gcloud apigee apis deploy \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:36:44.131993+00:00
---

# gcloud apigee apis deploy  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/apigee/apis/deploy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud apigee apis deploy Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud apigee apis deploy - deploy an Apigee API proxy to an environment 
SYNOPSIS
    

`gcloud apigee apis deploy` [[`REVISION`] `--api`=`API` `--environment`=`ENVIRONMENT` `--organization`=`ORGANIZATION`] [`--override`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Deploy an Apigee API proxy to an environment. 

`gcloud apigee apis deploy` installs an API proxy revision in an Apigee runtime environment. 

By default, the API proxy's base path must not already be in use by a deployed proxy in the target environment. To allow Apigee to undeploy any conflicting API proxy as part of the deployment, use the `--override` command. 

Once a particular revision of an API proxy has been deployed, that revision can no longer be modified. Any updates to the API proxy must be saved as a new revision. 

EXAMPLES
     To deploy the latest revision of the API proxy named ``demo`` to the ``test`` environment, given that the API proxy and environment's matching Cloud Platform project has been set in gcloud settings, run: 
    
    
    gcloud apigee apis deploy --environment=test --api=demo

To deploy revision 3 of that proxy, owned by an organization named ``my-org``, run, and replace any conflicting deployment that might already exist, run: 
    
    
    gcloud apigee apis deploy 3 --organization=my-org --environment=test --api=demo --override

To deploy that proxy and print the resulting deployment as a JSON object, run: 
    
    
    gcloud apigee apis deploy 3 --organization=my-org --environment=test --api=demo --format=json

POSITIONAL ARGUMENTS
    

Revision resource - API proxy revision to be deployed and environment in which to deploy it. Revisions can either be a positive revision number, or the special value ``latest``, which will deploy the latest revision of the API proxy. If revision is unspecified, the default is ``latest``. The arguments in this group can be used to specify the attributes of this resource. 
[`REVISION`]
     ID of the revision or fully qualified identifier for the revision. 

To set the `revision` attribute: 

  * provide the argument `REVISION` on the command line; 
  * leave the argument unspecified for it to be chosen automatically. 


`--api`=`API`
     API proxy to be deployed. To get a list of available API proxies, run `[gcloud apigee apis list](https://docs.cloud.google.com/sdk/gcloud/reference/apigee/apis/list)`. 

To set the `api` attribute: 

  * provide the argument `REVISION` on the command line with a fully specified name; 
  * leave the argument unspecified for it to be chosen automatically with a fully specified name; 
  * provide the argument `--api` on the command line. 


`--environment`=`ENVIRONMENT`
     Environment in which to deploy the API proxy. To get a list of available environments, run `[gcloud apigee environments list](https://docs.cloud.google.com/sdk/gcloud/reference/apigee/environments/list)`. 

To set the `environment` attribute: 

  * provide the argument `REVISION` on the command line with a fully specified name; 
  * leave the argument unspecified for it to be chosen automatically with a fully specified name; 
  * provide the argument `--environment` on the command line. 


`--organization`=`ORGANIZATION`
     Apigee organization of the proxy and environment. If unspecified, the Cloud Platform project's associated organization will be used. 

To set the `organization` attribute: 

  * provide the argument `REVISION` on the command line with a fully specified name; 
  * leave the argument unspecified for it to be chosen automatically with a fully specified name; 
  * provide the argument `--organization` on the command line; 
  * set the property [project] or provide the argument [--project] on the command line, using a Cloud Platform project with an associated Apigee organization. 


FLAGS
    

`--override`
     Force the deployment of the new revision, overriding any currently deployed revision that would conflict with it. 

If an existing API proxy revision is deployed, set this flag to ensure seamless deployment with zero downtime. In this case, the existing revision remains deployed until the new revision is fully deployed. 

If unset, `gcloud apigee apis deploy` will fail unless all conflicting API proxies are first undeployed from the environment. To do this, run `[gcloud apigee apis undeploy](https://docs.cloud.google.com/sdk/gcloud/reference/apigee/apis/undeploy)` on the conflicting deployment. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha apigee apis deploy](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/apigee/apis/deploy)
    
    
    [gcloud beta apigee apis deploy](https://docs.cloud.google.com/sdk/gcloud/reference/beta/apigee/apis/deploy)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
