---
url: https://docs.cloud.google.com/sdk/gcloud/reference/compute/org-security-policies/associations/create/
title: gcloud compute org-security-policies associations create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T07:10:16.759760+00:00
---

# gcloud compute org-security-policies associations create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/compute/org-security-policies/associations/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud compute org-security-policies associations create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud compute org-security-policies associations create - create a new association between a security policy and an organization or folder resource 
SYNOPSIS
    

`gcloud compute org-security-policies associations create` `--security-policy`=`SECURITY_POLICY` [`--excluded-folders`=[`EXCLUDED_FOLDERS`,…]] [`--excluded-projects`=[`EXCLUDED_PROJECTS`,…]] [`--name`=`NAME`] [`--organization`=`ORGANIZATION`] [`--replace-association-on-target`] [`--folder`=`FOLDER` | `--project-number`=`PROJECT_NUMBER`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `gcloud compute org-security-policies associations create` is used to create organization security policy associations. An organization security policy is a set of rules that controls access to various resources. 

This command has billing implications. Projects in the hierarchy with effective hierarchical security policies will be automatically enrolled into Cloud Armor Enterprise if not already enrolled. 

EXAMPLES
     To associate an organization security policy under folder with ID ``123456789`` to folder ``987654321``, run: 
    
    
    gcloud compute org-security-policies associations create --security-policy=123456789 --folder=987654321

REQUIRED FLAGS
    

`--security-policy`=`SECURITY_POLICY`
     Security policy ID of the association. 
OPTIONAL FLAGS
    

`--excluded-folders`=[`EXCLUDED_FOLDERS`,…]
     List of folders to exclude from the application of this security policy. Folders should be specified in the form "folders/123". 
`--excluded-projects`=[`EXCLUDED_PROJECTS`,…]
     List of projects to exclude from the application of this security policy. Projects should be specified in the form "projects/123". 
`--name`=`NAME`
     Name to identify this association. If unspecified, the name will be set to "organization-{ORGANIZATION_ID}" or "folder-{FOLDER_ID}". 
`--organization`=`ORGANIZATION`
     ID of the organization to associate the security policy with. Must be set if SECURITY_POLICY is short name. 
`--replace-association-on-target`
     By default, if you attempt to insert an association to an organization or folder resource that is already associated with a security policy the method will fail. If this is set, the existing association will be deleted at the same time that the new association is created. 
At most one of these can be specified: 

`--folder`=`FOLDER`
     ID of the folder to associate the security policy with. 
`--project-number`=`PROJECT_NUMBER`
     Project number to associate the security policy with. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha compute org-security-policies associations create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/org-security-policies/associations/create)
    
    
    [gcloud beta compute org-security-policies associations create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/org-security-policies/associations/create)
    
    
    [gcloud preview compute org-security-policies associations create](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/org-security-policies/associations/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
