---
url: https://docs.cloud.google.com/functions/docs/samples/functions-firebase-auth/
title: Firebase Auth \u00a0|\u00a0 Cloud Run functions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:03:35.484984+00:00
---

# Firebase Auth  |  Cloud Run functions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/docs/samples/functions-firebase-auth/

If you are creating a new function, see the [Console Quickstart](https://docs.cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ Samples ](https://docs.cloud.google.com/functions/docs/samples)



#  Firebase Auth Stay organized with collections  Save and categorize content based on your preferences. 

Triggers a function when a Firebase Auth user object changes.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Firebase Authentication Triggers](https://docs.cloud.google.com/functions/1stgendocs/calling/firebase-auth)



## Code sample

### C#

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using CloudNative.CloudEvents;
    using Google.Cloud.Functions.Framework;
    using Google.Events.Protobuf.Firebase.Auth.V1;
    using Microsoft.Extensions.Logging;
    using System.Threading;
    using System.Threading.Tasks;
    
    namespace FirebaseAuth;
    
    public class Function : ICloudEventFunction<AuthEventData>
    {
        private readonly ILogger _logger;
    
        public Function(ILogger<Function> logger) =>
            _logger = logger;
    
        public Task HandleAsync(CloudEvent cloudEvent, AuthEventData data, CancellationToken cancellationToken)
        {
            _logger.LogInformation("Function triggered by change to user: {uid}", data.Uid);
            if (data.Metadata is UserMetadata metadata)
            {
                _logger.LogInformation("User created at: {created:s}", metadata.CreateTime.ToDateTimeOffset());
            }
            if (!string.IsNullOrEmpty(data.Email))
            {
                _logger.LogInformation("Email: {email}", data.Email);
            }
    
            // In this example, we don't need to perform any asynchronous operations, so the
            // method doesn't need to be declared async.
            return Task.CompletedTask;
        }
    }

### Go

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Package firebase contains a Firestore Cloud Function.
    package firebase
    
    import (
    	"context"
    	"log"
    	"time"
    )
    
    // AuthEvent is the payload of a Firestore Auth event.
    type AuthEvent struct {
    	Email    string `json:"email"`
    	Metadata struct {
    		CreatedAt time.Time `json:"createdAt"`
    	} `json:"metadata"`
    	UID string `json:"uid"`
    }
    
    // HelloAuth is triggered by Firestore Auth events.
    func HelloAuth(ctx context.Context, e AuthEvent) error {
    	log.Printf("Function triggered by creation or deletion of user: %q", e.UID)
    	log.Printf("Created at: %v", e.Metadata.CreatedAt)
    	if e.Email != "" {
    		log.Printf("Email: %q", e.Email)
    	}
    	return nil
    }
    

### Java

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.functions.Context;
    import com.google.cloud.functions.RawBackgroundFunction;
    import com.google.gson.Gson;
    import com.google.gson.JsonObject;
    import java.util.logging.Logger;
    
    public class FirebaseAuth implements RawBackgroundFunction {
      private static final Logger logger = Logger.getLogger(FirebaseAuth.class.getName());
    
      // Use GSON (https://github.com/google/gson) to parse JSON content.
      private static final Gson gson = new Gson();
    
      @Override
      public void accept(String json, Context context) {
        JsonObject body = gson.fromJson(json, JsonObject.class);
    
        if (body != null && body.has("uid")) {
          logger.info("Function triggered by change to user: " + body.get("uid").getAsString());
        }
    
        if (body != null && body.has("metadata")) {
          JsonObject metadata = body.get("metadata").getAsJsonObject();
          logger.info("Created at: " + metadata.get("createdAt").getAsString());
        }
    
        if (body != null && body.has("email")) {
          logger.info("Email: " + body.get("email").getAsString());
        }
      }
    }
    

### Node.js

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * Background Function triggered by a change to a Firebase Auth user object.
     *
     * @param {!Object} event The Cloud Functions event.
     */
    exports.helloAuth = event => {
      try {
        console.log(`Function triggered by change to user: ${event.uid}`);
        console.log(`Created at: ${event.metadata.createdAt}`);
    
        if (event.email) {
          console.log(`Email: ${event.email}`);
        }
      } catch (err) {
        console.error(err);
      }
    };

### PHP

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\CloudFunctions\CloudEvent;
    
    function firebaseAuth(CloudEvent $cloudevent)
    {
        $log = fopen(getenv('LOGGER_OUTPUT') ?: 'php://stderr', 'wb');
        $data = $cloudevent->getData();
    
        fwrite(
            $log,
            'Function triggered by change to user: ' . $data['uid'] . PHP_EOL
        );
        fwrite($log, 'Created at: ' . $data['metadata']['createTime'] . PHP_EOL);
    
        if (isset($data['email'])) {
            fwrite($log, 'Email: ' . $data['email'] . PHP_EOL);
        }
    }

### Python

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import json
    
    def hello_auth(data, context):
        """Triggered by creation or deletion of a Firebase Auth user object.
        Args:
               data (dict): The event payload.
               context (google.cloud.functions.Context): Metadata for the event.
        """
        print("Function triggered by creation/deletion of user: %s" % data["uid"])
        print("Created at: %s" % data["metadata"]["createdAt"])
    
        if "email" in data:
            print("Email: %s" % data["email"])
    
    

### Ruby

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "functions_framework"
    
    # Triggered by creation or deletion of a Firebase Auth user object.
    FunctionsFramework.cloud_event "hello_auth" do |event|
      # Event-triggered Ruby functions receive a CloudEvents::Event::V1 object.
      # See https://cloudevents.github.io/sdk-ruby/latest/CloudEvents/Event/V1.html
      # The Firebase event payload can be obtained from the `data` field.
      payload = event.data
    
      logger.info "Function triggered by creation/deletion of user: #{payload['uid']}"
      logger.info "Created at: #{payload['metadata']['createdAt']}"
      logger.info "Email: #{payload['email']}" if payload.key? "email"
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudfunctions). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
