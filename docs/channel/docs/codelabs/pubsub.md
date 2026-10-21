---
url: https://docs.cloud.google.com/channel/docs/codelabs/pubsub/
title: Pub/Sub notifications \u00a0|\u00a0 Channel Services \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:47:03.022665+00:00
---

# Pub/Sub notifications  |  Channel Services  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/channel/docs/codelabs/pubsub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Channel Services ](https://docs.cloud.google.com/channel/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/channel/docs/reference/libraries)



Send feedback 

#  Pub/Sub notifications Stay organized with collections  Save and categorize content based on your preferences. 

  * Make sure you complete the [API setup codelab](https://docs.cloud.google.com/channel/docs/codelabs/setup) to set up a Google Cloud project and create a service account to call the Cloud Channel API. 

  * We recommend using your Test Partner Sales Console for this codelab. 

  * Familiarize yourself with Pub/Sub [concepts](https://docs.cloud.google.com/pubsub/docs/overview#data_model).




## Overview

The Cloud Channel API uses Pub/Sub to deliver notifications about various customer and entitlement events.

This is particularly useful to:

  * Reflect changes made directly in the Partner Sales Console in your own systems (for example, someone from your support team cancelling a Google Workspace entitlement).
  * Detect critical events that are triggered by your resold customers. For example: 
    * A Google Workspace customer accepting Terms of Service.
    * A Google Workspace customer verifying their domain.
    * A Google Workspace customer adding users on a Flexible entitlement.
    * A Google Workspace customer transferring away.



Setting up Pub/Sub consists of the following three steps:

  1. Enable Pub/Sub API and prepare your service account.

  2. Create a Pub/Sub topic. This topic is owned by Channel Services and you will specify a service account that can create a subscription.

  3. Create a Pub/Sub subscription. This subscription can be _push_ using webhooks (the preferred method) or _pull_.




For a _push_ subscription, you'll host a webhook that receives the events emitted by the Channel Services:

![Push notifications for Channel Services](https://docs.cloud.google.com/static/channel/docs/images/pubsub-push.png)

### Notification format

The following is an example Pub/Sub notification. The message data is transmitted as a base64-encoded JSON string. 
    
    
    {
      "message": {
        "attributes": {
          "event_type": "LICENSE_ASSIGNMENT_CHANGED",
          "subscriber_event_type": "ENTITLEMENT_EVENT"
        },
        "data": "eyJlbnRpdGxlbWVudF9ldmVudCI6eyJldmVudF90eXBlIjoiTElDRU5TRV9BU1NJR05NRU5UX0NIQU5HRUQiLCJlbnRpdGxlbWVudCI6ImFjY291bnRzL0MwMTIzNDU2L2N1c3RvbWVycy9TMDEyMzQ1NjcvZW50aXRsZW1lbnRzL1NhYmNkZWYxMjM0NSJ9fQ==",
        "message_id": 1918124788439510,
        "publish_time": "2021-01-14T01:23:45.678Z"
      },
      "subscription": "projects/project/subscriptions/channel-pubsub-test"
    }
    

This is the same message data, decoded:
    
    
    {
      "entitlement_event": {
        "event_type": "LICENSE_ASSIGNMENT_CHANGED",
        "entitlement": "accounts/C0123456/customers/S01234567/entitlements/Sabcdef12345"}
      }
    }
    

## Step 1: Enable Pub/Sub API and prepare your service account

To run this codelab you need the following:

  * The email address of a service account on your project. This address will look like: service-account@project.iam.gserviceaccount.com.
  * Access to a reseller domain Super Admin account (preferably your Test Partner Sales Console).
  * Your Account ID. You can find this in the Settings of your Partner Sales Console.



To prepare your service account:

  * Navigate to the [API Library](https://console.cloud.google.com/apis/library) section in the Google Cloud console and enable the Pub/Sub API.
  * Grant your service account the Pub/Sub IAM role on the project. Granting `roles/pubsub.editor` (role name = 'Pub/Sub Editor') is good enough for this codelab, but you may want to use more fine-grained privileges in your production integration. You can find full IAM role details on the [Pub/Sub access control](https://docs.cloud.google.com/pubsub/docs/access-control) page.
  * If you choose to apply a custom role instead, you need to grant that role the `pubsub.subscriptions.create` permission to create subscriptions.



There may be a delay after applying these roles and permissions to your account.

**Caution:** You will receive 403 errors if there are no IAM roles on the service account.

## Step 2: Create the topic for your account

To create the Pub/Sub topic, you need to use the `accounts.register` method. This method takes a service account email as a parameter. Only service accounts authorized through this method can subscribe to your new topic.

  1. Go to the [accounts.register](https://docs.cloud.google.com/channel/docs/reference/rest/v1alpha1/accounts/register) documentation and click **Try it!**.
  2. In the `account` field, enter `accounts/ACCOUNT_ID`, replacing `ACCOUNT_ID` with your Account ID.
  3. Click **Add request body parameters** , select `serviceAccount`, and enter your service account email address.
  4. Click **Execute** , making sure to log in as the Super Admin of your reseller domain.



You should get a 200 response similar to the following:
    
    
    {
      "topic": "projects/cloud-channel-pubsub/topics/C0123456-notify"
    }
    

This is the Pub/Sub topic where the events will post.

**Note:** This value is needed in step 3b.

## Step 3: Subscribe to the topic

After creating the Pub/Sub topic, you need to set up how your application consumes change events. You have two options:

  * **Push subscription** : You supply an HTTP POST callback. Pub/Sub will use this to notify your application about new events.
  * **Pull subscription** : Your application periodically makes HTTP calls to get queued changes.



In this codelab, we will use **Push** and send all events to a Cloud Run function that will log in Cloud Logging.

![Pushing Channel Services notifications to a Cloud Run function](https://docs.cloud.google.com/static/channel/docs/images/pubsub-push-codelab.png)

### Step 3a: Create a Cloud Run function

In this step, we're going to create a Cloud Run function that will log the received messages.

  1. Go to the [Cloud Run functions](https://console.cloud.google.com/functions) section of the Google Cloud console. You may have to enable the Cloud Run functions API.
  2. Click add_box**Create Function**.
  3. In the **Configuration** screen: 
     1. Change the name of the function. Optionally, pick a different region.
     2. In HTTP trigger, change **Authentication** to **Allow unauthenticated invocations** , and click **Save**.
     3. Keep note of the **Trigger URL**. You will need it in the next step.
     4. Click **Next**.
  4. In the **Code** screen:

     1. Pick any Node.js runtime
     2. Change the **Entry point** to `log`
     3. In the `index.js` file, replace the sample code with:
    
    exports.log = (req, res) => {
      if (req.body && req.body.message) {
        console.log(req.body);
        const message = req.body.message;
        // data is base64-encoded JSON
        const data = new Buffer.from(message.data, 'base64').toString();
        console.log(data);
      }
      res.status(200).send('OK');
    };
    




You can proceed with the next step while the Cloud Run function deploys.

### Step 3b: Create the subscription

Only service accounts that have been registered for the Channel Services topic (see step 2) can create a subscription.

You can do this with code by calling the Pub/Sub API with your service account credentials. Make sure you don't impersonate your reseller domain's Super Admin—which is required when calling the Cloud Channel API.

For the purpose of this codelab, you will use the gcloud CLI tool on [Cloud Shell](https://docs.cloud.google.com/shell/docs/launching-cloud-shell).

  1. Click **Activate Cloud Shell** at the top of the [Google Cloud console](https://console.cloud.google.com/).

  2. Once the shell is ready, run the following command. Replace the values of `SERVICE_ACCOUNT` with the email address of your service account, `TOPIC` with the topic created in step 2, and `PUSH_ENDPOINT` with the Trigger URL of the Cloud Run function created in step 3a:
         
         SERVICE_ACCOUNT=service-account@project.iam.gserviceaccount.com
         TOPIC=projects/cloud-channel-pubsub/topics/C0123456-notify
         PUSH_ENDPOINT=https://us-central1-project.cloudfunctions.net/pubsub
         

  3. Activate the service account in the shell:
         
         gcloud iam service-accounts keys create sa-keys.json \
             --iam-account=$SERVICE_ACCOUNT
         gcloud auth activate-service-account --key-file=sa-keys.json
         

  4. Create the subscription:
         
         gcloud pubsub subscriptions create channel-pubsub-test \
             --topic=$TOPIC \
             --push-endpoint=$PUSH_ENDPOINT
         




You can confirm the subscription is set up by going to the [Pub/Sub subscriptions section](https://console.cloud.google.com/cloudpubsub/subscription/list).

## Generate some data

After finishing the previous steps, you are ready to receive data.

The easiest way is to create a customer in your Partner Sales Console and provision a product. If you've finished the [end-to-end Workspace provisioning codelab](https://docs.cloud.google.com/channel/docs/codelabs/workspace/provisioning) you can create a customer with a Google Workspace by running the sample code.

Go to your function in the Google Cloud console and open the **Logs** tab. The following is an example of what you should see.

![Sample logs for Pub/Sub events](https://docs.cloud.google.com/static/channel/docs/images/pubsub-push-codelab-logs.png)

**Note:** in rare cases, it can take a few minutes for the Pub/Sub subscription to start receiving events from the topic.

## Clean up

  * Delete the Cloud Run function
  * Delete the subscription



The topic will be cleaned automatically when it doesn't have any remaining subscribers.

## Next steps

This codelab took you through discovering how Channel Services leverages Pub/Sub to let you build your integration in a reactive way, and at scale.

### Event reference

See [the RPC reference](https://cloud.google.com/channel/docs/reference/rpc/google.cloud.channel.v1#subscriberevent) for the list of events that are generated by Channel Services.

### API reference

This codelab makes use of the Google Cloud console, but you can perform these steps programmatically. To do so:

  * Use [`accounts.register`](https://docs.cloud.google.com/channel/docs/reference/rest/v1/accounts/register) to create the topic.
  * Use Pub/Sub API's [`subscriptions.create`](https://cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions/create) to create the Pub/Sub subscription.
  * See [`accounts.listSubscribers`](https://docs.cloud.google.com/channel/docs/reference/rest/v1/accounts/listSubscribers) and [`accounts.unregister`](https://docs.cloud.google.com/channel/docs/reference/rest/v1/accounts/unregister) for additional endpoints you can use in your integration.



### Pub/Sub guarantees and best practices

The delay between an event and its notification is not guaranteed. Similarly, the notification ordering is not guaranteed. Lastly, messages may be delivered multiple times.

Push endpoint best practices:

  * Since messages may be delayed, sent out of order, or sent multiple times, your endpoint should be idempotent, and use [`customers.get`](https://docs.cloud.google.com/channel/docs/reference/rest/v1/accounts.customers/get) and [`entitlements.get`](https://docs.cloud.google.com/channel/docs/reference/rest/v1/accounts.customers.entitlements/get)

  * While the default Pub/Sub timeout for push is 10 seconds (this can be increased via the Pub/Sub subscription's `ackDeadline`), it is recommended to use a message-based architecture and make the endpoint respond as fast as possible.

  * If your endpoint is down or returns 5xx errors, Pub/Sub will retry. You can find further information about [how to receive messages via push](https://docs.cloud.google.com/pubsub/docs/push) in the Pub/Sub documentation.




If you prefer to use **pull** , you can find information about [how to receive messages via pull](https://docs.cloud.google.com/pubsub/docs/pull) in the Pub/Sub documentation.

### Event filtering

Because Channel Services's notifications include `attributes`, you can create fine-grained subscriptions by creating specific Pub/Sub subscriptions with [Pub/Sub filtering](https://docs.cloud.google.com/pubsub/docs/filtering).

For example, filtering with `attributes.event_type = "LICENSE_ASSIGNMENT_CHANGED"` lets you track all Google Workspace seat changes.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
