---
url: https://docs.cloud.google.com/appengine/docs/managing-costs/
title: Manage App Engine costs \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:23:13.797310+00:00
---

# Manage App Engine costs  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/managing-costs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Resources ](https://docs.cloud.google.com/appengine/docs/standard/resources)



Send feedback 

#  Manage App Engine costs Stay organized with collections  Save and categorize content based on your preferences. 

With App Engine, you only pay for the resources that you use beyond the [free quotas](https://docs.cloud.google.com/appengine/docs/standard/quotas). After you exceed the free quotas, your costs scale with the amount of traffic that your application receives.

To limit the costs of your App Engine app, you can use any of the following mechanisms:

  * Specify the maximum number of instances
  * Create budget alerts
  * Disable your app manually
  * Disable your app programmatically



## Specify the maximum number of instances

Since App Engine costs usually scale based on the amount of traffic your app receives, you can limit your costs by limiting the [number of instances](https://docs.cloud.google.com/appengine/docs/standard/how-instances-are-managed) App Engine can create.

Setting the maximum to 1 instance usually keeps your instance hour usage within the free tier. However, **setting the maximum too low may prevent your app from having enough instances to adequately serve incoming requests**.

To specify the maximum number of instances, use the [`max_instances` setting](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml#scaling_elements) in your app's `app.yaml` file.

**Important:** App Engine applies the `max_instances` setting on a best effort basis. **In some circumstances, App Engine may briefly exceed the limit you specify.**

## Create budget alerts

Budget alerts send a notification when your costs rise above a threshold you specify. When you receive a notification, you can limit costs by lowering the value of the `max_instances` setting or disabling your app.

To get started with budget alerts, see [Set budget alerts](https://docs.cloud.google.com/billing/docs/how-to/budgets).

### Select the scope of a budget alert

You can create budget alerts for the total cost of all Google Cloud services in one or more projects, or just for the cost of App Engine.

To create a budget alert just for costs from App Engine, in the Budget alert's Products field, select **App Engine**. The alert will trigger when the total cost from all App Engine resources exceed the amount you specify, including:

  * Instance hours in the App Engine standard environment
  * Instance hours and RAM in the App Engine flexible environment
  * Bundled App Engine services



For the full list of billable App Engine resources, see [App Engine SKUs](https://docs.cloud.google.com/skus?filter=App+Engine).

## Disable your app manually

Disabling your app temporarily stops it from serving and incurring billing charges related to serving your app. All of your app's data and configuration settings remain unchanged, and when you are ready to start running your app again, you can enable it.

While the app is disabled, requests to your app will fail. You may continue to incur charges from other Google Cloud products. For example, if your project has exceeded the [free quota for Cloud Storage](https://docs.cloud.google.com/appengine/docs/standard/quotas#Default_Gcs_Bucket), you will continue to incur charges for storage.

For more information, see [Disable an app](https://docs.cloud.google.com/appengine/docs/standard/managing-projects-apps-billing#disabling_an_application).

## Disable your app programmatically

You can use Budget Alerts, Pub/Sub, and Cloud Run functions to automatically disable your app when your costs exceed a threshold you specify.

As with manually disabling an app:

  * All of your app's data and configuration settings remain unchanged.
  * When you are ready to start running your app again, you can enable it.
  * Requests to your app will fail while the app is disabled.
  * You may continue to incur charges from other Google Cloud products while your app is disabled.

**Important:** With this programmatic approach, you may pay more than the amount you specify in your budget alert. Because of the delay between the time a resource is used and the time it is billed, additional costs may be incurred before all services are stopped.

To programmatically disable your app:

  1. Create a budget alert that sends a notification to a Pub/Sub topic. For details, see [Manage programmatic notifications](https://docs.cloud.google.com/billing/docs/how-to/budgets#manage-notifications).

To create a budget alert just for costs from App Engine, in the Budget's Products field, select **App Engine**. For information about the resources that can trigger this alert, see Create budget alerts.

  2. In Cloud Run functions create a function that is triggered by the Pub/Sub topic. For details, see [Create a Cloud Function](https://docs.cloud.google.com/billing/docs/how-to/notify#create_a_cloud_function).

When creating the function:

     1. Use the following source code:

**Note:** The source code assumes that the function you are creating and the app you want to disable are in the same Google Cloud project. If the function and the app are in **separate projects** , change the source code so APP_NAME **identifies the project that contains the app you want to disable**.
            
            import base64
            import json
            import os
            from googleapiclient import discovery
            APP_NAME = os.getenv("GCP_PROJECT")
            
            
            def limit_use_appengine(data, context):
                pubsub_data = base64.b64decode(data["data"]).decode("utf-8")
                pubsub_json = json.loads(pubsub_data)
                cost_amount = pubsub_json["costAmount"]
                budget_amount = pubsub_json["budgetAmount"]
                if cost_amount <= budget_amount:
                    print(f"No action necessary. (Current cost: {cost_amount})")
                    return
            
                appengine = discovery.build("appengine", "v1", cache_discovery=False)
                apps = appengine.apps()
            
                # Get the target app's serving status
                target_app = apps.get(appsId=APP_NAME).execute()
                current_status = target_app["servingStatus"]
            
                # Disable target app, if necessary
                if current_status == "SERVING":
                    print(f"Attempting to disable app {APP_NAME}...")
                    body = {"servingStatus": "USER_DISABLED"}
                    apps.patch(appsId=APP_NAME, updateMask="serving_status", body=body).execute()
            
            

     2. Add the following dependencies to your function's `requirements.txt` file:
            
            google-api-python-client==2.131.0

     3. Under **Function to execute** enter `limit_use_appengine`.

     4. Click **Environment variables, networking, timeouts and more**.

     5. Select a service account that has the **App Engine Admin** role. The [App Engine default service account](https://docs.cloud.google.com/appengine/docs/standard/default-service-account) has this role by default.

  3. [Test the function](https://docs.cloud.google.com/billing/docs/how-to/notify#test_your_cloud_function).




When the budget alert is triggered, an email is sent to [users in your Cloud Billing account](https://docs.cloud.google.com/billing/docs/how-to/budgets), and your function starts disabling your app. It may take few minutes to complete this process.

To verify that the function ran successfully, view the App Engine dashboard. A message appears near the top to indicate that your app is disabled.

[Go to the App Engine dashboard](https://console.cloud.google.com/appengine)

When you want your app to continue serving requests, go to **Application settings** and click **Enable application**.

[Go to Application settings](https://console.cloud.google.com/appengine/settings)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
