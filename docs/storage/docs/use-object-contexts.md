---
url: https://docs.cloud.google.com/storage/docs/use-object-contexts/
title: Use object contexts \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:26:53.311880+00:00
---

# Use object contexts  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/use-object-contexts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Use object contexts Stay organized with collections  Save and categorize content based on your preferences. 

Object contexts let you attach custom key-value pairs to Cloud Storage objects. You can use these contexts to classify data, track processing workflows, and enrich metadata. Attached contexts persist when you copy, compose, or restore objects.

This document shows you how to attach and manage contexts on Cloud Storage objects. For background information, see [Object contexts](https://docs.cloud.google.com/storage/docs/object-contexts).

## Get the required roles

To get the permissions that you need to create and manage object contexts, ask your administrator to grant you the following IAM roles on the object: 

  * Create objects with contexts: [Storage Object Creator ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectCreator) (`roles/storage.objectCreator`) 
  * Attach, update, view, and delete contexts from objects, and view full context representations (including extended data): [Storage Object User ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectUser) (`roles/storage.objectUser`) 
  * View context keys and values: [Storage Object Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectViewer) (`roles/storage.objectViewer`) 
  * Drop object contexts during rewrite, copy, and compose operations: [Storage Legacy Object Owner ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyObjectOwner) (`roles/storage.legacyObjectOwner`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to create and manage object contexts. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create and manage object contexts:

  * Create an object with object contexts: 
    * `storage.objects.create`
    * `storage.objects.createContext`
  * Attach, update, and delete object contexts: 
    * `storage.objects.update`
    * `storage.objects.createContext`
    * `storage.objects.updateContext`
    * `storage.objects.deleteContext`
  * Drop object contexts: `storage.objects.dropContexts`
  * View object contexts: 
    * `storage.objects.get`
    * `storage.objects.list`
  * View the full context of an object, including extended data ([Preview](https://docs.cloud.google.com/products#product-launch-stages)): `storage.objects.viewFullContext`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Naming requirements for key-value pairs

Both keys and values for custom contexts must meet the following requirements:

  * Must be between 1 and 256 characters, inclusive.

  * Must begin with an alphanumeric character.

  * Must be a valid UTF-8 character. Most UTF-8 characters are supported, except for the following characters:

    * Single quote (`'`)

    * Double quote (`"`)

    * Backslash (`\`)

    * Forward slash (`/`)

  * Context keys starting with the prefix `google:` (for example, `google:annotation:face-detector-v1`) are reserved for Google-generated contexts. You can't create new contexts with the `google:` prefix or modify their values. If you attempt to do so, Cloud Storage returns an `INVALID_ARGUMENT` error. To remove contexts with the `google:` prefix, you must discard them by using the `dropContextGroups` parameter during a rewrite operation.




## Attach contexts to new objects

Attach contexts to objects when you upload new objects to Cloud Storage buckets. Each context consists of a key and a value.

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. [Upload the object](https://docs.cloud.google.com/storage/docs/uploads).

  3. Follow the steps to attach contexts to the object.




### Command line

To attach contexts when you [upload objects](https://docs.cloud.google.com/storage/docs/uploading-objects#upload-object-cli) with the [`gcloud storage cp`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/cp) command, use the `--custom-contexts` flag:
    
    
    gcloud storage cp OBJECT_LOCATION gs://DESTINATION_BUCKET_NAME --custom-contexts=KEY=VALUE,...

Where:

  * `OBJECT_LOCATION` is the local path to your object. For example, `Desktop/employees.txt`.
  * `DESTINATION_BUCKET_NAME` is the name of the bucket to which you are uploading your object. For example, `my-bucket`.
  * `KEY` is the context key to attach to an object. For example, `Department`. You can specify multiple key-value pairs separated by commas.
  * `VALUE` is the value to associate with the context key. For example, `Human resources`.



Alternatively, create a JSON file that contains the contexts you want to attach to the objects, and use the `--custom-contexts-file` flag:
    
    
      {
        "KEY": {
          "value": "VALUE"
        },
        ...
      }

Where:

  * `KEY` is the context key to attach to an object. For example, `Department`. You can specify multiple key-value pairs.
  * `VALUE` is the value to associate with the context key. For example, `Human resources`.



To attach contexts when you [upload directories](https://docs.cloud.google.com/storage/docs/uploading-objects#upload-directory-cli) with the [`gcloud storage rsync`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/rsync) command, use the `--custom-contexts` flag or the `--custom-contexts-file` flag:
    
    
    gcloud storage rsync DIRECTORY_LOCATION gs://DESTINATION_BUCKET_NAME --recursive --custom-contexts=KEY=VALUE,...

Where:

  * `DIRECTORY_LOCATION` is the local path to your directory. For example, `~/my_directory`.
  * `DESTINATION_BUCKET_NAME` is the name of the bucket to which you are uploading your directory. For example, `my-bucket`.
  * `KEY` is the context key to attach to objects. For example, `Department`. You can specify multiple key-value pairs separated by commas.
  * `VALUE` is the value to associate with the context key. For example, `Human resources`.



### JSON API

To attach contexts to objects when you upload new objects, use _any_ of the following methods:

  * [Multipart uploads](https://docs.cloud.google.com/storage/docs/uploading-objects#json-api-multipart-upload)

  * [Resumable uploads](https://docs.cloud.google.com/storage/docs/performing-resumable-uploads#json-api)




As part of the object metadata in JSON format, include the `contexts` field:
    
    
      {
        "contexts": {
          "custom": {
            "KEY": {
              "value": "VALUE"
            },
            ...
          }
        }
      }

Where:

  * `KEY` is the context key to attach to an object. For example, `Department`. You can specify multiple key-value pairs in the `custom` object.
  * `VALUE` is the value to associate with the context key. For example, `Human resources`.



## Attach or modify contexts on an existing object

You can attach new contexts to objects or update existing contexts in Cloud Storage buckets.

Only Google services, such as object enrichment jobs, can generate and attach contexts with [extended data](https://docs.cloud.google.com/storage/docs/object-contexts#extended-data), which use the reserved `google:` key prefix. You can't attach extended data to user-defined contexts, and you can't create or modify context keys that start with the `google:` prefix. If you attempt to create or modify `google:` keys, Cloud Storage returns an `INVALID_ARGUMENT` error.

If an existing context includes extended data, Cloud Storage retains that context on the updated object during update and patch operations. Setting a context value to `null` only deletes contexts that don't have extended data. To view extended data, see View full object context. To remove a context with extended data, including contexts with the `google:` prefix, you must discard it by using the `dropContextGroups` parameter during a rewrite operation.

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the bucket containing the object.

  3. Navigate to the object, and then click more_vert **Open object overflow menu**.

  4. Click **Edit contexts**.

  5. In the **Edit contexts** panel, do any of the following:

     * Add a new object context:

       1. Click **Add a custom context**.

       2. In the **Object context key** and **Object context value** fields, enter a new key-value pair.

       3. Click **Done**.

       4. Optional: To add additional object contexts, click **Add a custom context** , repeat the previous steps, and then click **Save**.

     * Edit an object context:

       1. Click the object context.

       2. Update the **Object context key** field, the **Object context value** field, or both.

       3. Click **Done** , and then click **Save**.

     * Delete an object context:

Click delete **Delete** , and then click **Save**.




### Command line

Use the [`gcloud storage objects update`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/objects/update) command:
    
    
    gcloud storage objects update gs://BUCKET_NAME/OBJECT_NAME CUSTOM_CONTEXTS_FLAG

Where:

  * `BUCKET_NAME` is the name of the bucket that contains the object for which you want to edit context. For example, `my-bucket`.
  * `OBJECT_NAME` is the name of the object. For example, `employees.txt`.
  * `CUSTOM_CONTEXTS_FLAG` is _any_ of the following flags:

    * To replace all existing contexts, use `--custom-contexts=KEY=VALUE,...` or `--custom-contexts-file=CUSTOM_CONTEXTS_FILE`

Where:

      * `KEY` is the context key to attach to an object. For example, `Department`. You can specify multiple key-value pairs separated by commas.
      * `VALUE` is the value to associate with the context key. For example, `Human resources`.
      * `CUSTOM_CONTEXTS_FILE` is the path to the JSON or YAML file that contains the contexts you want to attach to the object.
    * To delete all existing contexts, use the `--clear-custom-contexts` flag.

    * To add, modify, or delete individual contexts, use a combination of `--update-custom-contexts=KEY=VALUE,...` and `--remove-custom-contexts=KEY,...`

Where:

      * `KEY` is the context key that you want to attach to or delete from an object. For example, `Department`.
      * `VALUE` is the value to associate with the context key that you want to attach to or delete from an object. For example, `Human resources`.



If successful, the response looks like the following example:
    
    
    Patching gs://my-bucket/employees.txt#1560574162144861...
      Completed 1

**Note:** Modifying an object context updates the object's [metageneration number](https://docs.cloud.google.com/storage/docs/metadata#generation-number) and [ETag](https://docs.cloud.google.com/storage/docs/metadata#etags). Adding, updating, or removing a context doesn't create a new object version.

### Client libraries

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import com.google.cloud.storage.[Blob](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.html);
    import com.google.cloud.storage.[BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html);
    import com.google.cloud.storage.[BlobInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html);
    import com.google.cloud.storage.[BlobInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html).[ObjectContexts](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.ObjectContexts.html);
    import com.google.cloud.storage.[BlobInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html).[ObjectCustomContextPayload](https://docs.cloud.google.com/java/docs/reference/google-cloud-storagebatchoperations/latest/com.google.cloud.storagebatchoperations.v1.ObjectCustomContextPayload.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    import com.google.common.collect.Maps;
    import java.util.Map;
    
    public class SetObjectContexts {
      public static void setObjectContexts(
          String projectId, String bucketName, String objectName, String key, String value)
          throws Exception {
        // The ID of your GCP project
        // String projectId = "your-project-id";
    
        // The ID of your GCS bucket
        // String bucketName = "your-unique-bucket-name";
    
        // The ID of your GCS object
        // String objectName = "your-object-name";
    
        // The context key-value you want to add
        // String key = "your-context-key";
        // String value = "your-context-value";
    
        try ([Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage =
            [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder().setProjectId(projectId).build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)()) {
          [BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html) blobId = [BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html).of(bucketName, objectName);
          [Blob](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.html) blob = storage.get(blobId);
          if (blob == null) {
            System.out.println("The object " + objectName + " was not found in " + bucketName);
            return;
          }
    
          // Recommended: Set a generation-match precondition to avoid potential race
          // conditions and data corruptions. The request to update returns a 412 error if
          // the object's generation number does not match your precondition.
          [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html).BlobTargetOption precondition = [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html).BlobTargetOption.generationMatch();
    
          // This section demonstrates how to upsert, delete all, and delete a specific context.
    
          // To upsert a context (if the key already exists, its value is replaced;
          // otherwise, a new key-value pair is added):
          [ObjectCustomContextPayload](https://docs.cloud.google.com/java/docs/reference/google-cloud-storagebatchoperations/latest/com.google.cloud.storagebatchoperations.v1.ObjectCustomContextPayload.html) payload =
              [ObjectCustomContextPayload](https://docs.cloud.google.com/java/docs/reference/google-cloud-storagebatchoperations/latest/com.google.cloud.storagebatchoperations.v1.ObjectCustomContextPayload.html).newBuilder().setValue(value).build();
          Map<String, ObjectCustomContextPayload> custom = Maps.newHashMap();
          custom.put(key, payload);
          [ObjectContexts](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.ObjectContexts.html) contexts = [ObjectContexts](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.ObjectContexts.html).newBuilder().[setCustom](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.ObjectContexts.Builder.html#com_google_cloud_storage_BlobInfo_ObjectContexts_Builder_setCustom_java_util_Map_java_lang_String_com_google_cloud_storage_BlobInfo_ObjectCustomContextPayload__)(custom).build();
    
          /*
           * To delete all existing contexts:
           * ObjectContexts contexts = ObjectContexts.newBuilder().setCustom(null).build();
           */
    
          /*
           * To delete a specific key from the context:
           * Map<String, ObjectCustomContextPayload> custom = Maps.newHashMap();
           * custom.put(key, null);
           * ObjectContexts contexts = ObjectContexts.newBuilder().setCustom(custom).build();
           */
          [BlobInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html) pendingUpdate = blob.[toBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.html#com_google_cloud_storage_Blob_toBuilder__)().setContexts(contexts).build();
          storage.update(pendingUpdate, precondition);
    
          System.out.println(
              "Updated custom contexts for object " + objectName + " in bucket " + bucketName);
        }
      }
    }

### Rust
    
    
    use google_cloud_storage::client::StorageControl;
    use google_cloud_storage::model::ObjectContexts;
    use google_cloud_wkt::FieldMask;
    
    pub async fn sample(client: &StorageControl, bucket_id: &str) -> anyhow::Result<()> {
        const NAME: &str = "object-with-contexts";
        let object = client
            .get_object()
            .set_bucket(format!("projects/_/buckets/{bucket_id}"))
            .set_object(NAME)
            .send()
            .await?;
    
        let metageneration = object.metageneration;
        let mut custom = object.contexts.clone().unwrap_or_default().custom;
        custom.entry("example".to_string()).or_default().value = "true".into();
    
        let updated = client
            .update_object()
            .set_if_metageneration_match(metageneration)
            .set_object(object.set_contexts(ObjectContexts::new().set_custom(custom)))
            .set_update_mask(FieldMask::default().set_paths(["contexts.custom.example"]))
            .send()
            .await?;
        println!(
            "successfully set contexts for object {NAME} in bucket {bucket_id}: {:?}",
            updated.contexts
        );
        Ok(())
    }

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Create a JSON file that contains the settings for the object, which must include the `contexts` configuration fields for the object.

To add, modify, or overwrite existing contexts, use the following format:
         
         {
             "contexts": {
               "custom": {
                 "KEY": {
                   "value": "VALUE"
                 },
                 ...
               }
             }
           }

Where:

     * `KEY` is the context key to attach to an object. For example, `Department`. You can specify multiple key-value pairs in the `custom` object.
     * `VALUE` is the value to associate with the context key. For example, `Human resources`.

To delete all existing contexts, use the following format:
    
    {
        "contexts": {
          "custom": null
        }
      }

To delete a specific key from the context, use the following format:
    
    {
        "contexts": {
          "custom": {
            "KEY": null,
            ...
          }
        }
      }

Where:

`KEY` is the context key that you want to delete from an object. For example, `Department`. You can specify multiple keys to delete from the `custom` object.

**Note:** Setting a context key or the `custom` object to `null` only deletes contexts without extended data. If an existing context includes extended data, it is preserved and carried over to the updated object. To remove contexts with extended data, use the `dropContextGroups` parameter during a rewrite operation.
  3. Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with a [`PATCH` Object](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/patch) request:
         
         curl -X PATCH --data-binary @JSON_FILE_NAME \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "Content-Type: application/json" \
           "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME/o/OBJECT_NAME"

Where:

     * `JSON_FILE_NAME` is the path to the file that includes the object contexts information.
     * `BUCKET_NAME` is the name of the bucket that contains the object for which you want to edit context. For example, `my-bucket`.
     * `OBJECT_NAME` is the URL-encoded name of the object. For example, `employees.txt`.



Alternatively, you can replace an object's context with a [`PUT` Object](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/update) request. The `PUT` object request also replaces other object metadata. Therefore, we don't recommend using the `PUT` object request.

## View object contexts

You can view an object's contexts by listing object metadata or describing a specific object.

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the bucket that contains the object with the contexts you want to view.

  3. Navigate to the object, and then click the object's name.

On the **Object details** page, the key-value pairs for any attached contexts are listed in the **Object contexts** section.




### Command line

Use the [`gcloud storage objects describe`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/objects/describe) command:
    
    
    gcloud storage objects describe gs://BUCKET_NAME/OBJECT_NAME

Where:

  * `BUCKET_NAME` is the name of the bucket containing the object. For example, `my-bucket`.
  * `OBJECT_NAME` is the name of the object. For example, `employees.txt`.



If successful, the response looks similar to the following example:
    
    
    bucket: my-bucket
    contexts:
      custom:
        Department:
          createTime: '2023-01-01T00:00:00.000000+00:00'
          type: CUSTOM
          updateTime: '2023-01-01T00:00:00.000000+00:00'
          value: Human resources
        google:annotation:face-detector-v1:
          createTime: '2025-09-29T17:20:00.000000+00:00'
          extendedDataTypeUrl: type.googleapis.com/google.protobuf.Struct
          type: CUSTOM
          updateTime: '2025-09-29T17:20:00.000000+00:00'
          value: SUCCESS
    name: employees.txt
    

**Note:** To limit the output to display only the context keys and values, use `--format=contextsonly`.

### Client libraries

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import com.google.cloud.storage.[Blob](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.html);
    import com.google.cloud.storage.[BlobInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html).[ObjectContexts](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.ObjectContexts.html);
    import com.google.cloud.storage.[BlobInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html).[ObjectCustomContextPayload](https://docs.cloud.google.com/java/docs/reference/google-cloud-storagebatchoperations/latest/com.google.cloud.storagebatchoperations.v1.ObjectCustomContextPayload.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    import java.util.Map;
    
    public class GetObjectContexts {
      public static void getObjectContexts(String projectId, String bucketName, String objectName)
          throws Exception {
        // The ID of your GCP project
        // String projectId = "your-project-id";
    
        // The ID of your GCS bucket
        // String bucketName = "your-unique-bucket-name";
    
        // The ID of your GCS object
        // String objectName = "your-object-name";
    
        try ([Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage =
            [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder().setProjectId(projectId).build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)()) {
    
          [Blob](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.html) blob = storage.get(bucketName, objectName);
          if (blob == null) {
            System.out.println("The object " + objectName + " was not found in " + bucketName);
            return;
          }
          [ObjectContexts](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.ObjectContexts.html) objectContexts = blob.[getContexts](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html#com_google_cloud_storage_BlobInfo_getContexts__)();
    
          if (objectContexts != null) {
            Map<String, ObjectCustomContextPayload> customContexts = objectContexts.[getCustom](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.ObjectContexts.html#com_google_cloud_storage_BlobInfo_ObjectContexts_getCustom__)();
            if (customContexts == null) {
              System.out.println("No custom contexts found for object: " + objectName);
              return;
            }
            // Print blob's object contexts
            System.out.println("\nCustom Contexts:");
            for (Map.Entry<String, ObjectCustomContextPayload> custom : customContexts.entrySet()) {
              System.out.println(custom.getKey() + "=" + custom.getValue());
            }
          }
        }
      }
    }

### Rust
    
    
    use google_cloud_storage::client::StorageControl;
    
    pub async fn sample(client: &StorageControl, bucket_id: &str) -> anyhow::Result<()> {
        const NAME: &str = "object-with-contexts";
        let object = client
            .get_object()
            .set_bucket(format!("projects/_/buckets/{bucket_id}"))
            .set_object(NAME)
            .send()
            .await?;
        println!(
            "The contexts field for object {NAME} in bucket {bucket_id} is: {:?}",
            object.contexts
        );
        Ok(())
    }

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with a [`GET` Object](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/get) request:
         
         curl -X GET \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME/o/OBJECT_NAME"

Where:

     * `BUCKET_NAME` is the name of the bucket containing the object. For example, `my-bucket`.
     * `OBJECT_NAME` is the URL-encoded name of the object. For example, `employees.txt`.

If successful, the response looks similar to the following example:
    
    {
        "kind": "storage#object",
        "name": "employees.txt",
        "bucket": "my-bucket",
        "contexts": {
          "custom": {
            "Department": {
              "value": "Human resources",
              "createTime": "2023-01-01T00:00:00.000Z",
              "updateTime": "2023-01-01T00:00:00.000Z"
            },
            "google:annotation:face-detector-v1": {
              "value": "SUCCESS",
              "createTime": "2025-09-29T17:20:00.000Z",
              "updateTime": "2025-09-29T17:20:00.000Z",
              "extendedDataTypeUrl": "type.googleapis.com/google.protobuf.Struct"
            }
          }
        }
      }
      




### View full object context

To view a single context and its extended data, use the [`viewFullContext`](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/viewFullContext) method ([Preview](https://docs.cloud.google.com/products#product-launch-stages)).

### JSON API

To retrieve a single full context (including extended data) by key:

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with a [`GET` View Full Context](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/viewFullContext) request:
         
         curl -X GET \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME/o/OBJECT_NAME/viewFullContext?contextKey=KEY"

Where:

     * `BUCKET_NAME` is the name of the bucket containing the object. For example, `my-bucket`.
     * `OBJECT_NAME` is the URL-encoded name of the object. For example, `employees.txt`.
     * `KEY` is the specific context key to retrieve. For example, `google:annotation:face-detector-v1`.

If successful, the response looks similar to the following example:
    
    {
      "kind": "storage#objectFullContext",
      "type": "CUSTOM",
      "key": "google:annotation:face-detector-v1",
      "value": "SUCCESS",
      "createTime": "2025-09-29T17:20:00.000Z",
      "updateTime": "2025-09-29T17:20:00.000Z",
      "extendedData": {
        "@type": "type.googleapis.com/google.protobuf.Struct",
        "value": {
          "modelName": "face-detector",
          "modelVersion": "v1",
          "faceAnnotationGroup": {
            "faceAnnotations": [
              {
                "detectionConfidence": 0.9,
                "landmarkingConfidence": 0.8
              }
            ]
          }
        }
      }
    }




### Filter objects by contexts

Filter objects by the existence of object context keys or their specific values. Filtering objects by contexts helps to locate and manage particular groups of objects efficiently. For details, see [Filter objects by contexts](https://docs.cloud.google.com/storage/docs/listing-objects#filter-by-object-contexts).

## Manage object contexts during object operations

By default, Cloud Storage preserves object contexts when you copy, rewrite, compose, move, or restore objects.

### Copy objects

By default, Cloud Storage preserves object contexts from the source object during a copy operation, even if you override other metadata. To modify object contexts during a copy operation, complete the following steps:

### Command line

The [`gcloud storage cp`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/cp) command, [`gcloud storage rsync`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/rsync) command, and [`gcloud storage mv`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/mv) command preserve contexts from the source object by default. To modify contexts during these operations, use _any_ of the following flags:

  * The `--custom-contexts` flag to set new contexts for the destination object.

  * The `--clear-custom-contexts` flag to prevent contexts from the source object from being attached to the destination object.

  * A combination of the `--update-custom-contexts` and `--remove-custom-contexts` flags to modify individual contexts from the source object before attaching them to the destination object.




To set new contexts when you copy an object, use the [`gcloud storage cp`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/cp) command:
    
    
    gcloud storage cp gs://SOURCE_BUCKET_NAME/SOURCE_OBJECT_NAME gs://DESTINATION_BUCKET_NAME/DESTINATION_OBJECT_NAME --custom-contexts=KEY=VALUE,...

Where:

  * `SOURCE_BUCKET_NAME` is the name of the bucket containing the object to copy. For example, `my-source-bucket`.
  * `SOURCE_OBJECT_NAME` is the name of the object to copy. For example, `employees.txt`.
  * `DESTINATION_BUCKET_NAME` is the name of the bucket to copy the object to. For example, `my-destination-bucket`.
  * `DESTINATION_OBJECT_NAME` is the name of the destination object. For example, `employees-backup.txt`.
  * `KEY` is the context key to attach to an object. For example, `Department`. You can specify multiple key-value pairs separated by commas.
  * `VALUE` is the value to associate with the context key. For example, `Human resources`.



To remove all contexts from the source object when you copy an object, use the [`gcloud storage cp`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/cp) command:
    
    
    gcloud storage cp gs://SOURCE_BUCKET_NAME/SOURCE_OBJECT_NAME gs://DESTINATION_BUCKET_NAME/DESTINATION_OBJECT_NAME --clear-custom-contexts

Where:

  * `SOURCE_BUCKET_NAME` is the name of the bucket containing the object to copy. For example, `my-source-bucket`.
  * `SOURCE_OBJECT_NAME` is the name of the object to copy. For example, `pets/dog.png`.
  * `DESTINATION_BUCKET_NAME` is the name of the bucket to copy the object to. For example, `my-destination-bucket`.
  * `DESTINATION_OBJECT_NAME` is the name of the destination object. For example, `pets/cat.png`.



To modify individual contexts from the source object when you copy an object, use the [`gcloud storage cp`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/cp) command with `--update-custom-contexts` and `--remove-custom-contexts`:
    
    
    gcloud storage cp gs://SOURCE_BUCKET_NAME/SOURCE_OBJECT_NAME gs://DESTINATION_BUCKET_NAME/DESTINATION_OBJECT_NAME --update-custom-contexts=KEY=VALUE,... --remove-custom-contexts=KEY,...

Where:

  * `SOURCE_BUCKET_NAME` is the name of the bucket containing the object to copy. For example, `my-source-bucket`.
  * `SOURCE_OBJECT_NAME` is the name of the object to copy. For example, `pets/dog.png`.
  * `DESTINATION_BUCKET_NAME` is the name of the bucket to copy the object to. For example, `my-destination-bucket`.
  * `DESTINATION_OBJECT_NAME` is the name of the destination object. For example, `pets/cat.png`.
  * `KEY` is the context key to attach to an object. For example, `Department`. You can specify multiple key-value pairs or keys separated by commas.
  * `VALUE` is the value to associate with the context key. For example, `Human resources`.



### JSON API

To override contexts when [copying](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/copy) an object, include the `contexts.custom` property in the request body:

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Create a JSON file that contains the contexts to attach to the destination object:
         
         {
             "contexts": {
               "custom": {
                 "KEY": {
                   "value": "VALUE"
                 }
               }
             }
           }

Where:

     * `KEY` is the context key to attach to an object. For example, `Department`.
     * `VALUE` is the value to associate with the context key. For example, `Human resources`.
  3. Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with a [`POST` Object](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/copy) request:
         
         curl -X POST --data-binary @JSON_FILE_NAME \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "Content-Type: application/json" \
           "https://storage.googleapis.com/storage/v1/b/SOURCE_BUCKET_NAME/o/SOURCE_OBJECT_NAME/copyTo/b/DESTINATION_BUCKET_NAME/o/DESTINATION_OBJECT_NAME"

Where:

     * `JSON_FILE_NAME` is the path to the JSON file that includes the object contexts information.
     * `SOURCE_BUCKET_NAME` is the name of the bucket that contains the object to copy. For example, `my-source-bucket`.
     * `SOURCE_OBJECT_NAME` is the URL-encoded name of the object to copy. For example, `employees.txt`.
     * `DESTINATION_BUCKET_NAME` is the name of the bucket to copy the object to. For example, `my-destination-bucket`.
     * `DESTINATION_OBJECT_NAME` is the URL-encoded name of the destination object. For example, `employees-backup.txt`.



To discard source contexts during a copy operation, use the `dropContextGroups=custom` query parameter in your request:
    
    
    curl -X POST \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      "https://storage.googleapis.com/storage/v1/b/SOURCE_BUCKET_NAME/o/SOURCE_OBJECT_NAME/copyTo/b/DESTINATION_BUCKET_NAME/o/DESTINATION_OBJECT_NAME?dropContextGroups=custom"

If the request body contains contexts with the `google:` prefix, you can retain existing keys and values from the source object, but Cloud Storage rejects new `google:` keys or modified values.

To preserve contexts, omit the `contexts` property from the request body and exclude the `dropContextGroups` query parameter.

### Rewrite objects

By default, Cloud Storage preserves object contexts from the source object during a rewrite operation, even if you override other metadata. To modify object contexts during a rewrite operation, complete the following steps:

### Command line

The [`gcloud storage cp`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/cp) command, [`gcloud storage rsync`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/rsync) command, and [`gcloud storage mv`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/mv) commands perform rewrites automatically when necessary, for example, when copying objects between different locations or storage classes. `gcloud storage cp` and `gcloud storage rsync` result in a source and destination object, while `gcloud storage mv` creates the destination object and removes the source object. Because these operations create a new object, you can also modify or attach contexts as part of the same command by using _any_ of the following flags:

  * The `--custom-contexts` flag to set new contexts for the destination object.

  * The `--clear-custom-contexts` flag to prevent contexts from the source object from being attached to the destination object.

  * A combination of the `--update-custom-contexts` and `--remove-custom-contexts` flags to modify individual contexts from the source object before attaching them to the destination object.




To set new contexts when you copy an object, use the [`gcloud storage cp`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/cp) command:
    
    
    gcloud storage cp gs://SOURCE_BUCKET_NAME/SOURCE_OBJECT_NAME gs://DESTINATION_BUCKET_NAME/DESTINATION_OBJECT_NAME --custom-contexts=KEY=VALUE,...

Where:

  * `SOURCE_BUCKET_NAME` is the name of the bucket containing the object to copy. For example, `my-source-bucket`.
  * `SOURCE_OBJECT_NAME` is the name of the object to copy. For example, `employees.txt`.
  * `DESTINATION_BUCKET_NAME` is the name of the bucket to copy the object to. For example, `my-destination-bucket`.
  * `DESTINATION_OBJECT_NAME` is the name of the destination object. For example, `employees-backup.txt`.
  * `KEY` is the context key to attach to an object. For example, `Department`. You can specify multiple key-value pairs separated by commas.
  * `VALUE` is the value to associate with the context key. For example, `Human resources`.



To remove all contexts from the source object when you copy an object, use the [`gcloud storage cp`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/cp) command:
    
    
    gcloud storage cp gs://SOURCE_BUCKET_NAME/SOURCE_OBJECT_NAME gs://DESTINATION_BUCKET_NAME/DESTINATION_OBJECT_NAME --clear-custom-contexts

Where:

  * `SOURCE_BUCKET_NAME` is the name of the bucket containing the object to copy. For example, `my-source-bucket`.
  * `SOURCE_OBJECT_NAME` is the name of the object to copy. For example, `pets/dog.png`.
  * `DESTINATION_BUCKET_NAME` is the name of the bucket to copy the object to. For example, `my-destination-bucket`.
  * `DESTINATION_OBJECT_NAME` is the name of the destination object. For example, `pets/cat.png`.



To modify individual contexts from the source object when you copy an object, use the [`gcloud storage cp`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/cp) command with `--update-custom-contexts` and `--remove-custom-contexts`:
    
    
    gcloud storage cp gs://SOURCE_BUCKET_NAME/SOURCE_OBJECT_NAME gs://DESTINATION_BUCKET_NAME/DESTINATION_OBJECT_NAME --update-custom-contexts=KEY=VALUE,... --remove-custom-contexts=KEY,...

Where:

  * `SOURCE_BUCKET_NAME` is the name of the bucket containing the object to copy. For example, `my-source-bucket`.
  * `SOURCE_OBJECT_NAME` is the name of the object to copy. For example, `pets/dog.png`.
  * `DESTINATION_BUCKET_NAME` is the name of the bucket to copy the object to. For example, `my-destination-bucket`.
  * `DESTINATION_OBJECT_NAME` is the name of the destination object. For example, `pets/cat.png`.
  * `KEY` is the context key to attach to an object. For example, `Department`. You can specify multiple key-value pairs or keys separated by commas.
  * `VALUE` is the value to associate with the context key. For example, `Human resources`.



### JSON API

To override contexts when rewriting an object, include the `contexts.custom` property in the request body:

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Create a JSON file that contains the contexts to attach to the destination object:
         
         {
             "contexts": {
               "custom": {
                 "KEY": {
                   "value": "VALUE"
                 }
               }
             }
           }

Where:

     * `KEY` is the context key to attach to an object. For example, `Department`.
     * `VALUE` is the value to associate with the context key. For example, `Human resources`.
  3. Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with a [`POST` rewrite Object](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/rewrite) request:
         
         curl -X POST --data-binary @JSON_FILE_NAME \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "Content-Type: application/json" \
           "https://storage.googleapis.com/storage/v1/b/SOURCE_BUCKET_NAME/o/SOURCE_OBJECT_NAME/rewriteTo/b/DESTINATION_BUCKET_NAME/o/DESTINATION_OBJECT_NAME"

Where:

     * `JSON_FILE_NAME` is the path to the JSON file that includes the object contexts information.
     * `SOURCE_BUCKET_NAME` is the name of the bucket that contains the object to rewrite. For example, `my-source-bucket`.
     * `SOURCE_OBJECT_NAME` is the URL-encoded name of the object to rewrite. For example, `employees.txt`.
     * `DESTINATION_BUCKET_NAME` is the name of the bucket to rewrite the object to. For example, `my-destination-bucket`.
     * `DESTINATION_OBJECT_NAME` is the URL-encoded name of the destination object. For example, `employees-backup.txt`.



To discard source contexts during a rewrite operation, use the `dropContextGroups=custom` query parameter in your request:
    
    
    curl -X POST \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      "https://storage.googleapis.com/storage/v1/b/SOURCE_BUCKET_NAME/o/SOURCE_OBJECT_NAME/rewriteTo/b/DESTINATION_BUCKET_NAME/o/DESTINATION_OBJECT_NAME?dropContextGroups=custom"

If the request body contains contexts with the `google:` prefix, you can retain existing keys and values from the source object, but Cloud Storage rejects new `google:` keys or modified values.

To preserve contexts, omit the `contexts` property from the request body and exclude the `dropContextGroups` query parameter.

### Compose objects

The [`gcloud storage objects compose`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/objects/compose) command and the [JSON API compose](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/compose) method merge contexts from the source objects and attach them to the destination objects by default. Cloud Storage resolves conflicts by prioritizing contexts from source objects processed later. For more information about the object context behavior during a compose operation, see [Composite object contexts](https://docs.cloud.google.com/storage/docs/composite-objects#object-contexts).

### Command line

To specify new contexts for the destination object when composing objects, use the `--contexts` flag:
    
    
    gcloud storage objects compose gs://BUCKET_NAME/SOURCE_OBJECT_1 gs://BUCKET_NAME/SOURCE_OBJECT_2 gs://BUCKET_NAME/DESTINATION_OBJECT_NAME --contexts=KEY=VALUE,...

Where:

  * `BUCKET_NAME` is the name of the bucket that contains the source objects and where the destination object is created. For example, `my-bucket`.
  * `SOURCE_OBJECT_1` and `SOURCE_OBJECT_2` are source objects to compose.
  * `DESTINATION_OBJECT_NAME` is the name of the destination object to be created. For example, `my-composite-object`.
  * `KEY` is the context key to attach to an object. For example, `Department`. You can specify multiple key-value pairs separated by commas.
  * `VALUE` is the value to associate with the context key. For example, `Human resources`.



To prevent source contexts from being attached to composite objects, use the `--clear-custom-contexts` flag:
    
    
    gcloud storage objects compose gs://BUCKET_NAME/SOURCE_OBJECT_1 gs://BUCKET_NAME/SOURCE_OBJECT_2 gs://BUCKET_NAME/DESTINATION_OBJECT_NAME --clear-custom-contexts

Where:

  * `BUCKET_NAME` is the name of the bucket that contains source objects and where the destination object is created. For example, `my-bucket`.
  * `SOURCE_OBJECT_1` and `SOURCE_OBJECT_2` are the source objects to compose.
  * `DESTINATION_OBJECT_NAME` is the name of the destination object to be created. For example, `my-composite-object`.



### JSON API

To specify new contexts for the destination object when composing objects, include contexts in the `destination` property of the request body.

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Create a JSON file that contains the request body:
         
         {
           "sourceObjects": [
             {"name": "SOURCE_OBJECT_1"},
             {"name": "SOURCE_OBJECT_2"}
           ],
           "destination": {
             "contentType": "text/plain",
             "contexts": {
               "custom": {
                 "KEY": {
                   "value": "VALUE"
                 }
               }
             }
           }
         }

Where:

     * `SOURCE_OBJECT_1` and `SOURCE_OBJECT_2` are source objects to compose.
     * `KEY` is the context key to attach to an object. For example, `Department`.
     * `VALUE` is the value to associate with the context key. For example, `Human resources`.
  3. Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with a [`POST` compose Object](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/compose) request:
         
         curl -X POST --data-binary @JSON_FILE_NAME \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "Content-Type: application/json" \
           "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME/o/DESTINATION_OBJECT_NAME/compose"

Where:

     * `JSON_FILE_NAME` is the path to the JSON file that includes the request body.
     * `BUCKET_NAME` is the name of the bucket that contains source objects and where the destination object is created. For example, `my-bucket`.
     * `DESTINATION_OBJECT_NAME` is the name of the destination object to be created. For example, `my-composite-object`.



To prevent source contexts from being attached to composite objects, use the `dropContextGroups=custom` query parameter in your request:

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Create a JSON file that contains the request body:
         
         {
           "sourceObjects": [
             {"name": "SOURCE_OBJECT_1"},
             {"name": "SOURCE_OBJECT_2"}
           ],
           "destination": {
             "contentType": "text/plain"
         }
         }

Where:

     * `SOURCE_OBJECT_1` and `SOURCE_OBJECT_2` are source objects to compose.
  3. Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with a [`POST` compose Object](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/compose) request:
         
         curl -X POST --data-binary @JSON_FILE_NAME \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "Content-Type: application/json" \
           "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME/o/DESTINATION_OBJECT_NAME/compose?dropContextGroups=custom"

Where:

     * `JSON_FILE_NAME` is the path to the JSON file that includes the request body.
     * `BUCKET_NAME` is the name of the bucket that contains source objects and where the destination object is created. For example, `my-bucket`.
     * `DESTINATION_OBJECT_NAME` is the name of the destination object to be created. For example, `my-composite-object`.



## Manage object contexts in bulk

To manage object contexts for millions or billions of objects with a single job, use [Storage batch operations](https://docs.cloud.google.com/storage/docs/batch-operations/overview). To create a job, specify the target objects by providing a manifest file or by using object prefixes. After specifying the objects, [create a batch operation job to update object contexts](https://docs.cloud.google.com/storage/docs/batch-operations/create-manage-batch-operation-jobs).

## Analyze object contexts in BigQuery

If you have an active [Storage Intelligence](https://docs.cloud.google.com/storage/docs/insights/datasets) subscription, you can query and analyze object contexts in BigQuery. Use the [Object Contexts Catalog view (`object_contexts_catalog_view`)](https://docs.cloud.google.com/storage/docs/insights/dataset-tables-and-schemas#object-contexts-catalog-schema) to query context keys, values, and structured `extendedData` payloads (such as image labels, detected faces, and bounding boxes). The catalog view updates every 24 hours.

For example, to find all objects where a specific annotation score exceeds a threshold:
    
    
    SELECT
      t.project,
      t.bucket,
      t.name,
      t.generation,
      label
    FROM
      `PROJECT_ID.INSIGHTS_DATASET.object_contexts_catalog_view` AS t,
      UNNEST(t.contexts) AS context,
      UNNEST(JSON_QUERY_ARRAY(context.extendedData.labelAnnotationGroup.labelAnnotations)) AS label
    WHERE
      context.key = "google:annotation:label-detector-v1"
      AND FLOAT64(label.score) > 0.75;

Replace:

  * `PROJECT_ID`: the ID of the project that contains the Storage Insights dataset.
  * `INSIGHTS_DATASET`: the name of the Storage Insights dataset.



For more information about the catalog view schema, see [Object contexts catalog schema](https://docs.cloud.google.com/storage/docs/insights/dataset-tables-and-schemas#object-contexts-catalog-schema). For more example queries, see [Analyze object contexts](https://docs.cloud.google.com/storage/docs/insights/configure-datasets#analyze-object-contexts).

## What's next

  * Learn about the object context properties in the [Cloud Storage API documentation](https://docs.cloud.google.com/storage/docs/json_api/v1/objects).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-23 UTC."],[],[]] 
