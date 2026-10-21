---
url: https://docs.cloud.google.com/sdk/gcloud/reference/design-center/spaces/application-templates/generate/
title: gcloud design-center spaces application-templates generate \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:20:51.967406+00:00
---

# gcloud design-center spaces application-templates generate  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/design-center/spaces/application-templates/generate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud design-center spaces application-templates generate Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud design-center spaces application-templates generate - generate IaC for an application template 
SYNOPSIS
    

`gcloud design-center spaces application-templates generate` (`APPLICATION_TEMPLATE` : `--space`=`SPACE`) [`--gcs-uri`=`GCS_URI`] [`--iac-format`=`IAC_FORMAT`] [`--location`=`LOCATION`] [`--artifact-location-gcs-uri`=`ARTIFACT_LOCATION_GCS_URI` | [`--developer-connect-export-config-dir`=`DEVELOPER_CONNECT_EXPORT_CONFIG_DIR` (`--developer-connect-export-config-repo-uri`=`DEVELOPER_CONNECT_EXPORT_CONFIG_REPO_URI` : `--connection`=`CONNECTION`) : `--developer-connect-export-config-branch`=`DEVELOPER_CONNECT_EXPORT_CONFIG_BRANCH`]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Generates Terraform files for an application template. 
EXAMPLES
     To generate IaC for the application template `my-app-template` in space `my-space`, project `my-project` and location `us-central1`, run: 
    
    
    gcloud design-center spaces application-templates generate my-app-template --space=my-space --project=my-project --location=us-central1

Or run: 
    
    
    gcloud design-center spaces application-templates generate projects/my-project/locations/us-central1/spaces/my-space/applicationTemplates/my-app-template

To generate IaC for the application template `my-app-template` in space `my-space`, project `my-project` and location `us-central1` and save to cloud storage bucket `my-bucket`, run: 
    
    
    gcloud design-center spaces application-templates generate my-app-template --space=my-space --project=my-project --location=us-central1 --gcs-uri=gs://my-bucket

To generate IaC for the application template `my-app-template` in Terraform format in space `my-space`, project `my-project` and location `us-central1`, run: 
    
    
    gcloud design-center spaces application-templates generate my-app-template --space=my-space --project=my-project --location=us-central1 --iac-format=terraform

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
    

`--gcs-uri`=`GCS_URI`
     The Cloud Storage URI to write the generated IaC to. 

DEPRECATED: Use the 'artifact_location' field instead. 

`--iac-format`=`IAC_FORMAT`
     The IaC format to generate. `IAC_FORMAT` must be one of: 

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


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `designcenter/v1` API. The full documentation for this API can be found at: <http://cloud.google.com/application-design-center/docs>
NOTES
     This variant is also available: 
    
    
    [gcloud alpha design-center spaces application-templates generate](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/design-center/spaces/application-templates/generate)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-09 UTC."],[],[]] 
