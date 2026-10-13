---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/clusters/list/
title: gcloud beta dataproc clusters list \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:58:25.047532+00:00
---

# gcloud beta dataproc clusters list  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/clusters/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta dataproc clusters list Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta dataproc clusters list - view a list of clusters in a project 
SYNOPSIS
    

`gcloud beta dataproc clusters list` [`--region`=`REGION`] [`--filter`=`EXPRESSION`] [`--limit`=`LIMIT`] [`--page-size`=`PAGE_SIZE`; default=100] [`--sort-by`=[`FIELD`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` View a list of clusters in a project. An optional filter can be used to constrain the clusters returned. Filters are case-sensitive and have the following syntax: 
    
    
    field = value [AND [field = value]] …

where `field` is one of `status.state`, `clusterName`, or `labels.[KEY]`, and `[KEY]` is a label key. `value` can be `*` to match all values. `status.state` can be one of the following: `ACTIVE`, `INACTIVE`, `CREATING`, `RUNNING`, `ERROR`, `DELETING`, or `UPDATING`. `ACTIVE` contains the `CREATING`, `UPDATING`, and `RUNNING` states. `INACTIVE` contains the `DELETING` and `ERROR` states. `clusterName` is the name of the cluster provided at creation time. Only the logical `AND` operator is supported; space-separated items are treated as having an implicit `AND` operator. 

EXAMPLES
     To see the list of all clusters in Dataproc's 'us-central1' region, run: 
    
    
    gcloud beta dataproc clusters list --region='us-central1'

To show a cluster in Dataproc's 'global' region with the name 'mycluster', run: 
    
    
    gcloud beta dataproc clusters list --region='global' --filter='clusterName = mycluster'

To see the list of all clusters in Dataproc's 'global' region with specified labels, run: 
    
    
    gcloud beta dataproc clusters list --region='global' --filter='labels.env = staging AND
      labels.starred = *'

To see a list of all active clusters in Dataproc's 'europe-west1' region with specified labels, run: 
    
    
    gcloud beta dataproc clusters list --region='europe-west1' --filter='status.state = ACTIVE AND
      labels.env = staging AND labels.starred = *'

FLAGS
    

`--region`=`REGION`
     Dataproc region to use. Each Dataproc region constitutes an independent resource namespace constrained to deploying instances into Compute Engine zones inside the region. Overrides the default `dataproc/region` property value for this command invocation. 
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
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud dataproc clusters list](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/list)
    
    
    [gcloud alpha dataproc clusters list](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/clusters/list)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
