---
url: https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-update-mute-config/
title: Update a mute rule \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:31:36.876739+00:00
---

# Update a mute rule  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-update-mute-config/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Samples ](https://docs.cloud.google.com/security-command-center/docs/samples)



#  Update a mute rule Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates how to update a mute rule

## Code sample

### Go

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	securitycenter "cloud.google.com/go/securitycenter/apiv1"
    	"cloud.google.com/go/securitycenter/apiv1/securitycenterpb"
    	"google.golang.org/protobuf/types/known/fieldmaskpb"
    )
    
    // updateMuteRule Updates an existing mute configuration.
    // The following can be updated in a mute config: description and filter.
    func updateMuteRule(w io.Writer, muteConfigName string) error {
    	// Specify the name of the mute config to delete.
    	// muteConfigName: Use any one of the following formats:
    	//                 - organizations/{organization}/muteConfigs/{config_id}
    	//                 - folders/{folder}/muteConfigs/{config_id}
    	//                 - projects/{project}/muteConfigs/{config_id}
    	// muteConfigName := fmt.Sprintf("projects/%s/muteConfigs/%s", "project-id", "mute-config")
    	ctx := context.Background()
    	client, err := securitycenter.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv1.html#cloud_google_com_go_securitycenter_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("securitycenter.NewClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv1.html#cloud_google_com_go_securitycenter_apiv1_Client_Close)()
    
    	updateMuteConfig := &securitycenterpb.MuteConfig{
    		Name:        muteConfigName,
    		Description: "Updated mute config description",
    	}
    
    	req := &securitycenterpb.UpdateMuteConfigRequest{
    		MuteConfig: updateMuteConfig,
    		// Set the update mask to specify which properties of the mute config should be
    		// updated.
    		// If empty, all mutable fields will be updated.
    		// Make sure that the mask fields match the properties changed in 'updateMuteConfig'.
    		// For more info on constructing update mask path, see the proto or:
    		// https://cloud.google.com/security-command-center/docs/reference/rest/v1/folders.muteConfigs/patch?hl=en#query-parameters
    		UpdateMask: &fieldmaskpb.FieldMask{
    			Paths: []string{
    				"description",
    			},
    		},
    	}
    
    	response, err := client.UpdateMuteConfig(ctx, req)
    	if err != nil {
    		return fmt.Errorf("mute rule update failed! %w", err)
    	}
    	fmt.Fprintf(w, "Mute rule updated %s", response.Name)
    	return nil
    }
    

### Java

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.securitycenter.v1.[MuteConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.MuteConfig.html);
    import com.google.cloud.securitycenter.v1.[SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.SecurityCenterClient.html);
    import com.google.cloud.securitycenter.v1.[UpdateMuteConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.UpdateMuteConfigRequest.html);
    import com.google.protobuf.[FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html);
    import java.io.IOException;
    
    public class UpdateMuteRule {
    
      public static void main(String[] args) {
        // TODO: Replace the variables within {}
    
        // Specify the name of the mute config to delete.
        // muteConfigName: Use any one of the following formats:
        //                 - organizations/{organization}/muteConfigs/{config_id}
        //                 - folders/{folder}/muteConfigs/{config_id}
        //                 - projects/{project}/muteConfigs/{config_id}
        String muteConfigName = "{any-one-of-the-above-formats}";
        updateMuteRule(muteConfigName);
      }
    
      // Updates an existing mute configuration.
      // The following can be updated in a mute config: description and filter.
      public static void updateMuteRule(String muteConfigName) {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.SecurityCenterClient.html) securityCenterClient = [SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.SecurityCenterClient.html).create()) {
    
          [MuteConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.MuteConfig.html) updateMuteConfig =
              [MuteConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.MuteConfig.html).newBuilder()
                  .setName(muteConfigName)
                  .setDescription("Updated mute config description")
                  .build();
    
          [UpdateMuteConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.UpdateMuteConfigRequest.html) updateMuteConfigRequest =
              [UpdateMuteConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.UpdateMuteConfigRequest.html).newBuilder()
                  .setMuteConfig(updateMuteConfig)
                  // Set the update mask to specify which properties of the mute config should be
                  // updated.
                  // If empty, all mutable fields will be updated.
                  // Make sure that the mask fields match the properties changed in 'updateMuteConfig'.
                  // For more info on constructing update mask path, see the proto or:
                  // https://cloud.google.com/security-command-center/docs/reference/rest/v1/folders.muteConfigs/patch?hl=en#query-parameters
                  .setUpdateMask([FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html).newBuilder().[addPaths](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.Builder.html#com_google_protobuf_FieldMask_Builder_addPaths_java_lang_String_)("description").build())
                  .build();
    
          [MuteConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.MuteConfig.html) response = securityCenterClient.updateMuteConfig(updateMuteConfigRequest);
          System.out.println(response);
        } catch (IOException e) {
          System.out.println("Mute rule update failed! \n Exception: " + e);
        }
      }
    }

### Python

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def update_mute_rule(mute_config_name: str) -> None:
        """
        Updates an existing mute configuration.
        The following can be updated in a mute config: description, and filter/ mute rule.
        Args:
            mute_config_name: Specify the name of the mute config to delete.
                              Use any one of the following formats:
                              - organizations/{organization}/muteConfigs/{config_id}
                              - folders/{folder}/muteConfigs/{config_id}
                              - projects/{project}/muteConfigs/{config_id}
        """
        from google.cloud import securitycenter
        from google.protobuf import field_mask_pb2
    
        client = securitycenter.SecurityCenterClient()
    
        update_mute_config = securitycenter.[MuteConfig](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.MuteConfig.html)()
        update_mute_config.name = mute_config_name
        update_mute_config.description = "Updated mute config description"
    
        field_mask = field_mask_pb2.FieldMask(paths=["description"])
    
        request = securitycenter.[UpdateMuteConfigRequest](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.UpdateMuteConfigRequest.html)()
        request.mute_config = update_mute_config
        # Set the update mask to specify which properties of the Mute Config should be updated.
        # If empty, all mutable fields will be updated.
        # Make sure that the mask fields match the properties changed in 'update_mute_config'.
        # For more info on constructing update mask path, see the proto or:
        # https://cloud.google.com/security-command-center/docs/reference/rest/v1/folders.muteConfigs/patch?hl=en#query-parameters
        request.update_mask = field_mask
    
        mute_config = client.[update_mute_config](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_update_mute_config)(request)
        print(f"Updated mute rule : {mute_config}")
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=securitycommandcenter). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
