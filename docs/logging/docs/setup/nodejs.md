---
url: https://docs.cloud.google.com/logging/docs/setup/nodejs/
title: Setting Up Cloud Logging for Node.js \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:16:58.147436+00:00
---

# Setting Up Cloud Logging for Node.js  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/setup/nodejs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Guides ](https://docs.cloud.google.com/logging/docs/overview)



Send feedback 

#  Setting Up Cloud Logging for Node.js Stay organized with collections  Save and categorize content based on your preferences. 

For Node.js applications, plugins are maintained for the popular [Winston](https://github.com/winstonjs/winston) and [Bunyan](https://github.com/trentm/node-bunyan) logging libraries. Winston is a general-purpose library, implementing a variety of log formatters and transports. [Bunyan](https://github.com/trentm/node-bunyan), which is specialized for structured JSON logs, supports log formatting by piping to the Bunyan command line.

You can also use the Logging client library for Node.js directly, or create your own integrations with your preferred logging library. For example, you can use the [Pino log framework](https://getpino.io/#/) example.

> The Logging agent doesn't have to be installed to use the Winston or Bunyan on a Compute Engine virtual machine (VM) instance.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Cloud Logging API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=logging.googleapis.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Cloud Logging API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=logging.googleapis.com)

  8. Prepare your environment for Node.js development. 

[ Go to the Node.js setup guide ](https://docs.cloud.google.com/nodejs/docs/setup)




## Configure logging

This section describes how to install and configure the plugins for the [Winston](https://github.com/winstonjs/winston) and [Bunyan](https://github.com/trentm/node-bunyan) logging libraries. For Bunyan, information is provided about how to use Bunyan with a Node.js Express application.

You can use other libraries or frameworks. For example, you can use the [Pino log framework](https://getpino.io/#/). For sample code that uses OpenTelemetry to collect metrics and trace data, and the Pino log framework to collect log data, see [Node.js instrumentation sample](https://docs.cloud.google.com/stackdriver/docs/instrumentation/setup/nodejs). If you use Pino, then you must implement a mapping between the Pino severity levels and those used by Cloud Logging. For example code, see [Mapping Pino Log Levels](https://getpino.io/#/docs/help?id=stackdriver).

### Install and configure the Winston plugin

Cloud Logging provides a plugin for the [Winston](https://github.com/winstonjs/winston) Node.js Logging library. The Logging plugin for Winston provides a simpler, higher-level layer for working with Logging.

To install and configure the Winston plugin, do the following:

  1. To install the Logging Winston plugin, use [npm](https://www.npmjs.com/):
         
         npm install @google-cloud/logging-winston winston

  2. Import the plugin and add it to your Winston configuration:
         
         const winston = require('winston');
         
         // Imports the Google Cloud client library for Winston
         const {LoggingWinston} = require('[@google-cloud/logging-winston](https://docs.cloud.google.com/nodejs/docs/reference/logging-winston/latest/overview.html)');
         
         const loggingWinston = new [LoggingWinston](https://docs.cloud.google.com/nodejs/docs/reference/logging-winston/latest/logging-winston/loggingwinston.html)();
         
         // Create a Winston logger that streams to Cloud Logging
         // Logs will be written to: "projects/YOUR_PROJECT_ID/logs/winston_log"
         const logger = winston.createLogger({
           level: 'info',
           transports: [
             new winston.transports.Console(),
             // Add Cloud Logging
             loggingWinston,
           ],
         });
         
         // Writes some log entries
         logger.error('warp nacelles offline');
         logger.info('shields at 99%');

  3. Configure your plugin.

You can customize the behavior of the Winston plugin using the same configuration options supported by the [Cloud Logging API Cloud client library for Node.js](https://docs.cloud.google.com/logging/docs/reference/libraries). These options can be passed in the `options` object passed to the plugin's constructor.




### Install and configure the Bunyan plugin

Cloud Logging provides a plugin for the [Bunyan](https://github.com/trentm/node-bunyan) Node.js Logging library. The Logging plugin for Bunyan provides a simpler, higher-level layer for working with Logging.

To install and configure the Bunyan plugin, do the following:

  1. To install the Logging Bunyan plugin, use [npm](https://www.npmjs.com/):
         
         npm install bunyan @google-cloud/logging-bunyan

  2. Import the plugin and add it to your Bunyan configuration:
         
         const bunyan = require('bunyan');
         
         // Imports the Google Cloud client library for Bunyan
         const {LoggingBunyan} = require('[@google-cloud/logging-bunyan](https://docs.cloud.google.com/nodejs/docs/reference/logging-bunyan/latest/overview.html)');
         
         // Creates a Bunyan Cloud Logging client
         const loggingBunyan = new [LoggingBunyan](https://docs.cloud.google.com/nodejs/docs/reference/logging-bunyan/latest/logging-bunyan/loggingbunyan.html)();
         
         // Create a Bunyan logger that streams to Cloud Logging
         // Logs will be written to: "projects/YOUR_PROJECT_ID/logs/bunyan_log"
         const logger = bunyan.createLogger({
           // The JSON payload of the log as it appears in Cloud Logging
           // will contain "name": "my-service"
           name: 'my-service',
           streams: [
             // Log to the console at 'info' and above
             {stream: process.stdout, level: 'info'},
             // And log to Cloud Logging, logging at 'info' and above
             loggingBunyan.[stream](https://docs.cloud.google.com/nodejs/docs/reference/logging-bunyan/latest/logging-bunyan/loggingbunyan.html)('info'),
           ],
         });
         
         // Writes some log entries
         [logger](https://docs.cloud.google.com/nodejs/docs/reference/logging-bunyan/latest/logging-bunyan/express.middlewarereturntype.html).error('warp nacelles offline');
         [logger](https://docs.cloud.google.com/nodejs/docs/reference/logging-bunyan/latest/logging-bunyan/express.middlewarereturntype.html).info('shields at 99%');

  3. Configure your plugin.

You can customize the behavior of the Bunyan plugin using the same configuration options supported by the [Cloud Logging API Cloud client library for Node.js](https://docs.cloud.google.com/logging/docs/reference/libraries). These options can be passed in the `options` object passed to the plugin's constructor.




#### Use Bunyan and Express

You can set up and use Bunyan with Logging in a Node.js Express application.
    
    
    // Imports the Google Cloud client library for Bunyan.
    const lb = require('[@google-cloud/logging-bunyan](https://docs.cloud.google.com/nodejs/docs/reference/logging-bunyan/latest/overview.html)');
    
    // Import express module and create an http server.
    const express = require('express');
    
    async function startServer() {
      const {logger, mw} = await lb.express.[middleware](https://docs.cloud.google.com/nodejs/docs/reference/logging-bunyan/latest/overview.html)({
        logName: 'samples_express',
      });
      const app = express();
    
      // Install the logging middleware. This ensures that a Bunyan-style `log`
      // function is available on the `request` object. This should be the very
      // first middleware you attach to your app.
      app.use(mw);
    
      // Setup an http route and a route handler.
      app.get('/', (req, res) => {
        // `req.log` can be used as a bunyan style log method. All logs generated
        // using `req.log` use the current request context. That is, all logs
        // corresponding to a specific request will be bundled in the Stackdriver
        // UI.
        req.log.info('this is an info log message');
        res.send('hello world');
      });
    
      const port = process.env.PORT || 8080;
    
      // `logger` can be used as a global logger, one not correlated to any specific
      // request.
      [logger](https://docs.cloud.google.com/nodejs/docs/reference/logging-bunyan/latest/logging-bunyan/express.middlewarereturntype.html).info({port}, 'bonjour');
    
      // Start listening on the http server.
      const server = app.listen(port, () => {
        console.log(`http server listening on port ${port}`);
      });
    
      app.get('/shutdown', (req, res) => {
        res.sendStatus(200);
        server.close();
      });
    }
    
    startServer();

For more information on installation, see the [documentation](https://github.com/googleapis/nodejs-logging) for the Cloud Logging libraries for Node.js. You can also report issues using the [issue tracker](https://github.com/googleapis/nodejs-logging/issues).

## Write logs with the Cloud Logging client library

For information on using the Cloud Logging client library for Node.js directly, see [Cloud Logging Client Libraries](https://docs.cloud.google.com/logging/docs/reference/libraries).

## Run on Google Cloud

For an application to write logs by using the Cloud Logging libraries for Node.js, the service account for the underlying resource must have the [Logs Writer (`roles/logging.logWriter`)](https://docs.cloud.google.com/logging/docs/access-control#permissions_and_roles) [IAM](https://docs.cloud.google.com/iam/docs/understanding-roles) role. Most Google Cloud environments automatically configure the default service account to have this role.

### App Engine

Cloud Logging is automatically enabled for App Engine, and your app's [default service account](https://docs.cloud.google.com/appengine/docs/standard/nodejs/service-account) has the IAM permissions by default to write log entries.

To write log entries from your app, we recommend that you use Bunyan or Winston as described on this page.

For more information, see [Writing and viewing logs](https://docs.cloud.google.com/appengine/docs/standard/nodejs/writing-application-logs).

### Google Kubernetes Engine (GKE)

[GKE](https://docs.cloud.google.com/kubernetes-engine/docs) automatically grants the default service account the [Logs Writer (`roles/logging.logWriter`)](https://docs.cloud.google.com/logging/docs/access-control#permissions_and_roles) IAM role. If you use [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/workload-identity) with this default service account to let workloads access specific Google Cloud APIs, then no additional configuration is required. However, if you use Workload Identity Federation for GKE with a custom IAM service account, then ensure that the custom service account has the role of Logs Writer (`roles/logging.logWriter`).

If needed, you can also use the following command to add the `logging.write` access scope when creating the cluster:
    
    
    gcloud container clusters create example-cluster-name \
        --scopes https://www.googleapis.com/auth/logging.write
    

### Compute Engine

**Note:** To use the Cloud Logging libraries for Node.js on a **Compute Engine** VM instance, you do not need to install the Cloud Logging agent.

When using [Compute Engine](https://docs.cloud.google.com/compute/docs) VM instances, add the `cloud-platform` access scope to each instance. When creating a new instance through the Google Cloud console, you can do this in the **Identity and API access** section of the **Create Instance** panel. Use the Compute Engine default service account or another service account of your choice, and select **Allow full access to all Cloud APIs** in the **Identity and API access** section. Whichever service account you select, ensure that it has been granted the [Logs Writer role](https://docs.cloud.google.com/logging/docs/access-control#permissions_and_roles) in the **IAM & Admin** section of the Google Cloud console.

### Cloud Run functions

[Cloud Run functions](https://docs.cloud.google.com/functions/docs) grants the [Logs Writer role](https://docs.cloud.google.com/logging/docs/access-control#permissions_and_roles) by default.

The Cloud Logging libraries for Node.js can be used without needing to explicitly provide credentials.

Cloud Run functions is configured to use Cloud Logging automatically.

**Note:** Logs written to `stdout` and `stderr` are automatically sent to Cloud Logging for you, without needing to use the Cloud Logging libraries for Node.js. 

## Run locally and elsewhere

To use the Cloud Logging libraries for Node.js outside of Google Cloud, including running the library on your own workstation, on your data center's computers, or on the VM instances of another cloud provider, you must set up Application Default Credentials (ADC) in your local environment to authenticate to the Cloud Logging libraries for Node.js.

For more information, see [Set up ADC for on-premises or another cloud provider](https://docs.cloud.google.com/docs/authentication/set-up-adc-on-premises).

Use Winston: 
    
    
    // Imports the Google Cloud client library for Winston
    const {LoggingWinston} = require('[@google-cloud/logging-winston](https://docs.cloud.google.com/nodejs/docs/reference/logging-winston/latest/overview.html)');
    
    // Creates a client
    const loggingWinston = new [LoggingWinston](https://docs.cloud.google.com/nodejs/docs/reference/logging-winston/latest/logging-winston/loggingwinston.html)({
      projectId: 'your-project-id',
      keyFilename: '/path/to/key.json',
    });

Use Bunyan:
    
    
    // Imports the Google Cloud client library for Bunyan
    const {LoggingBunyan} = require('[@google-cloud/logging-bunyan](https://docs.cloud.google.com/nodejs/docs/reference/logging-bunyan/latest/overview.html)');
    
    // Creates a client
    const loggingBunyan = new [LoggingBunyan](https://docs.cloud.google.com/nodejs/docs/reference/logging-bunyan/latest/logging-bunyan/loggingbunyan.html)({
      projectId: 'your-project-id',
      keyFilename: '/path/to/key.json',
    });

## View the logs

In the Google Cloud console, go to the segment **Logs Explorer** page: 

[Go to **Logs Explorer**](https://console.cloud.google.com/logs/query)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

In the Logs Explorer, you must specify one or more resources, but the resource selection might not be obvious. Here are some tips to help you get started:

  * If you are deploying your application to App Engine or using the App Engine-specific libraries, set your resource to **GAE Application**.

  * If you are deploying your application on Compute Engine, set the resource to **GCE VM Instance**.

  * If you are deploying your application on Google Kubernetes Engine, your cluster's logging configuration determines the resource type of the log entries. For a detailed discussion on the Legacy Google Cloud Observability and the Google Cloud Observability Kubernetes Monitoring solutions, and how those options affect the resource type, see [Migrating to Google Cloud Observability Kubernetes Monitoring](https://docs.cloud.google.com/monitoring/kubernetes-engine/migration#stackdriver-options).

  * If your application is using the Cloud Logging API directly, the resource is dependent on the API and your configuration. For example, in your application, you can specify a resource or use a default resource.

  * If you don't see any logs in the Logs Explorer, to see all log entries, switch to the advanced query mode and use an empty query.

    1. To switch to the advanced query mode, click **menu** (▾) at the top of the Logs Explorer and then select **Convert to advanced filter**.
    2. Clear the content that appears in the filter box.
    3. Click **Submit Filter**.

You can examine the individual entries to identify your resources.




For additional information, see [Using the Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
