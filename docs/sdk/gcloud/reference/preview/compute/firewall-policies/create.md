---
url: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/firewall-policies/create/
title: gcloud preview compute firewall-policies create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:26:13.992670+00:00
---

# gcloud preview compute firewall-policies create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/firewall-policies/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud preview compute firewall-policies create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud preview compute firewall-policies create - create a Compute Engine organization firewall policy 
SYNOPSIS
    

`gcloud preview compute firewall-policies create` `--short-name`=`SHORT_NAME` (`--folder`=`FOLDER` | `--organization`=`ORGANIZATION`) [`--description`=`DESCRIPTION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(PREVIEW)` `gcloud preview compute firewall-policies create` is used to create organization firewall policies. An organization firewall policy is a set of rules that controls access to various resources. 
EXAMPLES
     To create an organization firewall policy under folder with ID ``123456789", run: 
    
    
    gcloud preview compute firewall-policies create --short-name=my-policy --folder=123456789

REQUIRED FLAGS
    

`--short-name`=`SHORT_NAME`
     A textual name of the firewall policy. The name must be 1-63 characters long, and comply with RFC 1035. 
Exactly one of these must be specified: 

`--folder`=`FOLDER`
     Folder in which the organization firewall policy is to be created. 
`--organization`=`ORGANIZATION`
     Organization in which the organization firewall policy is to be created. 
OPTIONAL FLAGS
    

`--description`=`DESCRIPTION`
     An optional, textual description for the organization security policy. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

IAM PERMISSIONS
     To create rules to a firewall policy, the user must have the following permission: ``compute.firewallPolicies.create`. 

To find predefined roles that contain those permissions, see the [Compute Engine IAM roles](https://cloud.google.com/compute/docs/access/iam). 

`
NOTES
     This command is currently in DEVELOPER PREVIEW and may change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud compute firewall-policies create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/firewall-policies/create)
    
    
    [gcloud alpha compute firewall-policies create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/create)
    
    
    [gcloud beta compute firewall-policies create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/firewall-policies/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
