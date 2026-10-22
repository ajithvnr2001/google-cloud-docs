---
url: https://docs.cloud.google.com/functions/docs/samples/functions-log-cloudevent/
title: Process a Cloud Audit Logging log entry \u00a0|\u00a0 Cloud Run functions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:51:45.819972+00:00
---

# Process a Cloud Audit Logging log entry  |  Cloud Run functions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/docs/samples/functions-log-cloudevent/

If you are creating a new function, see the [Console Quickstart](https://docs.cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ Samples ](https://docs.cloud.google.com/functions/docs/samples)



#  Process a Cloud Audit Logging log entry Stay organized with collections  Save and categorize content based on your preferences. 

Shows how to process an Audit Log entry.

## Code sample

### Go

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Package helloworld provides a set of Cloud Functions samples.
    package helloworld
    
    import (
    	"context"
    	"fmt"
    	"log"
    
    	"github.com/GoogleCloudPlatform/functions-framework-go/functions"
    	"github.com/cloudevents/sdk-go/v2/event"
    )
    
    func init() {
    	functions.CloudEvent("HelloAuditLog", helloAuditLog)
    }
    
    // AuditLogEntry represents a LogEntry as described at
    // https://cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry
    type AuditLogEntry struct {
    	ProtoPayload *AuditLogProtoPayload `json:"protoPayload"`
    }
    
    // AuditLogProtoPayload represents AuditLog within the LogEntry.protoPayload
    // See https://cloud.google.com/logging/docs/reference/audit/auditlog/rest/Shared.Types/AuditLog
    type AuditLogProtoPayload struct {
    	MethodName         string                 `json:"methodName"`
    	ResourceName       string                 `json:"resourceName"`
    	AuthenticationInfo map[string]interface{} `json:"authenticationInfo"`
    }
    
    // helloAuditLog receives a CloudEvent containing an AuditLogEntry, and logs a few fields.
    func helloAuditLog(ctx context.Context, e event.Event) error {
    	// Print out details from the CloudEvent itself
    	// See https://github.com/cloudevents/spec/blob/v1.0.1/spec.md#subject
    	// for details on the Subject field
    	log.Printf("Event Type: %s", e.Type())
    	log.Printf("Subject: %s", e.Subject())
    
    	// Decode the Cloud Audit Logging message embedded in the CloudEvent
    	logentry := &AuditLogEntry{}
    	if err := e.DataAs(logentry); err != nil {
    		ferr := fmt.Errorf("event.DataAs: %w", err)
    		log.Print(ferr)
    		return ferr
    	}
    	// Print out some of the information contained in the Cloud Audit Logging event
    	// See https://cloud.google.com/logging/docs/audit#audit_log_entry_structure
    	// for a full description of available fields.
    	log.Printf("API Method: %s", logentry.ProtoPayload.MethodName)
    	log.Printf("Resource Name: %s", logentry.ProtoPayload.ResourceName)
    	if v, ok := logentry.ProtoPayload.AuthenticationInfo["principalEmail"]; ok {
    		log.Printf("Principal: %s", v)
    	}
    	return nil
    }
    

### Java

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.functions.CloudEventsFunction;
    import com.google.gson.Gson;
    import com.google.gson.JsonObject;
    import io.cloudevents.CloudEvent;
    import java.nio.charset.StandardCharsets;
    import java.util.logging.Logger;
    
    public class LogCloudEvent implements CloudEventsFunction {
      private static final Logger logger = Logger.getLogger(LogCloudEvent.class.getName());
    
      @Override
      public void accept(CloudEvent event) {
        // Print out details from the CloudEvent
        // The type of event related to the originating occurrence
        logger.info("Event Type: " + event.getType());
        // The subject of the event in the context of the event producer
        logger.info("Event Subject: " + event.getSubject());
    
        if (event.getData() != null) {
          // Extract data from CloudEvent wrapper
          String cloudEventData = new String(event.getData().toBytes(), StandardCharsets.UTF_8);
    
          Gson gson = new Gson();
          // Convert data into a JSON object
          JsonObject eventData = gson.fromJson(cloudEventData, JsonObject.class);
    
          // Extract Cloud Audit Log data from protoPayload
          // https://cloud.google.com/logging/docs/audit#audit_log_entry_structure
          JsonObject payload = eventData.getAsJsonObject("protoPayload");
          logger.info("API Method: " + payload.get("methodName").getAsString());
          logger.info("Resource name: " + payload.get("resourceName").getAsString());
    
          JsonObject auth = payload.getAsJsonObject("authenticationInfo");
          if (auth != null) {
            // The email address of the authenticated user 
            // (or service account on behalf of third party principal) making the request
            logger.info("Authenticated User: " + auth.get("principalEmail").getAsString()); 
          }
        }
      }
    }

### Node.js

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const functions = require('@google-cloud/functions-framework');
    
    // Register a CloudEvent callback with the Functions Framework that will
    // be triggered by an Eventarc Cloud Audit Logging trigger.
    //
    // Note: this is NOT designed for second-party (Cloud Audit Logs -> Pub/Sub) triggers!
    functions.cloudEvent('helloAuditLog', cloudEvent => {
      // Print out details from the CloudEvent itself
      console.log('Event type:', cloudEvent.type);
    
      // Print out the CloudEvent's `subject` property
      // See https://github.com/cloudevents/spec/blob/v1.0.1/spec.md#subject
      console.log('Subject:', cloudEvent.subject);
    
      // Print out details from the `protoPayload`
      // This field encapsulates a Cloud Audit Logging entry
      // See https://cloud.google.com/logging/docs/audit#audit_log_entry_structure
      const payload = cloudEvent.data && cloudEvent.data.protoPayload;
      if (payload) {
        console.log('API method:', payload.methodName);
        console.log('Resource name:', payload.resourceName);
        console.log('Principal:', payload.authenticationInfo.principalEmail);
      }
    });

### Python

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import functions_framework
    
    
    # CloudEvent function to be triggered by an Eventarc Cloud Audit Logging trigger
    # Note: this is NOT designed for second-party (Cloud Audit Logs -> Pub/Sub) triggers!
    @functions_framework.cloud_event
    def hello_auditlog(cloud_event):
        # Print out the CloudEvent's (required) `type` property
        # See https://github.com/cloudevents/spec/blob/v1.0.1/spec.md#type
        print(f"Event type: {cloud_event['type']}")
    
        # Print out the CloudEvent's (optional) `subject` property
        # See https://github.com/cloudevents/spec/blob/v1.0.1/spec.md#subject
        if "subject" in cloud_event:
            # CloudEvent objects don't support `get` operations.
            # Use the `in` operator to verify `subject` is present.
            print(f"Subject: {cloud_event['subject']}")
    
        # Print out details from the `protoPayload`
        # This field encapsulates a Cloud Audit Logging entry
        # See https://cloud.google.com/logging/docs/audit#audit_log_entry_structure
    
        payload = cloud_event.data.get("protoPayload")
        if payload:
            print(f"API method: {payload.get('methodName')}")
            print(f"Resource name: {payload.get('resourceName')}")
            print(
                f"Principal: {payload.get('authenticationInfo', dict()).get('principalEmail')}"
            )
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudfunctions). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
