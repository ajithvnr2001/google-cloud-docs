---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/artifacts/versions/list/
title: gcloud alpha artifacts versions list \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:56:38.871421+00:00
---

# gcloud alpha artifacts versions list  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/artifacts/versions/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha artifacts versions list Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha artifacts versions list - list Artifact Registry package versions 
SYNOPSIS
    

`gcloud alpha artifacts versions list` `--package`=`PACKAGE` [`--location`=`LOCATION` `--repository`=`REPOSITORY`] [`--filter`=`EXPRESSION`] [`--limit`=`LIMIT`] [`--page-size`=`PAGE_SIZE`] [`--sort-by`=[`FIELD`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` List all Artifact Registry versions in the specified package. 

To specify the maximum number of versions to list, use the --limit flag. 

EXAMPLES
     The following command lists a maximum of five packages versions: 
    
    
    gcloud alpha artifacts versions list --limit=5

To list versions of package `my_pkg` with name as `1.0-SNAPSHOT`: 
    
    
    gcloud alpha artifacts versions list --package=my_pkg --filter='name="projects/my-project/locations/us/repositories/my-repo/packages/my_pkg/versions/1.0-SNAPSHOT"'

To list versions of package `my_pkg` with a given partial name, use `*` to match any character in name: 
    
    
    gcloud alpha artifacts versions list --package=my_pkg --filter='name="projects/my-project/locations/us/repositories/my-repo/packages/my_pkg/versions/1.0*"'
    
    
    gcloud alpha artifacts versions list --package=my_pkg --filter='name="projects/my-project/locations/us/repositories/my-repo/packages/my_pkg/versions/*SNAPSHOT"'

To list versions of package `my_pkg` that have annotations: 
    
    
    gcloud alpha artifacts versions list --package=my_pkg --filter=annotations:*

To list versions of package `my_pkg` with annotations pair as [annotation_key: annotation_value]: 
    
    
    gcloud alpha artifacts versions list --package=my_pkg --filter='annotations.annotation_key:annotation_value'

To list versions of package `my_pkg` with annotations containing key as `my_key`: 
    
    
    gcloud alpha artifacts versions list --package=my_pkg --filter=annotations.my_key
    
    
    If the key or value contains special characters, such as `my.key` and `my.value`, backtick("`") is required:
    
    
    gcloud alpha artifacts versions list --filter='annotations.`my.key`'
    
    
    gcloud alpha artifacts versions list --filter='annotations.`my.key`:`my.value`'

To list versions of package `my_pkg` with given partial annotation key or value, use `*` to match any character: 
    
    
    gcloud alpha artifacts versions list --filter='annotations.*key:`*.value`'

To list versions of package `my_pkg` ordered by create_time: 
    
    
    gcloud alpha artifacts versions list --package=my_pkg --sort-by=create_time

To list versions of package `my_pkg` ordered by update_time reversely: 
    
    
    gcloud alpha artifacts versions list --package=my_pkg --sort-by=~update_time

REQUIRED FLAGS
    

`--package`=`PACKAGE`
     List all versions in a specified artifact, such as a container image or a language package. 
FLAGS
    

Repository resource - The Artifact Registry repository. If not specified, the current artifacts/repository is used. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--repository` on the command line with a fully specified name; 
  * set the property `artifacts/repository` with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 


`--location`=`LOCATION`
     Location of the repository. 

To set the `location` attribute: 

  * provide the argument `--repository` on the command line with a fully specified name; 
  * set the property `artifacts/repository` with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `artifacts/location`. 


`--repository`=`REPOSITORY`
     ID of the repository or fully qualified identifier for the repository. 

To set the `repository` attribute: 

  * provide the argument `--repository` on the command line; 
  * set the property `artifacts/repository`. 


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
    
    
    [gcloud artifacts versions list](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/versions/list)
    
    
    [gcloud beta artifacts versions list](https://docs.cloud.google.com/sdk/gcloud/reference/beta/artifacts/versions/list)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
