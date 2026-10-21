---
url: https://docs.cloud.google.com/run/docs/triggering/using-tasks/
title: Executing asynchronous tasks \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:02:01.989475+00:00
---

# Executing asynchronous tasks  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/triggering/using-tasks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Executing asynchronous tasks Stay organized with collections  Save and categorize content based on your preferences. 

You can use Cloud Tasks to securely enqueue a task to be asynchronously processed by a Cloud Run service. Typical use cases include:

  * Preserving requests through unexpected production incidents
  * Smoothing traffic spikes by delaying work that is not user-facing
  * Speeding user response time by delegating slow background operations to be handled by another service, such as database updates or batch processing
  * Limiting the call rate to backing services like databases and third-party APIs



This page shows how to enqueue tasks that are securely pushed via the HTTPS protocol to a private Cloud Run service. It describes required behavior for the private Cloud Run service, required service account permissions, task queue creation, and task creation.

## Before you start

[Enable the Cloud Tasks API](https://console.cloud.google.com/apis/library/cloudtasks.googleapis.com/?q=cloud%20tasks) on the project you are using.

## Deploying a Cloud Run service to handle tasks

To deploy a service that accepts tasks sent to the task queue, [deploy the service](https://docs.cloud.google.com/run/docs/deploying) in the same way as any other Cloud Run service. The Cloud Run service must return an HTTP `200` code to confirm success after processing of the task is complete.

Tasks will be pushed to this Cloud Run service as HTTPS requests by Cloud Tasks.

The response to Cloud Tasks must occur within its configured [timeout](https://docs.cloud.google.com/tasks/docs/creating-http-target-tasks#handler). For workloads that need to run longer than the maximum Cloud Tasks timeout, consider using [Cloud Run jobs](https://docs.cloud.google.com/run/docs/create-jobs).

## Creating a task queue

###  Command line

To create a task queue, use the command
    
    
    gcloud tasks queues create QUEUE-ID

replacing QUEUE-ID with the name you want to give to your task queue: it must be unique in your project. If you are prompted to create an App Engine app in your project, respond `y` to create it. Cloud Tasks uses this for the queue: make sure you choose the same location as you are using for your Cloud Run service.

The default task queue configuration should work in most cases. However, you can optionally set different [rate limits](https://docs.cloud.google.com/tasks/docs/configuring-queues#rate) and [retry parameters](https://docs.cloud.google.com/tasks/docs/configuring-queues#retry) if you want.

### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

To create a task queue, add the following to your `.tf` file:
    
    
    resource "google_cloud_tasks_queue" "default" {
      name     = "cloud-tasks-queue-name"
      location = "us-central1"
    }

Apply the changes by entering `terraform apply`.

## Creating a service account to associate with the tasks

You must create a service account that will be associated with the enqueued tasks. This service account must have the Cloud Run Invoker IAM role to allow the task queue to push tasks to the Cloud Run service. .

### Console

  1. In the Google Cloud console, go to the **Service Accounts** page.

[Go to Service Accounts](https://console.cloud.google.com/projectselector/iam-admin/serviceaccounts/create?supportedpurview=project)

  2. Select a project.

  3. Enter a service account name to display in the Google Cloud console.

The Google Cloud console generates a service account ID based on this name. Edit the ID if necessary. You cannot change the ID later.

  4. Optional: Enter a description of the service account.

  5. Click **Create and continue**.

  6. Optional: Click the **Select a role** field.

  7. Select **Cloud Run** > **Cloud Run Invoker**.

  8. Click **Done**.




###  Command line

  1. Create the service account:
         
         gcloud iam service-accounts create SERVICE_ACCOUNT_NAME \
            --display-name "DISPLAYED_SERVICE_ACCOUNT_NAME"

Replace

     * SERVICE_ACCOUNT_NAME with a **lower case** name unique within your Google Cloud project, for example `my-invoker-service-account-name`.
     * DISPLAYED_SERVICE_ACCOUNT_NAME with the name you want to display for this service account, for example, in the console, for example, `My Invoker Service Account`.
  2. For Cloud Run, give your service account permission to invoke your service:
         
         gcloud run services add-iam-policy-binding SERVICE \
            --member=serviceAccount:SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com \
            --role=roles/run.invoker

Replace

     * SERVICE with the name of the service you want to be invoked by Cloud Tasks.
     * SERVICE_ACCOUNT_NAME with the name of the service account.
     * PROJECT_ID with your Google Cloud project ID.
  3. Grant your service account access to the project so that it has permission to complete specific actions on the resources in your project:
         
         gcloud projects add-iam-policy-binding RESOURCE_ID \
            --member=PRINCIPAL --role=roles/run.invoker

Replace

     * RESOURCE_ID: Your Google Cloud project ID.

     * PRINCIPAL: An identifier for the principal, or member, which usually has the following form: PRINCIPAL_TYPE:ID. For example, `user:my-user@example.com`. For a full list of the values that PRINCIPAL can have, see the [Policy Binding reference](https://docs.cloud.google.com/iam/docs/reference/rest/v1/Policy#Binding).




### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

Add the following to your `.tf` file:

Create the service account:
    
    
    resource "google_service_account" "default" {
      account_id   = "cloud-run-task-invoker"
      display_name = "Cloud Run Task Invoker"
    }

For Cloud Run, give your service account permission to invoke your service:
    
    
    resource "google_cloud_run_service_iam_binding" "default" {
      location = google_cloud_run_v2_service.default.location
      service  = google_cloud_run_v2_service.default.name
      role     = "roles/run.invoker"
      members  = ["serviceAccount:${google_service_account.default.email}"]
    }

Apply the changes by entering `terraform apply`.

## Creating HTTP tasks with authentication tokens

When you create a task to send to the task queue, you specify the project, the location, queue name, the email of the previously created service account to associate with tasks, the URL of the private Cloud Run service that will run the task, and any other data you need to send. You can choose to hardcode these values, though values like the project ID, location, and service account email can be [dynamically retrieved](https://docs.cloud.google.com/compute/docs/metadata/querying-metadata) from the [Cloud Run metadata server](https://docs.cloud.google.com/run/docs/container-contract#metadata-server).

Refer to the Cloud Tasks API documentation for details on the [task request body](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations.queues.tasks#Task). Note that requests that contain data payloads must use the HTTP `PUT` or `POST` method.

The code that enqueues the tasks must have the necessary IAM permissions to do so, such as the Cloud Tasks Enqueuer role. Your code will have the necessary IAM permissions if you use the default service account on Cloud Run.

The following examples create task requests that also include the creation of a header token. OIDC tokens are used in the examples. To use an OAuth token, replace the OIDC parameter with the language appropriate OAuth parameter in constructing the request.

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
    

## What's next

  * [Logging and viewing logs](https://docs.cloud.google.com/run/docs/logging)
  * [Monitoring health and performance](https://docs.cloud.google.com/run/docs/monitoring)
  * [Triggering from Pub/Sub](https://docs.cloud.google.com/run/docs/triggering/pubsub-push)
  * [Invoking with HTTPS](https://docs.cloud.google.com/run/docs/triggering/https-request)
  * [Running services on a schedule](https://docs.cloud.google.com/run/docs/triggering/using-scheduler)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
