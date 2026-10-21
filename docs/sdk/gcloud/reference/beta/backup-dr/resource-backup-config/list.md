---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/backup-dr/resource-backup-config/list/
title: gcloud beta backup-dr resource-backup-config list \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:09:03.435166+00:00
---

# gcloud beta backup-dr resource-backup-config list  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/backup-dr/resource-backup-config/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta backup-dr resource-backup-config list Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta backup-dr resource-backup-config list - show backup configuration metadata associated with specified resources in a particular location for the project 
SYNOPSIS
    

`gcloud beta backup-dr resource-backup-config list` `--location`=`LOCATION` [`--filter`=`EXPRESSION`] [`--limit`=`LIMIT`] [`--page-size`=`PAGE_SIZE`] [`--sort-by`=[`FIELD`,…]] [`--uri`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Show backup configuration metadata associated with specified resources in a particular location for the project. 
EXAMPLES
    

  * To list protection summary for a resource named `resource-1`: 


    
    
    gcloud beta backup-dr resource-backup-config list --project=sample-project --location=us-central1 --filter="target_resource_display_name=resource-1"

  * To list protection summary for a resource named `resource-1` that has backup configured: 


    
    
    gcloud beta backup-dr resource-backup-config list --project=sample-project --location=us-central1 --filter="target_resource_display_name=resource-1 AND backup_configured=true"

You can sort the results using the `--sort-by` flag. The only supported field for sorting is `target_resource_display_name`. 

Example of sorting: 
    
    
    gcloud beta backup-dr resource-backup-config list --project=sample-project --location=us-central1 --sort-by="target_resource_display_name"

REQUIRED FLAGS
    

Location resource - Location for which the resource backup config should be listed. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--location` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`--location`=`LOCATION`
     ID of the location or fully qualified identifier for the location. 

To set the `location` attribute: 

  * provide the argument `--location` on the command line. 


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

BRIEF
     list backup configurations for a specified project and location. 
FLAGS/ARGUMENTS
     `--project`: Project for which backup configurations should be listed. 

`--location`: Location for which backup configurations should be listed. 

`--filter`: The filter expression to filter results. 

`--sort-by`: The field to sort results by. 

SUBARGUMENTS
     `target_resource_display_name`: Name of the resource for which protection summary is to be listed. 

`target_resource_type`: Type of resource for which protection summary is to be displayed. 

Allowed values: 

  * CLOUD_SQL_INSTANCE 
  * COMPUTE_ENGINE_VM 



`backup_configured`: Displays if the specified resource has backups configured. 

`vaulted`: Displays if configured backups are protected using a backup vault. 

`backup_configs_details.backup_config_source_display_name`: Name of the backup schedule applied to the resource. 

`backup_configs_details.type`: Backup schedule type applied to the resource. 

Allowed values: 

  * CLOUD_SQL_INSTANCE_BACKUP_CONFIG 
  * COMPUTE_ENGINE_RESOURCE_POLICY 
  * BACKUPDR_BACKUP_PLAN 
  * BACKUPDR_TEMPLATE 


NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud backup-dr resource-backup-config list](https://docs.cloud.google.com/sdk/gcloud/reference/backup-dr/resource-backup-config/list)
    
    
    [gcloud alpha backup-dr resource-backup-config list](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/backup-dr/resource-backup-config/list)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
