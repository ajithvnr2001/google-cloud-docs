---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/samples/dlp-update-trigger/
title: Update a job trigger \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:24:45.072592+00:00
---

# Update a job trigger  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/samples/dlp-update-trigger/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Samples ](https://docs.cloud.google.com/sensitive-data-protection/docs/samples)



#  Update a job trigger Stay organized with collections  Save and categorize content based on your preferences. 

This sample updates the infoTypes and minimum likelihood of a job trigger.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Creating and scheduling Sensitive Data Protection inspection jobs](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-job-triggers)



## Code sample

### C#

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Dlp.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.html);
    using [Google.Protobuf.WellKnownTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.html);
    using System;
    using System.Collections.Generic;
    
    public class TriggersUpdate
    {
        public static JobTrigger UpdateJob(
            string projectId,
            string triggerId,
            IEnumerable<InfoType> infoTypes = null,
            [Likelihood](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Likelihood.html) minLikelihood = [Likelihood](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Likelihood.html).[Likely](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Likelihood.html#Google_Cloud_Dlp_V2_Likelihood_Likely))
        {
            // Instantiate the client.
            var dlp = [DlpServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html#Google_Cloud_Dlp_V2_DlpServiceClient_Create)();
    
            // Construct the update job trigger request object by providing the trigger name,
            // job trigger object which will specify the type of info to be inspected and
            // update mask object which specifies the field to be updated.
            // Refer to https://cloud.google.com/dlp/docs/reference/rest/v2/Container for specifying the paths in container object.
            var request = new [UpdateJobTriggerRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.UpdateJobTriggerRequest.html)
            {
                JobTriggerName = new [JobTriggerName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.JobTriggerName.html)(projectId, triggerId),
                JobTrigger = new [JobTrigger](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.JobTrigger.html)
                {
                    InspectJob = new [InspectJobConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectJobConfig.html)
                    {
                        InspectConfig = new [InspectConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectConfig.html)
                        {
                            InfoTypes =
                            {
                                infoTypes ?? new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html)[]
                                {
                                    new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html) { Name = "US_INDIVIDUAL_TAXPAYER_IDENTIFICATION_NUMBER" }
                                }
                            },
                            MinLikelihood = minLikelihood
                        }
                    }
                },
                // Specify fields of the jobTrigger resource to be updated when the job trigger is modified.
                // Refer https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask for constructing the field mask paths.
                UpdateMask = new [FieldMask](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)
                {
                    Paths =
                    {
                        "inspect_job.inspect_config.info_types",
                        "inspect_job.inspect_config.min_likelihood"
                    }
                }
            };
    
            // Call the API.
            [JobTrigger](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.JobTrigger.html) response = dlp.UpdateJobTrigger(request);
    
            // Inspect the result.
            Console.WriteLine($"Job Trigger Name: {response.[Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.JobTrigger.html#Google_Cloud_Dlp_V2_JobTrigger_Name)}");
            Console.WriteLine($"InfoType updated: {response.[InspectJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.JobTrigger.html#Google_Cloud_Dlp_V2_JobTrigger_InspectJob).[InspectConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectConfig.html).InfoTypes[0]}");
            Console.WriteLine($"Likelihood updated: {response.[InspectJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.JobTrigger.html#Google_Cloud_Dlp_V2_JobTrigger_InspectJob).[InspectConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectConfig.html).MinLikelihood}");
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
    
    // updateTrigger updates an existing job trigger in Google Cloud Data Loss Prevention (DLP).
    // It modifies the configuration of the specified job trigger with the provided updated settings.
    func updateTrigger(w io.Writer, jobTriggerName string) error {
    	// jobTriggerName := "your-job-trigger-name" (projects/<projectID>/locations/global/jobTriggers/my-trigger)
    
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
    
    	// Specify the type of info the inspection will look for.
    	// See https://cloud.google.com/dlp/docs/infotypes-reference for complete list of info types
    	infoType := &dlppb.InfoType{
    		Name: "PERSON_NAME",
    	}
    
    	// Specify the inspectConfig that represents the configuration settings for inspecting sensitive data in
    	// DLP API. It includes detection types, custom info types, inspection methods, and actions
    	// to be taken on detection.
    	inspectConfig := &dlppb.InspectConfig{
    		InfoTypes: []*dlppb.InfoType{
    			infoType,
    		},
    		MinLikelihood: dlppb.[Likelihood_LIKELY](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2/dlppb.html#cloud_google_com_go_dlp_apiv2_dlppb_Likelihood_LIKELIHOOD_UNSPECIFIED_Likelihood_VERY_UNLIKELY_Likelihood_UNLIKELY_Likelihood_POSSIBLE_Likelihood_LIKELY_Likelihood_VERY_LIKELY),
    	}
    
    	// Configure the inspection job we want the service to perform.
    	inspectJobConfig := &dlppb.InspectJobConfig{
    		InspectConfig: inspectConfig,
    	}
    
    	// Specify the jobTrigger that represents a DLP job trigger configuration.
    	// It defines the conditions, actions, and schedule for executing inspections
    	// on sensitive data in the specified data storage.
    	jobTrigger := &dlppb.JobTrigger{
    		Job: &dlppb.JobTrigger_InspectJob{
    			InspectJob: inspectJobConfig,
    		},
    	}
    
    	// fieldMask represents a set of fields to be included in an update operation.
    	// It is used to specify which fields of a resource should be updated.
    	updateMask := &fieldmaskpb.FieldMask{
    		Paths: []string{"inspect_job.inspect_config.info_types", "inspect_job.inspect_config.min_likelihood"},
    	}
    
    	// Combine configurations into a request for the service.
    	req := &dlppb.UpdateJobTriggerRequest{
    		Name:       jobTriggerName,
    		JobTrigger: jobTrigger,
    		UpdateMask: updateMask,
    	}
    
    	// Send the scan request and process the response
    	resp, err := client.UpdateJobTrigger(ctx, req)
    	if err != nil {
    		return err
    	}
    
    	// Print the result.
    	fmt.Fprintf(w, "Successfully Updated trigger: %v", resp)
    	return nil
    
    }
    

### Java

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.dlp.v2.[DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html);
    import com.google.privacy.dlp.v2.[InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html);
    import com.google.privacy.dlp.v2.[InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html);
    import com.google.privacy.dlp.v2.[InspectJobConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectJobConfig.html);
    import com.google.privacy.dlp.v2.[JobTrigger](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.JobTrigger.html);
    import com.google.privacy.dlp.v2.[JobTriggerName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.JobTriggerName.html);
    import com.google.privacy.dlp.v2.[Likelihood](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Likelihood.html);
    import com.google.privacy.dlp.v2.[UpdateJobTriggerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.UpdateJobTriggerRequest.html);
    import com.google.protobuf.[FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html);
    import java.io.IOException;
    
    public class TriggersPatch {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
    
        // The Google Cloud project id to use as a parent resource.
        String projectId = "your-project-id";
        // The name of the job trigger to be updated.
        String jobTriggerName = "your-job-trigger-name";
        patchTrigger(projectId, jobTriggerName);
      }
    
      // Uses the Data Loss Prevention API to update an existing job trigger.
      public static void patchTrigger(String projectId, String jobTriggerName) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html) dlpServiceClient = [DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html).create()) {
    
          // Specify the type of info the inspection will look for.
          // See https://cloud.google.com/dlp/docs/infotypes-reference for complete list of info types
          [InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html) infoType = [InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html).newBuilder().setName("PERSON_NAME").build();
    
          [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html) inspectConfig = [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html).newBuilder()
                  .addInfoTypes(infoType)
                  .setMinLikelihood([Likelihood](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Likelihood.html).LIKELY)
                  .build();
    
          [InspectJobConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectJobConfig.html) inspectJobConfig = [InspectJobConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectJobConfig.html).newBuilder()
                  .setInspectConfig(inspectConfig)
                  .build();
    
          [JobTrigger](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.JobTrigger.html) jobTrigger = [JobTrigger](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.JobTrigger.html).newBuilder()
                  .setInspectJob(inspectJobConfig)
                  .build();
    
          // Specify fields of the jobTrigger resource to be updated when the job trigger is modified.
          // Refer https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask for constructing the field mask paths.
          [FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html) fieldMask = [FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html).newBuilder()
                  .[addPaths](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.Builder.html#com_google_protobuf_FieldMask_Builder_addPaths_java_lang_String_)("inspect_job.inspect_config.info_types")
                  .[addPaths](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.Builder.html#com_google_protobuf_FieldMask_Builder_addPaths_java_lang_String_)("inspect_job.inspect_config.min_likelihood")
                  .build();
    
          // Update the job trigger with the new configuration.
          [UpdateJobTriggerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.UpdateJobTriggerRequest.html) updateJobTriggerRequest = [UpdateJobTriggerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.UpdateJobTriggerRequest.html).newBuilder()
                  .setName([JobTriggerName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.JobTriggerName.html).of(projectId, jobTriggerName).toString())
                  .setJobTrigger(jobTrigger)
                  .setUpdateMask(fieldMask)
                  .build();
    
          // Call the API to update the job trigger.
          [JobTrigger](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.JobTrigger.html) updatedJobTrigger = dlpServiceClient.updateJobTrigger(updateJobTriggerRequest);
    
          System.out.println("Job Trigger Name: " + updatedJobTrigger.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.JobTrigger.html#com_google_privacy_dlp_v2_JobTrigger_getName__)());
          System.out.println(
              "InfoType updated: "
                  + updatedJobTrigger.[getInspectJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.JobTrigger.html#com_google_privacy_dlp_v2_JobTrigger_getInspectJob__)().getInspectConfig().getInfoTypes(0).getName());
          System.out.println(
              "Likelihood updated: "
                  + updatedJobTrigger.[getInspectJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.JobTrigger.html#com_google_privacy_dlp_v2_JobTrigger_getInspectJob__)().getInspectConfig().getMinLikelihood());
        }
      }
    }
    

### Node.js

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud Data Loss Prevention library
    const DLP = require('[@google-cloud/dlp](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/overview.html)');
    
    // Instantiates a client
    const dlpClient = new DLP.[DlpServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/overview.html)();
    
    // The project ID to run the API call under
    // const projectId = 'my-project';
    
    // The job trigger ID to run the API call under
    // const jobTriggerName = 'your-job-trigger-name';
    
    async function updateTrigger() {
      // Construct inspect configuration to match PERSON_NAME infotype
      const inspectConfig = {
        infoTypes: [{name: 'PERSON_NAME'}],
        minLikelihood: '[LIKELY](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.likelihood.html)',
      };
    
      // Configure the job trigger we want to update.
      const jobTrigger = {inspectJob: {inspectConfig}};
    
      const updateMask = {
        paths: [
          'inspect_job.inspect_config.info_types',
          'inspect_job.inspect_config.min_likelihood',
        ],
      };
    
      // Combine configurations into a request for the service.
      const request = {
        name: `projects/${projectId}/jobTriggers/${jobTriggerName}`,
        jobTrigger,
        updateMask,
      };
    
      // Send the request and receive response from the service
      const [updatedJobTrigger] = await dlpClient.updateJobTrigger(request);
    
      // Print the results
      console.log(`Updated Trigger: ${JSON.stringify(updatedJobTrigger)}`);
    }
    updateTrigger(projectId, jobTriggerName);

### PHP

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Dlp\V2\Client\DlpServiceClient;
    use Google\Cloud\Dlp\V2\InfoType;
    use Google\Cloud\Dlp\V2\InspectConfig;
    use Google\Cloud\Dlp\V2\InspectJobConfig;
    use Google\Cloud\Dlp\V2\JobTrigger;
    use Google\Cloud\Dlp\V2\Likelihood;
    use Google\Cloud\Dlp\V2\UpdateJobTriggerRequest;
    use Google\Protobuf\FieldMask;
    
    /**
     * Update an existing job trigger.
     *
     * @param string $callingProjectId  The Google Cloud Project ID to run the API call under.
     * @param string $jobTriggerName    The job trigger name to update.
     *
     */
    function update_trigger(
        string $callingProjectId,
        string $jobTriggerName
    ): void {
        // Instantiate a client.
        $dlp = new DlpServiceClient();
    
        // Configure the inspectConfig.
        $inspectConfig = (new InspectConfig())
            ->setInfoTypes([
                (new InfoType())
                    ->setName('US_INDIVIDUAL_TAXPAYER_IDENTIFICATION_NUMBER')
            ])
            ->setMinLikelihood(Likelihood::LIKELY);
    
        // Configure the Job Trigger we want the service to perform.
        $jobTrigger = (new JobTrigger())
            ->setInspectJob((new InspectJobConfig())
                ->setInspectConfig($inspectConfig));
    
        // Specify fields of the jobTrigger resource to be updated when the job trigger is modified.
        // Refer https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask for constructing the field mask paths.
        $fieldMask = (new FieldMask())
            ->setPaths([
                'inspect_job.inspect_config.info_types',
                'inspect_job.inspect_config.min_likelihood'
            ]);
    
        // Send the update job trigger request and process the response.
        $name = "projects/$callingProjectId/locations/global/jobTriggers/" . $jobTriggerName;
        $updateJobTriggerRequest = (new UpdateJobTriggerRequest())
            ->setName($name)
            ->setJobTrigger($jobTrigger)
            ->setUpdateMask($fieldMask);
    
        $response = $dlp->updateJobTrigger($updateJobTriggerRequest);
    
        // Print results.
        printf('Successfully update trigger %s' . PHP_EOL, $response->getName());
    }

### Python

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from typing import List
    
    import google.cloud.dlp
    
    
    def update_trigger(
        project: str,
        info_types: List[str],
        trigger_id: str,
    ) -> None:
        """Uses the Data Loss Prevention API to update an existing job trigger.
        Args:
            project: The Google Cloud project id to use as a parent resource
            info_types: A list of strings representing infoTypes to update trigger with.
                A full list of infoType categories can be fetched from the API.
            trigger_id: The id of job trigger which needs to be updated.
        """
    
        # Instantiate a client.
        dlp = google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html)()
    
        # Prepare info_types by converting the list of strings into a list of
        # dictionaries.
        info_types = [{"name": info_type} for info_type in info_types]
    
        # Specify fields of the jobTrigger resource to be updated when the
        # job trigger is modified.
        job_trigger = {
            "inspect_job": {
                "inspect_config": {
                    "info_types": info_types,
                    "min_likelihood": google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[Likelihood](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.Likelihood.html).LIKELY,
                }
            }
        }
    
        # Convert the project id into a full resource id.
        trigger_name = f"projects/{project}/jobTriggers/{trigger_id}"
    
        # Call the API.
        # Refer https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask
        # for constructing the field mask paths.
        response = dlp.[update_job_trigger](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceClient_update_job_trigger)(
            request={
                "name": trigger_name,
                "job_trigger": job_trigger,
                "update_mask": {
                    "paths": [
                        "inspect_job.inspect_config.info_types",
                        "inspect_job.inspect_config.min_likelihood",
                    ]
                },
            }
        )
    
        # Print out the result.
        print(f"Successfully updated trigger: {response.name}")
        print(
            f"Updated InfoType: {response.inspect_job.inspect_config.info_types[0].name}"
            f" \nUpdates Likelihood: {response.inspect_job.inspect_config.min_likelihood}\n",
        )
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=clouddatalossprevention). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
