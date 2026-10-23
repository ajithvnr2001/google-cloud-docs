---
url: https://docs.cloud.google.com/kms/docs/samples/kms-iam-remove-member/
title: Remove an IAM member from a resource \u00a0|\u00a0 Cloud Key Management Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:25:32.149561+00:00
---

# Remove an IAM member from a resource  |  Cloud Key Management Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kms/docs/samples/kms-iam-remove-member/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud KMS ](https://docs.cloud.google.com/kms/docs)
  * [ Samples ](https://docs.cloud.google.com/kms/docs/samples)



#  Remove an IAM member from a resource Stay organized with collections  Save and categorize content based on your preferences. 

Remove an IAM member from a resource.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Access control with IAM](https://docs.cloud.google.com/kms/docs/iam)



## Code sample

### C#

To learn how to install and use the client library for Cloud KMS, see [Cloud KMS client libraries](https://docs.cloud.google.com/kms/docs/reference/libraries). 

To authenticate to Cloud KMS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Iam.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.html);
    using [Google.Cloud.Kms.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.html);
    
    public class IamRemoveMemberSample
    {
        public Policy IamRemoveMember(
          string projectId = "my-project", string locationId = "us-east1", string keyRingId = "my-key-ring", string keyId = "my-key",
          string member = "user:foo@example.com")
        {
            // Create the client.
            [KeyManagementServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html) client = [KeyManagementServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html#Google_Cloud_Kms_V1_KeyManagementServiceClient_Create)();
    
            // Build the resource name.
            [CryptoKeyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyName.html) resourceName = new [CryptoKeyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyName.html)(projectId, locationId, keyRingId, keyId);
    
            // The resource name could also be a key ring.
            // var resourceName = new KeyRingName(projectId, locationId, keyRingId);
    
            // Get the current IAM policy.
            [Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html) policy = client.[IAMPolicyClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html#Google_Cloud_Kms_V1_KeyManagementServiceClient_IAMPolicyClient).GetIamPolicy(
                new [GetIamPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.GetIamPolicyRequest.html)
                {
                    ResourceAsResourceName = resourceName
                });
    
            // Add the member to the policy.
            policy.[RemoveRoleMember](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html#Google_Cloud_Iam_V1_Policy_RemoveRoleMember_System_String_System_String_)("roles/cloudkms.cryptoKeyEncrypterDecrypter", member);
    
            // Save the updated IAM policy.
            [Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html) result = client.[IAMPolicyClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html#Google_Cloud_Kms_V1_KeyManagementServiceClient_IAMPolicyClient).SetIamPolicy(
                new [SetIamPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.SetIamPolicyRequest.html)
                {
                    ResourceAsResourceName = resourceName,
                    Policy = policy
                });
    
            // Return the resulting policy.
            return result;
        }
    }

### Go

To learn how to install and use the client library for Cloud KMS, see [Cloud KMS client libraries](https://docs.cloud.google.com/kms/docs/reference/libraries). 

To authenticate to Cloud KMS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	kms "cloud.google.com/go/kms/apiv1"
    )
    
    // iamRemoveMember removes the IAM member from the Cloud KMS key, if they exist.
    func iamRemoveMember(w io.Writer, name, member string) error {
    	// NOTE: The resource name can be either a key or a key ring.
    	//
    	// name := "projects/my-project/locations/us-east1/keyRings/my-key-ring/cryptoKeys/my-key"
    	// member := "user:foo@example.com"
    
    	// Create the client.
    	ctx := context.Background()
    	client, err := kms.[NewKeyManagementClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/kms/latest/apiv1.html#cloud_google_com_go_kms_apiv1_KeyManagementClient_NewKeyManagementClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("failed to create kms client: %w", err)
    	}
    	defer client.Close()
    
    	// Get the current IAM policy.
    	handle := client.[ResourceIAM](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/kms/latest/apiv1.html#cloud_google_com_go_kms_apiv1_KeyManagementClient_ResourceIAM)(name)
    	policy, err := handle.Policy(ctx)
    	if err != nil {
    		return fmt.Errorf("failed to get IAM policy: %w", err)
    	}
    
    	// Grant the member permissions. This example grants permission to use the key
    	// to encrypt data.
    	policy.Remove(member, "roles/cloudkms.cryptoKeyEncrypterDecrypter")
    	if err := handle.SetPolicy(ctx, policy); err != nil {
    		return fmt.Errorf("failed to save policy: %w", err)
    	}
    
    	fmt.Fprintf(w, "Updated IAM policy for %s\n", name)
    	return nil
    }
    

### Java

To learn how to install and use the client library for Cloud KMS, see [Cloud KMS client libraries](https://docs.cloud.google.com/kms/docs/reference/libraries). 

To authenticate to Cloud KMS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.kms.v1.[CryptoKeyName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyName.html);
    import com.google.cloud.kms.v1.[KeyManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html);
    import com.google.iam.v1.[Binding](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html);
    import com.google.iam.v1.[Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html);
    import java.io.IOException;
    
    public class IamRemoveMember {
    
      public void iamRemoveMember() throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String locationId = "us-east1";
        String keyRingId = "my-key-ring";
        String keyId = "my-key";
        String member = "user:foo@example.com";
        iamRemoveMember(projectId, locationId, keyRingId, keyId, member);
      }
    
      // Remove the given IAM membership on the resource, if it exists.
      public void iamRemoveMember(
          String projectId, String locationId, String keyRingId, String keyId, String member)
          throws IOException {
        // Initialize client that will be used to send requests. This client only
        // needs to be created once, and can be reused for multiple requests. After
        // completing all of your requests, call the "close" method on the client to
        // safely clean up any remaining background resources.
        try ([KeyManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html) client = [KeyManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html).create()) {
          // Build the key version name from the project, location, key ring, key,
          // and key version.
          [CryptoKeyName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyName.html) resourceName = [CryptoKeyName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyName.html).of(projectId, locationId, keyRingId, keyId);
    
          // The resource name could also be a key ring.
          // KeyRingName resourceName = KeyRingName.of(projectId, locationId, keyRingId);
    
          // Get the current policy.
          [Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) policy = client.getIamPolicy(resourceName);
    
          // Search through the bindings and remove matches.
          String roleToFind = "roles/cloudkms.cryptoKeyEncrypterDecrypter";
          // Create a new list of bindings, removing the member from the role.
          java.util.List<Binding> newBindings = new java.util.ArrayList<>();
          for ([Binding](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html) binding : policy.[getBindingsList](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html#com_google_iam_v1_Policy_getBindingsList__)()) {
            if (binding.getRole().equals(roleToFind) && binding.getMembersList().contains(member)) {
              [Binding](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html).Builder bindingBuilder = binding.toBuilder();
              // Remove the member.
              // Note: ProtocolStringList is immutable, so we need to rebuild the members list.
              java.util.List<String> validMembers = new java.util.ArrayList<>(binding.getMembersList());
              validMembers.remove(member);
    
              bindingBuilder.[clearMembers](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.Builder.html#com_google_iam_v1_Binding_Builder_clearMembers__)().[addAllMembers](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.Builder.html#com_google_iam_v1_Binding_Builder_addAllMembers_java_lang_Iterable_java_lang_String__)(validMembers);
              if (!validMembers.isEmpty()) {
                newBindings.add(bindingBuilder.build());
              }
              // If no members left, we can just omit the binding (effective removal).
            } else {
              newBindings.add(binding);
            }
          }
    
          [Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) newPolicy = policy.[toBuilder](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html#com_google_iam_v1_Policy_toBuilder__)().[clearBindings](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.Builder.html#com_google_iam_v1_Policy_Builder_clearBindings__)().[addAllBindings](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.Builder.html#com_google_iam_v1_Policy_Builder_addAllBindings_java_lang_Iterable___extends_com_google_iam_v1_Binding__)(newBindings).build();
    
          client.setIamPolicy(resourceName, newPolicy);
          System.out.printf("Updated IAM policy for %s%n", resourceName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyName.html#com_google_cloud_kms_v1_CryptoKeyName_toString__)());
        }
      }
    }

### Node.js

To learn how to install and use the client library for Cloud KMS, see [Cloud KMS client libraries](https://docs.cloud.google.com/kms/docs/reference/libraries). 

To authenticate to Cloud KMS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    //
    // TODO(developer): Uncomment these variables before running the sample.
    //
    // const projectId = 'my-project';
    // const locationId = 'us-east1';
    // const keyRingId = 'my-key-ring';
    // const keyId = 'my-key';
    // const member = 'user:foo@example.com';
    
    // Imports the Cloud KMS library
    const {KeyManagementServiceClient} = require('[@google-cloud/kms](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)');
    
    // Instantiates a client
    const client = new [KeyManagementServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)();
    
    // Build the resource name
    const resourceName = client.cryptoKeyPath(
      projectId,
      locationId,
      keyRingId,
      keyId
    );
    
    // The resource name could also be a key ring.
    // const resourceName = client.keyRingPath(projectId, locationId, keyRingId);
    
    async function iamRemoveMember() {
      // Get the current IAM policy.
      const [policy] = await client.getIamPolicy({
        resource: resourceName,
      });
    
      // Build a new list of policy bindings with the user excluded.
      for (const i in policy.bindings) {
        const binding = policy.bindings[i];
        if (binding.role !== 'roles/cloudkms.cryptoKeyEncrypterDecrypter') {
          continue;
        }
    
        const idx = binding.members.indexOf(member);
        if (idx !== -1) {
          binding.members.splice(idx, 1);
        }
      }
    
      // Save the updated IAM policy.
      const [updatedPolicy] = await client.setIamPolicy({
        resource: resourceName,
        policy: policy,
      });
    
      console.log('Updated policy');
      return updatedPolicy;
    }
    
    return iamRemoveMember();

### PHP

To learn how to install and use the client library for Cloud KMS, see [Cloud KMS client libraries](https://docs.cloud.google.com/kms/docs/reference/libraries). 

To authenticate to Cloud KMS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Iam\V1\Binding;
    use Google\Cloud\Iam\V1\GetIamPolicyRequest;
    use Google\Cloud\Iam\V1\Policy;
    use Google\Cloud\Iam\V1\SetIamPolicyRequest;
    use Google\Cloud\Kms\V1\Client\KeyManagementServiceClient;
    
    function iam_remove_member(
        string $projectId = 'my-project',
        string $locationId = 'us-east1',
        string $keyRingId = 'my-key-ring',
        string $keyId = 'my-key',
        string $member = 'user:foo@example.com'
    ): Policy {
        // Create the Cloud KMS client.
        $client = new KeyManagementServiceClient();
    
        // Build the resource name.
        $resourceName = $client->cryptoKeyName($projectId, $locationId, $keyRingId, $keyId);
    
        // The resource name could also be a key ring.
        // $resourceName = $client->keyRingName($projectId, $locationId, $keyRingId);
    
        // Get the current IAM policy.
        $getIamPolicyRequest = (new GetIamPolicyRequest())
            ->setResource($resourceName);
        $policy = $client->getIamPolicy($getIamPolicyRequest);
    
        // Remove the member from the policy by creating a new policy with everyone
        // but the member to remove.
        $newPolicy = new Policy();
        foreach ($policy->getBindings() as $binding) {
            if ($binding->getRole() !== 'roles/cloudkms.cryptoKeyEncrypterDecrypter') {
                $newPolicy->getBindings()[] = $binding;
            } else {
                $newBinding = (new Binding())
                  ->setRole($binding->getRole());
    
                $newMembers = [];
                foreach ($binding->getMembers() as $existingMember) {
                    if ($member !== $existingMember) {
                        $newMembers[] = $existingMember;
                    }
                }
    
                $newPolicy->getBindings()[] = (new Binding())
                  ->setRole($binding->getRole())
                  ->setMembers($newMembers);
            }
        }
    
        // Save the updated IAM policy.
        $setIamPolicyRequest = (new SetIamPolicyRequest())
            ->setResource($resourceName)
            ->setPolicy($newPolicy);
        $updatedPolicy = $client->setIamPolicy($setIamPolicyRequest);
        printf('Removed %s' . PHP_EOL, $member);
    
        return $updatedPolicy;
    }

### Python

To learn how to install and use the client library for Cloud KMS, see [Cloud KMS client libraries](https://docs.cloud.google.com/kms/docs/reference/libraries). 

To authenticate to Cloud KMS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import kms
    from google.iam.v1 import policy_pb2 as iam_policy
    
    
    def iam_remove_member(
        project_id: str, location_id: str, key_ring_id: str, key_id: str, member: str
    ) -> iam_policy.Policy:
        """
        Remove an IAM member from a resource.
    
        Args:
            project_id (string): Google Cloud project ID (e.g. 'my-project').
            location_id (string): Cloud KMS location (e.g. 'us-east1').
            key_ring_id (string): ID of the Cloud KMS key ring (e.g. 'my-key-ring').
            key_id (string): ID of the key to use (e.g. 'my-key').
            member (string): Member to remove (e.g. 'user:foo@example.com')
    
        Returns:
            Policy: Updated Cloud IAM policy.
    
        """
    
        # Create the client.
        client = kms.[KeyManagementServiceClient](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html)()
    
        # Build the resource name.
        resource_name = client.[crypto_key_path](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html#google_cloud_kms_v1_services_key_management_service_KeyManagementServiceClient_crypto_key_path)(project_id, location_id, key_ring_id, key_id)
    
        # The resource name could also be a key ring.
        # resource_name = client.key_ring_path(project_id, location_id, key_ring_id);
    
        # Get the current policy.
        policy = client.[get_iam_policy](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html#google_cloud_kms_v1_services_key_management_service_KeyManagementServiceClient_get_iam_policy)(request={"resource": resource_name})
    
        # Remove the member from the policy.
        for binding in policy.bindings:
            if binding.role == "roles/cloudkms.cryptoKeyEncrypterDecrypter":
                if member in binding.members:
                    binding.members.remove(member)
    
        # Save the updated IAM policy.
        request = {"resource": resource_name, "policy": policy}
        updated_policy = client.[set_iam_policy](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html#google_cloud_kms_v1_services_key_management_service_KeyManagementServiceClient_set_iam_policy)(request=request)
        print(f"Removed {member} from {resource_name}")
        return updated_policy
    
    

### Ruby

To learn how to install and use the client library for Cloud KMS, see [Cloud KMS client libraries](https://docs.cloud.google.com/kms/docs/reference/libraries). 

To authenticate to Cloud KMS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # TODO(developer): uncomment these values before running the sample.
    # project_id  = "my-project"
    # location_id = "us-east1"
    # key_ring_id = "my-key-ring"
    # key_id      = "my-key"
    # member      = "user:foo@example.com"
    
    # Require the library.
    require "google/cloud/kms"
    
    # Create the client.
    client = Google::Cloud::[Kms](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-v1/latest/Google-Cloud-Kms.html).[key_management_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms/latest/Google-Cloud-Kms.html)
    
    # Build the resource name.
    resource_name = client.crypto_key_path project:    project_id,
                                           location:   location_id,
                                           key_ring:   key_ring_id,
                                           crypto_key: key_id
    
    # The resource name could also be a key ring.
    # resource_name = client.key_ring_path project: project_id, location: location_id, key_ring: key_ring_id
    
    # Create the IAM client.
    iam_client = Google::Cloud::[Kms](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-v1/latest/Google-Cloud-Kms.html)::[V1](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-v1/latest/Google-Cloud-Kms-V1.html)::IAMPolicy::Client.new
    
    # Get the current IAM policy.
    policy = iam_client.get_iam_policy resource: resource_name
    
    # Remove the member from the current bindings
    policy.bindings.each do |bind|
      if bind.role == "roles/cloudkms.cryptoKeyEncrypterDecrypter"
        bind.members.delete member
      end
    end
    
    # Save the updated policy.
    updated_policy = iam_client.set_iam_policy resource: resource_name, policy: policy
    puts "Removed #{member}"

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudkeymanagementservice). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
