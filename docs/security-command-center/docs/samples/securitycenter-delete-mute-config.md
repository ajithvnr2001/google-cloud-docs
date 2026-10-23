---
url: https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-delete-mute-config/
title: Delete a mute rule \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:15.298721+00:00
---

# Delete a mute rule  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-delete-mute-config/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Samples ](https://docs.cloud.google.com/security-command-center/docs/samples)



#  Delete a mute rule Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates how to delete a mute rule

## Code sample

### Go

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	securitycenter "cloud.google.com/go/securitycenter/apiv1"
    	"cloud.google.com/go/securitycenter/apiv1/securitycenterpb"
    )
    
    // deleteMuteRule deletes a mute configuration given its resource name.
    // Note: Previously muted findings are not affected when a mute config is deleted.
    func deleteMuteRule(w io.Writer, parent string, muteConfigId string) error {
    	// parent: Use any one of the following options:
    	//             - organizations/{organization_id}
    	//             - folders/{folder_id}
    	//             - projects/{project_id}
    	// parent := fmt.Sprintf("projects/%s", "your-google-cloud-project-id")
    	//
    	// muteConfigId: Specify the name of the mute config to delete.
    	// muteConfigId := "mute-config-id"
    	ctx := context.Background()
    	client, err := securitycenter.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv1.html#cloud_google_com_go_securitycenter_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("securitycenter.NewClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv1.html#cloud_google_com_go_securitycenter_apiv1_Client_Close)()
    
    	req := &securitycenterpb.DeleteMuteConfigRequest{
    		Name: fmt.Sprintf("%s/muteConfigs/%s", parent, muteConfigId),
    	}
    
    	if err := client.DeleteMuteConfig(ctx, req); err != nil {
    		return fmt.Errorf("failed to delete Muteconfig: %w", err)
    	}
    	fmt.Fprintf(w, "Mute rule deleted successfully: %s", muteConfigId)
    	return nil
    }
    

### Java

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.securitycenter.v1.[MuteConfigName](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.MuteConfigName.html);
    import com.google.cloud.securitycenter.v1.[SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.SecurityCenterClient.html);
    import java.io.IOException;
    
    public class DeleteMuteRule {
    
      public static void main(String[] args) {
        // TODO(Developer): Replace the following variables
        // parentPath: Use any one of the following options:
        //             - organizations/{organization_id}
        //             - folders/{folder_id}
        //             - projects/{project_id}
        String parentPath = String.format("projects/%s", "your-google-cloud-project-id");
    
        // muteConfigId: Specify the name of the mute config to delete.
        String muteConfigId = "mute-config-id";
    
        deleteMuteRule(parentPath, muteConfigId);
      }
    
      // Deletes a mute configuration given its resource name.
      // Note: Previously muted findings are not affected when a mute config is deleted.
      public static void deleteMuteRule(String projectId, String muteConfigId) {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.SecurityCenterClient.html) client = [SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.SecurityCenterClient.html).create()) {
          // Use appropriate MuteConfigName methods depending on the type of parent.
          // org -> MuteConfigName.ofOrganizationMuteConfigName()
          // folder -> MuteConfigName.ofFolderMuteConfigName()
          // project -> MuteConfigName.ofProjectMuteConfigName)
          client.deleteMuteConfig([MuteConfigName](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.MuteConfigName.html).[ofProjectMuteConfigName](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.MuteConfigName.html#com_google_cloud_securitycenter_v1_MuteConfigName_ofProjectMuteConfigName_java_lang_String_java_lang_String_)(projectId, muteConfigId));
    
          System.out.println("Mute rule deleted successfully: " + muteConfigId);
        } catch (IOException e) {
          System.out.println("Mute rule deletion failed! \n Exception: " + e);
        }
      }
    }

### Python

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def delete_mute_rule(mute_config_name: str) -> None:
        """
        Deletes a mute configuration given its resource name.
        Note: Previously muted findings are not affected when a mute config is deleted.
        Args:
            mute_config_name: Specify the name of the mute config to delete.
                              Use any one of the following formats:
                              - organizations/{organization}/muteConfigs/{config_id}
                              - folders/{folder}/muteConfigs/{config_id} or
                              - projects/{project}/muteConfigs/{config_id}
        """
        from google.cloud import securitycenter
    
        client = securitycenter.SecurityCenterClient()
    
        request = securitycenter.[DeleteMuteConfigRequest](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.DeleteMuteConfigRequest.html)()
        request.name = mute_config_name
    
        client.[delete_mute_config](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_delete_mute_config)(request)
        print(f"Mute rule deleted successfully: {mute_config_name}")
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=securitycommandcenter). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
