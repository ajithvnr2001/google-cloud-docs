---
url: https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-create-event-threat-detection-custom-module/
title: Create Event Threat Detection custom modules \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:16.461139+00:00
---

# Create Event Threat Detection custom modules  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-create-event-threat-detection-custom-module/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Samples ](https://docs.cloud.google.com/security-command-center/docs/samples)



#  Create Event Threat Detection custom modules Stay organized with collections  Save and categorize content based on your preferences. 

Sample code to create Event Threat Detection custom modules

## Code sample

### Go

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"regexp"
    
    	securitycentermanagement "cloud.google.com/go/securitycentermanagement/apiv1"
    	securitycentermanagementpb "cloud.google.com/go/securitycentermanagement/apiv1/securitycentermanagementpb"
    	"github.com/google/uuid"
    	"google.golang.org/protobuf/types/known/structpb"
    )
    
    // createEventThreatDetectionCustomModule creates a custom module for Event Threat Detection.
    func createEventThreatDetectionCustomModule(w io.Writer, parent string) error {
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
    
    	uniqueSuffix := uuid.New().String()
    
    	// Remove invalid characters (anything that isn't alphanumeric or an underscore)
    	re := regexp.MustCompile(`[^a-zA-Z0-9_]`)
    	uniqueSuffix = re.ReplaceAllString(uniqueSuffix, "_")
    
    	// Create unique display name
    	displayName := fmt.Sprintf("go_sample_etd_custom_module_%s", uniqueSuffix)
    
    	// Define the metadata and other config parameters as a map
    	configMap := map[string]interface{}{
    		"metadata": map[string]interface{}{
    			"severity": "MEDIUM",
    			//Replace with the desired description.
    			"description":    "Sample custom module for testing purpose. Please do not delete.",
    			"recommendation": "na",
    		},
    		"ips": []interface{}{"0.0.0.0"},
    	}
    
    	// Convert the map to a Struct
    	configStruct, err := structpb.NewStruct(configMap)
    	if err != nil {
    		return fmt.Errorf("structpb.NewStruct: %w", err)
    	}
    
    	// Define the Event Threat Detection custom module configuration
    	customModule := &securitycentermanagementpb.EventThreatDetectionCustomModule{
    		Config: configStruct,
    		//Replace with desired Display Name.
    		DisplayName:     displayName,
    		EnablementState: securitycentermanagementpb.[EventThreatDetectionCustomModule_ENABLED](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycentermanagement/latest/apiv1/securitycentermanagementpb.html#cloud_google_com_go_securitycentermanagement_apiv1_securitycentermanagementpb_EventThreatDetectionCustomModule_ENABLEMENT_STATE_UNSPECIFIED_EventThreatDetectionCustomModule_ENABLED_EventThreatDetectionCustomModule_DISABLED_EventThreatDetectionCustomModule_INHERITED),
    		Type:            "CONFIGURABLE_BAD_IP",
    	}
    
    	req := &securitycentermanagementpb.CreateEventThreatDetectionCustomModuleRequest{
    		Parent:                           parent,
    		EventThreatDetectionCustomModule: customModule,
    	}
    
    	module, err := client.CreateEventThreatDetectionCustomModule(ctx, req)
    	if err != nil {
    		return fmt.Errorf("failed to create EventThreatDetectionCustomModule: %w", err)
    	}
    
    	fmt.Fprintf(w, "Created EventThreatDetectionCustomModule: %s\n", module.Name)
    	return nil
    }
    

### Java

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.securitycentermanagement.v1.[CreateEventThreatDetectionCustomModuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.CreateEventThreatDetectionCustomModuleRequest.html);
    import com.google.cloud.securitycentermanagement.v1.[EventThreatDetectionCustomModule](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.EventThreatDetectionCustomModule.html);
    import com.google.cloud.securitycentermanagement.v1.[EventThreatDetectionCustomModule](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.EventThreatDetectionCustomModule.html).EnablementState;
    import com.google.cloud.securitycentermanagement.v1.[SecurityCenterManagementClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterManagementClient.html);
    import com.google.protobuf.[ListValue](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ListValue.html);
    import com.google.protobuf.[Struct](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Struct.html);
    import com.google.protobuf.[Value](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html);
    import java.io.IOException;
    import java.util.Arrays;
    import java.util.HashMap;
    import java.util.List;
    import java.util.Map;
    
    public class CreateEventThreatDetectionCustomModule {
    
      public static void main(String[] args) throws IOException {
        // https://cloud.google.com/security-command-center/docs/reference/security-center-management/rest/v1/organizations.locations.eventThreatDetectionCustomModules/create
        // TODO: Developer should replace project_id with a real project ID before running this code
        String projectId = "project_id";
    
        String customModuleDisplayName = "custom_module_display_name";
    
        createEventThreatDetectionCustomModule(projectId, customModuleDisplayName);
      }
    
      public static [EventThreatDetectionCustomModule](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.EventThreatDetectionCustomModule.html) createEventThreatDetectionCustomModule(
          String projectId, String customModuleDisplayName) throws IOException {
    
        // Initialize client that will be used to send requests. This client only needs
        // to be created
        // once, and can be reused for multiple requests.
        try ([SecurityCenterManagementClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterManagementClient.html) client = [SecurityCenterManagementClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterManagementClient.html).create()) {
    
          String parent = String.format("projects/%s/locations/global", projectId);
    
          // define the metadata and other config parameters severity, description,
          // recommendation and ips below
          Map<String, Value> metadata = new HashMap<>();
          metadata.put("severity", [Value](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html).newBuilder().setStringValue("MEDIUM").build());
          metadata.put(
              "description", [Value](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html).newBuilder().setStringValue("add your description here").build());
          metadata.put(
              "recommendation",
              [Value](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html).newBuilder().setStringValue("add your recommendation here").build());
          [List<Value>](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ListValue.html) ips = Arrays.asList([Value](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html).newBuilder().setStringValue("0.0.0.0").build());
    
          [Value](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html) metadataVal =
              [Value](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html).newBuilder()
                  .setStructValue([Struct](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Struct.html).newBuilder().[putAllFields](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Struct.Builder.html#com_google_protobuf_Struct_Builder_putAllFields_java_util_Map_java_lang_String_com_google_protobuf_Value__)(metadata).build())
                  .build();
          [Value](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html) ipsValue =
              [Value](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html).newBuilder().setListValue([ListValue](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ListValue.html).newBuilder().[addAllValues](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ListValue.Builder.html#com_google_protobuf_ListValue_Builder_addAllValues_java_lang_Iterable___extends_com_google_protobuf_Value__)(ips).build()).build();
    
          [Struct](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Struct.html) configStruct =
              [Struct](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Struct.html).newBuilder().putFields("metadata", metadataVal).putFields("ips", ipsValue).build();
    
          // define the Event Threat Detection custom module configuration, update the EnablementState
          // below
          [EventThreatDetectionCustomModule](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.EventThreatDetectionCustomModule.html) eventThreatDetectionCustomModule =
              [EventThreatDetectionCustomModule](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.EventThreatDetectionCustomModule.html).newBuilder()
                  .setConfig(configStruct)
                  .setDisplayName(customModuleDisplayName)
                  .setEnablementState(EnablementState.ENABLED)
                  .setType("CONFIGURABLE_BAD_IP")
                  .build();
    
          [CreateEventThreatDetectionCustomModuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.CreateEventThreatDetectionCustomModuleRequest.html) request =
              [CreateEventThreatDetectionCustomModuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.CreateEventThreatDetectionCustomModuleRequest.html).newBuilder()
                  .setParent(parent)
                  .setEventThreatDetectionCustomModule(eventThreatDetectionCustomModule)
                  .build();
    
          [EventThreatDetectionCustomModule](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.EventThreatDetectionCustomModule.html) response =
              client.createEventThreatDetectionCustomModule(request);
    
          return response;
        }
      }
    }

### Node.js

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google cloud client library.
    const {SecurityCenterManagementClient} =
      require('[@google-cloud/securitycentermanagement](https://docs.cloud.google.com/nodejs/docs/reference/securitycentermanagement/latest/overview.html)').v1;
    
    // Create a Security Center Management client
    const client = new [SecurityCenterManagementClient](https://docs.cloud.google.com/nodejs/docs/reference/securitycentermanagement/latest/overview.html)();
    
    /**
     *  Required. The name of the parent resource of the create event threat detection module. Its
     *  format is "organizations/[organization_id]/locations/[location_id]",
     *  "folders/[folder_id]/locations/[location_id]", or
     *  "projects/[project_id]/locations/[location_id]".
     */
    //TODO(developer): Update the following references for your own environment before running the sample.
    // const organizationId = 'YOUR_ORGANIZATION_ID';
    // const location = 'LOCATION_ID';
    const parent = `organizations/${organizationId}/locations/${location}`;
    
    // define the event threat detection custom module configuration, update the EnablementState
    // below
    const eventThreatDetectionCustomModule = {
      displayName: customModuleDisplayName,
      enablementState: 'ENABLED',
      type: 'CONFIGURABLE_BAD_IP',
      config: prepareConfigDetails(),
    };
    
    // Build the request.
    const createEventThreatDetectionCustomModuleRequest = {
      parent: parent,
      eventThreatDetectionCustomModule: eventThreatDetectionCustomModule,
    };
    
    async function createEventThreatDetectionCustomModule() {
      // Call the API.
      const [response] = await client.createEventThreatDetectionCustomModule(
        createEventThreatDetectionCustomModuleRequest
      );
      console.log('EventThreatDetectionCustomModule created : %j', response);
    }
    
    function prepareConfigDetails() {
      // define the metadata and other config parameters severity, description,
      // recommendation and ips below
      const config = {
        fields: {
          metadata: {
            structValue: {
              fields: {
                severity: {stringValue: 'LOW'},
                description: {stringValue: 'Flagged by Cymbal as malicious'},
                recommendation: {
                  stringValue: 'Contact the owner of the relevant project.',
                },
              },
            },
          },
          ips: {
            listValue: {
              values: [{stringValue: '192.0.2.1'}, {stringValue: '192.0.2.0/24'}],
            },
          },
        },
      };
      return config;
    }
    
    createEventThreatDetectionCustomModule();

### Python

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def create_event_threat_detection_custom_module(parent: str) -> securitycentermanagement_v1.EventThreatDetectionCustomModule:
        """
        Creates a Event Threat Detection Custom Module.
    
        This custom module creates a configurable bad IP type custom module, which can be used to detect and block malicious IP addresses.
    
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
            # Generate a unique suffix
            unique_suffix = str(uuid.uuid4()).replace("-", "_")
            # Create unique display name
            display_name = f"python_sample_etd_custom_module_{unique_suffix}"
    
            # Define the metadata and other config parameters as a dictionary
            config_map = {
                "metadata": {
                    "severity": "MEDIUM",
                    "description": "Sample custom module for testing purposes. Please do not delete.",
                    "recommendation": "na",
                },
                "ips": ["0.0.0.0"],
            }
    
            # Convert the dictionary to a Struct
            config_struct = Struct()
            config_struct.update(config_map)
    
            # Define the Event Threat Detection custom module configuration
            custom_module = securitycentermanagement_v1.EventThreatDetectionCustomModule(
                config=config_struct,
                display_name=display_name,
                enablement_state=securitycentermanagement_v1.EventThreatDetectionCustomModule.EnablementState.ENABLED,
                type_="CONFIGURABLE_BAD_IP",
            )
    
            # Create the request
            request = securitycentermanagement_v1.CreateEventThreatDetectionCustomModuleRequest(
                parent=parent,
                event_threat_detection_custom_module=custom_module,
            )
    
            # Make the API call
            response = client.create_event_threat_detection_custom_module(request=request)
    
            print(f"Created EventThreatDetectionCustomModule: {response.name}")
            return response
    
        except GoogleAPICallError as e:
            print(f"Failed to create EventThreatDetectionCustomModule: {e}")
            raise
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=securitycommandcenter). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
