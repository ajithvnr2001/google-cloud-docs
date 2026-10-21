---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/health-checks/update/https/
title: gcloud alpha compute health-checks update https \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T08:16:26.232309+00:00
---

# gcloud alpha compute health-checks update https  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/health-checks/update/https/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha compute health-checks update https Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha compute health-checks update https - update a HTTPS health check 
SYNOPSIS
    

`gcloud alpha compute health-checks update https` `NAME` [`--check-interval`=`CHECK_INTERVAL`] [`--description`=`DESCRIPTION`] [`--enable-logging`] [`--healthy-threshold`=`HEALTHY_THRESHOLD`] [`--host`=`HOST`] [`--proxy-header`=`PROXY_HEADER`] [`--request-path`=`REQUEST_PATH`] [`--response`=`RESPONSE`] [`--source-regions`=`REGION`,…,[…]] [`--timeout`=`TIMEOUT`] [`--unhealthy-threshold`=`UNHEALTHY_THRESHOLD`] [`--weight-report-mode`=`WEIGHT_REPORT_MODE`] [`--global` | `--region`=`REGION`] [`--port`=`PORT` `--port-name`=`PORT_NAME` `--use-serving-port`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` `gcloud alpha compute health-checks update https` is used to update an existing HTTPS health check. Only arguments passed in will be updated on the health check. Other attributes will remain unaffected. 
POSITIONAL ARGUMENTS
    

`NAME`
     Name of the HTTPS health check to update. 
FLAGS
    

`--check-interval`=`CHECK_INTERVAL`
     How often to perform a health check for an instance. For example, specifying ``10s`` will run the check every 10 seconds. See $ [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes) for information on duration formats. 
`--description`=`DESCRIPTION`
     A textual description for the HTTPS health check. Pass in an empty string to unset. 
`--enable-logging`
     Enable logging of health check probe results to Stackdriver. Logging is disabled by default. 

Use --no-enable-logging to disable logging. 

`--healthy-threshold`=`HEALTHY_THRESHOLD`
     The number of consecutive successful health checks before an unhealthy instance is marked as healthy. 
`--host`=`HOST`
     The value of the host header used in this HTTP health check request. The host header is empty by default. When empty, the health check will set the host header to the IP address of the backend VM or endpoint. You can set the host header to an empty value to return to this default behavior. 
`--proxy-header`=`PROXY_HEADER`
     The type of proxy protocol header to be sent to the backend. `PROXY_HEADER` must be one of: 

`NONE`
     No proxy header is added. 
`PROXY_V1`
     Adds the header "PROXY UNKNOWN\r\n". 
`--request-path`=`REQUEST_PATH`
     The request path that this health check monitors. For example, ``/healthcheck``. 
`--response`=`RESPONSE`
     When empty, status code of the response determines health. When not empty, presence of specified string in first 1024 characters of response body determines health. Only ASCII characters allowed. 
`--source-regions`=`REGION`,…,[…]
     Define the list of Google Cloud regions from which health checks are performed. This option is supported only for global health checks that will be referenced by DNS routing policies. If specified, the --check-interval field should be at least 30 seconds. The --proxy-header and --request fields (for TCP health checks) are not supported with this option. 

If --source-regions is specified for a health check, then that health check cannot be used by a backend service or by a managed instance group (for autohealing). 

`--timeout`=`TIMEOUT`
     If Google Compute Engine doesn't receive a healthy response from the instance by the time specified by the value of this flag, the health check request is considered a failure. For example, specifying ``10s`` will cause the check to wait for 10 seconds before considering the request a failure. See $ [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes) for information on duration formats. 
`--unhealthy-threshold`=`UNHEALTHY_THRESHOLD`
     The number of consecutive health check failures before a healthy instance is marked as unhealthy. 
`--weight-report-mode`=`WEIGHT_REPORT_MODE`
     Defines whether Weighted Load Balancing is enabled. `WEIGHT_REPORT_MODE` must be one of: `ENABLE`, `DISABLE`, `DRY_RUN`. 
At most one of these can be specified: 

`--global`
     If set, the HTTPS health check is global. 
`--region`=`REGION`
     Region of the HTTPS health check to update. If not specified, you might be prompted to select a region (interactive mode only). 

To avoid prompting when this flag is omitted, you can set the ``compute/region`` property: 
    
    
    [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) compute/region REGION

A list of regions can be fetched by running: 
    
    
    [gcloud compute regions list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/regions/list)

To unset the property, run: 
    
    
    [gcloud config unset](https://docs.cloud.google.com/sdk/gcloud/reference/config/unset) compute/region

Alternatively, the region can be stored in the environment variable ``CLOUDSDK_COMPUTE_REGION``. 

These flags configure the port that the health check monitors. If both `--port` and `--port-name` are specified, `--port` takes precedence. 
`--port`=`PORT`
     The TCP port number that this health check monitors. 
`--port-name`=`PORT_NAME`
     The port name that this health check monitors. By default, this is empty. Setting this to an empty string will clear any existing port-name value. 
`--use-serving-port`
     If given, use the "serving port" for health checks: 

  * When health checking network endpoints in a Network Endpoint Group, use the port specified with each endpoint. `--use-serving-port` must be used when using a Network Endpoint Group as a backend as this flag specifies the `portSpecification` option for a Health Check object. 
  * When health checking other backends, use the port or named port of the backend service. 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud compute health-checks update https](https://docs.cloud.google.com/sdk/gcloud/reference/compute/health-checks/update/https)
    
    
    [gcloud beta compute health-checks update https](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/health-checks/update/https)
    
    
    [gcloud preview compute health-checks update https](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/health-checks/update/https)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
