---
url: https://docs.cloud.google.com/storage/docs/discover-object-storage-console/
title: Quickstart: Discover object storage with the Google Cloud console \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:10:49.196470+00:00
---

# Quickstart: Discover object storage with the Google Cloud console  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/discover-object-storage-console/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Discover object storage with the Google Cloud console

Learn how to get started with Cloud Storage using the Google Cloud console.

Costs that you incur in Cloud Storage are based on the resources you use. This quickstart typically uses less than $0.01 USD worth of Cloud Storage resources.

* * *

To follow step-by-step guidance for this task directly in the Google Cloud console, click **Guide me** : 

[Guide me](https://console.cloud.google.com/?walkthrough_id=storage--quickstart-basic-tasks)

* * *

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Make sure that you have the following role or roles on the project: Storage Admin 

#### Check for the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
     2. Select the project. 
     3. In the **Principal** column, find all rows that identify you or a group that you're included in. To learn which groups you're included in, contact your administrator. 

     4. For all rows that specify or include you, check the **Role** column to see whether the list of roles includes the required roles. 

#### Grant the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
     2. Select the project. 
     3. Click person_add **Grant access**. 
     4. In the **New principals** field, enter your user identifier. This is typically the email address for a Google Account.

     5. Click **Select a role** , then search for the role. 
     6. To grant additional roles, click add **Add another role** and add each additional role. 
     7. Click **Save**. 

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Make sure that you have the following role or roles on the project: Storage Admin 

#### Check for the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
     2. Select the project. 
     3. In the **Principal** column, find all rows that identify you or a group that you're included in. To learn which groups you're included in, contact your administrator. 

     4. For all rows that specify or include you, check the **Role** column to see whether the list of roles includes the required roles. 

#### Grant the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
     2. Select the project. 
     3. Click person_add **Grant access**. 
     4. In the **New principals** field, enter your user identifier. This is typically the email address for a Google Account.

     5. Click **Select a role** , then search for the role. 
     6. To grant additional roles, click add **Add another role** and add each additional role. 
     7. Click **Save**. 




## Create a bucket

_Buckets_ are the basic containers that hold your data in Cloud Storage.

To create a bucket:

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. Click add_box **Create**.

  3. In the **Get started** section, enter a globally unique name for your bucket.

**Caution:** Don't include sensitive information in the bucket name, because the bucket namespace is global and publicly visible.See bucket naming requirements.
     * Bucket names can only contain lowercase letters, numeric characters, dashes (`-`), underscores (`_`), and dots (`.`). Spaces are not allowed. Names containing dots require [verification](https://docs.cloud.google.com/storage/docs/domain-name-verification).
     * Bucket names must start and end with a number or letter.
     * Bucket names must contain 3-63 characters. Names containing dots can contain up to 222 characters, but each dot-separated component can be no longer than 63 characters.
     * Bucket names cannot be represented as an IP address in dotted-decimal notation (for example, 192.168.5.4).
     * Bucket names cannot begin with the "goog" prefix.
     * Bucket names cannot contain "google" or close misspellings, such as "g00gle".
  4. In the **Choose where to store your data** section, for **Location type** , select **Region**. Use the default value in this field.

  5. In the **Choose how to store your data** section, use the default values.

  6. In the **Choose how to control access to objects** section, clear the **Enforce public access prevention on this bucket** checkbox. This lets you share the object later.

  7. In the **Choose how to protect object data** section, use the default values.

  8. Click **Create**.




That's it — you've just created a Cloud Storage bucket!

## Upload an object into the bucket

  1. Save the following image to your device.

![A kitten with its paws outstretched.](https://docs.cloud.google.com/static/storage/images/kitten.png)

  2. On the **Bucket details** page, on the **Objects** tab, click **Upload**. Then, select **Upload files**.

  3. On your device, locate and select the image that you previously saved.




After the upload completes, you should see the filename and information about the file, such as its size and type.

## Download the object

To download the image from your bucket, click download**Download**.

## Share the object

To allow public access to the bucket and create a publicly accessible URL for the image:

  1. Click the **Permissions** tab.

  2. Click **Grant Access**.

  3. In the **New principals** field, enter `allUsers`.

  4. In the **Select a role** list, select **Cloud Storage**. Then, select **Storage Object Viewer**.

  5. Click **Save**.

  6. In the **Are you sure you want to make this resource public?** dialog, click **Allow public access**.

To verify, click the **Objects** tab to return to the list of objects. The object's **Public access** column should read **Public to internet**. The **Copy URL** button provides a shareable URL similar to the following: `https://storage.googleapis.com/YOUR_BUCKET_NAME/kitten.png`




To remove public access from the bucket and stop sharing the image publicly:

  1. Click the **Permissions** tab.

  2. In the **Principal** column, locate the **allUsers** principal, and then select the checkbox associated with it.

  3. Click the **Remove Access** button, and then confirm when prompted.

On the **Objects** tab, you should see that the image no longer has a **Copy URL** button.


**Note:** After you remove public access to the image, you might be able to access a cached version of it for a period of time.

## Create a simulated folder

  1. On the **Objects** tab, click **Create folder**.

  2. In the **Name** field, enter `quickstart-folder`.

  3. Click **Create**.

The simulated folder appears in the bucket, with a folder icon that distinguishes it from objects.

  4. To upload a file to the simulated folder, do the following:

     1. Click **quickstart-folder**.

     2. Click **Upload** , and then select **Upload files**.

     3. On your device, locate and select the image that you previously saved.

After the upload completes, you should see the filename and information about the file, such as its size and type.




## Delete the objects

  1. In the **Folder browser** panel, click the name of your bucket.

  2. Select the checkbox next to **quickstart-folder**.

  3. Click **Delete** , and then confirm when prompted.

The simulated folder and all objects in it are deleted.




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. Select the checkbox next to the bucket that you created.

  3. Click **Delete** , and then confirm when prompted.




## What's next

  * [Work through the Cloud Storage quickstart using the Google Cloud CLI](https://docs.cloud.google.com/storage/docs/discover-object-storage-gcloud).
  * Read the [Cloud Storage product overview](https://docs.cloud.google.com/storage/docs/introduction).
  * Learn about [storage classes](https://docs.cloud.google.com/storage/docs/storage-classes). 
  * Learn about [Cloud Storage pricing](https://cloud.google.com/storage/pricing). 
  * Get started with the [Cloud Storage client libraries](https://docs.cloud.google.com/storage/docs/reference/libraries).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
