---
url: https://docs.cloud.google.com/functions/docs/samples/functions-firebase-remote-config/
title: Firebase remote config \u00a0|\u00a0 Cloud Run functions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:51:22.461457+00:00
---

# Firebase remote config  |  Cloud Run functions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/docs/samples/functions-firebase-remote-config/

If you are creating a new function, see the [Console Quickstart](https://docs.cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ Samples ](https://docs.cloud.google.com/functions/docs/samples)



#  Firebase remote config Stay organized with collections  Save and categorize content based on your preferences. 

Process changes to Firebase remote config values.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Firebase Remote Config Triggers](https://docs.cloud.google.com/functions/1stgendocs/calling/firebase-remote-config)



## Code sample

### C#

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using CloudNative.CloudEvents;
    using Google.Cloud.Functions.Framework;
    using Google.Events.Protobuf.Firebase.RemoteConfig.V1;
    using Microsoft.Extensions.Logging;
    using System.Threading;
    using System.Threading.Tasks;
    
    namespace FirebaseRemoteConfig;
    
    public class Function : ICloudEventFunction<RemoteConfigEventData>
    {
        private readonly ILogger _logger;
    
        public Function(ILogger<Function> logger) =>
            _logger = logger;
    
        public Task HandleAsync(CloudEvent cloudEvent, RemoteConfigEventData data, CancellationToken cancellationToken)
        {
            _logger.LogInformation("Update type: {origin}", data.UpdateType);
            _logger.LogInformation("Update origin: {origin}", data.UpdateOrigin);
            _logger.LogInformation("Version number: {version}", data.VersionNumber);
    
            // In this example, we don't need to perform any asynchronous operations, so the
            // method doesn't need to be declared async.
            return Task.CompletedTask;
        }
    }

### Go

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Package helloworld provides a set of Cloud Functions samples.
    package helloworld
    
    import (
    	"context"
    	"log"
    )
    
    // A RemoteConfigEvent is an event triggered by Firebase Remote Config.
    type RemoteConfigEvent struct {
    	UpdateOrigin string `json:"updateOrigin"`
    	UpdateType   string `json:"updateType"`
    	UpdateUser   struct {
    		Email    string `json:"email"`
    		ImageURL string `json:"imageUrl"`
    		Name     string `json:"name"`
    	} `json:"updateUser"`
    	VersionNumber string `json:"versionNumber"`
    }
    
    // HelloRemoteConfig handles Firebase Remote Config events.
    func HelloRemoteConfig(ctx context.Context, e RemoteConfigEvent) error {
    	log.Printf("Update type: %v", e.UpdateType)
    	log.Printf("Origin: %v", e.UpdateOrigin)
    	log.Printf("Version: %v", e.VersionNumber)
    	return nil
    }
    

### Java

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.functions.Context;
    import com.google.cloud.functions.RawBackgroundFunction;
    import com.google.gson.Gson;
    import com.google.gson.JsonObject;
    import java.util.logging.Logger;
    
    public class FirebaseRemoteConfig implements RawBackgroundFunction {
      private static final Logger logger = Logger.getLogger(FirebaseRemoteConfig.class.getName());
    
      // Use GSON (https://github.com/google/gson) to parse JSON content.
      private static final Gson gson = new Gson();
    
      @Override
      public void accept(String json, Context context) {
        JsonObject body = gson.fromJson(json, JsonObject.class);
    
        if (body != null) {
          if (body.has("updateType")) {
            logger.info("Update type: " + body.get("updateType").getAsString());
          }
          if (body.has("updateOrigin")) {
            logger.info("Origin: " + body.get("updateOrigin").getAsString());
          }
          if (body.has("versionNumber")) {
            logger.info("Version: " + body.get("versionNumber").getAsString());
          }
        }
      }
    }
    

### Node.js

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * Background Function triggered by a change to a Firebase Remote Config value.
     *
     * @param {object} event The Cloud Functions event.
     */
    exports.helloRemoteConfig = event => {
      console.log(`Update type: ${event.updateType}`);
      console.log(`Origin: ${event.updateOrigin}`);
      console.log(`Version: ${event.versionNumber}`);
    };

### PHP

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\CloudFunctions\CloudEvent;
    
    function firebaseRemoteConfig(CloudEvent $cloudevent)
    {
        $log = fopen(getenv('LOGGER_OUTPUT') ?: 'php://stderr', 'wb');
    
        $data = $cloudevent->getData();
    
        fwrite($log, 'Update type: ' . $data['updateType'] . PHP_EOL);
        fwrite($log, 'Origin: ' . $data['updateOrigin'] . PHP_EOL);
        fwrite($log, 'Version: ' . $data['versionNumber'] . PHP_EOL);
    }

### Python

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def hello_remote_config(data, context):
        """Triggered by a change to a Firebase Remote Config value.
        Args:
               data (dict): The event payload.
               context (google.cloud.functions.Context): Metadata for the event.
        """
        print(f'Update type: {data["updateType"]}')
        print(f'Origin: {data["updateOrigin"]}')
        print(f'Version: {data["versionNumber"]}')
    
    

### Ruby

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "functions_framework"
    
    # Triggered by a change to a Firebase Remote Config value
    FunctionsFramework.cloud_event "hello_remote_config" do |event|
      # Event-triggered Ruby functions receive a CloudEvents::Event::V1 object.
      # See https://cloudevents.github.io/sdk-ruby/latest/CloudEvents/Event/V1.html
      # The Firebase event payload can be obtained from the event data.
      payload = event.data
    
      logger.info "Update type: #{payload['updateType']}"
      logger.info "Origin: #{payload['updateOrigin']}"
      logger.info "Version: #{payload['versionNumber']}"
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudfunctions). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
