---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/sql/users/set-password/
title: gcloud alpha sql users set-password \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:26:10.702378+00:00
---

# gcloud alpha sql users set-password  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/sql/users/set-password/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha sql users set-password Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha sql users set-password - changes a user's password in a given instance 
SYNOPSIS
    

`gcloud alpha sql users set-password` `USERNAME` `--instance`=`INSTANCE`, `-i` `INSTANCE` [`--async`] [`--host`=`HOST`] [`--discard-dual-password` | `--retain-password`] [`--password`=`PASSWORD` | `--prompt-for-password`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Changes a user's password in a given instance with specified username and host. 
POSITIONAL ARGUMENTS
    

`USERNAME`
     Cloud SQL username. 
REQUIRED FLAGS
    

`--instance`=`INSTANCE`, `-i` `INSTANCE`
     Cloud SQL instance ID. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--host`=`HOST`
     Cloud SQL user's hostname expressed as a specific IP address or address range. `%` denotes an unrestricted hostname. Applicable flag for MySQL instances; ignored for all other engines. Note, if you connect to your instance using IP addresses, you must add your client IP address as an authorized address, even if your hostname is unrestricted. For more information, see [Configure IP](https://cloud.google.com/sql/docs/mysql/configure-ip). 
At most one of these can be specified: 

`--discard-dual-password`
     Discard the user's secondary password. Cannot set password and set this flag. This flag is only available for MySQL 8.0. 
`--retain-password`
     Retain the old password when changing to the new password. Must set password with this flag. This flag is only available for MySQL 8.0. 
At most one of these can be specified: 

`--password`=`PASSWORD`
     Cloud SQL user's password. 
`--prompt-for-password`
     Prompt for the Cloud SQL user's password with character echo disabled. The password is all typed characters up to but not including the RETURN or ENTER key. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud sql users set-password](https://docs.cloud.google.com/sdk/gcloud/reference/sql/users/set-password)
    
    
    [gcloud beta sql users set-password](https://docs.cloud.google.com/sdk/gcloud/reference/beta/sql/users/set-password)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
