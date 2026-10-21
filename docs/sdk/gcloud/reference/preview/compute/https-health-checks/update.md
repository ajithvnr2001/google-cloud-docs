---
url: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/https-health-checks/update/
title: gcloud preview compute https-health-checks update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T07:27:17.935071+00:00
---

# gcloud preview compute https-health-checks update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/https-health-checks/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud preview compute https-health-checks update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud preview compute https-health-checks update - update a legacy HTTPS health check 
SYNOPSIS
    

`gcloud preview compute https-health-checks update` `NAME` [`--check-interval`=`CHECK_INTERVAL`] [`--description`=`DESCRIPTION`] [`--healthy-threshold`=`HEALTHY_THRESHOLD`] [`--host`=`HOST`] [`--port`=`PORT`] [`--request-path`=`REQUEST_PATH`] [`--timeout`=`TIMEOUT`] [`--unhealthy-threshold`=`UNHEALTHY_THRESHOLD`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(PREVIEW)` `gcloud preview compute https-health-checks update` is used to update an existing legacy HTTPS health check. Only arguments passed in will be updated on the health check. Other attributes will remain unaffected. 
POSITIONAL ARGUMENTS
    

`NAME`
     Name of the HTTPS health check to update. 
FLAGS
    

`--check-interval`=`CHECK_INTERVAL`
     How often to perform a health check for an instance. For example, specifying ``10s`` will run the check every 10 seconds. See $ [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes) for information on duration formats. 
`--description`=`DESCRIPTION`
     A textual description for the HTTPS health check. Pass in an empty string to unset. 
`--healthy-threshold`=`HEALTHY_THRESHOLD`
     The number of consecutive successful health checks before an unhealthy instance is marked as healthy. 
`--host`=`HOST`
     The value of the host header used in this HTTPS health check request. By default, this is empty and Compute Engine automatically sets the host header in health requests to the same external IP address as the forwarding rule associated with the target pool. Setting this to an empty string will clear any existing host value. 
`--port`=`PORT`
     The TCP port number that this health check monitors. 
`--request-path`=`REQUEST_PATH`
     The request path that this health check monitors. For example, ``/healthcheck``. 
`--timeout`=`TIMEOUT`
     If Compute Engine doesn't receive an HTTPS 200 response from the instance by the time specified by the value of this flag, the health check request is considered a failure. For example, specifying ``10s`` will cause the check to wait for 10 seconds before considering the request a failure. See $ [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes) for information on duration formats. 
`--unhealthy-threshold`=`UNHEALTHY_THRESHOLD`
     The number of consecutive health check failures before a healthy instance is marked as unhealthy. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in DEVELOPER PREVIEW and may change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud compute https-health-checks update](https://docs.cloud.google.com/sdk/gcloud/reference/compute/https-health-checks/update)
    
    
    [gcloud alpha compute https-health-checks update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/https-health-checks/update)
    
    
    [gcloud beta compute https-health-checks update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/https-health-checks/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
