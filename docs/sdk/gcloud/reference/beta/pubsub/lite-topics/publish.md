---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/pubsub/lite-topics/publish/
title: gcloud beta pubsub lite-topics publish \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:14:12.526825+00:00
---

# gcloud beta pubsub lite-topics publish  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/pubsub/lite-topics/publish/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta pubsub lite-topics publish Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta pubsub lite-topics publish - publish Pub/Sub Lite messages 
SYNOPSIS
    

`gcloud beta pubsub lite-topics publish` (`TOPIC` : `--location`=`LOCATION`) [`--attributes`=[`KEY`=`VALUE`,…]] [`--event-time`=`DATETIME`] [`--message`=`MESSAGE`] [`--ordering-key`=`ORDERING_KEY`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Publishes a message to the specified Pub/Sub Lite topic. This command requires Python 3.6 or greater, and requires the grpcio Python package to be installed. 

For MacOS, Linux, and Cloud Shell users, to install the gRPC client libraries, run: 
    
    
    sudo pip3 install grpcio
    export CLOUDSDK_PYTHON_SITEPACKAGES=1

EXAMPLES
     To publish a message to a Pub/Sub Lite topic, run: 
    
    
    gcloud beta pubsub lite-topics publish mytopic --location=us-central1-a --message="Hello World!"

To publish a message to a Pub/Sub Lite topic with an ordering key and attributes, run: 
    
    
    gcloud beta pubsub lite-topics publish mytopic --location=us-central1-a --message="Hello World!" --ordering-key="key" --attributes=KEY1=VAL1,KEY2=VAL2

To publish a message to a Pub/Sub Lite topic with an event time, run: 
    
    
    gcloud beta pubsub lite-topics publish mytopic --location=us-central1-a --message="Hello World!" --event-time="2021-01-01T12:00:00Z"

POSITIONAL ARGUMENTS
    

Topic resource - The pubsub lite topic to publish to. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `topic` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`TOPIC`
     ID of the topic or fully qualified identifier for the topic. 

To set the `topic` attribute: 

  * provide the argument `topic` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     ID of the location of the Pub/Sub Lite resource. To set the `location` attribute: 

  * provide the argument `topic` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


FLAGS
    

`--attributes`=[`KEY`=`VALUE`,…]
     Comma-separated list of attributes. Each ATTRIBUTE has the form name="value". You can specify up to 100 attributes. 
`--event-time`=`DATETIME`
     A user-specified event time. Run `[gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes)` for information on time formats. 
`--message`=`MESSAGE`
     The body of the message to publish to the given topic name. 
`--ordering-key`=`ORDERING_KEY`
     A string key, used for ordering delivery to subscribers. All messages with the same ordering key will be assigned to the same partition for ordered delivery. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud pubsub lite-topics publish](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/lite-topics/publish)
    
    
    [gcloud alpha pubsub lite-topics publish](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pubsub/lite-topics/publish)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
