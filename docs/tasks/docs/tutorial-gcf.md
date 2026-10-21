---
url: https://docs.cloud.google.com/tasks/docs/tutorial-gcf/
title: Trigger Cloud Run functions using Cloud Tasks \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:45.119514+00:00
---

# Trigger Cloud Run functions using Cloud Tasks  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tasks/docs/tutorial-gcf/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Tasks ](https://docs.cloud.google.com/tasks/docs)
  * [ Guides ](https://docs.cloud.google.com/tasks/docs/dual-overview)



Send feedback 

#  Trigger Cloud Run functions using Cloud Tasks Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial shows you how to use Cloud Tasks within an App Engine application to trigger a Cloud Run function and send a scheduled email.

## Objectives

  * Understand the code in each of the components.
  * Create a SendGrid account.
  * Download the source code.
  * Deploy a Cloud Run function to receive Cloud Tasks requests and send an email via the SendGrid API.
  * Create a Cloud Tasks queue.
  * Create a service account to authenticate your Cloud Tasks requests.
  * Deploy the client code that allows a user to send an email.



## Costs

Cloud Tasks, Cloud Run functions, and App Engine have a free tier, so as long as you are running the tutorial within the free tier of the given products it should not result in additional costs. For more information, see [Pricing](https://docs.cloud.google.com/free/docs/gcp-free-tier).

## Before you begin

  1. Select or create a Google Cloud project.

**Note:** If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to the App Engine page](https://console.cloud.google.com/projectselector/appengine/create)

  2. Initialize an App Engine application in your project:

     1. On the **Welcome to App Engine** page click **Create Application**.

     2. Select a region for your application. This location will serve as the `LOCATION_ID` parameter for your Cloud Tasks requests, so make a note of it. Note that two locations, called europe-west and us-central in App Engine commands, are called, respectively, europe-west1 and us-central1 in Cloud Tasks commands.

     3. Select **Node.js** for the language and **Standard** for the environment.

     4. If the **Enable billing** popup appears, select your billing account. If you do not currently have a billing account, click **Create billing account** and follow the wizard.

     5. On the **Get started** page, click **Next**. You'll take care of this later.

  3. Enable the Cloud Run functions and Cloud Tasks APIs.

[Enable the apis](https://console.cloud.google.com/apis/enableflow?apiid=cloudfunctions.googleapis.com,cloudtasks.googleapis.com)

  4. Install and initialize the [gcloud CLI](https://docs.cloud.google.com/sdk/docs/downloads-interactive).




## Understanding the code

This section walks you through the app's code and explains how it works.

### Creating the task

The index page is served using handlers in the `app.yaml`. The variables needed for task creation are passed in as environment variables.
    
    
    runtime: nodejs16
    
    env_variables:
      QUEUE_NAME: "my-queue"
      QUEUE_LOCATION: "us-central1"
      FUNCTION_URL: "https://<region>-<project_id>.cloudfunctions.net/sendEmail"
      SERVICE_ACCOUNT_EMAIL: "<member>@<project_id>.iam.gserviceaccount.com"
    
    # Handlers for serving the index page.
    handlers:
      - url: /static
        static_dir: static
      - url: /
        static_files: index.html
        upload: index.html

This code creates the endpoint `/send-email`. This endpoint handles form submissions from the index page and passes that data to the task creation code.
    
    
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

This code actually creates the task and sends it on to the Cloud Tasks queue. The code builds the task by:

  * Specifying the [target type](https://docs.cloud.google.com/tasks/docs/dual-overview#http) as `HTTP Request`.

  * Specifying the [`HTTP method`](https://docs.cloud.google.com/tasks/docs/reference/rest/v2beta3/projects.locations.queues.tasks#httpmethod) to be used and the `URL` of the target.

  * Setting the `Content-Type` header to `application/json` so downstream applications can parse the structured payload.

  * Adding a [service account email](https://docs.cloud.google.com/tasks/docs/creating-http-target-tasks#token) so that Cloud Tasks can provide credentials to the request target, which requires authentication. The service account is created separately.

  * Checking to make sure the user input for date is within the 30 days maximum and adding it to the request as field `scheduleTime`.



    
    
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

### Creating the email

This code creates the Cloud Run function that is the target for the Cloud Tasks request. It uses the request body to construct an email and send it via the SendGrid API.
    
    
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

## Preparing the application

### Setting up SendGrid

  1. Create a SendGrid account.

     * You can either do this manually via the [SendGrid website](https://sendgrid.com/free)
     * or you can use the [Google Cloud Launcher](https://cloud.google.com/launcher), which will create an account for you and integrate billing. See [Creating a SendGrid account using Cloud Launcher](https://cloud.google.com/launcher/solution/sendgrid-app/sendgrid-email).
  2. Create a SendGrid API key:

     1. Log in to your [SendGrid account](https://app.sendgrid.com).

     2. In the left hand navigation open **Settings** and click **API Keys**.

     3. Click **Create API Key** and select restricted access. Under the **Mail Send** header, select **Full Access**.

     4. Copy the API Key when it is displayed (you will only see this once, make sure you paste it somewhere so you can use it later on).




### Downloading the source code

  1. Clone the sample app repository to your local machine:
         
         git clone https://github.com/GoogleCloudPlatform/nodejs-docs-samples.git
         

  2. Change to the directory that contains the sample code:
         
         cd cloud-tasks/
         




## Deploying the Cloud Run function

  1. Navigate to the `function/` directory:
         
         cd function/
         

  2. Deploy the function:
         
         gcloud functions deploy sendEmail --runtime nodejs14 --trigger-http \
           --no-allow-unauthenticated \
           --set-env-vars SENDGRID_API_KEY=SENDGRID_API_KEY \

Replace `SENDGRID_API_KEY` with your API key.

This command uses flags:

     * `--trigger-http` to specify the Cloud Run functions trigger type.

     * `--no-allow-unauthenticated` to specify the function invocation requires authentication.

     * `--set-env-var` to set your SendGrid credentials

**Note:** You can manage Cloud Run functions from both the Firebase and Google Cloud console. Writing and deploying from the FirebaseUI can be replicated; however the function code needs to match the Firebase functions framework. Learn more about [getting started](https://firebase.google.com/docs/functions/get-started) with Firebase functions and [HTTP triggers](https://firebase.google.com/docs/functions/http-events).
  3. Set access control for the function to only allow authenticated users.

     1. Select the `sendEmail` function in the [Cloud Run functions UI](https://console.cloud.google.com/functions).

     2. If you don't see permissions info for `sendEmail`, click **SHOW INFO PANEL** in the upper right hand corner.

     3. Click the **Add principals** button above.

     4. Set **New principals** to `allAuthenticatedUsers`.

     5. Set the **Role**.

        * **First generation (1st gen) functions:** set the role to `Cloud Function Invoker`
        * **Second generation (2nd gen) functions:** set the role to `Cloud Run Invoker`
     6. Click **SAVE**.




## Creating a Cloud Tasks queue

  1. [Create a queue](https://docs.cloud.google.com/tasks/docs/creating-queues) using the following `gcloud` command:
         
         gcloud tasks queues create my-queue --location=LOCATION

Replace `LOCATION` with your preferred [location](https://cloud.google.com/about/locations) for the queue, for example, `us-west2`. If you do not specify the location, the gcloud CLI picks the default.

  2. Verify that it was created successfully:
         
         gcloud tasks queues describe my-queue --location=LOCATION

Replace `LOCATION` with the location of the queue.




## Creating a service account

The Cloud Tasks request must provide credentials in the `Authorization` header for the Cloud Run function to authenticate the request. This service account allows [Cloud Tasks](https://docs.cloud.google.com/tasks/docs/creating-http-target-tasks#token) to create and add an OIDC token for that purpose.

  1. In the [Service accounts UI](https://console.cloud.google.com/iam-admin/serviceaccounts), click **+CREATE SERVICE ACCOUNT**.

  2. Add a [service account name](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts)(friendly display name) and select **create**.

  3. Set the **Role** and click **Continue**.

     * **First generation (1st gen) functions:** set the role to `Cloud Function Invoker`
     * **Second generation (2nd gen) functions:** set the role to `Cloud Run Invoker`
  4. Select **Done**.




## Deploying the endpoint and the task creator to App Engine

  1. Navigate to `app/` directory:
         
         cd ../app/
         

  2. Update variables in the `app.yaml` with your values:
         
         env_variables:
           QUEUE_NAME: "my-queue"
           QUEUE_LOCATION: "us-central1"
           FUNCTION_URL: "https://<region>-<project_id>.cloudfunctions.net/sendEmail"
           SERVICE_ACCOUNT_EMAIL: "<member>@<project_id>.iam.gserviceaccount.com"

To find your queue location, use the following command:
         
         gcloud tasks queues describe my-queue --location=LOCATION

Replace `LOCATION` with the location of the queue.

To find your function URL, use the following command:
         
         gcloud functions describe sendEmail

  3. Deploy the application to the App Engine standard environment, using the following command:
         
         gcloud app deploy

  4. Open the application to send a postcard as an email:
         
         gcloud app browse




## Clean up

After you finish the tutorial, you can clean up the resources that you created so that they stop using quota and incurring charges. The following sections describe how to delete or turn off these resources. 

### Deleting Resources

You can clean up the resources that you created on Google Cloud so they won't take up quota and you won't be billed for them in the future. The following sections describe how to delete or turn off these resources.

**Note:** The only way you can delete the default version of your App Engine app is by deleting your project.

#### Delete the Cloud Run function

  1. Go to the **Cloud Run functions** page in the Google Cloud console.

[Go to the Cloud Run functions page](https://console.cloud.google.com/functions).

  2. Click the checkboxes next to your functions.

  3. Click the **Delete** button at the top of the page and confirm your delete.




#### Delete the Cloud Tasks queue

  1. Open the Cloud Tasks queues page in the console.

[Go to the Cloud Tasks queues page](https://console.cloud.google.com/cloudtasks?tab=push)

  2. Select the name of the queue you want to delete and click **Delete queue**.

  3. Confirm the action.

**Note:** If you delete a queue from the Google Cloud console, you must wait 7 days before recreating with the same name.



### Deleting the project

The easiest way to eliminate billing is to delete the project that you created for the tutorial. 

To delete the project: 

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



## What's next

  * Learn more about [creating HTTP target tasks programmatically](https://docs.cloud.google.com/tasks/docs/creating-http-target-tasks).
  * Learn more about [configuring your Cloud Tasks queue](https://docs.cloud.google.com/tasks/docs/creating-queues#configuring_your_queue).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
