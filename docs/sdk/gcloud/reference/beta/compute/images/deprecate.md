---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/images/deprecate/
title: gcloud beta compute images deprecate \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T09:11:56.766499+00:00
---

# gcloud beta compute images deprecate  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/images/deprecate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta compute images deprecate Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta compute images deprecate - manage deprecation status of Compute Engine images 
SYNOPSIS
    

`gcloud beta compute images deprecate` `IMAGE_NAME` `--state`=`STATE` [`--replacement`=`REPLACEMENT`] [`--delete-in`=`DELETE_IN` | `--delete-on`=`DELETE_ON`] [`--deprecate-in`=`DEPRECATE_IN` | `--deprecate-on`=`DEPRECATE_ON`] [`--obsolete-in`=`OBSOLETE_IN` | `--obsolete-on`=`OBSOLETE_ON`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` `gcloud beta compute images deprecate` is used to deprecate images. 
EXAMPLES
     To deprecate an image called 'IMAGE' immediately, mark it as obsolete in one day, and mark it as deleted in two days, use: 
    
    
    gcloud beta compute images deprecate IMAGE --state=DEPRECATED --obsolete-in=1d --delete-in=2d

To un-deprecate an image called 'IMAGE' and clear times for deprecated, obsoleted, and deleted, use: 
    
    
    gcloud beta compute images deprecate IMAGE --state=ACTIVE

POSITIONAL ARGUMENTS
    

`IMAGE_NAME`
     Name of the disk image to operate on. 
REQUIRED FLAGS
    

`--state`=`STATE`
     The deprecation state to set on the image. `STATE` must be one of: 

`ACTIVE`
     The image is currently supported. 
`DELETED`
     New uses result in an error. Setting this state will not automatically delete the image. You must still make a request to delete the image to remove it from the image list. 
`DEPRECATED`
     Operations which create a new `DEPRECATED` resource return successfully, but with a warning indicating that the image is deprecated and recommending its replacement. 
`OBSOLETE`
     New uses result in an error. 
OPTIONAL FLAGS
    

`--replacement`=`REPLACEMENT`
     Specifies a Compute Engine image as a replacement for the image being phased out. Users of the deprecated image will be advised to switch to this replacement. For example, `--replacement example-image` or `--replacement projects/google/global/images/example-image`. 

This flag value is purely informational and is not validated in any way. 

At most one of these can be specified: 

`--delete-in`=`DELETE_IN`
     Specifies a time duration in which the image should be marked as ``DELETED``. 

Note: This is only informational and the image will not be deleted unless you manually delete it. 

For example, specifying ``30d`` sets the planned ``DELETED`` time to 30 days from the current system time, but does not delete the image. You must manually delete the image in 30 days. See $ [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes) for information on duration formats. 

This flag is mutually exclusive with `--delete-on`. 

`--delete-on`=`DELETE_ON`
     Specifies a date when the image should be marked as ``DELETED``. 

Note: This is only informational and the image will not be deleted unless you manually delete it. 

This flag is mutually exclusive with `--delete-in`. 

The date and time specified must be valid RFC 3339 full-date or date-time. For times in UTC, this looks like ``YYYY-MM-DDTHH:MM:SSZ``. For example: 2020-01-02T00:00:00Z for midnight on January 2, 2020 in UTC. 

At most one of these can be specified: 

`--deprecate-in`=`DEPRECATE_IN`
     Specifies a time duration in which the image should be marked as ``DEPRECATED``. 

Note: This is only informational and the image will not be deprecated unless you manually deprecate it. 

This flag is mutually exclusive with `--deprecate-on`. 

For example, specifying ``30d`` sets the planned ``DEPRECATED`` date to 30 days from the current system time, but does not deprecate the image. You must manually deprecate the image in 30 days. See $ [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes) for information on duration formats. 

`--deprecate-on`=`DEPRECATE_ON`
     Specifies a date when the image should be marked as DEPRECATED. 

Note: This is only informational and the image will not be deprecated unless you manually deprecate it. 

This flag is mutually exclusive with `--deprecate-in`. 

The date and time specified must be valid RFC 3339 full-date or date-time. For times in UTC, this looks like ``YYYY-MM-DDTHH:MM:SSZ``. For example: 2020-01-02T00:00:00Z for midnight on January 2, 2020 in UTC. 

At most one of these can be specified: 

`--obsolete-in`=`OBSOLETE_IN`
     Specifies a time duration in which the image should be marked as ``OBSOLETE``. 

Note: This is only informational and the image will not be obsoleted unless you manually obsolete it. 

This flag is mutually exclusive with `--obsolete-on`. 

For example, specifying ``30d`` sets the planned ``OBSOLETE`` time to 30 days from the current system time, but does not obsolete the image. You must manually obsolete the image in 30 days. See $ [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes) for information on duration formats. 

`--obsolete-on`=`OBSOLETE_ON`
     Specifies a date when the image should be marked as ``OBSOLETE``. 

Note: This is only informational and the image will not be obsoleted unless you manually obsolete it. 

This flag is mutually exclusive with `--obsolete-in`. 

The date and time specified must be valid RFC 3339 full-date or date-time. For times in UTC, this looks like ``YYYY-MM-DDTHH:MM:SSZ``. For example: 2020-01-02T00:00:00Z for midnight on January 2, 2020 in UTC. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud compute images deprecate](https://docs.cloud.google.com/sdk/gcloud/reference/compute/images/deprecate)
    
    
    [gcloud alpha compute images deprecate](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/images/deprecate)
    
    
    [gcloud preview compute images deprecate](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/images/deprecate)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
