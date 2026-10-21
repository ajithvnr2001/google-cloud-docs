---
url: https://docs.cloud.google.com/sdk/gcloud/reference/eventarc/enrollments/create/
title: gcloud eventarc enrollments create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:20:42.347816+00:00
---

# gcloud eventarc enrollments create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/eventarc/enrollments/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud eventarc enrollments create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud eventarc enrollments create - create an Eventarc enrollment 
SYNOPSIS
    

`gcloud eventarc enrollments create` (`ENROLLMENT` : `--location`=`LOCATION`) `--cel-match`=`CEL_MATCH` `--destination-pipeline`=`DESTINATION_PIPELINE` (`--message-bus`=`MESSAGE_BUS` : `--message-bus-project`=`MESSAGE_BUS_PROJECT`) [`--async`] [`--labels`=[`KEY`=`VALUE`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Create an Eventarc enrollment. 
EXAMPLES
     To create a new enrollment `my-enrollment` in location `us-central1` for message-bus `my-message-bus` with cel matching expression `message.type == "google.cloud.pubsub.topic.v1.messagePublished"` and destination pipeline `my-pipeline`, run: 
    
    
    gcloud eventarc enrollments create my-enrollment --location=us-central1 --message-bus=my-message-bus --cel-match="message.type == 'google.cloud.pubsub.topic.v1.messagePublished'" --destination-pipeline=my-pipeline

POSITIONAL ARGUMENTS
    

Enrollment resource - The enrollment to create. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `enrollment` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`ENROLLMENT`
     ID of the enrollment or fully qualified identifier for the enrollment. 

To set the `enrollment` attribute: 

  * provide the argument `enrollment` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location for the Eventarc enrollment, which should be one of the supported regions. Alternatively, set the [eventarc/location] property. 

To set the `location` attribute: 

  * provide the argument `enrollment` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `eventarc/location`. 


REQUIRED FLAGS
    

`--cel-match`=`CEL_MATCH`
     The cel match expression for the enrollment. 
`--destination-pipeline`=`DESTINATION_PIPELINE`
     ID of the destination pipeline or fully qualified identifier for the destination pipeline. 

To set the `pipeline` attribute: 

  * provide the argument `--destination-pipeline` on the command line. 


Message bus resource - The message bus to which the enrollment attaches. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `location` attribute: 

  * provide the argument `--message-bus` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `eventarc/location`. 



This must be specified. 

`--message-bus`=`MESSAGE_BUS`
     ID of the message bus or fully qualified identifier for the message bus. 

To set the `message-bus` attribute: 

  * provide the argument `--message-bus` on the command line. 



This flag argument must be specified if any of the other arguments in this group are specified. 

`--message-bus-project`=`MESSAGE_BUS_PROJECT`
     Project ID of the Google Cloud project for the message bus. 

To set the `project` attribute: 

  * provide the argument `--message-bus` on the command line with a fully specified name; 
  * provide the argument `--message-bus-project` on the command line; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 


OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This variant is also available: 
    
    
    [gcloud beta eventarc enrollments create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/eventarc/enrollments/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
