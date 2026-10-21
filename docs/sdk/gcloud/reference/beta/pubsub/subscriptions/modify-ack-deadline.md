---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/pubsub/subscriptions/modify-ack-deadline/
title: gcloud beta pubsub subscriptions modify-ack-deadline \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:14:15.222430+00:00
---

# gcloud beta pubsub subscriptions modify-ack-deadline  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/pubsub/subscriptions/modify-ack-deadline/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta pubsub subscriptions modify-ack-deadline Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta pubsub subscriptions modify-ack-deadline - modifies the ACK deadline for a specific Cloud Pub/Sub message 
SYNOPSIS
    

`gcloud beta pubsub subscriptions modify-ack-deadline` `SUBSCRIPTION` ([`ACK_ID` …] `--ack-ids`=[`ACK_ID`,…]) `--ack-deadline`=`ACK_DEADLINE` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` `(DEPRECATED)` Modifies the ACK deadline for a specific Cloud Pub/Sub message. 

This command has been renamed. Please use `modify-message-ack-deadline` instead. 

This method is useful to indicate that more time is needed to process a message by the subscriber, or to make the message available for redelivery if the processing was interrupted. 

POSITIONAL ARGUMENTS
    

Subscription resource - Name of the subscription messages belong to. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `subscription` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`SUBSCRIPTION`
     ID of the subscription or fully qualified identifier for the subscription. 

To set the `subscription` attribute: 

  * provide the argument `subscription` on the command line. 


Exactly one of these must be specified: 

[`ACK_ID` …]
     (DEPRECATED) One or more ACK_IDs to modify the deadline for. An ACK_ID is a [string that is returned to subscribers](https://cloud.google.com/pubsub/docs/reference/rpc/google.pubsub.v1#google.pubsub.v1.ReceivedMessage). along with the message. The ACK_ID is different from the [message ID](https://cloud.google.com/pubsub/docs/reference/rpc/google.pubsub.v1#google.pubsub.v1.PubsubMessage). 

Positional argument `ACK_ID` is deprecated. Please use `--ack-ids` instead. 

`--ack-ids`=[`ACK_ID`,…]
     One or more ACK_IDs to modify the deadline for. An ACK_ID is a [string that is returned to subscribers](https://cloud.google.com/pubsub/docs/reference/rpc/google.pubsub.v1#google.pubsub.v1.ReceivedMessage). along with the message. The ACK_ID is different from the [message ID](https://cloud.google.com/pubsub/docs/reference/rpc/google.pubsub.v1#google.pubsub.v1.PubsubMessage). 
REQUIRED FLAGS
    

`--ack-deadline`=`ACK_DEADLINE`
     The number of seconds the system will wait for a subscriber to acknowledge receiving a message before re-attempting delivery. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. This variant is also available: 
    
    
    [gcloud alpha pubsub subscriptions modify-ack-deadline](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pubsub/subscriptions/modify-ack-deadline)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
