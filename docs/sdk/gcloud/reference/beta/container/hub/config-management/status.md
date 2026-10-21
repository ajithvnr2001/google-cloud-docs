---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/hub/config-management/status/
title: gcloud beta container hub config-management status \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:58:40.554766+00:00
---

# gcloud beta container hub config-management status  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/hub/config-management/status/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta container hub config-management status Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta container hub config-management status - print the status of all clusters with Config Management enabled 
SYNOPSIS
    

`gcloud beta container hub config-management status` [`--filter`=`EXPRESSION`] [`--limit`=`LIMIT`] [`--page-size`=`PAGE_SIZE`] [`--sort-by`=[`FIELD`,…]] [`--uri`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` The `Status` column indicates the status of the Config Sync component. `Status` displays `NOT_INSTALLED` when Config Sync is not installed. `Status` displays `NOT_CONFIGURED` when Config Sync is installed but git/oci is not configured. `Status` displays `SYNCED` when Config Sync is installed and git/oci is configured and the last sync was successful. `Status` displays `ERROR` when Config Sync encounters errors. `Status` displays `STOPPED` when Config Sync stops syncing configs to the cluster. `Status` displays `PENDING` when Config Sync has not reached the desired state. Otherwise, `Status` displays `UNSPECIFIED`. 

The `Synced_to_Fleet_Default` status indicates whether each membership's configuration has been synced with the [fleet-default membership configuration ](https://cloud.google.com/kubernetes-engine/fleet-management/docs/manage-features). `Synced_to_Fleet_Default` displays `FLEET_DEFAULT_NOT_CONFIGURED` when fleet-default membership configuration is not enabled. `Synced_to_Fleet_Default` for an individual membership may be `UNKNOWN` if configuration has yet to be applied to this membership since enabling fleet-default membership configuration. See the `enable` and `apply` commands for more details. 

EXAMPLES
     Print the status of the Config Management feature: 
    
    
    gcloud beta container hub config-management status

> Name | Status | Last_Synced_Token | Sync_Branch | Last_Synced_Time | Policy_Controller | Hierarchy_Controller | Version | Upgrades | Synced_To_Fleet_Default  
> ---|---|---|---|---|---|---|---|---|---  
> managed-cluster | SYNCED | 2945500b7f | acme | 2020-03-23 11:12:31 -0700 PDT | NA | NA | 1.18.3 | auto | FLEET_DEFAULT_NOT_CONFIGURED  
  
View the status for the cluster named `managed-cluster-a`: 
    
    
    gcloud beta container hub config-management status --flatten=acm_status --filter="acm_status.name:managed-cluster-a"

Use a regular expression to list status for multiple clusters: 
    
    
    gcloud beta container hub config-management status --flatten=acm_status --filter="acm_status.name ~ managed-cluster.*"

List all clusters where current Config Sync `Status` is `SYNCED`: 
    
    
    gcloud beta container hub config-management status --flatten=acm_status --filter="acm_status.config_sync:SYNCED"

List all the clusters where sync_branch is `v1` and current Config Sync `Status` is not `SYNCED`: 
    
    
    gcloud beta container hub config-management status --flatten=acm_status --filter="acm_status.sync_branch:v1 AND -acm_status.config_sync:SYNCED"

LIST COMMAND FLAGS
    

`--filter`=`EXPRESSION`
     Apply a Boolean filter `EXPRESSION` to each resource item to be listed. If the expression evaluates `True`, then that item is listed. For more details and examples of filter expressions, run $ [gcloud topic filters](https://docs.cloud.google.com/sdk/gcloud/reference/topic/filters). This flag interacts with other flags that are applied in this order: `--flatten`, `--sort-by`, `--filter`, `--limit`. 
`--limit`=`LIMIT`
     Maximum number of resources to list. The default is `unlimited`. This flag interacts with other flags that are applied in this order: `--flatten`, `--sort-by`, `--filter`, `--limit`. 
`--page-size`=`PAGE_SIZE`
     Some services group resource list output into pages. This flag specifies the maximum number of resources per page. The default is determined by the service if it supports paging, otherwise it is `unlimited` (no paging). Paging may be applied before or after `--filter` and `--limit` depending on the service. 
`--sort-by`=[`FIELD`,…]
     Comma-separated list of resource field key names to sort by. The default order is ascending. Prefix a field with ``~´´ for descending order on that field. This flag interacts with other flags that are applied in this order: `--flatten`, `--sort-by`, `--filter`, `--limit`. 
`--uri`
     Print a list of resource URIs instead of the default output, and change the command output to a list of URIs. If this flag is used with `--format`, the formatting is applied on this URI list. To display URIs alongside other keys instead, use the `uri()` transform. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. This variant is also available: 
    
    
    [gcloud alpha container hub config-management status](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/hub/config-management/status)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
