---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/pam/entitlements/export/
title: gcloud beta pam entitlements export \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:04:03.774678+00:00
---

# gcloud beta pam entitlements export  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/pam/entitlements/export/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta pam entitlements export Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta pam entitlements export - export a Privileged Access Manager entitlement into a local YAML file 
SYNOPSIS
    

`gcloud beta pam entitlements export` (`ENTITLEMENT` : `--folder`=`FOLDER` `--location`=`LOCATION` `--organization`=`ORGANIZATION`) [`--destination`=`DESTINATION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Export a Privileged Access Manager (PAM) entitlement into a local YAML file. 
EXAMPLES
     The following command exports an entitlement with a name of `sample-entitlement`, in a project named `sample-project`, and in location `global` to a local YAML file named `sample-entitlement.yaml`: 
    
    
    gcloud beta pam entitlements export sample-entitlement --project=sample-project --location=global --destination=sample-entitlement.yaml

The following command exports an entitlement with a name of `sample-entitlement`, in a folder with ID ``FOLDER_ID``, and in location `global` to a local YAML file named `sample-entitlement.yaml`: 
    
    
    gcloud beta pam entitlements export sample-entitlement --folder=FOLDER_ID --location=global --destination=sample-entitlement.yaml

The following command exports an entitlement with a name of `sample-entitlement`, in an organization with ID ``ORGANIZATION_ID``, and in location `global` to a local YAML file named `sample-entitlement.yaml`: 
    
    
    gcloud beta pam entitlements export sample-entitlement --organization=ORGANIZATION_ID --location=global --destination=sample-entitlement.yaml

POSITIONAL ARGUMENTS
    

Entitlement resource - Name of the entitlement to export. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `entitlement` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. This resource can be one of the following types: [privilegedaccessmanager.projects.locations.entitlements, privilegedaccessmanager.folders.locations.entitlements, privilegedaccessmanager.organizations.locations.entitlements]. 



This must be specified. 

`ENTITLEMENT`
     ID of the entitlement or fully qualified identifier for the entitlement. 

To set the `entitlement` attribute: 

  * provide the argument `entitlement` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--folder`=`FOLDER`
     The name of the folder 

To set the `folder` attribute: 

  * provide the argument `entitlement` on the command line with a fully specified name; 
  * provide the argument `--folder` on the command line. Must be specified for resource of type [privilegedaccessmanager.folders.locations.entitlements]. 


`--location`=`LOCATION`
     The resource location 

To set the `location` attribute: 

  * provide the argument `entitlement` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


`--organization`=`ORGANIZATION`
     The name of the organization 

To set the `organization` attribute: 

  * provide the argument `entitlement` on the command line with a fully specified name; 
  * provide the argument `--organization` on the command line. Must be specified for resource of type [privilegedaccessmanager.organizations.locations.entitlements]. 


FLAGS
    

`--destination`=`DESTINATION`
     Path to a YAML file where the configuration will be exported. The exported data will not contain any output-only fields. Alternatively, you may omit this flag to write to standard output. For a schema describing the export/import format, see $CLOUDSDKROOT/lib/googlecloudsdk/schemas/… 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `privilegedaccessmanager/v1beta` API. The full documentation for this API can be found at: <https://cloud.google.com/iam/docs/pam-overview>
NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud pam entitlements export](https://docs.cloud.google.com/sdk/gcloud/reference/pam/entitlements/export)
    
    
    [gcloud alpha pam entitlements export](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pam/entitlements/export)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
