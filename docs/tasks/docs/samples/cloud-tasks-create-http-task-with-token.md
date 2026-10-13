---
url: https://docs.cloud.google.com/tasks/docs/samples/cloud-tasks-create-http-task-with-token/
title: Create HTTP tasks with authentication \u00a0|\u00a0 Cloud Tasks \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:38:37.285017+00:00
---

# Create HTTP tasks with authentication  |  Cloud Tasks  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tasks/docs/samples/cloud-tasks-create-http-task-with-token/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Tasks ](https://docs.cloud.google.com/tasks/docs)
  * [ Samples ](https://docs.cloud.google.com/tasks/docs/samples)



#  Create HTTP tasks with authentication Stay organized with collections  Save and categorize content based on your preferences. 

Creates tasks with OIDC token to send to a Cloud Run, Cloud Function, or external URL.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create HTTP target tasks programmatically](https://docs.cloud.google.com/tasks/docs/creating-http-target-tasks)
  * [Executing asynchronous tasks](https://docs.cloud.google.com/run/docs/triggering/using-tasks)



## Code sample

### Go

To learn how to install and use the client library for Cloud Tasks, see [Cloud Tasks client libraries](https://docs.cloud.google.com/tasks/docs/reference/libraries). For more information, see the [Cloud Tasks Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudtasks/latest/apiv2). 

To authenticate to Cloud Tasks, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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
    

### Java

To learn how to install and use the client library for Cloud Tasks, see [Cloud Tasks client libraries](https://docs.cloud.google.com/tasks/docs/reference/libraries). For more information, see the [Cloud Tasks Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/overview). 

To authenticate to Cloud Tasks, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

### Node.js

To learn how to install and use the client library for Cloud Tasks, see [Cloud Tasks client libraries](https://docs.cloud.google.com/tasks/docs/reference/libraries). For more information, see the [Cloud Tasks Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/tasks/latest). 

To authenticate to Cloud Tasks, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

### PHP

To learn how to install and use the client library for Cloud Tasks, see [Cloud Tasks client libraries](https://docs.cloud.google.com/tasks/docs/reference/libraries). For more information, see the [Cloud Tasks PHP API reference documentation](https://docs.cloud.google.com/php/docs/reference/cloud-tasks/latest). 

To authenticate to Cloud Tasks, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Tasks\V2\Client\CloudTasksClient;
    use Google\Cloud\Tasks\V2\CreateTaskRequest;
    use Google\Cloud\Tasks\V2\HttpMethod;
    use Google\Cloud\Tasks\V2\HttpRequest;
    use Google\Cloud\Tasks\V2\OidcToken;
    use Google\Cloud\Tasks\V2\Task;
    
    /** Uncomment and populate these variables in your code */
    // $projectId = 'The Google project ID';
    // $locationId = 'The Location ID';
    // $queueId = 'The Cloud Tasks Queue ID';
    // $url = 'The full url path that the task request will be sent to.';
    // $serviceAccountEmail = 'The Cloud IAM service account to be used at the construction of the token';
    // $payload = 'The payload your task should carry to the task handler. Optional';
    
    // Instantiate the client and queue name.
    $client = new CloudTasksClient();
    $queueName = $client->queueName($projectId, $locationId, $queueId);
    
    // Add your service account email to construct the OIDC token
    // in order to add an authentication header to the request.
    $oidcToken = new OidcToken();
    $oidcToken->setServiceAccountEmail($serviceAccountEmail);
    
    // Create an Http Request Object.
    $httpRequest = new HttpRequest();
    // The full url path that the task request will be sent to.
    $httpRequest->setUrl($url);
    // POST is the default HTTP method, but any HTTP method can be used.
    $httpRequest->setHttpMethod(HttpMethod::POST);
    //The oidcToken used to assert identity.
    $httpRequest->setOidcToken($oidcToken);
    // Setting a body value is only compatible with HTTP POST and PUT requests.
    if (isset($payload)) {
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
    
    
    from typing import Optional
    
    from google.cloud import tasks_v2
    
    
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
        client = tasks_v2.[CloudTasksClient](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2.services.cloud_tasks.CloudTasksClient.html)()
    
        # Construct the request body.
        task = tasks_v2.[Task](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2.types.Task.html)(
            http_request=tasks_v2.[HttpRequest](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2.types.HttpRequest.html)(
                http_method=tasks_v2.[HttpMethod](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2.types.HttpMethod.html).POST,
                url=url,
                oidc_token=tasks_v2.[OidcToken](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2.types.OidcToken.html)(
                    service_account_email=service_account_email,
                    audience=audience,
                ),
                body=payload,
            ),
        )
    
        # Use the client to build and send the task.
        return client.[create_task](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2.services.cloud_tasks.CloudTasksClient.html#google_cloud_tasks_v2_services_cloud_tasks_CloudTasksClient_create_task)(
            tasks_v2.[CreateTaskRequest](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2.types.CreateTaskRequest.html)(
                parent=client.[queue_path](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2.services.cloud_tasks.CloudTasksClient.html#google_cloud_tasks_v2_services_cloud_tasks_CloudTasksClient_queue_path)(project, location, queue),
                task=task,
            )
        )
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudtasks). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
