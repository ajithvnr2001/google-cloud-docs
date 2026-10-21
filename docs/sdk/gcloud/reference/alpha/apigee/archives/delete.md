---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/apigee/archives/delete/
title: gcloud alpha apigee archives delete \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:28:23.379620+00:00
---

# gcloud alpha apigee archives delete  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/apigee/archives/delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha apigee archives delete Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha apigee archives delete - delete an Apigee archive deployment 
SYNOPSIS
    

`gcloud alpha apigee archives delete` (`ARCHIVE_DEPLOYMENT` : `--environment`=`ENVIRONMENT` `--organization`=`ORGANIZATION`) [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Delete an Apigee archive deployment. 

`gcloud alpha apigee archives delete` deletes an Apigee archive deployment. 

EXAMPLES
     To delete an archive deployment with the ID ``abcdefghijkl123456`` in the environment called ``my-env`` using the active Cloud Platform project, run: 
    
    
    gcloud alpha apigee archives delete abcdefghijkl123456 --environment=my-env

To delete an archive deployment with the ID ``mnopqurstuvw654321``, in an environment called ``my-env``, in an organization called ``my-org``, run: 
    
    
    gcloud alpha apigee archives delete mnopqurstuvw654321 --environment=my-env --organization=my-org

POSITIONAL ARGUMENTS
    

Archive deployment resource - Apigee archive deployment to delete. The arguments in this group can be used to specify the attributes of this resource. 

This must be specified. 

`ARCHIVE_DEPLOYMENT`
     ID of the archive deployment or fully qualified identifier for the archive deployment. 

To set the `archive_deployment` attribute: 

  * provide the argument `archive_deployment` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--environment`=`ENVIRONMENT`
     Deployment environment of the archive deployment. 

To set the `environment` attribute: 

  * provide the argument `archive_deployment` on the command line with a fully specified name; 
  * provide the argument `--environment` on the command line. 


`--organization`=`ORGANIZATION`
     Apigee organization containing the archive deployment. If unspecified, the Cloud Platform project's associated organization will be used. 

To set the `organization` attribute: 

  * provide the argument `archive_deployment` on the command line with a fully specified name; 
  * provide the argument `--organization` on the command line; 
  * set the property [project] or provide the argument [--project] on the command line, using a Cloud Platform project with an associated Apigee organization. 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud beta apigee archives delete](https://docs.cloud.google.com/sdk/gcloud/reference/beta/apigee/archives/delete)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
