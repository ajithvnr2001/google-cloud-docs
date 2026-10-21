---
url: https://docs.cloud.google.com/sdk/gcloud/reference/builds/connections/create/bitbucket-cloud/
title: gcloud builds connections create bitbucket-cloud \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:40:01.276836+00:00
---

# gcloud builds connections create bitbucket-cloud  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/builds/connections/create/bitbucket-cloud/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud builds connections create bitbucket-cloud Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud builds connections create bitbucket-cloud - create a Cloud Build Connection for Bitbucket Cloud 
SYNOPSIS
    

`gcloud builds connections create bitbucket-cloud` (`CONNECTION` : `--region`=`REGION`) `--authorizer-token-secret-version`=`AUTHORIZER_TOKEN_SECRET_VERSION` `--read-authorizer-token-secret-version`=`READ_AUTHORIZER_TOKEN_SECRET_VERSION` `--webhook-secret-secret-version`=`WEBHOOK_SECRET_SECRET_VERSION` `--workspace`=`WORKSPACE` [`--async`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Create a Cloud Build Connection for Bitbucket Cloud. 

A Bitbucket Cloud Connection can be created by using a repository/project/workspace access token with `repository_read`,`repository_admin`, `pullrequest_read`, `webhook` scope permission and a repository/project/workspace access token with `repository_read` scope permission. 

EXAMPLES
     To create a Bitbucket Cloud connection, provide all the required parameters: 
    
    
    gcloud builds connections create bitbucket-cloud my-bitbucket-conn --project=myproj --region=us-central1 --workspace=my-workspace --read-authorizer-token-secret-version=projects/myproj/secrets/read-pat/versions/1 --authorizer-token-secret-version=projects/myproj/secrets/admin-pat/versions/1 --webhook-secret-secret-version=projects/myproj/secrets/whsecret/versions/1

POSITIONAL ARGUMENTS
    

Connection resource - Connection to create. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `connection` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`CONNECTION`
     ID of the connection or fully qualified identifier for the connection. 

To set the `connection` attribute: 

  * provide the argument `connection` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--region`=`REGION`
     The Google Cloud region. 

To set the `region` attribute: 

  * provide the argument `connection` on the command line with a fully specified name; 
  * provide the argument `--region` on the command line; 
  * set the property `builds/region`. 


REQUIRED FLAGS
    

`--authorizer-token-secret-version`=`AUTHORIZER_TOKEN_SECRET_VERSION`
     Secret containing the `repository_read`,`repository_admin`, `pullrequest_read`, `webhook` repository/project/workspace access token. 
`--read-authorizer-token-secret-version`=`READ_AUTHORIZER_TOKEN_SECRET_VERSION`
     Secret containing the `repository_read` repository/project/workspace access token. 
`--webhook-secret-secret-version`=`WEBHOOK_SECRET_SECRET_VERSION`
     Secret containing the webhook secret string for validating webhook events sent by Bitbucket Cloud. 
`--workspace`=`WORKSPACE`
     Workspace of the Bitbucket Cloud instance. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `cloudbuild/v2` API. The full documentation for this API can be found at: <https://cloud.google.com/cloud-build/docs/>
NOTES
     These variants are also available: 
    
    
    [gcloud alpha builds connections create bitbucket-cloud](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/builds/connections/create/bitbucket-cloud)
    
    
    [gcloud beta builds connections create bitbucket-cloud](https://docs.cloud.google.com/sdk/gcloud/reference/beta/builds/connections/create/bitbucket-cloud)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
