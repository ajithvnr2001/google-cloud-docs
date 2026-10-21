---
url: https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-add-finding-security-marks/
title: Add security marks to findings \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:48:10.477337+00:00
---

# Add security marks to findings  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-add-finding-security-marks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Samples ](https://docs.cloud.google.com/security-command-center/docs/samples)



#  Add security marks to findings Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates adding security marks to findings

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
    
    // addSecurityMarks adds/updates security marks for the findingName and
    // returns the updated marks. Specifically, it sets "key_a" an "key_b" to
    // "value_a" and "value_b" respectively. findingName is the resource path for
    // the finding to add marks to.
    func addSecurityMarks(w io.Writer, findingName string) error {
    	// Specify the value of 'findingName' in one of the following formats:
    	// 		"organizations/{orgId}/sources/{sourceId}/findings/{findingId}"
    	// 		"projects/{projectId}/sources/{sourceId}/findings/{findingId}"
    	// 		"folders/{folderId}/sources/{sourceId}/findings/{findingId}"
    	// Instantiate a context and a security service client to make API calls.
    	ctx := context.Background()
    	client, err := securitycenter.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv1.html#cloud_google_com_go_securitycenter_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("securitycenter.NewClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv1.html#cloud_google_com_go_securitycenter_apiv1_Client_Close)() // Closing the client safely cleans up background resources.
    
    	req := &securitycenterpb.UpdateSecurityMarksRequest{
    		// If not set or empty, all marks would be cleared before
    		// adding the new marks below.
    		UpdateMask: &field_mask.FieldMask{
    			Paths: []string{"marks.key_a", "marks.key_b"},
    		},
    		SecurityMarks: &securitycenterpb.SecurityMarks{
    			Name: fmt.Sprintf("%s/securityMarks", findingName),
    			// Note keys correspond to the last part of each path.
    			Marks: map[string]string{"key_a": "value_a", "key_b": "value_b"},
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
    
    
    static SecurityMarks addToFinding(FindingName findingName) {
      try (SecurityCenterClient client = SecurityCenterClient.create()) {
        // Start setting up a request to add security marks for a finding.
        ImmutableMap markMap = ImmutableMap.of("key_a", "value_a", "key_b", "value_b");
    
        // Specify the value of 'findingName' in one of the following formats:
        //    FindingName.ofOrganizationSourceFindingName("org-id", "source", "finding-id");
        //    FindingName.ofProjectSourceFindingName("project-id", "source", "finding-id");
        //    FindingName.ofFolderSourceFindingName("folder-id", "source", "finding-id");
        // Add security marks and field mask for security marks.
        SecurityMarks securityMarks =
            SecurityMarks.newBuilder()
                .setName(findingName + "/securityMarks")
                .putAllMarks(markMap)
                .build();
        FieldMask updateMask =
            FieldMask.newBuilder().addPaths("marks.key_a").addPaths("marks.key_b").build();
    
        UpdateSecurityMarksRequest request =
            UpdateSecurityMarksRequest.newBuilder()
                .setSecurityMarks(securityMarks)
                .setUpdateMask(updateMask)
                .build();
    
        // Call the API.
        SecurityMarks response = client.updateSecurityMarks(request);
    
        System.out.println("Security Marks:");
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
    
    async function addFindingSecurityMarks() {
      // findingName is the full resource path for the finding to update.
      /*
       * TODO(developer): Uncomment the following lines
       */
      // Specify the value of 'findingName' in one of the following formats:
      //    `organizations/${org-id}/assets/${asset-id}/findings/${finding-id}`;
      //    `projects/${project-id}/assets/${asset-id}/findings/${finding-id}`;
      //    `folders/${folder-id}/assets/${asset-id}/findings/${finding-id}`;
      const [newMarks] = await client.updateSecurityMarks({
        securityMarks: {
          name: `${findingName}/securityMarks`,
          marks: {key_a: 'value_a', key_b: 'value_b'},
        },
        // Only update the marks with these keys.
        updateMask: {paths: ['marks.key_a', 'marks.key_b']},
      });
    
      console.log('New marks: %j', newMarks);
    }
    addFindingSecurityMarks();

### Python

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import securitycenter
    from google.protobuf import field_mask_pb2
    
    client = securitycenter.SecurityCenterClient()
    # 'finding_name' is the resource path for a finding that exists in SCC.
    # Specify the value of 'asset_name' in one of the following formats:
    #   f"organizations/{org_id}/assets/{asset_id}"
    #   f"projects/{project_id}/assets/{asset_id}"
    #   f"folders/{folder_id}/assets/{asset_id}"
    # finding_name = "organizations/1112/sources/1234/findings/findingid"
    finding_marks_name = f"{finding_name}/securityMarks"
    
    # Notice the suffix after "marks." in the field mask matches the keys
    # in marks.
    field_mask = field_mask_pb2.FieldMask(
        paths=["marks.finding_key_a", "marks.finding_key_b"]
    )
    marks = {"finding_key_a": "value_a", "finding_key_b": "value_b"}
    
    updated_marks = client.[update_security_marks](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_update_security_marks)(
        request={
            "security_marks": {"name": finding_marks_name, "marks": marks},
            "update_mask": field_mask,
        }
    )

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=securitycommandcenter). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
