---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/identity/groups/search/
title: gcloud alpha identity groups search \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:40:27.830956+00:00
---

# gcloud alpha identity groups search  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/identity/groups/search/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha identity groups search Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha identity groups search - searches for Groups matching a specified query 
SYNOPSIS
    

`gcloud alpha identity groups search` `--labels`=`LABELS` `--organization`=`ORGANIZATION` [`--page-size`=`PAGE_SIZE`] [`--page-token`=`PAGE_TOKEN`] [`--view`=`VIEW`; default="basic"] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Searches for Groups matching a specified query. 
EXAMPLES
     To Search groups: 
    
    
    gcloud alpha identity groups search --organization="5149234212" --labels="cloudidentity.googleapis.com/groups.discussion_forum" --page-size=3 --page-token="ala9glealanal908"

REQUIRED FLAGS
    

`--labels`=`LABELS`
     One or more label entries that apply to the Group. Currently supported labels contain a key with an empty value. 

Google Groups are the default type of group and have a label with a key of 'cloudidentity.googleapis.com/groups.discussion_forum' and an empty value. 

Existing Google Groups can have an additional label with a key of 'cloudidentity.googleapis.com/groups.security' and an empty value added to them. `This is an immutable change and the security label cannot be removed once added.`

POSIX groups have a label with a key of 'cloudidentity.googleapis.com/groups.posix'. 

Dynamic groups have a label with a key of 'cloudidentity.googleapis.com/groups.dynamic'. 

Identity-mapped groups for Cloud Search have a label with a key of 'system/groups/external' and an empty value. 

Examples: {"cloudidentity.googleapis.com/groups.discussion_forum": ""} or {"system/groups/external": ""}. 

`--organization`=`ORGANIZATION`
     The organization ID for the groups being searched. 
OPTIONAL FLAGS
    

`--page-size`=`PAGE_SIZE`
     The maximum number of results to return. 

Note that the number of results returned may be less than this value even if there are more available results. To fetch all results, clients must continue calling this method repeatedly until the response no longer contains a nextPageToken. 

If unspecified, defaults to 200 'basic' view and to 50 for 'full' view. 

Must not be greater than 1000 for 'basic' view or 500 for 'full' view. 

`--page-token`=`PAGE_TOKEN`
     The nextPageToken value returned from a previous search request, if any. 
`--view`=`VIEW`; default="basic"
     The level of detail to be returned. There are two possible views: 'basic' and 'full'. If unspecified, default to 'basic'. `VIEW` must be one of: 

`basic`
     Default. Only basic group information is returned. 
`full`
     All group information is returned. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `cloudidentity/v1alpha1` API. The full documentation for this API can be found at: <https://cloud.google.com/identity/>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud identity groups search](https://docs.cloud.google.com/sdk/gcloud/reference/identity/groups/search)
    
    
    [gcloud beta identity groups search](https://docs.cloud.google.com/sdk/gcloud/reference/beta/identity/groups/search)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
