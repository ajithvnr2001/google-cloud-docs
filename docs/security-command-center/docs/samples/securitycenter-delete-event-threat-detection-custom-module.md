---
url: https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-delete-event-threat-detection-custom-module/
title: Delete Event Threat Detection custom modules \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:48:11.003571+00:00
---

# Delete Event Threat Detection custom modules  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-delete-event-threat-detection-custom-module/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Samples ](https://docs.cloud.google.com/security-command-center/docs/samples)



#  Delete Event Threat Detection custom modules Stay organized with collections  Save and categorize content based on your preferences. 

Sample code to delete Event Threat Detection custom modules

## Code sample

### Go

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	securitycentermanagement "cloud.google.com/go/securitycentermanagement/apiv1"
    	securitycentermanagementpb "cloud.google.com/go/securitycentermanagement/apiv1/securitycentermanagementpb"
    )
    
    // deleteEventThreatDetectionCustomModule deletes a specific custom module by its name.
    func deleteEventThreatDetectionCustomModule(w io.Writer, parent string, customModuleID string) error {
    	// parent: Use any one of the following options:
    	//             - organizations/{organization_id}/locations/{location_id}
    	//             - folders/{folder_id}/locations/{location_id}
    	//             - projects/{project_id}/locations/{location_id}
    	// customModuleID := "your-module-id"
    	name := fmt.Sprintf("%s/eventThreatDetectionCustomModules/%s", parent, customModuleID)
    	ctx := context.Background()
    	client, err := securitycentermanagement.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycentermanagement/latest/apiv1.html#cloud_google_com_go_securitycentermanagement_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("securitycentermanagement.NewClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycentermanagement/latest/apiv1.html#cloud_google_com_go_securitycentermanagement_apiv1_Client_Close)()
    
    	req := &securitycentermanagementpb.DeleteEventThreatDetectionCustomModuleRequest{
    		Name: name,
    	}
    
    	err = client.DeleteEventThreatDetectionCustomModule(ctx, req)
    	if err != nil {
    		return fmt.Errorf("Failed to delete EventThreatDetectionCustomModule: %w", err)
    	}
    
    	fmt.Fprintf(w, "Deleted EventThreatDetectionCustomModule Successfully: %s\n", customModuleID)
    	return nil
    }
    

### Java

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.securitycentermanagement.v1.[DeleteEventThreatDetectionCustomModuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.DeleteEventThreatDetectionCustomModuleRequest.html);
    import com.google.cloud.securitycentermanagement.v1.[SecurityCenterManagementClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterManagementClient.html);
    import java.io.IOException;
    
    public class DeleteEventThreatDetectionCustomModule {
    
      public static void main(String[] args) throws IOException {
        // https://cloud.google.com/security-command-center/docs/reference/security-center-management/rest/v1/organizations.locations.eventThreatDetectionCustomModules/delete
        // TODO: Developer should replace project_id with a real project ID before running this code
        String projectId = "project_id";
    
        String customModuleId = "custom_module_id";
    
        deleteEventThreatDetectionCustomModule(projectId, customModuleId);
      }
    
      public static boolean deleteEventThreatDetectionCustomModule(
          String projectId, String customModuleId) throws IOException {
    
        // Initialize client that will be used to send requests. This client only needs
        // to be created
        // once, and can be reused for multiple requests.
        try ([SecurityCenterManagementClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterManagementClient.html) client = [SecurityCenterManagementClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterManagementClient.html).create()) {
    
          String qualifiedModuleName =
              String.format(
                  "projects/%s/locations/global/eventThreatDetectionCustomModules/%s",
                  projectId, customModuleId);
    
          [DeleteEventThreatDetectionCustomModuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.DeleteEventThreatDetectionCustomModuleRequest.html) request =
              [DeleteEventThreatDetectionCustomModuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.DeleteEventThreatDetectionCustomModuleRequest.html).newBuilder()
                  .setName(qualifiedModuleName)
                  .build();
    
          client.deleteEventThreatDetectionCustomModule(request);
    
          return true;
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
    
    /*
     * Required. Resource name of event threat detection module.
     *     Its format is
     *    `organizations/[organization_id]/locations/[location_id]/eventThreatDetectionCustomModules/[custom_module]`
     *    `folders/[folder_id]/locations/[location_id]/eventThreatDetectionCustomModules/[custom_module]`
     *    `projects/[project_id]/locations/[location_id]/eventThreatDetectionCustomModules/[custom_module]`
     */
    // TODO(developer): Update the following references for your own environment before running the sample.
    // const organizationId = 'YOUR_ORGANIZATION_ID';
    // const location = 'LOCATION_ID';
    // const customModuleId = 'CUSTOM_MODULE_ID';
    const name = `organizations/${organizationId}/locations/${location}/eventThreatDetectionCustomModules/${customModuleId}`;
    
    // Build the request.
    const deleteEventThreatDetectionCustomModuleRequest = {
      name: name,
    };
    
    async function deleteEventThreatDetectionCustomModule() {
      // Call the API.
      const [response] = await client.deleteEventThreatDetectionCustomModule(
        deleteEventThreatDetectionCustomModuleRequest
      );
      console.log(
        'EventThreatDetectionCustomModule deleted successfully: %j',
        response
      );
    }
    
    deleteEventThreatDetectionCustomModule();

### Python

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def delete_event_threat_detection_custom_module(parent: str, module_id: str):
        """
        Deletes an Event Threat Detection custom module.
        Args:
            parent: Use any one of the following options:
                    - organizations/{organization_id}/locations/{location_id}
                    - folders/{folder_id}/locations/{location_id}
                    - projects/{project_id}/locations/{location_id}
        Returns:
            Message that Event Threat Detection custom module is deleted.
        Raises:
            NotFound: If the specified custom module does not exist.
        """
        client = securitycentermanagement_v1.SecurityCenterManagementClient()
    
        try:
            request = securitycentermanagement_v1.DeleteEventThreatDetectionCustomModuleRequest(
                name=f"{parent}/eventThreatDetectionCustomModules/{module_id}",
            )
    
            client.delete_event_threat_detection_custom_module(request=request)
            print(f"Deleted Event Threat Detection Custom Module Successfully: {module_id}")
        except NotFound as e:
            print(f"Custom Module not found: {module_id}")
            raise e

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=securitycommandcenter). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
