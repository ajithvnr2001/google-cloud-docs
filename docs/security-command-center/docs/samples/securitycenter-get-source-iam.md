---
url: https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-get-source-iam/
title: Get IAM policies \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:33:09.387749+00:00
---

# Get IAM policies  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-get-source-iam/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Samples ](https://docs.cloud.google.com/security-command-center/docs/samples)



#  Get IAM policies Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates how to retrieve IAM policies for a source

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
    
    // getSourceIamPolicy prints the policy for sourceName to w and return it.
    // sourceName is the full resource name of the source with the policy of interest.
    func getSourceIamPolicy(w io.Writer, sourceName string) error {
    	// sourceName := "organizations/111122222444/sources/1234"
    	// Instantiate a context and a security service client to make API calls.
    	ctx := context.Background()
    	client, err := securitycenter.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv1.html#cloud_google_com_go_securitycenter_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("securitycenter.NewClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv1.html#cloud_google_com_go_securitycenter_apiv1_Client_Close)() // Closing the client safely cleans up background resources.
    
    	req := &iam.[GetIamPolicyRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/iam/latest/apiv1/iampb.html#cloud_google_com_go_iam_apiv1_iampb_GetIamPolicyRequest){
    		Resource: sourceName,
    	}
    
    	policy, err := client.GetIamPolicy(ctx, req)
    	if err != nil {
    		return fmt.Errorf("GetIamPolicy(%s): %w", sourceName, err)
    	}
    
    	fmt.Fprintf(w, "Policy: %v", policy)
    	return nil
    }
    

### Java

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    static Policy getIamPolicySource(SourceName sourceName) {
      try (SecurityCenterClient client = SecurityCenterClient.create()) {
        // Start setting up a request to get IAM policy for a source.
        // SourceName sourceName = SourceName.of(/*organization=*/"123234324",/*source=*/
        // "423432321");
        GetIamPolicyRequest request =
            GetIamPolicyRequest.newBuilder().setResource(sourceName.toString()).build();
    
        // Call the API.
        Policy response = client.getIamPolicy(request);
    
        System.out.println("Policy: " + response);
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
    
    async function getSourceIamPolicy() {
      // sourceName is the full resource name to retrieve the policy for.
      /*
       * TODO(developer): Uncomment the following lines
       */
      // const sourceName = "organizations/111122222444/sources/1234";
    
      const [existingPolicy] = await client.getIamPolicy({
        resource: sourceName,
      });
    
      console.log('Current policy: %j', existingPolicy);
    }
    getSourceIamPolicy();

### Python

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import securitycenter_v1
    
    client = securitycenter_v1.SecurityCenterClient()
    
    # 'source_name' is the resource path for a source that has been
    # created previously (you can use list_sources to find a specific one).
    # Its format is:
    # source_name = "organizations/{organization_id}/sources/{source_id}"
    # e.g.:
    # source_name = "organizations/111122222444/sources/1234"
    # Get the old policy so we can do an incremental update.
    policy = client.[get_iam_policy](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_get_iam_policy)(request={"resource": source_name})
    print(f"Policy: {policy}")

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=securitycommandcenter). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
