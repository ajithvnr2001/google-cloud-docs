---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/samples/dlp-deidentify-cloud-storage/
title: Create de-identified copies of Cloud Storage files \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:37:23.356769+00:00
---

# Create de-identified copies of Cloud Storage files  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/samples/dlp-deidentify-cloud-storage/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Samples ](https://docs.cloud.google.com/sensitive-data-protection/docs/samples)



#  Create de-identified copies of Cloud Storage files Stay organized with collections  Save and categorize content based on your preferences. 

This sample demonstrates how to inspect a Cloud Storage resource and create de-identified copies of the files.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create de-identified copies of data stored in Cloud Storage using the API](https://docs.cloud.google.com/sensitive-data-protection/docs/deidentify-storage)



## Code sample

### C#

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Dlp.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.html);
    using System.Linq;
    
    public class DeidentifyDataStoredInCloudStorage
    {
        public static DlpJob Deidentify(
            string projectId,
            string gcsInputPath,
            string unstructuredDeidentifyTemplatePath,
            string structuredDeidentifyTemplatePath,
            string imageRedactionTemplatePath,
            string gcsOutputPath,
            string datasetId,
            string tableId)
        {
            // Instantiate the client.
            var dlp = [DlpServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html#Google_Cloud_Dlp_V2_DlpServiceClient_Create)();
    
            //Construct the storage config by specifying the input directory.
            var storageConfig = new [StorageConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.StorageConfig.html)
            {
                CloudStorageOptions = new [CloudStorageOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CloudStorageOptions.html)
                {
                    FileSet = new CloudStorageOptions.Types.FileSet
                    {
                        Url = gcsInputPath
                    }
                }
            };
    
            // Construct the inspect config by specifying the type of info to be inspected.
            var inspectConfig = new [InspectConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectConfig.html)
            {
                InfoTypes =
                {
                    new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html)[]
                    {
                        new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html) { Name = "PERSON_NAME" },
                        new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html) { Name = "EMAIL_ADDRESS" }
                    }
                },
                IncludeQuote = true
            };
    
            // Construct the actions to take after the inspection portion of the job is completed.
            // Specify how Cloud DLP must de-identify sensitive data in structured files, unstructured files and images
            // using Transformation config.
            // The de-identified files will be written to the the GCS bucket path specified in gcsOutputPath and the details of 
            // transformations performed will be written to BigQuery table specified in datasetId and tableId.
            var actions = new [Action](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Action.html)[]
            {
                new [Action](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Action.html)
                {
                    Deidentify = new Action.Types.Deidentify
                    {
                        CloudStorageOutput = gcsOutputPath,
                        TransformationConfig = new [TransformationConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.TransformationConfig.html)
                        {
                            DeidentifyTemplate = unstructuredDeidentifyTemplatePath,
                            ImageRedactTemplate = imageRedactionTemplatePath,
                            StructuredDeidentifyTemplate = structuredDeidentifyTemplatePath,
                        },
                        TransformationDetailsStorageConfig = new [TransformationDetailsStorageConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.TransformationDetailsStorageConfig.html)
                        {
                            Table = new [BigQueryTable](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.BigQueryTable.html)
                            {
                                ProjectId = projectId,
                                DatasetId = datasetId,
                                TableId = tableId
                            }
                        }
                    }
                }
            };
    
            // Construct the inspect job config using created storage config, inspect config and actions.
            var inspectJob = new [InspectJobConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectJobConfig.html)
            {
                StorageConfig = storageConfig,
                InspectConfig = inspectConfig,
                Actions = { actions }
            };
    
            // Create the dlp job and call the API.
            [DlpJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpJob.html) response = dlp.CreateDlpJob(new [CreateDlpJobRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CreateDlpJobRequest.html)
            {
                ParentAsLocationName = new [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)(projectId, "global"),
                InspectJob = inspectJob
            });
    
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
    
    func deidentifyCloudStorage(w io.Writer, projectID, gcsUri, tableId, datasetId, outputDirectory, deidentifyTemplateId, structuredDeidentifyTemplateId, imageRedactTemplateId string) error {
    	// projectId := "my-project-id"
    	// gcsUri := "gs://" + "your-bucket-name" + "/path/to/your/file.txt"
    	// tableId := "your-bigquery-table-id"
    	// datasetId := "your-bigquery-dataset-id"
    	// outputDirectory := "your-output-directory"
    	// deidentifyTemplateId := "your-deidentify-template-id"
    	// structuredDeidentifyTemplateId := "your-structured-deidentify-template-id"
    	// imageRedactTemplateId := "your-image-redact-template-id"
    
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
    	cloudStorageOptions := &dlppb.CloudStorageOptions{
    		FileSet: &dlppb.CloudStorageOptions_FileSet{
    			Url: gcsUri,
    		},
    	}
    
    	// Define the storage config options for cloud storage options.
    	storageConfig := &dlppb.StorageConfig{
    		Type: &dlppb.StorageConfig_CloudStorageOptions{
    			CloudStorageOptions: cloudStorageOptions,
    		},
    	}
    
    	// Specify the type of info the inspection will look for.
    	// See https://cloud.google.com/dlp/docs/infotypes-reference for complete list of info types
    	infoTypes := []*dlppb.InfoType{
    		{Name: "PERSON_NAME"},
    		{Name: "EMAIL_ADDRESS"},
    	}
    
    	// inspectConfig holds the configuration settings for data inspection and analysis
    	// within the context of the Google Cloud Data Loss Prevention (DLP) API.
    	inspectConfig := &dlppb.InspectConfig{
    		InfoTypes:    infoTypes,
    		IncludeQuote: true,
    	}
    
    	// Types of files to include for de-identification.
    	fileTypesToTransform := []dlppb.FileType{
    		dlppb.[FileType_CSV](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2/dlppb.html#cloud_google_com_go_dlp_apiv2_dlppb_FileType_FILE_TYPE_UNSPECIFIED_FileType_BINARY_FILE_FileType_TEXT_FILE_FileType_IMAGE_FileType_WORD_FileType_PDF_FileType_AVRO_FileType_CSV_FileType_TSV_FileType_POWERPOINT_FileType_EXCEL),
    		dlppb.[FileType_IMAGE](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2/dlppb.html#cloud_google_com_go_dlp_apiv2_dlppb_FileType_FILE_TYPE_UNSPECIFIED_FileType_BINARY_FILE_FileType_TEXT_FILE_FileType_IMAGE_FileType_WORD_FileType_PDF_FileType_AVRO_FileType_CSV_FileType_TSV_FileType_POWERPOINT_FileType_EXCEL),
    		dlppb.[FileType_TEXT_FILE](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2/dlppb.html#cloud_google_com_go_dlp_apiv2_dlppb_FileType_FILE_TYPE_UNSPECIFIED_FileType_BINARY_FILE_FileType_TEXT_FILE_FileType_IMAGE_FileType_WORD_FileType_PDF_FileType_AVRO_FileType_CSV_FileType_TSV_FileType_POWERPOINT_FileType_EXCEL),
    	}
    
    	// Specify the BigQuery table to be inspected.
    	table := &dlppb.BigQueryTable{
    		ProjectId: projectID,
    		DatasetId: datasetId,
    		TableId:   tableId,
    	}
    
    	// transformationDetailsStorageConfig holds configuration settings for storing transformation
    	// details in the context of the Google Cloud Data Loss Prevention (DLP) API.
    	transformationDetailsStorageConfig := &dlppb.TransformationDetailsStorageConfig{
    		Type: &dlppb.TransformationDetailsStorageConfig_Table{
    			Table: table,
    		},
    	}
    
    	transformationConfig := &dlppb.TransformationConfig{
    		DeidentifyTemplate:           deidentifyTemplateId,
    		ImageRedactTemplate:          imageRedactTemplateId,
    		StructuredDeidentifyTemplate: structuredDeidentifyTemplateId,
    	}
    
    	// Action to execute on the completion of a job.
    	deidentify := &dlppb.Action_Deidentify{
    		TransformationConfig:               transformationConfig,
    		TransformationDetailsStorageConfig: transformationDetailsStorageConfig,
    		Output: &dlppb.Action_Deidentify_CloudStorageOutput{
    			CloudStorageOutput: outputDirectory,
    		},
    		FileTypesToTransform: fileTypesToTransform,
    	}
    
    	action := &dlppb.Action{
    		Action: &dlppb.Action_Deidentify_{
    			Deidentify: deidentify,
    		},
    	}
    
    	// Configure the inspection job we want the service to perform.
    	inspectJobConfig := &dlppb.InspectJobConfig{
    		StorageConfig: storageConfig,
    		InspectConfig: inspectConfig,
    		Actions: []*dlppb.Action{
    			action,
    		},
    	}
    
    	// Construct the job creation request to be sent by the client.
    	req := &dlppb.CreateDlpJobRequest{
    		Parent: fmt.Sprintf("projects/%s/locations/global", projectID),
    		Job: &dlppb.CreateDlpJobRequest_InspectJob{
    			InspectJob: inspectJobConfig,
    		},
    	}
    
    	// Send the request.
    	resp, err := client.CreateDlpJob(ctx, req)
    	if err != nil {
    		fmt.Fprintf(w, "error after resp: %v", err)
    		return err
    	}
    
    	// Print the results.
    	fmt.Fprint(w, "Job created successfully: ", resp.Name)
    	return nil
    
    }
    

### Java

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.dlp.v2.[DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html);
    import com.google.privacy.dlp.v2.[Action](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.html);
    import com.google.privacy.dlp.v2.[BigQueryTable](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.BigQueryTable.html);
    import com.google.privacy.dlp.v2.[CloudStorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CloudStorageOptions.html);
    import com.google.privacy.dlp.v2.[CreateDlpJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CreateDlpJobRequest.html);
    import com.google.privacy.dlp.v2.[DlpJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html);
    import com.google.privacy.dlp.v2.[FileType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FileType.html);
    import com.google.privacy.dlp.v2.[InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html);
    import com.google.privacy.dlp.v2.[InfoTypeStats](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeStats.html);
    import com.google.privacy.dlp.v2.[InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html);
    import com.google.privacy.dlp.v2.[InspectDataSourceDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectDataSourceDetails.html);
    import com.google.privacy.dlp.v2.[InspectJobConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectJobConfig.html);
    import com.google.privacy.dlp.v2.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html);
    import com.google.privacy.dlp.v2.[ProjectDeidentifyTemplateName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ProjectDeidentifyTemplateName.html);
    import com.google.privacy.dlp.v2.[StorageConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.StorageConfig.html);
    import com.google.privacy.dlp.v2.[TransformationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.TransformationConfig.html);
    import com.google.privacy.dlp.v2.[TransformationDetailsStorageConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.TransformationDetailsStorageConfig.html);
    import java.io.IOException;
    import java.util.ArrayList;
    import java.util.Arrays;
    import java.util.List;
    import java.util.concurrent.TimeUnit;
    
    public class DeidentifyCloudStorage {
    
      // Set the timeout duration in minutes.
      private static final int TIMEOUT_MINUTES = 15;
    
      public static void main(String[] args) throws IOException, InterruptedException {
        // TODO(developer): Replace these variables before running the sample.
        // The Google Cloud project id to use as a parent resource.
        String projectId = "your-project-id";
        // Specify the cloud storage directory that you want to inspect.
        String gcsPath = "gs://" + "your-bucket-name" + "/path/to/your/file.txt";
        // Specify the big query dataset id to store the transformation details.
        String datasetId = "your-bigquery-dataset-id";
        // Specify the big query table id to store the transformation details.
        String tableId = "your-bigquery-table-id";
        // Specify the cloud storage directory to store the de-identified files.
        String outputDirectory = "your-output-directory";
        // Specify the de-identify template ID for unstructured files.
        String deidentifyTemplateId = "your-deidentify-template-id";
        // Specify the de-identify template ID for structured files.
        String structuredDeidentifyTemplateId = "your-structured-deidentify-template-id";
        // Specify the de-identify template ID for images.
        String imageRedactTemplateId = "your-image-redact-template-id";
        deidentifyCloudStorage(
            projectId,
            gcsPath,
            tableId,
            datasetId,
            outputDirectory,
            deidentifyTemplateId,
            structuredDeidentifyTemplateId,
            imageRedactTemplateId);
      }
    
      public static void deidentifyCloudStorage(
          String projectId,
          String gcsPath,
          String tableId,
          String datasetId,
          String outputDirectory,
          String deidentifyTemplateId,
          String structuredDeidentifyTemplateId,
          String imageRedactTemplateId)
          throws IOException, InterruptedException {
    
        try ([DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html) dlp = [DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html).create()) {
          // Set path in Cloud Storage.
          [CloudStorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CloudStorageOptions.html) cloudStorageOptions =
              [CloudStorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CloudStorageOptions.html).newBuilder()
                  .[setFileSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CloudStorageOptions.Builder.html#com_google_privacy_dlp_v2_CloudStorageOptions_Builder_setFileSet_com_google_privacy_dlp_v2_CloudStorageOptions_FileSet_)([CloudStorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CloudStorageOptions.html).FileSet.newBuilder().setUrl(gcsPath))
                  .build();
    
          // Set storage config indicating the type of cloud storage.
          [StorageConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.StorageConfig.html) storageConfig =
              [StorageConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.StorageConfig.html).newBuilder().[setCloudStorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.StorageConfig.Builder.html#com_google_privacy_dlp_v2_StorageConfig_Builder_setCloudStorageOptions_com_google_privacy_dlp_v2_CloudStorageOptions_)(cloudStorageOptions).build();
    
          // Specify the type of info the inspection will look for.
          // See https://cloud.google.com/dlp/docs/infotypes-reference for complete list of info types
          List<InfoType> infoTypes = new ArrayList<>();
          for (String typeName : new String[] {"PERSON_NAME", "EMAIL_ADDRESS"}) {
            infoTypes.add([InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html).newBuilder().setName(typeName).build());
          }
    
          [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html) inspectConfig =
              [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html).newBuilder().addAllInfoTypes(infoTypes).[setIncludeQuote](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.Builder.html#com_google_privacy_dlp_v2_InspectConfig_Builder_setIncludeQuote_boolean_)(true).build();
    
          // Types of files to include for de-identification.
          List<FileType> fileTypesToTransform =
              Arrays.asList(
                  [FileType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FileType.html).valueOf("IMAGE"), [FileType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FileType.html).valueOf("CSV"), [FileType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FileType.html).valueOf("TEXT_FILE"));
    
          // Specify the big query table to store the transformation details.
          [BigQueryTable](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.BigQueryTable.html) table =
              [BigQueryTable](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.BigQueryTable.html).newBuilder()
                  .setProjectId(projectId)
                  .setTableId(tableId)
                  .setDatasetId(datasetId)
                  .build();
    
          [TransformationDetailsStorageConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.TransformationDetailsStorageConfig.html) transformationDetailsStorageConfig =
              [TransformationDetailsStorageConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.TransformationDetailsStorageConfig.html).newBuilder().setTable(table).build();
    
          // Specify the de-identify template used for the transformation.
          [TransformationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.TransformationConfig.html) transformationConfig =
              [TransformationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.TransformationConfig.html).newBuilder()
                  .setDeidentifyTemplate(
                      [ProjectDeidentifyTemplateName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ProjectDeidentifyTemplateName.html).of(projectId, deidentifyTemplateId).toString())
                  .[setImageRedactTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.TransformationConfig.Builder.html#com_google_privacy_dlp_v2_TransformationConfig_Builder_setImageRedactTemplate_java_lang_String_)(
                      [ProjectDeidentifyTemplateName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ProjectDeidentifyTemplateName.html).of(projectId, imageRedactTemplateId).toString())
                  .[setStructuredDeidentifyTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.TransformationConfig.Builder.html#com_google_privacy_dlp_v2_TransformationConfig_Builder_setStructuredDeidentifyTemplate_java_lang_String_)(
                      [ProjectDeidentifyTemplateName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ProjectDeidentifyTemplateName.html).of(projectId, structuredDeidentifyTemplateId)
                          .toString())
                  .build();
    
          [Action](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.html).[Deidentify](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.Deidentify.html) deidentify =
              [Action](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.html).Deidentify.newBuilder()
                  .[setCloudStorageOutput](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.Deidentify.Builder.html#com_google_privacy_dlp_v2_Action_Deidentify_Builder_setCloudStorageOutput_java_lang_String_)(outputDirectory)
                  .[setTransformationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.Deidentify.Builder.html#com_google_privacy_dlp_v2_Action_Deidentify_Builder_setTransformationConfig_com_google_privacy_dlp_v2_TransformationConfig_)(transformationConfig)
                  .[setTransformationDetailsStorageConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.Deidentify.Builder.html#com_google_privacy_dlp_v2_Action_Deidentify_Builder_setTransformationDetailsStorageConfig_com_google_privacy_dlp_v2_TransformationDetailsStorageConfig_)(transformationDetailsStorageConfig)
                  .[addAllFileTypesToTransform](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.Deidentify.Builder.html#com_google_privacy_dlp_v2_Action_Deidentify_Builder_addAllFileTypesToTransform_java_lang_Iterable___extends_com_google_privacy_dlp_v2_FileType__)(fileTypesToTransform)
                  .build();
    
          [Action](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.html) action = [Action](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.html).newBuilder().[setDeidentify](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.Builder.html#com_google_privacy_dlp_v2_Action_Builder_setDeidentify_com_google_privacy_dlp_v2_Action_Deidentify_)(deidentify).build();
    
          // Configure the long-running job we want the service to perform.
          [InspectJobConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectJobConfig.html) inspectJobConfig =
              [InspectJobConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectJobConfig.html).newBuilder()
                  .setInspectConfig(inspectConfig)
                  .[setStorageConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectJobConfig.Builder.html#com_google_privacy_dlp_v2_InspectJobConfig_Builder_setStorageConfig_com_google_privacy_dlp_v2_StorageConfig_)(storageConfig)
                  .addActions(action)
                  .build();
    
          // Construct the job creation request to be sent by the client.
          [CreateDlpJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CreateDlpJobRequest.html) createDlpJobRequest =
              [CreateDlpJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CreateDlpJobRequest.html).newBuilder()
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html).of(projectId, "global").toString())
                  .setInspectJob(inspectJobConfig)
                  .build();
    
          // Send the job creation request.
          [DlpJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html) response = dlp.createDlpJob(createDlpJobRequest);
    
          // Get the current time.
          long startTime = System.currentTimeMillis();
    
          // Check if the job state is DONE.
          while (response.[getState](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html#com_google_privacy_dlp_v2_DlpJob_getState__)() != [DlpJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html).JobState.DONE) {
            // Sleep for 30 second.
            Thread.sleep(30000);
    
            // Get the updated job status.
            response = dlp.getDlpJob(response.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html#com_google_privacy_dlp_v2_DlpJob_getName__)());
    
            // Check if the timeout duration has exceeded.
            long elapsedTime = System.currentTimeMillis() - startTime;
            if (TimeUnit.MILLISECONDS.toMinutes(elapsedTime) >= TIMEOUT_MINUTES) {
              System.out.printf("Job did not complete within %d minutes.%n", TIMEOUT_MINUTES);
              break;
            }
          }
          // Print the results.
          System.out.println("Job status: " + response.[getState](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html#com_google_privacy_dlp_v2_DlpJob_getState__)());
          System.out.println("Job name: " + response.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html#com_google_privacy_dlp_v2_DlpJob_getName__)());
          [InspectDataSourceDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectDataSourceDetails.html).[Result](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectDataSourceDetails.Result.html) result = response.[getInspectDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html#com_google_privacy_dlp_v2_DlpJob_getInspectDetails__)().getResult();
          System.out.println("Findings: ");
          for ([InfoTypeStats](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeStats.html) infoTypeStat : result.getInfoTypeStatsList()) {
            System.out.print("\tInfo type: " + infoTypeStat.getInfoType().getName());
            System.out.println("\tCount: " + infoTypeStat.getCount());
          }
        }
      }
    }

### Node.js

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud client library
    const DLP = require('[@google-cloud/dlp](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/overview.html)');
    // Instantiates a client
    const dlp = new DLP.[DlpServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/overview.html)();
    
    // The project ID to run the API call under
    // const projectId = 'my-project';
    
    // The Cloud Storage directory that needs to be inspected
    // const inputDirectory = 'your-google-cloud-storage-path';
    
    // The ID of the dataset to inspect, e.g. 'my_dataset'
    // const datasetId = 'my_dataset';
    
    // The ID of the table to inspect, e.g. 'my_table'
    // const tableId = 'my_table';
    
    // The Cloud Storage directory that will be used to store the de-identified files
    // const outputDirectory = 'your-output-directory';
    
    // The full resource name of the default de-identify template
    // const deidentifyTemplateId = 'your-deidentify-template-id';
    
    // The full resource name of the de-identify template for structured files
    // const structuredDeidentifyTemplateId = 'your-structured-deidentify-template-id';
    
    // The full resource name of the image redaction template for images
    // const imageRedactTemplateId = 'your-image-redact-template-id';
    
    async function deidentifyCloudStorage() {
      // Specify storage configuration that uses file set.
      const storageConfig = {
        cloudStorageOptions: {
          fileSet: {
            url: inputDirectory,
          },
        },
      };
    
      // Specify the type of info the inspection will look for.
      const infoTypes = [{name: 'PERSON_NAME'}, {name: 'EMAIL_ADDRESS'}];
    
      // Construct inspect configuration
      const inspectConfig = {
        infoTypes: infoTypes,
        includeQuote: true,
      };
    
      // Types of files to include for de-identification.
      const fileTypesToTransform = [
        {fileType: 'IMAGE'},
        {fileType: 'CSV'},
        {fileType: '[TEXT_FILE](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.filetype.html)'},
      ];
    
      // Specify the big query table to store the transformation details.
      const transformationDetailsStorageConfig = {
        table: {
          projectId: projectId,
          tableId: tableId,
          datasetId: datasetId,
        },
      };
    
      // Specify the de-identify template used for the transformation.
      const transformationConfig = {
        deidentifyTemplate: deidentifyTemplateId,
        structuredDeidentifyTemplate: structuredDeidentifyTemplateId,
        imageRedactTemplate: imageRedactTemplateId,
      };
    
      // Construct action to de-identify sensitive data.
      const action = {
        deidentify: {
          cloudStorageOutput: outputDirectory,
          transformationConfig: transformationConfig,
          transformationDetailsStorageConfig: transformationDetailsStorageConfig,
          fileTypes: fileTypesToTransform,
        },
      };
    
      // Construct the inspect job configuration.
      const inspectJobConfig = {
        inspectConfig: inspectConfig,
        storageConfig: storageConfig,
        actions: [action],
      };
    
      // Construct the job creation request to be sent by the client.
      const createDlpJobRequest = {
        parent: `projects/${projectId}/locations/global`,
        inspectJob: inspectJobConfig,
      };
      // Send the job creation request and process the response.
      const [response] = await dlp.createDlpJob(createDlpJobRequest);
      const jobName = response.name;
    
      // Waiting for a maximum of 15 minutes for the job to get complete.
      let job;
      let numOfAttempts = 30;
      while (numOfAttempts > 0) {
        // Fetch DLP Job status
        [job] = await dlp.getDlpJob({name: jobName});
    
        // Check if the job has completed.
        if (job.state === 'DONE') {
          break;
        }
        if (job.state === 'FAILED') {
          console.log('Job Failed, Please check the configuration.');
          return;
        }
        // Sleep for a short duration before checking the job status again.
        await new Promise(resolve => {
          setTimeout(() => resolve(), 30000);
        });
        numOfAttempts -= 1;
      }
    
      // Print out the results.
      const infoTypeStats = job.inspectDetails.result.infoTypeStats;
      if (infoTypeStats.length > 0) {
        infoTypeStats.forEach(infoTypeStat => {
          console.log(
            `  Found ${infoTypeStat.count} instance(s) of infoType ${infoTypeStat.infoType.name}.`
          );
        });
      } else {
        console.log('No findings.');
      }
    }
    await deidentifyCloudStorage();

### PHP

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Dlp\V2\Action;
    use Google\Cloud\Dlp\V2\Action\Deidentify;
    use Google\Cloud\Dlp\V2\BigQueryTable;
    use Google\Cloud\Dlp\V2\Client\DlpServiceClient;
    use Google\Cloud\Dlp\V2\CloudStorageOptions;
    use Google\Cloud\Dlp\V2\CloudStorageOptions\FileSet;
    use Google\Cloud\Dlp\V2\CreateDlpJobRequest;
    use Google\Cloud\Dlp\V2\DlpJob\JobState;
    use Google\Cloud\Dlp\V2\FileType;
    use Google\Cloud\Dlp\V2\GetDlpJobRequest;
    use Google\Cloud\Dlp\V2\InfoType;
    use Google\Cloud\Dlp\V2\InspectConfig;
    use Google\Cloud\Dlp\V2\InspectJobConfig;
    use Google\Cloud\Dlp\V2\StorageConfig;
    use Google\Cloud\Dlp\V2\TransformationConfig;
    use Google\Cloud\Dlp\V2\TransformationDetailsStorageConfig;
    
    /**
     * De-identify sensitive data stored in Cloud Storage using the API.
     * Create an inspection job that has a de-identification action.
     *
     * @param string $callingProjectId                  The project ID to run the API call under.
     * @param string $inputgcsPath                       The Cloud Storage directory that you want to de-identify.
     * @param string $outgcsPath                        The Cloud Storage directory where you want to store the
     *                                                  de-identified files.
     * @param string $deidentifyTemplateName            The full resource name of the default de-identify template — for
     *                                                  unstructured and structured files — if you created one. This value
     *                                                  must be in the format
     *                                                  `projects/projectName/(locations/locationId)/deidentifyTemplates/templateName`.
     * @param string $structuredDeidentifyTemplateName  The full resource name of the de-identify template for structured
     *                                                  files if you created one. This value must be in the format
     *                                                  `projects/projectName/(locations/locationId)/deidentifyTemplates/templateName`.
     * @param string $imageRedactTemplateName           The full resource name of the image redaction template for images if
     *                                                  you created one. This value must be in the format
     *                                                  `projects/projectName/(locations/locationId)/deidentifyTemplates/templateName`.
     * @param string $datasetId                         The ID of the BigQuery dataset where you want to store
     *                                                  the transformation details. If you don't provide a table ID, the
     *                                                  system automatically creates one.
     * @param string $tableId                           The ID of the BigQuery table where you want to store the
     *                                                  transformation details.
     */
    function deidentify_cloud_storage(
        // TODO(developer): Replace sample parameters before running the code.
        string $callingProjectId,
        string $inputgcsPath = 'gs://YOUR_GOOGLE_STORAGE_BUCKET',
        string $outgcsPath = 'gs://YOUR_GOOGLE_STORAGE_BUCKET',
        string $deidentifyTemplateName = 'YOUR_DEIDENTIFY_TEMPLATE_NAME',
        string $structuredDeidentifyTemplateName = 'YOUR_STRUCTURED_DEIDENTIFY_TEMPLATE_NAME',
        string $imageRedactTemplateName = 'YOUR_IMAGE_REDACT_DEIDENTIFY_TEMPLATE_NAME',
        string $datasetId = 'YOUR_DATASET_ID',
        string $tableId = 'YOUR_TABLE_ID'
    ): void {
        // Instantiate a client.
        $dlp = new DlpServiceClient();
    
        $parent = "projects/$callingProjectId/locations/global";
    
        // Specify the GCS Path to be de-identify.
        $cloudStorageOptions = (new CloudStorageOptions())
            ->setFileSet((new FileSet())
                ->setUrl($inputgcsPath));
        $storageConfig = (new StorageConfig())
            ->setCloudStorageOptions(($cloudStorageOptions));
    
        // Specify the type of info the inspection will look for.
        $inspectConfig = (new InspectConfig())
            ->setInfoTypes([
                (new InfoType())->setName('PERSON_NAME'),
                (new InfoType())->setName('EMAIL_ADDRESS')
            ]);
    
        // Specify the big query table to store the transformation details.
        $transformationDetailsStorageConfig = (new TransformationDetailsStorageConfig())
            ->setTable((new BigQueryTable())
                ->setProjectId($callingProjectId)
                ->setDatasetId($datasetId)
                ->setTableId($tableId));
    
        // Specify the de-identify template used for the transformation.
        $transformationConfig = (new TransformationConfig())
            ->setDeidentifyTemplate(
                DlpServiceClient::projectDeidentifyTemplateName($callingProjectId, $deidentifyTemplateName)
            )
            ->setStructuredDeidentifyTemplate(
                DlpServiceClient::projectDeidentifyTemplateName($callingProjectId, $structuredDeidentifyTemplateName)
            )
            ->setImageRedactTemplate(
                DlpServiceClient::projectDeidentifyTemplateName($callingProjectId, $imageRedactTemplateName)
            );
    
        $deidentify = (new Deidentify())
            ->setCloudStorageOutput($outgcsPath)
            ->setTransformationConfig($transformationConfig)
            ->setTransformationDetailsStorageConfig($transformationDetailsStorageConfig)
            ->setFileTypesToTransform([FileType::TEXT_FILE, FileType::IMAGE, FileType::CSV]);
    
        $action = (new Action())
            ->setDeidentify($deidentify);
    
        // Configure the inspection job we want the service to perform.
        $inspectJobConfig = (new InspectJobConfig())
            ->setInspectConfig($inspectConfig)
            ->setStorageConfig($storageConfig)
            ->setActions([$action]);
    
        // Send the job creation request and process the response.
        $createDlpJobRequest = (new CreateDlpJobRequest())
            ->setParent($parent)
            ->setInspectJob($inspectJobConfig);
        $job = $dlp->createDlpJob($createDlpJobRequest);
    
        $numOfAttempts = 10;
        do {
            printf('Waiting for job to complete' . PHP_EOL);
            sleep(30);
            $getDlpJobRequest = (new GetDlpJobRequest())
                ->setName($job->getName());
            $job = $dlp->getDlpJob($getDlpJobRequest);
            if ($job->getState() == JobState::DONE) {
                break;
            }
            $numOfAttempts--;
        } while ($numOfAttempts > 0);
    
        // Print finding counts.
        printf('Job %s status: %s' . PHP_EOL, $job->getName(), JobState::name($job->getState()));
        switch ($job->getState()) {
            case JobState::DONE:
                $infoTypeStats = $job->getInspectDetails()->getResult()->getInfoTypeStats();
                if (count($infoTypeStats) === 0) {
                    printf('No findings.' . PHP_EOL);
                } else {
                    foreach ($infoTypeStats as $infoTypeStat) {
                        printf(
                            '  Found %s instance(s) of infoType %s' . PHP_EOL,
                            $infoTypeStat->getCount(),
                            $infoTypeStat->getInfoType()->getName()
                        );
                    }
                }
                break;
            case JobState::FAILED:
                printf('Job %s had errors:' . PHP_EOL, $job->getName());
                $errors = $job->getErrors();
                foreach ($errors as $error) {
                    var_dump($error->getDetails());
                }
                break;
            case JobState::PENDING:
                printf('Job has not completed. Consider a longer timeout or an asynchronous execution model' . PHP_EOL);
                break;
            default:
                printf('Unexpected job state. Most likely, the job is either running or has not yet started.');
        }
    }

### Python

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import time
    from typing import List
    
    import google.cloud.dlp
    
    
    def deidentify_cloud_storage(
        project: str,
        input_gcs_bucket: str,
        output_gcs_bucket: str,
        info_types: List[str],
        deid_template_id: str,
        structured_deid_template_id: str,
        image_redact_template_id: str,
        dataset_id: str,
        table_id: str,
        timeout: int = 300,
    ) -> None:
        """
        Uses the Data Loss Prevention API to de-identify files in a Google Cloud
        Storage directory.
        Args:
            project: The Google Cloud project id to use as a parent resource.
            input_gcs_bucket: The name of google cloud storage bucket to inspect.
            output_gcs_bucket: The name of google cloud storage bucket where
                de-identified files would be stored.
            info_types: A list of strings representing info types to look for.
                A full list of info type categories can be fetched from the API.
            deid_template_id: The name of the de-identify template for
                unstructured and structured files.
            structured_deid_template_id: The name of the de-identify template
                for structured files.
            image_redact_template_id: The name of the image redaction template
                for images.
            dataset_id: The identifier of the BigQuery dataset where transformation
                details would be stored.
            table_id: The identifier of the BigQuery table where transformation
                details would be stored.
            timeout: The number of seconds to wait for a response from the API.
        """
    
        # Instantiate a client.
        dlp = google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html)()
    
        # Construct the configuration dictionary.
        # Specify the type of info the inspection will look for.
        # See https://cloud.google.com/dlp/docs/infotypes-reference for complete list of info types.
        inspect_config = {"info_types": [{"name": info_type} for info_type in info_types]}
    
        # Construct cloud_storage_options dictionary with the bucket's URL.
        storage_config = {
            "cloud_storage_options": {"file_set": {"url": f"gs://{input_gcs_bucket}"}}
        }
    
        # Specify the big query table to store the transformation details.
        big_query_table = {
            "project_id": project,
            "dataset_id": dataset_id,
            "table_id": table_id,
        }
    
        # Convert the project id into a full resource id.
        parent = f"projects/{project}/locations/global"
    
        # Construct Transformation Configuration with de-identify Templates used
        # for transformation.
        transformation_config = {
            "deidentify_template": f"{parent}/deidentifyTemplates/{deid_template_id}",
            "structured_deidentify_template": f"{parent}/deidentifyTemplates/{structured_deid_template_id}",
            "image_redact_template": f"{parent}/deidentifyTemplates/{image_redact_template_id}",
        }
    
        # Tell the API where to send notification when the job is completed.
        actions = [
            {
                "deidentify": {
                    "cloud_storage_output": f"gs://{output_gcs_bucket}",
                    "transformation_config": transformation_config,
                    "transformation_details_storage_config": {"table": big_query_table},
                    "file_types_to_transform": ["IMAGE", "CSV", "TEXT_FILE"],
                }
            }
        ]
    
        # Construct the job definition.
        inspect_job = {
            "inspect_config": inspect_config,
            "storage_config": storage_config,
            "actions": actions,
        }
    
        # Call the API.
        response = dlp.create_dlp_job(
            request={
                "parent": parent,
                "inspect_job": inspect_job,
            }
        )
    
        job_name = response.name
        print(f"Inspection Job started : {job_name}")
    
        # Waiting for the job to get completed.
        job = dlp.get_dlp_job(request={"name": job_name})
        # Since the sleep time is kept as 30s, number of calls would be timeout/30.
        no_of_attempts = timeout // 30
        while no_of_attempts != 0:
            # Check if the job has completed.
            if job.state == google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpJob](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.DlpJob.html).[JobState](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.DlpJob.JobState.html).DONE:
                break
            if job.state == google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpJob](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.DlpJob.html).[JobState](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.DlpJob.JobState.html).FAILED:
                print("Job Failed, Please check the configuration.")
                break
    
            # Sleep for a short duration before checking the job status again.
            time.sleep(30)
            no_of_attempts -= 1
    
            # Get DLP job status.
            job = dlp.get_dlp_job(request={"name": job_name})
    
        if job.state != google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpJob](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.DlpJob.html).[JobState](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.DlpJob.JobState.html).DONE:
            print(f"Job did not complete within {timeout} minutes.")
            return
    
        # Print out the results.
        print(f"Job name: {job.name}")
        result = job.inspect_details.result
        print(f"Processed Bytes: {result.processed_bytes}")
        if result.info_type_stats:
            for stats in result.info_type_stats:
                print(f"Info type: {stats.info_type.name}")
                print(f"Count: {stats.count}")
        else:
            print("No findings.")
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=clouddatalossprevention). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
