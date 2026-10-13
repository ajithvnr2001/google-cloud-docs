---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/asset/list/
title: gcloud alpha asset list \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:42:43.323720+00:00
---

# gcloud alpha asset list  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/asset/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha asset list Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha asset list - list the Cloud assets 
SYNOPSIS
    

`gcloud alpha asset list` (`--folder`=`FOLDER_ID` | `--organization`=`ORGANIZATION_ID` | `--project`=`PROJECT_ID`) [`--asset-types`=[`ASSET_TYPES`,…]] [`--content-type`=`CONTENT_TYPE`] [`--relationship-types`=[`RELATIONSHIP_TYPES`,…]] [`--snapshot-time`=`SNAPSHOT_TIME`] [`--filter`=`EXPRESSION`] [`--limit`=`LIMIT`] [`--page-size`=`PAGE_SIZE`] [`--sort-by`=[`FIELD`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` List the Cloud assets. Note that to list a project different from the project you want to bill, you can use --billing-project or authenticate with a service account. See <https://cloud.google.com/resource-manager/docs/cloud-asset-inventory/gcloud-asset> for examples of using a service account. 
EXAMPLES
     To list a snapshot of assets of type 'compute.googleapis.com/Disk' in project 'test-project' at '2019-03-05T00:00:00Z', run: 
    
    
    gcloud alpha asset list --project='test-project' --asset-types='compute.googleapis.com/Disk' --snapshot-time='2019-03-05T00:00:00Z'

REQUIRED FLAGS
    

Exactly one of these must be specified: 

`--folder`=`FOLDER_ID`
     The ID of the folder which is the root asset. 
`--organization`=`ORGANIZATION_ID`
     The ID of the organization which is the root asset. 
`--project`=`PROJECT_ID`
     The project which is the root asset. 

The Google Cloud project ID to use for this invocation. If omitted, then the current project is assumed; the current project can be listed using `gcloud config list --format='text(core.project)'` and can be set using `gcloud config set project PROJECTID`. 

`--project` and its fallback `core/project` property play two roles in the invocation: they specify both the project of the resource to operate on, and the project for API enablement checks, quota, and billing. To specify a different project for quota and billing, use the `--billing-project` flag or the `billing/quota_project` property. 

FLAGS
    

`--asset-types`=[`ASSET_TYPES`,…]
     A list of asset types (i.e., "compute.googleapis.com/Disk") to take a snapshot. If specified and non-empty, only assets matching the specified types will be returned. See <http://cloud.google.com/asset-inventory/docs/supported-asset-types> for supported asset types. 
`--content-type`=`CONTENT_TYPE`
     Asset content type. If not specified, no content but the asset name and type will be returned in the feed. For more information, see <https://cloud.google.com/asset-inventory/docs/reference/rest/v1/feeds#ContentType>. `CONTENT_TYPE` must be one of: `resource`, `iam-policy`, `org-policy`, `access-policy`, `os-inventory`, `relationship`. 
`--relationship-types`=[`RELATIONSHIP_TYPES`,…]
     A list of relationship types (i.e., "INSTANCE_TO_INSTANCEGROUP") to take a snapshot. This argument will only be honoured if content_type=RELATIONSHIP. If specified and non-empty, only relationships matching the specified types will be returned. See <http://cloud.google.com/asset-inventory/docs/supported-asset-types> for supported relationship types. 
`--snapshot-time`=`SNAPSHOT_TIME`
     Timestamp to take a snapshot on assets. This can only be a current or past time. If not specified, the current time will be used. Due to delays in resource data collection and indexing, there is a volatile window during which running the same query at different times may return different results. See $ [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes) for information on time formats. 
LIST COMMAND FLAGS
    

`--filter`=`EXPRESSION`
     Apply a Boolean filter `EXPRESSION` to each resource item to be listed. If the expression evaluates `True`, then that item is listed. For more details and examples of filter expressions, run $ [gcloud topic filters](https://docs.cloud.google.com/sdk/gcloud/reference/topic/filters). This flag interacts with other flags that are applied in this order: `--flatten`, `--sort-by`, `--filter`, `--limit`. 
`--limit`=`LIMIT`
     Maximum number of resources to list. The default is `unlimited`. This flag interacts with other flags that are applied in this order: `--flatten`, `--sort-by`, `--filter`, `--limit`. 
`--page-size`=`PAGE_SIZE`
     Some services group resource list output into pages. This flag specifies the maximum number of resources per page. The default is determined by the service if it supports paging, otherwise it is `unlimited` (no paging). Paging may be applied before or after `--filter` and `--limit` depending on the service. 
`--sort-by`=[`FIELD`,…]
     Comma-separated list of resource field key names to sort by. The default order is ascending. Prefix a field with ``~´´ for descending order on that field. This flag interacts with other flags that are applied in this order: `--flatten`, `--sort-by`, `--filter`, `--limit`. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud asset list](https://docs.cloud.google.com/sdk/gcloud/reference/asset/list)
    
    
    [gcloud beta asset list](https://docs.cloud.google.com/sdk/gcloud/reference/beta/asset/list)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-15 UTC."],[],[]] 
