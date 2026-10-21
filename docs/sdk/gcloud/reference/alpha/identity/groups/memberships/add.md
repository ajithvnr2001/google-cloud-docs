---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/identity/groups/memberships/add/
title: gcloud alpha identity groups memberships add \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:33:50.846518+00:00
---

# gcloud alpha identity groups memberships add  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/identity/groups/memberships/add/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha identity groups memberships add Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha identity groups memberships add - create a new membership in an existing group 
SYNOPSIS
    

`gcloud alpha identity groups memberships add` `--group-email`=`GROUP_EMAIL` `--member-email`=`MEMBER_EMAIL` [`--expiration`=`EXPIRATION`] [`--organization`=`ORGANIZATION`] [`--roles`=[`ROLES`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Create a new membership in an existing group. 
EXAMPLES
     To create a new membership in a group: 
    
    
    gcloud alpha identity groups memberships add --group-email="eng-discuss@foo.com" --member-email="user@foo.com"

REQUIRED FLAGS
    

`--group-email`=`GROUP_EMAIL`
     The email address of the group the new membership is being added to. 
`--member-email`=`MEMBER_EMAIL`
     The email address of the group or user being added to a group. 
OPTIONAL FLAGS
    

`--expiration`=`EXPIRATION`
     Optional time of expiration for the membership. This is given as a duration from now, for example '30d', '6m', '3y' for 30 days, 6 months, or 3 years respectively. 
`--organization`=`ORGANIZATION`
     The organization ID of the group the new membership is being added to. 
`--roles`=[`ROLES`,…]
     A comma-separated list of roles for a member within the Group. If not specified, MEMBER will be used as a default value. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `cloudidentity/v1alpha1` API. The full documentation for this API can be found at: <https://cloud.google.com/identity/>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud identity groups memberships add](https://docs.cloud.google.com/sdk/gcloud/reference/identity/groups/memberships/add)
    
    
    [gcloud beta identity groups memberships add](https://docs.cloud.google.com/sdk/gcloud/reference/beta/identity/groups/memberships/add)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
