---
url: https://docs.cloud.google.com/tasks/docs/samples/cloud-tasks-enqueue/
title: Create App Engine tasks when migrating push queues \u00a0|\u00a0 Cloud Tasks \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:33.233598+00:00
---

# Create App Engine tasks when migrating push queues  |  Cloud Tasks  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tasks/docs/samples/cloud-tasks-enqueue/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Tasks ](https://docs.cloud.google.com/tasks/docs)
  * [ Samples ](https://docs.cloud.google.com/tasks/docs/samples)



#  Create App Engine tasks when migrating push queues Stay organized with collections  Save and categorize content based on your preferences. 

Creates App Engine tasks when migrating push queue code from App Engine task queues to Cloud Tasks.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Migrate push queues to Cloud Tasks (Java)](https://docs.cloud.google.com/appengine/migration-center/standard/java/migrating-push-queues)



## Code sample

### Java

To learn how to install and use the client library for Cloud Tasks, see [Cloud Tasks client libraries](https://docs.cloud.google.com/tasks/docs/reference/libraries). For more information, see the [Cloud Tasks Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/overview). 

To authenticate to Cloud Tasks, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudtasks). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
