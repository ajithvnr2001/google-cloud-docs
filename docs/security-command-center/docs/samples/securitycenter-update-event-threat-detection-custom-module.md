---
url: https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-update-event-threat-detection-custom-module/
title: Update an Event Threat Detection custom module \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:49:55.294430+00:00
---

# Update an Event Threat Detection custom module  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-update-event-threat-detection-custom-module/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Samples ](https://docs.cloud.google.com/security-command-center/docs/samples)



#  Update an Event Threat Detection custom module Stay organized with collections  Save and categorize content based on your preferences. 

Sample code to update Event Threat Detection custom modules

## Code sample

### Go

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	securitycentermanagement "cloud.google.com/go/securitycentermanagement/apiv1"
    	securitycentermanagementpb "cloud.google.com/go/securitycentermanagement/apiv1/securitycentermanagementpb"
    	fieldmaskpb "google.golang.org/protobuf/types/known/fieldmaskpb"
    )
    
    // updateEventThreatDetectionCustomModule updates a custom module for Event Threat Detection.
    func updateEventThreatDetectionCustomModule(w io.Writer, parent string, customModuleID string) error {
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
    
    	// Define the custom module configuration
    	customModule := &securitycentermanagementpb.EventThreatDetectionCustomModule{
    		Name:            fmt.Sprintf("%s/eventThreatDetectionCustomModules/%s", parent, customModuleID),
    		EnablementState: securitycentermanagementpb.[EventThreatDetectionCustomModule_DISABLED](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycentermanagement/latest/apiv1/securitycentermanagementpb.html#cloud_google_com_go_securitycentermanagement_apiv1_securitycentermanagementpb_EventThreatDetectionCustomModule_ENABLEMENT_STATE_UNSPECIFIED_EventThreatDetectionCustomModule_ENABLED_EventThreatDetectionCustomModule_DISABLED_EventThreatDetectionCustomModule_INHERITED),
    	}
    
    	req := &securitycentermanagementpb.UpdateEventThreatDetectionCustomModuleRequest{
    		UpdateMask: &fieldmaskpb.FieldMask{
    			Paths: []string{
    				"enablement_state",
    			},
    		},
    		EventThreatDetectionCustomModule: customModule,
    	}
    
    	module, err := client.UpdateEventThreatDetectionCustomModule(ctx, req)
    	if err != nil {
    		return fmt.Errorf("failed to update EventThreatDetectionCustomModule: %w", err)
    	}
    
    	fmt.Fprintf(w, "Updated EventThreatDetectionCustomModule: %s\n", module.Name)
    	return nil
    }
    

### Java

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.securitycentermanagement.v1.[EventThreatDetectionCustomModule](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.EventThreatDetectionCustomModule.html);
    import com.google.cloud.securitycentermanagement.v1.[EventThreatDetectionCustomModule](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.EventThreatDetectionCustomModule.html).EnablementState;
    import com.google.cloud.securitycentermanagement.v1.[SecurityCenterManagementClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterManagementClient.html);
    import com.google.cloud.securitycentermanagement.v1.[UpdateEventThreatDetectionCustomModuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.UpdateEventThreatDetectionCustomModuleRequest.html);
    import com.google.protobuf.[FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html);
    import java.io.IOException;
    
    public class UpdateEventThreatDetectionCustomModule {
    
      public static void main(String[] args) throws IOException {
        // TODO: Developer should replace project_id with a real project ID before running this code
        String projectId = "project_id";
    
        String customModuleId = "custom_module_id";
    
        updateEventThreatDetectionCustomModule(projectId, customModuleId);
      }
    
      public static [EventThreatDetectionCustomModule](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.EventThreatDetectionCustomModule.html) updateEventThreatDetectionCustomModule(
          String projectId, String customModuleId) throws IOException {
    
        // Initialize client that will be used to send requests. This client only needs
        // to be created
        // once, and can be reused for multiple requests.
        try ([SecurityCenterManagementClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterManagementClient.html) client = [SecurityCenterManagementClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterManagementClient.html).create()) {
    
          String qualifiedModuleName =
              String.format(
                  "projects/%s/locations/global/eventThreatDetectionCustomModules/%s",
                  projectId, customModuleId);
    
          // Define the event threat detection custom module configuration, update the
          // DisplayName and EnablementState accordingly.
          [EventThreatDetectionCustomModule](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.EventThreatDetectionCustomModule.html) eventThreatDetectionCustomModule =
              [EventThreatDetectionCustomModule](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.EventThreatDetectionCustomModule.html).newBuilder()
                  .setName(qualifiedModuleName)
                  .setDisplayName("updated_custom_module_name")
                  .setEnablementState(EnablementState.DISABLED)
                  .build();
    
          // Set the field mask to specify which properties should be updated. In the below example we
          // are updating displayName and EnablementState
          // https://cloud.google.com/security-command-center/docs/reference/security-center-management/rest/v1/organizations.locations.eventThreatDetectionCustomModules/patch#query-parameters
          // https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask
          [FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html) fieldMask =
              [FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html).newBuilder().[addPaths](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.Builder.html#com_google_protobuf_FieldMask_Builder_addPaths_java_lang_String_)("display_name").[addPaths](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.Builder.html#com_google_protobuf_FieldMask_Builder_addPaths_java_lang_String_)("enablement_state").build();
    
          [UpdateEventThreatDetectionCustomModuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.UpdateEventThreatDetectionCustomModuleRequest.html) request =
              [UpdateEventThreatDetectionCustomModuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.UpdateEventThreatDetectionCustomModuleRequest.html).newBuilder()
                  .setEventThreatDetectionCustomModule(eventThreatDetectionCustomModule)
                  .setUpdateMask(fieldMask)
                  .build();
    
          [EventThreatDetectionCustomModule](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.EventThreatDetectionCustomModule.html) response =
              client.updateEventThreatDetectionCustomModule(request);
    
          return response;
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
    
    // Define the event threat detection custom module configuration, update the
    // EnablementState accordingly.
    const eventThreatDetectionCustomModule = {
      name: name,
      enablementState: 'DISABLED',
    };
    
    // Set the field mask to specify which properties should be updated.
    const fieldMask = {
      paths: ['enablement_state'],
    };
    
    // Build the request.
    const updateEventThreatDetectionCustomModuleRequest = {
      eventThreatDetectionCustomModule: eventThreatDetectionCustomModule,
      updateMask: fieldMask,
    };
    
    async function updateEventThreatDetectionCustomModule() {
      // Call the API.
      const [response] = await client.updateEventThreatDetectionCustomModule(
        updateEventThreatDetectionCustomModuleRequest
      );
      console.log('Updated EventThreatDetectionCustomModule: %j', response);
    }
    
    updateEventThreatDetectionCustomModule();

### Python

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def update_event_threat_detection_custom_module(parent: str, module_id: str):
        """
        Updates an Event Threat Detection Custom Module.
    
        Args:
            parent: Use any one of the following options:
                    - organizations/{organization_id}/locations/{location_id}
                    - folders/{folder_id}/locations/{location_id}
                    - projects/{project_id}/locations/{location_id}
        Returns:
            EventThreatDetectionCustomModule
        """
        client = securitycentermanagement_v1.SecurityCenterManagementClient()
    
        try:
    
            custom_module = securitycentermanagement_v1.EventThreatDetectionCustomModule(
                name=f"{parent}/eventThreatDetectionCustomModules/{module_id}",
                enablement_state=securitycentermanagement_v1.EventThreatDetectionCustomModule.EnablementState.DISABLED,
            )
    
            # Create the request
            request = securitycentermanagement_v1.UpdateEventThreatDetectionCustomModuleRequest(
                event_threat_detection_custom_module=custom_module,
                update_mask=FieldMask(paths=["enablement_state"]),
            )
    
            # Make the API call
            response = client.update_event_threat_detection_custom_module(request=request)
    
            print(f"Updated EventThreatDetectionCustomModule: {response.name}")
            return response
    
        except Exception as e:
            print(f"Failed to update EventThreatDetectionCustomModule: {e}")
            raise
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=securitycommandcenter). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
