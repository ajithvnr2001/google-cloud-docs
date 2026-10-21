---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/scc/manage/services/update/
title: gcloud alpha scc manage services update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:46:19.377930+00:00
---

# gcloud alpha scc manage services update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/scc/manage/services/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha scc manage services update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha scc manage services update - update a Security Command Center service 
SYNOPSIS
    

`gcloud alpha scc manage services update` `SERVICE_NAME` (`--enablement-state`=`ENABLEMENT_STATE` `--module-config-file`=`PATH_TO_FILE`) (`--folder`=`FOLDER_ID` | `--organization`=`ORGANIZATION_ID` | `--parent`=`PARENT` | `--project`=`PROJECT_ID_OR_NUMBER`) [`--validate-only`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Update the enablement state of the Security Center service and its corresponding modules for the specified folder, project or organization. 
EXAMPLES
     To update a Security Center Service with name `sha` for organization 123, run: 
    
    
    gcloud alpha scc manage services update sha --organization=organizations/123 --enablement-state="ENABLED"

To update a Security Center Service with name `sha` and its modules for organization 123, run: 
    
    
    gcloud alpha scc manage services update sha --organization=organizations/123 --enablement-state="ENABLED" --module-config-file=module_config.yaml

To validate an update of Security Center Service with name `sha` and its modules for organization 123, run: 
    
    
    gcloud alpha scc manage services update sha --organization=organizations/123 --enablement-state="ENABLED" --module-config-file=module_config.yaml --validate-only

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
    

At least one of these must be specified: 

`--enablement-state`=`ENABLEMENT_STATE`
     Sets the enablement state of the Security Center service. Valid options are ENABLED, DISABLED, OR INHERITED. The INHERITED state is only valid when setting the enablement state at the project or folder level. 
`--module-config-file`=`PATH_TO_FILE`
     Path to a JSON or YAML file that contains the module config to set for the given module and service. 

The file should contain a map where keys are module names (e.g., "DISK_CMEK_DISABLED") and values are objects with an "intended_enablement_state" field. Valid states are "ENABLED", "DISABLED", or "INHERITED". 

To find the available module names for a specific service and resource, use the `gcloud scc manage services describe <SERVICE_NAME> --parent=<RESOURCE>` command and look for the keys in the "modules" section of the output. 

Example YAML format: 
    
    
    DISK_CMEK_DISABLED:
      intended_enablement_state: DISABLED
    SQL_WEAK_ROOT_PASSWORD:
      intended_enablement_state: ENABLED

Example JSON format: 
    
    
    {
      "DISK_CMEK_DISABLED": {
        "intended_enablement_state": "DISABLED"
      },
      "SQL_WEAK_ROOT_PASSWORD": {
        "intended_enablement_state": "ENABLED"
      }
    }
    
    
    
     .

Use a full or relative path to a local file containing the value of module_config_file. 

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
    

`--validate-only`
     If present, the request is validated (including IAM checks) but no action is taken. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud scc manage services update](https://docs.cloud.google.com/sdk/gcloud/reference/scc/manage/services/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-09 UTC."],[],[]] 
