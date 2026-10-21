---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/samples/dlp-create-trigger/
title: Create a job trigger \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:41:01.342108+00:00
---

# Create a job trigger  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/samples/dlp-create-trigger/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Samples ](https://docs.cloud.google.com/sensitive-data-protection/docs/samples)



#  Create a job trigger Stay organized with collections  Save and categorize content based on your preferences. 

Creates a scheduled Cloud Data Loss Prevention API job trigger.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Creating and scheduling Sensitive Data Protection inspection jobs](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-job-triggers)



## Code sample

### C#

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Dlp.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.html);
    using System;
    using System.Collections.Generic;
    using static Google.Cloud.Dlp.V2.CloudStorageOptions.Types;
    using static Google.Cloud.Dlp.V2.InspectConfig.Types;
    using static Google.Cloud.Dlp.V2.JobTrigger.Types;
    using static Google.Cloud.Dlp.V2.StorageConfig.Types;
    
    public class TriggersCreate
    {
        public static JobTrigger Create(
            string projectId,
            string bucketName,
            [Likelihood](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Likelihood.html) minLikelihood,
            int maxFindings,
            bool autoPopulateTimespan,
            int scanPeriod,
            IEnumerable<InfoType> infoTypes,
            string triggerId,
            string displayName,
            string description)
        {
            var dlp = [DlpServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html#Google_Cloud_Dlp_V2_DlpServiceClient_Create)();
    
            var jobConfig = new [InspectJobConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectJobConfig.html)
            {
                InspectConfig = new [InspectConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectConfig.html)
                {
                    MinLikelihood = minLikelihood,
                    Limits = new [FindingLimits](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectConfig.Types.FindingLimits.html)
                    {
                        MaxFindingsPerRequest = maxFindings
                    },
                    InfoTypes = { infoTypes }
                },
                StorageConfig = new [StorageConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.StorageConfig.html)
                {
                    CloudStorageOptions = new [CloudStorageOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CloudStorageOptions.html)
                    {
                        FileSet = new FileSet
                        {
                            Url = $"gs://{bucketName}/*"
                        }
                    },
                    TimespanConfig = new TimespanConfig
                    {
                        EnableAutoPopulationOfTimespanConfig = autoPopulateTimespan
                    }
                }
            };
    
            var jobTrigger = new [JobTrigger](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.JobTrigger.html)
            {
                Triggers =
                {
                    new [Trigger](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.JobTrigger.Types.Trigger.html)
                    {
                        Schedule = new [Schedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Schedule.html)
                        {
                            RecurrencePeriodDuration = new Google.Protobuf.WellKnownTypes.Duration
                            {
                                Seconds = scanPeriod * 60 * 60 * 24
                            }
                        }
                    }
                },
                InspectJob = jobConfig,
                Status = Status.[Healthy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.JobTrigger.Types.Status.html#Google_Cloud_Dlp_V2_JobTrigger_Types_Status_Healthy),
                DisplayName = displayName,
                Description = description
            };
    
            var response = dlp.CreateJobTrigger(
                new [CreateJobTriggerRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CreateJobTriggerRequest.html)
                {
                    Parent = new [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)(projectId, "global").ToString(),
                    JobTrigger = jobTrigger,
                    TriggerId = triggerId
                });
    
            Console.WriteLine($"Successfully created trigger {response.Name}");
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
    	"github.com/golang/protobuf/ptypes/duration"
    )
    
    // createTrigger creates a trigger with the given configuration.
    func createTrigger(w io.Writer, projectID string, triggerID, displayName, description, bucketName string, infoTypeNames []string) error {
    	// projectID := "my-project-id"
    	// triggerID := "my-trigger"
    	// displayName := "My Trigger"
    	// description := "My trigger description"
    	// bucketName := "my-bucket"
    	// infoTypeNames := []string{"US_SOCIAL_SECURITY_NUMBER"}
    
    	ctx := context.Background()
    
    	client, err := dlp.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2.html#cloud_google_com_go_dlp_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("dlp.NewClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2.html#cloud_google_com_go_dlp_apiv2_Client_Close)()
    
    	// Convert the info type strings to a list of InfoTypes.
    	var infoTypes []*dlppb.InfoType
    	for _, it := range infoTypeNames {
    		infoTypes = append(infoTypes, &dlppb.InfoType{Name: it})
    	}
    
    	// Create a configured request.
    	req := &dlppb.CreateJobTriggerRequest{
    		Parent:    fmt.Sprintf("projects/%s/locations/global", projectID),
    		TriggerId: triggerID,
    		JobTrigger: &dlppb.JobTrigger{
    			DisplayName: displayName,
    			Description: description,
    			Status:      dlppb.[JobTrigger_HEALTHY](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2/dlppb.html#cloud_google_com_go_dlp_apiv2_dlppb_JobTrigger_STATUS_UNSPECIFIED_JobTrigger_HEALTHY_JobTrigger_PAUSED_JobTrigger_CANCELLED),
    			// Triggers control when the job will start.
    			Triggers: []*dlppb.JobTrigger_Trigger{
    				{
    					Trigger: &dlppb.JobTrigger_Trigger_Schedule{
    						Schedule: &dlppb.Schedule{
    							Option: &dlppb.Schedule_RecurrencePeriodDuration{
    								RecurrencePeriodDuration: &duration.Duration{
    									Seconds: 10 * 60 * 60 * 24, // 10 days in seconds.
    								},
    							},
    						},
    					},
    				},
    			},
    			// Job configures the job to run when the trigger runs.
    			Job: &dlppb.JobTrigger_InspectJob{
    				InspectJob: &dlppb.InspectJobConfig{
    					InspectConfig: &dlppb.InspectConfig{
    						InfoTypes:     infoTypes,
    						MinLikelihood: dlppb.[Likelihood_POSSIBLE](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2/dlppb.html#cloud_google_com_go_dlp_apiv2_dlppb_Likelihood_LIKELIHOOD_UNSPECIFIED_Likelihood_VERY_UNLIKELY_Likelihood_UNLIKELY_Likelihood_POSSIBLE_Likelihood_LIKELY_Likelihood_VERY_LIKELY),
    						Limits: &dlppb.InspectConfig_FindingLimits{
    							MaxFindingsPerRequest: 10,
    						},
    					},
    					StorageConfig: &dlppb.StorageConfig{
    						Type: &dlppb.StorageConfig_CloudStorageOptions{
    							CloudStorageOptions: &dlppb.CloudStorageOptions{
    								FileSet: &dlppb.CloudStorageOptions_FileSet{
    									Url: "gs://" + bucketName + "/*",
    								},
    							},
    						},
    						// Time-based configuration for each storage object. See more at
    						// https://cloud.google.com/dlp/docs/reference/rest/v2/InspectJobConfig#TimespanConfig
    						TimespanConfig: &dlppb.StorageConfig_TimespanConfig{
    							// Auto-populate start and end times in order to scan new objects only.
    							EnableAutoPopulationOfTimespanConfig: true,
    						},
    					},
    				},
    			},
    		},
    	}
    
    	// Send the request.
    	resp, err := client.CreateJobTrigger(ctx, req)
    	if err != nil {
    		return fmt.Errorf("CreateJobTrigger: %w", err)
    	}
    	fmt.Fprintf(w, "Successfully created trigger: %v", resp.GetName())
    	return nil
    }
    

### Java

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.dlp.v2.[DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html);
    import com.google.privacy.dlp.v2.[CloudStorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CloudStorageOptions.html);
    import com.google.privacy.dlp.v2.[CreateJobTriggerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CreateJobTriggerRequest.html);
    import com.google.privacy.dlp.v2.[InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html);
    import com.google.privacy.dlp.v2.[InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html);
    import com.google.privacy.dlp.v2.[InspectJobConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectJobConfig.html);
    import com.google.privacy.dlp.v2.[JobTrigger](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.JobTrigger.html);
    import com.google.privacy.dlp.v2.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html);
    import com.google.privacy.dlp.v2.[Schedule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Schedule.html);
    import com.google.privacy.dlp.v2.[StorageConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.StorageConfig.html);
    import com.google.privacy.dlp.v2.[StorageConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.StorageConfig.html).[TimespanConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.StorageConfig.TimespanConfig.html);
    import com.google.protobuf.[Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html);
    import java.io.IOException;
    import java.util.List;
    import java.util.stream.Collectors;
    import java.util.stream.Stream;
    
    public class TriggersCreate {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String gcsPath = "gs://" + "your-bucket-name" + "path/to/file.txt";
        createTrigger(projectId, gcsPath);
      }
    
      public static void createTrigger(String projectId, String gcsPath) throws IOException {
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
              Stream.of("PHONE_NUMBER", "EMAIL_ADDRESS", "CREDIT_CARD_NUMBER")
                  .map(it -> [InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html).newBuilder().setName(it).build())
                  .collect(Collectors.toList());
    
          [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html) inspectConfig = [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html).newBuilder().addAllInfoTypes(infoTypes).build();
    
          // Configure the inspection job we want the service to perform.
          [InspectJobConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectJobConfig.html) inspectJobConfig =
              [InspectJobConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectJobConfig.html).newBuilder()
                  .setInspectConfig(inspectConfig)
                  .[setStorageConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectJobConfig.Builder.html#com_google_privacy_dlp_v2_InspectJobConfig_Builder_setStorageConfig_com_google_privacy_dlp_v2_StorageConfig_)(storageConfig)
                  .build();
    
          // Set scanPeriod to the number of days between scans (minimum: 1 day)
          int scanPeriod = 1;
    
          // Optionally set a display name of max 100 chars and a description of max 250 chars
          String displayName = "Daily Scan";
          String description = "A daily inspection for personally identifiable information.";
    
          // Schedule scan of GCS bucket every scanPeriod number of days (minimum = 1 day)
          [Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html) duration = [Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html).newBuilder().setSeconds(scanPeriod * 24 * 3600).build();
          [Schedule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Schedule.html) schedule = [Schedule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Schedule.html).newBuilder().[setRecurrencePeriodDuration](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Schedule.Builder.html#com_google_privacy_dlp_v2_Schedule_Builder_setRecurrencePeriodDuration_com_google_protobuf_Duration_)(duration).build();
          [JobTrigger](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.JobTrigger.html).[Trigger](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.JobTrigger.Trigger.html) trigger = [JobTrigger](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.JobTrigger.html).Trigger.newBuilder().[setSchedule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.JobTrigger.Trigger.Builder.html#com_google_privacy_dlp_v2_JobTrigger_Trigger_Builder_setSchedule_com_google_privacy_dlp_v2_Schedule_)(schedule).build();
          [JobTrigger](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.JobTrigger.html) jobTrigger =
              [JobTrigger](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.JobTrigger.html).newBuilder()
                  .setInspectJob(inspectJobConfig)
                  .setDisplayName(displayName)
                  .setDescription(description)
                  .setStatus([JobTrigger](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.JobTrigger.html).Status.HEALTHY)
                  .[addTriggers](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.JobTrigger.Builder.html#com_google_privacy_dlp_v2_JobTrigger_Builder_addTriggers_com_google_privacy_dlp_v2_JobTrigger_Trigger_)(trigger)
                  .build();
    
          // Create scan request to be sent by client
          [CreateJobTriggerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CreateJobTriggerRequest.html) createJobTriggerRequest =
              [CreateJobTriggerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CreateJobTriggerRequest.html).newBuilder()
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html).of(projectId, "global").toString())
                  .setJobTrigger(jobTrigger)
                  .build();
    
          // Send the scan request and process the response
          [JobTrigger](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.JobTrigger.html) createdJobTrigger = dlpServiceClient.createJobTrigger(createJobTriggerRequest);
    
          System.out.println("Created Trigger: " + createdJobTrigger.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.JobTrigger.html#com_google_privacy_dlp_v2_JobTrigger_getName__)());
          System.out.println("Display Name: " + createdJobTrigger.[getDisplayName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.JobTrigger.html#com_google_privacy_dlp_v2_JobTrigger_getDisplayName__)());
          System.out.println("Description: " + createdJobTrigger.[getDescription](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.JobTrigger.html#com_google_privacy_dlp_v2_JobTrigger_getDescription__)());
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
    
    // The project ID to run the API call under
    // const projectId = 'my-project';
    
    // (Optional) The name of the trigger to be created.
    // const triggerId = 'my-trigger';
    
    // (Optional) A display name for the trigger to be created
    // const displayName = 'My Trigger';
    
    // (Optional) A description for the trigger to be created
    // const description = "This is a sample trigger.";
    
    // The name of the bucket to scan.
    // const bucketName = 'YOUR-BUCKET';
    
    // Limit scan to new content only.
    // const autoPopulateTimespan = true;
    
    // How often to wait between scans, in days (minimum = 1 day)
    // const scanPeriod = 1;
    
    // The infoTypes of information to match
    // const infoTypes = [{ name: 'PHONE_NUMBER' }, { name: 'EMAIL_ADDRESS' }, { name: 'CREDIT_CARD_NUMBER' }];
    
    // The minimum likelihood required before returning a match
    // const minLikelihood = 'LIKELIHOOD_UNSPECIFIED';
    
    // The maximum number of findings to report per request (0 = server maximum)
    // const maxFindings = 0;
    
    async function createTrigger() {
      // Get reference to the bucket to be inspected
      const storageItem = {
        cloudStorageOptions: {
          fileSet: {url: `gs://${bucketName}/*`},
        },
        timeSpanConfig: {
          enableAutoPopulationOfTimespanConfig: autoPopulateTimespan,
        },
      };
    
      // Construct job to be triggered
      const job = {
        inspectConfig: {
          infoTypes: infoTypes,
          minLikelihood: minLikelihood,
          limits: {
            maxFindingsPerRequest: maxFindings,
          },
        },
        storageConfig: storageItem,
      };
    
      // Construct trigger creation request
      const request = {
        parent: `projects/${projectId}/locations/global`,
        jobTrigger: {
          inspectJob: job,
          displayName: displayName,
          description: description,
          triggers: [
            {
              schedule: {
                recurrencePeriodDuration: {
                  seconds: scanPeriod * 60 * 60 * 24, // Trigger the scan daily
                },
              },
            },
          ],
          status: '[HEALTHY](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.jobtrigger.status.html)',
        },
        triggerId: triggerId,
      };
    
      // Run trigger creation request
      const [trigger] = await dlp.createJobTrigger(request);
      console.log(`Successfully created trigger ${[trigger](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.jobtrigger.trigger.html).name}.`);
    }
    
    createTrigger();

### PHP

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Dlp\V2\Client\DlpServiceClient;
    use Google\Cloud\Dlp\V2\CloudStorageOptions;
    use Google\Cloud\Dlp\V2\CloudStorageOptions\FileSet;
    use Google\Cloud\Dlp\V2\CreateJobTriggerRequest;
    use Google\Cloud\Dlp\V2\InfoType;
    use Google\Cloud\Dlp\V2\InspectConfig;
    use Google\Cloud\Dlp\V2\InspectConfig\FindingLimits;
    use Google\Cloud\Dlp\V2\InspectJobConfig;
    use Google\Cloud\Dlp\V2\JobTrigger;
    use Google\Cloud\Dlp\V2\JobTrigger\Status;
    use Google\Cloud\Dlp\V2\JobTrigger\Trigger;
    use Google\Cloud\Dlp\V2\Likelihood;
    use Google\Cloud\Dlp\V2\Schedule;
    use Google\Cloud\Dlp\V2\StorageConfig;
    use Google\Cloud\Dlp\V2\StorageConfig\TimespanConfig;
    use Google\Protobuf\Duration;
    
    /**
     * Create a Data Loss Prevention API job trigger.
     *
     * @param string $callingProjectId     The project ID to run the API call under
     * @param string $bucketName           The name of the bucket to scan
     * @param string $triggerId            (Optional) The name of the trigger to be created
     * @param string $displayName          (Optional) The human-readable name to give the trigger
     * @param string $description          (Optional) A description for the trigger to be created
     * @param int    $scanPeriod           (Optional) How often to wait between scans, in days (minimum = 1 day)
     * @param bool   $autoPopulateTimespan (Optional) Automatically limit scan to new content only
     * @param int    $maxFindings          (Optional) The maximum number of findings to report per request (0 = server maximum)
     */
    function create_trigger(
        string $callingProjectId,
        string $bucketName,
        string $triggerId,
        string $displayName,
        string $description,
        int $scanPeriod,
        bool $autoPopulateTimespan,
        int $maxFindings
    ): void {
        // Instantiate a client.
        $dlp = new DlpServiceClient();
    
        // ----- Construct job config -----
        // The infoTypes of information to match
        $personNameInfoType = (new InfoType())
            ->setName('PERSON_NAME');
        $phoneNumberInfoType = (new InfoType())
            ->setName('PHONE_NUMBER');
        $infoTypes = [$personNameInfoType, $phoneNumberInfoType];
    
        // The minimum likelihood required before returning a match
        $minLikelihood = likelihood::LIKELIHOOD_UNSPECIFIED;
    
        // Specify finding limits
        $limits = (new FindingLimits())
            ->setMaxFindingsPerRequest($maxFindings);
    
        // Create the inspectConfig object
        $inspectConfig = (new InspectConfig())
            ->setMinLikelihood($minLikelihood)
            ->setLimits($limits)
            ->setInfoTypes($infoTypes);
    
        // Create triggers
        $duration = (new Duration())
            ->setSeconds($scanPeriod * 60 * 60 * 24);
    
        $schedule = (new Schedule())
            ->setRecurrencePeriodDuration($duration);
    
        $triggerObject = (new Trigger())
            ->setSchedule($schedule);
    
        // Create the storageConfig object
        $fileSet = (new FileSet())
            ->setUrl('gs://' . $bucketName . '/*');
    
        $storageOptions = (new CloudStorageOptions())
            ->setFileSet($fileSet);
    
        // Auto-populate start and end times in order to scan new objects only.
        $timespanConfig = (new TimespanConfig())
            ->setEnableAutoPopulationOfTimespanConfig($autoPopulateTimespan);
    
        $storageConfig = (new StorageConfig())
            ->setCloudStorageOptions($storageOptions)
            ->setTimespanConfig($timespanConfig);
    
        // Construct the jobConfig object
        $jobConfig = (new InspectJobConfig())
            ->setInspectConfig($inspectConfig)
            ->setStorageConfig($storageConfig);
    
        // ----- Construct trigger object -----
        $jobTriggerObject = (new JobTrigger())
            ->setTriggers([$triggerObject])
            ->setInspectJob($jobConfig)
            ->setStatus(Status::HEALTHY)
            ->setDisplayName($displayName)
            ->setDescription($description);
    
        // Run trigger creation request
        $parent = $dlp->locationName($callingProjectId, 'global');
        $createJobTriggerRequest = (new CreateJobTriggerRequest())
            ->setParent($parent)
            ->setJobTrigger($jobTriggerObject)
            ->setTriggerId($triggerId);
        $trigger = $dlp->createJobTrigger($createJobTriggerRequest);
    
        // Print results
        printf('Successfully created trigger %s' . PHP_EOL, $trigger->getName());
    }

### Python

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from typing import Optional
    
    import google.cloud.dlp
    
    
    def create_trigger(
        project: str,
        bucket: str,
        scan_period_days: int,
        info_types: List[str],
        trigger_id: Optional[str] = None,
        display_name: Optional[str] = None,
        description: Optional[str] = None,
        min_likelihood: Optional[int] = None,
        max_findings: Optional[int] = None,
        auto_populate_timespan: Optional[bool] = False,
    ) -> None:
        """Creates a scheduled Data Loss Prevention API inspect_content trigger.
        Args:
            project: The Google Cloud project id to use as a parent resource.
            bucket: The name of the GCS bucket to scan. This sample scans all
                files in the bucket using a wildcard.
            scan_period_days: How often to repeat the scan, in days.
                The minimum is 1 day.
            info_types: A list of strings representing info types to look for.
                A full list of info type categories can be fetched from the API.
            trigger_id: The id of the trigger. If omitted, an id will be randomly
                generated.
            display_name: The optional display name of the trigger.
            description: The optional description of the trigger.
            min_likelihood: A string representing the minimum likelihood threshold
                that constitutes a match. One of: 'LIKELIHOOD_UNSPECIFIED',
                'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE', 'LIKELY', 'VERY_LIKELY'.
            max_findings: The maximum number of findings to report; 0 = no maximum.
            auto_populate_timespan: Automatically populates time span config start
                and end times in order to scan new content only.
        Returns:
            None; the response from the API is printed to the terminal.
        """
    
        # Instantiate a client.
        dlp = google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html)()
    
        # Prepare info_types by converting the list of strings into a list of
        # dictionaries (protos are also accepted).
        info_types = [{"name": info_type} for info_type in info_types]
    
        # Construct the configuration dictionary. Keys which are None may
        # optionally be omitted entirely.
        inspect_config = {
            "info_types": info_types,
            "min_likelihood": min_likelihood,
            "limits": {"max_findings_per_request": max_findings},
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
    
        # Construct the schedule definition:
        schedule = {
            "recurrence_period_duration": {"seconds": scan_period_days * 60 * 60 * 24}
        }
    
        # Construct the trigger definition.
        job_trigger = {
            "inspect_job": job,
            "display_name": display_name,
            "description": description,
            "triggers": [{"schedule": schedule}],
            "status": google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[JobTrigger](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.JobTrigger.html).Status.HEALTHY,
        }
    
        # Convert the project id into a full resource id.
        parent = f"projects/{project}"
    
        # Call the API.
        response = dlp.[create_job_trigger](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceClient_create_job_trigger)(
            request={"parent": parent, "job_trigger": job_trigger, "trigger_id": trigger_id}
        )
    
        print(f"Successfully created trigger {response.name}")
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=clouddatalossprevention). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
