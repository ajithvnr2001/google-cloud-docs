---
url: https://docs.cloud.google.com/sdk/gcloud/reference/eventarc/message-buses/publish/
title: gcloud eventarc message-buses publish \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:20:45.009707+00:00
---

# gcloud eventarc message-buses publish  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/eventarc/message-buses/publish/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud eventarc message-buses publish Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud eventarc message-buses publish - publish to an Eventarc message bus 
SYNOPSIS
    

`gcloud eventarc message-buses publish` (`MESSAGE_BUS` : `--location`=`LOCATION`) (`--avro-message`=`AVRO_MESSAGE` | `--json-message`=`JSON_MESSAGE` | [`--event-data`=`EVENT_DATA` `--event-id`=`EVENT_ID` `--event-source`=`EVENT_SOURCE` `--event-type`=`EVENT_TYPE` : `--event-attributes`=[`ATTRIBUTE`=`VALUE`,…]]) [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Publish to an Eventarc message bus. 
EXAMPLES
     To publish an event to the message bus `my-message-bus` with event id `1234`, event type `event-provider.event.v1.eventType`, event source `//event-provider/event/source`, event data `{ "key": "value" }` and event attributes of `attribute1=value`, run: 
    
    
    gcloud eventarc message-buses publish my-message-bus --location=us-central1 --event-id=1234 --event-type=event-provider.event.v1.eventType --event-source="//event-provider/event/source" --event-data='{"key": "value"}' --event-attributes=attribute1=value

To publish an event to the message bus `my-message-bus` with a json message, run: 
    
    
    gcloud eventarc message-buses publish my-message-bus --location=us-central1 --json-message='{"id": 1234, "type":
     "event-provider.event.v1.eventType", "source":
     "//event-provider/event/source", "specversion": "1.0", "data":
     {"key": "value"}}'

POSITIONAL ARGUMENTS
    

Message bus resource - Message bus to publish to. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `message_bus` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`MESSAGE_BUS`
     ID of the message bus or fully qualified identifier for the message bus. 

To set the `message-bus` attribute: 

  * provide the argument `message_bus` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location for the Eventarc message bus, which should be one of the supported regions. Alternatively, set the [eventarc/location] property. 

To set the `location` attribute: 

  * provide the argument `message_bus` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `eventarc/location`. 


REQUIRED FLAGS
    

Exactly one of these must be specified: 

`--avro-message`=`AVRO_MESSAGE`
     An Avro message to publish to the message bus. 
`--json-message`=`JSON_MESSAGE`
     A JSON message to publish to the message bus. 
Or at least one of these can be specified: 

`--event-data`=`EVENT_DATA`
     An event data. The event data of a published event. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--event-id`=`EVENT_ID`
     An event id. The id of a published event. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--event-source`=`EVENT_SOURCE`
     An event source. The event source of a published event. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--event-type`=`EVENT_TYPE`
     An event type. The event type of a published event. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--event-attributes`=[`ATTRIBUTE`=`VALUE`,…]
     Event attributes. The event attributes of a published event.This flag can be repeated to add more attributes. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This variant is also available: 
    
    
    [gcloud beta eventarc message-buses publish](https://docs.cloud.google.com/sdk/gcloud/reference/beta/eventarc/message-buses/publish)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
