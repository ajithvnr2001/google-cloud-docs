---
url: https://docs.cloud.google.com/security-command-center/docs/use-cloud-run-threat-detection/
title: Use Cloud Run Threat Detection \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:14:05.767446+00:00
---

# Use Cloud Run Threat Detection  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/use-cloud-run-threat-detection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Use Cloud Run Threat Detection Stay organized with collections  Save and categorize content based on your preferences. 

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This page describes how to configure [Cloud Run Threat Detection](https://docs.cloud.google.com/security-command-center/docs/cloud-run-threat-detection-overview) for your Cloud Run resources.

The procedures on this page apply only to [Cloud Run Threat Detection runtime detectors](https://docs.cloud.google.com/security-command-center/docs/cloud-run-threat-detection-overview#runtime-detectors). For information about how to work with the [control plane detectors](https://docs.cloud.google.com/security-command-center/docs/cloud-run-threat-detection-overview#control-plane-detectors) for Cloud Run, see [Use Event Threat Detection](https://docs.cloud.google.com/security-command-center/docs/how-to-use-event-threat-detection).

## Before you begin

  1. To get the permissions that you need to manage the Cloud Run Threat Detection service and its modules, ask your administrator to grant you the [Security Center Management Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycentermanagement#securitycentermanagement.admin) (`roles/securitycentermanagement.admin`) IAM role on the organization, folder, or project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

  2. Test your Cloud Run containers using the second generation execution environment to make sure that there are no compatibility issues. For more information, see [Supported execution environments](https://docs.cloud.google.com/security-command-center/docs/cloud-run-threat-detection-overview#execution-environments).

  3. Verify that the Container Threat Detection API is enabled on all projects that contain Cloud Run services that you want to monitor. If it's not enabled on a relevant project, then enable it.

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=containerthreatdetection.googleapis.com)




## Enable or disable Cloud Run Threat Detection

When you enable Cloud Run Threat Detection on an organization, folder, or project, it automatically monitors all [supported Cloud Run resources](https://docs.cloud.google.com/security-command-center/docs/cloud-run-threat-detection-overview#supported-resources) in that scope.

After enabling Cloud Run Threat Detection, you must [redeploy the Cloud Run services](https://docs.cloud.google.com/run/docs/deploying#revision) that you want to monitor.

To enable or disable Cloud Run Threat Detection, follow these steps:

### Console

  1. In the Google Cloud console, go to the **Service Enablement** page for Cloud Run Threat Detection.

[Go to Service Enablement](https://console.cloud.google.com/projectselector2/security/command-center/config/services/cloud-run-threat-detection/enablement?supportedpurview=project,folder,organizationId)

  2. Select your organization or project.

  3. On the **Service Enablement** tab, in the **Cloud Run Threat Detection** column, select the enablement status of the organization, folder, or project that you want to modify, and then select one of the following:

     * **Enable** : enable Cloud Run Threat Detection
     * **Disable** : disable Cloud Run Threat Detection
     * **Inherit** : available only for projects and folders; for Cloud Run Threat Detection, this setting is the same as **Disable**



### gcloud

The [`gcloud scc manage services update`](https://docs.cloud.google.com/sdk/gcloud/reference/scc/manage/services/update) command updates the state of a Security Command Center service or module. 

Before using any of the command data below, make the following replacements: 

  * `RESOURCE_TYPE`: the type of resource to update (`organization`, `folder`, or `project`) 
  * `RESOURCE_ID`: the numeric identifier of the organization, folder, or project to update; for projects, you can also use the alphanumeric project ID 
  * `NEW_STATE`: `ENABLED` to enable Cloud Run Threat Detection; `DISABLED` to disable Cloud Run Threat Detection; or `INHERITED` to inherit the enablement status of the parent resource (valid only for projects and folders) 



Execute the [`gcloud scc manage services update`](https://docs.cloud.google.com/sdk/gcloud/reference/scc/manage/services/update) command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud scc manage services update cloud-run-threat-detection \
        --RESOURCE_TYPE=RESOURCE_ID \
        --enablement-state=NEW_STATE

#### Windows (PowerShell)
    
    
    gcloud scc manage services update cloud-run-threat-detection `
        --RESOURCE_TYPE=RESOURCE_ID `
        --enablement-state=NEW_STATE

#### Windows (cmd.exe)
    
    
    gcloud scc manage services update cloud-run-threat-detection ^
        --RESOURCE_TYPE=RESOURCE_ID ^
        --enablement-state=NEW_STATE

You should receive a response similar to the following:
    
    
    effectiveEnablementState: ENABLED
    intendedEnablementState: ENABLED
    modules:
      CLOUD_RUN_ADDED_BINARY_EXECUTED:
        effectiveEnablementState: DISABLED
        intendedEnablementState: DISABLED
      CLOUD_RUN_ADDED_LIBRARY_LOADED:
        effectiveEnablementState: DISABLED
        intendedEnablementState: DISABLED
      CLOUD_RUN_ADDED_MALICIOUS_BINARY_EXECUTED:
        effectiveEnablementState: ENABLED
        intendedEnablementState: ENABLED
      CLOUD_RUN_ADDED_MALICIOUS_LIBRARY_LOADED:
        effectiveEnablementState: ENABLED
        intendedEnablementState: ENABLED
      CLOUD_RUN_BUILT_IN_MALICIOUS_BINARY_EXECUTED:
        effectiveEnablementState: ENABLED
        intendedEnablementState: ENABLED
      CLOUD_RUN_CONTAINER_ESCAPE:
        effectiveEnablementState: ENABLED
        intendedEnablementState: ENABLED
      CLOUD_RUN_KUBERNETES_ATTACK_TOOL_EXECUTION:
        effectiveEnablementState: ENABLED
        intendedEnablementState: ENABLED
      CLOUD_RUN_LOCAL_RECONNAISSANCE_TOOL_EXECUTION:
        effectiveEnablementState: ENABLED
        intendedEnablementState: ENABLED
      CLOUD_RUN_MALICIOUS_PYTHON_EXECUTED:
        effectiveEnablementState: ENABLED
        intendedEnablementState: ENABLED
      CLOUD_RUN_MALICIOUS_SCRIPT_EXECUTED:
        effectiveEnablementState: ENABLED
        intendedEnablementState: ENABLED
      CLOUD_RUN_MALICIOUS_URL_OBSERVED:
        effectiveEnablementState: ENABLED
        intendedEnablementState: ENABLED
      CLOUD_RUN_MODIFIED_MALICIOUS_BINARY_EXECUTED:
        effectiveEnablementState: ENABLED
        intendedEnablementState: ENABLED
      CLOUD_RUN_MODIFIED_MALICIOUS_LIBRARY_LOADED:
        effectiveEnablementState: ENABLED
        intendedEnablementState: ENABLED
      CLOUD_RUN_REPORT_CLI_ARGUMENTS:
        effectiveEnablementState: ENABLED
        intendedEnablementState: ENABLED
      CLOUD_RUN_REPORT_ENVIRONMENT_VARIABLES:
        effectiveEnablementState: ENABLED
        intendedEnablementState: ENABLED
      CLOUD_RUN_REVERSE_SHELL:
        effectiveEnablementState: ENABLED
        intendedEnablementState: ENABLED
      CLOUD_RUN_UNEXPECTED_CHILD_SHELL:
        effectiveEnablementState: ENABLED
        intendedEnablementState: ENABLED
    name: projects/1234567890123/locations/global/securityCenterServices/cloud-run-threat-detection
    updateTime: '2025-03-14T00:27:36.589993683Z'
    

### REST

The Security Command Center Management API's `[RESOURCE_TYPE.locations.securityCenterServices.patch](https://docs.cloud.google.com/security-command-center/docs/reference/security-center-management/rest/v1/organizations.locations.securityCenterServices/patch)` method updates the state of a Security Command Center service or module. 

Before using any of the request data, make the following replacements: 

  * `RESOURCE_TYPE`: the type of resource to update (`organizations`, `folders`, or `projects`) 
  * `QUOTA_PROJECT`: the project ID to use for billing and quota tracking. 
  * `RESOURCE_ID`: the numeric identifier of the organization, folder, or project to update; for projects, you can also use the alphanumeric project ID 
  * `NEW_STATE`: `ENABLED` to enable Cloud Run Threat Detection; `DISABLED` to disable Cloud Run Threat Detection; or `INHERITED` to inherit the enablement status of the parent resource (valid only for projects and folders) 



HTTP method and URL: 
    
    
    PATCH https://securitycentermanagement.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/securityCenterServices/cloud-run-threat-detection?updateMask=intendedEnablementState

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
         "https://securitycentermanagement.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/securityCenterServices/cloud-run-threat-detection?updateMask=intendedEnablementState"

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
        -Uri "https://securitycentermanagement.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/securityCenterServices/cloud-run-threat-detection?updateMask=intendedEnablementState" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/1234567890123/locations/global/securityCenterServices/cloud-run-threat-detection",
      "intendedEnablementState": "ENABLED",
      "effectiveEnablementState": "ENABLED",
      "modules": {
        "CLOUD_RUN_REPORT_CLI_ARGUMENTS": {
          "intendedEnablementState": "ENABLED",
          "effectiveEnablementState": "ENABLED"
        },
        "CLOUD_RUN_CONTAINER_ESCAPE": {
          "intendedEnablementState": "ENABLED",
          "effectiveEnablementState": "ENABLED"
        },
        "CLOUD_RUN_MALICIOUS_SCRIPT_EXECUTED": {
          "intendedEnablementState": "ENABLED",
          "effectiveEnablementState": "ENABLED"
        },
        "CLOUD_RUN_MODIFIED_MALICIOUS_BINARY_EXECUTED": {
          "intendedEnablementState": "ENABLED",
          "effectiveEnablementState": "ENABLED"
        },
        "CLOUD_RUN_ADDED_MALICIOUS_BINARY_EXECUTED": {
          "intendedEnablementState": "ENABLED",
          "effectiveEnablementState": "ENABLED"
        },
        "CLOUD_RUN_ADDED_LIBRARY_LOADED": {
          "intendedEnablementState": "DISABLED",
          "effectiveEnablementState": "DISABLED"
        },
        "CLOUD_RUN_REVERSE_SHELL": {
          "intendedEnablementState": "ENABLED",
          "effectiveEnablementState": "ENABLED"
        },
        "CLOUD_RUN_LOCAL_RECONNAISSANCE_TOOL_EXECUTION": {
          "intendedEnablementState": "ENABLED",
          "effectiveEnablementState": "ENABLED"
        },
        "CLOUD_RUN_KUBERNETES_ATTACK_TOOL_EXECUTION": {
          "intendedEnablementState": "ENABLED",
          "effectiveEnablementState": "ENABLED"
        },
        "CLOUD_RUN_REPORT_ENVIRONMENT_VARIABLES": {
          "intendedEnablementState": "ENABLED",
          "effectiveEnablementState": "ENABLED"
        },
        "CLOUD_RUN_UNEXPECTED_CHILD_SHELL": {
          "intendedEnablementState": "ENABLED",
          "effectiveEnablementState": "ENABLED"
        },
        "CLOUD_RUN_ADDED_BINARY_EXECUTED": {
          "intendedEnablementState": "DISABLED",
          "effectiveEnablementState": "DISABLED"
        },
        "CLOUD_RUN_MODIFIED_MALICIOUS_LIBRARY_LOADED": {
          "intendedEnablementState": "ENABLED",
          "effectiveEnablementState": "ENABLED"
        },
        "CLOUD_RUN_ADDED_MALICIOUS_LIBRARY_LOADED": {
          "intendedEnablementState": "ENABLED",
          "effectiveEnablementState": "ENABLED"
        },
        "CLOUD_RUN_BUILT_IN_MALICIOUS_BINARY_EXECUTED": {
          "intendedEnablementState": "ENABLED",
          "effectiveEnablementState": "ENABLED"
        },
        "CLOUD_RUN_MALICIOUS_PYTHON_EXECUTED": {
          "intendedEnablementState": "ENABLED",
          "effectiveEnablementState": "ENABLED"
        },
        "CLOUD_RUN_MALICIOUS_URL_OBSERVED": {
          "intendedEnablementState": "ENABLED",
          "effectiveEnablementState": "ENABLED"
        }
      },
      "updateTime": "2025-03-14T00:27:36.589993683Z"
    }
    

## Enable or disable a Cloud Run Threat Detection module

To enable or disable an individual Cloud Run Threat Detection module, follow these steps. For information about all Cloud Run Threat Detection threat findings and their modules, see [Cloud Run Threat Detection detectors](https://docs.cloud.google.com/security-command-center/docs/cloud-run-threat-detection-overview#detectors).

**Note:** If you disable Cloud Run Threat Detection, Security Command Center also disables the individual Cloud Run Threat Detection modules and stores their previous enablement states. If you re-enable Cloud Run Threat Detection, Security Command Center restores the modules to their previous enablement states. 

### Console

If the Cloud Run Threat Detection service is enabled, you can set the enablement state of its individual modules.

  1. In the Google Cloud console, go to the **Modules** page for Cloud Run Threat Detection. 

[Go to Modules](https://console.cloud.google.com/projectselector2/security/command-center/config/services/cloud-run-threat-detection/modules?supportedpurview=organizationId,project)

  2. Select your organization or project.
  3. On the **Modules** tab, in the **Status** column, select the current status of the module that you want to enable or disable, and then select one of the following: 
     * **Enable** : Enable the module.
     * **Disable** : Disable the module.



### gcloud

The [`gcloud scc manage services update`](https://docs.cloud.google.com/sdk/gcloud/reference/scc/manage/services/update) command updates the state of a Security Command Center service or module. 

Before using any of the command data below, make the following replacements: 

  * `RESOURCE_TYPE`: the type of resource to update (`organization`, `folder`, or `project`). 
  * `RESOURCE_ID`: the numeric identifier for the organization, folder, or project to update. For projects, you can also use the alphanumeric project ID. 
  * `MODULE_NAME`: the name of the module to enable or disable. For valid values, see [Cloud Run Threat Detection detectors](https://docs.cloud.google.com/security-command-center/docs/cloud-run-threat-detection-overview#detectors). 
  * `NEW_STATE`: `ENABLED` to enable the module; `DISABLED` to disable the module; or `INHERITED` to inherit the enablement status of the parent resource (valid only for projects and folders). 



Save the following content in a file called `request.json`: 
    
    
    {
      "MODULE_NAME": {
        "intendedEnablementState": "NEW_STATE"
      }
    }

Execute the [`gcloud scc manage services update`](https://docs.cloud.google.com/sdk/gcloud/reference/scc/manage/services/update) command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud scc manage services update cloud-run-threat-detection \
        --RESOURCE_TYPE=RESOURCE_ID \
        --module-config-file=request.json

#### Windows (PowerShell)
    
    
    gcloud scc manage services update cloud-run-threat-detection `
        --RESOURCE_TYPE=RESOURCE_ID `
        --module-config-file=request.json

#### Windows (cmd.exe)
    
    
    gcloud scc manage services update cloud-run-threat-detection ^
        --RESOURCE_TYPE=RESOURCE_ID ^
        --module-config-file=request.json

You should receive a response similar to the following:
    
    
    effectiveEnablementState: ENABLED
    intendedEnablementState: ENABLED
    modules:
      CLOUD_RUN_ADDED_BINARY_EXECUTED:
        effectiveEnablementState: DISABLED
        intendedEnablementState: DISABLED
      CLOUD_RUN_ADDED_LIBRARY_LOADED:
        effectiveEnablementState: DISABLED
        intendedEnablementState: DISABLED
      CLOUD_RUN_ADDED_MALICIOUS_BINARY_EXECUTED:
        effectiveEnablementState: ENABLED
        intendedEnablementState: ENABLED
      CLOUD_RUN_ADDED_MALICIOUS_LIBRARY_LOADED:
        effectiveEnablementState: ENABLED
        intendedEnablementState: ENABLED
      CLOUD_RUN_BUILT_IN_MALICIOUS_BINARY_EXECUTED:
        effectiveEnablementState: ENABLED
        intendedEnablementState: ENABLED
      CLOUD_RUN_CONTAINER_ESCAPE:
        effectiveEnablementState: ENABLED
        intendedEnablementState: ENABLED
      CLOUD_RUN_KUBERNETES_ATTACK_TOOL_EXECUTION:
        effectiveEnablementState: ENABLED
        intendedEnablementState: ENABLED
      CLOUD_RUN_LOCAL_RECONNAISSANCE_TOOL_EXECUTION:
        effectiveEnablementState: ENABLED
        intendedEnablementState: ENABLED
      CLOUD_RUN_MALICIOUS_PYTHON_EXECUTED:
        effectiveEnablementState: ENABLED
        intendedEnablementState: ENABLED
      CLOUD_RUN_MALICIOUS_SCRIPT_EXECUTED:
        effectiveEnablementState: ENABLED
        intendedEnablementState: ENABLED
      CLOUD_RUN_MALICIOUS_URL_OBSERVED:
        effectiveEnablementState: ENABLED
        intendedEnablementState: ENABLED
      CLOUD_RUN_MODIFIED_MALICIOUS_BINARY_EXECUTED:
        effectiveEnablementState: ENABLED
        intendedEnablementState: ENABLED
      CLOUD_RUN_MODIFIED_MALICIOUS_LIBRARY_LOADED:
        effectiveEnablementState: ENABLED
        intendedEnablementState: ENABLED
      CLOUD_RUN_REPORT_CLI_ARGUMENTS:
        effectiveEnablementState: ENABLED
        intendedEnablementState: ENABLED
      CLOUD_RUN_REPORT_ENVIRONMENT_VARIABLES:
        effectiveEnablementState: ENABLED
        intendedEnablementState: ENABLED
      CLOUD_RUN_REVERSE_SHELL:
        effectiveEnablementState: ENABLED
        intendedEnablementState: ENABLED
      CLOUD_RUN_UNEXPECTED_CHILD_SHELL:
        effectiveEnablementState: ENABLED
        intendedEnablementState: ENABLED
    name: projects/1234567890123/locations/global/securityCenterServices/cloud-run-threat-detection
    updateTime: '2025-03-14T00:27:36.589993683Z'
    

### REST

The Security Command Center Management API's `[RESOURCE_TYPE.locations.securityCenterServices.patch](https://docs.cloud.google.com/security-command-center/docs/reference/security-center-management/rest/v1/organizations.locations.securityCenterServices/patch)` method updates the state of a Security Command Center service or module. 

Before using any of the request data, make the following replacements: 

  * `RESOURCE_TYPE`: the type of resource to update (`organizations`, `folders`, or `projects`). 
  * `QUOTA_PROJECT`: the project ID to use for billing and quota tracking. 
  * `RESOURCE_ID`: the numeric identifier for the organization, folder, or project to update. For projects, you can also use the alphanumeric project ID. 
  * `MODULE_NAME`: the name of the module to enable or disable. For valid values, see [Cloud Run Threat Detection detectors](https://docs.cloud.google.com/security-command-center/docs/cloud-run-threat-detection-overview#detectors). 
  * `NEW_STATE`: `ENABLED` to enable the module; `DISABLED` to disable the module; or `INHERITED` to inherit the enablement status of the parent resource (valid only for projects and folders). 



HTTP method and URL: 
    
    
    PATCH https://securitycentermanagement.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/securityCenterServices/cloud-run-threat-detection?updateMask=modules

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
         "https://securitycentermanagement.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/securityCenterServices/cloud-run-threat-detection?updateMask=modules"

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
        -Uri "https://securitycentermanagement.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/securityCenterServices/cloud-run-threat-detection?updateMask=modules" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/1234567890123/locations/global/securityCenterServices/cloud-run-threat-detection",
      "intendedEnablementState": "ENABLED",
      "effectiveEnablementState": "ENABLED",
      "modules": {
        "CLOUD_RUN_REPORT_CLI_ARGUMENTS": {
          "intendedEnablementState": "ENABLED",
          "effectiveEnablementState": "ENABLED"
        },
        "CLOUD_RUN_CONTAINER_ESCAPE": {
          "intendedEnablementState": "ENABLED",
          "effectiveEnablementState": "ENABLED"
        },
        "CLOUD_RUN_MALICIOUS_SCRIPT_EXECUTED": {
          "intendedEnablementState": "ENABLED",
          "effectiveEnablementState": "ENABLED"
        },
        "CLOUD_RUN_MODIFIED_MALICIOUS_BINARY_EXECUTED": {
          "intendedEnablementState": "ENABLED",
          "effectiveEnablementState": "ENABLED"
        },
        "CLOUD_RUN_ADDED_MALICIOUS_BINARY_EXECUTED": {
          "intendedEnablementState": "ENABLED",
          "effectiveEnablementState": "ENABLED"
        },
        "CLOUD_RUN_ADDED_LIBRARY_LOADED": {
          "intendedEnablementState": "DISABLED",
          "effectiveEnablementState": "DISABLED"
        },
        "CLOUD_RUN_REVERSE_SHELL": {
          "intendedEnablementState": "ENABLED",
          "effectiveEnablementState": "ENABLED"
        },
        "CLOUD_RUN_LOCAL_RECONNAISSANCE_TOOL_EXECUTION": {
          "intendedEnablementState": "ENABLED",
          "effectiveEnablementState": "ENABLED"
        },
        "CLOUD_RUN_KUBERNETES_ATTACK_TOOL_EXECUTION": {
          "intendedEnablementState": "ENABLED",
          "effectiveEnablementState": "ENABLED"
        },
        "CLOUD_RUN_REPORT_ENVIRONMENT_VARIABLES": {
          "intendedEnablementState": "ENABLED",
          "effectiveEnablementState": "ENABLED"
        },
        "CLOUD_RUN_UNEXPECTED_CHILD_SHELL": {
          "intendedEnablementState": "ENABLED",
          "effectiveEnablementState": "ENABLED"
        },
        "CLOUD_RUN_ADDED_BINARY_EXECUTED": {
          "intendedEnablementState": "DISABLED",
          "effectiveEnablementState": "DISABLED"
        },
        "CLOUD_RUN_MODIFIED_MALICIOUS_LIBRARY_LOADED": {
          "intendedEnablementState": "ENABLED",
          "effectiveEnablementState": "ENABLED"
        },
        "CLOUD_RUN_ADDED_MALICIOUS_LIBRARY_LOADED": {
          "intendedEnablementState": "ENABLED",
          "effectiveEnablementState": "ENABLED"
        },
        "CLOUD_RUN_BUILT_IN_MALICIOUS_BINARY_EXECUTED": {
          "intendedEnablementState": "ENABLED",
          "effectiveEnablementState": "ENABLED"
        },
        "CLOUD_RUN_MALICIOUS_PYTHON_EXECUTED": {
          "intendedEnablementState": "ENABLED",
          "effectiveEnablementState": "ENABLED"
        },
        "CLOUD_RUN_MALICIOUS_URL_OBSERVED": {
          "intendedEnablementState": "ENABLED",
          "effectiveEnablementState": "ENABLED"
        }
      },
      "updateTime": "2025-03-14T00:27:36.589993683Z"
    }
    

## Exclude environment variables from findings

By default, when Cloud Run Threat Detection generates a finding, it reports the environment variables used for all processes referenced in the finding. The values of environment variables can be important in threat investigations.

However, you might decide to exclude environment variables from findings, because some software packages store secrets and other sensitive information in environment variables.

  * To exclude process environment variables from Cloud Run Threat Detection findings, set the `CLOUD_RUN_REPORT_ENVIRONMENT_VARIABLES` module to `DISABLED`.

  * To include process environment variables in Cloud Run Threat Detection findings, set the `CLOUD_RUN_REPORT_ENVIRONMENT_VARIABLES` module to `ENABLED`.




For instructions, see Enable or disable a Cloud Run Threat Detection module on this page.

## Exclude CLI arguments from findings

All processes have one or more command line interface (CLI) arguments. By default, when Cloud Run Threat Detection includes process details in a finding, it records the CLI arguments of the process. CLI argument values can be important in threat investigations.

However, you might decide to exclude CLI arguments from findings because some users might pass secrets and other sensitive information in CLI arguments.

  * To exclude CLI arguments from Cloud Run Threat Detection findings, set the `CLOUD_RUN_REPORT_CLI_ARGUMENTS` module to `DISABLED`.

  * To include CLI arguments in Cloud Run Threat Detection findings, set the `CLOUD_RUN_REPORT_CLI_ARGUMENTS` module to `ENABLED`.




For instructions, see Enable or disable a Cloud Run Threat Detection module on this page.

## View the settings of the Cloud Run Threat Detection modules

For information about all Cloud Run Threat Detection threat findings, see the [Cloud Run Threat Detection detectors](https://docs.cloud.google.com/security-command-center/docs/cloud-run-threat-detection-overview#detectors) table.

### gcloud

The [`gcloud scc manage services describe`](https://docs.cloud.google.com/sdk/gcloud/reference/scc/manage/services/describe) command gets the state of a Security Command Center service or module. 

Before using any of the command data below, make the following replacements: 

  * `RESOURCE_TYPE`: the type of resource to get (`organization`, `folder`, or `project`) 
  * `RESOURCE_ID`: the numeric identifier for the organization, folder, or project to get. For projects, you can also use the alphanumeric project ID. 



Execute the [`gcloud scc manage services describe`](https://docs.cloud.google.com/sdk/gcloud/reference/scc/manage/services/describe) command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud scc manage services describe cloud-run-threat-detection \
        --RESOURCE_TYPE=RESOURCE_ID

#### Windows (PowerShell)
    
    
    gcloud scc manage services describe cloud-run-threat-detection `
        --RESOURCE_TYPE=RESOURCE_ID

#### Windows (cmd.exe)
    
    
    gcloud scc manage services describe cloud-run-threat-detection ^
        --RESOURCE_TYPE=RESOURCE_ID

You should receive a response similar to the following:
    
    
    effectiveEnablementState: ENABLED
    intendedEnablementState: ENABLED
    modules:
      CLOUD_RUN_ADDED_BINARY_EXECUTED:
        effectiveEnablementState: DISABLED
        intendedEnablementState: DISABLED
      CLOUD_RUN_ADDED_LIBRARY_LOADED:
        effectiveEnablementState: DISABLED
        intendedEnablementState: DISABLED
      CLOUD_RUN_ADDED_MALICIOUS_BINARY_EXECUTED:
        effectiveEnablementState: ENABLED
        intendedEnablementState: ENABLED
      CLOUD_RUN_ADDED_MALICIOUS_LIBRARY_LOADED:
        effectiveEnablementState: ENABLED
        intendedEnablementState: ENABLED
      CLOUD_RUN_BUILT_IN_MALICIOUS_BINARY_EXECUTED:
        effectiveEnablementState: ENABLED
        intendedEnablementState: ENABLED
      CLOUD_RUN_CONTAINER_ESCAPE:
        effectiveEnablementState: ENABLED
        intendedEnablementState: ENABLED
      CLOUD_RUN_KUBERNETES_ATTACK_TOOL_EXECUTION:
        effectiveEnablementState: ENABLED
        intendedEnablementState: ENABLED
      CLOUD_RUN_LOCAL_RECONNAISSANCE_TOOL_EXECUTION:
        effectiveEnablementState: ENABLED
        intendedEnablementState: ENABLED
      CLOUD_RUN_MALICIOUS_PYTHON_EXECUTED:
        effectiveEnablementState: ENABLED
        intendedEnablementState: ENABLED
      CLOUD_RUN_MALICIOUS_SCRIPT_EXECUTED:
        effectiveEnablementState: ENABLED
        intendedEnablementState: ENABLED
      CLOUD_RUN_MALICIOUS_URL_OBSERVED:
        effectiveEnablementState: ENABLED
        intendedEnablementState: ENABLED
      CLOUD_RUN_MODIFIED_MALICIOUS_BINARY_EXECUTED:
        effectiveEnablementState: ENABLED
        intendedEnablementState: ENABLED
      CLOUD_RUN_MODIFIED_MALICIOUS_LIBRARY_LOADED:
        effectiveEnablementState: ENABLED
        intendedEnablementState: ENABLED
      CLOUD_RUN_REPORT_CLI_ARGUMENTS:
        effectiveEnablementState: ENABLED
        intendedEnablementState: ENABLED
      CLOUD_RUN_REPORT_ENVIRONMENT_VARIABLES:
        effectiveEnablementState: ENABLED
        intendedEnablementState: ENABLED
      CLOUD_RUN_REVERSE_SHELL:
        effectiveEnablementState: ENABLED
        intendedEnablementState: ENABLED
      CLOUD_RUN_UNEXPECTED_CHILD_SHELL:
        effectiveEnablementState: ENABLED
        intendedEnablementState: ENABLED
    name: projects/1234567890123/locations/global/securityCenterServices/cloud-run-threat-detection
    updateTime: '2025-03-14T00:27:36.589993683Z'
    

### REST

The Security Command Center Management API's `[RESOURCE_TYPE.locations.securityCenterServices.get](https://docs.cloud.google.com/security-command-center/docs/reference/security-center-management/rest/v1/organizations.locations.securityCenterServices/patch)` method gets the state of a Security Command Center service or module. 

Before using any of the request data, make the following replacements: 

  * `RESOURCE_TYPE`: the type of resource to get (`organizations`, `folders`, or `projects`). 
  * `QUOTA_PROJECT`: the project ID to use for billing and quota tracking. 
  * `RESOURCE_ID`: the numeric identifier for the organization, folder, or project to get. For projects, you can also use the alphanumeric project ID. 



HTTP method and URL: 
    
    
    GET https://securitycentermanagement.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/securityCenterServices/cloud-run-threat-detection

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: QUOTA_PROJECT" \  
         "https://securitycentermanagement.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/securityCenterServices/cloud-run-threat-detection"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "QUOTA_PROJECT" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://securitycentermanagement.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/securityCenterServices/cloud-run-threat-detection" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/1234567890123/locations/global/securityCenterServices/cloud-run-threat-detection",
      "intendedEnablementState": "ENABLED",
      "effectiveEnablementState": "ENABLED",
      "modules": {
        "CLOUD_RUN_REPORT_CLI_ARGUMENTS": {
          "intendedEnablementState": "ENABLED",
          "effectiveEnablementState": "ENABLED"
        },
        "CLOUD_RUN_CONTAINER_ESCAPE": {
          "intendedEnablementState": "ENABLED",
          "effectiveEnablementState": "ENABLED"
        },
        "CLOUD_RUN_MALICIOUS_SCRIPT_EXECUTED": {
          "intendedEnablementState": "ENABLED",
          "effectiveEnablementState": "ENABLED"
        },
        "CLOUD_RUN_MODIFIED_MALICIOUS_BINARY_EXECUTED": {
          "intendedEnablementState": "ENABLED",
          "effectiveEnablementState": "ENABLED"
        },
        "CLOUD_RUN_ADDED_MALICIOUS_BINARY_EXECUTED": {
          "intendedEnablementState": "ENABLED",
          "effectiveEnablementState": "ENABLED"
        },
        "CLOUD_RUN_ADDED_LIBRARY_LOADED": {
          "intendedEnablementState": "DISABLED",
          "effectiveEnablementState": "DISABLED"
        },
        "CLOUD_RUN_REVERSE_SHELL": {
          "intendedEnablementState": "ENABLED",
          "effectiveEnablementState": "ENABLED"
        },
        "CLOUD_RUN_LOCAL_RECONNAISSANCE_TOOL_EXECUTION": {
          "intendedEnablementState": "ENABLED",
          "effectiveEnablementState": "ENABLED"
        },
        "CLOUD_RUN_KUBERNETES_ATTACK_TOOL_EXECUTION": {
          "intendedEnablementState": "ENABLED",
          "effectiveEnablementState": "ENABLED"
        },
        "CLOUD_RUN_REPORT_ENVIRONMENT_VARIABLES": {
          "intendedEnablementState": "ENABLED",
          "effectiveEnablementState": "ENABLED"
        },
        "CLOUD_RUN_UNEXPECTED_CHILD_SHELL": {
          "intendedEnablementState": "ENABLED",
          "effectiveEnablementState": "ENABLED"
        },
        "CLOUD_RUN_ADDED_BINARY_EXECUTED": {
          "intendedEnablementState": "DISABLED",
          "effectiveEnablementState": "DISABLED"
        },
        "CLOUD_RUN_MODIFIED_MALICIOUS_LIBRARY_LOADED": {
          "intendedEnablementState": "ENABLED",
          "effectiveEnablementState": "ENABLED"
        },
        "CLOUD_RUN_ADDED_MALICIOUS_LIBRARY_LOADED": {
          "intendedEnablementState": "ENABLED",
          "effectiveEnablementState": "ENABLED"
        },
        "CLOUD_RUN_BUILT_IN_MALICIOUS_BINARY_EXECUTED": {
          "intendedEnablementState": "ENABLED",
          "effectiveEnablementState": "ENABLED"
        },
        "CLOUD_RUN_MALICIOUS_PYTHON_EXECUTED": {
          "intendedEnablementState": "ENABLED",
          "effectiveEnablementState": "ENABLED"
        },
        "CLOUD_RUN_MALICIOUS_URL_OBSERVED": {
          "intendedEnablementState": "ENABLED",
          "effectiveEnablementState": "ENABLED"
        }
      },
      "updateTime": "2025-03-14T00:27:36.589993683Z"
    }
    

## Review findings

When Cloud Run Threat Detection generates findings, you can view them in Security Command Center.

The IAM roles for Security Command Center can be granted at the organization, folder, or project level. Your ability to view, edit, create, or update findings, assets, and security sources depends on the level that you're granted access for. To learn more about Security Command Center roles, see [Access control](https://docs.cloud.google.com/security-command-center/docs/access-control). 

To review Cloud Run Threat Detection findings in Security Command Center, follow these steps:

  1. In the Google Cloud console, go to the **Findings** page of Security Command Center.

[Go to Findings](https://console.cloud.google.com/security/command-center/findingsv2)

  2. Select your Google Cloud project or organization.
  3. In the **Quick filters** section, in the **Source display name** subsection, select **Cloud Run Threat Detection**. The findings query results are updated to show only the findings from this source. 
  4. To view the details of a specific finding, click the finding name in the **Category** column. The details panel for the finding opens and displays the **Summary** tab. 
  5. On the **Summary** tab, review the details of the finding, including information about what was detected, the affected resource, and—if available—steps that you can take to remediate the finding. 
  6. Optional: To view the full JSON definition of the finding, click the **JSON** tab.



To aid in your investigation, threat findings also contain links to the following external resources:

  * [MITRE ATT&CK](https://attack.mitre.org/) framework entries. The framework explains techniques for attacks against cloud resources and provides remediation guidance.
  * [VirusTotal](https://www.virustotal.com/gui/home/search), an Alphabet-owned service that provides context on potentially malicious files, scripts, URLs, and domains.



For a list of Cloud Run Threat Detection finding types, see [Cloud Run Threat Detection detectors](https://docs.cloud.google.com/security-command-center/docs/cloud-run-threat-detection-overview#detectors).

## What's next

  * Learn more about [Cloud Run Threat Detection](https://docs.cloud.google.com/security-command-center/docs/cloud-run-threat-detection-overview).
  * Learn how to [test Cloud Run Threat Detection](https://docs.cloud.google.com/security-command-center/docs/how-to-test-cloud-run-threat-detection).
  * Learn how to [respond to Cloud Run threat findings](https://docs.cloud.google.com/security-command-center/docs/respond-cloud-run-threats).
  * Refer to the [Threat findings index](https://docs.cloud.google.com/security-command-center/docs/threat-findings-index).
  * Learn how to [redeploy Cloud Run services](https://docs.cloud.google.com/run/docs/deploying#revision).
  * Learn how Cloud Run implements [security best practices](https://docs.cloud.google.com/run/docs/securing/security). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
