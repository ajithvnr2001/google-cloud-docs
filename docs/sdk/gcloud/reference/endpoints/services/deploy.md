---
url: https://docs.cloud.google.com/sdk/gcloud/reference/endpoints/services/deploy/
title: gcloud endpoints services deploy \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:49:30.665712+00:00
---

# gcloud endpoints services deploy  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/endpoints/services/deploy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud endpoints services deploy Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud endpoints services deploy - deploys a service configuration for the given service name 
SYNOPSIS
    

`gcloud endpoints services deploy` `SERVICE_CONFIG_FILE` [`SERVICE_CONFIG_FILE` …] [`--async`] [`--force`, `-f`] [`--validate-only`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     This command is used to deploy a service configuration for a service to Google Service Management. As input, it takes one or more paths to service configurations that should be uploaded. These configuration files can be Proto Descriptors, Open API (Swagger) specifications, or Google Service Configuration files in JSON or YAML formats. 

If a service name is present in multiple configuration files (given in the `host` field in OpenAPI specifications or the `name` field in Google Service Configuration files), the first one will take precedence. 

This command will block until deployment is complete unless the `--async` flag is passed. 

EXAMPLES
     To deploy a single Open API service configuration, run: 
    
    
    gcloud endpoints services deploy ~/my_app/openapi.json

To run the deployment asynchronously (non-blocking), run: 
    
    
    gcloud endpoints services deploy ~/my_app/openapi.json --async

To deploy a service config with a Proto, run: 
    
    
    gcloud endpoints services deploy ~/my_app/service-config.yaml ~/my_app/service-protos.pb

POSITIONAL ARGUMENTS
    

`SERVICE_CONFIG_FILE` [`SERVICE_CONFIG_FILE` …]
     The service configuration file (or files) containing the API specification to upload. Proto Descriptors, Open API (Swagger) specifications, and Google Service Configuration files in JSON and YAML formats are acceptable. 
FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--force`, `-f`
     Force the deployment even if any hazardous changes to the service configuration are detected. 
`--validate-only`
     If included, the command validates the service configuration(s), but does not deploy them. The service must exist in order to validate the configuration(s). 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha endpoints services deploy](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/endpoints/services/deploy)
    
    
    [gcloud beta endpoints services deploy](https://docs.cloud.google.com/sdk/gcloud/reference/beta/endpoints/services/deploy)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
