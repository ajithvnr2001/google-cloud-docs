---
url: https://docs.cloud.google.com/tasks/docs/samples/cloud-tasks-list-queues/
title: List queues \u00a0|\u00a0 Cloud Tasks \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:58:44.761288+00:00
---

# List queues  |  Cloud Tasks  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tasks/docs/samples/cloud-tasks-list-queues/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Tasks ](https://docs.cloud.google.com/tasks/docs)
  * [ Samples ](https://docs.cloud.google.com/tasks/docs/samples)



#  List queues Stay organized with collections  Save and categorize content based on your preferences. 

Lists queues.

## Code sample

### Java

To learn how to install and use the client library for Cloud Tasks, see [Cloud Tasks client libraries](https://docs.cloud.google.com/tasks/docs/reference/libraries). For more information, see the [Cloud Tasks Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/overview). 

To authenticate to Cloud Tasks, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.tasks.v2.[CloudTasksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.CloudTasksClient.html);
    import com.google.cloud.tasks.v2.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.LocationName.html);
    import com.google.cloud.tasks.v2.[Queue](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Queue.html);
    import java.io.IOException;
    
    public class ListQueues {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project-id";
        String locationId = "us-central1";
        listQueues(projectId, locationId);
      }
    
      // List queues using the Cloud Tasks client.
      public static void listQueues(String projectId, String locationId) throws IOException {
    
        // Instantiates a client.
        try ([CloudTasksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.CloudTasksClient.html) client = [CloudTasksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.CloudTasksClient.html).create()) {
    
          // Construct the fully qualified location path.
          String parent = [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.LocationName.html).of(projectId, locationId).toString();
    
          // Send list queues request.
          [CloudTasksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.CloudTasksClient.html).[ListQueuesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.CloudTasksClient.ListQueuesPagedResponse.html) response = client.listQueues(parent);
    
          // Iterate over results and print queue names
          int total = 0;
          for ([Queue](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Queue.html) queue : response.iterateAll()) {
            System.out.println(queue.getName());
            total++;
          }
    
          if (total == 0) {
            System.out.println("No queues found!");
          }
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
    
    async function listQueues() {
      // Get the fully qualified path to the region
      const parent = client.locationPath(project, location);
    
      // list all fo the queues
      const [queues] = await client.listQueues({parent});
    
      if (queues.length > 0) {
        console.log('Queues:');
        queues.forEach(queue => {
          console.log(`  ${queue.name}`);
        });
      } else {
        console.log('No queues found!');
      }
    }
    listQueues();

### Python

To learn how to install and use the client library for Cloud Tasks, see [Cloud Tasks client libraries](https://docs.cloud.google.com/tasks/docs/reference/libraries). For more information, see the [Cloud Tasks Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest). 

To authenticate to Cloud Tasks, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from typing import List
    
    from google.cloud import tasks_v2
    
    
    def list_queues(project: str, location: str) -> List[str]:
        """List all queues
        Args:
            project: The project ID to list queues from.
            location: The location ID to list queues from.
    
        Returns:
            A list of queue names.
        """
    
        # Create a client.
        client = tasks_v2.CloudTasksClient()
    
        # Use the client to send a ListQueuesRequest.
        response = client.list_queues(
            tasks_v2.ListQueuesRequest(
                parent=client.common_location_path(project, location)
            )
        )
    
        # Return the results.
        return [queue.name for queue in response]
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudtasks). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
