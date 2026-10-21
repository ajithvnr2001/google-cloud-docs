---
url: https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/lite-subscriptions/create/
title: gcloud pubsub lite-subscriptions create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:25:59.007985+00:00
---

# gcloud pubsub lite-subscriptions create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/lite-subscriptions/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud pubsub lite-subscriptions create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud pubsub lite-subscriptions create - create a Pub/Sub Lite subscription 
SYNOPSIS
    

`gcloud pubsub lite-subscriptions create` `SUBSCRIPTION` `--topic`=`TOPIC` [`--delivery-requirement`=`DELIVERY_REQUIREMENT`; default="deliver-immediately"] [`--location`=`LOCATION`] [`--event-time`=`EVENT_TIME` | `--publish-time`=`PUBLISH_TIME` | `--starting-offset`=`STARTING_OFFSET`; default="end"] [`--export-pubsub-topic`=`EXPORT_PUBSUB_TOPIC` : `--export-dead-letter-topic`=`EXPORT_DEAD_LETTER_TOPIC` `--export-desired-state`=`EXPORT_DESIRED_STATE`; default="active"] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Create a Pub/Sub Lite subscription. 
EXAMPLES
     To create a Pub/Sub Lite subscription, run: 
    
    
    gcloud pubsub lite-subscriptions create mysubscription --location=us-central1-a --topic=mytopic

To create a Pub/Sub Lite subscription at the offset of the oldest retained message, run: 
    
    
    gcloud pubsub lite-subscriptions create mysubscription --location=us-central1-a --topic=mytopic --starting-offset=beginning

To create a Pub/Sub Lite subscription that exports messages from a Pub/Sub Lite topic to a Pub/Sub topic, run: 
    
    
    gcloud pubsub lite-subscriptions create mysubscription --location=us-central1-a --topic=mytopic --export-pubsub-topic=pubsubtopic

POSITIONAL ARGUMENTS
    

`SUBSCRIPTION`
     Subscription ID. 
REQUIRED FLAGS
    

`--topic`=`TOPIC`
     Topic ID associated with the subscription. 
OPTIONAL FLAGS
    

`--delivery-requirement`=`DELIVERY_REQUIREMENT`; default="deliver-immediately"
     When this subscription should send messages to subscribers relative to messages persistence in storage. See <https://cloud.google.com/pubsub/lite/docs/subscriptions#creating_lite_subscriptions> for more info. `DELIVERY_REQUIREMENT` must be one of: `deliver-after-stored`, `deliver-immediately`. 
Location resource - Identifies the Cloud zone this command will be executed on. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--location` on the command line with a fully specified name; 
  * provide the argument `--zone` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 


`--location`=`LOCATION`
     ID of the location or fully qualified identifier for the location. 

To set the `location` attribute: 

  * provide the argument `--location` on the command line; 
  * provide the argument `--zone` on the command line. 


At most one of these can be specified: 

`--event-time`=`EVENT_TIME`
     The event time to which you seek a subscription. The subscription seeks to the first message with event time greater than or equal to the specified event time. Messages missing an event time use publish time as a fallback. As event times are user supplied, subsequent messages may have event times less than the specified event time and must be filtered by the client, if necessary. Run $ [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes) for information on time formats. 
`--publish-time`=`PUBLISH_TIME`
     The publish time to which you seek a subscription. Messages with publish time greater than or equal to the specified time are delivered after the seek operation. Run $ [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes) for information on time formats. 
`--starting-offset`=`STARTING_OFFSET`; default="end"
     The offset at which a newly created or seeked subscription starts receiving messages. A subscription can be initialized at the offset of the oldest retained message (`beginning`), or at the current HEAD offset (`end`). `STARTING_OFFSET` must be one of: `beginning`, `end`. 
`--export-pubsub-topic`=`EXPORT_PUBSUB_TOPIC`
     The name of the destination Pub/Sub topic to which messages are exported. Must be the topic's fully specified path if it is not in the same project as the subscription to be created. 
`--export-dead-letter-topic`=`EXPORT_DEAD_LETTER_TOPIC`
     The name of the Pub/Sub Lite topic to write messages that cannot be exported. Must be in the same project and location as the subscription to be created. Note that this is a Lite topic. 
`--export-desired-state`=`EXPORT_DESIRED_STATE`; default="active"
     The desired state of the export. Process messages by setting the value to ACTIVE or pause message processing by setting the value to PAUSED. `EXPORT_DESIRED_STATE` must be one of: `active`, `paused`. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `pubsublite/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/pubsub/lite/docs>
NOTES
     These variants are also available: 
    
    
    [gcloud alpha pubsub lite-subscriptions create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pubsub/lite-subscriptions/create)
    
    
    [gcloud beta pubsub lite-subscriptions create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/pubsub/lite-subscriptions/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
