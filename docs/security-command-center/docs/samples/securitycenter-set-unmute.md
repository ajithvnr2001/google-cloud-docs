---
url: https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-set-unmute/
title: Unmute a finding \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:32:11.887042+00:00
---

# Unmute a finding  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-set-unmute/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Samples ](https://docs.cloud.google.com/security-command-center/docs/samples)



#  Unmute a finding Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates how to manually unmute an individual finding

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
    
    // setMute mutes an individual finding, can also unmute or reset the mute state of a finding.
    // If a finding is already muted, muting it again has no effect.
    // Various mute states are: UNDEFINED/MUTE/UNMUTE.
    func setUnmute(w io.Writer, findingPath string) error {
    	// findingPath: The relative resource name of the finding. See:
    	// https://cloud.google.com/apis/design/resource_names#relative_resource_name
    	// Use any one of the following formats:
    	//  - organizations/{organization_id}/sources/{source_id}/finding/{finding_id}
    	//  - folders/{folder_id}/sources/{source_id}/finding/{finding_id}
    	//  - projects/{project_id}/sources/{source_id}/finding/{finding_id}
    	// findingPath := fmt.Sprintf("projects/%s/sources/%s/finding/%s", "your-google-cloud-project-id", "source", "finding-id")
    	ctx := context.Background()
    	client, err := securitycenter.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv1.html#cloud_google_com_go_securitycenter_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("securitycenter.NewClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv1.html#cloud_google_com_go_securitycenter_apiv1_Client_Close)()
    
    	req := &securitycenterpb.SetMuteRequest{
    		Name: findingPath,
    		Mute: securitycenterpb.[Finding_UNMUTED](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv1/securitycenterpb.html#cloud_google_com_go_securitycenter_apiv1_securitycenterpb_Finding_MUTE_UNSPECIFIED_Finding_MUTED_Finding_UNMUTED_Finding_UNDEFINED)}
    
    	finding, err := client.SetMute(ctx, req)
    	if err != nil {
    		return fmt.Errorf("failed to set the specified mute value: %w", err)
    	}
    	fmt.Fprintf(w, "Mute value for the finding: %s is %s", finding.Name, finding.Mute)
    	return nil
    }
    

### Java

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.securitycenter.v1.[Finding](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Finding.html);
    import com.google.cloud.securitycenter.v1.[Finding](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Finding.html).[Mute](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Finding.Mute.html);
    import com.google.cloud.securitycenter.v1.[SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.SecurityCenterClient.html);
    import com.google.cloud.securitycenter.v1.[SetMuteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.SetMuteRequest.html);
    import java.io.IOException;
    
    public class SetUnmuteFinding {
    
      public static void main(String[] args) throws IOException {
        // TODO: Replace the variables within {}
    
        // findingPath: The relative resource name of the finding. See:
        // https://cloud.google.com/apis/design/resource_names#relative_resource_name
        // Use any one of the following formats:
        //  - organizations/{organization_id}/sources/{source_id}/finding/{finding_id}
        //  - folders/{folder_id}/sources/{source_id}/finding/{finding_id}
        //  - projects/{project_id}/sources/{source_id}/finding/{finding_id}
        String findingPath = "{path-to-the-finding}";
        setUnmute(findingPath);
      }
    
      // Unmute an individual finding.
      // Unmuting a finding that isn't muted has no effect.
      // Various mute states are: MUTE_UNSPECIFIED/MUTE/UNMUTE.
      public static [Finding](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Finding.html) setUnmute(String findingPath) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.SecurityCenterClient.html) client = [SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.SecurityCenterClient.html).create()) {
    
          [SetMuteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.SetMuteRequest.html) setMuteRequest =
              [SetMuteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.SetMuteRequest.html).newBuilder().setName(findingPath).setMute([Mute](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Finding.Mute.html).UNMUTED).build();
    
          [Finding](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Finding.html) finding = client.setMute(setMuteRequest);
          System.out.println(
              "Mute value for the finding " + finding.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Finding.html#com_google_cloud_securitycenter_v1_Finding_getName__)() + " is: " + finding.[getMute](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Finding.html#com_google_cloud_securitycenter_v1_Finding_getMute__)());
          return finding;
        }
      }
    }

### Python

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def set_unmute_finding(finding_path: str) -> None:
        """
          Unmute an individual finding.
          Unmuting a finding that isn't muted has no effect.
          Various mute states are: MUTE_UNSPECIFIED/MUTE/UNMUTE.
        Args:
            finding_path: The relative resource name of the finding. See:
            https://cloud.google.com/apis/design/resource_names#relative_resource_name
            Use any one of the following formats:
            - organizations/{organization_id}/sources/{source_id}/finding/{finding_id},
            - folders/{folder_id}/sources/{source_id}/finding/{finding_id},
            - projects/{project_id}/sources/{source_id}/finding/{finding_id}.
        """
        from google.cloud import securitycenter
    
        client = securitycenter.SecurityCenterClient()
    
        request = securitycenter.[SetMuteRequest](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.SetMuteRequest.html)()
        request.name = finding_path
        request.mute = securitycenter.Finding.Mute.UNMUTED
    
        finding = client.[set_mute](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_set_mute)(request)
        print(f"Mute value for the finding: {finding.mute.name}")
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=securitycommandcenter). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
