---
url: https://docs.cloud.google.com/tasks/docs/samples/cloud-tasks-func/
title: Use task handler to trigger Cloud Functions \u00a0|\u00a0 Cloud Tasks \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:58:45.356981+00:00
---

# Use task handler to trigger Cloud Functions  |  Cloud Tasks  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tasks/docs/samples/cloud-tasks-func/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Tasks ](https://docs.cloud.google.com/tasks/docs)
  * [ Samples ](https://docs.cloud.google.com/tasks/docs/samples)



#  Use task handler to trigger Cloud Functions Stay organized with collections  Save and categorize content based on your preferences. 

Uses Cloud Tasks to trigger Cloud Functions.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Trigger Cloud Run functions using Cloud Tasks](https://docs.cloud.google.com/tasks/docs/tutorial-gcf)



## Code sample

### Node.js

To learn how to install and use the client library for Cloud Tasks, see [Cloud Tasks client libraries](https://docs.cloud.google.com/tasks/docs/reference/libraries). For more information, see the [Cloud Tasks Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/tasks/latest). 

To authenticate to Cloud Tasks, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const sendgrid = require('@sendgrid/mail');
    
    /**
     * Responds to an HTTP request from Cloud Tasks and sends an email using data
     * from the request body.
     *
     * @param {object} req Cloud Function request context.
     * @param {object} req.body The request payload.
     * @param {string} req.body.to_email Email address of the recipient.
     * @param {string} req.body.to_name Name of the recipient.
     * @param {string} req.body.from_name Name of the sender.
     * @param {object} res Cloud Function response context.
     */
    exports.sendEmail = async (req, res) => {
      // Get the SendGrid API key from the environment variable.
      const key = process.env.SENDGRID_API_KEY;
      if (!key) {
        const error = new Error(
          'SENDGRID_API_KEY was not provided as environment variable.'
        );
        error.code = 401;
        throw error;
      }
      sendgrid.setApiKey(key);
    
      // Get the body from the Cloud Task request.
      const {to_email, to_name, from_name} = req.body;
      if (!to_email) {
        const error = new Error('Email address not provided.');
        error.code = 400;
        throw error;
      } else if (!to_name) {
        const error = new Error('Recipient name not provided.');
        error.code = 400;
        throw error;
      } else if (!from_name) {
        const error = new Error('Sender name not provided.');
        error.code = 400;
        throw error;
      }
    
      // Construct the email request.
      const msg = {
        to: to_email,
        from: 'postcard@example.com',
        subject: 'A Postcard Just for You!',
        html: postcardHTML(to_name, from_name),
      };
    
      try {
        await sendgrid.send(msg);
        // Send OK to Cloud Task queue to delete task.
        res.status(200).send('Postcard Sent!');
      } catch (error) {
        // Any status code other than 2xx or 503 will trigger the task to retry.
        res.status(error.code).send(error.message);
      }
    };

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudtasks). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
