---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/scc/assets/group/
title: gcloud beta scc assets group \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:25:29.790453+00:00
---

# gcloud beta scc assets group  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/scc/assets/group/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta scc assets group Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta scc assets group - filter an organization's assets and groups them by their specified properties 
SYNOPSIS
    

`gcloud beta scc assets group` [`PARENT`] [`--compare-duration`=`COMPARE_DURATION`] [`--filter`=`FILTER`] [`--group-by`=`GROUP_BY`] [`--page-size`=`PAGE_SIZE`] [`--page-token`=`PAGE_TOKEN`] [`--read-time`=`READ_TIME`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` `(DEPRECATED)` Security Command Center Asset APIs are deprecated and will be removed on or after June 26, 2024. Use Cloud Asset Inventory instead [(gcloud asset)](https://cloud.google.com/sdk/gcloud/reference/asset). For more information, [see the deprecation notice at Assets Page](https://cloud.google.com/security-command-center/docs/how-to-use-security-command-center#assets_page). Filter an organization's assets and groups them by their specified properties. 
EXAMPLES
     Group assets under organization 123456 by their type (e.g. project, disk, compute instance, service etc): 
    
    
    gcloud beta scc assets group 123456 --group-by="security_center_properties.resource_type"

Group assets under project example-project by their type (e.g. project, disk, compute instance, service etc): 
    
    
    gcloud beta scc assets group projects/example-project --group-by="security_center_properties.resource_type"

Group assets under folder 456 by their type (e.g. project, disk, compute instance, service etc): 
    
    
    gcloud beta scc assets group folders/456 --group-by="security_center_properties.resource_type"

Group compute instances (assets) under organization 123456 by their respective projects: 
    
    
    gcloud beta scc assets group 123456 --filter="security_center_properties.resource_type=\"google.compute.Instance\"" --group-by="security_center_properties.resource_project"

Group assets that were updated on or after 2019-01-01T01:00:00 GMT by their types. 
    
    
    gcloud beta scc assets group 123456 --filter="update_time >= 1546304400000" --group-by="security_center_properties.resource_type"

Group assets into following 3 state_changes (ADDED/DELETED/ACTIVE) based on the activity during past 24 hours: 
    
    
    gcloud beta scc assets group 123456 --compare-duration=86400s --group-by="state_change"

POSITIONAL ARGUMENTS
    

Parent resource - parent organization, folder, or project in the Google Cloud resource hierarchy to be used for the `[gcloud scc](https://docs.cloud.google.com/sdk/gcloud/reference/scc)` command. Specify the argument as either [RESOURCE_TYPE/RESOURCE_ID] or [RESOURCE_ID], as shown in the preceding examples. This represents a Cloud resource. 
[`PARENT`]
     ID of the parent or fully qualified identifier for the parent. 

To set the `parent` attribute: 

  * provide the argument `parent` on the command line; 
  * Set the parent property in configuration using `gcloud config set scc/parent` if it is not specified in command line. 


FLAGS
    

`--compare-duration`=`COMPARE_DURATION`
     The result's "state_change" attribute is updated to indicate whether the asset was added, removed, or remained present during the compare_duration period of time that precedes the read_time. See `$ [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes)` for information on supported duration formats. 
`--filter`=`FILTER`
     Expression is a list of one or more restrictions combined via logical operators 'AND' and 'OR'. Parentheses are not supported, and 'OR' has higher precedence than 'AND'. For example, 'update_time > 100 AND security_center_properties.resource_type=\"google.cloud.resourcemanager.Organization\"' is a valid filter string. 
`--group-by`=`GROUP_BY`
     Expression that defines what asset fields to use for grouping (including 'state'). String value should follow SQL syntax: comma separated list of fields. For example: "parent,resource_name". The following fields are supported: 

  * security_center_properties.resource_project 
  * security_center_properties.resource_type 
  * security_center_properties.resource_parent 
  * state_change 


`--page-size`=`PAGE_SIZE`
     The maximum number of results to return in a single response. Default is 10, minimum is 1, maximum is 1000. 
`--page-token`=`PAGE_TOKEN`
     Value returned by the last 'GroupAssetsResponse'; indicates that this is a continuation of a prior 'GroupAssets' call, and that the system should return the next page of data. 
`--read-time`=`READ_TIME`
     Time used as a reference point when filtering. Absence of this field will default to the API's version of NOW. See `$ [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes)` for information on supported time formats. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `securitycenter/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/security-command-center>
NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud scc assets group](https://docs.cloud.google.com/sdk/gcloud/reference/scc/assets/group)
    
    
    [gcloud alpha scc assets group](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/scc/assets/group)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
