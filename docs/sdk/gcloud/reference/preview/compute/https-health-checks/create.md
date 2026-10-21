---
url: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/https-health-checks/create/
title: gcloud preview compute https-health-checks create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:20:43.721826+00:00
---

# gcloud preview compute https-health-checks create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/https-health-checks/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud preview compute https-health-checks create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud preview compute https-health-checks create - create a legacy HTTPS health check 
SYNOPSIS
    

`gcloud preview compute https-health-checks create` `NAME` [`--check-interval`=`CHECK_INTERVAL`; default="5s"] [`--description`=`DESCRIPTION`] [`--healthy-threshold`=`HEALTHY_THRESHOLD`; default=2] [`--host`=`HOST`] [`--port`=`PORT`; default=443] [`--request-path`=`REQUEST_PATH`; default="/"] [`--timeout`=`TIMEOUT`; default="5s"] [`--unhealthy-threshold`=`UNHEALTHY_THRESHOLD`; default=2] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(PREVIEW)` Though you can use legacy HTTPS health checks in certain Google Cloud Platform load balancing configurations and for managed instance group autohealing, you should consider a non-legacy HTTPS health check created with `health-checks create https` instead. 

For more information about the differences between legacy and non-legacy health checks see: <https://cloud.google.com/load-balancing/docs/health-check-concepts#category_and_protocol>

For information about what type of health check to use for a particular load balancer, see: <https://cloud.google.com/load-balancing/docs/health-check-concepts#lb_guide>

POSITIONAL ARGUMENTS
    

`NAME`
     Name of the HTTPS health check to create. 
FLAGS
    

`--check-interval`=`CHECK_INTERVAL`; default="5s"
     How often to perform a health check for an instance. For example, specifying ``10s`` will run the check every 10 seconds. The default value is ``5s``. See $ [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes) for information on duration formats. 
`--description`=`DESCRIPTION`
     An optional, textual description for the HTTPS health check. 
`--healthy-threshold`=`HEALTHY_THRESHOLD`; default=2
     The number of consecutive successful health checks before an unhealthy instance is marked as healthy. The default is 2. 
`--host`=`HOST`
     The value of the host header used in this HTTPS health check request. By default, this is empty and Compute Engine automatically sets the host header in health requests to the same external IP address as the forwarding rule associated with the target pool. 
`--port`=`PORT`; default=443
     The TCP port number that this health check monitors. The default value is 443. 
`--request-path`=`REQUEST_PATH`; default="/"
     The request path that this health check monitors. For example, ``/healthcheck``. The default value is ``/´´. 
`--timeout`=`TIMEOUT`; default="5s"
     If Compute Engine doesn't receive an HTTPS 200 response from the instance by the time specified by the value of this flag, the health check request is considered a failure. For example, specifying ``10s`` will cause the check to wait for 10 seconds before considering the request a failure. The default value is ``5s``. See $ [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes) for information on duration formats. 
`--unhealthy-threshold`=`UNHEALTHY_THRESHOLD`; default=2
     The number of consecutive health check failures before a healthy instance is marked as unhealthy. The default is 2. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in DEVELOPER PREVIEW and may change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud compute https-health-checks create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/https-health-checks/create)
    
    
    [gcloud alpha compute https-health-checks create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/https-health-checks/create)
    
    
    [gcloud beta compute https-health-checks create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/https-health-checks/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
