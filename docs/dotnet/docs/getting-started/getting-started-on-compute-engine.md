---
url: https://docs.cloud.google.com/dotnet/docs/getting-started/getting-started-on-compute-engine/
title: Getting started with .NET on Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:01:22.567899+00:00
---

# Getting started with .NET on Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/getting-started/getting-started-on-compute-engine/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)



Send feedback 

#  Getting started with .NET on Compute Engine Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial shows how to get started with Compute Engine. Follow this tutorial by deploying a Hello World .NET web app to Compute Engine. For help getting started with App Engine, see the [App Engine standard environment](https://docs.cloud.google.com/dotnet/getting-started/tutorial-app).

## Objectives

  * Deploy a Hello World sample app to a single Compute Engine instance. 



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [Compute Engine](https://cloud.google.com/compute/all-pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Compute Engine API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=compute)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Compute Engine API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=compute)

  8. Install [.NET Core SDK 2.1](https://dotnet.microsoft.com/download/dotnet-core/2.1) or later on your local machine running [Microsoft Windows](https://www.microsoft.com/en-us/windows). 

  9. Install [Web Deploy 3.6](https://www.iis.net/downloads/microsoft/web-deploy) or later on your local machine running [Microsoft Windows](https://www.microsoft.com/en-us/windows). 



## Running the app locally

  1. [Download and unzip](https://github.com/GoogleCloudPlatform/getting-started-dotnet/archive/master.zip) or clone the sample repository from github:
         
         git clone https://github.com/GoogleCloudPlatform/getting-started-dotnet.git
         

  2. In a PowerShell window, go into the `HelloWorld` directory:
         
         cd getting-started-dotnet\HelloWorld
         

  3. Start a local web server:
         
         dotnet run
         

  4. Open a web browser to `localhost:8080`.

In your web browser, you see some Hello World text, served from your local machine.

  5. When you're ready to move on, stop the local web server by pressing `Control+C`.




## Deploying to a single instance

This section walks you through running a single instance of your app on Compute Engine.

![Single-instance deployment.](https://docs.cloud.google.com/static/languages/images/compute-single-instance.svg)

### Create and configure a Compute Engine instance

From Google Cloud Marketplace, you can launch an instance of Windows running Microsoft IIS on Compute Engine.

  1. In the Google Cloud console, go to the **ASP.NET Framework** Cloud Marketplace page.

[Go to Cloud Marketplace](https://docs.cloud.google.com/console/marketplace/details/click-to-deploy-images/aspnet)

  2. Click **Launch**.

  3. Leave the settings set to their default values, and click **Deploy**.

Wait for the Compute Engine instance to deploy. It usually takes about 5 minutes to deploy.

  4. To display resource information, click **VM instance**.

  5. To edit the VM instance, click **Manage Resource**.

  6. Click **Set Windows password** , and then make a note of the username.

  7. Copy the new Windows password, and then click **Close**.

  8. In the **VM instance details** page, make a note of the external IP address.

  9. On your local Windows machine, edit the file `HelloWorld/Properties/PublishProfiles/ComputeEngine.pubxml`.

  10. Enter your VM instance's external IP address between `<MSDeployServiceURL>` and `</MSDeployServiceURL>`. For example, `<MSDeployServiceURL>203.0.113.22</MSDeployServiceURL>`

  11. Enter the instance's username that you previously noted between `<UserName>` and `</UserName>`.

  12. Save your changes to the `ComputeEngine.pubxml` file.

  13. In a PowerShell window, publish your app to the Compute Engine instance:
         
         dotnet publish -c Release `
           /p:PublishProfile=Properties\PublishProfiles\ComputeEngine.pubxml `
           "/p:Password=YOUR-PASSWORD"
         

Replace `YOUR-PASSWORD` with the password you previously copied.

  14. Open a web browser to your instance's external IP address.

In your web browser, you see some Hello World text, served from your Compute Engine instance.




### Manage and monitor an instance

You can use the Google Cloud console to monitor and manage your instance.

  1. To view all of the logs generated by your Compute Engine resources, go to the **Logs Explorer** page.

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

[Cloud Logging](https://docs.cloud.google.com/logging) is automatically configured to gather logs from various common services, including `syslog`. 




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

### Delete the project

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



### Delete the individual resources
    
    
    gcloud compute instances delete my-app-instance --zone=YOUR_ZONE --delete-disks=all
    gcloud compute firewall-rules delete default-allow-http-80

## What's next

  * Explore reference architectures, diagrams, and best practices about Google Cloud. Take a look at our [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 

  * For other .NET resources for building your apps, see the following:

    * Manage and monitor your Instance Group deployment at [Compute Engine > Instance groups](https://console.cloud.google.com/compute/instanceGroups).
    * Manage your load balancing configuration, including URL maps and backend services, at [Network services > Load balancing](https://console.cloud.google.com/net-services/loadbalancing/list). 
    * [Deploy an app to Google Kubernetes Engine](https://docs.cloud.google.com/kubernetes-engine/docs/quickstarts/deploy-app-container-image)
    * Explore other [Google Cloud services](https://docs.cloud.google.com/). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
