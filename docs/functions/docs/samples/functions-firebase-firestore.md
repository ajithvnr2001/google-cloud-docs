---
url: https://docs.cloud.google.com/functions/docs/samples/functions-firebase-firestore/
title: Firestore trigger \u00a0|\u00a0 Cloud Run functions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:51:57.998324+00:00
---

# Firestore trigger  |  Cloud Run functions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/docs/samples/functions-firebase-firestore/

If you are creating a new function, see the [Console Quickstart](https://docs.cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ Samples ](https://docs.cloud.google.com/functions/docs/samples)



#  Firestore trigger Stay organized with collections  Save and categorize content based on your preferences. 

Triggers a function in response to a Firestore database update.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Google Cloud Firestore triggers (1st gen)](https://docs.cloud.google.com/functions/1stgendocs/calling/cloud-firestore-1st-gen)



## Code sample

### C#

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using CloudNative.CloudEvents;
    using Google.Cloud.Functions.Framework;
    using Google.Events.Protobuf.Cloud.Firestore.V1;
    using Microsoft.Extensions.Logging;
    using System.Collections.Generic;
    using System.Linq;
    using System.Threading;
    using System.Threading.Tasks;
    
    namespace FirebaseFirestore;
    
    public class Function : ICloudEventFunction<DocumentEventData>
    {
        private readonly ILogger _logger;
    
        public Function(ILogger<Function> logger) =>
            _logger = logger;
    
        public Task HandleAsync(CloudEvent cloudEvent, DocumentEventData data, CancellationToken cancellationToken)
        {
            _logger.LogInformation("Function triggered by event on {subject}", cloudEvent.Subject);
            _logger.LogInformation("Event type: {type}", cloudEvent.Type);
            MaybeLogDocument("Old value", data.OldValue);
            MaybeLogDocument("New value", data.Value);
    
            // In this example, we don't need to perform any asynchronous operations, so the
            // method doesn't need to be declared async.
            return Task.CompletedTask;
        }
    
        /// <summary>
        /// Logs the names and values of the fields in a document in a very simplistic way.
        /// </summary>
        private void MaybeLogDocument(string message, Document document)
        {
            if (document is null)
            {
                return;
            }
    
            // ConvertFields converts the Firestore representation into a .NET-friendly
            // representation.
            IReadOnlyDictionary<string, object> fields = document.ConvertFields();
            var fieldNamesAndTypes = fields
                .OrderBy(pair => pair.Key)
                .Select(pair => $"{pair.Key}: {pair.Value}");
            _logger.LogInformation(message + ": {fields}", string.Join(", ", fieldNamesAndTypes));
        }
    }

### Go

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Package hello contains a Cloud Function triggered by a Firestore event.
    package hello
    
    import (
    	"context"
    	"fmt"
    	"log"
    	"time"
    
    	"cloud.google.com/go/functions/metadata"
    )
    
    // FirestoreEvent is the payload of a Firestore event.
    type FirestoreEvent struct {
    	OldValue   FirestoreValue `json:"oldValue"`
    	Value      FirestoreValue `json:"value"`
    	UpdateMask struct {
    		FieldPaths []string `json:"fieldPaths"`
    	} `json:"updateMask"`
    }
    
    // FirestoreValue holds Firestore fields.
    type FirestoreValue struct {
    	CreateTime time.Time `json:"createTime"`
    	// Fields is the data for this value. The type depends on the format of your
    	// database. Log the interface{} value and inspect the result to see a JSON
    	// representation of your database fields.
    	Fields     interface{} `json:"fields"`
    	Name       string      `json:"name"`
    	UpdateTime time.Time   `json:"updateTime"`
    }
    
    // HelloFirestore is triggered by a change to a Firestore document.
    func HelloFirestore(ctx context.Context, e FirestoreEvent) error {
    	meta, err := metadata.[FromContext](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/functions/latest/metadata.html#cloud_google_com_go_functions_metadata_Metadata_FromContext)(ctx)
    	if err != nil {
    		return fmt.Errorf("metadata.FromContext: %w", err)
    	}
    	log.Printf("Function triggered by change to: %v", meta.[Resource](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/functions/latest/metadata.html#cloud_google_com_go_functions_metadata_Resource))
    	log.Printf("Old value: %+v", e.OldValue)
    	log.Printf("New value: %+v", e.Value)
    	return nil
    }
    

### Java

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.functions.Context;
    import com.google.cloud.functions.RawBackgroundFunction;
    import com.google.gson.Gson;
    import com.google.gson.JsonObject;
    import java.util.logging.Logger;
    
    public class FirebaseFirestore implements RawBackgroundFunction {
      private static final Logger logger = Logger.getLogger(FirebaseFirestore.class.getName());
    
      // Use GSON (https://github.com/google/gson) to parse JSON content.
      private static final Gson gson = new Gson();
    
      @Override
      public void accept(String json, Context context) {
        JsonObject body = gson.fromJson(json, JsonObject.class);
        logger.info("Function triggered by event on: " + context.resource());
        logger.info("Event type: " + context.eventType());
    
        if (body != null && body.has("oldValue")) {
          logger.info("Old value:");
          logger.info(body.get("oldValue").getAsString());
        }
    
        if (body != null && body.has("value")) {
          logger.info("New value:");
          logger.info(body.get("value").getAsString());
        }
      }
    }
    

### Node.js

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * Background Function triggered by a change to a Firestore document.
     *
     * @param {!Object} event The Cloud Functions event.
     * @param {!Object} context Cloud Functions event metadata.
     */
    exports.helloFirestore = (event, context) => {
      const triggerResource = context.resource;
    
      console.log(`Function triggered by event on: ${triggerResource}`);
      console.log(`Event type: ${context.eventType}`);
    
      if (event.oldValue && Object.keys(event.oldValue).length) {
        console.log('\nOld value:');
        console.log(JSON.stringify(event.oldValue, null, 2));
      }
    
      if (event.value && Object.keys(event.value).length) {
        console.log('\nNew value:');
        console.log(JSON.stringify(event.value, null, 2));
      }
    };

### PHP

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\CloudFunctions\CloudEvent;
    
    function firebaseFirestore(CloudEvent $cloudevent)
    {
        $log = fopen(getenv('LOGGER_OUTPUT') ?: 'php://stderr', 'wb');
    
        fwrite($log, 'Event: ' . $cloudevent->getId() . PHP_EOL);
        fwrite($log, 'Event Type: ' . $cloudevent->getType() . PHP_EOL);
    
        $data = $cloudevent->getData();
    
        $resource = $data['resource'];
        fwrite($log, 'Function triggered by event on: ' . $resource . PHP_EOL);
    
        if (isset($data['oldValue'])) {
            fwrite($log, 'Old value: ' . json_encode($data['oldValue']) . PHP_EOL);
        }
    
        if (isset($data['value'])) {
            fwrite($log, 'New value: ' . json_encode($data['value']) . PHP_EOL);
        }
    }

### Python

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import json
    
    def hello_firestore(data, context):
        """Triggered by a change to a Firestore document.
        Args:
            data (dict): The event payload.
            context (google.cloud.functions.Context): Metadata for the event.
        """
        trigger_resource = context.resource
    
        print("Function triggered by change to: %s" % trigger_resource)
    
        print("\nOld value:")
        print(json.dumps(data["oldValue"]))
    
        print("\nNew value:")
        print(json.dumps(data["value"]))
    
    

### Ruby

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "functions_framework"
    
    # Triggered by a change to a Firestore document.
    FunctionsFramework.cloud_event "hello_firestore" do |event|
      # The event parameter is a CloudEvents::Event::V1 object.
      # See https://cloudevents.github.io/sdk-ruby/latest/CloudEvents/Event/V1.html
      payload = event.data
    
      logger.info "Function triggered by change to: #{event.source}"
      logger.info "Old value: #{payload['oldValue']}"
      logger.info "New value: #{payload['value']}"
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudfunctions). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
