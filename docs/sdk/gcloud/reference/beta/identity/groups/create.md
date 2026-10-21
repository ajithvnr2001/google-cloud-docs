---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/identity/groups/create/
title: gcloud beta identity groups create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:28:33.251844+00:00
---

# gcloud beta identity groups create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/identity/groups/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta identity groups create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta identity groups create - create a new group 
SYNOPSIS
    

`gcloud beta identity groups create` `EMAIL` `--organization`=`ORGANIZATION` [`--description`=`DESCRIPTION`] [`--display-name`=`DISPLAY_NAME`] [`--dynamic-user-query`=`DYNAMIC_USER_QUERY`] [`--with-initial-owner`=`WITH_INITIAL_OWNER`] [`--group-type`=`GROUP_TYPE`; default="discussion" | `--labels`=`LABELS`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Create a new group. 
EXAMPLES
     To quickly create a new Google Groups discussion group with default settings: 
    
    
    gcloud beta identity groups create eng-discuss@example.com --organization="example.com"

To create a new Google Groups discussion group with a display name and descripton: 
    
    
    gcloud beta identity groups create eng-discuss@example.com --organization="example.com" --display-name="Engineer Discuss" --description="Group for engineering discussions"

To create a new security group: 
    
    
    gcloud beta identity groups create security-group@example.com --organization="example.com" --group-type="security" --display-name="Security Group" --description="Description of Security Group"

POSITIONAL ARGUMENTS
    

`EMAIL`
     The email address of the group to be created. 
REQUIRED FLAGS
    

`--organization`=`ORGANIZATION`
     The organization the Group being created belongs to. This can be specified either as an ID ("123456789") or as the associated domain ("example.com"). 
OPTIONAL FLAGS
    

`--description`=`DESCRIPTION`
     An extended description to help users determine the purpose of a Group. For example, you can include information about who should join the Group, the types of messages to send to the Group, links to FAQs about the Group, or related Groups. Maximum length is 4,096 characters. 
`--display-name`=`DISPLAY_NAME`
     The Group's display name. 
`--dynamic-user-query`=`DYNAMIC_USER_QUERY`
     Query that determines the memberships of the dynamic group. 

Example of a query: \--dynamic-user-query="user.organizations.exists(org,org.title=='SWE')" 

`--with-initial-owner`=`WITH_INITIAL_OWNER`
     If specified the user making the request will be added as the initial owner of the group being created. `WITH_INITIAL_OWNER` must be one of: 

`empty`
     The creator of the group will not be the owner of the group. This is the default for dynamic groups. 
`with-initial-owner`
     The creator of the group will be the owner of the group. This is the default for non-dynamic groups. 
At most one of these can be specified: 

`--group-type`=`GROUP_TYPE`; default="discussion"
     The type of group to create. Setting group-type will add the appropriate labels for the type of group being created. `GROUP_TYPE` must be one of: 

`discussion`
     Creates a Google Groups discussion group. 
`dynamic`
     Creates a dynamic group. 
`security`
     Creates a security group. 
`--labels`=`LABELS`
     Labels for group resource. Example of labels "--labels cloudidentity.googleapis.com/groups.discussion_forum" 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `cloudidentity/v1beta1` API. The full documentation for this API can be found at: <https://cloud.google.com/identity/>
NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud identity groups create](https://docs.cloud.google.com/sdk/gcloud/reference/identity/groups/create)
    
    
    [gcloud alpha identity groups create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/identity/groups/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
