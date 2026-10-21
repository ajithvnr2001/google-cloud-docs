---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/samples/dlp-create-stored-infotype/
title: Create a stored infoType \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:41:00.224942+00:00
---

# Create a stored infoType  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/samples/dlp-create-stored-infotype/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Samples ](https://docs.cloud.google.com/sensitive-data-protection/docs/samples)



#  Create a stored infoType Stay organized with collections  Save and categorize content based on your preferences. 

This sample creates a stored infoType.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create a large custom dictionary detector](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-stored-infotypes)



## Code sample

### C#

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using System;
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Dlp.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.html);
    
    public class CreateStoredInfoTypes
    {
        public static StoredInfoType Create(
            string projectId,
            string outputPath,
            string storedInfoTypeId)
        {
            // Instantiate the dlp client.
            var dlp = [DlpServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html#Google_Cloud_Dlp_V2_DlpServiceClient_Create)();
    
            // Construct the stored infotype config by specifying the public table and 
            // cloud storage output path.
            var storedInfoTypeConfig = new [StoredInfoTypeConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.StoredInfoTypeConfig.html)
            {
                DisplayName = "Github Usernames",
                Description = "Dictionary of Github usernames used in commits.",
                LargeCustomDictionary = new [LargeCustomDictionaryConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.LargeCustomDictionaryConfig.html)
                {
                    BigQueryField = new [BigQueryField](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.BigQueryField.html)
                    {
                        Table = new [BigQueryTable](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.BigQueryTable.html)
                        {
                            DatasetId = "samples",
                            ProjectId = "bigquery-public-data",
                            TableId = "github_nested"
                        },
                        Field = new [FieldId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FieldId.html)
                        {
                            Name = "actor"
                        }
                    },
                    OutputPath = new [CloudStoragePath](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CloudStoragePath.html)
                    {
                        Path = outputPath
                    }
                },
            };
    
            // Construct the request.
            var request = new [CreateStoredInfoTypeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CreateStoredInfoTypeRequest.html)
            {
                ParentAsLocationName = new [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)(projectId, "global"),
                Config = storedInfoTypeConfig,
                StoredInfoTypeId = storedInfoTypeId
            };
    
            // Call the API.
            [StoredInfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.StoredInfoType.html) response = dlp.CreateStoredInfoType(request);
    
            // Inspect the response.
            Console.WriteLine($"Created the stored infotype at path: {response.[Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.StoredInfoType.html#Google_Cloud_Dlp_V2_StoredInfoType_Name)}");
    
            return response;
        }
    }
    

### Go

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	dlp "cloud.google.com/go/dlp/apiv2"
    	"cloud.google.com/go/dlp/apiv2/dlppb"
    )
    
    // createStoredInfoType creates a custom stored info type based on your input data.
    func createStoredInfoType(w io.Writer, projectID, outputPath string) error {
    	// projectId := "my-project-id"
    	// outputPath := "gs://" + "your-bucket-name" + "path/to/directory"
    
    	ctx := context.Background()
    
    	// Initialize a client once and reuse it to send multiple requests. Clients
    	// are safe to use across goroutines. When the client is no longer needed,
    	// call the Close method to cleanup its resources.
    	client, err := dlp.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2.html#cloud_google_com_go_dlp_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		return err
    	}
    
    	// Closing the client safely cleans up background resources.
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2.html#cloud_google_com_go_dlp_apiv2_Client_Close)()
    
    	// Specify the name you want to give the dictionary.
    	displayName := "Github Usernames"
    
    	// Specify a description of the dictionary.
    	description := "Dictionary of GitHub usernames used in commits"
    
    	// Specify the path to the location in a Cloud Storage
    	// bucket to store the created dictionary.
    	cloudStoragePath := &dlppb.CloudStoragePath{
    		Path: outputPath,
    	}
    
    	// Specify your term list is stored in BigQuery.
    	bigQueryField := &dlppb.BigQueryField{
    		Table: &dlppb.BigQueryTable{
    			ProjectId: "bigquery-public-data",
    			DatasetId: "samples",
    			TableId:   "github_nested",
    		},
    		Field: &dlppb.FieldId{
    			Name: "actor",
    		},
    	}
    
    	// Specify the configuration of the large custom dictionary.
    	largeCustomDictionaryConfig := &dlppb.LargeCustomDictionaryConfig{
    		OutputPath: cloudStoragePath,
    		Source: &dlppb.LargeCustomDictionaryConfig_BigQueryField{
    			BigQueryField: bigQueryField,
    		},
    	}
    
    	// Specify the configuration for stored infoType.
    	storedInfoTypeConfig := &dlppb.StoredInfoTypeConfig{
    		DisplayName: displayName,
    		Description: description,
    		Type: &dlppb.StoredInfoTypeConfig_LargeCustomDictionary{
    			LargeCustomDictionary: largeCustomDictionaryConfig,
    		},
    	}
    
    	// Combine configurations into a request for the service.
    	req := &dlppb.CreateStoredInfoTypeRequest{
    		Parent:           fmt.Sprintf("projects/%s/locations/global", projectID),
    		Config:           storedInfoTypeConfig,
    		StoredInfoTypeId: "github-usernames",
    	}
    
    	// Send the request and receive response from the service.
    	resp, err := client.CreateStoredInfoType(ctx, req)
    	if err != nil {
    		return err
    	}
    
    	// Print the result.
    	fmt.Fprintf(w, "output: %v", resp.Name)
    	return nil
    
    }
    

### Java

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.dlp.v2.[DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html);
    import com.google.privacy.dlp.v2.[BigQueryField](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.BigQueryField.html);
    import com.google.privacy.dlp.v2.[BigQueryTable](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.BigQueryTable.html);
    import com.google.privacy.dlp.v2.[CloudStoragePath](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CloudStoragePath.html);
    import com.google.privacy.dlp.v2.[CreateStoredInfoTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CreateStoredInfoTypeRequest.html);
    import com.google.privacy.dlp.v2.[FieldId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldId.html);
    import com.google.privacy.dlp.v2.[LargeCustomDictionaryConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LargeCustomDictionaryConfig.html);
    import com.google.privacy.dlp.v2.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html);
    import com.google.privacy.dlp.v2.[StoredInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.StoredInfoType.html);
    import com.google.privacy.dlp.v2.[StoredInfoTypeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.StoredInfoTypeConfig.html);
    import java.io.IOException;
    
    public class CreateStoredInfoType {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
    
        //The Google Cloud project id to use as a parent resource.
        String projectId = "your-project-id";
        // The path to the location in a GCS bucket to store the created dictionary.
        String outputPath = "gs://" + "your-bucket-name" + "path/to/directory";
        createStoredInfoType(projectId, outputPath);
      }
    
      // Creates a custom stored info type that contains GitHub usernames used in commits.
      public static void createStoredInfoType(String projectId, String outputPath)
          throws IOException {
        try ([DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html) dlp = [DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html).create()) {
    
          // Optionally set a display name and a description.
          String displayName = "GitHub usernames";
          String description = "Dictionary of GitHub usernames used in commits";
    
          // The output path where the custom dictionary containing the GitHub usernames will be stored.
          [CloudStoragePath](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CloudStoragePath.html) cloudStoragePath =
              [CloudStoragePath](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CloudStoragePath.html).newBuilder()
                  .setPath(outputPath)
                  .build();
    
          // The reference to the table containing the GitHub usernames.
          [BigQueryTable](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.BigQueryTable.html) table = [BigQueryTable](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.BigQueryTable.html).newBuilder()
                  .setProjectId("bigquery-public-data")
                  .setDatasetId("samples")
                  .setTableId("github_nested")
                  .build();
    
          // The reference to the BigQuery field that contains the GitHub usernames.
          [BigQueryField](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.BigQueryField.html) bigQueryField = [BigQueryField](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.BigQueryField.html).newBuilder()
                  .setTable(table)
                  .setField([FieldId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldId.html).newBuilder().setName("actor").build())
                  .build();
    
          [LargeCustomDictionaryConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LargeCustomDictionaryConfig.html) largeCustomDictionaryConfig =
              [LargeCustomDictionaryConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LargeCustomDictionaryConfig.html).newBuilder()
                  .[setOutputPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LargeCustomDictionaryConfig.Builder.html#com_google_privacy_dlp_v2_LargeCustomDictionaryConfig_Builder_setOutputPath_com_google_privacy_dlp_v2_CloudStoragePath_)(cloudStoragePath)
                  .[setBigQueryField](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LargeCustomDictionaryConfig.Builder.html#com_google_privacy_dlp_v2_LargeCustomDictionaryConfig_Builder_setBigQueryField_com_google_privacy_dlp_v2_BigQueryField_)(bigQueryField)
                  .build();
    
          [StoredInfoTypeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.StoredInfoTypeConfig.html) storedInfoTypeConfig = [StoredInfoTypeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.StoredInfoTypeConfig.html).newBuilder()
                  .setDisplayName(displayName)
                  .setDescription(description)
                  .setLargeCustomDictionary(largeCustomDictionaryConfig)
                  .build();
    
          // Combine configurations into a request for the service.
          [CreateStoredInfoTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CreateStoredInfoTypeRequest.html) createStoredInfoType = [CreateStoredInfoTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CreateStoredInfoTypeRequest.html).newBuilder()
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html).of(projectId, "global").toString())
                  .setConfig(storedInfoTypeConfig)
                  .[setStoredInfoTypeId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CreateStoredInfoTypeRequest.Builder.html#com_google_privacy_dlp_v2_CreateStoredInfoTypeRequest_Builder_setStoredInfoTypeId_java_lang_String_)("github-usernames")
                  .build();
    
          // Send the request and receive response from the service.
          [StoredInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.StoredInfoType.html) response = dlp.createStoredInfoType(createStoredInfoType);
    
          // Print the results.
          System.out.println("Created Stored InfoType: " + response.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.StoredInfoType.html#com_google_privacy_dlp_v2_StoredInfoType_getName__)());
        }
      }
    }
    

### Node.js

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Import the required libraries
    const dlp = require('[@google-cloud/dlp](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/overview.html)');
    
    // Create a DLP client
    const dlpClient = new dlp.[DlpServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/overview.html)();
    
    // The project ID to run the API call under.
    // const projectId = "your-project-id";
    
    // The identifier for the stored infoType
    // const infoTypeId = 'github-usernames';
    
    // The path to the location in a Cloud Storage bucket to store the created dictionary
    // const outputPath = 'cloud-bucket-path';
    
    // The project ID the table is stored under
    // This may or (for public datasets) may not equal the calling project ID
    // const dataProjectId = 'my-project';
    
    // The ID of the dataset to inspect, e.g. 'my_dataset'
    // const datasetId = 'my_dataset';
    
    // The ID of the table to inspect, e.g. 'my_table'
    // const tableId = 'my_table';
    
    // Field ID to be used for constructing dictionary
    // const fieldName = 'field_name';
    
    async function createStoredInfoType() {
      // The name you want to give the dictionary.
      const displayName = 'GitHub usernames';
      // A description of the dictionary.
      const description = 'Dictionary of GitHub usernames used in commits';
    
      // Specify configuration for the large custom dictionary
      const largeCustomDictionaryConfig = {
        outputPath: {
          path: outputPath,
        },
        bigQueryField: {
          table: {
            datasetId: datasetId,
            projectId: dataProjectId,
            tableId: tableId,
          },
          field: {
            name: fieldName,
          },
        },
      };
    
      // Stored infoType configuration that uses large custom dictionary.
      const storedInfoTypeConfig = {
        displayName: displayName,
        description: description,
        largeCustomDictionary: largeCustomDictionaryConfig,
      };
    
      // Construct the job creation request to be sent by the client.
      const request = {
        parent: `projects/${projectId}/locations/global`,
        config: storedInfoTypeConfig,
        storedInfoTypeId: infoTypeId,
      };
    
      // Send the job creation request and process the response.
      const [response] = await dlpClient.createStoredInfoType(request);
    
      // Print results
      console.log(`InfoType stored successfully: ${response.name}`);
    }
    await createStoredInfoType();

### PHP

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Dlp\V2\BigQueryField;
    use Google\Cloud\Dlp\V2\BigQueryTable;
    use Google\Cloud\Dlp\V2\Client\DlpServiceClient;
    use Google\Cloud\Dlp\V2\CloudStoragePath;
    use Google\Cloud\Dlp\V2\CreateStoredInfoTypeRequest;
    use Google\Cloud\Dlp\V2\FieldId;
    use Google\Cloud\Dlp\V2\LargeCustomDictionaryConfig;
    use Google\Cloud\Dlp\V2\StoredInfoTypeConfig;
    
    /**
     * Create a stored infoType.
     *
     * @param string $callingProjectId  The Google Cloud Project ID to run the API call under.
     * @param string $outputgcsPath     The path to the location in a Cloud Storage bucket to store the created dictionary.
     * @param string $storedInfoTypeId  The name of the custom stored info type.
     * @param string $displayName       The human-readable name to give the stored infoType.
     * @param string $description       A description for the stored infoType to be created.
     */
    function create_stored_infotype(
        string $callingProjectId,
        string $outputgcsPath,
        string $storedInfoTypeId,
        string $displayName,
        string $description
    ): void {
        // Instantiate a client.
        $dlp = new DlpServiceClient();
    
        // The reference to the table containing the GitHub usernames.
        // The reference to the BigQuery field that contains the GitHub usernames.
        // Note: we have used public data
        $bigQueryField = (new BigQueryField())
            ->setTable((new BigQueryTable())
                ->setDatasetId('samples')
                ->setProjectId('bigquery-public-data')
                ->setTableId('github_nested'))
            ->setField((new FieldId())
                ->setName('actor'));
    
        $largeCustomDictionaryConfig = (new LargeCustomDictionaryConfig())
            // The output path where the custom dictionary containing the GitHub usernames will be stored.
            ->setOutputPath((new CloudStoragePath())
                ->setPath($outputgcsPath))
            ->setBigQueryField($bigQueryField);
    
        // Configure the StoredInfoType we want the service to perform.
        $storedInfoTypeConfig = (new StoredInfoTypeConfig())
            ->setDisplayName($displayName)
            ->setDescription($description)
            ->setLargeCustomDictionary($largeCustomDictionaryConfig);
    
        // Send the stored infoType creation request and process the response.
        $parent = "projects/$callingProjectId/locations/global";
        $createStoredInfoTypeRequest = (new CreateStoredInfoTypeRequest())
            ->setParent($parent)
            ->setConfig($storedInfoTypeConfig)
            ->setStoredInfoTypeId($storedInfoTypeId);
        $response = $dlp->createStoredInfoType($createStoredInfoTypeRequest);
    
        // Print results.
        printf('Successfully created Stored InfoType : %s', $response->getName());
    }

### Python

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import google.cloud.dlp
    
    
    def create_stored_infotype(
        project: str,
        stored_info_type_id: str,
        output_bucket_name: str,
    ) -> None:
        """Uses the Data Loss Prevention API to create stored infoType.
        Args:
            project: The Google Cloud project id to use as a parent resource.
            stored_info_type_id: The identifier for large custom dictionary.
            output_bucket_name: The name of the bucket in Google Cloud Storage
                that would store the created dictionary.
        """
    
        # Instantiate a client.
        dlp = google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html)()
    
        # Construct the stored infoType Configuration dictionary. This example creates
        # a stored infoType from a term list stored in a publicly available BigQuery
        # database (bigquery-public-data.samples.github_nested).
        # The database contains all GitHub usernames used in commits.
        stored_info_type_config = {
            "display_name": "GitHub usernames",
            "description": "Dictionary of GitHub usernames used in commits",
            "large_custom_dictionary": {
                "output_path": {"path": f"gs://{output_bucket_name}"},
                # We can either use bigquery field or gcs file as a term list input option.
                "big_query_field": {
                    "table": {
                        "project_id": "bigquery-public-data",
                        "dataset_id": "samples",
                        "table_id": "github_nested",
                    },
                    "field": {"name": "actor"},
                },
            },
        }
    
        # Convert the project id into a full resource id.
        parent = f"projects/{project}/locations/global"
    
        # Call the API.
        response = dlp.[create_stored_info_type](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceClient_create_stored_info_type)(
            request={
                "parent": parent,
                "config": stored_info_type_config,
                "stored_info_type_id": stored_info_type_id,
            }
        )
    
        # Print the result
        print(f"Created Stored InfoType: {response.name}")
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=clouddatalossprevention). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
