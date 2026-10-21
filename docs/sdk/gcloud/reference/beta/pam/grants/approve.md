---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/pam/grants/approve/
title: gcloud beta pam grants approve \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:04:03.485274+00:00
---

# gcloud beta pam grants approve  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/pam/grants/approve/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta pam grants approve Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta pam grants approve - approve a Privileged Access Manager grant 
SYNOPSIS
    

`gcloud beta pam grants approve` (`GRANT` : `--entitlement`=`ENTITLEMENT` `--folder`=`FOLDER` `--location`=`LOCATION` `--organization`=`ORGANIZATION`) [`--reason`=`REASON`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Approve a Privileged Access Manager (PAM) grant with a reason. 
EXAMPLES
     The following command approves a grant with the full name ``GRANT_NAME`` and a reason of `approval reason`: 
    
    
    gcloud beta pam grants approve GRANT_NAME --reason="approval reason"

POSITIONAL ARGUMENTS
    

Grant resource - Name of the grant to approve. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `grant` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. This resource can be one of the following types: [privilegedaccessmanager.projects.locations.entitlements.grants, privilegedaccessmanager.folders.locations.entitlements.grants, privilegedaccessmanager.organizations.locations.entitlements.grants]. 



This must be specified. 

`GRANT`
     ID of the grant or fully qualified identifier for the grant. 

To set the `grant` attribute: 

  * provide the argument `grant` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--entitlement`=`ENTITLEMENT`
     The entitlement id 

To set the `entitlement` attribute: 

  * provide the argument `grant` on the command line with a fully specified name; 
  * provide the argument `--entitlement` on the command line. 


`--folder`=`FOLDER`
     The name of the folder 

To set the `folder` attribute: 

  * provide the argument `grant` on the command line with a fully specified name; 
  * provide the argument `--folder` on the command line. Must be specified for resource of type [privilegedaccessmanager.folders.locations.entitlements.grants]. 


`--location`=`LOCATION`
     The resource location 

To set the `location` attribute: 

  * provide the argument `grant` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


`--organization`=`ORGANIZATION`
     The name of the organization 

To set the `organization` attribute: 

  * provide the argument `grant` on the command line with a fully specified name; 
  * provide the argument `--organization` on the command line. Must be specified for resource of type [privilegedaccessmanager.organizations.locations.entitlements.grants]. 


FLAGS
    

`--reason`=`REASON`
     Reason for approving the grant. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `privilegedaccessmanager/v1beta` API. The full documentation for this API can be found at: <https://cloud.google.com/iam/docs/pam-overview>
NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud pam grants approve](https://docs.cloud.google.com/sdk/gcloud/reference/pam/grants/approve)
    
    
    [gcloud alpha pam grants approve](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pam/grants/approve)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
