---
url: https://docs.cloud.google.com/dataproc-metastore/docs/api-explorer/
title: Use the API Explorer \u00a0|\u00a0 Dataproc Metastore \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:39:18.393143+00:00
---

# Use the API Explorer  |  Dataproc Metastore  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataproc-metastore/docs/api-explorer/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Dataproc Metastore ](https://docs.cloud.google.com/dataproc-metastore/docs)
  * [ Reference ](https://docs.cloud.google.com/dataproc-metastore/docs/reference)



Send feedback 

#  Use the API Explorer Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to use the API Explorer to try out Dataproc Metastore API methods. API Explorer is a widget attached to the REST API reference page for a method. It appears as a panel with the title **Try this API**.

The API Explorer is an excellent way to try out methods in the Dataproc Metastore API without having to write any code. The widget presents a form showing the parameters for each method. Fill in the form, click **Execute** , and see the results.

You can also hide the widget by clicking the close button at the top of the panel, or expand it to full screen by clicking the full screen button.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. Enable the Dataproc Metastore API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=metastore.googleapis.com)

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. Enable the Dataproc Metastore API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=metastore.googleapis.com)




## Access the API Explorer

The API Explorer is attached to the reference page for each REST API method. To find the widget, go to the reference page for a method, for example, the [reference page for Dataproc Metastore `projects.locations.services.create`](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services/create).

## Execute a minimal request

Most methods have some required parameters and some optional ones. The required ones are marked with a red bar until they are filled. You can execute a minimal request by supplying only the required arguments.

The `services.create` method creates a Dataproc Metastore service in a chosen project and location. The required fields are the **parent** and **serviceId** fields. To create a service, supply the project number and location ID of your project for **parent** using the form `projects/{projectNumber}/locations/{locationId}`. And supply the service ID for **serviceId**.

[Try It!](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services/create?apix_params=%7B%22parent%22%3A%22projects%2F%7BprojectNumber%7D%2Flocations%2F%7BlocationId%7D%22%7D)

The results of the method invocation appear in a box under the **Execute** button. Typically, the box has a green header with the HTTP status code `200` in it, indicating the request succeeded.

If the header is red and contains an HTTP failure code, the box contains the error message. See Tips for pointers on resolving errors.

## Supply additional parameters

The list of parameters you see depends on the method to which the API Explorer widget is attached. The `services.create` method has more than just the **parent** and **serviceId** parameters, but they are the only required parameters.

You can use the optional **requestId** parameter to specify a unique request ID to allow the server to ignore the request if it has completed.

## Use **fields** to limit output further

By default, the set of parameters that API Explorer shows corresponds to the parameters of the associated method. However, the API Explorer widget also has a set of extra fields that are not available via the method itself.

These parameters are hidden under the toggle **Show standard parameters**.

Click this toggle to expose the extra widget parameters. Click **Hide standard parameters** to hide them from view.

The most useful of these standard parameters is the **fields** parameter, which lets you select the fields in the returned output that you want to see. This is very useful in the API Explorer panel, where the output is displayed in a box. There is often a lot of output to scroll through.

## Tips

The following sections contain API Explorer tips.

### Remember to change `{projectNumber} and {locationId}`

Do not forget to replace `{projectNumber} and {locationId}` with your project's number and location ID. Note that the API also accepts the project ID in place of the number.

### Problems with the values

Here are some issues to watch for when using the API Explorer forms. These mistakes might cause errors or might be accepted but be treated like spelling errors in the API method:

  * Don't use quotation marks around field values of any type.
  * Be sure to quote strings appearing inside filters. Use double quotation marks (`"`) and not apostrophes (`'`).
  * Don't use backslashes or URL-encoding in form fields. If needed, URL-encoding is performed on the field values when you execute the method.
  * Look at the value in the result box after executing the call. You might notice the problem there.
  * Supply a value for the **pageSize** field, such as `2`. This limits the amount of data that is returned as you debug your API call.



### Bookmark URLs for debugging

After you get the output you want, bookmark the API Explorer URL. When you want to run the method again, paste the URL into your browser. You see the form already populated with your values. Make any necessary changes to the parameters, and click **Execute** to run the method again.

### Authentication

There is a **Credentials** section on the API Explorer page, above the **Execute** button. You typically don't need to change anything here.

The default authentication mechanism is `Google OAuth 2.0`.

There is also a **Show scopes** toggle in the **Credentials** section. This shows you which Compute Engine scopes you have available. By default, all available scopes are enabled.

## What's next

  * [Dataproc Metastore API](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest)
  * [Enable the API](https://docs.cloud.google.com/dataproc-metastore/docs/enable-service)
  * [Quickstart for deploying Dataproc Metastore](https://docs.cloud.google.com/dataproc-metastore/docs/create-service-cluster)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
