---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/samples/dlp-update-stored-infotype/
title: Update a stored infoType \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:40:51.940172+00:00
---

# Update a stored infoType  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/samples/dlp-update-stored-infotype/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Samples ](https://docs.cloud.google.com/sensitive-data-protection/docs/samples)



#  Update a stored infoType Stay organized with collections  Save and categorize content based on your preferences. 

This sample demonstrates how to update the source term list of a stored infoType and rebuild the dictionary.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create a large custom dictionary detector](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-stored-infotypes)



## Code sample

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
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=clouddatalossprevention). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
