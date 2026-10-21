---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/design-center/spaces/application-templates/export/
title: gcloud alpha design-center spaces application-templates export \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:20:44.265324+00:00
---

# gcloud alpha design-center spaces application-templates export  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/design-center/spaces/application-templates/export/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha design-center spaces application-templates export Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha design-center spaces application-templates export - export IaC for an application template 
SYNOPSIS
    

`gcloud alpha design-center spaces application-templates export` (`APPLICATION_TEMPLATE` : `--space`=`SPACE`) [`--async`] [`--export-iac-config-format`=`EXPORT_IAC_CONFIG_FORMAT`] [`--location`=`LOCATION`] [`--artifact-location-gcs-uri`=`ARTIFACT_LOCATION_GCS_URI` | [`--developer-connect-export-config-dir`=`DEVELOPER_CONNECT_EXPORT_CONFIG_DIR` (`--developer-connect-export-config-repo-uri`=`DEVELOPER_CONNECT_EXPORT_CONFIG_REPO_URI` : `--connection`=`CONNECTION`) : `--developer-connect-export-config-branch`=`DEVELOPER_CONNECT_EXPORT_CONFIG_BRANCH`]] [`--tf-config-module-git-proxy-enabled` | `--tf-config-module-local-references-enabled`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Exports Terraform files for an application template, with options to configure module references (such as downloading modules locally). 
EXAMPLES
     To export the application template `my-template` in space `my-space`, project `my-project` and location `us-central1` to a Cloud Storage bucket `gs://my-bucket`, run: 
    
    
    gcloud alpha design-center spaces application-templates export my-template --space=my-space --project=my-project --location=us-central1 --artifact-location-gcs-uri=gs://my-bucket

Or run using the resource URI: 
    
    
    gcloud alpha design-center spaces application-templates export projects/my-project/locations/us-central1/spaces/my-space/applicationTemplates/my-template --artifact-location-gcs-uri=gs://my-bucket

To export the application template `my-template` to a Developer Connect repository `projects/my-project/locations/us-central1/connections/my-connection/gitRepositoryLinks/my-repo` in directory `my-dir` on branch `main`, run: 
    
    
    gcloud alpha design-center spaces application-templates export my-template --space=my-space --project=my-project --location=us-central1 --developer-connect-export-config-repo-uri=projects/my-project/locations/us-central1/connections/my-connection/gitRepositoryLinks/my-repo --developer-connect-export-config-dir=my-dir --developer-connect-export-config-branch=main

POSITIONAL ARGUMENTS
    

ApplicationTemplate resource - The name of the application template. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `application_template` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `application_template` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 



This must be specified. 

`APPLICATION_TEMPLATE`
     ID of the applicationTemplate or fully qualified identifier for the applicationTemplate. 

To set the `application_template` attribute: 

  * provide the argument `application_template` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--space`=`SPACE`
     The space id of the applicationTemplate resource. 

To set the `space` attribute: 

  * provide the argument `application_template` on the command line with a fully specified name; 
  * provide the argument `--space` on the command line. 


FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--export-iac-config-format`=`EXPORT_IAC_CONFIG_FORMAT`
     IaC format of the export. Default is [IACFormat.TERRAFORM]. `EXPORT_IAC_CONFIG_FORMAT` must be one of: 

`helm`
     IaC format is HELM. 
`terraform`
     IaC format is Terraform. 
`--location`=`LOCATION`
     For resources [application_template, developer-connect-export-config-repo-uri], provides fallback value for resource location attribute. When the resource's full URI path is not provided, location will fallback to this flag value. 
Arguments for the location. 

At most one of these can be specified: 

`--artifact-location-gcs-uri`=`ARTIFACT_LOCATION_GCS_URI`
     The Cloud Storage URI for storing the generated IaC. 
Or at least one of these can be specified: 

Through Developer Connect, defines a location where content such as Infrastructure as Code (IaC) is stored. 
`--developer-connect-export-config-dir`=`DEVELOPER_CONNECT_EXPORT_CONFIG_DIR`
     Directory, relative to the source repo, where content such as Infrastructure as Code (IaC) will be stored. This must be a relative path.To specify the root directory, use '/'. If the path or any subdirectories do not exist, they will be created. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--developer-connect-export-config-branch`=`DEVELOPER_CONNECT_EXPORT_CONFIG_BRANCH`
     The branch in repo to which the content such as Infrastructure as Code (IaC) should be written to. If empty, Application Design Center will create a branch and push the changes. 
GitRepositoryLink resource - The Developer Connect Git repository link, formatted as `projects/*/locations/*/connections/*/gitRepositoryLinks/*`. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--developer-connect-export-config-repo-uri` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `--developer-connect-export-config-repo-uri` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 



This must be specified. 

`--developer-connect-export-config-repo-uri`=`DEVELOPER_CONNECT_EXPORT_CONFIG_REPO_URI`
     ID of the gitRepositoryLink or fully qualified identifier for the gitRepositoryLink. 

To set the `git-repository-link` attribute: 

  * provide the argument `--developer-connect-export-config-repo-uri` on the command line. 



This flag argument must be specified if any of the other arguments in this group are specified. 

`--connection`=`CONNECTION`
     The connection id of the gitRepositoryLink resource. 

To set the `connection` attribute: 

  * provide the argument `--developer-connect-export-config-repo-uri` on the command line with a fully specified name; 
  * provide the argument `--connection` on the command line. 


Arguments for the config payload. 
Configuration for exporting a resource as Terraform IAC. 
Configuration on how terraform module should be handled during export. 
Arguments for the source override. 

At most one of these can be specified: 

`--tf-config-module-git-proxy-enabled`
     This is typically only valid for 3P components if ingested via devconnect URI. Typically, for 1P components, since they are sourced from public git repos, this field is not applicable. 
`--tf-config-module-local-references-enabled`
     If set, all the dependent modules will be downloaded from the target repository and referenced locally. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `designcenter/v1alpha` API. The full documentation for this API can be found at: <http://cloud.google.com/application-design-center/docs>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-26 UTC."],[],[]] 
