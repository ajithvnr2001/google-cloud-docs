---
url: https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-bulk-mute/
title: Bulk-mute findings \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:47:36.566450+00:00
---

# Bulk-mute findings  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-bulk-mute/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Samples ](https://docs.cloud.google.com/security-command-center/docs/samples)



#  Bulk-mute findings Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates how to bulk-mute existing findings based on filters that you specify

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
    
    // bulkMute kicks off a long-running operation (LRO) to bulk mute findings for a parent based on a filter.
    // The parent can be either an organization, folder, or project. The findings
    // matched by the filter will be muted after the LRO is done.
    func bulkMute(w io.Writer, parent string, muteRule string) error {
    	// parent: Use any one of the following options:
    	//             - organizations/{organization_id}
    	//             - folders/{folder_id}
    	//             - projects/{project_id}
    	// parent := fmt.Sprintf("projects/%s", "your-google-cloud-project-id")
    	// muteRule: Expression that identifies findings that should be muted.
    	// To create mute rules, see:
    	// https://cloud.google.com/security-command-center/docs/how-to-mute-findings#create_mute_rules
    	// muteRule := "filter-condition"
    	ctx := context.Background()
    	client, err := securitycenter.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv1.html#cloud_google_com_go_securitycenter_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("securitycenter.NewClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv1.html#cloud_google_com_go_securitycenter_apiv1_Client_Close)()
    
    	req := &securitycenterpb.BulkMuteFindingsRequest{
    		Parent: parent,
    		Filter: muteRule,
    	}
    
    	op, err := client.BulkMuteFindings(ctx, req)
    	if err != nil {
    		return fmt.Errorf("failed to bulk mute findings: %w", err)
    	}
    	response, err := op.Wait(ctx)
    	if err != nil {
    		return fmt.Errorf("failed to bulk mute findings: %w", err)
    	}
    	fmt.Fprintf(w, "Bulk mute findings completed successfully! %s", response)
    	return nil
    }
    

### Java

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.securitycenter.v1.[BulkMuteFindingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.BulkMuteFindingsRequest.html);
    import com.google.cloud.securitycenter.v1.[BulkMuteFindingsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.BulkMuteFindingsResponse.html);
    import com.google.cloud.securitycenter.v1.[SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.SecurityCenterClient.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    
    public class BulkMuteFindings {
    
      public static void main(String[] args) {
        // TODO: Replace the variables within {}
    
        // parentPath: Use any one of the following options:
        //             - organizations/{organization_id}
        //             - folders/{folder_id}
        //             - projects/{project_id}
        String parentPath = String.format("projects/%s", "your-google-cloud-project-id");
    
        // muteRule: Expression that identifies findings that should be muted.
        // eg: "resource.project_display_name=\"PROJECT_ID\""
        String muteRule = "{filter-condition}";
    
        bulkMute(parentPath, muteRule);
      }
    
      // Kicks off a long-running operation (LRO) to bulk mute findings for a parent based on a filter.
      // The parent can be either an organization, folder, or project. The findings
      // matched by the filter will be muted after the LRO is done.
      public static void bulkMute(String parentPath, String muteRule) {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.SecurityCenterClient.html) client = [SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.SecurityCenterClient.html).create()) {
    
          [BulkMuteFindingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.BulkMuteFindingsRequest.html) bulkMuteFindingsRequest =
              [BulkMuteFindingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.BulkMuteFindingsRequest.html).newBuilder()
                  .setParent(parentPath)
                  // To create mute rules, see:
                  // https://cloud.google.com/security-command-center/docs/how-to-mute-findings#create_mute_rules
                  .setFilter(muteRule)
                  .build();
    
          // ExecutionException is thrown if the below call fails.
          [BulkMuteFindingsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.BulkMuteFindingsResponse.html) response =
              client.[bulkMuteFindingsAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.SecurityCenterClient.html#com_google_cloud_securitycenter_v1_SecurityCenterClient_bulkMuteFindingsAsync__org_jspecify_annotations_Nullable_com_google_api_resourcenames_ResourceName_)(bulkMuteFindingsRequest).get();
          System.out.println("Bulk mute findings completed successfully! " + response);
        } catch (IOException | InterruptedException | ExecutionException e) {
          System.out.println("Bulk mute findings failed! \n Exception: " + e);
        }
      }
    }

### Python

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def bulk_mute_findings(parent_path: str, mute_rule: str) -> None:
        """
          Kicks off a long-running operation (LRO) to bulk mute findings for a parent based on a filter.
          The parent can be either an organization, folder, or project. The findings
          matched by the filter will be muted after the LRO is done.
        Args:
            parent_path: use any one of the following options:
                         - organizations/{organization}
                         - folders/{folder}
                         - projects/{project}
            mute_rule: Expression that identifies findings that should be updated.
        """
        from google.cloud import securitycenter
    
        client = securitycenter.SecurityCenterClient()
    
        request = securitycenter.[BulkMuteFindingsRequest](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.BulkMuteFindingsRequest.html)()
        request.parent = parent_path
        # To create mute rules, see:
        # https://cloud.google.com/security-command-center/docs/how-to-mute-findings#create_mute_rules
        request.filter = mute_rule
    
        response = client.[bulk_mute_findings](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_bulk_mute_findings)(request)
        print(f"Bulk mute findings completed successfully! : {response}")
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=securitycommandcenter). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
