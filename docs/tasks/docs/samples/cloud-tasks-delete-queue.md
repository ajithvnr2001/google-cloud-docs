---
url: https://docs.cloud.google.com/tasks/docs/samples/cloud-tasks-delete-queue/
title: Delete a queue \u00a0|\u00a0 Cloud Tasks \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:43.857827+00:00
---

# Delete a queue  |  Cloud Tasks  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tasks/docs/samples/cloud-tasks-delete-queue/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Tasks ](https://docs.cloud.google.com/tasks/docs)
  * [ Samples ](https://docs.cloud.google.com/tasks/docs/samples)



#  Delete a queue Stay organized with collections  Save and categorize content based on your preferences. 

Deletes a queue.

## Code sample

### Java

To learn how to install and use the client library for Cloud Tasks, see [Cloud Tasks client libraries](https://docs.cloud.google.com/tasks/docs/reference/libraries). For more information, see the [Cloud Tasks Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/overview). 

To authenticate to Cloud Tasks, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.tasks.v2.[CloudTasksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.CloudTasksClient.html);
    import com.google.cloud.tasks.v2.[QueueName](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.QueueName.html);
    import java.io.IOException;
    
    public class DeleteQueue {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project-id";
        String locationId = "us-central1";
        String queueId = "my-queue";
        deleteQueue(projectId, locationId, queueId);
      }
    
      // Delete a queue using the Cloud Tasks client.
      public static void deleteQueue(String projectId, String locationId, String queueId)
          throws IOException {
    
        // Instantiates a client.
        try ([CloudTasksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.CloudTasksClient.html) client = [CloudTasksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.CloudTasksClient.html).create()) {
    
          // Construct the fully qualified queue path.
          String queuePath = [QueueName](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.QueueName.html).of(projectId, locationId, queueId).toString();
    
          // Send delete queue request.
          client.deleteQueue(queuePath);
    
          System.out.println("Queue deleted: " + queueId);
        }
      }
    }

### Node.js

To learn how to install and use the client library for Cloud Tasks, see [Cloud Tasks client libraries](https://docs.cloud.google.com/tasks/docs/reference/libraries). For more information, see the [Cloud Tasks Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/tasks/latest). 

To authenticate to Cloud Tasks, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud Tasks library.
    const cloudTasks = require('[@google-cloud/tasks](https://docs.cloud.google.com/nodejs/docs/reference/tasks/latest/overview.html)');
    
    // Instantiates a client.
    const client = new cloudTasks.[CloudTasksClient](https://docs.cloud.google.com/nodejs/docs/reference/tasks/latest/overview.html)();
    
    async function deleteQueue() {
      // Get the fully qualified path to the queue
      const name = client.queuePath(project, location, queue);
    
      // Send delete queue request.
      await client.deleteQueue({name});
      console.log(`Deleted queue '${queue}'.`);
    }
    deleteQueue();

### Python

To learn how to install and use the client library for Cloud Tasks, see [Cloud Tasks client libraries](https://docs.cloud.google.com/tasks/docs/reference/libraries). For more information, see the [Cloud Tasks Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest). 

To authenticate to Cloud Tasks, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import [tasks_v2](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest)
    
    
    def delete_queue(project: str, location: str, queue_id: str) -> None:
        """Delete a queue.
        Args:
            project: The project ID where the queue is located.
            location: The location ID where the queue is located.
            queue_id: The ID of the queue to delete.
        """
    
        # Create a client.
        client = [tasks_v2](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest).[CloudTasksClient](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2.services.cloud_tasks.CloudTasksClient.html)()
    
        # Use the client to send a DeleteQueueRequest.
        client.[delete_queue](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2.services.cloud_tasks.CloudTasksClient.html#google_cloud_tasks_v2_services_cloud_tasks_CloudTasksClient_delete_queue)(
            [tasks_v2](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest).[DeleteQueueRequest](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2.types.DeleteQueueRequest.html)(name=client.[queue_path](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2.services.cloud_tasks.CloudTasksClient.html#google_cloud_tasks_v2_services_cloud_tasks_CloudTasksClient_queue_path)(project, location, queue_id))
        )
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudtasks). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
