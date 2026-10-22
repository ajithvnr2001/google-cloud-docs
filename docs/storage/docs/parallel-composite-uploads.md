---
url: https://docs.cloud.google.com/storage/docs/parallel-composite-uploads/
title: Parallel composite uploads \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:28:52.345810+00:00
---

# Parallel composite uploads  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/parallel-composite-uploads/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Parallel composite uploads Stay organized with collections  Save and categorize content based on your preferences. 

Parallel composite uploads can help you upload large files significantly faster when network and disk speed aren't limiting factors. In a parallel composite upload, a file is divided into up to 32 chunks, the chunks are uploaded in parallel to temporary objects, the final object is [recreated using the temporary objects](https://docs.cloud.google.com/storage/docs/composing-objects), and the temporary objects are deleted.

If you interact with Cloud Storage by using the XML API, consider using [XML API multipart uploads](https://docs.cloud.google.com/storage/docs/multipart-uploads) instead. XML API multipart uploads support a greater number of parts than compose operations, have less potential for early deletion fees, and don't require `Delete` requests to remove the source parts once the final object is assembled.

## Considerations

The final object that a parallel composite upload stores in your bucket is a _composite object_ , which only has a crc32c hash and not an MD5 hash. As a result, you must use crcmod to perform integrity checks when downloading the object with Python applications. You should only perform parallel composite uploads if the following apply:

  * You don't need the uploaded objects to have an [MD5 hash](https://docs.cloud.google.com/storage/docs/metadata#md5).

  * Any Python user, including [gsutil](https://docs.cloud.google.com/storage/docs/gsutil) users, who needs to download your objects has either google-crc32c or crcmod installed.

For example, if you use Python to upload video assets that are only served by a Java application, parallel composite uploads are a good choice because there are efficient CRC32C implementations available in Java.


**Warning:** Parallel composite uploads involve deleting temporary objects. Keep in mind the following: 

  * To minimize billing for temporary objects, hard delete the temporary objects during the composition process.
  * If you plan to delete the temporary objects after the composition process has finished, then use [Standard storage](https://docs.cloud.google.com/storage/docs/storage-classes#standard) for temporary objects to avoid the [early deletion fees](https://docs.cloud.google.com/storage/pricing) that are charged for other storage classes. After the final object is composed, you can change its storage class.
  * If your bucket has data protection features like [soft delete](https://docs.cloud.google.com/storage/docs/soft-delete) or [Object Versioning](https://docs.cloud.google.com/storage/docs/object-versioning) enabled, deleting temporary objects after the composition process has finished can increase your storage bill significantly. Consider disabling these protections on your bucket if you perform parallel composite uploads frequently. Alternatively, hard delete the temporary objects during the composition process.
  * You shouldn't use parallel composite uploads when uploading to a bucket that has a [retention policy](https://docs.cloud.google.com/storage/docs/bucket-lock), because the temporary objects can't be deleted until they meet the retention period.
  * If the bucket you upload to has [default object holds](https://docs.cloud.google.com/storage/docs/object-holds#default-holds) enabled, you must [release the hold](https://docs.cloud.google.com/storage/docs/holding-objects#set-object-hold) from each temporary object before you can delete it.



## Required roles

To get the permissions that you need to perform parallel composite uploads, ask your administrator to grant you the [Storage Object User ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectUser) (`roles/storage.objectUser`) IAM role on the bucket. 

The Storage Admin (`roles/storage.admin`) role contains the permissions required to upload, read, and delete object chunks. It also contains the required permission for the gcloud CLI to perform a bucket-level compatibility check with parallel composite uploads. If you can't get the Storage Admin (`roles/storage.admin`) role, you can still perform parallel composite uploads using the gcloud CLI by getting the Storage Object User (`roles/storage.objectUser`) role and disabling the `storage/parallel_composite_upload_compatibility_check` property. For more information, see the **Command line** tab in the section **How tools and APIs use parallel composite uploads**. 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined).

For instructions on granting roles on buckets, see [Set and manage IAM policies on buckets](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions).

## How tools and APIs use parallel composite uploads

Depending on how you interact with Cloud Storage, parallel composite uploads might be managed automatically on your behalf. This section describes parallel composite upload behavior for different tools and provides information for how you can modify the behavior.

### Console

The Google Cloud console does not perform parallel composite uploads.

### Command line

The following properties work together to determine how and when the gcloud CLI performs parallel composite uploads:

  * **`storage/parallel_composite_upload_enabled`** : Property for enabling parallel composite uploads. If `False`, disables parallel composite uploads and skips bucket-level compatibility checks. If `True` or `None`, enables parallel composite uploads for objects that meet the criteria defined in the other properties and enables compatibility checks. The default setting is `None`.

  * **`storage/parallel_composite_upload_compatibility_check`** : Property for toggling bucket-level checks for compatibility and safety with parallel composite uploads. If `True`, the gcloud CLI sends a `GET` request for the destination bucket's metadata before it attempts a parallel composite upload, which requires the principal to have the `storage.buckets.get` permission. The gcloud CLI only performs parallel composite uploads when all of the following conditions are met:

    * The [storage class](https://docs.cloud.google.com/storage/docs/storage-classes) for the uploaded object is `STANDARD`.
    * The destination bucket does not have a [retention policy](https://docs.cloud.google.com/storage/docs/bucket-lock).
    * The destination bucket does not have [default object holds](https://docs.cloud.google.com/storage/docs/object-holds#default-holds) enabled.

The default setting is `True`. If `False`, the gcloud CLI doesn't perform the compatibility check.

Setting `storage/parallel_composite_upload_compatibility_check` to `False` doesn't disable parallel composite uploads. When `storage/parallel_composite_upload_compatibility_check` is set to `False` and `storage/parallel_composite_upload_enabled` is `None` or `True`, the gcloud CLI skips the bucket check and proceeds directly with a parallel composite upload.

To skip this check, disable the `storage/parallel_composite_upload_compatibility_check` property:
    
    gcloud config set storage/parallel_composite_upload_compatibility_check False
    

  * **`storage/parallel_composite_upload_threshold`** : The minimum total file size for performing a parallel composite upload. The default setting is 150 MiB.

  * **`storage/parallel_composite_upload_component_size`** : The maximum size for each temporary object. The property is ignored if the total file size is so large that it would require more than 32 chunks at this size.

  * **`storage/parallel_composite_upload_component_prefix`** : The prefix used when naming temporary objects. This property can be set either as an absolute path or as a path relative to the final object. See the [property description](https://docs.cloud.google.com/sdk/gcloud/reference/topic/configurations#parallel_composite_upload_component_prefix) for more information. The default prefix is the absolute path `/gcloud/tmp/parallel_composite_uploads/see_gcloud_storage_cp_help_for_details`.




You can modify these properties by creating a [named configuration](https://docs.cloud.google.com/sdk/gcloud/reference/topic/configurations) and applying the configuration either on a per-command basis by using the [`--configuration` project-wide flag](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration) or for all gcloud CLI commands by using the [`gcloud config set` command](https://docs.cloud.google.com/sdk/gcloud/reference/config/set).

No additional local disk space is required when using gcloud CLI to perform parallel composite uploads. If a parallel composite upload fails prior to composition, run the gcloud CLI command again to take advantage of resumable uploads for the temporary objects that failed. Any temporary objects that uploaded successfully before the failure don't get re-uploaded when you resume the upload.

Temporary objects are named in the following fashion:
    
    
    TEMPORARY_PREFIX/RANDOM_VALUE_HEX_DIGEST_COMPONENT_ID

Where:

  * `TEMPORARY_PREFIX` is controlled by the `storage/parallel_composite_upload_component_prefix` property.
  * `RANDOM_VALUE` is a random numerical value.
  * `HEX_DIGEST` is a hash derived from the name of the source resource.
  * `COMPONENT_ID` is the sequential number of the component.



Generally, temporary objects are deleted at the end of a parallel composite upload, but to avoid leaving temporary objects around, you should check the exit status from the gcloud CLI command, and you should manually delete any temporary objects that were uploaded as part of any aborted upload.

### Client libraries

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

You can perform parallel composite uploads by setting `AllowParallelCompositeUpload` to `true`. For example:
    
    
    import com.google.cloud.storage.transfermanager.[ParallelUploadConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.ParallelUploadConfig.html);
    import com.google.cloud.storage.transfermanager.[TransferManager](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManager.html);
    import com.google.cloud.storage.transfermanager.[TransferManagerConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html);
    import com.google.cloud.storage.transfermanager.[UploadResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.UploadResult.html);
    import java.io.IOException;
    import java.nio.file.Path;
    import java.util.List;
    
    class AllowParallelCompositeUpload {
    
      public static void parallelCompositeUploadAllowed(String bucketName, List<Path> files)
          throws IOException {
        [TransferManager](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManager.html) transferManager =
            [TransferManagerConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html).newBuilder()
                .[setAllowParallelCompositeUpload](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.Builder.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_Builder_setAllowParallelCompositeUpload_boolean_)(true)
                .build()
                .[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)();
        [ParallelUploadConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.ParallelUploadConfig.html) parallelUploadConfig =
            [ParallelUploadConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.ParallelUploadConfig.html).newBuilder().setBucketName(bucketName).build();
        List<UploadResult> results =
            transferManager.[uploadFiles](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManager.html#com_google_cloud_storage_transfermanager_TransferManager_uploadFiles_java_util_List_java_nio_file_Path__com_google_cloud_storage_transfermanager_ParallelUploadConfig_)(files, parallelUploadConfig).[getUploadResults](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.UploadJob.html#com_google_cloud_storage_transfermanager_UploadJob_getUploadResults__)();
        for ([UploadResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.UploadResult.html) result : results) {
          System.out.println(
              "Upload for "
                  + result.getInput().getName()
                  + " completed with status "
                  + result.getStatus());
        }
      }
    }

### Node.js

For more information, see the [Cloud Storage Node.js API reference documentation](https://cloud.google.com/nodejs/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The Node.js client library does not support parallel composite uploads. Instead, use [XML API multipart uploads](https://docs.cloud.google.com/storage/docs/multipart-uploads).

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The Python client library does not support parallel composite uploads. Instead, use [XML API multipart uploads](https://docs.cloud.google.com/storage/docs/multipart-uploads).

### REST APIs

### JSON API

The [JSON API](https://docs.cloud.google.com/storage/docs/json_api) supports uploading object chunks in parallel and recombining them into a single object using the [`compose` operation](https://docs.cloud.google.com/storage/docs/composing-objects).

Keep the following in mind when designing code for parallel composite uploads:

  * When using the `compose` operation, you can hard delete the source objects as part of the composition process. Use this option to minimize billing for temporary objects that don't need to be protected by soft delete or Object Versioning. 

  * In order to protect against changes to source objects between the upload and compose requests, you should provide an expected [generation number](https://docs.cloud.google.com/storage/docs/metadata#generation-number) for each source.




### XML API

The [XML API](https://docs.cloud.google.com/storage/docs/xml-api) supports uploading object chunks in parallel and recombining them into a single object using the [`compose` operation](https://docs.cloud.google.com/storage/docs/composing-objects).

Keep the following in mind when designing code for parallel composite uploads:

  * When using the `compose` operation, the source objects are unaffected by the composition process.

This means that if they are meant to be temporary, you must explicitly [delete them](https://docs.cloud.google.com/storage/docs/deleting-objects) once you've successfully completed the composition, or else the source objects remain in your bucket and are billed accordingly.

  * In order to protect against changes to source objects between the upload and compose requests, you should provide an expected [generation number](https://docs.cloud.google.com/storage/docs/metadata#generation-number) for each source.




## Troubleshooting

This section contains information on how to troubleshoot gcloud CLI errors that can occur with parallel composite uploads.

### Can't check if the destination bucket is compatible with parallel composite uploads

**Issue** : When you upload a file that's 150 MiB or larger by using `gcloud storage cp` or `gcloud storage mv`, the command logs the following message once, but the upload completes successfully with exit code `0`:
    
    
    ERROR: Cannot check if the destination bucket is compatible for running
    parallel composite uploads as the user does not permission to perform GET
    operation on the bucket. The operation will be performed without parallel
    composite upload feature and hence might perform relatively slower.
    

**Solution** : The gcloud CLI is attempting to run the parallel composite upload compatibility check. The principal doesn't have the `storage.buckets.get` permission on the destination bucket, so the request for the bucket's metadata is denied. The gcloud CLI handles the error internally and doesn't display an HTTP status code. Instead, it logs the message and falls back to a regular upload.

If you want parallel composite uploads, ensure that the principal has the `storage.buckets.get`, `storage.objects.get`, and `storage.objects.delete` permissions on the destination bucket. These permissions can be granted through the Storage Admin (`roles/storage.admin`) role. Alternatively, if the principal already has the `storage.objects.get` and `storage.objects.delete` permissions through a role like Storage Object User (`roles/storage.objectUser`), they can set the `storage/parallel_composite_upload_compatibility_check` property to `False` to disable the compatibility check.

### 403: does not have storage.objects.get access

**Issue** : Uploads of files smaller than 150 MiB succeed, but uploads of files that are 150 MiB or larger fail with exit code `1` and an error similar to the following:
    
    
    HTTPError 403: PRINCIPAL does not have storage.objects.get access to
    the Google Cloud Storage object.
    

**Solution** : `storage/parallel_composite_upload_compatibility_check` is set to `False` and `storage/parallel_composite_upload_enabled` is either set to `None` or `True`. In this configuration, the gcloud CLI skips the bucket compatibility check and proceeds directly with a parallel composite upload.

The temporary objects upload successfully because the principal has the `storage.objects.create` permission. However, composing the temporary objects into the final object requires the `storage.objects.get` permission, and deleting the temporary objects afterward requires the `storage.objects.delete` permission.

To resolve this issue, choose one of the following options:

  * If you don't need parallel composite uploads, disable them:
        
        gcloud config set storage/parallel_composite_upload_enabled False
        

All files are uploaded as regular uploads, and the principal needs only the permissions included in the Storage Object Creator (`roles/storage.objectCreator`) role. You can leave `storage/parallel_composite_upload_compatibility_check` at any value.

  * If you need parallel composite uploads, grant the principal the `storage.objects.get` and `storage.objects.delete` permissions on the destination bucket. These permissions can be granted through the Storage Object User (`roles/storage.objectUser`) role.




If the failed upload left temporary objects in your bucket, delete them. By default, temporary objects use the prefix `gcloud/tmp/parallel_composite_uploads/see_gcloud_storage_cp_help_for_details`. To delete temporary objects that resulted from a failed upload, you need the `storage.objects.delete` permission.

Note that the [`gcloud storage rsync`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/rsync) command behaves differently than `gcloud storage cp` and `gcloud storage mv`. When the destination is a bucket root, such as `gs://my-bucket`, `gcloud storage rsync` always requires the `storage.buckets.get` permission in order to sync to the bucket, regardless of your parallel composite upload settings. When the destination is a bucket subdirectory, such as `gs://my-bucket/dir/`, `gcloud storage rsync` doesn't require the `storage.buckets.get` permission, as long as the compatibility check is disabled in your parallel composite upload settings. In this scenario, `gcloud storage rsync` requires the `storage.objects.get` permission instead of `storage.buckets.get`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
