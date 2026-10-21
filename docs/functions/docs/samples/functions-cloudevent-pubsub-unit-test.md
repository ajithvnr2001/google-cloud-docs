---
url: https://docs.cloud.google.com/functions/docs/samples/functions-cloudevent-pubsub-unit-test/
title: Cloud Pub/Sub (2nd Gen) Unit Test \u00a0|\u00a0 Cloud Run functions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:03:34.026671+00:00
---

# Cloud Pub/Sub (2nd Gen) Unit Test  |  Cloud Run functions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/docs/samples/functions-cloudevent-pubsub-unit-test/

If you are creating a new function, see the [Console Quickstart](https://docs.cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ Samples ](https://docs.cloud.google.com/functions/docs/samples)



#  Cloud Pub/Sub (2nd Gen) Unit Test Stay organized with collections  Save and categorize content based on your preferences. 

Example unit test for a Cloud Pub/Sub-triggered function running on Cloud Functions (2nd Gen).

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
    
    	"github.com/cloudevents/sdk-go/v2/event"
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
    		msg := MessagePublishedData{
    			Message: m,
    		}
    		e := event.New()
    		e.SetDataContentType("application/json")
    		e.SetData(e.DataContentType(), msg)
    
    		helloPubSub(context.Background(), e)
    
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
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudfunctions). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
