---
url: https://docs.cloud.google.com/tasks/docs/deleting-appengine-queues-and-tasks/
title: Manage queues and tasks \u00a0|\u00a0 Cloud Tasks \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:41:30.146252+00:00
---

# Manage queues and tasks  |  Cloud Tasks  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tasks/docs/deleting-appengine-queues-and-tasks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Tasks ](https://docs.cloud.google.com/tasks/docs)
  * [ Guides ](https://docs.cloud.google.com/tasks/docs/dual-overview)



Send feedback 

#  Manage queues and tasks Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Tasks lets you control asynchronous workload execution, pause queue processing, and troubleshoot active task flows. You can configure and maintain your queues and tasks using the Google Cloud console, the Google Cloud CLI, or the Cloud Tasks API.

## Delete a task from a queue

You can delete a task if it is scheduled or dispatched. For example, you might need to delete a task that can't be completed successfully, no matter how many times it is retried. You can't delete a task if it has completed successfully or if it has run out of retries after consistently failing. A task is automatically deleted if the [maximum task retention](https://docs.cloud.google.com/tasks/docs/quotas#limits) limit is reached.

###  Console 

  1. In the Google Cloud console, go to the **Cloud Tasks** > **Queues** page.

[Go to Queues](https://console.cloud.google.com/cloudtasks)

  2. Click the name of the queue for the task that you want to delete.

  3. Select the checkbox for the task that you want to delete.

  4. Click delete **Delete task**.

  5. At the prompt, click **Delete**.




###  gcloud 

Delete a task using the [`gcloud tasks delete`](https://docs.cloud.google.com/sdk/gcloud/reference/tasks/delete) command:
    
    
    gcloud tasks delete TASK_NAME \
        --queue=QUEUE_ID \
        --location=LOCATION

Replace the following:

  * `TASK_NAME`: the name of the task that you want to delete
  * `QUEUE_ID`: the name of the queue that the task belongs to
  * `LOCATION`: the [region](https://docs.cloud.google.com/tasks/docs/locations) in which the queue is deployed—for example, `us-central1`



###  REST 

To delete a task, use the [`projects.locations.queues.tasks.delete`](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations.queues.tasks/delete) method.

Before using any of the request data, make the following replacements: 

  * `QUEUE_ID`: the name of the queue that the task belongs to
  * `TASK_NAME`: the name of the task you want to delete
  * `PROJECT_ID`: your Google Cloud project ID
  * `LOCATION`: the [region](https://docs.cloud.google.com/tasks/docs/locations) in which the queue exists—for example, `us-central1`



The request body must be empty.

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://cloudtasks.googleapis.com/v2/projects/PROJECT_ID/locations/LOCATION/queues/QUEUE_ID/tasks/TASK_NAME"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://cloudtasks.googleapis.com/v2/projects/PROJECT_ID/locations/LOCATION/queues/QUEUE_ID/tasks/TASK_NAME" | Select-Object -Expand Content

#### APIs Explorer (browser)

Open the [method reference page](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations.queues.tasks/delete). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Complete any required fields and click **Execute**. 

If successful, the response body is empty. 

## Delete a batch of tasks from a queue

You can delete a batch of tasks from a queue by using the [projects.locations.queues.tasks.batchDelete](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations.queues.tasks/batchDelete) method to delete a list of task names.

Note the following:

  * All tasks must be deleted from the same queue.

  * There is a limit to how many tasks can be deleted in a single batch. For more information, see [Quotas and limits](https://docs.cloud.google.com/tasks/docs/quotas#limits).

  * Batch requests, which aggregate individual operations into a single request, are not atomic because it's possible for some of the operations contained within the batch to fail while others succeed.

  * You can only delete a task if it is scheduled or dispatched. You can't delete a task if it has completed successfully or if it has run out of retries after consistently failing. A task is automatically deleted if the [maximum task retention](https://docs.cloud.google.com/tasks/docs/quotas#limits) limit is reached.

  * You can also create a batch of tasks. For more information, see [Create a batch of tasks](https://docs.cloud.google.com/tasks/docs/create-tasks#create-batch-tasks).




Before using any of the request data, make the following replacements: 

  * `TASK_NAME`: the name of the tasks to delete with the following format: `projects/PROJECT_ID/locations/REGION/queues/QUEUE_ID/tasks/TASK_ID`
  * `PROJECT_ID`: your Google Cloud project ID
  * `REGION`: the [region](https://docs.cloud.google.com/tasks/docs/locations) in which the queue exists—for example, `us-central1`
  * `QUEUE_ID`: the name of the queue that the tasks belong to



The request body contains a list of task names.

Request JSON body: 
    
    
    {
      "names": [
        "TASK_NAME"
      ]
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "names": [
        "TASK_NAME"
      ]
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://cloudtasks.googleapis.com/v2/projects/PROJECT_ID/locations/REGION/queues/QUEUE_ID/tasks:batchDelete"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "names": [
        "TASK_NAME"
      ]
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
        -Uri "https://cloudtasks.googleapis.com/v2/projects/PROJECT_ID/locations/REGION/queues/QUEUE_ID/tasks:batchDelete" | Select-Object -Expand Content

#### APIs Explorer (browser)

Copy the request body and open the [method reference page](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations.queues.tasks/batchDelete). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Paste the request body in this tool, complete any other required fields, and click **Execute**. 

If successful, the response body contains an instance of [`Operation`](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations.operations). 
    
    
    {
      "name": "projects/PROJECT_ID/locations/REGION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.tasks.v2.BatchDeleteTasksMetadata"
      },
      "done": false
    }
    

## Purge all tasks from a queue

You can delete _all_ tasks from a queue by purging them. All tasks created before the purge call are permanently deleted. However, purge operations can take up to one minute to take effect and tasks might be dispatched before the purge takes effect.

**Warning:** Tasks created in close temporal proximity (not more than a few seconds) to a purge call are also purged.

###  Console 

  1. In the Google Cloud console, go to the **Cloud Tasks** > **Queues** page.

[Go to Queues](https://console.cloud.google.com/cloudtasks)

  2. Click the name of the queue for the tasks that you want to delete.

  3. Click remove_circle_outline **Purge queue**.

  4. At the prompt, click **Purge**.




###  gcloud 

Purge a queue using the [`gcloud tasks queues purge`](https://docs.cloud.google.com/sdk/gcloud/reference/tasks/queues/purge) command:
    
    
    gcloud tasks queues purge QUEUE_ID \
        --location=LOCATION

Replace the following:

  * `QUEUE_ID`: the name of the queue that you want to purge
  * `LOCATION`: the [region](https://docs.cloud.google.com/tasks/docs/locations) in which the queue is deployed—for example, `us-central1`



###  REST 

To purge a queue, use the [`projects.locations.queues.purge`](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations.queues/purge) method.

Before using any of the request data, make the following replacements: 

  * `QUEUE_ID`: the name of the queue that you want to purge
  * `PROJECT_ID`: your Google Cloud project ID
  * `LOCATION`: the [region](https://docs.cloud.google.com/tasks/docs/locations) in which the queue is deployed—for example, `us-central1`



The request body must be empty.

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d "" \  
         "https://cloudtasks.googleapis.com/v2/projects/PROJECT_ID/locations/LOCATION/queues/QUEUE_ID:purge"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -Uri "https://cloudtasks.googleapis.com/v2/projects/PROJECT_ID/locations/LOCATION/queues/QUEUE_ID:purge" | Select-Object -Expand Content

#### APIs Explorer (browser)

Open the [method reference page](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations.queues/purge). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Complete any required fields and click **Execute**. 

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
      "state": "RUNNING",
      "purgeTime": "2025-03-28T13:06:30.110255Z"
    }
    

## Pause or resume queues

You can pause or resume a queue. Pausing a queue means that the execution and delivery of tasks are stopped. You can still create tasks and push or append them to the queue but the tasks won't be processed. Once the queue is resumed, any backlogged tasks are processed in the order of their addition to the queue backlog.

###  Console 

  1. In the Google Cloud console, go to the **Cloud Tasks** > **Queues** page.

[Go to Queues](https://console.cloud.google.com/cloudtasks)

  2. Select the checkbox for the queue that you want to pause.

  3. Click pause **Pause queue**.

  4. At the prompt, click **Pause**.

  5. To resume the queue, click play_arrow **Resume queue**.




###  gcloud 

  1. Pause a queue using the [`gcloud tasks queues pause`](https://docs.cloud.google.com/sdk/gcloud/reference/tasks/queues/pause) command:
         
         gcloud tasks queues pause QUEUE_ID \
             --location=LOCATION

Replace the following:

     * `QUEUE_ID`: the name of the queue that you want to pause
     * `LOCATION`: the [region](https://docs.cloud.google.com/tasks/docs/locations) in which the queue is deployed—for example, `us-central1`
  2. Resume a queue using the [`gcloud tasks queues resume`](https://docs.cloud.google.com/sdk/gcloud/reference/tasks/queues/resume) command:
         
         gcloud tasks queues resume QUEUE_ID \
             --location=LOCATION




###  REST 

  1. To pause a queue, use the [`projects.locations.queues.pause`](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations.queues/pause) method.

Before using any of the request data, make the following replacements: 

     * `QUEUE_ID`: the name of the queue that you want to pause
     * `PROJECT_ID`: your Google Cloud project ID
     * `LOCATION`: the [region](https://docs.cloud.google.com/tasks/docs/locations) in which the queue is deployed—for example, `us-central1`

The request body must be empty.

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d "" \  
         "https://cloudtasks.googleapis.com/v2/projects/PROJECT_ID/locations/LOCATION/queues/QUEUE_ID:pause"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -Uri "https://cloudtasks.googleapis.com/v2/projects/PROJECT_ID/locations/LOCATION/queues/QUEUE_ID:pause" | Select-Object -Expand Content

#### APIs Explorer (browser)

Open the [method reference page](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations.queues/pause). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Complete any required fields and click **Execute**. 

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
      "state": "PAUSED"
    }
    

  2. To resume a queue, use the [`projects.locations.queues.resume`](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations.queues/resume) method.

Before using any of the request data, make the following replacements: 

     * `QUEUE_ID`: the name of the queue that you want to resume
     * `PROJECT_ID`: your Google Cloud project ID
     * `LOCATION`: the [region](https://docs.cloud.google.com/tasks/docs/locations) in which the queue is deployed—for example, `us-central1`

The request body must be empty.

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d "" \  
         "https://cloudtasks.googleapis.com/v2/projects/PROJECT_ID/locations/LOCATION/queues/QUEUE_ID:resume"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -Uri "https://cloudtasks.googleapis.com/v2/projects/PROJECT_ID/locations/LOCATION/queues/QUEUE_ID:resume" | Select-Object -Expand Content

#### APIs Explorer (browser)

Open the [method reference page](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations.queues/resume). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Complete any required fields and click **Execute**. 

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
    




## List queues

You can list queues. When listing queues, some [rate limit](https://docs.cloud.google.com/tasks/docs/configuring-queues#rate) and [retry parameter](https://docs.cloud.google.com/tasks/docs/configuring-queues#retry) details are returned. Note that the following fields are equivalent:

  * **Max rate** (Console), `MAX_RATE` (gcloud), `maxDispatchesPerSecond` (REST)
  * **Max concurrent** (Console), `MAX_NUM_OF_TASKS` (gcloud), `maxConcurrentDispatches` (REST)




###  Console 

  1. In the Google Cloud console, go to the **Cloud Tasks** > **Queues** page.

[Go to Queues](https://console.cloud.google.com/cloudtasks)

All queues in your Google Cloud project are listed.

  2. For more details, click the name of a queue, and then click the **Configuration** tab.

Rate limit and retry parameter details are displayed.




###  gcloud 

List queues using the [`gcloud tasks queues list`](https://docs.cloud.google.com/sdk/gcloud/reference/tasks/queues/list) command:
    
    
    gcloud tasks queues list \
        --location=LOCATION

Replace `LOCATION` with the [region](https://docs.cloud.google.com/tasks/docs/locations) in which the queue is deployed—for example, `us-central1`. If a location is not specified, the location of your Google Cloud project's App Engine app is used if it exists; otherwise, you must specify a location.

The output should be similar to the following:
    
    
    QUEUE_NAME: my-queue
    STATE: PAUSED
    MAX_NUM_OF_TASKS: 1000
    MAX_RATE (/sec): 500.0
    MAX_ATTEMPTS: 100
    ...

###  REST 

To list queues, use the [`projects.locations.queues.list`](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations.queues/list) method.

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: your Google Cloud project ID.
  * `LOCATION`: the [region](https://docs.cloud.google.com/tasks/docs/locations) in which the queues are created—for example, `us-central1`.



To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://cloudtasks.googleapis.com/v2/projects/PROJECT_ID/locations/LOCATION/queues"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://cloudtasks.googleapis.com/v2/projects/PROJECT_ID/locations/LOCATION/queues" | Select-Object -Expand Content

#### APIs Explorer (browser)

Open the [method reference page](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations.queues/list). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Complete any required fields and click **Execute**. 

If successful, the response body contains instances of [`Queue`](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations.queues#Queue) resources and the response should be similar to the following: 
    
    
    {
      "queues": [
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
          "state": "PAUSED",
          "purgeTime": "2025-03-28T13:37:32.292552Z"
        },
        ...
      ],
      "nextPageToken": "CjQKCHppcHBlcjIAEgwI9-GExAYQ_oDc1AMaGioLeWlrZXMtYWdhaW4yC3VzLWNlbnRyYWwx"
    }
    

## Delete queues

You can delete a queue. Any tasks in the queue are deleted as well. If you delete a queue you must wait 3 days before recreating it with the same name. This waiting period prevents unexpected behavior in tasks that are running at the time of deletion or waiting to be run. It also avoids internal process failures in the delete or recreate cycle.

###  Console 

  1. In the Google Cloud console, go to the **Cloud Tasks** > **Queues** page.

[Go to Queues](https://console.cloud.google.com/cloudtasks)

  2. Select the checkbox for the queue that you want to delete.

  3. Click delete **Delete queue**.

  4. At the prompt, type the queue name, and then click **Confirm**.




###  gcloud 

Delete a queue using the [`gcloud tasks queues delete`](https://docs.cloud.google.com/sdk/gcloud/reference/tasks/queues/delete) command:
    
    
    gcloud tasks queues delete QUEUE_ID \
        --location=LOCATION

Replace the following:

  * `QUEUE_ID`: the name of the queue that you want to delete
  * `LOCATION`: the [region](https://docs.cloud.google.com/tasks/docs/locations) in which the queue is deployed—for example, `us-central1`



###  REST 

To delete a queue, use the [`projects.locations.queues.delete`](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations.queues/delete) method.

Before using any of the request data, make the following replacements: 

  * `QUEUE_ID`: the name of the queue that you want to delete
  * `PROJECT_ID`: your Google Cloud project ID
  * `LOCATION`: the [region](https://docs.cloud.google.com/tasks/docs/locations) in which the queue is deployed—for example, `us-central1`



The request body must be empty.

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://cloudtasks.googleapis.com/v2/projects/PROJECT_ID/locations/LOCATION/queues/QUEUE_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://cloudtasks.googleapis.com/v2/projects/PROJECT_ID/locations/LOCATION/queues/QUEUE_ID" | Select-Object -Expand Content

#### APIs Explorer (browser)

Open the [method reference page](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations.queues/delete). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Complete any required fields and click **Execute**. 

If successful, the response body is empty. 

## What's next

  * [Configure queue routing, limits, and retries](https://docs.cloud.google.com/tasks/docs/configuring-queues)
  * [Set retry parameters for a task](https://docs.cloud.google.com/tasks/docs/configure-retry-task)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
