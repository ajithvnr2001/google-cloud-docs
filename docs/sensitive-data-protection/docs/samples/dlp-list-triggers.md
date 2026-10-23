---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/samples/dlp-list-triggers/
title: List triggers \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:39:17.361042+00:00
---

# List triggers  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/samples/dlp-list-triggers/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Samples ](https://docs.cloud.google.com/sensitive-data-protection/docs/samples)



#  List triggers Stay organized with collections  Save and categorize content based on your preferences. 

List all job triggers for the current project.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Creating and scheduling Sensitive Data Protection inspection jobs](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-job-triggers)



## Code sample

### C#

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Api.Gax](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.html);
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Dlp.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.html);
    using System;
    
    public class TriggersList
    {
        public static PagedEnumerable<ListJobTriggersResponse, JobTrigger> List(string projectId)
        {
            var dlp = [DlpServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html#Google_Cloud_Dlp_V2_DlpServiceClient_Create)();
    
            var response = dlp.ListJobTriggers(
                new [ListJobTriggersRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ListJobTriggersRequest.html)
                {
                    Parent = new [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)(projectId, "global").ToString(),
                });
    
            foreach (var trigger in response)
            {
                Console.WriteLine($"Name: {trigger.Name}");
                Console.WriteLine($"  Created: {trigger.CreateTime}");
                Console.WriteLine($"  Updated: {trigger.UpdateTime}");
                Console.WriteLine($"  Display Name: {trigger.DisplayName}");
                Console.WriteLine($"  Description: {trigger.Description}");
                Console.WriteLine($"  Status: {trigger.Status}");
                Console.WriteLine($"  Error count: {trigger.Errors.Count}");
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
    	"time"
    
    	dlp "cloud.google.com/go/dlp/apiv2"
    	"cloud.google.com/go/dlp/apiv2/dlppb"
    	"github.com/golang/protobuf/ptypes"
    	"google.golang.org/api/iterator"
    )
    
    // listTriggers lists the triggers for the given project.
    func listTriggers(w io.Writer, projectID string) error {
    	// projectID := "my-project-id"
    
    	ctx := context.Background()
    
    	client, err := dlp.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2.html#cloud_google_com_go_dlp_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("dlp.NewClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2.html#cloud_google_com_go_dlp_apiv2_Client_Close)()
    
    	// Create a configured request.
    	req := &dlppb.ListJobTriggersRequest{
    		Parent: fmt.Sprintf("projects/%s/locations/global", projectID),
    	}
    	// Send the request and iterate over the results.
    	it := client.ListJobTriggers(ctx, req)
    	for {
    		t, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			return fmt.Errorf("Next: %w", err)
    		}
    		fmt.Fprintf(w, "Trigger %v\n", t.GetName())
    		c, err := ptypes.Timestamp(t.GetCreateTime())
    		if err != nil {
    			return fmt.Errorf("CreateTime Timestamp: %w", err)
    		}
    		fmt.Fprintf(w, "  Created: %v\n", c.Format(time.RFC1123))
    		u, err := ptypes.Timestamp(t.GetUpdateTime())
    		if err != nil {
    			return fmt.Errorf("UpdateTime Timestamp: %w", err)
    		}
    		fmt.Fprintf(w, "  Updated: %v\n", u.Format(time.RFC1123))
    		fmt.Fprintf(w, "  Display Name: %q\n", t.GetDisplayName())
    		fmt.Fprintf(w, "  Description: %q\n", t.GetDescription())
    		fmt.Fprintf(w, "  Status: %v\n", t.GetStatus())
    		fmt.Fprintf(w, "  Error Count: %v\n", len(t.GetErrors()))
    	}
    
    	return nil
    }
    

### Java

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.dlp.v2.[DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html);
    import com.google.privacy.dlp.v2.[JobTrigger](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.JobTrigger.html);
    import com.google.privacy.dlp.v2.[ListJobTriggersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ListJobTriggersRequest.html);
    import com.google.privacy.dlp.v2.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html);
    import java.io.IOException;
    
    class TriggersList {
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        listTriggers(projectId);
      }
    
      public static void listTriggers(String projectId) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html) dlpServiceClient = [DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html).create()) {
          // Build the request to be sent by the client
          [ListJobTriggersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ListJobTriggersRequest.html) listJobTriggersRequest =
              [ListJobTriggersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ListJobTriggersRequest.html).newBuilder()
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html).of(projectId, "global").toString())
                  .build();
    
          // Use the client to send the API request.
          [DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html).[ListJobTriggersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.ListJobTriggersPagedResponse.html) response =
              dlpServiceClient.listJobTriggers(listJobTriggersRequest);
    
          // Parse the response and process the results
          System.out.println("DLP triggers found:");
          for ([JobTrigger](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.JobTrigger.html) trigger : response.getPage().getValues()) {
            System.out.println("Trigger: " + trigger.getName());
            System.out.println("\tCreated: " + trigger.getCreateTime());
            System.out.println("\tUpdated: " + trigger.getUpdateTime());
            if (trigger.getDisplayName() != null) {
              System.out.println("\tDisplay name: " + trigger.getDisplayName());
            }
            if (trigger.getDescription() != null) {
              System.out.println("\tDescription: " + trigger.getDescription());
            }
            System.out.println("\tStatus: " + trigger.getStatus());
            System.out.println("\tError count: " + trigger.getErrorsCount());
          }
          ;
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
    
    async function listTriggers() {
      // Construct trigger listing request
      const request = {
        parent: `projects/${projectId}/locations/global`,
      };
    
      // Helper function to pretty-print dates
      const formatDate = date => {
        const msSinceEpoch = parseInt(date.seconds, 10) * 1000;
        return new [Date](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.type.date.html)(msSinceEpoch).toLocaleString('en-US');
      };
    
      // Run trigger listing request
      const [triggers] = await dlp.listJobTriggers(request);
      triggers.forEach(trigger => {
        // Log trigger details
        console.log(`Trigger ${[trigger](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.jobtrigger.trigger.html).name}:`);
        console.log(`  Created: ${formatDate([trigger](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.jobtrigger.trigger.html).createTime)}`);
        console.log(`  Updated: ${formatDate([trigger](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.jobtrigger.trigger.html).updateTime)}`);
        if ([trigger](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.jobtrigger.trigger.html).displayName) {
          console.log(`  Display Name: ${[trigger](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.jobtrigger.trigger.html).displayName}`);
        }
        if ([trigger](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.jobtrigger.trigger.html).description) {
          console.log(`  Description: ${[trigger](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.jobtrigger.trigger.html).description}`);
        }
        console.log(`  Status: ${[trigger](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.jobtrigger.trigger.html).status}`);
        console.log(`  Error count: ${[trigger](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.jobtrigger.trigger.html).errors.length}`);
      });
    }
    
    listTriggers();

### PHP

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Dlp\V2\Client\DlpServiceClient;
    use Google\Cloud\Dlp\V2\ListJobTriggersRequest;
    
    /**
     * List Data Loss Prevention API job triggers.
     *
     * @param string $callingProjectId  The project ID to run the API call under
     */
    function list_triggers(string $callingProjectId): void
    {
        // Instantiate a client.
        $dlp = new DlpServiceClient();
    
        $parent = "projects/$callingProjectId/locations/global";
    
        // Run request
        $listJobTriggersRequest = (new ListJobTriggersRequest())
            ->setParent($parent);
        $response = $dlp->listJobTriggers($listJobTriggersRequest);
    
        // Print results
        $triggers = $response->iterateAllElements();
        foreach ($triggers as $trigger) {
            printf('Trigger %s' . PHP_EOL, $trigger->getName());
            printf('  Created: %s' . PHP_EOL, $trigger->getCreateTime()->getSeconds());
            printf('  Updated: %s' . PHP_EOL, $trigger->getUpdateTime()->getSeconds());
            printf('  Display Name: %s' . PHP_EOL, $trigger->getDisplayName());
            printf('  Description: %s' . PHP_EOL, $trigger->getDescription());
            printf('  Status: %s' . PHP_EOL, $trigger->getStatus());
            printf('  Error count: %s' . PHP_EOL, count($trigger->getErrors()));
            $timespanConfig = $trigger->getInspectJob()->getStorageConfig()->getTimespanConfig();
            printf('  Auto-populates timespan config: %s' . PHP_EOL,
                ($timespanConfig && $timespanConfig->getEnableAutoPopulationOfTimespanConfig() ? 'yes' : 'no'));
        }
    }

### Python

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import google.cloud.dlp
    
    
    def list_triggers(project: str) -> None:
        """Lists all Data Loss Prevention API triggers.
        Args:
            project: The Google Cloud project id to use as a parent resource.
        Returns:
            None; the response from the API is printed to the terminal.
        """
    
        # Instantiate a client.
        dlp = google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html)()
    
        # Convert the project id into a full resource id.
        parent = f"projects/{project}"
    
        # Call the API.
        response = dlp.[list_job_triggers](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceClient_list_job_triggers)(request={"parent": parent})
    
        for trigger in response:
            print(f"Trigger {trigger.name}:")
            print(f"  Created: {trigger.create_time}")
            print(f"  Updated: {trigger.update_time}")
            if trigger.display_name:
                print(f"  Display Name: {trigger.display_name}")
            if trigger.description:
                print(f"  Description: {trigger.description}")
            print(f"  Status: {trigger.status}")
            print(f"  Error count: {len(trigger.errors)}")
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=clouddatalossprevention). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
