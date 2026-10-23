---
url: https://docs.cloud.google.com/security-command-center/docs/use-custom-modules-etd/
title: Create and manage custom modules for Event Threat Detection \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:37:51.395051+00:00
---

# Create and manage custom modules for Event Threat Detection  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/use-custom-modules-etd/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Create and manage custom modules for Event Threat Detection Stay organized with collections  Save and categorize content based on your preferences. 

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This page explains how to create and manage custom modules for Event Threat Detection.

## Before you begin

This section describes the requirements for using custom modules for Event Threat Detection.

### Security Command Center Premium and Event Threat Detection

To use Event Threat Detection custom modules, Event Threat Detection must be enabled. To enable Event Threat Detection, see [Enable or disable a built-in service](https://docs.cloud.google.com/security-command-center/docs/how-to-configure-security-command-center#enable-service).

### Required IAM roles and permissions

IAM roles determine the actions that you can perform with Event Threat Detection custom modules.

The following table contains a list of Event Threat Detection custom module permissions that are required as well as the predefined IAM roles that include them.

You can use the Google Cloud console or Security Command Center API to apply these roles at the organization, folder, or project level.

Permissions required | Role  
---|---  
`securitycentermanagement.eventThreatDetectionCustomModules.create`  
`securitycentermanagement.eventThreatDetectionCustomModules.update`  
`securitycentermanagement.eventThreatDetectionCustomModules.delete` | `roles/securitycentermanagement.etdCustomModulesEditor`  
`roles/securitycenter.settingsEditor`  
`roles/securitycenter.admin`  
`securitycentermanagement.eventThreatDetectionCustomModules.list`  
`securitycentermanagement.eventThreatDetectionCustomModules.get`  
`securitycentermanagement.effectiveEventThreatDetectionCustomModules.list`  
`securitycentermanagement.effectiveEventThreatDetectionCustomModules.get`  
`securitycentermanagement.eventThreatDetectionCustomModules.validate` | `roles/securitycentermanagement.etdCustomModulesViewer`  
`roles/securitycentermanagement.etdCustomModulesEditor`  
`roles/securitycenter.adminViewer`  
`roles/securitycenter.admin`  
  
If you encounter access errors in Security Command Center, ask your administrator for assistance. See one of the following pages depending on the level at which you activated Security Command Center:

  * [IAM for organization-level activations of Security Command Center](https://docs.cloud.google.com/security-command-center/docs/access-control-org)

  * [IAM for project-level activations of Security Command Center](https://docs.cloud.google.com/security-command-center/docs/access-control-project)




### Required logs

Make sure that the relevant logs are turned on for your organization, folders, and projects. For information about which logs are required by each custom module type, see the table in [Custom modules and templates](https://docs.cloud.google.com/security-command-center/docs/custom-modules-etd-overview#custom_modules_and_templates).

Logs from sources outside of Google Cloud aren't supported.

## Custom module levels

This document uses the following terms to describe the level at which a custom module was created:

Residential module
    The module was created at the current view or scope. For example, if you're in the organization view of the Google Cloud console, the residential modules are the modules that were created at the organization level.
Inherited module
    The module was created at a parent view or scope. For example, a module created at organization level is an inherited module at any folder or project level.
Descendant module
    The module was created at a child view or scope. For example, a module created at a folder or project level is a descendant module at the organization level.

## Create custom modules

You can create Event Threat Detection custom modules through the Google Cloud console or by modifying a JSON template and submitting it through the gcloud CLI. You need JSON templates only if you plan to use the gcloud CLI to create custom modules.

For a list of supported module templates, see [Custom modules and templates](https://docs.cloud.google.com/security-command-center/docs/custom-modules-etd-overview#custom_modules_and_templates).

### Template structure

Templates define the parameters that custom modules use to identify threats in your logs. Templates are written in JSON and are similar in structure to the findings generated by Security Command Center. You need to configure a JSON template only if you plan to use the gcloud CLI to create a custom module.

Each template contains customizable fields:

  * `severity`: the severity or risk level you want assigned to findings of this type, `LOW`, `MEDIUM`, `HIGH`, or `CRITICAL`.
  * `description`: the description of the custom module.
  * `recommendation`: recommended actions for addressing findings generated by the custom module.
  * Detection parameters: the variables used to evaluate logs and trigger findings. Detection parameters differ for each module, but they include one or more the following: 
    * `domains`: web domains to watch for
    * `ips`: IP addresses to watch for
    * `permissions`: permissions to watch for
    * `regions`: regions where new Compute Engine instances are allowed
    * `roles`: roles to watch for
    * `accounts`: accounts to watch for
    * Parameters that define the allowed Compute Engine instance types—for example, `series`, `cpus`, and `ram_mb`.
    * Regular expressions to check properties against—for example, `caller_pattern` and `resource_pattern`.



The following code sample is an example JSON template for `Configurable Bad IP`.
    
    
    {
      "metadata": {
        "severity": "LOW",
        "description": "Flagged by Cymbal as malicious",
        "recommendation": "Contact the owner of the relevant project."
      },
      "ips": [
        "192.0.2.1",
        "192.0.2.0/24"
      ]
    }
    

In the preceding example, the custom module generates a low-severity finding if your logs indicate a resource connected to the IP address `192.0.2.1` or `192.0.2.0/24`.

### Modify a module template

To create modules, you choose a module template and modify it.

If you plan to use the Google Cloud CLI to create your custom module, you must perform this task.

If you plan to use the Google Cloud console to create your custom module, skip this task. You will use the options presented on the screen to modify the parameters of the template.

  1. Choose a template from [Custom modules and templates](https://docs.cloud.google.com/security-command-center/docs/custom-modules-etd-overview#custom_modules_and_templates).
  2. Copy the code to a local file.
  3. Update the parameters that you want to use to evaluate your logs.
  4. Save the file as a JSON file.
  5. Create a custom module through the gcloud CLI using the JSON file.



### Create a custom module

This section describes how to create a custom module through the Google Cloud console, the gcloud CLI, the REST API, and Terraform. Each Event Threat Detection custom module has a size limit of 6 MB.

To create a custom module, follow these steps:

### Console

  1. [View the modules](https://docs.cloud.google.com/security-command-center/docs/how-to-configure-security-command-center#view-modules) of the **Event Threat Detection** service. The predefined and custom modules appear in a list.
  2. Click **Create module**.
  3. Click the module template that you want to use.
  4. Click **Select**.
  5. For **Module name** , enter a display name for the new template. The name must not exceed 128 characters and must contain only alphanumeric characters and underscores—for example, `example_custom_module`.
  6. Select or add the requested parameter values. The parameters differ for each module. For example, if you selected the `Configurable allowed Compute Engine region` module template, you select one or more regions. Alternatively, provide the list in JSON format.
  7. Click **Next**.
  8. For **Severity** , enter the severity level that you want to assign to findings generated by the new custom module.
  9. For **Description** , enter a description for the new custom module.
  10. For **Next steps** , enter the recommended actions in plain text format. Any paragraph breaks that you add are ignored.
  11. Click **Create**.



### gcloud

The [`gcloud scc manage custom-modules etd create`](https://docs.cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/etd/create) command creates an Event Threat Detection custom module for an organization, folder, or project. 

Before using any of the command data below, make the following replacements: 

  * `RESOURCE_TYPE`: the type of resource that the custom modules belong to (`organization`, `folder`, or `project`) 
  * `RESOURCE_ID`: the numeric identifier for the organization, folder, or project for the custom module. For projects, you can also use the alphanumeric project ID. 
  * `MODULE_CONFIG`: the configuration settings for the custom module. Use a [custom module template](https://docs.cloud.google.com/security-command-center/docs/custom-modules-etd-overview#custom_modules_and_templates) as a starting point. 
  * `MODULE_TYPE`: the type of custom module. For a list of supported types, see [Custom modules and templates](https://docs.cloud.google.com/security-command-center/docs/custom-modules-etd-overview#custom_modules_and_templates). 
  * `MODULE_DISPLAY_NAME`: the human-readable display name for the custom module. It can contain letters, numbers, and underscores (`_`). It can be up to 128 characters long. 



Save the following content in a file called `request.json`: 
    
    
    {
      MODULE_CONFIG
    }

Execute the [`gcloud scc manage custom-modules etd create`](https://docs.cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/etd/create) command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud scc manage custom-modules etd create \
        --RESOURCE_TYPE=RESOURCE_ID \
        --custom-config-file=request.json \
        --display-name=MODULE_DISPLAY_NAME \
        --module-type=MODULE_TYPE \
        --enablement-state=ENABLED

#### Windows (PowerShell)
    
    
    gcloud scc manage custom-modules etd create `
        --RESOURCE_TYPE=RESOURCE_ID `
        --custom-config-file=request.json `
        --display-name=MODULE_DISPLAY_NAME `
        --module-type=MODULE_TYPE `
        --enablement-state=ENABLED

#### Windows (cmd.exe)
    
    
    gcloud scc manage custom-modules etd create ^
        --RESOURCE_TYPE=RESOURCE_ID ^
        --custom-config-file=request.json ^
        --display-name=MODULE_DISPLAY_NAME ^
        --module-type=MODULE_TYPE ^
        --enablement-state=ENABLED

### REST

The Security Command Center Management API's `[RESOURCE_TYPE.locations.eventThreatDetectionCustomModules.create](https://docs.cloud.google.com/security-command-center/docs/reference/security-center-management/rest/v1/organizations.locations.eventThreatDetectionCustomModules/create)` method creates an Event Threat Detection custom module for an organization, folder, or project. 

Before using any of the request data, make the following replacements: 

  * `RESOURCE_TYPE`: the type of resource that the custom module belongs to (`organizations`, `folders`, or `projects`). 
  * `QUOTA_PROJECT`: the project ID to use for billing and quota tracking. 
  * `RESOURCE_ID`: the numeric identifier for the organization, folder, or project for the custom module. For projects, you can also use the alphanumeric project ID. 
  * `MODULE_CONFIG`: the configuration settings for the custom module. Use a [custom module template](https://docs.cloud.google.com/security-command-center/docs/custom-modules-etd-overview#custom_modules_and_templates) as a starting point. 
  * `MODULE_TYPE`: the type of custom module. For a list of supported types, see [Custom modules and templates](https://docs.cloud.google.com/security-command-center/docs/custom-modules-etd-overview#custom_modules_and_templates). 
  * `MODULE_DISPLAY_NAME`: the human-readable display name for the custom module. It can contain letters, numbers, and underscores (`_`). It can be up to 128 characters long. 



HTTP method and URL: 
    
    
    POST https://securitycentermanagement.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/eventThreatDetectionCustomModules

Request JSON body: 
    
    
    {
      "config": MODULE_CONFIG,
      "enablementState": "ENABLED",
      "type": "MODULE_TYPE",
      "displayName": "MODULE_DISPLAY_NAME"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: QUOTA_PROJECT" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://securitycentermanagement.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/eventThreatDetectionCustomModules"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "QUOTA_PROJECT" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://securitycentermanagement.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/eventThreatDetectionCustomModules" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/1234567890123/locations/global/eventThreatDetectionCustomModules/98765432109876543210",
      "config": {
        "metadata": {
          "severity": "MEDIUM",
          "description": "An IAM custom role contains permissions that aren't allowed.",
          "recommendation": "Remove the permissions from the custom role."
        },
        "permissions": [
          "accessapproval.requests.get",
          "accessapproval.requests.invalidate",
          "accessapproval.requests.list",
          "accessapproval.settings.delete"
        ]
      },
      "enablementState": "ENABLED",
      "type": "CONFIGURABLE_CUSTOM_ROLE_WITH_PROHIBITED_PERMISSION",
      "displayName": "iam_custom_role_prohibited_permissions",
      "updateTime": "2026-03-16T19:44:58.588134Z"
    }
    

### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands). For more information, see the [ Terraform provider reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs). 
    
    
    resource "google_scc_management_organization_event_threat_detection_custom_module" "example" {
      organization = "123456789"
      location = "global"
      display_name = "basic_custom_module"
      enablement_state = "ENABLED"
      type = "CONFIGURABLE_BAD_IP"
      description = "My Event Threat Detection Custom Module"
      config = jsonencode({
        "metadata": {
          "severity": "LOW",
          "description": "Flagged by Forcepoint as malicious",
          "recommendation": "Contact the owner of the relevant project."
        },
        "ips": [
          "192.0.2.1",
          "192.0.2.0/24"
        ]
      })
    }
    

Your custom module is created and starts scanning. To delete a module, see Delete a custom module.

The category name of the custom module contains the [finding category of the module type](https://docs.cloud.google.com/security-command-center/docs/custom-modules-etd-overview#custom_modules_and_templates) and the module display name that you set. For example, the category name of a custom module can be `Unexpected Compute Engine Region: example_custom_module`. In the Google Cloud console, underscores are displayed as spaces. However, in your queries, you must include the underscores.

[Quotas](https://docs.cloud.google.com/security-command-center/docs/custom-modules-etd-overview#pricing_and_quota) govern your use of custom modules for Event Threat Detection.

## Detection latency

The detection latency for Event Threat Detection and all other built-in Security Command Center services are described in [Scan latency](https://docs.cloud.google.com/security-command-center/docs/concepts-scan-latency-overview#scan_latency).

## Review findings

Findings generated by custom modules can be viewed in the Google Cloud console or by using the gcloud CLI or REST API.

### Console

  1. In the Google Cloud console, go to the **Findings** page of Security Command Center.

[Go to Findings](https://console.cloud.google.com/security/command-center/findingsv2)

  2. Select your Google Cloud project or organization.
  3. In the **Quick filters** section, in the **Source display name** subsection, select **Event Threat Detection Custom Modules**. The findings query results are updated to show only the findings from this source. 
  4. To view the details of a specific finding, click the finding name in the **Category** column. The details panel for the finding opens and displays the **Summary** tab. 
  5. On the **Summary** tab, review the details of the finding, including information about what was detected, the affected resource, and—if available—steps that you can take to remediate the finding. 
  6. Optional: To view the full JSON definition of the finding, click the **JSON** tab.



### gcloud

### Find the source ID

The [`gcloud scc sources describe`](https://docs.cloud.google.com/sdk/gcloud/reference/scc/sources/describe) command shows information about a findings source for Security Command Center. 

Before using any of the command data below, make the following replacements: 

  * `RESOURCE_TYPE`: the type of resource that the source belongs to (`organizations`, `folders`, or `projects`). 
  * `RESOURCE_ID`: the numeric identifier for the organization, folder, or project. For projects, you can also use the alphanumeric project ID. 



Execute the [`gcloud scc sources describe`](https://docs.cloud.google.com/sdk/gcloud/reference/scc/sources/describe) command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud scc sources describe RESOURCE_TYPE/RESOURCE_ID \
        --source-display-name="Event Threat Detection Custom Modules"

#### Windows (PowerShell)
    
    
    gcloud scc sources describe RESOURCE_TYPE/RESOURCE_ID `
        --source-display-name="Event Threat Detection Custom Modules"

#### Windows (cmd.exe)
    
    
    gcloud scc sources describe RESOURCE_TYPE/RESOURCE_ID ^
        --source-display-name="Event Threat Detection Custom Modules"

You should receive a response similar to the following:
    
    
    canonicalName: organizations/123456789012/sources/98765432109876543210
    description: Provider used by Event Threat Detection Custom Modules
    displayName: Event Threat Detection Custom Modules
    name: organizations/123456789012/sources/98765432109876543210
    

The source ID is the numeric value at the end of the `canonicalName` and `name` fields—for example, `98765432109876543210`. 

### List all findings for Event Threat Detection custom modules

The `[gcloud scc findings list](https://docs.cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/etd/create)` command lists findings for a source in a specific location. 

Before using any of the command data below, make the following replacements: 

  * `RESOURCE_TYPE`: the type of resource to get (`organizations`, `folders`, or `projects`). 
  * `RESOURCE_ID`: the numeric identifier for the organization, folder, or project to get. For projects, you can also use the alphanumeric project ID. 
  * `LOCATION`: the [Security Command Center location](https://docs.cloud.google.com/security-command-center/docs/data-residency-support#locations) to use, such as `eu`. If data residency is not enabled, use `global`. 
  * `SOURCE_ID`: the numeric identifier for the findings source. 



Execute the following command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud scc findings list RESOURCE_TYPE/RESOURCE_ID \
        --source=SOURCE_ID \
        --location=LOCATION

#### Windows (PowerShell)
    
    
    gcloud scc findings list RESOURCE_TYPE/RESOURCE_ID `
        --source=SOURCE_ID `
        --location=LOCATION

#### Windows (cmd.exe)
    
    
    gcloud scc findings list RESOURCE_TYPE/RESOURCE_ID ^
        --source=SOURCE_ID ^
        --location=LOCATION

The response contains a list of findings.

### List findings for a specific custom module

The `[gcloud scc findings list](https://docs.cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/etd/create)` command lists findings for a source in a specific location. 

Before using any of the command data below, make the following replacements: 

  * `RESOURCE_TYPE`: the type of resource to get (`organizations`, `folders`, or `projects`). 
  * `RESOURCE_ID`: the numeric identifier for the organization, folder, or project to get. For projects, you can also use the alphanumeric project ID. 
  * `LOCATION`: the [Security Command Center location](https://docs.cloud.google.com/security-command-center/docs/data-residency-support#locations) to use, such as `eu`. If data residency is not enabled, use `global`. 
  * `SOURCE_ID`: the numeric identifier for the findings source. 
  * `CUSTOM_MODULE_CATEGORY_NAME`: the custom module's category name, composed of the module's finding category (as listed in [Custom modules and templates](https://docs.cloud.google.com/security-command-center/docs/custom-modules-etd-overview#custom_modules_and_templates)); a colon; a space; and the module display name with spaces replaced by underscores. For example, `Unexpected Compute Engine region: example_custom_module`. 



Execute the following command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud scc findings list RESOURCE_TYPE/RESOURCE_ID \
        --source=SOURCE_ID \
        --location=LOCATION \
        --filter="category=\"CUSTOM_MODULE_CATEGORY_NAME\""

#### Windows (PowerShell)
    
    
    gcloud scc findings list RESOURCE_TYPE/RESOURCE_ID `
        --source=SOURCE_ID `
        --location=LOCATION `
        --filter="category=\"CUSTOM_MODULE_CATEGORY_NAME\""

#### Windows (cmd.exe)
    
    
    gcloud scc findings list RESOURCE_TYPE/RESOURCE_ID ^
        --source=SOURCE_ID ^
        --location=LOCATION ^
        --filter="category=\"CUSTOM_MODULE_CATEGORY_NAME\""

The response contains a list of findings.

### REST

### Find the source ID

The Security Command Center API's `[RESOURCE_TYPE.sources.list](https://docs.cloud.google.com/security-command-center/docs/reference/security-center-management/rest/v1/organizations.locations.eventThreatDetectionCustomModules/create)` method lists information about Security Command Center finding sources. 

Before using any of the request data, make the following replacements: 

  * `RESOURCE_TYPE`: the type of parent resource (`organizations`, `folders`, or `projects`). 
  * `QUOTA_PROJECT`: the project ID to use for billing and quota tracking. 
  * `RESOURCE_ID`: the numeric identifier for the organization, folder, or project. For projects, you can also use the alphanumeric project ID. 



HTTP method and URL: 
    
    
    GET https://securitycenter.googleapis.com/v2/RESOURCE_TYPE/RESOURCE_ID/sources

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://securitycenter.googleapis.com/v2/RESOURCE_TYPE/RESOURCE_ID/sources"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://securitycenter.googleapis.com/v2/RESOURCE_TYPE/RESOURCE_ID/sources" | Select-Object -Expand Content

The response contains a list of findings.
    
    
    {
      "sources": [
        {
          "name": "organizations/123456789012/sources/9876543210987654321",
          "displayName": "Security Command Center",
          "description": "Detector for misconfigurations within the Security Command Center platform.",
          "canonicalName": "organizations/123456789012/sources/9876543210987654321"
        },
        {
          "name": "organizations/123456789012/sources/8765432109876543210",
          "displayName": "Application Design Center",
          "description": "Provides vulnerabilities on ADC resources.",
          "canonicalName": "organizations/123456789012/sources/8765432109876543210"
        },
        {
          "name": "organizations/123456789012/sources/7654321098765432109",
          "displayName": "Cloud Anomaly Detection",
          "description": "Provider used by Cloud Anomaly Detection",
          "canonicalName": "organizations/123456789012/sources/7654321098765432109"
        },
        {
          "name": "organizations/123456789012/sources/6543210987654321098",
          "displayName": "Vulnerability Assessment",
          "description": "Provider for Vulnerability Assessment.",
          "canonicalName": "organizations/123456789012/sources/6543210987654321098"
        },
        {
          "name": "organizations/123456789012/sources/5432109876543210987",
          "displayName": "Data Security Posture Management",
          "description": "Service to detect drift and post findings",
          "canonicalName": "organizations/123456789012/sources/5432109876543210987"
        },
        {
          "name": "organizations/123456789012/sources/4321098765432109876",
          "displayName": "Notebook Security Scanner",
          "description": "Provider for the Notebook Security Scanner",
          "canonicalName": "organizations/123456789012/sources/4321098765432109876"
        },
        {
          "name": "organizations/123456789012/sources/3210987654321098765",
          "displayName": "GKE Security Posture",
          "description": "Provides actionable security issues on GKE.",
          "canonicalName": "organizations/123456789012/sources/3210987654321098765"
        },
        {
          "name": "organizations/123456789012/sources/2109876543210987654",
          "displayName": "Integrated Vulnerability Scanner",
          "description": "Provider for Integrated Vulnerability Scanner.",
          "canonicalName": "organizations/123456789012/sources/2109876543210987654"
        },
        {
          "name": "organizations/123456789012/sources/1098765432109876543",
          "displayName": "Event Threat Detection Custom Modules",
          "description": "Provider used by Event Threat Detection Custom Modules",
          "canonicalName": "organizations/123456789012/sources/1098765432109876543"
        },
        {
          "name": "organizations/123456789012/sources/9876543210987654321",
          "displayName": "Serverless Vulnerability Detection",
          "description": "Provides vulnerability detection for serverless assets.",
          "canonicalName": "organizations/123456789012/sources/9876543210987654321"
        }
      ]
    }
    

The source ID is the numeric value at the end of the `canonicalName` and `name` fields. 

### List findings for Event Threat Detection custom modules

The Security Command Center API's `[RESOURCE_TYPE.sources.locations.findings.list](https://docs.cloud.google.com/security-command-center/docs/reference/security-center-management/rest/v1/organizations.locations.eventThreatDetectionCustomModules/create)` method lists findings for a source in a specific location. 

Before using any of the request data, make the following replacements: 

  * `QUOTA_PROJECT`: the project ID to use for billing and quota tracking. 
  * `RESOURCE_TYPE`: the type of resource to get (`organizations`, `folders`, or `projects`). 
  * `RESOURCE_ID`: the numeric identifier for the organization, folder, or project to get. For projects, you can also use the alphanumeric project ID. 
  * `LOCATION`: the [Security Command Center location](https://docs.cloud.google.com/security-command-center/docs/data-residency-support#locations) to use, such as `eu`. If data residency is not enabled, use `global`. 
  * `SOURCE_ID`: the numeric identifier for the findings source. 



HTTP method and URL: 
    
    
    GET https://securitycenter.googleapis.com/v2/RESOURCE_TYPE/RESOURCE_ID/sources/SOURCE_ID/locations/LOCATION/findings

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://securitycenter.googleapis.com/v2/RESOURCE_TYPE/RESOURCE_ID/sources/SOURCE_ID/locations/LOCATION/findings"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://securitycenter.googleapis.com/v2/RESOURCE_TYPE/RESOURCE_ID/sources/SOURCE_ID/locations/LOCATION/findings" | Select-Object -Expand Content

The response contains a list of findings.

To learn more about filtering findings, see [Listing security findings](https://docs.cloud.google.com/security-command-center/docs/how-to-api-list-findings).

Findings generated by custom modules can be managed like all findings in Security Command Center. For more information, see the following:

  * [Annotate findings with security marks](https://docs.cloud.google.com/security-command-center/docs/how-to-security-marks-findings)
  * [Setting up finding notifications](https://docs.cloud.google.com/security-command-center/docs/how-to-notifications)
  * [Exporting Security Command Center data](https://docs.cloud.google.com/security-command-center/docs/how-to-export-data)



## Manage Event Threat Detection custom modules

This section describes how to view, list, update, and delete Event Threat Detection custom modules.

### View or list custom modules

By default, when you list custom modules for Event Threat Detection, you see all of the following:

  * All Event Threat Detection custom modules that belong to the organization, folder, or project.
  * All inherited Event Threat Detection custom modules. For example, if you're viewing a project, then the custom modules created in that project's parent organization and folders are included in the results.
  * All Event Threat Detection custom modules created in child resources. For example, if you're in the organization view, then the custom modules in the organization's folders and projects are included in the results.



### Console

  1. [View the modules](https://docs.cloud.google.com/security-command-center/docs/how-to-configure-security-command-center#view-modules) for the **Event Threat Detection** service. The predefined and custom modules appear in a list.
  2. Optional: To view only the custom modules, in the **Filter** box, enter `Type:Custom`.



### gcloud

The [`gcloud scc manage custom-modules etd list`](https://docs.cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/etd/list) command lists all Event Threat Detection custom modules for an organization, folder, or project. 

Before using any of the command data below, make the following replacements: 

  * `RESOURCE_TYPE`: the type of resource that the custom modules belong to (`organization`, `folder`, or `project`). 
  * `RESOURCE_ID`: the numeric identifier for the organization, folder, or project to get. For projects, you can also use the alphanumeric project ID. 



Execute the [`gcloud scc manage custom-modules etd list`](https://docs.cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/etd/list) command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud scc manage custom-modules etd list \
        --RESOURCE_TYPE=RESOURCE_ID

#### Windows (PowerShell)
    
    
    gcloud scc manage custom-modules etd list `
        --RESOURCE_TYPE=RESOURCE_ID

#### Windows (cmd.exe)
    
    
    gcloud scc manage custom-modules etd list ^
        --RESOURCE_TYPE=RESOURCE_ID

You should receive a response similar to the following:
    
    
    - config:
        metadata:
          description: There is a Compute Engine instance in a region that's not allowed.
          recommendation: Delete the instance. If necessary, create a new instance in
            an allowed region.
          severity: MEDIUM
        regions:
        - region: northamerica-northeast1
      displayName: compute_instance_prohibited_region
      enablementState: ENABLED
      name: organizations/123456789012/locations/global/eventThreatDetectionCustomModules/9876543210987654321
      type: CONFIGURABLE_ALLOWED_COMPUTE_ENGINE_REGION
      updateTime: '2026-02-19T01:23:10.237946Z'
    - config:
        metadata:
          description: An IAM custom role contains permissions that aren't allowed.
          recommendation: Remove the permissions from the custom role.
          severity: MEDIUM
        permissions:
        - accessapproval.requests.get
        - accessapproval.requests.invalidate
        - accessapproval.requests.list
        - accessapproval.settings.delete
      displayName: iam_custom_role_prohibited_permissions
      enablementState: ENABLED
      name: organizations/123456789012/locations/global/eventThreatDetectionCustomModules/8765432109876543210
      type: CONFIGURABLE_CUSTOM_ROLE_WITH_PROHIBITED_PERMISSION
      updateTime: '2025-12-23T06:54:15.618430Z'
    

### REST

The Security Command Center Management API's `[RESOURCE_TYPE.locations.eventThreatDetectionCustomModules.list](https://docs.cloud.google.com/security-command-center/docs/reference/security-center-management/rest/v1/organizations.locations.eventThreatDetectionCustomModules/list)` method lists all Event Threat Detection custom modules for an organization, folder, or project. 

Before using any of the request data, make the following replacements: 

  * `RESOURCE_TYPE`: the type of resource that the custom modules belong to (`organizations`, `folders`, or `projects`). 
  * `QUOTA_PROJECT`: the project ID to use for billing and quota tracking. 
  * `RESOURCE_ID`: the numeric identifier for the organization, folder, or project to get. For projects, you can also use the alphanumeric project ID. 



HTTP method and URL: 
    
    
    GET https://securitycentermanagement.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/eventThreatDetectionCustomModules

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: QUOTA_PROJECT" \  
         "https://securitycentermanagement.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/eventThreatDetectionCustomModules"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "QUOTA_PROJECT" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://securitycentermanagement.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/eventThreatDetectionCustomModules" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    [
      {
        "config": {
          "metadata": {
            "description": "There is a Compute Engine instance in a region that's not allowed.",
            "recommendation": "Delete the instance. If necessary, create a new instance in an allowed region.",
            "severity": "MEDIUM"
          },
          "regions": [
            {
              "region": "northamerica-northeast1"
            }
          ]
        },
        "displayName": "compute_instance_prohibited_region",
        "enablementState": "ENABLED",
        "name": "organizations/123456789012/locations/global/eventThreatDetectionCustomModules/9876543210987654321",
        "type": "CONFIGURABLE_ALLOWED_COMPUTE_ENGINE_REGION",
        "updateTime": "2026-02-19T01:23:10.237946Z"
      },
      {
        "config": {
          "metadata": {
            "description": "An IAM custom role contains permissions that aren't allowed.",
            "recommendation": "Remove the permissions from the custom role.",
            "severity": "MEDIUM"
          },
          "permissions": [
            "accessapproval.requests.get",
            "accessapproval.requests.invalidate",
            "accessapproval.requests.list",
            "accessapproval.settings.delete"
          ]
        },
        "displayName": "iam_custom_role_prohibited_permissions",
        "enablementState": "ENABLED",
        "name": "organizations/123456789012/locations/global/eventThreatDetectionCustomModules/8765432109876543210",
        "type": "CONFIGURABLE_CUSTOM_ROLE_WITH_PROHIBITED_PERMISSION",
        "updateTime": "2025-12-23T06:54:15.618430Z"
      }
    ]
    

### Enable or disable a custom module

When you enable or disable a custom module, that change applies to the organization, folder, or project that the custom module belongs to. This resource is the _parent_ of the custom module.

The change can also be inherited by any folders or projects that are descendants of the custom module's parent. For example, if you create a custom module in a folder, then projects within that folder can inherit the custom module's state.

If a custom module's parent is a folder or project, then you must enable or disable the custom module at the same level of the resource hierarchy, or at a lower level. For example, if a custom module's parent is a project, then you can't enable or disable the custom module for an organization or folder; these resource types are always ancestors of projects.

### Console

See [View and edit the modules of a service](https://docs.cloud.google.com/security-command-center/docs/how-to-configure-security-command-center#view-modules).

### gcloud

The [`gcloud scc manage custom-modules etd update`](https://docs.cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/etd/update) command updates the state of a custom module for Event Threat Detection. 

Before using any of the command data below, make the following replacements: 

  * `RESOURCE_TYPE`: the type of resource to update (`organization`, `folder`, or `project`). 
  * `RESOURCE_ID`: the numeric identifier for the organization, folder, or project for the custom module. For projects, you can also use the alphanumeric project ID. 
  * `MODULE_ID`: the numeric identifier for the module 
  * `NEW_STATE`: `ENABLED` to enable the module; `DISABLED` to disable the module; or `INHERITED` to inherit the enablement status of the parent resource (valid only for projects and folders). 



Execute the [`gcloud scc manage custom-modules etd update`](https://docs.cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/etd/update) command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud scc manage custom-modules etd update event-threat-detection MODULE_ID \
        --RESOURCE_TYPE=RESOURCE_ID \
        --enablement-state="NEW_STATE"

#### Windows (PowerShell)
    
    
    gcloud scc manage custom-modules etd update event-threat-detection MODULE_ID `
        --RESOURCE_TYPE=RESOURCE_ID `
        --enablement-state="NEW_STATE"

#### Windows (cmd.exe)
    
    
    gcloud scc manage custom-modules etd update event-threat-detection MODULE_ID ^
        --RESOURCE_TYPE=RESOURCE_ID ^
        --enablement-state="NEW_STATE"

You should receive a response similar to the following:
    
    
    config:
      metadata:
        description: An IAM custom role contains permissions that aren't allowed.
        recommendation: Remove the permissions from the custom role.
        severity: MEDIUM
      permissions:
      - accessapproval.requests.get
      - accessapproval.requests.invalidate
      - accessapproval.requests.list
      - accessapproval.settings.delete
    displayName: iam_custom_role_prohibited_permissions
    enablementState: DISABLED
    name: projects/1234567890123/locations/global/eventThreatDetectionCustomModules/98765432109876543210
    type: CONFIGURABLE_CUSTOM_ROLE_WITH_PROHIBITED_PERMISSION
    updateTime: '2026-03-20T16:52:27.046766Z'
    

### REST

The Security Command Center Management API's `[RESOURCE_TYPE.locations.eventThreatDetectionCustomModules.patch](https://docs.cloud.google.com/security-command-center/docs/reference/security-center-management/rest/v1/organizations.locations.eventThreatDetectionCustomModules/patch)` method updates the state of a custom module for Event Threat Detection. 

Before using any of the request data, make the following replacements: 

  * `RESOURCE_TYPE`: the type of resource to update (`organizations`, `folders`, or `projects`). 
  * `QUOTA_PROJECT`: the project ID to use for billing and quota tracking. 
  * `RESOURCE_ID`: the numeric identifier for the organization, folder, or project for the custom module. For projects, you can also use the alphanumeric project ID. 
  * `MODULE_ID`: the numeric identifier for the module 
  * `NEW_STATE`: `ENABLED` to enable the module; `DISABLED` to disable the module; or `INHERITED` to inherit the enablement status of the parent resource (valid only for projects and folders). 
  * `FIELDS_TO_UPDATE`: optional. A comma-separated list of fields to update. If omitted, all fields are updated. 



HTTP method and URL: 
    
    
    PATCH https://securitycentermanagement.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/eventThreatDetectionCustomModules/MODULE_ID?updateMask=enablementState

Request JSON body: 
    
    
    {
      "enablementState": "NEW_STATE"
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
         "https://securitycentermanagement.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/eventThreatDetectionCustomModules/MODULE_ID?updateMask=enablementState"

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
        -Uri "https://securitycentermanagement.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/eventThreatDetectionCustomModules/MODULE_ID?updateMask=enablementState" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/1234567890123/locations/global/eventThreatDetectionCustomModules/98765432109876543210",
      "config": {
        "metadata": {
          "severity": "MEDIUM",
          "description": "An IAM custom role contains permissions that aren't allowed.",
          "recommendation": "Remove the permissions from the custom role."
        },
        "permissions": [
          "accessapproval.requests.get",
          "accessapproval.requests.invalidate",
          "accessapproval.requests.list",
          "accessapproval.settings.delete"
        ]
      },
      "enablementState": "DISABLED",
      "type": "CONFIGURABLE_CUSTOM_ROLE_WITH_PROHIBITED_PERMISSION",
      "displayName": "iam_custom_role_prohibited_permissions",
      "updateTime": "2026-03-20T16:52:27.046766Z"
    }
    

### Update the definition of a custom module

This section describes how to update a custom module through the Google Cloud console and through the gcloud CLI. Each Event Threat Detection custom module has a size limit of 6 MB.

You can't update the module type of a custom module.

To update a custom module, follow these steps:

### Console

You can edit only residential custom modules. For example, if you're in the organization view, you can edit only the custom modules that were created at the organization level.

  1. [View the modules](https://docs.cloud.google.com/security-command-center/docs/how-to-configure-security-command-center#view-modules) of the **Event Threat Detection** service. The predefined and custom modules appear in a list.
  2. Find the custom module that you want to edit.
  3. For that custom module, click more_vert **Actions** > **Edit**.
  4. Edit the custom module as needed.
  5. Click **Save**.



### gcloud

To update a module, run the following command and include the updated module template JSON:
    
    
     gcloud alpha scc custom-modules etd update CUSTOM_MODULE_ID \
         --RESOURCE_FLAG=RESOURCE_ID \
         --enablement-state="ENABLED" \
         --custom-config-from-file=PATH_TO_JSON_FILE
    

Replace the following:

  * `CUSTOM_MODULE_ID`: the numerical ID of the Event Threat Detection custom module—for example, `1234567890`. You can get the numerical ID from the `name` field of the relevant custom module when you view the list of custom modules.
  * `RESOURCE_FLAG`: the scope of the parent resource where the custom module resides; one of `organization`, `folder`, or `project`.
  * `RESOURCE_ID`: the ID of the parent resource; that is, the organization ID, folder ID, or project ID.
  * `PATH_TO_JSON_FILE`: the JSON file containing the custom module's JSON definition.



### Check the status of a single custom module

### Console

  1. [View the modules](https://docs.cloud.google.com/security-command-center/docs/how-to-configure-security-command-center#view-modules) of the **Event Threat Detection** service. The predefined and custom modules appear in a list.
  2. Find the custom module in the list.

The status of the custom module is shown in the **Status** column.




### gcloud

The [`gcloud scc manage custom-modules etd describe`](https://docs.cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/etd/describe) command gets a Event Threat Detection custom module for an organization, folder, or project. 

Before using any of the command data below, make the following replacements: 

  * `RESOURCE_TYPE`: the type of resource that the custom module belongs to (`organization`, `folder`, or `project`). 
  * `RESOURCE_ID`: the numeric identifier for the organization, folder, or project to get. For projects, you can also use the alphanumeric project ID. 
  * `MODULE_ID`: the numeric identifier for the custom module. 



Execute the [`gcloud scc manage custom-modules etd describe`](https://docs.cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/etd/describe) command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud scc manage custom-modules etd describe MODULE_ID \
        --RESOURCE_TYPE=RESOURCE_ID

#### Windows (PowerShell)
    
    
    gcloud scc manage custom-modules etd describe MODULE_ID `
        --RESOURCE_TYPE=RESOURCE_ID

#### Windows (cmd.exe)
    
    
    gcloud scc manage custom-modules etd describe MODULE_ID ^
        --RESOURCE_TYPE=RESOURCE_ID

You should receive a response similar to the following:
    
    
    config:
      metadata:
        description: An IAM custom role contains permissions that aren't allowed.
        recommendation: Remove the permissions from the custom role.
        severity: MEDIUM
      permissions:
      - accessapproval.requests.get
      - accessapproval.requests.invalidate
      - accessapproval.requests.list
      - accessapproval.settings.delete
    displayName: iam_custom_role_prohibited_permissions
    enablementState: ENABLED
    name: organizations/123456789012/locations/global/eventThreatDetectionCustomModules/8765432109876543210
    type: CONFIGURABLE_CUSTOM_ROLE_WITH_PROHIBITED_PERMISSION
    updateTime: '2025-12-23T06:54:15.618430Z'
    

### REST

The Security Command Center Management API's `[RESOURCE_TYPE.locations.eventThreatDetectionCustomModules.get](https://docs.cloud.google.com/security-command-center/docs/reference/security-center-management/rest/v1/organizations.locations.eventThreatDetectionCustomModules/get)` method gets a Event Threat Detection custom module for an organization, folder, or project. 

Before using any of the request data, make the following replacements: 

  * `RESOURCE_TYPE`: the type of resource that the custom module belongs to (`organizations`, `folders`, or `projects`). 
  * `QUOTA_PROJECT`: the project ID to use for billing and quota tracking. 
  * `RESOURCE_ID`: the numeric identifier for the organization, folder, or project to get. For projects, you can also use the alphanumeric project ID. 
  * `MODULE_ID`: the numeric identifier for the custom module. 



HTTP method and URL: 
    
    
    GET https://securitycentermanagement.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/eventThreatDetectionCustomModules/MODULE_ID

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: QUOTA_PROJECT" \  
         "https://securitycentermanagement.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/eventThreatDetectionCustomModules/MODULE_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "QUOTA_PROJECT" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://securitycentermanagement.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/eventThreatDetectionCustomModules/MODULE_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "config": {
        "metadata": {
          "description": "An IAM custom role contains permissions that aren't allowed.",
          "recommendation": "Remove the permissions from the custom role.",
          "severity": "MEDIUM"
        },
        "permissions": [
          "accessapproval.requests.get",
          "accessapproval.requests.invalidate",
          "accessapproval.requests.list",
          "accessapproval.settings.delete"
        ]
      },
      "displayName": "iam_custom_role_prohibited_permissions",
      "enablementState": "ENABLED",
      "name": "organizations/123456789012/locations/global/eventThreatDetectionCustomModules/8765432109876543210",
      "type": "CONFIGURABLE_CUSTOM_ROLE_WITH_PROHIBITED_PERMISSION",
      "updateTime": "2025-12-23T06:54:15.618430Z"
    }
    

### Delete a custom module

When you delete an Event Threat Detection custom module, the findings that it has generated aren't modified and remain available in Security Command Center. In contrast, when you delete a [Security Health Analytics custom module](https://docs.cloud.google.com/security-command-center/docs/custom-modules-sha-overview), its generated findings are marked as inactive.

You can't recover a deleted custom module.

### Console

You can't delete inherited custom modules. For example, if you're in the project view, you can't delete custom modules that were created at the folder or organization level.

To delete a custom module through the Google Cloud console, do the following:

  1. [View the modules](https://docs.cloud.google.com/security-command-center/docs/how-to-configure-security-command-center#view-modules) of the **Event Threat Detection** service. The predefined and custom modules appear in a list.
  2. Find the custom module that you want to delete.
  3. For that custom module, click more_vert **Actions** > **Delete**. A message appears prompting you to confirm the deletion.
  4. Click **Delete**.



### gcloud

The [`gcloud scc manage custom-modules etd delete`](https://docs.cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/etd/delete) command creates an Event Threat Detection custom module for an organization, folder, or project. 

Before using any of the command data below, make the following replacements: 

  * `RESOURCE_TYPE`: the type of resource that the custom modules belong to (`organization`, `folder`, or `project`). 
  * `RESOURCE_ID`: the numeric identifier for the organization, folder, or project for the custom module. For projects, you can also use the alphanumeric project ID. 
  * `MODULE_ID`: the numeric identifier for the custom module. 



Execute the [`gcloud scc manage custom-modules etd delete`](https://docs.cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/etd/delete) command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud scc manage custom-modules etd delete MODULE_ID \
        --RESOURCE_TYPE=RESOURCE_ID

#### Windows (PowerShell)
    
    
    gcloud scc manage custom-modules etd delete MODULE_ID `
        --RESOURCE_TYPE=RESOURCE_ID

#### Windows (cmd.exe)
    
    
    gcloud scc manage custom-modules etd delete MODULE_ID ^
        --RESOURCE_TYPE=RESOURCE_ID

You should receive a response similar to the following:
    
    
    Deleted [projects/1234567890123/locations/global/eventThreatDetectionCustomModules/98765432109876543210].
    

### REST

The Security Command Center Management API's `[RESOURCE_TYPE.locations.eventThreatDetectionCustomModules.delete](https://docs.cloud.google.com/security-command-center/docs/reference/security-center-management/rest/v1/organizations.locations.eventThreatDetectionCustomModules/delete)` method creates an Event Threat Detection custom module for an organization, folder, or project. 

Before using any of the request data, make the following replacements: 

  * `RESOURCE_TYPE`: the type of resource that the custom module will belong to (`organizations`, `folders`, or `projects`) 
  * `QUOTA_PROJECT`: the project ID to use for billing and quota tracking. 
  * `RESOURCE_ID`: the numeric identifier for the organization, folder, or project for the custom module. For projects, you can also use the alphanumeric project ID. 
  * `MODULE_ID`: the numeric identifier for the custom module. 



HTTP method and URL: 
    
    
    DELETE https://securitycentermanagement.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/eventThreatDetectionCustomModules/MODULE_ID

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: QUOTA_PROJECT" \  
         "https://securitycentermanagement.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/eventThreatDetectionCustomModules/MODULE_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "QUOTA_PROJECT" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://securitycentermanagement.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/eventThreatDetectionCustomModules/MODULE_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {}
    

### Clone a custom module

When you clone a custom module, the resulting custom module is created as a resident of the resource that you're viewing. For example, if you clone a custom module that your project inherited from the organization, the new custom module is a residential module in the project.

You can't clone a descendant custom module.

**Note:** There is no `gcloud` command for cloning a custom module. To emulate the cloning process, you can run a `get` command to get the settings of a custom module and then run a `create` command to create a new module with the same settings.

To clone a custom module through the Google Cloud console, do the following:

  1. [View the modules](https://docs.cloud.google.com/security-command-center/docs/how-to-configure-security-command-center#view-modules) of the **Event Threat Detection** service. The predefined and custom modules appear in a list.
  2. Find the custom module that you want to clone.
  3. For that custom module, click more_vert **Actions** > **Clone**.
  4. Edit the custom module as needed.
  5. Click **Create**.



## What's next

  * Learn more about [custom modules for Event Threat Detection](https://docs.cloud.google.com/security-command-center/docs/custom-modules-etd-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
