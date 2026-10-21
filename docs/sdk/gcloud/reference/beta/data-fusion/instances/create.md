---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/data-fusion/instances/create/
title: gcloud beta data-fusion instances create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:12:11.188388+00:00
---

# gcloud beta data-fusion instances create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/data-fusion/instances/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta data-fusion instances create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta data-fusion instances create - create and initialize a Cloud Data Fusion instance 
SYNOPSIS
    

`gcloud beta data-fusion instances create` (`INSTANCE` : `--location`=`LOCATION`) [`--async`] [`--edition`=`EDITION`; default="basic"] [`--enable_rbac`] [`--enable_stackdriver_logging`] [`--enable_stackdriver_monitoring`] [`--endpoint-mode`=`ENDPOINT_MODE`] [`--labels`=[`KEY`=`VALUE`,…]] [`--options`=[`KEY`=`VALUE`,…]] [`--patch_revision`=`PATCH_REVISION`] [`--tags`=[`KEY`=`VALUE`,…]] [`--version`=`VERSION`] [`--zone`=`ZONE`] [`--maintenance-window-end`=`MAINTENANCE_WINDOW_END` `--maintenance-window-recurrence`=`MAINTENANCE_WINDOW_RECURRENCE` `--maintenance-window-start`=`MAINTENANCE_WINDOW_START`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` If run asynchronously with `--async`, exits after printing an operation that can be used to poll the status of the creation operation via: 
    
    
    gcloud beta data-fusion instances create operations list

EXAMPLES
     To create instance `my-instance` in project `my-project`, location in `my-location`, and zone in `my-zone` run: 
    
    
    gcloud beta data-fusion instances create my-instance --project=my-project --location=my-location --zone=my-zone

POSITIONAL ARGUMENTS
    

Instance resource - Instance to create. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `instance` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`INSTANCE`
     ID of the instance or fully qualified identifier for the instance. 

To set the `instance` attribute: 

  * provide the argument `instance` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     Compute Engine region in which to create the instance. 

To set the `location` attribute: 

  * provide the argument `instance` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `datafusion/location`. 


FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--edition`=`EDITION`; default="basic"
     Edition of the Data Fusion instance to create. For example: `--edition=enterprise`. `EDITION` must be one of: `basic`, `enterprise`, `developer`. 
`--enable_rbac`
     Enable granular role-based access control for this Data Fusion instance. 
`--enable_stackdriver_logging`
     Enable Stackdriver logging for this Data Fusion instance. 
`--enable_stackdriver_monitoring`
     Enable Stackdriver monitoring for this Data Fusion instance. 
`--endpoint-mode`=`ENDPOINT_MODE`
     Specifies endpoint mode for a given command. Regional endpoints provide enhanced data residency and reliability by ensuring your request is handled entirely within the specified Google Cloud region. This differs from global endpoints, which may process parts of the request outside the target region. Overrides the default `regional/endpoint_mode` property value for this command invocation. `ENDPOINT_MODE` must be one of: 

`global`
     (Default) Use global rather than regional endpoints. 
`regional`
     Only use regional endpoints. An error will be raised if a regional endpoint is not available for a given command. 
`regional-preferred`
     Use regional endpoints when available, otherwise use global endpoints. Recommended for most users. 
`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

`--options`=[`KEY`=`VALUE`,…]
     Options to use for instance creation, specified as KEY1=VALUE1,KEY2=VALUE2. 
`--patch_revision`=`PATCH_REVISION`
     Patch revision version of Cloud Data Fusion to use when creating the instance.For example: `--patch_revision=6.9.2.1`. 
`--tags`=[`KEY`=`VALUE`,…]
     List of tags KEY=VALUE pairs to bind. Each item must be specified in either ID `<tag_Key_id>=<tag_value_id>` or Namespaced format `<tag-key-namespaced-name>=<tag-value-short-name>`. 

Example: `123/environment=production,123/costCenter=marketing`

`--version`=`VERSION`
     The version of Cloud Data Fusion to use when creating the instance. For example: `--version=6.9.2`. 
`--zone`=`ZONE`
     Compute Engine zone in which the instance will be created. Only needed for DEVELOPER edition. For example: `--zone=us-central1-a`. 
Group of arguments for setting the maintenance window value. 
`--maintenance-window-end`=`MAINTENANCE_WINDOW_END`
     The end time of the maintenance window. Only the time of the day is used as a reference for an ending time of the window with a provided recurrence. This will be used in conjunction with start time, and the difference will determine the length of a single maintenance window. This flag must be specified if any of the other arguments in this group are specified. For example: \--maintenance_window_end=2024-01-02T01:00:00Z. See $ [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes) for information on time formats. 
`--maintenance-window-recurrence`=`MAINTENANCE_WINDOW_RECURRENCE`
     An RFC 5545 RRULE, specifying how the maintenance window will recur. Only FREQ=WEEKLY format is supported. This flag must be specified if any of the other arguments in this group are specified. For example: \--maintenance_window_recurrence="FREQ=WEEKLY;BYDAY=FR,SA,SU". 
`--maintenance-window-start`=`MAINTENANCE_WINDOW_START`
     The start time of the maintenance window. Only the time of the day is used as a reference for a starting time of the window with a provided recurrence. This flag must be specified if any of the other arguments in this group are specified. For example: --maintenance_window_start=2024-01-01T01:00:00Z. See $ [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes) for information on time formats. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

REGIONAL ENDPOINTS
     This command supports regional endpoints. To use regional endpoints for this command, use the `--endpoint-mode=regional-preferred` flag. To use regional endpoints by default, run `$ [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) regional/endpoint_mode regional-preferred`. 
NOTES
     This command is currently in beta and might change without notice. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
