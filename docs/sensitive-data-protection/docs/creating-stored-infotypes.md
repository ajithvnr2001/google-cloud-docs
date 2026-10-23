---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/creating-stored-infotypes/
title: Create a large custom dictionary detector \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:09:28.072882+00:00
---

# Create a large custom dictionary detector  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/creating-stored-infotypes/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Guides ](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview)



Send feedback 

#  Create a large custom dictionary detector Stay organized with collections  Save and categorize content based on your preferences. 

This topic describes how to create and rebuild large custom dictionaries. It also covers several error scenarios.

## When to choose a large custom dictionary over a regular custom dictionary

[Regular custom dictionary detectors](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes-dictionary) are sufficient when you have tens of thousands of sensitive words or phrases that you want to scan your content for. If you have more or if your term list changes frequently, consider creating a _large custom dictionary_ , which can support tens of millions of terms.

**Note:** For the exact usage limit amounts for dictionaries, see [Usage limits](https://docs.cloud.google.com/sensitive-data-protection/limits).

## How large custom dictionaries differ from other custom infoTypes

Large custom dictionaries are different from other custom infoTypes in that each large custom dictionary has two components:

  * A list of phrases that you create and define. The list is stored as either a text file within Cloud Storage or a column in a BigQuery table.
  * The dictionary files, which Sensitive Data Protection generates and stores in Cloud Storage. Dictionary files are composed of a copy of your term list plus bloom filters, which aid in searching and matching.

**Warning:** Do not alter custom dictionary files directly in Cloud Storage. Doing so will render the dictionary invalid and unusable.

## Create a large custom dictionary

This section describes how to create, edit, and rebuild a large custom dictionary.

### Create a term list

Create a list that contains all the words and phrases that you want the new infoType detector to search for. Do one of the following:

  * Place a text file with each word or phrase on its own line into a Cloud Storage bucket.
  * Designate one column of a BigQuery table as the container for the words and phrases. Give each entry its own row in the column. You can use an existing BigQuery table, as long as all dictionary words and phrases are in a single column.



It's possible to assemble a term list that is too large for Sensitive Data Protection to process. If you see an error message, see Troubleshooting errors later in this topic.

### Create a stored infoType

After you create your term list, use Sensitive Data Protection to create a dictionary:

### Console

  1. In a Cloud Storage bucket, create a new folder where Sensitive Data Protection will store the generated dictionary.

Sensitive Data Protection creates folders containing the dictionary files at the location that you specify.

  2. In the Google Cloud console, go to the **Create infoType** page.

[Go to Create infoType](https://console.cloud.google.com/security/sensitive-data-protection/create/storedInfoType)

  3. For **Type** , select **Large custom dictionary**.

  4. For **InfoType ID** , enter an identifier for the stored infoType.

You will use this identifier when configuring your inspection and de-identification jobs. You can use letters, numbers, hyphens, and underscores in the name.

  5. For **InfoType display name** , enter a name for your stored infoType.

You can use spaces and punctuation in the name.

  6. For **Description** , enter a description of what your stored infoType detects.

  7. For **Storage type** , select the location of your term list:

     * **BigQuery** : Enter the project ID, dataset ID, and table ID. In the **Field name** field, enter the column identifier. You can designate at most one column from the table.
     * **Google Cloud Storage** : Enter the path to the file.
  8. For **Output bucket or folder** , enter the Cloud Storage location of the folder that you created in step 1.

**Note:** Do not place files inside the folders that Sensitive Data Protection creates when it builds your dictionary. When Sensitive Data Protection creates or rebuilds dictionary files, it deletes any other files stored in folders that it creates. Any folders at the same level as the folders that Sensitive Data Protection creates are maintained.

  9. Click **Create**.




A summary of the stored infoType appears. When the dictionary is generated and the new stored infoType is ready to use, the status of the infoType shows **Ready**.

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
    
    

### REST

  1. Create a new folder for the dictionary in a Cloud Storage bucket. Sensitive Data Protection creates folders containing the dictionary files at the location that you specify.
**Note:** Do not place files inside the folders that Sensitive Data Protection creates when it builds your dictionary. Sensitive Data Protection will, when it creates or rebuilds dictionary files, delete any other files stored in folders that it creates. Any folders at the same level as the folders that Sensitive Data Protection creates will be maintained.
  2. Create the dictionary using the [`storedInfoTypes.create`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.storedInfoTypes/create) method. The `create` method takes the following parameters: 
     * A [`StoredInfoTypeConfig`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.storedInfoTypes#storedinfotypeconfig) object, which contains the configuration of the stored infoType. It includes: 
       * `description`: A description of the dictionary.
       * `displayName`: The name you want to give the dictionary.
       * [`LargeCustomDictionaryConfig`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.storedInfoTypes#largecustomdictionaryconfig): Contains the configuration of the large custom dictionary. It includes: 
         * [`BigQueryField`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.storedInfoTypes#bigqueryfield): Specified if your term list is stored in BigQuery. Includes a reference to the table that your list is stored in, plus the field that contains each dictionary phrase.
         * [`CloudStorageFileSet`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.storedInfoTypes#cloudstoragefileset): Specified if your term list is stored in Cloud Storage. Includes the URL to the source location in Cloud Storage, in the following form: `"gs://[PATH_TO_GS]"`. Wildcards are supported.
**Note:** You can specify either `BigQueryField` or `CloudStorageFileSet` in `LargeCustomDictionaryConfig`, but not both.
         * `outputPath`: The path to the location in a Cloud Storage bucket to store the created dictionary.
     * `storedInfoTypeId`: The identifier for the stored infoType. You use this identifier to refer to the stored infoType when you rebuild it, delete it, or use it in an inspection or de-identification job. If you leave this field empty, the system generates an identifier for you.



Following is example JSON that, when sent to the `storedInfoTypes.create` method, creates a new stored infoType—specifically, a large custom dictionary detector. This example creates a stored infoType from a term list stored in a publicly available BigQuery database (`bigquery-public-data.samples.github_nested`). The database contains all GitHub usernames used in commits. The output path for the generated dictionary is set to a Cloud Storage bucket called `dlptesting`, and the stored infoType is named `github-usernames`.

**JSON input**
    
    
    POST https://dlp.googleapis.com/v2/projects/PROJECT_ID/storedInfoTypes
    
    {
      "config":{
        "displayName":"GitHub usernames",
        "description":"Dictionary of GitHub usernames used in commits",
        "largeCustomDictionary":{
          "outputPath":{
            "path":"gs://[PATH_TO_GS]"
          },
          "bigQueryField":{
            "table":{
              "datasetId":"samples",
              "projectId":"bigquery-public-data",
              "tableId":"github_nested"
            }
          }
        }
      },
      "storedInfoTypeId":"github-usernames"
    }
    

## Rebuild the dictionary

If you want to update your dictionary, you first update your source term list, and then you instruct Sensitive Data Protection to rebuild the stored infoType.

  1. Update the existing source term list in either Cloud Storage or BigQuery.

Add, remove, or change the terms or phrases as needed.

  2. Create a new version of the stored infoType by "rebuilding" it using either the Google Cloud console or the [`storedInfoTypes.patch`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.storedInfoTypes/patch) method.

Rebuilding creates a new version of the dictionary, which replaces the old dictionary.




When you rebuild a stored infoType to a new version, the old version is deleted. While Sensitive Data Protection is updating the stored infoType, its status is "pending." During this time, the old version of the stored infoType still exists. Any scans that you run while the stored infoType is in pending state will be run using the old version of the stored infoType.

To rebuild the stored infoType:

### Console

  1. Update and save your term list in either Cloud Storage or BigQuery.
  2. In the Google Cloud console, go to your list of stored infoTypes.

[Go to stored infoTypes](https://console.cloud.google.com/security/sensitive-data-protection;source=7/landing/configuration/infoTypes/stored)

  3. Click the ID of the stored infoType that you want to update.

  4. On the **InfoType details** page, click **Rebuild data**.




Sensitive Data Protection rebuilds the stored infoType with the changes you made to the source term list. Once the status of the stored infoType is "Ready," you can use it. Any templates or job triggers that use the stored infoType will automatically use the rebuilt version.

### C#

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using System;
    using [Google.Cloud.Dlp.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.html);
    using [Google.Protobuf.WellKnownTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.html);
    
    public class UpdateStoredInfoTypes
    {
        public static StoredInfoType Update(
            string gcsFileUri,
            string storedInfoTypePath,
            string outputPath)
        {
            // Instantiate the client.
            var dlp = [DlpServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html#Google_Cloud_Dlp_V2_DlpServiceClient_Create)();
    
            // Construct the stored infotype config. Here, we will change the source from bigquery table to GCS file.
            var storedConfig = new [StoredInfoTypeConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.StoredInfoTypeConfig.html)
            {
                LargeCustomDictionary = new [LargeCustomDictionaryConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.LargeCustomDictionaryConfig.html)
                {
                    CloudStorageFileSet = new [CloudStorageFileSet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CloudStorageFileSet.html)
                    {
                        Url = gcsFileUri
                    },
                    OutputPath = new [CloudStoragePath](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CloudStoragePath.html)
                    {
                        Path = outputPath
                    }
                }
            };
    
            // Construct the request using the stored config by specifying the update mask object
            // which represent the path of field to be updated.
            var request = new [UpdateStoredInfoTypeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.UpdateStoredInfoTypeRequest.html)
            {
                Config = storedConfig,
                Name = storedInfoTypePath,
                UpdateMask = new [FieldMask](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)
                {
                    Paths =
                    {
                        "large_custom_dictionary.cloud_storage_file_set.url"
                    }
                }
            };
    
            // Call the API.
            [StoredInfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.StoredInfoType.html) response = dlp.UpdateStoredInfoType(request);
    
            // Inspect the result.
            Console.WriteLine(response);
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
    	"google.golang.org/protobuf/types/known/fieldmaskpb"
    )
    
    // updateStoredInfoType uses the Data Loss Prevention API to update stored infoType
    // detector by changing the source term list from one stored in Bigquery
    // to one stored in Cloud Storage.
    func updateStoredInfoType(w io.Writer, projectID, gcsUri, fileSetUrl, infoTypeId string) error {
    	// projectId := "your-project-id"
    	// gcsUri := "gs://" + "your-bucket-name" + "/path/to/your/file.txt"
    	// fileSetUrl := "your-cloud-storage-file-set"
    	// infoTypeId := "your-stored-info-type-id"
    
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
    
    	// Set path in Cloud Storage.
    	cloudStoragePath := &dlppb.CloudStoragePath{
    		Path: gcsUri,
    	}
    	cloudStorageFileSet := &dlppb.CloudStorageFileSet{
    		Url: fileSetUrl,
    	}
    
    	// Configuration for a custom dictionary created from a data source of any size
    	largeCustomDictionaryConfig := &dlppb.LargeCustomDictionaryConfig{
    		OutputPath: cloudStoragePath,
    		Source: &dlppb.LargeCustomDictionaryConfig_CloudStorageFileSet{
    			CloudStorageFileSet: cloudStorageFileSet,
    		},
    	}
    
    	// Set configuration for stored infoTypes.
    	storedInfoTypeConfig := &dlppb.StoredInfoTypeConfig{
    		Type: &dlppb.StoredInfoTypeConfig_LargeCustomDictionary{
    			LargeCustomDictionary: largeCustomDictionaryConfig,
    		},
    	}
    
    	// Set mask to control which fields get updated.
    	fieldMask := &fieldmaskpb.FieldMask{
    		Paths: []string{"large_custom_dictionary.cloud_storage_file_set.url"},
    	}
    	// Construct the job creation request to be sent by the client.
    	req := &dlppb.UpdateStoredInfoTypeRequest{
    		Name:       fmt.Sprint("projects/" + projectID + "/storedInfoTypes/" + infoTypeId),
    		Config:     storedInfoTypeConfig,
    		UpdateMask: fieldMask,
    	}
    
    	// Use the client to send the API request.
    	resp, err := client.UpdateStoredInfoType(ctx, req)
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
    import com.google.privacy.dlp.v2.[CloudStorageFileSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CloudStorageFileSet.html);
    import com.google.privacy.dlp.v2.[CloudStoragePath](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CloudStoragePath.html);
    import com.google.privacy.dlp.v2.[LargeCustomDictionaryConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LargeCustomDictionaryConfig.html);
    import com.google.privacy.dlp.v2.[StoredInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.StoredInfoType.html);
    import com.google.privacy.dlp.v2.[StoredInfoTypeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.StoredInfoTypeConfig.html);
    import com.google.privacy.dlp.v2.[StoredInfoTypeName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.StoredInfoTypeName.html);
    import com.google.privacy.dlp.v2.[UpdateStoredInfoTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.UpdateStoredInfoTypeRequest.html);
    import com.google.protobuf.[FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html);
    import java.io.IOException;
    
    public class UpdateStoredInfoType {
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        // The Google Cloud project id to use as a parent resource.
        String projectId = "your-project-id";
        // The path to file in GCS bucket that holds a collection of words and phrases to be searched by
        // the new infoType detector.
        String filePath = "gs://" + "your-bucket-name" + "/path/to/your/file.txt";
        // The path to the location in a GCS bucket to store the created dictionary.
        String outputPath = "your-cloud-storage-file-set";
        // The name of the stored InfoType which is to be updated.
        String infoTypeId = "your-stored-info-type-id";
        updateStoredInfoType(projectId, filePath, outputPath, infoTypeId);
      }
    
      // Update the stored info type rebuilding the Custom dictionary.
      public static void updateStoredInfoType(
          String projectId, String filePath, String outputPath, String infoTypeId) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html) dlp = [DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html).create()) {
          // Set path in Cloud Storage.
          [CloudStoragePath](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CloudStoragePath.html) cloudStoragePath = [CloudStoragePath](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CloudStoragePath.html).newBuilder().setPath(outputPath).build();
          [CloudStorageFileSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CloudStorageFileSet.html) cloudStorageFileSet =
              [CloudStorageFileSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CloudStorageFileSet.html).newBuilder().setUrl(filePath).build();
    
          // Configuration for a custom dictionary created from a data source of any size
          [LargeCustomDictionaryConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LargeCustomDictionaryConfig.html) largeCustomDictionaryConfig =
              [LargeCustomDictionaryConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LargeCustomDictionaryConfig.html).newBuilder()
                  .[setOutputPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LargeCustomDictionaryConfig.Builder.html#com_google_privacy_dlp_v2_LargeCustomDictionaryConfig_Builder_setOutputPath_com_google_privacy_dlp_v2_CloudStoragePath_)(cloudStoragePath)
                  .[setCloudStorageFileSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LargeCustomDictionaryConfig.Builder.html#com_google_privacy_dlp_v2_LargeCustomDictionaryConfig_Builder_setCloudStorageFileSet_com_google_privacy_dlp_v2_CloudStorageFileSet_)(cloudStorageFileSet)
                  .build();
    
          // Set configuration for stored infoTypes.
          [StoredInfoTypeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.StoredInfoTypeConfig.html) storedInfoTypeConfig =
              [StoredInfoTypeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.StoredInfoTypeConfig.html).newBuilder()
                  .setLargeCustomDictionary(largeCustomDictionaryConfig)
                  .build();
    
          // Set mask to control which fields get updated.
          // Refer https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask for constructing the field mask paths.
          [FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html) fieldMask =
              [FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html).newBuilder()
                  .[addPaths](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.Builder.html#com_google_protobuf_FieldMask_Builder_addPaths_java_lang_String_)("large_custom_dictionary.cloud_storage_file_set.url")
                  .build();
    
          // Construct the job creation request to be sent by the client.
          [UpdateStoredInfoTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.UpdateStoredInfoTypeRequest.html) updateStoredInfoTypeRequest =
              [UpdateStoredInfoTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.UpdateStoredInfoTypeRequest.html).newBuilder()
                  .setName(
                      [StoredInfoTypeName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.StoredInfoTypeName.html).[ofProjectStoredInfoTypeName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.StoredInfoTypeName.html#com_google_privacy_dlp_v2_StoredInfoTypeName_ofProjectStoredInfoTypeName_java_lang_String_java_lang_String_)(projectId, infoTypeId).toString())
                  .setConfig(storedInfoTypeConfig)
                  .setUpdateMask(fieldMask)
                  .build();
    
          // Send the job creation request and process the response.
          [StoredInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.StoredInfoType.html) response = dlp.updateStoredInfoType(updateStoredInfoTypeRequest);
    
          // Print the results.
          System.out.println("Updated stored InfoType successfully: " + response.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.StoredInfoType.html#com_google_privacy_dlp_v2_StoredInfoType_getName__)());
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
    
    // Path of file containing term list
    // const cloudStorageFileSet = 'gs://[PATH_TO_GS]';
    
    async function updateStoredInfoType() {
      // Specify configuration of the large custom dictionary including cloudStorageFileSet and outputPath
      const largeCustomDictionaryConfig = {
        outputPath: {
          path: outputPath,
        },
        cloudStorageFileSet: {
          url: fileSetUrl,
        },
      };
    
      // Construct the job creation request to be sent by the client.
      const updateStoredInfoTypeRequest = {
        name: `projects/${projectId}/storedInfoTypes/${infoTypeId}`,
        config: {
          largeCustomDictionary: largeCustomDictionaryConfig,
        },
        updateMask: {
          paths: ['large_custom_dictionary.cloud_storage_file_set.url'],
        },
      };
    
      // Send the job creation request and process the response.
      const [response] = await dlpClient.updateStoredInfoType(
        updateStoredInfoTypeRequest
      );
    
      // Print the results.
      console.log(`InfoType updated successfully: ${JSON.stringify(response)}`);
    }
    await updateStoredInfoType();

### PHP

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Dlp\V2\Client\DlpServiceClient;
    use Google\Cloud\Dlp\V2\CloudStorageFileSet;
    use Google\Cloud\Dlp\V2\CloudStoragePath;
    use Google\Cloud\Dlp\V2\LargeCustomDictionaryConfig;
    use Google\Cloud\Dlp\V2\StoredInfoTypeConfig;
    use Google\Cloud\Dlp\V2\UpdateStoredInfoTypeRequest;
    use Google\Protobuf\FieldMask;
    
    /**
     * Rebuild/Update the stored infoType.
     *
     * @param string $callingProjectId  The Google Cloud Project ID to run the API call under.
     * @param string $gcsPath           The path to file in GCS bucket that holds a collection of words and phrases to be searched by the new infoType detector.
     * @param string $outputgcsPath     The path to the location in a Cloud Storage bucket to store the created dictionary.
     * @param string $storedInfoTypeId  The name of the stored InfoType which is to be updated.
     *
     */
    function update_stored_infotype(
        string $callingProjectId,
        string $gcsPath,
        string $outputgcsPath,
        string $storedInfoTypeId
    ): void {
        // Instantiate a client.
        $dlp = new DlpServiceClient();
    
        // Set path in Cloud Storage.
        $cloudStorageFileSet = (new CloudStorageFileSet())
            ->setUrl($gcsPath);
    
        // Configuration for a custom dictionary created from a data source of any size
        $largeCustomDictionaryConfig = (new LargeCustomDictionaryConfig())
            ->setOutputPath((new CloudStoragePath())
                ->setPath($outputgcsPath))
            ->setCloudStorageFileSet($cloudStorageFileSet);
    
        // Set configuration for stored infoTypes.
        $storedInfoTypeConfig = (new StoredInfoTypeConfig())
            ->setLargeCustomDictionary($largeCustomDictionaryConfig);
    
        // Send the stored infoType creation request and process the response.
    
        $name = "projects/$callingProjectId/locations/global/storedInfoTypes/" . $storedInfoTypeId;
        // Set mask to control which fields get updated.
        // Refer https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask for constructing the field mask paths.
        $fieldMask = (new FieldMask())
            ->setPaths([
                'large_custom_dictionary.cloud_storage_file_set.url'
            ]);
    
        // Run request
        $updateStoredInfoTypeRequest = (new UpdateStoredInfoTypeRequest())
            ->setName($name)
            ->setConfig($storedInfoTypeConfig)
            ->setUpdateMask($fieldMask);
        $response = $dlp->updateStoredInfoType($updateStoredInfoTypeRequest);
    
        // Print results
        printf('Successfully update Stored InforType : %s' . PHP_EOL, $response->getName());
    }

### Python

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import google.cloud.dlp
    
    
    def update_stored_infotype(
        project: str,
        stored_info_type_id: str,
        gcs_input_file_path: str,
        output_bucket_name: str,
    ) -> None:
        """Uses the Data Loss Prevention API to update stored infoType
        detector by changing the source term list from one stored in Bigquery
        to one stored in Cloud Storage.
        Args:
            project: The Google Cloud project id to use as a parent resource.
            stored_info_type_id: The identifier of stored infoType which is to
                be updated.
            gcs_input_file_path: The url in the format <bucket>/<path_to_file>
                for the location of the source term list.
            output_bucket_name: The name of the bucket in Google Cloud Storage
                where large dictionary is stored.
        """
    
        # Instantiate a client.
        dlp = google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html)()
    
        # Construct the stored infoType configuration dictionary.
        stored_info_type_config = {
            "large_custom_dictionary": {
                "output_path": {"path": f"gs://{output_bucket_name}"},
                "cloud_storage_file_set": {"url": f"gs://{gcs_input_file_path}"},
            }
        }
    
        # Set mask to control which fields get updated. For more details, refer
        # https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask
        # for constructing the field mask paths.
        field_mask = {"paths": ["large_custom_dictionary.cloud_storage_file_set.url"]}
    
        # Convert the stored infoType id into a full resource id.
        stored_info_type_name = (
            f"projects/{project}/locations/global/storedInfoTypes/{stored_info_type_id}"
        )
    
        # Call the API.
        response = dlp.[update_stored_info_type](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceClient_update_stored_info_type)(
            request={
                "name": stored_info_type_name,
                "config": stored_info_type_config,
                "update_mask": field_mask,
            }
        )
    
        # Print the result
        print(f"Updated stored infoType successfully: {response.name}")
    
    

### REST

### Update the term list

If you're updating only the list of terms in the large custom dictionary, your [`storedInfoTypes.patch`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.storedInfoTypes/patch) request requires only the `name` field. Provide the full resource name of the stored infoType that you want to rebuild.

The following patterns represent valid entries for the `name` field:

  * `organizations/ORGANIZATION_ID/storedInfoTypes/STORED_INFOTYPE_ID`
  * `projects/PROJECT_ID/storedInfoTypes/STORED_INFOTYPE_ID`



Replace STORED_INFOTYPE_ID with the identifier of the stored infoType that you want to rebuild.

If you don't know the identifier of the stored infoType, call the [`storedInfoTypes.list`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.storedInfoTypes/list) method to view a list of all current stored infoTypes.

**Note:** Though stored infoTypes don't have version numbers, each one has a `createTime` field, which is refreshed with each rebuild. Use the [`storedInfoTypes.get`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.storedInfoTypes/get) method to retrieve information about the stored infoType, and use the `createTime` field to determine when it was last rebuilt.

#### Example
    
    
    PATCH https://dlp.googleapis.com/v2/projects/PROJECT_ID/storedInfoTypes/STORED_INFOTYPE_ID
    

In this case, a request body isn't required.

### Switch the source term list

You can change the source term list for a stored infoType from one stored in BigQuery to one stored in Cloud Storage. Use the [`storedInfoTypes.patch`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.storedInfoTypes/patch) method, but include a [`CloudStorageFileSet`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.storedInfoTypes#cloudstoragefileset) object in [`LargeCustomDictionaryConfig`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.storedInfoTypes#largecustomdictionaryconfig) where you'd used a [`BigQueryField`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.storedInfoTypes#bigqueryfield) object before. Then, set the `updateMask` parameter to the stored infoType parameter that you rebuilt, in [`FieldMask`](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.FieldMask) format. For instance, the following JSON states in the `updateMask` parameter that the URL of the Cloud Storage path has been updated ([`large_custom_dictionary.cloud_storage_file_set.url`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.storedInfoTypes#StoredInfoType.CloudStorageFileSet.FIELDS.url)):

#### Example
    
    
    PATCH https://dlp.googleapis.com/v2/projects/PROJECT_ID/storedInfoTypes/github-usernames
    
    {
      "config":{
        "largeCustomDictionary":{
          "cloudStorageFileSet":{
            "url":"gs://[BUCKET_NAME]/[PATH_TO_FILE]"
          }
        }
      },
      "updateMask":"large_custom_dictionary.cloud_storage_file_set.url"
    }
    

Similarly, you can switch your term list from one stored in a BigQuery table to one stored in a Cloud Storage bucket.

## Scan content using a large custom dictionary detector

Scanning content using a large custom dictionary detector is similar to scanning content using any other custom infoType detector.

This procedure assumes that you have an existing stored infoType. For more information, see Create a stored infoType on this page.

### Console

You can apply a large custom dictionary detector when doing the following:

  * Creating a new [job](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-job-triggers#create_a_new_inspection_job)
  * Creating or editing a [job trigger](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-job-triggers#create_a_new_job_trigger)
  * Creating or editing a [template](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-templates-inspect)
  * Configuring [data profiling](https://docs.cloud.google.com/sensitive-data-protection/docs/profile-org-folder)



In the **Configure detection** section of the page, in the **InfoTypes** subsection, you can specify your large custom dictionary infoType.

  1. Click **Manage infoTypes**.
  2. In the **InfoTypes** pane, click the **Custom** tab.
  3. Click **Add custom infoType**.
  4. In the **Add custom infoType** pane, do the following:

     1. For **Type** , select **Stored infoType**.
     2. For **InfoType** , enter a name for the custom infoType. You can use letters, numbers, and underscores.
     3. For **Likelihood** , select the default likelihood level that you want to assign to to all findings that match this custom infoType. You can further fine-tune the likelihood level of individual findings by using [hotword rules](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes-likelihood).

If you don't specify a default value, the default likelihood level is set to `VERY_LIKELY`. For more information, see [Match likelihood](https://docs.cloud.google.com/sensitive-data-protection/docs/likelihood).

     4. For **Sensitivity** , select the sensitivity level that you want to assign to to all findings that match this custom infoType. If you don't specify a value, the sensitivity levels of those findings are set to `HIGH`.

Sensitivity scores are used in [data profiles](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles). When profiling your data, Sensitive Data Protection uses the sensitivity scores of the infoTypes to [calculate the sensitivity level](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitivity-risk-calculation).

     5. For **Stored infoType name** , select the stored infoType that you want to base the new custom infoType on.

     6. Click **Done** to close the **Add custom infoType** pane.

  5. Optional: On the **Built-in** tab, edit your selection of built-in infoTypes.

  6. Click **Done** to close the **InfoTypes** pane.

The custom infoType is added to the list of infoTypes that Sensitive Data Protection scans for. However, this selection isn't final until you save the job, job trigger, template, or scan configuration.

  7. When you're done creating or editing the configuration, click **Save**.




### C#

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using System;
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Dlp.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.html);
    
    public class InspectDataWithStoredInfotypes
    {
        public static InspectContentResponse Inspect(
            string projectId,
            string storedInfotypePath,
            string text,
            [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html) infoType = null)
        {
            // Instantiate the dlp client.
            var dlp = [DlpServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html#Google_Cloud_Dlp_V2_DlpServiceClient_Create)();
    
            // Construct the infotype if null.
            var infotype = infoType ?? new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html) { Name = "GITHUB_LOGINS" };
    
            // Construct the inspect config using stored infotype.
            var inspectConfig = new [InspectConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectConfig.html)
            {
                CustomInfoTypes =
                {
                    new [CustomInfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CustomInfoType.html)
                    {
                        InfoType = infotype,
                        StoredType = new [StoredType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.StoredType.html) { Name = storedInfotypePath }
                    }
                },
                IncludeQuote = true
            };
    
            // Construct the request using inspect config.
            var request = new [InspectContentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectContentRequest.html)
            {
                ParentAsLocationName = new [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)(projectId, "global"),
                InspectConfig = inspectConfig,
                Item = new [ContentItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentItem.html) { Value = text }
            };
    
            // Call the API.
            [InspectContentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectContentResponse.html) response = dlp.InspectContent(request);
    
            // Inspect the results.
            var findings = response.[Result](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectContentResponse.html#Google_Cloud_Dlp_V2_InspectContentResponse_Result).Findings;
            Console.WriteLine($"Findings: {findings.Count}");
            foreach (var f in findings)
            {
                Console.WriteLine("\tQuote: " + f.Quote);
                Console.WriteLine("\tInfo type: " + f.[InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html).Name);
                Console.WriteLine("\tLikelihood: " + f.[Likelihood](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Likelihood.html));
            }
    
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
    
    // inspectWithStoredInfotype inspects the given text using the specified stored infoType detector.
    func inspectWithStoredInfotype(w io.Writer, projectID, infoTypeId, textToDeidentify string) error {
    	// projectId := "your-project-id"
    	// infoTypeId := "your-info-type-id"
    	// textToDeidentify := "This commit was made by kewin2010"
    
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
    
    	// Specify the content to be inspected.
    	contentItem := &dlppb.ContentItem{
    		DataItem: &dlppb.ContentItem_Value{
    			Value: textToDeidentify,
    		},
    	}
    
    	// Specify the info type the inspection will look for.
    	infoType := &dlppb.InfoType{
    		Name: "GITHUB_LOGINS",
    	}
    
    	// Specify the stored info type the inspection will look for.
    	storedType := &dlppb.StoredType{
    		Name: infoTypeId,
    	}
    
    	customInfoType := &dlppb.CustomInfoType{
    		InfoType: infoType,
    		Type: &dlppb.CustomInfoType_StoredType{
    			StoredType: storedType,
    		},
    	}
    
    	// Specify how the content should be inspected.
    	inspectConfig := &dlppb.InspectConfig{
    		CustomInfoTypes: []*dlppb.CustomInfoType{
    			customInfoType,
    		},
    		IncludeQuote: true,
    	}
    
    	// Construct the Inspect request to be sent by the client.
    	req := &dlppb.InspectContentRequest{
    		Parent:        fmt.Sprintf("projects/%s/locations/global", projectID),
    		InspectConfig: inspectConfig,
    		Item:          contentItem,
    	}
    
    	// Use the client to send the API request.
    	resp, err := client.InspectContent(ctx, req)
    	if err != nil {
    		return err
    	}
    
    	// Process the results.
    	fmt.Fprintf(w, "Findings: %d\n", len(resp.Result.Findings))
    	for _, f := range resp.Result.Findings {
    		fmt.Fprintf(w, "\tQuote: %s\n", f.Quote)
    		fmt.Fprintf(w, "\tInfo type: %s\n", f.InfoType.Name)
    		fmt.Fprintf(w, "\tLikelihood: %s\n", f.Likelihood)
    	}
    	return nil
    }
    

### Java

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.dlp.v2.[DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html);
    import com.google.privacy.dlp.v2.[ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html);
    import com.google.privacy.dlp.v2.[CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html);
    import com.google.privacy.dlp.v2.[Finding](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Finding.html);
    import com.google.privacy.dlp.v2.[InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html);
    import com.google.privacy.dlp.v2.[InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html);
    import com.google.privacy.dlp.v2.[InspectContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectContentRequest.html);
    import com.google.privacy.dlp.v2.[InspectContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectContentResponse.html);
    import com.google.privacy.dlp.v2.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html);
    import com.google.privacy.dlp.v2.[ProjectStoredInfoTypeName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ProjectStoredInfoTypeName.html);
    import com.google.privacy.dlp.v2.[StoredType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.StoredType.html);
    import java.io.IOException;
    
    public class InspectWithStoredInfotype {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        // The Google Cloud project id to use as a parent resource.
        String projectId = "your-project-id";
        // The sample assumes that you have an existing stored infoType.
        // To create a stored InfoType refer:
        // https://cloud.google.com/dlp/docs/creating-stored-infotypes#create-storedinfotye 
        String storedInfoTypeId = "your-info-type-id";
        // The string to de-identify.
        String textToInspect =
            "My phone number is (223) 456-7890 and my email address is gary@example.com.";
        inspectWithStoredInfotype(projectId, storedInfoTypeId, textToInspect);
      }
    
      //  Inspects the given text using the specified stored infoType detector.
      public static void inspectWithStoredInfotype(
          String projectId, String storedInfoTypeId, String textToInspect) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html) dlp = [DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html).create()) {
    
          // Specify the content to be inspected.
          [ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html) contentItem = [ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html).newBuilder().setValue(textToInspect).build();
    
          [InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html) infoType = [InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html).newBuilder().setName("STORED_TYPE").build();
    
          // Reference to the existing StoredInfoType to inspect the data.
          [StoredType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.StoredType.html) storedType = [StoredType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.StoredType.html).newBuilder()
                  .setName([ProjectStoredInfoTypeName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ProjectStoredInfoTypeName.html).of(projectId, storedInfoTypeId).toString())
                  .build();
    
          [CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html) customInfoType =
              [CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html).newBuilder().setInfoType(infoType).[setStoredType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Builder.html#com_google_privacy_dlp_v2_CustomInfoType_Builder_setStoredType_com_google_privacy_dlp_v2_StoredType_)(storedType).build();
    
          // Construct the configuration for the Inspect request.
          [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html) inspectConfig =
              [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html).newBuilder()
                  .[addCustomInfoTypes](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.Builder.html#com_google_privacy_dlp_v2_InspectConfig_Builder_addCustomInfoTypes_com_google_privacy_dlp_v2_CustomInfoType_)(customInfoType)
                  .[setIncludeQuote](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.Builder.html#com_google_privacy_dlp_v2_InspectConfig_Builder_setIncludeQuote_boolean_)(true)
                  .build();
    
          // Construct the Inspect request to be sent by the client.
          [InspectContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectContentRequest.html) inspectContentRequest =
              [InspectContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectContentRequest.html).newBuilder()
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html).of(projectId, "global").toString())
                  .setInspectConfig(inspectConfig)
                  .setItem(contentItem)
                  .build();
    
          // Use the client to send the API request.
          [InspectContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectContentResponse.html) response = dlp.inspectContent(inspectContentRequest);
    
          // Parse the response and process results.
          System.out.println("Findings: " + "" + response.[getResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectContentResponse.html#com_google_privacy_dlp_v2_InspectContentResponse_getResult__)().getFindingsCount());
          for ([Finding](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Finding.html) f : response.[getResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectContentResponse.html#com_google_privacy_dlp_v2_InspectContentResponse_getResult__)().getFindingsList()) {
            System.out.println("\tQuote: " + f.getQuote());
            System.out.println("\tInfoType: " + f.getInfoType().getName());
            System.out.println("\tLikelihood: " + f.getLikelihood() + "\n");
          }
        }
      }
    }

### Node.js

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud Data Loss Prevention library
    const DLP = require('[@google-cloud/dlp](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/overview.html)');
    
    // Instantiates a client
    const dlp = new DLP.[DlpServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/overview.html)();
    
    // The project ID to run the API call under.
    // const projectId = 'your-project-id';
    
    // The custom info-type id created and stored in the bucket.
    // const infoTypeId = 'your-info-type-id';
    
    // The string to inspect.
    // const string = 'My phone number is (223) 456-7890 and my email address is gary@example.com.';
    
    async function inspectWithStoredInfotype() {
      // Reference to the existing StoredInfoType to inspect the data.
      const customInfoType = {
        infoType: {
          name: 'GITHUB_LOGINS',
        },
        storedType: {
          name: infoTypeId,
        },
      };
    
      // Construct the configuration for the Inspect request.
      const inspectConfig = {
        customInfoTypes: [customInfoType],
        includeQuote: true,
      };
    
      // Construct the Inspect request to be sent by the client.
      const request = {
        parent: `projects/${projectId}/locations/global`,
        inspectConfig: inspectConfig,
        item: {
          value: string,
        },
      };
      // Run request
      const [response] = await dlp.inspectContent(request);
    
      // Print Findings
      const findings = response.result.findings;
      if (findings.length > 0) {
        console.log(`Findings: ${findings.length}\n`);
        findings.forEach(finding => {
          console.log(`InfoType: ${finding.infoType.name}`);
          console.log(`\tQuote: ${finding.quote}`);
          console.log(`\tLikelihood: ${finding.likelihood} \n`);
        });
      } else {
        console.log('No findings.');
      }
    }
    await inspectWithStoredInfotype();

### PHP

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Dlp\V2\Client\DlpServiceClient;
    use Google\Cloud\Dlp\V2\ContentItem;
    use Google\Cloud\Dlp\V2\CustomInfoType;
    use Google\Cloud\Dlp\V2\InfoType;
    use Google\Cloud\Dlp\V2\InspectConfig;
    use Google\Cloud\Dlp\V2\InspectContentRequest;
    use Google\Cloud\Dlp\V2\Likelihood;
    use Google\Cloud\Dlp\V2\StoredType;
    
    /**
     * Inspect with stored infoType.
     * Scan content using a large custom dictionary detector.
     *
     * @param string $projectId             The Google Cloud Project ID to run the API call under.
     * @param string $storedInfoTypeName    The name of the stored infotype whose This value must be in the format
     * projects/projectName/(locations/locationId)/storedInfoTypes/storedInfoTypeName.
     * @param string $textToInspect         The string to inspect.
     */
    function inspect_with_stored_infotype(
        string $projectId,
        string $storedInfoTypeName,
        string $textToInspect
    ): void {
        // Instantiate a client.
        $dlp = new DlpServiceClient();
    
        $parent = "projects/$projectId/locations/global";
    
        // Specify the content to be inspected.
        $item = (new ContentItem())
            ->setValue($textToInspect);
    
        // Reference to the existing StoredInfoType to inspect the data.
        $customInfoType = (new CustomInfoType())
            ->setInfoType((new InfoType())
                ->setName('STORED_TYPE'))
            ->setStoredType((new StoredType())
                ->setName($storedInfoTypeName));
    
        // Construct the configuration for the Inspect request.
        $inspectConfig = (new InspectConfig())
            ->setCustomInfoTypes([$customInfoType])
            ->setIncludeQuote(true);
    
        // Run request.
        $inspectContentRequest = (new InspectContentRequest())
            ->setParent($parent)
            ->setInspectConfig($inspectConfig)
            ->setItem($item);
        $response = $dlp->inspectContent($inspectContentRequest);
    
        // Print the results.
        $findings = $response->getResult()->getFindings();
        if (count($findings) == 0) {
            printf('No findings.' . PHP_EOL);
        } else {
            printf('Findings:' . PHP_EOL);
            foreach ($findings as $finding) {
                printf('  Quote: %s' . PHP_EOL, $finding->getQuote());
                printf('  Info type: %s' . PHP_EOL, $finding->getInfoType()->getName());
                printf('  Likelihood: %s' . PHP_EOL, Likelihood::name($finding->getLikelihood()));
            }
        }
    }

### Python

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import google.cloud.dlp
    
    
    def inspect_with_stored_infotype(
        project: str,
        stored_info_type_id: str,
        content_string: str,
    ) -> None:
        """Uses the Data Loss Prevention API to inspect/scan content using stored
        infoType.
        Args:
            project: The Google Cloud project id to use as a parent resource.
            content_string: The string to inspect.
            stored_info_type_id: The identifier of stored infoType used to inspect.
        """
    
        # Instantiate a client.
        dlp = google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html)()
    
        # Convert stored infoType id into full resource id
        stored_type_name = f"projects/{project}/storedInfoTypes/{stored_info_type_id}"
    
        # Construct a custom info type dictionary using stored infoType.
        custom_info_types = [
            {
                "info_type": {"name": "STORED_TYPE"},
                "stored_type": {
                    "name": stored_type_name,
                },
            }
        ]
    
        # Construct the inspection configuration dictionary.
        inspect_config = {
            "custom_info_types": custom_info_types,
            "include_quote": True,
        }
    
        # Construct the `item` to be inspected using stored infoType.
        item = {"value": content_string}
    
        # Convert the project id into a full resource id.
        parent = f"projects/{project}/locations/global"
    
        # Call the API.
        response = dlp.[inspect_content](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceClient_inspect_content)(
            request={
                "parent": parent,
                "inspect_config": inspect_config,
                "item": item,
            }
        )
    
        # Print out the results.
        if response.result.findings:
            for finding in response.result.findings:
                print(f"Quote: {finding.quote}")
                print(f"Info type: {finding.info_type.name}")
                print(f"Likelihood: {finding.likelihood}")
        else:
            print("No findings.")
    
    

### REST

When sent to the [`content.inspect`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.content/inspect) method, the following example scans the given text using the specified stored infoType detector. The `infoType` parameter is required because all custom infoTypes must have a name that doesn't conflict with built-in infoTypes or other custom infoTypes. The `storedType` parameter contains the full resource path of the stored infoType.

**JSON input**
    
    
    POST https://dlp.googleapis.com/v2/projects/PROJECT_ID/content:inspect
    
    {
      "inspectConfig":{
        "customInfoTypes":[
          {
            "infoType":{
              "name":"GITHUB_LOGINS"
            },
            "storedType":{
              "name":"projects/PROJECT_ID/storedInfoTypes/github-logins"
            }
          }
        ]
      },
      "item":{
        "value":"The commit was made by githubuser."
      }
    }
    

## Troubleshoot errors

If you get an error while attempting to create a stored infoType from a term list stored in Cloud Storage, the following are possible causes:

  * You've run into an [upper limit for stored infoTypes](https://docs.cloud.google.com/sensitive-data-protection/limits#stored-infotype-limits). Depending on the problem, there are several workarounds: 
    * If you run into the upper limit for a single input file in Cloud Storage (200 MB), try splitting the file into multiple files. You can use multiple files to assemble a single custom dictionary as long as the combined size of all files doesn't exceed 1 GB.
    * BigQuery doesn't have the same limits as Cloud Storage. Consider moving the terms into a BigQuery table. The maximum size of a custom dictionary column in BigQuery is 1 GB and the maximum number of rows is 5,000,000.
    * If your term list file exceeds all applicable limits for source term lists, you must split the term list file into multiple files and create a dictionary for each file. Then, create a separate scan job for each dictionary.
  * One or more of your terms doesn't contain at least one letter or number. Sensitive Data Protection can't scan for terms that are composed solely of spaces or symbols. It must have at least one letter or number. Look at your term list and see if there are any such terms included, and then fix or delete them.
  * Your term list contains a phrase with too many "components." A component in this context is a continuous sequence containing only letters, only numbers, or only non-letter and non-digit characters such as spaces or symbols. Look at your term list and see if there are any such terms included, and then fix or delete them.
  * The Sensitive Data Protection service agent does not have access to dictionary source data or to the Cloud Storage bucket for storing dictionary files. To fix this issue, grant the Sensitive Data Protection service agent the Storage Admin (`roles/storage.admin`) role or BigQuery Data Owner (`roles/bigquery.dataOwner`) and BigQuery Job User (`roles/bigquery.jobUser`) roles.



## API overview

Creating a stored infoType is required if you are creating a large custom dictionary detector.

**Note:** If you're [creating a regular custom dictionary detector](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes-dictionary) or a [regular expression detector](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes-regex), you don't need to create a stored infoType. It's simpler to define those directly in the [`CustomInfoType`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#CustomInfoType) object.

A stored infoType is represented in Sensitive Data Protection by the [`StoredInfoType`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.storedInfoTypes#resource-storedinfotype) object. It consists of the following related objects:

  * [`StoredInfoTypeVersion`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.storedInfoTypes#storedinfotypeversion) includes the creation date and time and the last five error messages that occurred when the current version was created.

    * [`StoredInfoTypeConfig`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.storedInfoTypes#storedinfotypeconfig) contains the configuration of the stored infoType, including its name and description. For a large custom dictionary, the `type` must be a [`LargeCustomDictionaryConfig`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.storedInfoTypes#largecustomdictionaryconfig).

      * `LargeCustomDictionaryConfig` specifies both of the following: 
        * The location within Cloud Storage or BigQuery where your list of phrases is stored.
        * The location in Cloud Storage to store the generated dictionary files.
    * [`StoredInfoTypeState`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.storedInfoTypes#storedinfotypestate) contains the state of the most current version and any pending versions of the stored infoType. State information includes whether the stored infoType is being rebuilt, is ready to use, or is invalid.




## Dictionary matching specifics

Following is guidance about how Sensitive Data Protection matches dictionary words and phrases. These points apply to both regular and large custom dictionaries:

  * Dictionary words are case-insensitive. If your dictionary includes `Abby`, it will match on `abby`, `ABBY`, `Abby`, and so on.
  * All characters—in dictionaries or in content to be scanned—other than letters, digits, and other alphabetic characters contained within the Unicode [Basic Multilingual Plane](https://en.wikipedia.org/wiki/Plane_%28Unicode%29#Basic_Multilingual_Plane) are considered as whitespace when scanning for matches. If your dictionary scans for `Abby Abernathy`, it will match on `abby abernathy`, `Abby, Abernathy`, `Abby (ABERNATHY)`, and so on.
  * The characters surrounding any match must be of a different type (letters or digits) than the adjacent characters within the word. If your dictionary scans for `Abi`, it will match the first three characters of `Abi904`, but not of `Abigail`.
  * Dictionary words containing characters in the [Supplementary Multilingual Plane](https://en.wikipedia.org/wiki/Plane_%28Unicode%29#Supplementary_Multilingual_Plane) of the Unicode standard can yield unexpected findings. Examples of such characters are emojis, scientific symbols, and historical scripts. 



Letters, digits, and other alphabetic characters are defined as follows:

  * Letters: characters with general categories `Lu`, `Ll`, `Lt`, `Lm`, or `Lo` in the Unicode specification
  * Digits: characters with general category `Nd` in the Unicode specification
  * Other alphabetic characters: characters with general category `Nl` in the Unicode specification or with contributory property `Other_Alphabetic` as defined by the Unicode Standard



To create, edit, or delete a stored infoType, you use the following methods:

  * [`storedInfoTypes.create`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.storedInfoTypes/create): Creates a new stored infoType given the `StoredInfoTypeConfig` that you specify.
  * [`storedInfoTypes.patch`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.storedInfoTypes/patch): Rebuilds the stored infoType with a new `StoredInfoTypeConfig` that you specify. If none is specified, this method creates a new version of the stored infoType with the existing `StoredInfoTypeConfig`.
  * [`storedInfoTypes.get`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.storedInfoTypes/get): Retrieves the `StoredInfoTypeConfig` and any pending versions of the specified stored infoType.
  * [`storedInfoTypes.list`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.storedInfoTypes/list): Lists all current stored infoTypes.
  * [`storedInfoTypes.delete`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.storedInfoTypes/delete): Deletes the specified stored infoType.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
