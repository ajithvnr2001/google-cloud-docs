---
url: https://docs.cloud.google.com/functions/docs/samples/functions-cloudevent-firebase-rtdb/
title: Listen to Firebase Realtime Database changes \u00a0|\u00a0 Cloud Run functions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:51:25.002359+00:00
---

# Listen to Firebase Realtime Database changes  |  Cloud Run functions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/docs/samples/functions-cloudevent-firebase-rtdb/

If you are creating a new function, see the [Console Quickstart](https://docs.cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ Samples ](https://docs.cloud.google.com/functions/docs/samples)



#  Listen to Firebase Realtime Database changes Stay organized with collections  Save and categorize content based on your preferences. 

This function is triggered by a change to a Firebase Realtime Database reference. It prints the source of the change, the data, and the delta.

## Code sample

### Go

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Package rtdb contains a Cloud Function triggered by a Firebase Realtime Database
    // event.
    package rtdb
    
    import (
    	"context"
    	"fmt"
    	"log"
    
    	"github.com/GoogleCloudPlatform/functions-framework-go/functions"
    	"github.com/cloudevents/sdk-go/v2/event"
    	"github.com/googleapis/google-cloudevents-go/firebase/databasedata"
    	"google.golang.org/protobuf/encoding/protojson"
    )
    
    func init() {
    	functions.CloudEvent("HelloRTDB", HelloRTDB)
    }
    
    // HelloRTDB handles changes to a Firebase RTDB.
    func HelloRTDB(ctx context.Context, e event.Event) error {
    	unmarshalOptions := protojson.UnmarshalOptions{DiscardUnknown: true}
    
    	var data databasedata.ReferenceEventData
    	if err := unmarshalOptions.Unmarshal(e.Data(), &data); err != nil {
    		return fmt.Errorf("Unmarshal: %w", err)
    	}
    	log.Printf("Function triggered by change to: %v", e.Source())
    	log.Printf("Data: %+v", data.GetData())
    	log.Printf("Delta: %+v", data.GetDelta())
    	return nil
    }
    

### Java

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.functions.CloudEventsFunction;
    import com.google.events.firebase.database.v1.[ReferenceEventData](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.firebase.database.v1.ReferenceEventData.html);
    import com.google.protobuf.util.[JsonFormat](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.JsonFormat.html);
    import io.cloudevents.CloudEvent;
    import java.nio.charset.StandardCharsets;
    import java.util.logging.Logger;
    
    public class FirebaseRtdb implements CloudEventsFunction {
      private static final Logger logger = Logger.getLogger(FirebaseRtdb.class.getName());
    
      @Override
      public void accept(CloudEvent event) throws Exception {
        if (event.getData() == null) {
          logger.info("No data found in event");
          return;
        }
    
        [ReferenceEventData](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.firebase.database.v1.ReferenceEventData.html).Builder builder = [ReferenceEventData](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.firebase.database.v1.ReferenceEventData.html).newBuilder();
        [JsonFormat](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.JsonFormat.html).[Parser](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.JsonFormat.Parser.html) jsonParser = [JsonFormat](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.JsonFormat.html).parser().[ignoringUnknownFields](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.JsonFormat.Parser.html#com_google_protobuf_util_JsonFormat_Parser_ignoringUnknownFields__)();
        jsonParser.merge(new String(event.getData().toBytes(), StandardCharsets.UTF_8), builder);
        [ReferenceEventData](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.firebase.database.v1.ReferenceEventData.html) data = builder.build();
    
        logger.info("Function triggered by change to: " + event.getSource().toString());
    
        if (data.[hasDelta](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.firebase.database.v1.ReferenceEventData.html#com_google_events_firebase_database_v1_ReferenceEventData_hasDelta__)()) {
          logger.info("Delta: " + data.[getDelta](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.firebase.database.v1.ReferenceEventData.html#com_google_events_firebase_database_v1_ReferenceEventData_getDelta__)().toString());
        }
    
        if (data.[hasData](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.firebase.database.v1.ReferenceEventData.html#com_google_events_firebase_database_v1_ReferenceEventData_hasData__)()) {
          logger.info("Data: " + data.[getData](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.firebase.database.v1.ReferenceEventData.html#com_google_events_firebase_database_v1_ReferenceEventData_getData__)().toString());
        }
      }
    }
    

### Node.js

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * Cloud Event Function triggered by a change to a Firebase RTDB reference.
     *
     * @param {!Object} event The Cloud Functions event.
     */
    const functions = require('@google-cloud/functions-framework');
    
    functions.cloudEvent('helloRTDB', event => {
      console.log(`Function triggered by change to: ${event.source}`);
      console.log('Data:');
      console.log(JSON.stringify(event.data.data, null, 2));
      console.log('Delta:');
      console.log(JSON.stringify(event.data.delta, null, 2));
    });

### Python

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import json
    
    from cloudevents.http import CloudEvent
    import functions_framework
    
    
    @functions_framework.cloud_event
    def hello_rtdb(event: CloudEvent) -> None:
        """Triggered by a change to a Firebase RTDB reference.
        Args:
            event: Cloud Event triggered by change to Firebase Real Time Database.
        """
        print(f"Function triggered by change to: {event['source']}")
        print("Data:")
        print(json.dumps(event.data["data"]))
        print("Delta:")
        print(json.dumps(event.data["delta"]))
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudfunctions). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
