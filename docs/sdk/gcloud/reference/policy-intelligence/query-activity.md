---
url: https://docs.cloud.google.com/sdk/gcloud/reference/policy-intelligence/query-activity/
title: gcloud policy-intelligence query-activity \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:17:27.461309+00:00
---

# gcloud policy-intelligence query-activity  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/policy-intelligence/query-activity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud policy-intelligence query-activity Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud policy-intelligence query-activity - query activities on cloud resource 
SYNOPSIS
    

`gcloud policy-intelligence query-activity` `--activity-type`=`ACTIVITY_TYPE` `--project`=`PROJECT` [`--limit`=`LIMIT`; default=1000] [`--page-size`=`PAGE_SIZE`; default=500] [`--query-filter`=`QUERY_FILTER`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Query activities with certain types of specific container resource. For \--activity-type, supported values are: 

  * serviceAccountLastAuthentication 
  * serviceAccountKeyLastAuthentication 


EXAMPLES
     To query serviceAccountKeyLastAuthentication activities of a project, run: 
    
    
    gcloud policy-intelligence query-activity --activity-type=serviceAccountKeyLastAuthentication --project=project-id

To query serviceAccountLastAuthentication activities of a project with no limit, run: 
    
    
    gcloud policy-intelligence query-activity --activity-type=serviceAccountLastAuthentication --project=project-id --limit=unlimited

To query serviceAccountLastAuthentication with filtering on certain service account, run: 
    
    
    gcloud policy-intelligence query-activity --activity-type=serviceAccountLastAuthentication --project=project-id --query-filter='activities.full_resource_name="//iam.googleapis.com/projects/project-id/serviceAccounts/service-account-name@project-id.iam.gserviceaccount.com"'

To query serviceAccountLastAuthentication with filtering on multiple service accounts, run: 
    
    
    gcloud policy-intelligence query-activity --activity-type=serviceAccountLastAuthentication --project=project-id --query-filter='activities.full_resource_name="//iam.googleapis.com/projects/project-id/serviceAccounts/service-account-name-1@project-id.iam.gserviceaccount.com" OR
     activities.full_resource_name="//iam.googleapis.com/projects/projec\
    t-id/serviceAccounts/service-account-name-2@project-id.iam.gservicea\
    ccount.com" OR
     activities.full_resource_name="//iam.googleapis.com/projects/projec\
    t-id/serviceAccounts/service-account-name-3@project-id.iam.gservicea\
    ccount.com"'

REQUIRED FLAGS
    

`--activity-type`=`ACTIVITY_TYPE`
     Type of the activities. `ACTIVITY_TYPE` must be one of: `serviceAccountLastAuthentication`, `serviceAccountKeyLastAuthentication`. 
`--project`=`PROJECT`
     The project ID or number to query the activities. 
OPTIONAL FLAGS
    

`--limit`=`LIMIT`; default=1000
     Max number of query result. Default to be 1000 and max to be unlimited, i.e., \--limit=unlimited. 
`--page-size`=`PAGE_SIZE`; default=500
     Max page size for each http response. Default to be 500 and max to be 1000. 
`--query-filter`=`QUERY_FILTER`
     Filter on activities, separated by "OR" if multiple filters are specified. At most 10 filter restrictions are supported in the query-filter. e.g. \--query-filter='activities.full_resource_name="//iam.googleapis.com/projects/project-id/serviceAccounts/service-account-name-1@project-id.iam.gserviceaccount.com" OR activities.full_resource_name="//iam.googleapis.com/projects/project-id/serviceAccounts/service-account-name-2@project-id.iam.gserviceaccount.com"' 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
