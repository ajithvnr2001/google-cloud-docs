---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/monitoring/channels/delete/
title: gcloud alpha monitoring channels delete \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:49:13.520138+00:00
---

# gcloud alpha monitoring channels delete  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/monitoring/channels/delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha monitoring channels delete Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha monitoring channels delete - delete a notification channel 
SYNOPSIS
    

`gcloud alpha monitoring channels delete` `CHANNEL` [`--force`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Delete a notification channel. 
EXAMPLES
     The following command will delete channel `projects/12345/notificationChannels/67890`, but only if the channel is not actively referenced by existing alerting policies: 
    
    
    gcloud alpha monitoring channels delete "projects/12345/notificationChannels/67890"

The following command will delete channel `projects/12345/notificationChannels/67890`, even if the channel is still actively referenced by alerting policies; if an existing policy references the channel, it will be modified as a side-effect to remove the channel. 
    
    
    gcloud alpha monitoring channels delete "projects/12345/notificationChannels/67890" --force

POSITIONAL ARGUMENTS
    

Notification channel resource - The notification channel to delete. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `channel` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`CHANNEL`
     ID of the notification_channel or fully qualified identifier for the notification_channel. 

To set the `channel` attribute: 

  * provide the argument `channel` on the command line. 


FLAGS
    

`--force`
     If true, the notification channel will be deleted regardless of its use in alerting policies (the policies will be updated to remove the channel). 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `monitoring/v3` API. The full documentation for this API can be found at: <https://cloud.google.com/monitoring/api/>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud beta monitoring channels delete](https://docs.cloud.google.com/sdk/gcloud/reference/beta/monitoring/channels/delete)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
