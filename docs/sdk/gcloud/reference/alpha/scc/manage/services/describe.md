---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/scc/manage/services/describe/
title: gcloud alpha scc manage services describe \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:46:19.102122+00:00
---

# gcloud alpha scc manage services describe  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/scc/manage/services/describe/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha scc manage services describe Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha scc manage services describe - get the details of a Security Command Center service 
SYNOPSIS
    

`gcloud alpha scc manage services describe` `SERVICE_NAME` (`--folder`=`FOLDER_ID` | `--organization`=`ORGANIZATION_ID` | `--parent`=`PARENT` | `--project`=`PROJECT_ID_OR_NUMBER`) [`--filter-modules`=`FILTER_MODULES`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Get the details of a Security Command Center service. It resolves INHERITED enablement states to ENABLED or DISABLED for services at ancestor levels. For example, if the service is enabled at the ancestor level, services for all child resources will have the enablement state set to ENABLED. 
EXAMPLES
     To get the details of a Security Command Center service with name `sha` for organization `123`, run: 
    
    
    gcloud alpha scc manage services describe sha --organization=123

To get the details of a Security Command Center service with name `sha` for folder `456`, run: 
    
    
    gcloud alpha scc manage services describe sha --folder=456

To get the details of a Security Command Center service with ID `sha` for project `789`, run: 
    
    
    gcloud alpha scc manage services describe sha --project=789

You can also specify the parent more generally: 
    
    
    gcloud alpha scc manage services describe sha --parent=organizations/123

To get the details of modules, `[ABC, DEF]` of a Security Command Center service with name `sha` for organization `123`, run: 
    
    
    gcloud alpha scc manage services describe sha --module-list=[ABC, DEF] --organization=123

POSITIONAL ARGUMENTS
    

`SERVICE_NAME`
     The service name, provided either in lowercase hyphenated form (e.g. security-health-analytics), or in abbreviated form (e.g. sha) if applicable. 

The list of supported services is: 

  * security-health-analytics (can be abbreviated as sha) 


  * event-threat-detection (can be abbreviated as etd) 


  * container-threat-detection (can be abbreviated as ctd) 


  * vm-threat-detection (can be abbreviated as vmtd) 


  * web-security-scanner (can be abbreviated as wss) 


  * vm-threat-detection-aws (can be abbreviated as vmtd-aws) 


  * cloud-run-threat-detection (can be abbreviated as crtd) 


  * external-exposure (can be abbreviated as ee) 


  * vm-manager (can be abbreviated as vmm) 


  * ec2-vulnerability-assessment (can be abbreviated as ec2-va) 


  * gce-vulnerability-assessment (can be abbreviated as gce-va) 


  * azure-vulnerability-assessment (can be abbreviated as azure-va) 


  * notebook-security-scanner (can be abbreviated as nss) 


  * agent-engine-threat-detection (can be abbreviated as aetd) 


REQUIRED FLAGS
    

Exactly one of these must be specified: 

`--folder`=`FOLDER_ID`
     Folder associated with the custom module. 
`--organization`=`ORGANIZATION_ID`
     Organization associated with the custom module. 
`--parent`=`PARENT`
     Parent associated with the custom module. Can be one of organizations/<id>, projects/<id or name>, folders/<id>
`--project`=`PROJECT_ID_OR_NUMBER`
     Project associated with the custom module. 
OPTIONAL FLAGS
    

`--filter-modules`=`FILTER_MODULES`
     If provided, only prints module information for modules specified in the list. Provided as a comma separated list of module names in SCREAMING_SNAKE_CASE format (e.g. WEB_UI_ENABLED, API_KEY_NOT_ROTATED). A single module name is also valid. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud scc manage services describe](https://docs.cloud.google.com/sdk/gcloud/reference/scc/manage/services/describe)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-09 UTC."],[],[]] 
