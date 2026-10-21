---
url: https://docs.cloud.google.com/tasks/docs/samples/cloud-tasks-app/
title: Create tasks from App Engine app \u00a0|\u00a0 Cloud Tasks \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:22.518105+00:00
---

# Create tasks from App Engine app  |  Cloud Tasks  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tasks/docs/samples/cloud-tasks-app/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Tasks ](https://docs.cloud.google.com/tasks/docs)
  * [ Samples ](https://docs.cloud.google.com/tasks/docs/samples)



#  Create tasks from App Engine app Stay organized with collections  Save and categorize content based on your preferences. 

App Engine app for tutorial: Using Cloud Tasks to trigger Cloud Functions.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Trigger Cloud Run functions using Cloud Tasks](https://docs.cloud.google.com/tasks/docs/tutorial-gcf)



## Code sample

### Node.js

To learn how to install and use the client library for Cloud Tasks, see [Cloud Tasks client libraries](https://docs.cloud.google.com/tasks/docs/reference/libraries). For more information, see the [Cloud Tasks Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/tasks/latest). 

To authenticate to Cloud Tasks, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    app.post('/send-email', (req, res) => {
      // Set the task payload to the form submission.
      const {to_name, from_name, to_email, date} = req.body;
      const payload = {to_name, from_name, to_email};
    
      createHttpTaskWithToken(
        process.env.GOOGLE_CLOUD_PROJECT,
        QUEUE_NAME,
        QUEUE_LOCATION,
        FUNCTION_URL,
        SERVICE_ACCOUNT_EMAIL,
        payload,
        date
      );
    
      res.status(202).send('📫 Your postcard is in the mail! 💌');
    });

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudtasks). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
