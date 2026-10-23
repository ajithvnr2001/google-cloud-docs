---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/samples/dlp-delete-trigger/
title: Delete a trigger \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:33:38.473940+00:00
---

# Delete a trigger  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/samples/dlp-delete-trigger/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Samples ](https://docs.cloud.google.com/sensitive-data-protection/docs/samples)



#  Delete a trigger Stay organized with collections  Save and categorize content based on your preferences. 

Delete a DLP trigger.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Creating and scheduling Sensitive Data Protection inspection jobs](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-job-triggers)



## Code sample

### C#

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Dlp.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.html);
    using System;
    
    public class TriggersDelete
    {
    
        public static void Delete(string triggerName)
        {
            var dlp = [DlpServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html#Google_Cloud_Dlp_V2_DlpServiceClient_Create)();
    
            dlp.DeleteJobTrigger(
                new [DeleteJobTriggerRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DeleteJobTriggerRequest.html)
                {
                    Name = triggerName
                });
    
            Console.WriteLine($"Successfully deleted trigger {triggerName}.");
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
    
    // deleteTrigger deletes the given trigger.
    func deleteTrigger(w io.Writer, triggerID string) error {
    	// triggerID := "my-trigger"
    
    	ctx := context.Background()
    
    	client, err := dlp.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2.html#cloud_google_com_go_dlp_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("dlp.NewClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2.html#cloud_google_com_go_dlp_apiv2_Client_Close)()
    
    	req := &dlppb.DeleteJobTriggerRequest{
    		Name: triggerID,
    	}
    
    	if err := client.DeleteJobTrigger(ctx, req); err != nil {
    		return fmt.Errorf("DeleteJobTrigger: %w", err)
    	}
    	fmt.Fprintf(w, "Successfully deleted trigger %v", triggerID)
    	return nil
    }
    

### Java

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.dlp.v2.[DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html);
    import com.google.privacy.dlp.v2.[DeleteJobTriggerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeleteJobTriggerRequest.html);
    import com.google.privacy.dlp.v2.[ProjectJobTriggerName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ProjectJobTriggerName.html);
    import java.io.IOException;
    
    class TriggersDelete {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String triggerId = "your-trigger-id";
        deleteTrigger(projectId, triggerId);
      }
    
      public static void deleteTrigger(String projectId, String triggerId) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html) dlpServiceClient = [DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html).create()) {
    
          // Get the full trigger name from the given triggerId and ProjectId
          [ProjectJobTriggerName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ProjectJobTriggerName.html) triggerName = [ProjectJobTriggerName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ProjectJobTriggerName.html).of(projectId, triggerId);
    
          // Construct the trigger deletion request to be sent by the client
          [DeleteJobTriggerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeleteJobTriggerRequest.html) deleteJobTriggerRequest =
              [DeleteJobTriggerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeleteJobTriggerRequest.html).newBuilder().setName(triggerName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ProjectJobTriggerName.html#com_google_privacy_dlp_v2_ProjectJobTriggerName_toString__)()).build();
    
          // Send the trigger deletion request
          dlpServiceClient.deleteJobTrigger(deleteJobTriggerRequest);
          System.out.println("Trigger deleted: " + triggerName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ProjectJobTriggerName.html#com_google_privacy_dlp_v2_ProjectJobTriggerName_toString__)());
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
    // const projectId = 'my-project'
    
    // The name of the trigger to be deleted
    // Parent project ID is automatically extracted from this parameter
    // const triggerId = 'projects/my-project/triggers/my-trigger';
    
    async function deleteTrigger() {
      // Construct trigger deletion request
      const request = {
        name: triggerId,
      };
    
      // Run trigger deletion request
      await dlp.deleteJobTrigger(request);
      console.log(`Successfully deleted trigger ${triggerId}.`);
    }
    
    deleteTrigger();

### PHP

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Dlp\V2\Client\DlpServiceClient;
    use Google\Cloud\Dlp\V2\DeleteJobTriggerRequest;
    
    /**
     * Delete a Data Loss Prevention API job trigger.
     *
     * @param string $callingProjectId  The project ID to run the API call under
     * @param string $triggerId         The name of the trigger to be deleted.
     */
    function delete_trigger(string $callingProjectId, string $triggerId): void
    {
        // Instantiate a client.
        $dlp = new DlpServiceClient();
    
        // Run request
        // The Parent project ID is automatically extracted from this parameter
        $triggerName = "projects/$callingProjectId/locations/global/jobTriggers/$triggerId";
        $deleteJobTriggerRequest = (new DeleteJobTriggerRequest())
            ->setName($triggerName);
        $dlp->deleteJobTrigger($deleteJobTriggerRequest);
    
        // Print the results
        printf('Successfully deleted trigger %s' . PHP_EOL, $triggerName);
    }

### Python

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import google.cloud.dlp
    
    
    def delete_trigger(project: str, trigger_id: str) -> None:
        """Deletes a Data Loss Prevention API trigger.
        Args:
            project: The id of the Google Cloud project which owns the trigger.
            trigger_id: The id of the trigger to delete.
        Returns:
            None; the response from the API is printed to the terminal.
        """
    
        # Instantiate a client.
        dlp = google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html)()
    
        # Convert the project id into a full resource id.
        parent = f"projects/{project}"
    
        # Combine the trigger id with the parent id.
        trigger_resource = f"{parent}/jobTriggers/{trigger_id}"
    
        # Call the API.
        dlp.[delete_job_trigger](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceClient_delete_job_trigger)(request={"name": trigger_resource})
    
        print(f"Trigger {trigger_resource} successfully deleted.")
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=clouddatalossprevention). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
