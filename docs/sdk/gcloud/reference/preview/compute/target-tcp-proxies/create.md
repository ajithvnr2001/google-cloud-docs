---
url: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/target-tcp-proxies/create/
title: gcloud preview compute target-tcp-proxies create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T22:13:43.545174+00:00
---

# gcloud preview compute target-tcp-proxies create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/target-tcp-proxies/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud preview compute target-tcp-proxies create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud preview compute target-tcp-proxies create - create a target TCP proxy 
SYNOPSIS
    

`gcloud preview compute target-tcp-proxies create` `NAME` [`--backend-service`=`BACKEND_SERVICE`] [`--description`=`DESCRIPTION`] [`--load-balancing-scheme`=`LOAD_BALANCING_SCHEME`] [`--[no-]proxy-bind`] [`--proxy-header`=`PROXY_HEADER`; default="NONE"] [`--backend-service-region`=`BACKEND_SERVICE_REGION` | `--global-backend-service`] [`--global` | `--region`=`REGION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(PREVIEW)` `gcloud preview compute target-tcp-proxies create` is used to create target TCP proxies. A target TCP proxy is referenced by one or more forwarding rules which define which packets the proxy is responsible for routing. The target TCP proxy points to a backend service which handle the actual requests. 
POSITIONAL ARGUMENTS
    

`NAME`
     Name of the target TCP proxy to create. 
FLAGS
    

`--backend-service`=`BACKEND_SERVICE`
     A backend service that will be used for connections to the target TCP proxy. 
`--description`=`DESCRIPTION`
     An optional, textual description for the target TCP proxy. 
`--load-balancing-scheme`=`LOAD_BALANCING_SCHEME`
     Specifies the load balancing scheme for the target TCP proxy. `LOAD_BALANCING_SCHEME` must be one of: 

`EXTERNAL`
     Classic Proxy Network Load Balancers. 
`EXTERNAL_MANAGED`
     Envoy-based global and regional external Proxy Network Load Balancer. 
`INTERNAL_MANAGED`
     Envoy-based cross-region and regional internal Proxy Network Load Balancer. 
`--[no-]proxy-bind`
     This field only applies when the forwarding rule that references this target proxy has a `--load-balancing-scheme` set to `INTERNAL_SELF_MANAGED`. 

When this field is set to `true`, Envoy proxies set up inbound traffic interception and bind to the IP address and port specified in the forwarding rule. This is generally useful when using Traffic Director to configure Envoy as a gateway or middle proxy (in other words, not a sidecar proxy). The Envoy proxy listens for inbound requests and handles requests when it receives them. 

Use `--proxy-bind` to enable and `--no-proxy-bind` to disable. 

`--proxy-header`=`PROXY_HEADER`; default="NONE"
     The type of proxy protocol header to be sent to the backend. `PROXY_HEADER` must be one of: 

`NONE`
     No proxy header is added. 
`PROXY_V1`
     Enables PROXY protocol (version 1) for passing client connection information. 
At most one of these can be specified: 

`--backend-service-region`=`BACKEND_SERVICE_REGION`
     Region of the backend service to operate on. If not specified it will be set to the region of the TCP Proxy. Overrides the default `compute/region` property value for this command invocation. 
`--global-backend-service`
     If set, the backend service is global. 
At most one of these can be specified: 

`--global`
     If set, the target TCP proxy is global. 
`--region`=`REGION`
     Region of the target TCP proxy to create. If not specified, you might be prompted to select a region (interactive mode only). 

To avoid prompting when this flag is omitted, you can set the ``compute/region`` property: 
    
    
    [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) compute/region REGION

A list of regions can be fetched by running: 
    
    
    [gcloud compute regions list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/regions/list)

To unset the property, run: 
    
    
    [gcloud config unset](https://docs.cloud.google.com/sdk/gcloud/reference/config/unset) compute/region

Alternatively, the region can be stored in the environment variable ``CLOUDSDK_COMPUTE_REGION``. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in DEVELOPER PREVIEW and may change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud compute target-tcp-proxies create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/target-tcp-proxies/create)
    
    
    [gcloud alpha compute target-tcp-proxies create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/target-tcp-proxies/create)
    
    
    [gcloud beta compute target-tcp-proxies create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/target-tcp-proxies/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-14 UTC."],[],[]] 
