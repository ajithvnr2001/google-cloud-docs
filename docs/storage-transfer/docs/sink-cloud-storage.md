---
url: https://docs.cloud.google.com/storage-transfer/docs/sink-cloud-storage/
title: Configure access to a sink: Cloud Storage \u00a0|\u00a0 Storage Transfer Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:01:43.649917+00:00
---

# Configure access to a sink: Cloud Storage  |  Storage Transfer Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage-transfer/docs/sink-cloud-storage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Storage Transfer Service ](https://docs.cloud.google.com/storage-transfer/docs/overview)



Send feedback 

#  Configure access to a sink: Cloud Storage Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Storage uses a [service agent](https://docs.cloud.google.com/iam/docs/service-account-types#service-agents) to move data to a Cloud Storage bucket. This service agent is created the first time that you call [`googleServiceAccounts.get`](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/googleServiceAccounts/get).

The destination bucket does not need to belong to the same project as the service agent. The steps are the same regardless of which project the bucket is in.

## User permissions

In order to grant the required permissions to the service agent, you must have the relevant permissions on the destination bucket:

  * `storage.buckets.getIamPolicy`
  * `storage.buckets.setIamPolicy`



The **Storage Legacy Bucket Owner** role (`roles/storage.legacyBucketOwner`) or the **Storage Admin** role (`roles/storage.admin`) provide the required permissions.

## Auto-granting permissions in the Google Cloud console

If you're using the Google Cloud console to create your transfer and have the permissions listed in User permissions, the service agent will automatically be granted the required permissions on your destination bucket.

You can skip the steps on this page. If required, [configure access to your source](https://docs.cloud.google.com/storage-transfer/docs/sources-and-sinks), then [create a transfer](https://docs.cloud.google.com/storage-transfer/docs/create-transfers).

## Required permissions

The service agent must have the following permissions for the destination bucket:

Permission | Description  
---|---  
`storage.buckets.get` | Allows the service account to get the location of the bucket.  
`storage.objects.get` | Allows the service account to view objects and their metadata, excluding ACLs. Required if your transfer is configured to [overwrite objects](/storage-transfer/docs/reference/rest/v1/TransferOptions#OverwriteWhen) in the sink when different, or never. Not required if your transfer setting is to overwrite always.   
`storage.objects.create` | Allows the service account to add objects to the bucket.  
`storage.objects.delete` | Allows the service account to delete objects in the bucket. Required if you set `overwriteObjectsAlreadyExistingInSink` or `deleteObjectsUniqueInSink` to `true`. Note that if the destination bucket has [object versioning](https://docs.cloud.google.com/storage/docs/object-versioning) enabled, neither `overwriteObjectsAlreadyExistingInSink` nor `deleteObjectsUniqueInSink` permanently delete any objects. Instead, relevant live object versions become noncurrent.  
`storage.objects.list` | Allows the service account to list objects in the bucket. Required if you set `overwriteObjectsAlreadyExistingInSink` to `false` or `deleteObjectsUniqueInSink` to `true`.  
  
The following predefined role grants the required permissions:

  * **Storage Legacy Bucket Writer** (`roles/storage.legacyBucketWriter`)



In addition, for transfers configured to [overwrite objects](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/TransferOptions#OverwriteWhen) in the sink when different, or never, assign the following predefined role to the service agent:

  * **Storage Object Viewer** (`roles/storage.objectViewer`)



For a complete list of Cloud Storage roles and the permissions they contain, see [IAM roles](https://docs.cloud.google.com/storage/docs/access-control/iam-roles).

## Grant the required permissions

To grant the **Storage Legacy Bucket Writer** and **Storage Object Viewer** roles to the service agent, follow these steps.

### Find the service agent's email

  1. Go to the [`googleServiceAccounts.get` reference page](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/googleServiceAccounts/get).

An interactive panel opens, titled **Try this method**.

  2. In the panel, under **Request parameters** , enter your [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). The project you specify here must be the project that you're using to manage Storage Transfer Service, which might be different from the destination bucket's project.

  3. Click **Execute**.

Your service agent's email is returned as the value of `accountEmail`. Copy this value.

The service agent's email uses the format `project-PROJECT_NUMBER@storage-transfer-service.iam.gserviceaccount.com`.




### Add the service agent to a bucket-level policy

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. Click the **Bucket overflow** menu (more_vert) associated with the bucket to which you want to grant a principal a role.

  3. Choose **Edit access**.

  4. Click the **\+ Add principal** button.

  5. In the **New principals** field, enter your service agent's account email.

  6. Select `Storage Legacy Bucket Writer` from the **Select a role** drop-down menu.

  7. Click **Save**.

  8. Repeat to add the `Storage Object Viewer` role if your transfer is configured to overwrite objects in the sink when different, or never.




### gcloud

Use the `gcloud storage buckets add-iam-policy-binding` command:
    
    
    gcloud storage buckets add-iam-policy-binding gs://BUCKET_NAME \
    --member=serviceAccount:YOUR_AGENT_EMAIL --role=roles/storage.legacyBucketWriter

Replace the following:

  * `BUCKET_NAME` is the name of the bucket that you're granting the principal access to. For example, `my-bucket`.
  * `YOUR_AGENT_EMAIL` is the agent account email that you copied in Find the service agent's email.



To grant the `Storage Object Viewer` role for transfers configured to [overwrite objects in the sink](https://docs.cloud.google.com/sdk/gcloud/reference/transfer/jobs/create#--overwrite-when) when different or never:
    
    
    gcloud storage buckets add-iam-policy-binding gs://BUCKET_NAME \
    --member=serviceAccount:YOUR_AGENT_EMAIL --role=roles/storage.objectViewer

### Code samples

### C++

To learn how to install and use the client library for Cloud Storage, see [Cloud Storage client libraries](https://docs.cloud.google.com/storage-transfer/docs/reference/libraries). For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    namespace gcs = ::google::cloud::storage;
    using ::google::cloud::StatusOr;
    [](gcs::Client client, std::string const& bucket_name,
       std::string const& role, std::string const& member) {
      auto policy = client.GetNativeBucketIamPolicy(
          bucket_name, gcs::RequestedPolicyVersion(3));
    
      if (!policy) throw std::move(policy).status();
    
      policy->set_version(3);
      for (auto& binding : policy->bindings()) {
        if (binding.role() != role || binding.has_condition()) {
          continue;
        }
        auto& members = binding.members();
        if (std::find(members.begin(), members.end(), member) == members.end()) {
          members.emplace_back(member);
        }
      }
    
      auto updated = client.SetNativeBucketIamPolicy(bucket_name, *policy);
      if (!updated) throw std::move(updated).status();
    
      std::cout << "Updated IAM policy bucket " << bucket_name
                << ". The new policy is " << *updated << "\n";
    }

### C#

To learn how to install and use the client library for Cloud Storage, see [Cloud Storage client libraries](https://docs.cloud.google.com/storage-transfer/docs/reference/libraries). For more information, see the [Cloud Storage C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    using Google.Apis.Storage.v1.Data;
    using [Google.Cloud.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html);
    using System;
    using System.Collections.Generic;
    
    public class AddBucketIamMemberSample
    {
        public Policy AddBucketIamMember(
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
    
            Policy.BindingsData bindingToAdd = new Policy.BindingsData
            {
                Role = role,
                Members = new List<string> { member }
            };
    
            policy.Bindings.Add(bindingToAdd);
            var bucketIamPolicy = storage.SetBucketIamPolicy(bucketName, policy);
            Console.WriteLine($"Added {member} with role {role} " + $"to {bucketName}");
            return bucketIamPolicy;
        }
    }

### Go

To learn how to install and use the client library for Cloud Storage, see [Cloud Storage client libraries](https://docs.cloud.google.com/storage-transfer/docs/reference/libraries). For more information, see the [Cloud Storage Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/storage). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"time"
    
    	"cloud.google.com/go/iam"
    	"cloud.google.com/go/storage"
    )
    
    // addBucketIAMMember adds the bucket IAM member to permission role.
    func addBucketIAMMember(w io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), bucketName string) error {
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
    	identity := "group:cloud-logs@google.com"
    	var role iam.[RoleName](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/iam/latest/index.html#cloud_google_com_go_iam_RoleName) = "roles/storage.objectViewer"
    
    	policy.Add(identity, role)
    	if err := bucket.[IAM](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketHandle_IAM)().SetPolicy(ctx, policy); err != nil {
    		return fmt.Errorf("Bucket(%q).IAM().SetPolicy: %w", bucketName, err)
    	}
    	// NOTE: It may be necessary to retry this operation if IAM policies are
    	// being modified concurrently. SetPolicy will return an error if the policy
    	// was modified since it was retrieved.
    	fmt.Fprintf(w, "Added %v with role %v to %v\n", identity, role, bucketName)
    	return nil
    }
    

### Java

To learn how to install and use the client library for Cloud Storage, see [Cloud Storage client libraries](https://docs.cloud.google.com/storage-transfer/docs/reference/libraries). For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import com.google.cloud.[Binding](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.Binding.html);
    import com.google.cloud.[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    import java.util.ArrayList;
    import java.util.Arrays;
    import java.util.[List](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.ExecuteDashboardQueryResponse.ColumnType.List.html);
    
    public class AddBucketIamMember {
      /** Example of adding a member to the Bucket-level IAM */
      public static void addBucketIamMember([String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) projectId, [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) bucketName) {
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
    
        // Create a new binding using role and member
        [Binding](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.Binding.html).Builder newMemberBindingBuilder = [Binding](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.Binding.html).newBuilder();
        newMemberBindingBuilder.setRole(role).setMembers(Arrays.asList(member));
        bindings.add(newMemberBindingBuilder.build());
    
        // Update policy to add member
        [Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy.html).Builder updatedPolicyBuilder = originalPolicy.[toBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy.html#com_google_cloud_compute_v1_Policy_toBuilder__)();
        updatedPolicyBuilder.setBindings(bindings).setVersion(3);
        [Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy.html) updatedPolicy = storage.[setIamPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_setIamPolicy_java_lang_String_com_google_cloud_Policy_com_google_cloud_storage_Storage_BucketSourceOption____)(bucketName, updatedPolicyBuilder.build());
    
        System.out.printf("Added %s with role %s to %s\n", member, role, bucketName);
      }
    }

### Node.js

To learn how to install and use the client library for Cloud Storage, see [Cloud Storage client libraries](https://docs.cloud.google.com/storage-transfer/docs/reference/libraries). For more information, see the [Cloud Storage Node.js API reference documentation](https://cloud.google.com/nodejs/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // The ID of your GCS bucket
    // const bucketName = 'your-unique-bucket-name';
    
    // The role to grant
    // const roleName = 'roles/storage.objectViewer';
    
    // The members to grant the new role to
    // const members = [
    //   'user:jdoe@example.com',
    //   'group:admins@example.com',
    // ];
    
    // Imports the Google Cloud client library
    const {Storage} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    
    // Creates a client
    const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)();
    
    async function addBucketIamMember() {
      // Get a reference to a Google Cloud Storage bucket
      const bucket = storage.bucket(bucketName);
    
      // For more information please read:
      // https://cloud.google.com/storage/docs/access-control/iam
      const [policy] = await bucket.[iam](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/bucket.html).[getPolicy](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/iam.html)({requestedPolicyVersion: 3});
    
      // Adds the new roles to the bucket's IAM policy
      policy.bindings.push({
        role: roleName,
        members: members,
      });
    
      // Updates the bucket's IAM policy
      await bucket.[iam](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/bucket.html).[setPolicy](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/iam.html)(policy);
    
      console.log(
        `Added the following member(s) with role ${roleName} to ${bucketName}:`
      );
    
      members.forEach(member => {
        console.log(`  ${member}`);
      });
    }
    
    addBucketIamMember().catch(console.error);

### PHP

To learn how to install and use the client library for Cloud Storage, see [Cloud Storage client libraries](https://docs.cloud.google.com/storage-transfer/docs/reference/libraries). For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Storage\StorageClient;
    
    /**
     * Adds a new member / role IAM pair to a given Cloud Storage bucket.
     *
     * @param string $bucketName The name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     * @param string $role The role to which the given member should be added.
     *        (e.g. 'roles/storage.objectViewer')
     * @param string[] $members The member(s) to be added to the role.
     *        (e.g. ['group:example@google.com'])
     */
    function add_bucket_iam_member(string $bucketName, string $role, array $members): void
    {
        $storage = new StorageClient();
        $bucket = $storage->bucket($bucketName);
    
        $policy = $bucket->iam()->policy(['requestedPolicyVersion' => 3]);
        $policy['version'] = 3;
    
        $policy['bindings'][] = [
            'role' => $role,
            'members' => $members
        ];
    
        $bucket->iam()->setPolicy($policy);
    
        printf('Added the following member(s) to role %s for bucket %s' . PHP_EOL, $role, $bucketName);
        foreach ($members as $member) {
            printf('    %s' . PHP_EOL, $member);
        }
    }

### Python

To learn how to install and use the client library for Cloud Storage, see [Cloud Storage client libraries](https://docs.cloud.google.com/storage-transfer/docs/reference/libraries). For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
    
    def add_bucket_iam_member(bucket_name, role, member):
        """Add a new member to an IAM Policy"""
        # bucket_name = "your-bucket-name"
        # role = "IAM role, e.g., roles/storage.objectViewer"
        # member = "IAM identity, e.g., user: name@example.com"
    
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
        bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(bucket_name)
    
        policy = bucket.get_iam_policy(requested_policy_version=3)
    
        policy.bindings.append({"role": role, "members": {member}})
    
        bucket.set_iam_policy(policy)
    
        print(f"Added {member} with role {role} to {bucket_name}.")
    
    

### Ruby

To learn how to install and use the client library for Cloud Storage, see [Cloud Storage client libraries](https://docs.cloud.google.com/storage-transfer/docs/reference/libraries). For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    def add_bucket_iam_member bucket_name:
      # The ID of your GCS bucket
      # bucket_name = "your-unique-bucket-name"
    
      require "google/cloud/storage"
    
      storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage-control/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
      bucket = storage.bucket bucket_name
    
      role   = "roles/storage.objectViewer"
      member = "group:example@google.com"
    
      bucket.[policy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html) requested_policy_version: 3 do |policy|
        policy.[bindings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-PolicyV3.html).[insert](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Policy-Bindings.html) role: role, members: [member]
      end
    
      puts "Added #{member} with role #{role} to #{bucket_name}"
    end

### Rust
    
    
    use google_cloud_iam_v1::model::Binding;
    use google_cloud_storage::client::StorageControl;
    
    pub async fn sample(
        client: &StorageControl,
        bucket_id: &str,
        role: &str,
        member: &str,
    ) -> anyhow::Result<()> {
        let mut policy = client
            .get_iam_policy()
            .set_resource(format!("projects/_/buckets/{bucket_id}"))
            .send()
            .await?;
        policy
            .bindings
            .push(Binding::new().set_role(role).set_members([member]));
        let updated_policy = client
            .set_iam_policy()
            .set_resource(format!("projects/_/buckets/{bucket_id}"))
            .set_policy(policy)
            .send()
            .await?;
        println!(
            "Successfully added binding for {member} to bucket {bucket_id} policy: {updated_policy:?}"
        );
        Ok(())
    }

### JSON

**Note:** This method replaces any existing IAM policy set on a bucket. If you want to modify the existing policy, retrieve it with the [getIamPolicy](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/getIamPolicy) method, edit it as needed, and use the edited version in your setIamPolicy request.

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Create a JSON file that contains the following information:
         
         {
         "bindings":[
           {
             "role": "roles/storage.legacyBucketWriter",
             "members":[
               "YOUR_AGENT_EMAIL"
             ]
           },
           {
             "role": "roles/storage.objectViewer",
             "members":[
               "YOUR_AGENT_EMAIL"
             ]
           }
         ]
         }

Replace the following:

     * `YOUR_AGENT_EMAIL` is the agent account email you copied in Find the service agent's email.
  3. Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with a [`PUT setIamPolicy`](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/setIamPolicy) request:
         
         curl -X PUT --data-binary @JSON_FILE_NAME \
         -H "Authorization: Bearer OAUTH2_TOKEN" \
         -H "Content-Type: application/json" \
         "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME/iam"

Replace the following:

     * `JSON_FILE_NAME` is the path for the file that you created in Step 2.
     * `OAUTH2_TOKEN` is the access token that you generated in Step 1.
     * `BUCKET_NAME` is the name of the bucket to which you want to give the principal access. For example, `my-bucket`.



For more information on assigning IAM roles to Cloud Storage resources, see the [Cloud Storage IAM documentation](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
