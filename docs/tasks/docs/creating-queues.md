---
url: https://docs.cloud.google.com/tasks/docs/creating-queues/
title: Create Cloud Tasks queues \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:23.589045+00:00
---

# Create Cloud Tasks queues  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tasks/docs/creating-queues/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Tasks ](https://docs.cloud.google.com/tasks/docs)
  * [ Guides ](https://docs.cloud.google.com/tasks/docs/dual-overview)



Send feedback 

#  Create Cloud Tasks queues Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create Cloud Tasks queues. When tasks are added to a queue, the queue dispatches them and makes sure they are reliably processed by a service, also known as a _worker_.

Note the following:

  * Queue names consist of three parts: a project ID, a location, and a queue ID. You must have a [Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) which provides the project ID.

  * If you are using App Engine target tasks, you must also have an [App Engine application](https://docs.cloud.google.com/appengine/docs/standard/python/console#create) which is located in a specific [region](https://docs.cloud.google.com/appengine/docs/locations) and which is where your queue and your handlers run. Note the region when you add the app.

**Note:** Two locations, called `europe-west` and `us-central` in App Engine commands, are called, respectively, `europe-west1` and `us-central1` in Cloud Tasks commands.
  * Using HTTP target tasks doesn't require an App Engine app. You select a Google Cloud location when you create your queue.




## Create a queue

You can create a queue in the following ways:

  * In the Google Cloud console
  * By using the Google Cloud CLI in either your terminal or Cloud Shell
  * By sending a direct request to the Cloud Tasks API

**Note:** If you are configuring routing for an App Engine queue and you don't explicitly set the target [service](https://docs.cloud.google.com/appengine/docs/flexible/python/an-overview-of-app-engine) that contains the appropriate worker, the [default service](https://docs.cloud.google.com/appengine/docs/standard/python/how-requests-are-routed#default_routing) is used. For more information, see [Configure queue routing, limits, and retries](https://docs.cloud.google.com/tasks/docs/configuring-queues).

### Console

  1. In the Google Cloud console, go to the **Cloud Tasks** > **Queues** page.

[Go to Queues](https://console.cloud.google.com/cloudtasks)

  2. Click add_box **Create queue**.

  3. Enter a **Queue name** —for example, `my-queue`.

  4. In the **Region** list, select a supported [location](https://cloud.google.com/about/locations) where the queue will run—for example, `asia-south1`.

If your organization [restricts resource location](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations) and you want to create your queue in either `us-central1` or `us-central2`, the organization policy must allow queue creation in both `us-central1` and `us-central2` (even if you only need a queue in one of those regions).

  5. Optionally, you can further [configure your queue](https://docs.cloud.google.com/tasks/docs/configuring-queues).

  6. Click **Create**.




###  gcloud 

Use the [`gcloud tasks queues create`](https://docs.cloud.google.com/sdk/gcloud/reference/tasks/queues/create) command to create your queue:
    
    
      gcloud tasks queues create QUEUE_ID \
          --location=LOCATION

Replace the following:

  * `QUEUE_ID`: the identifier you assign to your queue—for example, `my-queue`.

  * `LOCATION`: a supported [region](https://cloud.google.com/about/locations) where the queue will run—for example, `asia-south1`.

If your organization [restricts resource location](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations) and you want to create your queue in either `us-central1` or `us-central2`, the organization policy must allow queue creation in both `us-central1` and `us-central2` (even if you only need a queue in one of those regions).




Other flags for the gcloud CLI command let you configure rate limits, retry options, queue types, and more.

### REST API

To create a queue, use the [`projects.locations.queues.create`](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations.queues/create) method.

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: your Google Cloud project ID. 
  * `LOCATION`: a supported [region](https://docs.cloud.google.com/tasks/docs/locations) where the queue will run—for example, `asia-south1`. 

If your organization [restricts resource location](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations) and you want to create your queue in either `us-central1` or `us-central2`, the organization policy must allow queue creation in both `us-central1` and `us-central2` (even if you only need a queue in one of those regions).

  * `QUEUE_ID`: the identifier you assign to your queue—for example, `my-queue`. 

Other configurable properties for the [`Queue` resource](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations.queues#resource:-queue) include rate limits, retry options, queue types, and more. 

Request JSON body: 
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/queues/QUEUE_ID"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/queues/QUEUE_ID"
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://cloudtasks.googleapis.com/v2/projects/PROJECT_ID/locations/LOCATION/queues"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/queues/QUEUE_ID"
    }
    '@  | Out-File -FilePath request.json -Encoding utf8

Then execute the following command to send your REST request: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://cloudtasks.googleapis.com/v2/projects/PROJECT_ID/locations/LOCATION/queues" | Select-Object -Expand Content

#### APIs Explorer (browser)

Copy the request body and open the [method reference page](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations.queues/create). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Paste the request body in this tool, complete any other required fields, and click **Execute**. 

If successful, the response body contains a newly created instance of [`Queue`](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations.queues#resource:-queue): 
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/queues/QUEUE_ID",
      "rateLimits": {
        "maxDispatchesPerSecond": 500,
        "maxBurstSize": 100,
        "maxConcurrentDispatches": 1000
      },
      "retryConfig": {
        "maxAttempts": 100,
        "minBackoff": "0.100s",
        "maxBackoff": "3600s",
        "maxDoublings": 16
      },
      "state": "RUNNING"
    }
    

It can take a few minutes for a newly created queue to be available.

## Describe your queue

You can confirm that your queue was created successfully in the following ways:

  * In the Google Cloud console
  * By using the gcloud CLI in either your terminal or Cloud Shell
  * By sending a direct request to the Cloud Tasks API




### Console

  1. In the Google Cloud console, go to the **Cloud Tasks** > **Queues** page.

[Go to Queues](https://console.cloud.google.com/cloudtasks)

A green checkmark check_circle should indicate that your queue is running.

  2. For more details, click the name of the queue, and then click the **Configuration** tab.




###  gcloud 

Use the [`gcloud tasks queues describe`](https://docs.cloud.google.com/sdk/gcloud/reference/tasks/queues/describe) command to verify that your queue was created successfully:
    
    
    gcloud tasks queues describe QUEUE_ID \
        --location=LOCATION

Replace the following:

  * `QUEUE_ID`: the queue ID (its short name)
  * `LOCATION`: the location of the queue



The output should be similar to the following:
    
    
    name: projects/PROJECT_ID/locations/LOCATION/queues/QUEUE_ID
    rateLimits:
      maxBurstSize: 100
      maxConcurrentDispatches: 1000
      maxDispatchesPerSecond: 500.0
    retryConfig:
      maxAttempts: 100
      maxBackoff: 3600s
      maxDoublings: 16
      minBackoff: 0.100s
    state: RUNNING

### REST API

To retrieve a queue, use the [`projects.locations.queues.get`](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations.queues/get) method.

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: your Google Cloud project ID.
  * `LOCATION`: the [region](https://docs.cloud.google.com/tasks/docs/locations) in which the queue is deployed—for example, `us-central1`.
  * `QUEUE_ID`: the short ID of the queue—for example, `my-queue`.



To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://cloudtasks.googleapis.com/v2/projects/PROJECT_ID/locations/LOCATION/queues/QUEUE_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://cloudtasks.googleapis.com/v2/projects/PROJECT_ID/locations/LOCATION/queues/QUEUE_ID" | Select-Object -Expand Content

#### APIs Explorer (browser)

Open the [method reference page](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations.queues/get). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Complete any required fields and click **Execute**. 

If successful, the response body contains an instance of [`Queue`](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations.queues#resource:-queue): 
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/queues/QUEUE_ID",
      "rateLimits": {
        "maxDispatchesPerSecond": 500,
        "maxBurstSize": 100,
        "maxConcurrentDispatches": 1000
      },
      "retryConfig": {
        "maxAttempts": 100,
        "minBackoff": "0.100s",
        "maxBackoff": "3600s",
        "maxDoublings": 16
      },
      "state": "RUNNING"
    }
    

## Troubleshoot creating a queue

**Note:** Logging for your queue is not enabled by default. For information on enabling logging, see [Use Cloud Logging with queues](https://docs.cloud.google.com/tasks/docs/monitor#logging-queues).

If you don't see the expected output, you can try the following:

  * Wait at least one minute for the queue to initialize.
  * Make sure a queue with the same ID does not already exist. You can view the queues in your project by using the [`gcloud tasks queues list`](https://docs.cloud.google.com/sdk/gcloud/reference/tasks/queues/list) command:
        
        gcloud tasks queues list \
            --location=LOCATION

To search multiple locations you need to make multiple requests.

  * Check if you've reached your queue [quota](https://docs.cloud.google.com/tasks/docs/quotas):

    1. In the Google Cloud console, go to the **API/Service Details** page for the Cloud Tasks API.

[Go to API/Service Details](https://console.cloud.google.com/apis/api/cloudtasks.googleapis.com/overview)

    2. Click the **Quotas & System limits** tab.

    3. To increase a quota, in the row for the quota, click the ellipsis icon more_vert> **Edit quota**.

For more information, see [Request a quota adjustment](https://docs.cloud.google.com/docs/quotas/help/request_increase).

  * Re-run the commands to create your queue and ensure that each step is completed correctly.




## What's next

  * [Configure queue routing, limits, and retries](https://docs.cloud.google.com/tasks/docs/configuring-queues)
  * [Create Cloud Tasks tasks](https://docs.cloud.google.com/tasks/docs/create-tasks)
  * [Set retry parameters for a task](https://docs.cloud.google.com/tasks/docs/configure-retry-task)
  * [Manage queues and tasks](https://docs.cloud.google.com/tasks/docs/manage-queues-and-tasks)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
