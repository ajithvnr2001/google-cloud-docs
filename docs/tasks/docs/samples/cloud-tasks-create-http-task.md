---
url: https://docs.cloud.google.com/tasks/docs/samples/cloud-tasks-create-http-task/
title: Create HTTP tasks \u00a0|\u00a0 Cloud Tasks \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:36:43.934150+00:00
---

# Create HTTP tasks  |  Cloud Tasks  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tasks/docs/samples/cloud-tasks-create-http-task/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Tasks ](https://docs.cloud.google.com/tasks/docs)
  * [ Samples ](https://docs.cloud.google.com/tasks/docs/samples)



#  Create HTTP tasks Stay organized with collections  Save and categorize content based on your preferences. 

Creates tasks to send to a Cloud Run, Cloud Function, or external URL.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create HTTP target tasks programmatically](https://docs.cloud.google.com/tasks/docs/creating-http-target-tasks)



## Code sample

### C#

To learn how to install and use the client library for Cloud Tasks, see [Cloud Tasks client libraries](https://docs.cloud.google.com/tasks/docs/reference/libraries). For more information, see the [Cloud Tasks C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest). 

To authenticate to Cloud Tasks, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Tasks.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.html);
    using [Google.Protobuf](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.html);
    using [Google.Protobuf.WellKnownTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.html);
    using System;
    
    class CreateHttpTask
    {
        public string CreateTask(
            string projectId = "YOUR-PROJECT-ID",
            string location = "us-central1",
            string queue = "my-queue",
            string url = "http://example.com/taskhandler",
            string payload = "Hello World!",
            int inSeconds = 0)
        {
            [CloudTasksClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient.html) client = [CloudTasksClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient.html#Google_Cloud_Tasks_V2_CloudTasksClient_Create)();
            [QueueName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.QueueName.html) parent = new [QueueName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.QueueName.html)(projectId, location, queue);
    
            var response = client.[CreateTask](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient.html#Google_Cloud_Tasks_V2_CloudTasksClient_CreateTask_Google_Cloud_Tasks_V2_CreateTaskRequest_Google_Api_Gax_Grpc_CallSettings_)(new [CreateTaskRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CreateTaskRequest.html)
            {
                Parent = parent.[ToString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.QueueName.html#Google_Cloud_Tasks_V2_QueueName_ToString)(),
                Task = new [Task](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CreateTaskRequest.html#Google_Cloud_Tasks_V2_CreateTaskRequest_Task)
                {
                    HttpRequest = new [HttpRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.HttpRequest.html)
                    {
                        HttpMethod = [HttpMethod](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.HttpMethod.html).[Post](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.HttpMethod.html#Google_Cloud_Tasks_V2_HttpMethod_Post),
                        Url = url,
                        Body = [ByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html).[CopyFromUtf8](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html#Google_Protobuf_ByteString_CopyFromUtf8_System_String_)(payload)
                    },
                    ScheduleTime = [Timestamp](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html).[FromDateTime](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html#Google_Protobuf_WellKnownTypes_Timestamp_FromDateTime_System_DateTime_)(
                        DateTime.UtcNow.AddSeconds(inSeconds))
                }
            });
    
            Console.WriteLine($"Created Task {response.Name}");
            return response.Name;
        }
    }

### Go

To learn how to install and use the client library for Cloud Tasks, see [Cloud Tasks client libraries](https://docs.cloud.google.com/tasks/docs/reference/libraries). For more information, see the [Cloud Tasks Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudtasks/latest/apiv2). 

To authenticate to Cloud Tasks, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Command createHTTPtask constructs and adds a task to a Cloud Tasks Queue.
    package main
    
    import (
    	"context"
    	"fmt"
    
    	cloudtasks "cloud.google.com/go/cloudtasks/apiv2"
    	taskspb "cloud.google.com/go/cloudtasks/apiv2/cloudtaskspb"
    )
    
    // createHTTPTask creates a new task with a HTTP target then adds it to a Queue.
    func createHTTPTask(projectID, locationID, queueID, url, message string) (*taskspb.Task, error) {
    
    	// Create a new Cloud Tasks client instance.
    	// See https://godoc.org/cloud.google.com/go/cloudtasks/apiv2
    	ctx := context.Background()
    	client, err := cloudtasks.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudtasks/latest/apiv2.html#cloud_google_com_go_cloudtasks_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		return nil, fmt.Errorf("NewClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudtasks/latest/apiv2.html#cloud_google_com_go_cloudtasks_apiv2_Client_Close)()
    
    	// Build the Task queue path.
    	queuePath := fmt.Sprintf("projects/%s/locations/%s/queues/%s", projectID, locationID, queueID)
    
    	// Build the Task payload.
    	// https://godoc.org/google.golang.org/genproto/googleapis/cloud/tasks/v2#CreateTaskRequest
    	req := &taskspb.CreateTaskRequest{
    		Parent: queuePath,
    		Task: &taskspb.Task{
    			// https://godoc.org/google.golang.org/genproto/googleapis/cloud/tasks/v2#HttpRequest
    			MessageType: &taskspb.Task_HttpRequest{
    				HttpRequest: &taskspb.HttpRequest{
    					HttpMethod: taskspb.HttpMethod_POST,
    					Url:        url,
    				},
    			},
    		},
    	}
    
    	// Add a payload message if one is present.
    	req.Task.GetHttpRequest().Body = []byte(message)
    
    	createdTask, err := client.CreateTask(ctx, req)
    	if err != nil {
    		return nil, fmt.Errorf("cloudtasks.CreateTask: %w", err)
    	}
    
    	return createdTask, nil
    }
    

### Java

To learn how to install and use the client library for Cloud Tasks, see [Cloud Tasks client libraries](https://docs.cloud.google.com/tasks/docs/reference/libraries). For more information, see the [Cloud Tasks Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/overview). 

To authenticate to Cloud Tasks, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.tasks.v2.[CloudTasksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.CloudTasksClient.html);
    import com.google.cloud.tasks.v2.[HttpMethod](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.HttpMethod.html);
    import com.google.cloud.tasks.v2.[HttpRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.HttpRequest.html);
    import com.google.cloud.tasks.v2.[QueueName](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.QueueName.html);
    import com.google.cloud.tasks.v2.[Task](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Task.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import java.io.IOException;
    import java.nio.charset.Charset;
    
    public class CreateHttpTask {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project-id";
        String locationId = "us-central1";
        String queueId = "my-queue";
        createTask(projectId, locationId, queueId);
      }
    
      // Create a task with a HTTP target using the Cloud Tasks client.
      public static void createTask(String projectId, String locationId, String queueId)
          throws IOException {
    
        // Instantiates a client.
        try ([CloudTasksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.CloudTasksClient.html) client = [CloudTasksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.CloudTasksClient.html).create()) {
          String url = "https://example.com/taskhandler";
          String payload = "Hello, World!";
    
          // Construct the fully qualified queue name.
          String queuePath = [QueueName](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.QueueName.html).of(projectId, locationId, queueId).toString();
    
          // Construct the task body.
          [Task](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Task.html).Builder taskBuilder =
              [Task](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Task.html).newBuilder()
                  .[setHttpRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Task.Builder.html#com_google_cloud_tasks_v2_Task_Builder_setHttpRequest_com_google_cloud_tasks_v2_HttpRequest_)(
                      [HttpRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.HttpRequest.html).newBuilder()
                          .setBody([ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFrom](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFrom_byte___)(payload, Charset.defaultCharset()))
                          .[setUrl](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.HttpRequest.Builder.html#com_google_cloud_tasks_v2_HttpRequest_Builder_setUrl_java_lang_String_)(url)
                          .setHttpMethod([HttpMethod](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.HttpMethod.html).POST)
                          .build());
    
          // Send create task request.
          [Task](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Task.html) task = client.createTask(queuePath, taskBuilder.build());
          System.out.println("Task created: " + task.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Task.html#com_google_cloud_tasks_v2_Task_getName__)());
        }
      }
    }

### Node.js

To learn how to install and use the client library for Cloud Tasks, see [Cloud Tasks client libraries](https://docs.cloud.google.com/tasks/docs/reference/libraries). For more information, see the [Cloud Tasks Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/tasks/latest). 

To authenticate to Cloud Tasks, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud Tasks library.
    const {CloudTasksClient} = require('[@google-cloud/tasks](https://docs.cloud.google.com/nodejs/docs/reference/tasks/latest/overview.html)');
    
    // Instantiates a client.
    const client = new [CloudTasksClient](https://docs.cloud.google.com/nodejs/docs/reference/tasks/latest/overview.html)();
    
    async function createHttpTask() {
      // TODO(developer): Uncomment these lines and replace with your values.
      // const project = 'my-project-id';
      // const queue = 'my-queue';
      // const location = 'us-central1';
      // const url = 'https://example.com/taskhandler';
      // const payload = 'Hello, World!';
      // const inSeconds = 180;
    
      // Construct the fully qualified queue name.
      const parent = client.queuePath(project, location, queue);
    
      const task = {
        httpRequest: {
          headers: {
            'Content-Type': 'text/plain', // Set content type to ensure compatibility your application's request parsing
          },
          httpMethod: 'POST',
          url,
        },
      };
    
      if (payload) {
        task.httpRequest.body = Buffer.from(payload).toString('base64');
      }
    
      if (inSeconds) {
        // The time when the task is scheduled to be attempted.
        task.scheduleTime = {
          seconds: parseInt(inSeconds) + Date.now() / 1000,
        };
      }
    
      // Send create task request.
      console.log('Sending task:');
      console.log(task);
      const request = {parent: parent, task: task};
      const [response] = await client.createTask(request);
      console.log(`Created task ${response.name}`);
    }
    createHttpTask();

### PHP

To learn how to install and use the client library for Cloud Tasks, see [Cloud Tasks client libraries](https://docs.cloud.google.com/tasks/docs/reference/libraries). For more information, see the [Cloud Tasks PHP API reference documentation](https://docs.cloud.google.com/php/docs/reference/cloud-tasks/latest). 

To authenticate to Cloud Tasks, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Tasks\V2\Client\CloudTasksClient;
    use Google\Cloud\Tasks\V2\CreateTaskRequest;
    use Google\Cloud\Tasks\V2\HttpMethod;
    use Google\Cloud\Tasks\V2\HttpRequest;
    use Google\Cloud\Tasks\V2\Task;
    
    /** Uncomment and populate these variables in your code */
    // $projectId = 'The Google project ID';
    // $locationId = 'The Location ID';
    // $queueId = 'The Cloud Tasks Queue ID';
    // $url = 'The full url path that the task request will be sent to.'
    // $payload = 'The payload your task should carry to the task handler. Optional';
    
    // Instantiate the client and queue name.
    $client = new CloudTasksClient();
    $queueName = $client->queueName($projectId, $locationId, $queueId);
    
    // Create an Http Request Object.
    $httpRequest = new HttpRequest();
    // The full url path that the task request will be sent to.
    $httpRequest->setUrl($url);
    // POST is the default HTTP method, but any HTTP method can be used.
    $httpRequest->setHttpMethod(HttpMethod::POST);
    // Setting a body value is only compatible with HTTP POST and PUT requests.
    if (!empty($payload)) {
        $httpRequest->setBody($payload);
    }
    
    // Create a Cloud Task object.
    $task = new Task();
    $task->setHttpRequest($httpRequest);
    
    // Send request and print the task name.
    $request = (new CreateTaskRequest())
        ->setParent($queueName)
        ->setTask($task);
    $response = $client->createTask($request);
    printf('Created task %s' . PHP_EOL, $response->getName());
    

### Python

To learn how to install and use the client library for Cloud Tasks, see [Cloud Tasks client libraries](https://docs.cloud.google.com/tasks/docs/reference/libraries). For more information, see the [Cloud Tasks Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest). 

To authenticate to Cloud Tasks, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import datetime
    import json
    from typing import Dict, Optional
    
    from google.cloud import [tasks_v2](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest)
    from google.protobuf import duration_pb2, timestamp_pb2
    
    
    def create_http_task(
        project: str,
        location: str,
        queue: str,
        url: str,
        json_payload: Dict,
        scheduled_seconds_from_now: Optional[int] = None,
        task_id: Optional[str] = None,
        deadline_in_seconds: Optional[int] = None,
    ) -> tasks_v2.Task:
        """Create an HTTP POST task with a JSON payload.
        Args:
            project: The project ID where the queue is located.
            location: The location where the queue is located.
            queue: The ID of the queue to add the task to.
            url: The target URL of the task.
            json_payload: The JSON payload to send.
            scheduled_seconds_from_now: Seconds from now to schedule the task for.
            task_id: ID to use for the newly created task.
            deadline_in_seconds: The deadline in seconds for task.
        Returns:
            The newly created task.
        """
    
        # Create a client.
        client = [tasks_v2](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest).[CloudTasksClient](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2.services.cloud_tasks.CloudTasksClient.html)()
    
        # Construct the task.
        task = [tasks_v2](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest).[Task](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2.types.Task.html)(
            http_request=[tasks_v2](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest).[HttpRequest](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2.types.HttpRequest.html)(
                http_method=[tasks_v2](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest).[HttpMethod](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2.types.HttpMethod.html).POST,
                url=url,
                headers={"Content-type": "application/json"},
                body=json.dumps(json_payload).encode(),
            ),
            name=(
                client.[task_path](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2.services.cloud_tasks.CloudTasksClient.html#google_cloud_tasks_v2_services_cloud_tasks_CloudTasksClient_task_path)(project, location, queue, task_id)
                if task_id is not None
                else None
            ),
        )
    
        # Convert "seconds from now" to an absolute Protobuf Timestamp
        if scheduled_seconds_from_now is not None:
            timestamp = timestamp_pb2.Timestamp()
            timestamp.FromDatetime(
                datetime.datetime.utcnow()
                + datetime.timedelta(seconds=scheduled_seconds_from_now)
            )
            task.schedule_time = timestamp
    
        # Convert "deadline in seconds" to a Protobuf Duration
        if deadline_in_seconds is not None:
            duration = duration_pb2.Duration()
            duration.FromSeconds(deadline_in_seconds)
            task.dispatch_deadline = duration
    
        # Use the client to send a CreateTaskRequest.
        return client.[create_task](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2.services.cloud_tasks.CloudTasksClient.html#google_cloud_tasks_v2_services_cloud_tasks_CloudTasksClient_create_task)(
            [tasks_v2](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest).[CreateTaskRequest](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2.types.CreateTaskRequest.html)(
                # The queue to add the task to
                parent=client.[queue_path](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2.services.cloud_tasks.CloudTasksClient.html#google_cloud_tasks_v2_services_cloud_tasks_CloudTasksClient_queue_path)(project, location, queue),
                # The task itself
                task=task,
            )
        )
    
    

### Ruby

To learn how to install and use the client library for Cloud Tasks, see [Cloud Tasks client libraries](https://docs.cloud.google.com/tasks/docs/reference/libraries). For more information, see the [Cloud Tasks Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks/latest). 

To authenticate to Cloud Tasks, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/tasks"
    
    # Create a Task with an HTTP Target
    #
    # @param [String] project_id Your Google Cloud Project ID.
    # @param [String] location_id Your Google Cloud Project Location ID.
    # @param [String] queue_id Your Google Cloud Tasks Queue ID.
    # @param [String] url The full path to sent the task request to.
    # @param [String] payload The request body of your task.
    # @param [Integer] seconds The delay, in seconds, to process your task.
    def create_http_task project_id, location_id, queue_id, url, payload: nil, seconds: nil
      # Instantiates a client.
      client = Google::Cloud::[Tasks](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks.html).[cloud_tasks](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks/latest/Google-Cloud-Tasks.html)
    
      # Construct the fully qualified queue name.
      parent = client.queue_path project: project_id, location: location_id, queue: queue_id
    
      # Construct task.
      task = {
        http_request: {
          http_method: "POST",
          url:         url
        }
      }
    
      # Add payload to task body.
      task[:http_request][:body] = payload if payload
    
      # Add scheduled time to task.
      if seconds
        timestamp = Google::Protobuf::[Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_services-v1/latest/Google-Protobuf-Timestamp.html).new
        timestamp.[seconds](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_services-v1/latest/Google-Protobuf-Timestamp.html) = Time.now.to_i + seconds.to_i
        task[:schedule_time] = timestamp
      end
    
      # Send create task request.
      puts "Sending task #{task}"
    
      response = client.create_task parent: parent, task: task
    
      puts "Created task #{response.name}" if response.name
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudtasks). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
