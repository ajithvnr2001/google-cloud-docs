---
url: https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/conversion-workspaces/describe-ddls/
title: gcloud database-migration conversion-workspaces describe-ddls \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:40:49.512720+00:00
---

# gcloud database-migration conversion-workspaces describe-ddls  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/conversion-workspaces/describe-ddls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud database-migration conversion-workspaces describe-ddls Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud database-migration conversion-workspaces describe-ddls - describe DDLs in a Database Migration Service conversion workspace 
SYNOPSIS
    

`gcloud database-migration conversion-workspaces describe-ddls` (`CONVERSION_WORKSPACE` : `--region`=`REGION`) [`--commit-id`=`COMMIT_ID`] [`--endpoint-mode`=`ENDPOINT_MODE`] [`--tree-type`=`TREE_TYPE`; default="DRAFT"] [`--uncommitted`] [`--filter`=`EXPRESSION`] [`--limit`=`LIMIT`] [`--page-size`=`PAGE_SIZE`; default=100] [`--sort-by`=[`FIELD`,…]] [`--uri`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Describe DDLs in a Database Migration Service conversion workspace. 
EXAMPLES
     To describe the DDLs of the draft tree in my-conversion-workspace in a project and location `us-central1`, run: 
    
    
    gcloud database-migration conversion-workspaces describe-ddls my-conversion-workspace --region=us-central1

To describe the DDLs of the source tree in a conversion workspace in a project and location `us-central1`, run: 
    
    
    gcloud database-migration conversion-workspaces describe-ddls my-conversion-workspace --region=us-central1 --tree-type=SOURCE

POSITIONAL ARGUMENTS
    

Conversion workspace resource - The conversion workspace to describe DDLs. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `conversion_workspace` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`CONVERSION_WORKSPACE`
     ID of the conversion_workspace or fully qualified identifier for the conversion_workspace. 

To set the `conversion_workspace` attribute: 

  * provide the argument `conversion_workspace` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--region`=`REGION`
     The Cloud region for the conversion_workspace. 

To set the `region` attribute: 

  * provide the argument `conversion_workspace` on the command line with a fully specified name; 
  * provide the argument `--region` on the command line. 


FLAGS
    

`--commit-id`=`COMMIT_ID`
     Request a specific commit id. If not specified, the entities from the latest commit are returned. 
`--endpoint-mode`=`ENDPOINT_MODE`
     Specifies endpoint mode for a given command. Regional endpoints provide enhanced data residency and reliability by ensuring your request is handled entirely within the specified Google Cloud region. This differs from global endpoints, which may process parts of the request outside the target region. Overrides the default `regional/endpoint_mode` property value for this command invocation. `ENDPOINT_MODE` must be one of: 

`global`
     (Default) Use global rather than regional endpoints. 
`regional`
     Only use regional endpoints. An error will be raised if a regional endpoint is not available for a given command. 
`regional-preferred`
     Use regional endpoints when available, otherwise use global endpoints. Recommended for most users. 
`--tree-type`=`TREE_TYPE`; default="DRAFT"
     Tree type for database entities. `TREE_TYPE` must be one of: `SOURCE`, `DRAFT`. 
`--uncommitted`
     Whether to retrieve the latest committed version of the entities or the latest version. This field is ignored if a specific commit_id is specified. 
LIST COMMAND FLAGS
    

`--filter`=`EXPRESSION`
     Apply a Boolean filter `EXPRESSION` to each resource item to be listed. If the expression evaluates `True`, then that item is listed. For more details and examples of filter expressions, run $ [gcloud topic filters](https://docs.cloud.google.com/sdk/gcloud/reference/topic/filters). This flag interacts with other flags that are applied in this order: `--flatten`, `--sort-by`, `--filter`, `--limit`. 
`--limit`=`LIMIT`
     Maximum number of resources to list. The default is `unlimited`. This flag interacts with other flags that are applied in this order: `--flatten`, `--sort-by`, `--filter`, `--limit`. 
`--page-size`=`PAGE_SIZE`; default=100
     Some services group resource list output into pages. This flag specifies the maximum number of resources per page. The default is `100`. Paging may be applied before or after `--filter` and `--limit` depending on the service. 
`--sort-by`=[`FIELD`,…]
     Comma-separated list of resource field key names to sort by. The default order is ascending. Prefix a field with ``~´´ for descending order on that field. This flag interacts with other flags that are applied in this order: `--flatten`, `--sort-by`, `--filter`, `--limit`. 
`--uri`
     Print a list of resource URIs instead of the default output, and change the command output to a list of URIs. If this flag is used with `--format`, the formatting is applied on this URI list. To display URIs alongside other keys instead, use the `uri()` transform. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

REGIONAL ENDPOINTS
     This command supports regional endpoints. To use regional endpoints for this command, use the `--endpoint-mode=regional-preferred` flag. To use regional endpoints by default, run `$ [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) regional/endpoint_mode regional-preferred`. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-23 UTC."],[],[]] 
