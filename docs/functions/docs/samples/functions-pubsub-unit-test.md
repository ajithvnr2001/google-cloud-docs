---
url: https://docs.cloud.google.com/functions/docs/samples/functions-pubsub-unit-test/
title: Pub/Sub unit tests \u00a0|\u00a0 Cloud Run functions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:51:46.667275+00:00
---

# Pub/Sub unit tests  |  Cloud Run functions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/docs/samples/functions-pubsub-unit-test/

If you are creating a new function, see the [Console Quickstart](https://docs.cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ Samples ](https://docs.cloud.google.com/functions/docs/samples)



#  Pub/Sub unit tests Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates how to unit test a function triggered by Pub/Sub.

## Code sample

### C#

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using CloudNative.CloudEvents;
    using Google.Cloud.Functions.Testing;
    using Google.Events.Protobuf.Cloud.PubSub.V1;
    using Microsoft.Extensions.Logging;
    using System;
    using System.Threading;
    using System.Threading.Tasks;
    using Xunit;
    
    namespace HelloWorld.Tests;
    
    public class HelloPubSubUnitTest
    {
        [Fact]
        public async Task MessageWithTextData()
        {
            var data = new MessagePublishedData { Message = new PubsubMessage { TextData = "PubSub user" } };
            var cloudEvent = new CloudEvent
            {
                Type = MessagePublishedData.MessagePublishedCloudEventType,
                Source = new Uri("//pubsub.googleapis.com", UriKind.RelativeOrAbsolute),
                Id = Guid.NewGuid().ToString(),
                Time = DateTimeOffset.UtcNow,
                Data = data
            };
    
            var logger = new MemoryLogger<HelloPubSub.Function>();
            var function = new HelloPubSub.Function(logger);
            await function.HandleAsync(cloudEvent, data, CancellationToken.None);
    
            var logEntry = Assert.Single(logger.ListLogEntries());
            Assert.Equal("Hello PubSub user", logEntry.Message);
            Assert.Equal(LogLevel.Information, logEntry.Level);
        }
    
        [Fact]
        public async Task MessageWithoutTextData()
        {
            var data = new MessagePublishedData
            {
                Message = new PubsubMessage { Attributes = { { "key", "value" } } }
            };
            var cloudEvent = new CloudEvent
            {
                Type = MessagePublishedData.MessagePublishedCloudEventType,
                Source = new Uri("//pubsub.googleapis.com", UriKind.RelativeOrAbsolute),
                Id = Guid.NewGuid().ToString(),
                Time = DateTimeOffset.UtcNow
            };
    
            var logger = new MemoryLogger<HelloPubSub.Function>();
            var function = new HelloPubSub.Function(logger);
            await function.HandleAsync(cloudEvent, data, CancellationToken.None);
    
            var logEntry = Assert.Single(logger.ListLogEntries());
            Assert.Equal("Hello world", logEntry.Message);
            Assert.Equal(LogLevel.Information, logEntry.Level);
        }
    }

### Go

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    package helloworld
    
    import (
    	"context"
    	"io"
    	"log"
    	"os"
    	"testing"
    )
    
    func TestHelloPubSub(t *testing.T) {
    	tests := []struct {
    		data string
    		want string
    	}{
    		{want: "Hello, World!\n"},
    		{data: "Go", want: "Hello, Go!\n"},
    	}
    	for _, test := range tests {
    		r, w, _ := os.Pipe()
    		log.SetOutput(w)
    		originalFlags := log.Flags()
    		log.SetFlags(log.Flags() &^ (log.Ldate | log.Ltime))
    
    		m := PubSubMessage{
    			Data: []byte(test.data),
    		}
    		HelloPubSub(context.Background(), m)
    
    		w.Close()
    		log.SetOutput(os.Stderr)
    		log.SetFlags(originalFlags)
    
    		out, err := io.ReadAll(r)
    		if err != nil {
    			t.Fatalf("ReadAll: %v", err)
    		}
    		if got := string(out); got != test.want {
    			t.Errorf("HelloPubSub(%q) = %q, want %q", test.data, got, test.want)
    		}
    	}
    }
    

### Java

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import static com.google.common.truth.Truth.assertThat;
    
    import com.google.common.testing.TestLogHandler;
    import functions.eventpojos.PubsubMessage;
    import java.nio.charset.StandardCharsets;
    import java.util.Base64;
    import java.util.logging.Logger;
    import org.junit.Before;
    import org.junit.Test;
    import org.junit.runner.RunWith;
    import org.junit.runners.JUnit4;
    
    /**
     * Unit tests for main.java.com.example.functions.helloworld.HelloPubSub.
     */
    @RunWith(JUnit4.class)
    public class HelloPubSubTest {
    
      private HelloPubSub sampleUnderTest;
      private static final Logger logger = Logger.getLogger(HelloPubSub.class.getName());
    
      private static final TestLogHandler LOG_HANDLER = new TestLogHandler();
    
      @Before
      public void setUp() {
        sampleUnderTest = new HelloPubSub();
        logger.addHandler(LOG_HANDLER);
        LOG_HANDLER.clear();
      }
    
      @Test
      public void helloPubSub_shouldPrintName() {
        PubsubMessage pubSubMessage = new PubsubMessage();
        pubSubMessage.setData(Base64.getEncoder().encodeToString(
            "John".getBytes(StandardCharsets.UTF_8)));
        sampleUnderTest.accept(pubSubMessage, null);
    
        String logMessage = LOG_HANDLER.getStoredLogRecords().get(0).getMessage();
        assertThat("Hello John!").isEqualTo(logMessage);
      }
    
      @Test
      public void helloPubSub_shouldPrintHelloWorld() {
        PubsubMessage pubSubMessage = new PubsubMessage();
        sampleUnderTest.accept(pubSubMessage, null);
    
        String logMessage = LOG_HANDLER.getStoredLogRecords().get(0).getMessage();
        assertThat("Hello world!").isEqualTo(logMessage);
      }
    }

### Node.js

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const assert = require('assert');
    const uuid = require('uuid');
    const sinon = require('sinon');
    
    const {helloPubSub} = require('..');
    
    const stubConsole = function () {
      sinon.stub(console, 'error');
      sinon.stub(console, 'log');
    };
    
    const restoreConsole = function () {
      console.log.restore();
      console.error.restore();
    };
    
    beforeEach(stubConsole);
    afterEach(restoreConsole);
    
    it('helloPubSub: should print a name', () => {
      // Create mock Pub/Sub event
      const name = uuid.v4();
      const event = {
        data: Buffer.from(name).toString('base64'),
      };
    
      // Call tested function and verify its behavior
      helloPubSub(event);
      assert.ok(console.log.calledWith(`Hello, ${name}!`));
    });

### PHP

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    namespace Google\Cloud\Samples\Functions\HelloworldPubsub\Test;
    
    use CloudEvents\V1\CloudEventImmutable;
    use CloudEvents\V1\CloudEventInterface;
    use PHPUnit\Framework\TestCase;
    
    /**
     * Class SampleUnitTest.
     *
     * Unit test for 'Helloworld Pub/Sub' Cloud Function.
     */
    class SampleUnitTest extends TestCase
    {
        /**
         * Include the Cloud Function code before running any tests.
         *
         * @see https://phpunit.readthedocs.io/en/latest/fixtures.html
         */
        public static function setUpBeforeClass(): void
        {
            require_once __DIR__ . '/index.php';
        }
    
        public function dataProvider()
        {
            return [
                [
                    'cloudevent' => new CloudEventImmutable(
                        uniqId(), // id
                        'pubsub.googleapis.com', // source
                        'google.cloud.pubsub.topic.v1.messagePublished', // type
                        [
                            'data' => base64_encode('John')
                        ]
                    ),
                    'expected' => 'Hello, John!'
                ],
            ];
        }
    
        /**
         * @dataProvider dataProvider
         */
        public function testFunction(
            CloudEventInterface $cloudevent,
            string $expected
        ): void {
            // Capture function output by overriding the function's logging behavior.
            // The 'LOGGER_OUTPUT' environment variable must be used in your function:
            //
            // $log = fopen(getenv('LOGGER_OUTPUT') ?: 'php://stderr', 'wb');
            // fwrite($log, 'Log Entry');
            putenv('LOGGER_OUTPUT=php://output');
            helloworldPubsub($cloudevent);
            // Provided by PHPUnit\Framework\TestCase.
            $actual = $this->getActualOutput();
    
            // Test that output includes the expected value.
            $this->assertStringContainsString($expected, $actual);
        }
    }
    

### Python

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import base64
    
    from unittest import mock
    
    import main
    
    
    mock_context = mock.Mock()
    mock_context.event_id = "617187464135194"
    mock_context.timestamp = "2019-07-15T22:09:03.761Z"
    mock_context.resource = {
        "name": "projects/my-project/topics/my-topic",
        "service": "pubsub.googleapis.com",
        "type": "type.googleapis.com/google.pubsub.v1.PubsubMessage",
    }
    
    
    def test_print_hello_world(capsys):
        data = {}
    
        # Call tested function
        main.hello_pubsub(data, mock_context)
        out, err = capsys.readouterr()
        assert "Hello World!" in out
    
    
    def test_print_name(capsys):
        name = "test"
        data = {"data": base64.b64encode(name.encode())}
    
        # Call tested function
        main.hello_pubsub(data, mock_context)
        out, err = capsys.readouterr()
        assert f"Hello {name}!\n" in out
    
    

### Ruby

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "minitest/autorun"
    require "functions_framework/testing"
    require "base64"
    
    describe "functions_helloworld_pubsub" do
      include FunctionsFramework::Testing
    
      let(:resource_type) { "type.googleapis.com/google.pubsub.v1.PubsubMessage" }
      let(:source) { "//pubsub.googleapis.com/projects/sample-project/topics/gcf-test" }
      let(:type) { "google.cloud.pubsub.topic.v1.messagePublished" }
    
      it "prints a name" do
        load_temporary "helloworld/pubsub/app.rb" do
          payload = { "@type" => resource_type, "message" => { "data" => Base64.encode64("Ruby") } }
          event = make_cloud_event payload, source: source, type: type
          _out, err = capture_subprocess_io do
            # Call tested function
            call_event "hello_pubsub", event
          end
          assert_match(/Hello, Ruby!/, err)
        end
      end
    
      it "prints hello world" do
        load_temporary "helloworld/pubsub/app.rb" do
          payload = { "@type" => resource_type, "message" => { "data" => nil } }
          event = make_cloud_event payload, source: source, type: type
          _out, err = capture_subprocess_io do
            # Call tested function
            call_event "hello_pubsub", event
          end
          assert_match(/Hello, World!/, err)
        end
      end
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudfunctions). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
