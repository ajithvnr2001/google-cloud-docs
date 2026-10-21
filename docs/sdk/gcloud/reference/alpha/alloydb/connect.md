---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/alloydb/connect/
title: gcloud alpha alloydb connect \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:03:48.731605+00:00
---

# gcloud alpha alloydb connect  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/alloydb/connect/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha alloydb connect Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha alloydb connect - connect to an AlloyDB instance using the AlloyDB Auth Proxy 
SYNOPSIS
    

`gcloud alpha alloydb connect` `INSTANCE` `--cluster`=`CLUSTER` `--region`=`REGION` [`--database`=`DATABASE`, `-d` `DATABASE`] [`--port`=`PORT`; default=9471] [`--auto-iam-authn` | `--user`=`USER`, `-u` `USER`] [`--psc` | `--public-ip`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Connects to an AlloyDB instance using the AlloyDB Auth Proxy and psql. 
EXAMPLES
     To connect to an AlloyDB instance using the postgres user and database over private IP, run: 
    
    
    gcloud alpha alloydb connect my-instance --cluster=my-cluster --region=us-central1

To connect over public IP, run: 
    
    
    gcloud alpha alloydb connect my-instance --cluster=my-cluster --region=us-central1 --public-ip

To connect over Private Service Connect, run: 
    
    
    gcloud alpha alloydb connect my-instance --cluster=my-cluster --region=us-central1 --psc

To connect with a particular user and database, run: 
    
    
    gcloud alpha alloydb connect my-instance --cluster=my-cluster --region=us-central1 --user mydbuser --database mydatabase

To connect with Auto IAM Authentication using your authenticated gcloud user, run 
    
    
    gcloud alpha alloydb connect my-instance --cluster=my-cluster --region=us-central1 --auto-iam-authn

To use an impersonated service account with the AlloyDB Auth Proxy, run: 
    
    
    gcloud alpha alloydb connect my-instance --cluster=my-cluster --region=us-central1 --impersonate-service-account impersonated@myproject.iam.gserviceaccount.com

NOTE: the impersonated service account will be used by the Auth Proxy to retrieve connection info, but will not be used for authenticating to the database. To also authenticate to the database as the impersonated user, add the \--auto-iam-authn flag. 

To use an impersonated service account with the AlloyDB Auth Proxy and authenticate to your database with the same impersonated user, run: 
    
    
    gcloud alpha alloydb connect my-instance --cluster=my-cluster --region=us-central1 --impersonate-service-account impersonated@myproject.iam.gserviceaccount.com --auto-iam-authn

POSITIONAL ARGUMENTS
    

`INSTANCE`
     AlloyDB instance ID 
REQUIRED FLAGS
    

`--cluster`=`CLUSTER`
     AlloyDB cluster ID 
`--region`=`REGION`
     Regional location (e.g. `asia-east1`, `us-east1`). See the full list of regions at <https://cloud.google.com/sql/docs/instance-locations>. 
OPTIONAL FLAGS
    

`--database`=`DATABASE`, `-d` `DATABASE`
     The AlloyDB database to connect to 
`--port`=`PORT`; default=9471
     Port number used by the AlloyDB Auth Proxy to start a localhost listener 
At most one of these can be specified: 

`--auto-iam-authn`
     Enables Auto IAM authentication 
`--user`=`USER`, `-u` `USER`
     Built-in database user to connect to the database as 
At most one of these can be specified: 

`--psc`
     Connect to the AlloyDB instance using Private Service Connect. 
`--public-ip`
     Connect to the AlloyDB instance with Public IP 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud beta alloydb connect](https://docs.cloud.google.com/sdk/gcloud/reference/beta/alloydb/connect)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
