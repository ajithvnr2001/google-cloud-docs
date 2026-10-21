---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/reservations/update/
title: gcloud alpha compute reservations update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T01:01:08.874002+00:00
---

# gcloud alpha compute reservations update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/reservations/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha compute reservations update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha compute reservations update - update Compute Engine reservations 
SYNOPSIS
    

`gcloud alpha compute reservations update` `RESERVATION` [`--add-share-with`=`PROJECT`,[`PROJECT`,…]] [`--add-share-with-folder`=`FOLDER`,[`FOLDER`,…]] [`--add-share-with-project`=`PROJECT`,[`PROJECT`,…]] [`--early-access-maintenance`=`EARLY_ACCESS_MAINTENANCE`] [`--[no-]enable-emergent-maintenance`] [`--remove-share-with`=`PROJECT`,[`PROJECT`,…]] [`--remove-share-with-folder`=`FOLDER`,[`FOLDER`,…]] [`--remove-share-with-project`=`PROJECT`,[`PROJECT`,…]] [`--[no-]require-specific-reservation`] [`--reservation-sharing-policy`=`RESERVATION_SHARING_POLICY`] [`--scheduling-type`=`SCHEDULING_TYPE`] [`--share-setting`=`SHARE_SETTING`] [`--share-with`=`SHARE_WITH`,[`SHARE_WITH`,…]] [`--vm-count`=`VM_COUNT`] [`--zone`=`ZONE`] [`--delete-after-duration`=`DELETE_AFTER_DURATION` | `--delete-at-time`=`DELETE_AT_TIME` | `--disable-auto-delete`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Update Compute Engine reservations. 
EXAMPLES
     To add `project-1,project-2,project-3` to the list of projects that are shared with a Compute Engine reservation, `my-reservation` in zone: `us-central1-a`, run: 
    
    
    gcloud alpha compute reservations update my-reservation --add-share-with=project-1,project-2,project-3 --zone=us-central1-a

To remove `project-1,project-2,project-3` from the list of projects that are shared with a Compute Engine reservation, `my-reservation` in zone: `us-central1-a`, run: 
    
    
    gcloud alpha compute reservations update my-reservation --remove-share-with=project-1,project-2,project-3 --zone=us-central1-a

To update the entire list of projects that are shared with a Compute Engine reservation, `my-reservation` in zone: `us-central1-a`, run: 
    
    
    gcloud alpha compute reservations update my-reservation --share-with=project-1,project-2,project-3 --zone=us-central1-a

To update the number of reserved VM instances to 500 for a Compute Engine reservation, `my-reservation` in zone: `us-central1-a`, run: 
    
    
    gcloud alpha compute reservations update my-reservation --zone=us-central1-a --vm-count=500

POSITIONAL ARGUMENTS
    

`RESERVATION`
     Name of the reservation to update. 
FLAGS
    

`--add-share-with`=`PROJECT`,[`PROJECT`,…]
     If this reservation is shared (--share-setting is projects), then specify a comma-separated list of projects to share the reservation with. You must list the projects using project IDs or project numbers. 
`--add-share-with-folder`=`FOLDER`,[`FOLDER`,…]
     Specify a comma-separated list of folders to share the reservation with. You must list the folders using folder IDs. 
`--add-share-with-project`=`PROJECT`,[`PROJECT`,…]
     Specify a comma-separated list of projects to share the reservation with. You must list the projects using project IDs or project numbers. 
`--early-access-maintenance`=`EARLY_ACCESS_MAINTENANCE`
     Enable this feature to receive quarterly updates and new features for your reservation earlier than the standard schedule.. `EARLY_ACCESS_MAINTENANCE` must be one of: 

`NO_EARLY_ACCESS`
     Standard maintenance schedule. The reservation doesn't have early access maintenance. 
`WAVE1`
     Provides the earliest available notification and maintenance. 
`WAVE2`
     Provides notification and maintenance after WAVE1, but before the standard maintenance schedule. 
`--[no-]enable-emergent-maintenance`
     Enables the reservation to receive notifications when urgent maintenance for a GPU VM starts after the VM encounters a host error. Use `--enable-emergent-maintenance` to enable and `--no-enable-emergent-maintenance` to disable. 
`--remove-share-with`=`PROJECT`,[`PROJECT`,…]
     A list of specific projects to remove from the list of projects that this reservation is shared with. List must contain project IDs or project numbers. 
`--remove-share-with-folder`=`FOLDER`,[`FOLDER`,…]
     Specify a comma-separated list of folders to remove from the list of folders that this reservation is shared with. List must contain folder IDs. 
`--remove-share-with-project`=`PROJECT`,[`PROJECT`,…]
     Specify a comma-separated list of projects to remove from the list of projects that this reservation is shared with. List must contain project IDs or project numbers. 
`--[no-]require-specific-reservation`
     Indicates whether the reservation can be consumed by VMs with "any reservation" defined. If enabled, then only VMs that target this reservation by name using `--reservation-affinity=specific` can consume from this reservation. Use `--require-specific-reservation` to enable and `--no-require-specific-reservation` to disable. 
`--reservation-sharing-policy`=`RESERVATION_SHARING_POLICY`
     The reservation sharing policy to use for this reservation. `RESERVATION_SHARING_POLICY` must be one of: 

`ALLOW_ALL`
     The reservation can be shared with Google Cloud services. 
`DISALLOW_ALL`
     The reservation won't be shared with Google Cloud services. If you omit this flag during creation, the default value is DISALLOW_ALL. 
`--scheduling-type`=`SCHEDULING_TYPE`
     How Compute Engine schedules maintenance events for your reserved hosts. `SCHEDULING_TYPE` must be one of: 

`GROUPED`
     In GROUPED mode, maintenance is synchronized across all your VMs. 
`INDEPENDENT`
     In INDEPENDENT mode, your VMs have different, unsynchronized maintenance schedules. 
`--share-setting`=`SHARE_SETTING`
     The projects that can use the reservation. `SHARE_SETTING` must be one of: 

`folders`
     Any project on the specified list of folders can use the reservation. 
`local`
     Only your project can use the reservation. This is the default value. 
`projects`
     Your project and up to 100 other projects within your project's organization can use the reservation. If you specify this value, then you must also include the \--share-with flag in the command. 
`--share-with`=`SHARE_WITH`,[`SHARE_WITH`,…]
     If this reservation is shared (--share-setting=projects), then specify a comma-separated list of projects to share the reservation with. List projects using project IDs, project numbers, or folder IDs. 
`--vm-count`=`VM_COUNT`
     The number of VM instances that are allocated to this reservation. The value of this field must be an int in the range [1, 1000]. 
`--zone`=`ZONE`
     Zone of the reservation to update. If not specified and the ``compute/zone`` property isn't set, you might be prompted to select a zone (interactive mode only). 

To avoid prompting when this flag is omitted, you can set the ``compute/zone`` property: 
    
    
    [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) compute/zone ZONE

A list of zones can be fetched by running: 
    
    
    [gcloud compute zones list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/zones/list)

To unset the property, run: 
    
    
    [gcloud config unset](https://docs.cloud.google.com/sdk/gcloud/reference/config/unset) compute/zone

Alternatively, the zone can be stored in the environment variable ``CLOUDSDK_COMPUTE_ZONE``. 

Manage auto-delete properties for reservations. 

At most one of these can be specified: 

`--delete-after-duration`=`DELETE_AFTER_DURATION`
     Automatically deletes the reservations after a specified number of days, hours, minutes, or seconds from its creation. For example, specify 30m for 30 minutes, or 1d2h3m4s for 1 day, 2 hours, 3 minutes, and 4 seconds. For more information, see $ [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes). 
`--delete-at-time`=`DELETE_AT_TIME`
     Automatically deletes the reservation at a specific time from its creation. The specified time must be an RFC3339 timestamp, which must be formatted as "YYYY-MM-DDTHH:MM:SSZ" where YYYY = year, MM = month, DD = day, HH = hours, MM = minutes, SS = seconds, and Z = time zone in Coordinated Universal Time (UTC). For example, specify 2021-11-20T07:00:00Z. 
`--disable-auto-delete`
     Disables the auto-delete setting for the reservation. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud compute reservations update](https://docs.cloud.google.com/sdk/gcloud/reference/compute/reservations/update)
    
    
    [gcloud beta compute reservations update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/reservations/update)
    
    
    [gcloud preview compute reservations update](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/reservations/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-29 UTC."],[],[]] 
