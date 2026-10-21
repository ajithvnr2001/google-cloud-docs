---
url: https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-test-iam/
title: Test IAM permissions \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:49:59.527906+00:00
---

# Test IAM permissions  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-test-iam/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Samples ](https://docs.cloud.google.com/security-command-center/docs/samples)



#  Test IAM permissions Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates how to verify IAM permissions to create findings

## Code sample

### Go

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	iam "cloud.google.com/go/iam/apiv1/iampb"
    	securitycenter "cloud.google.com/go/securitycenter/apiv1"
    )
    
    // testIam demonstrates how to determine if your service user has appropriate
    // access to create and update findings, it writes permissions to w.
    // sourceName is the full resource name of the source to test for permissions.
    func testIam(w io.Writer, sourceName string) error {
    	// sourceName := "organizations/111122222444/sources/1234"
    	// Instantiate a context and a security service client to make API calls.
    	ctx := context.Background()
    	client, err := securitycenter.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv1.html#cloud_google_com_go_securitycenter_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("securitycenter.NewClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv1.html#cloud_google_com_go_securitycenter_apiv1_Client_Close)() // Closing the client safely cleans up background resources.
    	// Check for create/update Permissions.
    	req := &iam.[TestIamPermissionsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/iam/latest/apiv1/iampb.html#cloud_google_com_go_iam_apiv1_iampb_TestIamPermissionsRequest){
    		Resource:    sourceName,
    		Permissions: []string{"securitycenter.findings.update"},
    	}
    
    	policy, err := client.TestIamPermissions(ctx, req)
    	if err != nil {
    		return fmt.Errorf("Error getting IAM policy: %w", err)
    	}
    	fmt.Fprintf(w, "Permision to create/update findings? %t",
    		len(policy.Permissions) > 0)
    
    	// Check for updating state Permissions
    	req = &iam.[TestIamPermissionsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/iam/latest/apiv1/iampb.html#cloud_google_com_go_iam_apiv1_iampb_TestIamPermissionsRequest){
    		Resource:    sourceName,
    		Permissions: []string{"securitycenter.findings.setState"},
    	}
    
    	policy, err = client.TestIamPermissions(ctx, req)
    	if err != nil {
    		return fmt.Errorf("Error getting IAM policy: %w", err)
    	}
    	fmt.Fprintf(w, "Permision to update state? %t",
    		len(policy.Permissions) > 0)
    
    	return nil
    }
    

### Java

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    static TestIamPermissionsResponse testIamPermissions(SourceName sourceName) {
      try (SecurityCenterClient client = SecurityCenterClient.create()) {
        // SourceName sourceName = SourceName.of(/*organizationId=*/"123234324",
        // /*sourceId=*/"423432321");
    
        // Iam permission to test.
        List<String> permissionsToTest = new ArrayList<>();
        permissionsToTest.add("securitycenter.findings.update");
    
        // Call the API.
        TestIamPermissionsResponse response =
            client.testIamPermissions(sourceName.toString(), permissionsToTest);
        System.out.println("IAM Permission:");
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
    
    // sourceName is the full resource name of the source to test for permissions.
    /*
     * TODO(developer): Uncomment the following lines
     */
    // const sourceName = "organizations/111122222444/sources/1234";
    async function testIam() {
      {
        const [policy] = await client.testIamPermissions({
          resource: sourceName,
          permissions: ['securitycenter.findings.update'],
        });
        console.log(
          `Permissions to create/update findings? ${
            policy.permissions.length > 0
          }`
        );
      }
      {
        const [policy] = await client.testIamPermissions({
          resource: sourceName,
          permissions: ['securitycenter.findings.setState'],
        });
        console.log(
          `Permissions to update state? ${policy.permissions.length > 0}`
        );
      }
    }
    testIam();

### Python

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import securitycenter_v1
    
    # Create a client.
    client = securitycenter_v1.SecurityCenterClient()
    # 'source_name' is the resource path for a source that has been
    # created previously (you can use list_sources to find a specific one).
    # Its format is:
    # source_name = "organizations/{organization_id}/sources/{source_id}"
    # e.g.:
    # source_name = "organizations/111122222444/sources/1234"
    
    # Check for permssions to call create_finding or update_finding.
    permission_response = client.[test_iam_permissions](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_test_iam_permissions)(
        request={
            "resource": source_name,
            "permissions": ["securitycenter.findings.update"],
        }
    )
    
    print(
        "Permision to create or update findings? {}".format(
            len(permission_response.permissions) > 0
        )
    )
    # Check for permissions necessary to call set_finding_state.
    permission_response = client.[test_iam_permissions](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_test_iam_permissions)(
        request={
            "resource": source_name,
            "permissions": ["securitycenter.findings.setState"],
        }
    )
    print(f"Permision to update state? {len(permission_response.permissions) > 0}")

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=securitycommandcenter). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
