---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/bigtable/logical-views/update/
title: gcloud beta bigtable logical-views update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:10:12.024174+00:00
---

# gcloud beta bigtable logical-views update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/bigtable/logical-views/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta bigtable logical-views update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta bigtable logical-views update - update a Bigtable logical view 
SYNOPSIS
    

`gcloud beta bigtable logical-views update` (`LOGICAL_VIEW` : `--instance`=`INSTANCE`) (`--deletion-protection`=`DELETION_PROTECTION` `--query`=`QUERY`) [`--async`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Update a Bigtable logical view. 
EXAMPLES
     To update a logical view to a new query, run: 
    
    
    gcloud beta bigtable logical-views update my-logical-view-id --instance=my-instance-id --query="SELECT my-column-family2 FROM my-table"

To enable deletion protection on a logical view, run: 
    
    
    gcloud beta bigtable logical-views update my-logical-view-id --instance=my-instance-id --deletion-protection

POSITIONAL ARGUMENTS
    

Logical view resource - The logical view to update. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `logical_view` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`LOGICAL_VIEW`
     ID of the logical view or fully qualified identifier for the logical view. 

To set the `name` attribute: 

  * provide the argument `logical_view` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--instance`=`INSTANCE`
     Bigtable instance for the logical view. 

To set the `instance` attribute: 

  * provide the argument `logical_view` on the command line with a fully specified name; 
  * provide the argument `--instance` on the command line. 


REQUIRED FLAGS
    

At least one of these must be specified: 

`--deletion-protection`=`DELETION_PROTECTION`
     Whether the view is protected from deletion. 
`--query`=`QUERY`
     The query of the view. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud bigtable logical-views update](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/logical-views/update)
    
    
    [gcloud alpha bigtable logical-views update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/bigtable/logical-views/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
