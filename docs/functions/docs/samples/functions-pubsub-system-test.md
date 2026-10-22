---
url: https://docs.cloud.google.com/functions/docs/samples/functions-pubsub-system-test/
title: Pub/Sub system tests \u00a0|\u00a0 Cloud Run functions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:51:19.149981+00:00
---

# Pub/Sub system tests  |  Cloud Run functions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/docs/samples/functions-pubsub-system-test/

If you are creating a new function, see the [Console Quickstart](https://docs.cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ Samples ](https://docs.cloud.google.com/functions/docs/samples)



#  Pub/Sub system tests Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates how to system test a function triggered by Pub/Sub. This is an "end-to-end" test that assumes you have deployed the Cloud Function to test. The code in this example triggers the Cloud Function by publishing a Pub/Sub message and then waiting to observe expected output in Cloud Logging.

## Code sample

### Go

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    package helloworld
    
    import (
    	"context"
    	"log"
    	"os"
    	"os/exec"
    	"strings"
    	"testing"
    	"time"
    
    	"cloud.google.com/go/pubsub"
    	"github.com/gobuffalo/uuid"
    )
    
    func TestHelloPubSubSystem(t *testing.T) {
    	ctx := context.Background()
    
    	topicName := os.Getenv("FUNCTIONS_TOPIC")
    	projectID := os.Getenv("GCP_PROJECT")
    
    	startTime := time.Now().UTC().Format(time.RFC3339)
    
    	// Create the Pub/Sub client and topic.
    	client, err := pubsub.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/index.html#cloud_google_com_go_pubsub_Client_NewClient)(ctx, projectID)
    	if err != nil {
    		log.Fatal(err)
    	}
    	topic := client.Topic(topicName)
    
    	// Publish a message with a random string to verify.
    	// We use a random string to make sure the function is logging the correct
    	// message for this test invocation.
    	u := uuid.Must(uuid.NewV4())
    	msg := &pubsub.Message{
    		Data: []byte(u.String()),
    	}
    	topic.Publish(ctx, msg).Get(ctx)
    
    	// Wait for logs to be consistent.
    	time.Sleep(20 * time.Second)
    
    	// Check logs after a delay.
    	cmd := exec.Command("gcloud", "alpha", "functions", "logs", "read", "HelloPubSub", "--start-time", startTime)
    	out, err := cmd.CombinedOutput()
    	if err != nil {
    		t.Fatalf("exec.Command: %v", err)
    	}
    	if got := string(out); !strings.Contains(got, u.String()) {
    		t.Errorf("HelloPubSub got %q, want to contain %q", got, u.String())
    	}
    }
    

### Java

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import static com.google.common.truth.Truth.assertThat;
    
    import com.google.api.gax.paging.[Page](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.paging.Page.html);
    import com.google.cloud.logging.[LogEntry](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LogEntry.html);
    import com.google.cloud.logging.[Logging](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.html);
    import com.google.cloud.logging.[LoggingOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LoggingOptions.html);
    import com.google.cloud.pubsub.v1.[Publisher](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import com.google.pubsub.v1.[ProjectTopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectTopicName.html);
    import com.google.pubsub.v1.[PubsubMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html);
    import io.github.resilience4j.core.IntervalFunction;
    import io.github.resilience4j.retry.Retry;
    import io.github.resilience4j.retry.RetryConfig;
    import io.github.resilience4j.retry.RetryRegistry;
    import java.io.IOException;
    import java.nio.charset.StandardCharsets;
    import java.time.[Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html);
    import java.time.Instant;
    import java.time.format.DateTimeFormatter;
    import java.util.UUID;
    import java.util.stream.Collectors;
    import java.util.stream.StreamSupport;
    import org.junit.BeforeClass;
    import org.junit.Test;
    
    public class ExampleSystemIT {
    
      // TODO<developer>: set these values (as environment variables)
      private static final String PROJECT_ID = System.getenv("GCP_PROJECT");
      private static final String TOPIC_NAME = System.getenv("FUNCTIONS_SYSTEM_TEST_TOPIC");
    
      // TODO<developer>: set this value (as an environment variable) to HelloPubSub
      private static final String FUNCTION_DEPLOYED_NAME = System.getenv("FUNCTIONS_PUBSUB_FN_NAME");
    
      private static [Logging](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.html) loggingClient;
    
      private static [Publisher](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html) publisher;
    
      private HelloPubSub sampleUnderTest;
    
      @BeforeClass
      public static void setUp() throws IOException {
        loggingClient = [LoggingOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LoggingOptions.html).getDefaultInstance().getService();
        publisher = [Publisher](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html).newBuilder(
            [ProjectTopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectTopicName.html).of(PROJECT_ID, TOPIC_NAME)).build();
      }
    
      private static String getLogEntriesAsString(String startTimestamp) {
        // Construct Stackdriver logging filter
        // See this page for more info: https://cloud.google.com/logging/docs/view/advanced-queries
        String filter = "resource.type=\"cloud_function\""
            + " AND severity=INFO"
            + " AND resource.labels.function_name=" + FUNCTION_DEPLOYED_NAME
            + String.format(" AND timestamp>=\"%s\"", startTimestamp);
    
        // Get Stackdriver logging entries
        Page<LogEntry> logEntries =
            loggingClient.[listLogEntries](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.html#com_google_cloud_logging_Logging_listLogEntries_com_google_cloud_logging_Logging_EntryListOption____)(
                Logging.EntryListOption.filter(filter),
                Logging.EntryListOption.sortOrder(
                    Logging.SortingField.TIMESTAMP, Logging.SortingOrder.DESCENDING)
            );
    
        // Serialize Stackdriver logging entries + collect them into a single string
        String logsConcat = StreamSupport.stream(logEntries.getValues().spliterator(), false)
            .map((x) -> x.toString())
            .collect(Collectors.joining("%n"));
    
        return logsConcat;
      }
    
      @Test
      public void helloPubSub_shouldRunOnGcf() throws Exception {
        String name = UUID.randomUUID().toString();
    
        // Subtract time to work-around local-GCF clock difference
        Instant startInstant = Instant.now().minus([Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html).ofMinutes(4));
        String startTimestamp = DateTimeFormatter.ISO_INSTANT.format(startInstant);
    
        // Publish to pub/sub topic
        [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html) byteStr = [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFrom](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFrom_byte___)(name, StandardCharsets.UTF_8);
        [PubsubMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html) pubsubApiMessage = [PubsubMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html).newBuilder().[setData](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.Builder.html#com_google_pubsub_v1_PubsubMessage_Builder_setData_com_google_protobuf_ByteString_)(byteStr).build();
        [publish](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html#com_google_cloud_pubsub_v1_Publisher_publish_com_google_pubsub_v1_PubsubMessage_)er.[publish](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html#com_google_cloud_pubsub_v1_Publisher_publish_com_google_pubsub_v1_PubsubMessage_)(pubsubApiMessage).get();
    
        // Keep retrying until the logs contain the desired invocation's log entry
        // (If the invocation failed, the retry process will eventually time out)
        RetryRegistry registry = RetryRegistry.of(RetryConfig.custom()
            .maxAttempts(8)
            .intervalFunction(IntervalFunction.ofExponentialBackoff(1000, 2))
            .retryOnResult(s -> !s.toString().contains(name))
            .build());
        Retry retry = registry.retry(name);
        String logEntry = Retry
            .decorateFunction(retry, ExampleSystemIT::getLogEntriesAsString)
            .apply(startTimestamp);
    
        // Perform final assertion (to make sure we fail on timeout)
        assertThat(logEntry).contains(name);
      }
    }

### Node.js

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const childProcess = require('child_process');
    const assert = require('assert');
    const uuid = require('uuid');
    const {PubSub} = require('[@google-cloud/pubsub](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/overview.html)');
    const moment = require('moment');
    const promiseRetry = require('promise-retry');
    
    const pubsub = new [PubSub](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/pubsub.html)();
    const topicName = process.env.FUNCTIONS_TOPIC;
    if (!topicName) throw new Error('"FUNCTIONS_TOPIC" env var must be set.');
    if (!process.env.GCF_REGION) {
      throw new Error('"GCF_REGION" env var must be set.');
    }
    const baseCmd = 'gcloud functions';
    
    describe('system tests', () => {
      it('helloPubSub: should print a name', async () => {
        const name = uuid.v4();
    
        // Subtract time to work-around local-GCF clock difference
        const startTime = moment().subtract(4, 'minutes').toISOString();
    
        // Publish to pub/sub topic
        const topic = pubsub.topic(topicName);
        const data = Buffer.from(name);
        await topic.publishMessage({data});
    
        console.log(`published topic ${topicName}, ${name}`);
    
        // Wait for logs to become consistent
        await promiseRetry(retry => {
          const logs = childProcess
            .execSync(`${baseCmd} logs read helloPubSub --start-time ${startTime}`)
            .toString();
    
          try {
            assert.ok(logs.includes(`Hello, ${name}!`));
          } catch (err) {
            console.log('An error occurred, retrying:', err);
            retry(err);
          }
        });
      });

### Python

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from datetime import datetime
    from os import getenv
    import subprocess
    import time
    import uuid
    
    from google.cloud import pubsub_v1
    import pytest
    
    PROJECT = getenv("GCP_PROJECT")
    TOPIC = getenv("FUNCTIONS_TOPIC")
    
    assert PROJECT is not None
    assert TOPIC is not None
    
    
    @pytest.fixture(scope="module")
    def publisher_client():
        yield pubsub_v1.[PublisherClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.PublisherClient.html)()
    
    
    def test_print_name(publisher_client):
        start_time = datetime.utcnow().isoformat()
        topic_path = [publisher_client](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.html).topic_path(PROJECT, TOPIC)
    
        # Publish the message
        name = uuid.uuid4()
        data = str(name).encode("utf-8")
        [publisher_client](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.html).publish(topic_path, data=data).result()
    
        # Wait for logs to become consistent
        time.sleep(15)
    
        # Check logs after a delay
        log_process = subprocess.Popen(
            [
                "gcloud",
                "alpha",
                "functions",
                "logs",
                "read",
                "hello_pubsub",
                "--start-time",
                start_time,
            ],
            stdout=subprocess.PIPE,
        )
        logs = str(log_process.communicate()[0])
        assert f"Hello {name}!" in logs
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudfunctions). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
