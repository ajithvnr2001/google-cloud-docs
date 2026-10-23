---
url: https://docs.cloud.google.com/functions/docs/samples/functions-storage-unit-test/
title: Cloud Storage unit tests \u00a0|\u00a0 Cloud Run functions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:02:43.987303+00:00
---

# Cloud Storage unit tests  |  Cloud Run functions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/docs/samples/functions-storage-unit-test/

If you are creating a new function, see the [Console Quickstart](https://docs.cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ Samples ](https://docs.cloud.google.com/functions/docs/samples)



#  Cloud Storage unit tests Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates how to unit test a function triggered by Cloud Storage.

## Code sample

### C#

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using CloudNative.CloudEvents;
    using Google.Cloud.Functions.Testing;
    using Google.Events;
    using Google.Events.Protobuf.Cloud.Storage.V1;
    using Microsoft.Extensions.Logging;
    using System;
    using System.Threading;
    using System.Threading.Tasks;
    using Xunit;
    
    namespace HelloWorld.Tests;
    
    public class HelloGcsUnitTest
    {
        [Fact]
        public async Task FileNameIsLogged()
        {
            // Prepare the inputs
            var data = new StorageObjectData { Name = "new-file.txt" };
            var cloudEvent = new CloudEvent
            {
                Type = StorageObjectData.FinalizedCloudEventType,
                Source = new Uri("//storage.googleapis.com", UriKind.RelativeOrAbsolute),
                Id = "1234",
                Data = data
            };
            var logger = new MemoryLogger<HelloGcs.Function>();
    
            // Execute the function
            var function = new HelloGcs.Function(logger);
            await function.HandleAsync(cloudEvent, data, CancellationToken.None);
    
            // Check the log results - just the entry starting with "File:".
            var logEntry = Assert.Single(logger.ListLogEntries(), entry => entry.Message.StartsWith("File:"));
            Assert.Equal("File: new-file.txt", logEntry.Message);
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
    	"strings"
    	"testing"
    
    	"cloud.google.com/go/functions/metadata"
    )
    
    func TestHelloGCS(t *testing.T) {
    	r, w, _ := os.Pipe()
    	log.SetOutput(w)
    	originalFlags := log.Flags()
    	log.SetFlags(log.Flags() &^ (log.Ldate | log.Ltime))
    
    	name := "hello_gcs.txt"
    	e := GCSEvent{
    		Name: name,
    	}
    	meta := &metadata.[Metadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/functions/latest/metadata.html#cloud_google_com_go_functions_metadata_Metadata){
    		EventID: "event ID",
    	}
    	ctx := metadata.[NewContext](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/functions/latest/metadata.html#cloud_google_com_go_functions_metadata_NewContext)(context.Background(), meta)
    
    	HelloGCS(ctx, e)
    
    	w.Close()
    	log.SetOutput(os.Stderr)
    	log.SetFlags(originalFlags)
    
    	out, err := io.ReadAll(r)
    	if err != nil {
    		t.Fatalf("ReadAll: %v", err)
    	}
    
    	got := string(out)
    	wants := []string{
    		"File: " + name,
    		"Event ID: " + meta.EventID,
    	}
    	for _, want := range wants {
    		if !strings.Contains(got, want) {
    			t.Errorf("HelloGCS(%v) = %q, want to contain %q", e, got, want)
    		}
    	}
    }
    

### Java

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import static com.google.common.truth.Truth.assertThat;
    
    import com.google.common.testing.TestLogHandler;
    import functions.eventpojos.GcsEvent;
    import functions.eventpojos.MockContext;
    import java.util.logging.Logger;
    import org.junit.After;
    import org.junit.Before;
    import org.junit.Test;
    
    /**
     * Unit tests for main.java.com.example.functions.helloworld.HelloGcs.
     */
    public class HelloGcsTest {
      private static final TestLogHandler LOG_HANDLER = new TestLogHandler();
      private static final Logger logger = Logger.getLogger(HelloGcs.class.getName());
    
      @Before
      public void beforeTest() throws Exception {
        logger.addHandler(LOG_HANDLER);
      }
    
      @After
      public void afterTest() {
        LOG_HANDLER.clear();
      }
    
      @Test
      public void helloGcs_shouldPrintFileName() {
        GcsEvent event = new GcsEvent();
        event.setName("foo.txt");
    
        MockContext context = new MockContext();
        context.eventType = "google.storage.object.finalize";
    
        new HelloGcs().accept(event, context);
    
        String message = LOG_HANDLER.getStoredLogRecords().get(3).getMessage();
        assertThat(message).contains("File: foo.txt");
      }
    }

### Node.js

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const assert = require('assert');
    const uuid = require('uuid');
    const sinon = require('sinon');
    
    const {helloGCS} = require('..');
    
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
    
    it('helloGCS: should print out event', () => {
      // Initialize mocks
      const filename = uuid.v4();
      const eventType = 'google.storage.object.finalize';
      const event = {
        name: filename,
        resourceState: 'exists',
        metageneration: '1',
      };
      const context = {
        eventId: 'g1bb3r1sh',
        eventType: eventType,
      };
    
      // Call tested function and verify its behavior
      helloGCS(event, context);
      assert.ok(console.log.calledWith(`  File: ${filename}`));
      assert.ok(console.log.calledWith(`  Event Type: ${eventType}`));
    });

### PHP

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    namespace Google\Cloud\Samples\Functions\HelloworldStorage\Test;
    
    use CloudEvents\V1\CloudEventImmutable;
    use CloudEvents\V1\CloudEventInterface;
    
    use PHPUnit\Framework\TestCase;
    
    /**
     * Class SampleUnitTest.
     *
     * Unit test for 'Helloworld Storage' Cloud Function.
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
                        'storage.googleapis.com', // source
                        'google.cloud.storage.object.v1.finalized', // type
                        [
                            'bucket' => 'some-bucket',
                            'metageneration' => '1',
                            'name' => 'folder/friendly.txt',
                            'timeCreated' => '2020-04-23T07:38:57.230Z',
                            'updated' => '2020-04-23T07:38:57.230Z',
                        ] // data
                    ),
                    'statusCode' => '200',
                ],
            ];
        }
    
        /**
         * @dataProvider dataProvider
         */
        public function testFunction(CloudEventInterface $cloudevent): void
        {
            // Capture function output by overriding the function's logging behavior.
            // The 'LOGGER_OUTPUT' environment variable must be used in your function:
            //
            // $log = fopen(getenv('LOGGER_OUTPUT') ?: 'php://stderr', 'wb');
            // fwrite($log, 'Log Entry');
            putenv('LOGGER_OUTPUT=php://output');
            helloGCS($cloudevent);
            // Provided by PHPUnit\Framework\TestCase.
            $actual = $this->getActualOutput();
    
            // Test output includes the properties provided in the CloudEvent.
            foreach ($cloudevent->getData() as $property => $value) {
                $this->assertStringContainsString($value, $actual);
            }
            $this->assertStringContainsString($cloudevent->getId(), $actual);
            $this->assertStringContainsString($cloudevent->getType(), $actual);
        }
    }
    

### Python

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from unittest import mock
    
    import main
    
    
    def test_print(capsys):
        name = "test"
        event = {
            "bucket": "some-bucket",
            "name": name,
            "metageneration": "some-metageneration",
            "timeCreated": "0",
            "updated": "0",
        }
    
        context = mock.MagicMock()
        context.event_id = "some-id"
        context.event_type = "gcs-event"
    
        # Call tested function
        main.hello_gcs(event, context)
        out, err = capsys.readouterr()
        assert f"File: {name}\n" in out
    
    

### Ruby

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "minitest/autorun"
    require "functions_framework/testing"
    require "date"
    
    describe "functions_helloworld_storage" do
      include FunctionsFramework::Testing
    
      let(:source) { "//storage.googleapis.com/projects/sample-project/buckets/sample-bucket/objects/ruby-rocks.rb" }
      let(:type) { "google.cloud.storage.object.v1.finalized" }
    
      it "responds to generic event" do
        load_temporary "helloworld/storage/app.rb" do
          timestamp = DateTime.new(2020, 2, 3, 4, 5, 6).rfc3339
          payload = {
            "bucket"         => "sample-bucket",
            "name"           => "ruby-rocks.rb",
            "metageneration" => "1",
            "timeCreated"    => timestamp,
            "updated"        => timestamp
          }
          event = make_cloud_event payload, source: source, type: type
          _out, err = capture_subprocess_io do
            call_event "hello_gcs", event
          end
    
          assert_match(/Event: /, err)
          assert_match(/Event Type: google.cloud.storage.object.v1.finalized/, err)
          assert_match(/Bucket: sample-bucket/, err)
          assert_match(/File: ruby-rocks.rb/, err)
          assert_match(/Metageneration: 1/, err)
          assert_match(/Created: 2020-02-03T04:05:06\+00:00/, err)
          assert_match(/Updated: 2020-02-03T04:05:06\+00:00/, err)
        end
      end
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudfunctions). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
