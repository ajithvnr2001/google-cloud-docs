---
url: https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/message-transforms/test/
title: gcloud pubsub message-transforms test \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:26:01.348127+00:00
---

# gcloud pubsub message-transforms test  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/message-transforms/test/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud pubsub message-transforms test Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud pubsub message-transforms test - tests message transforms against a given message 
SYNOPSIS
    

`gcloud pubsub message-transforms test` (`--attribute`=[`ATTRIBUTE`,…] `--message`=`MESSAGE`) (`--message-transforms-file`=`MESSAGE_TRANSFORMS_FILE` | `--subscription`=`SUBSCRIPTION` | [`--topic`=`TOPIC` : `--topic-project`=`TOPIC_PROJECT`]) [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Tests message transforms against a given message. 
REQUIRED FLAGS
    

Message to test the message transforms against. 

At least one of these must be specified: 

`--attribute`=[`ATTRIBUTE`,…]
     Comma-separated list of attributes to attach to the message. Each ATTRIBUTE has the form name="value". You can specify up to 100 attributes. 
`--message`=`MESSAGE`
     Message body to test the message transforms against. 
Exactly one of these must be specified: 

`--message-transforms-file`=`MESSAGE_TRANSFORMS_FILE`
     Path to YAML or JSON file containing message transforms. 
Or at least one of these can be specified: 

Subscription resource - Name of the subscription from which the message transforms are taken to be applied to the message. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--subscription` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 


`--subscription`=`SUBSCRIPTION`
     ID of the subscription or fully qualified identifier for the subscription. 

To set the `subscription` attribute: 

  * provide the argument `--subscription` on the command line. 


Or at least one of these can be specified: 

Topic resource - Name of the topic from which the message transforms are taken to be applied to the message. The arguments in this group can be used to specify the attributes of this resource. 
`--topic`=`TOPIC`
     ID of the topic or fully qualified identifier for the topic. 

To set the `topic` attribute: 

  * provide the argument `--topic` on the command line. 



This flag argument must be specified if any of the other arguments in this group are specified. 

`--topic-project`=`TOPIC_PROJECT`
     Project ID of the Google Cloud project for the topic. 

To set the `project` attribute: 

  * provide the argument `--topic` on the command line with a fully specified name; 
  * provide the argument `--topic-project` on the command line; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha pubsub message-transforms test](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pubsub/message-transforms/test)
    
    
    [gcloud beta pubsub message-transforms test](https://docs.cloud.google.com/sdk/gcloud/reference/beta/pubsub/message-transforms/test)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
