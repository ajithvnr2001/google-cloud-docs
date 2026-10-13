---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/associations/create/
title: gcloud alpha compute firewall-policies associations create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:45:08.909366+00:00
---

# gcloud alpha compute firewall-policies associations create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/associations/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha compute firewall-policies associations create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha compute firewall-policies associations create - create a new association between a firewall policy and an organization or folder resource 
SYNOPSIS
    

`gcloud alpha compute firewall-policies associations create` `--firewall-policy`=`FIREWALL_POLICY` [`--folder`=`FOLDER`] [`--name`=`NAME`] [`--organization`=`ORGANIZATION`] [`--replace-association-on-target`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` `gcloud alpha compute firewall-policies associations create` is used to create organization firewall policy associations. An organization firewall policy is a set of rules that controls access to various resources. 
EXAMPLES
     To associate an organization firewall policy under folder with ID ``123456789" to folder ``987654321", run: 
    
    
    gcloud alpha compute firewall-policies associations create --firewall-policy=123456789 --folder=987654321

REQUIRED FLAGS
    

`--firewall-policy`=`FIREWALL_POLICY`
     Security policy ID of the association. 
OPTIONAL FLAGS
    

`--folder`=`FOLDER`
     ID of the folder with which the association is created. 
`--name`=`NAME`
     Name to identify this association. If unspecified, the name will be set to "organization-{ORGANIZATION_ID}" or "folder-{FOLDER_ID}". 
`--organization`=`ORGANIZATION`
     ID of the organization in which the firewall policy is to be associated. Must be set if FIREWALL_POLICY is short name. 
`--replace-association-on-target`
     By default, if you attempt to insert an association to an organization or folder resource that is already associated with a firewall policy the method will fail. If this is set, the existing association will be deleted at the same time that the new association is created. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud compute firewall-policies associations create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/firewall-policies/associations/create)
    
    
    [gcloud beta compute firewall-policies associations create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/firewall-policies/associations/create)
    
    
    [gcloud preview compute firewall-policies associations create](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/firewall-policies/associations/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
