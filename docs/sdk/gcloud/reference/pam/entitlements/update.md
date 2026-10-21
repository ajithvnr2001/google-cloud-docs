---
url: https://docs.cloud.google.com/sdk/gcloud/reference/pam/entitlements/update/
title: gcloud pam entitlements update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:28:32.479975+00:00
---

# gcloud pam entitlements update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/pam/entitlements/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud pam entitlements update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud pam entitlements update - update an existing Privileged Access Manager entitlement 
SYNOPSIS
    

`gcloud pam entitlements update` (`ENTITLEMENT` : `--folder`=`FOLDER` `--location`=`LOCATION` `--organization`=`ORGANIZATION`) `--entitlement-file`=`PATH_TO_FILE` [`--async`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Update an existing Privileged Access Manager (PAM) entitlement. 
EXAMPLES
     The following command updates an entitlement with a name of `sample-entitlement`, in a project named `sample-project`, in location `global`, and the new entitlement configuration stored in a file named `sample-entitlement.yaml`: 
    
    
    gcloud pam entitlements update sample-entitlement --project=sample-project --location=global --entitlement-file=sample-entitlement.yaml

The following command updates an entitlement with a name of `sample-entitlement`, in a folder with ID ``FOLDER_ID``, in location `global`, and the new entitlement configuration stored in a file named `sample-entitlement.yaml`: 
    
    
    gcloud pam entitlements update sample-entitlement --folder=FOLDER_ID --location=global --entitlement-file=sample-entitlement.yaml

The following command updates an entitlement with a name of `sample-entitlement`, in an organization with ID ``ORGANIZATION_ID``, in location `global`, and the new entitlement configuration stored in a file named `sample-entitlement.yaml`: 
    
    
    gcloud pam entitlements update sample-entitlement --organization=ORGANIZATION_ID --location=global --entitlement-file=sample-entitlement.yaml

POSITIONAL ARGUMENTS
    

Entitlement resource - Name of the entitlement to update. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

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


REQUIRED FLAGS
    

`--entitlement-file`=`PATH_TO_FILE`
     YAML file containing the new configuration of the entitlement. Use a full or relative path to a local file containing the value of entitlement_file. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `privilegedaccessmanager/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/iam/docs/pam-overview>
NOTES
     These variants are also available: 
    
    
    [gcloud alpha pam entitlements update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pam/entitlements/update)
    
    
    [gcloud beta pam entitlements update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/pam/entitlements/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
