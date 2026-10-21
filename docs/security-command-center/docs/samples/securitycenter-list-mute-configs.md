---
url: https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-list-mute-configs/
title: List mute rules \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:49:50.465260+00:00
---

# List mute rules  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-list-mute-configs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Samples ](https://docs.cloud.google.com/security-command-center/docs/samples)



#  List mute rules Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates how to list all mute rules, for your organizations, folders, or projects

## Code sample

### Go

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	securitycenter "cloud.google.com/go/securitycenter/apiv1"
    	"cloud.google.com/go/securitycenter/apiv1/securitycenterpb"
    	"google.golang.org/api/iterator"
    )
    
    // listMuteRules lists mute configs at the organization level will return all the configs
    // at the org, folder, and project levels.
    // Similarly, listing configs at folder level will list all the configs
    // at the folder and project levels.
    func listMuteRules(w io.Writer, parent string) error {
    	// Use any one of the following resource paths to list mute configurations:
    	//         - organizations/{organization_id}
    	//         - folders/{folder_id}
    	//         - projects/{project_id}
    	// parent := fmt.Sprintf("projects/%s", "your-google-cloud-project-id")
    	ctx := context.Background()
    	client, err := securitycenter.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv1.html#cloud_google_com_go_securitycenter_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("securitycenter.NewClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv1.html#cloud_google_com_go_securitycenter_apiv1_Client_Close)()
    
    	req := &securitycenterpb.ListMuteConfigsRequest{Parent: parent}
    
    	// List all mute configs present in the resource.
    	it := client.ListMuteConfigs(ctx, req)
    	for {
    		muteconfig, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			return fmt.Errorf("it.Next: %w", err)
    		}
    		fmt.Fprintf(w, "Muteconfig Name: %s, ", muteconfig.Name)
    	}
    	return nil
    }
    

### Java

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.securitycenter.v1.[ListMuteConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.ListMuteConfigsRequest.html);
    import com.google.cloud.securitycenter.v1.[MuteConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.MuteConfig.html);
    import com.google.cloud.securitycenter.v1.[SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.SecurityCenterClient.html);
    import java.io.IOException;
    
    public class ListMuteRules {
    
      public static void main(String[] args) {
        // TODO: Replace variables enclosed within {}
    
        // parent: Use any one of the following resource paths to list mute configurations:
        //         - organizations/{organization_id}
        //         - folders/{folder_id}
        //         - projects/{project_id}
        String parentPath = String.format("projects/%s", "your-google-cloud-project-id");
        listMuteRules(parentPath);
      }
    
      // Listing mute configs at the organization level will return all the configs
      // at the org, folder, and project levels.
      // Similarly, listing configs at folder level will list all the configs
      // at the folder and project levels.
      public static void listMuteRules(String parent) {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.SecurityCenterClient.html) client = [SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.SecurityCenterClient.html).create()) {
    
          [ListMuteConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.ListMuteConfigsRequest.html) listMuteConfigsRequest =
              [ListMuteConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.ListMuteConfigsRequest.html).newBuilder().setParent(parent).build();
    
          // List all mute configs present in the resource.
          for ([MuteConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.MuteConfig.html) muteConfig : client.listMuteConfigs(listMuteConfigsRequest).iterateAll()) {
            System.out.println(muteConfig.getName());
          }
        } catch (IOException e) {
          System.out.println("Listing Mute rule failed! \n Exception: " + e);
        }
      }
    }

### Python

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def list_mute_rules(parent: str) -> None:
        """
        Listing mute configs at organization level will return all the configs
        at the org, folder and project levels.
        Similarly, listing configs at folder level will list all the configs
        at the folder and project levels.
        Args:
            parent: Use any one of the following resource paths to list mute configurations:
                    - organizations/{organization_id}
                    - folders/{folder_id}
                    - projects/{project_id}
        """
        from google.cloud import securitycenter
    
        client = securitycenter.SecurityCenterClient()
    
        request = securitycenter.[ListMuteConfigsRequest](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.ListMuteConfigsRequest.html)()
        request.parent = parent
    
        # List all Mute Configs present in the resource.
        for mute_config in client.[list_mute_configs](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_list_mute_configs)(request):
            print(mute_config.name)
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=securitycommandcenter). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
