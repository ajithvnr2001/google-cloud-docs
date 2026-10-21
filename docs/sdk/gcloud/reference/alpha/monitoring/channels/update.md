---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/monitoring/channels/update/
title: gcloud alpha monitoring channels update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:49:12.794392+00:00
---

# gcloud alpha monitoring channels update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/monitoring/channels/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha monitoring channels update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha monitoring channels update - update a notification channel 
SYNOPSIS
    

`gcloud alpha monitoring channels update` `CHANNEL` [`--channel-content`=`CHANNEL_CONTENT` | `--channel-content-from-file`=`PATH_TO_FILE`] [`--fields`=[`field`,…] | `--description`=`DESCRIPTION` `--display-name`=`DISPLAY_NAME` `--[no-]enabled` `--type`=`TYPE` `--update-channel-labels`=[`KEY`=`VALUE`,…] `--clear-channel-labels` | `--remove-channel-labels`=[`KEY`,…] `--update-user-labels`=[`KEY`=`VALUE`,…] `--clear-user-labels` | `--remove-user-labels`=[`KEY`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Updates a notification channel. 

If `--channel-content` or `--channel-content-from-file` are specified: 

  * \--fields can be specified; only the specified fields will be updated. 
  * Alternatively, the channel will be replaced with the provided channel. The channel can be modified further using the flags from the notification channel settings group below. 



Otherwise, the channel will be updated with the values specified in the flags from the notification channel settings group. 

For information about the JSON/YAML format of a notification channel: <https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannels>

`Note:` When specifying the Channel as a YAML/JSON, the use of `channelLabels` as an alternative name for `labels` is supported. 

EXAMPLES
     The following command updates an existing email notification channel to point from its original email address to "newaddress@newdomain.tld": 
    
    
    gcloud alpha monitoring channels update "projects/12345/notificationChannels/67890" --update-channel-labels=email_address=newaddress@newdomain.tld

POSITIONAL ARGUMENTS
    

Notification Channel resource - Name of the Notification Channel to update This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `channel` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`CHANNEL`
     ID of the Notification Channel or fully qualified identifier for the Notification Channel. 

To set the `notification_channels` attribute: 

  * provide the argument `channel` on the command line. 


FLAGS
    

At most one of these can be specified: 

`--channel-content`=`CHANNEL_CONTENT`
     The channel-content as a string. In either JSON or YAML format. 
`--channel-content-from-file`=`PATH_TO_FILE`
     The path to a JSON or YAML file containing the channel-content. Use a full or relative path to a local file containing the value of channel_content. 
At most one of these can be specified: 

`--fields`=[`field`,…]
     The list of fields to update. Must specify `--channel-content` or `--channel-content-from-file` if using this flag. 
Or at least one of these can be specified: 

Notification channel settings 
`--description`=`DESCRIPTION`
     An optional description for the channel. 
`--display-name`=`DISPLAY_NAME`
     The display name for the channel. 
`--[no-]enabled`
     Whether notifications are forwarded to the described channel. Use `--enabled` to enable and `--no-enabled` to disable. 
`--type`=`TYPE`
     The type of the notification channel. This field matches the value of the NotificationChannelDescriptor type field. 
Configuration Fields: Key-Value pairs that define the channel and its behavior. 
`--update-channel-labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to update. If a label exists, its value is modified. Otherwise, a new label is created. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

At most one of these can be specified: 

`--clear-channel-labels`
     Remove all labels. If `--update-channel-labels` is also specified then `--clear-channel-labels` is applied first. 

For example, to remove all labels: 
    
    
    gcloud alpha monitoring channels update --clear-channel-labels

To remove all existing labels and create two new labels, ``foo`` and ``baz``: 
    
    
    gcloud alpha monitoring channels update --clear-channel-labels --update-channel-labels foo=bar,baz=qux

`--remove-channel-labels`=[`KEY`,…]
     List of label keys to remove. If a label does not exist it is silently ignored. If `--update-channel-labels` is also specified then `--update-channel-labels` is applied first. 
User Labels 
`--update-user-labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to update. If a label exists, its value is modified. Otherwise, a new label is created. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

At most one of these can be specified: 

`--clear-user-labels`
     Remove all labels. If `--update-user-labels` is also specified then `--clear-user-labels` is applied first. 

For example, to remove all labels: 
    
    
    gcloud alpha monitoring channels update --clear-user-labels

To remove all existing labels and create two new labels, ``foo`` and ``baz``: 
    
    
    gcloud alpha monitoring channels update --clear-user-labels --update-user-labels foo=bar,baz=qux

`--remove-user-labels`=[`KEY`,…]
     List of label keys to remove. If a label does not exist it is silently ignored. If `--update-user-labels` is also specified then `--update-user-labels` is applied first. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud beta monitoring channels update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/monitoring/channels/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
