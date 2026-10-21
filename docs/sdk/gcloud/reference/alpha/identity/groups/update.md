---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/identity/groups/update/
title: gcloud alpha identity groups update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:26:42.153787+00:00
---

# gcloud alpha identity groups update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/identity/groups/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha identity groups update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha identity groups update - update a group 
SYNOPSIS
    

`gcloud alpha identity groups update` `EMAIL` [`--dynamic-user-query`=`DYNAMIC_USER_QUERY`] [`--clear-posix-groups` | `--remove-posix-groups`=[`POSIX_GROUP`,…]] [`--clear-description` | `--description`=`DESCRIPTION`] [`--clear-display-name` | `--display-name`=`DISPLAY_NAME`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Update a group. 
EXAMPLES
     To update a group: 
    
    
    gcloud alpha identity groups update eng-discuss@foo.com --display-name="New Engineer Discuss" --description="Group for engineering discussions"

To remove POSIX information from a Google Group: 
    
    
    gcloud alpha identity groups update eng-discuss@foo.com --remove-posix-groups=eng

POSITIONAL ARGUMENTS
    

`EMAIL`
     The email address of the group to be updated. 
FLAGS
    

`--dynamic-user-query`=`DYNAMIC_USER_QUERY`
     Query that determines the memberships of the dynamic group. 

Example of a query: `--dynamic-user-query="user.organizations.exists(org,org.title=='SWE')"`

At most one of these can be specified: 

`--clear-posix-groups`
     Clear all POSIX groups from the specified Cloud Identity group. 
`--remove-posix-groups`=[`POSIX_GROUP`,…]
     Remove POSIX groups from the specified Cloud Identity group. You can specify multiple POSIX groups by either name or gid by using a comma-separated list. 

For example, use '--remove-posix-groups=1005,1006' to remove POSIX groups with group ids '1005' and '1006', or use '--remove-posix-groups=eng,docs' to remove POSIX groups named 'eng' and 'docs'. 

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
     This command uses the `cloudidentity/v1alpha1` API. The full documentation for this API can be found at: <https://cloud.google.com/identity/>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud identity groups update](https://docs.cloud.google.com/sdk/gcloud/reference/identity/groups/update)
    
    
    [gcloud beta identity groups update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/identity/groups/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
