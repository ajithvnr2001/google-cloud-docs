---
url: https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/
title: Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:00:07.853829+00:00
---

# Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 4.8.0 (latest) ](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/)
  * [ 4.4.0 ](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/4.4.0/)
  * [ 4.3.3 ](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/4.3.3/)
  * [ 4.1.1 ](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/4.1.1/)
  * [ 4.0.7 ](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/4.0.7/)
  * [ 3.7.5 ](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/3.7.5/)
  * [ 3.2.1 ](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/3.2.1/)
  * [ 3.1.1 ](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/3.1.1/)
  * [ 3.0.3 ](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/3.0.3/)
  * [ 2.18.3 ](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/2.18.3/)
  * [ 2.17.0 ](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/2.17.0/)
  * [ 2.16.6 ](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/2.16.6/)
  * [ 2.13.0 ](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/2.13.0/)



# [Google Cloud Pub/Sub: Node.js Client](https://github.com/googleapis/nodejs-pubsub)

[![release level](https://img.shields.io/badge/release%20level-stable-brightgreen.svg?style=flat)](https://cloud.google.com/terms/launch-stages) [![npm version](https://img.shields.io/npm/v/@google-cloud/pubsub.svg)](https://www.npmjs.org/package/@google-cloud/pubsub)

[Cloud Pub/Sub](https://cloud.google.com/pubsub/docs) is a fully-managed real-time messaging service that allows you to send and receive messages between independent applications.

This document contains links to an [API reference](https://cloud.google.com/nodejs/docs/reference/pubsub/latest/overview), samples, and other resources useful to developing Node.js applications. For additional help developing Pub/Sub applications, in Node.js and other languages, see our [Pub/Sub quickstart](https://cloud.google.com/pubsub/docs/quickstart-client-libraries), [publisher](https://cloud.google.com/pubsub/docs/publisher), and [subscriber](https://cloud.google.com/pubsub/docs/subscriber) guides.

A comprehensive list of changes in each version may be found in [the CHANGELOG](https://github.com/googleapis/nodejs-pubsub/blob/main/CHANGELOG.md).

  * [Google Cloud Pub/Sub Node.js Client API Reference](https://cloud.google.com/nodejs/docs/reference/pubsub/latest)
  * [Google Cloud Pub/Sub Documentation](https://cloud.google.com/pubsub/docs/)
  * [github.com/googleapis/nodejs-pubsub](https://github.com/googleapis/nodejs-pubsub)



Read more about the client libraries for Cloud APIs, including the older Google APIs Client Libraries, in [Client Libraries Explained](https://cloud.google.com/apis/docs/client-libraries-explained).

**Table of contents:**

  * Quickstart
    * Before you begin
    * Installing the client library
    * Using the client library
  * Samples
  * Versioning
  * Contributing
  * License



## Quickstart

### Before you begin

  1. [Select or create a Cloud Platform project](https://console.cloud.google.com/project).
  2. [Enable billing for your project](https://support.google.com/cloud/answer/6293499#enable-billing).
  3. [Enable the Google Cloud Pub/Sub API](https://console.cloud.google.com/flows/enableapi?apiid=pubsub.googleapis.com).
  4. [Set up authentication](https://cloud.google.com/docs/authentication/external/set-up-adc-local) so you can access the API from your local workstation.



### Installing the client library
    
    
    npm install @google-cloud/pubsub
    

### Using the client library
    
    
    // Imports the Google Cloud client library
    const {PubSub} = require('[@google-cloud/pubsub](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/overview.html)');
    
    async function quickstart(
      projectId = 'your-project-id', // Your Google Cloud Platform project ID
      topicNameOrId = 'my-topic', // Name for the new topic to create
      subscriptionName = 'my-sub' // Name for the new subscription to create
    ) {
      // Instantiates a client
      const pubsub = new [PubSub](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/pubsub.html)({projectId});
    
      // Creates a new topic
      const [topic] = await pubsub.createTopic(topicNameOrId);
      console.log(`Topic ${topic.name} created.`);
    
      // Creates a subscription on that new topic
      const [subscription] = await topic.createSubscription(subscriptionName);
    
      // Receive callbacks for new messages on the subscription
      subscripti[on](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/subscription-interface.html).[on](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/subscription-interface.html)('message', message => {
        console.log('Received message:', message.data.toString());
        process.exit(0);
      });
    
      // Receive callbacks for errors on the subscription
      subscripti[on](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/subscription-interface.html).[on](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/subscription-interface.html)('error', error => {
        console.error('Received error:', error);
        process.exit(1);
      });
    
      // Send a message to the topic
      topic.[publishMessage](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/topic.html)({data: Buffer.[from](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/duration.html)('Test message!')});
    }
    

## Running gRPC C++ bindings

For some workflows and environments it might make sense to use the C++ gRPC implementation, instead of the default one (see: [#770](https://github.com/googleapis/nodejs-pubsub/issues/770)):

To configure `@google-cloud/pubsub` to use an alternative `grpc` transport:

  1. `npm install grpc`, adding `grpc` as a dependency.
  2. instantiate `@google-cloud/pubsub` with `grpc`:
         
         const {PubSub} = require('[@google-cloud/pubsub](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/overview.html)');
         const grpc = require('grpc');
         const pubsub = new [PubSub](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/pubsub.html)({grpc});
         




## Samples

Samples are in the [`samples/`](https://github.com/googleapis/nodejs-pubsub/tree/main/samples) directory. Each sample's `README.md` has instructions for running its sample.

Sample | Source Code | Try it  
---|---|---  
Commit an Avro-Based Schema | [source code](https://github.com/googleapis/nodejs-pubsub/blob/main/samples/commitAvroSchema.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-pubsub&page=editor&open_in_editor=samples/commitAvroSchema.js,samples/README.md)  
Commit an Proto-Based Schema | [source code](https://github.com/googleapis/nodejs-pubsub/blob/main/samples/commitProtoSchema.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-pubsub&page=editor&open_in_editor=samples/commitProtoSchema.js,samples/README.md)  
Create an Avro based Schema | [source code](https://github.com/googleapis/nodejs-pubsub/blob/main/samples/createAvroSchema.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-pubsub&page=editor&open_in_editor=samples/createAvroSchema.js,samples/README.md)  
Create BigQuery Subscription | [source code](https://github.com/googleapis/nodejs-pubsub/blob/main/samples/createBigQuerySubscription.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-pubsub&page=editor&open_in_editor=samples/createBigQuerySubscription.js,samples/README.md)  
Create a Proto based Schema | [source code](https://github.com/googleapis/nodejs-pubsub/blob/main/samples/createProtoSchema.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-pubsub&page=editor&open_in_editor=samples/createProtoSchema.js,samples/README.md)  
Create Push Subscription | [source code](https://github.com/googleapis/nodejs-pubsub/blob/main/samples/createPushSubscription.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-pubsub&page=editor&open_in_editor=samples/createPushSubscription.js,samples/README.md)  
Create Push Subscription With No Wrapper | [source code](https://github.com/googleapis/nodejs-pubsub/blob/main/samples/createPushSubscriptionNoWrapper.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-pubsub&page=editor&open_in_editor=samples/createPushSubscriptionNoWrapper.js,samples/README.md)  
Create Subscription | [source code](https://github.com/googleapis/nodejs-pubsub/blob/main/samples/createSubscription.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-pubsub&page=editor&open_in_editor=samples/createSubscription.js,samples/README.md)  
Create a Cloud Storage subscription | [source code](https://github.com/googleapis/nodejs-pubsub/blob/main/samples/createSubscriptionWithCloudStorage.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-pubsub&page=editor&open_in_editor=samples/createSubscriptionWithCloudStorage.js,samples/README.md)  
Create Subscription With Dead Letter Policy | [source code](https://github.com/googleapis/nodejs-pubsub/blob/main/samples/createSubscriptionWithDeadLetterPolicy.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-pubsub&page=editor&open_in_editor=samples/createSubscriptionWithDeadLetterPolicy.js,samples/README.md)  
Create an exactly-once delivery subscription | [source code](https://github.com/googleapis/nodejs-pubsub/blob/main/samples/createSubscriptionWithExactlyOnceDelivery.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-pubsub&page=editor&open_in_editor=samples/createSubscriptionWithExactlyOnceDelivery.js,samples/README.md)  
Create Subscription With Filtering | [source code](https://github.com/googleapis/nodejs-pubsub/blob/main/samples/createSubscriptionWithFiltering.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-pubsub&page=editor&open_in_editor=samples/createSubscriptionWithFiltering.js,samples/README.md)  
Create Subscription with ordering enabled | [source code](https://github.com/googleapis/nodejs-pubsub/blob/main/samples/createSubscriptionWithOrdering.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-pubsub&page=editor&open_in_editor=samples/createSubscriptionWithOrdering.js,samples/README.md)  
Create Subscription With Retry Policy | [source code](https://github.com/googleapis/nodejs-pubsub/blob/main/samples/createSubscriptionWithRetryPolicy.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-pubsub&page=editor&open_in_editor=samples/createSubscriptionWithRetryPolicy.js,samples/README.md)  
Create Topic | [source code](https://github.com/googleapis/nodejs-pubsub/blob/main/samples/createTopic.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-pubsub&page=editor&open_in_editor=samples/createTopic.js,samples/README.md)  
Create Topic With Cloud Storage Ingestion | [source code](https://github.com/googleapis/nodejs-pubsub/blob/main/samples/createTopicWithCloudStorageIngestion.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-pubsub&page=editor&open_in_editor=samples/createTopicWithCloudStorageIngestion.js,samples/README.md)  
Create Topic With Kinesis Ingestion | [source code](https://github.com/googleapis/nodejs-pubsub/blob/main/samples/createTopicWithKinesisIngestion.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-pubsub&page=editor&open_in_editor=samples/createTopicWithKinesisIngestion.js,samples/README.md)  
Create Topic With Schema | [source code](https://github.com/googleapis/nodejs-pubsub/blob/main/samples/createTopicWithSchema.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-pubsub&page=editor&open_in_editor=samples/createTopicWithSchema.js,samples/README.md)  
Create Topic With Schema Revisions | [source code](https://github.com/googleapis/nodejs-pubsub/blob/main/samples/createTopicWithSchemaRevisions.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-pubsub&page=editor&open_in_editor=samples/createTopicWithSchemaRevisions.js,samples/README.md)  
Delete a previously created schema | [source code](https://github.com/googleapis/nodejs-pubsub/blob/main/samples/deleteSchema.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-pubsub&page=editor&open_in_editor=samples/deleteSchema.js,samples/README.md)  
Delete a Schema Revision | [source code](https://github.com/googleapis/nodejs-pubsub/blob/main/samples/deleteSchemaRevision.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-pubsub&page=editor&open_in_editor=samples/deleteSchemaRevision.js,samples/README.md)  
Delete Subscription | [source code](https://github.com/googleapis/nodejs-pubsub/blob/main/samples/deleteSubscription.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-pubsub&page=editor&open_in_editor=samples/deleteSubscription.js,samples/README.md)  
Delete Topic | [source code](https://github.com/googleapis/nodejs-pubsub/blob/main/samples/deleteTopic.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-pubsub&page=editor&open_in_editor=samples/deleteTopic.js,samples/README.md)  
Detach Subscription | [source code](https://github.com/googleapis/nodejs-pubsub/blob/main/samples/detachSubscription.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-pubsub&page=editor&open_in_editor=samples/detachSubscription.js,samples/README.md)  
Get a previously created schema | [source code](https://github.com/googleapis/nodejs-pubsub/blob/main/samples/getSchema.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-pubsub&page=editor&open_in_editor=samples/getSchema.js,samples/README.md)  
Get a previously created schema revision | [source code](https://github.com/googleapis/nodejs-pubsub/blob/main/samples/getSchemaRevision.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-pubsub&page=editor&open_in_editor=samples/getSchemaRevision.js,samples/README.md)  
Get Subscription | [source code](https://github.com/googleapis/nodejs-pubsub/blob/main/samples/getSubscription.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-pubsub&page=editor&open_in_editor=samples/getSubscription.js,samples/README.md)  
Get Subscription Policy | [source code](https://github.com/googleapis/nodejs-pubsub/blob/main/samples/getSubscriptionPolicy.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-pubsub&page=editor&open_in_editor=samples/getSubscriptionPolicy.js,samples/README.md)  
Get Topic Policy | [source code](https://github.com/googleapis/nodejs-pubsub/blob/main/samples/getTopicPolicy.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-pubsub&page=editor&open_in_editor=samples/getTopicPolicy.js,samples/README.md)  
List All Topics | [source code](https://github.com/googleapis/nodejs-pubsub/blob/main/samples/listAllTopics.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-pubsub&page=editor&open_in_editor=samples/listAllTopics.js,samples/README.md)  
List Revisions on a Schema | [source code](https://github.com/googleapis/nodejs-pubsub/blob/main/samples/listSchemaRevisions.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-pubsub&page=editor&open_in_editor=samples/listSchemaRevisions.js,samples/README.md)  
List schemas on a project | [source code](https://github.com/googleapis/nodejs-pubsub/blob/main/samples/listSchemas.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-pubsub&page=editor&open_in_editor=samples/listSchemas.js,samples/README.md)  
List Subscriptions | [source code](https://github.com/googleapis/nodejs-pubsub/blob/main/samples/listSubscriptions.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-pubsub&page=editor&open_in_editor=samples/listSubscriptions.js,samples/README.md)  
List Subscriptions On a Topic | [source code](https://github.com/googleapis/nodejs-pubsub/blob/main/samples/listTopicSubscriptions.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-pubsub&page=editor&open_in_editor=samples/listTopicSubscriptions.js,samples/README.md)  
Listen For Avro Records | [source code](https://github.com/googleapis/nodejs-pubsub/blob/main/samples/listenForAvroRecords.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-pubsub&page=editor&open_in_editor=samples/listenForAvroRecords.js,samples/README.md)  
Listen For Avro Records With Revisions | [source code](https://github.com/googleapis/nodejs-pubsub/blob/main/samples/listenForAvroRecordsWithRevisions.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-pubsub&page=editor&open_in_editor=samples/listenForAvroRecordsWithRevisions.js,samples/README.md)  
Listen For Errors | [source code](https://github.com/googleapis/nodejs-pubsub/blob/main/samples/listenForErrors.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-pubsub&page=editor&open_in_editor=samples/listenForErrors.js,samples/README.md)  
Listen For Messages | [source code](https://github.com/googleapis/nodejs-pubsub/blob/main/samples/listenForMessages.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-pubsub&page=editor&open_in_editor=samples/listenForMessages.js,samples/README.md)  
Listen with exactly-once delivery | [source code](https://github.com/googleapis/nodejs-pubsub/blob/main/samples/listenForMessagesWithExactlyOnceDelivery.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-pubsub&page=editor&open_in_editor=samples/listenForMessagesWithExactlyOnceDelivery.js,samples/README.md)  
Listen For Protobuf Messages | [source code](https://github.com/googleapis/nodejs-pubsub/blob/main/samples/listenForProtobufMessages.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-pubsub&page=editor&open_in_editor=samples/listenForProtobufMessages.js,samples/README.md)  
Listen For Messages With Custom Attributes | [source code](https://github.com/googleapis/nodejs-pubsub/blob/main/samples/listenWithCustomAttributes.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-pubsub&page=editor&open_in_editor=samples/listenWithCustomAttributes.js,samples/README.md)  
Subscribe with OpenTelemetry Tracing | [source code](https://github.com/googleapis/nodejs-pubsub/blob/main/samples/listenWithOpenTelemetryTracing.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-pubsub&page=editor&open_in_editor=samples/listenWithOpenTelemetryTracing.js,samples/README.md)  
Modify Push Configuration | [source code](https://github.com/googleapis/nodejs-pubsub/blob/main/samples/modifyPushConfig.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-pubsub&page=editor&open_in_editor=samples/modifyPushConfig.js,samples/README.md)  
Optimistic Subscribe | [source code](https://github.com/googleapis/nodejs-pubsub/blob/main/samples/optimisticSubscribe.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-pubsub&page=editor&open_in_editor=samples/optimisticSubscribe.js,samples/README.md)  
Publish Avro Records to a Topic | [source code](https://github.com/googleapis/nodejs-pubsub/blob/main/samples/publishAvroRecords.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-pubsub&page=editor&open_in_editor=samples/publishAvroRecords.js,samples/README.md)  
Publish Batched Messages | [source code](https://github.com/googleapis/nodejs-pubsub/blob/main/samples/publishBatchedMessages.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-pubsub&page=editor&open_in_editor=samples/publishBatchedMessages.js,samples/README.md)  
Publish Message | [source code](https://github.com/googleapis/nodejs-pubsub/blob/main/samples/publishMessage.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-pubsub&page=editor&open_in_editor=samples/publishMessage.js,samples/README.md)  
Publish Message With Custom Attributes | [source code](https://github.com/googleapis/nodejs-pubsub/blob/main/samples/publishMessageWithCustomAttributes.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-pubsub&page=editor&open_in_editor=samples/publishMessageWithCustomAttributes.js,samples/README.md)  
Publish Ordered Message | [source code](https://github.com/googleapis/nodejs-pubsub/blob/main/samples/publishOrderedMessage.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-pubsub&page=editor&open_in_editor=samples/publishOrderedMessage.js,samples/README.md)  
Publish Protobuf Messages to a Topic | [source code](https://github.com/googleapis/nodejs-pubsub/blob/main/samples/publishProtobufMessages.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-pubsub&page=editor&open_in_editor=samples/publishProtobufMessages.js,samples/README.md)  
Publish with flow control | [source code](https://github.com/googleapis/nodejs-pubsub/blob/main/samples/publishWithFlowControl.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-pubsub&page=editor&open_in_editor=samples/publishWithFlowControl.js,samples/README.md)  
Publish with OpenTelemetry Tracing | [source code](https://github.com/googleapis/nodejs-pubsub/blob/main/samples/publishWithOpenTelemetryTracing.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-pubsub&page=editor&open_in_editor=samples/publishWithOpenTelemetryTracing.js,samples/README.md)  
Publish With Retry Settings | [source code](https://github.com/googleapis/nodejs-pubsub/blob/main/samples/publishWithRetrySettings.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-pubsub&page=editor&open_in_editor=samples/publishWithRetrySettings.js,samples/README.md)  
Quickstart | [source code](https://github.com/googleapis/nodejs-pubsub/blob/main/samples/quickstart.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-pubsub&page=editor&open_in_editor=samples/quickstart.js,samples/README.md)  
Remove Dead Letter Policy | [source code](https://github.com/googleapis/nodejs-pubsub/blob/main/samples/removeDeadLetterPolicy.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-pubsub&page=editor&open_in_editor=samples/removeDeadLetterPolicy.js,samples/README.md)  
Resume Publish | [source code](https://github.com/googleapis/nodejs-pubsub/blob/main/samples/resumePublish.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-pubsub&page=editor&open_in_editor=samples/resumePublish.js,samples/README.md)  
Rollback a Schema | [source code](https://github.com/googleapis/nodejs-pubsub/blob/main/samples/rollbackSchema.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-pubsub&page=editor&open_in_editor=samples/rollbackSchema.js,samples/README.md)  
Set Subscription IAM Policy | [source code](https://github.com/googleapis/nodejs-pubsub/blob/main/samples/setSubscriptionPolicy.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-pubsub&page=editor&open_in_editor=samples/setSubscriptionPolicy.js,samples/README.md)  
Set Topic IAM Policy | [source code](https://github.com/googleapis/nodejs-pubsub/blob/main/samples/setTopicPolicy.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-pubsub&page=editor&open_in_editor=samples/setTopicPolicy.js,samples/README.md)  
Subscribe With Flow Control Settings | [source code](https://github.com/googleapis/nodejs-pubsub/blob/main/samples/subscribeWithFlowControlSettings.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-pubsub&page=editor&open_in_editor=samples/subscribeWithFlowControlSettings.js,samples/README.md)  
Synchronous Pull | [source code](https://github.com/googleapis/nodejs-pubsub/blob/main/samples/synchronousPull.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-pubsub&page=editor&open_in_editor=samples/synchronousPull.js,samples/README.md)  
Synchronous Pull with delivery attempt. | [source code](https://github.com/googleapis/nodejs-pubsub/blob/main/samples/synchronousPullWithDeliveryAttempts.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-pubsub&page=editor&open_in_editor=samples/synchronousPullWithDeliveryAttempts.js,samples/README.md)  
Synchronous Pull With Lease Management | [source code](https://github.com/googleapis/nodejs-pubsub/blob/main/samples/synchronousPullWithLeaseManagement.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-pubsub&page=editor&open_in_editor=samples/synchronousPullWithLeaseManagement.js,samples/README.md)  
Test Subscription Permissions | [source code](https://github.com/googleapis/nodejs-pubsub/blob/main/samples/testSubscriptionPermissions.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-pubsub&page=editor&open_in_editor=samples/testSubscriptionPermissions.js,samples/README.md)  
Test Topic Permissions | [source code](https://github.com/googleapis/nodejs-pubsub/blob/main/samples/testTopicPermissions.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-pubsub&page=editor&open_in_editor=samples/testTopicPermissions.js,samples/README.md)  
Update Dead Letter Policy | [source code](https://github.com/googleapis/nodejs-pubsub/blob/main/samples/updateDeadLetterPolicy.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-pubsub&page=editor&open_in_editor=samples/updateDeadLetterPolicy.js,samples/README.md)  
Update Topic Ingestion Type | [source code](https://github.com/googleapis/nodejs-pubsub/blob/main/samples/updateTopicIngestionType.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-pubsub&page=editor&open_in_editor=samples/updateTopicIngestionType.js,samples/README.md)  
Update Topic Schema | [source code](https://github.com/googleapis/nodejs-pubsub/blob/main/samples/updateTopicSchema.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-pubsub&page=editor&open_in_editor=samples/updateTopicSchema.js,samples/README.md)  
Validate a schema definition | [source code](https://github.com/googleapis/nodejs-pubsub/blob/main/samples/validateSchema.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-pubsub&page=editor&open_in_editor=samples/validateSchema.js,samples/README.md)  
  
The [Google Cloud Pub/Sub Node.js Client API Reference](https://cloud.google.com/nodejs/docs/reference/pubsub/latest) documentation also contains samples.

## Supported Node.js Versions

Our client libraries follow the [Node.js release schedule](https://github.com/nodejs/release#release-schedule). Libraries are compatible with all current _active_ and _maintenance_ versions of Node.js. If you are using an end-of-life version of Node.js, we recommend that you update as soon as possible to an actively supported LTS version.

Google's client libraries support legacy versions of Node.js runtimes on a best-efforts basis with the following warnings:

  * Legacy versions are not tested in continuous integration.
  * Some security patches and features cannot be backported.
  * Dependencies cannot be kept up-to-date.



Client libraries targeting some end-of-life versions of Node.js are available, and can be installed through npm [dist-tags](https://docs.npmjs.com/cli/dist-tag). The dist-tags follow the naming convention `legacy-(version)`. For example, `npm install @google-cloud/pubsub@legacy-8` installs client libraries for versions compatible with Node.js 8.

## Versioning

This library follows [Semantic Versioning](http://semver.org/).

This library is considered to be **stable**. The code surface will not change in backwards-incompatible ways unless absolutely necessary (e.g. because of critical security issues) or with an extensive deprecation period. Issues and requests against **stable** libraries are addressed with the highest priority.

More Information: [Google Cloud Platform Launch Stages](https://cloud.google.com/terms/launch-stages)

## Contributing

Contributions welcome! See the [Contributing Guide](https://github.com/googleapis/nodejs-pubsub/blob/main/CONTRIBUTING.md).

Please note that this `README.md`, the `samples/README.md`, and a variety of configuration files in this repository (including `.nycrc` and `tsconfig.json`) are generated from a central template. To edit one of these files, make an edit to its templates in [directory](https://github.com/googleapis/synthtool).

## License

Apache Version 2.0

See [LICENSE](https://github.com/googleapis/nodejs-pubsub/blob/main/LICENSE)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
