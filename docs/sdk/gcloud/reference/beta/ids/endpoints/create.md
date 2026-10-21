---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/ids/endpoints/create/
title: gcloud beta ids endpoints create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T19:21:00.473054+00:00
---

# gcloud beta ids endpoints create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/ids/endpoints/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta ids endpoints create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta ids endpoints create - create a Cloud IDS endpoint 
SYNOPSIS
    

`gcloud beta ids endpoints create` (`ENDPOINT` : `--zone`=`ZONE`) `--network`=`NETWORK` `--severity`=`SEVERITY` [`--async`] [`--description`=`DESCRIPTION`] [`--enable-traffic-logs`] [`--labels`=[`KEY`=`VALUE`,…]] [`--max-wait`=`MAX_WAIT`; default="60m"] [`--threat-exceptions`=[`exc1`,`exc2`,…,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Create an endpoint for the specified VPC network. Successful creation of an endpoint results in an endpoint in READY state. Check the progress of endpoint creation by using `gcloud alpha ids endpoints list`. 

For more examples, refer to the EXAMPLES section below. 

EXAMPLES
     To create an endpoint called `my-endpoint` for VPC network `my-net`, in zone `us-central1-a`, alerting on LOW threats or higher, run: 
    
    
    gcloud beta ids endpoints create my-endpoint --network=my-net --zone=us-central1-a --project=my-project --severity=LOW

To create an endpoint called `my-endpoint` for VPC network `my-net`, in zone `us-central1-a`, alerting on LOW threats or higher, excluding threat IDs 1000 and 2000, run: 
    
    
    gcloud beta ids endpoints create my-endpoint --network=my-net --zone=us-central1-a --project=my-project --severity=LOW --threat-exceptions=1000,2000

POSITIONAL ARGUMENTS
    

Endpoint resource - endpoint. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `endpoint` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`ENDPOINT`
     ID of the endpoint or fully qualified identifier for the endpoint. 

To set the `endpoint` attribute: 

  * provide the argument `endpoint` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--zone`=`ZONE`
     Zone of the endpoint. 

To set the `zone` attribute: 

  * provide the argument `endpoint` on the command line with a fully specified name; 
  * provide the argument `--zone` on the command line. 


REQUIRED FLAGS
    

`--network`=`NETWORK`
     Name of the VPC network to monitor 
`--severity`=`SEVERITY`
     Minimum severity of threats to report on. `SEVERITY` must be one of: `INFORMATIONAL`, `LOW`, `MEDIUM`, `HIGH`, `CRITICAL`. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. The default is `True`. Enabled by default, use `--no-async` to disable. 
`--description`=`DESCRIPTION`
     Description of the endpoint. 
`--enable-traffic-logs`
     Whether to enable traffic logs on the endpoint. Enabling traffic logs can generate a large number of logs which can increase costs in Cloud Logging. 
`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

`--max-wait`=`MAX_WAIT`; default="60m"
     Time to synchronously wait for the operation to complete, after which the operation continues asynchronously. Ignored if --no-async isn't specified. See $ [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes) for information on time formats. 
`--threat-exceptions`=[`exc1`,`exc2`,…,…]
     List of threat IDs to be excepted from alerting. Passing empty list clears the exceptions. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud ids endpoints create](https://docs.cloud.google.com/sdk/gcloud/reference/ids/endpoints/create)
    
    
    [gcloud alpha ids endpoints create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/ids/endpoints/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
