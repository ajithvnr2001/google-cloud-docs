---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/artifacts/files/list/
title: gcloud beta artifacts files list \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:29:02.498109+00:00
---

# gcloud beta artifacts files list  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/artifacts/files/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta artifacts files list Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta artifacts files list - list Artifact Registry files 
SYNOPSIS
    

`gcloud beta artifacts files list` [`--package`=`PACKAGE`] [`--tag`=`TAG`] [`--version`=`VERSION`] [`--location`=`LOCATION` `--repository`=`REPOSITORY`] [`--filter`=`EXPRESSION`] [`--limit`=`LIMIT`] [`--page-size`=`PAGE_SIZE`] [`--sort-by`=[`FIELD`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` List all Artifact Registry files in the specified repository and location. 

To specify the maximum number of files to list, use the --limit flag. 

EXAMPLES
     To list files in the current project under repository `my-repo` in `us`: 
    
    
    gcloud beta artifacts files list --repository=my-repo --location=us

The following command lists a maximum of five files: 
    
    
    gcloud beta artifacts files list --repository=my-repo --location=us --limit=5

To list files in the current project under repository `my-repo` in `us` owned by package `my-package`: 
    
    
    gcloud beta artifacts files list --repository=my-repo --location=us --package=my-package

To list files in the current project under repository `my-repo` in `us` owned by package `my-package` and version `1.0.0`: 
    
    
    gcloud beta artifacts files list --repository=my-repo --location=us --package=my-package --version=1.0.0

To list files in the current project under repository `my-repo` in `us` owned by package `my-package` and tag name `my-tag`: 
    
    
    gcloud beta artifacts files list --repository=my-repo --location=us --package=my-package --tag=my-tag

To list files with name as `my-file`: 
    
    
    gcloud beta artifacts files list --filter='name="projects/my-project/locations/us/repositories/my-repo/files/my-file"'

To list files with a given partial name, use `*` to match any character in name: 
    
    
    gcloud beta artifacts files list --filter='name="projects/my-project/locations/us/repositories/my-repo/files/*file"'
    
    
    gcloud beta artifacts files list --filter='name="projects/my-project/locations/us/repositories/my-repo/files/my-*"'

To list files that have annotations: 
    
    
    gcloud beta artifacts files list --filter=annotations:*

To list files with annotations pair as [annotation_key: annotation_value] 
    
    
    gcloud beta artifacts files list --filter='annotations.annotation_key:annotation_value'

To list files with annotations containing key as `my_key`: 
    
    
    gcloud beta artifacts files list --filter='annotations.my_key'
    
    
    If the key or value contains special characters, such as `my.key` and `my.value`, backtick("`") is required:
    
    
    gcloud beta artifacts files list --filter='annotations.`my.key`'
    
    
    gcloud beta artifacts files list --filter='annotations.`my.key`:`my.value`'

To list files with given partial annotation key or value, use `*` to match any character: 
    
    
    gcloud beta artifacts files list --filter='annotations.*key:`*.value`'

To list files in the current project under repository `my-repo` in `us`, ordering by create_time: 
    
    
    gcloud beta artifacts files list --repository=my-repo --location=us --sort-by=create_time

To list files in the current project under repository `my-repo` in `us`, ordering by update_time reversely: 
    
    
    gcloud beta artifacts files list --repository=my-repo --location=us --sort-by=~update_time

FLAGS
    

`--package`=`PACKAGE`
     List all files in a specified artifact, such as a container image or a language package. If you do not use --tag or --version in the command, the command lists files in all versions of the artifact. 
`--tag`=`TAG`
     List all files in the artifact version with the specified tag. This flag only works with formats that use tags, such as container images. Use the --package flag to specify the artifact. 
`--version`=`VERSION`
     List all files in the specified artifact version. Use the --package flag to specify the artifact. 
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
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud artifacts files list](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/files/list)
    
    
    [gcloud alpha artifacts files list](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/artifacts/files/list)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
