---
url: https://docs.cloud.google.com/sdk/gcloud/reference/compute/os-config/policy-orchestrators/delete/
title: gcloud compute os-config policy-orchestrators delete \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T11:54:50.302686+00:00
---

# gcloud compute os-config policy-orchestrators delete  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/compute/os-config/policy-orchestrators/delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud compute os-config policy-orchestrators delete Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud compute os-config policy-orchestrators delete - delete a policy orchestrator 
SYNOPSIS
    

`gcloud compute os-config policy-orchestrators delete` (`POLICY_ORCHESTRATOR` : `--folder`=`FOLDER` `--organization`=`ORGANIZATION`) [`--async`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Delete a policy orchestrator and cancel ongoing rollouts (best-effort). 
EXAMPLES
    

To delete a policy orchestrator `my-orchestrator` in the folder `123456`: 
    
    
    gcloud compute os-config policy-orchestrators delete my-orchestrator --folder=123456

POSITIONAL ARGUMENTS
    

Policy orchestrator resource - policy orchestrator to delete. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `policy_orchestrator` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. This resource can be one of the following types: [policy_orchestrator_project, policy_orchestrator_folder, policy_orchestrator_organization]. 



This must be specified. 

`POLICY_ORCHESTRATOR`
     ID of the policy_orchestrator or fully qualified identifier for the policy_orchestrator. 

To set the `policy_orchestrator` attribute: 

  * provide the argument `policy_orchestrator` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--folder`=`FOLDER`
     Folder of the policy_orchestrator. To set the `folder` attribute: 

  * provide the argument `policy_orchestrator` on the command line with a fully specified name; 
  * provide the argument `--folder` on the command line. Must be specified for resource of type [policy_orchestrator_folder]. 


`--organization`=`ORGANIZATION`
     Organization of the policy_orchestrator. To set the `organization` attribute: 

  * provide the argument `policy_orchestrator` on the command line with a fully specified name; 
  * provide the argument `--organization` on the command line. Must be specified for resource of type [policy_orchestrator_organization]. 


FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `osconfig/v2` API. The full documentation for this API can be found at: <https://cloud.google.com/compute/docs/osconfig/rest>
NOTES
     These variants are also available: 
    
    
    [gcloud alpha compute os-config policy-orchestrators delete](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/os-config/policy-orchestrators/delete)
    
    
    [gcloud beta compute os-config policy-orchestrators delete](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/os-config/policy-orchestrators/delete)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
