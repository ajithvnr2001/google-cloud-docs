---
url: https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/lite-subscriptions/seek/
title: gcloud pubsub lite-subscriptions seek \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:25:59.965597+00:00
---

# gcloud pubsub lite-subscriptions seek  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/lite-subscriptions/seek/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud pubsub lite-subscriptions seek Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud pubsub lite-subscriptions seek - seek a Pub/Sub Lite subscription 
SYNOPSIS
    

`gcloud pubsub lite-subscriptions seek` (`SUBSCRIPTION` : `--location`=`LOCATION`) (`--event-time`=`EVENT_TIME` | `--publish-time`=`PUBLISH_TIME` | `--starting-offset`=`STARTING_OFFSET`) [`--async`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Initiate an out-of-band seek operation for a Pub/Sub Lite subscription to a specified target, which may be timestamps or named locations within the message backlog. 

The seek operation will complete once subscriber clients react to the seek for all partitions of the topic. Note that the seek operation will not complete until subscribers are online. It may take some time (usually within 30 seconds) for the seek to propagate if subscribers are online. Use the --async flag if it's not necessary to wait for completion. 

EXAMPLES
     To seek a Pub/Sub Lite subscription to the beginning of the message backlog, run: 
    
    
    gcloud pubsub lite-subscriptions seek mysubscription --location=us-central1-a --starting-offset=beginning

To seek a Pub/Sub Lite subscription to a publish time without waiting for the operation to complete, run: 
    
    
    gcloud pubsub lite-subscriptions seek mysubscription --location=us-central1-a --publish-time="2021-01-01T12:00:00Z" --async

POSITIONAL ARGUMENTS
    

Subscription resource - Subscription to seek. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

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


REQUIRED FLAGS
    

Exactly one of these must be specified: 

`--event-time`=`EVENT_TIME`
     The event time to which you seek a subscription. The subscription seeks to the first message with event time greater than or equal to the specified event time. Messages missing an event time use publish time as a fallback. As event times are user supplied, subsequent messages may have event times less than the specified event time and must be filtered by the client, if necessary. Run $ [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes) for information on time formats. 
`--publish-time`=`PUBLISH_TIME`
     The publish time to which you seek a subscription. Messages with publish time greater than or equal to the specified time are delivered after the seek operation. Run $ [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes) for information on time formats. 
`--starting-offset`=`STARTING_OFFSET`
     The offset at which a newly created or seeked subscription starts receiving messages. A subscription can be initialized at the offset of the oldest retained message (`beginning`), or at the current HEAD offset (`end`). `STARTING_OFFSET` must be one of: `beginning`, `end`. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `pubsublite/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/pubsub/lite/docs>
NOTES
     These variants are also available: 
    
    
    [gcloud alpha pubsub lite-subscriptions seek](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pubsub/lite-subscriptions/seek)
    
    
    [gcloud beta pubsub lite-subscriptions seek](https://docs.cloud.google.com/sdk/gcloud/reference/beta/pubsub/lite-subscriptions/seek)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
