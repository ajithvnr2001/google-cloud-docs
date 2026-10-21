---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/monitoring/channels/create/
title: gcloud alpha monitoring channels create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:38:51.563653+00:00
---

# gcloud alpha monitoring channels create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/monitoring/channels/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha monitoring channels create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha monitoring channels create - create a new notification channel 
SYNOPSIS
    

`gcloud alpha monitoring channels create` [`--channel-content`=`CHANNEL_CONTENT` | `--channel-content-from-file`=`PATH_TO_FILE`] [`--channel-labels`=[`KEY`=`VALUE`,…] `--description`=`DESCRIPTION` `--display-name`=`DISPLAY_NAME` `--no-enabled` `--type`=`TYPE` `--user-labels`=[`KEY`=`VALUE`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Creates a new notification channel. A channel can be specified as JSON/YAML passed in as a string through the `--channel-content` flag or as a file through the `--channel-content-from-file` flag. A basic channel can also be specified through command line flags. If a channel is specified through `--channel-content` or `--channel-content-from-file`, and additional flags are supplied, the flags will override the given channel's settings. 

For information about the JSON/YAML format of a notification channel: <https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannels>

Additional documentation can for this operation can be found at: <https://cloud.google.com/monitoring/alerts/using-channels-api>

EXAMPLES
     The following commands setup both email and SMS notification channels for the team lead. Note that the display name and description focus on the purpose/semantics of the channel rather than its destination. This is a best-practice that facilitates swapping/updating notification channels in-place (such as when users change teams, projects, roles, companies, etc.) with minimal impact to the alerting policies that reference the existing channels. It is also a best practice to supply at least two channels of different types for a given person. 
    
    
    gcloud alpha monitoring channels create --display-name="Foo Team Lead (Primary)" --description="Primary contact method for the Foo team lead" --type=email --user-labels=team=foo,role=lead,ord=1 --channel-labels=email_address=user@somedomain.tld
    
    
    gcloud alpha monitoring channels create --display-name="Foo Team Lead (Secondary)" --description="Secondary contact method for the Foo team lead" --type=sms --user-labels=team=foo,role=lead,ord=2 --channel-labels=number=123-456-7890

FLAGS
    

At most one of these can be specified: 

`--channel-content`=`CHANNEL_CONTENT`
     The channel-content as a string. In either JSON or YAML format. 
`--channel-content-from-file`=`PATH_TO_FILE`
     The path to a JSON or YAML file containing the channel-content. Use a full or relative path to a local file containing the value of channel_content. 
Notification channel settings 
`--channel-labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

These are configuration fields that define the channel and its behavior.If the channel was given as a JSON/YAML object from a string or file, this flag will replace the labels value in the given channel. 

`--description`=`DESCRIPTION`
     An optional description for the channel. 
`--display-name`=`DISPLAY_NAME`
     The display name for the channel. 
`--enabled`
     Whether notifications are forwarded to the described channel. Enabled by default, use `--no-enabled` to disable. 
`--type`=`TYPE`
     The type of the notification channel. This field matches the value of the NotificationChannelDescriptor type field. 
`--user-labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

If the channel was given as a JSON/YAML object from a string or file, this flag will replace the labels value in the given channel. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud beta monitoring channels create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/monitoring/channels/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
