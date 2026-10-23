---
url: https://docs.cloud.google.com/storage/docs/encryption/using-customer-managed-keys/
title: Use customer-managed encryption keys \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:34.602404+00:00
---

# Use customer-managed encryption keys  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/encryption/using-customer-managed-keys/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Use customer-managed encryption keys Stay organized with collections  Save and categorize content based on your preferences. 

[Overview](https://docs.cloud.google.com/storage/docs/encryption/customer-managed-keys)

You can use customer-managed encryption keys (CMEK) with [Cloud Key Management Service](https://docs.cloud.google.com/kms/docs). You create and manage CMEK through Cloud KMS. For an overview of all encryption options, see [Data encryption options](https://docs.cloud.google.com/storage/docs/encryption).

You can use manually-created Cloud KMS encryption keys to protect your Cloud Storage data. For example, you can set a default key on a bucket or encrypt individual objects with a Cloud KMS key.

These keys can be stored as software keys, in an [HSM cluster](https://docs.cloud.google.com/kms/docs/hsm), or [externally](https://docs.cloud.google.com/kms/docs/ekm). If you want to use the Cloud KMS [Autokey feature](https://docs.cloud.google.com/kms/docs/autokey-overview) to generate key rings and keys on demand that help protect your Cloud Storage buckets and the objects within them, see [Using Autokey with Cloud Storage resources](https://docs.cloud.google.com/kms/docs/create-resource-with-autokey#storage-autokey). For a comparison of CMEK with Autokey and Google default encryption, see [Comparison of CMEK and Google-owned and Google-managed encryption keys](https://docs.cloud.google.com/kms/docs/cmek#cmek-comparison). 

## Before you begin

Before using this feature in Cloud Storage, you must:

  1. Enable the Cloud KMS API for the project that will store your encryption keys.

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=cloudkms.googleapis.com)

  2. Have sufficient permission for the project that will store your encryption keys:

     * If you own the project that will store your keys, you most likely have the necessary permission.

     * If you plan to create new encryption key rings and keys, you should have [`cloudkms.keyRings.create` and `cloudkms.cryptoKeys.create`](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles) permission.

     * Whether you plan to use new or existing key rings and keys, you should have [`cloudkms.cryptoKeys.setIamPolicy`](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles) permission for the keys that you will use for encryption.

This permission allows you to give Cloud Storage service agents access to Cloud KMS keys.

     * The above permissions are contained in the **Cloud KMS Admin** role.

See [Using IAM with Cloud KMS](https://docs.cloud.google.com/kms/docs/iam) for instructions on how to get this or other Cloud KMS roles.

  3. [Have a Cloud KMS key ring](https://docs.cloud.google.com/kms/docs/creating-keys#create_a_key_ring), and [have at least one key](https://docs.cloud.google.com/kms/docs/creating-keys#create_a_key) within the key ring.

The key ring must be in the same location as the data you intend to encrypt, but it can be in a different project. For available Cloud KMS locations, see [Cloud KMS locations](https://docs.cloud.google.com/kms/docs/locations).

**Note:** For buckets in [dual-regions](https://docs.cloud.google.com/storage/docs/locations#location-dr), the Cloud KMS location must match the location code associated with the dual-region. This means that for configurable dual-regions, you must create the key ring in the associated multi-region, but for predefined dual-regions, you must create the key ring in the same predefined dual-region.
  4. Have sufficient permission to work with objects in your Cloud Storage bucket:

     * If you own the project that contains the bucket, you most likely have the necessary permission.

     * If you use IAM, you should have `storage.objects.create` [permission](https://docs.cloud.google.com/storage/docs/access-control/iam#permissions) to write objects to the bucket and `storage.objects.get` permission to read objects from the bucket. See [Using IAM Permissions](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions#bucket-add) for instructions on how to get a role, such as **Storage Object Admin** that has these permissions.

     * If you use ACLs, you should have bucket-scoped [`WRITER` permission](https://docs.cloud.google.com/storage/docs/access-control/lists#permissions) to write objects to the bucket and object-scoped `READER` permission to read objects from the bucket. See [Setting ACLs](https://docs.cloud.google.com/storage/docs/access-control/create-manage-lists#set-an-acl) for instructions on how to do this.

  5. **Note:** The following step is not necessary if you are using the Google Cloud CLI.

[Get the email address of the service agent](https://docs.cloud.google.com/storage/docs/getting-service-agent) associated with the project that contains your Cloud Storage bucket. By performing this step, you automatically create the service agent if it doesn't currently exist.




## Assign a Cloud KMS key to a service agent

In order to use CMEKs, grant the Cloud Storage service agent associated with your bucket the permission to use your Cloud KMS key for encrypting and decrypting:

### Console

  1. In the Google Cloud console, go to the **Key management** page. 

[Go to Key management](https://console.cloud.google.com/security/kms)

  2. Click the name of the key ring that contains the key you want to use.

  3. Select the checkbox for the desired key.

The **Permissions** tab in the right window pane becomes available.

  4. In the **Add principals** dialog, specify the email address of the Cloud Storage service agent you are granting access.

  5. In the **Select a role** drop down, select **Cloud KMS CryptoKey Encrypter/Decrypter**.

  6. Click **Add**.




To learn how to get detailed error information about failed Cloud Storage operations in the Google Cloud console, see [Troubleshooting](https://docs.cloud.google.com/storage/docs/troubleshooting#trouble-console).

### Command line

Use the [`gcloud storage service-agent`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/service-agent) command with the `--authorize-cmek` flag to give the service agent associated with your bucket permission to encrypt and decrypt objects using your Cloud KMS key:
    
    
    gcloud storage service-agent --project=PROJECT_STORING_OBJECTS --authorize-cmek=KEY_RESOURCE

Where:

  * `PROJECT_STORING_OBJECTS` is the ID or number for the project containing the objects you want to encrypt or decrypt. For example, `my-pet-project`.
  * `KEY_RESOURCE` is your [Cloud KMS key resource](https://docs.cloud.google.com/kms/docs/resource-hierarchy#retrieve_resource_id).



### Client libraries

### C#

For more information, see the [Cloud Storage C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
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

For more information, see the [Cloud Storage Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/storage). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
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

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
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

For more information, see the [Cloud Storage Node.js API reference documentation](https://cloud.google.com/nodejs/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
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

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
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

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
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

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    # TODO(developer): uncomment these values before running the sample.
    # project_id  = "my-project"
    # location_id = "us-east1"
    # key_ring_id = "my-key-ring"
    # key_id      = "my-key"
    # member      = "user:foo@example.com"
    
    # Require the library.
    require "google/cloud/kms"
    
    # Create the client.
    client = Google::Cloud::[Kms](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms/latest/Google-Cloud-Kms.html).[key_management_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms/latest/Google-Cloud-Kms.html)
    
    # Build the resource name.
    resource_name = client.crypto_key_path project:    project_id,
                                           location:   location_id,
                                           key_ring:   key_ring_id,
                                           crypto_key: key_id
    
    # The resource name could also be a key ring.
    # resource_name = client.key_ring_path project: project_id, location: location_id, key_ring: key_ring_id
    
    # Create the IAM client.
    iam_client = Google::Cloud::[Kms](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms/latest/Google-Cloud-Kms.html)::[V1](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-v1/latest/Google-Cloud-Kms-V1.html)::IAMPolicy::Client.new
    
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

### REST APIs

### JSON API

**Note:** This task uses a separate endpoint compared to most Cloud Storage tasks.

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Create a JSON file that contains the following information:
         
         {
           "policy": {
             "bindings": {
               "role": "roles/cloudkms.cryptoKeyEncrypterDecrypter",
               "members": "serviceAccount:SERVICE_AGENT_EMAIL_ADDRESS"
             },
           }
         }

Where `SERVICE_AGENT_EMAIL_ADDRESS` is the email address associated with your service agent. For example, `service-7550275089395@gs-project-accounts.iam.gserviceaccount.com`.

  3. Use [`cURL`](https://curl.haxx.se/) to call the Cloud KMS API with a [`POST setIamPolicy`](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/setIamPolicy) request:
         
         curl -X POST --data-binary @JSON_FILE_NAME \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         "https://cloudkms.googleapis.com/v1/KEY_RESOURCE:setIamPolicy"

Where:

     * `JSON_FILE_NAME` is the path for the JSON file that you created in Step 2.
     * `KEY_RESOURCE` is your [Cloud KMS key resource](https://docs.cloud.google.com/kms/docs/resource-hierarchy#retrieve_resource_id).

**Caution:** This request replaces any existing IAM policy on the key resource.**Note:** There may be a delay of several seconds between assigning the role and having it applied to your service agent. If you grant this permission programmatically, wait 30 seconds before configuring Cloud Storage.

### XML API

The XML API cannot be used to assign a Cloud KMS to a service agent. Use one of the other Cloud Storage tools, such as the gcloud CLI, instead.

## Use default encryption keys

The following sections describe how to use default encryption keys.

### Set the default key for a bucket

To add, change, or remove the Cloud KMS key that is used by default when objects are written to a bucket:

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the bucket.

  3. Click the **Configuration** tab.

  4. In the **Protection** section, click edit **Edit encryption**.

  5. In the **Default encryption key type** section, do either of the following things:

     * To add or change the default Cloud KMS key for the bucket, select **Cloud KMS key**. Then, select one of the available keys from the list.

     * To remove the default Cloud KMS key, select **Google-managed encryption key**.

  6. Click **Save**.




To learn how to get detailed error information about failed Cloud Storage operations in the Google Cloud console, see [Troubleshooting](https://docs.cloud.google.com/storage/docs/troubleshooting#trouble-console).

### Command line

Use the [`gcloud storage buckets update`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/update) command with the appropriate flag:
    
    
    gcloud storage buckets update gs://BUCKET_NAME FLAG

Where:

  * `BUCKET_NAME` is the name of the relevant bucket. For example, `my-bucket`.

  * `FLAG` is the desired setting for the default key on the bucket. Use one of the following formats:

    * `--default-encryption-key=` and a [Cloud KMS key resource](https://docs.cloud.google.com/kms/docs/resource-hierarchy#retrieve_resource_id), if you want to add or change a default key.
    * `--clear-default-encryption-key`, if you want to remove the default key on the bucket.



If successful, the response looks like:
    
    
    Updating gs://my-bucket/...
      Completed 1  

### Client libraries

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample sets a default customer-managed encryption key on a bucket:
    
    
    namespace gcs = ::google::cloud::storage;
    using ::google::cloud::StatusOr;
    [](gcs::Client client, std::string const& bucket_name,
       std::string const& key_name) {
      StatusOr<gcs::BucketMetadata> updated = client.PatchBucket(
          bucket_name, gcs::BucketMetadataPatchBuilder().SetEncryption(
                           gcs::BucketEncryption{key_name, {}, {}, {}}));
      if (!updated) throw std::move(updated).status();
    
      if (!updated->has_encryption()) {
        std::cerr << "The change to set the encryption attribute on bucket "
                  << updated->name()
                  << " was successful, but the encryption is not set."
                  << "This is unexpected, maybe a concurrent change?\n";
        return;
      }
    
      std::cout << "Successfully set default KMS key on bucket "
                << updated->name() << " to "
                << updated->encryption().default_kms_key_name << "."
                << "\nFull metadata: " << *updated << "\n";
    }

The following sample removes the default customer-managed encryption key from a bucket:
    
    
    namespace gcs = ::google::cloud::storage;
    using ::google::cloud::StatusOr;
    [](gcs::Client client, std::string const& bucket_name) {
      StatusOr<gcs::BucketMetadata> updated = client.PatchBucket(
          bucket_name, gcs::BucketMetadataPatchBuilder().ResetEncryption());
      if (!updated) throw std::move(updated).status();
    
      std::cout << "Successfully removed default KMS key on bucket "
                << updated->name() << "\n";
    }

### C#

For more information, see the [Cloud Storage C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample sets a default customer-managed encryption key on a bucket:
    
    
    using Google.Apis.Storage.v1.Data;
    using [Google.Cloud.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html);
    using System;
    
    public class EnableDefaultKMSKeySample
    {
        public Bucket EnableDefaultKMSKey(
            string projectId = "your-project-id",
            string bucketName = "your-unique-bucket-name",
            string keyLocation = "us-west1",
            string kmsKeyRing = "kms-key-ring",
            string kmsKeyName = "key-name")
        {
            // KMS Key identifier of an already created KMS key.
            // If you use the Google.Cloud.Kms.V1 library, you can construct these names using helper class CryptoKeyName.
            // var fullKeyName = new CryptoKeyName(projectId, keyLocation, kmsKeyRing, kmsKeyName).ToString();
            string keyPrefix = $"projects/{projectId}/locations/{keyLocation}";
            string fullKeyringName = $"{keyPrefix}/keyRings/{kmsKeyRing}";
            string fullKeyName = $"{fullKeyringName}/cryptoKeys/{kmsKeyName}";
            var storage = [StorageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html#Google_Cloud_Storage_V1_StorageClient_Create)();
            var bucket = storage.GetBucket(bucketName, new [GetBucketOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.GetBucketOptions.html) { Projection = [Projection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.Projection.html).[Full](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.Projection.html#Google_Cloud_Storage_V1_Projection_Full) });
            bucket.Encryption = new Bucket.EncryptionData { DefaultKmsKeyName = fullKeyName };
            var updatedBucket = storage.UpdateBucket(bucket);
            Console.WriteLine($"Default KMS key for {bucketName} was set to {kmsKeyName}.");
            return updatedBucket;
        }
    }

The following sample removes the default customer-managed encryption key from a bucket:
    
    
    using Google.Apis.Storage.v1.Data;
    using [Google.Cloud.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html);
    using System;
    
    public class BucketDeleteDefaultKmsKeySample
    {
        public Bucket BucketDeleteDefaultKmsKey(string bucketName = "your-bucket-name")
        {
            var storage = [StorageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html#Google_Cloud_Storage_V1_StorageClient_Create)();
            var bucket = storage.GetBucket(bucketName);
    
            if (bucket.Encryption == null)
            {
                Console.WriteLine("No default kms key to remove");
            }
            else
            {
                bucket.Encryption.DefaultKmsKeyName = null;
                bucket = storage.UpdateBucket(bucket);
                Console.WriteLine($"Default KMS key was removed from {bucketName}. ");
            }
    
            return bucket;
        }
    }

### Go

For more information, see the [Cloud Storage Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/storage). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample sets a default customer-managed encryption key on a bucket:
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"time"
    
    	"cloud.google.com/go/storage"
    )
    
    // setBucketDefaultKMSKey sets the Cloud KMS encryption key for the bucket.
    func setBucketDefaultKMSKey(w io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), bucketName, keyName string) error {
    	// bucketName := "bucket-name"
    	// keyName := "key"
    	ctx := context.Background()
    	client, err := storage.NewClient(ctx)
    	if err != nil {
    		return fmt.Errorf("storage.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	ctx, cancel := context.WithTimeout(ctx, time.Second*10)
    	defer cancel()
    
    	bucket := client.[Bucket](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Bucket)(bucketName)
    	bucketAttrsToUpdate := storage.[BucketAttrsToUpdate](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketAttrsToUpdate){
    		Encryption: &storage.[BucketEncryption](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketEncryption){DefaultKMSKeyName: keyName},
    	}
    	if _, err := bucket.Update(ctx, bucketAttrsToUpdate); err != nil {
    		return fmt.Errorf("Bucket(%q).Update: %w", bucketName, err)
    	}
    	fmt.Fprintf(w, "Default KMS Key Name: %v", bucketAttrsToUpdate.Encryption.DefaultKMSKeyName)
    	return nil
    }
    

The following sample removes the default customer-managed encryption key from a bucket:
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"time"
    
    	"cloud.google.com/go/storage"
    )
    
    // removeBucketDefaultKMSKey removes any default Cloud KMS key set on a bucket.
    func removeBucketDefaultKMSKey(w io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), bucketName string) error {
    	// bucketName := "bucket-name"
    	ctx := context.Background()
    	client, err := storage.NewClient(ctx)
    	if err != nil {
    		return fmt.Errorf("storage.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	ctx, cancel := context.WithTimeout(ctx, time.Second*10)
    	defer cancel()
    
    	bucket := client.[Bucket](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Bucket)(bucketName)
    	bucketAttrsToUpdate := storage.[BucketAttrsToUpdate](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketAttrsToUpdate){
    		Encryption: &storage.[BucketEncryption](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketEncryption){},
    	}
    	if _, err := bucket.Update(ctx, bucketAttrsToUpdate); err != nil {
    		return fmt.Errorf("Bucket(%q).Update: %w", bucketName, err)
    	}
    	fmt.Fprintf(w, "Default KMS key was removed from: %v", bucketName)
    	return nil
    }
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample sets a default customer-managed encryption key on a bucket:
    
    
    import com.google.cloud.storage.[Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html).[BucketTargetOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.BucketTargetOption.html);
    import com.google.cloud.storage.[StorageException](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageException.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    
    public class SetBucketDefaultKmsKey {
      public static void setBucketDefaultKmsKey(String projectId, String bucketName, String kmsKeyName)
          throws [StorageException](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageException.html) {
        // The ID of your GCP project
        // String projectId = "your-project-id";
    
        // The ID of your GCS bucket
        // String bucketName = "your-unique-bucket-name";
    
        // The name of the KMS key to use as a default
        // String kmsKeyName =
        // "projects/your-project-id/locations/us/keyRings/my_key_ring/cryptoKeys/my_key"
    
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder().setProjectId(projectId).build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)();
        // first look up the bucket, so we will have its metageneration
        [Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html) bucket = storage.[get](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_get_com_google_cloud_storage_BlobId_)(bucketName);
    
        [Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html) updated =
            storage.[update](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_update_com_google_cloud_storage_BlobInfo_)(
                bucket.toBuilder().setDefaultKmsKeyName(kmsKeyName).build(),
                BucketTargetOption.metagenerationMatch());
    
        System.out.println(
            "KMS Key "
                + updated.[getDefaultKmsKeyName](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html#com_google_cloud_storage_BucketInfo_getDefaultKmsKeyName__)()
                + "was set to default for bucket "
                + bucketName);
      }
    }

The following sample removes the default customer-managed encryption key from a bucket:
    
    
    import com.google.cloud.storage.[Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html).[BucketTargetOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.BucketTargetOption.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    
    public class RemoveBucketDefaultKmsKey {
      public static void removeBucketDefaultKmsKey(String projectId, String bucketName) {
        // The ID of your GCP project
        // String projectId = "your-project-id";
    
        // The ID of your GCS bucket
        // String bucketName = "your-unique-bucket-name";
    
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder().setProjectId(projectId).build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)();
        // first look up the bucket, so we will have its metageneration
        [Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html) bucket = storage.[get](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_get_com_google_cloud_storage_BlobId_)(bucketName);
        storage.[update](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_update_com_google_cloud_storage_BlobInfo_)(
            bucket.toBuilder().setDefaultKmsKeyName(null).build(),
            BucketTargetOption.metagenerationMatch());
    
        System.out.println("Default KMS key was removed from " + bucketName);
      }
    }

### Node.js

For more information, see the [Cloud Storage Node.js API reference documentation](https://cloud.google.com/nodejs/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample sets a default customer-managed encryption key on a bucket:
    
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // The ID of your GCS bucket
    // const bucketName = 'your-unique-bucket-name';
    
    // The name of the KMS-key to use as a default
    // const defaultKmsKeyName = 'my-key';
    
    // Imports the Google Cloud client library
    const {Storage} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    
    // Creates a client
    const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)();
    
    async function enableDefaultKMSKey() {
      await storage.bucket(bucketName).setMetadata({
        encryption: {
          defaultKmsKeyName,
        },
      });
    
      console.log(
        `Default KMS key for ${bucketName} was set to ${defaultKmsKeyName}.`
      );
    }
    
    enableDefaultKMSKey().catch(console.error);

The following sample removes the default customer-managed encryption key from a bucket:
    
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // The ID of your GCS bucket
    // const bucketName = 'your-unique-bucket-name';
    
    // Imports the Google Cloud client library
    const {Storage} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    
    // Creates a client
    const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)();
    
    async function removeDefaultKMSKey() {
      await storage.bucket(bucketName).setMetadata({
        encryption: {
          defaultKmsKeyName: null,
        },
      });
    
      console.log(`Default KMS key was removed from ${bucketName}`);
    }
    
    removeDefaultKMSKey().catch(console.error);

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample sets a default customer-managed encryption key on a bucket:
    
    
    use Google\Cloud\Storage\StorageClient;
    
    /**
     * Enable a bucket's requesterpays metadata.
     *
     * @param string $bucketName The name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     * @param string $kmsKeyName The KMS key to use as the default KMS key.
     *     Key names are provided in the following format:
     *     `projects/<PROJECT>/locations/<LOCATION>/keyRings/<RING_NAME>/cryptoKeys/<KEY_NAME>`.
     */
    function enable_default_kms_key(string $bucketName, string $kmsKeyName): void
    {
        $storage = new StorageClient();
        $bucket = $storage->bucket($bucketName);
        $bucket->update([
            'encryption' => [
                'defaultKmsKeyName' => $kmsKeyName
            ]
        ]);
        printf('Default KMS key for %s was set to %s' . PHP_EOL,
            $bucketName,
            $bucket->info()['encryption']['defaultKmsKeyName']);
    }

The following sample removes the default customer-managed encryption key from a bucket:
    
    
    use Google\Cloud\Storage\StorageClient;
    
    /**
     * Delete the default KMS key on the given bucket.
     *
     * @param string $bucketName The name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     */
    function bucket_delete_default_kms_key(string $bucketName): void
    {
        $storage = new StorageClient();
        $bucket = $storage->bucket($bucketName);
    
        $objects = $bucket->objects([
            'encryption' => [
                'defaultKmsKeyName' => null,
            ]
        ]);
    
        printf('Default KMS key was removed from %s', $bucketName);
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample sets a default customer-managed encryption key on a bucket:
    
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
    
    def enable_default_kms_key(bucket_name, kms_key_name):
        """Sets a bucket's default KMS key."""
        # bucket_name = "your-bucket-name"
        # kms_key_name = "projects/PROJ/locations/LOC/keyRings/RING/cryptoKey/KEY"
    
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
        bucket = storage_client.[get_bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_get_bucket)(bucket_name)
        bucket.default_kms_key_name = kms_key_name
        bucket.patch()
    
        print(
            "Set default KMS key for bucket {} to {}.".format(
                bucket.name, bucket.default_kms_key_name
            )
        )
    
    

The following sample removes the default customer-managed encryption key from a bucket:
    
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
    
    def bucket_delete_default_kms_key(bucket_name):
        """Delete a default KMS key of bucket"""
        # bucket_name = "your-bucket-name"
    
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
    
        bucket = storage_client.[get_bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_get_bucket)(bucket_name)
        bucket.default_kms_key_name = None
        bucket.patch()
    
        print(f"Default KMS key was removed from {bucket.name}")
        return bucket
    
    

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample sets a default customer-managed encryption key on a bucket:
    
    
    def set_bucket_default_kms_key bucket_name:, default_kms_key:
      # The ID of your GCS bucket
      # bucket_name = "your-unique-bucket-name"
    
      # The name of the KMS key to manage this object with
      # default_kms_key = "projects/your-project-id/locations/global/keyRings/your-key-ring/cryptoKeys/your-key"
    
      require "google/cloud/storage"
    
      storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage-control-v2/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
      bucket  = storage.bucket bucket_name
    
      bucket.[default_kms_key](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html) = default_kms_key
    
      puts "Default KMS key for #{bucket.name} was set to #{bucket.[default_kms_key](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html)}"
    end

The following sample removes the default customer-managed encryption key from a bucket:
    
    
    def bucket_delete_default_kms_key bucket_name:
      # The ID of your GCS bucket
      # bucket_name = "your-unique-bucket-name"
    
      require "google/cloud/storage"
    
      storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage-control-v2/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
      bucket = storage.bucket bucket_name
    
      bucket.[default_kms_key](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html) = nil
    
      puts "Default KMS key was removed from #{bucket_name}"
    end

### Rust

The following sample sets a default customer-managed encryption key on a bucket:
    
    
    use google_cloud_storage::client::StorageControl;
    use google_cloud_storage::model::bucket::Encryption;
    use google_cloud_wkt::FieldMask;
    
    pub async fn sample(client: &StorageControl, bucket_id: &str, kms_key: &str) -> anyhow::Result<()> {
        let bucket = client
            .get_bucket()
            .set_name(format!("projects/_/buckets/{bucket_id}"))
            .send()
            .await?;
        let metageneration = bucket.metageneration;
        let bucket = client
            .update_bucket()
            .set_bucket(bucket.set_encryption(Encryption::new().set_default_kms_key(kms_key)))
            .set_if_metageneration_match(metageneration)
            .set_update_mask(FieldMask::default().set_paths(["encryption.default_kms_key"]))
            .send()
            .await?;
        println!(
            "successfully updated default KMS key for bucket {bucket_id}: {:?}",
            bucket.encryption
        );
        Ok(())
    }

The following sample removes the default customer-managed encryption key from a bucket:
    
    
    use google_cloud_storage::client::StorageControl;
    use google_cloud_storage::model::bucket::Encryption;
    use google_cloud_wkt::FieldMask;
    
    pub async fn sample(client: &StorageControl, bucket_id: &str) -> anyhow::Result<()> {
        let bucket = client
            .get_bucket()
            .set_name(format!("projects/_/buckets/{bucket_id}"))
            .send()
            .await?;
        let metageneration = bucket.metageneration;
        let bucket = client
            .update_bucket()
            .set_bucket(bucket.set_or_clear_encryption(None::<Encryption>))
            .set_if_metageneration_match(metageneration)
            .set_update_mask(FieldMask::default().set_paths(["encryption.default_kms_key"]))
            .send()
            .await?;
        println!(
            "successfully deleted default kms key for bucket {bucket_id}: {:?}",
            bucket.encryption
        );
        Ok(())
    }

### REST APIs

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Create a JSON file that contains the following information:
         
         {
           "encryption": {
             "defaultKmsKeyName": "KEY_RESOURCE"
           }
         }

Where `KEY_RESOURCE` is your [Cloud KMS key resource](https://docs.cloud.google.com/kms/docs/resource-hierarchy#retrieve_resource_id).

To remove the default Cloud KMS key from a bucket, use the following in the JSON file:
         
         {
           "encryption": {
             "defaultKmsKeyName": null
           }
         }

  3. Use [`cURL`](https://curl.haxx.se/) to call the JSON API with a [`PATCH` Bucket](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/patch) request:
         
         curl -X PATCH --data-binary @JSON_FILE_NAME \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME?fields=encryption"

Where:

     * `JSON_FILE_NAME` is the path for the JSON file that you created in Step 2.
     * `BUCKET_NAME` is the name of the relevant bucket. For example, `my-bucket`.



### XML API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Create an XML file that contains the following information:
         
         <EncryptionConfiguration>
           <DefaultKmsKeyName>KEY_RESOURCE</DefaultKmsKeyName>
         </EncryptionConfiguration>

Where `KEY_RESOURCE` is your [Cloud KMS key resource](https://docs.cloud.google.com/kms/docs/resource-hierarchy#retrieve_resource_id).

To remove the default Cloud KMS key from a bucket, use the following in the XML file.

**Caution:** The contents of the request body replace any existing encryption settings, including [which encryption methods are restricted for the bucket](https://docs.cloud.google.com/storage/docs/encryption/enforce-encryption-types#update-encryption-enforcement) (if any), so include all values that you want to apply. For a complete list of encryption settings, see the [`EncryptionConfiguration` request body elements](https://docs.cloud.google.com/storage/docs/xml-api/put-bucket-metadata#encryptionconfig-body).
         
         <EncryptionConfiguration></EncryptionConfiguration>

  3. Use [`cURL`](https://curl.haxx.se/) to call the XML API with a [`PUT` Bucket](https://docs.cloud.google.com/storage/docs/xml-api/put-bucket-metadata) request and `encryptionConfig` query string parameter:
         
         curl -X PUT --data-binary @XML_FILE_NAME \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         "https://storage.googleapis.com/BUCKET_NAME?encryptionConfig"

Where:

     * `XML_FILE_NAME` is the path for the XML file that you created in Step 2.
     * `BUCKET_NAME` is the name of the relevant bucket. For example, `my-bucket`.



**Note:** The encryption state of objects that were written to a bucket prior to adding, changing, or removing the default key are unaffected by changes to the default key.

### View the default key for a bucket

To view the Cloud KMS key that is set as default for your bucket:

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the bucket.

  3. Click the **Configuration** tab.

  4. The default key for the bucket appears in the **Default encryption key type** field.




To learn how to get detailed error information about failed Cloud Storage operations in the Google Cloud console, see [Troubleshooting](https://docs.cloud.google.com/storage/docs/troubleshooting#trouble-console).

### Command line

Use the [`gcloud storage buckets describe`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/describe) command with the `--format` flag:
    
    
    gcloud storage buckets describe gs://BUCKET_NAME --format="default(default_kms_key)"

Where `BUCKET_NAME` is the name of the bucket whose key you want to view. For example, `my-bucket`.

If successful, the response looks like:
    
    
    default_kms_key: KEY_RESOURCE

### Client libraries

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    namespace gcs = ::google::cloud::storage;
    using ::google::cloud::StatusOr;
    [](gcs::Client client, std::string const& bucket_name) {
      StatusOr<gcs::BucketMetadata> metadata =
          client.GetBucketMetadata(bucket_name);
      if (!metadata) throw std::move(metadata).status();
    
      if (!metadata->has_encryption()) {
        std::cout << "The bucket " << metadata->name()
                  << " does not have a default KMS key set.\n";
        return;
      }
    
      std::cout << "The default KMS key for bucket " << metadata->name()
                << " is: " << metadata->encryption().default_kms_key_name << "\n";
    }

### C#

For more information, see the [Cloud Storage C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

To view the default KMS key, follow the instructions for displaying a bucket's metadata and look for the default KMS key field in the response. 
    
    
    using Google.Apis.Storage.v1.Data;
    using [Google.Cloud.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html);
    using System;
    
    public class GetBucketMetadataSample
    {
        public Bucket GetBucketMetadata(string bucketName = "your-unique-bucket-name")
        {
            var storage = [StorageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html#Google_Cloud_Storage_V1_StorageClient_Create)();
            var bucket = storage.GetBucket(bucketName, new [GetBucketOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.GetBucketOptions.html) { Projection = [Projection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.Projection.html).[Full](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.Projection.html#Google_Cloud_Storage_V1_Projection_Full) });
            Console.WriteLine($"Bucket:\t{bucket.Name}");
            Console.WriteLine($"Acl:\t{bucket.[Acl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.UrlSigner.PostPolicyStandardElement.html#Google_Cloud_Storage_V1_UrlSigner_PostPolicyStandardElement_Acl)}");
            Console.WriteLine($"Billing:\t{bucket.Billing}");
            Console.WriteLine($"Cors:\t{bucket.Cors}");
            Console.WriteLine($"DefaultEventBasedHold:\t{bucket.DefaultEventBasedHold}");
            Console.WriteLine($"DefaultObjectAcl:\t{bucket.DefaultObjectAcl}");
            Console.WriteLine($"Encryption:\t{bucket.Encryption}");
            if (bucket.Encryption != null)
            {
                Console.WriteLine($"KmsKeyName:\t{bucket.Encryption.DefaultKmsKeyName}");
            }
            Console.WriteLine($"Id:\t{bucket.Id}");
            Console.WriteLine($"Kind:\t{bucket.Kind}");
            Console.WriteLine($"Lifecycle:\t{bucket.Lifecycle}");
            Console.WriteLine($"Location:\t{bucket.Location}");
            Console.WriteLine($"LocationType:\t{bucket.LocationType}");
            Console.WriteLine($"Logging:\t{bucket.Logging}");
            Console.WriteLine($"Metageneration:\t{bucket.Metageneration}");
            Console.WriteLine($"ObjectRetention:\t{bucket.ObjectRetention}");
            Console.WriteLine($"Owner:\t{bucket.Owner}");
            Console.WriteLine($"ProjectNumber:\t{bucket.ProjectNumber}");
            Console.WriteLine($"RetentionPolicy:\t{bucket.RetentionPolicy}");
            Console.WriteLine($"SelfLink:\t{bucket.SelfLink}");
            Console.WriteLine($"StorageClass:\t{bucket.StorageClass}");
            Console.WriteLine($"TimeCreated:\t{bucket.TimeCreated}");
            Console.WriteLine($"Updated:\t{bucket.Updated}");
            Console.WriteLine($"Versioning:\t{bucket.Versioning}");
            Console.WriteLine($"Website:\t{bucket.Website}");
            Console.WriteLine($"TurboReplication:\t{bucket.Rpo}");
            if (bucket.Labels != null)
            {
                Console.WriteLine("Labels:");
                foreach (var label in bucket.Labels)
                {
                    Console.WriteLine($"{label.[Key](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.UrlSigner.PostPolicyStandardElement.html#Google_Cloud_Storage_V1_UrlSigner_PostPolicyStandardElement_Key)}:\t{label.Value}");
                }
            }
            return bucket;
        }
    }

### Go

For more information, see the [Cloud Storage Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/storage). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

To view the default KMS key, follow the instructions for displaying a bucket's metadata and look for the default KMS key field in the response. 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"time"
    
    	"cloud.google.com/go/storage"
    )
    
    // getBucketMetadata gets the bucket metadata.
    func getBucketMetadata(w io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), bucketName string) (*storage.[BucketAttrs](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketAttrs), error) {
    	// bucketName := "bucket-name"
    	ctx := context.Background()
    	client, err := storage.NewClient(ctx)
    	if err != nil {
    		return nil, fmt.Errorf("storage.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	ctx, cancel := context.WithTimeout(ctx, time.Second*10)
    	defer cancel()
    	attrs, err := client.[Bucket](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Bucket)(bucketName).Attrs(ctx)
    	if err != nil {
    		return nil, fmt.Errorf("Bucket(%q).Attrs: %w", bucketName, err)
    	}
    	fmt.Fprintf(w, "BucketName: %v\n", attrs.Name)
    	fmt.Fprintf(w, "Location: %v\n", attrs.Location)
    	fmt.Fprintf(w, "LocationType: %v\n", attrs.LocationType)
    	fmt.Fprintf(w, "StorageClass: %v\n", attrs.StorageClass)
    	fmt.Fprintf(w, "Turbo replication (RPO): %v\n", attrs.[RPO](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_RPO))
    	fmt.Fprintf(w, "TimeCreated: %v\n", attrs.Created)
    	fmt.Fprintf(w, "Metageneration: %v\n", attrs.MetaGeneration)
    	fmt.Fprintf(w, "PredefinedACL: %v\n", attrs.PredefinedACL)
    	if attrs.Encryption != nil {
    		fmt.Fprintf(w, "DefaultKmsKeyName: %v\n", attrs.Encryption.DefaultKMSKeyName)
    	}
    	if attrs.Website != nil {
    		fmt.Fprintf(w, "IndexPage: %v\n", attrs.Website.MainPageSuffix)
    		fmt.Fprintf(w, "NotFoundPage: %v\n", attrs.Website.NotFoundPage)
    	}
    	fmt.Fprintf(w, "DefaultEventBasedHold: %v\n", attrs.DefaultEventBasedHold)
    	if attrs.[RetentionPolicy](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_RetentionPolicy) != nil {
    		fmt.Fprintf(w, "RetentionEffectiveTime: %v\n", attrs.[RetentionPolicy](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_RetentionPolicy).EffectiveTime)
    		fmt.Fprintf(w, "RetentionPeriod: %v\n", attrs.[RetentionPolicy](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_RetentionPolicy).RetentionPeriod)
    		fmt.Fprintf(w, "RetentionPolicyIsLocked: %v\n", attrs.[RetentionPolicy](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_RetentionPolicy).IsLocked)
    	}
    	fmt.Fprintf(w, "ObjectRetentionMode: %v\n", attrs.ObjectRetentionMode)
    	fmt.Fprintf(w, "RequesterPays: %v\n", attrs.RequesterPays)
    	fmt.Fprintf(w, "VersioningEnabled: %v\n", attrs.VersioningEnabled)
    	if attrs.Logging != nil {
    		fmt.Fprintf(w, "LogBucket: %v\n", attrs.Logging.LogBucket)
    		fmt.Fprintf(w, "LogObjectPrefix: %v\n", attrs.Logging.LogObjectPrefix)
    	}
    	if attrs.[CORS](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_CORS) != nil {
    		fmt.Fprintln(w, "CORS:")
    		for _, v := range attrs.[CORS](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_CORS) {
    			fmt.Fprintf(w, "\tMaxAge: %v\n", v.MaxAge)
    			fmt.Fprintf(w, "\tMethods: %v\n", v.Methods)
    			fmt.Fprintf(w, "\tOrigins: %v\n", v.Origins)
    			fmt.Fprintf(w, "\tResponseHeaders: %v\n", v.ResponseHeaders)
    		}
    	}
    	if attrs.Labels != nil {
    		fmt.Fprintf(w, "\n\n\nLabels:")
    		for key, value := range attrs.Labels {
    			fmt.Fprintf(w, "\t%v = %v\n", key, value)
    		}
    	}
    	return attrs, nil
    }
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

To view the default KMS key, follow the instructions for displaying a bucket's metadata and look for the default KMS key field in the response. 
    
    
    import com.google.cloud.storage.[Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html);
    import com.google.cloud.storage.[BucketInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    import java.util.Map;
    
    public class GetBucketMetadata {
      public static void getBucketMetadata(String projectId, String bucketName) {
        // The ID of your GCP project
        // String projectId = "your-project-id";
    
        // The ID of your GCS bucket
        // String bucketName = "your-unique-bucket-name";
    
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder().setProjectId(projectId).build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)();
    
        // Select all fields. Fields can be selected individually e.g. Storage.BucketField.NAME
        [Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html) bucket =
            storage.[get](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_get_com_google_cloud_storage_BlobId_)(bucketName, Storage.BucketGetOption.fields(Storage.BucketField.values()));
    
        // Print bucket metadata
        System.out.println("BucketName: " + bucket.getName());
        System.out.println("DefaultEventBasedHold: " + bucket.[getDefaultEventBasedHold](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html#com_google_cloud_storage_BucketInfo_getDefaultEventBasedHold__)());
        System.out.println("DefaultKmsKeyName: " + bucket.[getDefaultKmsKeyName](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html#com_google_cloud_storage_BucketInfo_getDefaultKmsKeyName__)());
        System.out.println("Id: " + bucket.getGeneratedId());
        System.out.println("IndexPage: " + bucket.[getIndexPage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html#com_google_cloud_storage_BucketInfo_getIndexPage__)());
        System.out.println("Location: " + bucket.getLocation());
        System.out.println("LocationType: " + bucket.[getLocationType](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html#com_google_cloud_storage_BucketInfo_getLocationType__)());
        System.out.println("Metageneration: " + bucket.getMetageneration());
        System.out.println("NotFoundPage: " + bucket.[getNotFoundPage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html#com_google_cloud_storage_BucketInfo_getNotFoundPage__)());
        System.out.println("RetentionEffectiveTime: " + bucket.[getRetentionEffectiveTime](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html#com_google_cloud_storage_BucketInfo_getRetentionEffectiveTime__)());
        System.out.println("RetentionPeriod: " + bucket.[getRetentionPeriod](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html#com_google_cloud_storage_BucketInfo_getRetentionPeriod__)());
        System.out.println("RetentionPolicyIsLocked: " + bucket.[retentionPolicyIsLocked](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html#com_google_cloud_storage_BucketInfo_retentionPolicyIsLocked__)());
        System.out.println("RequesterPays: " + bucket.requesterPays());
        System.out.println("SelfLink: " + bucket.getSelfLink());
        System.out.println("StorageClass: " + bucket.getStorageClass().[name](https://docs.cloud.google.com/java/docs/reference/google-cloud-nio/latest/com.google.cloud.storage.contrib.nio.CloudStorageFileAttributeView.html#com_google_cloud_storage_contrib_nio_CloudStorageFileAttributeView_name__)());
        System.out.println("TimeCreated: " + bucket.getCreateTime());
        System.out.println("VersioningEnabled: " + bucket.[versioningEnabled](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html#com_google_cloud_storage_BucketInfo_versioningEnabled__)());
        System.out.println("ObjectRetention: " + bucket.getObjectRetention());
        if (bucket.getLabels() != null) {
          System.out.println("\n\n\nLabels:");
          for (Map.Entry<String, String> label : bucket.getLabels().entrySet()) {
            System.out.println(label.getKey() + "=" + label.getValue());
          }
        }
        if (bucket.getLifecycleRules() != null) {
          System.out.println("\n\n\nLifecycle Rules:");
          for (BucketInfo.LifecycleRule rule : bucket.getLifecycleRules()) {
            System.out.println(rule);
          }
        }
      }
    }

### Node.js

For more information, see the [Cloud Storage Node.js API reference documentation](https://cloud.google.com/nodejs/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

To view the default KMS key, follow the instructions for displaying a bucket's metadata and look for the default KMS key field in the response. 
    
    
    // Imports the Google Cloud client library
    const {Storage} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    
    // Creates a client
    const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)();
    
    async function getBucketMetadata() {
      /**
       * TODO(developer): Uncomment the following lines before running the sample.
       */
      // The ID of your GCS bucket
      // const bucketName = 'your-unique-bucket-name';
    
      // Get Bucket Metadata
      const [metadata] = await storage.bucket(bucketName).getMetadata();
    
      console.log([JSON](https://docs.cloud.google.com/nodejs/docs/reference/storage-transfer/latest/storage-transfer/protos.google.storagetransfer.v1.notificationconfig.payloadformat.html).stringify(metadata, null, 2));
    }

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

To view the default KMS key, follow the instructions for displaying a bucket's metadata and look for the default KMS key field in the response. 
    
    
    use Google\Cloud\Storage\StorageClient;
    
    /**
     * Get bucket metadata.
     *
     * @param string $bucketName The name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     */
    function get_bucket_metadata(string $bucketName): void
    {
        $storage = new StorageClient();
        $bucket = $storage->bucket($bucketName);
        $info = $bucket->info();
    
        printf('Bucket Metadata: %s' . PHP_EOL, print_r($info, true));
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

To view the default KMS key, follow the instructions for displaying a bucket's metadata and look for the default KMS key field in the response. 
    
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
    
    def bucket_metadata(bucket_name):
        """Prints out a bucket's metadata."""
        # bucket_name = 'your-bucket-name'
    
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
        bucket = storage_client.[get_bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_get_bucket)(bucket_name)
    
        print(f"ID: {bucket.id}")
        print(f"Name: {bucket.name}")
        print(f"Storage Class: {bucket.storage_class}")
        print(f"Location: {bucket.[location](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_location)}")
        print(f"Location Type: {bucket.[location_type](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_location_type)}")
        print(f"Cors: {bucket.[cors](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_cors)}")
        print(f"Default Event Based Hold: {bucket.[default_event_based_hold](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_default_event_based_hold)}")
        print(f"Default KMS Key Name: {bucket.default_kms_key_name}")
        print(f"Metageneration: {bucket.metageneration}")
        print(
            f"Public Access Prevention: {bucket.[iam_configuration](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_iam_configuration).[public_access_prevention](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.IAMConfiguration.html#google_cloud_storage_bucket_IAMConfiguration_public_access_prevention)}"
        )
        print(f"Retention Effective Time: {bucket.[retention_policy_effective_time](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_retention_policy_effective_time)}")
        print(f"Retention Period: {bucket.[retention_period](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_retention_period)}")
        print(f"Retention Policy Locked: {bucket.[retention_policy_locked](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_retention_policy_locked)}")
        print(f"Object Retention Mode: {bucket.[object_retention_mode](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_object_retention_mode)}")
        print(f"Requester Pays: {bucket.[requester_pays](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_requester_pays)}")
        print(f"Self Link: {bucket.self_link}")
        print(f"Time Created: {bucket.time_created}")
        print(f"Versioning Enabled: {bucket.[versioning_enabled](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_versioning_enabled)}")
        print(f"Labels: {bucket.[labels](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_labels)}")
    
    

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

To view the default KMS key, follow the instructions for displaying a bucket's metadata and look for the default KMS key field in the response. 
    
    
    def get_bucket_metadata bucket_name:
      # The ID of your GCS bucket
      # bucket_name = "your-unique-bucket-name"
    
      require "google/cloud/storage"
    
      storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage-control-v2/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
      bucket  = storage.bucket bucket_name
    
      puts "ID:                       #{bucket.id}"
      puts "Name:                     #{bucket.name}"
      puts "Storage Class:            #{bucket.storage_class}"
      puts "Location:                 #{bucket.location}"
      puts "Location Type:            #{bucket.location_type}"
      puts "Cors:                     #{bucket.cors}"
      puts "Default Event Based Hold: #{bucket.[default_event_based_hold?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html)}"
      puts "Default KMS Key Name:     #{bucket.[default_kms_key](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html)}"
      puts "Logging Bucket:           #{bucket.[logging_bucket](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html)}"
      puts "Logging Prefix:           #{bucket.[logging_prefix](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html)}"
      puts "Metageneration:           #{bucket.metageneration}"
      puts "Retention Effective Time: #{bucket.[retention_effective_at](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html)}"
      puts "Retention Period:         #{bucket.[retention_period](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html)}"
      puts "Retention Policy Locked:  #{bucket.[retention_policy_locked?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html)}"
      puts "Requester Pays:           #{bucket.[requester_pays](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html)}"
      puts "Self Link:                #{bucket.api_url}"
      puts "Time Created:             #{bucket.created_at}"
      puts "Versioning Enabled:       #{bucket.[versioning?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html)}"
      puts "Index Page:               #{bucket.[website_main](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html)}"
      puts "Not Found Page:           #{bucket.[website_404](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html)}"
      puts "Labels:"
      bucket.labels.[each](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Policy-Bindings.html) do |key, value|
        puts " - #{key} = #{value}"
      end
      puts "Lifecycle Rules:"
      bucket.lifecycle.[each](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Policy-Bindings.html) do |rule|
        puts "#{rule.[action](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket-Lifecycle-Rule.html)} - #{rule.storage_class} - #{rule.[age](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket-Lifecycle-Rule.html)} - #{rule.[matches_storage_class](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket-Lifecycle-Rule.html)}"
      end
    end

### Rust
    
    
    use google_cloud_storage::client::StorageControl;
    
    pub async fn sample(client: &StorageControl, bucket_id: &str) -> anyhow::Result<()> {
        let bucket = client
            .get_bucket()
            .set_name(format!("projects/_/buckets/{bucket_id}"))
            .send()
            .await?;
        println!(
            "Encryption config for bucket {bucket_id}: {:?}",
            bucket.encryption
        );
        Ok(())
    }

### REST APIs

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](https://curl.haxx.se/) to call the JSON API with a [`GET` Bucket](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/get) request that includes the desired `fields`:
         
         curl -X GET -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME?fields=encryption"

Where `BUCKET_NAME` is the name of the bucket whose key you want to view. For example, `my-bucket`.

The response looks like the following example:
         
         {
           "encryption" : {
              "defaultKmsKeyName": "KEY_RESOURCE"
            },
         }




### XML API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](https://curl.haxx.se/) to call the XML API with a [`GET` Bucket](https://docs.cloud.google.com/storage/docs/xml-api/get-bucket) request that includes the `encryption` query parameter:
         
         curl -X GET -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         "https://storage.googleapis.com/BUCKET_NAME?encryptionConfig"

Where `BUCKET_NAME` is the name of the bucket whose key you want to view. For example, `my-bucket`.

The response looks like the following example:
         
         <EncryptionConfiguration>
           <DefaultKmsKeyName>KEY_RESOURCE</DefaultKmsKeyName>
         </EncryptionConfiguration>




## Encrypt an object with a Cloud KMS key

You can encrypt an individual object with a Cloud KMS key. This is useful if you want to use a different key from the default key set on the bucket, or if you don't have a default key set on the bucket. The name of the key resource used to encrypt the object is stored in the object's metadata.

### Console

The Google Cloud console cannot be used to specify Cloud KMS keys on a per-object basis. Use the gcloud CLI or the client libraries instead.

### Command line

Use the [`gcloud storage cp`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/cp) command with the `--encryption-key` flag:
    
    
    gcloud storage cp SOURCE_DATA gs://BUCKET_NAME/OBJECT_NAME --encryption-key=KEY_RESOURCE

Where:

  * `SOURCE_DATA` is the source location of the data you're encrypting. This can be any source location supported by the `cp` command. For example `gs://my-bucket/pets/old-dog.png`.
  * `BUCKET_NAME` is the name of the destination bucket for this copy command. For example, `my-bucket`.
  * `OBJECT_NAME` is the name of the final, encrypted object. For example, `pets/new-dog.png`.
  * `KEY_RESOURCE` is the [Cloud KMS key resource](https://docs.cloud.google.com/kms/docs/resource-hierarchy#retrieve_resource_id) you want to use for encrypting the object.



### Client libraries

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    namespace gcs = ::google::cloud::storage;
    using ::google::cloud::StatusOr;
    [](gcs::Client client, std::string const& bucket_name,
       std::string const& object_name, std::string const& kms_key_name) {
      gcs::ObjectWriteStream stream = client.WriteObject(
          bucket_name, object_name, gcs::KmsKeyName(kms_key_name));
    
      // Line numbers start at 1.
      for (int lineno = 1; lineno <= 10; ++lineno) {
        stream << lineno << ": placeholder text for CMEK example.\n";
      }
    
      stream.Close();
    
      StatusOr<gcs::ObjectMetadata> metadata = std::move(stream).metadata();
      if (!metadata) throw std::move(metadata).status();
    
      std::cout << "Successfully wrote to object " << metadata->name()
                << " its size is: " << metadata->size()
                << "\nFull metadata: " << *metadata << "\n";
    }

### C#

For more information, see the [Cloud Storage C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    using [Google.Cloud.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html);
    using System;
    using System.IO;
    
    public class UploadFileWithKmsKeySample
    {
        public void UploadFileWithKmsKey(
            string projectId = "your-project-id",
            string bucketName = "your-unique-bucket-name",
            string keyLocation = "us-west1",
            string kmsKeyRing = "kms-key-ring",
            string kmsKeyName = "key-name",
            string localPath = "my-local-path/my-file-name",
            string objectName = "my-file-name")
        {
            // KMS Key identifier of an already created KMS key.
            // If you use the Google.Cloud.Kms.V1 library, you can construct these names using helper class CryptoKeyName.
            // var fullKeyName = new CryptoKeyName(projectId, keyLocation, kmsKeyRing, kmsKeyName).ToString();
            string keyPrefix = $"projects/{projectId}/locations/{keyLocation}";
            string fullKeyringName = $"{keyPrefix}/keyRings/{kmsKeyRing}";
            string fullKeyName = $"{fullKeyringName}/cryptoKeys/{kmsKeyName}";
    
            var storage = [StorageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html#Google_Cloud_Storage_V1_StorageClient_Create)();
            using var fileStream = File.OpenRead(localPath);
            storage.UploadObject(bucketName, objectName, null, fileStream, new [UploadObjectOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.UploadObjectOptions.html) { KmsKeyName = fullKeyName });
            Console.WriteLine($"Uploaded {objectName}.");
        }
    }

### Go

For more information, see the [Cloud Storage Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/storage). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"time"
    
    	"cloud.google.com/go/storage"
    )
    
    // uploadWithKMSKey writes an object using Cloud KMS encryption.
    func uploadWithKMSKey(w io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), bucket, object, keyName string) error {
    	// bucket := "bucket-name"
    	// object := "object-name"
    	// keyName := "projects/projectId/locations/global/keyRings/keyRingID/cryptoKeys/cryptoKeyID"
    	ctx := context.Background()
    	client, err := storage.NewClient(ctx)
    	if err != nil {
    		return fmt.Errorf("storage.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	ctx, cancel := context.WithTimeout(ctx, time.Second*50)
    	defer cancel()
    
    	o := client.[Bucket](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Bucket)(bucket).[Object](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketHandle_Object)(object)
    
    	// Optional: set a generation-match precondition to avoid potential race
    	// conditions and data corruptions. The request to upload is aborted if the
    	// object's generation number does not match your precondition.
    	// For an object that does not yet exist, set the DoesNotExist precondition.
    	o = o.If(storage.[Conditions](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Conditions){DoesNotExist: true})
    	// If the live object already exists in your bucket, set instead a
    	// generation-match precondition using the live object's generation number.
    	// attrs, err := o.Attrs(ctx)
    	// if err != nil {
    	// 	return fmt.Errorf("object.Attrs: %w", err)
    	// }
    	// o = o.If(storage.Conditions{GenerationMatch: attrs.Generation})
    
    	// Encrypt the object's contents.
    	wc := o.[NewWriter](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_ObjectHandle_NewWriter)(ctx)
    	wc.KMSKeyName = keyName
    	if _, err := wc.[Write](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer_Write)([]byte("top secret")); err != nil {
    		return fmt.Errorf("Writer.Write: %w", err)
    	}
    	if err := wc.Close(); err != nil {
    		return fmt.Errorf("Writer.Close: %w", err)
    	}
    	fmt.Fprintf(w, "Uploaded blob %v with KMS key.\n", object)
    	return nil
    }
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import static java.nio.charset.StandardCharsets.UTF_8;
    
    import com.google.cloud.storage.[BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html);
    import com.google.cloud.storage.[BlobInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    
    public class UploadKmsEncryptedObject {
      public static void uploadKmsEncryptedObject(
          String projectId, String bucketName, String objectName, String kmsKeyName) {
        // The ID of your GCP project
        // String projectId = "your-project-id";
    
        // The ID of your GCS bucket
        // String bucketName = "your-unique-bucket-name";
    
        // The ID of your GCS object
        // String objectName = "your-object-name";
    
        // The name of the KMS key to encrypt with
        // String kmsKeyName = "projects/my-project/locations/us/keyRings/my_key_ring/cryptoKeys/my_key"
    
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder().setProjectId(projectId).build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)();
        byte[] data = "Hello, World!".getBytes(UTF_8);
    
        [BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html) blobId = [BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html).of(bucketName, objectName);
        [BlobInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html) blobInfo = [BlobInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html).newBuilder(blobId).setContentType("text/plain").build();
    
        // Optional: set a generation-match precondition to avoid potential race
        // conditions and data corruptions. The request returns a 412 error if the
        // preconditions are not met.
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html).BlobTargetOption precondition;
        if (storage.[get](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_get_com_google_cloud_storage_BlobId_)(bucketName, objectName) == null) {
          // For a target object that does not yet exist, set the DoesNotExist precondition.
          // This will cause the request to fail if the object is created before the request runs.
          precondition = [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html).BlobTargetOption.doesNotExist();
        } else {
          // If the destination already exists in your bucket, instead set a generation-match
          // precondition. This will cause the request to fail if the existing object's generation
          // changes before the request runs.
          precondition =
              [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html).BlobTargetOption.generationMatch(
                  storage.[get](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_get_com_google_cloud_storage_BlobId_)(bucketName, objectName).getGeneration());
        }
    
        storage.[create](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_create_com_google_cloud_storage_BlobInfo_byte___com_google_cloud_storage_Storage_BlobTargetOption____)(blobInfo, data, Storage.BlobTargetOption.kmsKeyName(kmsKeyName), precondition);
    
        System.out.println(
            "Uploaded object "
                + objectName
                + " in bucket "
                + bucketName
                + " encrypted with "
                + kmsKeyName);
      }
    }

### Node.js

For more information, see the [Cloud Storage Node.js API reference documentation](https://cloud.google.com/nodejs/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // The ID of your GCS bucket
    // const bucketName = 'your-unique-bucket-name';
    
    // The path to your file to upload
    // const filePath = 'path/to/your/file';
    
    // The name of the KMS-key
    // const kmsKeyName = 'my-key';
    
    // Imports the Google Cloud client library
    const {Storage} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    
    // Creates a client
    const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)();
    
    async function uploadFileWithKmsKey() {
      const options = {
        kmsKeyName,
        // Optional:
        // Set a generation-match precondition to avoid potential race conditions
        // and data corruptions. The request to upload is aborted if the object's
        // generation number does not match your precondition. For a destination
        // object that does not yet exist, set the ifGenerationMatch precondition to 0
        // If the destination object already exists in your bucket, set instead a
        // generation-match precondition using its generation number.
        preconditionOpts: {ifGenerationMatch: generationMatchPrecondition},
      };
    
      await storage.bucket(bucketName).[upload](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/bucket.html)(filePath, options);
    
      console.log(`${filePath} uploaded to ${bucketName} using ${kmsKeyName}.`);
    }
    
    uploadFileWithKmsKey().catch(console.error);

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Storage\StorageClient;
    
    /**
     * Upload a file using KMS encryption.
     *
     * @param string $bucketName The name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     * @param string $objectName The name of your Cloud Storage object.
     *        (e.g. 'my-object')
     * @param string $source The path to the file to upload.
     *        (e.g. '/path/to/your/file')
     * @param string $kmsKeyName The KMS key used to encrypt objects server side.
     *     Key names are provided in the following format:
     *     `projects/<PROJECT>/locations/<LOCATION>/keyRings/<RING_NAME>/cryptoKeys/<KEY_NAME>`.
     */
    function upload_with_kms_key(string $bucketName, string $objectName, string $source, string $kmsKeyName): void
    {
        $storage = new StorageClient();
        if (!$file = fopen($source, 'r')) {
            throw new \InvalidArgumentException('Unable to open file for reading');
        }
        $bucket = $storage->bucket($bucketName);
        $object = $bucket->upload($file, [
            'name' => $objectName,
            'destinationKmsKeyName' => $kmsKeyName,
        ]);
        printf('Uploaded %s to gs://%s/%s using encryption key %s' . PHP_EOL,
            basename($source),
            $bucketName,
            $objectName,
            $kmsKeyName);
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
    
    def upload_blob_with_kms(
        bucket_name, source_file_name, destination_blob_name, kms_key_name,
    ):
        """Uploads a file to the bucket, encrypting it with the given KMS key."""
        # bucket_name = "your-bucket-name"
        # source_file_name = "local/path/to/file"
        # destination_blob_name = "storage-object-name"
        # kms_key_name = "projects/PROJ/locations/LOC/keyRings/RING/cryptoKey/KEY"
    
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
        bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(bucket_name)
        blob = bucket.blob(destination_blob_name, kms_key_name=kms_key_name)
    
        # Optional: set a generation-match precondition to avoid potential race conditions
        # and data corruptions. The request to upload is aborted if the object's
        # generation number does not match your precondition. For a destination
        # object that does not yet exist, set the if_generation_match precondition to 0.
        # If the destination object already exists in your bucket, set instead a
        # generation-match precondition using its generation number.
        generation_match_precondition = 0
    
        blob.[upload_from_filename](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_filename)(source_file_name, if_generation_match=generation_match_precondition)
    
        print(
            "File {} uploaded to {} with encryption key {}.".format(
                source_file_name, destination_blob_name, kms_key_name
            )
        )
    
    

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    def upload_with_kms_key bucket_name:, local_file_path:, file_name: nil, kms_key:
      # The ID of your GCS bucket
      # bucket_name = "your-unique-bucket-name"
    
      # The path to your file to upload
      # local_file_path = "/local/path/to/file.txt"
    
      # The ID of your GCS object
      # file_name = "your-file-name"
    
      # The name of the KMS key to manage this object with
      # kms_key = "projects/your-project-id/locations/global/keyRings/your-key-ring/cryptoKeys/your-key"
    
      require "google/cloud/storage"
    
      storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage-control-v2/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
    
      bucket = storage.bucket bucket_name, skip_lookup: true
    
      file = bucket.[create_file](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html) local_file_path, file_name, kms_key: kms_key
    
      puts "Uploaded #{file.name} and encrypted service side using #{file.kms_key}"
    end

### Rust
    
    
    use google_cloud_storage::client::Storage;
    
    pub async fn sample(
        client: &Storage,
        bucket_id: &str,
        file_path: &str,
        kms_key: &str,
    ) -> Result<(), anyhow::Error> {
        const NAME: &str = "object-to-upload.txt";
        let payload = tokio::fs::File::open(file_path).await?;
        let _result = client
            .write_object(format!("projects/_/buckets/{bucket_id}"), NAME, payload)
            .set_kms_key(kms_key)
            .send_unbuffered()
            .await?;
    
        println!("Uploaded {NAME} to bucket {bucket_id} with KMS key {kms_key}.");
        Ok(())
    }

### REST APIs

### JSON API

**Note:** These steps apply specifically to inserting objects using the JSON API. You can follow a similar procedure to compose or rewrite objects with the JSON API.

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Add the object's data to the request body.

  3. Use [`cURL`](https://curl.haxx.se/) to call the JSON API with a [`POST` Object](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/insert) request:
         
         curl -X POST --data-binary @OBJECT \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: OBJECT_CONTENT_TYPE" \
         "https://storage.googleapis.com/upload/storage/v1/b/BUCKET_NAME/o?uploadType=media&name=OBJECT_NAME&kmsKeyName=KEY_RESOURCE"

Where:

     * `OBJECT` is the path to the object you are uploading. For example, `Desktop/dog.png`.
     * `OBJECT_CONTENT_TYPE` is the [content type](https://docs.cloud.google.com/storage/docs/metadata#content-type) of the object. For example, `image/png`.
     * `BUCKET_NAME` is the name of the bucket to which you are uploading your object. For example,`my-bucket`.
     * `OBJECT_NAME` is the URL-encoded name of the object you are uploading. For example, `pets/dog.png`, URL-encoded as `pets%2Fdog.png`.
     * `KEY_RESOURCE` is the [Cloud KMS key resource](https://docs.cloud.google.com/kms/docs/resource-hierarchy#retrieve_resource_id).



### XML API

**Note:** These steps apply specifically to uploading objects using the XML API. You can follow a similar procedure to compose or copy objects with the XML API.

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Add the object's data to the request body.

  3. Use [`cURL`](https://curl.haxx.se/) to call the XML API with a [`PUT` Object](https://docs.cloud.google.com/storage/docs/xml-api/put-object-upload) request:
         
         curl -X PUT --data-binary @OBJECT \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: OBJECT_CONTENT_TYPE" \
         -H "x-goog-encryption-kms-key-name: KEY_RESOURCE" \
         "https://storage.googleapis.com/BUCKET_NAME/OBJECT_NAME"

Where:

     * `OBJECT` is the path to the object you are uploading. For example, `Desktop/dog.png`.
     * `OBJECT_CONTENT_TYPE` is the [content type](https://docs.cloud.google.com/storage/docs/metadata#content-type) of the object. For example, `image/png`.
     * `BUCKET_NAME` is the name of the bucket to which you are uploading your object. For example,`my-bucket`.
     * `OBJECT_NAME` is the URL-encoded name of the object you are uploading. For example, `pets/dog.png`, URL-encoded as `pets%2Fdog.png`.
     * `KEY_RESOURCE` is your [Cloud KMS key resource](https://docs.cloud.google.com/kms/docs/resource-hierarchy#retrieve_resource_id).



## Rotate from a customer-supplied key to a Cloud KMS key

If your objects are encrypted with [customer-supplied encryption keys](https://docs.cloud.google.com/storage/docs/encryption/customer-supplied-keys), you can rotate them to use Cloud KMS keys by rewriting the object.

**Note:** Rotating from customer-supplied encryption keys to Cloud KMS keys involves rewriting data, which might incur [early deletion](https://docs.cloud.google.com/storage/pricing#early-delete) charges, depending on the age and storage class of the data.

### Console

The Google Cloud console cannot be used to change encryption keys on a per-object basis. Use the gcloud CLI or the client libraries instead.

### Command line

Use the [`gcloud storage objects update`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/objects/update) command with the appropriate flags:
    
    
    gcloud storage objects update gs://BUCKET_NAME/OBJECT_NAME --encryption-key=KMS_KEY --decryption-keys=CSEK_KEY

Where:

  * `BUCKET_NAME` is the name of the bucket that contains the object whose key you are rotating. For example, `my-bucket`.
  * `OBJECT_NAME` is the name of the object whose key you are rotating. For example, `pets/dog.png`.
  * `KMS_KEY` is the [Cloud KMS key resource](https://docs.cloud.google.com/kms/docs/resource-hierarchy#retrieve_resource_id) you want to use for encrypting the object.
  * `CSEK_KEY` is the current customer-supplied encryption key used on the object.



### Client libraries

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    namespace gcs = ::google::cloud::storage;
    using ::google::cloud::StatusOr;
    [](gcs::Client client, std::string const& bucket_name,
       std::string const& object_name, std::string const& old_csek_key_base64,
       std::string const& new_cmek_key_name) {
      StatusOr<gcs::ObjectMetadata> metadata = client.RewriteObjectBlocking(
          bucket_name, object_name, bucket_name, object_name,
          gcs::SourceEncryptionKey::FromBase64Key(old_csek_key_base64),
          gcs::DestinationKmsKeyName(new_cmek_key_name));
      if (!metadata) throw std::move(metadata).status();
    
      std::cout << "Changed object " << metadata->name() << " in bucket "
                << metadata->bucket()
                << " from using CSEK to CMEK key.\nFull Metadata: " << *metadata
                << "\n";
    }

### C#

For more information, see the [Cloud Storage C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    using [Google.Cloud.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html);
    using System;
    using System.IO;
    
    public class ObjectCsekToCmekSample
    {
        public void ObjectCsekToCmek(
            string projectId = "your-project-id",
            string bucketName = "your-unique-bucket-name",
            string objectName = "your-object-name",
            string currrentEncryptionKey = "TIbv/fjexq+VmtXzAlc63J4z5kFmWJ6NdAPQulQBT7g=",
            string keyLocation = "us-west1",
            string kmsKeyRing = "kms-key-ring",
            string kmsKeyName = "key-name")
        {
            string keyPrefix = $"projects/{projectId}/locations/{keyLocation}";
            string fullKeyringName = $"{keyPrefix}/keyRings/{kmsKeyRing}";
            string fullKeyName = $"{fullKeyringName}/cryptoKeys/{kmsKeyName}";
            var storage = [StorageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html#Google_Cloud_Storage_V1_StorageClient_Create)();
    
            using var outputStream = new MemoryStream();
            storage.DownloadObject(bucketName, objectName, outputStream, new [DownloadObjectOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.DownloadObjectOptions.html)()
            {
                EncryptionKey = [EncryptionKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.EncryptionKey.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.EncryptionKey.html#Google_Cloud_Storage_V1_EncryptionKey_Create_System_Byte___)(Convert.FromBase64String(currrentEncryptionKey))
            });
    
            outputStream.Position = 0;
    
            storage.UploadObject(bucketName, objectName, null, outputStream, new [UploadObjectOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.UploadObjectOptions.html)()
            {
                KmsKeyName = fullKeyName
            });
    
            Console.WriteLine($"Object {objectName} in bucket {bucketName} is now managed" +
                $" by the KMS key ${kmsKeyName}  instead of a customer-supplied encryption key");
        }
    }

### Go

For more information, see the [Cloud Storage Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/storage). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"time"
    
    	"cloud.google.com/go/storage"
    )
    
    // сhangeObjectCSEKtoKMS changes the key used to encrypt an object from
    // a customer-supplied encryption key to a customer-managed encryption key.
    func сhangeObjectCSEKToKMS(w io.Wr[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer)bucket, object string, encryptionKey []byte, kmsKeyName string) error {
    	// bucket := "bucket-name"
    	// object := "object-name"
    
    	// encryptionKey is the Base64 encoded decryption key, which should be the same
    	// key originally used to encrypt the object.
    	// encryptionKey := []byte("TIbv/fjexq+VmtXzAlc63J4z5kFmWJ6NdAPQulQBT7g=")
    
    	// kmsKeyName is the name of the KMS key to manage this object with.
    	// kmsKeyName := "projects/projectId/locations/global/keyRings/keyRingID/cryptoKeys/cryptoKeyID"
    	ctx := context.Background()
    	client, err := storage.NewClient(ctx)
    	if err != nil {
    		return fmt.Errorf("storage.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	ctx, cancel := context.WithTimeout(ctx, time.Second*10)
    	defer cancel()
    
    	o := clclient.[Bucket](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Bucket)(bucket).[Object](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketHandle_Object)bject)
    
    	// Optional: set a generation-match precondition to avoid potential race
    	// conditions and data corruptions. The request to copy is aborted if the
    	// object's generation number does not match your precondition.
    	attrs, err := o.Attrs(ctx)
    	if err != nil {
    		return fmt.Errorf("object.Attrs: %w", err)
    	}
    	o = o.If(storage.Co[Conditions](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Conditions)enerationMatch: atattrs.[Generation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_ObjectHandle_Generation)
    
    	// You can't change an object's encryption key directly. Instead, you must
    	// rewrite the object using the new key.
    	src := o.o.[Key](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_ObjectHandle_Key)ncryptionKey)
    	c := o.o.[CopierFrom](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_ObjectHandle_CopierFrom)rc)
    	c.DestinationKMSKeyName = kmsKeyName
    	if _, err := c.Run(ctx); err != nil {
    		return fmt.Errorf("Copier.Run: %w", err)
    	}
    	fmt.Fprintf(w, "Object %v in bucket %v is now managed by the KMS key %v instead of a customer-supplied encryption key\n", object, bucket, kmsKeyName)
    	return nil
    }
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import com.google.cloud.storage.[Blob](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.html);
    import com.google.cloud.storage.[BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    
    public class ChangeObjectCsekToKms {
      public static void changeObjectFromCsekToKms(
          String projectId,
          String bucketName,
          String objectName,
          String decryptionKey,
          String kmsKeyName) {
        // The ID of your GCP project
        // String projectId = "your-project-id";
    
        // The ID of your GCS bucket
        // String bucketName = "your-unique-bucket-name";
    
        // The ID of your GCS object
        // String objectName = "your-object-name";
    
        // The Base64 encoded decryption key, which should be the same key originally used to encrypt
        // the object
        // String decryptionKey = "TIbv/fjexq+VmtXzAlc63J4z5kFmWJ6NdAPQulQBT7g=";
    
        // The name of the KMS key to manage this object with
        // String kmsKeyName =
        // "projects/your-project-id/locations/global/keyRings/your-key-ring/cryptoKeys/your-key";
    
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder().setProjectId(projectId).build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)();
        [BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html) blobId = [BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html).of(bucketName, objectName);
        [Blob](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.html) blob = storage.[get](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_get_com_google_cloud_storage_BlobId_)(blobId);
        if (blob == null) {
          System.out.println("The object " + objectName + " wasn't found in " + bucketName);
          return;
        }
    
        // Optional: set a generation-match precondition to avoid potential race
        // conditions and data corruptions. The request to upload returns a 412 error if
        // the object's generation number does not match your precondition.
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html).BlobSourceOption precondition =
            [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html).BlobSourceOption.generationMatch(blob.getGeneration());
    
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html).[CopyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.CopyRequest.html) request =
            [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html).CopyRequest.newBuilder()
                .setSource(blobId)
                .setSourceOptions([Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html).BlobSourceOption.decryptionKey(decryptionKey), precondition)
                .setTarget(blobId, [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html).BlobTargetOption.kmsKeyName(kmsKeyName))
                .build();
        storage.[copy](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_copy_com_google_cloud_storage_Storage_CopyRequest_)(request);
    
        System.out.println(
            "Object "
                + objectName
                + " in bucket "
                + bucketName
                + " is now managed by the KMS key "
                + kmsKeyName
                + " instead of a customer-supplied encryption key");
      }
    }

### Node.js

For more information, see the [Cloud Storage Node.js API reference documentation](https://cloud.google.com/nodejs/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // The ID of your GCS bucket
    // const bucketName = 'your-unique-bucket-name';
    
    // The ID of your GCS file
    // const fileName = 'your-file-name';
    
    // The Base64 encoded decryption key, which should be the same key originally
    // used to encrypt the file
    // const encryptionKey = 'TIbv/fjexq+VmtXzAlc63J4z5kFmWJ6NdAPQulQBT7g=';
    
    // The name of the KMS key to manage this file with
    // const kmsKeyName = 'projects/your-project-id/locations/global/keyRings/your-key-ring/cryptoKeys/your-key';
    
    // Imports the Google Cloud client library
    const {Storage} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    
    // Creates a client
    const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)();
    
    async function changeFileCSEKToCMEK() {
      const rotateEncryptionKeyOptions = {
        kmsKeyName,
        // Optional: set a generation-match precondition to avoid potential race
        // conditions and data corruptions. The request to copy is aborted if the
        // object's generation number does not match your precondition.
        preconditionOpts: {
          ifGenerationMatch: generationMatchPrecondition,
        },
      };
    
      console.log(rotateEncryptionKeyOptions);
    
      await storage
        .bucket(bucketName)
        .file(fileName, {
          encryptionKey: Buffer.from(encryptionKey, '[base64](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/policydocument.html)'),
        })
        .[rotateEncryptionKey](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/file_2.html)({
          rotateEncryptionKeyOptions,
        });
    
      console.log(
        `file ${fileName} in bucket ${bucketName} is now managed by KMS key ${kmsKeyName} instead of customer-supplied encryption key`
      );
    }
    
    changeFileCSEKToCMEK().catch(console.error);

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Storage\StorageClient;
    
    /**
     * Migrate an object from a Customer-Specified Encryption Key to a Customer-Managed
     * Encryption Key.
     *
     * @param string $bucketName The name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     * @param string $objectName The name of your Cloud Storage object.
     *        (e.g. 'my-object')
     * @param string $decryptionKey The Base64 encoded decryption key, which should
     *        (e.g. 'TIbv/fjexq+VmtXzAlc63J4z5kFmWJ6NdAPQulQBT7g=')
     *     be the same key originally used to encrypt the object.
     * @param string $kmsKeyName The name of the KMS key to manage this object.
     *     Key names are provided in the following format:
     *     `projects/<PROJECT>/locations/<LOCATION>/keyRings/<RING_NAME>/cryptoKeys/<KEY_NAME>`.
     */
    function object_csek_to_cmek(string $bucketName, string $objectName, string $decryptionKey, string $kmsKeyName): void
    {
        $storage = new StorageClient();
        $bucket = $storage->bucket($bucketName);
    
        $object = $bucket->object($objectName, [
            'encryptionKey' => $decryptionKey,
        ]);
    
        $object->rewrite($bucketName, [
            'destinationKmsKeyName' => $kmsKeyName,
        ]);
    
        printf(
            'Object %s in bucket %s is now managed by the KMS key %s instead of a customer-supplied encryption key',
            $objectName,
            $bucketName,
            $kmsKeyName
        );
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
    
    def object_csek_to_cmek(bucket_name, blob_name, encryption_key, kms_key_name):
        """Change a blob's customer-supplied encryption key to KMS key"""
        # bucket_name = "your-bucket-name"
        # blob_name = "your-object-name"
        # encryption_key = "TIbv/fjexq+VmtXzAlc63J4z5kFmWJ6NdAPQulQBT7g="
        # kms_key_name = "projects/PROJ/locations/LOC/keyRings/RING/cryptoKey/KEY"
    
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
        bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(bucket_name)
    
        current_encryption_key = base64.b64decode(encryption_key)
        source_blob = bucket.blob(blob_name, encryption_key=current_encryption_key)
        destination_blob = bucket.blob(blob_name, kms_key_name=kms_key_name)
        generation_match_precondition = None
        token = None
    
        # Optional: set a generation-match precondition to avoid potential race conditions
        # and data corruptions. The request to rewrite is aborted if the object's
        # generation number does not match your precondition.
        source_blob.reload()  # Fetch blob metadata to use in generation_match_precondition.
        generation_match_precondition = source_blob.generation
    
        while True:
            token, bytes_rewritten, total_bytes = destination_blob.[rewrite](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_rewrite)(
                source_blob, token=token, if_generation_match=generation_match_precondition
            )
            if token is None:
                break
    
        print(
            "Blob {} in bucket {} is now managed by the KMS key {} instead of a customer-supplied encryption key".format(
                blob_name, bucket_name, kms_key_name
            )
        )
        return destination_blob
    
    

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    def object_csek_to_cmek bucket_name:, file_name:, encryption_key:, kms_key_name:
      # The ID of your GCS bucket
      # bucket_name = "your-unique-bucket-name"
    
      # The ID of your GCS object
      # file_name = "your-file-name"
    
      # The Base64 encoded encryption key, which should be the same key originally used to encrypt the object
      # encryption_key = "TIbv/fjexq+VmtXzAlc63J4z5kFmWJ6NdAPQulQBT7g="
    
      # The name of the KMS key to manage this object with
      # kms_key_name = "projects/your-project-id/locations/global/keyRings/your-key-ring/cryptoKeys/your-key"
    
      require "google/cloud/storage"
    
      storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage-control-v2/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
      bucket = storage.bucket bucket_name, skip_lookup: true
    
      file = bucket.[file](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html) file_name, encryption_key: encryption_key
    
      file.[rotate](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-File.html) encryption_key: encryption_key, new_kms_key: kms_key_name
    
      puts "File #{file_name} in bucket #{bucket_name} is now managed by the KMS key #{kms_key_name} instead of a " \
           "customer-supplied encryption key"
    end

### Rust
    
    
    use google_cloud_storage::builder_ext::RewriteObjectExt;
    use google_cloud_storage::client::StorageControl;
    use google_cloud_storage::model::CommonObjectRequestParams;
    use google_cloud_storage::model_ext::KeyAes256;
    
    pub async fn sample(
        client: &StorageControl,
        bucket_id: &str,
        object_id: &str,
        csek_key: KeyAes256,
        kms_key: &str,
    ) -> anyhow::Result<()> {
        let csek: CommonObjectRequestParams = csek_key.into();
        let updated = client
            .rewrite_object()
            .set_source_bucket(format!("projects/_/buckets/{bucket_id}"))
            .set_source_object(object_id)
            .set_copy_source_encryption_algorithm(csek.encryption_algorithm)
            .set_copy_source_encryption_key_bytes(csek.encryption_key_bytes)
            .set_copy_source_encryption_key_sha256_bytes(csek.encryption_key_sha256_bytes)
            .set_destination_bucket(format!("projects/_/buckets/{bucket_id}"))
            .set_destination_name(object_id)
            .set_destination_kms_key(kms_key.to_string())
            .rewrite_until_done()
            .await?;
    
        println!(
            "successfully rotated encryption key for object {object_id} in bucket {bucket_id} from CSEK to CMEK: {updated:?}"
        );
        Ok(())
    }

### REST APIs

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](https://curl.haxx.se/) to call the JSON API with a [`POST` Object](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/rewrite) request:
         
         curl -X POST \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "Content-Length: 0" \
           -H "x-goog-copy-source-encryption-algorithm: AES256" \
           -H "x-goog-copy-source-encryption-key: OLD_ENCRYPTION_KEY" \
           -H "x-goog-copy-source-encryption-key-sha256: HASH_OF_OLD_KEY" \
           "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME/o/OBJECT_NAME/rewriteTo/b/BUCKET_NAME/o/OBJECT_NAME?kmsKeyName=KEY_RESOURCE"

Where:

     * `OLD_ENCRYPTION_KEY` is the current AES-256 key used to encrypt your object.
     * `HASH_OF_OLD_KEY` is the current SHA-256 hash for your AES-256 key.
     * `BUCKET_NAME` is the name of the bucket containing the relevant object. For example, `my-bucket`.
     * `OBJECT_NAME` is the URL-encoded name of the object whose keys you are rotating. For example, `pets/dog.png`, URL-encoded as `pets%2Fdog.png`.
     * `KEY_RESOURCE` is the [Cloud KMS key resource](https://docs.cloud.google.com/kms/docs/resource-hierarchy#retrieve_resource_id).



### XML API

The XML API does not support rotating from a customer-supplied encryption key to a Cloud KMS key through rewriting object. To perform such a rotation using the XML API, you should:

  1. [Download the existing object](https://docs.cloud.google.com/storage/docs/encryption/using-customer-supplied-keys#download-decrypt).
  2. Re-upload the object using a Cloud KMS key.



## Identify the key used to encrypt an object

To find the Cloud KMS key that was used to encrypt an object:

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the bucket that contains the object.

The **Bucket details** page opens, with the **Objects** tab selected.

  3. Navigate to the object, which might be located in a folder.

  4. In the **Encryption** column, hold the pointer over the entry for the object.

The key name and version appear in the format:
         
         LOCATION/KEY_RING_NAME/KEY_NAME/KEY_VERSION




### Command line

Use the [`gcloud storage objects describe`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/objects/describe) command with the `--format` flag:
    
    
    gcloud storage objects describe gs://BUCKET_NAME/OBJECT_NAME --format="default(kms_key)"

Where:

  * `BUCKET_NAME` is the name of the bucket containing the encrypted object. For example, `my-bucket`.
  * `OBJECT_NAME` is the name of the encrypted object. For example, `pets/dog.png`.



If successful, the response looks like:
    
    
    kms_key: projects/my-pet-project/locations/LOCATION_NAME/keyRings/KEYRING_NAME/cryptoKeys/KEY_NAME/cryptoKeyVersions/VERSION_NUMBER

### Client libraries

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    namespace gcs = ::google::cloud::storage;
    using ::google::cloud::StatusOr;
    [](gcs::Client client, std::string const& bucket_name,
       std::string const& object_name) {
      StatusOr<gcs::ObjectMetadata> metadata =
          client.GetObjectMetadata(bucket_name, object_name);
      if (!metadata) throw std::move(metadata).status();
    
      std::cout << "KMS key on object " << metadata->name() << " in bucket "
                << metadata->bucket() << ": " << metadata->kms_key_name() << "\n";
    }

### C#

For more information, see the [Cloud Storage C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

To view the KMS key associated with an object, follow the instructions for displaying an object's metadata and look for the KMS key name field in the response. 
    
    
    using [Google.Cloud.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html);
    using System;
    
    public class GetMetadataSample
    {
        public Google.Apis.Storage.v1.Data.Object GetMetadata(
            string bucketName = "your-unique-bucket-name",
            string objectName = "your-object-name")
        {
            var storage = [StorageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html#Google_Cloud_Storage_V1_StorageClient_Create)();
            var storageObject = storage.GetObject(bucketName, objectName, new [GetObjectOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.GetObjectOptions.html) { Projection = [Projection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.Projection.html).[Full](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.Projection.html#Google_Cloud_Storage_V1_Projection_Full) });
            Console.WriteLine($"Bucket:\t{storageObject.Bucket}");
            Console.WriteLine($"CacheControl:\t{storageObject.[CacheControl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.UrlSigner.PostPolicyStandardElement.html#Google_Cloud_Storage_V1_UrlSigner_PostPolicyStandardElement_CacheControl)}");
            Console.WriteLine($"ComponentCount:\t{storageObject.ComponentCount}");
            Console.WriteLine($"ContentDisposition:\t{storageObject.[ContentDisposition](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.UrlSigner.PostPolicyStandardElement.html#Google_Cloud_Storage_V1_UrlSigner_PostPolicyStandardElement_ContentDisposition)}");
            Console.WriteLine($"ContentEncoding:\t{storageObject.[ContentEncoding](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.UrlSigner.PostPolicyStandardElement.html#Google_Cloud_Storage_V1_UrlSigner_PostPolicyStandardElement_ContentEncoding)}");
            Console.WriteLine($"ContentLanguage:\t{storageObject.ContentLanguage}");
            Console.WriteLine($"ContentType:\t{storageObject.[ContentType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.UrlSigner.PostPolicyStandardElement.html#Google_Cloud_Storage_V1_UrlSigner_PostPolicyStandardElement_ContentType)}");
            Console.WriteLine($"Crc32c:\t{storageObject.Crc32c}");
            Console.WriteLine($"ETag:\t{storageObject.ETag}");
            Console.WriteLine($"Generation:\t{storageObject.Generation}");
            Console.WriteLine($"Id:\t{storageObject.Id}");
            Console.WriteLine($"Kind:\t{storageObject.Kind}");
            Console.WriteLine($"KmsKeyName:\t{storageObject.KmsKeyName}");
            Console.WriteLine($"Md5Hash:\t{storageObject.Md5Hash}");
            Console.WriteLine($"MediaLink:\t{storageObject.MediaLink}");
            Console.WriteLine($"Metageneration:\t{storageObject.Metageneration}");
            Console.WriteLine($"Name:\t{storageObject.Name}");
            Console.WriteLine($"Retention:\t{storageObject.Retention}");
            Console.WriteLine($"Size:\t{storageObject.Size}");
            Console.WriteLine($"StorageClass:\t{storageObject.StorageClass}");
            Console.WriteLine($"TimeCreated:\t{storageObject.TimeCreated}");
            Console.WriteLine($"Updated:\t{storageObject.Updated}");
            bool eventBasedHold = storageObject.EventBasedHold ?? false;
            Console.WriteLine("Event-based hold enabled? {0}", eventBasedHold);
            bool temporaryHold = storageObject.TemporaryHold ?? false;
            Console.WriteLine("Temporary hold enabled? {0}", temporaryHold);
            Console.WriteLine($"RetentionExpirationTime\t{storageObject.RetentionExpirationTime}");
            if (storageObject.Metadata != null)
            {
                Console.WriteLine("Metadata: ");
                foreach (var metadata in storageObject.Metadata)
                {
                    Console.WriteLine($"{metadata.[Key](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.UrlSigner.PostPolicyStandardElement.html#Google_Cloud_Storage_V1_UrlSigner_PostPolicyStandardElement_Key)}:\t{metadata.Value}");
                }
            }
            Console.WriteLine($"CustomTime:\t{storageObject.CustomTime}");
            return storageObject;
        }
    }

### Go

For more information, see the [Cloud Storage Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/storage). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

To view the KMS key associated with an object, follow the instructions for displaying an object's metadata and look for the KMS key name field in the response. 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"time"
    
    	"cloud.google.com/go/storage"
    )
    
    // getMetadata prints all of the object attributes.
    func getMetadata(w io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), bucket, object string) (*storage.[ObjectAttrs](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_ObjectAttrs), error) {
    	// bucket := "bucket-name"
    	// object := "object-name"
    	ctx := context.Background()
    	client, err := storage.NewClient(ctx)
    	if err != nil {
    		return nil, fmt.Errorf("storage.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	ctx, cancel := context.WithTimeout(ctx, time.Second*10)
    	defer cancel()
    
    	o := client.[Bucket](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Bucket)(bucket).[Object](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketHandle_Object)(object)
    	attrs, err := o.Attrs(ctx)
    	if err != nil {
    		return nil, fmt.Errorf("Object(%q).Attrs: %w", object, err)
    	}
    	fmt.Fprintf(w, "Bucket: %v\n", attrs.[Bucket](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Bucket))
    	fmt.Fprintf(w, "CacheControl: %v\n", attrs.[CacheControl](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Reader_CacheControl))
    	fmt.Fprintf(w, "ContentDisposition: %v\n", attrs.ContentDisposition)
    	fmt.Fprintf(w, "ContentEncoding: %v\n", attrs.[ContentEncoding](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Reader_ContentEncoding))
    	fmt.Fprintf(w, "ContentLanguage: %v\n", attrs.ContentLanguage)
    	fmt.Fprintf(w, "ContentType: %v\n", attrs.[ContentType](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Reader_ContentType))
    	fmt.Fprintf(w, "Crc32c: %v\n", attrs.CRC32C)
    	fmt.Fprintf(w, "Generation: %v\n", attrs.[Generation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_ObjectHandle_Generation))
    	fmt.Fprintf(w, "KmsKeyName: %v\n", attrs.KMSKeyName)
    	fmt.Fprintf(w, "Md5Hash: %v\n", attrs.MD5)
    	fmt.Fprintf(w, "MediaLink: %v\n", attrs.MediaLink)
    	fmt.Fprintf(w, "Metageneration: %v\n", attrs.Metageneration)
    	fmt.Fprintf(w, "Name: %v\n", attrs.Name)
    	fmt.Fprintf(w, "Size: %v\n", attrs.[Size](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Reader_Size))
    	fmt.Fprintf(w, "StorageClass: %v\n", attrs.StorageClass)
    	fmt.Fprintf(w, "TimeCreated: %v\n", attrs.Created)
    	fmt.Fprintf(w, "Updated: %v\n", attrs.Updated)
    	fmt.Fprintf(w, "Event-based hold enabled? %t\n", attrs.EventBasedHold)
    	fmt.Fprintf(w, "Temporary hold enabled? %t\n", attrs.TemporaryHold)
    	fmt.Fprintf(w, "Retention expiration time %v\n", attrs.RetentionExpirationTime)
    	fmt.Fprintf(w, "Custom time %v\n", attrs.CustomTime)
    	fmt.Fprintf(w, "Retention: %+v\n", attrs.Retention)
    	fmt.Fprintf(w, "\n\nMetadata\n")
    	for key, value := range attrs.Metadata {
    		fmt.Fprintf(w, "\t%v = %v\n", key, value)
    	}
    	return attrs, nil
    }
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

To view the KMS key associated with an object, follow the instructions for displaying an object's metadata and look for the KMS key name field in the response. 
    
    
    import com.google.cloud.storage.[Blob](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageException](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageException.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    import java.util.Date;
    import java.util.Map;
    
    public class GetObjectMetadata {
      public static void getObjectMetadata(String projectId, String bucketName, String blobName)
          throws [StorageException](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageException.html) {
        // The ID of your GCP project
        // String projectId = "your-project-id";
    
        // The ID of your GCS bucket
        // String bucketName = "your-unique-bucket-name";
    
        // The ID of your GCS object
        // String objectName = "your-object-name";
    
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder().setProjectId(projectId).build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)();
    
        // Select all fields
        // Fields can be selected individually e.g. Storage.BlobField.CACHE_CONTROL
        [Blob](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.html) blob =
            storage.[get](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_get_com_google_cloud_storage_BlobId_)(bucketName, blobName, Storage.BlobGetOption.fields(Storage.BlobField.values()));
    
        // Print blob metadata
        System.out.println("Bucket: " + blob.getBucket());
        System.out.println("CacheControl: " + blob.getCacheControl());
        System.out.println("ComponentCount: " + blob.[getComponentCount](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html#com_google_cloud_storage_BlobInfo_getComponentCount__)());
        System.out.println("ContentDisposition: " + blob.getContentDisposition());
        System.out.println("ContentEncoding: " + blob.getContentEncoding());
        System.out.println("ContentLanguage: " + blob.getContentLanguage());
        System.out.println("ContentType: " + blob.getContentType());
        System.out.println("CustomTime: " + blob.getCustomTime());
        System.out.println("Crc32c: " + blob.[getCrc32c](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html#com_google_cloud_storage_BlobInfo_getCrc32c__)());
        System.out.println("Crc32cHexString: " + blob.[getCrc32cToHexString](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html#com_google_cloud_storage_BlobInfo_getCrc32cToHexString__)());
        System.out.println("ETag: " + blob.getEtag());
        System.out.println("Generation: " + blob.getGeneration());
        System.out.println("Id: " + blob.[getBlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html#com_google_cloud_storage_BlobInfo_getBlobId__)());
        System.out.println("KmsKeyName: " + blob.[getKmsKeyName](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html#com_google_cloud_storage_BlobInfo_getKmsKeyName__)());
        System.out.println("Md5Hash: " + blob.[getMd5](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html#com_google_cloud_storage_BlobInfo_getMd5__)());
        System.out.println("Md5HexString: " + blob.[getMd5ToHexString](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html#com_google_cloud_storage_BlobInfo_getMd5ToHexString__)());
        System.out.println("MediaLink: " + blob.[getMediaLink](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html#com_google_cloud_storage_BlobInfo_getMediaLink__)());
        System.out.println("Metageneration: " + blob.getMetageneration());
        System.out.println("Name: " + blob.getName());
        System.out.println("Size: " + blob.[getSize](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html#com_google_cloud_storage_BlobInfo_getSize__)());
        System.out.println("StorageClass: " + blob.getStorageClass());
        System.out.println("TimeCreated: " + new Date(blob.getCreateTime()));
        System.out.println("Last Metadata Update: " + new Date(blob.getUpdateTime()));
        System.out.println("Object Retention Policy: " + blob.[getRetention](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html#com_google_cloud_storage_BlobInfo_getRetention__)());
        Boolean temporaryHoldIsEnabled = (blob.getTemporaryHold() != null && blob.getTemporaryHold());
        System.out.println("temporaryHold: " + (temporaryHoldIsEnabled ? "enabled" : "disabled"));
        Boolean eventBasedHoldIsEnabled =
            (blob.getEventBasedHold() != null && blob.getEventBasedHold());
        System.out.println("eventBasedHold: " + (eventBasedHoldIsEnabled ? "enabled" : "disabled"));
        if (blob.[getRetentionExpirationTime](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html#com_google_cloud_storage_BlobInfo_getRetentionExpirationTime__)() != null) {
          System.out.println("retentionExpirationTime: " + new Date(blob.[getRetentionExpirationTime](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html#com_google_cloud_storage_BlobInfo_getRetentionExpirationTime__)()));
        }
        if (blob.getMetadata() != null) {
          System.out.println("\n\n\nUser metadata:");
          for (Map.Entry<String, String> userMetadata : blob.getMetadata().entrySet()) {
            System.out.println(userMetadata.getKey() + "=" + userMetadata.getValue());
          }
        }
      }
    }

### Node.js

For more information, see the [Cloud Storage Node.js API reference documentation](https://cloud.google.com/nodejs/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

To view the KMS key associated with an object, follow the instructions for displaying an object's metadata and look for the KMS key name field in the response. 
    
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // The ID of your GCS bucket
    // const bucketName = 'your-unique-bucket-name';
    
    // The ID of your GCS file
    // const fileName = 'your-file-name';
    
    // Imports the Google Cloud client library
    const {Storage} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    
    // Creates a client
    const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)();
    
    async function getMetadata() {
      // Gets the metadata for the file
      const [metadata] = await storage
        .bucket(bucketName)
        .file(fileName)
        .getMetadata();
    
      console.log(`Bucket: ${metadata.bucket}`);
      console.log(`CacheControl: ${metadata.cacheControl}`);
      console.log(`ComponentCount: ${metadata.componentCount}`);
      console.log(`ContentDisposition: ${metadata.contentDisposition}`);
      console.log(`ContentEncoding: ${metadata.contentEncoding}`);
      console.log(`ContentLanguage: ${metadata.contentLanguage}`);
      console.log(`ContentType: ${metadata.contentType}`);
      console.log(`CustomTime: ${metadata.customTime}`);
      console.log(`Crc32c: ${metadata.crc32c}`);
      console.log(`ETag: ${metadata.etag}`);
      console.log(`Generation: ${metadata.generation}`);
      console.log(`Id: ${metadata.id}`);
      console.log(`KmsKeyName: ${metadata.kmsKeyName}`);
      console.log(`Md5Hash: ${metadata.md5Hash}`);
      console.log(`MediaLink: ${metadata.[mediaLink](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/filemetadata.html)}`);
      console.log(`Metageneration: ${metadata.metageneration}`);
      console.log(`Name: ${metadata.name}`);
      console.log(`Size: ${metadata.size}`);
      console.log(`StorageClass: ${metadata.storageClass}`);
      console.log(`TimeCreated: ${new Date(metadata.timeCreated)}`);
      console.log(`Last Metadata Update: ${new Date(metadata.updated)}`);
      console.log(`TurboReplication: ${metadata.rpo}`);
      console.log(
        `temporaryHold: ${metadata.temporaryHold ? 'enabled' : 'disabled'}`
      );
      console.log(
        `eventBasedHold: ${metadata.eventBasedHold ? 'enabled' : 'disabled'}`
      );
      if (metadata.[retentionExpirationTime](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/filemetadata.html)) {
        console.log(
          `retentionExpirationTime: ${new Date(metadata.[retentionExpirationTime](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/filemetadata.html))}`
        );
      }
      if (metadata.metadata) {
        console.log('\n\n\nUser metadata:');
        for (const key in metadata.metadata) {
          console.log(`${key}=${metadata.metadata[key]}`);
        }
      }
    }
    
    getMetadata().catch(console.error);

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

To view the KMS key associated with an object, follow the instructions for displaying an object's metadata and look for the KMS key name field in the response. 
    
    
    use Google\Cloud\Storage\StorageClient;
    
    /**
     * List object metadata.
     *
     * @param string $bucketName The name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     * @param string $objectName The name of your Cloud Storage object.
     *        (e.g. 'my-object')
     */
    function object_metadata(string $bucketName, string $objectName): void
    {
        $storage = new StorageClient();
        $bucket = $storage->bucket($bucketName);
        $object = $bucket->object($objectName);
        $info = $object->info();
        if (isset($info['name'])) {
            printf('Blob: %s' . PHP_EOL, $info['name']);
        }
        if (isset($info['bucket'])) {
            printf('Bucket: %s' . PHP_EOL, $info['bucket']);
        }
        if (isset($info['storageClass'])) {
            printf('Storage class: %s' . PHP_EOL, $info['storageClass']);
        }
        if (isset($info['id'])) {
            printf('ID: %s' . PHP_EOL, $info['id']);
        }
        if (isset($info['size'])) {
            printf('Size: %s' . PHP_EOL, $info['size']);
        }
        if (isset($info['updated'])) {
            printf('Updated: %s' . PHP_EOL, $info['updated']);
        }
        if (isset($info['generation'])) {
            printf('Generation: %s' . PHP_EOL, $info['generation']);
        }
        if (isset($info['metageneration'])) {
            printf('Metageneration: %s' . PHP_EOL, $info['metageneration']);
        }
        if (isset($info['etag'])) {
            printf('Etag: %s' . PHP_EOL, $info['etag']);
        }
        if (isset($info['crc32c'])) {
            printf('Crc32c: %s' . PHP_EOL, $info['crc32c']);
        }
        if (isset($info['md5Hash'])) {
            printf('MD5 Hash: %s' . PHP_EOL, $info['md5Hash']);
        }
        if (isset($info['contentType'])) {
            printf('Content-type: %s' . PHP_EOL, $info['contentType']);
        }
        if (isset($info['temporaryHold'])) {
            printf('Temporary hold: %s' . PHP_EOL, ($info['temporaryHold'] ? 'enabled' : 'disabled'));
        }
        if (isset($info['eventBasedHold'])) {
            printf('Event-based hold: %s' . PHP_EOL, ($info['eventBasedHold'] ? 'enabled' : 'disabled'));
        }
        if (isset($info['retentionExpirationTime'])) {
            printf('Retention Expiration Time: %s' . PHP_EOL, $info['retentionExpirationTime']);
        }
        if (isset($info['retention'])) {
            printf('Retention mode: %s' . PHP_EOL, $info['retention']['mode']);
            printf('Retain until time is: %s' . PHP_EOL, $info['retention']['retainUntilTime']);
        }
        if (isset($info['customTime'])) {
            printf('Custom Time: %s' . PHP_EOL, $info['customTime']);
        }
        if (isset($info['metadata'])) {
            printf('Metadata: %s' . PHP_EOL, print_r($info['metadata'], true));
        }
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
    
    def object_get_kms_key(bucket_name, blob_name):
        """Retrieve the KMS key of a blob"""
        # bucket_name = "your-bucket-name"
        # blob_name = "your-object-name"
    
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
    
        bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(bucket_name)
        blob = bucket.[get_blob](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_get_blob)(blob_name)
    
        kms_key = blob.[kms_key_name](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_kms_key_name)
    
        print(f"The KMS key of a blob is {blob.[kms_key_name](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_kms_key_name)}")
        return kms_key
    
    

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

To view the KMS key associated with an object, follow the instructions for displaying an object's metadata and look for the KMS key name field in the response. 
    
    
    def get_metadata bucket_name:, file_name:
      # The ID of your GCS bucket
      # bucket_name = "your-unique-bucket-name"
    
      # The ID of your GCS object
      # file_name = "your-file-name"
    
      require "google/cloud/storage"
    
      storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage-control-v2/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
      bucket  = storage.bucket bucket_name
      file    = bucket.[file](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html) file_name
    
      puts "Name: #{file.name}"
      puts "Bucket: #{bucket.name}"
      puts "Storage class: #{bucket.storage_class}"
      puts "ID: #{file.id}"
      puts "Size: #{file.[size](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-File.html)} bytes"
      puts "Created: #{file.created_at}"
      puts "Updated: #{file.updated_at}"
      puts "Generation: #{file.generation}"
      puts "Metageneration: #{file.metageneration}"
      puts "Etag: #{file.etag}"
      puts "Owners: #{file.acl.owners.join ','}"
      puts "Crc32c: #{file.[crc32c](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-File.html)}"
      puts "md5_hash: #{file.[md5](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-File.html)}"
      puts "Cache-control: #{file.cache_control}"
      puts "Content-type: #{file.content_type}"
      puts "Contexts: #{file.[contexts](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-File.html)}"
      puts "Content-disposition: #{file.content_disposition}"
      puts "Content-encoding: #{file.content_encoding}"
      puts "Content-language: #{file.content_language}"
      puts "KmsKeyName: #{file.kms_key}"
      puts "Event-based hold enabled?: #{file.[event_based_hold?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-File.html)}"
      puts "Temporary hold enaled?: #{file.[temporary_hold?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-File.html)}"
      puts "Retention Expiration: #{file.[retention_expires_at](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-File.html)}"
      puts "Custom Time: #{file.custom_time}"
      puts "Metadata:"
      file.metadata.[each](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Policy-Bindings.html) do |key, value|
        puts " - #{key} = #{value}"
      end
    end

### Rust

To view the KMS key associated with an object, follow the instructions for displaying an object's metadata and look for the KMS key name field in the response. 
    
    
    use google_cloud_storage::client::StorageControl;
    
    pub async fn sample(client: &StorageControl, bucket_id: &str) -> anyhow::Result<()> {
        const NAME: &str = "object-to-read";
        let object = client
            .get_object()
            .set_bucket(format!("projects/_/buckets/{bucket_id}"))
            .set_object(NAME)
            .send()
            .await?;
        println!(
            "Object {NAME} in bucket {bucket_id} has KMS key: {}",
            object.kms_key
        );
        Ok(())
    }

### REST APIs

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](https://curl.haxx.se/) to call the JSON API with a [`GET` Object](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/get) request:
         
         curl -X GET \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME/o/OBJECT_NAME?fields=kmsKeyName"

Where:

     * `BUCKET_NAME` is the name of the bucket containing the encrypted object. For example, `my-bucket`.
     * `OBJECT_NAME` is the URL-encoded name of the encrypted object. For example, `pets/dog.png`, URL-encoded as `pets%2Fdog.png`.



### XML API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](https://curl.haxx.se/) to call the XML API with a [`GET` Object](https://docs.cloud.google.com/storage/docs/xml-api/get-object-encryption) request:
         
         curl -X GET \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         "https://storage.googleapis.com/BUCKET_NAME/OBJECT_NAME?encryption"

Where:

     * `BUCKET_NAME` is the name of the bucket containing the encrypted object. For example, `my-bucket`.
     * `OBJECT_NAME` is the URL-encoded name of the encrypted object. For example, `pets/dog.png`, URL-encoded as `pets%2Fdog.png`.



**Note:** If the object was written with an encryption method other than Cloud KMS, there is no information associated with this metadata field.

## Re-encrypt objects in bulk

To re-encrypt millions or billions of objects with a different key with a single job, use [Storage batch operations](https://docs.cloud.google.com/storage/docs/batch-operations/overview). To create a job, specify the objects you want to re-encrypt and the destination key, either by providing a list of objects in a manifest file or by using object prefixes. After you have specified the object list, [create a batch operation job to re-encrypt the objects](https://docs.cloud.google.com/storage/docs/batch-operations/create-manage-batch-operation-jobs).

## Decrypt an object

Decrypting an object encrypted with a Cloud KMS key is performed automatically as long as the relevant service agent has access to the key. For more information, see [Service agents with CMEKs](https://docs.cloud.google.com/storage/docs/encryption/customer-managed-keys#service-agents).

## What's next

  * Learn more about [CMEKs in Cloud Storage](https://docs.cloud.google.com/storage/docs/encryption/customer-managed-keys).
  * [Configure which encryption methods are allowed or restricted](https://docs.cloud.google.com/storage/docs/encryption/enforce-encryption-types) for new objects in your buckets.
  * [Rotate your Cloud KMS keys](https://docs.cloud.google.com/kms/docs/rotating-keys).
  * Explore [other products that can work with Cloud KMS](https://docs.cloud.google.com/kms/docs/using-other-products).
  * Learn about the [`restrictNonCmekServices`](https://docs.cloud.google.com/kms/docs/cmek-org-policy#require-cmek) and [`restrictCmekCryptoKeyProjects`](https://docs.cloud.google.com/kms/docs/cmek-org-policy#project-constraint) organization policy constraints to take more control over the usage of Cloud KMS keys.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
