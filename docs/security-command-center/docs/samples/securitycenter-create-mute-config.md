---
url: https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-create-mute-config/
title: Create a mute rule \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:15.239866+00:00
---

# Create a mute rule  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-create-mute-config/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Samples ](https://docs.cloud.google.com/security-command-center/docs/samples)



#  Create a mute rule Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates how to create a mute rule, which is a configuration that uses a filter to automatically mute future findings

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
    
    // createMuteRule: Creates a mute configuration under a given scope that will mute
    // all new findings that match a given filter.
    // Existing findings will not be muted.
    func createMuteRule(w io.Writer, parent string, muteConfigId string) error {
    	// parent: Use any one of the following options:
    	//             - organizations/{organization_id}
    	//             - folders/{folder_id}
    	//             - projects/{project_id}
    	// parent := fmt.Sprintf("projects/%s", "your-google-cloud-project-id")
    	// muteConfigId: Set a random id; max of 63 chars.
    	// muteConfigId := "random-mute-id-" + uuid.New().String()
    	ctx := context.Background()
    	client, err := securitycenter.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv1.html#cloud_google_com_go_securitycenter_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("securitycenter.NewClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv1.html#cloud_google_com_go_securitycenter_apiv1_Client_Close)()
    
    	muteConfig := &securitycenterpb.MuteConfig{
    		Description: "Mute low-medium IAM grants excluding 'compute' ",
    		// Set mute rule(s).
    		// To construct mute rules and for supported properties, see:
    		// https://cloud.google.com/security-command-center/docs/how-to-mute-findings#create_mute_rules
    		Filter: "severity=\"LOW\" OR severity=\"MEDIUM\" AND " +
    			"category=\"Persistence: IAM Anomalous Grant\" AND " +
    			"-resource.type:\"compute\"",
    	}
    
    	req := &securitycenterpb.CreateMuteConfigRequest{
    		Parent:       parent,
    		MuteConfigId: muteConfigId,
    		MuteConfig:   muteConfig,
    	}
    
    	response, err := client.CreateMuteConfig(ctx, req)
    	if err != nil {
    		return fmt.Errorf("failed to create mute rule: %w", err)
    	}
    	fmt.Fprintf(w, "Mute rule created successfully: %s", response.Name)
    	return nil
    }
    

### Java

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.securitycenter.v1.[CreateMuteConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.CreateMuteConfigRequest.html);
    import com.google.cloud.securitycenter.v1.[MuteConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.MuteConfig.html);
    import com.google.cloud.securitycenter.v1.[SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.SecurityCenterClient.html);
    import java.io.IOException;
    import java.util.UUID;
    
    public class CreateMuteRule {
    
      public static void main(String[] args) {
        // TODO: Replace the variables within {}
    
        // parentPath: Use any one of the following options:
        //             - organizations/{organization_id}
        //             - folders/{folder_id}
        //             - projects/{project_id}
        String parentPath = String.format("projects/%s", "your-google-cloud-project-id");
    
        // muteConfigId: Set a random id; max of 63 chars.
        String muteConfigId = "random-mute-id-" + UUID.randomUUID();
        createMuteRule(parentPath, muteConfigId);
      }
    
      // Creates a mute configuration under a given scope that will mute
      // all new findings that match a given filter.
      // Existing findings will not be muted.
      public static void createMuteRule(String parentPath, String muteConfigId) {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.SecurityCenterClient.html) client = [SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.SecurityCenterClient.html).create()) {
    
          [MuteConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.MuteConfig.html) muteConfig =
              [MuteConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.MuteConfig.html).newBuilder()
                  .setDescription("Mute low-medium IAM grants excluding 'compute' ")
                  // Set mute rule(s).
                  // To construct mute rules and for supported properties, see:
                  // https://cloud.google.com/security-command-center/docs/how-to-mute-findings#create_mute_rules
                  .setFilter(
                      "severity=\"LOW\" OR severity=\"MEDIUM\" AND "
                          + "category=\"Persistence: IAM Anomalous Grant\" AND "
                          + "-resource.type:\"compute\"")
                  .build();
    
          [CreateMuteConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.CreateMuteConfigRequest.html) request =
              [CreateMuteConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.CreateMuteConfigRequest.html).newBuilder()
                  .setParent(parentPath)
                  .[setMuteConfigId](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.CreateMuteConfigRequest.Builder.html#com_google_cloud_securitycenter_v1_CreateMuteConfigRequest_Builder_setMuteConfigId_java_lang_String_)(muteConfigId)
                  .setMuteConfig(muteConfig)
                  .build();
    
          // ExecutionException is thrown if the below call fails.
          [MuteConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.MuteConfig.html) response = client.createMuteConfig(request);
          System.out.println("Mute rule created successfully: " + response.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.MuteConfig.html#com_google_cloud_securitycenter_v1_MuteConfig_getName__)());
        } catch (IOException e) {
          System.out.println("Mute rule creation failed! \n Exception: " + e);
        }
      }
    }

### Python

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    
    def create_mute_rule(parent_path: str, mute_config_id: str) -> None:
        """
        Creates a mute configuration under a given scope that will mute
        all new findings that match a given filter.
        Existing findings will NOT BE muted.
        Args:
            parent_path: use any one of the following options:
                         - organizations/{organization_id}
                         - folders/{folder_id}
                         - projects/{project_id}
            mute_config_id: Set a unique id; max of 63 chars.
        """
    
        from google.cloud import securitycenter
    
        client = securitycenter.SecurityCenterClient()
    
        mute_config = securitycenter.[MuteConfig](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.MuteConfig.html)()
        mute_config.description = "Mute low-medium IAM grants excluding 'compute' "
        # Set mute rule(s).
        # To construct mute rules and for supported properties, see:
        # https://cloud.google.com/security-command-center/docs/how-to-mute-findings#create_mute_rules
        mute_config.filter = (
            'severity="LOW" OR severity="MEDIUM" AND '
            'category="Persistence: IAM Anomalous Grant" AND '
            '-resource.type:"compute"'
        )
    
        request = securitycenter.[CreateMuteConfigRequest](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.CreateMuteConfigRequest.html)()
        request.parent = parent_path
        request.mute_config_id = mute_config_id
        request.mute_config = mute_config
    
        mute_config = client.[create_mute_config](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_create_mute_config)(request=request)
        print(f"Mute rule created successfully: {mute_config.name}")
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=securitycommandcenter). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
