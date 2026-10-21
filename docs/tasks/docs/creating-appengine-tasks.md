---
url: https://docs.cloud.google.com/tasks/docs/creating-appengine-tasks/
title: Create App Engine tasks programmatically \u00a0|\u00a0 Cloud Tasks \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:13.061736+00:00
---

# Create App Engine tasks programmatically  |  Cloud Tasks  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tasks/docs/creating-appengine-tasks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Tasks ](https://docs.cloud.google.com/tasks/docs)
  * [ Guides ](https://docs.cloud.google.com/tasks/docs/dual-overview)



Send feedback 

#  Create App Engine tasks programmatically Stay organized with collections  Save and categorize content based on your preferences. 

This document demonstrates how to programmatically create App Engine tasks and place them in [Cloud Tasks queues](https://docs.cloud.google.com/tasks/docs/creating-queues).

Using this process you can explicitly specify the service and handler that should process the task, and optionally pass task-specific data along to the handler. The Cloud Tasks service forwards the task request to the handler, but this worker is located within App Engine. So all queues that target App Engine handlers must have an [App Engine app](https://docs.cloud.google.com/appengine/docs/standard/python/console#create). The handlers must run in the [region](https://docs.cloud.google.com/appengine/docs/locations) where the App Engine app runs. This region also serves as the `LOCATION_ID` parameter for your Cloud Tasks requests. For more information, see [Cloud Tasks queues with App Engine targets](https://docs.cloud.google.com/tasks/docs/dual-overview#appe).

You can fine-tune the [configuration](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations.queues.tasks#resource-task) for the task, like scheduling a time in the future when it should be executed or limiting the number of times you want the task to be retried if it fails. If you chose to specify a name for the [task](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations.queues.tasks/create#request-body), Cloud Tasks can use that name to ensure [task deduplication](https://docs.cloud.google.com/tasks/docs/dual-overview#task_deduplication), although the processing necessary for this can add increased latency.

You can also create App Engine tasks by using the Google Cloud CLI or by sending a direct request to the Cloud Tasks API. For more information, see [Create tasks](https://docs.cloud.google.com/tasks/docs/create-tasks).

## App Engine firewall rules

In the App Engine standard environment, the App Engine firewall can allow certain internal traffic to bypass the firewall. This means that if you set the `default` rule to `deny`, requests from certain services destined for the App Engine standard environment don't get blocked. These are all types of traffic requested in the app's own configuration, or sent from the same app. Requests that bypass firewall rules in this way also include App Engine tasks in Cloud Tasks (including App Engine Task Queues).

To allow incoming requests, the following are the IP ranges for App Engine tasks in Cloud Tasks (including App Engine Task Queues):

  * IP range for requests sent to the App Engine standard environment: `0.1.0.2/32` (bypasses the default firewall rule if set to deny)

  * IP range for requests sent to the App Engine flexible environment: `0.1.0.2/32`




## Create tasks using the client libraries

You create tasks in the form of an [HTTP request](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations.queues.tasks/create), which you can construct as you like. Using the [client libraries](https://docs.cloud.google.com/apis/docs/cloud-client-libraries) however, as the following samples do, can help you manage details of low level communication with the server, including authenticating with Google. For adding a task to a queue, see [Add a task to a Cloud Tasks queue](https://docs.cloud.google.com/tasks/docs/add-task-queue)

###  C# 
    
    
    using [Google.Cloud.Tasks.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.html);
    using [Google.Protobuf](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.html);
    using [Google.Protobuf.WellKnownTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.html);
    using System;
    
    class CreateAppEngineTask
    {
        public string CreateTask(
            // TODO<developer>: call this method by passing correct values for
            // the following parameters or change the parameters' default values.
            string projectId = "YOUR-PROJECT-ID",
            string location = "us-central1",
            string queue = "my-queue",
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
                    AppEngineHttpRequest = new [AppEngineHttpRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.AppEngineHttpRequest.html)
                    {
                        HttpMethod = [HttpMethod](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.HttpMethod.html).[Post](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.HttpMethod.html#Google_Cloud_Tasks_V2_HttpMethod_Post),
                        RelativeUri = "/log_payload",
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
    
    
    // Command create_task constructs and adds a task to an App Engine Queue.
    package main
    
    import (
    	"context"
    	"fmt"
    
    	cloudtasks "cloud.google.com/go/cloudtasks/apiv2"
    	taskspb "cloud.google.com/go/cloudtasks/apiv2/cloudtaskspb"
    )
    
    // createTask creates a new task in your App Engine queue.
    func createTask(projectID, locationID, queueID, message string) (*taskspb.Task, error) {
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
    			// https://godoc.org/google.golang.org/genproto/googleapis/cloud/tasks/v2#AppEngineHttpRequest
    			MessageType: &taskspb.Task_AppEngineHttpRequest{
    				AppEngineHttpRequest: &taskspb.AppEngineHttpRequest{
    					HttpMethod:  taskspb.HttpMethod_POST,
    					RelativeUri: "/task_handler",
    				},
    			},
    		},
    	}
    
    	// Add a payload message if one is present.
    	req.Task.GetAppEngineHttpRequest().Body = []byte(message)
    
    	createdTask, err := client.CreateTask(ctx, req)
    	if err != nil {
    		return nil, fmt.Errorf("cloudtasks.CreateTask: %w", err)
    	}
    
    	return createdTask, nil
    }
    

###  Java 
    
    
    import com.google.cloud.tasks.v2.[AppEngineHttpRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.AppEngineHttpRequest.html);
    import com.google.cloud.tasks.v2.[CloudTasksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.CloudTasksClient.html);
    import com.google.cloud.tasks.v2.[HttpMethod](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.HttpMethod.html);
    import com.google.cloud.tasks.v2.[QueueName](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.QueueName.html);
    import com.google.cloud.tasks.v2.[Task](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Task.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import com.google.protobuf.[Timestamp](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html);
    import java.io.IOException;
    import java.nio.charset.Charset;
    import java.time.Clock;
    import java.time.Instant;
    
    public class CreateTask {
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project-id";
        String queue = "my-appengine-queue";
        String location = "us-central1";
        String payload = "hello";
        int seconds = 0; // Scheduled delay for the task in seconds
        createTask(projectId, queue, location, payload, seconds);
      }
    
      // This is an example snippet for showing best practices.
      public static void createTask(
          String projectId, String queueName, String location, String payload, int seconds)
          throws IOException {
        // Instantiates a client.
        try ([CloudTasksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.CloudTasksClient.html) client = [CloudTasksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.CloudTasksClient.html).create()) {
          // Construct the fully qualified queue name.
          String queuePath = [QueueName](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.QueueName.html).of(projectId, location, queueName).toString();
    
          // Construct the task body.
          [Task](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Task.html).Builder taskBuilder =
              [Task](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Task.html).newBuilder()
                  .[setAppEngineHttpRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Task.Builder.html#com_google_cloud_tasks_v2_Task_Builder_setAppEngineHttpRequest_com_google_cloud_tasks_v2_AppEngineHttpRequest_)(
                      [AppEngineHttpRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.AppEngineHttpRequest.html).newBuilder()
                          .setBody([ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFrom](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFrom_byte___)(payload, Charset.defaultCharset()))
                          .[setRelativeUri](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.AppEngineHttpRequest.Builder.html#com_google_cloud_tasks_v2_AppEngineHttpRequest_Builder_setRelativeUri_java_lang_String_)("/tasks/create")
                          .setHttpMethod([HttpMethod](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.HttpMethod.html).POST)
                          .build());
    
          // Add the scheduled time to the request.
          taskBuilder.setScheduleTime(
              [Timestamp](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html).newBuilder()
                  .setSeconds(Instant.now(Clock.systemUTC()).plusSeconds(seconds).getEpochSecond()));
    
          // Send create task request.
          [Task](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Task.html) task = client.createTask(queuePath, taskBuilder.build());
          System.out.println("Task created: " + task.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Task.html#com_google_cloud_tasks_v2_Task_getName__)());
        }
      }
    }

Note the `pom.xml` file:
    
    
    <?xml version="1.0" encoding="UTF-8"?>
    <!--
    Copyright 2019 Google LLC
    
     Licensed under the Apache License, Version 2.0 (the "License");
     you may not use this file except in compliance with the License.
     You may obtain a copy of the License at
    
           http://www.apache.org/licenses/LICENSE-2.0
    
     Unless required by applicable law or agreed to in writing, software
     distributed under the License is distributed on an "AS IS" BASIS,
     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
     See the License for the specific language governing permissions and
     limitations under the License.
    -->
    <project xmlns="http://maven.apache.org/POM/4.0.0"
             xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
             xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
      <modelVersion>4.0.0</modelVersion>
      <packaging>war</packaging>
      <version>1.0-SNAPSHOT</version>
      <groupId>com.example.appengine</groupId>
      <artifactId>appengine-tasks-j11</artifactId>
    
      <!--
        The parent pom defines common style checks and testing strategies for our samples.
        Removing or replacing it should not affect the execution of the samples in anyway.
      -->
      <parent>
        <groupId>com.google.cloud.samples</groupId>
        <artifactId>shared-configuration</artifactId>
        <version>1.2.0</version>
        <relativePath></relativePath>
      </parent>
    
      <properties>
        <maven.compiler.target>11</maven.compiler.target>
        <maven.compiler.source>11</maven.compiler.source>
      </properties>
    
      <!--  Using libraries-bom to manage versions.
      See https://github.com/GoogleCloudPlatform/cloud-opensource-java/wiki/The-Google-Cloud-Platform-Libraries-BOM -->
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
        <!-- Test dependencies -->
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
      <build>
        <finalName>tasks</finalName>
        <plugins>
          <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-war-plugin</artifactId>
            <version>3.4.0</version>
            <configuration>
              <failOnMissingWebXml>false</failOnMissingWebXml>
            </configuration>
          </plugin>
    
          <plugin>
            <groupId>org.codehaus.mojo</groupId>
            <artifactId>exec-maven-plugin</artifactId>
            <version>3.1.1</version>
            <configuration>
              <mainClass>com.example.task.CreateTask</mainClass>
              <cleanupDaemonThreads>false</cleanupDaemonThreads>
            </configuration>
          </plugin>
        </plugins>
      </build>
    </project>
    

###  Node.js 
    
    
    // Imports the Google Cloud Tasks library.
    const {CloudTasksClient} = require('[@google-cloud/tasks](https://docs.cloud.google.com/nodejs/docs/reference/tasks/latest/overview.html)');
    
    // Instantiates a client.
    const client = new [CloudTasksClient](https://docs.cloud.google.com/nodejs/docs/reference/tasks/latest/overview.html)();
    
    async function createTask() {
      // TODO(developer): Uncomment these lines and replace with your values.
      // const project = 'my-project-id';
      // const queue = 'my-appengine-queue';
      // const location = 'us-central1';
      // const payload = 'Hello, World!';
    
      // Construct the fully qualified queue name.
      const parent = client.queuePath(project, location, queue);
    
      const task = {
        appEngineHttpRequest: {
          headers: {
            'Content-Type': 'text/plain', // Set content type to ensure compatibility your application's request parsing
          },
          httpMethod: 'POST',
          relativeUri: '/log_payload',
        },
      };
    
      if (payload) {
        task.appEngineHttpRequest.body = Buffer.from(payload).toString('base64');
      }
    
      if (inSeconds) {
        // The time when the task is scheduled to be attempted.
        task.scheduleTime = {
          seconds: inSeconds + Date.now() / 1000,
        };
      }
    
      console.log('Sending task:');
      console.log(task);
    
      // Send create task request.
      const request = {parent: parent, task: task};
      const [response] = await client.createTask(request);
      const name = response.name;
      console.log(`Created task ${name}`);
    }
    
    createTask();

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
    
    
    use Google\Cloud\Tasks\V2\AppEngineHttpRequest;
    use Google\Cloud\Tasks\V2\CloudTasksClient;
    use Google\Cloud\Tasks\V2\HttpMethod;
    use Google\Cloud\Tasks\V2\Task;
    
    /** Uncomment and populate these variables in your code */
    // $projectId = 'The Google project ID';
    // $locationId = 'The Location ID';
    // $queueId = 'The Cloud Tasks App Engine Queue ID';
    // $payload = 'The payload your task should carry to the task handler. Optional';
    
    // Instantiate the client and queue name.
    $client = new CloudTasksClient();
    $queueName = $client->queueName($projectId, $locationId, $queueId);
    
    // Create an App Engine Http Request Object.
    $httpRequest = new AppEngineHttpRequest();
    // The path of the HTTP request to the App Engine service.
    $httpRequest->setRelativeUri('/task_handler');
    // POST is the default HTTP method, but any HTTP method can be used.
    $httpRequest->setHttpMethod(HttpMethod::POST);
    // Setting a body value is only compatible with HTTP POST and PUT requests.
    if (isset($payload)) {
        $httpRequest->setBody($payload);
    }
    
    // Create a Cloud Task object.
    $task = new Task();
    $task->setAppEngineHttpRequest($httpRequest);
    
    // Send request and print the task name.
    $response = $client->createTask($queueName, $task);
    printf('Created task %s' . PHP_EOL, $response->getName());
    

Note the `composer.json` file:
    
    
    {
        "require": {
            "google/cloud-tasks": "^2.0.0"
        }
    }
    

###  Python 
    
    
    """Create a task for a given queue with an arbitrary payload."""
    
    from google.cloud import [tasks_v2](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest)
    from google.protobuf import timestamp_pb2
    import datetime
    import json
    
    # Create a client.
    client = [tasks_v2](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest).[CloudTasksClient](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2.services.cloud_tasks.CloudTasksClient.html)()
    
    # TODO(developer): Uncomment these lines and replace with your values.
    # project = 'my-project-id'
    # queue = 'my-appengine-queue'
    # location = 'us-central1'
    # payload = 'hello' or {'param': 'value'} for application/json
    # in_seconds = None
    
    # Construct the fully qualified queue name.
    parent = client.[queue_path](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2.services.cloud_tasks.CloudTasksClient.html#google_cloud_tasks_v2_services_cloud_tasks_CloudTasksClient_queue_path)(project, location, queue)
    
    # Construct the request body.
    task = {
        "app_engine_http_request": {  # Specify the type of request.
            "http_method": [tasks_v2](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest).[HttpMethod](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2.types.HttpMethod.html).POST,
            "relative_uri": "/example_task_handler",
        }
    }
    if payload is not None:
        if isinstance(payload, dict):
            # Convert dict to JSON string
            payload = json.dumps(payload)
            # specify http content-type to application/json
            task["app_engine_http_request"]["headers"] = {
                "Content-type": "application/json"
            }
        # The API expects a payload of type bytes.
        converted_payload = payload.encode()
    
        # Add the payload to the request.
        task["app_engine_http_request"]["body"] = converted_payload
    
    if in_seconds is not None:
        # Convert "seconds from now" into an rfc3339 datetime string.
        d = datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(
            seconds=in_seconds
        )
    
        # Create Timestamp protobuf.
        timestamp = timestamp_pb2.Timestamp()
        timestamp.FromDatetime(d)
    
        # Add the timestamp to the tasks.
        task["schedule_time"] = timestamp
    
    # Use the client to build and send the task.
    response = client.[create_task](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2.services.cloud_tasks.CloudTasksClient.html#google_cloud_tasks_v2_services_cloud_tasks_CloudTasksClient_create_task)(parent=parent, task=task)
    
    print(f"Created task {response.name}")
    return response
    
    

Note the `requirements.txt` file:
    
    
    Flask==3.1.3; python_version >= '3.9'
    gunicorn==23.0.0
    google-cloud-tasks==2.18.0
    

###  Ruby 
    
    
    require "google/cloud/tasks"
    
    # Create an App Engine Task
    #
    # @param [String] project_id Your Google Cloud Project ID.
    # @param [String] location_id Your Google Cloud Project Location ID.
    # @param [String] queue_id Your Google Cloud App Engine Queue ID.
    # @param [String] payload The request body of your task.
    # @param [Integer] seconds The delay, in seconds, to process your task.
    def create_task project_id, location_id, queue_id, payload: nil, seconds: nil
      # Instantiates a client.
      client = Google::Cloud::[Tasks](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks/latest/Google-Cloud-Tasks.html).[cloud_tasks](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks/latest/Google-Cloud-Tasks.html)
    
      # Construct the fully qualified queue name.
      parent = client.queue_path project: project_id, location: location_id, queue: queue_id
    
      # Construct task.
      task = {
        app_engine_http_request: {
          http_method:  "POST",
          relative_uri: "/log_payload"
        }
      }
    
      # Add payload to task body.
      if payload
        task[:app_engine_http_request][:body] = payload
      end
    
      # Add scheduled time to task.
      if seconds
        timestamp = Google::Protobuf::[Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-binary_authorization-v1/latest/Google-Protobuf-Timestamp.html).new
        timestamp.[seconds](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-binary_authorization-v1/latest/Google-Protobuf-Timestamp.html) = Time.now.to_i + seconds.to_i
        task[:schedule_time] = timestamp
      end
    
      # Send create task request.
      puts "Sending task #{task}"
      response = client.create_task parent: parent, task: task
    
      puts "Created task #{response.name}" if response.name
    end

## What's next

  * Learn about creating [App Engine task handlers](https://docs.cloud.google.com/tasks/docs/creating-appengine-handlers).
  * Learn more about tasks in the [RPC API reference](https://docs.cloud.google.com/tasks/docs/reference/rpc).
  * Learn more about tasks in the [REST API reference](https://docs.cloud.google.com/tasks/docs/reference/rest). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
