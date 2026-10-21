---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/recommender/insights/list/
title: gcloud alpha recommender insights list \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:43:16.592739+00:00
---

# gcloud alpha recommender insights list  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/recommender/insights/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha recommender insights list Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha recommender insights list - list insights for Google Cloud resources 
SYNOPSIS
    

`gcloud alpha recommender insights list` (`--billing-account`=`BILLING_ACCOUNT` | `--folder`=`FOLDER_ID` | `--organization`=`ORGANIZATION_ID` | `--project`=`PROJECT_ID`) [`--insight-type`=`INSIGHT_TYPE`] [`--location`=`LOCATION`] [`--[no-]recursive`] [`--filter`=`EXPRESSION`] [`--limit`=`LIMIT`] [`--page-size`=`PAGE_SIZE`] [`--sort-by`=[`FIELD`,…]] [`--uri`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` This command lists all insights for the specified Google Cloud resource, location, and insight type. If an insight type or location is not specified, insights for all supported insight types or locations, respectively, are listed. If the `--recursive` flag is set, insights for child resources and projects are also listed. Supported insight types can be found here: <https://cloud.google.com/recommender/docs/insights/insight-types>. 
EXAMPLES
     To list all insights for a billing account: 
    
    
    gcloud alpha recommender insights list --project=project-id --location=global --insight-type=google.compute.firewall.Insight

REQUIRED FLAGS
    

Resource that is associated with cloud entity type. Currently four mutually exclusive flags are supported, --project, --billing-account, --folder, \--organization. 

Exactly one of these must be specified: 

`--billing-account`=`BILLING_ACCOUNT`
     The Google Cloud Platform billing account ID to use for this invocation. 
`--folder`=`FOLDER_ID`
     The Google Cloud Platform folder ID to use for this invocation. 
`--organization`=`ORGANIZATION_ID`
     The Google Cloud Platform organization ID to use for this invocation. 
`--project`=`PROJECT_ID`
     The Google Cloud Platform project ID. Overrides the default `core/project` property value for this command invocation. 
FLAGS
    

`--insight-type`=`INSIGHT_TYPE`
     Insight type to list insights for. If no insight type is specified, insights for all supported insight types are listed. Supported insight types can be found here: <https://cloud.google.com/recommender/docs/insights/insight-types> Not specifying an insight-type can add a minute to the runtime. 
`--location`=`LOCATION`
     Location to list insights for. If no location is specified, insights for all supported locations are listed. Not specifying a location can add 15-20 seconds to the runtime. 
`--[no-]recursive`
     In addition to listing the insights for the specified organization or folder, recursively list all of the insights for the resource's child resources, including their descendants (for example, a folder's sub-folders), and for the resource's child projects. For example, when using the `--recursive` flag and specifying an organization, the response lists all of the insights associated with that organization, all of the insights associated with that organization's folders and sub-folders, and all of the insights associated with that organization's child projects. The maximum number of resources (organization, folders, projects, and descendant resources) that can be accessed at once with the `--recursive` flag is 100. For a larger number of nested resources, use [BigQuery export](https://cloud.google.com/recommender/docs/bq-export/export-recommendations-to-bq). Using `--recursive` can add 15-20 seconds per resource to the runtime. Use `--recursive` to enable and `--no-recursive` to disable. 
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
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud recommender insights list](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/insights/list)
    
    
    [gcloud beta recommender insights list](https://docs.cloud.google.com/sdk/gcloud/reference/beta/recommender/insights/list)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
