---
url: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/org-security-policies/create/
title: gcloud preview compute org-security-policies create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T12:41:46.568122+00:00
---

# gcloud preview compute org-security-policies create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/org-security-policies/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud preview compute org-security-policies create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud preview compute org-security-policies create - create a Compute Engine organization security policy 
SYNOPSIS
    

`gcloud preview compute org-security-policies create` (`--folder`=`FOLDER` | `--organization`=`ORGANIZATION`) [`--description`=`DESCRIPTION`] [`--display-name`=`DISPLAY_NAME`] [`--file-format`=`FILE_FORMAT`] [`--short-name`=`SHORT_NAME`] [`--file-name`=`FILE_NAME` | `--type`=`SECURITY_POLICY_TYPE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(PREVIEW)` `gcloud preview compute org-security-policies create` is used to create organization security policies. An organization security policy is a set of rules that controls access to various resources. 
EXAMPLES
     To create an organization security policy under folder with ID ``123456789``, run: 
    
    
    gcloud preview compute org-security-policies create --short-name=my-policy --folder=123456789

To create an organization security under organization with ID ``12345`` from an input file, run: 
    
    
    gcloud preview compute org-security-policies create --file-name=my-file-name --organization=12345

REQUIRED FLAGS
    

Exactly one of these must be specified: 

`--folder`=`FOLDER`
     Folder in which the organization security policy is to be created. 
`--organization`=`ORGANIZATION`
     Organization in which the organization security policy is to be created. 
OPTIONAL FLAGS
    

`--description`=`DESCRIPTION`
     An optional, textual description for the organization security policy. 
`--display-name`=`DISPLAY_NAME`
     A textual name of the security policy. 
`--file-format`=`FILE_FORMAT`
     The format of the file to create the organization security policy config from. Specify either yaml or json. Defaults to yaml if not specified. Will be ignored if --file-name is not specified. `FILE_FORMAT` must be one of: `json`, `yaml`. 
`--short-name`=`SHORT_NAME`
     A textual name of the security policy. 
Creation options. 

At most one of these can be specified: 

`--file-name`=`FILE_NAME`
     The name of the JSON or YAML file to create a organization security policy config from. 
`--type`=`SECURITY_POLICY_TYPE`
     The type indicates the intended use of the organization security policy. `SECURITY_POLICY_TYPE` must be one of: `CLOUD_ARMOR`, `FIREWALL`. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in DEVELOPER PREVIEW and may change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud compute org-security-policies create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/org-security-policies/create)
    
    
    [gcloud alpha compute org-security-policies create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/org-security-policies/create)
    
    
    [gcloud beta compute org-security-policies create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/org-security-policies/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
