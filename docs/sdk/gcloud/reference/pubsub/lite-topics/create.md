---
url: https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/lite-topics/create/
title: gcloud pubsub lite-topics create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:26:00.078188+00:00
---

# gcloud pubsub lite-topics create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/lite-topics/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud pubsub lite-topics create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud pubsub lite-topics create - create a Pub/Sub Lite topic 
SYNOPSIS
    

`gcloud pubsub lite-topics create` `TOPIC` `--partitions`=`PARTITIONS` `--per-partition-bytes`=`PER_PARTITION_BYTES` [`--location`=`LOCATION`] [`--message-retention-period`=`MESSAGE_RETENTION_PERIOD`] [`--per-partition-publish-mib`=`PER_PARTITION_PUBLISH_MIB`] [`--per-partition-subscribe-mib`=`PER_PARTITION_SUBSCRIBE_MIB`] [`--throughput-reservation`=`THROUGHPUT_RESERVATION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Create a Pub/Sub Lite topic. 
EXAMPLES
     To create a Pub/Sub lite-topic, run: 
    
    
    gcloud pubsub lite-topics create mytopic --location=us-central1-a --partitions=1 --per-partition-bytes=30GiB --message-retention-period=2w

POSITIONAL ARGUMENTS
    

`TOPIC`
     Topic ID. 
REQUIRED FLAGS
    

`--partitions`=`PARTITIONS`
     Number of partitions in the topic. 
`--per-partition-bytes`=`PER_PARTITION_BYTES`
     Provisioned storage, in bytes, per partition. If the number of bytes stored in any of the topic's partitions exceeds this value, older messages will be dropped to make room for newer ones, regardless of the value of `message-retention-period`. A valid example value of this flag would be `per-partition-bytes=30GiB`. 
OPTIONAL FLAGS
    

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


`--message-retention-period`=`MESSAGE_RETENTION_PERIOD`
     How long a published message is retained. If unset, messages will only be dropped to make space for new ones once the `per-partition-bytes` limit is reached. A valid example value of this flag would be `message-retention-period="2w"`. 
`--per-partition-publish-mib`=`PER_PARTITION_PUBLISH_MIB`
     Topic partition publish throughput capacity in MiB/s. Must be between 4 and 16. 
`--per-partition-subscribe-mib`=`PER_PARTITION_SUBSCRIBE_MIB`
     Topic partition subscribe throughput capacity in MiB/s. Must be between 4 and 32\. 
`--throughput-reservation`=`THROUGHPUT_RESERVATION`
     Reservation ID to use for topic throughput. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `pubsublite/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/pubsub/lite/docs>
NOTES
     These variants are also available: 
    
    
    [gcloud alpha pubsub lite-topics create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pubsub/lite-topics/create)
    
    
    [gcloud beta pubsub lite-topics create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/pubsub/lite-topics/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
