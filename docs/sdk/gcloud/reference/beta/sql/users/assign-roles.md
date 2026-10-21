---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/sql/users/assign-roles/
title: gcloud beta sql users assign-roles \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:07:10.927504+00:00
---

# gcloud beta sql users assign-roles  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/sql/users/assign-roles/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta sql users assign-roles Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta sql users assign-roles - updates a user's database roles in a given instance 
SYNOPSIS
    

`gcloud beta sql users assign-roles` `USERNAME` `--instance`=`INSTANCE`, `-i` `INSTANCE` `--type`=`TYPE` [`--async`] [`--database-roles`=[`ROLE`,…]] [`--host`=`HOST`] [`--revoke-existing-roles`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Updates a user's database roles in a given instance with a specified username and host. 
EXAMPLES
     To grant database roles ``role1`` and ``role2`` for ``my-user`` in instance ``prod-instance``, run: 
    
    
    gcloud beta sql users assign-roles my-user --instance=prod-instance --database-roles=role1,role2 --type=BUILT_IN

To revoke existing database roles and grant new database roles ``role3`` and ``role4`` for ``my-user`` in instance ``prod-instance``, run: 
    
    
    gcloud beta sql users assign-roles my-user --instance=prod-instance --revoke-existing-roles --database-roles=role3,role4 --type=BUILT_IN

POSITIONAL ARGUMENTS
    

`USERNAME`
     Cloud SQL username. 
REQUIRED FLAGS
    

`--instance`=`INSTANCE`, `-i` `INSTANCE`
     Cloud SQL instance ID. 
`--type`=`TYPE`
     Cloud SQL user's type. It determines the method to authenticate the user during login. See the list of user types at <https://cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/SqlUserType>
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--database-roles`=[`ROLE`,…]
     A comma-separated list of database roles to be assigned to the user. This option is only available for MySQL and PostgreSQL instances. You can include predefined Cloud SQL roles, like cloudsqlsuperuser, or your own custom roles. Custom roles must be created in the database before you can assign them. You can create roles using the CREATE ROLE statement for both MySQL and PostgreSQL. 
`--host`=`HOST`
     Cloud SQL user's hostname expressed as a specific IP address or address range. `%` denotes an unrestricted hostname. Applicable flag for MySQL instances; ignored for all other engines. Note, if you connect to your instance using IP addresses, you must add your client IP address as an authorized address, even if your hostname is unrestricted. For more information, see [Configure IP](https://cloud.google.com/sql/docs/mysql/configure-ip). 
`--revoke-existing-roles`
     A boolean flag for revoking existing database roles from the user. This option is only available for MySQL and PostgreSQL instances. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud sql users assign-roles](https://docs.cloud.google.com/sdk/gcloud/reference/sql/users/assign-roles)
    
    
    [gcloud alpha sql users assign-roles](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/sql/users/assign-roles)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
