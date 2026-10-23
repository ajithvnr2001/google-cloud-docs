---
url: https://docs.cloud.google.com/storage/docs/access-control/using-iam-for-managed-folders/
title: Set and manage IAM policies on managed folders \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:47.302136+00:00
---

# Set and manage IAM policies on managed folders  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/access-control/using-iam-for-managed-folders/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Set and manage IAM policies on managed folders Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to set [Identity and Access Management (IAM) policies](https://docs.cloud.google.com/iam/docs/policies) on [managed folders](https://docs.cloud.google.com/storage/docs/managed-folders), so you can get fine-grained access control over specific groups of objects within a bucket.

If you're looking for other methods of access control, see the following resources:

  * To learn about how to control access to whole buckets and the objects within them, see [Set and manage IAM policies on buckets](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions).

  * For an alternative way to control access to individual objects in your buckets, see [Access Control Lists](https://docs.cloud.google.com/storage/docs/access-control/lists).

  * For more information about controlling access to Cloud Storage resources, read [Overview of Access Control](https://docs.cloud.google.com/storage/docs/access-control).




## Required roles

To get the permissions that you need to set and manage IAM policies for managed folders, ask your administrator to grant you the Storage Folder Admin (`roles/storage.folderAdmin`) IAM role for the bucket that contains the managed folders.

This role contain the following permissions, which are required to set and manage IAM policies for managed folders:

  * `storage.managedFolders.getIamPolicy`

  * `storage.managedFolders.setIamPolicy`




You can also get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles).

For information about granting roles for buckets, see [Set and manage IAM policies on buckets](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions).

## Set an IAM policy on a managed folder

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the bucket that contains the managed folder you want to set an IAM policy on.

  3. In the **Bucket details** page, click the **More options** icon more_vert in the **Folder browser** pane next to the managed folder you want to set an IAM policy on.

If you want to control access within a folder or a simulated folder, follow the steps in [Create a managed folder](https://docs.cloud.google.com/storage/docs/creating-managing-managed-folders#create) to enable management on the folder or simulated folder.

  4. Click **Edit access**.

  5. In the **Permissions for` MANAGED_FOLDER_NAME`** pane, click **Add principal** person_add.

  6. In the **New principals** field, enter the principal for which you want to grant access. For more information about principals you can include, see [Principal identifiers](https://docs.cloud.google.com/iam/docs/principal-identifiers).

  7. In the **Assign roles** section, use the **Select a role** drop-down to specify the level of access you want to grant to the principal.

  8. Click **Save**.




### Command line

  1. Create a JSON file that contains the following information:
         
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

     * `PRINCIPAL_IDENTIFIER` identifies who you are granting managed folder access to. For example, `user:jeffersonloveshiking@gmail.com`. For a list of principal identifier formats, see [Principal identifiers](https://docs.cloud.google.com/iam/docs/principal-identifiers).

  2. Use the [`gcloud storage managed-folders set-iam-policy` command](https://docs.cloud.google.com/sdk/gcloud/reference/storage/managed-folders/set-iam-policy):
         
         gcloud storage managed-folders set-iam-policy gs://BUCKET_NAME/MANAGED_FOLDER_NAME POLICY_FILE

Where:

     * `BUCKET_NAME` is the name of the bucket that contains the managed folder to which you want to apply the IAM policy. For example, `my-bucket`.

     * `MANAGED_FOLDER_NAME` is the name of the managed folder to which you want to apply the IAM policy. For example, `my-managed-folder/`.

     * `POLICY_FILE` is the path to the JSON file you created in step 1.




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

     * `PRINCIPAL_IDENTIFIER` identifies who you are granting managed folder access to. For example, `user:jeffersonloveshiking@gmail.com`. For a list of principal identifier formats, see [Principal identifiers](https://docs.cloud.google.com/iam/docs/principal-identifiers).

  3. Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with a [`PUT setIamPolicy`](https://docs.cloud.google.com/storage/docs/json_api/v1/managedFolder/setIamPolicy) request:
         
         curl -X PUT --data-binary @POLICY_FILE \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "Content-Type: application/json" \
           "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME/managedFolders/MANAGED_FOLDER_NAME/iam"

Where:

     * `POLICY_FILE` is the path to the JSON policy file that you created in the previous step.

     * `BUCKET_NAME` is the name of the bucket that contains the managed folder to which you want to apply the IAM policy. For example, `my-bucket`.

     * `MANAGED_FOLDER_NAME` is the name of the managed folder to which you want to give the principal access. For example, `my-managed-folder/`.




## View the IAM policy for a managed folder

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the bucket that contains the managed folder for which you want to view IAM policies.

  3. In the **Bucket details** page, click the **More options** icon more_vert in the **Folder browser** pane next to the managed folder for which you want to view the IAM policy.

  4. Click **Edit access**.




The **Permissions for` FOLDER_NAME`** pane displays the permissions on the managed folder, including the principal, role, inherited roles, and IAM conditions.

### Command line

Use the [`gcloud storage managed-folder get-iam-policy` command](https://docs.cloud.google.com/sdk/gcloud/reference/storage/managed-folders/get-iam-policy):
    
    
    gcloud storage managed-folders get-iam-policy gs://BUCKET_NAME/MANAGED_FOLDER_NAME

Where:

  * `BUCKET_NAME` is the name of the bucket that contains the managed folder whose IAM policy you want to view. For example, `my-bucket`.

  * `MANAGED_FOLDER_NAME` is the name of the managed folder whose IAM policy you want to view. For example, `my-managed-folder/`.




### REST APIs

### JSON

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with a [`GET getIamPolicy`](https://docs.cloud.google.com/storage/docs/json_api/v1/managedFolder/getIamPolicy) request:
         
         curl -X GET \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME/managedFolders/MANAGED_FOLDER_NAME/iam"

Where:

     * `BUCKET_NAME` is the name of the bucket that contains the managed folder whose IAM policy you want to view. For example, `my-bucket`.

     * `MANAGED_FOLDER_NAME` is the name of the managed folder whose IAM policy you want to view. For example, `my-managed-folder/`.




## Remove a principal from a managed folder policy

**Note:** You can't remove principals from inherited IAM policies by using the following steps. To remove a principal from an inherited policy, identify the resource that has the policy and remove the principal from the resource. For example, a principal might have the Storage Object User (`roles/storage.objectUser`) role on the bucket containing the managed folder. In order to remove the principal, you must [remove them from the bucket-level policy](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions#bucket-remove).

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the bucket that contains the managed folder for which you want to view IAM policies.

  3. In the **Bucket details** page, click the **More options** icon more_vert in the **Folder browser** pane next to the managed folder for which you want to remove a principal.

  4. Click **Edit access**.

  5. In the **Permissions for` FOLDER_NAME`** pane, enter the name of the principal in the **Filter** field.

  6. Click the **Delete** icon delete to delete the principal.




Cloud Storage deletes the principal from your managed folder.

### Command line

Use the [`gcloud storage managed-folder remove-iam-policy-binding` command](https://docs.cloud.google.com/sdk/gcloud/reference/storage/managed-folders/remove-iam-policy-binding):
    
    
    gcloud storage managed-folders remove-iam-policy-binding  gs://BUCKET_NAME/MANAGED_FOLDER_NAME --member=PRINCIPAL_IDENTIFIER --role=IAM_ROLE

Where:

  * `BUCKET_NAME` is the name of the bucket that contains the managed folder you are revoking access to. For example, `my-bucket`.

  * `MANAGED_FOLDER_NAME` is the name of the managed folder whose IAM policy you want to remove. For example, `my-managed-folder/`.

  * `PRINCIPAL_IDENTIFIER` identifies who you are revoking access from. For example, `user:jeffersonloveshiking@gmail.com`. For a list of principal identifier formats, see [Principal identifiers](https://docs.cloud.google.com/iam/docs/principal-identifiers).

  * `IAM_ROLE` is the [IAM role](https://docs.cloud.google.com/storage/docs/access-control/iam-roles) you are revoking. For example, `roles/storage.objectViewer`.




### REST APIs

### JSON

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Get the existing policy applied to your managed folder. To do so, use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with a [`GET getIamPolicy`](https://docs.cloud.google.com/storage/docs/json_api/v1/managedFolder/getIamPolicy) request:
         
         curl -X GET \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME/managedFolders/MANAGED_FOLDER_NAME/iam"

Where:

     * `BUCKET_NAME` is the name of the bucket that contains the managed folder you are revoking access to. For example, `my-bucket`.

     * `MANAGED_FOLDER_NAME` is the name of the managed folder whose IAM policy you want to remove. For example, `my-managed-folder/`.

  3. Create a JSON file that contains the policy you retrieved in the previous step.

  4. Edit the JSON file to remove the principal from the policy.

  5. Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with a [`PUT setIamPolicy`](https://docs.cloud.google.com/storage/docs/json_api/v1/managedFolder/setIamPolicy) request:
         
         curl -X PUT --data-binary @JSON_FILE_NAME \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME/managedFolders/MANAGED_FOLDER_NAME/iam"

Where:

     * `JSON_FILE_NAME` is the path for the file that you created in Step 3.

     * `BUCKET_NAME` is the name of the bucket that contains the managed folder you are revoking access to. For example, `my-bucket`.

     * `MANAGED_FOLDER_NAME` is the name of the managed folder whose IAM policy you want to remove. For example, `my-managed-folder/`.




## Use IAM Conditions on managed folders

The following sections show you how to add and remove [IAM Conditions](https://docs.cloud.google.com/iam/docs/conditions-overview) on your managed folders. To view the IAM Conditions for your managed folders, see Viewing the IAM policy for a managed folder. For more information about using IAM Conditions with Cloud Storage, see [Conditions](https://docs.cloud.google.com/storage/docs/access-control/iam#conditions).

Managed folders can be specified as a resource in IAM allow policy conditions, but they can't be specified as a resource in IAM deny policy conditions. Denial conditions only recognize resource tag functions, and tags can't be attached to managed folders.

You must enable uniform bucket-level access on the bucket before adding conditions to managed folders.

### Set a new condition on a managed folder

### Command line

  1. Create a JSON or YAML file that defines the condition, including the `title` of the condition, the [attribute-based](https://docs.cloud.google.com/iam/docs/conditions-overview#attributes) logic `expression` for the condition, and, optionally, a `description` for the condition.

Note that Cloud Storage only supports the [date/time](https://docs.cloud.google.com/iam/docs/conditions-attribute-reference#date-time), [resource type](https://docs.cloud.google.com/iam/docs/conditions-attribute-reference#resourcetype_attribute), and [resource name](https://docs.cloud.google.com/iam/docs/conditions-attribute-reference#resourcename_attribute) attributes in the `expression`.

  2. Use the [`gcloud storage managed-folders add-iam-policy-binding` command](https://docs.cloud.google.com/sdk/gcloud/reference/storage/managed-folders/add-iam-policy-binding) with the `--condition-from-file` flag:



    
    
    gcloud storage managed-folders add-iam-policy-binding  gs://BUCKET_NAME/MANAGED_FOLDER_NAME --member=PRINCIPAL_IDENTIFIER --role=IAM_ROLE --condition-from-file=CONDITION_FILE

Where:

  * `BUCKET_NAME` is the name of the bucket that contains the managed folder to which you are granting the principal access. For example, `my-bucket`.

  * `MANAGED_FOLDER_NAME` is the name of managed folder to which you are granting the principal access. For example, `my-managed-folder/`.

  * `PRINCIPAL_IDENTIFIER` identifies who the condition applies to. For example, `user:jeffersonloveshiking@gmail.com`. For a list of principal identifier formats, see [Principal identifiers](https://docs.cloud.google.com/iam/docs/principal-identifiers).

  * `IAM_ROLE` is the [IAM role](https://docs.cloud.google.com/storage/docs/access-control/iam-roles) you are granting to the principal. For example, `roles/storage.objectViewer`.

  * `CONDITION_FILE` is the file you created in the previous step.




Alternatively, you can include the condition directly in the command with the `--condition` flag instead of the `--condition-from-file` flag.

### REST APIs

### JSON

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use a [`GET getIamPolicy`](https://docs.cloud.google.com/storage/docs/json_api/v1/managedFolder/getIamPolicy) request to save the managed folder's IAM policy to a temporary JSON file:
         
         curl \
         'https://storage.googleapis.com/storage/v1/b/BUCKET_NAME/managedFolders/MANAGED_FOLDER_NAMEiam' \
         --header 'Authorization: Bearer $(gcloud auth print-access-token)' > tmp-policy.json

Where:

     * `BUCKET_NAME` is the name of the bucket that contains the managed folder you want to set an IAM Condition on.

     * `MANAGED_FOLDER_NAME` is the name of the managed folder you want to set an IAM Condition on.

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

     * `VERSION` is the [IAM policy version](https://docs.cloud.google.com/iam/docs/policies#versions), which is required to be 3 for managed folders with IAM Conditions.

     * `IAM_ROLE` is the role to which the condition applies. For example, `roles/storage.objectViewer`.

     * `PRINCIPAL_IDENTIFIER` identifies who the condition applies to. For example, `user:jeffersonloveshiking@gmail.com`. For a list of principal identifier formats, see [Principal identifiers](https://docs.cloud.google.com/iam/docs/principal-identifiers).

     * `TITLE` is the title of the condition. For example, `expires in 2019`.

     * `DESCRIPTION` is an optional description of the condition. For example, `Permission revoked on New Year's`.

     * `EXPRESSION` is an [attribute-based](https://docs.cloud.google.com/iam/docs/conditions-overview#attributes) logic expression. For example, `request.time < timestamp(\"2019-01-01T00:00:00Z\")`. For more examples of expressions, see the [Conditions attribute reference](https://docs.cloud.google.com/iam/docs/conditions-attribute-reference). Cloud Storage only supports the [date/time](https://docs.cloud.google.com/iam/docs/conditions-attribute-reference#date-time), [resource type](https://docs.cloud.google.com/iam/docs/conditions-attribute-reference#resourcetype_attribute), and [resource name](https://docs.cloud.google.com/iam/docs/conditions-attribute-reference#resourcename_attribute) attributes.

Don't modify `ETAG`.

  4. Use a [`PUT setIamPolicy`](https://docs.cloud.google.com/storage/docs/json_api/v1/managedFolder/setIamPolicy) request to set the modified IAM policy on the bucket:
         
         curl -X PUT --data-binary @tmp-policy.json \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME/managedFoldersMANAGED_FOLDER_NAME/iam"

Where:

     * `BUCKET_NAME` is the name of the bucket that contains the managed folder you want to set an IAM Condition on.

     * `MANAGED_FOLDER_NAME` is the name of the managed folder you want to set an IAM Condition on.




### Remove a condition from a managed folder

### Command line

  1. Use the [`gcloud storage managed-folders get-iam-policy` command](https://docs.cloud.google.com/sdk/gcloud/reference/storage/managed-folders/get-iam-policy) to save the managed folder's IAM policy to a temporary JSON file.
         
         gcloud storage managed-folders get-iam-policy gs://BUCKET_NAME/MANAGED_FOLDER_NAME > tmp-policy.json

  2. Edit the `tmp-policy.json` file in a text editor to remove conditions from the IAM policy.

  3. Use the `gcloud storage managed-folders set-iam-policy` command to set the modified IAM policy on the managed folder.
         
         gcloud storage managed-folders set-iam-policy gs://BUCKET_NAME/MANAGED_FOLDER_NAME tmp-policy.json




### REST APIs

### JSON

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use a [`GET getIamPolicy`](https://docs.cloud.google.com/storage/docs/json_api/v1/managedFolder/getIamPolicy) request to save the managed folder's IAM policy to a temporary JSON file:
         
         curl \
         'https://storage.googleapis.com/storage/v1/b/BUCKET_NAME/managedFolders/MANAGED_FOLDER_NAMEiam' \
         --header 'Authorization: Bearer $(gcloud auth print-access-token)' > tmp-policy.json

Where:

     * `BUCKET_NAME` is the name of the bucket that contains the managed folder you are changing access to. For example, `my-bucket`.

     * `MANAGED_FOLDER_NAME` is the name of the managed folder you are changing access to. For example, `my-managed-folder/`.

  3. Edit the `tmp-policy.json` file in a text editor to remove conditions from the IAM policy.

  4. Use a [`PUT setIamPolicy`](https://docs.cloud.google.com/storage/docs/json_api/v1/managedFolder/setIamPolicy) request to set the modified IAM policy on the managed folder:
         
         curl -X PUT --data-binary @tmp-policy.json \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME/managedFolders/MANAGED_FOLDER_NAMEiam"

Where:

     * `BUCKET_NAME` is the name of the bucket that contains the managed folder you are changing access to. For example, `my-bucket`.

     * `MANAGED_FOLDER_NAME` is the name of the managed folder you are changing access to. For example, `my-managed-folder/`.




## Use IAM with projects

See [Manage access to projects, managed folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) for guides about granting and revoking IAM roles at the project level and above.

## Best practices

You should set the minimum role possible that gives the principal the required access. For example, if a team member only needs to view the managed folders in a bucket, grant them the Storage Object Admin (`roles/storage.objectAdmin`) role instead of the Storage Folder Admin (`roles/storage.folderAdmin`) role. Similarly, if the team member needs full control of the managed folders in a bucket, grant them the Storage Folder Admin (`roles/storage.folderAdmin`) role instead of the Storage Admin (`roles/storage.admin`) role.

## What's next

  * Learn how to [publicly share your data](https://docs.cloud.google.com/storage/docs/access-control/making-data-public).

  * See specific [Sharing and collaboration examples](https://docs.cloud.google.com/storage/docs/collaboration).

  * Learn about [best practices when using IAM](https://docs.cloud.google.com/storage/docs/access-control#best-practices).

  * To troubleshoot failed operations related to IAM roles and permissions, see [Troubleshooting](https://docs.cloud.google.com/storage/docs/troubleshooting).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
