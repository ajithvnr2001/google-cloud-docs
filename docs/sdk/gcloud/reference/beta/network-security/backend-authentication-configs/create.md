---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security/backend-authentication-configs/create/
title: gcloud beta network-security backend-authentication-configs create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:55:49.472392+00:00
---

# gcloud beta network-security backend-authentication-configs create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security/backend-authentication-configs/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta network-security backend-authentication-configs create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta network-security backend-authentication-configs create - create a BackendAuthenticationConfig 
SYNOPSIS
    

`gcloud beta network-security backend-authentication-configs create` (`BACKEND_AUTHENTICATION_CONFIG` : `--location`=`LOCATION`) [`--async`] [`--client-certificate`=`CLIENT_CERTIFICATE`] [`--description`=`DESCRIPTION`] [`--labels`=[`KEY`=`VALUE`,…]] [`--trust-config`=`TRUST_CONFIG`] [`--well-known-roots`=`WELL_KNOWN_ROOTS`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Create a new BackendAuthenticationConfig. 
EXAMPLES
     To create a config named `backend-authentication-config`, run: 
    
    
    [gcloud beta network-security backend-authentication-configs](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security/backend-authentication-configs) create backend-authentication-config --trust-config=projects/my-project/locations/global/trustConfigs/my-trust-config --location=global

POSITIONAL ARGUMENTS
    

Backend authentication config resource - Realm to be created. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `backend_authentication_config` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`BACKEND_AUTHENTICATION_CONFIG`
     ID of the backend authentication config or fully qualified identifier for the backend authentication config. 

To set the `backend_authentication_config` attribute: 

  * provide the argument `backend_authentication_config` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location Id. To set the `location` attribute: 

  * provide the argument `backend_authentication_config` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--client-certificate`=`CLIENT_CERTIFICATE`
     ID of certificate resource. 
`--description`=`DESCRIPTION`
     Description of the backend authentication config. 
`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 
`--trust-config`=`TRUST_CONFIG`
     ID of trust config resource. 
`--well-known-roots`=`WELL_KNOWN_ROOTS`
     Indicates whether the load balancer should trust backend server certificates. `WELL_KNOWN_ROOTS` must be one of: `none`, `public-roots`. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `networksecurity/v1beta1` API. The full documentation for this API can be found at: <https://cloud.google.com/networking>
NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud network-security backend-authentication-configs create](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/backend-authentication-configs/create)
    
    
    [gcloud alpha network-security backend-authentication-configs create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/network-security/backend-authentication-configs/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
