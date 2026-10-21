---
url: https://docs.cloud.google.com/tasks/docs/samples/cloud-tasks-taskqueues-using-yaml/
title: Create a queue when migrating App Engine push queues \u00a0|\u00a0 Cloud Tasks \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:25.912850+00:00
---

# Create a queue when migrating App Engine push queues  |  Cloud Tasks  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tasks/docs/samples/cloud-tasks-taskqueues-using-yaml/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Tasks ](https://docs.cloud.google.com/tasks/docs)
  * [ Samples ](https://docs.cloud.google.com/tasks/docs/samples)



#  Create a queue when migrating App Engine push queues Stay organized with collections  Save and categorize content based on your preferences. 

Creates a queue when migrating App Engine push queue code from task queues to Cloud Tasks.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Migrate push queues to Cloud Tasks (Java)](https://docs.cloud.google.com/appengine/migration-center/standard/java/migrating-push-queues)
  * [Migrate push queues to Cloud Tasks (Python)](https://docs.cloud.google.com/appengine/migration-center/standard/python/migrating-push-queues)



## Code sample

### Java

To learn how to install and use the client library for Cloud Tasks, see [Cloud Tasks client libraries](https://docs.cloud.google.com/tasks/docs/reference/libraries). For more information, see the [Cloud Tasks Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/overview). 

To authenticate to Cloud Tasks, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

### Python

To learn how to install and use the client library for Cloud Tasks, see [Cloud Tasks client libraries](https://docs.cloud.google.com/tasks/docs/reference/libraries). For more information, see the [Cloud Tasks Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest). 

To authenticate to Cloud Tasks, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudtasks). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
