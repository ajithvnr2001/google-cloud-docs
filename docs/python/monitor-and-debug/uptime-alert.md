---
url: https://docs.cloud.google.com/python/monitor-and-debug/uptime-alert/
title: Setting an uptime alert \u00a0|\u00a0 Python \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:24:49.142667+00:00
---

# Setting an uptime alert  |  Python  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/monitor-and-debug/uptime-alert/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Guides ](https://docs.cloud.google.com/python/docs/setup)



Send feedback 

#  Setting an uptime alert Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial shows how to set up an uptime alert for the [Python Hello World app](https://docs.cloud.google.com/python/getting-started/hello-world) running on App Engine flexible environment using [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs). Uptime alerts let you know when your app is not serving traffic. You can also set uptime alerts for apps running on [Compute Engine](https://docs.cloud.google.com/compute) or [Google Kubernetes Engine (GKE)](https://docs.cloud.google.com/kubernetes-engine).

## Objectives

  * Run a basic Hello World app.
  * Create an uptime check that monitors whether the app returns an HTTP '200' status code.
  * Create an alert that sends an email message to you when the uptime check fails.
  * Restart the app to trigger the alert.



## Costs

**Important:** In this document, you use the following billable components of Google Cloud: 

  * [App Engine](https://cloud.google.com/appengine/pricing)
  * [Cloud Monitoring](https://cloud.google.com/stackdriver/pricing)

To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

Monitoring is currently offered to beta users at no charge.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 




## Cloning the sample app

The sample app is available on GitHub at [`GoogleCloudPlatform/getting-started-python`](https://github.com/GoogleCloudPlatform/getting-started-python).

  1. Clone the repository.
         
         git clone https://github.com/GoogleCloudPlatform/getting-started-python.git
         

  2. Go to the sample directory.
         
         cd getting-started-python/gce
         

  3. Because the app only returns "Hello World!", it requires no configuration, and you can run it right away.
         
         gcloud app deploy
         

  4. To see the returned message, enter the following URL in your browser:

`https://PROJECT_ID.REGION_ID.r.appspot.com`

Replace the following:

     * `PROJECT_ID`: Your Google Cloud project ID
     * `REGION_ID`: A [code that App Engine assigns to your app](https://docs.cloud.google.com/appengine/docs/standard/python3/how-requests-are-routed#region-id)



## Creating an uptime check

After you deploy your app, you can use Monitoring to create an uptime check. The check continually pings your deployed app to ensure that it's returning a healthy response.

  1. In the Google Cloud console, go to the ![](https://docs.cloud.google.com/static/monitoring/images/uptime-check-icon.png) **Uptime checks** page: 

[Go to **Uptime checks**](https://console.cloud.google.com/monitoring/uptime)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Click **Create Uptime Check**.
  3. Give your check a title, such as `Check Hello World`, and then click **Next**.

  4. In the **Target** section, you specify what the uptime check is to monitor:

     1. Because you deployed to App Engine, change **Resource Type** to **App Engine** instead of **URL**. (**URL** is for generating a custom URL on a Compute Engine instance.)
     2. Select the **Service** to be monitored by the uptime check.
     3. Leave **Path** blank to default to the main index page.
     4. Leave **Check frequency** at the default of **1** minute.
     5. Click **Next**.
  5. Leave the **Response Validation** fields at their default values and click **Next**.

  6. In the **Alert & Notification** section, you specify how you are notified if an alert occurs:

     * Ensure that the toggle's label is **Alerting is enabled**.
     * Leave the name and duration fields at their default values.
     * To add a notification channel to the alerting policy, in the text box labeled **Notification channels** , click **Menu**. Select the channels to add and click **OK**. The notifications are grouped alphabetically for each channel type.

To add an entry to the checkbox list, click **Manage notification channels** and follow the instructions. When you return to this dialog, click **Refresh** _refresh_.

  7. Click **Create**. When the create action is successful, the message **Check and alert created** is displayed and then the **Uptime checks** dashboard page is displayed.

In the uptime checks dashboard, your new uptime check is listed. If you click the check name, then you open the detail view for that uptime check. This view displays several charts, shows the uptime percentage and the configuration information, and lists the configured alert policies. To view a policy, click its name.

You can also view the alert policy by starting at the **Alerting** page. From the alerting page, the **Policies** pane lists a subset of policies. To view a list of all policies, click **See all policies**.




## Simulating an outage

Now that the uptime check is created, you can simulate an outage by changing your app to respond with an HTTP `404 Sorry, we can't find that page` error rather than an HTTP `200 OK` response.

  1. The following code shows where the Hello World app returns only a 'Hello World!' message, and that the status code of the response defaults to `200 OK`. To view this code in the Hello World app, use the view function.
         
         # Copyright 2019 Google LLC All Rights Reserved.
         #
         # Licensed under the Apache License, Version 2.0 (the "License");
         # you may not use this file except in compliance with the License.
         # You may obtain a copy of the License at
         #
         #     http://www.apache.org/licenses/LICENSE-2.0
         #
         # Unless required by applicable law or agreed to in writing, software
         # distributed under the License is distributed on an "AS IS" BASIS,
         # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
         # See the License for the specific language governing permissions and
         # limitations under the License.
         
         from flask import Flask
         app = Flask(__name__)
         
         
         @app.route('/', methods=['GET'])
         def say_hello():
             return "Hello, world!"
         
         
         if __name__ == '__main__':
             app.run(host='127.0.0.1', port=8080, debug=True)
         

  2. To cause the Hello World app to return an HTTP `404` error code, change the return line by adding a `404` value to the second part of the return value.
         
         return 'Hello World', 404

  3. Deploy the new, intentionally broken app.
         
         gcloud app deploy

Within half an hour, you'll receive an email message that states that your uptime check is failing.




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

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

< Prev [Next >](https://docs.cloud.google.com/python/monitor-and-debug/reporting-errors)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
