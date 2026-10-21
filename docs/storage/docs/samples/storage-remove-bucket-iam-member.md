---
url: https://docs.cloud.google.com/storage/docs/samples/storage-remove-bucket-iam-member/
title: Delete an IAM member \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:28:26.779608+00:00
---

# Delete an IAM member  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/samples/storage-remove-bucket-iam-member/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Samples ](https://docs.cloud.google.com/storage/docs/samples)



#  Delete an IAM member Stay organized with collections  Save and categorize content based on your preferences. 

Delete a member from the IAM policy for a Cloud Storage bucket.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Set and manage IAM policies on buckets](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions)



## Code sample

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    namespace gcs = ::google::cloud::storage;
    using ::google::cloud::StatusOr;
    [](gcs::Client client, std::string const& bucket_name,
       std::string const& role, std::string const& member) {
      auto policy = client.GetNativeBucketIamPolicy(
          bucket_name, gcs::RequestedPolicyVersion(3));
      if (!policy) throw std::move(policy).status();
    
      policy->set_version(3);
      std::vector<google::cloud::storage::NativeIamBinding> updated_bindings;
      for (auto& binding : policy->bindings()) {
        auto& members = binding.members();
        if (binding.role() == role && !binding.has_condition()) {
          members.erase(std::remove(members.begin(), members.end(), member),
                        members.end());
        }
        if (!members.empty()) {
          updated_bindings.emplace_back(std::move(binding));
        }
      }
      policy->bindings() = std::move(updated_bindings);
    
      auto updated = client.SetNativeBucketIamPolicy(bucket_name, *policy);
      if (!updated) throw std::move(updated).status();
    
      std::cout << "Updated IAM policy bucket " << bucket_name
                << ". The new policy is " << *updated << "\n";
    }

### C#

For more information, see the [Cloud Storage C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    using [Google.Cloud.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html);
    using System;
    using System.Linq;
    
    public class RemoveBucketIamMemberSample
    {
        public void RemoveBucketIamMember(
            string bucketName = "your-unique-bucket-name",
            string role = "roles/storage.objectViewer",
            string member = "serviceAccount:dev@iam.gserviceaccount.com")
        {
            var storage = [StorageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html#Google_Cloud_Storage_V1_StorageClient_Create)();
            var policy = storage.GetBucketIamPolicy(bucketName, new [GetBucketIamPolicyOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.GetBucketIamPolicyOptions.html)
            {
                RequestedPolicyVersion = 3
            });
            // Set the policy schema version. For more information, please refer to https://cloud.google.com/iam/docs/policies#versions.
            policy.Version = 3;
    
            foreach (var binding in policy.Bindings.Where(c => c.Role == role).ToList())
            {
                // Remove the role/member combo from the IAM policy.
                binding.Members = binding.Members.Where(m => m != member).ToList();
                // Remove role if it contains no members.
                if (binding.Members.Count == 0)
                {
                    policy.Bindings.Remove(binding);
                }
            }
            // Set the modified IAM policy to be the current IAM policy.
            storage.SetBucketIamPolicy(bucketName, policy);
            Console.WriteLine($"Removed {member} with role {role} from {bucketName}");
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
    
    	"cloud.google.com/go/iam"
    	"cloud.google.com/go/storage"
    )
    
    // removeBucketIAMMember removes the bucket IAM member.
    func removeBucketIAMMember(w io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), bucketName string) error {
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
    	policy, err := bucket.[IAM](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketHandle_IAM)().Policy(ctx)
    	if err != nil {
    		return fmt.Errorf("Bucket(%q).IAM().Policy: %w", bucketName, err)
    	}
    	// Other valid prefixes are "serviceAccount:", "user:"
    	// See the documentation for more values.
    	// https://cloud.google.com/storage/docs/access-control/iam
    	// member string, role iam.RoleName
    	identity := "group:cloud-logs@google.com"
    	var role iam.[RoleName](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/iam/latest/index.html#cloud_google_com_go_iam_RoleName) = "roles/storage.objectViewer"
    
    	policy.[Remove](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/iam/latest/index.html#cloud_google_com_go_iam_Policy_Remove)(identity, role)
    	if err := bucket.[IAM](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketHandle_IAM)().SetPolicy(ctx, policy); err != nil {
    		return fmt.Errorf("Bucket(%q).IAM().SetPolicy: %w", bucketName, err)
    	}
    	// NOTE: It may be necessary to retry this operation if IAM policies are
    	// being modified concurrently. SetPolicy will return an error if the policy
    	// was modified since it was retrieved.
    	fmt.Fprintf(w, "Removed %v with role %v from %v\n", identity, role, bucketName)
    	return nil
    }
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import com.google.cloud.[Binding](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.Binding.html);
    import com.google.cloud.[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    import java.util.ArrayList;
    import java.util.[List](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.ExecuteDashboardQueryResponse.ColumnType.List.html);
    
    public class RemoveBucketIamMember {
      public static void removeBucketIamMember([String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) projectId, [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) bucketName) {
        // The ID of your GCP project
        // String projectId = "your-project-id";
    
        // The ID of your GCS bucket
        // String bucketName = "your-unique-bucket-name";
    
        // For more information please read:
        // https://cloud.google.com/storage/docs/access-control/iam
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder().setProjectId(projectId).build().getService();
    
        [Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy.html) originalPolicy =
            storage.[getIamPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_getIamPolicy_java_lang_String_com_google_cloud_storage_Storage_BucketSourceOption____)(bucketName, Storage.BucketSourceOption.requestedPolicyVersion(3));
    
        [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) role = "roles/storage.objectViewer";
        [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) member = "group:example@google.com";
    
        // getBindingsList() returns an ImmutableList and copying over to an ArrayList so it's mutable.
        List<Binding> bindings = new ArrayList(originalPolicy.[getBindingsList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy.html#com_google_cloud_compute_v1_Policy_getBindingsList__)());
    
        // Remove role-member binding without a condition.
        for (int index = 0; index < bindings.size(); index++) {
          [Binding](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.Binding.html) binding = bindings.get(index);
          boolean foundRole = binding.[getRole](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Binding.html#com_google_cloud_compute_v1_Binding_getRole__)().equals(role);
          boolean foundMember = binding.[getMembers](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Binding.html#com_google_cloud_compute_v1_Binding_getMembers_int_)().contains(member);
          boolean bindingIsNotConditional = binding.[getCondition](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Binding.html#com_google_cloud_compute_v1_Binding_getCondition__)() == null;
    
          if (foundRole && foundMember && bindingIsNotConditional) {
            bindings.set(index, binding.[toBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.Binding.html#com_google_cloud_agentregistry_v1_Binding_toBuilder__)().[removeMembers](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.Binding.Builder.html#com_google_cloud_Binding_Builder_removeMembers_java_lang_String____)(member).build());
            break;
          }
        }
    
        // Update policy to remove member
        [Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy.html).Builder updatedPolicyBuilder = originalPolicy.[toBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy.html#com_google_cloud_compute_v1_Policy_toBuilder__)();
        updatedPolicyBuilder.setBindings(bindings).setVersion(3);
        [Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy.html) updatedPolicy = storage.[setIamPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_setIamPolicy_java_lang_String_com_google_cloud_Policy_com_google_cloud_storage_Storage_BucketSourceOption____)(bucketName, updatedPolicyBuilder.build());
    
        System.out.printf("Removed %s with role %s from %s\n", member, role, bucketName);
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
    
    // The role to revoke
    // const roleName = 'roles/storage.objectViewer';
    
    // The members to revoke the roles from
    // const members = [
    //   'user:jdoe@example.com',
    //   'group:admins@example.com',
    // ];
    
    // Imports the Google Cloud client library
    const {Storage} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    
    // Creates a client
    const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)();
    
    async function removeBucketIamMember() {
      // Get a reference to a Google Cloud Storage bucket
      const bucket = storage.bucket(bucketName);
    
      // For more information please read:
      // https://cloud.google.com/storage/docs/access-control/iam
      const [policy] = await bucket.[iam](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/bucket.html).[getPolicy](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/iam.html)({requestedPolicyVersion: 3});
    
      // Finds and updates the appropriate role-member group, without a condition.
      const index = policy.bindings.findIndex(
        binding => binding.role === roleName && !binding.condition
      );
    
      const role = policy.bindings[index];
      if (role) {
        role.members = role.members.filter(
          member => members.indexOf(member) === -1
        );
    
        // Updates the policy object with the new (or empty) role-member group
        if (role.members.length === 0) {
          policy.bindings.splice(index, 1);
        } else {
          policy.bindings.index = role;
        }
    
        // Updates the bucket's IAM policy
        await bucket.[iam](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/bucket.html).[setPolicy](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/iam.html)(policy);
      } else {
        // No matching role-member group(s) were found
        throw new Error('No matching role-member group(s) found.');
      }
    
      console.log(
        `Removed the following member(s) with role ${roleName} from ${bucketName}:`
      );
      members.forEach(member => {
        console.log(`  ${member}`);
      });
    }
    
    removeBucketIamMember().catch(console.error);

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Storage\StorageClient;
    
    /**
     * Removes a member / role IAM pair from a given Cloud Storage bucket.
     *
     * @param string $bucketName The name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     * @param string $role The role from which the specified member should be removed.
     *        (e.g. 'roles/storage.objectViewer')
     * @param string $member The member to be removed from the specified role.
     *        (e.g. 'group:example@google.com')
     */
    function remove_bucket_iam_member(string $bucketName, string $role, string $member): void
    {
        $storage = new StorageClient();
        $bucket = $storage->bucket($bucketName);
        $iam = $bucket->iam();
        $policy = $iam->policy(['requestedPolicyVersion' => 3]);
        $policy['version'] = 3;
    
        foreach ($policy['bindings'] as $i => $binding) {
            // This example only removes member from bindings without a condition.
            if ($binding['role'] == $role && !isset($binding['condition'])) {
                $key = array_search($member, $binding['members']);
                if ($key !== false) {
                    unset($binding['members'][$key]);
    
                    // If the last member is removed from the binding, clean up the
                    // binding.
                    if (count($binding['members']) == 0) {
                        unset($policy['bindings'][$i]);
                        // Ensure array keys are sequential, otherwise JSON encodes
                        // the array as an object, which fails when calling the API.
                        $policy['bindings'] = array_values($policy['bindings']);
                    } else {
                        // Ensure array keys are sequential, otherwise JSON encodes
                        // the array as an object, which fails when calling the API.
                        $binding['members'] = array_values($binding['members']);
                        $policy['bindings'][$i] = $binding;
                    }
    
                    $iam->setPolicy($policy);
                    printf('User %s removed from role %s for bucket %s' . PHP_EOL, $member, $role, $bucketName);
                    return;
                }
            }
        }
    
        throw new \RuntimeException('No matching role-member group(s) found.');
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
    
    def remove_bucket_iam_member(bucket_name, role, member):
        """Remove member from bucket IAM Policy"""
        # bucket_name = "your-bucket-name"
        # role = "IAM role, e.g. roles/storage.objectViewer"
        # member = "IAM identity, e.g. user: name@example.com"
    
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
        bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(bucket_name)
    
        policy = bucket.get_iam_policy(requested_policy_version=3)
    
        for binding in policy.bindings:
            print(binding)
            if binding["role"] == role and binding.get("condition") is None:
                binding["members"].discard(member)
    
        bucket.set_iam_policy(policy)
    
        print(f"Removed {member} with role {role} from {bucket_name}.")
    
    

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    def remove_bucket_iam_member bucket_name:
      # The ID of your GCS bucket
      # bucket_name = "your-unique-bucket-name"
    
      # For more information please read: https://cloud.google.com/storage/docs/access-control/iam
    
      require "google/cloud/storage"
    
      storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
      bucket = storage.bucket bucket_name
    
      role   = "roles/storage.objectViewer"
      member = "group:example@google.com"
    
      bucket.[policy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html) requested_policy_version: 3 do |policy|
        policy.[bindings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-PolicyV3.html).[each](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Policy-Bindings.html) do |binding|
          if binding.role == role && binding.[condition](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Policy-Binding.html).nil?
            binding.[members](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Policy-Binding.html).delete member
          end
        end
      end
    
      puts "Removed #{member} with role #{role} from #{bucket_name}"
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=storage). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
