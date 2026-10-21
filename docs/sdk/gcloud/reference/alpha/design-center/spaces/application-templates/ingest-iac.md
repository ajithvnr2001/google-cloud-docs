---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/design-center/spaces/application-templates/ingest-iac/
title: gcloud alpha design-center spaces application-templates ingest-iac \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:20:44.501705+00:00
---

# gcloud alpha design-center spaces application-templates ingest-iac  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/design-center/spaces/application-templates/ingest-iac/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha design-center spaces application-templates ingest-iac Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha design-center spaces application-templates ingest-iac - ingest Infrastructure as Code (IaC) for an application template 
SYNOPSIS
    

`gcloud alpha design-center spaces application-templates ingest-iac` (`APPLICATION_TEMPLATE` : `--location`=`LOCATION` `--space`=`SPACE`) (`--gcs-uri`=`GCS_URI` | `--iac-module-from-file`=`PATH_TO_FILE` | `--developer-connect-dir`=`DEVELOPER_CONNECT_DIR` `--developer-connect-repo-uri`=`DEVELOPER_CONNECT_REPO_URI` (`--developer-connect-branch`=`DEVELOPER_CONNECT_BRANCH` | `--developer-connect-commit-sha`=`DEVELOPER_CONNECT_COMMIT_SHA` | `--developer-connect-ref-tag`=`DEVELOPER_CONNECT_REF_TAG`) | [`--git-source-ref-tag`=`GIT_SOURCE_REF_TAG` `--git-source-repo`=`GIT_SOURCE_REPO` : `--git-source-dir`=`GIT_SOURCE_DIR`]) [`--async`] [`--raw-terraform-import-enabled`] [`--validate-catalog-compatibility`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Ingest Infrastructure as Code (IaC) for a Design Center application template from a Cloud Storage bucket, a local IaC module file, a Developer Connect repository, or a public Git repository. 
EXAMPLES
     To ingest IaC from a Cloud Storage URI into the application template `my-template` in space `my-space` and location `us-central1`, run: 
    
    
    [gcloud alpha design-center spaces application-templates](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/design-center/spaces/application-templates) ingest-iac my-template --space=my-space --location=us-central1 --gcs-uri=gs://my-bucket/iac

To ingest IaC from a local YAML file named `iac_module.yaml` as raw Terraform, run: 
    
    
    [gcloud alpha design-center spaces application-templates](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/design-center/spaces/application-templates) ingest-iac my-template --space=my-space --location=us-central1 --iac-module-from-file=iac_module.yaml --raw-terraform-import-enabled

To ingest IaC from the `main` branch of a Developer Connect repository, run: 
    
    
    [gcloud alpha design-center spaces application-templates](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/design-center/spaces/application-templates) ingest-iac my-template --space=my-space --location=us-central1 --developer-connect-repo-uri=projects/my-project/locations/us-central1/connections/my-connection/gitRepositoryLinks/my-repo --developer-connect-dir=infra --developer-connect-branch=main

To return immediately without waiting for the operation to complete, run: 
    
    
    [gcloud alpha design-center spaces application-templates](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/design-center/spaces/application-templates) ingest-iac my-template --space=my-space --location=us-central1 --gcs-uri=gs://my-bucket/iac --async

POSITIONAL ARGUMENTS
    

Application template resource - The application template into which to ingest IaC. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `APPLICATION_TEMPLATE` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`APPLICATION_TEMPLATE`
     ID of the application_template or fully qualified identifier for the application_template. 

To set the `application_template_id` attribute: 

  * provide the argument `APPLICATION_TEMPLATE` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The Cloud location for the application_template. 

To set the `location` attribute: 

  * provide the argument `APPLICATION_TEMPLATE` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


`--space`=`SPACE`
     The ID of the space. 

To set the `space` attribute: 

  * provide the argument `APPLICATION_TEMPLATE` on the command line with a fully specified name; 
  * provide the argument `--space` on the command line. 


REQUIRED FLAGS
    

The source of the IaC to ingest. 

Exactly one of these must be specified: 

`--gcs-uri`=`GCS_URI`
     The Cloud Storage URI of the Terraform code (e.g., gs://my-bucket/iac). 
`--iac-module-from-file`=`PATH_TO_FILE`
     Path to a local YAML or JSON file containing the IaC module definition. Use a full or relative path to a local file containing the value of iac_module. 
Or at least one of these can be specified: 

Ingest IaC from a Git repository linked through Developer Connect. 
`--developer-connect-dir`=`DEVELOPER_CONNECT_DIR`
     The directory, relative to the repository root, to read the IaC from (e.g., `dir1/dir2`). Use `/` for the repository root. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--developer-connect-repo-uri`=`DEVELOPER_CONNECT_REPO_URI`
     The Developer Connect Git repository link, formatted as `projects/{project}/locations/{location}/connections/{connection}/gitRepositoryLinks/{gitRepositoryLink}`. 

This flag argument must be specified if any of the other arguments in this group are specified. 

The Git reference to read the IaC from. 

Exactly one of these must be specified: 

`--developer-connect-branch`=`DEVELOPER_CONNECT_BRANCH`
     The branch to read the IaC from (e.g., `main`). 
`--developer-connect-commit-sha`=`DEVELOPER_CONNECT_COMMIT_SHA`
     The full SHA of the commit to read the IaC from. 
`--developer-connect-ref-tag`=`DEVELOPER_CONNECT_REF_TAG`
     The tag to read the IaC from (e.g., `v1.2.3`). 
Or at least one of these can be specified: 

Ingest IaC from a public Git repository. 
`--git-source-ref-tag`=`GIT_SOURCE_REF_TAG`
     The Git reference tag to read the IaC from. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--git-source-repo`=`GIT_SOURCE_REPO`
     The HTTPS URL of the public Git repository (e.g., `https://github.com/my-org/my-repo`). 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--git-source-dir`=`GIT_SOURCE_DIR`
     The directory, relative to the repository root, to read from. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--raw-terraform-import-enabled`
     If set, ingest the IaC as raw Terraform without converting it to application template components. 
`--validate-catalog-compatibility`
     If set, validate that the IaC is compatible with the catalog. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
