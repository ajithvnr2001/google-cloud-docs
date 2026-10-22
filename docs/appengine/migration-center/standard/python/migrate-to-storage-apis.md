---
url: https://docs.cloud.google.com/appengine/migration-center/standard/python/migrate-to-storage-apis/
title: Migrating to the Cloud Client Library for Storage \u00a0|\u00a0 App Engine migration center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:49:44.061800+00:00
---

# Migrating to the Cloud Client Library for Storage  |  App Engine migration center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/migration-center/standard/python/migrate-to-storage-apis/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Migration center ](https://docs.cloud.google.com/appengine/migration-center)
  * [ Guides ](https://docs.cloud.google.com/appengine/migration-center/standard/services/migrating-services)



Send feedback 

#  Migrating to the Cloud Client Library for Storage Stay organized with collections  Save and categorize content based on your preferences. 

[Cloud Storage](https://docs.cloud.google.com/storage/docs) enables your application to serve large data objects such as video or image files, and enables your users to upload large data files. In the Python 2 runtime, App Engine provides its own client library for writing and reading objects in Cloud Storage. This App Engine library is not available in newer App Engine runtimes, including the Python 3 runtime.

If your Python 2 app uses the `GoogleAppEngineCloudStorageClient` library, you need to migrate to the Cloud Client Library for Cloud Storage before you can run the app in the Python 3 runtime. Note that you only need to migrate your app to use a new client library. **All of the data objects and permissions in your existing Cloud Storage buckets remain unchanged, and you can access your existing buckets using the new client library**.

## Comparison of the App Engine and Cloud Client Libraries

Similarities:

  * The Cloud Client Library supports all of the Cloud Storage features enabled by the App Engine client library, such as reading, writing, removing, and listing objects. Migration should require only small changes to your code.

The Cloud Client Library also supports additional features, such as creating and [labeling](https://docs.cloud.google.com/storage/docs/using-bucket-labels) buckets, and [retrieving older versions of objects](https://docs.cloud.google.com/storage/docs/object-versioning).




Differences:

  * In the App Engine library, the function that retrieves a list of objects works asynchronously. The Cloud Client Library doesn't provide an asynchronous function for listing objects, though you can use paging and iterate through a small set of objects.

  * The App Engine client library requires you to use access control lists (ACL) to control access to buckets and objects. However, Cloud Storage and the Cloud Client Library support two systems for granting users permission to access your buckets and objects: ACLs and [uniform bucket-level access](https://docs.cloud.google.com/storage/docs/uniform-bucket-level-access). Uniform bucket-level access provides a simpler, consistent access control experience across all of your Cloud resources.

All ACLs that you used with the App Engine client library remain in effect for your existing buckets after you migrate to the Cloud Client Library, and you can continue to use ACLs if needed.

If uniform bucket-level access meets your needs, we recommend you use this simpler system for any new buckets you create. While you can convert existing buckets to use uniform bucket-level access, this may require significant changes to how your app secures access to its storage objects.




Code samples:

  * Basic storage operations [using the App Engine APIs](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/appengine/standard/storage/appengine-client/main.py)

  * Basic storage operations [using the Cloud client library for Cloud Storage](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/appengine/standard/migration/storage/main.py)




## Before you start migrating

If you have not done so already, set up your [Python development environment](https://docs.cloud.google.com/python/docs/setup) to use a Python version that is compatible with Google Cloud, and install testing tools for creating isolated Python environments.

### Understanding Cloud Storage permissions

By default, your app's [auto-created default service account](https://docs.cloud.google.com/iam/docs/service-accounts#default) has read and write privileges to the buckets in your project, and it has full rights to the objects it creates, both before and after migration.

If you used a different service account or user account to secure access to your Cloud Storage buckets and objects, be sure you continue to use the same accounts and [authentication techniques](https://docs.cloud.google.com/docs/authentication#service-accounts) before and after migration.

## Overview of the migration process

To migrate your Python app to use the Cloud Client Library for Cloud Storage instead of the App Engine client library:

  1. Install the Cloud Client Library for Cloud Storage.

  2. Update your code to use the Cloud Client Library.

  3. Test your updates.

  4. Deploy your app to App Engine.




## Installing the Cloud Client Library for Cloud Storage

To make the Cloud Client Library for Cloud Storage available to your app when it runs in App Engine:

  1. Update the `app.yaml` file:

     1. If you use Cloud Client Libraries, add the latest versions of `grpcio` and `setuptools` libraries.
     2. Add the `ssl` library since this is required by Cloud Storage.

The following is an example `app.yaml` file:
    
    runtime: python27
    threadsafe: yes
    api_version: 1
    
    libraries:
    - name: grpcio
      version: 1.0.0
    - name: setuptools
      version: 36.6.0
    - name: ssl
      version: latest
    

Some client libraries don't need the SSL library. If you don't include the SSL library for a client library that needs it, you'll see an SSL error in the Logs Explorer when your app receives a request.

  2. Update the `requirements.txt` file by adding the Cloud Client Libraries for Cloud Storage to your list of dependencies:
         
         google-cloud-storage==1.24.1
         

We recommend you use the 1.24.1 version of the Cloud Storage client library since it supports Python 2.7 apps.

Then run `pip install -t lib -r requirements.txt` to update the list of available libraries for your app.

  3. For Python 2 apps, if your app is using built-in or copied libraries, you must specify those paths in the `appengine_config.py` file:
         
         import pkg_resources
         from google.appengine.ext import vendor
         
         # Set PATH to your libraries folder.
         PATH = 'lib'
         # Add libraries installed in the PATH folder.
         vendor.add(PATH)
         # Add libraries to pkg_resources working set to find the distribution.
         pkg_resources.working_set.add_entry(PATH)
         

The `appengine_config.py` file in the preceding example assumes that the the `lib` folder is located in the current working directory. If you can't guarantee that `lib` will always be in the current working directory, specify the full path to the `lib` folder. For example:
         
         import os
         path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'lib')




## Updating your code to use the Cloud Client Library

### Creating a Cloud Storage Client

To use the Cloud Client Library for Cloud Storage, create a [`Client` object](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client). The client contains credentials and other data needed to connect to Cloud Storage. For example:
    
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
    client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
    

In the default authorization scenario described previously, the Cloud Storage client contains credentials from App Engine's default service account, which is authorized to interact with your project's buckets and objects. If you aren't working in this default scenario, see [Application Default Credentials (ADC)](https://docs.cloud.google.com/docs/authentication/application-default-credentials) for information on how to provide credentials.

### Using Cloud Client Library methods

The following table summarizes which methods from the Cloud Client Library to use when implementing specific Cloud Storage features.

**Note:** See the [list of code samples](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/master/storage/cloud-client) and the [reference documentation](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client) for the Cloud Client Library.**Cloud Storage feature** | **Cloud client methods**  
---|---  
List objects in a bucket  | `[Client.list_blobs](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client#google_cloud_storage_client_Client_list_blobs) ` See a [simple code sample](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_list_files.py) and a sample of [ emulating directory mode](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_list_files_with_prefix.py).  To page through the list of objects, use the `pages` property of the iterator object that `Client.list_blobs` returns.  
Write to storage  | `[blob.upload_from_file](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob#google_cloud_storage_blob_Blob_upload_from_file)`   
`[blob.upload_from_filename](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob#google_cloud_storage_blob_Blob_upload_from_filename)`   
`[blob.upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob#google_cloud_storage_blob_Blob_upload_from_string)` See a [code sample](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_upload_file.py).  
Specify ACLs  | To apply a [predefined ACL](https://docs.cloud.google.com/storage/docs/access-control/lists#predefined-acl), use the `predefined_acl` parameter when you [create a bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket#google_cloud_storage_bucket_Bucket_create) or [create an object](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob#google_cloud_storage_blob_Blob_upload_from_file). For more fine-grained control, use `bucket.acl.reload()` or `blob.acl.reload()` to retrieve any ACLs currently defined. Then use `[ACL](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.acl.ACL)` methods to add or remove ACLs. See a [code sample](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_add_file_owner.py).  
Read from storage  | `[blob.download_to_file](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob#google_cloud_storage_blob_Blob_download_to_file)`   
`[blob.download_to_filename](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob#google_cloud_storage_blob_Blob_download_to_filename)`   
`[blob.download_as_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob#google_cloud_storage_blob_Blob_download_as_string)` See a [code sample](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_download_file.py).  
Delete an object  | ` [blob.delete](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob#google_cloud_storage_blob_Blob_delete) ` See a [code sample](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_delete_file.py).  
Copy an object  | `[bucket.copy_blob](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket#google_cloud_storage_bucket_Bucket_copy_blob) ` See a [code sample](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_copy_file.py).  
Read metadata for an object  | `blob.propertyname`   
and  
`blob.metadata` See a [code sample](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_get_metadata.py).  
  
## Testing your updates

You can test your updates to your app in a local environment, but all Cloud Storage requests must be sent over the internet to an actual Cloud Storage bucket. Neither App Engine nor Cloud Storage provides a Cloud Storage emulator.

For more information about testing Python 3 apps, see [Testing and deploying your application](https://docs.cloud.google.com/appengine/docs/standard/testing-and-deploying-your-app).

## Deploying your app

Once you are ready to deploy your app, you should:

  1. [Test the app on App Engine](https://docs.cloud.google.com/appengine/docs/standard/testing-and-deploying-your-app#testing-on-app-engine).

  2. If the app runs without errors, [use traffic splitting](https://docs.cloud.google.com/appengine/docs/standard/splitting-traffic) to slowly ramp up traffic for your updated app. Monitor the app closely for any issues before routing more traffic to the updated app.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
