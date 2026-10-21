---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/identity/groups/preview/
title: gcloud alpha identity groups preview \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:56:08.084127+00:00
---

# gcloud alpha identity groups preview  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/identity/groups/preview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha identity groups preview Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha identity groups preview - retrieve a list of users in a customer account using CEL query 
SYNOPSIS
    

`gcloud alpha identity groups preview` `--customer`=`CUSTOMER` [`--custom-field-mask`=[`custom-mask`,…]] [`--max-results`=`MAX_RESULTS`; default=100] [`--page-token`=`PAGE_TOKEN`] [`--projection`=`PROJECTION`; default="basic"] [`--query`=`QUERY`] [`--view-type`=`VIEW_TYPE`; default="admin-view"] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Retrieve a list of users in a customer account using CEL query. 
EXAMPLES
     To retrieve a list of user in a customer and filter it with a query, run: 
    
    
    gcloud alpha identity groups preview --query="user.locations.exists(loc, loc.desk_code == 'abc')" --customer=A1234abcd

To retrieve a list of users with only fullName and primaryEMail fields, run: 
    
    
    gcloud alpha identity groups preview --query="user.locations.exists(loc, loc.desk_code == 'abc')" --customer=A1234abcd --format="flattened(nextPageToken, users[].primaryEmail, users[].name.fullName)"

REQUIRED FLAGS
    

`--customer`=`CUSTOMER`
     The customer ID for the customer's G Suite account. 
OPTIONAL FLAGS
    

`--custom-field-mask`=[`custom-mask`,…]
     A comma-separated list of schema names. All fields from these schemas are fetched. This should only be set when --projection=custom. 
`--max-results`=`MAX_RESULTS`; default=100
     Maximum number of results to return. Acceptable values are 1 to 500, inclusive. 
`--page-token`=`PAGE_TOKEN`
     Token to specify next page in the list. 
`--projection`=`PROJECTION`; default="basic"
     Subsets of fields to fetch for this user. `PROJECTION` must be one of: `basic`, `full`, `custom`. 
`--query`=`QUERY`
     Query string using CEL and supported user attributes 
`--view-type`=`VIEW_TYPE`; default="admin-view"
     Whether to fetch the administrator-only or domain-wide public view of the user. `VIEW_TYPE` must be one of: `admin-view`, `domain-public`. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud beta identity groups preview](https://docs.cloud.google.com/sdk/gcloud/reference/beta/identity/groups/preview)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
