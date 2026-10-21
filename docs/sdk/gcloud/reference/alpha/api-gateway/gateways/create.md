---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/api-gateway/gateways/create/
title: gcloud alpha api-gateway gateways create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:22:12.707788+00:00
---

# gcloud alpha api-gateway gateways create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/api-gateway/gateways/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha api-gateway gateways create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha api-gateway gateways create - create a new gateway 
SYNOPSIS
    

`gcloud alpha api-gateway gateways create` (`GATEWAY` : `--location`=`LOCATION`) (`--api-config`=`API_CONFIG` : `--api`=`API`) [`--async`] [`--display-name`=`DISPLAY_NAME`] [`--enable-streaming`] [`--labels`=[`KEY`=`VALUE`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Create a new gateway. 
EXAMPLES
     To create a gateway in 'us-central1' run: 
    
    
    gcloud alpha api-gateway gateways create my-gateway --api=my-api --api-config=my-config --location=us-central1

POSITIONAL ARGUMENTS
    

Gateway resource - Name for gateway which will be created. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `gateway` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`GATEWAY`
     ID of the gateway or fully qualified identifier for the gateway. 

To set the `gateway` attribute: 

  * provide the argument `gateway` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     Cloud location for gateway. 

To set the `location` attribute: 

  * provide the argument `gateway` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


REQUIRED FLAGS
    

Api config resource - Resource name for API config the gateway will use. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--api-config` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `--api-config` on the command line with a fully specified name; 
  * Location for API and API Configs. Defaults to global. 



This must be specified. 

`--api-config`=`API_CONFIG`
     ID of the api-config or fully qualified identifier for the api-config. 

To set the `api-config` attribute: 

  * provide the argument `--api-config` on the command line. 



This flag argument must be specified if any of the other arguments in this group are specified. 

`--api`=`API`
     API ID. 

To set the `api` attribute: 

  * provide the argument `--api-config` on the command line with a fully specified name; 
  * provide the argument `--api` on the command line. 


OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--display-name`=`DISPLAY_NAME`
     Human readable name which can optionally be supplied. 
`--enable-streaming`
     Creates the gateway with streaming enabled, which supports Server-Sent Events (SSE), HTTP/2 streaming, HTTP chunked transfer, WebSockets, and gRPC bidirectional streaming. 

This can only be set when the gateway is created and cannot be changed afterwards. When omitted, API Gateway selects the streaming mode. 

The API config's backend `deadline` field governs how long a request (unary or streaming) may run. 

Enabling streaming on a gateway does not change how the `deadline` field behaves on an SSE or chunked-transfer path. The deadline remains a wall-clock bound on the complete response, so a stream is cut once the deadline elapses regardless of how much data it is sending. The default is 15 seconds and the maximum is 3,600 seconds. 

On gRPC streaming and WebSockets, `deadline` bounds the gap between messages instead: default 300 seconds; set `deadline` to change it, up to 3,600 seconds. On WebSockets, a `deadline` of less than 300 seconds is ignored and a 300-second minimum applies. The maximum total request duration is always 3,600 seconds, not configurable. 

`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud api-gateway gateways create](https://docs.cloud.google.com/sdk/gcloud/reference/api-gateway/gateways/create)
    
    
    [gcloud beta api-gateway gateways create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/api-gateway/gateways/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
