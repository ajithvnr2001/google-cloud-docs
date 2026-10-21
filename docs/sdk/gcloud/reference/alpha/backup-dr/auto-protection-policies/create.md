---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/backup-dr/auto-protection-policies/create/
title: gcloud alpha backup-dr auto-protection-policies create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:48:14.598872+00:00
---

# gcloud alpha backup-dr auto-protection-policies create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/backup-dr/auto-protection-policies/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha backup-dr auto-protection-policies create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha backup-dr auto-protection-policies create - create a Backup and DR AutoProtectionPolicy 
SYNOPSIS
    

`gcloud alpha backup-dr auto-protection-policies create` (`AUTO_PROTECTION_POLICY` : `--location`=`LOCATION`) `--backup-plan-details`=[`backup-plan`=`BACKUP-PLAN`],[`resource-type`=`RESOURCE-TYPE`] `--criteria`=`key`=`KEY`,`values`=`VALUES` [`--async`] [`--description`=`DESCRIPTION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Create a Backup and DR AutoProtectionPolicy. 
EXAMPLES
     To create an AutoProtectionPolicy 'my-policy' in 'us-central1' with a criteria label, run: 
    
    
    # gcloud-disable-gdu-domain
    gcloud alpha backup-dr auto-protection-policies create my-policy --location=us-central1 --criteria=key=environment,values=prod --description="My Policy" --backup-plan-details="resource-type=compute.googleapis.com/Instance,backup-plan=projects/my-proj/locations/us-central1/backupPlans/my-plan"

POSITIONAL ARGUMENTS
    

AutoProtectionPolicy resource - Name of the AutoProtectionPolicy to create. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `auto_protection_policy` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`AUTO_PROTECTION_POLICY`
     ID of the AutoProtectionPolicy or fully qualified identifier for the AutoProtectionPolicy. 

To set the `name` attribute: 

  * provide the argument `auto_protection_policy` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location of the AutoProtectionPolicy. 

To set the `location` attribute: 

  * provide the argument `auto_protection_policy` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


REQUIRED FLAGS
    

`--backup-plan-details`=[`backup-plan`=`BACKUP-PLAN`],[`resource-type`=`RESOURCE-TYPE`]
     Backup plan details in format resource-type=VALUE,backup-plan=VALUE. This flag can be repeated to specify multiple backup plans. 
`--criteria`=`key`=`KEY`,`values`=`VALUES`
     Criteria of the policy in format key=KEY,values=VALUE. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. The default is `True`. Enabled by default, use `--no-async` to disable. 
`--description`=`DESCRIPTION`
     Description for the policy. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

BRIEF
     Create a Backup and DR AutoProtectionPolicy. 
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud beta backup-dr auto-protection-policies create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/backup-dr/auto-protection-policies/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-09 UTC."],[],[]] 
