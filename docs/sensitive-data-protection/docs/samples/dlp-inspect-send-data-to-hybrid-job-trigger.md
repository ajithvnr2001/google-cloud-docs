---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/samples/dlp-inspect-send-data-to-hybrid-job-trigger/
title: Create a hybrid job trigger and inspect example data \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:50:54.404420+00:00
---

# Create a hybrid job trigger and inspect example data  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/samples/dlp-inspect-send-data-to-hybrid-job-trigger/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Samples ](https://docs.cloud.google.com/sensitive-data-protection/docs/samples)



#  Create a hybrid job trigger and inspect example data Stay organized with collections  Save and categorize content based on your preferences. 

This sample creates a hybrid job trigger and sends example data to it for inspection. 

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Inspect data from external sources using hybrid jobs](https://docs.cloud.google.com/sensitive-data-protection/docs/how-to-hybrid-jobs)



## Code sample

### C#

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using System;
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Api.Gax](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.html);
    using [Google.Cloud.Dlp.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.html);
    using [Grpc.Core](https://docs.cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.html);
    
    public class SendDataToTheHybridJobTrigger
    {
        public static DlpJob SendToHybridJobTrigger(
           string projectId,
           string jobTriggerId,
           string text = null)
        {
            // Instantiate the dlp client.
            var dlp = [DlpServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html#Google_Cloud_Dlp_V2_DlpServiceClient_Create)();
    
            // Construct the hybrid finding details which will be used as metadata with the content.
            // Refer to this for more information: https://cloud.google.com/dlp/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Container
            var findingDetails = new [HybridFindingDetails](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.HybridFindingDetails.html)
            {
                ContainerDetails = new [Container](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Container.html)
                {
                    FullPath = "10.0.0.2:logs1:aap1",
                    RelativePath = "app1",
                    RootPath = "10.0.0.2:logs1",
                    Type = "System Logs"
                }
            };
    
            // Construct the hybrid content item using the finding details and text to be inspected.
            var hybridContentItem = new [HybridContentItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.HybridContentItem.html)
            {
                Item = new [ContentItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentItem.html) { Value = text ?? "My email is ariel@example.org and name is Ariel." },
                FindingDetails = findingDetails
            };
    
            var jobTriggerName = new [JobTriggerName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.JobTriggerName.html)(projectId, jobTriggerId);
    
            // Construct the request to activate the Job Trigger.
            var activate = new [ActivateJobTriggerRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ActivateJobTriggerRequest.html)
            {
                JobTriggerName = jobTriggerName
            };
    
            [DlpJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpJob.html) triggerJob = null;
    
            try
            {
                // Call the API to activate the trigger.
                triggerJob = dlp.ActivateJobTrigger(activate);
            }
            catch ([RpcException](https://docs.cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.RpcException.html))
            {
                [ListDlpJobsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ListDlpJobsRequest.html) listJobsRequest = new [ListDlpJobsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ListDlpJobsRequest.html)
                {
                    ParentAsLocationName = new [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)(projectId, "global"),
                    Filter = $"trigger_name={jobTriggerName}"
                };
    
                PagedEnumerable<ListDlpJobsResponse, DlpJob> res = dlp.ListDlpJobs(listJobsRequest);
                foreach ([DlpJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpJob.html) j in res)
                {
                    triggerJob = j;
                }
            }
    
            // Construct the request using hybrid content item.
            var request = new [HybridInspectJobTriggerRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.HybridInspectJobTriggerRequest.html)
            {
                HybridItem = hybridContentItem,
                JobTriggerName = jobTriggerName
            };
    
            // Call the API.
            [HybridInspectResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.HybridInspectResponse.html) _ = dlp.HybridInspectJobTrigger(request);
    
            Console.WriteLine($"Hybrid job created successfully. Job name: {triggerJob.[Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpJob.html#Google_Cloud_Dlp_V2_DlpJob_Name)}");
    
            return triggerJob;
        }
    }
    

### Go

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"log"
    	"time"
    
    	dlp "cloud.google.com/go/dlp/apiv2"
    	"cloud.google.com/go/dlp/apiv2/dlppb"
    )
    
    // inspectDataToHybridJobTrigger uses the Data Loss Prevention API to inspect sensitive
    // information using Hybrid jobs trigger that scans payloads of data sent from
    // virtually any source and stores findings in Google Cloud.
    func inspectDataToHybridJobTrigger(w io.Writer, projectID, textToDeIdentify, jobTriggerName string) error {
    	// projectId := "your-project-id"
    	// jobTriggerName := "your-job-trigger-name"
    	// textToDeIdentify := "My email is test@example.org"
    
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
    			Value: textToDeIdentify,
    		},
    	}
    
    	// Contains metadata to associate with the content.
    	// Refer to https://cloud.google.com/dlp/docs/reference/rpc/google.privacy.dlp.v2#container for specifying the paths in container object.
    	container := &dlppb.Container{
    		Type:         "logging_sys",
    		FullPath:     "10.0.0.2:logs1:app1",
    		RelativePath: "app1",
    		RootPath:     "10.0.0.2:logs1",
    		Version:      "1.2",
    	}
    
    	// Set the required label.
    	labels := map[string]string{
    		"env":                           "prod",
    		"appointment-bookings-comments": "",
    	}
    
    	hybridFindingDetails := &dlppb.HybridFindingDetails{
    		ContainerDetails: container,
    		Labels:           labels,
    	}
    
    	hybridContentItem := &dlppb.HybridContentItem{
    		Item:           contentItem,
    		FindingDetails: hybridFindingDetails,
    	}
    
    	// Activate the job trigger.
    	activateJobreq := &dlppb.ActivateJobTriggerRequest{
    		Name: jobTriggerName,
    	}
    
    	dlpJob, err := client.ActivateJobTrigger(ctx, activateJobreq)
    	if err != nil {
    		log.Printf("Error from return part %v", err)
    		return err
    	}
    	// Build the hybrid inspect request.
    	req := &dlppb.HybridInspectJobTriggerRequest{
    		Name:       jobTriggerName,
    		HybridItem: hybridContentItem,
    	}
    
    	// Send the hybrid inspect request.
    	_, err = client.HybridInspectJobTrigger(ctx, req)
    	if err != nil {
    		return err
    	}
    
    	getDlpJobReq := &dlppb.GetDlpJobRequest{
    		Name: dlpJob.Name,
    	}
    
    	var result *dlppb.DlpJob
    	for i := 0; i < 5; i++ {
    		// Get DLP job
    		result, err = client.GetDlpJob(ctx, getDlpJobReq)
    		if err != nil {
    			fmt.Printf("Error getting DLP job: %v\n", err)
    			return err
    		}
    
    		// Check if processed bytes is greater than 0
    		if result.GetInspectDetails().GetResult().GetProcessedBytes() > 0 {
    			break
    		}
    
    		// Wait for 5 seconds before checking again
    		time.Sleep(5 * time.Second)
    		i++
    	}
    
    	fmt.Fprintf(w, "Job Name: %v\n", result.Name)
    	fmt.Fprintf(w, "Job State: %v\n", result.State)
    
    	inspectionResult := result.GetInspectDetails().GetResult()
    	fmt.Fprint(w, "Findings: \n")
    	for _, v := range inspectionResult.GetInfoTypeStats() {
    		fmt.Fprintf(w, "Infotype: %v\n", v.InfoType.Name)
    		fmt.Fprintf(w, "Likelihood: %v\n", v.GetCount())
    	}
    
    	fmt.Fprint(w, "successfully inspected data using hybrid job trigger ")
    	return nil
    }
    

### Java

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.gax.rpc.[InvalidArgumentException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.InvalidArgumentException.html);
    import com.google.cloud.dlp.v2.[DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html);
    import com.google.privacy.dlp.v2.[ActivateJobTriggerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ActivateJobTriggerRequest.html);
    import com.google.privacy.dlp.v2.[Container](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Container.html);
    import com.google.privacy.dlp.v2.[ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html);
    import com.google.privacy.dlp.v2.[DlpJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html);
    import com.google.privacy.dlp.v2.[GetDlpJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.GetDlpJobRequest.html);
    import com.google.privacy.dlp.v2.[HybridContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.HybridContentItem.html);
    import com.google.privacy.dlp.v2.[HybridFindingDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.HybridFindingDetails.html);
    import com.google.privacy.dlp.v2.[HybridInspectJobTriggerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.HybridInspectJobTriggerRequest.html);
    import com.google.privacy.dlp.v2.[InfoTypeStats](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeStats.html);
    import com.google.privacy.dlp.v2.[InspectDataSourceDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectDataSourceDetails.html);
    import com.google.privacy.dlp.v2.[JobTriggerName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.JobTriggerName.html);
    import com.google.privacy.dlp.v2.[ListDlpJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ListDlpJobsRequest.html);
    
    public class InspectDataToHybridJobTrigger {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        // The Google Cloud project id to use as a parent resource.
        String projectId = "your-project-id";
        // The job trigger id used to for processing a hybrid job trigger.
        String jobTriggerId = "your-job-trigger-id";
        // The string to de-identify.
        String textToDeIdentify = "My email is test@example.org and my name is Gary.";
        inspectDataToHybridJobTrigger(textToDeIdentify, projectId, jobTriggerId);
      }
    
      // Inspects data using a hybrid job trigger.
      // Hybrid jobs trigger allows to scan payloads of data sent from virtually any source for
      // sensitive information and then store the findings in Google Cloud.
      public static void inspectDataToHybridJobTrigger(
          String textToDeIdentify, String projectId, String jobTriggerId) throws Exception {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html) dlpClient = [DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html).create()) {
          // Specify the content to be inspected.
          [ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html) contentItem = [ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html).newBuilder().setValue(textToDeIdentify).build();
    
          // Contains metadata to associate with the content.
          // Refer to https://cloud.google.com/dlp/docs/reference/rest/v2/Container for specifying the
          // paths in container object.
          [Container](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Container.html) container =
              [Container](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Container.html).newBuilder()
                  .[setFullPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Container.Builder.html#com_google_privacy_dlp_v2_Container_Builder_setFullPath_java_lang_String_)("10.0.0.2:logs1:app1")
                  .[setRelativePath](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Container.Builder.html#com_google_privacy_dlp_v2_Container_Builder_setRelativePath_java_lang_String_)("app1")
                  .[setRootPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Container.Builder.html#com_google_privacy_dlp_v2_Container_Builder_setRootPath_java_lang_String_)("10.0.0.2:logs1")
                  .setType("logging_sys")
                  .setVersion("1.2")
                  .build();
    
          [HybridFindingDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.HybridFindingDetails.html) hybridFindingDetails =
              [HybridFindingDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.HybridFindingDetails.html).newBuilder().[setContainerDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.HybridFindingDetails.Builder.html#com_google_privacy_dlp_v2_HybridFindingDetails_Builder_setContainerDetails_com_google_privacy_dlp_v2_Container_)(container).build();
    
          [HybridContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.HybridContentItem.html) hybridContentItem =
              [HybridContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.HybridContentItem.html).newBuilder()
                  .setItem(contentItem)
                  .[setFindingDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.HybridContentItem.Builder.html#com_google_privacy_dlp_v2_HybridContentItem_Builder_setFindingDetails_com_google_privacy_dlp_v2_HybridFindingDetails_)(hybridFindingDetails)
                  .build();
    
          // Activate the job trigger.
          [ActivateJobTriggerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ActivateJobTriggerRequest.html) activateJobTriggerRequest =
              [ActivateJobTriggerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ActivateJobTriggerRequest.html).newBuilder()
                  .setName([JobTriggerName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.JobTriggerName.html).of(projectId, jobTriggerId).toString())
                  .build();
    
          [DlpJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html) dlpJob;
    
          try {
            dlpJob = dlpClient.activateJobTrigger(activateJobTriggerRequest);
          } catch ([InvalidArgumentException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.InvalidArgumentException.html) e) {
            [ListDlpJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ListDlpJobsRequest.html) request =
                [ListDlpJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ListDlpJobsRequest.html).newBuilder()
                    .setParent([JobTriggerName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.JobTriggerName.html).of(projectId, jobTriggerId).toString())
                    .setFilter("trigger_name=" + [JobTriggerName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.JobTriggerName.html).of(projectId, jobTriggerId).toString())
                    .build();
    
            // Retrieve the DLP jobs triggered by the job trigger
            [DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html).[ListDlpJobsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.ListDlpJobsPagedResponse.html) response = dlpClient.listDlpJobs(request);
            dlpJob = response.getPage().getResponse().getJobs(0);
          }
    
          // Build the hybrid inspect request.
          [HybridInspectJobTriggerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.HybridInspectJobTriggerRequest.html) request =
              [HybridInspectJobTriggerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.HybridInspectJobTriggerRequest.html).newBuilder()
                  .setName([JobTriggerName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.JobTriggerName.html).of(projectId, jobTriggerId).toString())
                  .setHybridItem(hybridContentItem)
                  .build();
    
          // Send the hybrid inspect request.
          dlpClient.hybridInspectJobTrigger(request);
    
          // Build a request to get the completed job
          [GetDlpJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.GetDlpJobRequest.html) getDlpJobRequest =
              [GetDlpJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.GetDlpJobRequest.html).newBuilder().setName(dlpJob.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html#com_google_privacy_dlp_v2_DlpJob_getName__)()).build();
    
          [DlpJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html) result = null;
    
          do {
            result = dlpClient.getDlpJob(getDlpJobRequest);
            Thread.sleep(5000);
          } while (result.[getInspectDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html#com_google_privacy_dlp_v2_DlpJob_getInspectDetails__)().getResult().getProcessedBytes() <= 0);
    
          System.out.println("Job status: " + result.[getState](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html#com_google_privacy_dlp_v2_DlpJob_getState__)());
          System.out.println("Job name: " + result.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html#com_google_privacy_dlp_v2_DlpJob_getName__)());
          // Parse the response and process results.
          [InspectDataSourceDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectDataSourceDetails.html).[Result](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectDataSourceDetails.Result.html) inspectionResult = result.[getInspectDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DlpJob.html#com_google_privacy_dlp_v2_DlpJob_getInspectDetails__)().getResult();
          System.out.println("Findings: ");
          for ([InfoTypeStats](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeStats.html) infoTypeStat : inspectionResult.getInfoTypeStatsList()) {
            System.out.println("\tInfoType: " + infoTypeStat.getInfoType().getName());
            System.out.println("\tCount: " + infoTypeStat.getCount() + "\n");
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
    const dlpClient = new DLP.[DlpServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/overview.html)();
    
    // The project ID to run the API call under.
    // const projectId = "your-project-id";
    
    // The string to de-identify
    // const string = 'My email is test@example.org';
    
    // Job Trigger ID
    // const jobTriggerId = 'your-job-trigger-id';
    
    async function inspectDataToHybridJobTrigger() {
      // Contains metadata to associate with the content.
      const container = {
        full_path: '10.0.0.2:logs1:app1',
        relative_path: 'app1',
        root_path: '10.0.0.2:logs1',
        type: 'logging_sys',
        version: '1.2',
      };
    
      const labels = {env: 'prod', 'appointment-bookings-comments': ''};
    
      // Build the hybrid content item.
      const hybridContentItem = {
        item: {value: string},
        findingDetails: {
          containerDetails: container,
          labels,
        },
      };
      let jobName;
      const fullTriggerName = `projects/${projectId}/jobTriggers/${jobTriggerId}`;
      // Activate the job trigger.
      try {
        const response = await dlpClient.activateJobTrigger({
          name: fullTriggerName,
        });
        jobName = response[0].name;
      } catch (err) {
        console.log(err);
        if (err.code === 3) {
          const response = await dlpClient.listDlpJobs({
            parent: fullTriggerName,
            filter: `trigger_name=${fullTriggerName}`,
          });
          jobName = response[0][0].name;
        }
        // Ignore error related to job trigger already active
        if (err.code !== 3) {
          console.log(err.message);
          return;
        }
      }
      // Build the hybrid inspect request.
      const request = {
        name: `projects/${projectId}/jobTriggers/${jobTriggerId}`,
        hybridItem: hybridContentItem,
      };
      // Send the hybrid inspect request.
      await dlpClient.hybridInspectJobTrigger(request);
      // Waiting for a maximum of 15 minutes for the job to get complete.
      let job;
      let numOfAttempts = 30;
      while (numOfAttempts > 0) {
        // Fetch DLP Job status
        [job] = await dlpClient.getDlpJob({name: jobName});
    
        if (job.state === 'FAILED') {
          console.log('Job Failed, Please check the configuration.');
          return;
        }
        // Check if the job has completed.
        if (job.inspectDetails.result.processedBytes > 0) {
          break;
        }
        // Sleep for a short duration before checking the job status again.
        await new Promise(resolve => {
          setTimeout(() => resolve(), 30000);
        });
        numOfAttempts -= 1;
      }
      // Finish the job once the inspection is complete.
      await dlpClient.finishDlpJob({name: jobName});
    
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
    await inspectDataToHybridJobTrigger();

### PHP

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\Dlp\V2\ActivateJobTriggerRequest;
    use Google\Cloud\Dlp\V2\Client\DlpServiceClient;
    use Google\Cloud\Dlp\V2\Container;
    use Google\Cloud\Dlp\V2\ContentItem;
    use Google\Cloud\Dlp\V2\DlpJob\JobState;
    use Google\Cloud\Dlp\V2\GetDlpJobRequest;
    use Google\Cloud\Dlp\V2\HybridContentItem;
    use Google\Cloud\Dlp\V2\HybridFindingDetails;
    use Google\Cloud\Dlp\V2\HybridInspectJobTriggerRequest;
    use Google\Cloud\Dlp\V2\ListDlpJobsRequest;
    
    /**
     * Inspect data hybrid job trigger.
     * Send data to the hybrid job or hybrid job trigger.
     *
     * @param string $callingProjectId  The Google Cloud project id to use as a parent resource.
     * @param string $string            The string to inspect (will be treated as text).
     */
    
    function inspect_send_data_to_hybrid_job_trigger(
        // TODO(developer): Replace sample parameters before running the code.
        string $callingProjectId,
        string $jobTriggerId,
        string $string
    ): void {
        // Instantiate a client.
        $dlp = new DlpServiceClient();
    
        $content = (new ContentItem())
            ->setValue($string);
    
        $container = (new Container())
            ->setFullPath('10.0.0.2:logs1:app1')
            ->setRelativePath('app1')
            ->setRootPath('10.0.0.2:logs1')
            ->setType('logging_sys')
            ->setVersion('1.2');
    
        $findingDetails = (new HybridFindingDetails())
            ->setContainerDetails($container)
            ->setLabels([
                'env' => 'prod',
                'appointment-bookings-comments' => ''
            ]);
    
        $hybridItem = (new HybridContentItem())
            ->setItem($content)
            ->setFindingDetails($findingDetails);
    
        $parent = "projects/$callingProjectId/locations/global";
        $name = "projects/$callingProjectId/locations/global/jobTriggers/" . $jobTriggerId;
    
        $triggerJob = null;
        try {
            $activateJobTriggerRequest = (new ActivateJobTriggerRequest())
                ->setName($name);
            $triggerJob = $dlp->activateJobTrigger($activateJobTriggerRequest);
        } catch (ApiException $e) {
            $listDlpJobsRequest = (new ListDlpJobsRequest())
                ->setParent($parent)
                ->setFilter('trigger_name=' . $name);
            $result = $dlp->listDlpJobs($listDlpJobsRequest);
            foreach ($result as $job) {
                $triggerJob = $job;
            }
        }
        $hybridInspectJobTriggerRequest = (new HybridInspectJobTriggerRequest())
            ->setName($name)
            ->setHybridItem($hybridItem);
    
        $dlp->hybridInspectJobTrigger($hybridInspectJobTriggerRequest);
    
        $numOfAttempts = 10;
        do {
            printf('Waiting for job to complete' . PHP_EOL);
            sleep(10);
            $getDlpJobRequest = (new GetDlpJobRequest())
                ->setName($triggerJob->getName());
            $job = $dlp->getDlpJob($getDlpJobRequest);
            if ($job->getState() != JobState::RUNNING) {
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
    
    import google.cloud.dlp
    
    
    def inspect_data_to_hybrid_job_trigger(
        project: str,
        trigger_id: str,
        content_string: str,
    ) -> None:
        """
        Uses the Data Loss Prevention API to inspect sensitive information
        using Hybrid jobs trigger that scans payloads of data sent from
        virtually any source and stores findings in Google Cloud.
        Args:
            project: The Google Cloud project id to use as a parent resource.
            trigger_id: The job trigger identifier for hybrid job trigger.
            content_string: The string to inspect.
        """
    
        # Instantiate a client.
        dlp = google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html)()
    
        # Construct the `item` to inspect.
        item = {"value": content_string}
    
        # Construct the container details that contains metadata to be
        # associated with the content. For more details, please refer to
        # https://cloud.google.com/dlp/docs/reference/rest/v2/Container
        container_details = {
            "full_path": "10.0.0.2:logs1:app1",
            "relative_path": "app1",
            "root_path": "10.0.0.2:logs1",
            "type_": "logging_sys",
            "version": "1.2",
        }
    
        # Construct hybrid inspection configuration.
        hybrid_config = {
            "item": item,
            "finding_details": {
                "container_details": container_details,
                "labels": {
                    "env": "prod",
                    "appointment-bookings-comments": "",
                },
            },
        }
    
        # Convert the trigger id into a full resource id.
        trigger_id = f"projects/{project}/jobTriggers/{trigger_id}"
    
        # Activate the job trigger.
        dlp_job = dlp.[activate_job_trigger](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceClient_activate_job_trigger)(request={"name": trigger_id})
    
        # Call the API.
        dlp.[hybrid_inspect_job_trigger](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceClient_hybrid_inspect_job_trigger)(
            request={
                "name": trigger_id,
                "hybrid_item": hybrid_config,
            }
        )
    
        # Get inspection job details.
        job = dlp.get_dlp_job(request={"name": dlp_job.name})
    
        # Wait for dlp job to get finished.
        while job.inspect_details.result.processed_bytes <= 0:
            time.sleep(5)
            job = dlp.get_dlp_job(request={"name": dlp_job.name})
    
        # Print the results.
        print(f"Job name: {dlp_job.name}")
        if job.inspect_details.result.info_type_stats:
            for finding in job.inspect_details.result.info_type_stats:
                print(f"Info type: {finding.info_type.name}; Count: {finding.count}")
        else:
            print("No findings.")
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=clouddatalossprevention). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
