---
url: https://docs.cloud.google.com/appengine/migration-center/standard/python/migrating-push-queues/
title: Migrate push queues to Cloud Tasks (Python) \u00a0|\u00a0 App Engine migration center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:56:40.223273+00:00
---

# Migrate push queues to Cloud Tasks (Python)  |  App Engine migration center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/migration-center/standard/python/migrating-push-queues/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Migration center ](https://docs.cloud.google.com/appengine/migration-center)
  * [ Guides ](https://docs.cloud.google.com/appengine/migration-center/standard/services/migrating-services)



Send feedback 

#  Migrate push queues to Cloud Tasks (Python) Stay organized with collections  Save and categorize content based on your preferences. 

Before you upgrade to the latest App Engine services SDK version, review the [migration overview](https://docs.cloud.google.com/appengine/migration-center/standard/python/migrating-push-queues-overview).

## Upgrade to the Cloud Tasks client libraries

If you prefer to move away from legacy bundled services entirely, you can migrate your code to use the Cloud Tasks API directly. This requires refactoring your application code.

With Cloud Tasks, you access the same service that you access with the Task Queues RPC API. This means that you don't need to recreate your existing push queues and push tasks. However, you must migrate code that creates or interacts with push queues or push tasks in order to use the Cloud Tasks API.

You can create and interact with push queues and push tasks using the Cloud Tasks REST and RPC APIs, the Cloud Tasks client library, the Google Cloud CLI, and the [Google Cloud console](https://console.cloud.google.com/). This page provides examples using the gcloud CLI and the Cloud Tasks client library.

### Features not available in Cloud Tasks

For the Cloud Tasks client libraries migration, the following features are not available in Cloud Tasks:

  * Enqueueing tasks in Datastore transactions
  * Using the deferred tasks library instead of a worker service
  * Working with tasks in multi-tenant applications
  * Simulating with the local development server
  * Adding tasks asynchronously



Alternatively, if you [upgrade to the latest SDK](https://docs.cloud.google.com/appengine/migration-center/standard/python/migrating-push-queues-upgrade-sdk), features like deferred tasks, namespaces, and local simulation are supported through the SDK wrapper.

## Pricing and quotas

Migrating your push queues to Cloud Tasks might affect the pricing and quotas for your app.

### Pricing

Review the [Cloud Tasks pricing](https://cloud.google.com/tasks/pricing) to estimate your monthly cost before migrating.

Similar to Task Queues, sending requests to your App Engine app with a Cloud Tasks push target is free. However, unlike Task Queues, Cloud Tasks charges for operation performed, such as creating, deleting, or managing tasks. This might lead to higher overall monthly cost compared to the complimentary App Engine Task Queue.

### Quotas

Cloud Tasks requests also count towards your App Engine requests quotas.

Like Task Queues, Cloud Tasks has service-specific [quotas](https://cloud.google.com/tasks/docs/quotas). Migrating to Cloud Tasks will likely change your quotas.

## Before you begin

If you have not done so already, set up your [Python development environment](https://docs.cloud.google.com/python/docs/setup) to use a Python version that is compatible with Google Cloud, and install testing tools for creating isolated Python environments. 

The following sections discuss the setup steps before migrating your push queues to Cloud Tasks.

### Migrate pull queues

Before you begin, [migrate pull queues](https://docs.cloud.google.com/appengine/migration-center/standard/python/migrating-pull-queues) before following the instructions in this guide to migrate push queues. Migrating pull queues after migrating push queues is not recommended because the required use of the `queue.yaml` file is likely to cause unexpected behavior with Cloud Tasks.

### Protect queue configuration

Once you begin the process of migrating to Cloud Tasks, modifying your `queue.yaml` file can cause unexpected behavior and is not recommended. Protect your queue configuration from modifications by the `queue.yaml` file with the following steps.

  1. Configure the gcloud CLI to omit your `queue.yaml` file in future deployments.

Add your `queue.yaml` file to a `.gcloudignore` file. To check if you already have a `.gcloudignore` file, you can run the following command in your terminal from the top level directory of your app. This command will output the filename if the file exists.
         
         ls -a | grep .gcloudignore

To learn more about `.gcloudignore` files, read the [`.gcloudignore` reference](https://docs.cloud.google.com/sdk/gcloud/reference/topic/gcloudignore).

  2. Restrict permissions on your `queue.yaml` file.

Follow the best practices described in our guide on [securing queue configuration](https://docs.cloud.google.com/tasks/docs/secure-queue-configuration).

  3. Learn about Cloud Tasks and the `queue.yaml` file (optional).

When using the Cloud Tasks API to manage your queue configuration, deploying a `queue.yaml` file overrides the configuration set by Cloud Tasks, which can cause unexpected behavior. Read [Using queue management versus queue.yaml](https://docs.cloud.google.com/tasks/docs/queue-yaml) to learn more.




### Authenticate your app to the Cloud Tasks API

You must authenticate your app to the Cloud Tasks API. This section discusses authentication for two different use cases.

To develop or test your app locally, we recommend using a service account. For instructions on setting up a service account and connecting it to your app, read [Obtaining and providing service account credentials manually](https://docs.cloud.google.com/docs/authentication#service-accounts).

To deploy your app on App Engine, you don't need to provide any new authentication. The Application Default Credentials (ADC) infer authentication details for App Engine apps.

### Import the Cloud Client Libraries

To use the Cloud Tasks client library with your App Engine app: 

  1. Update the `app.yaml` file. Follow the instructions for your version of Python:

###  Python 2 

For Python 2 apps, add the latest versions of `grpcio` and `setuptools` libraries.

The following is an example `app.yaml` file:
         
         runtime: python27
         threadsafe: yes
         api_version: 1
         
         libraries:
         - name: grpcio
           version: latest
         - name: setuptools
           version: latest
         

###  Python 3 

For Python 3 apps, specify the `runtime` element in your `app.yaml` file with a supported Python 3 version. For example:
         
         runtime: python310 # or another support version
         

The Python 3 runtime installs libraries automatically, so you don't need to specify built-in libraries from the previous Python 2 runtime. If your Python 3 app is using other legacy bundled services when migrating, you can continue to specify the necessary built-in libraries. Otherwise, you can delete the unnecessary lines in your `app.yaml` file.

  2. Update the `requirements.txt` file. Follow the instructions for your version of Python:

###  Python 2 

Add the Cloud Client Libraries for Cloud Tasks to your list of dependencies in the `requirements.txt` file.
         
         google-cloud-tasks
         

Then run `pip install -t lib -r requirements.txt` to update the list of available libraries for your app.

###  Python 3 

Add the Cloud Client Libraries for Cloud Tasks to your list of dependencies in the `requirements.txt` file.
         
         google-cloud-tasks
         

App Engine automatically installs these dependencies during app deployment in the Python 3 runtime, so delete the `lib` folder if one exists.

  3. For Python 2 apps, if your app is using built-in or copied libraries, you must specify those paths in the `appengine_config.py` file, located in the same folder as your `app.yaml` file:
         
         import pkg_resources
         from google.appengine.ext import vendor
         
         # Set PATH to your libraries folder.
         PATH = 'lib'
         # Add libraries installed in the PATH folder.
         vendor.add(PATH)
         # Add libraries to pkg_resources working set to find the distribution.
         pkg_resources.working_set.add_entry(PATH)
         

The `appengine_config.py` file assumes that the current working directory is where the `lib` folder is located. In some cases, such as unit tests, the current working directory can be different. To avoid errors, you can explicitly pass in the full path to the `lib` folder using:
         
         import os
         path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'lib')

  4. Import the Cloud Tasks client library in any files that use push queues from the Task Queues API:
         
         from google.cloud import tasks

When you have successfully completed the full migration of all your code that creates or interacts with push queues to Cloud Tasks, remove statements that import the Task Queues API; for example, `from google.appengine.api import taskqueue`.




## Create and manage queues

This section describes how to create and manage queues using the Cloud Tasks API.

With Cloud Tasks, you don't use a `queue.yaml` file to create or manage queues. Instead, you use the Cloud Tasks API. Using both a `queue.yaml` file and the Cloud Tasks API is not recommended, but it might be an inevitable part of migrating from Task Queues to Cloud Tasks depending on your app. Read [Using Queue management versus queue.yaml](https://docs.cloud.google.com/tasks/docs/queue-yaml) to learn about best practices.

### Create queues

Read this section if your app creates queues programmatically, or if you want to create additional queues from the command line.

In Cloud Tasks, queue names have the form `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID`. The `LOCATION_ID` portion of the queue name corresponds to a Google Cloud _region_. The `QUEUE_ID` portion of the queue name is equivalent to the Task Queues queue `name` field. The queue name is generated during queue creation based on the project, region and `QUEUE_ID` you specify.

In general, the queue location (i.e., region) must be the same as the region of your app. The two exceptions to this rule are for apps using the `europe-west` region and apps using the `us-central` region. In Cloud Tasks, these regions are called `europe-west1` and `us-central1` respectively.

You can specify optional queue configuration during queue creation, however you can also do so by updating the queue after it has been created.

You don't need to recreate existing queues. Instead, migrate the code that interacts with your existing queues by reading the relevant parts of this guide.

**Note:** The App Engine Task Queue service automatically creates a default queue named `default`. Cloud Tasks does not automatically create this queue.

#### Reuse queue names

You must wait 7 days after deleting a queue to create a queue with the same queue ID in the same project and location (i.e., region).

The following example creates two queues using Cloud Tasks. The first queue has queue ID `queue-blue`, and is configured to send all tasks to the version `v2` of the service `task-module` at a rate of `5/s`. The second queue has queue ID `queue-red` and dispatches tasks at a rate of `1/s`. Both are created on the project with project ID `my-project-id` in location `us-central1`. This is the Cloud Tasks equivalent of [creating queues](https://docs.cloud.google.com/appengine/docs/standard/services/taskqueue/push/creating-push-queues#using_a_queue_configuration_file_to_create_queues) in Task Queues.

### gcloud

The gcloud CLI infers the project and location from the gcloud CLI configuration.
    
    
    gcloud tasks queues create queue-blue \
        --max-dispatches-per-second=5 \
        --routing-override=service:task-module,version:v2
    
    
    gcloud tasks queues create queue-red \
        --max-dispatches-per-second=1

### client library
    
    
    client = tasks.CloudTasksClient()
    
    # TODO(developer): Uncomment these lines and replace with your values.
    # project = 'my-project-id'
    # location = 'us- central1'
    # queue_blue_name = 'queue-blue'
    # queue_red_name = 'queue-red'
    
    parent = f"projects/{project}/locations/{location}"
    
    queue_blue = {
        "name": client.queue_path(project, location, queue_blue_name),
        "rate_limits": {"max_dispatches_per_second": 5},
        "app_engine_routing_override": {"version": "v2", "service": "task-module"},
    }
    
    queue_red = {
        "name": client.queue_path(project, location, queue_red_name),
        "rate_limits": {"max_dispatches_per_second": 1},
    }
    
    queues = [queue_blue, queue_red]
    for queue in queues:
        response = client.create_queue(parent=parent, queue=queue)
        print(response)

To learn more, read the Cloud Tasks reference [Creating a Cloud Tasks queue](https://docs.cloud.google.com/tasks/docs/creating-queues#creating_a_queue).

### Set the queue processing rate

The following table lists the fields that differ from Task Queues to Cloud Tasks.

Task Queues field | Cloud Tasks field | Description  
---|---|---  
`rate` | `max_dispatches_per_second` | The maximum rate at which tasks are dispatched from the queue  
`max_concurrent_requests` | `max_concurrent_dispatches` | The maximum number of concurrent tasks that can be dispatched from the queue  
`bucket_size` | `max_burst_size` |  Cloud Tasks calculates a get-only property `max_burst_size` that limits how fast tasks in the queue are processed based on the value of `max_dispatches_per_second`. This field allows the queue to have a high rate so that processing starts shortly after a task is enqueued, but still limits resource usage when many tasks are enqueued in a short period of time.  For App Engine queues that were created or updated using a `queue.yaml` file, `max_burst_size` is initially equal to `bucket_size`. However, if the queue is later passed to an `update` command using any Cloud Tasks interface, `max_burst_size` will be reset based on the value of `max_dispatches_per_second`, regardless of whether `max_dispatches_per_second` is updated.   
`total_storage_limit` | Deprecated in Cloud Tasks | Cloud Tasks does not support setting a custom storage limit  
  
You can set the queue processing rate when you create the queue or update it afterwards. The following example uses Cloud Tasks to set the processing rate on a queue named `queue-blue` that has already been created. If `queue-blue` was created or configured using a `queue.yaml` file, the following example resets`max_burst_size` based on the `max_dispatches_per_second` value of `20`. This is the Cloud Tasks equivalent of [setting the queue processing rate](https://docs.cloud.google.com/appengine/docs/standard/services/taskqueue/push/creating-push-queues#defining_the_push_queue_processing_rate) in Task Queues.

### gcloud
    
    
    gcloud tasks queues update queue-blue \
        --max-dispatches-per-second=20 \
        --max-concurrent-dispatches=10

### client library
    
    
    client = tasks.CloudTasksClient()
    
    # TODO(developer): Uncomment these lines and replace with your values.
    # project = 'my-project-id'
    # location = 'us- central1'
    # queue = 'queue-blue'
    
    # Get queue object
    queue_path = client.queue_path(project, location, queue)
    queue = client.get_queue(name=queue_path)
    
    # Update queue object
    queue.rate_limits.max_dispatches_per_second = 20
    queue.rate_limits.max_concurrent_dispatches = 10
    
    response = client.update_queue(queue=queue)
    print(response)

To learn more, see [Define rate limits](https://docs.cloud.google.com/tasks/docs/configuring-queues#rate).

### Disable and resuming queues

Cloud Tasks uses the term _pause_ in the same way that Task Queues uses the term _disable_. Pausing a queue stops the tasks in the queue from executing until the queue is resumed. However, you can continue to add tasks to a queue that is paused. Cloud Tasks uses the term _resume_ in the same way as Task Queues does.

The following example pauses a queue with queue ID `queue1`. This is the Cloud Tasks equivalent of [disabling queues](https://docs.cloud.google.com/appengine/docs/standard/services/taskqueue/push/deleting-tasks-and-queues#disabling_queues) in Task Queues.

### gcloud
    
    
    gcloud tasks queues pause queue1

### client library
    
    
    client = tasks.CloudTasksClient()
    
    # TODO(developer): Uncomment these lines and replace with your values.
    # project = 'my-project-id'
    # location = 'us- central1'
    # queue = 'queue1'
    
    queue_path = client.queue_path(project, location, queue)
    response = client.pause_queue(name=queue_path)

To learn more, read the Cloud Tasks reference [Pausing queues](https://docs.cloud.google.com/tasks/docs/deleting-appengine-queues-and-tasks#pause-queues).

### Delete queues

Once you delete a queue, you must wait 7 days before creating a queue with the same name. Consider purging all tasks from a queue and reconfiguring the queue if you cannot wait 7 days.

The following example deletes the queue with queue ID `queue1`. This is the Cloud Tasks equivalent of [deleting queues](https://docs.cloud.google.com/appengine/docs/standard/services/taskqueue/push/deleting-tasks-and-queues#deleting_queues) in Task Queues.

### gcloud
    
    
    gcloud tasks queues delete queue1

### client library
    
    
    client = tasks.CloudTasksClient()
    
    # TODO(developer): Uncomment these lines and replace with your values.
    # project = 'my-project-id'
    # location = 'us- central1'
    # queue = 'queue1'
    
    queue_path = client.queue_path(project, location, queue)
    response = client.delete_queue(name=queue_path)

To learn more, read the Cloud Tasks reference [Deleting queues](https://docs.cloud.google.com/tasks/docs/deleting-appengine-queues-and-tasks#delete-queues).

## Create and managing tasks

This section describes how to create and manage tasks using the Cloud Tasks API.

### Create tasks

The following table lists the fields that differ from Task Queues to Cloud Tasks.

Task Queues field | Cloud Tasks field | Description  
---|---|---  
N/A | `app_engine_http_request` | Creates a request that targets an App Engine service. These tasks are referred to as App Engine tasks.  
`method` | `http_method` | Specifies the request method; for example, `POST`  
`url` | `relative_uri` | Specifies the task handler. Note the difference in the final letter: `i` for _uniform resource identifier_ rather than `l` for _uniform resource locator_  
`target` | `app_engine_routing` | Optional. Specifies the App Engine `service`, `version`, and `instance` for an App Engine task. If not set, the default service, version, and instance are used.  
  
The following example creates a task that routes to an App Engine service named `worker` with the `/update_counter` handler . This is the Cloud Tasks equivalent to [creating tasks](https://docs.cloud.google.com/appengine/docs/standard/services/taskqueue/push/creating-push-tasks#creating_a_new_task) in Task Queues.

### gcloud
    
    
    gcloud tasks create-app-engine-task \
        --queue=default \
        --method=POST \
        --relative-uri=/update_counter \
        --routing=service:worker \
        --body-content=10

### client library
    
    
    client = tasks.CloudTasksClient()
    
    # TODO(developer): Uncomment these lines and replace with your values.
    # project = 'my-project-id'
    # location = 'us- central1'
    # queue = 'default'
    amount = 10
    
    parent = client.queue_path(project, location, queue)
    
    task = {
        "app_engine_http_request": {
            "http_method": tasks.HttpMethod.POST,
            "relative_uri": "/update_counter",
            "app_engine_routing": {"service": "worker"},
            "body": str(amount).encode(),
        }
    }
    
    response = client.create_task(parent=parent, task=task)
    eta = response.schedule_time.strftime("%m/%d/%Y, %H:%M:%S")
    print(f"Task {response.name} enqueued, ETA {eta}.")

To learn more, read the Cloud Tasks reference [Creating App Engine tasks](https://docs.cloud.google.com/tasks/docs/creating-appengine-tasks).

### Specify the target service and routing

Specifying the App Engine target service, version, and instance for App Engine tasks is optional. By default, App Engine tasks are routed to the service, version, and instance that are the default at the time the task is attempted.

Set the task's `app_engine_routing` property during task creation to specify a different App Engine service, version, or instance for your task.

To route all tasks on a given queue to the same App Engine service, version, and instance, you can set the `app_engine_routing_override` property on the queue.

To learn more, read the Cloud Tasks reference [Configure routing](https://docs.cloud.google.com/tasks/docs/configuring-queues#routing).

### Pass data to the handler

As with Task Queues, you can pass data to the handler in two ways using Cloud Tasks. You can either pass data as query parameters in the relative URI, or you can pass data in the request body using the HTTP methods POST or PUT.

Cloud Tasks uses the term _body_ in the same way that Task Queues uses the term _payload_. In Cloud Tasks, the default body content type is octet-stream rather than plain text. You can set the body content type by specifying it in the header.

The following example passes a key to the handler `/update_counter` in two different ways. This is the Cloud Tasks equivalent of [passing data to the handler](https://docs.cloud.google.com/appengine/docs/standard/services/taskqueue/push/creating-push-tasks#passing_data) in Task Queues.

### gcloud
    
    
    gcloud tasks create-app-engine-task \
        --queue=default \
        --method=GET  \
        --relative-uri=/update_counter?key=blue \
        --routing=service:worker
    
    
    gcloud tasks create-app-engine-task \
        --queue=default \
        --method=POST \
        --relative-uri=/update_counter \
        --routing=service:worker \
        --body-content="{'key': 'blue'}"

### client library
    
    
    import json
    
    client = tasks.CloudTasksClient()
    
    # TODO(developer): Uncomment these lines and replace with your values.
    # project = 'my-project-id'
    # location = 'us- central1'
    # queue = 'default'
    
    parent = client.queue_path(project, location, queue)
    
    task1 = {
        "app_engine_http_request": {
            "http_method": tasks.HttpMethod.POST,
            "relative_uri": "/update_counter?key=blue",
            "app_engine_routing": {"service": "worker"},
        }
    }
    
    task2 = {
        "app_engine_http_request": {
            "http_method": tasks.HttpMethod.POST,
            "relative_uri": "/update_counter",
            "app_engine_routing": {"service": "worker"},
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"key": "blue"}).encode(),
        }
    }
    
    response = client.create_task(parent=parent, task=task1)
    print(response)
    response = client.create_task(parent=parent, task=task2)
    print(response)

### Specify the task name

Specifying the task name is optional. If you don't specify the task name, Cloud Tasks constructs it for you by generating a task ID and inferring the project and location (i.e., region) based on the queue you specified during task creation.

Task names have the form `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID/tasks/TASK_ID`. The `TASK_ID` portion of the task name is equivalent to the Task Queues task `name` field.

#### Reuse task names

You must wait before reusing the name of a task. The amount of time you must wait before doing so differs based on whether the queue dispatching the task was created in Cloud Tasks or Task Queues.

For tasks on queues that were created using Task Queues (including the default queue), you must wait approximately 9 days after the original task was deleted or executed. For tasks on queues that were created using Cloud Tasks, you must wait approximately 1 hour after the original task was deleted or executed.

The following example creates a task with the `TASK_ID` set to `first-try`, and adds it to the default queue. This is the Cloud Tasks equivalent of [naming tasks](https://docs.cloud.google.com/appengine/docs/standard/services/taskqueue/push/creating-push-tasks#naming_a_task) in Task Queues.

### gcloud

The gcloud CLI constructs the task name by inferring the project and location from your configuration.
    
    
    gcloud tasks create-app-engine-task first-try \
        --queue=default \
        --method=GET \
        --relative-uri=/url/path

### client library

With the client library, you must specify the full task name if you want to specify the `TASK_ID`. The project and location must match the project and location of the queue to which the task is added.
    
    
    client = tasks.CloudTasksClient()
    
    # TODO(developer): Uncomment these lines and replace with your values.
    # project = 'my-project-id'
    # location = 'us- central1'
    # queue = 'default'
    # task_name = 'first-try'
    
    parent = client.queue_path(project, location, queue)
    
    task = {
        "name": client.task_path(project, location, queue, task_name),
        "app_engine_http_request": {
            "http_method": tasks.HttpMethod.GET,
            "relative_uri": "/url/path",
        },
    }
    response = client.create_task(parent=parent, task=task)
    print(response)

### Retry failed tasks

You can set task retry configuration on queues during queue creation, or by updating the queue. The following table lists the Task Queues field and the corresponding Cloud Tasks field.

Task Queues field | Cloud Tasks field  
---|---  
`task_retry_limit` | `max_attempts`  
`task_age_limit` | `max_retry_duration`  
`min_backoff_seconds` | `min_backoff`  
`max_backoff_seconds` | `max_backoff`  
`max_doublings` | `max_doublings`  
  
#### Use task-specific retry parameters

Task-specific retry parameters that were configured in Task Queues work in Cloud Tasks, however you cannot edit them or set them on new tasks. To change the retry parameters for a task that has task-specific retry parameters, recreate the task with a Cloud Tasks queue that has the desired retry parameters.

The following example demonstrates various retry scenarios:

  * In `fooqueue`, tasks are retried up to seven times and for up to two days from the first execution attempt. After both limits are passed, it fails permanently.
  * In `barqueue`, App Engine attempts to retry tasks, increasing the interval linearly between each retry until reaching the maximum backoff and retrying indefinitely at the maximum interval (so the intervals between requests are 10s, 20s, 30s, ..., 190s, 200s, 200s, ...).
  * In `bazqueue`, the retry interval starts at 10s, then doubles three times, then increases linearly, and finally retries indefinitely at the maximum interval (so the intervals between requests are 10s, 20s, 40s, 80s, 160s, 240s, 300s, 300s, ...).



This is the Cloud Tasks equivalent of [retrying tasks](https://docs.cloud.google.com/appengine/docs/standard/services/taskqueue/push/retrying-tasks) in Task Queues.

### gcloud

When setting options that specify a number of seconds, you must include `s` after the integer number (e.g. `200s` not `200`).
    
    
    gcloud tasks queues create fooqueue \
        --max-attempts=7 \
        --max-retry-duration=172800s  #2*60*60*24 seconds in 2 days
    
    
    gcloud tasks queues create barqueue \
        --min-backoff=10s \
        --max-backoff=200s \
        --max-doublings=0
    
    
    gcloud tasks queues create bazqueue \
        --min-backoff=10s \
        --max-backoff=300s \
        --max-doublings=3

### client library
    
    
    from google.protobuf import duration_pb2
    
    client = tasks.CloudTasksClient()
    
    # TODO(developer): Uncomment these lines and replace with your values.
    # project = 'my-project-id'
    # location = 'us- central1'
    # fooqueue = 'fooqueue'
    # barqueue = 'barqueue'
    # bazqueue = 'bazqueue'
    
    parent = f"projects/{project}/locations/{location}"
    
    max_retry = duration_pb2.Duration()
    max_retry.seconds = 2 * 60 * 60 * 24
    
    foo = {
        "name": client.queue_path(project, location, fooqueue),
        "rate_limits": {"max_dispatches_per_second": 1},
        "retry_config": {"max_attempts": 7, "max_retry_duration": max_retry},
    }
    
    min = duration_pb2.Duration()
    min.seconds = 10
    
    max = duration_pb2.Duration()
    max.seconds = 200
    
    bar = {
        "name": client.queue_path(project, location, barqueue),
        "rate_limits": {"max_dispatches_per_second": 1},
        "retry_config": {"min_backoff": min, "max_backoff": max, "max_doublings": 0},
    }
    
    max.seconds = 300
    baz = {
        "name": client.queue_path(project, location, bazqueue),
        "rate_limits": {"max_dispatches_per_second": 1},
        "retry_config": {"min_backoff": min, "max_backoff": max, "max_doublings": 3},
    }
    
    queues = [foo, bar, baz]
    for queue in queues:
        response = client.create_queue(parent=parent, queue=queue)
        print(response)

To learn more, read the Cloud Tasks reference [Set retry parameters](https://docs.cloud.google.com/tasks/docs/configuring-queues#retry).

### Delete tasks from a queue

When you delete a task, you must wait 9 days before creating a task with the same name if the task was on a queue created using a `queue.yaml` file, or 1 hour if the task was on a queue created using Cloud Tasks.

The following example deletes the task with task ID `foo` from the queue with queue ID `queue1`. This is the Cloud Tasks equivalent of [deleting tasks](https://docs.cloud.google.com/appengine/docs/standard/services/taskqueue/push/deleting-tasks-and-queues#deleting_tasks_from_a_queue) in Task Queues.

### gcloud

The task project and location are inferred from the gcloud CLI default project.
    
    
    gcloud tasks delete foo --queue=queue1

### client library
    
    
    client = tasks.CloudTasksClient()
    
    # TODO(developer): Uncomment these lines and replace with your values.
    # project = 'my-project-id'
    # location = 'us- central1'
    # queue = 'queue1'
    
    task_path = client.task_path(project, location, queue, "foo")
    response = client.delete_task(name=task_path)

To learn more, read the Cloud Tasks reference [Deleting a task from a queue](https://docs.cloud.google.com/tasks/docs/deleting-appengine-queues-and-tasks#delete-task).

### Purge tasks

The following example purges all tasks from the queue with queue ID `queue1`. This is the Cloud Tasks equivalent of [purging tasks](https://docs.cloud.google.com/appengine/docs/standard/services/taskqueue/push/deleting-tasks-and-queues#purging_all_tasks_from_a_queue) in Task Queues.

### gcloud

The queue project and location are inferred from the gcloud CLI default project.
    
    
    gcloud tasks queues purge queue1

### client library
    
    
    client = tasks.CloudTasksClient()
    
    # TODO(developer): Uncomment these lines and replace with your values.
    # project = 'my-project-id'
    # location = 'us- central1'
    # queue = 'queue1'
    
    queue_path = client.queue_path(project, location, queue)
    response = client.purge_queue(name=queue_path)

To learn more, read the Cloud Tasks reference [Purging all tasks from a queue](https://docs.cloud.google.com/tasks/docs/deleting-appengine-queues-and-tasks#purge-tasks).

## What's next

  * [Cloud Tasks documentation](https://docs.cloud.google.com/tasks/docs)
  * [Cloud Tasks client library](https://docs.cloud.google.com/tasks/docs/reference/libraries)
  * [Cloud Tasks REST reference](https://docs.cloud.google.com/tasks/docs/reference/rest) overview
  * [Cloud Tasks RPC reference](https://docs.cloud.google.com/tasks/docs/reference/rpc) overview 
  * For a tutorial, see the [Migrate from App Engine Task Queue push queues to Cloud Tasks codelab](https://codelabs.developers.google.com/codelabs/cloud-gae-python-migrate-8-cloudtasks). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
