---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/binauthz/policy/evaluate/
title: gcloud beta container binauthz policy evaluate \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:38:27.254029+00:00
---

# gcloud beta container binauthz policy evaluate  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/binauthz/policy/evaluate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta container binauthz policy evaluate Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta container binauthz policy evaluate - evaluate a Binary Authorization platform policy 
SYNOPSIS
    

`gcloud beta container binauthz policy evaluate` (`POLICY_RESOURCE_NAME` : `--platform`=`PLATFORM`) (`--image`=`IMAGE` | `--resource`=`RESOURCE`) [`GCLOUD_WIDE_FLAG …`]
EXAMPLES
     To evaluate a policy using its resource name: 
    
    
    gcloud beta container binauthz policy evaluate projects/my-proj/platforms/gke/policies/my-policy --resource=$KUBERNETES_RESOURCE

To evaluate the same policy using flags against an image: 
    
    
    gcloud beta container binauthz policy evaluate my-policy --platform=gke --project=my-proj --image=$IMAGE

POSITIONAL ARGUMENTS
    

Policy resource - The resource name of the policy to evaluate. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `policy_resource_name` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`POLICY_RESOURCE_NAME`
     ID of the policy or fully qualified identifier for the policy. 

To set the `policy` attribute: 

  * provide the argument `policy_resource_name` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--platform`=`PLATFORM`
     The platform that the policy belongs to. PLATFORM must be one of the following: cloudRun, gke. 

To set the `platform` attribute: 

  * provide the argument `policy_resource_name` on the command line with a fully specified name; 
  * provide the argument `--platform` on the command line. 


REQUIRED FLAGS
    

Exactly one of these must be specified: 

`--image`=`IMAGE`
     The image to evaluate. If the policy being evaluated has scoped checksets, this mode of evaluation will always use the default (unscoped) checkset. 
`--resource`=`RESOURCE`
     The JSON or YAML file containing the Kubernetes resource to evaluate. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. This variant is also available: 
    
    
    [gcloud alpha container binauthz policy evaluate](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/binauthz/policy/evaluate)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
