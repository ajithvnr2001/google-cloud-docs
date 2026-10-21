---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/pam/grants/create/
title: gcloud beta pam grants create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:04:03.687969+00:00
---

# gcloud beta pam grants create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/pam/grants/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta pam grants create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta pam grants create - create a new Privileged Access Manager grant 
SYNOPSIS
    

`gcloud beta pam grants create` `--requested-duration`=`REQUESTED_DURATION` (`--entitlement`=`ENTITLEMENT` : `--folder`=`FOLDER` `--location`=`LOCATION` `--organization`=`ORGANIZATION`) [`--additional-email-recipients`=[`ADDITIONAL_EMAIL_RECIPIENTS`,…]] [`--justification`=`JUSTIFICATION`] [`--scheduled-activation-time`=`SCHEDULED_ACTIVATION_TIME`] [`--requested-access-from-file`=[`REQUESTED_ACCESS_FROM_FILE`,…] | `--requested-resources`=[`REQUESTED_RESOURCES`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Create a new Privileged Access Manager (PAM) grant under an entitlement. 
EXAMPLES
     The following command creates a new grant against the entitlement with the full name ``ENTITLEMENT_NAME``, a requested duration of 1 hour 30 minutes, a justification of `some justification` and two additional email recipients `abc@example.com` and `xyz@example.com`: 
    
    
    gcloud beta pam grants create --entitlement=ENTITLEMENT_NAME --requested-duration=5400s --justification="some justification" --additional-email-recipients=abc@example.com,xyz@example.com

REQUIRED FLAGS
    

`--requested-duration`=`REQUESTED_DURATION`
     Duration of the grant being created. 
Entitlement resource - Entitlement the grant is to be created against. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--entitlement` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. This resource can be one of the following types: [privilegedaccessmanager.projects.locations.entitlements, privilegedaccessmanager.folders.locations.entitlements, privilegedaccessmanager.organizations.locations.entitlements]. 



This must be specified. 

`--entitlement`=`ENTITLEMENT`
     ID of the entitlement or fully qualified identifier for the entitlement. 

To set the `entitlement` attribute: 

  * provide the argument `--entitlement` on the command line. 



This flag argument must be specified if any of the other arguments in this group are specified. 

`--folder`=`FOLDER`
     The name of the folder 

To set the `folder` attribute: 

  * provide the argument `--entitlement` on the command line with a fully specified name; 
  * provide the argument `--folder` on the command line. Must be specified for resource of type [privilegedaccessmanager.folders.locations.entitlements]. 


`--location`=`LOCATION`
     The resource location 

To set the `location` attribute: 

  * provide the argument `--entitlement` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


`--organization`=`ORGANIZATION`
     The name of the organization 

To set the `organization` attribute: 

  * provide the argument `--entitlement` on the command line with a fully specified name; 
  * provide the argument `--organization` on the command line. Must be specified for resource of type [privilegedaccessmanager.organizations.locations.entitlements]. 


OPTIONAL FLAGS
    

`--additional-email-recipients`=[`ADDITIONAL_EMAIL_RECIPIENTS`,…]
     Additional email addresses that are notified for all actions performed on the grant. 
`--justification`=`JUSTIFICATION`
     Justification for the grant. 
`--scheduled-activation-time`=`SCHEDULED_ACTIVATION_TIME`
     To schedule the grant, specify a start date and time up to 7 days in the future. If not scheduled, the grant activates immediately upon creation or approval(s). 
Specify the grant's scope using either high-level resource or a fine-grained scope configuration. At most one of these can be specified: 

`--requested-access-from-file`=[`REQUESTED_ACCESS_FROM_FILE`,…]
     Path to a YAML file defining the fine-grained scope for the grant. 
`--requested-resources`=[`REQUESTED_RESOURCES`,…]
     The Google Cloud resources to be granted access to. Format: `{resource-type}/{resource_id}`. Example: `projects/{project_id}` or `folders/{folder_id}` or `organizations/{organization_id}`. This command currently accepts only one resource. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `privilegedaccessmanager/v1beta` API. The full documentation for this API can be found at: <https://cloud.google.com/iam/docs/pam-overview>
NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud pam grants create](https://docs.cloud.google.com/sdk/gcloud/reference/pam/grants/create)
    
    
    [gcloud alpha pam grants create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pam/grants/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
