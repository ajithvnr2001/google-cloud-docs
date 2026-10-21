---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/scc/notifications/create/
title: gcloud beta scc notifications create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:25:35.711734+00:00
---

# gcloud beta scc notifications create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/scc/notifications/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta scc notifications create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta scc notifications create - create a Security Command Center notification config 
SYNOPSIS
    

`gcloud beta scc notifications create` `NOTIFICATION_CONFIG_ID` `--pubsub-topic`=`PUBSUB_TOPIC` [`--[no-]deletion-notifications-enabled`] [`--description`=`DESCRIPTION`] [`--filter`=`FILTER`] [`--location`=`LOCATION`; default="global"] [`--folder`=`FOLDER` | `--organization`=`ORGANIZATION` | `--project`=`PROJECT`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Create a Security Command Center notification config. 

Notification configs that are created with Security Command Center API V2 and later include a `location` attribute. If a location is not specified, the default `global` location is used. For example, the following Notification config name has `location=global` attribute: `organizations/123/locations/global/notificationConfigs/my-config`. 

EXAMPLES
     Create a notification config test-config under organization 123 for findings for pubsub-topic projects/test-project/topics/notification-test with a filter on resource name: 
    
    
    gcloud beta scc notifications create test-config --organization=123 --pubsub-topic=projects/test-project/topics/notification-test --filter="resource_name: \"a\""

Create a notification config `test-config` under folder `456` for findings for pubsub-topic `projects/test-project/topics/notification-test` with a filter on resource name: 
    
    
    gcloud beta scc notifications create test-config --folder=456 --pubsub-topic=projects/test-project/topics/notification-test --filter="resource_name: \"a\""

Create a notification config `test-config` under project `789` for findings for pubsub-topic `projects/test-project/topics/notification-test` with a filter on resource name: 
    
    
    gcloud beta scc notifications create test-config --project=789 --pubsub-topic=projects/test-project/topics/notification-test --filter="resource_name: \"a\""

Create a notification config `test-config` under organization `123` for findings for `pubsub-topic projects/test-project/topics/notification-test` with a filter on resource name and `location=eu`
    
    
    gcloud beta scc notifications create test-config --project=789 --pubsub-topic=projects/test-project/topics/notification-test --filter="resource_name: \"a\"" --location=eu

POSITIONAL ARGUMENTS
    

`NOTIFICATION_CONFIG_ID`
     The ID of the notification config. Formatted as "organizations/123/notificationConfigs/456" or just "456". 
REQUIRED FLAGS
    

`--pubsub-topic`=`PUBSUB_TOPIC`
     The Pub/Sub topic which will receive notifications. Its format is "projects/[project_id]/topics/[topic]". 
OPTIONAL FLAGS
    

`--[no-]deletion-notifications-enabled`
     Indicates whether the notifications will be sent for deleted findings. Use `--deletion-notifications-enabled` to enable and `--no-deletion-notifications-enabled` to disable. 
`--description`=`DESCRIPTION`
     The text that will be used to describe a notification configuration. 
`--filter`=`FILTER`
     Filter to be used for notification config. 
`--location`=`LOCATION`; default="global"
     If data residency is enabled, specify the Security Command Center location in which to create the notification. The resulting `notificationConfig` resource is stored only in this location. Only findings that are issued in this location are sent to Pub/Sub. 

If data residency is not enabled, specifying the `--location` flag creates the notification by using Security Command Center API v2, and the only valid value for the flag is `global`. 

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
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud scc notifications create](https://docs.cloud.google.com/sdk/gcloud/reference/scc/notifications/create)
    
    
    [gcloud alpha scc notifications create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/scc/notifications/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-29 UTC."],[],[]] 
