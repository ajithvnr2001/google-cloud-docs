---
url: https://docs.cloud.google.com/billing/docs/how-to/control-usage/
title: Control resource usage with notifications \u00a0|\u00a0 Cloud Billing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:37:22.250851+00:00
---

# Control resource usage with notifications  |  Cloud Billing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/billing/docs/how-to/control-usage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud Billing ](https://docs.cloud.google.com/billing/docs)
  * [ Guides ](https://docs.cloud.google.com/billing/docs/concepts)



Send feedback 

#  Control resource usage with notifications Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to use budget notifications to selectively control resource usage.

When you [disable billing on a project](https://docs.cloud.google.com/billing/docs/how-to/disable-billing-with-notifications), all services stop and all resources are eventually deleted. If you need a more nuanced response, you can selectively control resources. For example, you can stop some Compute Engine resources while leaving Cloud Storage resources intact. Stopping only some resources reduces your costs without completely disabling your environment.

In the following example, the project runs research with a number of Compute Engine virtual machines (VMs) and stores results in Cloud Storage buckets. Using the budget notifications as the trigger, after the budget is exceeded, this Cloud Run function shuts down all Compute Engine instances, but doesn't affect the stored results.

## Before you begin

Before you begin, you must complete the following tasks:

  1. [Enable the Cloud Billing API](https://console.cloud.google.com/apis/api/cloudbilling.googleapis.com)
  2. [Create a budget](https://docs.cloud.google.com/billing/docs/how-to/budgets)
  3. [Set up programmatic budget notifications](https://docs.cloud.google.com/billing/docs/how-to/budgets-programmatic-notifications)



## Set up a Cloud Run function

  1. Complete the steps in [Create a Cloud Run function](https://docs.cloud.google.com/billing/docs/how-to/listen-to-notifications#create-function). Ensure that you set the **Trigger type** to the same Pub/Sub topic that your budget will use.
  2. Add the following dependencies:

###  Node.js 

Copy the following to your `package.json` file:
         
         {
           "name": "cloud-functions-billing",
           "private": "true",
           "version": "0.0.1",
           "description": "Examples of integrating Cloud Functions with billing",
           "main": "index.js",
           "engines": {
             "node": ">=20.0.0"
           },
           "scripts": {
             "compute-test": "c8 mocha -p -j 2 test/periodic.test.js --timeout=600000",
             "test": "c8 mocha -p -j 2 test/index.test.js --timeout=5000 --exit"
           },
           "author": "Ace Nassri <anassri@google.com>",
           "license": "Apache-2.0",
           "dependencies": {
             "@google-cloud/billing": "^5.0.0",
             "@google-cloud/compute": "^6.0.0",
             "@slack/web-api": "^8.0.0",
             "google-auth-library": "^9.0.0",
             "googleapis": "^143.0.0"
           },
           "devDependencies": {
             "@google-cloud/functions-framework": "^5.0.0",
             "c8": "^12.0.0",
             "gaxios": "^7.0.0",
             "mocha": "^10.0.0",
             "promise-retry": "^2.0.0",
             "proxyquire": "^2.1.0",
             "sinon": "^18.0.0",
             "wait-port": "^1.0.4"
           }
         }
         

###  Python 

Copy the following to your `requirements.txt` file:
         
         slackclient==2.9.4
         google-api-python-client==2.131.0
         

  3. Copy the following code into your Cloud Run function:

###  Node.js 
         
         const {CloudBillingClient} = require('[@google-cloud/billing](https://docs.cloud.google.com/nodejs/docs/reference/billing/latest/overview.html)');
         const {InstancesClient} = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)');
         
         const PROJECT_ID = process.env.GOOGLE_CLOUD_PROJECT;
         const PROJECT_NAME = `projects/${PROJECT_ID}`;
         const instancesClient = new [InstancesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
         const ZONE = 'us-central1-a';
         
         exports.limitUse = async pubsubEvent => {
           const pubsubData = JSON.parse(
             Buffer.from(pubsubEvent.data, 'base64').toString()
           );
           if (pubsubData.costAmount <= pubsubData.budgetAmount) {
             return `No action necessary. (Current cost: ${pubsubData.costAmount})`;
           }
         
           const instanceNames = await _listRunningInstances(PROJECT_ID, ZONE);
           if (!instanceNames.length) {
             return 'No running instances were found.';
           }
         
           await _stopInstances(PROJECT_ID, ZONE, instanceNames);
           return `${instanceNames.length} instance(s) stopped successfully.`;
         };
         
         /**
          * @return {Promise} Array of names of running instances
          */
         const _listRunningInstances = async (projectId, zone) => {
           const [instances] = await instancesClient.list({
             project: projectId,
             zone: zone,
           });
           return instances
             .filter(item => item.status === 'RUNNING')
             .map(item => item.name);
         };
         
         /**
          * @param {Array} instanceNames Names of instance to stop
          * @return {Promise} Response from stopping instances
          */
         const _stopInstances = async (projectId, zone, instanceNames) => {
           await Promise.all(
             instanceNames.map(instanceName => {
               return instancesClient
                 .stop({
                   project: projectId,
                   zone: zone,
                   instance: instanceName,
                 })
                 .then(() => {
                   console.log(`Instance stopped successfully: ${instanceName}`);
                 });
             })
           );
         };

###  Python 
         
         import base64
         import json
         import os
         from googleapiclient import discovery
         PROJECT_ID = os.getenv("GCP_PROJECT")
         PROJECT_NAME = f"projects/{PROJECT_ID}"
         ZONE = "us-west1-b"
         
         
         def limit_use(data, context):
             pubsub_data = base64.b64decode(data["data"]).decode("utf-8")
             pubsub_json = json.loads(pubsub_data)
             cost_amount = pubsub_json["costAmount"]
             budget_amount = pubsub_json["budgetAmount"]
             if cost_amount <= budget_amount:
                 print(f"No action necessary. (Current cost: {cost_amount})")
                 return
         
             compute = discovery.build(
                 "compute",
                 "v1",
                 cache_discovery=False,
             )
             instances = compute.instances()
         
             instance_names = __list_running_instances(PROJECT_ID, ZONE, instances)
             __stop_instances(PROJECT_ID, ZONE, instance_names, instances)
         
         
         def __list_running_instances(project_id, zone, instances):
             """
             @param {string} project_id ID of project that contains instances to stop
             @param {string} zone Zone that contains instances to stop
             @return {Promise} Array of names of running instances
             """
             res = instances.list(project=project_id, zone=zone).execute()
         
             if "items" not in res:
                 return []
         
             items = res["items"]
             running_names = [i["name"] for i in items if i["status"] == "RUNNING"]
             return running_names
         
         
         def __stop_instances(project_id, zone, instance_names, instances):
             """
             @param {string} project_id ID of project that contains instances to stop
             @param {string} zone Zone that contains instances to stop
             @param {Array} instance_names Names of instance to stop
             @return {Promise} Response from stopping instances
             """
             if not len(instance_names):
                 print("No running instances were found.")
                 return
         
             for name in instance_names:
                 instances.stop(project=project_id, zone=zone, instance=name).execute()
                 print(f"Instance stopped successfully: {name}")
         
         

  4. Set the **Entry point** to the correct function to execute:

### Node.js

Set the **Entry point** to `limitUse`.

### Python

Set the **Entry point** to `limit_use`.

  5. Review the [list of environment variables set automatically](https://docs.cloud.google.com/functions/docs/configuring/env-var#environment_variables_set_automatically) and determine if you need to manually set the GCP_PROJECT variable to the project running the virtual machines.

  6. Set the ZONE parameter. This parameter is the zone where instances are stopped when the budget is exceeded.

**Note:** This code sample only stops instances in a single zone in the specified project. Depending on your needs, you can change the code inside your Cloud Run function to handle other projects and zones.
  7. Click **DEPLOY**.




## Configure service account permissions

Your Cloud Run function runs as an automatically created service account. To control usage, you need to grant the service account permissions to any services on the project that it needs to modify by completing the following steps:

  1. Identify the correct service account by viewing the details of your Cloud Run function. The service account is listed at the bottom of the page.
  2. Go to the **IAM** page in the Google Cloud console to set the appropriate permissions.

[Go to the IAM page](https://console.cloud.google.com/iam-admin/iam)


**Note:** We recommend that you grant the lowest required permissions for the services that the function manages. The [Compute Instance Admin (v1)](https://docs.cloud.google.com/compute/docs/access/iam#compute.instanceAdmin.v1) role will grant you the appropriate permissions. However, to be more secure, you might want to [create a custom role](https://docs.cloud.google.com/iam/docs/creating-custom-roles) that only grants the necessary permissions.

## Test that instances are stopped

To ensure your function works as expected, follow the steps in [Test a Cloud Run function](https://docs.cloud.google.com/billing/docs/how-to/listen-to-notifications#test-function).

If successful, your Compute Engine VMs in the Google Cloud console are stopped.

## What's next

Review other programmatic notification examples to learn how to do the following:

  * [Listen to your notifications](https://docs.cloud.google.com/billing/docs/how-to/listen-to-notifications)
  * [Disable billing usage with notifications](https://docs.cloud.google.com/billing/docs/how-to/disable-billing-with-notifications)
  * [Send notifications to Slack](https://docs.cloud.google.com/billing/docs/how-to/send-notifications-to-slack)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
