---
url: https://docs.cloud.google.com/tasks/docs/creating-http-target-tasks/
title: Create HTTP target tasks programmatically \u00a0|\u00a0 Cloud Tasks \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:34:46.073969+00:00
---

# Create HTTP target tasks programmatically  |  Cloud Tasks  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tasks/docs/creating-http-target-tasks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Tasks ](https://docs.cloud.google.com/tasks/docs)
  * [ Guides ](https://docs.cloud.google.com/tasks/docs/dual-overview)



Send feedback 

#  Create HTTP target tasks programmatically Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Tasks handlers can be run on any HTTP endpoint with an external IP address such as [GKE](https://docs.cloud.google.com/kubernetes-engine/docs), [Compute Engine](https://docs.cloud.google.com/compute/docs), or even an on-premises web server. Your tasks can be executed on any of these services in a reliable, configurable fashion.

This document demonstrates how to programmatically create HTTP target tasks using Cloud Tasks client libraries, and place them in [Cloud Tasks queues](https://docs.cloud.google.com/tasks/docs/creating-queues). You can also create HTTP target tasks in the Google Cloud console, by using the Google Cloud CLI, or by sending a direct request to the Cloud Tasks API. For more information, see [Create tasks](https://docs.cloud.google.com/tasks/docs/create-tasks).

For tasks that have HTTP targets (as opposed to explicit App Engine targets, which are less common), there are two ways to create tasks:

  * **`CreateTask` method:** You must explicitly create a task object. Use this method if the tasks in your queue have different routing configurations. In this case, you specify routing at the task level and cannot use queue-level routing. This approach uses the `CreateTask` method.

  * **`BufferTask` method:** Use this method if your queue is set up to buffer tasks in front of a service. The queue must have queue-level routing. This approach uses the `BufferTask` method.




For guidance on how to choose between the two methods for creating HTTP tasks, see [Choose your task creation method](https://docs.cloud.google.com/tasks/docs/choose-task-creation-method).

## Create a task using the `CreateTask` method

This section discusses creating a task by constructing the task object. You use the `CreateTask` method.

When you create a task using the `CreateTask` method, you explicitly create and define the task object. You must specify the service and handler that process the task.

Optionally, you can pass task-specific data along to the handler. You can also fine-tune the [configuration](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations.queues.tasks#Task) for the task, like scheduling a time in the future when it should be executed or limiting the number of times you want the task to be retried if it fails (see Advanced configuration).

The following examples call the `CreateTask` method to create a task using the Cloud Tasks client libraries.

###  C# 
    
    
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

###  Go 
    
    
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
    

###  Java 
    
    
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

Note the `pom.xml` file:
    
    
    <?xml version='1.0' encoding='UTF-8'?>
    <project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
      <modelVersion>4.0.0</modelVersion>
      <groupId>com.example.tasks</groupId>
      <artifactId>cloudtasks-snippets</artifactId>
      <packaging>jar</packaging>
      <name>Google Cloud Tasks Snippets</name>
    
      <!--
        The parent pom defines common style checks and testing strategies for our samples.
        Removing or replacing it should not affect the execution of the samples in anyway.
      -->
      <parent>
        <groupId>com.google.cloud.samples</groupId>
        <artifactId>shared-configuration</artifactId>
        <version>1.2.0</version>
      </parent>
    
      <properties>
        <maven.compiler.target>1.8</maven.compiler.target>
        <maven.compiler.source>1.8</maven.compiler.source>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
      </properties>
    
    
      <dependencyManagement>
        <dependencies>
          <dependency>
            <groupId>com.google.cloud</groupId>
            <artifactId>libraries-bom</artifactId>
            <version>26.32.0</version>
            <type>pom</type>
            <scope>import</scope>
          </dependency>
        </dependencies>
      </dependencyManagement>
    
      <dependencies>
        <dependency>
          <groupId>com.google.cloud</groupId>
          <artifactId>google-cloud-tasks</artifactId>
        </dependency>
    
        <dependency>
          <groupId>junit</groupId>
          <artifactId>junit</artifactId>
          <version>4.13.2</version>
          <scope>test</scope>
        </dependency>
        <dependency>
          <groupId>com.google.truth</groupId>
          <artifactId>truth</artifactId>
          <version>1.4.0</version>
          <scope>test</scope>
        </dependency>
      </dependencies>
    </project>

###  Node.js 
    
    
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

Note the `package.json` file:
    
    
    {
      "name": "appengine-cloudtasks",
      "description": "Google App Engine Cloud Tasks example.",
      "license": "Apache-2.0",
      "author": "Google Inc.",
      "private": true,
      "engines": {
        "node": ">=20.0.0"
      },
      "files": [
        "*.js"
      ],
      "scripts": {
        "test": "c8 mocha -p -j 2 --timeout 30000",
        "start": "node server.js"
      },
      "dependencies": {
        "@google-cloud/tasks": "^6.0.0",
        "express": "^5.0.0"
      },
      "devDependencies": {
        "c8": "^12.0.0",
        "chai": "^6.0.0",
        "mocha": "^10.0.0",
        "uuid": "^11.1.1"
      }
    }
    

###  PHP 
    
    
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
    

Note the `composer.json` file:
    
    
    {
        "require": {
            "google/cloud-tasks": "^2.0"
        }
    }
    

###  Python 
    
    
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
    
    

Note the `requirements.txt` file:
    
    
    google-cloud-tasks==2.18.0
    

###  Ruby 
    
    
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

## Create a task using the `BufferTask` method

This section discusses creating a task by sending an HTTP request. The method you use is called `BufferTask`.

### Limitations

The `BufferTask` method is subject to the following limitations:

  * **Client libraries:** The `BufferTask` method is not supported in client libraries.

  * **RPC API:** The `BufferTask` method is not supported in the RPC API.

  * **Task-level routing:** This method does not support task-level routing. Since there is nowhere to add routing information when creating a task this way, you must use queue-level routing (otherwise the task has no routing information). If your queue does not already use queue-level routing, see [Configure queue-level routing for HTTP tasks](https://docs.cloud.google.com/tasks/docs/configuring-queues#configure_queue-level_routing_for_http_tasks).




### Call the `BufferTask` method

The following examples show how to create a task by sending an HTTP `POST` request to the Cloud Tasks API [`buffer` endpoint](https://docs.cloud.google.com/tasks/docs/reference/rest/v2beta3/projects.locations.queues.tasks/buffer).

###  curl 

The following code snippet shows an example of task creation using the `BufferTask` method with `curl`:
    
    
    curl -X HTTP_METHOD\
    "https://cloudtasks.googleapis.com/v2/projects/PROJECT_ID/locations/LOCATION/queues/QUEUE_ID/tasks:buffer" \

Replace the following:

  * `HTTP_METHOD`: the HTTP method for your request; for example `GET` or `POST`.
  * `PROJECT_ID`: the ID of your Google Cloud project. You can get this by running the following in your terminal: 
        
        gcloud config get-value project

  * `LOCATION`: the location of your queue.
  * `QUEUE_ID`: the ID of your queue.



###  Python 
    
    
    from google.cloud import tasks_v2beta3 as tasks
    
    import requests
    
    
    def send_task_to_http_queue(
        queue: tasks.Queue, body: str = "", token: str = "", headers: dict = {}
    ) -> int:
        """Send a task to an HTTP queue.
        Args:
            queue: The queue to send task to.
            body: The body of the task.
            auth_token: An authorization token for the queue.
            headers: Headers to set on the task.
        Returns:
            The matching queue, or None if it doesn't exist.
        """
    
        # Use application default credentials if not supplied in a header
        if token:
            headers["Authorization"] = f"Bearer {token}"
    
        endpoint = f"https://cloudtasks.googleapis.com/v2beta3/{queue.name}/tasks:buffer"
        response = requests.post(endpoint, body, headers=headers)
    
        return response.status_code
    
    

## Set up a service account for HTTP target handler authentication

Cloud Tasks can call HTTP target handlers that require authentication if you have a [service account](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts) with the appropriate credentials to access the handler.

You can use your current service account if you grant it the appropriate roles. These instructions cover creating a new service account specifically for this function. The existing or new service account used for Cloud Tasks authentication **must** be in the same project as your Cloud Tasks queues.

  1. In the Google Cloud console, go to the **Service Accounts** page.

[Go to Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

  2. If necessary, select the appropriate project.

  3. Click add **Create service account**.

  4. Give your service account a name. Note the related email address that is generated in the console. You will search for this email in a subsequent step. To copy the email, click **Copy to clipboard** content_copy. You can also add a description of what the account is for.

  5. Click **Create and continue**.

  6. In the **Select a role** list, search for and select **Cloud Tasks Enqueuer (Beta)**. This role gives the service account permission to add tasks to the queue.

  7. If you are using a Google Cloud handler, click **\+ Add another role** to grant the service account the role associated with accessing the service where your handler is running. Each service within Google Cloud requires a different role. For example, to access a handler on Cloud Run, grant the **Cloud Run Invoker** role.

  8. To finish creating the service account, click **Done**.

  9. To allow Cloud Tasks to create authentication tokens using the service account you just created, you must grant the [Service Account User](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) role to the Cloud Tasks [primary service agent](https://docs.cloud.google.com/iam/docs/service-agents) on the service account you just created.

     1. In the Google Cloud console, go to the **Service accounts** page.

[Go to Service accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

     2. In the row for the service account you just created, select the checkbox, and then click person_add **Manage access**.

     3. In the **Manage Access** pane, click person_add **Add principal**.

     4. In the **New principals** list, search for and select the Cloud Tasks service agent which will have an email address in the format `service-PROJECT_NUMBER@gcp-sa-cloudtasks.iam.gserviceaccount.com`.

     5. In the **Select a role** list, search for and select the **Service Account User** role.

     6. Click **Save**.


**Note:** Cloud Tasks must have a primary service agent with the `Cloud Tasks Service Agent` role granted. This allows Cloud Tasks to generate header tokens based on the credentials associated with the Cloud Tasks service account and authenticate with its handler. The Cloud Tasks service agent is automatically created with this role granted when you enable the Cloud Tasks API, _unless_ you enabled it prior to March 19, 2019, in which case you must add the role manually.

## Use HTTP target tasks with authentication tokens

To authenticate between Cloud Tasks and an HTTP target handler that requires authentication, Cloud Tasks creates a header token. This token is based on the credentials in the `Cloud Tasks Enqueuer` service account, identified by its email address. The service account used for authentication must be part of the same project where your Cloud Tasks queue resides. The request, with the header token, is sent from the queue to the handler using HTTPS. You can use either an [ID token](https://www.oauth.com/oauth2-servers/openid-connect/id-tokens/) or an [access token](https://datatracker.ietf.org/doc/html/rfc6749#section-1.4). ID tokens should generally be used for any handler running on Google Cloud; for example, on Cloud Run functions or Cloud Run. The main exception is for Google APIs hosted on `*.googleapis.com` which expect an access token.

You can configure authentication at the queue level by setting the [`httpTarget`](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations.queues#httptarget) override (specifically the [`oauthToken`](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/OAuthToken) or [`oidcToken`](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/OidcToken) fields). If authentication is configured at the queue level, this configuration overrides any authentication configured at the task level. For example, if a queue has an OIDC token override configured, tasks added to that queue with OAuth tokens will dispatch with the queue-level OIDC token.

To configure authentication at the task level, specify either an ID token, or an access token, in the [task](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations.queues.tasks#HttpRequest) itself.

### `CreateTask` method

The following examples use the `CreateTask` method with the Cloud Tasks client libraries to create a task that also includes the creation of a header token. ID tokens are used in the examples. To use an access token, replace the OIDC parameter with the language appropriate OAuth parameter in constructing the request.

###  Go 
    
    
    import (
    	"context"
    	"fmt"
    
    	cloudtasks "cloud.google.com/go/cloudtasks/apiv2"
    	taskspb "cloud.google.com/go/cloudtasks/apiv2/cloudtaskspb"
    )
    
    // createHTTPTaskWithToken constructs a task with a authorization token
    // and HTTP target then adds it to a Queue.
    func createHTTPTaskWithToken(projectID, locationID, queueID, url, email, message string) (*taskspb.Task, error) {
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
    					AuthorizationHeader: &taskspb.HttpRequest_OidcToken{
    						OidcToken: &taskspb.OidcToken{
    							ServiceAccountEmail: email,
    						},
    					},
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
    

###  Java 
    
    
    import com.google.cloud.tasks.v2.[CloudTasksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.CloudTasksClient.html);
    import com.google.cloud.tasks.v2.[HttpMethod](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.HttpMethod.html);
    import com.google.cloud.tasks.v2.[HttpRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.HttpRequest.html);
    import com.google.cloud.tasks.v2.[OidcToken](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.OidcToken.html);
    import com.google.cloud.tasks.v2.[QueueName](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.QueueName.html);
    import com.google.cloud.tasks.v2.[Task](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Task.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import java.io.IOException;
    import java.nio.charset.Charset;
    
    public class CreateHttpTaskWithToken {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project-id";
        String locationId = "us-central1";
        String queueId = "my-queue";
        String serviceAccountEmail =
            "java-docs-samples-testing@java-docs-samples-testing.iam.gserviceaccount.com";
        createTask(projectId, locationId, queueId, serviceAccountEmail);
      }
    
      // Create a task with a HTTP target and authorization token using the Cloud Tasks client.
      public static void createTask(
          String projectId, String locationId, String queueId, String serviceAccountEmail)
          throws IOException {
    
        // Instantiates a client.
        try ([CloudTasksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.CloudTasksClient.html) client = [CloudTasksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.CloudTasksClient.html).create()) {
          String url =
              "https://example.com/taskhandler"; // The full url path that the request will be sent to
          String payload = "Hello, World!"; // The task HTTP request body
    
          // Construct the fully qualified queue name.
          String queuePath = [QueueName](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.QueueName.html).of(projectId, locationId, queueId).toString();
    
          // Add your service account email to construct the OIDC token.
          // in order to add an authentication header to the request.
          [OidcToken](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.OidcToken.html).Builder oidcTokenBuilder =
              [OidcToken](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.OidcToken.html).newBuilder().setServiceAccountEmail(serviceAccountEmail);
    
          // Construct the task body.
          [Task](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Task.html).Builder taskBuilder =
              [Task](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Task.html).newBuilder()
                  .[setHttpRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Task.Builder.html#com_google_cloud_tasks_v2_Task_Builder_setHttpRequest_com_google_cloud_tasks_v2_HttpRequest_)(
                      [HttpRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.HttpRequest.html).newBuilder()
                          .setBody([ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFrom](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFrom_byte___)(payload, Charset.defaultCharset()))
                          .setHttpMethod([HttpMethod](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.HttpMethod.html).POST)
                          .[setUrl](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.HttpRequest.Builder.html#com_google_cloud_tasks_v2_HttpRequest_Builder_setUrl_java_lang_String_)(url)
                          .setOidcToken(oidcTokenBuilder)
                          .build());
    
          // Send create task request.
          [Task](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Task.html) task = client.createTask(queuePath, taskBuilder.build());
          System.out.println("Task created: " + task.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Task.html#com_google_cloud_tasks_v2_Task_getName__)());
        }
      }
    }

Note the `pom.xml` file:
    
    
    <?xml version='1.0' encoding='UTF-8'?>
    <project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
      <modelVersion>4.0.0</modelVersion>
      <groupId>com.example.tasks</groupId>
      <artifactId>cloudtasks-snippets</artifactId>
      <packaging>jar</packaging>
      <name>Google Cloud Tasks Snippets</name>
    
      <!--
        The parent pom defines common style checks and testing strategies for our samples.
        Removing or replacing it should not affect the execution of the samples in anyway.
      -->
      <parent>
        <groupId>com.google.cloud.samples</groupId>
        <artifactId>shared-configuration</artifactId>
        <version>1.2.0</version>
      </parent>
    
      <properties>
        <maven.compiler.target>1.8</maven.compiler.target>
        <maven.compiler.source>1.8</maven.compiler.source>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
      </properties>
    
    
      <dependencyManagement>
        <dependencies>
          <dependency>
            <groupId>com.google.cloud</groupId>
            <artifactId>libraries-bom</artifactId>
            <version>26.32.0</version>
            <type>pom</type>
            <scope>import</scope>
          </dependency>
        </dependencies>
      </dependencyManagement>
    
      <dependencies>
        <dependency>
          <groupId>com.google.cloud</groupId>
          <artifactId>google-cloud-tasks</artifactId>
        </dependency>
    
        <dependency>
          <groupId>junit</groupId>
          <artifactId>junit</artifactId>
          <version>4.13.2</version>
          <scope>test</scope>
        </dependency>
        <dependency>
          <groupId>com.google.truth</groupId>
          <artifactId>truth</artifactId>
          <version>1.4.0</version>
          <scope>test</scope>
        </dependency>
      </dependencies>
    </project>

###  Node.js 
    
    
    // Imports the Google Cloud Tasks library.
    const {CloudTasksClient} = require('[@google-cloud/tasks](https://docs.cloud.google.com/nodejs/docs/reference/tasks/latest/overview.html)');
    
    // Instantiates a client.
    const client = new [CloudTasksClient](https://docs.cloud.google.com/nodejs/docs/reference/tasks/latest/overview.html)();
    
    async function createHttpTaskWithToken() {
      // TODO(developer): Uncomment these lines and replace with your values.
      // const project = 'my-project-id';
      // const queue = 'my-queue';
      // const location = 'us-central1';
      // const url = 'https://example.com/taskhandler';
      // const serviceAccountEmail = 'client@<project-id>.iam.gserviceaccount.com';
      // const payload = 'Hello, World!';
    
      // Construct the fully qualified queue name.
      const parent = client.queuePath(project, location, queue);
    
      const task = {
        httpRequest: {
          headers: {
            'Content-Type': 'text/plain', // Set content type to ensure compatibility your application's request parsing
          },
          httpMethod: 'POST',
          url,
          oidcToken: {
            serviceAccountEmail,
          },
        },
      };
    
      if (payload) {
        task.httpRequest.body = Buffer.from(payload).toString('base64');
      }
    
      console.log('Sending task:');
      console.log(task);
      // Send create task request.
      const request = {parent: parent, task: task};
      const [response] = await client.createTask(request);
      const name = response.name;
      console.log(`Created task ${name}`);
    }
    createHttpTaskWithToken();

Note the `package.json` file:
    
    
    {
      "name": "appengine-cloudtasks",
      "description": "Google App Engine Cloud Tasks example.",
      "license": "Apache-2.0",
      "author": "Google Inc.",
      "private": true,
      "engines": {
        "node": ">=20.0.0"
      },
      "files": [
        "*.js"
      ],
      "scripts": {
        "test": "c8 mocha -p -j 2 --timeout 30000",
        "start": "node server.js"
      },
      "dependencies": {
        "@google-cloud/tasks": "^6.0.0",
        "express": "^5.0.0"
      },
      "devDependencies": {
        "c8": "^12.0.0",
        "chai": "^6.0.0",
        "mocha": "^10.0.0",
        "uuid": "^11.1.1"
      }
    }
    

###  Python 
    
    
    from typing import Optional
    
    from google.cloud import [tasks_v2](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest)
    
    
    def create_http_task_with_token(
        project: str,
        location: str,
        queue: str,
        url: str,
        payload: bytes,
        service_account_email: str,
        audience: Optional[str] = None,
    ) -> tasks_v2.Task:
        """Create an HTTP POST task with an OIDC token and an arbitrary payload.
        Args:
            project: The project ID where the queue is located.
            location: The location where the queue is located.
            queue: The ID of the queue to add the task to.
            url: The target URL of the task.
            payload: The payload to send.
            service_account_email: The service account to use for generating the OIDC token.
            audience: Audience to use when generating the OIDC token.
        Returns:
            The newly created task.
        """
    
        # Create a client.
        client = [tasks_v2](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest).[CloudTasksClient](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2.services.cloud_tasks.CloudTasksClient.html)()
    
        # Construct the request body.
        task = [tasks_v2](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest).[Task](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2.types.Task.html)(
            http_request=[tasks_v2](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest).[HttpRequest](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2.types.HttpRequest.html)(
                http_method=[tasks_v2](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest).[HttpMethod](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2.types.HttpMethod.html).POST,
                url=url,
                oidc_token=[tasks_v2](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest).[OidcToken](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2.types.OidcToken.html)(
                    service_account_email=service_account_email,
                    audience=audience,
                ),
                body=payload,
            ),
        )
    
        # Use the client to build and send the task.
        return client.[create_task](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2.services.cloud_tasks.CloudTasksClient.html#google_cloud_tasks_v2_services_cloud_tasks_CloudTasksClient_create_task)(
            [tasks_v2](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest).[CreateTaskRequest](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2.types.CreateTaskRequest.html)(
                parent=client.[queue_path](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2.services.cloud_tasks.CloudTasksClient.html#google_cloud_tasks_v2_services_cloud_tasks_CloudTasksClient_queue_path)(project, location, queue),
                task=task,
            )
        )
    
    

Note the `requirements.txt` file:
    
    
    google-cloud-tasks==2.18.0
    

### `BufferTask` method

The following examples use application default credentials to authenticate when using the `BufferTask` method for creating a task.

###  curl 
    
    
    curl -X HTTP_METHOD\
    "https://cloudtasks.googleapis.com/v2/projects/PROJECT_ID/locations/LOCATION/queues/QUEUE_ID/tasks:buffer" \
        -H "Authorization: Bearer ACCESS_TOKEN"

Replace the following:

  * `HTTP_METHOD`: the HTTP method for your request; for example `GET` or `POST`.
  * `PROJECT_ID`: the ID of your Google Cloud project. You can get this by running the following in your terminal: 
        
        gcloud config get-value project

  * `LOCATION`: the location of your queue.
  * `QUEUE_ID`: the ID of your queue.
  * `ACCESS_TOKEN`: your access token. You can get this by running the following in your terminal:
  * gcloud auth application-default login

  * gcloud auth application-default print-access-token




###  Python 

In the following code sample, provide your authentication token value.
    
    
    from google.cloud import tasks_v2beta3 as tasks
    
    import requests
    
    
    def send_task_to_http_queue(
        queue: tasks.Queue, body: str = "", token: str = "", headers: dict = {}
    ) -> int:
        """Send a task to an HTTP queue.
        Args:
            queue: The queue to send task to.
            body: The body of the task.
            auth_token: An authorization token for the queue.
            headers: Headers to set on the task.
        Returns:
            The matching queue, or None if it doesn't exist.
        """
    
        # Use application default credentials if not supplied in a header
        if token:
            headers["Authorization"] = f"Bearer {token}"
    
        endpoint = f"https://cloudtasks.googleapis.com/v2beta3/{queue.name}/tasks:buffer"
        response = requests.post(endpoint, body, headers=headers)
    
        return response.status_code
    
    

## Provide your own HTTP target task handlers

HTTP target task handlers are very similar to [App Engine task handlers](https://docs.cloud.google.com/tasks/docs/creating-appengine-handlers), with the following exceptions:

  * **Timeouts** : for all HTTP target task handlers the default timeout is 10 minutes, with a maximum of 30 minutes.
  * **Authentication logic** : if you are writing your own code in the targeted service to validate the token, you should use an ID token. For more information on what this entails, see [OpenID Connect](https://developers.google.com/identity/protocols/OpenIDConnect), particularly [Validating an ID token](https://developers.google.com/identity/protocols/OpenIDConnect#validatinganidtoken).
  * **Headers** : an HTTP target request has headers set by the queue, which contain task-specific information your handler can use. These are similar to, but not identical with, the headers set on [App Engine task requests](https://docs.cloud.google.com/tasks/docs/creating-appengine-handlers#reading_request_headers). These headers provide information **only**. They should **not** be used as sources of identity.

If these headers were present in an external user request to your app, they are replaced by the internal ones. The sole exception is for requests from logged-in administrators of the application, who are allowed to set headers for testing purposes.

HTTP target requests always contain the following headers:

Header | Description  
---|---  
`X-CloudTasks-QueueName` | The name of the queue.  
`X-CloudTasks-TaskName` | The "short" name of the task, or, if no name was specified at creation, a unique system-generated id. This is the `my-task-id` value in the complete task name, ie, task_name = `projects/my-project-id/locations/my-location/queues/my-queue-id/tasks/my-task-id`.  
`X-CloudTasks-TaskRetryCount` | The number of times this task has been retried. For the first attempt, this value is `0`. This number includes attempts where the task failed due to 5XX error codes and never reached the execution phase.  
`X-CloudTasks-TaskExecutionCount` | The total number of times that the task has received a response from the handler. Since Cloud Tasks deletes the task once a successful response has been received, all previous handler responses were failures. This number does not include failures due to 5XX error codes.  
`X-CloudTasks-TaskETA` | Initially, the originally scheduled time of the task, specified in seconds since January 1st 1970. Note that it represents the expected dispatch time. On retries, it is updated closer to the current time and can be used to measure delivery latency. It should _not_ be used for [task deduplication](https://docs.cloud.google.com/tasks/docs/dual-overview#task_deduplication).  
  
In addition, requests from Cloud Tasks might contain the following headers:

Header | Description  
---|---  
`X-CloudTasks-TaskPreviousResponse` | The HTTP response code from the previous retry.  
`X-CloudTasks-TaskRetryReason` | The reason for retrying the task.  



## Manually add the Cloud Tasks Service Agent role

You can manually add the [Cloud Tasks Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtasks#cloudtasks.serviceAgent) (`roles/cloudtasks.serviceAgent`) role to your Cloud Tasks service account which is the [primary service agent](https://docs.cloud.google.com/iam/docs/service-account-types#primary) for Cloud Tasks.

This is necessary **only** if you enabled the Cloud Tasks API prior to March 19, 2019.

###  Console 

  1. Find and copy the project number for your Google Cloud project on the [Welcome](https://console.cloud.google.com/welcome) page of the Google Cloud console.
  2. In the Google Cloud console, go to the **IAM** page.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  3. Click **Grant access**. The **Grant access** pane opens.

  4. In the **Add principals** section, add an email address in this format: 
         
         service-PROJECT_NUMBER@gcp-sa-cloudtasks.iam.gserviceaccount.com
          

Replace `PROJECT_NUMBER` with your Google Cloud project number.

  5. In the **Assign roles** section, search for and select **Cloud Tasks Service Agent**.

  6. Click **Save**.




###  gcloud 

  1. Find your project number: 
         
         gcloud projects describe PROJECT_ID --format='table(projectNumber)'

Replace PROJECT_ID with your project ID.

  2. Copy down the number.

  3. Grant the Cloud Tasks service account the `Cloud Tasks Service Agent` role, using the project number you copied down:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member serviceAccount:service-PROJECT_NUMBER@gcp-sa-cloudtasks.iam.gserviceaccount.com \
             --role roles/cloudtasks.serviceAgent

Replace the following:

     * `PROJECT_ID`: your Google Cloud project ID.
     * `PROJECT_NUMBER`: your Google Cloud project number.



**Note:** Adding the service account can take a few minutes to complete.

## Other configurations

There are a number of task attributes that you can configure. For a full list, see the [task resource definition](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations.queues.tasks#resource:-task). For example, you can customize the following attributes:

  * **Naming:** If you choose to specify a name for the task, Cloud Tasks can use that name to ensure [task deduplication](https://docs.cloud.google.com/tasks/docs/dual-overview#task_deduplication), although the processing necessary for this can add increased latency.
  * **Scheduling:** You can schedule a task at a future time. This is supported for `CreateTask` only and not supported for `BufferTask`.



You can also configure queue attributes such as routing overrides, rate limits, and retry parameters. These configurations are applied to all tasks in a queue. For more information, see [Configure queue routing, limits, and retries](https://docs.cloud.google.com/tasks/docs/configuring-queues).

## What's next

  * Learn more about HTTP target tasks in the [RPC API reference](https://docs.cloud.google.com/tasks/docs/reference/rpc/google.cloud.tasks.v2).
  * Learn more about HTTP target tasks in the [REST API reference](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations.queues.tasks). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
