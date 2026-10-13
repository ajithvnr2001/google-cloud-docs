---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/builds/connections/create/bitbucket-data-center/
title: gcloud beta builds connections create bitbucket-data-center \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:22:09.596046+00:00
---

# gcloud beta builds connections create bitbucket-data-center  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/builds/connections/create/bitbucket-data-center/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta builds connections create bitbucket-data-center Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta builds connections create bitbucket-data-center - create a Cloud Build Connection for Bitbucket Data Center 
SYNOPSIS
    

`gcloud beta builds connections create bitbucket-data-center` (`CONNECTION` : `--region`=`REGION`) `--authorizer-token-secret-version`=`AUTHORIZER_TOKEN_SECRET_VERSION` `--read-authorizer-token-secret-version`=`READ_AUTHORIZER_TOKEN_SECRET_VERSION` `--webhook-secret-secret-version`=`WEBHOOK_SECRET_SECRET_VERSION` [`--async`] [`--host-uri`=`HOST_URI`] [`--service-directory-service`=`SERVICE_DIRECTORY_SERVICE` : `--ssl-ca-file`=`SSL_CA_FILE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Create a Cloud Build Connection for Bitbucket Data Center. 

A Bitbucket Data Center Connection can be created by using a personal access token with `REPO_ADMIN` scope permission. A `REPO_READ` scoped personal access token will also be required. 

If the Bitbucket Data Center can only be accessed within a VPC, a Service Directory service resource can be provided for connecting to it. 

EXAMPLES
     To create a Bitbucket Data Center connection, provide all the required parameters: 
    
    
    gcloud beta builds connections create bitbucket-data-center my-bitbucket-conn --project=myproj --region=us-central1 --host-uri=https://bitbucket-server.net --read-authorizer-token-secret-version=projects/myproj/secrets/read-pat/versions/1 --authorizer-token-secret-version=projects/myproj/secrets/admin-pat/versions/1 --webhook-secret-secret-version=projects/myproj/secrets/whsecret/versions/1

To create a Bitbucket Data Center connection for a private Bitbucket Data Center server. Provide the service-directory-service and ssl-ca-file as well: 
    
    
    gcloud beta builds connections create bitbucket-data-center my-private-bitbucket-conn --host-uri=https://my.private-bitbucket-server.net --project=myproj --region=us-central1 --service-directory-service=projects/myproj/namespaces/x/services/mysds --ssl-ca-file=mycertificate.crt --authorizer-token-secret-version=projects/myproj/secrets/admin-pat/versions/1 --read-authorizer-token-secret-version=projects/myproj/secrets/read-pat/versions/1 --webhook-secret-secret-version=projects/myproj/secrets/whsecret/versions/1

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
     Secret containing the REPO_ADMIN personal access token. 
`--read-authorizer-token-secret-version`=`READ_AUTHORIZER_TOKEN_SECRET_VERSION`
     Secret containing the REPO_READ personal access token. 
`--webhook-secret-secret-version`=`WEBHOOK_SECRET_SECRET_VERSION`
     Secret containing the webhook secret string for validating webhook events sent by Bitbucket Data Center. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--host-uri`=`HOST_URI`
     URI of the Bitbucket Data Center instance. 
Group of arguments for configuring access through Service Directory. 
`--service-directory-service`=`SERVICE_DIRECTORY_SERVICE`
     Service Directory service resource to use for accessing the Bitbucket Data Center. Necessary only if the server has no public access from the internet. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--ssl-ca-file`=`SSL_CA_FILE`
     File containing the SSL_CA to be used. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `cloudbuild/v2` API. The full documentation for this API can be found at: <https://cloud.google.com/cloud-build/docs/>
NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud builds connections create bitbucket-data-center](https://docs.cloud.google.com/sdk/gcloud/reference/builds/connections/create/bitbucket-data-center)
    
    
    [gcloud alpha builds connections create bitbucket-data-center](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/builds/connections/create/bitbucket-data-center)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
