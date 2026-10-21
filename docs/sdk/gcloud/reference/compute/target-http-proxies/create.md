---
url: https://docs.cloud.google.com/sdk/gcloud/reference/compute/target-http-proxies/create/
title: gcloud compute target-http-proxies create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:29:29.140539+00:00
---

# gcloud compute target-http-proxies create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/compute/target-http-proxies/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud compute target-http-proxies create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud compute target-http-proxies create - create a target HTTP proxy 
SYNOPSIS
    

`gcloud compute target-http-proxies create` `NAME` `--url-map`=`URL_MAP` [`--description`=`DESCRIPTION`] [`--http-keep-alive-timeout-sec`=`HTTP_KEEP_ALIVE_TIMEOUT_SEC`] [`--global` | `--region`=`REGION`] [`--global-url-map` | `--url-map-region`=`URL_MAP_REGION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `gcloud compute target-http-proxies create` is used to create target HTTP proxies. A target HTTP proxy is referenced by one or more forwarding rules which specify the network traffic that the proxy is responsible for routing. The target HTTP proxy points to a URL map that defines the rules for routing the requests. The URL map's job is to map URLs to backend services which handle the actual requests. 
EXAMPLES
     If there is an already-created URL map with the name URL_MAP, create a global target HTTP proxy pointing to this map by running: 
    
    
    gcloud compute target-http-proxies create PROXY_NAME --url-map=URL_MAP

Create a regional target HTTP proxy by running: 
    
    
    gcloud compute target-http-proxies create PROXY_NAME --url-map=URL_MAP --region=REGION_NAME

To create a proxy with a textual description, run: 
    
    
    gcloud compute target-http-proxies create PROXY_NAME --url-map=URL_MAP --description="default proxy"

POSITIONAL ARGUMENTS
    

`NAME`
     Name of the target HTTP proxy to create. 
REQUIRED FLAGS
    

`--url-map`=`URL_MAP`
     A reference to a URL map resource. A URL map defines the mapping of URLs to backend services. Before you can refer to a URL map, you must create the URL map. To delete a URL map that a target proxy is referring to, you must first delete the target HTTP proxy. 
OPTIONAL FLAGS
    

`--description`=`DESCRIPTION`
     An optional, textual description for the target HTTP proxy. 
`--http-keep-alive-timeout-sec`=`HTTP_KEEP_ALIVE_TIMEOUT_SEC`
     Represents the maximum amount of time that a TCP connection can be idle between the (downstream) client and the target HTTP proxy. If an HTTP keepalive timeout is not specified, the default value is 610 seconds. For global external Application Load Balancers, the minimum allowed value is 5 seconds and the maximum allowed value is 1200 seconds. 
At most one of these can be specified: 

`--global`
     If set, the target HTTP proxy is global. 
`--region`=`REGION`
     Region of the target HTTP proxy to create. If not specified, you might be prompted to select a region (interactive mode only). 

To avoid prompting when this flag is omitted, you can set the ``compute/region`` property: 
    
    
    [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) compute/region REGION

A list of regions can be fetched by running: 
    
    
    [gcloud compute regions list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/regions/list)

To unset the property, run: 
    
    
    [gcloud config unset](https://docs.cloud.google.com/sdk/gcloud/reference/config/unset) compute/region

Alternatively, the region can be stored in the environment variable ``CLOUDSDK_COMPUTE_REGION``. 

At most one of these can be specified: 

`--global-url-map`
     If set, the URL map is global. 
`--url-map-region`=`URL_MAP_REGION`
     Region of the URL map to operate on. Overrides the default `compute/region` property value for this command invocation. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha compute target-http-proxies create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/target-http-proxies/create)
    
    
    [gcloud beta compute target-http-proxies create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/target-http-proxies/create)
    
    
    [gcloud preview compute target-http-proxies create](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/target-http-proxies/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
