---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/samples/dlp-create-job/
title: Create an inspection job \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:40:56.340063+00:00
---

# Create an inspection job  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/samples/dlp-create-job/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Samples ](https://docs.cloud.google.com/sensitive-data-protection/docs/samples)



#  Create an inspection job Stay organized with collections  Save and categorize content based on your preferences. 

Creates an inspection job with the Cloud Data Loss Prevention API.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Creating and scheduling Sensitive Data Protection inspection jobs](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-job-triggers)



## Code sample

### C#

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using System;
    using System.Linq;
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Dlp.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.html);
    using static Google.Cloud.Dlp.V2.StorageConfig.Types;
    
    public class JobsCreate
    {
        public static DlpJob CreateJob(string projectId, string gcsPath)
        {
            var dlp = [DlpServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html#Google_Cloud_Dlp_V2_DlpServiceClient_Create)();
    
            var storageConfig = new [StorageConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.StorageConfig.html)
            {
                CloudStorageOptions = new [CloudStorageOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CloudStorageOptions.html)
                {
                    FileSet = new CloudStorageOptions.Types.FileSet()
                    {
                        Url = gcsPath
                    }
                },
                TimespanConfig = new TimespanConfig
                {
                    EnableAutoPopulationOfTimespanConfig = true
                }
            };
    
            var inspectConfig = new [InspectConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectConfig.html)
            {
                InfoTypes = { new[] { "EMAIL_ADDRESS", "CREDIT_CARD_NUMBER" }.Select(it => new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html)() { Name = it }) },
                IncludeQuote = true,
                MinLikelihood = [Likelihood](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Likelihood.html).[Unlikely](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Likelihood.html#Google_Cloud_Dlp_V2_Likelihood_Unlikely),
                Limits = new InspectConfig.Types.FindingLimits() { MaxFindingsPerItem = 100 }
            };
    
            var response = dlp.CreateDlpJob(new [CreateDlpJobRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CreateDlpJobRequest.html)
            {
                Parent = new [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)(projectId, "global").ToString(),
                InspectJob = new [InspectJobConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectJobConfig.html)
                {
                    InspectConfig = inspectConfig,
                    StorageConfig = storageConfig,
                }
            });
    
            Console.WriteLine($"Job: {response.Name} status: {response.State}");
    
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
    
    // createJob creates an inspection job
    func createJob(w io.Writer, projectID, gcsPath string, infoTypeNames []string) error {
    	// projectID := "my-project-id"
    	// gcsPath := "gs://" + "your-bucket-name" + "path/to/file.txt";
    	// infoTypeNames := []string{"EMAIL_ADDRESS", "PERSON_NAME", "LOCATION", "PHONE_NUMBER"}
    
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
    
    	// Specify the GCS file to be inspected.
    	storageConfig := &dlppb.StorageConfig{
    		Type: &dlppb.StorageConfig_CloudStorageOptions{
    			CloudStorageOptions: &dlppb.CloudStorageOptions{
    				FileSet: &dlppb.CloudStorageOptions_FileSet{
    					Url: gcsPath,
    				},
    			},
    		},
    
    		// Set autoPopulateTimespan to true to scan only new content.
    		TimespanConfig: &dlppb.StorageConfig_TimespanConfig{
    			EnableAutoPopulationOfTimespanConfig: true,
    		},
    	}
    
    	// Specify the type of info the inspection will look for.
    	// See https://cloud.google.com/dlp/docs/infotypes-reference for complete list of info types.
    	var infoTypes []*dlppb.InfoType
    	for _, c := range infoTypeNames {
    		infoTypes = append(infoTypes, &dlppb.InfoType{Name: c})
    	}
    
    	inspectConfig := &dlppb.InspectConfig{
    		InfoTypes:    infoTypes,
    		IncludeQuote: true,
    
    		// The minimum likelihood required before returning a match:
    		// See: https://cloud.google.com/dlp/docs/likelihood
    		MinLikelihood: dlppb.[Likelihood_UNLIKELY](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2/dlppb.html#cloud_google_com_go_dlp_apiv2_dlppb_Likelihood_LIKELIHOOD_UNSPECIFIED_Likelihood_VERY_UNLIKELY_Likelihood_UNLIKELY_Likelihood_POSSIBLE_Likelihood_LIKELY_Likelihood_VERY_LIKELY),
    
    		// The maximum number of findings to report (0 = server maximum)
    		Limits: &dlppb.InspectConfig_FindingLimits{
    			MaxFindingsPerItem: 100,
    		},
    	}
    
    	// Create and send the request.
    	req := dlppb.CreateDlpJobRequest{
    		Parent: fmt.Sprintf("projects/%s/locations/global", projectID),
    		Job: &dlppb.CreateDlpJobRequest_InspectJob{
    			InspectJob: &dlppb.InspectJobConfig{
    				InspectConfig: inspectConfig,
    				StorageConfig: storageConfig,
    			},
    		},
    	}
    
    	// Send the request.
    	response, err := client.CreateDlpJob(ctx, &req)
    	if err != nil {
    		return err
    	}
    
    	// Print the results.
    	fmt.Fprintf(w, "Created a Dlp Job %v and Status is: %v", response.Name, response.State)
    	return nil
    }
    

### Java

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.dlp.v2.[DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html);
    import com.google.privacy.dlp.v2.[Action](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.html);
    import com.google.privacy.dlp.v2.[CloudStorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CloudStorageOptions.html);
    import com.google.privacy.dlp.v2.[CreateDlpJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CreateDlpJobRequest.html);
    import com.google.privacy.dlp.v2.[DlpJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html);
    import com.google.privacy.dlp.v2.[InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html);
    import com.google.privacy.dlp.v2.[InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html);
    import com.google.privacy.dlp.v2.[InspectJobConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectJobConfig.html);
    import com.google.privacy.dlp.v2.[Likelihood](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Likelihood.html);
    import com.google.privacy.dlp.v2.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html);
    import com.google.privacy.dlp.v2.[StorageConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.StorageConfig.html);
    import com.google.privacy.dlp.v2.[StorageConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.StorageConfig.html).[TimespanConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.StorageConfig.TimespanConfig.html);
    import java.io.IOException;
    import java.util.List;
    import java.util.stream.Collectors;
    import java.util.stream.Stream;
    
    public class JobsCreate {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String gcsPath = "gs://" + "your-bucket-name" + "path/to/file.txt";
        createJobs(projectId, gcsPath);
      }
    
      // Creates a DLP Job
      public static void createJobs(String projectId, String gcsPath) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html) dlpServiceClient = [DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html).create()) {
    
          // Set autoPopulateTimespan to true to scan only new content
          boolean autoPopulateTimespan = true;
          [TimespanConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.StorageConfig.TimespanConfig.html) timespanConfig =
              [TimespanConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.StorageConfig.TimespanConfig.html).newBuilder()
                  .[setEnableAutoPopulationOfTimespanConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.StorageConfig.TimespanConfig.Builder.html#com_google_privacy_dlp_v2_StorageConfig_TimespanConfig_Builder_setEnableAutoPopulationOfTimespanConfig_boolean_)(autoPopulateTimespan)
                  .build();
    
          // Specify the GCS file to be inspected.
          [CloudStorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CloudStorageOptions.html) cloudStorageOptions =
              [CloudStorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CloudStorageOptions.html).newBuilder()
                  .[setFileSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CloudStorageOptions.Builder.html#com_google_privacy_dlp_v2_CloudStorageOptions_Builder_setFileSet_com_google_privacy_dlp_v2_CloudStorageOptions_FileSet_)([CloudStorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CloudStorageOptions.html).FileSet.newBuilder().setUrl(gcsPath))
                  .build();
          [StorageConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.StorageConfig.html) storageConfig =
              [StorageConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.StorageConfig.html).newBuilder()
                  .[setCloudStorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.StorageConfig.Builder.html#com_google_privacy_dlp_v2_StorageConfig_Builder_setCloudStorageOptions_com_google_privacy_dlp_v2_CloudStorageOptions_)(cloudStorageOptions)
                  .[setTimespanConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.StorageConfig.Builder.html#com_google_privacy_dlp_v2_StorageConfig_Builder_setTimespanConfig_com_google_privacy_dlp_v2_StorageConfig_TimespanConfig_)(timespanConfig)
                  .build();
    
          // Specify the type of info the inspection will look for.
          // See https://cloud.google.com/dlp/docs/infotypes-reference for complete list of info types
          List<InfoType> infoTypes =
              Stream.of("EMAIL_ADDRESS", "PERSON_NAME", "LOCATION", "PHONE_NUMBER")
                  .map(it -> [InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html).newBuilder().setName(it).build())
                  .collect(Collectors.toList());
          // The minimum likelihood required before returning a match:
          // See: https://cloud.google.com/dlp/docs/likelihood
          [Likelihood](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Likelihood.html) minLikelihood = [Likelihood](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Likelihood.html).UNLIKELY;
    
          // The maximum number of findings to report (0 = server maximum)
          [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html).[FindingLimits](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.FindingLimits.html) findingLimits =
              [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html).FindingLimits.newBuilder().[setMaxFindingsPerItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.FindingLimits.Builder.html#com_google_privacy_dlp_v2_InspectConfig_FindingLimits_Builder_setMaxFindingsPerItem_int_)(100).build();
    
          [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html) inspectConfig =
              [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html).newBuilder()
                  .addAllInfoTypes(infoTypes)
                  .[setIncludeQuote](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.Builder.html#com_google_privacy_dlp_v2_InspectConfig_Builder_setIncludeQuote_boolean_)(true)
                  .setMinLikelihood(minLikelihood)
                  .[setLimits](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.Builder.html#com_google_privacy_dlp_v2_InspectConfig_Builder_setLimits_com_google_privacy_dlp_v2_InspectConfig_FindingLimits_)(findingLimits)
                  .build();
    
          // Specify the action that is triggered when the job completes.
          [Action](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.html).[PublishSummaryToCscc](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.PublishSummaryToCscc.html) publishSummaryToCscc =
              [Action](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.html).PublishSummaryToCscc.getDefaultInstance();
          [Action](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.html) action = [Action](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.html).newBuilder().[setPublishSummaryToCscc](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.Builder.html#com_google_privacy_dlp_v2_Action_Builder_setPublishSummaryToCscc_com_google_privacy_dlp_v2_Action_PublishSummaryToCscc_)(publishSummaryToCscc).build();
    
          // Configure the inspection job we want the service to perform.
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
    
          // Send the job creation request and process the response.
          [DlpJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html) createdDlpJob = dlpServiceClient.createDlpJob(createDlpJobRequest);
          System.out.println("Job created successfully: " + createdDlpJob.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html#com_google_privacy_dlp_v2_DlpJob_getName__)());
        }
      }
    }

### Node.js

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud Data Loss Prevention library
    const DLP = require('[@google-cloud/dlp](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/overview.html)');
    
    // Initialize google DLP Client
    const dlp = new DLP.[DlpServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/overview.html)();
    
    async function jobsCreate() {
      // Construct cloud storage configuration
      const cloudStorageConfig = {
        cloudStorageOptions: {
          fileSet: {
            url: cloudFileUrl,
          },
        },
        timespanConfig: {
          enableAutoPopulationOfTimespanConfig: true,
        },
      };
    
      // Construct inspect job configuration
      const inspectJob = {
        storageConfig: cloudStorageConfig,
      };
    
      // Construct inspect configuration
      const inspectConfig = {
        infoTypes: [
          {name: 'EMAIL_ADDRESS'},
          {name: 'PERSON_NAME'},
          {name: 'LOCATION'},
          {name: 'PHONE_NUMBER'},
        ],
        includeQuote: true,
        minLikelihood: DLP.protos.google.privacy.dlp.v2.[Likelihood](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.likelihood.html).[LIKELY](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.likelihood.html),
        excludeInfoTypes: false,
      };
    
      // Combine configurations into a request for the service.
      const request = {
        parent: `projects/${projectId}/locations/global`,
        inspectJob: inspectJob,
        inspectConfig: inspectConfig,
      };
    
      // Send the request and receive response from the service
      const [response] = await dlp.createDlpJob(request);
      // Print the results
      console.log(`Job created successfully: ${response.name}`);
    }
    
    jobsCreate();

### PHP

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Dlp\V2\Action;
    use Google\Cloud\Dlp\V2\Action\PublishSummaryToCscc;
    use Google\Cloud\Dlp\V2\Client\DlpServiceClient;
    use Google\Cloud\Dlp\V2\CloudStorageOptions;
    use Google\Cloud\Dlp\V2\CloudStorageOptions\FileSet;
    use Google\Cloud\Dlp\V2\CreateDlpJobRequest;
    use Google\Cloud\Dlp\V2\InfoType;
    use Google\Cloud\Dlp\V2\InspectConfig;
    use Google\Cloud\Dlp\V2\InspectConfig\FindingLimits;
    use Google\Cloud\Dlp\V2\InspectJobConfig;
    use Google\Cloud\Dlp\V2\Likelihood;
    use Google\Cloud\Dlp\V2\StorageConfig;
    use Google\Cloud\Dlp\V2\StorageConfig\TimespanConfig;
    
    /**
     * Creates an inspection job with the Cloud Data Loss Prevention API.
     *
     * @param string $callingProjectId  The project ID to run the API call under.
     * @param string $gcsPath           GCS file to be inspected. Example : gs://GOOGLE_STORAGE_BUCKET_NAME/dlp_sample.csv
     */
    function create_job(
        string $callingProjectId,
        string $gcsPath
    ): void {
        // Instantiate a client.
        $dlp = new DlpServiceClient();
    
        // Set autoPopulateTimespan to true to scan only new content.
        $timespanConfig = (new TimespanConfig())
            ->setEnableAutoPopulationOfTimespanConfig(true);
    
        // Specify the GCS file to be inspected.
        $cloudStorageOptions = (new CloudStorageOptions())
            ->setFileSet((new FileSet())
                ->setUrl($gcsPath));
        $storageConfig = (new StorageConfig())
            ->setCloudStorageOptions(($cloudStorageOptions))
            ->setTimespanConfig($timespanConfig);
    
        // ----- Construct inspection config -----
        $emailAddressInfoType = (new InfoType())
            ->setName('EMAIL_ADDRESS');
        $personNameInfoType = (new InfoType())
            ->setName('PERSON_NAME');
        $locationInfoType = (new InfoType())
            ->setName('LOCATION');
        $phoneNumberInfoType = (new InfoType())
            ->setName('PHONE_NUMBER');
        $infoTypes = [$emailAddressInfoType, $personNameInfoType, $locationInfoType, $phoneNumberInfoType];
    
        // Whether to include the matching string in the response.
        $includeQuote = true;
        // The minimum likelihood required before returning a match.
        $minLikelihood = likelihood::LIKELIHOOD_UNSPECIFIED;
    
        // The maximum number of findings to report (0 = server maximum).
        $limits = (new FindingLimits())
            ->setMaxFindingsPerRequest(100);
    
        // Create the Inspect configuration object.
        $inspectConfig = (new InspectConfig())
            ->setMinLikelihood($minLikelihood)
            ->setLimits($limits)
            ->setInfoTypes($infoTypes)
            ->setIncludeQuote($includeQuote);
    
        // Specify the action that is triggered when the job completes.
        $action = (new Action())
            ->setPublishSummaryToCscc(new PublishSummaryToCscc());
    
        // Configure the inspection job we want the service to perform.
        $inspectJobConfig = (new InspectJobConfig())
            ->setInspectConfig($inspectConfig)
            ->setStorageConfig($storageConfig)
            ->setActions([$action]);
    
        // Send the job creation request and process the response.
        $parent = "projects/$callingProjectId/locations/global";
        $createDlpJobRequest = (new CreateDlpJobRequest())
            ->setParent($parent)
            ->setInspectJob($inspectJobConfig);
        $job = $dlp->createDlpJob($createDlpJobRequest);
    
        // Print results.
        printf($job->getName());
    }

### Python

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import google.cloud.dlp
    
    
    def create_dlp_job(
        project: str,
        bucket: str,
        info_types: list[str],
        job_id: str = None,
        max_findings: int = 100,
        auto_populate_timespan: bool = True,
    ) -> None:
        """Uses the Data Loss Prevention API to create a DLP job.
        Args:
            project: The project id to use as a parent resource.
            bucket: The name of the GCS bucket to scan. This sample scans all
                files in the bucket.
            info_types: A list of strings representing info types to look for.
                A full list of info type categories can be fetched from the API.
            job_id: The id of the job. If omitted, an id will be randomly generated.
            max_findings: The maximum number of findings to report; 0 = no maximum.
            auto_populate_timespan: Automatically populates time span config start
                and end times in order to scan new content only.
        """
    
        # Instantiate a client.
        dlp = google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html)()
    
        # Convert the project id into a full resource id.
        parent = f"projects/{project}"
    
        # Prepare info_types by converting the list of strings into a list of
        # dictionaries (protos are also accepted).
        info_types = [{"name": info_type} for info_type in info_types]
    
        # Construct the configuration dictionary. Keys which are None may
        # optionally be omitted entirely.
        inspect_config = {
            "info_types": info_types,
            "min_likelihood": google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[Likelihood](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.Likelihood.html).UNLIKELY,
            "limits": {"max_findings_per_request": max_findings},
            "include_quote": True,
        }
    
        # Construct a cloud_storage_options dictionary with the bucket's URL.
        url = f"gs://{bucket}/*"
        storage_config = {
            "cloud_storage_options": {"file_set": {"url": url}},
            # Time-based configuration for each storage object.
            "timespan_config": {
                # Auto-populate start and end times in order to scan new objects
                # only.
                "enable_auto_population_of_timespan_config": auto_populate_timespan
            },
        }
    
        # Construct the job definition.
        job = {"inspect_config": inspect_config, "storage_config": storage_config}
    
        # Call the API.
        response = dlp.create_dlp_job(
            request={"parent": parent, "inspect_job": job, "job_id": job_id}
        )
    
        # Print out the result.
        print(f"Job : {response.name} status: {response.state}")
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=clouddatalossprevention). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
