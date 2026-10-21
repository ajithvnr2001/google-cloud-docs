---
url: https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/lite-subscriptions/subscribe/
title: gcloud pubsub lite-subscriptions subscribe \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:43:00.757928+00:00
---

# gcloud pubsub lite-subscriptions subscribe  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/lite-subscriptions/subscribe/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud pubsub lite-subscriptions subscribe Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud pubsub lite-subscriptions subscribe - stream messages from a Pub/Sub Lite subscription 
SYNOPSIS
    

`gcloud pubsub lite-subscriptions subscribe` (`SUBSCRIPTION` : `--location`=`LOCATION`) [`--auto-ack`] [`--num-messages`=`NUM_MESSAGES`; default=1] [`--partitions`=[`INT`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Streams messages from a Pub/Sub Lite subscription. This command requires Python 3.6 or greater, and requires the grpcio Python package to be installed. 

For MacOS, Linux, and Cloud Shell users, to install the gRPC client libraries, run: 
    
    
    sudo pip3 install grpcio
    export CLOUDSDK_PYTHON_SITEPACKAGES=1

EXAMPLES
     To subscribe to a Pub/Sub Lite subscription and automatically acknowledge messages, run: 
    
    
    gcloud pubsub lite-subscriptions subscribe mysubscription --location=us-central1-a --auto-ack

To subscribe to specific partitions in a subscription, run: 
    
    
    gcloud pubsub lite-subscriptions subscribe mysubscription --location=us-central1-a --partitions=0,1,2

POSITIONAL ARGUMENTS
    

Subscription resource - The Pub/Sub Lite subscription to receive messages from. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `subscription` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`SUBSCRIPTION`
     ID of the subscription or fully qualified identifier for the subscription. 

To set the `subscription` attribute: 

  * provide the argument `subscription` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     ID of the location of the Pub/Sub Lite resource. To set the `location` attribute: 

  * provide the argument `subscription` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


FLAGS
    

`--auto-ack`
     Automatically ACK every message received on this subscription. 
`--num-messages`=`NUM_MESSAGES`; default=1
     The number of messages to stream before exiting. This value must be less than or equal to 1000. 
`--partitions`=[`INT`,…]
     The partitions this subscriber should connect to to receive messages. If empty, partitions will be automatically assigned. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha pubsub lite-subscriptions subscribe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pubsub/lite-subscriptions/subscribe)
    
    
    [gcloud beta pubsub lite-subscriptions subscribe](https://docs.cloud.google.com/sdk/gcloud/reference/beta/pubsub/lite-subscriptions/subscribe)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
