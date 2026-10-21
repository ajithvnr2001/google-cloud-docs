---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/api-gateway/api-configs/create/
title: gcloud alpha api-gateway api-configs create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:22:10.463472+00:00
---

# gcloud alpha api-gateway api-configs create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/api-gateway/api-configs/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha api-gateway api-configs create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha api-gateway api-configs create - add a new config to an API 
SYNOPSIS
    

`gcloud alpha api-gateway api-configs create` (`API_CONFIG` : `--api`=`API`) (`--grpc-files`=[`FILE`,…] | `--openapi-spec`=[`FILE`,…]) [`--async`] [`--backend-auth-service-account`=`BACKEND_AUTH_SERVICE_ACCOUNT`] [`--display-name`=`DISPLAY_NAME`] [`--labels`=[`KEY`=`VALUE`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Add a new config to an API. 

NOTE: If the specified API does not exist it will be created. 

EXAMPLES
     To create an API config for the API 'my-api' with an OpenAPI spec, run: 
    
    
    gcloud alpha api-gateway api-configs create my-config --api=my-api --openapi-spec=path/to/openapi_spec.yaml

POSITIONAL ARGUMENTS
    

Api config resource - Name for API Config which will be created. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `api_config` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `api_config` on the command line with a fully specified name; 
  * Location for API and API Configs. Defaults to global. 



This must be specified. 

`API_CONFIG`
     ID of the api-config or fully qualified identifier for the api-config. 

To set the `api-config` attribute: 

  * provide the argument `api_config` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--api`=`API`
     API ID. 

To set the `api` attribute: 

  * provide the argument `api_config` on the command line with a fully specified name; 
  * provide the argument `--api` on the command line. 


REQUIRED FLAGS
    

Configuration files for the API. 

Exactly one of these must be specified: 

`--grpc-files`=[`FILE`,…]
     Files describing the GRPC service. Google Service Configuration files in JSON or YAML formats as well as Proto descriptors should be listed. 
`--openapi-spec`=[`FILE`,…]
     The OpenAPI specifications containing service configuration information, and API specification for the gateway. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--backend-auth-service-account`=`BACKEND_AUTH_SERVICE_ACCOUNT`
     Service account which will be used to sign tokens for backends with authentication configured. 
`--display-name`=`DISPLAY_NAME`
     Human readable name which can optionally be supplied. 
`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud api-gateway api-configs create](https://docs.cloud.google.com/sdk/gcloud/reference/api-gateway/api-configs/create)
    
    
    [gcloud beta api-gateway api-configs create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/api-gateway/api-configs/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
