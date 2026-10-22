---
url: https://docs.cloud.google.com/cdn/docs/quickstart-backend-bucket-console/
title: Quickstart: Set up a backend bucket as an origin \u00a0|\u00a0 Cloud CDN \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:35:53.329659+00:00
---

# Quickstart: Set up a backend bucket as an origin  |  Cloud CDN  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cdn/docs/quickstart-backend-bucket-console/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud CDN ](https://docs.cloud.google.com/cdn/docs)
  * [ Guides ](https://docs.cloud.google.com/cdn/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Set up a backend bucket as an origin for Cloud CDN

This quickstart shows you how to set up a backend bucket as an origin for Cloud CDN by using the Google Cloud console.

* * *

To follow step-by-step guidance for this task directly in the Google Cloud console, click **Guide me** : 

[Guide me](https://docs.cloud.google.com/cdn/docs/Google%20Cloud%20console/?walkthrough_id=cdn--console_quickstart)

* * *

## Before you begin

Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

  * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
  * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

[Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

  * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
  * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

[Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

### Required roles

To get the permissions that you need to complete this tutorial, ask your administrator to grant you the following IAM roles on your project: 

  * [Storage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)
  * [Compute Load Balancer Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.loadBalancerAdmin) (`roles/compute.loadBalancerAdmin`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a Cloud Storage bucket

_Buckets_ are the basic containers that hold your data in Cloud Storage. 

To create a bucket, follow these steps: 

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. Click add_box **Create**. Show me. 
  3. In the **Name your bucket** section, enter a unique name for your bucket. 

**Warning:** Do not include sensitive information in the bucket name. The bucket namespace is global and publicly visible. 

Click **Continue**. 

  4. In the **Choose where to store your data** section, do the following: 
     1. For **Location type** , select **Region** , and then select `us-east1 (South Carolina)` from the list.
     2. Click **Continue**.
  5. In the **Choose a storage class for your data** section, do the following: 
     1. Select **Set a default class** , and then select **Standard**. 
     2. Click **Continue**.
  6. In the **Choose how to control access to objects** section, do the following: 
     * Clear the **Enforce public access prevention on this bucket** checkbox.
     * For **Access control** , select **Uniform**.
     * Click **Continue**.
  7. In the **Choose how to protect object data** section, keep the selected defaults, and then click **Create** . 



## Upload an object into the bucket

  1. Save the following image on your device:

![The image of a kitten to upload into the bucket.](https://docs.cloud.google.com/static/storage/images/kitten.png)
  2. On the **Bucket details** page, on the **Objects** tab, click **Upload files** . 
  3. In the file dialog, select the file that you downloaded.

After the upload completes, the filename and information about the file, such as its size and file type, are displayed. 

## Make your bucket public

  1. On the **Bucket details** page, click the **Permissions** tab. 
  2. Ensure that the view is set to **View by principals** , and then click **Grant access** .

The **Add principals** pane is displayed.

  3. In the **New principals** field, enter `allUsers`.
  4. In the **Select a role** list, select **Cloud Storage > Storage Object Viewer**.
  5. Click **Save**.
  6. On the **Are you sure you want to make this resource public?** page, click **Allow public access**.
  7. To verify that the object has been shared publicly, click the **Objects** tab to return to the list of objects. Your object's **Public access** column should read **Public to internet**. The **Copy URL** button provides a shareable URL similar to the following: 

`https://storage.googleapis.com/YOUR_BUCKET_NAME/kitten.png`




## Create a backend bucket

To create a backend bucket and an external Application Load Balancer, do the following:

  1. In the Google Cloud console, go to the **Cloud CDN** page. 

[Go to Cloud CDN](https://console.cloud.google.com/net-services/cdn)

  2. Click **Add origin** .

  3. On the **New origin** page, in the **Origin name** section, enter a name for your origin.

  4. For **Origin type** , select **Backend bucket**.

  5. For **Define your backend bucket** , select **New backend bucket**.

  6. In the **Cloud Storage bucket** field, click **Browse**.

  7. Select the Cloud Storage bucket that you created earlier, click **Select** , and then click **Next**.

  8. In the **Attach a load balancer** section, select **Create new load balancer for me** , enter a name for the load balancer, and then click **Next**.

  9. For **Cache performance** , keep the selected defaults, and then click **Done** .

The new origin appears in the list of origins. It might take a few minutes for the origin to be fully created. Proceed to the next step only after you see a notification indicating that the origin has been created.




## Test Cloud CDN

  1. In the Google Cloud console, go to the **Load balancing** page. 

[Go to Load balancing](https://console.cloud.google.com/net-services/loadbalancing/list/loadBalancers)

  2. Click the  name of the load balancer that you created earlier.

The **Load balancer details** page is displayed.

  3. Note the IPv4 addresses displayed under **IP:Port** .

  4. Test Cloud CDN by entering the following URL with the load balancer's IP address in a new browser tab:
         
         http://IP_ADDRESS/kitten.png
         

Your browser should render a page with the uploaded image.

  5. Refresh the page multiple times.

  6. Return to the **Load balancer details** page, and then click **Monitoring**.

  7. After a few minutes, observe the served traffic.

Traffic that is served directly from your backend bucket is labeled **SERVED_FROM_BACKEND_BUCKET**. Traffic that is served from Cloud CDN is labeled **SERVED_FROM_CACHE**. For more information, see [Monitoring metrics](https://docs.cloud.google.com/load-balancing/docs/https/https-logging-monitoring#monitoring_metrics).




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

  1. Delete the load balancer and the backend bucket:

     1. In the Google Cloud console, go to the **Load balancing** page. 

[Go to Load balancing](https://console.cloud.google.com/net-services/loadbalancing/list/loadBalancers)

     2. Select the check box next to the load balancer that you created, and then click **Delete**.

     3. On the page that opens, select the check box next to the backend bucket that you created, and then confirm that you want to delete the load balancer and the selected resources.

  2. Delete the Cloud Storage bucket:

     1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

     2. Select the checkbox next to the bucket that you created, and then click **Delete**. 
     3. In the **Delete bucket** dialog, confirm that you want to delete the bucket, and then click **Delete**.



## What's next

Here's what you can do next:

  * [Set up Cloud CDN](https://docs.cloud.google.com/cdn/docs/using-cdn)
  * [Automate Cloud CDN setup with Terraform](https://docs.cloud.google.com/cdn/docs/cdn-terraform-examples)
  * [Authenticate content](https://docs.cloud.google.com/cdn/docs/private-content)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
