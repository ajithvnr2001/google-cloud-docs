---
url: https://docs.cloud.google.com/tasks/docs/configure-retry-task/
title: Set retry parameters for a task \u00a0|\u00a0 Cloud Tasks \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:53.687319+00:00
---

# Set retry parameters for a task  |  Cloud Tasks  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tasks/docs/configure-retry-task/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Tasks ](https://docs.cloud.google.com/tasks/docs)
  * [ Guides ](https://docs.cloud.google.com/tasks/docs/dual-overview)



Send feedback 

#  Set retry parameters for a task Stay organized with collections  Save and categorize content based on your preferences. 

When creating a task, you can specify the maximum number of times to retry a failed task, set a time limit for retry attempts, and control the interval between attempts by using the [`projects.locations.queues.tasks.create`](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations.queues.tasks/create) method. Once a task is successfully executed, it is removed from the queue. In all cases, the [maximum task retention](https://docs.cloud.google.com/tasks/docs/quotas#limits) limit also applies.

This task-level retry configuration overrides the [queue-level retry configuration](https://docs.cloud.google.com/tasks/docs/configuring-queues#retry) for the task.

## Configure retries when creating a task

The following example demonstrates setting retry parameters when creating an HTTP target task by sending a direct request to the Cloud Tasks API. You can use the same retry parameters when [creating an App Engine task](https://docs.cloud.google.com/tasks/docs/create-tasks#create-gae-task). For more parameter details, see the [`RetryConfig` settings](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/RetryConfig) for the `Task` resource.

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: required. The project ID of the Google Cloud project where the task will be created.
  * `REGION`: required. The [region](https://docs.cloud.google.com/tasks/docs/locations) in which the queue is deployed—for example, `us-central1`.
  * `QUEUE_ID`: required. The ID of the queue to which the task will be added.
  * `URL`: required. The fully qualified URL that the request will be sent to. This string must begin with either `http://` or `https://`—for example: `https://www.example.com`. **Note:** To target a Cloud Run service or function, use its [default `run.app` URL](https://docs.cloud.google.com/run/docs/triggering/https-request#url).
  * `SERVICE_ACCOUNT_EMAIL`: optional. The service account email used to generate an authorization token that is included in the request sent to the target when executing the task. The service account must be in the same project as the queue. The caller must have the [`iam.serviceAccounts.actAs`](https://docs.cloud.google.com/iam/docs/service-account-permissions#attaching) permission for the service account. 

To generate an OAuth2 access token instead of an OpenID Connect token, replace the `oidcToken` field with `oauthToken` to specify the service account email.

  * `MAX_ATTEMPTS`: optional. The maximum number of attempts for a task, including the first. To allow unlimited retries, set this to `-1`. `MAX_RETRY_DURATION` still applies even if `MAX_ATTEMPTS` is reached or set to `-1`.
  * `MAX_RETRY_DURATION`: optional. The maximum amount of time for retrying a failed task, measured from when the task was first attempted. The value must be a string that ends in "s," such as `5s`. To specify an unlimited duration, set this to `0s`. `MAX_ATTEMPTS` still applies even if `MAX_RETRY_DURATION` is reached or set to `0s`. **Note:** If you specify unlimited attempts (`MAX_ATTEMPTS` is `-1`) and an unlimited duration (`MAX_RETRY_DURATION` is `0s`), then the task is retried until it reaches the [maximum task retention](https://docs.cloud.google.com/tasks/docs/quotas#limits) limit. Otherwise, Cloud Tasks stops retrying only after both conditions are met or the task succeeds.
  * `MIN_INTERVAL`: optional. The minimum amount of time to wait between retry attempts. The value must be a string that ends in "s," such as `5s`.
  * `MAX_INTERVAL`: optional. The maximum amount of time to wait between retry attempts. The value must be a string that ends in "s," such as `5s`.
  * `MAX_DOUBLINGS`: optional. The maximum number of times that the interval between failed task retries will be doubled before the increase becomes constant. A task's retry interval starts at `MIN_INTERVAL`, then doubles `MAX_DOUBLINGS` times, then increases linearly, and finally retries at intervals of `MAX_INTERVAL` up to `MAX_ATTEMPTS` times. 

For example, if `MIN_INTERVAL` is `10s`, `MAX_INTERVAL` is `300s`, and `MAX_DOUBLINGS` is `3`, the retry interval will double `3` times, increase linearly by 2^3 * 10s, and then retry at intervals of `MAX_INTERVAL` until the task has been attempted `MAX_ATTEMPTS` times: 10s, 20s, 40s, 80s, 160s, 240s, 300s, 300s, and so forth.

  * `SCHEDULE_TIME`: optional. The time when the task is scheduled to be attempted, in RFC 3339 format—for example, `2026-10-02T15:01:23Z`. If the time isn't set or is in the past, Cloud Tasks will set it to the current time.



Request JSON body: 
    
    
    {
      "task": {
        "httpRequest": {
          "url": "URL",
          "httpMethod": "POST",
          "oidcToken": {
            "serviceAccountEmail": "SERVICE_ACCOUNT_EMAIL"
          }
        },
        "retryConfig": {
          "maxAttempts": MAX_ATTEMPTS,
          "maxRetryDuration": "MAX_RETRY_DURATION",
          "minBackoff": "MIN_INTERVAL",
          "maxBackoff": "MAX_INTERVAL",
          "maxDoublings": MAX_DOUBLINGS
        },
        "scheduleTime": "SCHEDULE_TIME"
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "task": {
        "httpRequest": {
          "url": "URL",
          "httpMethod": "POST",
          "oidcToken": {
            "serviceAccountEmail": "SERVICE_ACCOUNT_EMAIL"
          }
        },
        "retryConfig": {
          "maxAttempts": MAX_ATTEMPTS,
          "maxRetryDuration": "MAX_RETRY_DURATION",
          "minBackoff": "MIN_INTERVAL",
          "maxBackoff": "MAX_INTERVAL",
          "maxDoublings": MAX_DOUBLINGS
        },
        "scheduleTime": "SCHEDULE_TIME"
      }
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://cloudtasks.googleapis.com/v2/projects/PROJECT_ID/locations/REGION/queues/QUEUE_ID/tasks"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "task": {
        "httpRequest": {
          "url": "URL",
          "httpMethod": "POST",
          "oidcToken": {
            "serviceAccountEmail": "SERVICE_ACCOUNT_EMAIL"
          }
        },
        "retryConfig": {
          "maxAttempts": MAX_ATTEMPTS,
          "maxRetryDuration": "MAX_RETRY_DURATION",
          "minBackoff": "MIN_INTERVAL",
          "maxBackoff": "MAX_INTERVAL",
          "maxDoublings": MAX_DOUBLINGS
        },
        "scheduleTime": "SCHEDULE_TIME"
      }
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
        -Uri "https://cloudtasks.googleapis.com/v2/projects/PROJECT_ID/locations/REGION/queues/QUEUE_ID/tasks" | Select-Object -Expand Content

#### APIs Explorer (browser)

Copy the request body and open the [method reference page](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations.queues.tasks/create). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Paste the request body in this tool, complete any other required fields, and click **Execute**. 

If successful, the response body contains the newly created instance of the `Task` resource. 
    
    
    {
      "name": "projects/PROJECT_ID/locations/REGION/queues/QUEUE_ID/tasks/TASK_ID",
      "httpRequest": {
        "url": "URL",
        "httpMethod": "POST",
        "headers": {
          "User-Agent": "Google-Cloud-Tasks"
        },
        "oidcToken": {
          "serviceAccountEmail": "SERVICE_ACCOUNT_EMAIL",
          "audience": "URL"
        }
      },
      "retryConfig": {
        "maxAttempts": MAX_ATTEMPTS,
        "maxRetryDuration": "MAX_RETRY_DURATION",
        "minBackoff": "MIN_INTERVAL",
        "maxBackoff": "MAX_INTERVAL",
        "maxDoublings": MAX_DOUBLINGS
      },
      "scheduleTime": "SCHEDULE_TIME",
      "createTime": "2026-04-30T19:11:50Z",
      "dispatchDeadline": "600s",
      "view": "BASIC"
    }
    

## What's next

  * [Create Cloud Tasks queues](https://docs.cloud.google.com/tasks/docs/creating-queues)
  * [Create Cloud Tasks tasks](https://docs.cloud.google.com/tasks/docs/create-tasks)
  * [Configure queue routing, limits, and retries](https://docs.cloud.google.com/tasks/docs/configuring-queues)
  * [Manage queues and tasks](https://docs.cloud.google.com/tasks/docs/manage-queues-and-tasks)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
