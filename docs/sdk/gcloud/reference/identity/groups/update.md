---
url: https://docs.cloud.google.com/sdk/gcloud/reference/identity/groups/update/
title: gcloud identity groups update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:40:27.411162+00:00
---

# gcloud identity groups update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/identity/groups/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud identity groups update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud identity groups update - update a group 
SYNOPSIS
    

`gcloud identity groups update` `EMAIL` [`--dynamic-user-query`=`DYNAMIC_USER_QUERY`] [`--labels`=`LABELS`] [`--clear-description` | `--description`=`DESCRIPTION`] [`--clear-display-name` | `--display-name`=`DISPLAY_NAME`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Update a group. 
EXAMPLES
     To update a group: 
    
    
    gcloud identity groups update eng-discuss@foo.com --display-name="New Engineer Discuss" --description="Group for engineering discussions"

POSITIONAL ARGUMENTS
    

`EMAIL`
     The email address of the group to be updated. 
FLAGS
    

`--dynamic-user-query`=`DYNAMIC_USER_QUERY`
     Query that determines the memberships of the dynamic group. 

Example of a query: `--dynamic-user-query="user.organizations.exists(org,org.title=='SWE')"`

`--labels`=`LABELS`
     One or more label entries that apply to the group. Currently supported labels contain a key with an empty value. 

Google Groups are the default type of group and have a label with a key of 'cloudidentity.googleapis.com/groups.discussion_forum' and an empty value. 

Existing Google Groups can have an additional label with a key of 'cloudidentity.googleapis.com/groups.security' and an empty value added to them. `This is an immutable change and the security label cannot be removed once added.`

Dynamic groups have a label with a key of 'cloudidentity.googleapis.com/groups.dynamic'. 

Identity-mapped groups for Cloud Search have a label with a key of 'system/groups/external' and an empty value. 

Examples: {"cloudidentity.googleapis.com/groups.discussion_forum": ""} or {"system/groups/external": ""}. 

At most one of these can be specified: 

`--clear-description`
     Clear existing description on group being updated. 
`--description`=`DESCRIPTION`
     Replace existing description on group being updated. 
At most one of these can be specified: 

`--clear-display-name`
     Clear existing display name on group being updated. 
`--display-name`=`DISPLAY_NAME`
     Replace existing display name on group being updated. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `cloudidentity/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/identity/>
NOTES
     These variants are also available: 
    
    
    [gcloud alpha identity groups update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/identity/groups/update)
    
    
    [gcloud beta identity groups update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/identity/groups/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
