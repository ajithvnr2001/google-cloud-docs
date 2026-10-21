---
url: https://docs.cloud.google.com/storage/docs/access-control/making-data-public/
title: Make data public \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:01:08.201911+00:00
---

# Make data public  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/access-control/making-data-public/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Make data public Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to make objects you own readable to everyone on the public internet and how to remove public access from your bucket. To learn how to access data that has been made public, see [Accessing Public Data](https://docs.cloud.google.com/storage/docs/access-public-data).

When an object is shared publicly, any user with knowledge of the object URI can access the object for as long as the object is public.

**Important:** You cannot publicly share an object if the bucket it's stored in is subject to [public access prevention](https://docs.cloud.google.com/storage/docs/public-access-prevention).

## Required roles

In order to get the required permissions for making objects publicly readable, ask your administrator to grant you the following roles for the bucket that contains the data you want to make public:

  * To make all objects in a bucket publicly readable: Storage Admin (`roles/storage.admin`)

  * To make individual objects publicly readable: Storage Object Admin (`roles/storage.objectAdmin`)

    * If you plan on using the Google Cloud console, you'll need the Storage Admin (`roles/storage.admin`) role instead of the Storage Object Admin role.
  * To remove public access from all objects in a bucket: Storage Admin (`roles/storage.admin`)




These roles contain the permissions required to make objects public. To see the exact permissions that are required, expand the **Required permissions** section:

#### Required permissions

  * `storage.buckets.get`
  * `storage.buckets.getIamPolicy`
  * `storage.buckets.setIamPolicy`
  * `storage.buckets.update`
  * `storage.objects.get`
  * `storage.objects.getIamPolicy`
  * `storage.objects.setIamPolicy`
  * `storage.objects.update`



The following permissions are only required for using the Google Cloud console to perform the tasks on this page:

  * `storage.buckets.list`
  * `storage.objects.list`



You might also be able to get these permissions with other [predefined roles](https://docs.cloud.google.com/iam/docs/understanding-roles) or [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles).

For instructions on granting roles on buckets, see [Set and manage IAM policies on buckets](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions).

## Make all objects in a bucket publicly readable

To make all objects in a bucket readable to everyone on the public internet, grant the principal `allUsers` the Storage Object Viewer (`roles/storage.objectViewer`) role on the bucket.

The Storage Object Viewer (`roles/storage.objectViewer`) role includes the `storage.objects.list` permission, which allows your users to list the objects in the bucket. For a less permissive role that only allows your users to get objects without listing them, grant the [Storage Legacy Object Reader (`roles/storage.legacyObjectReader`) role](https://docs.cloud.google.com/storage/docs/access-control/iam-roles#standard-roles) instead.

**Caution:** Making objects publicly accessible exposes both object data and object metadata to anyone on the internet, including editable and non-editable metadata. For example, objects encrypted with customer-managed encryption keys (CMEK) will have their Cloud KMS key resource exposed in the `kmsKeyName` metadata field, formatted as `projects/PROJECT_ID/locations/LOCATION/keyRings/KEY_RING/cryptoKeys/KEY_NAME`. To protect your data, ensure that your project IDs, key rings, and key names don't contain sensitive information if your bucket or objects are publicly accessible.

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the bucket that you want to make public.

  3. Select the **Permissions** tab near the top of the page.

  4. In the **Permissions** section, click the person_add **Grant access** button.

The _Grant access_ dialog appears.

  5. In the **New principals** field, enter `allUsers`.

  6. In the **Select a role** drop down, enter `Storage Object Viewer` in the filter box and select the **Storage Object Viewer** from the filtered results.

  7. Click **Save**.

  8. Click **Allow public access**.




Once public access has been granted, a **Copy URL** button appears for each object in the _public access_ column. You can click this button to get the public URL for the object. The public URL is different from the link you get from directly right-clicking an object. Both links provide access to an object, but the public URL works without the user having to sign into a user account. See [Request endpoints](https://docs.cloud.google.com/storage/docs/request-endpoints) for more information.

To learn how to get detailed error information about failed Cloud Storage operations in the Google Cloud console, see [Troubleshooting](https://docs.cloud.google.com/storage/docs/troubleshooting#trouble-console).

To learn how to resolve organization policy error and permission error, see [Troubleshoot making data public](https://docs.cloud.google.com/storage/docs/troubleshooting#make-data-public).

### Command line

**Note:** Cloud Shell provisions a temporary virtual machine. If you want to upload objects to Cloud Storage or download objects from Cloud Storage, use a local development environment.

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. In your development environment, run the [`buckets add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/add-iam-policy-binding) command:
         
         gcloud storage buckets add-iam-policy-binding gs://BUCKET_NAME --member=allUsers --role=roles/storage.objectViewer

Where `BUCKET_NAME` is the name of the bucket whose objects you want to make public. For example, `my-bucket`.




### Client libraries

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    namespace gcs = ::google::cloud::storage;
    using ::google::cloud::StatusOr;
    [](gcs::Client client, std::string const& bucket_name) {
      auto current_policy = client.GetNativeBucketIamPolicy(
          bucket_name, gcs::RequestedPolicyVersion(3));
      if (!current_policy) throw std::move(current_policy).status();
    
      current_policy->set_version(3);
      current_policy->bindings().emplace_back(
          gcs::NativeIamBinding("roles/storage.objectViewer", {"allUsers"}));
    
      auto updated =
          client.SetNativeBucketIamPolicy(bucket_name, *current_policy);
      if (!updated) throw std::move(updated).status();
    
      std::cout << "Policy successfully updated: " << *updated << "\n";
    }

### C#

For more information, see the [Cloud Storage C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    using Google.Apis.Storage.v1.Data;
    using [Google.Cloud.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html);
    using System;
    using System.Collections.Generic;
    
    public class MakeBucketPublicSample
    {
        public void MakeBucketPublic(string bucketName = "your-unique-bucket-name")
        {
            var storage = [StorageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html#Google_Cloud_Storage_V1_StorageClient_Create)();
    
            Policy policy = storage.GetBucketIamPolicy(bucketName);
    
            policy.Bindings.Add(new Policy.BindingsData
            {
                Role = "roles/storage.objectViewer",
                Members = new List<string> { "allUsers" }
            });
    
            storage.SetBucketIamPolicy(bucketName, policy);
            Console.WriteLine(bucketName + " is now public ");
        }
    }

### Go

For more information, see the [Cloud Storage Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/storage). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	"cloud.google.com/go/iam"
    	"cloud.google.com/go/iam/apiv1/iampb"
    	"cloud.google.com/go/storage"
    )
    
    // setBucketPublicIAM makes all objects in a bucket publicly readable.
    func setBucketPublicIAM(w io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), bucketName string) error {
    	// bucketName := "bucket-name"
    	ctx := context.Background()
    	client, err := storage.NewClient(ctx)
    	if err != nil {
    		return fmt.Errorf("storage.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	policy, err := client.[Bucket](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Bucket)(bucketName).[IAM](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketHandle_IAM)().[V3](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/iam/latest/index.html#cloud_google_com_go_iam_Handle_V3)().Policy(ctx)
    	if err != nil {
    		return fmt.Errorf("Bucket(%q).IAM().V3().Policy: %w", bucketName, err)
    	}
    	role := "roles/storage.objectViewer"
    	policy.Bindings = append(policy.Bindings, &iampb.Binding{
    		Role:    role,
    		Members: []string{iam.[AllUsers](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/iam/latest/index.html#cloud_google_com_go_iam_AllUsers_AllAuthenticatedUsers)},
    	})
    	if err := client.[Bucket](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Bucket)(bucketName).[IAM](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketHandle_IAM)().[V3](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/iam/latest/index.html#cloud_google_com_go_iam_Handle_V3)().SetPolicy(ctx, policy); err != nil {
    		return fmt.Errorf("Bucket(%q).IAM().SetPolicy: %w", bucketName, err)
    	}
    	fmt.Fprintf(w, "Bucket %v is now publicly readable\n", bucketName)
    	return nil
    }
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import com.google.cloud.[Identity](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.Identity.html);
    import com.google.cloud.[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    import com.google.cloud.storage.[StorageRoles](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageRoles.html);
    
    public class MakeBucketPublic {
      public static void makeBucketPublic([String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) projectId, [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) bucketName) {
        // The ID of your GCP project
        // String projectId = "your-project-id";
    
        // The ID of your GCS bucket
        // String bucketName = "your-unique-bucket-name";
    
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder().setProjectId(projectId).build().getService();
        [Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy.html) originalPolicy = storage.[getIamPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_getIamPolicy_java_lang_String_com_google_cloud_storage_Storage_BucketSourceOption____)(bucketName);
        storage.[setIamPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_setIamPolicy_java_lang_String_com_google_cloud_Policy_com_google_cloud_storage_Storage_BucketSourceOption____)(
            bucketName,
            originalPolicy.toBuilder()
                .addIdentity(StorageRoles.objectViewer(), Identity.allUsers()) // All users can view
                .build());
    
        System.out.println("Bucket " + bucketName + " is now publicly readable");
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
    
    async function makeBucketPublic() {
      await storage.bucket(bucketName).makePublic();
    
      console.log(`Bucket ${bucketName} is now publicly readable`);
    }
    
    makeBucketPublic().catch(console.error);

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Storage\StorageClient;
    
    /**
     * Update the specified bucket's IAM configuration to make it publicly accessible.
     *
     * @param string $bucketName The name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     */
    function set_bucket_public_iam(string $bucketName): void
    {
        $storage = new StorageClient();
        $bucket = $storage->bucket($bucketName);
    
        $policy = $bucket->iam()->policy(['requestedPolicyVersion' => 3]);
        $policy['version'] = 3;
    
        $role = 'roles/storage.objectViewer';
        $members = ['allUsers'];
    
        $policy['bindings'][] = [
            'role' => $role,
            'members' => $members
        ];
    
        $bucket->iam()->setPolicy($policy);
    
        printf('Bucket %s is now public', $bucketName);
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    from typing import List
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
    
    def set_bucket_public_iam(
        bucket_name: str = "your-bucket-name",
        members: List[str] = ["allUsers"],
    ):
        """Set a public IAM Policy to bucket"""
        # bucket_name = "your-bucket-name"
    
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
        bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(bucket_name)
    
        policy = bucket.get_iam_policy(requested_policy_version=3)
        policy.bindings.append(
            {"role": "roles/storage.objectViewer", "members": members}
        )
    
        bucket.set_iam_policy(policy)
    
        print(f"Bucket {bucket.name} is now publicly readable")
    
    

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    def set_bucket_public_iam bucket_name:
      # The ID of your GCS bucket
      # bucket_name = "your-unique-bucket-name"
    
      require "google/cloud/storage"
    
      storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
      bucket = storage.bucket bucket_name
    
      bucket.[policy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html) do |p|
        p.[add](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-PolicyV1.html) "roles/storage.objectViewer", "allUsers"
      end
    
      puts "Bucket #{bucket_name} is now publicly readable"
    end

### Rust
    
    
    use google_cloud_iam_v1::model::{Binding, GetPolicyOptions};
    use google_cloud_storage::client::StorageControl;
    
    pub async fn sample(client: &StorageControl, bucket_id: &str) -> anyhow::Result<()> {
        let mut policy = client
            .get_iam_policy()
            .set_resource(format!("projects/_/buckets/{bucket_id}"))
            .set_options(GetPolicyOptions::new().set_requested_policy_version(3))
            .send()
            .await?;
        policy.version = 3;
        policy.bindings.push(
            Binding::new()
                .set_role("roles/storage.objectViewer")
                .set_members(["allUsers"]),
        );
        let updated_policy = client
            .set_iam_policy()
            .set_resource(format!("projects/_/buckets/{bucket_id}"))
            .set_policy(policy)
            .send()
            .await?;
        println!(
            "Successfully set public IAM policy for bucket {}",
            bucket_id
        );
        println!("The updated policy is: {:?}", updated_policy);
        Ok(())
    }

### Terraform

You can use a [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/storage_bucket_iam) to make all objects in a bucket public.
    
    
    # Make bucket public
    resource "google_storage_bucket_iam_member" "member" {
      provider = google
      bucket   = google_storage_bucket.default.name
      role     = "roles/storage.objectViewer"
      member   = "allUsers"
    }

### REST APIs

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Create a JSON file that contains the following information:
         
         {
           "bindings":[
             {
               "role": "roles/storage.objectViewer",
               "members":["allUsers"]
             }
           ]
         }

  3. Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with a [`PUT` Bucket](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/setIamPolicy) request:
         
         curl -X PUT --data-binary @JSON_FILE_NAME \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "Content-Type: application/json" \
           "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME/iam"

Where:

     * `JSON_FILE_NAME` is the path for the file that you created in Step 2.
     * `BUCKET_NAME` is the name of the bucket whose objects you want to make public. For example, `my-bucket`.



### XML API

Making all objects in a bucket publicly readable is not supported by the XML API. Use the Google Cloud console or `gcloud storage`.

## Make a portion of a bucket publicly readable

**Important:** To complete this task, the target bucket must use [uniform bucket-level access](https://docs.cloud.google.com/storage/docs/uniform-bucket-level-access). If uniform bucket-level access is disabled for the bucket, you can [enable it](https://docs.cloud.google.com/storage/docs/using-uniform-bucket-level-access#set), or you can use [access control lists (ACLs)](https://docs.cloud.google.com/storage/docs/access-control/lists) instead to grant access to individual objects.

Use a [managed folder](https://docs.cloud.google.com/storage/docs/managed-folders) to control access to objects whose name prefix match the name of the managed folder. For example, a managed folder named `my-folder` can be used to control access to objects named `my-folder/cats.jpg` and `my-folder/dogs.jpg`.

To make such objects publicly accessible, first create the managed folder, and then set an IAM policy on the folder that grants `allUsers` the Storage Object Viewer (`roles/storage.objectViewer`) role:

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. Click the name of the bucket that contains the objects you want to make public.

  3. Create a folder, using the following steps:

     1. Click the **Create folder** button.

     2. Enter the **Name** for the folder. Once the folder is converted to a managed folder, objects whose name start with this name will be subject to IAM roles set on the folder.

     3. Click **Create**.

  4. Convert the folder to a managed folder, using the following steps:

     1. In the pane that shows the bucket's contents, find the name of the folder you created, and click the **More options** icon more_vert.

     2. Click **Edit access**.

     3. In the window that appears, click **Enable**.

  5. Add an IAM policy to the folder that grants `allUsers` the Storage Object Viewer (`roles/storage.objectViewer`) role, using the following steps:

     1. If the **Permissions** pane for your managed folder isn't already open, click the **More options** icon more_vert for the managed folder, and then click **Edit access**.

     2. In the **Permissions** pane, click the person_add **Add principal** button.

     3. In the **New principals** field, enter `allUsers`.

     4. In the **Select a role** drop down, enter `Storage Object Viewer` in the filter box, and select **Storage Object Viewer** from the filtered results.

     5. Click **Save**.

     6. Click **Allow public access**.




Once public access has been granted, a **Copy URL** button appears for each applicable object in the _public access_ column. You can click this button to get the public URL for the object. The public URL is different from the link you get from directly right-clicking an object. Both links provide access to an object, but the public URL works without the user having to sign into a user account. See [Request endpoints](https://docs.cloud.google.com/storage/docs/request-endpoints) for more information.

To learn how to get detailed error information about failed Cloud Storage operations in the Google Cloud console, see [Troubleshooting](https://docs.cloud.google.com/storage/docs/troubleshooting#trouble-console).

To learn how to resolve organization policy error and permission error, see [Troubleshoot making data public](https://docs.cloud.google.com/storage/docs/troubleshooting#make-data-public).

### Command line

**Note:** Cloud Shell provisions a temporary virtual machine. If you want to upload objects to Cloud Storage or download objects from Cloud Storage, use a local development environment.

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. In your development environment, create a managed folder using the [`gcloud storage managed-folders create` command](https://docs.cloud.google.com/sdk/gcloud/reference/storage/managed-folders/create):
         
         gcloud storage managed-folders create gs://BUCKET_NAME/MANAGED_FOLDER_NAME/

Where:

     * `BUCKET_NAME` is the name of the bucket in which you want to create a managed folder. For example, `my-bucket`.

     * `MANAGED_FOLDER_NAME` is the name of the managed folder you want to create. For example, `my-managed-folder`.

  3. In your development environment, add `allUsers` to the managed folder's IAM policy using the [`gcloud storage managed-folders add-iam-policy-binding` command](https://docs.cloud.google.com/sdk/gcloud/reference/storage/managed-folders/add-iam-policy-binding):
         
         gcloud storage managed-folders add-iam-policy-binding gs://BUCKET_NAME/MANAGED_FOLDER_NAME --member=allUsers --role=roles/storage.objectViewer

Where:

     * `BUCKET_NAME` is the name of the bucket containing the managed folder you're adding the IAM policy to. For example, `my-bucket`.
     * `MANAGED_FOLDER_NAME` is the name of the managed folder that you want to add public access to. For example, `my-managed-folder`.



### REST APIs

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Create a JSON file that contains the following information:
         
         {
           "name": "MANAGED_FOLDER_NAME"
         }

Where `MANAGED_FOLDER_NAME` is the name of the managed folder you want to create. For example, `my-managed-folder`.

  3. Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with a [`Insert ManagedFolder`](https://docs.cloud.google.com/storage/docs/json_api/v1/managedFolder/insert) request:
         
         curl -X POST --data-binary @JSON_FILE_NAME \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "Content-Type: application/json" \
           "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME/managedFolders"

Where:

     * `JSON_FILE_NAME` is the path for the file that you created in the previous step.
     * `BUCKET_NAME` is the name of the bucket in which you want to create a managed folder. For example, `my-bucket`.
  4. Create a JSON file that contains the following information:
         
         {
           "bindings":[
             {
               "role": "roles/storage.objectViewer",
               "members":["allUsers"]
             }
           ]
         }

  5. Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with a [`setIamPolicy` ManagedFolder](https://docs.cloud.google.com/storage/docs/json_api/v1/managedFolder/setIamPolicy) request:
         
         curl -X PUT --data-binary @JSON_FILE_NAME \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "Content-Type: application/json" \
           "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME/managedFolders/MANAGED_FOLDER_NAME/iam"

Where:

     * `JSON_FILE_NAME` is the path for the file that you created in the previous step.
     * `BUCKET_NAME` is the name of the bucket containing the managed folder you're adding the IAM policy to. For example, `my-bucket`.
     * `MANAGED_FOLDER_NAME` is the name of the managed folder you're adding the IAM policy to. For example, `my-managed-folder`.



### XML API

The XML API does not support working with managed folders. Use a different tool, such as the Google Cloud console, or set ACLs on individual objects using [`Set Object ACL`](https://docs.cloud.google.com/storage/docs/xml-api/put-object-acls) requests. The following is an example ACL file the would grant `allUsers` access to an object:
    
    
    <AccessControlList>
      <Entries>
        <Entry>
          <Scope type="AllUsers"/>
          <Permission>READ</Permission>
        </Entry>
      </Entries>
    </AccessControlList>

## Remove public access for all objects within a bucket

To remove public access for all objects within a bucket, remove the IAM policy that grants `allUsers` the Storage Object Viewer (`roles/storage.objectViewer`) role:

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the bucket you want to remove public access from.

  3. Select the **Permissions** tab.

The IAM policy that applies to the bucket appears in the **Permissions** section.

  4. In the **View by principals** tab, select the checkbox for the `allUsers` principal you're removing.

  5. Click the **\- Remove access** button.

  6. In the overlay window that appears, click **Confirm**.




To learn how to get detailed error information about failed Cloud Storage operations in the Google Cloud console, see [Troubleshooting](https://docs.cloud.google.com/storage/docs/troubleshooting#trouble-console).

### Command line

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. In your development environment, run the [`buckets remove-iam-policy-binding` command](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/remove-iam-policy-binding):



    
    
    gcloud storage buckets remove-iam-policy-binding  gs://BUCKET_NAME --member=allUsers --role=roles/storage.objectViewer

Where `BUCKET_NAME` is the name of the bucket you are revoking access to. For example, `my-bucket`.

### REST APIs

### JSON

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Get the existing policy applied to your bucket. To do so, use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with a [`GET getIamPolicy`](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/getIamPolicy) request:
         
         curl -X GET \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME/iam"

Where `BUCKET_NAME` is the name of the bucket whose IAM policy you want to view. For example, `my-bucket`.

  3. Create a JSON file that contains the policy you retrieved in the previous step and edit the file to remove the binding of the `allUsers` principal from the policy.

  4. Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with a [`PUT setIamPolicy`](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/setIamPolicy) request:
         
         curl -X PUT --data-binary @JSON_FILE_NAME \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME/iam"

Where:

     * `JSON_FILE_NAME` is the path for the file that you created in Step 3.

     * `BUCKET_NAME` is the name of the bucket from which you want to remove access. For example, `my-bucket`.




**Important:** It typically takes about a minute for revoking access to take effect. In some cases it may take longer. If you remove a user's access, this change is immediately reflected in the metadata; however, the user may still have access to the object for a short period of time.

## What's next

  * [Access data that has been made public](https://docs.cloud.google.com/storage/docs/access-public-data).
  * Learn about more [access control options](https://docs.cloud.google.com/storage/docs/access-control) for your buckets and objects.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
