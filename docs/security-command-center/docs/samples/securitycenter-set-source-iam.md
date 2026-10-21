---
url: https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-set-source-iam/
title: Set IAM policies \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:50:24.276747+00:00
---

# Set IAM policies  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-set-source-iam/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Samples ](https://docs.cloud.google.com/security-command-center/docs/samples)



#  Set IAM policies Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates how to set IAM policies on a source

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
    
    // setSourceIamPolicy grants user roles/securitycenter.findingsEditor permision
    // for a source. sourceName is the full resource name of the source to be
    // updated. user is an email address that IAM can grant permissions to.
    func setSourceIamPolicy(w io.Writer, sourceName string, user string) error {
    	// sourceName := "organizations/111122222444/sources/1234"
    	// user := "someuser@some_domain.com
    	// Instantiate a context and a security service client to make API calls.
    	ctx := context.Background()
    	client, err := securitycenter.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv1.html#cloud_google_com_go_securitycenter_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("securitycenter.NewClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv1.html#cloud_google_com_go_securitycenter_apiv1_Client_Close)() // Closing the client safely cleans up background resources.
    
    	// Retrieve the existing policy so we can update only a specific
    	// field.
    	existing, err := client.GetIamPolicy(ctx, &iam.[GetIamPolicyRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/iam/latest/apiv1/iampb.html#cloud_google_com_go_iam_apiv1_iampb_GetIamPolicyRequest){
    		Resource: sourceName,
    	})
    	if err != nil {
    		return fmt.Errorf("GetIamPolicy(%s): %w", sourceName, err)
    	}
    
    	req := &iam.[SetIamPolicyRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/iam/latest/apiv1/iampb.html#cloud_google_com_go_iam_apiv1_iampb_SetIamPolicyRequest){
    		Resource: sourceName,
    		Policy: &iam.[Policy](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/iam/latest/apiv1/iampb.html#cloud_google_com_go_iam_apiv1_iampb_Policy){
    			// Enables partial update of existing policy
    			Etag: existing.Etag,
    			Bindings: []*iam.[Binding](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/iam/latest/apiv1/iampb.html#cloud_google_com_go_iam_apiv1_iampb_Binding){{
    				Role: "roles/securitycenter.findingsEditor",
    				// New IAM Binding for the user.
    				Members: []string{fmt.Sprintf("user:%s", user)},
    			},
    			},
    		},
    	}
    	policy, err := client.SetIamPolicy(ctx, req)
    	if err != nil {
    		return fmt.Errorf("SetIamPolicy(%s, %v): %w", sourceName, req.[Policy](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/iam/latest/apiv1/iampb.html#cloud_google_com_go_iam_apiv1_iampb_Policy), err)
    	}
    
    	fmt.Fprint(w, "Bindings:\n")
    	for _, binding := range policy.Bindings {
    		for _, member := range binding.Members {
    			fmt.Fprintf(w, "Principal: %s Role: %s\n", member, binding.Role)
    		}
    	}
    	return nil
    }
    

### Java

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    static Policy setIamPolicySource(SourceName sourceName, String userEmail) {
      try (SecurityCenterClient client = SecurityCenterClient.create()) {
        // userEmail = "someuser@domain.com"
        // Set up IAM Policy for the user userMail to use the role findingsEditor.
        // The user must be a valid google account.
        Policy oldPolicy = client.getIamPolicy(sourceName.toString());
        Binding bindings =
            Binding.newBuilder()
                .setRole("roles/securitycenter.findingsEditor")
                .addMembers("user:" + userEmail)
                .build();
        Policy policy = oldPolicy.toBuilder().addBindings(bindings).build();
    
        // Start setting up a request to set IAM policy for a source.
        // SourceName sourceName = SourceName.of("123234324", "423432321");
        SetIamPolicyRequest.Builder request =
            SetIamPolicyRequest.newBuilder().setPolicy(policy).setResource(sourceName.toString());
    
        // Call the API.
        Policy response = client.setIamPolicy(request.build());
    
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
    
    async function setSourceIamPolicy() {
      // sourceName is the full resource name of the source to be
      // updated.
      // user is an email address that IAM can grant permissions to.
      /*
       * TODO(developer): Uncomment the following lines
       */
      // const sourceName = "organizations/111122222444/sources/1234";
      // const user = "someuser@domain.com";
      const [existingPolicy] = await client.getIamPolicy({
        resource: sourceName,
      });
    
      const [updatedPolicy] = await client.setIamPolicy({
        resource: sourceName,
        policy: {
          // Enables partial update of existing policy
          etag: existingPolicy.etag,
          bindings: [
            {
              role: 'roles/securitycenter.findingsEditor',
              // New IAM Binding for the user.
              members: [`user:${user}`],
            },
          ],
        },
      });
      console.log('Updated policy: %j', updatedPolicy);
    }
    setSourceIamPolicy();

### Python

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import securitycenter_v1
    from google.iam.v1 import policy_pb2
    
    client = securitycenter_v1.SecurityCenterClient()
    
    # 'source_name' is the resource path for a source that has been
    # created previously (you can use list_sources to find a specific one).
    # Its format is:
    # source_name = "organizations/{organization_id}/sources/{source_id}"
    # e.g.:
    # source_name = "organizations/111122222444/sources/1234"
    # Get the old policy so we can do an incremental update.
    old_policy = client.[get_iam_policy](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_get_iam_policy)(request={"resource": source_name})
    print(f"Old Policy: {old_policy}")
    
    # Setup a new IAM binding.
    binding = policy_pb2.Binding()
    binding.role = "roles/securitycenter.findingsEditor"
    # user_email is an e-mail address known to Cloud IAM (e.g. a gmail address).
    # user_mail = user@somedomain.com
    binding.members.append(f"user:{user_email}")
    
    # Setting the e-tag avoids over-write existing policy
    updated = client.[set_iam_policy](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_set_iam_policy)(
        request={
            "resource": source_name,
            "policy": {"etag": old_policy.etag, "bindings": [binding]},
        }
    )
    
    print(f"Updated Policy: {updated}")

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=securitycommandcenter). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
