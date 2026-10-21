---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/design-center/spaces/application-templates/revisions/generate/
title: gcloud alpha design-center spaces application-templates revisions generate \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:20:45.754651+00:00
---

# gcloud alpha design-center spaces application-templates revisions generate  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/design-center/spaces/application-templates/revisions/generate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha design-center spaces application-templates revisions generate Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha design-center spaces application-templates revisions generate - generate IaC for an application template revision 
SYNOPSIS
    

`gcloud alpha design-center spaces application-templates revisions generate` (`REVISION` : `--application-template`=`APPLICATION_TEMPLATE` `--space`=`SPACE`) [`--iac-format`=`IAC_FORMAT`] [`--location`=`LOCATION`] [`--artifact-location-gcs-uri`=`ARTIFACT_LOCATION_GCS_URI` | [`--developer-connect-export-config-dir`=`DEVELOPER_CONNECT_EXPORT_CONFIG_DIR` (`--developer-connect-export-config-repo-uri`=`DEVELOPER_CONNECT_EXPORT_CONFIG_REPO_URI` : `--connection`=`CONNECTION`) : `--developer-connect-export-config-branch`=`DEVELOPER_CONNECT_EXPORT_CONFIG_BRANCH`]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Generates Terraform files for an application template revision. 
EXAMPLES
     To generate IaC for the application template `my-app-template` revision `my-revision` in space `my-space`, project `my-project` and location `us-central1`, run: 
    
    
    [gcloud alpha design-center spaces application-templates](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/design-center/spaces/application-templates) revisions generate my-revision --application-template=my-app-template --space=my-space --project=my-project --location=us-central1

Or run: 
    
    
    [gcloud alpha design-center spaces application-templates](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/design-center/spaces/application-templates) revisions generate projects/my-project/locations/us-central1/spaces/my-space/applicationTemplates/my-app-template/revisions/my-revision

To generate IaC for the application template `my-app-template` revision `my-revision` in space `my-space`, project `my-project` and location `us-central1` and save to cloud storage bucket `my-bucket`, run: 
    
    
    [gcloud alpha design-center spaces application-templates](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/design-center/spaces/application-templates) revisions generate my-revision --application-template=my-app-template --space=my-space --project=my-project --location=us-central1 --gcs-uri=gs://my-bucket

POSITIONAL ARGUMENTS
    

Revision resource - The name of the application template revision. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `revision` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `revision` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 



This must be specified. 

`REVISION`
     ID of the revision or fully qualified identifier for the revision. 

To set the `revision` attribute: 

  * provide the argument `revision` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--application-template`=`APPLICATION_TEMPLATE`
     The applicationTemplate id of the revision resource. 

To set the `application-template` attribute: 

  * provide the argument `revision` on the command line with a fully specified name; 
  * provide the argument `--application-template` on the command line. 


`--space`=`SPACE`
     The space id of the revision resource. 

To set the `space` attribute: 

  * provide the argument `revision` on the command line with a fully specified name; 
  * provide the argument `--space` on the command line. 


FLAGS
    

`--iac-format`=`IAC_FORMAT`
     The IaC format to generate. `IAC_FORMAT` must be one of: 

`helm`
     IaC format is HELM. 
`terraform`
     IaC format is Terraform. 
`--location`=`LOCATION`
     For resources [revision, developer-connect-export-config-repo-uri], provides fallback value for resource location attribute. When the resource's full URI path is not provided, location will fallback to this flag value. 
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
     This command uses the `designcenter/v1alpha` API. The full documentation for this API can be found at: <http://cloud.google.com/application-design-center/docs>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud design-center spaces application-templates revisions](https://docs.cloud.google.com/sdk/gcloud/reference/design-center/spaces/application-templates/revisions) generate

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-09 UTC."],[],[]] 
