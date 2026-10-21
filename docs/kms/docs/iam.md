---
url: https://docs.cloud.google.com/kms/docs/iam/
title: Access control with IAM \u00a0|\u00a0 Cloud Key Management Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:37:08.971051+00:00
---

# Access control with IAM  |  Cloud Key Management Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kms/docs/iam/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud KMS ](https://docs.cloud.google.com/kms/docs)
  * [ Guides ](https://docs.cloud.google.com/kms/docs/key-management-service)



Send feedback 

#  Access control with IAM Stay organized with collections  Save and categorize content based on your preferences. 

This topic shows how to manage access to Cloud KMS resources.

## Overview

To manage access to Cloud KMS resources, such as keys and key rings, you grant [Identity and Access Management (IAM) roles](https://docs.cloud.google.com/iam/docs/overview). You can grant or restrict the ability to perform specific cryptographic operations, such as rotating a key or encrypting data. You can grant IAM roles on:

  * A key directly
  * A key ring, inherited by all keys in that key ring
  * A Google Cloud project, inherited by all keys in the project
  * A Google Cloud folder, inherited by all keys in all projects in the folder
  * A Google Cloud organization, inherited by all keys in folders in the organization



For a complete list of Cloud KMS actions and IAM roles and permissions, see [Permissions and roles](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles). For a complete list of Cloud KMS resources and how they relate to each other, see [Cloud KMS resources](https://docs.cloud.google.com/kms/docs/resource-hierarchy).

## Before you begin

To complete these tasks, you need permission to administer Cloud KMS resources in the Google Cloud project. The Cloud KMS Admin role (`roles/cloudkms.admin`) includes the required permissions.

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the required API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=cloudkms.googleapis.com&redirect=https%3A//console.cloud.google.com)

  5. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  6. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  7. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  8. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  9. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  10. Enable the required API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=cloudkms.googleapis.com&redirect=https%3A//console.cloud.google.com)

  11. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  12. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  13. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  14. [Create a resource](https://docs.cloud.google.com/kms/docs/creating-keys), such as a key ring.
  15. [Get the resource IDs](https://docs.cloud.google.com/kms/docs/getting-resource-ids) for the resources created, such as a key ring, key, and key version. 



Only IAM principals with Owner (`roles/owner`) or Cloud KMS Admin (`roles/cloudkms.admin`) roles can grant or revoke access to Cloud KMS resources.

## Granting roles on a resource

The following example grants a role that provides access to a Cloud KMS key:

### gcloud

To use Cloud KMS on the command line, first [Install or upgrade to the latest version of Google Cloud CLI](https://docs.cloud.google.com/sdk/install).
    
    
    gcloud kms keys add-iam-policy-binding key \
        --keyring key-ring \
        --location location \
        --member principal-type:principal-email \
        --role roles/role
    

Replace key with the name of the key. Replace key-ring with the name of the key ring where the key is located. Replace location with the Cloud KMS location for the key ring. Replace principal-type and principal-email with the type of principal and the principal's email address. Replace role with the name of the role to add.

### C#

To run this code, first [set up a C# development environment](https://docs.cloud.google.com/dotnet/docs/setup) and [install the Cloud KMS C# SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-csharp).
    
    
    using [Google.Cloud.Iam.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.html);
    using [Google.Cloud.Kms.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.html);
    
    public class IamAddMemberSample
    {
        public Policy IamAddMember(
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
            policy.[AddRoleMember](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html#Google_Cloud_Iam_V1_Policy_AddRoleMember_System_String_System_String_)("roles/cloudkms.cryptoKeyEncrypterDecrypter", member);
    
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

To run this code, first [set up a Go development environment](https://docs.cloud.google.com/go/docs/setup) and [install the Cloud KMS Go SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-go).
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	kms "cloud.google.com/go/kms/apiv1"
    )
    
    // iamAddMember adds a new IAM member to the Cloud KMS key
    func iamAddMember(w io.Writer, name, member string) error {
    	// NOTE: The resource name can be either a key or a key ring. If IAM
    	// permissions are granted on the key ring, the permissions apply to all keys
    	// in the key ring.
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
    	policy.Add(member, "roles/cloudkms.cryptoKeyEncrypterDecrypter")
    	if err := handle.SetPolicy(ctx, policy); err != nil {
    		return fmt.Errorf("failed to save policy: %w", err)
    	}
    
    	fmt.Fprintf(w, "Updated IAM policy for %s\n", name)
    	return nil
    }
    

### Java

To run this code, first [set up a Java development environment](https://docs.cloud.google.com/java/docs/setup) and [install the Cloud KMS Java SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-java).
    
    
    import com.google.cloud.kms.v1.[CryptoKeyName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyName.html);
    import com.google.cloud.kms.v1.[KeyManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html);
    import com.google.iam.v1.[Binding](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html);
    import com.google.iam.v1.[Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html);
    import java.io.IOException;
    
    public class IamAddMember {
    
      public void iamAddMember() throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String locationId = "us-east1";
        String keyRingId = "my-key-ring";
        String keyId = "my-key";
        String member = "user:foo@example.com";
        iamAddMember(projectId, locationId, keyRingId, keyId, member);
      }
    
      // Add the given IAM member to the key.
      public void iamAddMember(
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
    
          // Create a new IAM binding for the member and role.
          [Binding](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html) binding =
              [Binding](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html).newBuilder()
                  .setRole("roles/cloudkms.cryptoKeyEncrypterDecrypter")
                  .[addMembers](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.Builder.html#com_google_iam_v1_Binding_Builder_addMembers_java_lang_String_)(member)
                  .build();
    
          // Add the binding to the policy.
          [Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) newPolicy = policy.[toBuilder](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html#com_google_iam_v1_Policy_toBuilder__)().[addBindings](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.Builder.html#com_google_iam_v1_Policy_Builder_addBindings_com_google_iam_v1_Binding_)(binding).build();
    
          client.setIamPolicy(resourceName, newPolicy);
          System.out.printf("Updated IAM policy for %s%n", resourceName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyName.html#com_google_cloud_kms_v1_CryptoKeyName_toString__)());
        }
      }
    }

### Node.js

To run this code, first [set up a Node.js development environment](https://docs.cloud.google.com/nodejs/docs/setup) and [install the Cloud KMS Node.js SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-nodejs).
    
    
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
    
    async function iamAddMember() {
      // Get the current IAM policy.
      const [policy] = await client.getIamPolicy({
        resource: resourceName,
      });
    
      // Add the member to the policy.
      policy.bindings.push({
        role: 'roles/cloudkms.cryptoKeyEncrypterDecrypter',
        members: [member],
      });
    
      // Save the updated policy.
      const [updatedPolicy] = await client.setIamPolicy({
        resource: resourceName,
        policy: policy,
      });
    
      console.log('Updated policy');
      return updatedPolicy;
    }
    
    return iamAddMember();

### PHP

To run this code, first learn about [using PHP on Google Cloud](https://docs.cloud.google.com/php/docs) and [install the Cloud KMS PHP SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-php).
    
    
    use Google\Cloud\Iam\V1\Binding;
    use Google\Cloud\Iam\V1\GetIamPolicyRequest;
    use Google\Cloud\Iam\V1\SetIamPolicyRequest;
    use Google\Cloud\Kms\V1\Client\KeyManagementServiceClient;
    
    function iam_add_member(
        string $projectId = 'my-project',
        string $locationId = 'us-east1',
        string $keyRingId = 'my-key-ring',
        string $keyId = 'my-key',
        string $member = 'user:foo@example.com'
    ) {
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
    
        // Add the member to the policy.
        $bindings = $policy->getBindings();
        $bindings[] = (new Binding())
            ->setRole('roles/cloudkms.cryptoKeyEncrypterDecrypter')
            ->setMembers([$member]);
        $policy->setBindings($bindings);
    
        // Save the updated IAM policy.
        $setIamPolicyRequest = (new SetIamPolicyRequest())
            ->setResource($resourceName)
            ->setPolicy($policy);
        $updatedPolicy = $client->setIamPolicy($setIamPolicyRequest);
        printf('Added %s' . PHP_EOL, $member);
    
        return $updatedPolicy;
    }

### Python

To run this code, first [set up a Python development environment](https://docs.cloud.google.com/python/docs/setup) and [install the Cloud KMS Python SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-python).
    
    
    from google.cloud import kms
    from google.iam.v1 import policy_pb2 as iam_policy
    
    
    def iam_add_member(
        project_id: str, location_id: str, key_ring_id: str, key_id: str, member: str
    ) -> iam_policy.Policy:
        """
        Add an IAM member to a resource.
    
        Args:
            project_id (string): Google Cloud project ID (e.g. 'my-project').
            location_id (string): Cloud KMS location (e.g. 'us-east1').
            key_ring_id (string): ID of the Cloud KMS key ring (e.g. 'my-key-ring').
            key_id (string): ID of the key to use (e.g. 'my-key').
            member (string): Member to add (e.g. 'user:foo@example.com')
    
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
    
        # Add the member to the policy.
        policy.bindings.add(
            role="roles/cloudkms.cryptoKeyEncrypterDecrypter", members=[member]
        )
    
        # Save the updated IAM policy.
        request = {"resource": resource_name, "policy": policy}
    
        updated_policy = client.[set_iam_policy](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html#google_cloud_kms_v1_services_key_management_service_KeyManagementServiceClient_set_iam_policy)(request=request)
        print(f"Added {member} to {resource_name}")
        return updated_policy
    
    

### Ruby

To run this code, first [set up a Ruby development environment](https://docs.cloud.google.com/ruby/docs/setup) and [install the Cloud KMS Ruby SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-ruby).
    
    
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
    
    # Add the member to the policy.
    policy.bindings << Google::Iam::[V1](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-v1/latest/Google-Cloud-Kms-V1.html)::Binding.new(
      members: [member],
      role:    "roles/cloudkms.cryptoKeyEncrypterDecrypter"
    )
    
    # Save the updated policy.
    updated_policy = iam_client.set_iam_policy resource: resource_name, policy: policy
    puts "Added #{member}"

## Revoking access to a resource

To remove a principal's access to a Cloud KMS key:

### gcloud

To use Cloud KMS on the command line, first [Install or upgrade to the latest version of Google Cloud CLI](https://docs.cloud.google.com/sdk/install).
    
    
    gcloud kms keys remove-iam-policy-binding key \
        --keyring key-ring \
        --location location \
        --member principal-type:principal-email \
        --role roles/role-name
    

Replace key with the name of the key. Replace key-ring with the name of the key ring where the key is located. Replace location with the Cloud KMS location for the key ring. Replace principal-type and principal-email with the type of principal and the principal's email address. Replace role-name with the name of the role to remove.

For information on all flags and possible values, run the command with the `--help` flag.

### C#

To run this code, first [set up a C# development environment](https://docs.cloud.google.com/dotnet/docs/setup) and [install the Cloud KMS C# SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-csharp).
    
    
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

To run this code, first [set up a Go development environment](https://docs.cloud.google.com/go/docs/setup) and [install the Cloud KMS Go SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-go).
    
    
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

To run this code, first [set up a Java development environment](https://docs.cloud.google.com/java/docs/setup) and [install the Cloud KMS Java SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-java).
    
    
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

To run this code, first [set up a Node.js development environment](https://docs.cloud.google.com/nodejs/docs/setup) and [install the Cloud KMS Node.js SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-nodejs).
    
    
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

To run this code, first learn about [using PHP on Google Cloud](https://docs.cloud.google.com/php/docs) and [install the Cloud KMS PHP SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-php).
    
    
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

To run this code, first [set up a Python development environment](https://docs.cloud.google.com/python/docs/setup) and [install the Cloud KMS Python SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-python).
    
    
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

To run this code, first [set up a Ruby development environment](https://docs.cloud.google.com/ruby/docs/setup) and [install the Cloud KMS Ruby SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-ruby).
    
    
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

## Viewing permissions on a resource

To view the IAM policy for a Cloud KMS key:

### gcloud

To use Cloud KMS on the command line, first [Install or upgrade to the latest version of Google Cloud CLI](https://docs.cloud.google.com/sdk/install).
    
    
    gcloud kms keys get-iam-policy key \
        --keyring key-ring \
        --location location
    

Replace key with the name of the key. Replace key-ring with the name of the key ring where the key is located. Replace location with the Cloud KMS location for the key ring.

For information on all flags and possible values, run the command with the `--help` flag.

### C#

To run this code, first [set up a C# development environment](https://docs.cloud.google.com/dotnet/docs/setup) and [install the Cloud KMS C# SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-csharp).
    
    
    using [Google.Cloud.Iam.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.html);
    using [Google.Cloud.Kms.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.html);
    using System;
    
    public class IamGetPolicySample
    {
        public Policy IamGetPolicy(
          string projectId = "my-project", string locationId = "us-east1", string keyRingId = "my-key-ring", string keyId = "my-key")
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
    
            // Print the policy.
            foreach ([Binding](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Binding.html) b in policy.[Bindings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html#Google_Cloud_Iam_V1_Policy_Bindings))
            {
                String role = b.Role;
    
                foreach (String member in b.[Members](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Binding.html#Google_Cloud_Iam_V1_Binding_Members))
                {
                    // ...
                }
            }
    
            // Return the policy.
            return policy;
        }
    }

### Go

To run this code, first [set up a Go development environment](https://docs.cloud.google.com/go/docs/setup) and [install the Cloud KMS Go SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-go).
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	kms "cloud.google.com/go/kms/apiv1"
    )
    
    // iamGetPolicy retrieves and prints the Cloud IAM policy associated with the
    // Cloud KMS key.
    func iamGetPolicy(w io.Writer, name string) error {
    	// NOTE: The resource name can be either a key or a key ring.
    	//
    	// name := "projects/my-project/locations/us-east1/keyRings/my-key-ring/cryptoKeys/my-key"
    	// name := "projects/my-project/locations/us-east1/keyRings/my-key-ring"
    
    	// Create the client.
    	ctx := context.Background()
    	client, err := kms.[NewKeyManagementClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/kms/latest/apiv1.html#cloud_google_com_go_kms_apiv1_KeyManagementClient_NewKeyManagementClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("failed to create kms client: %w", err)
    	}
    	defer client.Close()
    
    	// Get the current policy.
    	policy, err := client.[ResourceIAM](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/kms/latest/apiv1.html#cloud_google_com_go_kms_apiv1_KeyManagementClient_ResourceIAM)(name).Policy(ctx)
    	if err != nil {
    		return fmt.Errorf("failed to get IAM policy: %w", err)
    	}
    
    	// Print the policy members.
    	for _, role := range policy.Roles() {
    		fmt.Fprintf(w, "%s\n", role)
    		for _, member := range policy.Members(role) {
    			fmt.Fprintf(w, "- %s\n", member)
    		}
    		fmt.Fprintf(w, "\n")
    	}
    	return nil
    }
    

### Java

To run this code, first [set up a Java development environment](https://docs.cloud.google.com/java/docs/setup) and [install the Cloud KMS Java SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-java).
    
    
    import com.google.cloud.kms.v1.[CryptoKeyName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyName.html);
    import com.google.cloud.kms.v1.[KeyManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html);
    import com.google.iam.v1.[Binding](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html);
    import com.google.iam.v1.[Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html);
    import java.io.IOException;
    
    public class IamGetPolicy {
    
      public void iamGetPolicy() throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String locationId = "us-east1";
        String keyRingId = "my-key-ring";
        String keyId = "my-key";
        iamGetPolicy(projectId, locationId, keyRingId, keyId);
      }
    
      // Get the IAM policy for the given key.
      public void iamGetPolicy(String projectId, String locationId, String keyRingId, String keyId)
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
    
          // Print the policy.
          System.out.printf("IAM policy:%n");
          for ([Binding](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html) binding : policy.[getBindingsList](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html#com_google_iam_v1_Policy_getBindingsList__)()) {
            System.out.printf("%s%n", binding.getRole());
            for (String member : binding.getMembersList()) {
              System.out.printf("- %s%n", member);
            }
          }
        }
      }
    }

### Node.js

To run this code, first [set up a Node.js development environment](https://docs.cloud.google.com/nodejs/docs/setup) and [install the Cloud KMS Node.js SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-nodejs).
    
    
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
    
    async function iamGetPolicy() {
      const [policy] = await client.getIamPolicy({
        resource: resourceName,
      });
    
      for (const binding of policy.bindings) {
        console.log(`Role: ${binding.role}`);
        for (const member of binding.members) {
          console.log(`  - ${member}`);
        }
      }
    
      return policy;
    }
    
    return iamGetPolicy();

### PHP

To run this code, first learn about [using PHP on Google Cloud](https://docs.cloud.google.com/php/docs) and [install the Cloud KMS PHP SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-php).
    
    
    use Google\Cloud\Iam\V1\GetIamPolicyRequest;
    use Google\Cloud\Kms\V1\Client\KeyManagementServiceClient;
    
    function iam_get_policy(
        string $projectId = 'my-project',
        string $locationId = 'us-east1',
        string $keyRingId = 'my-key-ring',
        string $keyId = 'my-key'
    ) {
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
    
        // Print the policy.
        printf('IAM policy for %s' . PHP_EOL, $resourceName);
        foreach ($policy->getBindings() as $binding) {
            printf('%s' . PHP_EOL, $binding->getRole());
    
            foreach ($binding->getMembers() as $member) {
                printf('- %s' . PHP_EOL, $member);
            }
        }
    
        return $policy;
    }

### Python

To run this code, first [set up a Python development environment](https://docs.cloud.google.com/python/docs/setup) and [install the Cloud KMS Python SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-python).
    
    
    from google.cloud import kms
    from google.iam.v1 import policy_pb2 as iam_policy
    
    
    def iam_get_policy(
        project_id: str, location_id: str, key_ring_id: str, key_id: str
    ) -> iam_policy.Policy:
        """
        Get the IAM policy for a resource.
    
        Args:
            project_id (string): Google Cloud project ID (e.g. 'my-project').
            location_id (string): Cloud KMS location (e.g. 'us-east1').
            key_ring_id (string): ID of the Cloud KMS key ring (e.g. 'my-key-ring').
            key_id (string): ID of the key to use (e.g. 'my-key').
    
        Returns:
            Policy: Cloud IAM policy.
    
        """
    
        # Create the client.
        client = kms.[KeyManagementServiceClient](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html)()
    
        # Build the resource name.
        resource_name = client.[crypto_key_path](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html#google_cloud_kms_v1_services_key_management_service_KeyManagementServiceClient_crypto_key_path)(project_id, location_id, key_ring_id, key_id)
    
        # The resource name could also be a key ring.
        # resource_name = client.key_ring_path(project_id, location_id, key_ring_id);
    
        # Get the current policy.
        policy = client.[get_iam_policy](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html#google_cloud_kms_v1_services_key_management_service_KeyManagementServiceClient_get_iam_policy)(request={"resource": resource_name})
    
        # Print the policy
        print(f"IAM policy for {resource_name}")
        for binding in policy.bindings:
            print(binding.role)
            for member in binding.members:
                print(f"- {member}")
    
        return policy
    
    

### Ruby

To run this code, first [set up a Ruby development environment](https://docs.cloud.google.com/ruby/docs/setup) and [install the Cloud KMS Ruby SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-ruby).
    
    
    # TODO(developer): uncomment these values before running the sample.
    # project_id  = "my-project"
    # location_id = "us-east1"
    # key_ring_id = "my-key-ring"
    # key_id      = "my-key"
    
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
    
    # Print the policy.
    puts "Policy for #{resource_name}"
    policy.bindings.each do |bind|
      puts bind.role
      bind.members.each do |member|
        puts "- #{member}"
      end
    end

## Principle of least privilege

To practice the principle of least privilege, grant the most limited set of permissions to the lowest object in the resource hierarchy.

  * To grant a principal permissions to encrypt (but not decrypt) data, grant the `roles/cloudkms.cryptoKeyEncrypter` role on the key.

  * To grant a principal permissions to encrypt and decrypt data, grant the `roles/cloudkms.cryptoKeyEncrypterDecrypter` role on the key.

  * To grant a principal permissions to verify (but not sign) data, grant the `roles/cloudkms.publicKeyViewer` role on the key.

  * To grant a principal permissions to sign and verify data, grant the `roles/cloudkms.signerVerifier` role on the key.

  * To grant a principal permissions to manage a key, grant the `roles/cloudkms.admin` role on the key.




This is not an exhaustive list. See [Cloud KMS permissions and roles](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles) for a full list of permissions and roles.

## Hierarchy and inheritance

Policy bindings can be specified on the project, key ring, key, import job, and other Cloud KMS resources.

Since keys belong to key rings, and key rings belong to projects, a principal with a specific role or permission at a higher level in that hierarchy inherits the same permissions on the child resources. That is, a user who has the role of `owner` on a project is also an `owner` on all the key rings and keys in that project. Similarly, if a user is granted the `cloudkms.admin` role on a key ring, they have the associated permissions on all the keys in that key ring.

The inverse is not true; that is, a user who has a permission on a key but does not have the permission on the parent key ring has no permissions on that key ring.

**Note:** A user that only has permissions on key rings or keys, but not on the project itself, will not be able to manage key resources in the Google Cloud console. To enable their use of the Google Cloud console, depending on security requirements, one option might be to also grant that user a `browser` role on the project.

## What's next

  * Learn more about [Permissions and roles in Cloud KMS](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles).
  * [Create a key](https://docs.cloud.google.com/kms/docs/creating-keys).
  * [Encrypt and decrypt data](https://docs.cloud.google.com/kms/docs/encrypt-decrypt).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
