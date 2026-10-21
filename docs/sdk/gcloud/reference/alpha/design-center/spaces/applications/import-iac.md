---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/design-center/spaces/applications/import-iac/
title: gcloud alpha design-center spaces applications import-iac \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:19:19.262859+00:00
---

# gcloud alpha design-center spaces applications import-iac  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/design-center/spaces/applications/import-iac/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha design-center spaces applications import-iac Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha design-center spaces applications import-iac - import Infrastructure as Code (IaC) for an Application 
SYNOPSIS
    

`gcloud alpha design-center spaces applications import-iac` (`APPLICATION` : `--location`=`LOCATION` `--space`=`SPACE`) (`--gcs-uri`=`GCS_URI` | `--iac-module-from-file`=`PATH_TO_FILE`) [`--allow-partial-import`] [`--validate-iac`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Import Infrastructure as Code (IaC) for a Design Center Application. 
EXAMPLES
     To import IaC from a Google Cloud Storage URI into the application `my-app` in space `dev-space` and location `us-central1`, run: 
    
    
    gcloud alpha design-center spaces applications import-iac my-app --location=us-central1 --space=dev-space --gcs-uri=gs://my-bucket/iac

To import IaC from a local YAML file named `iac_module.yaml` into the application `my-app` in space `dev-space` and location `us-central1`, run: 
    
    
    gcloud alpha design-center spaces applications import-iac my-app --location=us-central1 --space=dev-space --iac-module-from-file=iac_module.yaml

To import IaC from a Google Cloud Storage URI into the application `my-app`, allowing partial imports of valid edits, run: 
    
    
    gcloud alpha design-center spaces applications import-iac my-app --location=us-central1 --space=dev-space --gcs-uri=gs://my-bucket/iac --allow-partial-import

To import IaC from a local YAML file into the application `my-app`, allowing partial imports of valid edits, run: 
    
    
    gcloud alpha design-center spaces applications import-iac my-app --location=us-central1 --space=dev-space --iac-module-from-file=iac_module.yaml --allow-partial-import

To validate IaC from a Google Cloud Storage URI for the application `my-app` without importing, run: 
    
    
    gcloud alpha design-center spaces applications import-iac my-app --location=us-central1 --space=dev-space --gcs-uri=gs://my-bucket/iac --validate-iac

To validate IaC from a local YAML file for the application `my-app` without importing, run: 
    
    
    gcloud alpha design-center spaces applications import-iac my-app --location=us-central1 --space=dev-space --iac-module-from-file=iac_module.yaml --validate-iac

To validate IaC from a Google Cloud Storage URI for the application `my-app` and indicate that a future import should allow partial success, run: 
    
    
    gcloud alpha design-center spaces applications import-iac my-app --location=us-central1 --space=dev-space --gcs-uri=gs://my-bucket/iac --validate-iac --allow-partial-import

To validate IaC from a local YAML file for the application `my-app` and indicate that a future import should allow partial success, run: 
    
    
    gcloud alpha design-center spaces applications import-iac my-app --location=us-central1 --space=dev-space --iac-module-from-file=iac_module.yaml --validate-iac --allow-partial-import

POSITIONAL ARGUMENTS
    

Application resource - The application to import IaC into IaC. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `APPLICATION` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`APPLICATION`
     ID of the application or fully qualified identifier for the application. 

To set the `application` attribute: 

  * provide the argument `APPLICATION` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The Cloud location for the application. 

To set the `location` attribute: 

  * provide the argument `APPLICATION` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


`--space`=`SPACE`
     The ID of the space. 

To set the `space` attribute: 

  * provide the argument `APPLICATION` on the command line with a fully specified name; 
  * provide the argument `--space` on the command line. 


REQUIRED FLAGS
    

Exactly one of these must be specified: 

`--gcs-uri`=`GCS_URI`
     The Cloud Storage URI of the Terraform code (e.g., gs://my-bucket/iac). 
`--iac-module-from-file`=`PATH_TO_FILE`
     Path to a local YAML or JSON file containing the IaC module definition. Use a full or relative path to a local file containing the value of iac_module. 
OPTIONAL FLAGS
    

`--allow-partial-import`
     If set, partially import valid IaC changes and ignore invalid ones. 
`--validate-iac`
     Validate the IaC without performing the import. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the designcenter/v1alpha API. The full documentation for this API can be found at: <http://cloud.google.com/application-design-center/docs>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud design-center spaces applications import-iac](https://docs.cloud.google.com/sdk/gcloud/reference/design-center/spaces/applications/import-iac)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
