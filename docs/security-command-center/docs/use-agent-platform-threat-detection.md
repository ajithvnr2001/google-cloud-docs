---
url: https://docs.cloud.google.com/security-command-center/docs/use-agent-platform-threat-detection/
title: Use Agent Platform Threat Detection \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:25:23.910935+00:00
---

# Use Agent Platform Threat Detection  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/use-agent-platform-threat-detection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Use Agent Platform Threat Detection Stay organized with collections  Save and categorize content based on your preferences. 

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes how to configure [Agent Platform Threat Detection](https://docs.cloud.google.com/security-command-center/docs/agent-engine-threat-detection-overview).

The procedures in this document apply only to [Agent Platform Threat Detection runtime detectors](https://docs.cloud.google.com/security-command-center/docs/agent-engine-threat-detection-overview#runtime-detectors). For information about how to work with the [control plane detectors](https://docs.cloud.google.com/security-command-center/docs/agent-engine-threat-detection-overview#control-plane-detectors) for [Agent Runtime](https://docs.cloud.google.com/agent-builder/agent-engine/overview), see [Use Event Threat Detection](https://docs.cloud.google.com/security-command-center/docs/how-to-use-event-threat-detection).

## Before you begin

  1. To get the permissions that you need to manage the Agent Platform Threat Detection service and its modules, ask your administrator to grant you the [Security Center Management Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycentermanagement#securitycentermanagement.admin) (`roles/securitycentermanagement.admin`) IAM role on the organization, folder, or project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

  2. Enable the Container Threat Detection API on all projects that contain hosted AI agents that you want to monitor. If this API is disabled on a project, Agent Platform Threat Detection can't monitor any AI agent in that project.

To view the supported AI agents in your organization or project, see View agents deployed to Agent Runtime in this document.

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=containerthreatdetection.googleapis.com)




## Enable or disable Agent Platform Threat Detection

By default, Agent Platform Threat Detection is enabled on your organization or project. To disable or re-enable Agent Platform Threat Detection, follow these steps:

### Console

To enable or disable Agent Platform Threat Detection through the Google Cloud console, follow these steps:

  1. In the Google Cloud console, go to the **Service Enablement** page for **AI Protection**.

[Go to Service Enablement](https://console.cloud.google.com/projectselector2/security/command-center/config/services/ai-protection/enablement?supportedpurview=organizationId,project)

  2. Select your organization or project.

  3. If AI Protection isn't enabled, click **Activate**. After it's enabled, all of the services that depend on AI Protection are displayed on the page, including Agent Platform Threat Detection.

  4. If the status of Agent Platform Threat Detection is **Disabled** , do the following:

     1. Click **Manage Settings**.
     2. Select the enablement status of the organization, folder, or project that you want to modify, and then select one of the following:

        * **Enable** : enable Agent Platform Threat Detection.
        * **Disable** : disable Agent Platform Threat Detection.
        * **Inherit** : inherit the enablement status from the parent folder or organization; available only for projects and folders.



### gcloud

The [`gcloud scc manage services update`](https://docs.cloud.google.com/sdk/gcloud/reference/scc/manage/services/update) command updates the state of a Security Command Center service or module. 

Before using any of the command data below, make the following replacements: 

  * `RESOURCE_TYPE`: the type of resource to update (`organization`, `folder`, or `project`) 
  * `RESOURCE_ID`: the numeric identifier of the organization, folder, or project to update; for projects, you can also use the alphanumeric project ID 
  * `NEW_STATE`: `ENABLED` to enable Agent Platform Threat Detection; `DISABLED` to disable Agent Platform Threat Detection; or `INHERITED` to inherit the enablement status of the parent resource (valid only for projects and folders) 



Execute the [`gcloud scc manage services update`](https://docs.cloud.google.com/sdk/gcloud/reference/scc/manage/services/update) command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud scc manage services update agent-engine-threat-detection \
        --RESOURCE_TYPE=RESOURCE_ID \
        --enablement-state=NEW_STATE

#### Windows (PowerShell)
    
    
    gcloud scc manage services update agent-engine-threat-detection `
        --RESOURCE_TYPE=RESOURCE_ID `
        --enablement-state=NEW_STATE

#### Windows (cmd.exe)
    
    
    gcloud scc manage services update agent-engine-threat-detection ^
        --RESOURCE_TYPE=RESOURCE_ID ^
        --enablement-state=NEW_STATE

You should receive a response similar to the following:
    
    
    effectiveEnablementState: ENABLED
    intendedEnablementState: INHERITED
    modules:
      AGENT_ENGINE_ADDED_MALICIOUS_BINARY_EXECUTED:
        effectiveEnablementState: ENABLED
      AGENT_ENGINE_ADDED_MALICIOUS_LIBRARY_LOADED:
        effectiveEnablementState: ENABLED
      AGENT_ENGINE_BUILT_IN_MALICIOUS_BINARY_EXECUTED:
        effectiveEnablementState: ENABLED
      AGENT_ENGINE_CONTAINER_ESCAPE:
        effectiveEnablementState: ENABLED
      AGENT_ENGINE_KUBERNETES_ATTACK_TOOL_EXECUTION:
        effectiveEnablementState: ENABLED
      AGENT_ENGINE_LOCAL_RECONNAISSANCE_TOOL_EXECUTION:
        effectiveEnablementState: ENABLED
      AGENT_ENGINE_MALICIOUS_PYTHON_EXECUTED:
        effectiveEnablementState: ENABLED
      AGENT_ENGINE_MALICIOUS_SCRIPT_EXECUTED:
        effectiveEnablementState: ENABLED
      AGENT_ENGINE_MALICIOUS_URL_OBSERVED:
        effectiveEnablementState: ENABLED
      AGENT_ENGINE_MODIFIED_MALICIOUS_BINARY_EXECUTED:
        effectiveEnablementState: ENABLED
      AGENT_ENGINE_MODIFIED_MALICIOUS_LIBRARY_LOADED:
        effectiveEnablementState: ENABLED
      AGENT_ENGINE_REPORT_CLI_ARGUMENTS:
        effectiveEnablementState: ENABLED
      AGENT_ENGINE_REVERSE_SHELL:
        effectiveEnablementState: ENABLED
      AGENT_ENGINE_UNEXPECTED_CHILD_SHELL:
        effectiveEnablementState: ENABLED
    name: organizations/1234567890/locations/global/securityCenterServices/agent-engine-threat-detection
    updateTime: '2025-08-20T18:14:24.731692211Z'
    

### REST

The Security Command Center Management API's `[RESOURCE_TYPE.locations.securityCenterServices.patch](https://docs.cloud.google.com/security-command-center/docs/reference/security-center-management/rest/v1/organizations.locations.securityCenterServices/patch)` method updates the state of a Security Command Center service or module. 

Before using any of the request data, make the following replacements: 

  * `RESOURCE_TYPE`: the type of resource to update (`organizations`, `folders`, or `projects`) 
  * `QUOTA_PROJECT`: the project ID to use for billing and quota tracking. 
  * `RESOURCE_ID`: the numeric identifier of the organization, folder, or project to update; for projects, you can also use the alphanumeric project ID 
  * `NEW_STATE`: `ENABLED` to enable Agent Platform Threat Detection; `DISABLED` to disable Agent Platform Threat Detection; or `INHERITED` to inherit the enablement status of the parent resource (valid only for projects and folders) 



HTTP method and URL: 
    
    
    PATCH https://securitycentermanagement.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/securityCenterServices/agent-engine-threat-detection?updateMask=intendedEnablementState

Request JSON body: 
    
    
    {
      "intendedEnablementState": "NEW_STATE"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: QUOTA_PROJECT" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://securitycentermanagement.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/securityCenterServices/agent-engine-threat-detection?updateMask=intendedEnablementState"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "QUOTA_PROJECT" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://securitycentermanagement.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/securityCenterServices/agent-engine-threat-detection?updateMask=intendedEnablementState" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "organizations/1234567890/locations/global/securityCenterServices/agent-engine-threat-detection",
      "intendedEnablementState": "INHERITED",
      "effectiveEnablementState": "ENABLED",
      "modules": {
        "AGENT_ENGINE_REPORT_CLI_ARGUMENTS": {
          "effectiveEnablementState": "ENABLED"
        },
        "AGENT_ENGINE_BUILT_IN_MALICIOUS_BINARY_EXECUTED": {
          "effectiveEnablementState": "ENABLED"
        },
        "AGENT_ENGINE_ADDED_MALICIOUS_BINARY_EXECUTED": {
          "effectiveEnablementState": "ENABLED"
        },
        "AGENT_ENGINE_KUBERNETES_ATTACK_TOOL_EXECUTION": {
          "effectiveEnablementState": "ENABLED"
        },
        "AGENT_ENGINE_MALICIOUS_URL_OBSERVED": {
          "effectiveEnablementState": "ENABLED"
        },
        "AGENT_ENGINE_MODIFIED_MALICIOUS_LIBRARY_LOADED": {
          "effectiveEnablementState": "ENABLED"
        },
        "AGENT_ENGINE_ADDED_MALICIOUS_LIBRARY_LOADED": {
          "effectiveEnablementState": "ENABLED"
        },
        "AGENT_ENGINE_LOCAL_RECONNAISSANCE_TOOL_EXECUTION": {
          "effectiveEnablementState": "ENABLED"
        },
        "AGENT_ENGINE_CONTAINER_ESCAPE": {
          "effectiveEnablementState": "ENABLED"
        },
        "AGENT_ENGINE_MALICIOUS_SCRIPT_EXECUTED": {
          "effectiveEnablementState": "ENABLED"
        },
        "AGENT_ENGINE_MALICIOUS_PYTHON_EXECUTED": {
          "effectiveEnablementState": "ENABLED"
        },
        "AGENT_ENGINE_REVERSE_SHELL": {
          "effectiveEnablementState": "ENABLED"
        },
        "AGENT_ENGINE_MODIFIED_MALICIOUS_BINARY_EXECUTED": {
          "effectiveEnablementState": "ENABLED"
        },
        "AGENT_ENGINE_UNEXPECTED_CHILD_SHELL": {
          "effectiveEnablementState": "ENABLED"
        }
      },
      "updateTime": "2025-08-20T18:14:24.731692211Z"
    }
    

## Enable or disable an Agent Platform Threat Detection module

To enable or disable an individual Agent Platform Threat Detection module, follow these steps. For information about all Agent Platform Threat Detection threat findings and their modules, see [Detectors](https://docs.cloud.google.com/security-command-center/docs/agent-engine-threat-detection-overview#detectors).

**Note:** If you disable Agent Platform Threat Detection, Security Command Center also disables the individual Agent Platform Threat Detection modules and stores their previous enablement states. If you re-enable Agent Platform Threat Detection, Security Command Center restores the modules to their previous enablement states. 

### Console

In the Google Cloud console, you can enable or disable Agent Platform Threat Detection modules at the organization or project level.

  1. In the Google Cloud console, go to the **Modules** page for Agent Platform Threat Detection.

[Go to Modules](https://console.cloud.google.com/projectselector2/security/command-center/config/services/agent-platform-threat-detection/modules?supportedpurview=organizationId,project)

  2. Select your organization or project.

  3. On the **Modules** tab, in the **Status** column, select the current status of the module that you want to enable or disable, and then select one of the following:

     * **Enable** : enable the module.
     * **Disable** : disable the module. 



### gcloud

The [`gcloud scc manage services update`](https://docs.cloud.google.com/sdk/gcloud/reference/scc/manage/services/update) command updates the state of a Security Command Center service or module. 

Before using any of the command data below, make the following replacements: 

  * `RESOURCE_TYPE`: the type of resource to update (`organization`, `folder`, or `project`). 
  * `RESOURCE_ID`: the numeric identifier for the organization, folder, or project to update. For projects, you can also use the alphanumeric project ID. 
  * `MODULE_NAME`: the name of the module to enable or disable. For valid values, see [Agent Platform Threat Detection detectors](https://docs.cloud.google.com/security-command-center/docs/agent-engine-threat-detection-overview#detectors). 
  * `NEW_STATE`: `ENABLED` to enable the module; `DISABLED` to disable the module; or `INHERITED` to inherit the enablement status of the parent resource (valid only for projects and folders). 



Save the following content in a file called `request.json`: 
    
    
    {
      "MODULE_NAME": {
        "intendedEnablementState": "NEW_STATE"
      }
    }

Execute the [`gcloud scc manage services update`](https://docs.cloud.google.com/sdk/gcloud/reference/scc/manage/services/update) command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud scc manage services update agent-engine-threat-detection \
        --RESOURCE_TYPE=RESOURCE_ID \
        --module-config-file=request.json

#### Windows (PowerShell)
    
    
    gcloud scc manage services update agent-engine-threat-detection `
        --RESOURCE_TYPE=RESOURCE_ID `
        --module-config-file=request.json

#### Windows (cmd.exe)
    
    
    gcloud scc manage services update agent-engine-threat-detection ^
        --RESOURCE_TYPE=RESOURCE_ID ^
        --module-config-file=request.json

You should receive a response similar to the following:
    
    
    effectiveEnablementState: ENABLED
    intendedEnablementState: INHERITED
    modules:
      AGENT_ENGINE_ADDED_MALICIOUS_BINARY_EXECUTED:
        effectiveEnablementState: ENABLED
      AGENT_ENGINE_ADDED_MALICIOUS_LIBRARY_LOADED:
        effectiveEnablementState: ENABLED
      AGENT_ENGINE_BUILT_IN_MALICIOUS_BINARY_EXECUTED:
        effectiveEnablementState: ENABLED
      AGENT_ENGINE_CONTAINER_ESCAPE:
        effectiveEnablementState: ENABLED
      AGENT_ENGINE_KUBERNETES_ATTACK_TOOL_EXECUTION:
        effectiveEnablementState: ENABLED
      AGENT_ENGINE_LOCAL_RECONNAISSANCE_TOOL_EXECUTION:
        effectiveEnablementState: ENABLED
      AGENT_ENGINE_MALICIOUS_PYTHON_EXECUTED:
        effectiveEnablementState: ENABLED
      AGENT_ENGINE_MALICIOUS_SCRIPT_EXECUTED:
        effectiveEnablementState: ENABLED
      AGENT_ENGINE_MALICIOUS_URL_OBSERVED:
        effectiveEnablementState: ENABLED
      AGENT_ENGINE_MODIFIED_MALICIOUS_BINARY_EXECUTED:
        effectiveEnablementState: ENABLED
      AGENT_ENGINE_MODIFIED_MALICIOUS_LIBRARY_LOADED:
        effectiveEnablementState: ENABLED
      AGENT_ENGINE_REPORT_CLI_ARGUMENTS:
        effectiveEnablementState: ENABLED
      AGENT_ENGINE_REVERSE_SHELL:
        effectiveEnablementState: ENABLED
      AGENT_ENGINE_UNEXPECTED_CHILD_SHELL:
        effectiveEnablementState: ENABLED
    name: organizations/1234567890/locations/global/securityCenterServices/agent-engine-threat-detection
    updateTime: '2025-08-20T18:14:24.731692211Z'
    

### REST

The Security Command Center Management API's `[RESOURCE_TYPE.locations.securityCenterServices.patch](https://docs.cloud.google.com/security-command-center/docs/reference/security-center-management/rest/v1/organizations.locations.securityCenterServices/patch)` method updates the state of a Security Command Center service or module. 

Before using any of the request data, make the following replacements: 

  * `RESOURCE_TYPE`: the type of resource to update (`organizations`, `folders`, or `projects`). 
  * `QUOTA_PROJECT`: the project ID to use for billing and quota tracking. 
  * `RESOURCE_ID`: the numeric identifier for the organization, folder, or project to update. For projects, you can also use the alphanumeric project ID. 
  * `MODULE_NAME`: the name of the module to enable or disable. For valid values, see [Agent Platform Threat Detection detectors](https://docs.cloud.google.com/security-command-center/docs/agent-engine-threat-detection-overview#detectors). 
  * `NEW_STATE`: `ENABLED` to enable the module; `DISABLED` to disable the module; or `INHERITED` to inherit the enablement status of the parent resource (valid only for projects and folders). 



HTTP method and URL: 
    
    
    PATCH https://securitycentermanagement.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/securityCenterServices/agent-engine-threat-detection?updateMask=modules

Request JSON body: 
    
    
    {
      "modules": {
        "MODULE_NAME": {
          "intendedEnablementState": "NEW_STATE"
        }
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: QUOTA_PROJECT" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://securitycentermanagement.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/securityCenterServices/agent-engine-threat-detection?updateMask=modules"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "QUOTA_PROJECT" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://securitycentermanagement.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/securityCenterServices/agent-engine-threat-detection?updateMask=modules" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "organizations/1234567890/locations/global/securityCenterServices/agent-engine-threat-detection",
      "intendedEnablementState": "INHERITED",
      "effectiveEnablementState": "ENABLED",
      "modules": {
        "AGENT_ENGINE_REPORT_CLI_ARGUMENTS": {
          "effectiveEnablementState": "ENABLED"
        },
        "AGENT_ENGINE_BUILT_IN_MALICIOUS_BINARY_EXECUTED": {
          "effectiveEnablementState": "ENABLED"
        },
        "AGENT_ENGINE_ADDED_MALICIOUS_BINARY_EXECUTED": {
          "effectiveEnablementState": "ENABLED"
        },
        "AGENT_ENGINE_KUBERNETES_ATTACK_TOOL_EXECUTION": {
          "effectiveEnablementState": "ENABLED"
        },
        "AGENT_ENGINE_MALICIOUS_URL_OBSERVED": {
          "effectiveEnablementState": "ENABLED"
        },
        "AGENT_ENGINE_MODIFIED_MALICIOUS_LIBRARY_LOADED": {
          "effectiveEnablementState": "ENABLED"
        },
        "AGENT_ENGINE_ADDED_MALICIOUS_LIBRARY_LOADED": {
          "effectiveEnablementState": "ENABLED"
        },
        "AGENT_ENGINE_LOCAL_RECONNAISSANCE_TOOL_EXECUTION": {
          "effectiveEnablementState": "ENABLED"
        },
        "AGENT_ENGINE_CONTAINER_ESCAPE": {
          "effectiveEnablementState": "ENABLED"
        },
        "AGENT_ENGINE_MALICIOUS_SCRIPT_EXECUTED": {
          "effectiveEnablementState": "ENABLED"
        },
        "AGENT_ENGINE_MALICIOUS_PYTHON_EXECUTED": {
          "effectiveEnablementState": "ENABLED"
        },
        "AGENT_ENGINE_REVERSE_SHELL": {
          "effectiveEnablementState": "ENABLED"
        },
        "AGENT_ENGINE_MODIFIED_MALICIOUS_BINARY_EXECUTED": {
          "effectiveEnablementState": "ENABLED"
        },
        "AGENT_ENGINE_UNEXPECTED_CHILD_SHELL": {
          "effectiveEnablementState": "ENABLED"
        }
      },
      "updateTime": "2025-08-20T18:14:24.731692211Z"
    }
    

## View the statuses of the Agent Platform Threat Detection modules

To view the statuses of the Agent Platform Threat Detection modules, follow these steps. For information about all Agent Platform Threat Detection threat findings and their modules, see [Detectors](https://docs.cloud.google.com/security-command-center/docs/agent-engine-threat-detection-overview#detectors).

### Console

In the Google Cloud console, you can view the enablement state of Agent Platform Threat Detection modules at the organization or project level.

  1. In the Google Cloud console, go to the **Modules** page for Agent Platform Threat Detection.

[Go to Modules](https://console.cloud.google.com/projectselector2/security/command-center/config/services/agent-platform-threat-detection/modules?supportedpurview=organizationId,project)

  2. Select your organization or project. 




### gcloud

The [`gcloud scc manage services describe`](https://docs.cloud.google.com/sdk/gcloud/reference/scc/manage/services/describe) command gets the state of a Security Command Center service or module. 

Before using any of the command data below, make the following replacements: 

  * `RESOURCE_TYPE`: the type of resource to get (`organization`, `folder`, or `project`) 
  * `RESOURCE_ID`: the numeric identifier for the organization, folder, or project to get. For projects, you can also use the alphanumeric project ID. 



Execute the [`gcloud scc manage services describe`](https://docs.cloud.google.com/sdk/gcloud/reference/scc/manage/services/describe) command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud scc manage services describe agent-engine-threat-detection \
        --RESOURCE_TYPE=RESOURCE_ID

#### Windows (PowerShell)
    
    
    gcloud scc manage services describe agent-engine-threat-detection `
        --RESOURCE_TYPE=RESOURCE_ID

#### Windows (cmd.exe)
    
    
    gcloud scc manage services describe agent-engine-threat-detection ^
        --RESOURCE_TYPE=RESOURCE_ID

You should receive a response similar to the following:
    
    
    effectiveEnablementState: ENABLED
    intendedEnablementState: INHERITED
    modules:
      AGENT_ENGINE_ADDED_MALICIOUS_BINARY_EXECUTED:
        effectiveEnablementState: ENABLED
      AGENT_ENGINE_ADDED_MALICIOUS_LIBRARY_LOADED:
        effectiveEnablementState: ENABLED
      AGENT_ENGINE_BUILT_IN_MALICIOUS_BINARY_EXECUTED:
        effectiveEnablementState: ENABLED
      AGENT_ENGINE_CONTAINER_ESCAPE:
        effectiveEnablementState: ENABLED
      AGENT_ENGINE_KUBERNETES_ATTACK_TOOL_EXECUTION:
        effectiveEnablementState: ENABLED
      AGENT_ENGINE_LOCAL_RECONNAISSANCE_TOOL_EXECUTION:
        effectiveEnablementState: ENABLED
      AGENT_ENGINE_MALICIOUS_PYTHON_EXECUTED:
        effectiveEnablementState: ENABLED
      AGENT_ENGINE_MALICIOUS_SCRIPT_EXECUTED:
        effectiveEnablementState: ENABLED
      AGENT_ENGINE_MALICIOUS_URL_OBSERVED:
        effectiveEnablementState: ENABLED
      AGENT_ENGINE_MODIFIED_MALICIOUS_BINARY_EXECUTED:
        effectiveEnablementState: ENABLED
      AGENT_ENGINE_MODIFIED_MALICIOUS_LIBRARY_LOADED:
        effectiveEnablementState: ENABLED
      AGENT_ENGINE_REPORT_CLI_ARGUMENTS:
        effectiveEnablementState: ENABLED
      AGENT_ENGINE_REVERSE_SHELL:
        effectiveEnablementState: ENABLED
      AGENT_ENGINE_UNEXPECTED_CHILD_SHELL:
        effectiveEnablementState: ENABLED
    name: organizations/1234567890/locations/global/securityCenterServices/agent-engine-threat-detection
    updateTime: '2025-08-20T18:14:24.731692211Z'
    

### REST

The Security Command Center Management API's `[RESOURCE_TYPE.locations.securityCenterServices.get](https://docs.cloud.google.com/security-command-center/docs/reference/security-center-management/rest/v1/organizations.locations.securityCenterServices/patch)` method gets the state of a Security Command Center service or module. 

Before using any of the request data, make the following replacements: 

  * `RESOURCE_TYPE`: the type of resource to get (`organizations`, `folders`, or `projects`). 
  * `QUOTA_PROJECT`: the project ID to use for billing and quota tracking. 
  * `RESOURCE_ID`: the numeric identifier for the organization, folder, or project to get. For projects, you can also use the alphanumeric project ID. 



HTTP method and URL: 
    
    
    GET https://securitycentermanagement.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/securityCenterServices/agent-engine-threat-detection

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: QUOTA_PROJECT" \  
         "https://securitycentermanagement.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/securityCenterServices/agent-engine-threat-detection"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "QUOTA_PROJECT" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://securitycentermanagement.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/securityCenterServices/agent-engine-threat-detection" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "organizations/1234567890/locations/global/securityCenterServices/agent-engine-threat-detection",
      "intendedEnablementState": "INHERITED",
      "effectiveEnablementState": "ENABLED",
      "modules": {
        "AGENT_ENGINE_REPORT_CLI_ARGUMENTS": {
          "effectiveEnablementState": "ENABLED"
        },
        "AGENT_ENGINE_BUILT_IN_MALICIOUS_BINARY_EXECUTED": {
          "effectiveEnablementState": "ENABLED"
        },
        "AGENT_ENGINE_ADDED_MALICIOUS_BINARY_EXECUTED": {
          "effectiveEnablementState": "ENABLED"
        },
        "AGENT_ENGINE_KUBERNETES_ATTACK_TOOL_EXECUTION": {
          "effectiveEnablementState": "ENABLED"
        },
        "AGENT_ENGINE_MALICIOUS_URL_OBSERVED": {
          "effectiveEnablementState": "ENABLED"
        },
        "AGENT_ENGINE_MODIFIED_MALICIOUS_LIBRARY_LOADED": {
          "effectiveEnablementState": "ENABLED"
        },
        "AGENT_ENGINE_ADDED_MALICIOUS_LIBRARY_LOADED": {
          "effectiveEnablementState": "ENABLED"
        },
        "AGENT_ENGINE_LOCAL_RECONNAISSANCE_TOOL_EXECUTION": {
          "effectiveEnablementState": "ENABLED"
        },
        "AGENT_ENGINE_CONTAINER_ESCAPE": {
          "effectiveEnablementState": "ENABLED"
        },
        "AGENT_ENGINE_MALICIOUS_SCRIPT_EXECUTED": {
          "effectiveEnablementState": "ENABLED"
        },
        "AGENT_ENGINE_MALICIOUS_PYTHON_EXECUTED": {
          "effectiveEnablementState": "ENABLED"
        },
        "AGENT_ENGINE_REVERSE_SHELL": {
          "effectiveEnablementState": "ENABLED"
        },
        "AGENT_ENGINE_MODIFIED_MALICIOUS_BINARY_EXECUTED": {
          "effectiveEnablementState": "ENABLED"
        },
        "AGENT_ENGINE_UNEXPECTED_CHILD_SHELL": {
          "effectiveEnablementState": "ENABLED"
        }
      },
      "updateTime": "2025-08-20T18:14:24.731692211Z"
    }
    

## Exclude CLI arguments from findings

By default, when Agent Platform Threat Detection provides process details in a finding, it includes the command line interface (CLI) arguments of the process. CLI argument values can be important in threat investigations.

However, you might decide to exclude CLI arguments from findings because CLI arguments can contain secrets and other sensitive information.

  * To exclude CLI arguments from Agent Platform Threat Detection findings, set the `AGENT_ENGINE_REPORT_CLI_ARGUMENTS` module to `DISABLED`.

  * To include CLI arguments in Agent Platform Threat Detection findings, set the `AGENT_ENGINE_REPORT_CLI_ARGUMENTS` module to `ENABLED`.




For instructions, see Enable or disable an Agent Platform Threat Detection module in this document.

## Review findings

When Agent Platform Threat Detection generates findings, you can view them in Security Command Center.

The IAM roles for Security Command Center can be granted at the organization, folder, or project level. Your ability to view, edit, create, or update findings, assets, and security sources depends on the level that you're granted access for. To learn more about Security Command Center roles, see [Access control](https://docs.cloud.google.com/security-command-center/docs/access-control). 

To review Agent Platform Threat Detection findings in Security Command Center, follow these steps:

  1. In the Google Cloud console, go to the **Findings** page of Security Command Center.

[Go to Findings](https://console.cloud.google.com/security/command-center/findingsv2)

  2. Select your Google Cloud project or organization.
  3. In the **Quick filters** section, in the **Source display name** subsection, select **Agent Platform Threat Detection**. The findings query results are updated to show only the findings from this source. 
  4. To view the details of a specific finding, click the finding name in the **Category** column. The details panel for the finding opens and displays the **Summary** tab. 
  5. On the **Summary** tab, review the details of the finding, including information about what was detected, the affected resource, and—if available—steps that you can take to remediate the finding. 
  6. Optional: To view the full JSON definition of the finding, click the **JSON** tab.



To aid in your investigation, threat findings also contain links to the following external resources:

  * [MITRE ATT&CK](https://attack.mitre.org/) framework entries. The framework explains techniques for attacks against cloud resources and provides remediation guidance.
  * [VirusTotal](https://www.virustotal.com/gui/home/search), an Alphabet-owned service that provides context on potentially malicious files, scripts, URLs, and domains.



For a list of Agent Platform Threat Detection finding types, see [Agent Platform Threat Detection detectors](https://docs.cloud.google.com/security-command-center/docs/agent-engine-threat-detection-overview#detectors).

## View agents deployed to Agent Runtime

If Agent Platform Threat Detection is enabled, it monitors the AI agents that are deployed to Agent Runtime Runtime. This section describes how to view information about each agent that Agent Platform Threat Detection monitors, including its associated project, framework, location, and any findings detected for that agent.

Enterprise (Deprecated) [service tier](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

To get the permissions that you need to view the AI agents that Agent Platform Threat Detection can monitor, ask your administrator to grant you the [Security Command Center Admin Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`) IAM role on organization or project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

  1. In the Google Cloud console, go to the **AI Security** page.

[Go to AI Security](https://console.cloud.google.com/projectselector2/security/command-center/assetsv2/ai-security?supportedpurview=organizationId,project)

  2. Select your organization or project.

  3. In the list of resource types, select **Agent Platform agents**. The agents are displayed.

  4. To view more details about an agent, click its name.




For more information about how to work with resources in the Google Cloud console, see [Inspect assets that are monitored by Security Command Center](https://docs.cloud.google.com/security-command-center/docs/work-with-resources-in-the-console).

## What's next

  * Learn more about [Agent Platform Threat Detection](https://docs.cloud.google.com/security-command-center/docs/agent-engine-threat-detection-overview).
  * Learn how to [test Agent Platform Threat Detection](https://docs.cloud.google.com/security-command-center/docs/how-to-test-agent-engine-threat-detection).
  * Learn how to [respond to AI threat findings](https://docs.cloud.google.com/security-command-center/docs/respond-ai-threats).
  * Refer to the [Threat findings index](https://docs.cloud.google.com/security-command-center/docs/threat-findings-index). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
