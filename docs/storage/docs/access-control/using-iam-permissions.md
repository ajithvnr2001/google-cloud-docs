---
url: https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions/
title: Set and manage IAM policies on buckets \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:29.340638+00:00
---

# Set and manage IAM policies on buckets  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Set and manage IAM policies on buckets Stay organized with collections  Save and categorize content based on your preferences. 

[Overview](https://docs.cloud.google.com/storage/docs/access-control/iam)

This page describes how to set [Identity and Access Management (IAM) policies](https://docs.cloud.google.com/iam/docs/policies) on buckets, so you can control access to objects and managed folders within those buckets.

If you're looking for other methods of access control, see the following resources:

  * To learn about how to get finer-grained control over groups of objects, see [Set and manage IAM policies on managed folders](https://docs.cloud.google.com/storage/docs/access-control/using-iam-for-managed-folders).

  * For an alternative way to control access to individual objects in your buckets, see [Access Control Lists](https://docs.cloud.google.com/storage/docs/access-control/lists).

  * For more information about controlling access to Cloud Storage resources, read [Overview of Access Control](https://docs.cloud.google.com/storage/docs/access-control).


**Note:** IAM policies cannot be managed using the XML API.

## Required roles

To get the permissions that you need to set and manage IAM policies for a bucket, ask your administrator to grant you the Storage Admin (`roles/storage.admin`) IAM role for the bucket.

This role contains the following permissions, which are required to set and manage IAM policies for buckets:

  * `storage.buckets.get`

  * `storage.buckets.getIamPolicy`

  * `storage.buckets.setIamPolicy`

  * `storage.buckets.update`

  * `storage.buckets.list`

    * This permission is only required if you plan on using the Google Cloud console to perform the tasks on this page.



You can also get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles).

## Add a principal to a bucket-level policy

For a list of roles associated with Cloud Storage, see [IAM Roles](https://docs.cloud.google.com/storage/docs/access-control/iam-roles). For information on entities to which you grant IAM roles, see [Principal identifiers](https://docs.cloud.google.com/iam/docs/principal-identifiers).

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the bucket for which you want to grant a principal a role.

  3. Select the **Permissions** tab near the top of the page.

  4. Click the _add_box_ **Grant access** button.

The _Add principals_ dialog appears.

  5. In the **New principals** field, enter one or more identities that need access to your bucket.

  6. Select a role (or roles) from the **Select a role** drop-down menu. The roles you select appear in the pane with a short description of the permissions they grant.

  7. Click **Save**.




To learn how to get detailed error information about failed Cloud Storage operations in the Google Cloud console, see [Troubleshooting](https://docs.cloud.google.com/storage/docs/troubleshooting#trouble-console).

### Command line

Use the [`buckets add-iam-policy-binding` command](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/add-iam-policy-binding):
    
    
    gcloud storage buckets add-iam-policy-binding gs://BUCKET_NAME --member=PRINCIPAL_IDENTIFIER --role=IAM_ROLE

Where:

  * `BUCKET_NAME` is the name of the bucket you are granting the principal access to. For example, `my-bucket`.

  * `PRINCIPAL_IDENTIFIER` identifies who you are granting bucket access to. For example, `user:jeffersonloveshiking@gmail.com`. For a list of principal identifier formats, see [Principal identifiers](https://docs.cloud.google.com/iam/docs/principal-identifiers).

  * `IAM_ROLE` is the [IAM role](https://docs.cloud.google.com/storage/docs/access-control/iam-roles) you are granting to the principal. For example, `roles/storage.objectViewer`.




### Client libraries

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

For more information, see the [Cloud Storage C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest). 

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

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

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

For more information, see the [Cloud Storage Node.js API reference documentation](https://cloud.google.com/nodejs/docs/reference/storage/latest). 

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

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

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

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

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

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    def add_bucket_iam_member bucket_name:
      # The ID of your GCS bucket
      # bucket_name = "your-unique-bucket-name"
    
      require "google/cloud/storage"
    
      storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage-control-v2/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
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

### REST APIs

### JSON

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Create a JSON file that contains the following information:
         
         {
         "bindings":[
           {
             "role": "IAM_ROLE",
             "members":[
               "PRINCIPAL_IDENTIFIER"
             ]
           }
         ]
         }

Where:

     * `IAM_ROLE` is the [IAM role](https://docs.cloud.google.com/storage/docs/access-control/iam-roles) you are granting. For example, `roles/storage.objectViewer`.

     * `PRINCIPAL_IDENTIFIER` identifies who you are granting bucket access to. For example, `user:jeffersonloveshiking@gmail.com`. For a list of principal identifier formats, see [Principal identifiers](https://docs.cloud.google.com/iam/docs/principal-identifiers).

  3. Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with a [`PUT setIamPolicy`](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/setIamPolicy) request:
         
         curl -X PUT --data-binary @JSON_FILE_NAME \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME/iam"

Where:

     * `JSON_FILE_NAME` is the path for the file that you created in Step 2.

     * `BUCKET_NAME` is the name of the bucket to which you want to give the principal access. For example, `my-bucket`.




## View the IAM policy for a bucket

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the bucket whose policy you want to view.

  3. In the **Bucket details** page, click the **Permissions** tab.

The IAM policy that applies to the bucket appears in the **Permissions** section.

  4. Optional: Use the **Filter** bar to filter your results.

If you search by principal, your results display each role that the principal is granted.




### Command line

Use the [`buckets get-iam-policy` command](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/get-iam-policy):
    
    
    gcloud storage buckets get-iam-policy gs://BUCKET_NAME

Where `BUCKET_NAME` is the name of the bucket whose IAM policy you want to view. For example, `my-bucket`.

### Client libraries

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    namespace gcs = ::google::cloud::storage;
    using ::google::cloud::StatusOr;
    [](gcs::Client client, std::string const& bucket_name) {
      auto policy = client.GetNativeBucketIamPolicy(
          bucket_name, gcs::RequestedPolicyVersion(3));
    
      if (!policy) throw std::move(policy).status();
      std::cout << "The IAM policy for bucket " << bucket_name << " is "
                << *policy << "\n";
    }

### C#

For more information, see the [Cloud Storage C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    using Google.Apis.Storage.v1.Data;
    using [Google.Cloud.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html);
    using System;
    
    public class ViewBucketIamMembersSample
    {
        public Policy ViewBucketIamMembers(string bucketName = "your-unique-bucket-name")
        {
            var storage = [StorageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html#Google_Cloud_Storage_V1_StorageClient_Create)();
            var policy = storage.GetBucketIamPolicy(bucketName, new [GetBucketIamPolicyOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.GetBucketIamPolicyOptions.html)
            {
                RequestedPolicyVersion = 3
            });
    
            foreach (var binding in policy.Bindings)
            {
                Console.WriteLine($"Role: {binding.Role}");
                Console.WriteLine("Members:");
                foreach (var member in binding.Members)
                {
                    Console.WriteLine($"{member}");
                }
            }
            return policy;
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
    
    // getBucketPolicy gets the bucket IAM policy.
    func getBucketPolicy(w io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), bucketName string) (*iam.[Policy3](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/iam/latest/index.html#cloud_google_com_go_iam_Policy3), error) {
    	// bucketName := "bucket-name"
    	ctx := context.Background()
    	client, err := storage.NewClient(ctx)
    	if err != nil {
    		return nil, fmt.Errorf("storage.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	ctx, cancel := context.WithTimeout(ctx, time.Second*10)
    	defer cancel()
    
    	policy, err := client.[Bucket](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Bucket)(bucketName).[IAM](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketHandle_IAM)().[V3](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/iam/latest/index.html#cloud_google_com_go_iam_Handle_V3)().Policy(ctx)
    	if err != nil {
    		return nil, fmt.Errorf("Bucket(%q).IAM().V3().Policy: %w", bucketName, err)
    	}
    	for _, binding := range policy.Bindings {
    		fmt.Fprintf(w, "%q: %q (condition: %v)\n", binding.[Role](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/iam/latest/admin/apiv1/adminpb.html#cloud_google_com_go_iam_admin_apiv1_adminpb_Role), binding.[Members](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/iam/latest/index.html#cloud_google_com_go_iam_Policy_Members), binding.Condition)
    	}
    	return policy, nil
    }
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import com.google.cloud.[Binding](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.Binding.html);
    import com.google.cloud.[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    
    public class ListBucketIamMembers {
      public static void listBucketIamMembers([String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) projectId, [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) bucketName) {
        // The ID of your GCP project
        // String projectId = "your-project-id";
    
        // The ID of your GCS bucket
        // String bucketName = "your-unique-bucket-name";
    
        // For more information please read:
        // https://cloud.google.com/storage/docs/access-control/iam
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder().setProjectId(projectId).build().getService();
    
        [Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy.html) policy =
            storage.[getIamPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_getIamPolicy_java_lang_String_com_google_cloud_storage_Storage_BucketSourceOption____)(bucketName, Storage.BucketSourceOption.requestedPolicyVersion(3));
    
        // Print binding information
        for ([Binding](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.Binding.html) binding : policy.[getBindingsList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy.html#com_google_cloud_compute_v1_Policy_getBindingsList__)()) {
          System.out.printf("Role: %s Members: %s\n", binding.getRole(), binding.getMembers());
    
          // Print condition if one is set
          boolean bindingIsConditional = binding.getCondition() != null;
          if (bindingIsConditional) {
            System.out.printf("Condition Title: %s\n", binding.getCondition().getTitle());
            System.out.printf("Condition Description: %s\n", binding.getCondition().getDescription());
            System.out.printf("Condition Expression: %s\n", binding.getCondition().getExpression());
          }
        }
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
    
    // Imports the Google Cloud client library
    const {Storage} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    
    // Creates a client
    const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)();
    
    async function viewBucketIamMembers() {
      // For more information please read:
      // https://cloud.google.com/storage/docs/access-control/iam
      const results = await storage
        .bucket(bucketName)
        .[iam](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/bucket.html).[getPolicy](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/iam.html)({requestedPolicyVersion: 3});
    
      const bindings = results[0].bindings;
    
      console.log(`Bindings for bucket ${bucketName}:`);
      for (const binding of bindings) {
        console.log(`  Role: ${binding.role}`);
        console.log('  Members:');
    
        const members = binding.members;
        for (const member of members) {
          console.log(`    ${member}`);
        }
    
        const condition = binding.condition;
        if (condition) {
          console.log('  Condition:');
          console.log(`    Title: ${condition.title}`);
          console.log(`    Description: ${condition.description}`);
          console.log(`    Expression: ${condition.expression}`);
        }
      }
    }
    
    viewBucketIamMembers().catch(console.error);

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Storage\StorageClient;
    
    /**
     * View Bucket IAM members for a given Cloud Storage bucket.
     *
     * @param string $bucketName The name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     */
    function view_bucket_iam_members(string $bucketName): void
    {
        $storage = new StorageClient();
        $bucket = $storage->bucket($bucketName);
    
        $policy = $bucket->iam()->policy(['requestedPolicyVersion' => 3]);
    
        printf('Printing Bucket IAM members for Bucket: %s' . PHP_EOL, $bucketName);
        printf(PHP_EOL);
    
        foreach ($policy['bindings'] as $binding) {
            printf('Role: %s' . PHP_EOL, $binding['role']);
            printf('Members:' . PHP_EOL);
            foreach ($binding['members'] as $member) {
                printf('  %s' . PHP_EOL, $member);
            }
    
            if (isset($binding['condition'])) {
                $condition = $binding['condition'];
                printf('  with condition:' . PHP_EOL);
                printf('    Title: %s' . PHP_EOL, $condition['title']);
                printf('    Description: %s' . PHP_EOL, $condition['description']);
                printf('    Expression: %s' . PHP_EOL, $condition['expression']);
            }
            printf(PHP_EOL);
        }
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
    
    def view_bucket_iam_members(bucket_name):
        """View IAM Policy for a bucket"""
        # bucket_name = "your-bucket-name"
    
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
        bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(bucket_name)
    
        policy = bucket.get_iam_policy(requested_policy_version=3)
    
        for binding in policy.bindings:
            print(f"Role: {binding['role']}, Members: {binding['members']}")
    
    

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    def view_bucket_iam_members bucket_name:
      # The ID of your GCS bucket
      # bucket_name = "your-unique-bucket-name"
    
      require "google/cloud/storage"
    
      storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage-control-v2/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
      bucket = storage.bucket bucket_name
    
      policy = bucket.[policy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html) requested_policy_version: 3
      policy.[bindings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-PolicyV3.html).[each](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Policy-Bindings.html) do |binding|
        puts "Role: #{binding.role}"
        puts "Members: #{binding.[members](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Policy-Binding.html)}"
    
        # if a conditional binding exists print the condition.
        if binding.[condition](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Policy-Binding.html)
          puts "Condition Title: #{binding.[condition](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Policy-Binding.html).[title](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Policy-Condition.html)}"
          puts "Condition Description: #{binding.[condition](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Policy-Binding.html).description}"
          puts "Condition Expression: #{binding.[condition](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Policy-Binding.html).[expression](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Policy-Condition.html)}"
        end
      end
    end

### Rust
    
    
    use google_cloud_storage::client::StorageControl;
    
    pub async fn sample(client: &StorageControl, bucket_id: &str) -> anyhow::Result<()> {
        let policy = client
            .get_iam_policy()
            .set_resource(format!("projects/_/buckets/{bucket_id}"))
            .send()
            .await?;
        println!("IAM policy for bucket {}: {:?}", bucket_id, policy);
        Ok(())
    }

### REST APIs

### JSON

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with a [`GET getIamPolicy`](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/getIamPolicy) request:
         
         curl -X GET \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME/iam"

Where `BUCKET_NAME` is the name of the bucket whose IAM policy you want to view. For example, `my-bucket`.




**Note:** Some roles may not appear in the bucket permissions window. If you grant roles at the project level, they don't appear in the bucket permission window, even when users with that role have access to your bucket. To view these project-level permissions, go to the [**IAM & Admin** screen](https://console.cloud.google.com/iam-admin/projects).

## Remove a principal from a bucket-level policy

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the bucket from which you want to remove a principal's role.

  3. In the **Bucket details** page, click the **Permissions** tab.

The IAM policy that applies to the bucket appears in the **Permissions** section.

  4. In the **View by principals** tab, select the checkbox for the principal you're removing.

  5. Click the **\- Remove access** button.

  6. In the overlay window that appears, click **Confirm**.




To learn how to get detailed error information about failed Cloud Storage operations in the Google Cloud console, see [Troubleshooting](https://docs.cloud.google.com/storage/docs/troubleshooting#trouble-console).

### Command line

Use the [`buckets remove-iam-policy-binding` command](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/remove-iam-policy-binding):
    
    
    gcloud storage buckets remove-iam-policy-binding  gs://BUCKET_NAME --member=PRINCIPAL_IDENTIFIER --role=IAM_ROLE

Where:

  * `BUCKET_NAME` is the name of the bucket you are revoking access to. For example, `my-bucket`.

  * `PRINCIPAL_IDENTIFIER` identifies who you are revoking access from. For example, `user:jeffersonloveshiking@gmail.com`. For a list of principal identifier formats, see [Principal identifiers](https://docs.cloud.google.com/iam/docs/principal-identifiers).

  * `IAM_ROLE` is the [IAM role](https://docs.cloud.google.com/storage/docs/access-control/iam-roles) you are revoking. For example, `roles/storage.objectViewer`.




### Client libraries

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
    
      storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage-control-v2/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
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

### Rust
    
    
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
        if let Some(binding) = policy.bindings.iter_mut().find(|b| b.role == role) {
            binding.members.retain(|m| m != member);
        }
        policy.bindings.retain(|b| !b.members.is_empty());
        let updated_policy = client
            .set_iam_policy()
            .set_resource(format!("projects/_/buckets/{bucket_id}"))
            .set_policy(policy)
            .send()
            .await?;
        println!("Successfully removed {member} with role {role} from bucket {bucket_id}");
        println!("The updated policy is: {:?}", updated_policy);
        Ok(())
    }

### REST APIs

### JSON

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Get the existing policy applied to your bucket. To do so, use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with a [`GET getIamPolicy`](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/getIamPolicy) request:
         
         curl -X GET \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME/iam"

Where `BUCKET_NAME` is the name of the bucket whose IAM policy you want to view. For example, `my-bucket`.

  3. Create a JSON file that contains the policy you retrieved in the previous step.

  4. Edit the JSON file to remove the principal from the policy.

  5. Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with a [`PUT setIamPolicy`](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/setIamPolicy) request:
         
         curl -X PUT --data-binary @JSON_FILE_NAME \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME/iam"

Where:

     * `JSON_FILE_NAME` is the path for the file that you created in Step 3.

     * `BUCKET_NAME` is the name of the bucket from which you want to remove access. For example, `my-bucket`.




**Important:** It typically takes about a minute for revoking access to take effect. In some cases it may take longer. If you remove a user's access, this change is immediately reflected in the metadata; however, the user may still have access to the object for a short period of time.

## Use IAM Conditions on buckets

The following sections show you how to add and remove [IAM Conditions](https://docs.cloud.google.com/iam/docs/conditions-overview) on your buckets. To view the IAM Conditions for your bucket, see [Viewing the IAM policy for a bucket](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions#bucket-view). For more information about using IAM Conditions with Cloud Storage, see [Conditions](https://docs.cloud.google.com/storage/docs/access-control/iam#conditions).

You must [enable uniform bucket-level access](https://docs.cloud.google.com/storage/docs/using-uniform-bucket-level-access#set) on the bucket before adding conditions.

### Set a new condition on a bucket

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the bucket that you want to add a new condition for.

  3. In the **Bucket details** page, click the **Permissions** tab.

The IAM policy that applies to the bucket appears in the **Permissions** section.

  4. Click **\+ Grant access**.

  5. For **New principals** , fill out the principals to which you want to grant access to your bucket.

  6. For each role to which you want to apply a condition:

     1. Select a **Role** to grant the principals.

     2. Click **Add condition** to open the **Edit condition** form.

     3. Fill out the **Title** of the condition. The **Description** field is optional.

     4. Use the **Condition builder** to build your condition visually, or use the **Condition editor** tab to enter the [CEL expression](https://docs.cloud.google.com/iam/docs/conditions-overview).

     5. Click **Save** to return to the **Add principal** form. To add multiple roles, click **Add another role**.

  7. Click **Save**.




To learn how to get detailed error information about failed Cloud Storage operations in the Google Cloud console, see [Troubleshooting](https://docs.cloud.google.com/storage/docs/troubleshooting#trouble-console).

### Command line

  1. Create a JSON or YAML file that defines the condition, including the `title` of the condition, the [attribute-based](https://docs.cloud.google.com/iam/docs/conditions-overview#attributes) logic `expression` for the condition, and, optionally, a `description` for the condition.

Note that Cloud Storage only supports the [date/time](https://docs.cloud.google.com/iam/docs/conditions-attribute-reference#date-time), [resource type](https://docs.cloud.google.com/iam/docs/conditions-attribute-reference#resourcetype_attribute), and [resource name](https://docs.cloud.google.com/iam/docs/conditions-attribute-reference#resourcename_attribute) attributes in the `expression`.

  2. Use the [`buckets add-iam-policy-binding` command](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/add-iam-policy-binding) with the `--condition-from-file` flag:



    
    
    gcloud storage buckets add-iam-policy-binding  gs://BUCKET_NAME --member=PRINCIPAL_IDENTIFIER --role=IAM_ROLE --condition-from-file=CONDITION_FILE

Where:

  * `BUCKET_NAME` is the name of the bucket you are granting the principal access to. For example, `my-bucket`.

  * `PRINCIPAL_IDENTIFIER` identifies who the condition applies to. For example, `user:jeffersonloveshiking@gmail.com`. For a list of principal identifier formats, see [Principal identifiers](https://docs.cloud.google.com/iam/docs/principal-identifiers).

  * `IAM_ROLE` is the [IAM role](https://docs.cloud.google.com/storage/docs/access-control/iam-roles) you are granting to the principal. For example, `roles/storage.objectViewer`.

  * `CONDITION_FILE` is the file you created in the previous step.




Alternatively, you can include the condition directly in the command with the `--condition` flag instead of the `--condition-from-file` flag.

### Client libraries

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    namespace gcs = ::google::cloud::storage;
    using ::google::cloud::StatusOr;
    [](gcs::Client client, std::string const& bucket_name,
       std::string const& role, std::string const& member,
       std::string const& condition_title,
       std::string const& condition_description,
       std::string const& condition_expression) {
      auto policy = client.GetNativeBucketIamPolicy(
          bucket_name, gcs::RequestedPolicyVersion(3));
      if (!policy) throw std::move(policy).status();
    
      policy->set_version(3);
      policy->bindings().emplace_back(gcs::NativeIamBinding(
          role, {member},
          gcs::NativeExpression(condition_expression, condition_title,
                                condition_description)));
    
      auto updated = client.SetNativeBucketIamPolicy(bucket_name, *policy);
      if (!updated) throw std::move(updated).status();
    
      std::cout << "Updated IAM policy bucket " << bucket_name
                << ". The new policy is " << *updated << "\n";
    
      std::cout << "Added member " << member << " with role " << role << " to "
                << bucket_name << ":\n";
      std::cout << "with condition:\n"
                << "\t Title: " << condition_title << "\n"
                << "\t Description: " << condition_description << "\n"
                << "\t Expression: " << condition_expression << "\n";
    }

### C#

For more information, see the [Cloud Storage C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    using Google.Apis.Storage.v1.Data;
    using [Google.Cloud.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html);
    using System;
    using System.Collections.Generic;
    
    public class AddBucketConditionalIamBindingSample
    {
        /// <summary>
        /// Adds a conditional Iam policy to a bucket.
        /// </summary>
        /// <param name="bucketName">The name of the bucket.</param>
        /// <param name="role">The role that members may assume.</param>
        /// <param name="member">The identifier of the member who may assume the provided role.</param>
        /// <param name="title">Title for the expression.</param>
        /// <param name="description">Description of the expression.</param>
        /// <param name="expression">Describes the conditions that need to be met for the policy to be applied.
        /// It's represented as a string using Common Expression Language syntax.</param>
        public Policy AddBucketConditionalIamBinding(
            string bucketName = "your-unique-bucket-name",
            string role = "roles/storage.objectViewer",
            string member = "serviceAccount:dev@iam.gserviceaccount.com",
            string title = "title",
            string description = "description",
            string expression = "resource.name.startsWith(\"projects/_/buckets/bucket-name/objects/prefix-a-\")")
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
                Members = new List<string> { member },
                Condition = new Expr
                {
                    Title = title,
                    Description = description,
                    Expression = expression
                }
            };
    
            policy.Bindings.Add(bindingToAdd);
    
            var bucketIamPolicy = storage.SetBucketIamPolicy(bucketName, policy);
            Console.WriteLine($"Added {member} with role {role} " + $"to {bucketName}");
            return bucketIamPolicy;
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
    
    	"cloud.google.com/go/iam/apiv1/iampb"
    	"cloud.google.com/go/storage"
    	"google.golang.org/genproto/googleapis/type/expr"
    )
    
    // addBucketConditionalIAMBinding adds bucket conditional IAM binding.
    func addBucketConditionalIAMBinding(w io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), bucketName, role, member, title, description, expression string) error {
    	// bucketName := "bucket-name"
    	// role := "bucket-level IAM role"
    	// member := "bucket-level IAM member"
    	// title := "condition title"
    	// description := "condition description"
    	// expression := "condition expression"
    	ctx := context.Background()
    	client, err := storage.NewClient(ctx)
    	if err != nil {
    		return fmt.Errorf("storage.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	ctx, cancel := context.WithTimeout(ctx, time.Second*10)
    	defer cancel()
    
    	bucket := client.[Bucket](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Bucket)(bucketName)
    	policy, err := bucket.[IAM](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketHandle_IAM)().V3().[Policy](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/iam/latest/apiv1/iampb.html#cloud_google_com_go_iam_apiv1_iampb_Policy)(ctx)
    	if err != nil {
    		return fmt.Errorf("Bucket(%q).IAM().V3().Policy: %w", bucketName, err)
    	}
    
    	policy.Bindings = append(policy.Bindings, &iampb.[Binding](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/iam/latest/apiv1/iampb.html#cloud_google_com_go_iam_apiv1_iampb_Binding){
    		Role:    role,
    		Members: []string{member},
    		Condition: &expr.Expr{
    			Title:       title,
    			Description: description,
    			Expression:  expression,
    		},
    	})
    
    	if err := bucket.[IAM](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketHandle_IAM)().V3().SetPolicy(ctx, policy); err != nil {
    		return fmt.Errorf("Bucket(%q).IAM().V3().SetPolicy: %w", bucketName, err)
    	}
    	// NOTE: It may be necessary to retry this operation if IAM policies are
    	// being modified concurrently. SetPolicy will return an error if the policy
    	// was modified since it was retrieved.
    	fmt.Fprintf(w, "Added %v with role %v to %v with condition %v %v %v\n", member, role, bucketName, title, description, expression)
    	return nil
    }
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import com.google.cloud.[Binding](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.Binding.html);
    import com.google.cloud.[Condition](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Condition.html);
    import com.google.cloud.[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    import java.util.ArrayList;
    import java.util.Arrays;
    import java.util.[List](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.ExecuteDashboardQueryResponse.ColumnType.List.html);
    
    public class AddBucketIamConditionalBinding {
      /** Example of adding a conditional binding to the Bucket-level IAM */
      public static void addBucketIamConditionalBinding([String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) projectId, [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) bucketName) {
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
    
        // Create a condition
        [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) conditionTitle = "Title";
        [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) conditionDescription = "Description";
        [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) conditionExpression =
            "resource.name.startsWith(\"projects/_/buckets/bucket-name/objects/prefix-a-\")";
        [Condition](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Condition.html).Builder conditionBuilder = [Condition](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Condition.html).newBuilder();
        conditionBuilder.setTitle(conditionTitle);
        conditionBuilder.setDescription(conditionDescription);
        conditionBuilder.setExpression(conditionExpression);
    
        // getBindingsList() returns an ImmutableList, we copy over to an ArrayList so it's mutable
        List<Binding> bindings = new ArrayList(originalPolicy.[getBindingsList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy.html#com_google_cloud_compute_v1_Policy_getBindingsList__)());
    
        // Add condition to a binding
        [Binding](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.Binding.html).Builder newBindingBuilder =
            [Binding](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.Binding.html).newBuilder()
                .setRole(role)
                .setMembers(Arrays.asList(member))
                .setCondition(conditionBuilder.build());
        bindings.add(newBindingBuilder.build());
    
        // Update policy with new conditional binding
        [Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy.html).Builder updatedPolicyBuilder = originalPolicy.[toBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy.html#com_google_cloud_compute_v1_Policy_toBuilder__)();
        updatedPolicyBuilder.setBindings(bindings).setVersion(3);
    
        storage.[setIamPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_setIamPolicy_java_lang_String_com_google_cloud_Policy_com_google_cloud_storage_Storage_BucketSourceOption____)(bucketName, updatedPolicyBuilder.build());
    
        System.out.printf(
            "Added %s with role %s to %s with condition %s %s %s\n",
            member, role, bucketName, conditionTitle, conditionDescription, conditionExpression);
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
    
    // The role to grant
    // const roleName = 'roles/storage.objectViewer';
    
    // The members to grant the new role to
    // const members = [
    //   'user:jdoe@example.com',
    //   'group:admins@example.com',
    // ];
    
    // Create a condition
    // const title = 'Title';
    // const description = 'Description';
    // const expression = 'resource.name.startsWith(\"projects/_/buckets/bucket-name/objects/prefix-a-\")';
    
    // Imports the Google Cloud client library
    const {Storage} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    
    // Creates a client
    const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)();
    
    async function addBucketConditionalBinding() {
      // Get a reference to a Google Cloud Storage bucket
      const bucket = storage.bucket(bucketName);
    
      // Gets and updates the bucket's IAM policy
      const [policy] = await bucket.[iam](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/bucket.html).[getPolicy](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/iam.html)({requestedPolicyVersion: 3});
    
      // Set the policy's version to 3 to use condition in bindings.
      policy.version = 3;
    
      // Adds the new roles to the bucket's IAM policy
      policy.bindings.push({
        role: roleName,
        members: members,
        condition: {
          title: title,
          description: description,
          expression: expression,
        },
      });
    
      // Updates the bucket's IAM policy
      await bucket.[iam](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/bucket.html).[setPolicy](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/iam.html)(policy);
    
      console.log(
        `Added the following member(s) with role ${roleName} to ${bucketName}:`
      );
    
      members.forEach(member => {
        console.log(`  ${member}`);
      });
    
      console.log('with condition:');
      console.log(`  Title: ${title}`);
      console.log(`  Description: ${description}`);
      console.log(`  Expression: ${expression}`);
    }
    
    addBucketConditionalBinding().catch(console.error);

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Storage\StorageClient;
    
    /**
     * Adds a conditional IAM binding to a bucket's IAM policy.
     *
     * @param string $bucketName The name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     * @param string $role The role that will be given to members in this binding.
     *        (e.g. 'roles/storage.objectViewer')
     * @param string[] $members The member(s) associated with this binding.
     *        (e.g. ['group:example@google.com'])
     * @param string $title The title of the condition. (e.g. 'Title')
     * @param string $description The description of the condition.
     *        (e.g. 'Condition Description')
     * @param string $expression The condition specified in CEL expression language.
     *        (e.g. 'resource.name.startsWith("projects/_/buckets/bucket-name/objects/prefix-a-")')
     *
     * To see how to express a condition in CEL, visit:
     * @see https://cloud.google.com/storage/docs/access-control/iam#conditions.
     */
    function add_bucket_conditional_iam_binding(string $bucketName, string $role, array $members, string $title, string $description, string $expression): void
    {
        $storage = new StorageClient();
        $bucket = $storage->bucket($bucketName);
    
        $policy = $bucket->iam()->policy(['requestedPolicyVersion' => 3]);
    
        $policy['version'] = 3;
    
        $policy['bindings'][] = [
            'role' => $role,
            'members' => $members,
            'condition' => [
                'title' => $title,
                'description' => $description,
                'expression' => $expression,
            ],
        ];
    
        $bucket->iam()->setPolicy($policy);
    
        printf('Added the following member(s) with role %s to %s:' . PHP_EOL, $role, $bucketName);
        foreach ($members as $member) {
            printf('    %s' . PHP_EOL, $member);
        }
        printf('with condition:' . PHP_EOL);
        printf('    Title: %s' . PHP_EOL, $title);
        printf('    Description: %s' . PHP_EOL, $description);
        printf('    Expression: %s' . PHP_EOL, $expression);
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
    
    def add_bucket_conditional_iam_binding(
        bucket_name, role, title, description, expression, members
    ):
        """Add a conditional IAM binding to a bucket's IAM policy."""
        # bucket_name = "your-bucket-name"
        # role = "IAM role, e.g. roles/storage.objectViewer"
        # members = {"IAM identity, e.g. user: name@example.com}"
        # title = "Condition title."
        # description = "Condition description."
        # expression = "Condition expression."
    
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
        bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(bucket_name)
    
        policy = bucket.get_iam_policy(requested_policy_version=3)
    
        # Set the policy's version to 3 to use condition in bindings.
        policy.version = 3
    
        policy.bindings.append(
            {
                "role": role,
                "members": members,
                "condition": {
                    "title": title,
                    "description": description,
                    "expression": expression,
                },
            }
        )
    
        bucket.set_iam_policy(policy)
    
        print(f"Added the following member(s) with role {role} to {bucket_name}:")
    
        for member in members:
            print(f"    {member}")
    
        print("with condition:")
        print(f"    Title: {title}")
        print(f"    Description: {description}")
        print(f"    Expression: {expression}")
    
    

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    def add_bucket_conditional_iam_binding bucket_name:
      # The ID of your GCS bucket
      # bucket_name = "your-unique-bucket-name"
    
      require "google/cloud/storage"
    
      storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage-control-v2/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
      bucket = storage.bucket bucket_name
    
      role        = "roles/storage.objectViewer"
      member      = "group:example@google.com"
      title       = "Title"
      description = "Description"
      expression  = "resource.name.startsWith(\"projects/_/buckets/bucket-name/objects/prefix-a-\")"
    
      bucket.[policy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html) requested_policy_version: 3 do |policy|
        policy.[version](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Policy.html) = 3
        policy.[bindings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-PolicyV3.html).[insert](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Policy-Bindings.html)(
          role:      role,
          members:   member,
          condition: {
            title:       title,
            description: description,
            expression:  expression
          }
        )
      end
    
      puts "Added #{member} with role #{role} to #{bucket_name} with condition #{title} #{description} #{expression}"
    end

### Rust
    
    
    use google_cloud_iam_v1::model::{Binding, GetPolicyOptions};
    use google_cloud_storage::client::StorageControl;
    use google_cloud_type::model::Expr;
    
    pub async fn sample(
        client: &StorageControl,
        bucket_id: &str,
        service_account: &str,
    ) -> anyhow::Result<()> {
        const ROLE: &str = "roles/storage.objectViewer";
        const TITLE: &str = "A service account can read prefix-a-*";
    
        let mut policy = client
            .get_iam_policy()
            .set_resource(format!("projects/_/buckets/{bucket_id}"))
            .set_options(GetPolicyOptions::new().set_requested_policy_version(3))
            .send()
            .await?;
        let condition = Expr::new()
            .set_expression(format!(
                r#"resource.name.startsWith("projects/_/buckets/{bucket_id}/objects/prefix-a-")"#
            ))
            .set_title(TITLE)
            .set_description(format!(
                "Allows {service_account} read access to objects starting with `prefix-a-`"
            ));
        let binding = Binding::new()
            .set_role(ROLE)
            .set_members([format!("serviceAccount:{service_account}")])
            .set_condition(condition);
        policy.version = 3;
        policy.bindings.push(binding);
        let updated_policy = client
            .set_iam_policy()
            .set_resource(format!("projects/_/buckets/{bucket_id}"))
            .set_policy(policy)
            .send()
            .await?;
        println!(
            "Successfully added conditional IAM binding to bucket {bucket_id}: {updated_policy:?}"
        );
        Ok(())
    }

### REST APIs

### JSON

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use a [`GET getIamPolicy`](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/getIamPolicy) request to save the bucket's IAM policy to a temporary JSON file:
         
         curl \
         'https://storage.googleapis.com/storage/v1/b/BUCKET_NAME/iam' \
         --header 'Authorization: Bearer $(gcloud auth print-access-token)' > tmp-policy.json

Where `BUCKET_NAME` is the name of the relevant bucket. For example, `my-bucket`.

  3. Edit the `tmp-policy.json` file in a text editor to add new conditions to the bindings in the IAM policy:
         
         {
             "version": VERSION,
             "bindings": [
               {
                 "role": "IAM_ROLE",
                 "members": [
                   "PRINCIPAL_IDENTIFIER"
                 ],
                 "condition": {
                   "title": "TITLE",
                   "description": "DESCRIPTION",
                   "expression": "EXPRESSION"
                 }
               }
             ],
             "etag": "ETAG"
         }

Where:

     * `VERSION` is the [IAM policy version](https://docs.cloud.google.com/iam/docs/policies#versions), which is required to be 3 for buckets with IAM Conditions.

     * `IAM_ROLE` is the role to which the condition applies. For example, `roles/storage.objectViewer`.

     * `PRINCIPAL_IDENTIFIER` identifies who the condition applies to. For example, `user:jeffersonloveshiking@gmail.com`. For a list of principal identifier formats, see [Principal identifiers](https://docs.cloud.google.com/iam/docs/principal-identifiers).

     * `TITLE` is the title of the condition. For example, `expires in 2019`.

     * `DESCRIPTION` is an optional description of the condition. For example, `Permission revoked on New Year's`.

     * `EXPRESSION` is an [attribute-based](https://docs.cloud.google.com/iam/docs/conditions-overview#attributes) logic expression. For example, `request.time < timestamp(\"2019-01-01T00:00:00Z\")`. For more examples of expressions, see the [Conditions attribute reference](https://docs.cloud.google.com/iam/docs/conditions-attribute-reference). Note that Cloud Storage only supports the [date/time](https://docs.cloud.google.com/iam/docs/conditions-attribute-reference#date-time), [resource type](https://docs.cloud.google.com/iam/docs/conditions-attribute-reference#resourcetype_attribute), and [resource name](https://docs.cloud.google.com/iam/docs/conditions-attribute-reference#resourcename_attribute) attributes.

Don't modify `ETAG`.

  4. Use a [`PUT setIamPolicy`](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/setIamPolicy) request to set the modified IAM policy on the bucket:
         
         curl -X PUT --data-binary @tmp-policy.json \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME/iam"

Where `BUCKET_NAME` is the name of the relevant bucket. For example, `my-bucket`.




### Remove a condition from a bucket

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the bucket that you want to remove a condition from.

  3. In the **Bucket details** page, click the **Permissions** tab.

The IAM policy that applies to the bucket appears in the **Permissions** section.

  4. Click the **Edit** icon _edit_ for the principal associated with the condition.

  5. In the **Edit access** overlay that appears, click the name of the condition you want to delete.

  6. In the **Edit condition** overlay that appears, click **Delete** , then **Confirm**.

  7. Click **Save**.




To learn how to get detailed error information about failed Cloud Storage operations in the Google Cloud console, see [Troubleshooting](https://docs.cloud.google.com/storage/docs/troubleshooting#trouble-console).

### Command line

  1. Use the [`buckets get-iam-policy` command](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/get-iam-policy) to save the bucket's IAM policy to a temporary JSON file.
         
         gcloud storage buckets get-iam-policy gs://BUCKET_NAME > tmp-policy.json

  2. Edit the `tmp-policy.json` file in a text editor to remove conditions from the IAM policy.

  3. Use [`buckets set-iam-policy`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/set-iam-policy) to set the modified IAM policy on the bucket.
         
         gcloud storage buckets set-iam-policy gs://BUCKET_NAME tmp-policy.json




### Code samples

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    namespace gcs = ::google::cloud::storage;
    using ::google::cloud::StatusOr;
    [](gcs::Client client, std::string const& bucket_name,
       std::string const& role, std::string const& condition_title,
       std::string const& condition_description,
       std::string const& condition_expression) {
      auto policy = client.GetNativeBucketIamPolicy(
          bucket_name, gcs::RequestedPolicyVersion(3));
      if (!policy) throw std::move(policy).status();
    
      policy->set_version(3);
      auto& bindings = policy->bindings();
      auto e = std::remove_if(
          bindings.begin(), bindings.end(),
          [role, condition_title, condition_description,
           condition_expression](gcs::NativeIamBinding b) {
            return (b.role() == role && b.has_condition() &&
                    b.condition().title() == condition_title &&
                    b.condition().description() == condition_description &&
                    b.condition().expression() == condition_expression);
          });
      if (e == bindings.end()) {
        std::cout << "No matching binding group found.\n";
        return;
      }
      bindings.erase(e);
      auto updated = client.SetNativeBucketIamPolicy(bucket_name, *policy);
      if (!updated) throw std::move(updated).status();
    
      std::cout << "Conditional binding was removed.\n";
    }

### C#

For more information, see the [Cloud Storage C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    using Google.Apis.Storage.v1.Data;
    using [Google.Cloud.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html);
    using System;
    using System.Linq;
    
    public class RemoveBucketConditionalIamBindingSample
    {
        public Policy RemoveBucketConditionalIamBinding(
            string bucketName = "your-unique-bucket-name",
            string role = "roles/storage.objectViewer",
            string title = "title",
            string description = "description",
            string expression = "resource.name.startsWith(\"projects/_/buckets/bucket-name/objects/prefix-a-\")")
        {
            var storage = [StorageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html#Google_Cloud_Storage_V1_StorageClient_Create)();
            var policy = storage.GetBucketIamPolicy(bucketName, new [GetBucketIamPolicyOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.GetBucketIamPolicyOptions.html)
            {
                RequestedPolicyVersion = 3
            });
            // Set the policy schema version. For more information, please refer to https://cloud.google.com/iam/docs/policies#versions.
            policy.Version = 3;
    
            var bindingsToRemove = policy.Bindings.Where(binding => binding.Role == role
                  && binding.Condition != null
                  && binding.Condition.Title == title
                  && binding.Condition.Description == description
                  && binding.Condition.Expression == expression).ToList();
            if (bindingsToRemove.Count() > 0)
            {
                foreach (var binding in bindingsToRemove)
                {
                    policy.Bindings.Remove(binding);
                }
                // Set the modified IAM policy to be the current IAM policy.
                policy = storage.SetBucketIamPolicy(bucketName, policy);
                Console.WriteLine("Conditional Binding was removed.");
            }
            else
            {
                Console.WriteLine("No matching conditional binding found.");
            }
            return policy;
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
    
    // removeBucketConditionalIAMBinding removes bucket conditional IAM binding.
    func removeBucketConditionalIAMBinding(w io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), bucketName, role, title, description, expression string) error {
    	// bucketName := "bucket-name"
    	// role := "bucket-level IAM role"
    	// title := "condition title"
    	// description := "condition description"
    	// expression := "condition expression"
    	ctx := context.Background()
    	client, err := storage.NewClient(ctx)
    	if err != nil {
    		return fmt.Errorf("storage.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	ctx, cancel := context.WithTimeout(ctx, time.Second*10)
    	defer cancel()
    
    	bucket := client.[Bucket](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Bucket)(bucketName)
    	policy, err := bucket.[IAM](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketHandle_IAM)().V3().Policy(ctx)
    	if err != nil {
    		return fmt.Errorf("Bucket(%q).IAM().V3().Policy: %w", bucketName, err)
    	}
    
    	// Find the index of the binding matching inputs.
    	i := -1
    	for j, binding := range policy.Bindings {
    		if binding.Role == role && binding.Condition != nil {
    			condition := binding.Condition
    			if condition.Title == title &&
    				condition.Description == description &&
    				condition.Expression == expression {
    				i = j
    			}
    		}
    	}
    
    	if i == -1 {
    		return fmt.Errorf("no matching binding group found")
    	}
    
    	// Get a slice of the bindings, removing the binding at index i.
    	policy.Bindings = append(policy.Bindings[:i], policy.Bindings[i+1:]...)
    
    	if err := bucket.[IAM](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketHandle_IAM)().V3().SetPolicy(ctx, policy); err != nil {
    		return fmt.Errorf("Bucket(%q).IAM().V3().SetPolicy: %w", bucketName, err)
    	}
    	// NOTE: It may be necessary to retry this operation if IAM policies are
    	// being modified concurrently. SetPolicy will return an error if the policy
    	// was modified since it was retrieved.
    	fmt.Fprintln(w, "Conditional binding was removed")
    	return nil
    }
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import com.google.cloud.[Binding](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.Binding.html);
    import com.google.cloud.[Condition](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Condition.html);
    import com.google.cloud.[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    import java.util.ArrayList;
    import java.util.Iterator;
    import java.util.[List](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.ExecuteDashboardQueryResponse.ColumnType.List.html);
    
    public class RemoveBucketIamConditionalBinding {
      /** Example of removing a conditional binding to the Bucket-level IAM */
      public static void removeBucketIamConditionalBinding([String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) projectId, [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) bucketName) {
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
    
        // getBindingsList() returns an ImmutableList and copying over to an ArrayList so it's mutable.
        List<Binding> bindings = new ArrayList(originalPolicy.[getBindingsList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy.html#com_google_cloud_compute_v1_Policy_getBindingsList__)());
    
        // Create a condition to compare against
        [Condition](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Condition.html).Builder conditionBuilder = [Condition](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Condition.html).newBuilder();
        conditionBuilder.setTitle("Title");
        conditionBuilder.setDescription("Description");
        conditionBuilder.setExpression(
            "resource.name.startsWith(\"projects/_/buckets/bucket-name/objects/prefix-a-\")");
    
        Iterator iterator = bindings.iterator();
        while (iterator.hasNext()) {
          [Binding](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.Binding.html) binding = ([Binding](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.Binding.html)) iterator.next();
          boolean foundRole = binding.[getRole](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Binding.html#com_google_cloud_compute_v1_Binding_getRole__)().equals(role);
          boolean conditionsEqual = conditionBuilder.build().equals(binding.[getCondition](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Binding.html#com_google_cloud_compute_v1_Binding_getCondition__)());
    
          // Remove condition when the role and condition are equal
          if (foundRole && conditionsEqual) {
            iterator.remove();
            break;
          }
        }
    
        // Update policy to remove conditional binding
        [Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy.html).Builder updatedPolicyBuilder = originalPolicy.[toBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy.html#com_google_cloud_compute_v1_Policy_toBuilder__)();
        updatedPolicyBuilder.setBindings(bindings).setVersion(3);
        [Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy.html) updatedPolicy = storage.[setIamPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_setIamPolicy_java_lang_String_com_google_cloud_Policy_com_google_cloud_storage_Storage_BucketSourceOption____)(bucketName, updatedPolicyBuilder.build());
    
        System.out.println("Conditional Binding was removed.");
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
    
    // The role to grant
    // const roleName = 'roles/storage.objectViewer';
    
    // The members to grant the new role to
    // const members = [
    //   'user:jdoe@example.com',
    //   'group:admins@example.com',
    // ];
    
    // Create a condition
    // const title = 'Title';
    // const description = 'Description';
    // const expression = 'resource.name.startsWith(\"projects/_/buckets/bucket-name/objects/prefix-a-\")';
    
    // Imports the Google Cloud client library
    const {Storage} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    
    // Creates a client
    const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)();
    
    async function removeBucketConditionalBinding() {
      // Get a reference to a Google Cloud Storage bucket
      const bucket = storage.bucket(bucketName);
    
      // Gets and updates the bucket's IAM policy
      const [policy] = await bucket.[iam](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/bucket.html).[getPolicy](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/iam.html)({requestedPolicyVersion: 3});
    
      // Set the policy's version to 3 to use condition in bindings.
      policy.version = 3;
    
      // Finds and removes the appropriate role-member group with specific condition.
      const index = policy.bindings.findIndex(
        binding =>
          binding.role === roleName &&
          binding.condition &&
          binding.condition.title === title &&
          binding.condition.description === description &&
          binding.condition.expression === expression
      );
    
      const binding = policy.bindings[index];
      if (binding) {
        policy.bindings.splice(index, 1);
    
        // Updates the bucket's IAM policy
        await bucket.[iam](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/bucket.html).[setPolicy](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/iam.html)(policy);
    
        console.log('Conditional Binding was removed.');
      } else {
        // No matching role-member group with specific condition were found
        throw new Error('No matching binding group found.');
      }
    }
    
    removeBucketConditionalBinding().catch(console.error);

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Storage\StorageClient;
    
    /**
     * Removes a conditional IAM binding from a bucket's IAM policy.
     *
     * To see how to express a condition in CEL, visit:
     * @see https://cloud.google.com/storage/docs/access-control/iam#conditions.
     *
     * @param string $bucketName The name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     * @param string $role the role that will be given to members in this binding.
     *        (e.g. 'roles/storage.objectViewer')
     * @param string $title The title of the condition. (e.g. 'Title')
     * @param string $description The description of the condition.
     *        (e.g. 'Condition Description')
     * @param string $expression Te condition specified in CEL expression language.
     *        (e.g. 'resource.name.startsWith("projects/_/buckets/bucket-name/objects/prefix-a-")')
     */
    function remove_bucket_conditional_iam_binding(string $bucketName, string $role, string $title, string $description, string $expression): void
    {
        $storage = new StorageClient();
        $bucket = $storage->bucket($bucketName);
    
        $policy = $bucket->iam()->policy(['requestedPolicyVersion' => 3]);
    
        $policy['version'] = 3;
    
        $key_of_conditional_binding = null;
        foreach ($policy['bindings'] as $key => $binding) {
            if ($binding['role'] == $role && isset($binding['condition'])) {
                $condition = $binding['condition'];
                if ($condition['title'] == $title
                     && $condition['description'] == $description
                     && $condition['expression'] == $expression) {
                    $key_of_conditional_binding = $key;
                    break;
                }
            }
        }
    
        if ($key_of_conditional_binding != null) {
            unset($policy['bindings'][$key_of_conditional_binding]);
            // Ensure array keys are sequential, otherwise JSON encodes
            // the array as an object, which fails when calling the API.
            $policy['bindings'] = array_values($policy['bindings']);
            $bucket->iam()->setPolicy($policy);
            print('Conditional Binding was removed.' . PHP_EOL);
        } else {
            print('No matching conditional binding found.' . PHP_EOL);
        }
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
    
    def remove_bucket_conditional_iam_binding(
        bucket_name, role, title, description, expression
    ):
        """Remove a conditional IAM binding from a bucket's IAM policy."""
        # bucket_name = "your-bucket-name"
        # role = "IAM role, e.g. roles/storage.objectViewer"
        # title = "Condition title."
        # description = "Condition description."
        # expression = "Condition expression."
    
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
        bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(bucket_name)
    
        policy = bucket.get_iam_policy(requested_policy_version=3)
    
        # Set the policy's version to 3 to use condition in bindings.
        policy.version = 3
    
        condition = {
            "title": title,
            "description": description,
            "expression": expression,
        }
        policy.bindings = [
            binding
            for binding in policy.bindings
            if not (binding["role"] == role and binding.get("condition") == condition)
        ]
    
        bucket.set_iam_policy(policy)
    
        print("Conditional Binding was removed.")
    
    

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    def remove_bucket_conditional_iam_binding bucket_name:
      # The ID of your GCS bucket
      # bucket_name = "your-unique-bucket-name"
    
      require "google/cloud/storage"
    
      storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage-control-v2/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
      bucket = storage.bucket bucket_name
    
      role        = "roles/storage.objectViewer"
      title       = "Title"
      description = "Description"
      expression  = "resource.name.startsWith(\"projects/_/buckets/bucket-name/objects/prefix-a-\")"
    
      bucket.[policy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html) requested_policy_version: 3 do |policy|
        policy.[version](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Policy.html) = 3
    
        binding_to_remove = nil
        policy.[bindings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-PolicyV3.html).[each](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Policy-Bindings.html) do |b|
          condition = {
            title:       title,
            description: description,
            expression:  expression
          }
          if b.role == role && b.[condition](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Policy-Binding.html) &&
             b.[condition](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Policy-Binding.html).[title](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Policy-Condition.html) == title &&
             b.[condition](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Policy-Binding.html).description == description &&
             b.[condition](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Policy-Binding.html).[expression](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Policy-Condition.html) == expression
            binding_to_remove = b
          end
        end
        if binding_to_remove
          policy.[bindings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-PolicyV3.html).remove binding_to_remove
          puts "Conditional Binding was removed."
        else
          puts "No matching conditional binding found."
        end
      end
    end

### Rust
    
    
    use google_cloud_iam_v1::model::GetPolicyOptions;
    use google_cloud_storage::client::StorageControl;
    
    pub async fn sample(client: &StorageControl, bucket_id: &str) -> anyhow::Result<()> {
        const ROLE: &str = "roles/storage.objectViewer";
        const TITLE: &str = "A service account can read prefix-a-*";
    
        let mut policy = client
            .get_iam_policy()
            .set_resource(format!("projects/_/buckets/{bucket_id}"))
            .set_options(GetPolicyOptions::new().set_requested_policy_version(3))
            .send()
            .await?;
        policy.version = 3;
        policy.bindings.retain(|b| {
            // Remove the bindings matching the role *and* the condition title.
            b.role != ROLE || b.condition.as_ref().is_none_or(|c| c.title != TITLE)
        });
        let updated_policy = client
            .set_iam_policy()
            .set_resource(format!("projects/_/buckets/{bucket_id}"))
            .set_policy(policy)
            .send()
            .await?;
        println!("Successfully removed conditional IAM binding from bucket {bucket_id}");
        println!("The updated policy is: {:?}", updated_policy);
        Ok(())
    }

### REST APIs

### JSON

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use a [`GET getIamPolicy`](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/getIamPolicy) request to save the bucket's IAM policy to a temporary JSON file:
         
         curl \
         'https://storage.googleapis.com/storage/v1/b/BUCKET_NAME/iam' \
         --header 'Authorization: Bearer $(gcloud auth print-access-token)' > tmp-policy.json

Where `BUCKET_NAME` is the name of the bucket you are granting access to. For example, `my-bucket`.

  3. Edit the `tmp-policy.json` file in a text editor to remove conditions from the IAM policy.

  4. Use a [`PUT setIamPolicy`](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/setIamPolicy) request to set the modified IAM policy on the bucket:
         
         curl -X PUT --data-binary @tmp-policy.json \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME/iam"

Where `BUCKET_NAME` is the name of the bucket whose IAM policy you want to modify. For example, `my-bucket`.




## Best practices

You should set the minimum role needed to give the principal the required access. For example, if a team member only needs to read objects stored in a bucket, grant them the Storage Object Viewer (`roles/storage.objectViewer`) role instead of the Storage Object Admin (`roles/storage.objectAdmin`) role. Similarly, if the team member needs full control of objects in the bucket but not the bucket itself, grant them the Storage Object Admin (`roles/storage.objectAdmin`) role instead of the Storage Admin (`roles/storage.admin`) role.

## What's next

  * Learn how to [publicly share your data](https://docs.cloud.google.com/storage/docs/access-control/making-data-public).
  * See specific [Sharing and collaboration examples](https://docs.cloud.google.com/storage/docs/collaboration).
  * Learn about [best practices when using IAM](https://docs.cloud.google.com/storage/docs/access-control#best-practices).
  * Learn how to [use role recommendations for buckets](https://docs.cloud.google.com/policy-intelligence/docs/review-apply-role-recommendations-buckets).
  * To troubleshoot failed operations related to IAM roles and permissions, see [Troubleshooting](https://docs.cloud.google.com/storage/docs/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
