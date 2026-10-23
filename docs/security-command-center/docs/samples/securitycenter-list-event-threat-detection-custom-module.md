---
url: https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-list-event-threat-detection-custom-module/
title: List Event Threat Detection custom modules \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:32:44.736543+00:00
---

# List Event Threat Detection custom modules  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-list-event-threat-detection-custom-module/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Samples ](https://docs.cloud.google.com/security-command-center/docs/samples)



#  List Event Threat Detection custom modules Stay organized with collections  Save and categorize content based on your preferences. 

Sample code to list Event Threat Detection custom modules

## Code sample

### Go

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	securitycentermanagement "cloud.google.com/go/securitycentermanagement/apiv1"
    	securitycentermanagementpb "cloud.google.com/go/securitycentermanagement/apiv1/securitycentermanagementpb"
    	iterator "google.golang.org/api/iterator"
    )
    
    // listEventThreatDetectionCustomModule lists all custom modules for Event Threat Detection.
    func listEventThreatDetectionCustomModule(w io.Writer, parent string) error {
    	// parent: Use any one of the following options:
    	// - organizations/{organization_id}/locations/{location_id}
    	// - folders/{folder_id}/locations/{location_id}
    	// - projects/{project_id}/locations/{location_id}
    
    	ctx := context.Background()
    	client, err := securitycentermanagement.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycentermanagement/latest/apiv1.html#cloud_google_com_go_securitycentermanagement_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("securitycentermanagement.NewClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycentermanagement/latest/apiv1.html#cloud_google_com_go_securitycentermanagement_apiv1_Client_Close)()
    
    	req := &securitycentermanagementpb.ListEventThreatDetectionCustomModulesRequest{
    		Parent: parent,
    	}
    
    	// List all Event Threat Detection custom modules present in the resource.
    	it := client.ListEventThreatDetectionCustomModules(ctx, req)
    	for {
    		resp, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			return fmt.Errorf("it.Next: %w", err)
    		}
    		fmt.Fprintf(w, "Custom Module Name: %s,\n", resp.Name)
    	}
    	return nil
    }
    

### Java

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.securitycentermanagement.v1.[EventThreatDetectionCustomModule](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.EventThreatDetectionCustomModule.html);
    import com.google.cloud.securitycentermanagement.v1.[ListEventThreatDetectionCustomModulesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.ListEventThreatDetectionCustomModulesRequest.html);
    import com.google.cloud.securitycentermanagement.v1.[SecurityCenterManagementClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterManagementClient.html);
    import com.google.common.collect.ImmutableList;
    import java.io.IOException;
    
    public class ListEventThreatDetectionCustomModules {
    
      public static void main(String[] args) throws IOException {
        // https://cloud.google.com/security-command-center/docs/reference/security-center-management/rest/v1/organizations.locations.eventThreatDetectionCustomModules/list
        // TODO: Developer should replace project_id with a real project ID before running this code
        String projectId = "project_id";
    
        listEventThreatDetectionCustomModules(projectId);
      }
    
      public static ImmutableList<EventThreatDetectionCustomModule>
          listEventThreatDetectionCustomModules(String projectId) throws IOException {
    
        // Initialize client that will be used to send requests. This client only needs
        // to be created
        // once, and can be reused for multiple requests.
        try ([SecurityCenterManagementClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterManagementClient.html) client = [SecurityCenterManagementClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterManagementClient.html).create()) {
    
          String parent = String.format("projects/%s/locations/global", projectId);
    
          [ListEventThreatDetectionCustomModulesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.ListEventThreatDetectionCustomModulesRequest.html) request =
              [ListEventThreatDetectionCustomModulesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.ListEventThreatDetectionCustomModulesRequest.html).newBuilder().setParent(parent).build();
    
          return ImmutableList.copyOf(
              client.listEventThreatDetectionCustomModules(request).iterateAll());
        }
      }
    }

### Node.js

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud client library.
    const {SecurityCenterManagementClient} =
      require('[@google-cloud/securitycentermanagement](https://docs.cloud.google.com/nodejs/docs/reference/securitycentermanagement/latest/overview.html)').v1;
    
    // Create a Security Center Management client
    const client = new [SecurityCenterManagementClient](https://docs.cloud.google.com/nodejs/docs/reference/securitycentermanagement/latest/overview.html)();
    
    /**
     *  Required. The name of the parent resource of the list event threat detection custom module. Its
     *  format is "organizations/[organization_id]/locations/[location_id]",
     *  "folders/[folder_id]/locations/[location_id]", or
     *  "projects/[project_id]/locations/[location_id]".
     */
    //TODO(developer): Update the following references for your own environment before running the sample.
    // const organizationId = 'YOUR_ORGANIZATION_ID';
    // const location = 'LOCATION_ID';
    const parent = `organizations/${organizationId}/locations/${location}`;
    
    // Build the request.
    const listEventThreatDetectionCustomModulesRequest = {
      parent: parent,
    };
    
    async function listEventThreatDetectionCustomModules() {
      // Call the API.
      const [modules] = await client.listEventThreatDetectionCustomModules(
        listEventThreatDetectionCustomModulesRequest
      );
      for (const module of modules) {
        console.log('Custom Module name:', module.name);
      }
    }
    
    listEventThreatDetectionCustomModules();

### Python

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def list_event_threat_detection_custom_module(parent: str):
        """
        Retrieves list of Event Threat Detection custom module.
        Args:
            parent: Use any one of the following options:
                    - organizations/{organization_id}/locations/{location_id}
                    - folders/{folder_id}/locations/{location_id}
                    - projects/{project_id}/locations/{location_id}
        Returns:
            List of retrieved Event Threat Detection custom modules.
        Raises:
            NotFound: If the specified custom module does not exist.
        """
    
        client = securitycentermanagement_v1.SecurityCenterManagementClient()
    
        try:
            request = securitycentermanagement_v1.ListEventThreatDetectionCustomModulesRequest(
                parent=parent,
            )
    
            response = client.list_event_threat_detection_custom_modules(request=request)
    
            custom_modules = []
            for custom_module in response:
                print(f"Custom Module: {custom_module.name}")
                custom_modules.append(custom_module)
            return custom_modules
        except NotFound as e:
            print(f"Parent resource not found: {parent}")
            raise e
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=securitycommandcenter). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
