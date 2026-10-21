---
url: https://docs.cloud.google.com/functions/docs/samples/functions-firebase-rtdb/
title: Firebase RTDB trigger \u00a0|\u00a0 Cloud Run functions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:03:35.390202+00:00
---

# Firebase RTDB trigger  |  Cloud Run functions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/docs/samples/functions-firebase-rtdb/

If you are creating a new function, see the [Console Quickstart](https://docs.cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ Samples ](https://docs.cloud.google.com/functions/docs/samples)



#  Firebase RTDB trigger Stay organized with collections  Save and categorize content based on your preferences. 

Triggers a function when a Firebase realtime database is updated.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Firebase Realtime Database Triggers](https://docs.cloud.google.com/functions/1stgendocs/calling/realtime-database)



## Code sample

### C#

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using CloudNative.CloudEvents;
    using Google.Cloud.Functions.Framework;
    using Google.Events.Protobuf.Firebase.Database.V1;
    using Microsoft.Extensions.Logging;
    using System.Threading;
    using System.Threading.Tasks;
    
    namespace FirebaseRtdb;
    
    public class Function : ICloudEventFunction<ReferenceEventData>
    {
        private readonly ILogger _logger;
    
        public Function(ILogger<Function> logger) =>
            _logger = logger;
    
        public Task HandleAsync(CloudEvent cloudEvent, ReferenceEventData data, CancellationToken cancellationToken)
        {
            _logger.LogInformation("Function triggered by change to {subject}", cloudEvent.Subject);
            _logger.LogInformation("Delta: {delta}", data.Delta);
    
            // In this example, we don't need to perform any asynchronous operations, so the
            // method doesn't need to be declared async.
            return Task.CompletedTask;
        }
    }

### Go

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Package p contains a Cloud Function triggered by a Firebase Realtime Database
    // event.
    package p
    
    import (
    	"context"
    	"fmt"
    	"log"
    
    	"cloud.google.com/go/functions/metadata"
    )
    
    // RTDBEvent is the payload of a RTDB event.
    type RTDBEvent struct {
    	Data  interface{} `json:"data"`
    	Delta interface{} `json:"delta"`
    }
    
    // HelloRTDB handles changes to a Firebase RTDB.
    func HelloRTDB(ctx context.Context, e RTDBEvent) error {
    	meta, err := metadata.[FromContext](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/functions/latest/metadata.html#cloud_google_com_go_functions_metadata_Metadata_FromContext)(ctx)
    	if err != nil {
    		return fmt.Errorf("metadata.FromContext: %w", err)
    	}
    	log.Printf("Function triggered by change to: %v", meta.[Resource](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/functions/latest/metadata.html#cloud_google_com_go_functions_metadata_Resource))
    	log.Printf("%+v", e)
    	return nil
    }
    

### Java

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.functions.Context;
    import com.google.cloud.functions.RawBackgroundFunction;
    import com.google.gson.Gson;
    import com.google.gson.JsonObject;
    import java.util.logging.Logger;
    
    public class FirebaseRtdb implements RawBackgroundFunction {
      private static final Logger logger = Logger.getLogger(FirebaseRtdb.class.getName());
    
      // Use GSON (https://github.com/google/gson) to parse JSON content.
      private static final Gson gson = new Gson();
    
      @Override
      public void accept(String json, Context context) {
        logger.info("Function triggered by change to: " + context.resource());
    
        JsonObject body = gson.fromJson(json, JsonObject.class);
    
        boolean isAdmin = false;
        if (body != null && body.has("auth")) {
          JsonObject authObj = body.getAsJsonObject("auth");
          isAdmin = authObj.has("admin") && authObj.get("admin").getAsBoolean();
        }
    
        logger.info("Admin?: " + isAdmin);
    
        if (body != null && body.has("delta")) {
          logger.info("Delta:");
          logger.info(body.get("delta").toString());
        }
      }
    }
    

### Node.js

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * Background Function triggered by a change to a Firebase RTDB reference.
     *
     * @param {!Object} event The Cloud Functions event.
     * @param {!Object} context The Cloud Functions event context.
     */
    exports.helloRTDB = (event, context) => {
      const triggerResource = context.resource;
    
      console.log(`Function triggered by change to: ${triggerResource}`);
      console.log(`Admin?: ${!!context.auth.admin}`);
      console.log('Delta:');
      console.log(JSON.stringify(event.delta, null, 2));
    };

### PHP

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\CloudFunctions\CloudEvent;
    
    function firebaseRTDB(CloudEvent $cloudevent)
    {
        $log = fopen(getenv('LOGGER_OUTPUT') ?: 'php://stderr', 'wb');
    
        fwrite($log, 'Event: ' . $cloudevent->getId() . PHP_EOL);
    
        $data = $cloudevent->getData();
        $resource = $data['resource'] ?? '<null>';
    
        fwrite($log, 'Function triggered by change to: ' . $resource . PHP_EOL);
    
        $isAdmin = isset($data['auth']['admin']) && $data['auth']['admin'] == true;
    
        fwrite($log, 'Admin?: ' . var_export($isAdmin, true) . PHP_EOL);
        fwrite($log, 'Delta: ' . json_encode($data['delta'] ?? '') . PHP_EOL);
    }

### Python

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import json
    
    def hello_rtdb(data, context):
        """Triggered by a change to a Firebase RTDB reference.
        Args:
            data (dict): The event payload.
            context (google.cloud.functions.Context): Metadata for the event.
        """
        trigger_resource = context.resource
    
        print("Function triggered by change to: %s" % trigger_resource)
        print("Admin?: %s" % data.get("admin", False))
        print("Delta:")
        print(json.dumps(data["delta"]))
    
    

### Ruby

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "functions_framework"
    
    # Triggered by a change to a Firebase RTDB document.
    FunctionsFramework.cloud_event "hello_rtdb" do |event|
      # Event-triggered Ruby functions receive a CloudEvents::Event::V1 object.
      # See https://cloudevents.github.io/sdk-ruby/latest/CloudEvents/Event/V1.html
      # The Firebase event payload can be obtained from the `data` field.
      payload = event.data
    
      logger.info "Function triggered by change to: #{event.source}"
      logger.info "Admin?: #{payload.fetch 'admin', false}"
      logger.info "Delta: #{payload['delta']}"
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudfunctions). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
