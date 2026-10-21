---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/operations/list/
title: gcloud alpha dataproc operations list \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:32:06.619423+00:00
---

# gcloud alpha dataproc operations list  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/operations/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha dataproc operations list Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha dataproc operations list - view the list of all operations 
SYNOPSIS
    

`gcloud alpha dataproc operations list` [`--cluster`=`CLUSTER`] [`--region`=`REGION`] [`--state-filter`=`STATE_FILTER`] [`--filter`=`EXPRESSION`] [`--limit`=`LIMIT`] [`--page-size`=`PAGE_SIZE`; default=100] [`--sort-by`=[`FIELD`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` View a list of operations in a project. An optional filter can be used to constrain the operations returned. Filters are case-sensitive and have the following syntax: 
    
    
    field = value [AND [field = value]] …

where `field` is either of `status.state` or `labels.[KEY]`, where `[KEY]` is a label key. `value` can be `*` to match all values. `status.state` is one of: `PENDING`, `ACTIVE`, `DONE`. Only the logical `AND` operator is supported; space-separated items are treated as having an implicit `AND` operator. 

EXAMPLES
     To see the list of all operations in Dataproc's 'us-central1' region, run: 
    
    
    gcloud alpha dataproc operations list --region='us-central1'

To see the list of all create cluster operations in Dataproc's 'global' region, run: 
    
    
    gcloud alpha dataproc operations list --region='global' --filter='operationType = CREATE'

To see the list of all active operations in a cluster named 'mycluster' located in Dataproc's 'global' region, run: 
    
    
    gcloud alpha dataproc operations list --region='global' --filter='status.state = RUNNING AND
      clusterName = mycluster'

To see a list of all pending operations with the label `env=staging` on cluster `mycluster` located in Dataproc's 'us-central1' region, run: 
    
    
    gcloud alpha dataproc operations list --region='us-central1' --filter='status.state = PENDING
      AND labels.env = staging AND clusterName = mycluster'

FLAGS
    

`--cluster`=`CLUSTER`
     Restrict to the operations of this Dataproc cluster. This flag is ignored when \--filter is specified. The equivalent term in a --filter expression is: `clusterName = myclustername`
`--region`=`REGION`
     Dataproc region to use. Each Dataproc region constitutes an independent resource namespace constrained to deploying instances into Compute Engine zones inside the region. Overrides the default `dataproc/region` property value for this command invocation. 
`--state-filter`=`STATE_FILTER`
     Filter by cluster state. This flag is ignored when --filter is specified. The equivalent term in a --filter expression is: `status.state = ACTIVE`. `STATE_FILTER` must be one of: `active`, `inactive`. 
LIST COMMAND FLAGS
    

`--filter`=`EXPRESSION`
     Apply a Boolean filter `EXPRESSION` to each resource item to be listed. If the expression evaluates `True`, then that item is listed. For more details and examples of filter expressions, run $ [gcloud topic filters](https://docs.cloud.google.com/sdk/gcloud/reference/topic/filters). This flag interacts with other flags that are applied in this order: `--flatten`, `--sort-by`, `--filter`, `--limit`. 
`--limit`=`LIMIT`
     Maximum number of resources to list. The default is `unlimited`. This flag interacts with other flags that are applied in this order: `--flatten`, `--sort-by`, `--filter`, `--limit`. 
`--page-size`=`PAGE_SIZE`; default=100
     Some services group resource list output into pages. This flag specifies the maximum number of resources per page. The default is `100`. Paging may be applied before or after `--filter` and `--limit` depending on the service. 
`--sort-by`=[`FIELD`,…]
     Comma-separated list of resource field key names to sort by. The default order is ascending. Prefix a field with ``~´´ for descending order on that field. This flag interacts with other flags that are applied in this order: `--flatten`, `--sort-by`, `--filter`, `--limit`. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud dataproc operations list](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/operations/list)
    
    
    [gcloud beta dataproc operations list](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/operations/list)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
