---
url: https://docs.cloud.google.com/functions/docs/samples/functions-pubsub-publish/
title: Pub/Sub publish message \u00a0|\u00a0 Cloud Run functions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:51:25.197511+00:00
---

# Pub/Sub publish message  |  Cloud Run functions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/docs/samples/functions-pubsub-publish/

If you are creating a new function, see the [Console Quickstart](https://docs.cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ Samples ](https://docs.cloud.google.com/functions/docs/samples)



#  Pub/Sub publish message Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates how to interact with Pub/Sub from Cloud Functions.

## Code sample

### Java

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.functions.HttpFunction;
    import com.google.cloud.functions.HttpRequest;
    import com.google.cloud.functions.HttpResponse;
    import com.google.cloud.pubsub.v1.[Publisher](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import com.google.pubsub.v1.[ProjectTopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectTopicName.html);
    import com.google.pubsub.v1.[PubsubMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html);
    import java.io.BufferedWriter;
    import java.io.IOException;
    import java.net.HttpURLConnection;
    import java.nio.charset.StandardCharsets;
    import java.util.Optional;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.logging.Level;
    import java.util.logging.Logger;
    
    public class PublishMessage implements HttpFunction {
      // TODO<developer> set this environment variable
      private static final String PROJECT_ID = System.getenv("GOOGLE_CLOUD_PROJECT");
    
      private static final Logger logger = Logger.[getLogger](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.LoggingUtil.SubSystem.html#com_google_cloud_pubsub_v1_LoggingUtil_SubSystem_getLogger__)(PublishMessage.class.getName());
    
      @Override
      public void service(HttpRequest request, HttpResponse response)
          throws IOException, InterruptedException {
        Optional<String> maybeTopicName = request.getFirstQueryParameter("topic");
        Optional<String> maybeMessage = request.getFirstQueryParameter("message");
    
        BufferedWriter responseWriter = response.getWriter();
    
        if (maybeTopicName.isEmpty() || maybeMessage.isEmpty()) {
          response.setStatusCode(HttpURLConnection.HTTP_BAD_REQUEST);
    
          responseWriter.write("Missing 'topic' and/or 'message' parameter(s).");
          return;
        }
    
        String topicName = maybeTopicName.get();
        logger.info("Publishing message to topic: " + topicName);
    
        // Create the PubsubMessage object
        // (This is different than the PubsubMessage POJO used in Pub/Sub-triggered functions)
        [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html) byteStr = [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFrom](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFrom_byte___)(maybeMessage.get(), StandardCharsets.UTF_8);
        [PubsubMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html) pubsubApiMessage = [PubsubMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html).newBuilder().setData(byteStr).build();
    
        [Publisher](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html) publisher = [Publisher](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html).newBuilder(
            [ProjectTopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectTopicName.html).of(PROJECT_ID, topicName)).build();
    
        // Attempt to publish the message
        String responseMessage;
        try {
          [publish](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html#com_google_cloud_pubsub_v1_Publisher_publish_com_google_pubsub_v1_PubsubMessage_)er.[publish](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html#com_google_cloud_pubsub_v1_Publisher_publish_com_google_pubsub_v1_PubsubMessage_)(pubsubApiMessage).get();
          responseMessage = "Message published.";
        } catch (InterruptedException | ExecutionException e) {
          logger.log(Level.SEVERE, "Error publishing Pub/Sub message: " + e.getMessage(), e);
          responseMessage = "Error publishing Pub/Sub message; see logs for more info.";
        } finally {
          if (publisher != null) {
            // When finished with the publisher, shutdown to free up resources.
            publisher.[shutdown](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html#com_google_cloud_pubsub_v1_Publisher_shutdown__)();
            publisher.[awaitTermination](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html#com_google_cloud_pubsub_v1_Publisher_awaitTermination_long_java_util_concurrent_TimeUnit_)(1, TimeUnit.MINUTES);
          }
        }
    
        responseWriter.write(responseMessage);
      }
    }

### Node.js

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const {PubSub} = require('[@google-cloud/pubsub](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/overview.html)');
    
    // Instantiates a client
    const pubsub = new [PubSub](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/pubsub.html)();
    
    /**
     * Publishes a message to a Cloud Pub/Sub Topic.
     *
     * @param {object} req Cloud Function request context.
     * @param {object} req.body The request body.
     * @param {string} req.body.topic Topic name on which to publish.
     * @param {string} req.body.message Message to publish.
     * @param {object} res Cloud Function response context.
     */
    exports.publish = async (req, res) => {
      if (!req.body.topic || !req.body.message) {
        res
          .status(400)
          .send(
            'Missing parameter(s); include "topic" and "message" properties in your request.'
          );
        return;
      }
    
      console.log(`Publishing message to topic ${req.body.topic}`);
    
      // References an existing topic
      const topic = pubsub.topic(req.body.topic);
    
      const messageObject = {
        data: {
          message: req.body.message,
        },
      };
      const messageBuffer = Buffer.[from](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/duration.html)(JSON.stringify(messageObject), 'utf8');
    
      // Publishes a message
      try {
        topic.[publishMessage](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/topic.html)(messageBuffer);
        res.status(200).send('Message published.');
      } catch (err) {
        console.error(err);
        res.status(500).send(err);
        return [Promise](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/pubsub.html).reject(err);
      }
    };

### Python

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import base64
    import json
    import os
    
    from google.cloud import pubsub_v1
    
    
    # TODO(developer): set this environment variable
    PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT")
    
    
    # Instantiates a Pub/Sub client
    publisher = pubsub_v1.[PublisherClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.PublisherClient.html)()
    
    
    # Publishes a message to a Cloud Pub/Sub topic.
    def publish(request):
        request_json = request.get_json(silent=True)
    
        topic_name = request_json.get("topic")
        message = request_json.get("message")
    
        if not topic_name or not message:
            return ('Missing "topic" and/or "message" parameter.', 400)
    
        print(f"Publishing message to topic {topic_name}")
    
        # References an existing topic
        topic_path = publisher.topic_path(PROJECT_ID, topic_name)
    
        message_json = json.dumps(
            {
                "data": {"message": message},
            }
        )
        message_bytes = message_json.encode("utf-8")
    
        # Publishes a message
        try:
            publish_future = [publish](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.PublisherClient.html)er.[publish](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.PublisherClient.html)(topic_path, data=message_bytes)
            publish_future.result()  # Verify the publish succeeded
            return "Message published."
        except Exception as e:
            print(e)
            return (e, 500)
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudfunctions). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
