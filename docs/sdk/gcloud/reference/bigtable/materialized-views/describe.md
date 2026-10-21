---
url: https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/materialized-views/describe/
title: gcloud bigtable materialized-views describe \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:07:57.299410+00:00
---

# gcloud bigtable materialized-views describe  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/materialized-views/describe/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud bigtable materialized-views describe Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud bigtable materialized-views describe - describe an existing Bigtable materialized view 
SYNOPSIS
    

`gcloud bigtable materialized-views describe` (`MATERIALIZED_VIEW` : `--instance`=`INSTANCE`) [`--view`=`VIEW`; default="schema"] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Describe an existing Bigtable materialized view. 
EXAMPLES
     To get back information related to a view's schema (for example, description), run: 
    
    
    gcloud bigtable materialized-views describe my-materialized-view-id --instance=my-instance-id --view=schema

or (because schema is the default view) simply: 
    
    
    gcloud bigtable materialized-views describe my-materialized-view-id --instance=my-instance-id

To get back information related to the view's replication state, run: 
    
    
    gcloud bigtable materialized-views describe my-materialized-view-id --instance=my-instance-id --view=replication

To get back all information for the view, run: 
    
    
    gcloud bigtable materialized-views describe my-materialized-view-id --instance=my-instance-id --view=full

POSITIONAL ARGUMENTS
    

Materialized view resource - The materialized view to describe. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `materialized_view` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`MATERIALIZED_VIEW`
     ID of the materialized view or fully qualified identifier for the materialized view. 

To set the `name` attribute: 

  * provide the argument `materialized_view` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--instance`=`INSTANCE`
     Bigtable instance for the materialized view. 

To set the `instance` attribute: 

  * provide the argument `materialized_view` on the command line with a fully specified name; 
  * provide the argument `--instance` on the command line. 


FLAGS
    

`--view`=`VIEW`; default="schema"
     Specifies what type of information to return about the view. `VIEW` must be one of: `full`, `replication`, `schema`. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha bigtable materialized-views describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/bigtable/materialized-views/describe)
    
    
    [gcloud beta bigtable materialized-views describe](https://docs.cloud.google.com/sdk/gcloud/reference/beta/bigtable/materialized-views/describe)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
