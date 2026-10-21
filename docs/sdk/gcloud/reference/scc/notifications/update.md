---
url: https://docs.cloud.google.com/sdk/gcloud/reference/scc/notifications/update/
title: gcloud scc notifications update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:31:06.169703+00:00
---

# gcloud scc notifications update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/scc/notifications/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud scc notifications update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud scc notifications update - update a Security Command Center notification config 
SYNOPSIS
    

`gcloud scc notifications update` `NOTIFICATION_CONFIG_ID` [`--[no-]deletion-notifications-enabled`] [`--description`=`DESCRIPTION`] [`--filter`=`FILTER`] [`--location`=`LOCATION`; default="global"] [`--pubsub-topic`=`PUBSUB_TOPIC`] [`--folder`=`FOLDER` | `--organization`=`ORGANIZATION` | `--project`=`PROJECT`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Update a Security Command Center notification config. 

Notification configs that are created with Security Command Center API V2 and later include a `location` attribute. If the `location` attribute is included in the resource name of a Notification configs, you must specify it when referencing the Notification config. For example, the following Notification configs name has `location=eu`: `organizations/123/locations/eu/notificationConfigs/test-config`. 

EXAMPLES
     Update all mutable fields under an organization parent `test-config` (description + pubsub topic + filter): 
    
    
    gcloud scc notifications update scc notifications update test-config --organization=123 --description="New description" --pubsub-topic="projects/22222/topics/newtopic"

Update all mutable fields under a folder parent `test-config` (description + pubsub topic + filter): 
    
    
    gcloud scc notifications update scc notifications update test-config --folder=456 --description="New description" --pubsub-topic="projects/22222/topics/newtopic"

Update all mutable fields under a project parent `test-config` (description + pubsub topic + filter): 
    
    
    gcloud scc notifications update scc notifications update test-config --project=789 --description="New description" --pubsub-topic="projects/22222/topics/newtopic"

Update test-config's description 
    
    
    gcloud scc notifications update test-config --organization=123 --description="New description"

Update test-config's pubsub-topic 
    
    
    gcloud scc notifications update test-config --organization=123 --pubsub-topic="projects/22222/topics/newtopic"

Update test-config's filter 
    
    
    gcloud scc notifications update test-config --organization=123 --filter='state = \"ACTIVE\"'

Update all mutable fields for `test-config` with `location=global` under an organization parent (description + pubsub topic + filter): 
    
    
    gcloud scc notifications update scc notifications update test-config --organization=123 --description="New description" --pubsub-topic="projects/22222/topics/newtopic" --location=global

POSITIONAL ARGUMENTS
    

`NOTIFICATION_CONFIG_ID`
     The ID of the notification config. Formatted as "organizations/123/notificationConfigs/456" or just "456". 
FLAGS
    

`--[no-]deletion-notifications-enabled`
     Indicates whether the notifications will be sent for deleted findings. Use `--deletion-notifications-enabled` to enable and `--no-deletion-notifications-enabled` to disable. 
`--description`=`DESCRIPTION`
     The text that will be used to describe a notification configuration. 
`--filter`=`FILTER`
     The filter string which will applied to events of findings of a notification configuration. 
`--location`=`LOCATION`; default="global"
     Required if either data residency is enabled or the `notificationConfig` was created by using the API v2. 

If data residency is enabled, specify the Security Command Center location in which the notification is stored. 

If data residency is not enabled, include `/locations/```LOCATION´´ in the full name or specify the `--location` flag only if the `notificationConfig` resource was created by using the Security Command Center API v2, in which case, the only valid location is `global`. 

`--pubsub-topic`=`PUBSUB_TOPIC`
     The Pub/Sub topic which will receive notifications. Its format is "projects/[project_id]/topics/[topic]". 
At most one of these can be specified: 

`--folder`=`FOLDER`
     Folder where the notification config resides. Formatted as ``folders/456`` or just ``456``. 
`--organization`=`ORGANIZATION`
     Organization where the notification config resides. Formatted as ``organizations/123`` or just ``123``. 
`--project`=`PROJECT`
     Project (ID or number) where the notification config resides. Formatted as ``projects/789`` or just ``789``. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the Security Command Center API. For more information, see [Security Command Center API.](https://cloud.google.com/security-command-center/docs/reference/rest)
NOTES
     These variants are also available: 
    
    
    [gcloud alpha scc notifications update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/scc/notifications/update)
    
    
    [gcloud beta scc notifications update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/scc/notifications/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-29 UTC."],[],[]] 
