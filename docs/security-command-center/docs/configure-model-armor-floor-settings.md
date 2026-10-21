---
url: https://docs.cloud.google.com/security-command-center/docs/configure-model-armor-floor-settings/
title: Configure floor settings \u00a0|\u00a0 Model Armor \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T08:30:20.671811+00:00
---

# Configure floor settings  |  Model Armor  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/configure-model-armor-floor-settings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Model Armor ](https://docs.cloud.google.com/model-armor)
  * [ Guides ](https://docs.cloud.google.com/model-armor/overview)



Send feedback 

#  Configure floor settings Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to view and update Model Armor floor settings and provides an example of a floor setting violation.

Floor settings serve two primary purposes:

  * Template conformance: Ensure new templates are at least as restrictive as those defined in the floor settings. Template conformance is defined at the organization and folder levels.

  * Inline enforcement: Apply Model Armor protections to Gemini models and Google Cloud MCP servers. Inline enforcement is configured at the project level. If you use floor settings for inline enforcement, any template that you create in the project must conform to those floor settings.




## When to use floor settings

The following are some common use cases:

  * **Enforce template compliance and prevent policy regressions** : Define minimum filter thresholds at the organization, folder, or project level to ensure that newly created and updated templates meet your security standards and can't lower protection below established baselines.
  * **Enable inline enforcement for models and tools** : Help protect supported Gemini models and Google Cloud remote MCP servers at the project level without altering application code.
  * **Govern decentralized team configurations** : Allow autonomous project teams to create custom templates while guaranteeing that their settings conform to organizational governance policies.



## Before you begin

Before you begin, complete the following tasks.

### Obtain the required permissions

To get the permissions that you need to manage floor settings, ask your administrator to grant you the [Model Armor Floor Setting Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/modelarmor#modelarmor.floorSettingsAdmin) (`roles/modelarmor.floorSettingsAdmin`) IAM role on Model Armor floor settings. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Enable APIs

You must enable the Model Armor API before you can use Model Armor.

###  Console 

  1. Enable the Model Armor API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=modelarmor.googleapis.com)

  2. Select the project where you want to activate Model Armor.




###  gcloud 

Before you begin, follow these steps using the Google Cloud CLI with the Model Armor API:

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Enable the Model Armor API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable modelarmor.googleapis.com

  3. Set the API endpoint override using the gcloud CLI.




### Set the API endpoint override using the gcloud CLI

This step is only required if you use the gcloud CLI with Model Armor and want to use a region or multi-region other than the default `us` multi-region. You must manually set the API endpoint override to ensure the gcloud CLI correctly routes requests to the Model Armor service.

Run the following command to use the global API endpoint:
    
    
    gcloud config set api_endpoint_overrides/modelarmor "https://modelarmor.googleapis.com/"

## Floor settings application

Local settings are always applied. For example, if floor settings conflict, the settings lower in the resource hierarchy take precedence. Similarly, project-level floor settings override conflicting folder-level floor settings.

The following table lists how floor settings are applied at different levels:

Floor settings level | Application  
---|---  
Organization level | Applies to everything within the organization.  
Folder level | Applies to all projects inside that specific folder.  
Project level | Applies only to that one specific project.  
  
To illustrate how floor settings are applied when set at different levels, consider the following example scenario. For example, suppose you set floor settings as follows:

  * Folder-level (less specific) floor settings: All content in this folder must enable a malicious URI filter.
  * Project-level (more specific) floor settings: Your project in the folder must use prompt injection and jailbreak detection with medium confidence.



In this scenario, the settings result in the following:

  * Any template you create in your project must include the prompt injection and jailbreak detection filter because the project-level settings always take precedence over folder-level settings.

  * A template created in a different project or folder isn't affected by the malicious URI filter rule from the first folder.




Floor settings apply only within their specific level in the hierarchy, unless set at the organization level, in which case, they apply throughout the organization.

## Templates and floor settings conformance

When a Model Armor template is created or updated, Model Armor checks whether the template's configuration conforms with the floor settings. You cannot create or update a template that's less strict than the floor settings.

You can set floor settings at the organization, folder, and project levels. The user interface is available only at the project level and lets you inherit organization-level or folder-level settings. To set floor settings at the organization or folder level, you must use the API.

Template conformance validates template configurations. Data inspection uses the configurations defined in a conformant template to analyze prompts or responses during runtime. The following table describes how template conformance and data inspection apply to templates and floor settings.

Check | Floor settings | Templates  
---|---|---  
Template conformance | Configured at the organization, folder, or project level.  
Note: Sensitive Data Protection can be set to enforce data security policies on the templates. However, it does not validate the template conformance. | Configured only at the project level.  
Data inspection | Enforced only at the project level using the inspect and block mode. | Enforced using REST API, Service Extensions, Gemini Enterprise, and Agent Runtime.  
  
## Integration with Gemini Enterprise Agent Platform and Google Cloud MCP servers

Model Armor integrates with Agent Platform and Google Cloud MCP servers to screen requests and responses from Gemini models and Google Cloud remote MCP servers based on the floor settings you define. You must enable Cloud Logging to view prompts and responses. For more information, see [Model Armor integration with Gemini Enterprise Agent Platform](https://docs.cloud.google.com/model-armor/model-armor-vertex-integration) and [Model Armor integration with Google Cloud MCP servers](https://docs.cloud.google.com/model-armor/model-armor-mcp-google-cloud-integration).

## Floor settings filter versions

Floor settings use the `Stable` [filter version](https://docs.cloud.google.com/model-armor/set-filter-version) by default. The following list describes how filter versions work with each integration:

  * [Integration with Gemini Enterprise Agent Platform](https://docs.cloud.google.com/model-armor/model-armor-vertex-integration): if you want to override this setting, specify a template in the `generateContent` call to the Gemini model.
  * [Integration with Google and Google Cloud MCP servers](https://docs.cloud.google.com/model-armor/model-armor-mcp-google-cloud-integration): you can't override the filter version because this integration only supports floor settings.



## Configure floor settings

Configure floor settings to define the minimum detection thresholds for Model Armor templates. These settings ensure that all new and modified templates meet specific requirements.

To configure floor settings, do the following:

  1. In the Google Cloud console, go to the **Model Armor** page. 

[Go to Model Armor](https://console.cloud.google.com/projectselector2/security/modelarmor?supportedpurview=organizationId,folder,project)

  2. Select a project.
  3. On the **Model Armor** page, go to the **Floor settings** tab and click **Configure floor settings**.
  4. On the **Configure floor settings** page, select the configuration option.
  5. In the **Detections** section, [configure the detection settings](https://docs.cloud.google.com/model-armor/manage-templates#configure-detections).
  6. Optional: If you select Sensitive Data Protection detection, configure the [Sensitive Data Protection settings](https://docs.cloud.google.com/model-armor/manage-templates#set-sdp-settings).
  7. In the **Responsible AI** section, [set the confidence level for each content filter](https://docs.cloud.google.com/model-armor/manage-templates#set-confidence-level).

**Note:** If you don't specify a confidence level, it defaults to **Medium and above**.
  8. In the **Services** section, select the services where these floor settings apply.

  9. In the **Logs** section, select **Enable Cloud Logging** to log all user prompts, model responses, and the floor settings detector results.

  10. Select **Enable multi-language support** to use the [multi-language detection settings](https://docs.cloud.google.com/model-armor/overview#languages-supported%7D).

  11. Click **Save floor settings**.




Allow a few minutes for the changes to the floor settings to take effect.

## Define how floor settings are inherited

When configuring floor settings, select the configuration option.

  * **Inherit parent's floor settings** : Inherit floor settings set earlier in the resource hierarchy. Click **Save floor settings** and skip the remaining steps. To view the inherited settings, go to the **Floor settings** tab.

**Note:** When you enable inheritance, the inherited settings override existing floor settings.
  * **Custom** : Define floor settings for this project. Custom settings that you define for a project override any inherited floor settings.

  * **Disable** : Disable any inherited floor settings. This means no detection rules apply to the Model Armor templates and Agent Platform for your Gemini workloads. Click **Save floor settings** and skip the remaining steps. View the disabled status on the **Floor settings** tab.




## Define where floor settings are applied

Select one of the following services where the configured floor settings apply.

  * **Model Armor - Template creation & update**: Model Armor checks every new and modified Model Armor template in a project to ensure that the minimum settings align with the floor settings.

**Note:** Floor settings don't check templates for Sensitive Data Protection conformance.
  * **Google MCP Server** : Floor settings check requests sent to or from Google or Google Cloud remote MCP servers to ensure they meet the floor setting thresholds. For more information, see [Model Armor integration with Google Cloud MCP servers](https://docs.cloud.google.com/model-armor/model-armor-mcp-google-cloud-integration) ([Preview](https://cloud.google.com/products#product-launch-stages)).

  * **Agent Platform** : Screen requests sent to Gemini models, and then log or block requests that meet floor settings thresholds.

If you select **Agent Platform** , the **Agent Platform** section appears where you choose how floor settings are enforced.

    * **Inspect only** : Detect requests that don't meet floor settings but don't block them.
    * **Inspect and block violations** : Detect and block requests that don't meet the floor settings.



## View Model Armor floor settings

View Model Armor floor settings to verify existing settings, to identify the minimum requirements for your AI applications, or to troubleshoot issues when a template is not behaving as expected.

Run the following command to view the Model Armor floor settings.

### Console

  1. In the Google Cloud console, go to the **Model Armor** page.

[Go to Model Armor](https://console.cloud.google.com/projectselector2/security/modelarmor?supportedpurview=organizationId,folder,project)

  2. Verify that you are viewing the project that you activated Model Armor on.

  3. On the **Model Armor** page, go to the **Floor settings** tab. If floor settings are set at the organization level, you can view them. If no floor settings are defined, you must configure them. For more information, see Configure floor settings.




### gcloud

  * View the Model Armor floor setting for a project.
        
        gcloud model-armor floorsettings describe \
              --full-uri='projects/PROJECT_ID/locations/global/floorSetting'

  * View the Model Armor floor setting for an organization.
        
        gcloud model-armor floorsettings describe \
              --full-uri='organizations/ORGANIZATION_ID/locations/global/floorSetting'

  * View the Model Armor floor setting for a folder.
        
        gcloud model-armor floorsettings describe \
               --full-uri='folders/FOLDER_ID/locations/global/floorSetting'

Replace the following:

    * The ID of the project for the floor settings.
    * The ID of the folder for the floor settings.
    * The ID of the organization for the floor settings.



### REST

  * View the Model Armor floor setting for a project.
        
        curl -X GET \
          -H "Authorization: Bearer $(gcloud auth print-access-token)" \
          -H "Content-Type: application/json" \
          "https://modelarmor.googleapis.com/v1/projects/PROJECT_ID/locations/global/floorSetting"

  * View the Model Armor floor setting for a folder.
        
        curl -X GET \
          -H "Authorization: Bearer $(gcloud auth print-access-token)" \
          -H "Content-Type: application/json" \
          "https://modelarmor.googleapis.com/v1/folders/FOLDER_ID/locations/global/floorSetting"

  * View the Model Armor floor setting for an organization.
        
        curl -X GET \
          -H "Authorization: Bearer $(gcloud auth print-access-token)" \
          -H "Content-Type: application/json" \
          "https://modelarmor.googleapis.com/v1/organizations/ORGANIZATION_ID/locations/global/floorSetting"




Replace the following:

  * The ID of the project for the floor settings.
  * The ID of the folder for the floor settings.
  * The ID of the organization for the floor settings.



###  C# 

To run this code, first [set up a C# development environment](https://docs.cloud.google.com/dotnet/docs/setup) and [install the Model Armor C# SDK](https://docs.cloud.google.com/model-armor//reference/libraries#client-libraries-install-csharp).

  * View the Model Armor floor setting for a given project.
        
        using [Google.Cloud.ModelArmor.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.html);
        using System;
        
        public class GetProjectFloorSettings
        {
            public FloorSetting GetProjectFloorSetting(string projectId)
            {
                // Initialize client
                [ModelArmorClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.ModelArmorClient.html) client = [ModelArmorClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.ModelArmorClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.ModelArmorClient.html#Google_Cloud_ModelArmor_V1_ModelArmorClient_Create)();
        
                // Construct the resource name
                string name = $"projects/{projectId}/locations/global/floorSetting";
        
                // Create the request
                [GetFloorSettingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.GetFloorSettingRequest.html) request = new [GetFloorSettingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.GetFloorSettingRequest.html) { Name = name };
        
                // Make the request
                [FloorSetting](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.FloorSetting.html) response = client.[GetFloorSetting](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.ModelArmorClient.html#Google_Cloud_ModelArmor_V1_ModelArmorClient_GetFloorSetting_Google_Cloud_ModelArmor_V1_FloorSettingName_Google_Api_Gax_Grpc_CallSettings_)(request);
        
                Console.WriteLine($"Floor settings retrieved successfully: {response}");
        
                return response;
            }
        }

  * View the Model Armor floor setting for a given folder.
        
        using [Google.Cloud.ModelArmor.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.html);
        using System;
        
        public class GetFolderFloorSettings
        {
            public FloorSetting GetFolderFloorSetting(string folderId)
            {
                // Initialize client.
                [ModelArmorClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.ModelArmorClient.html) client = [ModelArmorClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.ModelArmorClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.ModelArmorClient.html#Google_Cloud_ModelArmor_V1_ModelArmorClient_Create)();
        
                // Construct the resource name.
                string name = $"folders/{folderId}/locations/global/floorSetting";
        
                // Create the request.
                [GetFloorSettingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.GetFloorSettingRequest.html) request = new [GetFloorSettingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.GetFloorSettingRequest.html) { Name = name };
        
                // Make the request.
                [FloorSetting](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.FloorSetting.html) response = client.[GetFloorSetting](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.ModelArmorClient.html#Google_Cloud_ModelArmor_V1_ModelArmorClient_GetFloorSetting_Google_Cloud_ModelArmor_V1_FloorSettingName_Google_Api_Gax_Grpc_CallSettings_)(request);
        
                return response;
            }
        }

  * View the Model Armor floor setting for a given organization.
        
        using [Google.Cloud.ModelArmor.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.html);
        using System;
        
        public class GetOrganizationFloorSettings
        {
            public FloorSetting GetOrganizationFloorSetting(string organizationId)
            {
                // Initialize client
                [ModelArmorClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.ModelArmorClient.html) client = [ModelArmorClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.ModelArmorClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.ModelArmorClient.html#Google_Cloud_ModelArmor_V1_ModelArmorClient_Create)();
        
                // Construct the resource name
                string name = $"organizations/{organizationId}/locations/global/floorSetting";
        
                // Create the request
                [GetFloorSettingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.GetFloorSettingRequest.html) request = new [GetFloorSettingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.GetFloorSettingRequest.html) { Name = name };
        
                // Make the request
                [FloorSetting](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.FloorSetting.html) response = client.[GetFloorSetting](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.ModelArmorClient.html#Google_Cloud_ModelArmor_V1_ModelArmorClient_GetFloorSetting_Google_Cloud_ModelArmor_V1_FloorSettingName_Google_Api_Gax_Grpc_CallSettings_)(request);
        
                Console.WriteLine($"Floor settings retrieved successfully: {response}");
        
                return response;
            }
        }




###  Go 

To run this code, first [set up a Go development environment](https://docs.cloud.google.com/go/docs/setup) and [install the Model Armor Go SDK](https://docs.cloud.google.com/model-armor/reference/libraries#client-libraries-install-go).

  * View the Model Armor floor setting for a given project.
        
        import (
        	"context"
        	"fmt"
        	"io"
        
        	modelarmor "cloud.google.com/go/modelarmor/apiv1"
        	modelarmorpb "cloud.google.com/go/modelarmor/apiv1/modelarmorpb"
        )
        
        // getProjectFloorSettings gets details of a single floor setting of a project.
        //
        // This method retrieves the details of a single floor setting of a project.
        //
        // w io.Writer: The writer to use for logging.
        // projectID string: The ID of the project.
        func getProjectFloorSettings(w io.Writer, projectID string) error {
        	ctx := context.Background()
        
        	// Create the Model Armor client.
        	client, err := modelarmor.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/modelarmor/latest/apiv1.html#cloud_google_com_go_modelarmor_apiv1_Client_NewClient)(ctx)
        	if err != nil {
        		return fmt.Errorf("failed to create client: %w", err)
        	}
        	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/modelarmor/latest/apiv1.html#cloud_google_com_go_modelarmor_apiv1_Client_Close)()
        
        	floorSettingsName := fmt.Sprintf("projects/%s/locations/global/floorSetting", projectID)
        
        	// Get the project floor setting.
        	req := &modelarmorpb.GetFloorSettingRequest{
        		Name: floorSettingsName,
        	}
        
        	response, err := client.GetFloorSetting(ctx, req)
        	if err != nil {
        		return fmt.Errorf("failed to get floor setting: %w", err)
        	}
        
        	// Print the retrieved floor setting using fmt.Fprintf with the io.Writer.
        	fmt.Fprintf(w, "Retrieved floor setting: %v\n", response)
        
        	return nil
        }
        

  * View the Model Armor floor setting for a given folder.
        
        import (
        	"context"
        	"fmt"
        	"io"
        
        	modelarmor "cloud.google.com/go/modelarmor/apiv1"
        	modelarmorpb "cloud.google.com/go/modelarmor/apiv1/modelarmorpb"
        )
        
        // getFolderFloorSettings gets details of a single floor setting of a folder.
        //
        // This method retrieves the details of a single floor setting of a folder.
        //
        // w io.Writer: The writer to use for logging.
        // folderID string: The ID of the folder.
        func getFolderFloorSettings(w io.Writer, folderID string) error {
        	ctx := context.Background()
        
        	// Create the Model Armor client.
        	client, err := modelarmor.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/modelarmor/latest/apiv1.html#cloud_google_com_go_modelarmor_apiv1_Client_NewClient)(ctx)
        	if err != nil {
        		return fmt.Errorf("failed to create client: %w", err)
        	}
        	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/modelarmor/latest/apiv1.html#cloud_google_com_go_modelarmor_apiv1_Client_Close)()
        
        	// Prepare folder floor setting path/name
        	floorSettingsName := fmt.Sprintf("folders/%s/locations/global/floorSetting", folderID)
        
        	// Get the folder floor setting.
        	req := &modelarmorpb.GetFloorSettingRequest{
        		Name: floorSettingsName,
        	}
        
        	response, err := client.GetFloorSetting(ctx, req)
        	if err != nil {
        		return fmt.Errorf("failed to get floor setting: %w", err)
        	}
        
        	// Print the retrieved floor setting using fmt.Fprintf with the io.Writer.
        	fmt.Fprintf(w, "Retrieved folder floor setting: %v\n", response)
        
        	return nil
        }
        

  * View the Model Armor floor setting for a given organization.
        
        import (
        	"context"
        	"fmt"
        	"io"
        
        	modelarmor "cloud.google.com/go/modelarmor/apiv1"
        	modelarmorpb "cloud.google.com/go/modelarmor/apiv1/modelarmorpb"
        )
        
        // getOrganizationFloorSettings gets details of a single floor setting of an organization.
        //
        // This method retrieves the details of a single floor setting of an organization.
        //
        // w io.Writer: The writer to use for logging.
        // organizationID string: The ID of the organization.
        func getOrganizationFloorSettings(w io.Writer, organizationID string) error {
        	ctx := context.Background()
        
        	// Create the Model Armor client.
        	client, err := modelarmor.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/modelarmor/latest/apiv1.html#cloud_google_com_go_modelarmor_apiv1_Client_NewClient)(ctx)
        	if err != nil {
        		return fmt.Errorf("failed to create client: %w", err)
        	}
        	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/modelarmor/latest/apiv1.html#cloud_google_com_go_modelarmor_apiv1_Client_Close)()
        
        	floorSettingsName := fmt.Sprintf("organizations/%s/locations/global/floorSetting", organizationID)
        
        	// Get the organization floor setting.
        	req := &modelarmorpb.GetFloorSettingRequest{
        		Name: floorSettingsName,
        	}
        
        	response, err := client.GetFloorSetting(ctx, req)
        	if err != nil {
        		return fmt.Errorf("failed to get floor setting: %w", err)
        	}
        
        	// Print the retrieved floor setting using fmt.Fprintf with the io.Writer.
        	fmt.Fprintf(w, "Retrieved org floor setting: %v\n", response)
        
        	return nil
        }
        




###  Java 

To run this code, first [set up a Java development environment](https://docs.cloud.google.com/java/docs/setup) and [install the Model Armor Java SDK](https://docs.cloud.google.com/model-armor/reference/libraries#install-java).

  * View the Model Armor floor setting for a given project.
        
        import com.google.cloud.modelarmor.v1.[FloorSetting](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.FloorSetting.html);
        import com.google.cloud.modelarmor.v1.[FloorSettingName](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.FloorSettingName.html);
        import com.google.cloud.modelarmor.v1.[GetFloorSettingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.GetFloorSettingRequest.html);
        import com.google.cloud.modelarmor.v1.[ModelArmorClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.ModelArmorClient.html);
        import java.io.IOException;
        
        public class GetProjectFloorSetting {
        
          public static void main(String[] args) throws IOException {
            // TODO(developer): Replace these variables before running the sample.
            String projectId = "your-project-id";
        
            getProjectFloorSetting(projectId);
          }
        
          public static [FloorSetting](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.FloorSetting.html) getProjectFloorSetting(String projectId) throws IOException {
        
            // Initialize client that will be used to send requests. This client only
            // needs to be created once, and can be reused for multiple requests.
            try ([ModelArmorClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.ModelArmorClient.html) client = [ModelArmorClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.ModelArmorClient.html).create()) {
              String name = [FloorSettingName](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.FloorSettingName.html).of(projectId, "global").toString();
        
              [GetFloorSettingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.GetFloorSettingRequest.html) request = [GetFloorSettingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.GetFloorSettingRequest.html).newBuilder().setName(name).build();
        
              [FloorSetting](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.FloorSetting.html) floorSetting = client.getFloorSetting(request);
              System.out.println("Fetched floor setting for project: " + projectId);
        
              return floorSetting;
            }
          }
        }

  * View the Model Armor floor setting for a given folder.
        
        import com.google.cloud.modelarmor.v1.[FloorSetting](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.FloorSetting.html);
        import com.google.cloud.modelarmor.v1.[FloorSettingName](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.FloorSettingName.html);
        import com.google.cloud.modelarmor.v1.[GetFloorSettingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.GetFloorSettingRequest.html);
        import com.google.cloud.modelarmor.v1.[ModelArmorClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.ModelArmorClient.html);
        import java.io.IOException;
        
        public class GetFolderFloorSetting {
        
          public static void main(String[] args) throws IOException {
            // TODO(developer): Replace these variables before running the sample.
            String folderId = "your-folder-id";
        
            getFolderFloorSetting(folderId);
          }
        
          public static [FloorSetting](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.FloorSetting.html) getFolderFloorSetting(String folderId) throws IOException {
        
            // Initialize client that will be used to send requests. This client only
            // needs to be created once, and can be reused for multiple requests.
            try ([ModelArmorClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.ModelArmorClient.html) client = [ModelArmorClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.ModelArmorClient.html).create()) {
              String name = [FloorSettingName](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.FloorSettingName.html).[ofFolderLocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.FloorSettingName.html#com_google_cloud_modelarmor_v1_FloorSettingName_ofFolderLocationName_java_lang_String_java_lang_String_)(folderId, "global").toString();
        
              [GetFloorSettingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.GetFloorSettingRequest.html) request = [GetFloorSettingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.GetFloorSettingRequest.html).newBuilder().setName(name).build();
        
              [FloorSetting](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.FloorSetting.html) floorSetting = client.getFloorSetting(request);
              System.out.println("Fetched floor setting for folder: " + folderId);
        
              return floorSetting;
            }
          }
        }

  * View the Model Armor floor setting for a given organization.
        
        import com.google.cloud.modelarmor.v1.[FloorSetting](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.FloorSetting.html);
        import com.google.cloud.modelarmor.v1.[FloorSettingName](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.FloorSettingName.html);
        import com.google.cloud.modelarmor.v1.[GetFloorSettingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.GetFloorSettingRequest.html);
        import com.google.cloud.modelarmor.v1.[ModelArmorClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.ModelArmorClient.html);
        import java.io.IOException;
        
        public class GetOrganizationFloorSetting {
        
          public static void main(String[] args) throws IOException {
            // TODO(developer): Replace these variables before running the sample.
            String organizationId = "your-organization-id";
        
            getOrganizationFloorSetting(organizationId);
          }
        
          public static [FloorSetting](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.FloorSetting.html) getOrganizationFloorSetting(String organizationId) throws IOException {
        
            // Initialize client that will be used to send requests. This client only
            // needs to be created once, and can be reused for multiple requests.
            try ([ModelArmorClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.ModelArmorClient.html) client = [ModelArmorClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.ModelArmorClient.html).create()) {
              String name = [FloorSettingName](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.FloorSettingName.html).[ofOrganizationLocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.FloorSettingName.html#com_google_cloud_modelarmor_v1_FloorSettingName_ofOrganizationLocationName_java_lang_String_java_lang_String_)(organizationId, "global")
                  .toString();
        
              [GetFloorSettingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.GetFloorSettingRequest.html) request = [GetFloorSettingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.GetFloorSettingRequest.html).newBuilder().setName(name).build();
        
              [FloorSetting](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.FloorSetting.html) floorSetting = client.getFloorSetting(request);
              System.out.println("Fetched floor setting for organization: " + organizationId);
        
              return floorSetting;
            }
          }
        }




###  Node.js 

To run this code, first [set up a Node.js development environment](https://docs.cloud.google.com/nodejs/docs/setup) and [install the Model Armor Node.js SDK](https://docs.cloud.google.com/model-armor/reference/libraries#install).

  * View the Model Armor floor setting for a given project.
        
        /**
         * TODO(developer): Uncomment these variables before running the sample.
         */
        // const projectId = 'your-project-id';
        
        const name = `projects/${projectId}/locations/global/floorSetting`;
        
        // Imports the Modelarmor library
        const {ModelArmorClient} = require('[@google-cloud/modelarmor](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/overview.html)').v1;
        
        // Instantiates a client
        const modelarmorClient = new [ModelArmorClient](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/overview.html)();
        
        async function getProjectFloorSettings() {
          // Construct request
          const request = {
            name,
          };
        
          // Run request
          const [response] = await modelarmorClient.getFloorSetting(request);
          return response;
        }
        
        return await getProjectFloorSettings();

  * View the Model Armor floor setting for a given folder.
        
        /**
         * TODO(developer): Uncomment these variables before running the sample.
         */
        // const folderId = 'your-folder-id';
        
        const name = `folders/${folderId}/locations/global/floorSetting`;
        
        // Imports the Modelarmor library
        const {ModelArmorClient} = require('[@google-cloud/modelarmor](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/overview.html)').v1;
        
        // Instantiates a client
        const modelarmorClient = new [ModelArmorClient](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/overview.html)();
        
        async function getFolderFloorSettings() {
          // Construct request
          const request = {
            name,
          };
        
          const [response] = await modelarmorClient.getFloorSetting(request);
          return response;
        }
        
        return await getFolderFloorSettings();

  * View the Model Armor floor setting for a given organization.
        
        /**
         * TODO(developer): Uncomment these variables before running the sample.
         */
        // const organizationId = 'your-organization-id';
        const name = `organizations/${organizationId}/locations/global/floorSetting`;
        
        // Imports the Modelarmor library
        const {ModelArmorClient} = require('[@google-cloud/modelarmor](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/overview.html)').v1;
        
        // Instantiates a client
        const modelarmorClient = new [ModelArmorClient](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/overview.html)();
        
        async function getOrganizationFloorSettings() {
          // Construct request
          const request = {
            name,
          };
        
          // Run request
          const [response] = await modelarmorClient.getFloorSetting(request);
          return response;
        }
        
        return await getOrganizationFloorSettings();




###  PHP 

To run this code, first [set up a PHP development environment](https://docs.cloud.google.com/php/docs/setup) and [install the Model Armor PHP SDK](https://docs.cloud.google.com/model-armor/reference/libraries#install).

  * View the Model Armor floor setting for a given project.
        
        use Google\Cloud\ModelArmor\V1\Client\ModelArmorClient;
        use Google\Cloud\ModelArmor\V1\GetFloorSettingRequest;
        
        /**
         * Gets the floor settings for a given project.
         *
         * @param string $projectId The project Id for which the floor settings is to be retrieved.
         *
         */
        function get_project_floor_settings(string $projectId): void
        {
            $client = new ModelArmorClient();
        
            $floorSettingsName = sprintf('projects/%s/locations/global/floorSetting', $projectId);
        
            $response = $client->getFloorSetting((new GetFloorSettingRequest())->setName($floorSettingsName));
        
            printf("Floor settings retrieved successfully: %s\n", $response->serializeToJsonString());
        }

  * View the Model Armor floor setting for a given folder.
        
        use Google\Cloud\ModelArmor\V1\Client\ModelArmorClient;
        use Google\Cloud\ModelArmor\V1\GetFloorSettingRequest;
        
        /**
         * Gets the floor settings for a given folder.
         *
         * @param string $folderId The folder Id for which the floor settings is to be retrieved.
         *
         */
        function get_folder_floor_settings(string $folderId): void
        {
            $client = new ModelArmorClient();
        
            $floorSettingsName = sprintf('folders/%s/locations/global/floorSetting', $folderId);
        
            $response = $client->getFloorSetting((new GetFloorSettingRequest())->setName($floorSettingsName));
        
            printf("Floor settings retrieved successfully: %s\n", $response->serializeToJsonString());
        }

  * View the Model Armor floor setting for a given organization.
        
        use Google\Cloud\ModelArmor\V1\Client\ModelArmorClient;
        use Google\Cloud\ModelArmor\V1\GetFloorSettingRequest;
        
        /**
         * Gets the floor settings for a given organization.
         *
         * @param string $organizationId The organization Id for which the floor settings is to be retrieved.
         *
         */
        function get_organization_floor_settings(string $organizationId): void
        {
            $client = new ModelArmorClient();
        
            $floorSettingsName = sprintf('organizations/%s/locations/global/floorSetting', $organizationId);
        
            $response = $client->getFloorSetting((new GetFloorSettingRequest())->setName($floorSettingsName));
        
            printf("Floor settings retrieved successfully: %s\n", $response->serializeToJsonString());
        }




### Python

To run this code, first [set up a Python development environment](https://docs.cloud.google.com/python/docs/setup) and [install the Model Armor Python SDK](https://docs.cloud.google.com/model-armor/reference/libraries#install).

  * View the Model Armor floor setting for a given project.
        
        from google.cloud import [modelarmor_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest)
        
        # Create the Model Armor client.
        client = [modelarmor_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest).[ModelArmorClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.html)(transport="rest")
        
        # TODO(Developer): Uncomment below variable.
        # project_id = "YOUR_PROJECT_ID"
        
        floor_settings_name = f"projects/{project_id}/locations/global/floorSetting"
        
        # Get the project floor setting.
        response = client.[get_floor_setting](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.html#google_cloud_modelarmor_v1_services_model_armor_ModelArmorClient_get_floor_setting)(
            request=[modelarmor_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest).[GetFloorSettingRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.GetFloorSettingRequest.html)(name=floor_settings_name)
        )
        
        # Print the retrieved floor setting.
        print(response)
        

  * View the Model Armor floor setting for a given folder.
        
        from google.cloud import [modelarmor_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest)
        
        # Create the Model Armor client.
        client = [modelarmor_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest).[ModelArmorClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.html)(transport="rest")
        
        # TODO(Developer): Uncomment below variable.
        # folder_id = "YOUR_FOLDER_ID"
        
        # Prepare folder floor setting path/name
        floor_settings_name = f"folders/{folder_id}/locations/global/floorSetting"
        
        # Get the folder floor setting.
        response = client.[get_floor_setting](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.html#google_cloud_modelarmor_v1_services_model_armor_ModelArmorClient_get_floor_setting)(
            request=[modelarmor_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest).[GetFloorSettingRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.GetFloorSettingRequest.html)(name=floor_settings_name)
        )
        
        # Print the retrieved floor setting.
        print(response)
        

  * View the Model Armor floor setting for a given organization.
        
        from google.cloud import [modelarmor_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest)
        
        # Create the Model Armor client.
        client = [modelarmor_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest).[ModelArmorClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.html)(transport="rest")
        
        # TODO(Developer): Uncomment below variable.
        # organization_id = "YOUR_ORGANIZATION_ID"
        
        floor_settings_name = (
            f"organizations/{organization_id}/locations/global/floorSetting"
        )
        
        # Get the organization floor setting.
        response = client.[get_floor_setting](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.html#google_cloud_modelarmor_v1_services_model_armor_ModelArmorClient_get_floor_setting)(
            request=[modelarmor_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest).[GetFloorSettingRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.GetFloorSettingRequest.html)(name=floor_settings_name)
        )
        
        # Print the retrieved floor setting.
        print(response)
        




## Update Model Armor floor settings

Update Model Armor floor settings to change the minimum requirements for templates, reflect changes in security policies, correct misconfigurations, or resolve conflicts between floor settings.

Run the following command to update the Model Armor floor settings.

### Console

  1. In the Google Cloud console, go to the **Model Armor** page.

[Go to Model Armor](https://console.cloud.google.com/projectselector2/security/modelarmor?supportedpurview=organizationId,folder,project)

  2. Verify that you are viewing the project that you activated Model Armor on.

  3. On the **Model Armor** page, go to the **Floor settings** tab and click **Configure floor settings**.

  4. Update the required fields and click **Save floor settings**.




### gcloud
    
    
       gcloud model-armor floorsettings update --full-uri=<full-uri-of-the-floorsetting>
    

Example command:
    
    
           gcloud model-armor floorsettings update \
               --malicious-uri-filter-settings-enforcement=ENABLED \
               --pi-and-jailbreak-filter-settings-enforcement=DISABLED \
               --pi-and-jailbreak-filter-settings-confidence-level=LOW_AND_ABOVE \
               --basic-config-filter-enforcement=ENABLED \
               --add-rai-settings-filters='[{"confidenceLevel": "low_and_above", "filterType": "HARASSMENT"}, {"confidenceLevel": "high", "filterType": "SEXUALLY_EXPLICIT"}]' \
               --full-uri='folders/FOLDER_ID/locations/global/floorSetting' \
               --enable-floor-setting-enforcement=true
    

To configure floor settings with multi-language detection enabled, run the following command:
    
    
        gcloud model-armor floorsettings update \
            --full-uri=projects/PROJECT_ID/locations/global/floorSetting \
            --enable-multi-language-detection
    

Replace the following:

  * `PROJECT_ID`: the ID of the project for the floor settings.
  * `FOLDER_ID`: the ID of the folder for the floor settings.



### REST

  * Update the Model Armor floor setting for a given project.
        
        curl -X PATCH
          -d '{"filterConfig" :{"piAndJailbreakFilterSettings": { "filterEnforcement": "ENABLED"}, "maliciousUriFilterSettings": { "filterEnforcement": "ENABLED" }, "rai_settings":{"rai_filters":{"filter_type":"DANGEROUS", "confidence_level":"LOW_AND_ABOVE" }, \
          "rai_filters":{"filter_type":"HATE_SPEECH", "confidence_level":"LOW_AND_ABOVE" }, "rai_filters":{"filter_type":"HARASSMENT", "confidence_level":"LOW_AND_ABOVE" }, "rai_filters":{"filter_type":"SEXUALLY_EXPLICIT", "confidence_level":"LOW_AND_ABOVE" }}},"enableFloorSettingEnforcement":"true"}' \
          -H "Content-Type: application/json" \
          -H "Authorization: Bearer $(gcloud auth print-access-token) \
          "https://modelarmor.googleapis.com/v1/projects/PROJECT_ID/locations/global/floorSetting"

  * Update the Model Armor floor setting for a given folder.
        
        curl -X PATCH \
          -d '{"filterConfig" :{"piAndJailbreakFilterSettings": { "filterEnforcement": "ENABLED"}, "maliciousUriFilterSettings": {"filterEnforcement": "ENABLED" }},"enableFloorSettingEnforcement":"true"}' \
          -H "Content-Type: application/json" \
          -H "Authorization: Bearer $(gcloud auth print-access-token)" \
          "https://modelarmor.googleapis.com/v1/folders/FOLDER_ID/locations/global/floorSetting"

  * Update the Model Armor floor setting for a given organization.
        
        curl -X PATCH \
          -d '{"filterConfig" :{"piAndJailbreakFilterSettings": { "filterEnforcement": "ENABLED"}, "maliciousUriFilterSettings": {
              "filterEnforcement": "ENABLED" }},"enableFloorSettingEnforcement":"true"}' \
          -H "Content-Type: application/json" \
          -H "Authorization: Bearer $(gcloud auth print-access-token)" \
              "https://modelarmor.googleapis.com/v1/organizations/ORGANIZATION_ID/locations/global/floorSetting"




Replace the following:

  * `PROJECT_ID`: the ID of the project for the floor settings.
  * `FOLDER_ID`: the ID of the folder for the floor settings.
  * `ORGANIZATION_ID`: the ID of the organization for the floor settings.

**Note:** If you don't specify the prompt injection and jailbreak detection confidence level, the confidence level defaults to **LOW_AND_ABOVE** for all levels: project, organization, or folder.

The update command returns the following response:
    
    
    {
    "name": "projects/PROJECT_ID/locations/global/floorSetting",
    "updateTime": "2024-12-19T15:36:21.318191Z",
    "filterConfig": {
      "piAndJailbreakFilterSettings": {
        "filterEnforcement": "ENABLED"
      },
    "maliciousUriFilterSettings": {
      "filterEnforcement": "ENABLED"
     }
    }
    }

**Note:** If you want to disable the inherited floor settings, set the `enableFloorSettingEnforcement` flag to `false`.

###  C# 

To run this code, first [set up a C# development environment](https://docs.cloud.google.com/dotnet/docs/setup) and [install the Model Armor C# SDK](https://docs.cloud.google.com/model-armor//reference/libraries#client-libraries-install-csharp).

  * Update the Model Armor floor setting for a given project.
        
        using [Google.Cloud.ModelArmor.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.html);
        using System;
        
        public class UpdateProjectFloorSettings
        {
            public FloorSetting UpdateProjectFloorSetting(string projectId)
            {
                // Create the client
                [ModelArmorClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.ModelArmorClient.html) client = [ModelArmorClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.ModelArmorClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.ModelArmorClient.html#Google_Cloud_ModelArmor_V1_ModelArmorClient_Create)();
        
                // Construct the floor settings name
                string floorSettingsName = $"projects/{projectId}/locations/global/floorSetting";
        
                // Build the floor settings with your preferred filters
                // For more details on filters, please refer to the following doc:
                // https://cloud.google.com/security-command-center/docs/key-concepts-model-armor#ma-filters
                var raiFilter = new RaiFilterSettings.Types.RaiFilter
                {
                    FilterType = [RaiFilterType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.RaiFilterType.html).[HateSpeech](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.RaiFilterType.html#Google_Cloud_ModelArmor_V1_RaiFilterType_HateSpeech),
                    ConfidenceLevel = [DetectionConfidenceLevel](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.DetectionConfidenceLevel.html).[High](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.DetectionConfidenceLevel.html#Google_Cloud_ModelArmor_V1_DetectionConfidenceLevel_High),
                };
        
                var raiFilterSettings = new [RaiFilterSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.RaiFilterSettings.html)();
                raiFilterSettings.[RaiFilters](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.RaiFilterSettings.html#Google_Cloud_ModelArmor_V1_RaiFilterSettings_RaiFilters).Add(raiFilter);
        
                var filterConfig = new [FilterConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.FilterConfig.html) { RaiSettings = raiFilterSettings };
        
                var floorSetting = new [FloorSetting](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.FloorSetting.html)
                {
                    Name = floorSettingsName,
                    FilterConfig = filterConfig,
                    EnableFloorSettingEnforcement = true,
                };
        
                // Create the update request
                var updateRequest = new [UpdateFloorSettingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.UpdateFloorSettingRequest.html) { FloorSetting = floorSetting };
        
                // Update the floor settings
                [FloorSetting](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.FloorSetting.html) response = client.[UpdateFloorSetting](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.ModelArmorClient.html#Google_Cloud_ModelArmor_V1_ModelArmorClient_UpdateFloorSetting_Google_Cloud_ModelArmor_V1_FloorSetting_Google_Protobuf_WellKnownTypes_FieldMask_Google_Api_Gax_Grpc_CallSettings_)(updateRequest);
        
                Console.WriteLine($"Floor setting updated: {response.[Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.FloorSetting.html#Google_Cloud_ModelArmor_V1_FloorSetting_Name)}");
        
                return response;
            }
        }

  * Update the Model Armor floor setting for a given folder.
        
        using [Google.Cloud.ModelArmor.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.html);
        using System;
        
        public class UpdateFolderFloorSettings
        {
            public FloorSetting UpdateFolderFloorSetting(string folderId)
            {
                // Create the client
                [ModelArmorClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.ModelArmorClient.html) client = [ModelArmorClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.ModelArmorClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.ModelArmorClient.html#Google_Cloud_ModelArmor_V1_ModelArmorClient_Create)();
        
                // Construct the floor settings name
                string floorSettingsName = $"folders/{folderId}/locations/global/floorSetting";
        
                // Build the floor settings with your preferred filters
                // For more details on filters, please refer to the following doc:
                // https://cloud.google.com/security-command-center/docs/key-concepts-model-armor#ma-filters
                var raiFilter = new RaiFilterSettings.Types.RaiFilter
                {
                    FilterType = [RaiFilterType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.RaiFilterType.html).[HateSpeech](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.RaiFilterType.html#Google_Cloud_ModelArmor_V1_RaiFilterType_HateSpeech),
                    ConfidenceLevel = [DetectionConfidenceLevel](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.DetectionConfidenceLevel.html).[High](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.DetectionConfidenceLevel.html#Google_Cloud_ModelArmor_V1_DetectionConfidenceLevel_High),
                };
        
                var raiFilterSettings = new [RaiFilterSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.RaiFilterSettings.html)();
                raiFilterSettings.[RaiFilters](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.RaiFilterSettings.html#Google_Cloud_ModelArmor_V1_RaiFilterSettings_RaiFilters).Add(raiFilter);
        
                var filterConfig = new [FilterConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.FilterConfig.html) { RaiSettings = raiFilterSettings };
        
                var floorSetting = new [FloorSetting](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.FloorSetting.html)
                {
                    Name = floorSettingsName,
                    FilterConfig = filterConfig,
                    EnableFloorSettingEnforcement = true,
                };
        
                // Create the update request
                var updateRequest = new [UpdateFloorSettingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.UpdateFloorSettingRequest.html) { FloorSetting = floorSetting };
        
                // Update the floor settings
                [FloorSetting](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.FloorSetting.html) response = client.[UpdateFloorSetting](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.ModelArmorClient.html#Google_Cloud_ModelArmor_V1_ModelArmorClient_UpdateFloorSetting_Google_Cloud_ModelArmor_V1_FloorSetting_Google_Protobuf_WellKnownTypes_FieldMask_Google_Api_Gax_Grpc_CallSettings_)(updateRequest);
        
                Console.WriteLine($"Floor setting updated: {response.[Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.FloorSetting.html#Google_Cloud_ModelArmor_V1_FloorSetting_Name)}");
        
                return response;
            }
        }

  * Update the Model Armor floor setting for a given organization.
        
        using [Google.Cloud.ModelArmor.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.html);
        using System;
        
        public class UpdateOrganizationFloorSettings
        {
            public FloorSetting UpdateOrganizationFloorSetting(string organizationId)
            {
                // Create the client
                [ModelArmorClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.ModelArmorClient.html) client = [ModelArmorClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.ModelArmorClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.ModelArmorClient.html#Google_Cloud_ModelArmor_V1_ModelArmorClient_Create)();
        
                // Construct the floor settings name
                string floorSettingsName = $"organizations/{organizationId}/locations/global/floorSetting";
        
                // Build the floor settings with your preferred filters
                // For more details on filters, please refer to the following doc:
                // https://cloud.google.com/security-command-center/docs/key-concepts-model-armor#ma-filters
                var raiFilter = new RaiFilterSettings.Types.RaiFilter
                {
                    FilterType = [RaiFilterType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.RaiFilterType.html).[HateSpeech](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.RaiFilterType.html#Google_Cloud_ModelArmor_V1_RaiFilterType_HateSpeech),
                    ConfidenceLevel = [DetectionConfidenceLevel](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.DetectionConfidenceLevel.html).[High](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.DetectionConfidenceLevel.html#Google_Cloud_ModelArmor_V1_DetectionConfidenceLevel_High),
                };
        
                var raiFilterSettings = new [RaiFilterSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.RaiFilterSettings.html)();
                raiFilterSettings.[RaiFilters](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.RaiFilterSettings.html#Google_Cloud_ModelArmor_V1_RaiFilterSettings_RaiFilters).Add(raiFilter);
        
                var filterConfig = new [FilterConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.FilterConfig.html) { RaiSettings = raiFilterSettings };
        
                var floorSetting = new [FloorSetting](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.FloorSetting.html)
                {
                    Name = floorSettingsName,
                    FilterConfig = filterConfig,
                    EnableFloorSettingEnforcement = true,
                };
        
                // Create the update request
                var updateRequest = new [UpdateFloorSettingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.UpdateFloorSettingRequest.html) { FloorSetting = floorSetting };
        
                // Update the floor settings
                [FloorSetting](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.FloorSetting.html) response = client.[UpdateFloorSetting](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.ModelArmorClient.html#Google_Cloud_ModelArmor_V1_ModelArmorClient_UpdateFloorSetting_Google_Cloud_ModelArmor_V1_FloorSetting_Google_Protobuf_WellKnownTypes_FieldMask_Google_Api_Gax_Grpc_CallSettings_)(updateRequest);
        
                Console.WriteLine($"Floor setting updated: {response.[Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.FloorSetting.html#Google_Cloud_ModelArmor_V1_FloorSetting_Name)}");
        
                return response;
            }
        }




###  Go 

To run this code, first [set up a Go development environment](https://docs.cloud.google.com/go/docs/setup) and [install the Model Armor Go SDK](https://docs.cloud.google.com/model-armor/reference/libraries#client-libraries-install-go).

  * Update the Model Armor floor setting for a given project.
        
        import (
        	"context"
        	"fmt"
        	"io"
        
        	modelarmor "cloud.google.com/go/modelarmor/apiv1"
        	modelarmorpb "cloud.google.com/go/modelarmor/apiv1/modelarmorpb"
        )
        
        // updateProjectFloorSettings updates the floor settings of a project.
        //
        // This method updates the floor settings of a project.
        //
        // w io.Writer: The writer to use for logging.
        // projectID string: The ID of the project.
        func updateProjectFloorSettings(w io.Writer, projectID string) error {
        	ctx := context.Background()
        
        	// Create the Model Armor client.
        	client, err := modelarmor.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/modelarmor/latest/apiv1.html#cloud_google_com_go_modelarmor_apiv1_Client_NewClient)(ctx)
        	if err != nil {
        		return fmt.Errorf("failed to create client: %w", err)
        	}
        	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/modelarmor/latest/apiv1.html#cloud_google_com_go_modelarmor_apiv1_Client_Close)()
        
        	// Prepare project floor setting path/name
        	floorSettingsName := fmt.Sprintf("projects/%s/locations/global/floorSetting", projectID)
        
        	// Update the project floor setting
        	// For more details on filters, please refer to the following doc:
        	// [https://cloud.google.com/security-command-center/docs/key-concepts-model-armor#ma-filters](https://cloud.google.com/security-command-center/docs/key-concepts-model-armor#ma-filters)
        	enableEnforcement := true
        	req := &modelarmorpb.UpdateFloorSettingRequest{
        		FloorSetting: &modelarmorpb.FloorSetting{
        			Name: floorSettingsName,
        			FilterConfig: &modelarmorpb.FilterConfig{
        				RaiSettings: &modelarmorpb.RaiFilterSettings{
        					RaiFilters: []*modelarmorpb.RaiFilterSettings_RaiFilter{
        						{
        							FilterType:      modelarmorpb.[RaiFilterType_HATE_SPEECH](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/modelarmor/latest/apiv1/modelarmorpb.html#cloud_google_com_go_modelarmor_apiv1_modelarmorpb_RaiFilterType_RAI_FILTER_TYPE_UNSPECIFIED_RaiFilterType_SEXUALLY_EXPLICIT_RaiFilterType_HATE_SPEECH_RaiFilterType_HARASSMENT_RaiFilterType_DANGEROUS),
        							ConfidenceLevel: modelarmorpb.[DetectionConfidenceLevel_HIGH](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/modelarmor/latest/apiv1/modelarmorpb.html#cloud_google_com_go_modelarmor_apiv1_modelarmorpb_DetectionConfidenceLevel_DETECTION_CONFIDENCE_LEVEL_UNSPECIFIED_DetectionConfidenceLevel_LOW_AND_ABOVE_DetectionConfidenceLevel_MEDIUM_AND_ABOVE_DetectionConfidenceLevel_HIGH),
        						},
        					},
        				},
        			},
        			EnableFloorSettingEnforcement: &enableEnforcement,
        		},
        	}
        
        	response, err := client.UpdateFloorSetting(ctx, req)
        	if err != nil {
        		return fmt.Errorf("failed to update floor setting: %w", err)
        	}
        
        	// Print the updated config
        	fmt.Fprintf(w, "Updated project floor setting: %+v\n", response)
        
        	return nil
        }
        

  * Update the Model Armor floor setting for a given folder.
        
        import (
        	"context"
        	"fmt"
        	"io"
        
        	modelarmor "cloud.google.com/go/modelarmor/apiv1"
        	modelarmorpb "cloud.google.com/go/modelarmor/apiv1/modelarmorpb"
        )
        
        // updateFolderFloorSettings updates floor settings of a folder.
        //
        // This method updates the floor settings of a folder.
        //
        // w io.Writer: The writer to use for logging.
        // folderID string: The ID of the folder.
        func updateFolderFloorSettings(w io.Writer, folderID string) error {
        	ctx := context.Background()
        
        	// Create the Model Armor client.
        	client, err := modelarmor.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/modelarmor/latest/apiv1.html#cloud_google_com_go_modelarmor_apiv1_Client_NewClient)(ctx)
        	if err != nil {
        		return fmt.Errorf("failed to create client: %w", err)
        	}
        	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/modelarmor/latest/apiv1.html#cloud_google_com_go_modelarmor_apiv1_Client_Close)()
        
        	// Prepare folder floor settings path/name
        	floorSettingsName := fmt.Sprintf("folders/%s/locations/global/floorSetting", folderID)
        
        	// Prepare the floor setting update
        	enableEnforcement := true
        	floorSetting := &modelarmorpb.FloorSetting{
        		Name: floorSettingsName,
        		FilterConfig: &modelarmorpb.FilterConfig{
        			RaiSettings: &modelarmorpb.RaiFilterSettings{
        				RaiFilters: []*modelarmorpb.RaiFilterSettings_RaiFilter{
        					{
        						FilterType:      modelarmorpb.[RaiFilterType_HATE_SPEECH](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/modelarmor/latest/apiv1/modelarmorpb.html#cloud_google_com_go_modelarmor_apiv1_modelarmorpb_RaiFilterType_RAI_FILTER_TYPE_UNSPECIFIED_RaiFilterType_SEXUALLY_EXPLICIT_RaiFilterType_HATE_SPEECH_RaiFilterType_HARASSMENT_RaiFilterType_DANGEROUS),
        						ConfidenceLevel: modelarmorpb.[DetectionConfidenceLevel_HIGH](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/modelarmor/latest/apiv1/modelarmorpb.html#cloud_google_com_go_modelarmor_apiv1_modelarmorpb_DetectionConfidenceLevel_DETECTION_CONFIDENCE_LEVEL_UNSPECIFIED_DetectionConfidenceLevel_LOW_AND_ABOVE_DetectionConfidenceLevel_MEDIUM_AND_ABOVE_DetectionConfidenceLevel_HIGH),
        					},
        				},
        			},
        		},
        		EnableFloorSettingEnforcement: &enableEnforcement,
        	}
        
        	// Prepare request for updating the floor setting.
        	req := &modelarmorpb.UpdateFloorSettingRequest{
        		FloorSetting: floorSetting,
        	}
        
        	// Update the floor setting.
        	response, err := client.UpdateFloorSetting(ctx, req)
        	if err != nil {
        		return fmt.Errorf("failed to update floor setting: %w", err)
        	}
        
        	// Print the updated config
        	fmt.Fprintf(w, "Updated folder floor setting: %v\n", response)
        
        	return nil
        
        }
        

  * Update the Model Armor floor setting for a given organization.
        
        import (
        	"context"
        	"fmt"
        	"io"
        
        	modelarmor "cloud.google.com/go/modelarmor/apiv1"
        	modelarmorpb "cloud.google.com/go/modelarmor/apiv1/modelarmorpb"
        )
        
        // updateOrganizationFloorSettings updates floor settings of an organization.
        //
        // This method updates the floor settings of an organization.
        //
        // w io.Writer: The writer to use for logging.
        // organizationID string: The ID of the organization.
        func updateOrganizationFloorSettings(w io.Writer, organizationID string) error {
        	ctx := context.Background()
        
        	// Create the Model Armor client.
        	client, err := modelarmor.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/modelarmor/latest/apiv1.html#cloud_google_com_go_modelarmor_apiv1_Client_NewClient)(ctx)
        	if err != nil {
        		return fmt.Errorf("failed to create client: %w", err)
        	}
        	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/modelarmor/latest/apiv1.html#cloud_google_com_go_modelarmor_apiv1_Client_Close)()
        
        	// Prepare organization floor setting path/name
        	floorSettingsName := fmt.Sprintf("organizations/%s/locations/global/floorSetting", organizationID)
        
        	// Update the organization floor setting
        	// For more details on filters, please refer to the following doc:
        	// [https://cloud.google.com/security-command-center/docs/key-concepts-model-armor#ma-filters](https://cloud.google.com/security-command-center/docs/key-concepts-model-armor#ma-filters)
        	enableEnforcement := true
        	req := &modelarmorpb.UpdateFloorSettingRequest{
        		FloorSetting: &modelarmorpb.FloorSetting{
        			Name: floorSettingsName,
        			FilterConfig: &modelarmorpb.FilterConfig{
        				RaiSettings: &modelarmorpb.RaiFilterSettings{
        					RaiFilters: []*modelarmorpb.RaiFilterSettings_RaiFilter{
        						{
        							FilterType:      modelarmorpb.[RaiFilterType_HATE_SPEECH](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/modelarmor/latest/apiv1/modelarmorpb.html#cloud_google_com_go_modelarmor_apiv1_modelarmorpb_RaiFilterType_RAI_FILTER_TYPE_UNSPECIFIED_RaiFilterType_SEXUALLY_EXPLICIT_RaiFilterType_HATE_SPEECH_RaiFilterType_HARASSMENT_RaiFilterType_DANGEROUS),
        							ConfidenceLevel: modelarmorpb.[DetectionConfidenceLevel_HIGH](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/modelarmor/latest/apiv1/modelarmorpb.html#cloud_google_com_go_modelarmor_apiv1_modelarmorpb_DetectionConfidenceLevel_DETECTION_CONFIDENCE_LEVEL_UNSPECIFIED_DetectionConfidenceLevel_LOW_AND_ABOVE_DetectionConfidenceLevel_MEDIUM_AND_ABOVE_DetectionConfidenceLevel_HIGH),
        						},
        					},
        				},
        			},
        			EnableFloorSettingEnforcement: &enableEnforcement,
        		},
        	}
        
        	response, err := client.UpdateFloorSetting(ctx, req)
        	if err != nil {
        		return fmt.Errorf("failed to update floor setting: %w", err)
        	}
        
        	// Print the updated config
        	fmt.Fprintf(w, "Updated org floor setting: %+v\n", response)
        




###  Java 

To run this code, first [set up a Java development environment](https://docs.cloud.google.com/java/docs/setup) and [install the Model Armor Java SDK](https://docs.cloud.google.com/model-armor/reference/libraries#install-java).

  * Update the Model Armor floor setting for a given project.
        
        import com.google.cloud.modelarmor.v1.[DetectionConfidenceLevel](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.DetectionConfidenceLevel.html);
        import com.google.cloud.modelarmor.v1.[FilterConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.FilterConfig.html);
        import com.google.cloud.modelarmor.v1.[FloorSetting](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.FloorSetting.html);
        import com.google.cloud.modelarmor.v1.[FloorSettingName](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.FloorSettingName.html);
        import com.google.cloud.modelarmor.v1.[ModelArmorClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.ModelArmorClient.html);
        import com.google.cloud.modelarmor.v1.[RaiFilterSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.RaiFilterSettings.html);
        import com.google.cloud.modelarmor.v1.[RaiFilterSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.RaiFilterSettings.html).[RaiFilter](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.RaiFilterSettings.RaiFilter.html);
        import com.google.cloud.modelarmor.v1.[RaiFilterType](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.RaiFilterType.html);
        import com.google.cloud.modelarmor.v1.[UpdateFloorSettingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.UpdateFloorSettingRequest.html);
        import com.google.protobuf.[FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html);
        import java.io.IOException;
        import java.util.List;
        
        public class UpdateProjectFloorSetting {
        
          public static void main(String[] args) throws IOException {
            // TODO(developer): Replace these variables before running the sample.
            String projectId = "your-project-id";
        
            updateProjectFloorSetting(projectId);
          }
        
          public static [FloorSetting](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.FloorSetting.html) updateProjectFloorSetting(String projectId)
              throws IOException {
        
            // Initialize client that will be used to send requests. This client only
            // needs to be created once, and can be reused for multiple requests.
            try ([ModelArmorClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.ModelArmorClient.html) client = [ModelArmorClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.ModelArmorClient.html).create()) {
              String name = [FloorSettingName](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.FloorSettingName.html).of(projectId, "global").toString();
        
              // For more details on filters, please refer to the following doc:
              // https://cloud.google.com/security-command-center/docs/key-concepts-model-armor#ma-filters
              [RaiFilterSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.RaiFilterSettings.html) raiFilterSettings =
                  [RaiFilterSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.RaiFilterSettings.html).newBuilder()
                      .[addAllRaiFilters](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.RaiFilterSettings.Builder.html#com_google_cloud_modelarmor_v1_RaiFilterSettings_Builder_addAllRaiFilters_java_lang_Iterable___extends_com_google_cloud_modelarmor_v1_RaiFilterSettings_RaiFilter__)(
                          List.of(
                              [RaiFilter](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.RaiFilterSettings.RaiFilter.html).newBuilder()
                                  .setFilterType([RaiFilterType](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.RaiFilterType.html).HARASSMENT)
                                  .setConfidenceLevel([DetectionConfidenceLevel](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.DetectionConfidenceLevel.html).LOW_AND_ABOVE)
                                  .build(),
                              [RaiFilter](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.RaiFilterSettings.RaiFilter.html).newBuilder()
                                  .setFilterType([RaiFilterType](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.RaiFilterType.html).SEXUALLY_EXPLICIT)
                                  .setConfidenceLevel([DetectionConfidenceLevel](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.DetectionConfidenceLevel.html).HIGH)
                                  .build()))
                      .build();
        
              [FilterConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.FilterConfig.html) modelArmorFilter = [FilterConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.FilterConfig.html).newBuilder()
                  .[setRaiSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.FilterConfig.Builder.html#com_google_cloud_modelarmor_v1_FilterConfig_Builder_setRaiSettings_com_google_cloud_modelarmor_v1_RaiFilterSettings_)(raiFilterSettings)
                  .build();
        
              // Create a field mask to specify which fields to update.
              // Ref: https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask
              [FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html) updateMask = [FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html).newBuilder().[addPaths](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.Builder.html#com_google_protobuf_FieldMask_Builder_addPaths_java_lang_String_)("filter_config.rai_settings").build();
        
              [FloorSetting](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.FloorSetting.html) floorSetting = [FloorSetting](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.FloorSetting.html).newBuilder()
                  .setName(name)
                  .setFilterConfig(modelArmorFilter)
                  .[setEnableFloorSettingEnforcement](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.FloorSetting.Builder.html#com_google_cloud_modelarmor_v1_FloorSetting_Builder_setEnableFloorSettingEnforcement_boolean_)(true)
                  .build();
        
              [UpdateFloorSettingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.UpdateFloorSettingRequest.html) request = [UpdateFloorSettingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.UpdateFloorSettingRequest.html).newBuilder()
                  .[setFloorSetting](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.UpdateFloorSettingRequest.Builder.html#com_google_cloud_modelarmor_v1_UpdateFloorSettingRequest_Builder_setFloorSetting_com_google_cloud_modelarmor_v1_FloorSetting_)(floorSetting)
                  .setUpdateMask(updateMask)
                  .build();
        
              [FloorSetting](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.FloorSetting.html) updatedFloorSetting = client.updateFloorSetting(request);
              System.out.println("Updated floor setting for project: " + projectId);
        
              return updatedFloorSetting;
            }
          }
        }

  * Update the Model Armor floor setting for a given folder.
        
        import com.google.cloud.modelarmor.v1.[DetectionConfidenceLevel](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.DetectionConfidenceLevel.html);
        import com.google.cloud.modelarmor.v1.[FilterConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.FilterConfig.html);
        import com.google.cloud.modelarmor.v1.[FloorSetting](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.FloorSetting.html);
        import com.google.cloud.modelarmor.v1.[FloorSettingName](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.FloorSettingName.html);
        import com.google.cloud.modelarmor.v1.[ModelArmorClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.ModelArmorClient.html);
        import com.google.cloud.modelarmor.v1.[RaiFilterSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.RaiFilterSettings.html);
        import com.google.cloud.modelarmor.v1.[RaiFilterSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.RaiFilterSettings.html).[RaiFilter](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.RaiFilterSettings.RaiFilter.html);
        import com.google.cloud.modelarmor.v1.[RaiFilterType](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.RaiFilterType.html);
        import com.google.cloud.modelarmor.v1.[UpdateFloorSettingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.UpdateFloorSettingRequest.html);
        import com.google.protobuf.[FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html);
        import java.io.IOException;
        import java.util.List;
        
        public class UpdateFolderFloorSetting {
        
          public static void main(String[] args) throws IOException {
            // TODO(developer): Replace these variables before running the sample.
            String folderId = "your-folder-id";
        
            updateFolderFloorSetting(folderId);
          }
        
          public static [FloorSetting](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.FloorSetting.html) updateFolderFloorSetting(String folderId)
              throws IOException {
        
            // Initialize client that will be used to send requests. This client only
            // needs to be created once, and can be reused for multiple requests.
            try ([ModelArmorClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.ModelArmorClient.html) client = [ModelArmorClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.ModelArmorClient.html).create()) {
              String name = [FloorSettingName](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.FloorSettingName.html).[ofFolderLocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.FloorSettingName.html#com_google_cloud_modelarmor_v1_FloorSettingName_ofFolderLocationName_java_lang_String_java_lang_String_)(folderId, "global").toString();
        
              // For more details on filters, please refer to the following doc:
              // https://cloud.google.com/security-command-center/docs/key-concepts-model-armor#ma-filters
              [RaiFilterSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.RaiFilterSettings.html) raiFilterSettings =
                  [RaiFilterSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.RaiFilterSettings.html).newBuilder()
                      .[addAllRaiFilters](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.RaiFilterSettings.Builder.html#com_google_cloud_modelarmor_v1_RaiFilterSettings_Builder_addAllRaiFilters_java_lang_Iterable___extends_com_google_cloud_modelarmor_v1_RaiFilterSettings_RaiFilter__)(
                          List.of(
                              [RaiFilter](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.RaiFilterSettings.RaiFilter.html).newBuilder()
                                  .setFilterType([RaiFilterType](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.RaiFilterType.html).HARASSMENT)
                                  .setConfidenceLevel([DetectionConfidenceLevel](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.DetectionConfidenceLevel.html).LOW_AND_ABOVE)
                                  .build(),
                              [RaiFilter](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.RaiFilterSettings.RaiFilter.html).newBuilder()
                                  .setFilterType([RaiFilterType](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.RaiFilterType.html).SEXUALLY_EXPLICIT)
                                  .setConfidenceLevel([DetectionConfidenceLevel](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.DetectionConfidenceLevel.html).HIGH)
                                  .build()))
                      .build();
        
              [FilterConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.FilterConfig.html) modelArmorFilter = [FilterConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.FilterConfig.html).newBuilder()
                  .[setRaiSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.FilterConfig.Builder.html#com_google_cloud_modelarmor_v1_FilterConfig_Builder_setRaiSettings_com_google_cloud_modelarmor_v1_RaiFilterSettings_)(raiFilterSettings)
                  .build();
        
              // Create a field mask to specify which fields to update.
              // Ref: https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask
              [FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html) updateMask = [FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html).newBuilder().[addPaths](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.Builder.html#com_google_protobuf_FieldMask_Builder_addPaths_java_lang_String_)("filter_config.rai_settings").build();
        
              [FloorSetting](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.FloorSetting.html) floorSetting = [FloorSetting](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.FloorSetting.html).newBuilder()
                  .setName(name)
                  .setFilterConfig(modelArmorFilter)
                  .[setEnableFloorSettingEnforcement](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.FloorSetting.Builder.html#com_google_cloud_modelarmor_v1_FloorSetting_Builder_setEnableFloorSettingEnforcement_boolean_)(true)
                  .build();
        
              [UpdateFloorSettingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.UpdateFloorSettingRequest.html) request = [UpdateFloorSettingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.UpdateFloorSettingRequest.html).newBuilder()
                  .[setFloorSetting](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.UpdateFloorSettingRequest.Builder.html#com_google_cloud_modelarmor_v1_UpdateFloorSettingRequest_Builder_setFloorSetting_com_google_cloud_modelarmor_v1_FloorSetting_)(floorSetting)
                  .setUpdateMask(updateMask)
                  .build();
        
              [FloorSetting](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.FloorSetting.html) updatedFloorSetting = client.updateFloorSetting(request);
              System.out.println("Updated floor setting for folder: " + folderId);
        
              return updatedFloorSetting;
            }
          }
        }

  * Update the Model Armor floor setting for a given organization.
        
        import com.google.cloud.modelarmor.v1.[DetectionConfidenceLevel](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.DetectionConfidenceLevel.html);
        import com.google.cloud.modelarmor.v1.[FilterConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.FilterConfig.html);
        import com.google.cloud.modelarmor.v1.[FloorSetting](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.FloorSetting.html);
        import com.google.cloud.modelarmor.v1.[FloorSettingName](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.FloorSettingName.html);
        import com.google.cloud.modelarmor.v1.[ModelArmorClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.ModelArmorClient.html);
        import com.google.cloud.modelarmor.v1.[RaiFilterSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.RaiFilterSettings.html);
        import com.google.cloud.modelarmor.v1.[RaiFilterSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.RaiFilterSettings.html).[RaiFilter](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.RaiFilterSettings.RaiFilter.html);
        import com.google.cloud.modelarmor.v1.[RaiFilterType](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.RaiFilterType.html);
        import com.google.cloud.modelarmor.v1.[UpdateFloorSettingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.UpdateFloorSettingRequest.html);
        import com.google.protobuf.[FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html);
        import java.io.IOException;
        import java.util.List;
        
        public class UpdateOrganizationsFloorSetting {
        
          public static void main(String[] args) throws IOException {
            // TODO(developer): Replace these variables before running the sample.
            String organizationId = "your-organization-id";
        
            updateOrganizationFloorSetting(organizationId);
          }
        
          public static [FloorSetting](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.FloorSetting.html) updateOrganizationFloorSetting(String organizationId)
              throws IOException {
        
            // Initialize client that will be used to send requests. This client only
            // needs to be created once, and can be reused for multiple requests.
            try ([ModelArmorClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.ModelArmorClient.html) client = [ModelArmorClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.ModelArmorClient.html).create()) {
              String name = [FloorSettingName](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.FloorSettingName.html).[ofOrganizationLocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.FloorSettingName.html#com_google_cloud_modelarmor_v1_FloorSettingName_ofOrganizationLocationName_java_lang_String_java_lang_String_)(organizationId, "global")
                  .toString();
        
              // For more details on filters, please refer to the following doc:
              // https://cloud.google.com/security-command-center/docs/key-concepts-model-armor#ma-filters
              [RaiFilterSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.RaiFilterSettings.html) raiFilterSettings =
                  [RaiFilterSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.RaiFilterSettings.html).newBuilder()
                      .[addAllRaiFilters](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.RaiFilterSettings.Builder.html#com_google_cloud_modelarmor_v1_RaiFilterSettings_Builder_addAllRaiFilters_java_lang_Iterable___extends_com_google_cloud_modelarmor_v1_RaiFilterSettings_RaiFilter__)(
                          List.of(
                              [RaiFilter](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.RaiFilterSettings.RaiFilter.html).newBuilder()
                                  .setFilterType([RaiFilterType](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.RaiFilterType.html).HARASSMENT)
                                  .setConfidenceLevel([DetectionConfidenceLevel](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.DetectionConfidenceLevel.html).LOW_AND_ABOVE)
                                  .build(),
                              [RaiFilter](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.RaiFilterSettings.RaiFilter.html).newBuilder()
                                  .setFilterType([RaiFilterType](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.RaiFilterType.html).SEXUALLY_EXPLICIT)
                                  .setConfidenceLevel([DetectionConfidenceLevel](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.DetectionConfidenceLevel.html).HIGH)
                                  .build()))
                      .build();
        
              [FilterConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.FilterConfig.html) modelArmorFilter = [FilterConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.FilterConfig.html).newBuilder()
                  .[setRaiSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.FilterConfig.Builder.html#com_google_cloud_modelarmor_v1_FilterConfig_Builder_setRaiSettings_com_google_cloud_modelarmor_v1_RaiFilterSettings_)(raiFilterSettings)
                  .build();
        
              // Create a field mask to specify which fields to update.
              // Ref: https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask
              [FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html) updateMask = [FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html).newBuilder()
                  .[addPaths](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.Builder.html#com_google_protobuf_FieldMask_Builder_addPaths_java_lang_String_)("filter_config.rai_settings")
                  .build();
        
              [FloorSetting](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.FloorSetting.html) floorSetting = [FloorSetting](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.FloorSetting.html).newBuilder()
                  .setName(name)
                  .setFilterConfig(modelArmorFilter)
                  .[setEnableFloorSettingEnforcement](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.FloorSetting.Builder.html#com_google_cloud_modelarmor_v1_FloorSetting_Builder_setEnableFloorSettingEnforcement_boolean_)(true)
                  .build();
        
              [UpdateFloorSettingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.UpdateFloorSettingRequest.html) request = [UpdateFloorSettingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.UpdateFloorSettingRequest.html).newBuilder()
                  .[setFloorSetting](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.UpdateFloorSettingRequest.Builder.html#com_google_cloud_modelarmor_v1_UpdateFloorSettingRequest_Builder_setFloorSetting_com_google_cloud_modelarmor_v1_FloorSetting_)(floorSetting)
                  .setUpdateMask(updateMask)
                  .build();
        
              [FloorSetting](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.FloorSetting.html) updatedFloorSetting = client.updateFloorSetting(request);
              System.out.println("Updated floor setting for organization: " + organizationId);
        
              return updatedFloorSetting;
            }
          }
        }




###  Node.js 

To run this code, first [set up a Node.js development environment](https://docs.cloud.google.com/nodejs/docs/setup) and [install the Model Armor Node.js SDK](https://docs.cloud.google.com/model-armor/reference/libraries#install).

  * Update the Model Armor floor setting for a given project.
        
        /**
         * TODO(developer): Uncomment these variables before running the sample.
         */
        // const projectId = 'your-project-id';
        
        const modelarmor = require('[@google-cloud/modelarmor](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/overview.html)');
        const {ModelArmorClient} = modelarmor.v1;
        const {protos} = modelarmor;
        
        // Initiate client
        const client = new [ModelArmorClient](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/overview.html)();
        
        async function updateProjectFloorSettings() {
          const floorSettingsName = `projects/${projectId}/locations/global/floorSetting`;
        
          // Build the floor settings with your preferred filters
          // For more details on filters, please refer to the following doc:
          // https://cloud.google.com/security-command-center/docs/key-concepts-model-armor#ma-filters
          const floorSetting = {
            name: floorSettingsName,
            filterConfig: {
              raiSettings: {
                raiFilters: [
                  {
                    filterType:
                      protos.google.cloud.modelarmor.v1.[RaiFilterType](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1.raifiltertype.html).[HARASSMENT](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1.raifiltertype.html),
                    confidenceLevel:
                      protos.google.cloud.modelarmor.v1.[DetectionConfidenceLevel](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1.detectionconfidencelevel.html)
                        .LOW_AND_ABOVE,
                  },
                  {
                    filterType:
                      protos.google.cloud.modelarmor.v1.[RaiFilterType](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1.raifiltertype.html)
                        .SEXUALLY_EXPLICIT,
                    confidenceLevel:
                      protos.google.cloud.modelarmor.v1.[DetectionConfidenceLevel](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1.detectionconfidencelevel.html)
                        .LOW_AND_ABOVE,
                  },
                ],
              },
            },
            enableFloorSettingEnforcement: true,
          };
        
          const request = {
            floorSetting: floorSetting,
          };
        
          const [response] = await client.updateFloorSetting(request);
          return response;
        }
        
        return await updateProjectFloorSettings();

  * Update the Model Armor floor setting for a given folder.
        
        /**
         * TODO(developer): Uncomment these variables before running the sample.
         */
        // const folderId = 'your-folder-id';
        
        // Imports the Model Armor library
        const modelarmor = require('[@google-cloud/modelarmor](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/overview.html)');
        const {ModelArmorClient} = modelarmor.v1;
        const {protos} = modelarmor;
        
        // Instantiates a client
        const client = new [ModelArmorClient](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/overview.html)();
        
        async function updateFolderFloorSettings() {
          const floorSettingsName = `folders/${folderId}/locations/global/floorSetting`;
        
          // Build the floor settings with your preferred filters
          // For more details on filters, please refer to the following doc:
          // https://cloud.google.com/security-command-center/docs/key-concepts-model-armor#ma-filters
          const floorSetting = {
            name: floorSettingsName,
            filterConfig: {
              raiSettings: {
                raiFilters: [
                  {
                    filterType:
                      protos.google.cloud.modelarmor.v1.[RaiFilterType](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1.raifiltertype.html).[HARASSMENT](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1.raifiltertype.html),
                    confidenceLevel:
                      protos.google.cloud.modelarmor.v1.[DetectionConfidenceLevel](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1.detectionconfidencelevel.html)
                        .LOW_AND_ABOVE,
                  },
                  {
                    filterType:
                      protos.google.cloud.modelarmor.v1.[RaiFilterType](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1.raifiltertype.html)
                        .SEXUALLY_EXPLICIT,
                    confidenceLevel:
                      protos.google.cloud.modelarmor.v1.[DetectionConfidenceLevel](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1.detectionconfidencelevel.html)
                        .LOW_AND_ABOVE,
                  },
                ],
              },
            },
            enableFloorSettingEnforcement: true,
          };
        
          const request = {
            floorSetting: floorSetting,
          };
        
          const [response] = await client.updateFloorSetting(request);
          return response;
        }
        
        return await updateFolderFloorSettings();

  * Update the Model Armor floor setting for a given organization.
        
        /**
         * TODO(developer): Uncomment these variables before running the sample.
         */
        // const organizationId = 'your-organization-id';
        
        const modelarmor = require('[@google-cloud/modelarmor](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/overview.html)');
        const {ModelArmorClient} = modelarmor.v1;
        const {protos} = modelarmor;
        
        const client = new [ModelArmorClient](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/overview.html)();
        
        async function updateOrganizationFloorSettings() {
          const floorSettingsName = `organizations/${organizationId}/locations/global/floorSetting`;
        
          // Build the floor settings with your preferred filters
          // For more details on filters, please refer to the following doc:
          // https://cloud.google.com/security-command-center/docs/key-concepts-model-armor#ma-filters
          const floorSetting = {
            name: floorSettingsName,
            filterConfig: {
              raiSettings: {
                raiFilters: [
                  {
                    filterType:
                      protos.google.cloud.modelarmor.v1.[RaiFilterType](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1.raifiltertype.html).[HARASSMENT](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1.raifiltertype.html),
                    confidenceLevel:
                      protos.google.cloud.modelarmor.v1.[DetectionConfidenceLevel](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1.detectionconfidencelevel.html)
                        .LOW_AND_ABOVE,
                  },
                  {
                    filterType:
                      protos.google.cloud.modelarmor.v1.[RaiFilterType](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1.raifiltertype.html)
                        .SEXUALLY_EXPLICIT,
                    confidenceLevel:
                      protos.google.cloud.modelarmor.v1.[DetectionConfidenceLevel](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1.detectionconfidencelevel.html)
                        .LOW_AND_ABOVE,
                  },
                ],
              },
            },
            enableFloorSettingEnforcement: true,
          };
        
          const request = {
            floorSetting: floorSetting,
          };
        
          const [response] = await client.updateFloorSetting(request);
          return response;
        }
        
        return await updateOrganizationFloorSettings();




###  PHP 

To run this code, first [set up a PHP development environment](https://docs.cloud.google.com/php/docs/setup) and [install the Model Armor PHP SDK](https://docs.cloud.google.com/model-armor/reference/libraries#install).

  * Update the Model Armor floor setting for a given project.
        
        use Google\Cloud\ModelArmor\V1\Client\ModelArmorClient;
        use Google\Cloud\ModelArmor\V1\RaiFilterType;
        use Google\Cloud\ModelArmor\V1\DetectionConfidenceLevel;
        use Google\Cloud\ModelArmor\V1\UpdateFloorSettingRequest;
        use Google\Cloud\ModelArmor\V1\FilterConfig;
        use Google\Cloud\ModelArmor\V1\FloorSetting;
        use Google\Cloud\ModelArmor\V1\RaiFilterSettings;
        use Google\Cloud\ModelArmor\V1\RaiFilterSettings\RaiFilter;
        
        /**
         * Updates the floor settings for a given project.
         *
         * @param string $projectId The project Id for which the floor settings is to be updated.
         *
         */
        function update_project_floor_settings(string $projectId): void
        {
            $client = new ModelArmorClient();
        
            $floorSettingsName = sprintf('projects/%s/locations/global/floorSetting', $projectId);
        
            // Build the floor settings with your preferred filters
            // For more details on filters, please refer to the following doc:
            // https://cloud.google.com/security-command-center/docs/key-concepts-model-armor#ma-filters
        
            $raiFilterSetting = (new RaiFilterSettings())
                ->setRaiFilters([
                    (new RaiFilter())
                        ->setFilterType(RaiFilterType::HATE_SPEECH)
                        ->setConfidenceLevel(DetectionConfidenceLevel::HIGH)
                ]);
        
            $filterConfig = (new FilterConfig())->setRaiSettings($raiFilterSetting);
            $floorSetting = (new FloorSetting())
                ->setName($floorSettingsName)
                ->setFilterConfig($filterConfig)
                ->setEnableFloorSettingEnforcement(true);
        
            $updateRequest = (new UpdateFloorSettingRequest())->setFloorSetting($floorSetting);
        
            $response = $client->updateFloorSetting($updateRequest);
        
            printf("Floor setting updated: %s\n", $response->getName());
        }

  * Update the Model Armor floor setting for a given folder.
        
        use Google\Cloud\ModelArmor\V1\Client\ModelArmorClient;
        use Google\Cloud\ModelArmor\V1\RaiFilterType;
        use Google\Cloud\ModelArmor\V1\DetectionConfidenceLevel;
        use Google\Cloud\ModelArmor\V1\UpdateFloorSettingRequest;
        use Google\Cloud\ModelArmor\V1\FilterConfig;
        use Google\Cloud\ModelArmor\V1\FloorSetting;
        use Google\Cloud\ModelArmor\V1\RaiFilterSettings;
        use Google\Cloud\ModelArmor\V1\RaiFilterSettings\RaiFilter;
        
        /**
         * Updates the floor settings for a given folder.
         *
         * @param string $folderId The folder Id for which the floor settings is to be updated.
         *
         */
        function update_folder_floor_settings(string $folderId): void
        {
            $client = new ModelArmorClient();
        
            $floorSettingsName = sprintf('folders/%s/locations/global/floorSetting', $folderId);
        
            // Build the floor settings with your preferred filters
            // For more details on filters, please refer to the following doc:
            // https://cloud.google.com/security-command-center/docs/key-concepts-model-armor#ma-filters
        
            $raiFilterSetting = (new RaiFilterSettings())
                ->setRaiFilters([
                    (new RaiFilter())
                        ->setFilterType(RaiFilterType::HATE_SPEECH)
                        ->setConfidenceLevel(DetectionConfidenceLevel::HIGH)
                ]);
        
            $filterConfig = (new FilterConfig())->setRaiSettings($raiFilterSetting);
            $floorSetting = (new FloorSetting())
                ->setName($floorSettingsName)
                ->setFilterConfig($filterConfig)
                ->setEnableFloorSettingEnforcement(true);
        
            $updateRequest = (new UpdateFloorSettingRequest())->setFloorSetting($floorSetting);
        
            $response = $client->updateFloorSetting($updateRequest);
        
            printf("Floor setting updated: %s\n", $response->getName());
        }

  * Update the Model Armor floor setting for a given organization.
        
        use Google\Cloud\ModelArmor\V1\Client\ModelArmorClient;
        use Google\Cloud\ModelArmor\V1\RaiFilterType;
        use Google\Cloud\ModelArmor\V1\DetectionConfidenceLevel;
        use Google\Cloud\ModelArmor\V1\UpdateFloorSettingRequest;
        use Google\Cloud\ModelArmor\V1\FilterConfig;
        use Google\Cloud\ModelArmor\V1\FloorSetting;
        use Google\Cloud\ModelArmor\V1\RaiFilterSettings;
        use Google\Cloud\ModelArmor\V1\RaiFilterSettings\RaiFilter;
        
        /**
         * Updates the floor settings for a given organization.
         *
         * @param string $organizationId The organization Id for which the floor settings is to be updated.
         *
         */
        function update_organization_floor_settings(string $organizationId)
        {
            $client = new ModelArmorClient();
        
            $floorSettingsName = sprintf('organizations/%s/locations/global/floorSetting', $organizationId);
        
            // Build the floor settings with your preferred filters
            // For more details on filters, please refer to the following doc:
            // https://cloud.google.com/security-command-center/docs/key-concepts-model-armor#ma-filters
        
            $raiFilterSetting = (new RaiFilterSettings())
                ->setRaiFilters([
                    (new RaiFilter())
                        ->setFilterType(RaiFilterType::HATE_SPEECH)
                        ->setConfidenceLevel(DetectionConfidenceLevel::HIGH)
                ]);
        
            $filterConfig = (new FilterConfig())->setRaiSettings($raiFilterSetting);
            $floorSetting = (new FloorSetting())
                ->setName($floorSettingsName)
                ->setFilterConfig($filterConfig)
                ->setEnableFloorSettingEnforcement(true);
        
            $updateRequest = (new UpdateFloorSettingRequest())->setFloorSetting($floorSetting);
        
            $response = $client->updateFloorSetting($updateRequest);
        
            printf("Floor setting updated: %s\n", $response->getName());
        }




###  Python 

To run this code, first [set up a Python development environment](https://docs.cloud.google.com/python/docs/setup) and [install the Model Armor Python SDK](https://docs.cloud.google.com/model-armor/reference/libraries#install).

  * Update the Model Armor floor setting for a given project.
        
        from google.cloud import [modelarmor_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest)
        
        # Create the Model Armor client.
        client = [modelarmor_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest).[ModelArmorClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.html)(transport="rest")
        
        # TODO(Developer): Uncomment these variables.
        # project_id = "YOUR_PROJECT_ID"
        
        # Prepare project floor setting path/name
        floor_settings_name = f"projects/{project_id}/locations/global/floorSetting"
        
        # Update the project floor setting
        # For more details on filters, please refer to the following doc:
        # https://cloud.google.com/security-command-center/docs/key-concepts-model-armor#ma-filters
        response = client.[update_floor_setting](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.html#google_cloud_modelarmor_v1_services_model_armor_ModelArmorClient_update_floor_setting)(
            request=[modelarmor_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest).[UpdateFloorSettingRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.UpdateFloorSettingRequest.html)(
                floor_setting=[modelarmor_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest).[FloorSetting](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.FloorSetting.html)(
                    name=floor_settings_name,
                    filter_config=[modelarmor_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest).[FilterConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.FilterConfig.html)(
                        rai_settings=[modelarmor_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest).[RaiFilterSettings](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.RaiFilterSettings.html)(
                            rai_filters=[
                                [modelarmor_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest).[RaiFilterSettings](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.RaiFilterSettings.html).[RaiFilter](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.RaiFilterSettings.RaiFilter.html)(
                                    filter_type=[modelarmor_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest).[RaiFilterType](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.RaiFilterType.html).HATE_SPEECH,
                                    confidence_level=[modelarmor_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest).[DetectionConfidenceLevel](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.DetectionConfidenceLevel.html).HIGH,
                                )
                            ]
                        ),
                    ),
                    enable_floor_setting_enforcement=True,
                )
            )
        )
        # Print the updated config
        print(response)
        

  * Update the Model Armor floor setting for a given folder.
        
        from google.cloud import [modelarmor_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest)
        
        # Create the Model Armor client.
        client = [modelarmor_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest).[ModelArmorClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.html)(transport="rest")
        
        # TODO (Developer): Uncomment these variables and initialize
        # folder_id = "YOUR_FOLDER_ID"
        
        # Prepare folder floor settings path/name
        floor_settings_name = f"folders/{folder_id}/locations/global/floorSetting"
        
        # Update the folder floor setting
        # For more details on filters, please refer to the following doc:
        # https://cloud.google.com/security-command-center/docs/key-concepts-model-armor#ma-filters
        response = client.[update_floor_setting](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.html#google_cloud_modelarmor_v1_services_model_armor_ModelArmorClient_update_floor_setting)(
            request=[modelarmor_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest).[UpdateFloorSettingRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.UpdateFloorSettingRequest.html)(
                floor_setting=[modelarmor_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest).[FloorSetting](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.FloorSetting.html)(
                    name=floor_settings_name,
                    filter_config=[modelarmor_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest).[FilterConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.FilterConfig.html)(
                        rai_settings=[modelarmor_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest).[RaiFilterSettings](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.RaiFilterSettings.html)(
                            rai_filters=[
                                [modelarmor_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest).[RaiFilterSettings](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.RaiFilterSettings.html).[RaiFilter](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.RaiFilterSettings.RaiFilter.html)(
                                    filter_type=[modelarmor_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest).[RaiFilterType](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.RaiFilterType.html).HATE_SPEECH,
                                    confidence_level=[modelarmor_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest).[DetectionConfidenceLevel](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.DetectionConfidenceLevel.html).HIGH,
                                )
                            ]
                        ),
                    ),
                    enable_floor_setting_enforcement=True,
                )
            )
        )
        # Print the updated config
        print(response)
        

  * Update the Model Armor floor setting for a given organization.
        
        from google.cloud import [modelarmor_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest)
        
        # Create the Model Armor client.
        client = [modelarmor_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest).[ModelArmorClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.html)(transport="rest")
        
        # TODO (Developer): Uncomment these variables and initialize
        # organization_id = "YOUR_ORGANIZATION_ID"
        
        # Prepare organization floor setting path/name
        floor_settings_name = (
            f"organizations/{organization_id}/locations/global/floorSetting"
        )
        
        # Update the organization floor setting
        # For more details on filters, please refer to the following doc:
        # https://cloud.google.com/security-command-center/docs/key-concepts-model-armor#ma-filters
        response = client.[update_floor_setting](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.html#google_cloud_modelarmor_v1_services_model_armor_ModelArmorClient_update_floor_setting)(
            request=[modelarmor_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest).[UpdateFloorSettingRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.UpdateFloorSettingRequest.html)(
                floor_setting=[modelarmor_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest).[FloorSetting](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.FloorSetting.html)(
                    name=floor_settings_name,
                    filter_config=[modelarmor_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest).[FilterConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.FilterConfig.html)(
                        rai_settings=[modelarmor_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest).[RaiFilterSettings](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.RaiFilterSettings.html)(
                            rai_filters=[
                                [modelarmor_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest).[RaiFilterSettings](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.RaiFilterSettings.html).[RaiFilter](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.RaiFilterSettings.RaiFilter.html)(
                                    filter_type=[modelarmor_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest).[RaiFilterType](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.RaiFilterType.html).HATE_SPEECH,
                                    confidence_level=[modelarmor_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest).[DetectionConfidenceLevel](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.DetectionConfidenceLevel.html).HIGH,
                                )
                            ]
                        ),
                    ),
                    enable_floor_setting_enforcement=True,
                )
            )
        )
        # Print the updated config
        print(response)
        




## Review findings about floor setting violation

Each [Model Armor finding](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#model-armor-findings) identifies a floor setting violation. A violation occurs when a Model Armor template fails to meet the minimum security standards defined by the resource hierarchy's floor settings. Floor settings define the minimum requirements for templates.

Findings are generated when any of the following floor setting violations occur:

  * A template with less restrictive settings is created before you configure floor settings.
  * A template is missing required filters.
  * A template does not meet the minimum confidence level for the filters.



When the system detects a violation, the system generates a high-severity finding in Security Command Center (if you use the [Premium or Enterprise service tier of Security Command Center](https://docs.cloud.google.com/security-command-center/docs/service-tiers)). The finding specifies the violated floor setting, the non-compliant template, and details about the violation.

The following example shows the finding's `sourceProperties` field. This violation, related to the malicious URI filter, occurred because the template setting for `maliciousUriFilterSettings` is **DISABLED** , but the floor settings require it to be **ENABLED**.
    
    
    {
      "filterConfig": {
        "raiSettings": {
          "raiFilters": [
            {
              "filterType": "HATE_SPEECH",
              "confidenceLevel": {
                "floorSettings": "LOW_AND_ABOVE",
                "template": "MEDIUM_AND_ABOVE"
              }
            },
            {
              "filterType": "HARASSMENT",
              "confidenceLevel": {
                "floorSettings": "MEDIUM_AND_ABOVE",
                "template": "HIGH"
              }
            }
          ]
        },
        "piAndJailbreakFilterSettings": {
          "confidenceLevel": {
            "floorSettings": "LOW_AND_ABOVE",
            "template": "HIGH"
          }
        },
        "maliciousUriFilterSettings": {
          "floorSettings": "ENABLED",
          "template": "DISABLED"
        }
      }
    }

## What's next

  * Learn more about [Model Armor](https://docs.cloud.google.com/model-armor/overview).
  * Learn about [Model Armor templates](https://docs.cloud.google.com/model-armor/manage-templates).
  * [Sanitize prompts and responses](https://docs.cloud.google.com/model-armor/sanitize-prompts-responses).
  * [Troubleshoot Model Armor issues](https://docs.cloud.google.com/model-armor/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
