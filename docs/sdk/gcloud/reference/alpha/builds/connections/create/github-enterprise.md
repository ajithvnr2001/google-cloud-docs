---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/builds/connections/create/github-enterprise/
title: gcloud alpha builds connections create github-enterprise \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:56:01.621520+00:00
---

# gcloud alpha builds connections create github-enterprise  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/builds/connections/create/github-enterprise/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha builds connections create github-enterprise Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha builds connections create github-enterprise - create a Cloud Build Connection of type GitHub Enterprise 
SYNOPSIS
    

`gcloud alpha builds connections create github-enterprise` (`CONNECTION` : `--region`=`REGION`) `--host-uri`=`HOST_URI` [`--async`] [`--app-id`=`APP_ID` `--app-slug`=`APP_SLUG` `--private-key-secret-version`=`PRIVATE_KEY_SECRET_VERSION` `--webhook-secret-secret-version`=`WEBHOOK_SECRET_SECRET_VERSION` : `--app-installation-id`=`APP_INSTALLATION_ID`] [`--service-directory-service`=`SERVICE_DIRECTORY_SERVICE` : `--ssl-ca-file`=`SSL_CA_FILE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Create a Cloud Build Connection of type GitHub Enterprise. 

Connections for GitHub Enterprise can be created either by following an intallation process (that requires manual steps in a web browser) or by providing all the properties of an already-installed application as arguments to this command. 

If the GitHub Enterprise server can only be accessed within a VPC, a Service Directory service resource can be provided for connecting to it. 

EXAMPLES
     To create a connection by following the installation process, provide only the connection name and the host URI. If the server can only be accessed within a VPC, provide also the Service Directory service resource: 
    
    
    gcloud alpha builds connections create github-enterprise my-ghe-conn --project=myproj --region=us-central1 --host-uri=https://my.ghe-server.net --service-directory-service=projects/myproj/namespaces/x/services/mysds

The command will print a URL to be opened in a web browser in order create and install a GitHub App in that server. After following the URL, you can get the connection's installation state with The ``describe`` command: 
    
    
    [gcloud alpha builds connections describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/builds/connections/describe) my-ghe-conn --region=us-central1

If the connection's installation state is not COMPLETE yet, it will provide a link to continue the installation process. Once the connection is in installation state COMPLETE, repositories can be added to it (see ``gcloud`` alpha builds repositories create). 

\-- 

To create a complete connection (e.g. based on an existing installation), provide all the parameters: 
    
    
    gcloud alpha builds connections create github-enterprise my-ghe-conn --project=myproj --region=us-central1 --app-id=111 --app-slug=gcb-app --service-directory-service=projects/myproj/namespaces/x/services/mysds --private-key-secret-version=projects/myproj/secrets/pk/versions/1 --webhook-secret-secret-version=projects/myproj/secrets/whsecret/versions/1 --app-slug=myapp --app-installation-id=1234

Above command creates the connection in installation state COMPLETE, ready for adding repositories. 

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
    

`--host-uri`=`HOST_URI`
     URI of the GitHub Enterprise server. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
Group of arguments for the GitHub App properties. 
`--app-id`=`APP_ID`
     App ID of the GitHub App in the GitHub Enterprise server. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--app-slug`=`APP_SLUG`
     App slug (url-friendly name) of the GitHub App. When seeing the configuration page of the App (e.g. in https://my-ghe-server.net/settings/apps/my-app), the app-slug is the last component of the URL path ("my-app" in that example). 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--private-key-secret-version`=`PRIVATE_KEY_SECRET_VERSION`
     Secret containing the private key of the GitHub App. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--webhook-secret-secret-version`=`WEBHOOK_SECRET_SECRET_VERSION`
     Secret containing the webhook secret string for validating webhook events generated by the GitHub App. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--app-installation-id`=`APP_INSTALLATION_ID`
     Installation ID of the Cloud Build GitHub App. 
Group of arguments for configuring access through Service Directory. 
`--service-directory-service`=`SERVICE_DIRECTORY_SERVICE`
     Service Directory service resource to use for accessing the GitHub Enterprise Server. Necessary only if the server has no public access from the internet. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--ssl-ca-file`=`SSL_CA_FILE`
     File containing the SSL_CA to be used. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `cloudbuild/v2` API. The full documentation for this API can be found at: <https://cloud.google.com/cloud-build/docs/>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud builds connections create github-enterprise](https://docs.cloud.google.com/sdk/gcloud/reference/builds/connections/create/github-enterprise)
    
    
    [gcloud beta builds connections create github-enterprise](https://docs.cloud.google.com/sdk/gcloud/reference/beta/builds/connections/create/github-enterprise)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
