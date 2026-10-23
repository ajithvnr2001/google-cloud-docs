---
url: https://docs.cloud.google.com/tasks/docs/samples/cloud-tasks-app-create-task/
title: Create an HTTP task within an App Engine app \u00a0|\u00a0 Cloud Tasks \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:58:47.150364+00:00
---

# Create an HTTP task within an App Engine app  |  Cloud Tasks  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tasks/docs/samples/cloud-tasks-app-create-task/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Tasks ](https://docs.cloud.google.com/tasks/docs)
  * [ Samples ](https://docs.cloud.google.com/tasks/docs/samples)



#  Create an HTTP task within an App Engine app Stay organized with collections  Save and categorize content based on your preferences. 

Creates an HTTP task within an App Engine application to trigger a Cloud Function.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Trigger Cloud Run functions using Cloud Tasks](https://docs.cloud.google.com/tasks/docs/tutorial-gcf)



## Code sample

### Node.js

To learn how to install and use the client library for Cloud Tasks, see [Cloud Tasks client libraries](https://docs.cloud.google.com/tasks/docs/reference/libraries). For more information, see the [Cloud Tasks Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/tasks/latest). 

To authenticate to Cloud Tasks, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const MAX_SCHEDULE_LIMIT = 30 * 60 * 60 * 24; // Represents 30 days in seconds.
    
    const createHttpTaskWithToken = async function (
      project = 'my-project-id', // Your GCP Project id
      queue = 'my-queue', // Name of your Queue
      location = 'us-central1', // The GCP region of your queue
      url = 'https://example.com/taskhandler', // The full url path that the request will be sent to
      email = '<member>@<project-id>.iam.gserviceaccount.com', // Cloud IAM service account
      payload = 'Hello, World!', // The task HTTP request body
      date = new Date() // Intended date to schedule task
    ) {
      // Imports the Google Cloud Tasks library.
      const {v2beta3} = require('[@google-cloud/tasks](https://docs.cloud.google.com/nodejs/docs/reference/tasks/latest/overview.html)');
    
      // Instantiates a client.
      const client = new v2beta3.[CloudTasksClient](https://docs.cloud.google.com/nodejs/docs/reference/tasks/latest/tasks/v2beta3.cloudtasksclient.html)();
    
      // Construct the fully qualified queue name.
      const parent = client.queuePath(project, location, queue);
    
      // Convert message to buffer.
      const convertedPayload = JSON.stringify(payload);
      const body = Buffer.from(convertedPayload).toString('base64');
    
      const task = {
        httpRequest: {
          httpMethod: 'POST',
          url,
          oidcToken: {
            serviceAccountEmail: email,
            audience: url,
          },
          headers: {
            'Content-Type': 'application/json',
          },
          body,
        },
      };
    
      const convertedDate = new Date(date);
      const currentDate = new Date();
    
      // Schedule time can not be in the past.
      if (convertedDate < currentDate) {
        console.error('Scheduled date in the past.');
      } else if (convertedDate > currentDate) {
        const date_diff_in_seconds = (convertedDate - currentDate) / 1000;
        // Restrict schedule time to the 30 day maximum.
        if (date_diff_in_seconds > MAX_SCHEDULE_LIMIT) {
          console.error('Schedule time is over 30 day maximum.');
        }
        // Construct future date in Unix time.
        const date_in_seconds =
          Math.min(date_diff_in_seconds, MAX_SCHEDULE_LIMIT) + Date.now() / 1000;
        // Add schedule time to request in Unix time using Timestamp structure.
        // https://googleapis.dev/nodejs/tasks/latest/google.protobuf.html#.Timestamp
        task.scheduleTime = {
          seconds: date_in_seconds,
        };
      }
    
      try {
        // Send create task request.
        const [response] = await client.createTask({parent, task});
        console.log(`Created task ${response.name}`);
        return response.name;
      } catch (error) {
        // Construct error for Stackdriver Error Reporting
        console.error(Error(error.message));
      }
    };
    
    module.exports = createHttpTaskWithToken;

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudtasks). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
