---
url: https://docs.cloud.google.com/sdk/gcloud/reference/sql/users/create/
title: gcloud sql users create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:39:44.627686+00:00
---

# gcloud sql users create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/sql/users/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud sql users create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud sql users create - creates a user in a given instance 
SYNOPSIS
    

`gcloud sql users create` `USERNAME` `--instance`=`INSTANCE`, `-i` `INSTANCE` [`--async`] [`--database-roles`=[`ROLE`,…]] [`--host`=`HOST`] [`--password`=`PASSWORD`] [`--password-policy-allowed-failed-attempts`=`PASSWORD_POLICY_ALLOWED_FAILED_ATTEMPTS`] [`--[no-]password-policy-enable-failed-attempts-check`] [`--[no-]password-policy-enable-password-verification`] [`--password-policy-password-expiration-duration`=`PASSWORD_POLICY_PASSWORD_EXPIRATION_DURATION`] [`--type`=`TYPE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Creates a user in a given instance with specified username, host, type, and password. 
POSITIONAL ARGUMENTS
    

`USERNAME`
     Cloud SQL username. 
REQUIRED FLAGS
    

`--instance`=`INSTANCE`, `-i` `INSTANCE`
     Cloud SQL instance ID. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--database-roles`=[`ROLE`,…]
     A comma-separated list of database roles to be assigned to the user. This option is only available for MySQL and PostgreSQL instances. You can include predefined Cloud SQL roles, like cloudsqlsuperuser, or your own custom roles. Custom roles must be created in the database before you can assign them. You can create roles using the CREATE ROLE statement for both MySQL and PostgreSQL. 
`--host`=`HOST`
     Cloud SQL user's hostname expressed as a specific IP address or address range. `%` denotes an unrestricted hostname. Applicable flag for MySQL instances; ignored for all other engines. Note, if you connect to your instance using IP addresses, you must add your client IP address as an authorized address, even if your hostname is unrestricted. For more information, see [Configure IP](https://cloud.google.com/sql/docs/mysql/configure-ip). 
`--password`=`PASSWORD`
     Cloud SQL user's password. 
`--password-policy-allowed-failed-attempts`=`PASSWORD_POLICY_ALLOWED_FAILED_ATTEMPTS`
     Number of failed login attempts allowed before a user is locked out. 
`--[no-]password-policy-enable-failed-attempts-check`
     Enables the failed login attempts check if set to true. Use `--password-policy-enable-failed-attempts-check` to enable and `--no-password-policy-enable-failed-attempts-check` to disable. 
`--[no-]password-policy-enable-password-verification`
     The current password must be specified when altering the password. Use `--password-policy-enable-password-verification` to enable and `--no-password-policy-enable-password-verification` to disable. 
`--password-policy-password-expiration-duration`=`PASSWORD_POLICY_PASSWORD_EXPIRATION_DURATION`
     Expiration duration after a password is updated, for example, 2d for 2 days. See `[gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes)` for information on duration formats. 
`--type`=`TYPE`
     Cloud SQL user's type. It determines the method to authenticate the user during login. See the list of user types at <https://cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/SqlUserType>
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha sql users create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/sql/users/create)
    
    
    [gcloud beta sql users create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/sql/users/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
