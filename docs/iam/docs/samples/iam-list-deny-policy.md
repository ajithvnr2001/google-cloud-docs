---
url: https://docs.cloud.google.com/iam/docs/samples/iam-list-deny-policy/
title: List deny policies \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:10:06.213560+00:00
---

# List deny policies  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/samples/iam-list-deny-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Samples ](https://docs.cloud.google.com/iam/docs/samples)



#  List deny policies Stay organized with collections  Save and categorize content based on your preferences. 

List the deny policies in the resource provided.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Deny access to resources](https://docs.cloud.google.com/iam/docs/deny-access)



## Code sample

### Go

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/iam/admin/apiv1). 

To authenticate to IAM, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	iam "cloud.google.com/go/iam/apiv2"
    	"cloud.google.com/go/iam/apiv2/iampb"
    	"google.golang.org/api/iterator"
    )
    
    // listDenyPolicies lists all the deny policies that are attached to a resource.
    // A resource can have up to 5 deny policies.
    func listDenyPolicies(w io.Writer, projectID string) error {
    	// projectID := "your_project_id"
    
    	ctx := context.Background()
    	policiesClient, err := iam.NewPoliciesClient(ctx)
    	if err != nil {
    		return fmt.Errorf("NewPoliciesClient: %w", err)
    	}
    	defer policiesClient.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/iam/latest/apiv2.html#cloud_google_com_go_iam_apiv2_PoliciesClient_Close)()
    
    	// Each deny policy is attached to an organization, folder, or project.
    	// To work with deny policies, specify the attachment point.
    	//
    	// Its format can be one of the following:
    	// 1. cloudresourcemanager.googleapis.com/organizations/ORG_ID
    	// 2. cloudresourcemanager.googleapis.com/folders/FOLDER_ID
    	// 3. cloudresourcemanager.googleapis.com/projects/PROJECT_ID
    	//
    	// The attachment point is identified by its URL-encoded resource name. Hence, replace
    	// the "/" with "%%2F".
    	attachmentPoint := fmt.Sprintf(
    		"cloudresourcemanager.googleapis.com%%2Fprojects%%2F%s",
    		projectID,
    	)
    
    	req := &iampb.ListPoliciesRequest{
    		// Construct the full path of the resource's deny policies.
    		// Its format is: "policies/ATTACHMENT_POINT/denypolicies"
    		Parent: fmt.Sprintf("policies/%s/denypolicies", attachmentPoint),
    	}
    	it := policiesClient.ListPolicies(ctx, req)
    	fmt.Fprintf(w, "Policies found in project %s:\n", projectID)
    
    	for {
    		policy, err := it.[Next](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/iam/latest/apiv2.html#cloud_google_com_go_iam_apiv2_PolicyIterator_Next)()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			return err
    		}
    		fmt.Fprintf(w, "- %s\n", policy.GetName())
    	}
    	return nil
    }
    

### Java

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Java API reference documentation](https://developers.google.com/api-client-library/java/apis/iam/v1). 

To authenticate to IAM, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.iam.v2.[PoliciesClient](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2.PoliciesClient.html);
    import com.google.iam.v2.[Policy](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2.Policy.html);
    import java.io.IOException;
    import java.net.URLEncoder;
    import java.nio.charset.StandardCharsets;
    
    public class ListDenyPolicies {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        // ID or number of the Google Cloud project you want to use.
        String projectId = "your-google-cloud-project-id";
    
        listDenyPolicies(projectId);
      }
    
      // List all the deny policies that are attached to a resource.
      // A resource can have up to 5 deny policies.
      public static void listDenyPolicies(String projectId) throws IOException {
        // Initialize the Policies client.
        try ([PoliciesClient](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2.PoliciesClient.html) policiesClient = [PoliciesClient](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2.PoliciesClient.html).create()) {
    
          // Each deny policy is attached to an organization, folder, or project.
          // To work with deny policies, specify the attachment point.
          //
          // Its format can be one of the following:
          // 1. cloudresourcemanager.googleapis.com/organizations/ORG_ID
          // 2. cloudresourcemanager.googleapis.com/folders/FOLDER_ID
          // 3. cloudresourcemanager.googleapis.com/projects/PROJECT_ID
          //
          // The attachment point is identified by its URL-encoded resource name.
          String urlEncodedResource =
              URLEncoder.encode(
                  "cloudresourcemanager.googleapis.com/projects/", StandardCharsets.UTF_8);
          String attachmentPoint = String.format("%s%s", urlEncodedResource, projectId);
    
          // Construct the full path of the resource to which the policy is attached.
          // Its format is: "policies/{attachmentPoint}/denypolicies"
          String policyParent = String.format("policies/%s/denypolicies", attachmentPoint);
    
          // Create a list request and iterate over the returned policies.
          for ([Policy](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2.Policy.html) policy : policiesClient.listPolicies(policyParent).iterateAll()) {
            System.out.println(policy.getName());
          }
          System.out.println("Listed all deny policies");
        }
      }
    }

### Node.js

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Node.js API reference documentation](https://googleapis.dev/nodejs/googleapis/latest/iam/index.html). 

To authenticate to IAM, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment and replace these variables before running the sample.
     */
    // const projectId = 'YOUR_PROJECT_ID';
    
    const {PoliciesClient} = require('[@google-cloud/iam](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/overview.html)').v2;
    
    const iamClient = new [PoliciesClient](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/overview.html)();
    
    // Each deny policy is attached to an organization, folder, or project.
    // To work with deny policies, specify the attachment point.
    //
    // Its format can be one of the following:
    // 1. cloudresourcemanager.googleapis.com/organizations/ORG_ID
    // 2. cloudresourcemanager.googleapis.com/folders/FOLDER_ID
    // 3. cloudresourcemanager.googleapis.com/projects/PROJECT_ID
    //
    // The attachment point is identified by its URL-encoded resource name. Hence, replace
    // the "/" with "%2F".
    const attachmentPoint = `cloudresourcemanager.googleapis.com%2Fprojects%2F${projectId}`;
    
    async function listDenyPolicies() {
      const request = {
        parent: `policies/${attachmentPoint}/denypolicies`,
      };
    
      const policies = await iamClient.listPoliciesAsync(request);
      for await (const policy of policies) {
        console.log(`- ${policy.name}`);
      }
    }
    
    listDenyPolicies();

### Python

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Python API reference documentation](https://developers.google.com/api-client-library/python/apis/iam/v1). 

To authenticate to IAM, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def list_deny_policy(project_id: str) -> None:
        """List all the deny policies that are attached to a resource.
    
        A resource can have up to 5 deny policies.
    
        project_id: ID or number of the Google Cloud project you want to use.
        """
    
        from google.cloud import [iam](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.html)_v2
        from google.cloud.iam_v2 import types
    
        policies_client = iam_v2.[PoliciesClient](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.services.policies.PoliciesClient.html)()
    
        # Each deny policy is attached to an organization, folder, or project.
        # To work with deny policies, specify the attachment point.
        #
        # Its format can be one of the following:
        # 1. cloudresourcemanager.googleapis.com/organizations/ORG_ID
        # 2. cloudresourcemanager.googleapis.com/folders/FOLDER_ID
        # 3. cloudresourcemanager.googleapis.com/projects/PROJECT_ID
        #
        # The attachment point is identified by its URL-encoded resource name. Hence, replace
        # the "/" with "%2F".
        attachment_point = f"cloudresourcemanager.googleapis.com%2Fprojects%2F{project_id}"
    
        request = types.[ListPoliciesRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.types.ListPoliciesRequest.html)()
        # Construct the full path of the resource's deny policies.
        # Its format is: "policies/{attachmentPoint}/denypolicies"
        request.parent = f"policies/{attachment_point}/denypolicies"
    
        # Create a list request and iterate over the returned policies.
        policies = policies_client.[list_policies](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.services.policies.PoliciesClient.html#google_cloud_iam_v2_services_policies_PoliciesClient_list_policies)(request=request)
    
        for policy in policies:
            print(policy.name)
        print("Listed all deny policies")
    
    
    if __name__ == "__main__":
        # Your Google Cloud project ID.
        PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT", "your-google-cloud-project-id")
    
        # Any unique ID (0 to 63 chars) starting with a lowercase letter.
        policy_id = f"deny-{uuid.uuid4()}"
    
        list_deny_policy(PROJECT_ID)

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=identityandaccessmanagement). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
