---
url: https://docs.cloud.google.com/functions/docs/samples/functions-cloudevent-storage-unit-test/
title: Cloud Storage (2nd Gen) Unit Test \u00a0|\u00a0 Cloud Run functions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:02:44.557630+00:00
---

# Cloud Storage (2nd Gen) Unit Test  |  Cloud Run functions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/docs/samples/functions-cloudevent-storage-unit-test/

If you are creating a new function, see the [Console Quickstart](https://docs.cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ Samples ](https://docs.cloud.google.com/functions/docs/samples)



#  Cloud Storage (2nd Gen) Unit Test Stay organized with collections  Save and categorize content based on your preferences. 

Example unit test for a Cloud Storage-triggered function running on Cloud Functions (2nd Gen).

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
    	"time"
    
    	"github.com/cloudevents/sdk-go/v2/event"
    	"github.com/googleapis/google-cloudevents-go/cloud/storagedata"
    	"google.golang.org/protobuf/encoding/protojson"
    	"google.golang.org/protobuf/types/known/timestamppb"
    )
    
    func TestHelloStorage(t *testing.T) {
    	r, w, _ := os.Pipe()
    	log.SetOutput(w)
    	originalFlags := log.Flags()
    	log.SetFlags(log.Flags() &^ (log.Ldate | log.Ltime))
    
    	d := &storagedata.StorageObjectData{
    		Name:        "hello_gcs.txt",
    		TimeCreated: timestamppb.New(time.Now()),
    	}
    
    	jsonData, err := protojson.Marshal(d)
    	if err != nil {
    		t.Fatalf("protojson.Marshal: %v", err)
    	}
    
    	e := event.New()
    	e.SetDataContentType("application/json")
    	e.SetData(e.DataContentType(), jsonData)
    
    	helloStorage(context.Background(), e)
    
    	w.Close()
    	log.SetOutput(os.Stderr)
    	log.SetFlags(originalFlags)
    
    	out, err := io.ReadAll(r)
    	if err != nil {
    		t.Fatalf("ReadAll: %v", err)
    	}
    	got := string(out)
    	if want := d.Name; strings.Contains(want, got) {
    		t.Errorf("HelloStorage = %q, want to contain %q", got, want)
    	}
    	if want := d.TimeCreated.String(); strings.Contains(want, got) {
    		t.Errorf("HelloStorage = %q, want to contain %q", got, want)
    	}
    }
    

### Java

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import static com.google.common.truth.Truth.assertThat;
    
    import com.google.common.testing.TestLogHandler;
    import com.google.events.cloud.storage.v1.[StorageObjectData](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.storage.v1.StorageObjectData.html);
    import com.google.protobuf.[InvalidProtocolBufferException](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html);
    import com.google.protobuf.[Timestamp](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html);
    import com.google.protobuf.util.[JsonFormat](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.JsonFormat.html);
    import io.cloudevents.CloudEvent;
    import io.cloudevents.core.[builder](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TextFormatParseInfoTree.html#com_google_protobuf_TextFormatParseInfoTree_builder__).CloudEventBuilder;
    import java.net.URI;
    import java.util.logging.Logger;
    import org.junit.After;
    import org.junit.BeforeClass;
    import org.junit.Test;
    import org.junit.runner.RunWith;
    import org.junit.runners.JUnit4;
    
    /** Unit tests for main.java.com.example.functions.helloworld.HelloGcs. */
    @RunWith(JUnit4.class)
    public class HelloGcsTest {
      private static final TestLogHandler LOG_HANDLER = new TestLogHandler();
      private static final Logger logger = Logger.getLogger(HelloGcs.class.getName());
    
      @BeforeClass
      public static void beforeClass() throws Exception {
        logger.addHandler(LOG_HANDLER);
      }
    
      @After
      public void afterTest() {
        LOG_HANDLER.clear();
      }
    
      @Test
      public void helloGcs_shouldPrintFileName() throws [InvalidProtocolBufferException](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html) {
        // Create event data
        String file = "foo.txt";
        String bucket = "gs://test-bucket";
    
        // Get the current time in milliseconds
        long millis = System.currentTimeMillis();
    
        // Create a Timestamp object
        [Timestamp](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html) timestamp = [Timestamp](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html).newBuilder()
            .setSeconds(millis / 1000)
            .setNanos((int) ((millis % 1000) * 1000000))
            .build();
    
        [StorageObjectData](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.storage.v1.StorageObjectData.html).Builder dataBuilder = [StorageObjectData](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.storage.v1.StorageObjectData.html).newBuilder()
            .setName(file)
            .[setBucket](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.storage.v1.StorageObjectData.Builder.html#com_google_events_cloud_storage_v1_StorageObjectData_Builder_setBucket_java_lang_String_)(bucket)
            .[setMetageneration](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.storage.v1.StorageObjectData.Builder.html#com_google_events_cloud_storage_v1_StorageObjectData_Builder_setMetageneration_long_)(10)
            .[setTimeCreated](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.storage.v1.StorageObjectData.Builder.html#com_google_events_cloud_storage_v1_StorageObjectData_Builder_setTimeCreated_com_google_protobuf_Timestamp_)(timestamp)
            .[setUpdated](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.storage.v1.StorageObjectData.Builder.html#com_google_events_cloud_storage_v1_StorageObjectData_Builder_setUpdated_com_google_protobuf_Timestamp_)(timestamp);
    
        String jsonData = [JsonFormat](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.JsonFormat.html).printer().print(dataBuilder);
    
        // Construct a CloudEvent
        CloudEvent event = CloudEventBuilder.v1()
            .withId("0")
            .withType("google.storage.object.finalize")
            .withSource(URI.create("https://example.com"))
            .withData("application/json", jsonData.getBytes())
            .build();
    
        new HelloGcs().accept(event);
    
        String actualBucket = LOG_HANDLER.getStoredLogRecords().get(2).getMessage();
        String actualFile = LOG_HANDLER.getStoredLogRecords().get(3).getMessage();
        assertThat(actualFile).contains("File: " + file);
        assertThat(actualBucket).contains("Bucket: " + bucket);
      }
    
      @Test
      public void helloGcs_shouldPrintNotifyIfDataIsNull() throws [InvalidProtocolBufferException](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html) {
        // Construct a CloudEvent
        CloudEvent event = CloudEventBuilder.v1()
            .withId("0")
            .withType("google.storage.object.finalize")
            .withSource(URI.create("https://example.com"))
            .build();
    
        new HelloGcs().accept(event);
    
        String logMessage = LOG_HANDLER.getStoredLogRecords().get(2).getMessage();
        assertThat(logMessage).isEqualTo("No data found in cloud event payload!");
      }
    }
    

### Node.js

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const {getFunction} = require('@google-cloud/functions-framework/testing');
    
    describe('functions_cloudevent_storage', () => {
      const assert = require('assert');
      const sinon = require('sinon');
      require('..');
    
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
        const event = {
          id: '1234',
          type: 'mock-gcs-event',
          data: {
            bucket: 'my-bucket',
            name: 'my-file.txt',
          },
        };
    
        // Call tested function and verify its behavior
        const helloGCS = getFunction('helloGCS');
        helloGCS(event);
    
        assert(console.log.calledWith('Event ID: 1234'));
        assert(console.log.calledWith('Event Type: mock-gcs-event'));
        assert(console.log.calledWith('Bucket: my-bucket'));
        assert(console.log.calledWith('File: my-file.txt'));
      });
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
    
    
    from cloudevents.http import CloudEvent
    import pytest
    
    import main
    
    
    def test_functions_eventsource_storage(capsys: pytest.LogCaptureFixture) -> None:
        attributes = {
            "id": "5e9f24a",
            "type": "google.cloud.storage.object.v1.finalized",
            "source": "sourceUrlHere",
        }
    
        data = {
            "bucket": "test_bucket_for_storage",
            "name": "new_blob_uploaded",
            "generation": 1,
            "metageneration": 1,
            "timeCreated": "2021-10-10 00:00:00.000000Z",
            "updated": "2021-11-11 00:00:00.000000Z",
        }
    
        event = CloudEvent(attributes, data)
    
        (
            event_id,
            event_type,
            bucket,
            name,
            metageneration,
            timeCreated,
            updated,
        ) = main.hello_gcs(event)
    
        out, _ = capsys.readouterr()
        assert "5e9f24a" in event_id
        assert "google.cloud.storage.object.v1.finalized" in event_type
        assert "test_bucket_for_storage" in bucket
        assert "new_blob_uploaded" in name
        assert metageneration == 1
        assert "2021-10-10 00:00:00.000000Z" in timeCreated
        assert "2021-11-11 00:00:00.000000Z" in updated
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudfunctions). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
