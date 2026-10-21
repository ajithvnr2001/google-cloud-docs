---
url: https://docs.cloud.google.com/sdk/gcloud/reference/firestore/databases/update/
title: gcloud firestore databases update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:36:17.336528+00:00
---

# gcloud firestore databases update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/firestore/databases/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud firestore databases update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud firestore databases update - update the database configuration of a Cloud Firestore database 
SYNOPSIS
    

`gcloud firestore databases update` [`--async`] [`--concurrency-mode`=`CONCURRENCY_MODE`] [`--database`=`DATABASE`] [`--delete-protection`] [`--enable-pitr`] [`--type`=`TYPE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Update the database configuration of a Cloud Firestore database. 
EXAMPLES
     The following command updates the database type of a Cloud Firestore database. 
    
    
    gcloud firestore databases update --type=firestore-native

FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--concurrency-mode`=`CONCURRENCY_MODE`
     The concurrency control mode to use for this database. `CONCURRENCY_MODE` must be one of: `optimistic`, `pessimistic`. 
Database resource - Cloud Firestore database to update. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--database` on the command line with a fully specified name; 
  * the default value of argument [--database] is `(default)` with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 


`--database`=`DATABASE`
     ID of the database or fully qualified identifier for the database. 

To set the `database` attribute: 

  * provide the argument `--database` on the command line; 
  * the default value of argument [--database] is `(default)`. 


`--delete-protection`
     If set to true, the Firestore database will be updated to have database delete protection enabled. A database with delete protection enabled cannot be deleted. You can disable the delete protection via --no-delete-protection. 
`--enable-pitr`
     If set to true, the Firestore database will be updated to enable Point In Time Recovery. You can disable the this feature via --no-enable-pitr. 
`--type`=`TYPE`
     The database type. `TYPE` must be one of: `datastore-mode`, `firestore-native`. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `firestore/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/firestore>
NOTES
     These variants are also available: 
    
    
    [gcloud alpha firestore databases update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/firestore/databases/update)
    
    
    [gcloud beta firestore databases update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/firestore/databases/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
