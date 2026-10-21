---
url: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/target-grpc-proxies/create/
title: gcloud preview compute target-grpc-proxies create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T04:28:02.203645+00:00
---

# gcloud preview compute target-grpc-proxies create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/target-grpc-proxies/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud preview compute target-grpc-proxies create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud preview compute target-grpc-proxies create - create a target gRPC proxy 
SYNOPSIS
    

`gcloud preview compute target-grpc-proxies create` `NAME` `--url-map`=`URL_MAP` [`--description`=`DESCRIPTION`] [`--validate-for-proxyless`] [`--global-url-map` | `--url-map-region`=`URL_MAP_REGION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(PREVIEW)` `gcloud preview compute target-grpc-proxies create` is used to create target gRPC proxies. A target gRPC proxy is a component of load balancers intended for load balancing gRPC traffic. Global forwarding rules reference a target gRPC proxy. The Target gRPC proxy references a URL map which specifies how traffic routes to gRPC backend services. 
EXAMPLES
     If there is an already-created URL map with the name URL_MAP, create a global target gRPC proxy pointing to this map by running: 
    
    
    gcloud preview compute target-grpc-proxies create PROXY_NAME --url-map=URL_MAP

To create a proxy with a textual description, run: 
    
    
    gcloud preview compute target-grpc-proxies create PROXY_NAME --url-map=URL_MAP --description="default proxy"

POSITIONAL ARGUMENTS
    

`NAME`
     Name of the target gRPC proxy to create. 
REQUIRED FLAGS
    

`--url-map`=`URL_MAP`
     A reference to a URL map resource. A URL map defines the mapping of URLs to backend services. Before you can refer to a URL map, you must create the URL map. To delete a URL map that a target proxy is referring to, you must first delete the target gRPC proxy. 
OPTIONAL FLAGS
    

`--description`=`DESCRIPTION`
     An optional, textual description for the target gRPC proxy. 
`--validate-for-proxyless`
     If specified, configuration in the associated urlMap and the BackendServices is checked to allow only the features that are supported in the latest release of gRPC. 

If unspecified, no such configuration checks are performed. This may cause unexpected behavior in gRPC applications if unsupported features are configured. 

At most one of these can be specified: 

`--global-url-map`
     If set, the URL map is global. 
`--url-map-region`=`URL_MAP_REGION`
     Region of the URL map to operate on. Overrides the default `compute/region` property value for this command invocation. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in DEVELOPER PREVIEW and may change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud compute target-grpc-proxies create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/target-grpc-proxies/create)
    
    
    [gcloud alpha compute target-grpc-proxies create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/target-grpc-proxies/create)
    
    
    [gcloud beta compute target-grpc-proxies create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/target-grpc-proxies/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
