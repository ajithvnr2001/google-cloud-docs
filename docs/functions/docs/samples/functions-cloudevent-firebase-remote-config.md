---
url: https://docs.cloud.google.com/functions/docs/samples/functions-cloudevent-firebase-remote-config/
title: Firebase Remote Config Change Trigger \u00a0|\u00a0 Cloud Run functions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:53:41.486721+00:00
---

# Firebase Remote Config Change Trigger  |  Cloud Run functions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/docs/samples/functions-cloudevent-firebase-remote-config/

If you are creating a new function, see the [Console Quickstart](https://docs.cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ Samples ](https://docs.cloud.google.com/functions/docs/samples)



#  Firebase Remote Config Change Trigger Stay organized with collections  Save and categorize content based on your preferences. 

This sample demonstrates how to trigger a Cloud Function when a Firebase Remote Config value changes.

## Code sample

### Go

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Package remote_config provides cloud event sample for firebase remote config updates.
    package remoteconfig
    
    import (
    	"context"
    	"fmt"
    	"log"
    
    	"github.com/GoogleCloudPlatform/functions-framework-go/functions"
    	"github.com/cloudevents/sdk-go/v2/event"
    	"github.com/googleapis/google-cloudevents-go/firebase/remoteconfigdata"
    	"google.golang.org/protobuf/encoding/protojson"
    )
    
    func init() {
    	functions.CloudEvent("HelloRemoteConfig", HelloRemoteConfig)
    }
    
    // HelloRemoteConfig handles Firebase Remote Config events.
    func HelloRemoteConfig(ctx context.Context, e event.Event) error {
    	unmarshalOptions := protojson.UnmarshalOptions{DiscardUnknown: true}
    
    	var data remoteconfigdata.RemoteConfigEventData
    	if err := unmarshalOptions.Unmarshal(e.Data(), &data); err != nil {
    		return fmt.Errorf("UnmarshalTo: %w", err)
    	}
    
    	log.Printf("Update type: %+v", data.GetUpdateType())
    	log.Printf("Origin: %+v", data.GetUpdateOrigin())
    	log.Printf("Version: %+v", data.GetVersionNumber())
    	return nil
    }
    

### Java

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.functions.CloudEventsFunction;
    import com.google.events.firebase.remoteconfig.v1.[RemoteConfigEventData](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.firebase.remoteconfig.v1.RemoteConfigEventData.html);
    import com.google.protobuf.util.[JsonFormat](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.JsonFormat.html);
    import io.cloudevents.CloudEvent;
    import java.nio.charset.StandardCharsets;
    import java.util.logging.Logger;
    
    public class FirebaseRemoteConfig implements CloudEventsFunction {
      private static final Logger logger = Logger.getLogger(FirebaseRemoteConfig.class.getName());
    
      @Override
      public void accept(CloudEvent event) throws Exception {
        if (event.getData() == null) {
          logger.info("No data found in event");
          return;
        }
    
        [RemoteConfigEventData](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.firebase.remoteconfig.v1.RemoteConfigEventData.html).Builder builder = [RemoteConfigEventData](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.firebase.remoteconfig.v1.RemoteConfigEventData.html).newBuilder();
        [JsonFormat](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.JsonFormat.html).[Parser](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.JsonFormat.Parser.html) jsonParser = [JsonFormat](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.JsonFormat.html).parser().[ignoringUnknownFields](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.JsonFormat.Parser.html#com_google_protobuf_util_JsonFormat_Parser_ignoringUnknownFields__)();
        jsonParser.merge(new String(event.getData().toBytes(), StandardCharsets.UTF_8), builder);
        [RemoteConfigEventData](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.firebase.remoteconfig.v1.RemoteConfigEventData.html) data = builder.build();
    
        logger.info("Update type: " + data.[getUpdateType](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.firebase.remoteconfig.v1.RemoteConfigEventData.html#com_google_events_firebase_remoteconfig_v1_RemoteConfigEventData_getUpdateType__)().name());
        logger.info("Origin: " + data.[getUpdateOrigin](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.firebase.remoteconfig.v1.RemoteConfigEventData.html#com_google_events_firebase_remoteconfig_v1_RemoteConfigEventData_getUpdateOrigin__)().name());
        logger.info("Version: " + data.[getVersionNumber](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.firebase.remoteconfig.v1.RemoteConfigEventData.html#com_google_events_firebase_remoteconfig_v1_RemoteConfigEventData_getVersionNumber__)());
      }
    }
    

### Node.js

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const functions = require('@google-cloud/functions-framework');
    
    /**
     * Cloud Event Function triggered by a change to a Firebase Remote Config value.
     *
     * @param {object} event The Cloud Functions event.
     */
    functions.cloudEvent('helloRemoteConfig', event => {
      console.log(`Update type: ${event.data.updateType}`);
      console.log(`Origin: ${event.data.updateOrigin}`);
      console.log(`Version: ${event.data.versionNumber}`);
    });

### Python

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from cloudevents.http import CloudEvent
    import functions_framework
    
    
    @functions_framework.cloud_event
    def hello_remote_config(event: CloudEvent) -> None:
        """Triggered by a change to a Firebase Remote Config value.
        Args:
            event: Cloud Event triggered by change to Firebase Remote Config
        """
        print(f'Update type: {event.data["updateType"]}')
        print(f'Origin: {event.data["updateOrigin"]}')
        print(f'Version: {event.data["versionNumber"]}')
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudfunctions). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
