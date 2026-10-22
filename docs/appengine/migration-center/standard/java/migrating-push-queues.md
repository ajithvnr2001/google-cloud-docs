---
url: https://docs.cloud.google.com/appengine/migration-center/standard/java/migrating-push-queues/
title: Migrate push queues to Cloud Tasks (Java) \u00a0|\u00a0 App Engine migration center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:48:45.998750+00:00
---

# Migrate push queues to Cloud Tasks (Java)  |  App Engine migration center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/migration-center/standard/java/migrating-push-queues/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Migration center ](https://docs.cloud.google.com/appengine/migration-center)
  * [ Guides ](https://docs.cloud.google.com/appengine/migration-center/standard/services/migrating-services)



Send feedback 

#  Migrate push queues to Cloud Tasks (Java) Stay organized with collections  Save and categorize content based on your preferences. 

Before you upgrade to the latest App Engine services SDK version, review the [migration overview](https://docs.cloud.google.com/appengine/migration-center/standard/java/migrating-push-queues-overview).

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



Alternatively, if you [upgrade to the latest SDK](https://docs.cloud.google.com/appengine/migration-center/standard/java/migrating-push-queues-upgrade-sdk), features like deferred tasks, namespaces, and local simulation are supported through the SDK wrapper.

## Pricing and quotas

Migrating your push queues to Cloud Tasks might affect the pricing and quotas for your app.

### Pricing

Review the [Cloud Tasks pricing](https://cloud.google.com/tasks/pricing) to estimate your monthly cost before migrating.

Similar to Task Queues, sending requests to your App Engine app with a Cloud Tasks push target is free. However, unlike Task Queues, Cloud Tasks charges for operation performed, such as creating, deleting, or managing tasks. This might lead to higher overall monthly cost compared to the complimentary App Engine Task Queue.

### Quotas

Cloud Tasks requests also count towards your App Engine requests quotas.

Like Task Queues, Cloud Tasks has service-specific [quotas](https://cloud.google.com/tasks/docs/quotas). Migrating to Cloud Tasks will likely change your quotas.

## Before you begin

The following sections discuss the setup steps before migrating your push queues to Cloud Tasks.

### Migrate pull queues

Before you begin, [migrate pull queues](https://docs.cloud.google.com/appengine/migration-center/standard/java/migrating-pull-queues) before following the instructions in this guide to migrate push queues. Migrating pull queues after migrating push queues is not recommended because the required use of the `queue.yaml` file is likely to cause unexpected behavior with Cloud Tasks.

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

  1. Specify the Cloud Tasks client library dependency in your `pom.xml` file:
         
         <dependency>
           <groupId>com.google.cloud</groupId>
           <artifactId>google-cloud-tasks</artifactId>
           <version>1.3.0</version>
         </dependency>

  2. Import the Cloud Tasks client library dependencies in the files that are responsible for creating and enqueueing your tasks:
         
         import com.google.cloud.tasks.v2.[AppEngineHttpRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.AppEngineHttpRequest.html);
         import com.google.cloud.tasks.v2.[CloudTasksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.CloudTasksClient.html);
         import com.google.cloud.tasks.v2.[HttpMethod](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.HttpMethod.html);
         import com.google.cloud.tasks.v2.[QueueName](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.QueueName.html);
         import com.google.cloud.tasks.v2.[Task](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Task.html);




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

The following example creates two queues using Cloud Tasks. The first queue has queue ID `queue-blue`, and is configured to send all tasks to the version `v2` of the service `task-module` at a rate of `5/s`. The second queue has queue ID `queue-red` and dispatches tasks at a rate of `1/s`. Both are created on the project with project ID `your-project-id` in location `us-central1`. This is the Cloud Tasks equivalent of [creating queues](https://docs.cloud.google.com/appengine/docs/standard/services/taskqueue/push/creating-push-queues#using_a_queue_configuration_file_to_create_queues) in Task Queues.

### gcloud

The gcloud CLI infers the project and location from the gcloud CLI configuration.
    
    
    gcloud tasks queues create queue-blue \
        --max-dispatches-per-second=5 \
        --routing-override=service:task-module,version:v2
    
    
    gcloud tasks queues create queue-red \
        --max-dispatches-per-second=1

### client library
    
    
    import com.google.cloud.tasks.v2.[AppEngineRouting](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.AppEngineRouting.html);
    import com.google.cloud.tasks.v2.[CloudTasksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.CloudTasksClient.html);
    import com.google.cloud.tasks.v2.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.LocationName.html);
    import com.google.cloud.tasks.v2.[Queue](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Queue.html);
    import com.google.cloud.tasks.v2.[QueueName](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.QueueName.html);
    import com.google.cloud.tasks.v2.[RateLimits](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.RateLimits.html);
    
    public class CreateQueue {
      public static void createQueue(
          String projectId, String locationId, String queueBlueName, String queueRedName)
          throws Exception {
        try ([CloudTasksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.CloudTasksClient.html) client = [CloudTasksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.CloudTasksClient.html).create()) {
          // TODO(developer): Uncomment these lines and replace with your values.
          // String projectId = "your-project-id";
          // String locationId = "us-central1";
          // String queueBlueName = "queue-blue";
          // String queueRedName = "queue-red";
    
          [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.LocationName.html) parent = [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.LocationName.html).of(projectId, locationId);
    
          [Queue](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Queue.html) queueBlue =
              [Queue](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Queue.html).newBuilder()
                  .setName([QueueName](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.QueueName.html).of(projectId, locationId, queueBlueName).toString())
                  .[setRateLimits](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Queue.Builder.html#com_google_cloud_tasks_v2_Queue_Builder_setRateLimits_com_google_cloud_tasks_v2_RateLimits_)([RateLimits](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.RateLimits.html).newBuilder().[setMaxDispatchesPerSecond](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.RateLimits.Builder.html#com_google_cloud_tasks_v2_RateLimits_Builder_setMaxDispatchesPerSecond_double_)(5.0))
                  .[setAppEngineRoutingOverride](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Queue.Builder.html#com_google_cloud_tasks_v2_Queue_Builder_setAppEngineRoutingOverride_com_google_cloud_tasks_v2_AppEngineRouting_)(
                      [AppEngineRouting](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.AppEngineRouting.html).newBuilder().[setVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.AppEngineRouting.Builder.html#com_google_cloud_tasks_v2_AppEngineRouting_Builder_setVersion_java_lang_String_)("v2").[setService](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.AppEngineRouting.Builder.html#com_google_cloud_tasks_v2_AppEngineRouting_Builder_setService_java_lang_String_)("task-module"))
                  .build();
    
          [Queue](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Queue.html) queueRed =
              [Queue](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Queue.html).newBuilder()
                  .setName([QueueName](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.QueueName.html).of(projectId, locationId, queueRedName).toString())
                  .[setRateLimits](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Queue.Builder.html#com_google_cloud_tasks_v2_Queue_Builder_setRateLimits_com_google_cloud_tasks_v2_RateLimits_)([RateLimits](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.RateLimits.html).newBuilder().[setMaxDispatchesPerSecond](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.RateLimits.Builder.html#com_google_cloud_tasks_v2_RateLimits_Builder_setMaxDispatchesPerSecond_double_)(1.0))
                  .build();
    
          [Queue](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Queue.html)[] queues = new [Queue](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Queue.html)[] {queueBlue, queueRed};
          for ([Queue](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Queue.html) queue : queues) {
            [Queue](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Queue.html) response = client.createQueue(parent, queue);
            System.out.println(response);
          }
        }
      }
    }

To learn more, read the Cloud Tasks reference [Creating a Cloud Tasks queue](https://docs.cloud.google.com/tasks/docs/creating-queues#creating_a_queue).

### Set the queue processing rate

The following table lists the fields that differ from Task Queues to Cloud Tasks.

Task Queues field | Cloud Tasks field | Description  
---|---|---  
`rate` | `max_dispatches_per_second` | The maximum rate at which tasks are dispatched from the queue  
`max_concurrent_requests` | `max_concurrent_dispatches` | The maximum number of concurrent tasks that can be dispatched from the queue  
`bucket_size` | `max_burst_size` |  Cloud Tasks calculates a get-only property `max_burst_size` that limits how fast tasks in the queue are processed based on the value of `max_dispatches_per_second`. This field allows the queue to have a high rate so that processing starts shortly after a task is enqueued, but still limits resource usage when many tasks are enqueued in a short period of time.  For App Engine queues that were created or updated using a `queue.xml/yaml` file, `max_burst_size` is initially equal to `bucket_size`. However, if the queue is later passed to an `update` command using any Cloud Tasks interface, `max_burst_size` will be reset based on the value of `max_dispatches_per_second`, regardless of whether `max_dispatches_per_second` is updated.   
`total_storage_limit` | Deprecated in Cloud Tasks | Cloud Tasks does not support setting a custom storage limit  
  
You can set the queue processing rate when you create the queue or update it afterwards. The following example uses Cloud Tasks to set the processing rate on a queue named `queue-blue` that has already been created. If `queue-blue` was created or configured using a `queue.yaml` file, the following example resets`max_burst_size` based on the `max_dispatches_per_second` value of `20`. This is the Cloud Tasks equivalent of [setting the queue processing rate](https://docs.cloud.google.com/appengine/docs/standard/services/taskqueue/push/creating-push-queues#defining_the_push_queue_processing_rate) in Task Queues.

### gcloud
    
    
    gcloud tasks queues update queue-blue \
        --max-dispatches-per-second=20 \
        --max-concurrent-dispatches=10

### client library
    
    
    import com.google.cloud.tasks.v2.[CloudTasksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.CloudTasksClient.html);
    import com.google.cloud.tasks.v2.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.LocationName.html);
    import com.google.cloud.tasks.v2.[Queue](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Queue.html);
    import com.google.cloud.tasks.v2.[QueueName](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.QueueName.html);
    import com.google.cloud.tasks.v2.[RateLimits](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.RateLimits.html);
    import com.google.cloud.tasks.v2.[UpdateQueueRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.UpdateQueueRequest.html);
    
    public class UpdateQueue {
      public static void updateQueue(String projectId, String locationId, String queueId)
          throws Exception {
        try ([CloudTasksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.CloudTasksClient.html) client = [CloudTasksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.CloudTasksClient.html).create()) {
          // TODO(developer): Uncomment these lines and replace with your values.
          // String projectId = "your-project-id";
          // String locationId = "us-central1";
          // String queueId = "queue-blue";
    
          [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.LocationName.html) parent = [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.LocationName.html).of(projectId, locationId);
    
          [Queue](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Queue.html) queueBlue =
              [Queue](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Queue.html).newBuilder()
                  .setName([QueueName](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.QueueName.html).of(projectId, locationId, queueId).toString())
                  .[setRateLimits](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Queue.Builder.html#com_google_cloud_tasks_v2_Queue_Builder_setRateLimits_com_google_cloud_tasks_v2_RateLimits_)(
                      [RateLimits](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.RateLimits.html).newBuilder()
                          .[setMaxDispatchesPerSecond](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.RateLimits.Builder.html#com_google_cloud_tasks_v2_RateLimits_Builder_setMaxDispatchesPerSecond_double_)(20.0)
                          .[setMaxConcurrentDispatches](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.RateLimits.Builder.html#com_google_cloud_tasks_v2_RateLimits_Builder_setMaxConcurrentDispatches_int_)(10))
                  .build();
    
          [UpdateQueueRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.UpdateQueueRequest.html) request = [UpdateQueueRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.UpdateQueueRequest.html).newBuilder().setQueue(queueBlue).build();
    
          [Queue](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Queue.html) response = client.updateQueue(request);
          System.out.println(response);
        }
      }
    }

To learn more, see [Define rate limits](https://docs.cloud.google.com/tasks/docs/configuring-queues#rate).

### Disable and resuming queues

Cloud Tasks uses the term _pause_ in the same way that Task Queues uses the term _disable_. Pausing a queue stops the tasks in the queue from executing until the queue is resumed. However, you can continue to add tasks to a queue that is paused. Cloud Tasks uses the term _resume_ in the same way as Task Queues does.

The following example pauses a queue with queue ID `queueName`. This is the Cloud Tasks equivalent of [disabling queues](https://docs.cloud.google.com/appengine/docs/standard/services/taskqueue/push/deleting-tasks-and-queues#disabling_queues) in Task Queues.

### gcloud
    
    
    gcloud tasks queues pause queueName

### client library
    
    
    import com.google.cloud.tasks.v2.[CloudTasksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.CloudTasksClient.html);
    import com.google.cloud.tasks.v2.[QueueName](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.QueueName.html);
    
    public class PauseQueue {
      public static void pauseQueue(String projectId, String locationId, String queueId)
          throws Exception {
        try ([CloudTasksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.CloudTasksClient.html) client = [CloudTasksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.CloudTasksClient.html).create()) {
          // TODO(developer): Uncomment these lines and replace with your values.
          // String projectId = "your-project-id";
          // String locationId = "us-central1";
          // String queueId = "foo";
    
          // Construct the fully qualified queue name.
          String queueName = [QueueName](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.QueueName.html).of(projectId, locationId, queueId).toString();
    
          client.pauseQueue(queueName);
          System.out.println("Queue Paused.");
        }
      }
    }

To learn more, read the Cloud Tasks reference [Pausing queues](https://docs.cloud.google.com/tasks/docs/deleting-appengine-queues-and-tasks#pause-queues).

### Delete queues

Once you delete a queue, you must wait 7 days before creating a queue with the same name. Consider purging all tasks from a queue and reconfiguring the queue if you cannot wait 7 days.

The following example deletes the queue with queue ID `foo`. This is the Cloud Tasks equivalent of [deleting queues](https://docs.cloud.google.com/appengine/docs/standard/services/taskqueue/push/deleting-tasks-and-queues#deleting_queues) in Task Queues.

### gcloud
    
    
    gcloud tasks queues delete foo

### client library
    
    
    import com.google.cloud.tasks.v2.[CloudTasksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.CloudTasksClient.html);
    import com.google.cloud.tasks.v2.[QueueName](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.QueueName.html);
    
    public class DeleteQueue {
      public static void deleteQueue(String projectId, String locationId, String queueId)
          throws Exception {
        try ([CloudTasksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.CloudTasksClient.html) client = [CloudTasksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.CloudTasksClient.html).create()) {
          // TODO(developer): Uncomment these lines and replace with your values.
          // String projectId = "your-project-id";
          // String locationId = "us-central1";
          // String queueId = "foo";
    
          // Construct the fully qualified queue name.
          String queueName = [QueueName](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.QueueName.html).of(projectId, locationId, queueId).toString();
    
          client.deleteQueue(queueName);
          System.out.println("Queue Deleted.");
        }
      }
    }

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
  
The following example creates a task that routes to the handler `/worker` on the default App Engine service. This is the Cloud Tasks equivalent to [creating tasks](https://docs.cloud.google.com/appengine/docs/standard/services/taskqueue/push/creating-push-tasks#creating_a_new_task) in Task Queues.

### gcloud
    
    
    gcloud tasks create-app-engine-task \
        --queue=default \
        --method=POST \
        --relative-uri=/worker?key=key

### client library
    
    
    import com.google.cloud.tasks.v2.[AppEngineHttpRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.AppEngineHttpRequest.html);
    import com.google.cloud.tasks.v2.[CloudTasksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.CloudTasksClient.html);
    import com.google.cloud.tasks.v2.[HttpMethod](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.HttpMethod.html);
    import com.google.cloud.tasks.v2.[QueueName](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.QueueName.html);
    import com.google.cloud.tasks.v2.[Task](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Task.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import java.nio.charset.Charset;
    
    public class CreateTask {
      public static void createTask(String projectId, String locationId, String queueId)
          throws Exception {
        try ([CloudTasksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.CloudTasksClient.html) client = [CloudTasksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.CloudTasksClient.html).create()) {
          // TODO(developer): Uncomment these lines and replace with your values.
          // String projectId = "your-project-id";
          // String locationId = "us-central1";
          // String queueId = "default";
          String key = "key";
    
          // Construct the fully qualified queue name.
          String queueName = [QueueName](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.QueueName.html).of(projectId, locationId, queueId).toString();
    
          // Construct the task body.
          [Task](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Task.html) taskParam =
              [Task](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Task.html).newBuilder()
                  .[setAppEngineHttpRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Task.Builder.html#com_google_cloud_tasks_v2_Task_Builder_setAppEngineHttpRequest_com_google_cloud_tasks_v2_AppEngineHttpRequest_)(
                      [AppEngineHttpRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.AppEngineHttpRequest.html).newBuilder()
                          .[setRelativeUri](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.AppEngineHttpRequest.Builder.html#com_google_cloud_tasks_v2_AppEngineHttpRequest_Builder_setRelativeUri_java_lang_String_)("/worker?key=" + key)
                          .setHttpMethod([HttpMethod](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.HttpMethod.html).GET)
                          .build())
                  .build();
    
          [Task](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Task.html) taskPayload =
              [Task](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Task.html).newBuilder()
                  .[setAppEngineHttpRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Task.Builder.html#com_google_cloud_tasks_v2_Task_Builder_setAppEngineHttpRequest_com_google_cloud_tasks_v2_AppEngineHttpRequest_)(
                      [AppEngineHttpRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.AppEngineHttpRequest.html).newBuilder()
                          .setBody([ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFrom](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFrom_byte___)(key, Charset.defaultCharset()))
                          .[setRelativeUri](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.AppEngineHttpRequest.Builder.html#com_google_cloud_tasks_v2_AppEngineHttpRequest_Builder_setRelativeUri_java_lang_String_)("/worker")
                          .setHttpMethod([HttpMethod](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.HttpMethod.html).POST)
                          .build())
                  .build();
    
          // Send create task request.
          [Task](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Task.html)[] tasks = new [Task](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Task.html)[] {taskParam, taskPayload};
          for ([Task](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Task.html) task : tasks) {
            [Task](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Task.html) response = client.createTask(queueName, task);
            System.out.println(response);
          }
        }
      }
    }

To learn more, read the Cloud Tasks reference [Creating App Engine tasks](https://docs.cloud.google.com/tasks/docs/creating-appengine-tasks).

### Specify the target service and routing

Specifying the App Engine target service, version, and instance for App Engine tasks is optional. By default, App Engine tasks are routed to the service, version, and instance that are the default at the time the task is attempted.

Set the task's `app_engine_routing` property during task creation to specify a different App Engine service, version, or instance for your task.

To route all tasks on a given queue to the same App Engine service, version, and instance, you can set the `app_engine_routing_override` property on the queue.

To learn more, read the Cloud Tasks reference [Configure routing](https://docs.cloud.google.com/tasks/docs/configuring-queues#routing).

### Pass data to the handler

As with Task Queues, you can pass data to the handler in two ways using Cloud Tasks. You can either pass data as query parameters in the relative URI, or you can pass data in the request body using the HTTP methods POST or PUT.

Cloud Tasks uses the term _body_ in the same way that Task Queues uses the term _payload_. In Cloud Tasks, the default body content type is octet-stream rather than plain text. You can set the body content type by specifying it in the header.

The following example passes a key to the handler `/worker` in two different ways. This is the Cloud Tasks equivalent of [passing data to the handler](https://docs.cloud.google.com/appengine/docs/standard/services/taskqueue/push/creating-push-tasks#passing_data) in Task Queues.

### gcloud
    
    
    gcloud tasks create-app-engine-task \
        --queue=default \
        --method=GET  \
        --relative-uri=/worker?key=blue \
        --routing=service:worker
    
    
    gcloud tasks create-app-engine-task \
        --queue=default \
        --method=POST \
        --relative-uri=/worker \
        --routing=service:worker \
        --body-content="{'key': 'blue'}"

### client library
    
    
    import com.google.cloud.tasks.v2.[AppEngineHttpRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.AppEngineHttpRequest.html);
    import com.google.cloud.tasks.v2.[CloudTasksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.CloudTasksClient.html);
    import com.google.cloud.tasks.v2.[HttpMethod](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.HttpMethod.html);
    import com.google.cloud.tasks.v2.[QueueName](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.QueueName.html);
    import com.google.cloud.tasks.v2.[Task](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Task.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import java.nio.charset.Charset;
    
    public class CreateTask {
      public static void createTask(String projectId, String locationId, String queueId)
          throws Exception {
        try ([CloudTasksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.CloudTasksClient.html) client = [CloudTasksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.CloudTasksClient.html).create()) {
          // TODO(developer): Uncomment these lines and replace with your values.
          // String projectId = "your-project-id";
          // String locationId = "us-central1";
          // String queueId = "default";
          String key = "key";
    
          // Construct the fully qualified queue name.
          String queueName = [QueueName](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.QueueName.html).of(projectId, locationId, queueId).toString();
    
          // Construct the task body.
          [Task](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Task.html) taskParam =
              [Task](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Task.html).newBuilder()
                  .[setAppEngineHttpRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Task.Builder.html#com_google_cloud_tasks_v2_Task_Builder_setAppEngineHttpRequest_com_google_cloud_tasks_v2_AppEngineHttpRequest_)(
                      [AppEngineHttpRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.AppEngineHttpRequest.html).newBuilder()
                          .[setRelativeUri](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.AppEngineHttpRequest.Builder.html#com_google_cloud_tasks_v2_AppEngineHttpRequest_Builder_setRelativeUri_java_lang_String_)("/worker?key=" + key)
                          .setHttpMethod([HttpMethod](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.HttpMethod.html).GET)
                          .build())
                  .build();
    
          [Task](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Task.html) taskPayload =
              [Task](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Task.html).newBuilder()
                  .[setAppEngineHttpRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Task.Builder.html#com_google_cloud_tasks_v2_Task_Builder_setAppEngineHttpRequest_com_google_cloud_tasks_v2_AppEngineHttpRequest_)(
                      [AppEngineHttpRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.AppEngineHttpRequest.html).newBuilder()
                          .setBody([ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFrom](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFrom_byte___)(key, Charset.defaultCharset()))
                          .[setRelativeUri](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.AppEngineHttpRequest.Builder.html#com_google_cloud_tasks_v2_AppEngineHttpRequest_Builder_setRelativeUri_java_lang_String_)("/worker")
                          .setHttpMethod([HttpMethod](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.HttpMethod.html).POST)
                          .build())
                  .build();
    
          // Send create task request.
          [Task](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Task.html)[] tasks = new [Task](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Task.html)[] {taskParam, taskPayload};
          for ([Task](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Task.html) task : tasks) {
            [Task](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Task.html) response = client.createTask(queueName, task);
            System.out.println(response);
          }
        }
      }
    }

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
        --relative-uri=/worker

### client library

With the client library, you must specify the full task name if you want to specify the `TASK_ID`. The project and location must match the project and location of the queue to which the task is added.
    
    
    import com.google.cloud.tasks.v2.[AppEngineHttpRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.AppEngineHttpRequest.html);
    import com.google.cloud.tasks.v2.[CloudTasksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.CloudTasksClient.html);
    import com.google.cloud.tasks.v2.[HttpMethod](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.HttpMethod.html);
    import com.google.cloud.tasks.v2.[QueueName](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.QueueName.html);
    import com.google.cloud.tasks.v2.[Task](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Task.html);
    import com.google.cloud.tasks.v2.[TaskName](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.TaskName.html);
    
    public class CreateTaskWithName {
      public static void createTaskWithName(
          String projectId, String locationId, String queueId, String taskId) throws Exception {
        try ([CloudTasksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.CloudTasksClient.html) client = [CloudTasksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.CloudTasksClient.html).create()) {
          // TODO(developer): Uncomment these lines and replace with your values.
          // String projectId = "your-project-id";
          // String locationId = "us-central1";
          // String queueId = "default";
          // String taskId = "first-try"
    
          String queueName = [QueueName](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.QueueName.html).of(projectId, locationId, queueId).toString();
    
          [Task](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Task.html).Builder taskBuilder =
              [Task](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Task.html).newBuilder()
                  .setName([TaskName](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.TaskName.html).of(projectId, locationId, queueId, taskId).toString())
                  .[setAppEngineHttpRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Task.Builder.html#com_google_cloud_tasks_v2_Task_Builder_setAppEngineHttpRequest_com_google_cloud_tasks_v2_AppEngineHttpRequest_)(
                      [AppEngineHttpRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.AppEngineHttpRequest.html).newBuilder()
                          .[setRelativeUri](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.AppEngineHttpRequest.Builder.html#com_google_cloud_tasks_v2_AppEngineHttpRequest_Builder_setRelativeUri_java_lang_String_)("/worker")
                          .setHttpMethod([HttpMethod](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.HttpMethod.html).GET)
                          .build());
    
          // Send create task request.
          [Task](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Task.html) response = client.createTask(queueName, taskBuilder.build());
          System.out.println(response);
        }
      }
    }

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
    
    
    import com.google.cloud.tasks.v2.[CloudTasksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.CloudTasksClient.html);
    import com.google.cloud.tasks.v2.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.LocationName.html);
    import com.google.cloud.tasks.v2.[Queue](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Queue.html);
    import com.google.cloud.tasks.v2.[QueueName](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.QueueName.html);
    import com.google.cloud.tasks.v2.[RateLimits](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.RateLimits.html);
    import com.google.cloud.tasks.v2.[RetryConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.RetryConfig.html);
    import com.google.protobuf.[Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html);
    
    public class RetryTask {
      public static void retryTask(
          String projectId, String locationId, String fooqueue, String barqueue, String bazqueue)
          throws Exception {
        try ([CloudTasksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.CloudTasksClient.html) client = [CloudTasksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.CloudTasksClient.html).create()) {
          // TODO(developer): Uncomment these lines and replace with your values.
          // String projectId = "your-project-id";
          // String locationId = "us-central1";
          // String fooqueue = "fooqueue";
          // String barqueue = "barqueue";
          // String bazqueue = "bazqueue";
    
          [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.LocationName.html) parent = [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.LocationName.html).of(projectId, locationId);
    
          [Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html) retryDuration = [Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html).newBuilder().setSeconds(2 * 60 * 60 * 24).build();
          [Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html) min = [Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html).newBuilder().setSeconds(10).build();
          [Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html) max1 = [Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html).newBuilder().setSeconds(200).build();
          [Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html) max2 = [Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html).newBuilder().setSeconds(300).build();
    
          [Queue](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Queue.html) foo =
              [Queue](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Queue.html).newBuilder()
                  .setName([QueueName](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.QueueName.html).of(projectId, locationId, fooqueue).toString())
                  .[setRateLimits](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Queue.Builder.html#com_google_cloud_tasks_v2_Queue_Builder_setRateLimits_com_google_cloud_tasks_v2_RateLimits_)([RateLimits](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.RateLimits.html).newBuilder().[setMaxDispatchesPerSecond](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.RateLimits.Builder.html#com_google_cloud_tasks_v2_RateLimits_Builder_setMaxDispatchesPerSecond_double_)(1.0))
                  .setRetryConfig(
                      [RetryConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.RetryConfig.html).newBuilder().[setMaxAttempts](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.RetryConfig.Builder.html#com_google_cloud_tasks_v2_RetryConfig_Builder_setMaxAttempts_int_)(7).[setMaxRetryDuration](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.RetryConfig.Builder.html#com_google_cloud_tasks_v2_RetryConfig_Builder_setMaxRetryDuration_com_google_protobuf_Duration_)(retryDuration))
                  .build();
    
          [Queue](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Queue.html) bar =
              [Queue](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Queue.html).newBuilder()
                  .setName([QueueName](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.QueueName.html).of(projectId, locationId, barqueue).toString())
                  .[setRateLimits](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Queue.Builder.html#com_google_cloud_tasks_v2_Queue_Builder_setRateLimits_com_google_cloud_tasks_v2_RateLimits_)([RateLimits](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.RateLimits.html).newBuilder().[setMaxDispatchesPerSecond](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.RateLimits.Builder.html#com_google_cloud_tasks_v2_RateLimits_Builder_setMaxDispatchesPerSecond_double_)(1.0))
                  .setRetryConfig(
                      [RetryConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.RetryConfig.html).newBuilder()
                          .[setMinBackoff](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.RetryConfig.Builder.html#com_google_cloud_tasks_v2_RetryConfig_Builder_setMinBackoff_com_google_protobuf_Duration_)(min)
                          .[setMaxBackoff](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.RetryConfig.Builder.html#com_google_cloud_tasks_v2_RetryConfig_Builder_setMaxBackoff_com_google_protobuf_Duration_)(max1)
                          .[setMaxDoublings](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.RetryConfig.Builder.html#com_google_cloud_tasks_v2_RetryConfig_Builder_setMaxDoublings_int_)(0))
                  .build();
    
          [Queue](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Queue.html) baz =
              [Queue](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Queue.html).newBuilder()
                  .setName([QueueName](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.QueueName.html).of(projectId, locationId, bazqueue).toString())
                  .[setRateLimits](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Queue.Builder.html#com_google_cloud_tasks_v2_Queue_Builder_setRateLimits_com_google_cloud_tasks_v2_RateLimits_)([RateLimits](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.RateLimits.html).newBuilder().[setMaxDispatchesPerSecond](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.RateLimits.Builder.html#com_google_cloud_tasks_v2_RateLimits_Builder_setMaxDispatchesPerSecond_double_)(1.0))
                  .setRetryConfig(
                      [RetryConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.RetryConfig.html).newBuilder()
                          .[setMinBackoff](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.RetryConfig.Builder.html#com_google_cloud_tasks_v2_RetryConfig_Builder_setMinBackoff_com_google_protobuf_Duration_)(min)
                          .[setMaxBackoff](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.RetryConfig.Builder.html#com_google_cloud_tasks_v2_RetryConfig_Builder_setMaxBackoff_com_google_protobuf_Duration_)(max2)
                          .[setMaxDoublings](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.RetryConfig.Builder.html#com_google_cloud_tasks_v2_RetryConfig_Builder_setMaxDoublings_int_)(3))
                  .build();
    
          [Queue](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Queue.html)[] queues = new [Queue](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Queue.html)[] {foo, bar, baz};
          for ([Queue](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Queue.html) queue : queues) {
            [Queue](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Queue.html) response = client.createQueue(parent, queue);
            System.out.println(response);
          }
        }
      }
    }

To learn more, read the Cloud Tasks reference [Set retry parameters](https://docs.cloud.google.com/tasks/docs/configuring-queues#retry).

### Delete tasks from a queue

When you delete a task, you must wait 9 days before creating a task with the same name if the task was on a queue created using a `queue.yaml` file, or 1 hour if the task was on a queue created using Cloud Tasks.

The following example deletes the task with task ID `foo` from the queue with queue ID `queue1`. This is the Cloud Tasks equivalent of [deleting tasks](https://docs.cloud.google.com/appengine/docs/standard/services/taskqueue/push/deleting-tasks-and-queues#deleting_tasks_from_a_queue) in Task Queues.

### gcloud

The task project and location are inferred from the gcloud CLI default project.
    
    
    gcloud tasks delete foo --queue=queue1

### client library
    
    
    import com.google.cloud.tasks.v2.[CloudTasksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.CloudTasksClient.html);
    import com.google.cloud.tasks.v2.[TaskName](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.TaskName.html);
    
    public class DeleteTask {
      public static void deleteTask(String projectId, String locationId, String queueId, String taskId)
          throws Exception {
        try ([CloudTasksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.CloudTasksClient.html) client = [CloudTasksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.CloudTasksClient.html).create()) {
          // TODO(developer): Uncomment these lines and replace with your values.
          // String projectId = "your-project-id";
          // String locationId = "us-central1";
          // String queueId = "queue1";
          // String taskId = "foo";
    
          // Construct the fully qualified queue name.
          String taskName = [TaskName](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.TaskName.html).of(projectId, locationId, queueId, taskId).toString();
    
          client.deleteTask(taskName);
          System.out.println("Task Deleted.");
        }
      }
    }

To learn more, read the Cloud Tasks reference [Deleting a task from a queue](https://docs.cloud.google.com/tasks/docs/deleting-appengine-queues-and-tasks#delete-task).

### Purge tasks

The following example purges all tasks from the queue with queue ID `foo`. This is the Cloud Tasks equivalent of [purging tasks](https://docs.cloud.google.com/appengine/docs/standard/services/taskqueue/push/deleting-tasks-and-queues#purging_all_tasks_from_a_queue) in Task Queues.

### gcloud

The queue project and location are inferred from the gcloud CLI default project.
    
    
    gcloud tasks queues purge foo

### client library
    
    
    import com.google.cloud.tasks.v2.[CloudTasksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.CloudTasksClient.html);
    import com.google.cloud.tasks.v2.[QueueName](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.QueueName.html);
    
    public class PurgeQueue {
      public static void purgeQueue(String projectId, String locationId, String queueId)
          throws Exception {
        try ([CloudTasksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.CloudTasksClient.html) client = [CloudTasksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.CloudTasksClient.html).create()) {
          // TODO(developer): Uncomment these lines and replace with your values.
          // String projectId = "your-project-id";
          // String locationId = "us-central1";
          // String queueId = "foo";
    
          // Construct the fully qualified queue name.
          String queueName = [QueueName](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.QueueName.html).of(projectId, locationId, queueId).toString();
    
          client.purgeQueue(queueName);
          System.out.println("Queue Purged.");
        }
      }
    }

To learn more, read the Cloud Tasks reference [Purging all tasks from a queue](https://docs.cloud.google.com/tasks/docs/deleting-appengine-queues-and-tasks#purge-tasks).

## Java 8 Cloud Tasks example

The following example is a basic setup for creating a queue and enqueueing a task to it with Cloud Tasks. It assumes that the developer has created a `pom.xml` file to specify the Cloud Tasks dependency as described in the section Importing the client library. This is the Cloud Tasks equivalent of a Java 8 task queue example in Task Queues.

The file that is responsible for creating and enqueueing the task creates a task and adds it to the default queue using the Cloud Tasks client library:
    
    
    import com.google.cloud.tasks.v2.[AppEngineHttpRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.AppEngineHttpRequest.html);
    import com.google.cloud.tasks.v2.[CloudTasksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.CloudTasksClient.html);
    import com.google.cloud.tasks.v2.[HttpMethod](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.HttpMethod.html);
    import com.google.cloud.tasks.v2.[QueueName](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.QueueName.html);
    import com.google.cloud.tasks.v2.[Task](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Task.html);
    import java.io.IOException;
    import javax.servlet.ServletException;
    import javax.servlet.annotation.WebServlet;
    import javax.servlet.http.HttpServlet;
    import javax.servlet.http.HttpServletRequest;
    import javax.servlet.http.HttpServletResponse;
    
    @WebServlet(
        name = "TaskEnqueue",
        description = "Enqueue a task targeted at endpoint '/cloudtasks/worker'",
        urlPatterns = "/cloudtasks/enqueue")
    public class Enqueue extends HttpServlet {
    
      // TODO(developer): Replace these variables before running the sample.
      static final String projectId = "my-project-id";
      static final String locationId = "us-central1";
    
      // Function creates Cloud Tasks from form submissions.
      protected void doPost(HttpServletRequest request, HttpServletResponse response)
          throws ServletException, IOException {
        String key = request.getParameter("key");
    
        try ([CloudTasksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.CloudTasksClient.html) client = [CloudTasksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.CloudTasksClient.html).create()) {
          // Construct the fully qualified queue name.
          String queueName = [QueueName](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.QueueName.html).of(projectId, locationId, "default").toString();
    
          // Construct the task body.
          [Task](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Task.html) task =
              [Task](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Task.html).newBuilder()
                  .[setAppEngineHttpRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Task.Builder.html#com_google_cloud_tasks_v2_Task_Builder_setAppEngineHttpRequest_com_google_cloud_tasks_v2_AppEngineHttpRequest_)(
                      [AppEngineHttpRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.AppEngineHttpRequest.html).newBuilder()
                          .[setRelativeUri](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.AppEngineHttpRequest.Builder.html#com_google_cloud_tasks_v2_AppEngineHttpRequest_Builder_setRelativeUri_java_lang_String_)("/cloudtasks/worker?key=" + key)
                          .setHttpMethod([HttpMethod](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.HttpMethod.html).POST)
                          .build())
                  .build();
    
          // Add the task to the default queue.
          [Task](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Task.html) taskResponse = client.createTask(queueName, task);
          System.out.println("Task created: " + taskResponse.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Task.html#com_google_cloud_tasks_v2_Task_getName__)());
        }
    
        response.sendRedirect("/");
      }
    }

The file that defines the worker handles the task:
    
    
    import java.io.IOException;
    import java.util.logging.Logger;
    import javax.servlet.ServletException;
    import javax.servlet.annotation.WebServlet;
    import javax.servlet.http.HttpServlet;
    import javax.servlet.http.HttpServletRequest;
    import javax.servlet.http.HttpServletResponse;
    
    @WebServlet(
        name = "TaskWorker",
        description = "Endpoint to process Cloud Task requests",
        urlPatterns = "/cloudtasks/worker"
    )
    public class Worker extends HttpServlet {
    
      private static final Logger log = Logger.getLogger(Worker.class.getName());
    
      // Worker function to process POST requests from Cloud Tasks targeted at the
      // '/cloudtasks/worker' endpoint.
      protected void doPost(HttpServletRequest request, HttpServletResponse response)
          throws ServletException, IOException {
        String key = request.getParameter("key");
        log.info("Worker is processing " + key);
      }
    }

## What's next

  * [Cloud Tasks documentation](https://docs.cloud.google.com/tasks/docs)
  * [Cloud Tasks client library](https://docs.cloud.google.com/tasks/docs/reference/libraries)
  * [Cloud Tasks REST reference](https://docs.cloud.google.com/tasks/docs/reference/rest) overview
  * [Cloud Tasks RPC reference](https://docs.cloud.google.com/tasks/docs/reference/rpc) overview 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
