---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/agent-identity/auth-providers/authorizations/describe/
title: gcloud beta agent-identity auth-providers authorizations describe \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:33:16.023199+00:00
---

# gcloud beta agent-identity auth-providers authorizations describe  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/agent-identity/auth-providers/authorizations/describe/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta agent-identity auth-providers authorizations describe Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta agent-identity auth-providers authorizations describe - describe an authorization 
SYNOPSIS
    

`gcloud beta agent-identity auth-providers authorizations describe` (`AUTHORIZATION` : `--auth-provider`=`AUTH_PROVIDER` `--location`=`LOCATION`) [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Get details of a single authorization. 
EXAMPLES
     To describe authorization 'my-auth' for auth provider 'my-auth-provider' in location 'us-central1' and project 'my-project', run: 
    
    
    [gcloud beta agent-identity auth-providers authorizations](https://docs.cloud.google.com/sdk/gcloud/reference/beta/agent-identity/auth-providers/authorizations) describe my-auth --auth-provider=my-auth-provider --location=us-central1 --project=my-project

POSITIONAL ARGUMENTS
    

Authorization resource - Name of the resource The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `authorization` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`AUTHORIZATION`
     ID of the authorization or fully qualified identifier for the authorization. 

To set the `authorization` attribute: 

  * provide the argument `authorization` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--auth-provider`=`AUTH_PROVIDER`
     The authProvider id of the authorization resource. 

To set the `auth-provider` attribute: 

  * provide the argument `authorization` on the command line with a fully specified name; 
  * provide the argument `--auth-provider` on the command line. 


`--location`=`LOCATION`
     The location id of the authorization resource. 

To set the `location` attribute: 

  * provide the argument `authorization` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `agentidentity/v1alpha` API. The full documentation for this API can be found at: <https://cloud.google.com/iam/docs/>
NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud agent-identity auth-providers authorizations describe](https://docs.cloud.google.com/sdk/gcloud/reference/agent-identity/auth-providers/authorizations/describe)
    
    
    [gcloud alpha agent-identity auth-providers authorizations describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/agent-identity/auth-providers/authorizations/describe)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-21 UTC."],[],[]] 
