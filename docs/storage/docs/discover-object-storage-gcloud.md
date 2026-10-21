---
url: https://docs.cloud.google.com/storage/docs/discover-object-storage-gcloud/
title: Quickstart: Discover object storage with the Google Cloud CLI \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:33.153382+00:00
---

# Quickstart: Discover object storage with the Google Cloud CLI  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/discover-object-storage-gcloud/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Discover object storage with the Google Cloud CLI

This page shows you how to perform basic tasks in Cloud Storage using the Google Cloud CLI.

Costs that you incur in Cloud Storage are based on the resources you use. This quickstart typically uses less than $0.01 USD worth of Cloud Storage resources.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  3. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  4. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  5. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Grant roles to your user account. Run the following command once for each of the following IAM roles: `roles/storage.admin`
         
         gcloud projects add-iam-policy-binding PROJECT_ID --member="user:USER_IDENTIFIER" --role=ROLE

Replace the following:

     * `PROJECT_ID`: Your project ID.
     * `USER_IDENTIFIER`: The identifier for your user account. For example, `myemail@example.com`. 
     * `ROLE`: The IAM role that you grant to your user account.

  8. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  9. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  10. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  11. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  12. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  13. Grant roles to your user account. Run the following command once for each of the following IAM roles: `roles/storage.admin`
         
         gcloud projects add-iam-policy-binding PROJECT_ID --member="user:USER_IDENTIFIER" --role=ROLE

Replace the following:

     * `PROJECT_ID`: Your project ID.
     * `USER_IDENTIFIER`: The identifier for your user account. For example, `myemail@example.com`. 
     * `ROLE`: The IAM role that you grant to your user account.


**Note:** If you are using Cloud Shell or a Compute Engine instance, the Google Cloud SDK is pre-installed and authenticated. If your Compute Engine instance is set up without a service account scope to Cloud Storage, run `gcloud init` and follow the instructions.

## Create a bucket

_Buckets_ are the basic containers that hold your data in Cloud Storage.

To create a bucket:

  1. Open a terminal window.
  2. Use the `gcloud storage buckets create` command and a globally unique name to create a bucket:
         
         gcloud storage buckets create gs://BUCKET_NAME/ --uniform-bucket-level-access

Replace `BUCKET_NAME` with a name for your bucket.

**Caution:** Don't include sensitive information in the bucket name, because the bucket namespace is global and publicly visible.See bucket naming requirements.
     * Bucket names can only contain lowercase letters, numeric characters, dashes (`-`), underscores (`_`), and dots (`.`). Spaces are not allowed. Names containing dots require [verification](https://docs.cloud.google.com/storage/docs/domain-name-verification).
     * Bucket names must start and end with a number or letter.
     * Bucket names must contain 3-63 characters. Names containing dots can contain up to 222 characters, but each dot-separated component can be no longer than 63 characters.
     * Bucket names cannot be represented as an IP address in dotted-decimal notation (for example, 192.168.5.4).
     * Bucket names cannot begin with the "goog" prefix.
     * Bucket names cannot contain "google" or close misspellings, such as "g00gle".

If successful, the command returns a response like the following:
    
    Creating gs://my-awesome-bucket/...

If the bucket name that you chose is already in use, either by you or someone else, the command returns a response like `ServiceException: 409 Bucket my-awesome-bucket already exists.` Try again with a different bucket name.




You've just created a bucket where you can store your data!

## Upload an object into your bucket

  1. Save the following image to your computer, such as on the desktop.

![A kitten with its paws outstretched.](https://docs.cloud.google.com/static/storage/images/kitten.png)

**Note:** If you are using Cloud Shell or a Compute Engine instance, download the image using the following command: `wget https://docs.cloud.google.com/storage/images/kitten.png`

The image is saved to a location in the current directory, such as `~/kitten.png`.

  2. Use the `gcloud storage cp` command to copy the image from the location where you saved it to the bucket that you created:
         
         gcloud storage cp OBJECT_LOCATION gs://BUCKET_NAME

Replace `OBJECT_LOCATION` with the location where you saved the image, such as `Desktop/kitten.png`.

**Tip:** When typing your bucket name, you can use the tab key to autocomplete it.

If successful, the command returns a response like the following:
         
         Copying file://Desktop/kitten.png to gs://my-awesome-bucket/kitten.png
           Completed files 1/1 | 8.6kiB/8.6kiB

You've just stored an object in your bucket.




## Download the object from your bucket

  1. Use the `gcloud storage cp` command to download the image that you stored in your bucket to somewhere on your computer, such as the desktop:
         
         gcloud storage cp gs://BUCKET_NAME/kitten.png Desktop/kitten2.png

If successful, the command returns a response like the following:
         
         Copying gs://my-awesome-bucket/kitten.png to file://Desktop/kitten2.png
           Completed files 1/1 | 8.6kiB/8.6kiB 

You've just downloaded something from your bucket.




## Copy the object to a simulated folder in the bucket

  1. Use the `gcloud storage cp` command to create a simulated folder and copy the image into it:
         
         gcloud storage cp gs://BUCKET_NAME/kitten.png gs://BUCKET_NAME/quickstart-folder/kitten3.png

**Note:** [Simulated folders in Cloud Storage have limitations](https://docs.cloud.google.com/storage/docs/objects#namespace) compared to local file systems or folders in buckets that have hierarchical namespace enabled, but many of the same operations are supported.

If successful, the command returns a response like the following:
         
         Copying gs://my-awesome-bucket/kitten.png to gs://my-awesome-bucket/quickstart-folder/kitten3.png
           Completed files 1/1 | 8.6kiB/8.6kiB 

You've just copied your image into a new simulated folder in your bucket.




## List contents of a bucket

  1. Use the `gcloud storage ls` command to list the contents at the top level of your bucket:
         
         gcloud storage ls gs://BUCKET_NAME

If successful, the command returns a response like the following:
         
         gs://my-awesome-bucket/kitten.png
         gs://my-awesome-bucket/quickstart-folder/

You've just seen the contents at the top level of your bucket.




## List details for an object

  1. Use the `gcloud storage ls` command with the `--long` flag to get some details about one of your images:
         
         gcloud storage ls gs://BUCKET_NAME/kitten.png --long

If successful, the command returns a response like the following:
         
         8775  2026-01-21T01:22:17Z  gs://srs-bucketcli/kitten.png
         TOTAL: 1 objects, 8775 bytes (8.57kiB)

You've just obtained information about the image's size and date of creation.




## Make the objects publicly accessible

  1. Use the `gcloud storage buckets add-iam-policy-binding` command to grant all users permission to read the images stored in your bucket:
         
         gcloud storage buckets add-iam-policy-binding gs://BUCKET_NAME --member=allUsers --role=roles/storage.objectViewer

The command is successful if your response contains the following:
         
         bindings:
           - members:
             - allUsers
             role: roles/storage.objectViewer
         

Now anyone can get your images.

  2. To remove this access, use the following command:
         
         gcloud storage buckets remove-iam-policy-binding gs://BUCKET_NAME --member=allUsers --role=roles/storage.objectViewer

The command is successful if no error is returned.

You have removed public access to the images in your bucket.


**Note:** After you remove public access, you may still be able to access a cached version of your images for a period of time.

## Give someone access to your bucket

  1. Use the `gcloud storage buckets add-iam-policy-binding` command to give a specific email address permission to add objects to your bucket:
         
         gcloud storage buckets add-iam-policy-binding gs://BUCKET_NAME --member=user:jeffersonloveshiking@gmail.com --role=roles/storage.objectCreator

The command is successful if your response contains the following:
         
         bindings:
           - members:
             - user:jeffersonloveshiking@gmail.com
             role: roles/storage.objectCreator
         

Now this user can add items to your bucket.

  2. To remove this permission, use the following command:
         
         gcloud storage buckets remove-iam-policy-binding gs://BUCKET_NAME --member=user:jeffersonloveshiking@gmail.com --role=roles/storage.objectCreator

The command is successful if no error is returned.

You have removed the user's access to this bucket.




## Delete an object

  1. Use the `gcloud storage rm` command to delete one of your images:
         
         gcloud storage rm gs://BUCKET_NAME/kitten.png

If successful, the command returns a response like the following:
         
         Removing gs://my-awesome-bucket/kitten.png...

This copy of the image is no longer stored on Cloud Storage (though the copy you made in the simulated folder `quickstart-folder/` still exists).




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, delete the Google Cloud project with the resources. 

  1. Use the `gcloud storage rm` command with the `--recursive` flag to delete the bucket and anything inside of it:
         
         gcloud storage rm gs://BUCKET_NAME --recursive

If successful, the command returns a response like the following:
         
         Removing objects:
         Removing gs://my-awesome-bucket/quickstart-folder/kitten3.png#1768960201129254
           Completed 1/1
         Removing buckets:
         Removing gs://my-awesome-bucket/...
           Completed 1/1

Your bucket and its contents are deleted. 




## What's next

  * [Work through the Cloud Storage Quickstart using the Google Cloud console](https://docs.cloud.google.com/storage/docs/quickstart-console).
  * Read the [Cloud Storage product overview](https://docs.cloud.google.com/storage/docs/introduction). 
  * Learn about [Cloud Storage pricing](https://docs.cloud.google.com/storage/pricing). 
  * See the reference pages for gcloud CLI commands. For example: 
    * [Create buckets (`buckets create`)](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/create)
    * [Upload, download, and copy objects (`cp`)](https://docs.cloud.google.com/sdk/gcloud/reference/storage/cp)
    * [List buckets and objects (`ls`)](https://docs.cloud.google.com/sdk/gcloud/reference/storage/ls)
    * [Add access to buckets (`buckets add-iam-policy-binding`)](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/add-iam-policy-binding)
    * [Delete objects and buckets (`rm`)](https://docs.cloud.google.com/sdk/gcloud/reference/storage/rm)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
