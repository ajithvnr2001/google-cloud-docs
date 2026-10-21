---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/firestore/databases/connection-string/
title: gcloud beta firestore databases connection-string \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:07:58.927687+00:00
---

# gcloud beta firestore databases connection-string  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/firestore/databases/connection-string/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta firestore databases connection-string Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta firestore databases connection-string - prints the mongo connection string for the given Firestore database 
SYNOPSIS
    

`gcloud beta firestore databases connection-string` `--database`=`DATABASE` [`--auth`=`AUTH`; default="none" | `--validate`=`VALIDATE`] [`GCLOUD_WIDE_FLAG …`]
EXAMPLES
     To get the connection string for a Firestore database with a databaseId `testdb` without auth configuration. 
    
    
    gcloud beta firestore databases connection-string --database=testdb --auth=none

To get the connection string for a Firestore database with a databaseId `testdb` with Google Compute Engine VM auth. 
    
    
    gcloud beta firestore databases connection-string --database=testdb --auth=gce-vm

REQUIRED FLAGS
    

`--database`=`DATABASE`
     The database to operate on. 

For example, to operate on database `foo`: 
    
    
    gcloud beta firestore databases connection-string --database='foo'

OPTIONAL FLAGS
    

At most one of these can be specified: 

`--auth`=`AUTH`; default="none"
     The auth configuration for the connection string. 

If connecting from a Google Compute Engine VM, use `gce-vm`. For short term access using the gcloud CLI's access token, use `access-token`. For password auth use scram-sha-256. Otherwise, use `none` and configure auth manually. 

`AUTH` must be one of: `none`, `gce-vm`, `access-token`, `scram-sha-256`. 

`--validate`=`VALIDATE`
     Validate the specified connection string for the current database. This command checks that the connection string is well formed, contains the required parameters, and specifies correct configuration values for the current database. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud firestore databases connection-string](https://docs.cloud.google.com/sdk/gcloud/reference/firestore/databases/connection-string)
    
    
    [gcloud alpha firestore databases connection-string](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/firestore/databases/connection-string)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
