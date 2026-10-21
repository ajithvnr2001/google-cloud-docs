---
url: https://docs.cloud.google.com/sdk/gcloud/reference/compute/health-checks/create/ssl/
title: gcloud compute health-checks create ssl \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:08:30.959182+00:00
---

# gcloud compute health-checks create ssl  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/compute/health-checks/create/ssl/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud compute health-checks create ssl Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud compute health-checks create ssl - create a SSL health check to monitor load balanced instances 
SYNOPSIS
    

`gcloud compute health-checks create ssl` `NAME` [`--check-interval`=`CHECK_INTERVAL`; default="5s"] [`--description`=`DESCRIPTION`] [`--enable-logging`] [`--healthy-threshold`=`HEALTHY_THRESHOLD`; default=2] [`--proxy-header`=`PROXY_HEADER`; default="NONE"] [`--request`=`REQUEST`] [`--response`=`RESPONSE`] [`--timeout`=`TIMEOUT`; default="5s"] [`--unhealthy-threshold`=`UNHEALTHY_THRESHOLD`; default=2] [`--global` | `--region`=`REGION`] [`--port`=`PORT`; default=80 `--port-name`=`PORT_NAME` `--use-serving-port`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `gcloud compute health-checks create ssl` is used to create a non-legacy health check using the SSL protocol. You can use this health check for Google Cloud load balancers or for managed instance group autohealing. For more information, see the health checks overview at: <https://cloud.google.com/load-balancing/docs/health-check-concepts>
POSITIONAL ARGUMENTS
    

`NAME`
     Name of the SSL health check to create. 
FLAGS
    

`--check-interval`=`CHECK_INTERVAL`; default="5s"
     How often to perform a health check for an instance. For example, specifying ``10s`` will run the check every 10 seconds. The default value is ``5s``. See $ [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes) for information on duration formats. 
`--description`=`DESCRIPTION`
     An optional string description for the SSL health check. 
`--enable-logging`
     Enable logging of health check probe results to Stackdriver. Logging is disabled by default. 

Use --no-enable-logging to disable logging. 

`--healthy-threshold`=`HEALTHY_THRESHOLD`; default=2
     The number of consecutive successful health checks before an unhealthy instance is marked as healthy. The default is 2. 
`--proxy-header`=`PROXY_HEADER`; default="NONE"
     The type of proxy protocol header to be sent to the backend. `PROXY_HEADER` must be one of: 

`NONE`
     No proxy header is added. 
`PROXY_V1`
     Adds the header "PROXY UNKNOWN\r\n". 
`--request`=`REQUEST`
     An optional string of up to 1024 characters to send once the health check TCP connection has been established. The health checker then looks for a reply of the string provided in the `--response` field. 

If `--response` is not configured, the health checker does not wait for a response and regards the probe as successful if the TCP or SSL handshake was successful. 

`--response`=`RESPONSE`
     An optional string of up to 1024 characters that the health checker expects to receive from the instance. If the response is not received exactly, the health check probe fails. If `--response` is configured, but not `--request`, the health checker will wait for a response anyway. Unless your system automatically sends out a message in response to a successful handshake, only configure `--response` to match an explicit `--request`. 
`--timeout`=`TIMEOUT`; default="5s"
     If Google Compute Engine doesn't receive a healthy response from the instance by the time specified by the value of this flag, the health check request is considered a failure. For example, specifying ``10s`` will cause the check to wait for 10 seconds before considering the request a failure. The default value is ``5s``. See $ [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes) for information on duration formats. 
`--unhealthy-threshold`=`UNHEALTHY_THRESHOLD`; default=2
     The number of consecutive health check failures before a healthy instance is marked as unhealthy. The default is 2. 
At most one of these can be specified: 

`--global`
     If set, the SSL health check is global. 
`--region`=`REGION`
     Region of the SSL health check to create. If not specified, you might be prompted to select a region (interactive mode only). 

To avoid prompting when this flag is omitted, you can set the ``compute/region`` property: 
    
    
    [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) compute/region REGION

A list of regions can be fetched by running: 
    
    
    [gcloud compute regions list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/regions/list)

To unset the property, run: 
    
    
    [gcloud config unset](https://docs.cloud.google.com/sdk/gcloud/reference/config/unset) compute/region

Alternatively, the region can be stored in the environment variable ``CLOUDSDK_COMPUTE_REGION``. 

These flags configure the port that the health check monitors. If none is specified, the default port of 80 is used. If both `--port` and `--port-name` are specified, `--port` takes precedence. 
`--port`=`PORT`; default=80
     The TCP port number that this health check monitors. 
`--port-name`=`PORT_NAME`
     The port name that this health check monitors. By default, this is empty. 
`--use-serving-port`
     If given, use the "serving port" for health checks: 

  * When health checking network endpoints in a Network Endpoint Group, use the port specified with each endpoint. `--use-serving-port` must be used when using a Network Endpoint Group as a backend as this flag specifies the `portSpecification` option for a Health Check object. 
  * When health checking other backends, use the port or named port of the backend service. 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha compute health-checks create ssl](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/health-checks/create/ssl)
    
    
    [gcloud beta compute health-checks create ssl](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/health-checks/create/ssl)
    
    
    [gcloud preview compute health-checks create ssl](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/health-checks/create/ssl)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
