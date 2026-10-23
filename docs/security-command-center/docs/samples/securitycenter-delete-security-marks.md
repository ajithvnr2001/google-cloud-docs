---
url: https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-delete-security-marks/
title: Delete security marks \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:58:08.227967+00:00
---

# Delete security marks  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-delete-security-marks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Samples ](https://docs.cloud.google.com/security-command-center/docs/samples)



#  Delete security marks Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates how to delete security marks

## Code sample

### Go

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	securitycenter "cloud.google.com/go/securitycenter/apiv1"
    	"cloud.google.com/go/securitycenter/apiv1/securitycenterpb"
    	"google.golang.org/genproto/protobuf/field_mask"
    )
    
    // deleteSecurityMarks deletes security marks "key_a" and  "key_b" from
    // assetName's marks. assetName is the resource path for an asset.
    func deleteSecurityMarks(w io.Writer, assetName string) error {
    	// Specify the value of 'assetName' in one of the following formats:
    	// 		assetName := "organizations/{org_id}/assets/{asset_id}"
    	//		assetName := "projects/{project_id}/assets/{asset_id}"
    	//		assetName := "folders/{folder_id}/assets/{asset_id}"
    	// Instantiate a context and a security service client to make API calls.
    	ctx := context.Background()
    	client, err := securitycenter.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv1.html#cloud_google_com_go_securitycenter_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("securitycenter.NewClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv1.html#cloud_google_com_go_securitycenter_apiv1_Client_Close)() // Closing the client safely cleans up background resources.
    
    	req := &securitycenterpb.UpdateSecurityMarksRequest{
    		// If not set or empty, all marks would be cleared.
    		UpdateMask: &field_mask.FieldMask{
    			Paths: []string{"marks.key_a", "marks.key_b"},
    		},
    		SecurityMarks: &securitycenterpb.SecurityMarks{
    			Name: fmt.Sprintf("%s/securityMarks", assetName),
    			// Intentionally not setting marks with the
    			// corresponding field mask deletes them.
    		},
    	}
    	updatedMarks, err := client.UpdateSecurityMarks(ctx, req)
    	if err != nil {
    		return fmt.Errorf("UpdateSecurityMarks: %w", err)
    	}
    
    	fmt.Fprintf(w, "Updated marks: %s\n", updatedMarks.Name)
    	for k, v := range updatedMarks.Marks {
    		fmt.Fprintf(w, "%s = %s\n", k, v)
    	}
    	return nil
    }
    

### Java

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    static SecurityMarks clearFromAsset(String assetName) {
      try (SecurityCenterClient client = SecurityCenterClient.create()) {
        // Specify the value of 'assetName' in one of the following formats:
        //    String assetName = "organizations/{org-id}/assets/{asset-id}";
        //    String assetName = "projects/{project-id}/assets/{asset-id}";
        //    String assetName = "folders/{folder-id}/assets/{asset-id}";
        // Start setting up a request to clear security marks for an asset.
        // Create security mark and field mask for clearing security marks.
        SecurityMarks securityMarks =
            SecurityMarks.newBuilder().setName(assetName + "/securityMarks").build();
        FieldMask updateMask =
            FieldMask.newBuilder().addPaths("marks.key_a").addPaths("marks.key_b").build();
    
        UpdateSecurityMarksRequest request =
            UpdateSecurityMarksRequest.newBuilder()
                .setSecurityMarks(securityMarks)
                .setUpdateMask(updateMask)
                .build();
    
        // Call the API.
        SecurityMarks response = client.updateSecurityMarks(request);
    
        System.out.println("Security Marks cleared:");
        System.out.println(response);
        return response;
      } catch (IOException e) {
        throw new RuntimeException("Couldn't create client.", e);
      }
    }

### Node.js

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud client library.
    const {SecurityCenterClient} = require('[@google-cloud/security-center](https://docs.cloud.google.com/nodejs/docs/reference/security-center/latest/overview.html)');
    
    // Creates a new client.
    const client = new [SecurityCenterClient](https://docs.cloud.google.com/nodejs/docs/reference/security-center/latest/overview.html)();
    
    async function deleteSecurityMarks() {
      // assetName is the full resource path for the asset to update.
      /*
       * TODO(developer): Uncomment the following lines
       */
      // Specify the value of 'assetName' in one of the following formats:
      //    `organizations/${org-id}/assets/${asset-id}`;
      //    `projects/${project-id}/assets/${asset-id}`;
      //    `folders/${folder-id}/assets/${asset-id}`;
      // const assetName = "organizations/123123342/assets/12312321";
      const [newMarks] = await client.updateSecurityMarks({
        securityMarks: {
          name: `${assetName}/securityMarks`,
          // Intentionally, not setting marks to delete them.
        },
        // Only delete marks for the following keys.
        updateMask: {paths: ['marks.key_a', 'marks.key_b']},
      });
    
      console.log('Updated marks: %j', newMarks);
    }
    deleteSecurityMarks();

### Python

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import securitycenter
    from google.protobuf import field_mask_pb2
    
    # Create a new client.
    client = securitycenter.SecurityCenterClient()
    
    # 'asset_name' is the resource path for an asset that exists in SCC.
    # Specify the value of 'asset_name' in one of the following formats:
    #   f"organizations/{org_id}/assets/{asset_id}"
    #   f"projects/{project_id}/assets/{asset_id}"
    #   f"folders/{folder_id}/assets/{asset_id}"
    # asset_name = organizations/123123342/assets/12312321
    marks_name = f"{asset_name}/securityMarks"
    
    field_mask = field_mask_pb2.FieldMask(paths=["marks.key_a", "marks.key_b"])
    
    updated_marks = client.[update_security_marks](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_update_security_marks)(
        request={
            "security_marks": {
                "name": marks_name
                # Note, no marks specified, so the specified values in
                # the fields masks will be deleted.
            },
            "update_mask": field_mask,
        }
    )
    print(updated_marks)

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=securitycommandcenter). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
