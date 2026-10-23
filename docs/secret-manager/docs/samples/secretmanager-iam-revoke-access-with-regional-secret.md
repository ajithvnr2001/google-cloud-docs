---
url: https://docs.cloud.google.com/secret-manager/docs/samples/secretmanager-iam-revoke-access-with-regional-secret/
title: IAM revoke access with regional secret \u00a0|\u00a0 Secret Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:40:34.527200+00:00
---

# IAM revoke access with regional secret  |  Secret Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secret-manager/docs/samples/secretmanager-iam-revoke-access-with-regional-secret/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Secret Manager ](https://docs.cloud.google.com/secret-manager/docs)
  * [ Samples ](https://docs.cloud.google.com/secret-manager/docs/samples)



#  IAM revoke access with regional secret Stay organized with collections  Save and categorize content based on your preferences. 

Revokes access of an IAM for a regional secret

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Manage access to regional secrets](https://docs.cloud.google.com/secret-manager/regional-secrets/manage-access-regional-secrets)



## Code sample

### C#

To learn how to install and use the client library for Secret Manager, see [Secret Manager client libraries](https://docs.cloud.google.com/secret-manager/docs/reference/libraries). 

To authenticate to Secret Manager, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Iam.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.html);
    using [Google.Cloud.SecretManager.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.html);
    
    public class IamRegionalRevokeAccessSample
    {
        public Policy IamRegionalRevokeAccess(
          string projectId = "my-project",
          string locationId = "my-location",
          string secretId = "my-secret",
          string member = "user:foo@example.com"
        )
        {
            // Create the Regional Secret Manager Client.
            [SecretManagerServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretManagerServiceClient.html) client = new [SecretManagerServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretManagerServiceClientBuilder.html)
            {
                Endpoint = $"secretmanager.{locationId}.rep.googleapis.com"
            }.Build();
    
            // Build the resource name.
            [SecretName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretName.html) secretName = [SecretName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretName.html).[FromProjectLocationSecret](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretName.html#Google_Cloud_SecretManager_V1_SecretName_FromProjectLocationSecret_System_String_System_String_System_String_)(projectId, locationId, secretId);
    
            // Get current policy.
            [Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html) policy = client.[GetIamPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretManagerServiceClient.html#Google_Cloud_SecretManager_V1_SecretManagerServiceClient_GetIamPolicy_Google_Cloud_Iam_V1_GetIamPolicyRequest_Google_Api_Gax_Grpc_CallSettings_)(new [GetIamPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.GetIamPolicyRequest.html)
            {
                ResourceAsResourceName = secretName,
            });
    
            // Remove the user from the list of bindings.
            policy.[RemoveRoleMember](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html#Google_Cloud_Iam_V1_Policy_RemoveRoleMember_System_String_System_String_)("roles/secretmanager.secretAccessor", member);
    
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
    	"google.golang.org/api/option"
    )
    
    // iamRevokeAccess revokes the given member's access on the secret.
    func IamRevokeAccessWithRegionalSecret(w io.Writer, projectId, locationId, secretId, member string) error {
    	// name := "projects/my-project/locations/my-location/secrets/my-secret"
    	// member := "user:foo@example.com"
    
    	// Create the client.
    	ctx := context.Background()
    	//Endpoint to send the request to regional server
    	endpoint := fmt.Sprintf("secretmanager.%s.rep.googleapis.com:443", locationId)
    	client, err := secretmanager.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/secretmanager/latest/apiv1.html#cloud_google_com_go_secretmanager_apiv1_Client_NewClient)(ctx, option.WithEndpoint(endpoint))
    
    	if err != nil {
    		return fmt.Errorf("failed to create regional secretmanager client: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/secretmanager/latest/apiv1.html#cloud_google_com_go_secretmanager_apiv1_Client_Close)()
    
    	name := fmt.Sprintf("projects/%s/locations/%s/secrets/%s", projectId, locationId, secretId)
    
    	// Get the current IAM policy.
    	handle := client.[IAM](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/secretmanager/latest/apiv1.html#cloud_google_com_go_secretmanager_apiv1_Client_IAM)(name)
    	policy, err := handle.Policy(ctx)
    	if err != nil {
    		return fmt.Errorf("failed to get policy: %w", err)
    	}
    
    	// Grant the member access permissions.
    	policy.Remove(member, "roles/secretmanager.secretAccessor")
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
    import com.google.cloud.secretmanager.v1.[SecretManagerServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceSettings.html);
    import com.google.cloud.secretmanager.v1.[SecretName](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretName.html);
    import com.google.iam.v1.[Binding](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html);
    import com.google.iam.v1.[GetIamPolicyRequest](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.GetIamPolicyRequest.html);
    import com.google.iam.v1.[Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html);
    import com.google.iam.v1.[SetIamPolicyRequest](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.SetIamPolicyRequest.html);
    import java.io.IOException;
    
    public class IamRevokeAccessWithRegionalSecret {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
    
        // Your GCP project ID.
        String projectId = "your-project-id";
        // Location of the secret.
        String locationId = "your-location-id";
        // Resource ID of the secret to revoke access to.
        String secretId = "your-secret-id";
        // IAM member, such as a user group or service account you want to revoke access.
        String member = "user:foo@example.com";
        iamRevokeAccessWithRegionalSecret(projectId, locationId, secretId, member);
      }
    
      // Revoke a member access to a particular secret.
      public static [Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) iamRevokeAccessWithRegionalSecret(
          String projectId, String locationId, String secretId, String member)
          throws IOException {
    
        // Endpoint to call the regional secret manager sever
        String apiEndpoint = String.format("secretmanager.%s.rep.googleapis.com:443", locationId);
        [SecretManagerServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceSettings.html) secretManagerServiceSettings =
            [SecretManagerServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceSettings.html).newBuilder().setEndpoint(apiEndpoint).build();
    
        // Initialize the client that will be used to send requests. This client only needs to be
        // created once, and can be reused for multiple requests.
        try ([SecretManagerServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceClient.html) client = 
            [SecretManagerServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceClient.html).create(secretManagerServiceSettings)) {
          // Build the name from the version.
          [SecretName](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretName.html) secretName = 
              [SecretName](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretName.html).[ofProjectLocationSecretName](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretName.html#com_google_cloud_secretmanager_v1_SecretName_ofProjectLocationSecretName_java_lang_String_java_lang_String_java_lang_String_)(projectId, locationId, secretId);
    
          // Request the current IAM policy.
          [Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) policy =
              client.getIamPolicy(
                  [GetIamPolicyRequest](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.GetIamPolicyRequest.html).newBuilder().setResource(secretName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretName.html#com_google_cloud_secretmanager_v1_SecretName_toString__)()).build());
    
          // Search through bindings and remove matches.
          String roleToFind = "roles/secretmanager.secretAccessor";
          for ([Binding](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html) binding : policy.[getBindingsList](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html#com_google_iam_v1_Policy_getBindingsList__)()) {
            if (binding.getRole() == roleToFind && binding.getMembersList().contains(member)) {
              binding.getMembersList().remove(member);
            }
          }
    
          // Save the updated IAM policy.
          [Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) updatedPolicy = client.setIamPolicy(
              [SetIamPolicyRequest](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.SetIamPolicyRequest.html).newBuilder()
                  .setResource(secretName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretName.html#com_google_cloud_secretmanager_v1_SecretName_toString__)())
                  .[setPolicy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.SetIamPolicyRequest.Builder.html#com_google_iam_v1_SetIamPolicyRequest_Builder_setPolicy_com_google_iam_v1_Policy_)(policy)
                  .build());
    
          System.out.printf("Updated IAM policy for %s\n", secretId);
    
          return updatedPolicy;
        }
      }
    }

### Node.js

To learn how to install and use the client library for Secret Manager, see [Secret Manager client libraries](https://docs.cloud.google.com/secret-manager/docs/reference/libraries). 

To authenticate to Secret Manager, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const projectId = 'my-project';
    // const locationId = 'my-location';
    // const secretId = 'my-secret';
    // const versionId = 'my-version';
    // const member = 'user:you@example.com';
    //
    // NOTE: Each member must be prefixed with its type. See the IAM documentation
    // for more information: https://cloud.google.com/iam/docs/overview.
    
    const name = `projects/${projectId}/locations/${locationId}/secrets/${secretId}`;
    
    // Imports the Secret Manager library
    const {SecretManagerServiceClient} = require('[@google-cloud/secret-manager](https://docs.cloud.google.com/nodejs/docs/reference/secret-manager/latest/overview.html)');
    
    // Adding the endpoint to call the regional secret manager sever
    const options = {};
    options.apiEndpoint = `secretmanager.${locationId}.rep.googleapis.com`;
    
    // Instantiates a client
    const client = new [SecretManagerServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/secret-manager/latest/overview.html)(options);
    
    async function grantAccessRegionalSecret() {
      // Get the current IAM policy.
      const [policy] = await client.getIamPolicy({
        resource: name,
      });
    
      // Build a new list of policy bindings with the user excluded.
      for (const i in policy.bindings) {
        const binding = policy.bindings[i];
        if (binding.role !== 'roles/secretmanager.secretAccessor') {
          continue;
        }
    
        const idx = binding.members.indexOf(member);
        if (idx !== -1) {
          binding.members.splice(idx, 1);
        }
      }
    
      // Save the updated IAM policy.
      await client.setIamPolicy({
        resource: name,
        policy: policy,
      });
    
      console.log(`Updated IAM policy for ${name}`);
    }
    
    grantAccessRegionalSecret();

### PHP

To learn how to install and use the client library for Secret Manager, see [Secret Manager client libraries](https://docs.cloud.google.com/secret-manager/docs/reference/libraries). 

To authenticate to Secret Manager, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Import the Secret Manager client library.
    use Google\Cloud\SecretManager\V1\Client\SecretManagerServiceClient;
    use Google\Cloud\Iam\V1\GetIamPolicyRequest;
    use Google\Cloud\Iam\V1\SetIamPolicyRequest;
    
    /**
     * @param string $projectId Your Google Cloud Project ID (e.g. 'my-project')
     * @param string $locationId Your secret Location (e.g. "us-central1")
     * @param string $secretId  Your secret ID (e.g. 'my-secret')
     * @param string $member Your member (e.g. 'user:foo@example.com')
     */
    function regional_iam_revoke_access(string $projectId, string $locationId, string $secretId, string $member): void
    {
        // Specify regional endpoint.
        $options = ['apiEndpoint' => "secretmanager.$locationId.rep.googleapis.com"];
    
        // Create the Secret Manager client.
        $client = new SecretManagerServiceClient($options);
    
        // Build the resource name of the secret.
        $name = $client->projectLocationSecretName($projectId, $locationId, $secretId);
    
        // Get the current IAM policy.
        $policy = $client->getIamPolicy((new GetIamPolicyRequest)->setResource($name));
    
        // Remove the member from the list of bindings.
        foreach ($policy->getBindings() as $binding) {
            if ($binding->getRole() == 'roles/secretmanager.secretAccessor') {
                $members = iterator_to_array($binding->getMembers());
                foreach ($members as $i => $existingMember) {
                    if ($member == $existingMember) {
                        unset($members[$i]);
                        $binding->setMembers($members);
                        break;
                    }
                }
            }
        }
    
        // Build the request.
        $request = (new SetIamPolicyRequest)
            ->setResource($name)
            ->setPolicy($policy);
    
        // Save the updated policy to the server.
        $client->setIamPolicy($request);
    
        // Print out a success message.
        printf('Updated IAM policy for %s', $secretId);
    }

### Ruby

To learn how to install and use the client library for Secret Manager, see [Secret Manager client libraries](https://docs.cloud.google.com/secret-manager/docs/reference/libraries). 

To authenticate to Secret Manager, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # project_id  = "YOUR-GOOGLE-CLOUD-PROJECT"  # (e.g. "my-project")
    # location_id = "YOUR-GOOGLE-CLOUD-LOCATION" # (e.g. "us-west1")
    # secret_id   = "YOUR-SECRET-ID"             # (e.g. "my-secret")
    # member      = "USER-OR-ACCOUNT"            # (e.g. "user:foo@example.com")
    
    # Require the Secret Manager client library.
    require "google/cloud/secret_manager"
    
    # Endpoint for the regional secret manager service.
    api_endpoint = "secretmanager.#{location_id}.rep.googleapis.com"
    
    # Create the Secret Manager client.
    client = Google::Cloud::[SecretManager](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta2/latest/Google-Cloud-SecretManager.html).[secret_manager_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager/latest/Google-Cloud-SecretManager.html) do |config|
      config.endpoint = api_endpoint
    end
    
    # Build the resource name of the secret.
    name = client.secret_path project: project_id, location: location_id, secret: secret_id
    
    # Get the current IAM policy.
    policy = client.get_iam_policy resource: name
    
    # Remove the member from the current bindings
    policy.bindings.each do |bind|
      if bind.role == "roles/secretmanager.secretAccessor"
        bind.members.delete member
      end
    end
    
    # Update IAM policy
    new_policy = client.set_iam_policy resource: name, policy: policy
    
    # Print a success message.
    puts "Updated regional IAM policy for #{secret_id}"

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=secretmanager). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
