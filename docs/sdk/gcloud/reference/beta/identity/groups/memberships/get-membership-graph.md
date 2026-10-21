---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/identity/groups/memberships/get-membership-graph/
title: gcloud beta identity groups memberships get-membership-graph \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:03:39.642915+00:00
---

# gcloud beta identity groups memberships get-membership-graph  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/identity/groups/memberships/get-membership-graph/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta identity groups memberships get-membership-graph Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta identity groups memberships get-membership-graph - get a membership graph of just a member or both a member and a group 
SYNOPSIS
    

`gcloud beta identity groups memberships get-membership-graph` `--labels`=`LABELS` `--member-email`=`MEMBER_EMAIL` [`--group-email`=`GROUP_EMAIL`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Get a membership graph of just a member or both a member and a group. 
EXAMPLES
     To get a membership graph of just a member. 
    
    
    gcloud beta identity groups memberships get-membership-graph --member-email=eng-discuss@foo.com --labels=cloudidentity.googleapis.com/groups.discussion_forum

To get a membership graph between a member and a group. 
    
    
    gcloud beta identity groups memberships get-membership-graph --member-email=eng-discuss@foo.com --group-email=eng@foo.com --labels=cloudidentity.googleapis.com/groups.discussion_forum

REQUIRED FLAGS
    

`--labels`=`LABELS`
     The labels of the groups in the membership graph. 
`--member-email`=`MEMBER_EMAIL`
     The email address of the member to get the membership graph for. 
OPTIONAL FLAGS
    

`--group-email`=`GROUP_EMAIL`
     The email address of the group to constrain the membership graph with. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `cloudidentity/v1beta1` API. The full documentation for this API can be found at: <https://cloud.google.com/identity/>
NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud identity groups memberships get-membership-graph](https://docs.cloud.google.com/sdk/gcloud/reference/identity/groups/memberships/get-membership-graph)
    
    
    [gcloud alpha identity groups memberships get-membership-graph](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/identity/groups/memberships/get-membership-graph)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
