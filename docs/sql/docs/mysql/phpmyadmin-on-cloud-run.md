---
url: https://docs.cloud.google.com/sql/docs/mysql/phpmyadmin-on-cloud-run/
title: Use phpMyAdmin with Cloud SQL on Cloud Run \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:11:47.468898+00:00
---

# Use phpMyAdmin with Cloud SQL on Cloud Run  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/phpmyadmin-on-cloud-run/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Use phpMyAdmin with Cloud SQL on Cloud Run Stay organized with collections  Save and categorize content based on your preferences. 

This guide show how to install [phpMyAdmin](https://docs.phpmyadmin.net/en/latest/intro.html) on Cloud Run. You can use phpMyAdmin to administer Cloud SQL over the web. 

You will find this tutorial helpful if you:

  * Host applications on Cloud Run.
  * Use [Cloud SQL](https://docs.cloud.google.com/sql/docs) as your database.
  * Want to use phpMyAdmin as an interface for MySQL or prefer a web interface for database administration.



## Objectives

  * Learn how to deploy phpMyAdmin on Cloud Run.



## Costs

This tutorial uses billable components of Google Cloud, including:

  * [Cloud Run](https://cloud.google.com/run/pricing)
  * [Cloud SQL](https://cloud.google.com/sql/pricing)



To generate a cost estimate based on your projected usage, use the [Pricing Calculator](https://cloud.google.com/products/calculator). 

New Cloud Platform users might be eligible for a Google Cloud [free trial](https://cloud.google.com/free). 

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. [Install](https://docs.cloud.google.com/sdk/docs/install) the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud). 

  5. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  6. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  7. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  8. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  9. [Install](https://docs.cloud.google.com/sdk/docs/install) the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud). 

  10. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  11. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  12. Create a [Cloud SQL Second Generation instance](https://docs.cloud.google.com/sql/docs/mysql/create-instance#create-2nd-gen) with a [private IP](https://docs.cloud.google.com/sql/docs/mysql/configure-private-ip).
  13. Create a [database user](https://docs.cloud.google.com/sql/docs/mysql/create-manage-users#creating).




## Create a service using the phpMyAdmin image

### Console

  1. In the Google Cloud console, go to Cloud Run:

[Go to Cloud Run](https://console.cloud.google.com/run)

  2. Select **Create service**.

     1. In the **Container image** URL field, enter `phpmyadmin`. Cloud Run pulls the image from the public [Docker Hub](https://hub.docker.com/_/phpmyadmin).
     2. In the **Service name** field, enter `phpmyadmin`.
     3. Check `Require authentication`.
     4. Click **Container(s), volumes, networking, security** to set the following options: 
        1. In the **Port** field, enter `80` for the value of the container port.
        2. In **Environment variables** , add `PMA_HOST` and set the value to be the internal IP address of the Cloud SQL instance.
     5. In **Networking** , select **Connect to a VPC for outbound traffic** and **Send traffic directly to a VPC**. Choose the same network as the Cloud SQL instance.

**Note:** You can also use a Serverless VPC Access instead of routing traffic directly to a VPC. In the [comparison table](https://docs.cloud.google.com/run/docs/configuring/connecting-vpc#comparison-table), learn the difference between the two ways.



## Connect to the service using Cloud Run proxy

To securely access the IAM-protected service, use the Cloud Run developer proxy.

**Important:** We don't recommend exposing phpMyAdmin to the public internet directly. If you prefer an alternative to the local proxy, you can configure [IAP](https://docs.cloud.google.com/iap/docs/enabling-cloud-run) to enforce user authentication.

  1. To start the proxy on the previously created service, use the following command:
         
         gcloud run services proxy phpmyadmin --port=8080
         

If [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) prompts you to install the `cloud-run-proxy` components, then enter `Y`.

  2. To test the setup, enter the URL and port number (for example, `http://127.0.0.1:8080/`), and then with the username (admin name) and password. Since you're using the local Cloud Run developer proxy to access the service securely, you might see an error message, which can be ignored: `There is a mismatch between HTTPS indicated on the server and client`.




## Troubleshoot

To obtain information about Cloud Run errors, access the [Cloud Run logs](https://console.cloud.google.com/logs) in the [Google Cloud console](https://console.cloud.google.com/).

## Clean up

After you finish the tutorial, you can clean up the resources that you created so that they stop using quota and incurring charges. The following sections describe how to delete or turn off these resources. 

### Delete the project

The easiest way to eliminate billing is to delete the project that you created for the tutorial. 

To delete the project: 

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



### Delete instances

To delete a Cloud SQL instance: 

  1. In the Google Cloud console, go to the **Instances** page. 

[Go to Instances](https://console.cloud.google.com/sql/instances)

  2. Click the name of the SQL instance you that want to delete. 
  3. To delete the instance, click delete **Delete** , and then follow the instructions. 



## What's next

  * [Learn more about phpMyAdmin](http://www.phpmyadmin.net/home_page/docs.php).
  * Explore reference architectures, diagrams, and best practices about Google Cloud. Take a look at our [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
