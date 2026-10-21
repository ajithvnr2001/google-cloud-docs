---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/bigtable/authorized-views/create/
title: gcloud alpha bigtable authorized-views create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:21:57.422873+00:00
---

# gcloud alpha bigtable authorized-views create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/bigtable/authorized-views/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha bigtable authorized-views create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha bigtable authorized-views create - create a new Cloud Bigtable authorized view 
SYNOPSIS
    

`gcloud alpha bigtable authorized-views create` (`AUTHORIZED_VIEW` : `--instance`=`INSTANCE` `--table`=`TABLE`) [`--async`] [`--definition-file`=`DEFINITION_FILE`] [`--pre-encoded`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Create a new Cloud Bigtable authorized view. 
EXAMPLES
     To create an authorized view `my-authorized-view` in instance `my-instance` and table `my-table`, using the definition file `authorized_view.json`: 
    
    
    gcloud alpha bigtable authorized-views create my-authorized-view --instance=test-instance --table=test-table --definition-file=authorized_view.json

To create an authorized view `my-authorized-view` in instance `my-instance` and table `my-table`, using the pre-encoded definition file `authorized_view_pre_encoded.json`: 
    
    
    gcloud alpha bigtable authorized-views create my-authorized-view --instance=test-instance --table=test-table --definition-file=authorized_view_pre_encoded.json --pre-encoded

POSITIONAL ARGUMENTS
    

Authorized view resource - Cloud Bigtable authorized view to create. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `authorized_view` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`AUTHORIZED_VIEW`
     ID of the authorized-view or fully qualified identifier for the authorized-view. 

To set the `authorized_view` attribute: 

  * provide the argument `authorized_view` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--instance`=`INSTANCE`
     Name of the Bigtable instance. 

To set the `instance` attribute: 

  * provide the argument `authorized_view` on the command line with a fully specified name; 
  * provide the argument `--instance` on the command line. 


`--table`=`TABLE`
     Name of the Bigtable table. 

To set the `table` attribute: 

  * provide the argument `authorized_view` on the command line with a fully specified name; 
  * provide the argument `--table` on the command line. 


FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--definition-file`=`DEFINITION_FILE`
     Path to a JSON or YAML file containing a valid authorized view protobuf. 

The `name` field is ignored. The name is deduced from the other command line arguments. 

Example: { "subsetView": { "rowPrefixes": ["store1#"], "familySubsets": { "column_family_name": { "qualifiers":["address"], "qualifierPrefixes":["tel"] } } }, "deletionProtection": true } 

`--pre-encoded`
     By default, Base64 encoding is applied to all binary fields ("rowPrefixes", "qualifiers" and "qualifierPrefixes") in the JSON or YAML definition file. 

Use this to indicate that all binary fields are already Base64-encoded and should be used directly. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `bigtableadmin/v2` API. The full documentation for this API can be found at: <https://cloud.google.com/bigtable/>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud bigtable authorized-views create](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/authorized-views/create)
    
    
    [gcloud beta bigtable authorized-views create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/bigtable/authorized-views/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
