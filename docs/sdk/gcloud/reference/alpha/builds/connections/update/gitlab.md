---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/builds/connections/update/gitlab/
title: gcloud alpha builds connections update gitlab \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:18:10.204529+00:00
---

# gcloud alpha builds connections update gitlab  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/builds/connections/update/gitlab/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha builds connections update gitlab Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha builds connections update gitlab - update a Cloud Build Connection of type gitlab.com or GitLab Enterprise 
SYNOPSIS
    

`gcloud alpha builds connections update gitlab` (`CONNECTION` : `--region`=`REGION`) [`--async`] [`--authorizer-token-secret-version`=`AUTHORIZER_TOKEN_SECRET_VERSION`] [`--[no-]disabled`] [`--host-uri`=`HOST_URI`] [`--read-authorizer-token-secret-version`=`READ_AUTHORIZER_TOKEN_SECRET_VERSION`] [`--service-directory-service`=`SERVICE_DIRECTORY_SERVICE`] [`--ssl-ca-file`=`SSL_CA_FILE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Update a Cloud Build Connection of type gitlab.com or GitLab Enterprise. 
EXAMPLES
     To update the ssl_ca, provide the connection name and the ssl_ca file: 
    
    
    gcloud alpha builds connections update gitlab my-gle-conn --region=us-west1 --ssl-ca-file=mycertificate.crt

To update the authorization token, provide the connection name and the new authorization token
    
    
    secret version.
    
    
    gcloud alpha builds connections update gitlab my-gle-conn --region=us-west1 --authorizer-token-secret-version=projects/myproj/secrets/api-pat/versions/1

POSITIONAL ARGUMENTS
    

Connection resource - Connection to update. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

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


FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--authorizer-token-secret-version`=`AUTHORIZER_TOKEN_SECRET_VERSION`
     Secret containing the api personal access token. 
`--[no-]disabled`
     If disabled is set to true, functionality is disabled for this connection. Repository based API methods and webhooks processing for repositories in this connection will be disabled. Use `--disabled` to enable and `--no-disabled` to disable. 
`--host-uri`=`HOST_URI`
     URI of the GitLab instance. 
`--read-authorizer-token-secret-version`=`READ_AUTHORIZER_TOKEN_SECRET_VERSION`
     Secret containing the read_repository personal access token. Required for GitLab Enterprise versions older than 13.10. 
`--service-directory-service`=`SERVICE_DIRECTORY_SERVICE`
     Service Directory service resource to use for accessing the GitLab Enterprise Server. Necessary only if the server has no public access from the internet. 
`--ssl-ca-file`=`SSL_CA_FILE`
     File containing the SSL_CA to be used. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `cloudbuild/v2` API. The full documentation for this API can be found at: <https://cloud.google.com/cloud-build/docs/>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud builds connections update gitlab](https://docs.cloud.google.com/sdk/gcloud/reference/builds/connections/update/gitlab)
    
    
    [gcloud beta builds connections update gitlab](https://docs.cloud.google.com/sdk/gcloud/reference/beta/builds/connections/update/gitlab)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-15 UTC."],[],[]] 
