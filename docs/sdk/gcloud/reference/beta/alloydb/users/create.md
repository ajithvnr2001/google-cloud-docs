---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/alloydb/users/create/
title: gcloud beta alloydb users create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:21:38.542850+00:00
---

# gcloud beta alloydb users create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/alloydb/users/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta alloydb users create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta alloydb users create - creates a user in a given cluster 
SYNOPSIS
    

`gcloud beta alloydb users create` `USERNAME` `--cluster`=`CLUSTER` `--region`=`REGION` [`--db-roles`=[`ROLE`,…]] [`--keep-extra-roles`=`KEEP_EXTRA_ROLES`] [`--password`=`PASSWORD`] [`--superuser`=`SUPERUSER`] [`--type`=`TYPE`; default=`"BUILT_IN"`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Creates a user in a given cluster with specified username, cluster, region, type, and password. 
EXAMPLES
     To create a new user, run: 
    
    
    gcloud beta alloydb users create my-username --cluster=my-cluster --region=us-central1 --password=postgres

POSITIONAL ARGUMENTS
    

`USERNAME`
     AlloyDB username 
REQUIRED FLAGS
    

`--cluster`=`CLUSTER`
     AlloyDB cluster ID 
`--region`=`REGION`
     Regional location (e.g. `asia-east1`, `us-east1`). See the full list of regions at <https://cloud.google.com/sql/docs/instance-locations>. 
OPTIONAL FLAGS
    

`--db-roles`=[`ROLE`,…]
     Comma separated list of database roles this new user will be granted upon creation. 
`--keep-extra-roles`=`KEEP_EXTRA_ROLES`
     If the user already exists and has extra roles, keep them. 
`--password`=`PASSWORD`
     Password for this database user. 
`--superuser`=`SUPERUSER`
     If true, new user will have AlloyDB superuser privileges. Default value is false. 
`--type`=`TYPE`; default=`"BUILT_IN"`
     Type corresponds to the user type. `TYPE` must be one of: 

`BUILT_IN`
     This database user can authenticate via password-based authentication 
`IAM_BASED`
     This database user can authenticate via IAM-based authentication 
`IAM_GROUP`
     This database user represents an IAM group whose members can authenticate via IAM group-based authentication 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud alloydb users create](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/users/create)
    
    
    [gcloud alpha alloydb users create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/alloydb/users/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
