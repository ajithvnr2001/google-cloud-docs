---
url: https://docs.cloud.google.com/knowledge-catalog/docs/configure-lineage-ingestion/
title: Configure data lineage ingestion for a service \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:37:39.828805+00:00
---

# Configure data lineage ingestion for a service  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/configure-lineage-ingestion/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  Configure data lineage ingestion for a service Stay organized with collections  Save and categorize content based on your preferences. 

You can selectively enable or disable lineage ingestion for specific integrations at the project, folder, or organization level.

For more information about supported integrations and configuration scenarios, see [Control data lineage ingestion](https://docs.cloud.google.com/knowledge-catalog/docs/control-lineage-ingestion).

## Prerequisites

To control lineage ingestion, you must use the Data Lineage API. Ensure you have a client project configured for billing and quota, because the Data Lineage API is a [client-based API](https://docs.cloud.google.com/docs/quotas/quota-project#project-client-based).

### Roles and permissions

To get the permissions that you need to configure and control data lineage ingestion, ask your administrator to grant you the following Identity and Access Management (IAM) roles:

To get the permissions that you need to configure and control data lineage ingestion, ask your administrator to grant you the following IAM roles on your project: 

  * Configure and manage data lineage: [Data Lineage Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/datalineage#datalineage.admin) (`roles/datalineage.admin`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to configure and control data lineage ingestion. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to configure and control data lineage ingestion:

  * Get and update lineage configurations: 
    * `datalineage.configs.get`
    * `datalineage.configs.update`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

  1. Enable the `datalineage.googleapis.com` API in your client project. For more information, see [Enable data lineage](https://docs.cloud.google.com/knowledge-catalog/docs/use-lineage#enable-apis).

  2. Set the client project. For the following examples, use the `X-Goog-User-Project` header. For more information, see [System parameters](https://docs.cloud.google.com/apis/docs/system-parameters).




## Get current configuration

To check whether lineage ingestion is enabled for a resource or to obtain the `etag` value before you modify the configuration, retrieve the current configuration.

### C#

### C#

Before trying this sample, follow the C# setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.DataCatalog.Lineage.ConfigManagement.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.ConfigManagement.V1/latest/Google.Cloud.DataCatalog.Lineage.ConfigManagement.V1.html);
    
    public sealed partial class GeneratedConfigManagementServiceClientSnippets
    {
        /// <summary>Snippet for GetConfig</summary>
        /// <remarks>
        /// This snippet has been automatically generated and should be regarded as a code template only.
        /// It will require modifications to work:
        /// - It may require correct/in-range values for request initialization.
        /// - It may require specifying regional endpoints when creating the service client as shown in
        ///   https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
        /// </remarks>
        public void GetConfigRequestObject()
        {
            // Create client
            [ConfigManagementServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.ConfigManagement.V1/latest/Google.Cloud.DataCatalog.Lineage.ConfigManagement.V1.ConfigManagementServiceClient.html) configManagementServiceClient = [ConfigManagementServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.ConfigManagement.V1/latest/Google.Cloud.DataCatalog.Lineage.ConfigManagement.V1.ConfigManagementServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.ConfigManagement.V1/latest/Google.Cloud.DataCatalog.Lineage.ConfigManagement.V1.ConfigManagementServiceClient.html#Google_Cloud_DataCatalog_Lineage_ConfigManagement_V1_ConfigManagementServiceClient_Create)();
            // Initialize request argument(s)
            [GetConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.ConfigManagement.V1/latest/Google.Cloud.DataCatalog.Lineage.ConfigManagement.V1.GetConfigRequest.html) request = new [GetConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.ConfigManagement.V1/latest/Google.Cloud.DataCatalog.Lineage.ConfigManagement.V1.GetConfigRequest.html)
            {
                ConfigName = [ConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.ConfigManagement.V1/latest/Google.Cloud.DataCatalog.Lineage.ConfigManagement.V1.ConfigName.html).[FromProjectLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.ConfigManagement.V1/latest/Google.Cloud.DataCatalog.Lineage.ConfigManagement.V1.ConfigName.html#Google_Cloud_DataCatalog_Lineage_ConfigManagement_V1_ConfigName_FromProjectLocation_System_String_System_String_)("[PROJECT]", "[LOCATION]"),
            };
            // Make the request
            [Config](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.ConfigManagement.V1/latest/Google.Cloud.DataCatalog.Lineage.ConfigManagement.V1.UpdateConfigRequest.html#Google_Cloud_DataCatalog_Lineage_ConfigManagement_V1_UpdateConfigRequest_Config) response = configManagementServiceClient.[GetConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.ConfigManagement.V1/latest/Google.Cloud.DataCatalog.Lineage.ConfigManagement.V1.ConfigManagementServiceClient.html#Google_Cloud_DataCatalog_Lineage_ConfigManagement_V1_ConfigManagementServiceClient_GetConfig_Google_Cloud_DataCatalog_Lineage_ConfigManagement_V1_ConfigName_Google_Api_Gax_Grpc_CallSettings_)(request);
        }
    }

### Go

### Go

Before trying this sample, follow the Go setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/dataplex). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    //go:build examples
    
    package main
    
    import (
    	"context"
    
    	configmanagement "cloud.google.com/go/datacatalog/lineage/configmanagement/apiv1"
    	configmanagementpb "cloud.google.com/go/datacatalog/lineage/configmanagement/apiv1/configmanagementpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := configmanagement.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/configmanagement/apiv1.html#cloud_google_com_go_datacatalog_lineage_configmanagement_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/configmanagement/apiv1.html#cloud_google_com_go_datacatalog_lineage_configmanagement_apiv1_Client_Close)()
    
    	req := &configmanagementpb.GetConfigRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/datacatalog/lineage/configmanagement/apiv1/configmanagementpb#GetConfigRequest.
    	}
    	resp, err := c.GetConfig(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### Java

### Java

Before trying this sample, follow the Java setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/overview). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.datacatalog.lineage.configmanagement.v1.[Config](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.Config.html);
    import com.google.cloud.datacatalog.lineage.configmanagement.v1.[ConfigManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.ConfigManagementServiceClient.html);
    import com.google.cloud.datacatalog.lineage.configmanagement.v1.[ConfigName](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.ConfigName.html);
    import com.google.cloud.datacatalog.lineage.configmanagement.v1.[GetConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.GetConfigRequest.html);
    
    public class SyncGetConfig {
    
      public static void main(String[] args) throws Exception {
        syncGetConfig();
      }
    
      public static void syncGetConfig() throws Exception {
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try ([ConfigManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.ConfigManagementServiceClient.html) configManagementServiceClient =
            [ConfigManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.ConfigManagementServiceClient.html).create()) {
          [GetConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.GetConfigRequest.html) request =
              [GetConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.GetConfigRequest.html).newBuilder()
                  .setName([ConfigName](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.ConfigName.html).[ofProjectLocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.ConfigName.html#com_google_cloud_datacatalog_lineage_configmanagement_v1_ConfigName_ofProjectLocationName_java_lang_String_java_lang_String_)("[PROJECT]", "[LOCATION]").[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.ConfigName.html#com_google_cloud_datacatalog_lineage_configmanagement_v1_ConfigName_toString__)())
                  .build();
          [Config](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.Config.html) response = configManagementServiceClient.getConfig(request);
        }
      }
    }

### Python

### Python

Before trying this sample, follow the Python setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [datacatalog_lineage_configmanagement_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-datacatalog-lineage-configmanagement/latest)
    
    
    def sample_get_config():
        # Create a client
        client = [datacatalog_lineage_configmanagement_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-datacatalog-lineage-configmanagement/latest).[ConfigManagementServiceClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-datacatalog-lineage-configmanagement/latest/google.cloud.datacatalog_lineage_configmanagement_v1.services.config_management_service.ConfigManagementServiceClient.html)()
    
        # Initialize request argument(s)
        request = [datacatalog_lineage_configmanagement_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-datacatalog-lineage-configmanagement/latest).[GetConfigRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-datacatalog-lineage-configmanagement/latest/google.cloud.datacatalog_lineage_configmanagement_v1.types.GetConfigRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = client.[get_config](https://docs.cloud.google.com/python/docs/reference/google-cloud-datacatalog-lineage-configmanagement/latest/google.cloud.datacatalog_lineage_configmanagement_v1.services.config_management_service.ConfigManagementServiceClient.html#google_cloud_datacatalog_lineage_configmanagement_v1_services_config_management_service_ConfigManagementServiceClient_get_config)(request=request)
    
        # Handle the response
        print(response)
    
    

### gcloud

To view the current lineage configuration, use the [`gcloud datalineage config describe`](https://docs.cloud.google.com/sdk/gcloud/reference/datalineage/config/describe) command. You can retrieve the configuration for a project, folder, or organization.

The following example shows how to get the configuration for the current project:
    
    
    gcloud datalineage config describe
    

For example, to get the configuration for a specific project, use the `--project` flag:
    
    
    gcloud datalineage config describe --project=PROJECT_ID
    

Replace the following:

  * `PROJECT_ID`: The ID of the project whose configuration you want to view.



To view the current lineage ingestion configuration of a service for a folder or organization, replace `--project=`PROJECT_ID`` with one of the following:

  * `--folder=`FOLDER_ID`` if you want to view the data ingestion settings for a folder.
  * `--organization=`ORGANIZATION_ID`` if you want to view the data ingestion settings for an organization.



### REST

To view the current lineage configuration, use the [`projects.locations.config.get`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/data-lineage/rest/v1/projects.locations.config/get) method. You can retrieve the configuration for a project, folder, or organization.

The following example shows how to get the configuration for a project:

Before using any of the request data, make the following replacements: 

  * `CLIENT_PROJECT_ID`: The ID of your client project used for billing or quotas.
  * `PROJECT_ID`: The ID of the project whose configuration you want to view.



HTTP method and URL: 
    
    
    GET https://datalineage.googleapis.com/v1/projects/PROJECT_ID/locations/global/config

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: CLIENT_PROJECT_ID" \  
         "https://datalineage.googleapis.com/v1/projects/PROJECT_ID/locations/global/config"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "CLIENT_PROJECT_ID" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://datalineage.googleapis.com/v1/projects/PROJECT_ID/locations/global/config" | Select-Object -Expand Content

The command returns one of the following outputs:

  * If you don't provide any lineage ingestion settings, you get an output with an empty `ingestion` object: 
        
        {
          "name": "projects/123456789012/locations/global/config",
          "ingestion": {}
        }
          

This means that the service uses the default lineage ingestion setting. In this example, the lineage ingestion setting for Managed Service for Apache Spark is `enabled`.

  * If you enable lineage ingestion explicitly, you get the following output: 
        
        {
          "name": "projects/123456789012/locations/global/config",
          "ingestion": {
            "rules": [
              {
                "integrationSelector": {
                  "integration": "DATAPROC"
                },
                "lineageEnablement": {
                  "enabled": true
                }
              }
            ]
          },
          "etag": "1a2b3c4d5e"
        }
          

  * If the lineage ingestion is disabled, you get the following output: 
        
        {
          "name": "projects/123456789012/locations/global/config",
          "ingestion": {
            "rules": [
              {
                "integrationSelector": {
                  "integration": "DATAPROC"
                },
                "lineageEnablement": {
                  "enabled": false
                }
              }
            ]
          },
          "etag": "1a2b3c4d5e"
        }
          




To get the configuration for a folder or organization, replace `projects/`"PROJECT_ID`` with `folders/`FOLDER_ID`` or `organizations/`ORGANIZATION_ID``.

The `etag` field in the response is a checksum generated by the server based on the current value of the configuration. When you update a configuration by using the `patch` method, you can include the `etag` value returned from a recent `get` request in the request body. If you provide the `etag`, Knowledge Catalog uses it to verify that the configuration hasn't changed since your last read request. If there's a mismatch, the update request fails. This prevents you from unintentionally overwriting configurations made by other users in read-modify-write scenarios. If you don't provide an `etag` in your `patch` request, Knowledge Catalog overwrites the configuration unconditionally.

## Disable lineage ingestion for a service

To manage costs, enforce data governance policies, or exclude development projects and other workloads that don't benefit from lineage tracking, disable lineage ingestion for a service.

### Java
    
    
    package com.google.cloud.datacatalog.lineage.configmanagement.v1.samples;
    
    import com.google.api.gax.rpc.[NotFoundException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.NotFoundException.html);
    import com.google.cloud.datacatalog.lineage.configmanagement.v1.[Config](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.Config.html);
    import com.google.cloud.datacatalog.lineage.configmanagement.v1.[Config](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.Config.html).[Ingestion](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.Config.Ingestion.html);
    import com.google.cloud.datacatalog.lineage.configmanagement.v1.[Config](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.Config.html).[Ingestion](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.Config.Ingestion.html).[IngestionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.Config.Ingestion.IngestionRule.html);
    import com.google.cloud.datacatalog.lineage.configmanagement.v1.[Config](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.Config.html).[Ingestion](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.Config.Ingestion.html).[IngestionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.Config.Ingestion.IngestionRule.html).[IntegrationSelector](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.Config.Ingestion.IngestionRule.IntegrationSelector.html);
    import com.google.cloud.datacatalog.lineage.configmanagement.v1.[Config](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.Config.html).[Ingestion](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.Config.Ingestion.html).[IngestionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.Config.Ingestion.IngestionRule.html).[IntegrationSelector](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.Config.Ingestion.IngestionRule.IntegrationSelector.html).[Integration](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.Config.Ingestion.IngestionRule.IntegrationSelector.Integration.html);
    import com.google.cloud.datacatalog.lineage.configmanagement.v1.[Config](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.Config.html).[Ingestion](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.Config.Ingestion.html).[IngestionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.Config.Ingestion.IngestionRule.html).[LineageEnablement](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.Config.Ingestion.IngestionRule.LineageEnablement.html);
    import com.google.cloud.datacatalog.lineage.configmanagement.v1.[ConfigManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.ConfigManagementServiceClient.html);
    import com.google.cloud.datacatalog.lineage.configmanagement.v1.[ConfigName](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.ConfigName.html);
    import com.google.cloud.datacatalog.lineage.configmanagement.v1.[GetConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.GetConfigRequest.html);
    import com.google.cloud.datacatalog.lineage.configmanagement.v1.[UpdateConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.UpdateConfigRequest.html);
    
    public class DisableLineageIngestion {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String location = "global";
        disableLineageIngestion(projectId, location);
      }
    
      // Disables lineage ingestion for a specific service
      // (Managed Service for Apache Spark).
      public static void disableLineageIngestion(String projectId, String location) throws Exception {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([ConfigManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.ConfigManagementServiceClient.html) client = [ConfigManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.ConfigManagementServiceClient.html).create()) {
          // Format the resource name.
          String name = [ConfigName](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.ConfigName.html).[ofProjectLocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.ConfigName.html#com_google_cloud_datacatalog_lineage_configmanagement_v1_ConfigName_ofProjectLocationName_java_lang_String_java_lang_String_)(projectId, location).toString();
    
          [Config](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.Config.html).Builder configBuilder = [Config](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.Config.html).newBuilder().setName(name);
    
          // It is a best practice to read the existing config to preserve other rules
          // and use the etag for optimistic concurrency control.
          try {
            [GetConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.GetConfigRequest.html) getRequest = [GetConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.GetConfigRequest.html).newBuilder().setName(name).build();
            [Config](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.Config.html) existingConfig = client.getConfig(getRequest);
            configBuilder.mergeFrom(existingConfig);
          } catch ([NotFoundException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.NotFoundException.html) e) {
            // If config doesn't exist, we will proceed by creating a new one.
          }
    
          // Create an integration selector for the service you want to disable.
          [IntegrationSelector](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.Config.Ingestion.IngestionRule.IntegrationSelector.html) selector =
              [IntegrationSelector](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.Config.Ingestion.IngestionRule.IntegrationSelector.html).newBuilder().[setIntegration](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.Config.Ingestion.IngestionRule.IntegrationSelector.Builder.html#com_google_cloud_datacatalog_lineage_configmanagement_v1_Config_Ingestion_IngestionRule_IntegrationSelector_Builder_setIntegration_com_google_cloud_datacatalog_lineage_configmanagement_v1_Config_Ingestion_IngestionRule_IntegrationSelector_Integration_)([Integration](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.Config.Ingestion.IngestionRule.IntegrationSelector.Integration.html).DATAPROC).build();
    
          // Set lineage enablement to false to disable tracking.
          [LineageEnablement](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.Config.Ingestion.IngestionRule.LineageEnablement.html) enablement = [LineageEnablement](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.Config.Ingestion.IngestionRule.LineageEnablement.html).newBuilder().[setEnabled](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.Config.Ingestion.IngestionRule.LineageEnablement.Builder.html#com_google_cloud_datacatalog_lineage_configmanagement_v1_Config_Ingestion_IngestionRule_LineageEnablement_Builder_setEnabled_boolean_)(false).build();
    
          // Build the ingestion rule.
          [IngestionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.Config.Ingestion.IngestionRule.html) disableRule =
              [IngestionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.Config.Ingestion.IngestionRule.html).newBuilder()
                  .[setIntegrationSelector](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.Config.Ingestion.IngestionRule.Builder.html#com_google_cloud_datacatalog_lineage_configmanagement_v1_Config_Ingestion_IngestionRule_Builder_setIntegrationSelector_com_google_cloud_datacatalog_lineage_configmanagement_v1_Config_Ingestion_IngestionRule_IntegrationSelector_)(selector)
                  .[setLineageEnablement](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.Config.Ingestion.IngestionRule.Builder.html#com_google_cloud_datacatalog_lineage_configmanagement_v1_Config_Ingestion_IngestionRule_Builder_setLineageEnablement_com_google_cloud_datacatalog_lineage_configmanagement_v1_Config_Ingestion_IngestionRule_LineageEnablement_)(enablement)
                  .build();
    
          // Preserve existing rules except for the one we are modifying, then add the new rule.
          // We clear the ingestion block out of the configBuilder entirely to reconstruct it.
          [Ingestion](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.Config.Ingestion.html).Builder ingestionBuilder = [Ingestion](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.Config.Ingestion.html).newBuilder();
          if (configBuilder.hasIngestion()) {
            for ([IngestionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.Config.Ingestion.IngestionRule.html) rule : configBuilder.getIngestion().getRulesList()) {
              // Keep all existing rules EXCEPT the one targeting DATAPROC
              if (rule.getIntegrationSelector().getIntegration() != [Integration](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.Config.Ingestion.IngestionRule.IntegrationSelector.Integration.html).DATAPROC) {
                ingestionBuilder.[addRules](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.Config.Ingestion.Builder.html#com_google_cloud_datacatalog_lineage_configmanagement_v1_Config_Ingestion_Builder_addRules_com_google_cloud_datacatalog_lineage_configmanagement_v1_Config_Ingestion_IngestionRule_)(rule);
              }
            }
          }
          ingestionBuilder.[addRules](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.Config.Ingestion.Builder.html#com_google_cloud_datacatalog_lineage_configmanagement_v1_Config_Ingestion_Builder_addRules_com_google_cloud_datacatalog_lineage_configmanagement_v1_Config_Ingestion_IngestionRule_)(disableRule);
    
          // Update the config builder with the reconstructed ingestion settings.
          configBuilder.[setIngestion](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.Config.Builder.html#com_google_cloud_datacatalog_lineage_configmanagement_v1_Config_Builder_setIngestion_com_google_cloud_datacatalog_lineage_configmanagement_v1_Config_Ingestion_)(ingestionBuilder.build());
    
          // Build the update request.
          [UpdateConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.UpdateConfigRequest.html) request = [UpdateConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.UpdateConfigRequest.html).newBuilder()
              .[setConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.UpdateConfigRequest.Builder.html#com_google_cloud_datacatalog_lineage_configmanagement_v1_UpdateConfigRequest_Builder_setConfig_com_google_cloud_datacatalog_lineage_configmanagement_v1_Config_)(configBuilder.build())
              .build();
    
          // Update the config.
          [Config](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.Config.html) response = client.updateConfig(request);
          System.out.printf("Successfully updated config: %s\n", response.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.Config.html#com_google_cloud_datacatalog_lineage_configmanagement_v1_Config_getName__)());
        }
      }
    }
    

### Python
    
    
    from google.api_core.exceptions import NotFound
    from google.cloud.datacatalog.lineage import configmanagement_v1
    
    def disable_lineage_ingestion(project_id: str, location: str = "global") -> configmanagement_v1.Config:
        """Disables lineage ingestion for a specific service.
    
        Args:
            project_id: The ID of your Google Cloud project.
            location: The region location, usually 'global'.
    
        Returns:
            The updated Configuration object.
        """
        # Initialize client that will be used to send requests.
        client = configmanagement_v1.ConfigManagementServiceClient()
    
        # The config name format
        name = f"projects/{project_id}/locations/{location}/config"
    
        try:
            # Retrieve the existing config to preserve other configurations and
            # obtain the latest etag for optimistic concurrency control.
            config = client.get_config(name=name)
    
            # Filter out existing rules for the integration we are updating
            new_rules = [
                rule for rule in config.ingestion.rules
                if rule.integration_selector.integration != configmanagement_v1.Config.Ingestion.IngestionRule.IntegrationSelector.Integration.DATAPROC
            ]
        except NotFound:
            # If the config does not exist, start fresh
            config = configmanagement_v1.Config(name=name)
            new_rules = []
    
        # Define the integration to disable tracking for (e.g., DATAPROC).
        integration_selector = configmanagement_v1.Config.Ingestion.IngestionRule.IntegrationSelector(
            integration=configmanagement_v1.Config.Ingestion.IngestionRule.IntegrationSelector.Integration.DATAPROC
        )
    
        # Set lineage enablement to False to disable tracking.
        lineage_enablement = configmanagement_v1.Config.Ingestion.IngestionRule.LineageEnablement(
            enabled=False
        )
    
        # Create the ingestion rule.
        disable_rule = configmanagement_v1.Config.Ingestion.IngestionRule(
            integration_selector=integration_selector,
            lineage_enablement=lineage_enablement,
        )
         # Append the new disabling rule and assign it back to the config ingestion rules
        new_rules.append(disable_rule)
        config.ingestion = configmanagement_v1.Config.Ingestion(rules=new_rules)
    
        # Create the update request using the config (which includes the etag if it existed).
        request = configmanagement_v1.UpdateConfigRequest(
            config=config,
        )
    
        # Make the request to update the config
        response = client.update_config(request=request)
    
        print(f"Successfully updated config: {response.name}")
        return response
    

### gcloud

To disable lineage ingestion for a specific service, use the [`gcloud datalineage config update`](https://docs.cloud.google.com/sdk/gcloud/reference/datalineage/config/update) command with an inline JSON string or a path to a JSON file that sets `lineageEnablement.enabled` to `false` for the specific `integration`.

The following example shows how to disable lineage ingestion of a service for a project using an inline JSON string:
    
    
    gcloud datalineage config update --project=PROJECT_ID \
      --config='{
        "ingestion": {
          "rules": [
            {
              "integrationSelector": {
                "integration": "INTEGRATION"
              },
              "lineageEnablement": {
                "enabled": false
              }
            }
          ]
        },
        "etag": "ETAG"
      }'
    

Replace the following:

  * `PROJECT_ID`: The ID of the project whose configuration you want to update.
  * `INTEGRATION`: The integration you set the configuration for. For example, `DATAPROC` or `BIGQUERY`.
  * `ETAG`: The `etag` value returned from a recent `get` request in the request body, used to verify that the configuration hasn't changed since your last read request.



To update the configuration using a JSON file, run:
    
    
    gcloud datalineage config update --project=PROJECT_ID --config=CONFIG_FILE
    

Replace the following:

  * `CONFIG_FILE`: The path to the JSON file containing the configuration.



To disable lineage ingestion of a service for a folder or organization, replace `--project=`PROJECT_ID`` with one of the following:

  * `--folder=`FOLDER_ID`` if you want to update the data ingestion settings for a folder.
  * `--organization=`ORGANIZATION_ID`` if you want to update the data ingestion settings for an organization.



### REST

To disable lineage ingestion for a specific service, use the [`projects.locations.config.patch`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/data-lineage/rest/v1/projects.locations.config/patch) method with an ingestion rule that sets `lineageEnablement.enabled` to `false` for the specific `integration`.

To prevent unintentionally overwriting configurations made by other users in read-modify-write scenarios, you can include the `etag` field in the request body. For more information, see Get current configuration.

Before using any of the request data, make the following replacements: 

  * `CLIENT_PROJECT_ID`: The ID of your client project used for billing or quotas.
  * `PROJECT_ID`: The ID of the project whose configuration you want to update.
  * `ETAG`: The `etag` value returned from a recent `get` request.
  * `INTEGRATION`: The `integration` you set the configuration for. For example, `DATAPROC`.



HTTP method and URL: 
    
    
    PATCH https://datalineage.googleapis.com/v1/projects/PROJECT_ID/locations/global/config

Request JSON body: 
    
    
    {
      "ingestion": {
        "rules": [
          {
            "integrationSelector": {
              "integration": "INTEGRATION"
            },
            "lineageEnablement": {
              "enabled": false
            }
          }
        ]
      },
      "etag": "ETAG"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: CLIENT_PROJECT_ID" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://datalineage.googleapis.com/v1/projects/PROJECT_ID/locations/global/config"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "CLIENT_PROJECT_ID" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://datalineage.googleapis.com/v1/projects/PROJECT_ID/locations/global/config" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/global/config",
      "ingestion": {
        "rules": [
          {
            "integrationSelector": {
              "integration": "INTEGRATION"
            },
            "lineageEnablement": {
              "enabled": false
            }
          }
        ]
      },
      "etag": "1a2b3c4d5e"
    }
    

To disable the lineage ingestion for a folder or organization, replace `projects/`"PROJECT_ID`` with `folders/`FOLDER_ID`` or `organizations/`ORGANIZATION_ID``.

## Enable lineage ingestion for a service

To resume tracking after disabling it, or to enable an integration that is disabled by default, enable lineage ingestion for a service.

### Java
    
    
    package com.google.cloud.datacatalog.lineage.configmanagement.v1.samples;
    
    import com.google.api.gax.rpc.[NotFoundException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.NotFoundException.html);
    import com.google.cloud.datacatalog.lineage.configmanagement.v1.[Config](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.Config.html);
    import com.google.cloud.datacatalog.lineage.configmanagement.v1.[Config](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.Config.html).[Ingestion](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.Config.Ingestion.html);
    import com.google.cloud.datacatalog.lineage.configmanagement.v1.[Config](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.Config.html).[Ingestion](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.Config.Ingestion.html).[IngestionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.Config.Ingestion.IngestionRule.html);
    import com.google.cloud.datacatalog.lineage.configmanagement.v1.[Config](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.Config.html).[Ingestion](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.Config.Ingestion.html).[IngestionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.Config.Ingestion.IngestionRule.html).[IntegrationSelector](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.Config.Ingestion.IngestionRule.IntegrationSelector.html);
    import com.google.cloud.datacatalog.lineage.configmanagement.v1.[Config](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.Config.html).[Ingestion](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.Config.Ingestion.html).[IngestionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.Config.Ingestion.IngestionRule.html).[IntegrationSelector](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.Config.Ingestion.IngestionRule.IntegrationSelector.html).[Integration](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.Config.Ingestion.IngestionRule.IntegrationSelector.Integration.html);
    import com.google.cloud.datacatalog.lineage.configmanagement.v1.[Config](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.Config.html).[Ingestion](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.Config.Ingestion.html).[IngestionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.Config.Ingestion.IngestionRule.html).[LineageEnablement](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.Config.Ingestion.IngestionRule.LineageEnablement.html);
    import com.google.cloud.datacatalog.lineage.configmanagement.v1.[ConfigManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.ConfigManagementServiceClient.html);
    import com.google.cloud.datacatalog.lineage.configmanagement.v1.[ConfigName](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.ConfigName.html);
    import com.google.cloud.datacatalog.lineage.configmanagement.v1.[GetConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.GetConfigRequest.html);
    import com.google.cloud.datacatalog.lineage.configmanagement.v1.[UpdateConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.UpdateConfigRequest.html);
    
    public class EnableLineageIngestion {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String location = "global";
        enableLineageIngestion(projectId, location);
      }
    
      // Enables lineage ingestion for a specific service
      // (Managed Service for Apache Spark).
      public static void enableLineageIngestion(String projectId, String location) throws Exception {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([ConfigManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.ConfigManagementServiceClient.html) client = [ConfigManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.ConfigManagementServiceClient.html).create()) {
          // Format the resource name.
          String name = [ConfigName](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.ConfigName.html).[ofProjectLocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.ConfigName.html#com_google_cloud_datacatalog_lineage_configmanagement_v1_ConfigName_ofProjectLocationName_java_lang_String_java_lang_String_)(projectId, location).toString();
    
          [Config](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.Config.html).Builder configBuilder = [Config](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.Config.html).newBuilder().setName(name);
    
          // It is a best practice to read the existing config to preserve other rules
          // and use the etag for optimistic concurrency control.
          try {
            [GetConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.GetConfigRequest.html) getRequest = [GetConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.GetConfigRequest.html).newBuilder().setName(name).build();
            [Config](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.Config.html) existingConfig = client.getConfig(getRequest);
            configBuilder.mergeFrom(existingConfig);
          } catch ([NotFoundException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.NotFoundException.html) e) {
            // If config doesn't exist, we will proceed by creating a new one.
          }
    
          // Create an integration selector for the service you want to enable (e.g., DATAPROC).
          [IntegrationSelector](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.Config.Ingestion.IngestionRule.IntegrationSelector.html) selector =
              [IntegrationSelector](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.Config.Ingestion.IngestionRule.IntegrationSelector.html).newBuilder().[setIntegration](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.Config.Ingestion.IngestionRule.IntegrationSelector.Builder.html#com_google_cloud_datacatalog_lineage_configmanagement_v1_Config_Ingestion_IngestionRule_IntegrationSelector_Builder_setIntegration_com_google_cloud_datacatalog_lineage_configmanagement_v1_Config_Ingestion_IngestionRule_IntegrationSelector_Integration_)([Integration](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.Config.Ingestion.IngestionRule.IntegrationSelector.Integration.html).DATAPROC).build();
    
          // Set lineage enablement to true to enable tracking.
          [LineageEnablement](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.Config.Ingestion.IngestionRule.LineageEnablement.html) enablement = [LineageEnablement](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.Config.Ingestion.IngestionRule.LineageEnablement.html).newBuilder().[setEnabled](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.Config.Ingestion.IngestionRule.LineageEnablement.Builder.html#com_google_cloud_datacatalog_lineage_configmanagement_v1_Config_Ingestion_IngestionRule_LineageEnablement_Builder_setEnabled_boolean_)(true).build();
    
          // Build the ingestion rule.
          [IngestionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.Config.Ingestion.IngestionRule.html) enableRule =
              [IngestionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.Config.Ingestion.IngestionRule.html).newBuilder()
                  .[setIntegrationSelector](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.Config.Ingestion.IngestionRule.Builder.html#com_google_cloud_datacatalog_lineage_configmanagement_v1_Config_Ingestion_IngestionRule_Builder_setIntegrationSelector_com_google_cloud_datacatalog_lineage_configmanagement_v1_Config_Ingestion_IngestionRule_IntegrationSelector_)(selector)
                  .[setLineageEnablement](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.Config.Ingestion.IngestionRule.Builder.html#com_google_cloud_datacatalog_lineage_configmanagement_v1_Config_Ingestion_IngestionRule_Builder_setLineageEnablement_com_google_cloud_datacatalog_lineage_configmanagement_v1_Config_Ingestion_IngestionRule_LineageEnablement_)(enablement)
                  .build();
    
          // Preserve existing rules except for the one we are modifying, then add the new rule.
          // We clear the ingestion block out of the configBuilder entirely to reconstruct it.
          [Ingestion](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.Config.Ingestion.html).Builder ingestionBuilder = [Ingestion](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.Config.Ingestion.html).newBuilder();
          if (configBuilder.hasIngestion()) {
            for ([IngestionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.Config.Ingestion.IngestionRule.html) rule : configBuilder.getIngestion().getRulesList()) {
              // Keep all existing rules EXCEPT the one targeting DATAPROC
              if (rule.getIntegrationSelector().getIntegration() != [Integration](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.Config.Ingestion.IngestionRule.IntegrationSelector.Integration.html).DATAPROC) {
                ingestionBuilder.[addRules](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.Config.Ingestion.Builder.html#com_google_cloud_datacatalog_lineage_configmanagement_v1_Config_Ingestion_Builder_addRules_com_google_cloud_datacatalog_lineage_configmanagement_v1_Config_Ingestion_IngestionRule_)(rule);
              }
            }
          }
          ingestionBuilder.[addRules](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.Config.Ingestion.Builder.html#com_google_cloud_datacatalog_lineage_configmanagement_v1_Config_Ingestion_Builder_addRules_com_google_cloud_datacatalog_lineage_configmanagement_v1_Config_Ingestion_IngestionRule_)(enableRule);
    
          // Update the config builder with the reconstructed ingestion settings.
          configBuilder.[setIngestion](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.Config.Builder.html#com_google_cloud_datacatalog_lineage_configmanagement_v1_Config_Builder_setIngestion_com_google_cloud_datacatalog_lineage_configmanagement_v1_Config_Ingestion_)(ingestionBuilder.build());
    
          // Build the update request.
          [UpdateConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.UpdateConfigRequest.html) request = [UpdateConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.UpdateConfigRequest.html).newBuilder()
              .[setConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.UpdateConfigRequest.Builder.html#com_google_cloud_datacatalog_lineage_configmanagement_v1_UpdateConfigRequest_Builder_setConfig_com_google_cloud_datacatalog_lineage_configmanagement_v1_Config_)(configBuilder.build())
              .build();
    
          // Update the config.
          [Config](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.Config.html) response = client.updateConfig(request);
          System.out.printf("Successfully updated config: %s\n", response.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.configmanagement.v1.Config.html#com_google_cloud_datacatalog_lineage_configmanagement_v1_Config_getName__)());
        }
      }
    }
    

### Python
    
    
    from google.api_core.exceptions import NotFound
    from google.cloud.datacatalog.lineage import configmanagement_v1
    
    def enable_lineage_ingestion(project_id: str, location: str = "global") -> configmanagement_v1.Config:
        """Enables lineage ingestion for a specific service like Dataproc
        (Managed Service for Apache Spark).
    
        Args:
            project_id: The ID of your Google Cloud project.
            location: The region location, usually 'global'.
    
        Returns:
            The updated Configuration object.
        """
        # Initialize client that will be used to send requests.
        client = configmanagement_v1.ConfigManagementServiceClient()
    
        # The config name format
        name = f"projects/{project_id}/locations/{location}/config"
    
        try:
            # Retrieve the existing config to preserve other configurations and
            # obtain the latest etag for optimistic concurrency control.
            config = client.get_config(name=name)
    
            # Filter out existing rules for the integration we are updating
            new_rules = [
                rule for rule in config.ingestion.rules
                if rule.integration_selector.integration != configmanagement_v1.Config.Ingestion.IngestionRule.IntegrationSelector.Integration.DATAPROC
            ]
        except NotFound:
            # If the config does not exist, start fresh
            config = configmanagement_v1.Config(name=name)
            new_rules = []
    
        # Define the integration to enable tracking for (e.g., DATAPROC).
        integration_selector = configmanagement_v1.Config.Ingestion.IngestionRule.IntegrationSelector(
            integration=configmanagement_v1.Config.Ingestion.IngestionRule.IntegrationSelector.Integration.DATAPROC
        )
    
        # Set lineage enablement to True to enable tracking.
        lineage_enablement = configmanagement_v1.Config.Ingestion.IngestionRule.LineageEnablement(
            enabled=True
        )
    
        # Create the ingestion rule.
        enable_rule = configmanagement_v1.Config.Ingestion.IngestionRule(
            integration_selector=integration_selector,
            lineage_enablement=lineage_enablement,
        )
    
        # Append the new enabling rule and assign it back to the config ingestion rules
        new_rules.append(enable_rule)
        config.ingestion = configmanagement_v1.Config.Ingestion(rules=new_rules)
    
        # Create the update request using the config (which includes the etag if it existed).
        request = configmanagement_v1.UpdateConfigRequest(
            config=config,
        )
    
        # Make the request to update the config
        response = client.update_config(request=request)
    
        print(f"Successfully updated config: {response.name}")
        return response
    

### gcloud

To enable lineage ingestion for a specific service, use the [`gcloud datalineage config update`](https://docs.cloud.google.com/sdk/gcloud/reference/datalineage/config/update) command with an inline JSON string or a path to a JSON file that sets `lineageEnablement.enabled` to `true` for the specific `integration`. Current integrations include Managed Service for Apache Spark, BigQuery, and Managed Airflow.

The following example shows how to enable lineage ingestion of a service for a project using an inline JSON string:
    
    
    gcloud datalineage config update --project=PROJECT_ID \
      --config='{
        "ingestion": {
          "rules": [
            {
              "integrationSelector": {
                "integration": "INTEGRATION"
              },
              "lineageEnablement": {
                "enabled": true
              }
            }
          ]
        },
        "etag": "ETAG"
      }'
    

Replace the following:

  * `PROJECT_ID`: The ID of the project whose configuration you want to update.
  * `INTEGRATION`: The integration you set the configuration for (for example, `DATAPROC` or `BIGQUERY`).
  * `ETAG`: The `etag` value returned from a recent `get` request in the request body, used to verify that the configuration hasn't changed since your last read request.



To update the configuration using a JSON file, run:
    
    
    gcloud datalineage config update --project=PROJECT_ID --config=CONFIG_FILE
    

Replace the following:

  * `CONFIG_FILE`: The path to the JSON file containing the configuration.



To enable lineage ingestion of a service for a folder or organization, replace `--project=`PROJECT_ID`` with one of the following:

  * `--folder=`FOLDER_ID`` if you want to update the data ingestion settings for a folder.
  * `--organization=`ORGANIZATION_ID`` if you want to update the data ingestion settings for an organization.



### REST

To enable lineage ingestion for a specific service, use the [`projects.locations.config.patch`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/data-lineage/rest/v1/projects.locations.config/patch) method with an ingestion rule that sets `lineageEnablement.enabled` to `true` for the specific [`integration`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/data-lineage/rest/v1/folders.locations.config#Config.Integration).

To prevent unintentionally overwriting configurations made by other users in read-modify-write scenarios, you can include the `etag` field in the request body. For more information, see Get current configuration.

Before using any of the request data, make the following replacements: 

  * `CLIENT_PROJECT_ID`: The ID of your client project used for billing or quotas.
  * `PROJECT_ID`: The ID of the project whose configuration you want to update.
  * `ETAG`: The `etag` value returned from a recent `get` request.
  * `INTEGRATION`: The `integration` you set the configuration for. For example, `DATAPROC`.



HTTP method and URL: 
    
    
    PATCH https://datalineage.googleapis.com/v1/projects/PROJECT_ID/locations/global/config

Request JSON body: 
    
    
    {
      "ingestion": {
        "rules": [
          {
            "integrationSelector": {
              "integration": "INTEGRATION"
            },
            "lineageEnablement": {
              "enabled": true
            }
          }
        ]
      },
      "etag": "ETAG"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: CLIENT_PROJECT_ID" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://datalineage.googleapis.com/v1/projects/PROJECT_ID/locations/global/config"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "CLIENT_PROJECT_ID" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://datalineage.googleapis.com/v1/projects/PROJECT_ID/locations/global/config" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/global/config",
      "ingestion": {
        "rules": [
          {
            "integrationSelector": {
              "integration": "INTEGRATION"
            },
            "lineageEnablement": {
              "enabled": true
            }
          }
        ]
      },
      "etag": "1a2b3c4d5e"
    }
    

To enable lineage ingestion of a service for a folder or organization, replace `projects/`PROJECT_ID`` with `folders/`FOLDER_ID`` or `organizations/`ORGANIZATION_ID``.

## Configure lineage ingestion for several services

To configure lineage ingestion for several integrations simultaneously, use the `projects.locations.config.patch`, `folders.locations.config.patch`, or `organizations.locations.config.patch` methods. You can update the configuration at the project, folder, or organization level by defining multiple rules in the request body. For more information, see [How data ingestion configuration works for multi-service integrations](https://docs.cloud.google.com/knowledge-catalog/docs/control-lineage-ingestion#multi-service-integrations).

### Organization level

Configure the organization to **Enable** lineage ingestion for Managed Service for Apache Spark:
    
    
    curl -X PATCH \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json; charset=utf-8" \
      -H "X-Goog-User-Project: CLIENT_PROJECT_ID" \
      "https://datalineage.googleapis.com/v1/organizations/ORGANIZATION_ID/locations/global/config" \
      -d '{
        "ingestion": {
          "rules": [
            {
              "integrationSelector": {
                "integration": "DATAPROC"
              },
              "lineageEnablement": {
                "enabled": true
              }
            }
          ]
        },
        "etag": "ORGANIZATION_CONFIG_ETAG"
      }'
    

Replace the following:

  * `ORGANIZATION_ID`: The ID of the organization whose configuration you want to update.
  * `CLIENT_PROJECT_ID`: The ID of your client project used for billing or quotas.
  * `ORGANIZATION_CONFIG_ETAG`: The `etag` value returned from a recent `get` request for the organization configuration.



### Folder level

Configure the folder to **Enable** lineage ingestion for BigQuery:
    
    
    curl -X PATCH \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json; charset=utf-8" \
      -H "X-Goog-User-Project: CLIENT_PROJECT_ID" \
      "https://datalineage.googleapis.com/v1/folders/FOLDER_ID/locations/global/config" \
      -d '{
        "ingestion": {
          "rules": [
            {
              "integrationSelector": {
                "integration": "BIGQUERY"
              },
              "lineageEnablement": {
                "enabled": true
              }
            }
          ]
        },
        "etag": "FOLDER_CONFIG_ETAG"
      }'
    

Replace the following:

  * `FOLDER_ID`: The ID of the folder whose configuration you want to update.
  * `CLIENT_PROJECT_ID`: The ID of your client project used for billing or quotas.
  * `FOLDER_CONFIG_ETAG`: The `etag` value returned from a recent `get` request for the folder's configuration.



### Project level

Configure the project to **Disable** lineage ingestion for BigQuery and **Enable** lineage ingestion for Managed Service for Apache Airflow simultaneously:
    
    
    curl -X PATCH \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json; charset=utf-8" \
      -H "X-Goog-User-Project: CLIENT_PROJECT_ID" \
      "https://datalineage.googleapis.com/v1/projects/PROJECT_ID/locations/global/config" \
      -d '{
        "ingestion": {
          "rules": [
            {
              "integrationSelector": {
                "integration": "BIGQUERY"
              },
              "lineageEnablement": {
                "enabled": false
              }
            },
            {
              "integrationSelector": {
                "integration": "MANAGED_AIRFLOW"
              },
              "lineageEnablement": {
                "enabled": true
              }
            }
          ]
        },
        "etag": "PROJECT_CONFIG_ETAG"
      }'
    

Replace the following:

  * `PROJECT_ID`: The ID of the project whose configuration you want to update.
  * `CLIENT_PROJECT_ID`: The ID of your client project used for billing or quotas.
  * `PROJECT_CONFIG_ETAG`: The `etag` value returned from a recent `get` request for the project's configuration.



## What's next

  * Learn about [controlling data lineage ingestion](https://docs.cloud.google.com/knowledge-catalog/docs/control-lineage-ingestion).
  * Learn how to [view lineage information](https://docs.cloud.google.com/knowledge-catalog/docs/use-lineage).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
