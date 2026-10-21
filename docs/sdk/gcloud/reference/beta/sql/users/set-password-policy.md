---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/sql/users/set-password-policy/
title: gcloud beta sql users set-password-policy \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:07:11.684322+00:00
---

# gcloud beta sql users set-password-policy  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/sql/users/set-password-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta sql users set-password-policy Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta sql users set-password-policy - replaces a user's password policy in a given instance 
SYNOPSIS
    

`gcloud beta sql users set-password-policy` `USERNAME` `--instance`=`INSTANCE`, `-i` `INSTANCE` [`--async`] [`--clear-password-policy`] [`--host`=`HOST`] [`--password-policy-allowed-failed-attempts`=`PASSWORD_POLICY_ALLOWED_FAILED_ATTEMPTS`] [`--[no-]password-policy-enable-failed-attempts-check`] [`--[no-]password-policy-enable-password-verification`] [`--password-policy-password-expiration-duration`=`PASSWORD_POLICY_PASSWORD_EXPIRATION_DURATION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Replaces a user's password policy in a given instance with a specified username and host. 
EXAMPLES
     To replace the password policy with 2 minutes password expiration time for ``my-user`` in instance ``prod-instance``, run: 
    
    
    gcloud beta sql users set-password-policy my-user --instance=prod-instance --password-policy-password-expiration-duration=2m

To clear the existing password policy of ``my-user`` in instance ``prod-instance``, run: 
    
    
    gcloud beta sql users set-password-policy my-user --instance=prod-instance --clear-password-policy

POSITIONAL ARGUMENTS
    

`USERNAME`
     Cloud SQL username. 
REQUIRED FLAGS
    

`--instance`=`INSTANCE`, `-i` `INSTANCE`
     Cloud SQL instance ID. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--clear-password-policy`
     Clear the existing password policy. This flag is only available for Postgres. 
`--host`=`HOST`
     Cloud SQL user's hostname expressed as a specific IP address or address range. `%` denotes an unrestricted hostname. Applicable flag for MySQL instances; ignored for all other engines. Note, if you connect to your instance using IP addresses, you must add your client IP address as an authorized address, even if your hostname is unrestricted. For more information, see [Configure IP](https://cloud.google.com/sql/docs/mysql/configure-ip). 
`--password-policy-allowed-failed-attempts`=`PASSWORD_POLICY_ALLOWED_FAILED_ATTEMPTS`
     Number of failed login attempts allowed before a user is locked out. 
`--[no-]password-policy-enable-failed-attempts-check`
     Enables the failed login attempts check if set to true. Use `--password-policy-enable-failed-attempts-check` to enable and `--no-password-policy-enable-failed-attempts-check` to disable. 
`--[no-]password-policy-enable-password-verification`
     The current password must be specified when altering the password. Use `--password-policy-enable-password-verification` to enable and `--no-password-policy-enable-password-verification` to disable. 
`--password-policy-password-expiration-duration`=`PASSWORD_POLICY_PASSWORD_EXPIRATION_DURATION`
     Expiration duration after a password is updated, for example, 2d for 2 days. See `[gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes)` for information on duration formats. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud sql users set-password-policy](https://docs.cloud.google.com/sdk/gcloud/reference/sql/users/set-password-policy)
    
    
    [gcloud alpha sql users set-password-policy](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/sql/users/set-password-policy)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
