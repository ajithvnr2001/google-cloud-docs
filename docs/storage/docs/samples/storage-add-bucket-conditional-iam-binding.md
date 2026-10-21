---
url: https://docs.cloud.google.com/storage/docs/samples/storage-add-bucket-conditional-iam-binding/
title: Add conditional role binding \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:06:35.629040+00:00
---

# Add conditional role binding  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/samples/storage-add-bucket-conditional-iam-binding/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Samples ](https://docs.cloud.google.com/storage/docs/samples)



#  Add conditional role binding Stay organized with collections  Save and categorize content based on your preferences. 

An example of how to set a startsWith condition with the client libraries.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Set and manage IAM policies on buckets](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions)



## Code sample

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    //! [native add bucket conditional iam binding]
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
    //! [native add bucket conditional iam binding]

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
    
      storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
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

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=storage). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
