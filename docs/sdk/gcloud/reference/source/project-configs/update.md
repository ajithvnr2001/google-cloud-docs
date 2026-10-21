---
url: https://docs.cloud.google.com/sdk/gcloud/reference/source/project-configs/update/
title: gcloud source project-configs update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:40:41.361143+00:00
---

# gcloud source project-configs update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/source/project-configs/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud source project-configs update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud source project-configs update - update the Cloud Source Repositories configuration of the current project 
SYNOPSIS
    

`gcloud source project-configs update` (`--disable-pushblock` | `--enable-pushblock` | `--message-format`=`MESSAGE_FORMAT` `--service-account`=`SERVICE_ACCOUNT` `--topic-project`=`TOPIC_PROJECT` `--add-topic`=`ADD_TOPIC` | `--remove-topic`=`REMOVE_TOPIC` | `--update-topic`=`UPDATE_TOPIC`) [`GCLOUD_WIDE_FLAG …`]
EXAMPLES
     To enable PushBlock for all repositories under current project, run: 
    
    
    gcloud source project-configs update --enable-pushblock

To associate a Cloud Pub/Sub topic to receive repository update notifications, run: 
    
    
    gcloud source project-configs update --add-topic=TOPIC_NAME --service-account=SERVICE_ACCOUNT_EMAIL --message-format=json

REQUIRED FLAGS
    

Exactly one of these must be specified: 

`--disable-pushblock`
     Disable PushBlock for all repositories under current project. PushBlock allows repository owners to block git push transactions containing private key data. 
`--enable-pushblock`
     Enable PushBlock for all repositories under current project. PushBlock allows repository owners to block git push transactions containing private key data. 
Or at least one of these can be specified: 

Manage Cloud Pub/Sub topics associated with the Cloud project. 
`--message-format`=`MESSAGE_FORMAT`
     The format of the message to publish to the topic. `MESSAGE_FORMAT` must be one of: `json`, `protobuf`. 
`--service-account`=`SERVICE_ACCOUNT`
     Email address of the service account used for publishing Cloud Pub/Sub messages. This service account needs to be in the same project as the project. When added, the caller needs to have iam.serviceAccounts.actAs permission on this service account. If unspecified, it defaults to the Compute Engine default service account. 
`--topic-project`=`TOPIC_PROJECT`
     Cloud project for the topic. If not set, the currently set project will be used. 
At most one of these can be specified: 

Topic resource - The Cloud Pub/Sub topic to add to the project. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--add-topic` on the command line with a fully specified name; 
  * provide the argument `--topic-project` on the command line; 
  * set the property `core/project`. 


`--add-topic`=`ADD_TOPIC`
     ID of the topic or fully qualified identifier for the topic. 

To set the `topic` attribute: 

  * provide the argument `--add-topic` on the command line. 


Topic resource - The Cloud Pub/Sub topic to remove from the project. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--remove-topic` on the command line with a fully specified name; 
  * provide the argument `--topic-project` on the command line; 
  * set the property `core/project`. 


`--remove-topic`=`REMOVE_TOPIC`
     ID of the topic or fully qualified identifier for the topic. 

To set the `topic` attribute: 

  * provide the argument `--remove-topic` on the command line. 


Topic resource - The Cloud Pub/Sub topic to update in the project. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--update-topic` on the command line with a fully specified name; 
  * provide the argument `--topic-project` on the command line; 
  * set the property `core/project`. 


`--update-topic`=`UPDATE_TOPIC`
     ID of the topic or fully qualified identifier for the topic. 

To set the `topic` attribute: 

  * provide the argument `--update-topic` on the command line. 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha source project-configs update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/source/project-configs/update)
    
    
    [gcloud beta source project-configs update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/source/project-configs/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
