---
url: https://docs.cloud.google.com/secret-manager/docs/samples/secretmanager-iam-grant-access/
title: IAM grant access \u00a0|\u00a0 Secret Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:40:07.517093+00:00
---

# IAM grant access  |  Secret Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secret-manager/docs/samples/secretmanager-iam-grant-access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Secret Manager ](https://docs.cloud.google.com/secret-manager/docs)
  * [ Samples ](https://docs.cloud.google.com/secret-manager/docs/samples)



#  IAM grant access Stay organized with collections  Save and categorize content based on your preferences. 

Sets roles/secretmanager.secretAccessor policy.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Configure authentication to remote repository upstreams](https://docs.cloud.google.com/artifact-registry/docs/repositories/configure-remote-authentication)
  * [Configure remote repository authentication to Docker Hub](https://docs.cloud.google.com/artifact-registry/docs/docker/configure-remote-auth-docker-hub)
  * [Configure remote repository authentication to Maven Central](https://docs.cloud.google.com/artifact-registry/docs/java/configure-remote-auth-maven-central)
  * [Configure remote repository authentication to the npm registry](https://docs.cloud.google.com/artifact-registry/docs/nodejs/configure-remote-auth-npm-registry)
  * [Configure remote repository authentication to the Python Package Index (PyPI)](https://docs.cloud.google.com/artifact-registry/docs/python/configure-remote-auth-pypi)
  * [Manage access to secrets](https://docs.cloud.google.com/secret-manager/docs/manage-access-to-secrets)
  * [Use a Weaviate database with Vertex AI RAG Engine](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/rag-engine/use-weaviate-db)



## Code sample

### C#

To learn how to install and use the client library for Secret Manager, see [Secret Manager client libraries](https://docs.cloud.google.com/secret-manager/docs/reference/libraries). 

To authenticate to Secret Manager, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.SecretManager.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.html);
    using [Google.Cloud.Iam.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.html);
    
    public class IamGrantAccessSample
    {
        public Policy IamGrantAccess(
          string projectId = "my-project", string secretId = "my-secret",
          string member = "user:foo@example.com")
        {
            // Create the client.
            [SecretManagerServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretManagerServiceClient.html) client = [SecretManagerServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretManagerServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretManagerServiceClient.html#Google_Cloud_SecretManager_V1_SecretManagerServiceClient_Create)();
    
            // Build the resource name.
            [SecretName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretName.html) secretName = new [SecretName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretName.html)(projectId, secretId);
    
            // Get current policy.
            [Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html) policy = client.[GetIamPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretManagerServiceClient.html#Google_Cloud_SecretManager_V1_SecretManagerServiceClient_GetIamPolicy_Google_Cloud_Iam_V1_GetIamPolicyRequest_Google_Api_Gax_Grpc_CallSettings_)(new [GetIamPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.GetIamPolicyRequest.html)
            {
                ResourceAsResourceName = secretName,
            });
    
            // Add the user to the list of bindings.
            policy.[AddRoleMember](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html#Google_Cloud_Iam_V1_Policy_AddRoleMember_System_String_System_String_)("roles/secretmanager.secretAccessor", member);
    
            // Save the updated policy.
            policy = client.[SetIamPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretManagerServiceClient.html#Google_Cloud_SecretManager_V1_SecretManagerServiceClient_SetIamPolicy_Google_Cloud_Iam_V1_SetIamPolicyRequest_Google_Api_Gax_Grpc_CallSettings_)(new [SetIamPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.SetIamPolicyRequest.html)
            {
                ResourceAsResourceName = secretName,
                Policy = policy,
            });
            return policy;
        }
    }

### Go

To learn how to install and use the client library for Secret Manager, see [Secret Manager client libraries](https://docs.cloud.google.com/secret-manager/docs/reference/libraries). 

To authenticate to Secret Manager, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	secretmanager "cloud.google.com/go/secretmanager/apiv1"
    )
    
    // iamGrantAccess grants the given member access to the secret.
    func iamGrantAccess(w io.Writer, name, member string) error {
    	// name := "projects/my-project/secrets/my-secret"
    	// member := "user:foo@example.com"
    
    	// Create the client.
    	ctx := context.Background()
    	client, err := secretmanager.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/secretmanager/latest/apiv1.html#cloud_google_com_go_secretmanager_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("failed to create secretmanager client: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/secretmanager/latest/apiv1.html#cloud_google_com_go_secretmanager_apiv1_Client_Close)()
    
    	// Get the current IAM policy.
    	handle := client.[IAM](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/secretmanager/latest/apiv1.html#cloud_google_com_go_secretmanager_apiv1_Client_IAM)(name)
    	policy, err := handle.Policy(ctx)
    	if err != nil {
    		return fmt.Errorf("failed to get policy: %w", err)
    	}
    
    	// Grant the member access permissions.
    	policy.Add(member, "roles/secretmanager.secretAccessor")
    	if err = handle.SetPolicy(ctx, policy); err != nil {
    		return fmt.Errorf("failed to save policy: %w", err)
    	}
    
    	fmt.Fprintf(w, "Updated IAM policy for %s\n", name)
    	return nil
    }
    

### Java

To learn how to install and use the client library for Secret Manager, see [Secret Manager client libraries](https://docs.cloud.google.com/secret-manager/docs/reference/libraries). 

To authenticate to Secret Manager, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.secretmanager.v1.[SecretManagerServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceClient.html);
    import com.google.cloud.secretmanager.v1.[SecretName](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretName.html);
    import com.google.iam.v1.[Binding](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html);
    import com.google.iam.v1.[GetIamPolicyRequest](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.GetIamPolicyRequest.html);
    import com.google.iam.v1.[Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html);
    import com.google.iam.v1.[SetIamPolicyRequest](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.SetIamPolicyRequest.html);
    import java.io.IOException;
    
    public class IamGrantAccess {
    
      public static void iamGrantAccess() throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String secretId = "your-secret-id";
        String member = "user:foo@example.com";
        iamGrantAccess(projectId, secretId, member);
      }
    
      // Grant a member access to a particular secret.
      public static void iamGrantAccess(String projectId, String secretId, String member)
          throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([SecretManagerServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceClient.html) client = [SecretManagerServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceClient.html).create()) {
          // Build the name from the version.
          [SecretName](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretName.html) secretName = [SecretName](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretName.html).of(projectId, secretId);
    
          // Request the current IAM policy.
          [Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) currentPolicy =
              client.getIamPolicy(
                  [GetIamPolicyRequest](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.GetIamPolicyRequest.html).newBuilder().setResource(secretName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretName.html#com_google_cloud_secretmanager_v1_SecretName_toString__)()).build());
    
          // Build the new binding.
          [Binding](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html) binding =
              [Binding](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html).newBuilder()
                  .setRole("roles/secretmanager.secretAccessor")
                  .[addMembers](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.Builder.html#com_google_iam_v1_Binding_Builder_addMembers_java_lang_String_)(member)
                  .build();
    
          // Create a new IAM policy from the current policy, adding the binding.
          [Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) newPolicy = [Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html).newBuilder().mergeFrom(currentPolicy).[addBindings](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.Builder.html#com_google_iam_v1_Policy_Builder_addBindings_com_google_iam_v1_Binding_)(binding).build();
    
          // Save the updated IAM policy.
          client.setIamPolicy(
              [SetIamPolicyRequest](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.SetIamPolicyRequest.html).newBuilder()
                  .setResource(secretName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretName.html#com_google_cloud_secretmanager_v1_SecretName_toString__)())
                  .[setPolicy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.SetIamPolicyRequest.Builder.html#com_google_iam_v1_SetIamPolicyRequest_Builder_setPolicy_com_google_iam_v1_Policy_)(newPolicy)
                  .build());
    
          System.out.printf("Updated IAM policy for %s\n", secretId);
        }
      }
    }

### Node.js

To learn how to install and use the client library for Secret Manager, see [Secret Manager client libraries](https://docs.cloud.google.com/secret-manager/docs/reference/libraries). 

To authenticate to Secret Manager, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const name = 'projects/my-project/secrets/my-secret';
    // const member = 'user:you@example.com';
    //
    // NOTE: Each member must be prefixed with its type. See the IAM documentation
    // for more information: https://cloud.google.com/iam/docs/overview.
    
    // Imports the Secret Manager library
    const {SecretManagerServiceClient} = require('[@google-cloud/secret-manager](https://docs.cloud.google.com/nodejs/docs/reference/secret-manager/latest/overview.html)');
    
    // Instantiates a client
    const client = new [SecretManagerServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/secret-manager/latest/overview.html)();
    
    async function grantAccess() {
      // Get the current IAM policy.
      const [policy] = await client.getIamPolicy({
        resource: name,
      });
    
      // Add the user with accessor permissions to the bindings list.
      policy.bindings.push({
        role: 'roles/secretmanager.secretAccessor',
        members: [member],
      });
    
      // Save the updated IAM policy.
      await client.setIamPolicy({
        resource: name,
        policy: policy,
      });
    
      console.log(`Updated IAM policy for ${name}`);
    }
    
    grantAccess();

### PHP

To learn how to install and use the client library for Secret Manager, see [Secret Manager client libraries](https://docs.cloud.google.com/secret-manager/docs/reference/libraries). 

To authenticate to Secret Manager, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Import the Secret Manager client library.
    use Google\Cloud\SecretManager\V1\Client\SecretManagerServiceClient;
    
    // Import the Secret Manager IAM library.
    use Google\Cloud\Iam\V1\Binding;
    use Google\Cloud\Iam\V1\GetIamPolicyRequest;
    use Google\Cloud\Iam\V1\SetIamPolicyRequest;
    
    /**
     * @param string $projectId Your Google Cloud Project ID (e.g. 'my-project')
     * @param string $secretId  Your secret ID (e.g. 'my-secret')
     * @param string $member Your member (e.g. 'user:foo@example.com')
     */
    function iam_grant_access(string $projectId, string $secretId, string $member): void
    {
        // Create the Secret Manager client.
        $client = new SecretManagerServiceClient();
    
        // Build the resource name of the secret.
        $name = $client->secretName($projectId, $secretId);
    
        // Get the current IAM policy.
        $policy = $client->getIamPolicy((new GetIamPolicyRequest)->setResource($name));
    
        // Update the bindings to include the new member.
        $bindings = iterator_to_array($policy->getBindings());
        $bindings[] = new Binding([
            'members' => [$member],
            'role' => 'roles/secretmanager.secretAccessor',
        ]);
        $policy->setBindings($bindings);
    
        // Build the request.
        $request = (new SetIamPolicyRequest)
            ->setResource($name)
            ->setPolicy($policy);
    
        // Save the updated policy to the server.
        $client->setIamPolicy($request);
    
        // Print out a success message.
        printf('Updated IAM policy for %s', $secretId);
    }

### Python

To learn how to install and use the client library for Secret Manager, see [Secret Manager client libraries](https://docs.cloud.google.com/secret-manager/docs/reference/libraries). 

To authenticate to Secret Manager, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def iam_grant_access(
        project_id: str, secret_id: str, member: str
    ) -> iam_policy_pb2.SetIamPolicyRequest:
        """
        Grant the given member access to a secret.
        """
    
        # Import the Secret Manager client library.
        from google.cloud import secretmanager
    
        # Create the Secret Manager client.
        client = secretmanager.SecretManagerServiceClient()
    
        # Build the resource name of the secret.
        name = client.secret_path(project_id, secret_id)
    
        # Get the current IAM policy.
        policy = client.get_iam_policy(request={"resource": name})
    
        # Add the given member with access permissions.
        policy.bindings.add(role="roles/secretmanager.secretAccessor", members=[member])
    
        # Update the IAM Policy.
        new_policy = client.set_iam_policy(request={"resource": name, "policy": policy})
    
        # Print data about the secret.
        print(f"Updated IAM policy on {secret_id}")

### Ruby

To learn how to install and use the client library for Secret Manager, see [Secret Manager client libraries](https://docs.cloud.google.com/secret-manager/docs/reference/libraries). 

To authenticate to Secret Manager, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # project_id = "YOUR-GOOGLE-CLOUD-PROJECT"  # (e.g. "my-project")
    # secret_id  = "YOUR-SECRET-ID"             # (e.g. "my-secret")
    # member     = "USER-OR-ACCOUNT"            # (e.g. "user:foo@example.com")
    
    # Require the Secret Manager client library.
    require "google/cloud/secret_manager"
    
    # Create a Secret Manager client.
    client = Google::Cloud::[SecretManager](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta2/latest/Google-Cloud-SecretManager.html).[secret_manager_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager/latest/Google-Cloud-SecretManager.html)
    
    # Build the resource name of the secret.
    name = client.secret_path project: project_id, secret: secret_id
    
    # Get the current IAM policy.
    policy = client.get_iam_policy resource: name
    
    # Add new member to current bindings
    policy.bindings << Google::Iam::[V1](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1.html)::Binding.new(
      members: [member],
      role:    "roles/secretmanager.secretAccessor"
    )
    
    # Update IAM policy
    new_policy = client.set_iam_policy resource: name, policy: policy
    
    # Print a success message.
    puts "Updated IAM policy for #{secret_id}"

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=secretmanager). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
