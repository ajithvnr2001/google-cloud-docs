---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/ai/persistent-resources/delete/
title: gcloud alpha ai persistent-resources delete \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:22:27.886372+00:00
---

# gcloud alpha ai persistent-resources delete  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/ai/persistent-resources/delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha ai persistent-resources delete Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha ai persistent-resources delete - delete an active Persistent Resource 
SYNOPSIS
    

`gcloud alpha ai persistent-resources delete` (`PERSISTENT_RESOURCE` : `--region`=`REGION`) [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` If the Persistent Resource is not in the active state, the command will not perform any operation. 
EXAMPLES
     To delete a persistent resource ``123`` under project ``example`` in region ``us-central1``, run: 
    
    
    gcloud alpha ai persistent-resources delete 123 --project=example --region=us-central1

POSITIONAL ARGUMENTS
    

Persistent resource resource - The persistent resource to delete. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `persistent_resource` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`PERSISTENT_RESOURCE`
     ID of the persistent resource or fully qualified identifier for the persistent resource. 

To set the `name` attribute: 

  * provide the argument `persistent_resource` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--region`=`REGION`
     Cloud region for the persistent resource. 

To set the `region` attribute: 

  * provide the argument `persistent_resource` on the command line with a fully specified name; 
  * provide the argument `--region` on the command line; 
  * set the property `ai/region`; 
  * choose one from the prompted list of available regions. 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud ai persistent-resources delete](https://docs.cloud.google.com/sdk/gcloud/reference/ai/persistent-resources/delete)
    
    
    [gcloud beta ai persistent-resources delete](https://docs.cloud.google.com/sdk/gcloud/reference/beta/ai/persistent-resources/delete)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
