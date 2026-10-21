---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/network-firewall-policies/create/
title: gcloud alpha compute network-firewall-policies create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:27:31.194635+00:00
---

# gcloud alpha compute network-firewall-policies create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/network-firewall-policies/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha compute network-firewall-policies create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha compute network-firewall-policies create - create a Compute Engine Network firewall policy 
SYNOPSIS
    

`gcloud alpha compute network-firewall-policies create` `FIREWALL_POLICY` [`--description`=`DESCRIPTION`] [`--policy-type`=`POLICY_TYPE`] [`--security-profile-fallback-action`=`SECURITY_PROFILE_FALLBACK_ACTION`] [`--global` | `--region`=`REGION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` `gcloud alpha compute network-firewall-policies create` is used to create network firewall policies. A network firewall policy is a set of rules that controls access to various resources. 
EXAMPLES
     To create a global network firewall policy named ``my-policy`` under project with ID ``test-project``, run: 
    
    
    gcloud alpha compute network-firewall-policies create my-policy --project=test-project --global

To create a regional network firewall policy named ``my-region-policy`` under project with ID ``test-project``, in region ``my-region``, run: 
    
    
    gcloud alpha compute network-firewall-policies create my-region-policy --project=test-project --region=my-region

POSITIONAL ARGUMENTS
    

`FIREWALL_POLICY`
     name of the network firewall policy to create. 
FLAGS
    

`--description`=`DESCRIPTION`
     An optional, textual description for the network firewall policy. 
`--policy-type`=`POLICY_TYPE`
     Network firewall policy type. `POLICY_TYPE` must be one of: `VPC_POLICY`, `RDMA_ROCE_POLICY`, `RDMA_FALCON_POLICY`, `ULL_POLICY`. 
`--security-profile-fallback-action`=`SECURITY_PROFILE_FALLBACK_ACTION`
     The action to take if the security profile group cannot be applied. If unspecified, the effective action defaults to allow for backwards compatibility, and will not be displayed in describe output unless explicitly set. `SECURITY_PROFILE_FALLBACK_ACTION` must be one of: `allow`, `deny`. 
At most one of these can be specified: 

`--global`
     If set, the firewall policy is global. 
`--region`=`REGION`
     Region of the firewall policy to create. Overrides the default `compute/region` property value for this command invocation. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud compute network-firewall-policies create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/create)
    
    
    [gcloud beta compute network-firewall-policies create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/network-firewall-policies/create)
    
    
    [gcloud preview compute network-firewall-policies create](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/network-firewall-policies/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-09 UTC."],[],[]] 
