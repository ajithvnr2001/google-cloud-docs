---
url: https://docs.cloud.google.com/sdk/gcloud/reference/source-manager/repos/create/
title: gcloud source-manager repos create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:25:04.612373+00:00
---

# gcloud source-manager repos create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/source-manager/repos/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud source-manager repos create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud source-manager repos create - create a Secure Source Manager repository 
SYNOPSIS
    

`gcloud source-manager repos create` (`REPOSITORY` : `--region`=`REGION`) `--instance`=`INSTANCE` [`--description`=`DESCRIPTION`] [`--endpoint-mode`=`ENDPOINT_MODE`] [`--service-account`=`SERVICE_ACCOUNT`] [`--default-branch`=`DEFAULT_BRANCH` `--gitignores`=[`GITIGNORES`,…] `--license`=`LICENSE` `--readme`=`README`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Create a Secure Source Manager repository. 
EXAMPLES
     To create a repository called 'my-repo' in location 'us-central1' in instance 'my-instance', run the following command: 
    
    
    gcloud source-manager repos create my-repo --region=us-central1 --instance=my-instance

POSITIONAL ARGUMENTS
    

Repository resource - The Secure Source Manager repository to create. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `repository` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`REPOSITORY`
     ID of the repository or fully qualified identifier for the repository. 

To set the `repository` attribute: 

  * provide the argument `repository` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--region`=`REGION`
     Secure Source Manager location. 

To set the `region` attribute: 

  * provide the argument `repository` on the command line with a fully specified name; 
  * provide the argument `--region` on the command line. 


REQUIRED FLAGS
    

`--instance`=`INSTANCE`
     A Secure Source Manager instance ID. 
OPTIONAL FLAGS
    

`--description`=`DESCRIPTION`
     Description of the repository. Cannot exceed 500 characters. 
`--endpoint-mode`=`ENDPOINT_MODE`
     Specifies endpoint mode for a given command. Regional endpoints provide enhanced data residency and reliability by ensuring your request is handled entirely within the specified Google Cloud region. This differs from global endpoints, which may process parts of the request outside the target region. Overrides the default `regional/endpoint_mode` property value for this command invocation. `ENDPOINT_MODE` must be one of: 

`global`
     (Default) Use global rather than regional endpoints. 
`regional`
     Only use regional endpoints. An error will be raised if a regional endpoint is not available for a given command. 
`regional-preferred`
     Use regional endpoints when available, otherwise use global endpoints. Recommended for most users. 
`--service-account`=`SERVICE_ACCOUNT`
     The service account to attach to the repository. 
Repository initialization configuration. 
`--default-branch`=`DEFAULT_BRANCH`
     Default branch name of the repository. 
`--gitignores`=[`GITIGNORES`,…]
     List of gitignore template names user can choose from. Full list can be found here: <https://cloud.google.com/secure-source-manager/docs/reference/rest/v1/projects.locations.repositories#InitialConfig>
`--license`=`LICENSE`
     License template name user can choose from. Full list can be found here: <https://cloud.google.com/secure-source-manager/docs/reference/rest/v1/projects.locations.repositories#InitialConfig>
`--readme`=`README`
     README template name. Valid template name(s) are: default. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha source-manager repos create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/source-manager/repos/create)
    
    
    [gcloud beta source-manager repos create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/source-manager/repos/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-23 UTC."],[],[]] 
