---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/functions/call/
title: gcloud beta functions call \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T19:19:59.789584+00:00
---

# gcloud beta functions call  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/functions/call/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta functions call Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta functions call - triggers execution of a Google Cloud Function 
SYNOPSIS
    

`gcloud beta functions call` (`NAME` : `--region`=`REGION`) [`--cloud-event`=`CLOUD_EVENT` | `--data`=`DATA`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Triggers execution of a Google Cloud Function. 
EXAMPLES
     To call a function, giving it 'Hello World!' in the message field of its event argument (depending on your environment you might need to escape characters in `--data` flag value differently), run: 
    
    
    gcloud beta functions call helloWorld --data='{"message": "Hello World!"}'

Note that this method has a limited quota which cannot be increased. It is intended for testing and debugging and should not be used in production. 

Calls to HTTP-triggered functions are sent as HTTP POST requests. To use other HTTP methods, use a dedicated HTTP request tool such as cURL or wget. 

POSITIONAL ARGUMENTS
    

Function resource - The Cloud Function name to execute. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `NAME` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`NAME`
     ID of the function or fully qualified identifier for the function. 

To set the `function` attribute: 

  * provide the argument `NAME` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--region`=`REGION`
     The Cloud region for the function. Overrides the default `functions/region` property value for this command invocation. 

To set the `region` attribute: 

  * provide the argument `NAME` on the command line with a fully specified name; 
  * provide the argument `--region` on the command line; 
  * set the property `functions/region`. 


FLAGS
    

At most one of these can be specified: 

`--cloud-event`=`CLOUD_EVENT`
     JSON encoded string with a CloudEvent in structured content mode. 

Mutually exclusive with --data flag. 

Use for Cloud Functions 2nd Gen CloudEvent functions. The CloudEvent object will be sent to your function as a binary content mode message with the top-level 'data' field set as the HTTP body and all other JSON fields sent as HTTP headers. 

`--data`=`DATA`
     JSON string with data that will be passed to the function. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud functions call](https://docs.cloud.google.com/sdk/gcloud/reference/functions/call)
    
    
    [gcloud alpha functions call](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/functions/call)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
