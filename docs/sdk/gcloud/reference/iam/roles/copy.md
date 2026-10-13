---
url: https://docs.cloud.google.com/sdk/gcloud/reference/iam/roles/copy/
title: gcloud iam roles copy \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:29:55.950324+00:00
---

# gcloud iam roles copy  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/iam/roles/copy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud iam roles copy Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud iam roles copy - create a role from an existing role 
SYNOPSIS
    

`gcloud iam roles copy` [`--dest-organization`=`DEST_ORGANIZATION`] [`--dest-project`=`DEST_PROJECT`] [`--destination`=`DESTINATION`] [`--source`=`SOURCE`] [`--source-organization`=`SOURCE_ORGANIZATION`] [`--source-project`=`SOURCE_PROJECT`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     This command creates a role from an existing role. 
EXAMPLES
     To create a copy of an existing role ``spanner.databaseAdmin`` into an organization with ``1234567``, run: 
    
    
    gcloud iam roles copy --source="roles/spanner.databaseAdmin" --destination=CustomViewer --dest-organization=1234567

To create a copy of an existing role ``spanner.databaseAdmin`` into a project with ``PROJECT_ID``, run: 
    
    
    gcloud iam roles copy --source="roles/spanner.databaseAdmin" --destination=CustomSpannerDbAdmin --dest-project=PROJECT_ID

To modify the newly created role see the roles update command. 

FLAGS
    

`--dest-organization`=`DEST_ORGANIZATION`
     The organization of the destination role. 
`--dest-project`=`DEST_PROJECT`
     The project of the destination role. 
`--destination`=`DESTINATION`
     The destination role ID for the new custom role. For example: viewer. 
`--source`=`SOURCE`
     The source role ID. For predefined roles, for example: roles/viewer. For custom roles, for example: myCompanyAdmin. 
`--source-organization`=`SOURCE_ORGANIZATION`
     The organization of the source role if it is an custom role. 
`--source-project`=`SOURCE_PROJECT`
     The project of the source role if it is an custom role. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha iam roles copy](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/iam/roles/copy)
    
    
    [gcloud beta iam roles copy](https://docs.cloud.google.com/sdk/gcloud/reference/beta/iam/roles/copy)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
