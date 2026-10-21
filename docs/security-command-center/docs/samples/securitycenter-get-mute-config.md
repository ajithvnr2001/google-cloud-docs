---
url: https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-get-mute-config/
title: View a mute rule \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:48:09.843953+00:00
---

# View a mute rule  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-get-mute-config/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Samples ](https://docs.cloud.google.com/security-command-center/docs/samples)



#  View a mute rule Stay organized with collections  Save and categorize content based on your preferences. 

Sample code to view a mute rule

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
    
    // getMuteRule retrieves a mute configuration given its resource name.
    func getMuteRule(w io.Writer, parent string, muteConfigId string) error {
    	// Use any one of the following resource paths to get mute configuration:
    	//         - organizations/{organization_id}
    	//         - folders/{folder_id}
    	//         - projects/{project_id}
    	// parent := fmt.Sprintf("projects/%s", "your-google-cloud-project-id")
    	//
    	// Name of the mute config to retrieve.
    	// muteConfigId := "mute-config-id"
    	ctx := context.Background()
    	client, err := securitycenter.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv1.html#cloud_google_com_go_securitycenter_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("securitycenter.NewClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv1.html#cloud_google_com_go_securitycenter_apiv1_Client_Close)()
    
    	req := &securitycenterpb.GetMuteConfigRequest{
    		Name: fmt.Sprintf("%s/muteConfigs/%s", parent, muteConfigId),
    	}
    
    	muteconfig, err := client.GetMuteConfig(ctx, req)
    	if err != nil {
    		return fmt.Errorf("Failed to retrieve Muteconfig: %w", err)
    	}
    	fmt.Fprintf(w, "Muteconfig Name: %s ", muteconfig.Name)
    	return nil
    }
    

### Java

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.securitycenter.v1.[MuteConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.MuteConfig.html);
    import com.google.cloud.securitycenter.v1.[MuteConfigName](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.MuteConfigName.html);
    import com.google.cloud.securitycenter.v1.[SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.SecurityCenterClient.html);
    import java.io.IOException;
    
    public class GetMuteRule {
    
      public static void main(String[] args) {
        // TODO(Developer): Replace the following variables
    
        // parentPath: Use any one of the following options:
        //             - organizations/{organization_id}
        //             - folders/{folder_id}
        //             - projects/{project_id}
        String parentPath = String.format("projects/%s", "your-google-cloud-project-id");
    
        // muteConfigId: Name of the mute config to retrieve.
        String muteConfigId = "mute-config-id";
    
        getMuteRule(parentPath, muteConfigId);
      }
    
      // Retrieves a mute configuration given its resource name.
      public static void getMuteRule(String projectId, String muteConfigId) {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.SecurityCenterClient.html) client = [SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.SecurityCenterClient.html).create()) {
          // Use appropriate MuteConfigName methods depending on the type of parent.
          // (org -> MuteConfigName.ofOrganizationMuteConfigName()
          // folder -> MuteConfigName.ofFolderMuteConfigName()
          // project -> MuteConfigName.ofProjectMuteConfigName)
          [MuteConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.MuteConfig.html) muteConfig =
              client.getMuteConfig([MuteConfigName](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.MuteConfigName.html).[ofProjectMuteConfigName](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.MuteConfigName.html#com_google_cloud_securitycenter_v1_MuteConfigName_ofProjectMuteConfigName_java_lang_String_java_lang_String_)(projectId, muteConfigId));
    
          System.out.println("Retrieved the mute config: " + muteConfig);
        } catch (IOException e) {
          System.out.println("Mute rule retrieval failed! \n Exception: " + e);
        }
      }
    }

### Python

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def get_mute_rule(mute_config_name: str) -> None:
        """
        Retrieves a mute configuration given its resource name.
        Args:
            mute_config_name: Name of the mute config to retrieve.
                              Use any one of the following formats:
                              - organizations/{organization}/muteConfigs/{config_id}
                              - folders/{folder}/muteConfigs/{config_id}
                              - projects/{project}/muteConfigs/{config_id}
        """
        from google.cloud import securitycenter
    
        client = securitycenter.SecurityCenterClient()
    
        request = securitycenter.[GetMuteConfigRequest](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.GetMuteConfigRequest.html)()
        request.name = mute_config_name
    
        mute_config = client.[get_mute_config](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_get_mute_config)(request)
        print(f"Retrieved the mute rule: {mute_config.name}")
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=securitycommandcenter). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
