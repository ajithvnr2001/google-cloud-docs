---
url: https://docs.cloud.google.com/tasks/docs/create-tasks/
title: Create Cloud Tasks tasks \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:40:14.716934+00:00
---

# Create Cloud Tasks tasks  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tasks/docs/create-tasks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Tasks ](https://docs.cloud.google.com/tasks/docs)
  * [ Guides ](https://docs.cloud.google.com/tasks/docs/dual-overview)



Send feedback 

#  Create Cloud Tasks tasks Stay organized with collections  Save and categorize content based on your preferences. 

You can use Cloud Tasks to create asynchronous work items called _tasks_. This document demonstrates how to create HTTP target tasks and App Engine tasks.

HTTP target tasks are requests forwarded to a worker located at any generic HTTP endpoint with an external IP address such as Cloud Run, Google Kubernetes Engine, Compute Engine, or an on-premises web server.

For App Engine targets, Cloud Tasks forwards task requests to a handler within App Engine. All queues targeting App Engine handlers must have an [App Engine app](https://docs.cloud.google.com/appengine/docs/standard/python/console#create). Handlers must run in the [region](https://docs.cloud.google.com/appengine/docs/locations) where the App Engine app runs. This region also serves as the `REGION` parameter for your Cloud Tasks requests.

You can create an HTTP target task in the following ways:

  * In the Google Cloud console
  * By using the Google Cloud CLI in either your terminal or Cloud Shell
  * By sending a direct request to the Cloud Tasks API



To learn how to programmatically add an HTTP target task to a Cloud Tasks queue, see [Create HTTP target tasks programmatically](https://docs.cloud.google.com/tasks/docs/creating-http-target-tasks).

You can create an App Engine task in the following ways:

  * By using the Google Cloud CLI in either your terminal or Cloud Shell
  * By sending a direct request to the Cloud Tasks API



To learn how to programmatically add an App Engine task to a Cloud Tasks queue, see [Create App Engine tasks programmatically](https://docs.cloud.google.com/tasks/docs/creating-appengine-tasks).

## Before you begin

Make sure that you have already created a Cloud Tasks queue. For more information, see [Create Cloud Tasks queues](https://docs.cloud.google.com/tasks/docs/creating-queues).

## Create an HTTP target task

When creating a task, you can specify a task name. If the name is identical to that of an existing task or a task that was deleted or completed recently, the call will fail. If you don't specify a task name, a random unique task ID is generated.

Because there is an extra lookup cost to identify duplicate task names, tasks created with user-specified IDs have significantly increased latency. Using hashed strings for the task ID or for the prefix of the task ID is recommended. For more information, see [Task deduplication](https://docs.cloud.google.com/tasks/docs/dual-overview#task_deduplication).

###  Console 

  1. In the Google Cloud console, go to the **Cloud Tasks** > **Queues** page.

[Go to Queues](https://console.cloud.google.com/cloudtasks)

  2. Click the name of the queue to which you want to add your task.

  3. Click add_box **Create HTTP task**.

  4. Optionally, specify the **Task name**.

  5. For **URL** , specify the fully qualified URL that the request will be sent to. The path must begin with either `http://` or `https://`—for example: `https://www.example.com`.

**Note:** To target a Cloud Run service or function, use its [default `run.app` URL](https://docs.cloud.google.com/run/docs/triggering/https-request#url).
  6. Optionally, specify the **HTTP method** to use for the request. The default is `POST`.

  7. Optionally, for **Request body** , provide the HTTP body data to be sent to the worker processing the task.

  8. Optionally, specify one or more HTTP request headers by clicking add **Add a header**.

  9. For **Auth header** , select one of the following authorization options to specify how the request sent to the target is authenticated when executing the task:

     * **None** —no header, for public endpoints without authorization
     * **Add OAuth token** —generally used for Google APIs hosted on `*.googleapis.com`
     * **Add OIDC token** —used for Google Cloud and third-party endpoint calls, with the exception of Google APIs hosted on `*.googleapis.com`
  10. If applicable, for **Service account** , provide the service account email that will be used to generate the authorization token included in the request sent to the target when executing the task. The service account must be in the same project as the queue. The caller must have the [`iam.serviceAccounts.actAs`](https://docs.cloud.google.com/iam/docs/service-account-permissions#attaching) permission for the service account.

  11. Optionally, and if applicable, specify the **Audience** to limit types of actions or recipients for the authorization token.

  12. Click **Create**.




Your task should be listed on the **Queue details** page.

###  gcloud 

To create an HTTP target task and add it to an existing queue, use the [`gcloud tasks create-http-task`](https://docs.cloud.google.com/sdk/gcloud/reference/tasks/create-http-task) command.
    
    
    gcloud tasks create-http-task \
        --queue=QUEUE_ID \
        --url=URL \
        --location=REGION \
        --project=PROJECT_ID \
        --oidc-service-account-email=SERVICE_ACCOUNT_EMAIL
    

Replace the following:

  * `QUEUE_ID`: the name of the queue to add the task to.
  * `URL`: the fully qualified URL that the request will be sent to. The path must begin with either `http://` or `https://`—for example: `https://www.example.com`.

**Note:** To target a Cloud Run service or function, use its [default `run.app` URL](https://docs.cloud.google.com/run/docs/triggering/https-request#url).
  * `REGION`: optional. The [region](https://docs.cloud.google.com/tasks/docs/locations) in which the queue is deployed—for example, `us-central1`.

  * `PROJECT_ID`: optional. The project ID of the Google Cloud project where the task will be created.

  * `SERVICE_ACCOUNT_EMAIL`: optional. The service account email used to generate an authorization token that is included in the request sent to the target when executing the task. The service account must be in the same project as the queue. The caller must have the [`iam.serviceAccounts.actAs`](https://docs.cloud.google.com/iam/docs/service-account-permissions#attaching) permission for the service account.

To generate an OAuth2 access token instead of an OpenID Connect token, replace the `--oidc-service-account-email` flag with `--oauth-service-account-email` to specify the service account email.




After creating the task, you should see a confirmation message with the full resource name of the created task.

###  REST 

To create an HTTP target task and add it to an existing queue, use the [`projects.locations.queues.tasks.create`](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations.queues.tasks/create) method.

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: required. The project ID of the Google Cloud project where the task will be created.
  * `REGION`: required. The [region](https://docs.cloud.google.com/tasks/docs/locations) in which the queue is deployed—for example, `us-central1`.
  * `QUEUE_ID`: required. The ID of the queue to which the task will be added.
  * `URL`: required. The fully qualified URL that the request will be sent to. This string must begin with either `http://` or `https://`—for example: `https://www.example.com`. **Note:** To target a Cloud Run service or function, use its [default `run.app` URL](https://docs.cloud.google.com/run/docs/triggering/https-request#url).
  * `SERVICE_ACCOUNT_EMAIL`: optional. The service account email used to generate an authorization token that is included in the request sent to the target when executing the task. The service account must be in the same project as the queue. The caller must have the [`iam.serviceAccounts.actAs`](https://docs.cloud.google.com/iam/docs/service-account-permissions#attaching) permission for the service account. 

To generate an OAuth2 access token instead of an OpenID Connect token, replace the `oidcToken` field with `oauthToken` to specify the service account email.

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
      "scheduleTime": "SCHEDULE_TIME",
      "createTime": "2026-04-30T19:11:50Z",
      "dispatchDeadline": "600s",
      "view": "BASIC"
    }
    

## Create an App Engine task

When creating a task, you can specify a task name. If the name is identical to that of an existing task or a task that was deleted or completed recently, the call will fail. If you don't specify a task name, a random unique task ID is generated.

Because there is an extra lookup cost to identify duplicate task names, tasks created with user-specified IDs have significantly increased latency. Using hashed strings for the task ID or for the prefix of the task ID is recommended. For more information, see [Task deduplication](https://docs.cloud.google.com/tasks/docs/dual-overview#task_deduplication).

###  gcloud 

To create an App Engine task and add it to an existing queue, use the [`gcloud tasks create-app-engine-task`](https://docs.cloud.google.com/sdk/gcloud/reference/tasks/create-app-engine-task) command.
    
    
    gcloud tasks create-app-engine-task \
        --queue=QUEUE_ID \
        --relative-uri=RELATIVE_URI \
        --location=REGION \
        --project=PROJECT_ID \
        --routing=KEY:VALUE
    

Replace the following:

  * `QUEUE_ID`: the name of the queue to add the task to.
  * `RELATIVE_URI`: the relative URI of the request. The path must begin with a forward slash (`/`). If not specified, the root path is used (`/`).
  * `REGION`: optional. The [region](https://docs.cloud.google.com/tasks/docs/locations) in which the queue is deployed. If not specified, the location of the current project's App Engine app is used.
  * `PROJECT_ID`: optional. The project ID of the Google Cloud project where the task will be created.
  * `KEY`:`VALUE`: optional. The route to be used for this task where `KEY` is at least one of: `service`, `version`, or `instance`. Any missing keys will use the default routing.



After creating the task, you should see a confirmation message with the full resource name of the created task.

###  REST 

To create an App Engine task and add it to an existing queue, use the [`projects.locations.queues.tasks.create`](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations.queues.tasks/create) method.

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: required. The project ID of the Google Cloud project where the task will be created.
  * `REGION`: required. The [region](https://docs.cloud.google.com/tasks/docs/locations) in which the queue is deployed.
  * `QUEUE_ID`: required. The ID of the queue to which the task will be added.
  * `RELATIVE_URI`: required. The relative URI of the request. The path must begin with a forward slash (`/`). If not specified, the root path is used (`/`).
  * `SERVICE`: optional. The App Engine service which will process the task. By default, the task is sent to the service which is the default service when the task is attempted.
  * `VERSION`: optional. The App Engine version which will process the task. By default, the task is sent to the version which is the default version when the task is attempted.
  * `SCHEDULE_TIME`: optional. The time when the task is scheduled to be attempted, in RFC 3339 format—for example, `2026-10-02T15:01:23Z`. If the time isn't set or is in the past, Cloud Tasks will set it to the current time.



Request JSON body: 
    
    
    {
      "task": {
        "appEngineHttpRequest": {
          "httpMethod": "POST",
          "relativeUri": "RELATIVE_URI",
          "appEngineRouting": {
            "service": "SERVICE",
            "version": "VERSION"
          }
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
        "appEngineHttpRequest": {
          "httpMethod": "POST",
          "relativeUri": "RELATIVE_URI",
          "appEngineRouting": {
            "service": "SERVICE",
            "version": "VERSION"
          }
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
        "appEngineHttpRequest": {
          "httpMethod": "POST",
          "relativeUri": "RELATIVE_URI",
          "appEngineRouting": {
            "service": "SERVICE",
            "version": "VERSION"
          }
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
      "appEngineHttpRequest": {
        "httpMethod": "POST",
        "relativeUri": "RELATIVE_URI",
        "appEngineRouting": {
          "service": "SERVICE",
          "version": "VERSION",
          "host": "VERSION.SERVICE.PROJECT_ID.appspot.com"
        }
      },
      "scheduleTime": "SCHEDULE_TIME",
      "createTime": "2026-04-30T19:11:50Z",
      "dispatchDeadline": "600s",
      "view": "BASIC"
    }
    

## Create a batch of tasks

You can create a batch of target tasks and add the batch to an existing queue by using the [projects.locations.queues.tasks.batchCreate](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations.queues.tasks/batchCreate) method to create a list of requests.

Note the following:

  * All tasks must be added to the same queue.

  * There is a limit to how many tasks can be created in a single batch. For more information, see [Quotas and limits](https://docs.cloud.google.com/tasks/docs/quotas#limits).

  * Batch requests, which aggregate individual operations into a single request, are not atomic because it's possible for some of the operations contained within the batch to fail while others succeed.

  * You can also delete a batch of tasks. For more information, see [Delete a batch of tasks from a queue](https://docs.cloud.google.com/tasks/docs/manage-queues-and-tasks#delete-batch-tasks).




###  HTTP tasks 

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: required. The project ID of the Google Cloud project where the tasks will be created.
  * `REGION`: required. The [region](https://docs.cloud.google.com/tasks/docs/locations) in which the queue is deployed—for example, `us-central1`.
  * `QUEUE_ID`: required. The ID of the queue to which the tasks will be added.
  * `URL`: required. The fully qualified URL that the request will be sent to. This string must begin with either `http://` or `https://`—for example: `https://www.example.com`. **Note:** To target a Cloud Run service or function, use its [default `run.app` URL](https://docs.cloud.google.com/run/docs/triggering/https-request#url).
  * `SERVICE_ACCOUNT_EMAIL`: optional. The service account email used to generate an authorization token that is included in the request sent to the target when executing the task. The service account must be in the same project as the queue. The caller must have the [`iam.serviceAccounts.actAs`](https://docs.cloud.google.com/iam/docs/service-account-permissions#attaching) permission for the service account. 

To generate an OAuth2 access token instead of an OpenID Connect token, replace the `oidcToken` field with `oauthToken` to specify the service account email.




The request body contains a list of requests.

Request JSON body: 
    
    
    {
      "requests": [
        {
          "task": {
            "httpRequest": {
              "url": "URL",
              "httpMethod": "POST",
              "oidcToken": {
                "serviceAccountEmail": "SERVICE_ACCOUNT_EMAIL"
              }
            },
            "scheduleTime": "SCHEDULE_TIME"
          }
        }
      ]
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "requests": [
        {
          "task": {
            "httpRequest": {
              "url": "URL",
              "httpMethod": "POST",
              "oidcToken": {
                "serviceAccountEmail": "SERVICE_ACCOUNT_EMAIL"
              }
            },
            "scheduleTime": "SCHEDULE_TIME"
          }
        }
      ]
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://cloudtasks.googleapis.com/v2/projects/PROJECT_ID/locations/REGION/queues/QUEUE_ID/tasks:batchCreate"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "requests": [
        {
          "task": {
            "httpRequest": {
              "url": "URL",
              "httpMethod": "POST",
              "oidcToken": {
                "serviceAccountEmail": "SERVICE_ACCOUNT_EMAIL"
              }
            },
            "scheduleTime": "SCHEDULE_TIME"
          }
        }
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
        -Uri "https://cloudtasks.googleapis.com/v2/projects/PROJECT_ID/locations/REGION/queues/QUEUE_ID/tasks:batchCreate" | Select-Object -Expand Content

#### APIs Explorer (browser)

Copy the request body and open the [method reference page](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations.queues.tasks/batchCreate). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Paste the request body in this tool, complete any other required fields, and click **Execute**. 

If successful, the response body contains an instance of the `Operation` resource. 
    
    
    {
      "name": "projects/PROJECT_ID/locations/REGION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.tasks.v2.BatchCreateTasksMetadata"
      },
      "done": false
    }
    

###  App Engine tasks 

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: required. The project ID of the Google Cloud project where the task will be created.
  * `REGION`: required. The [region](https://docs.cloud.google.com/tasks/docs/locations) in which the queue is deployed.
  * `QUEUE_ID`: required. The ID of the queue to which the tasks will be added.
  * `RELATIVE_URI`: required. The relative URI of the request. The path must begin with a forward slash (`/`). If not specified, the root path is used (`/`).
  * `SERVICE`: optional. The App Engine service which will process the task. By default, the task is sent to the service which is the default service when the task is attempted.
  * `VERSION`: optional. The App Engine version which will process the task. By default, the task is sent to the version which is the default version when the task is attempted.
  * `SCHEDULE_TIME`: optional. The time when the task is scheduled to be attempted, in RFC 3339 format—for example, `2026-10-02T15:01:23Z`. If the time isn't set or is in the past, Cloud Tasks will set it to the current time.



The request body contains a list of requests.

Request JSON body: 
    
    
    {
      "requests": [
        {
          "task": {
            "appEngineHttpRequest": {
              "httpMethod": "POST",
              "relativeUri": "RELATIVE_URI",
              "appEngineRouting": {
                "service": "SERVICE",
                "version": "VERSION"
              }
            },
            "scheduleTime": "SCHEDULE_TIME"
          }
        }
      ]
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "requests": [
        {
          "task": {
            "appEngineHttpRequest": {
              "httpMethod": "POST",
              "relativeUri": "RELATIVE_URI",
              "appEngineRouting": {
                "service": "SERVICE",
                "version": "VERSION"
              }
            },
            "scheduleTime": "SCHEDULE_TIME"
          }
        }
      ]
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://cloudtasks.googleapis.com/v2/projects/PROJECT_ID/locations/REGION/queues/QUEUE_ID/tasks:batchCreate"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "requests": [
        {
          "task": {
            "appEngineHttpRequest": {
              "httpMethod": "POST",
              "relativeUri": "RELATIVE_URI",
              "appEngineRouting": {
                "service": "SERVICE",
                "version": "VERSION"
              }
            },
            "scheduleTime": "SCHEDULE_TIME"
          }
        }
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
        -Uri "https://cloudtasks.googleapis.com/v2/projects/PROJECT_ID/locations/REGION/queues/QUEUE_ID/tasks:batchCreate" | Select-Object -Expand Content

#### APIs Explorer (browser)

Copy the request body and open the [method reference page](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations.queues.tasks/batchCreate). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Paste the request body in this tool, complete any other required fields, and click **Execute**. 

If successful, the response body contains an instance of the `Operation` resource. 
    
    
    {
      "name": "projects/PROJECT_ID/locations/REGION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.tasks.v2.BatchCreateTasksMetadata"
      },
      "done": false
    }
    

## What's next

  * [Configure queue routing, limits, and retries](https://docs.cloud.google.com/tasks/docs/configuring-queues)
  * [Set retry parameters for a task](https://docs.cloud.google.com/tasks/docs/configure-retry-task)
  * [Manage queues and tasks](https://docs.cloud.google.com/tasks/docs/manage-queues-and-tasks)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
