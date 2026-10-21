---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/developer-connect/connections/git-repository-links/update/
title: gcloud beta developer-connect connections git-repository-links update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:40:57.347369+00:00
---

# gcloud beta developer-connect connections git-repository-links update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/developer-connect/connections/git-repository-links/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta developer-connect connections git-repository-links update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta developer-connect connections git-repository-links update - update a git repository link to enable metrics collection 
SYNOPSIS
    

`gcloud beta developer-connect connections git-repository-links update` (`GIT_REPOSITORY_LINK` : `--connection`=`CONNECTION` `--location`=`LOCATION`) [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Update a git repository link to enable metrics collection. 
EXAMPLES
     To update a git repository link to enable metrics collection, run: 
    
    
    [gcloud beta developer-connect connections git-repository-links](https://docs.cloud.google.com/sdk/gcloud/reference/beta/developer-connect/connections/git-repository-links) update developer-connect connections git-repository-links update <LINK> --collect-metrics

POSITIONAL ARGUMENTS
    

Git repository link resource - The git repository link to update. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `git_repository_link` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`GIT_REPOSITORY_LINK`
     ID of the git_repository_link or fully qualified identifier for the git_repository_link. 

To set the `git_repository_link` attribute: 

  * provide the argument `git_repository_link` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--connection`=`CONNECTION`
     The connection ID. 

To set the `connection` attribute: 

  * provide the argument `git_repository_link` on the command line with a fully specified name; 
  * provide the argument `--connection` on the command line. 


`--location`=`LOCATION`
     The region of the insight config. 

To set the `location` attribute: 

  * provide the argument `git_repository_link` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. This variant is also available: 
    
    
    [gcloud alpha developer-connect connections git-repository-links](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/developer-connect/connections/git-repository-links) update

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-16 UTC."],[],[]] 
