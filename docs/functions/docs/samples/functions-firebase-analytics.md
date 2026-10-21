---
url: https://docs.cloud.google.com/functions/docs/samples/functions-firebase-analytics/
title: Firebase Analytics \u00a0|\u00a0 Cloud Run functions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:03:35.284964+00:00
---

# Firebase Analytics  |  Cloud Run functions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/docs/samples/functions-firebase-analytics/

If you are creating a new function, see the [Console Quickstart](https://docs.cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ Samples ](https://docs.cloud.google.com/functions/docs/samples)



#  Firebase Analytics Stay organized with collections  Save and categorize content based on your preferences. 

Triggers a function when a Firebase Analytics event is received.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Google Analytics for Firebase Triggers](https://docs.cloud.google.com/functions/1stgendocs/calling/google-analytics-firebase)



## Code sample

### C#

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using CloudNative.CloudEvents;
    using Google.Cloud.Functions.Framework;
    using Google.Events.Protobuf.Firebase.Analytics.V1;
    using Microsoft.Extensions.Logging;
    using System;
    using System.Linq;
    using System.Threading;
    using System.Threading.Tasks;
    
    namespace FirebaseAnalytics;
    
    public class Function : ICloudEventFunction<AnalyticsLogData>
    {
        private readonly ILogger _logger;
    
        public Function(ILogger<Function> logger) =>
            _logger = logger;
    
        public Task HandleAsync(CloudEvent cloudEvent, AnalyticsLogData data, CancellationToken cancellationToken)
        {
            _logger.LogInformation("Event source: {source}", cloudEvent.Source);
            _logger.LogInformation("Event count: {count}", data.EventDim.Count);
    
            var firstEvent = data.EventDim.FirstOrDefault();
            if (firstEvent is object)
            {
                _logger.LogInformation("First event name: {name}", firstEvent.Name);
                DateTimeOffset timestamp = DateTimeOffset.FromUnixTimeMilliseconds(firstEvent.TimestampMicros / 1000);
                _logger.LogInformation("First event timestamp: {timestamp:u}", timestamp);
            }
    
            var userObject = data.UserDim;
            if (userObject is object)
            {
                _logger.LogInformation("Device model: {device}", userObject.DeviceInfo?.DeviceModel);
                _logger.LogInformation("Location: {city}, {country}", userObject.GeoInfo?.City, userObject.GeoInfo.Country);
            }
            // In this example, we don't need to perform any asynchronous operations, so the
            // method doesn't need to be declared async.
            return Task.CompletedTask;
        }
    }

### Go

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Package p contains a Google Analytics for Firebase Cloud Function.
    package p
    
    import (
    	"context"
    	"fmt"
    	"log"
    
    	"cloud.google.com/go/functions/metadata"
    )
    
    // AnalyticsEvent is the payload of an Analytics log event.
    type AnalyticsEvent struct {
    	EventDimensions []EventDimensions `json:"eventDim"`
    	UserDimensions  interface{}       `json:"userDim"`
    }
    
    // EventDimensions holds Analytics event dimensions.
    type EventDimensions struct {
    	Name                    string      `json:"name"`
    	Date                    string      `json:"date"`
    	TimestampMicros         string      `json:"timestampMicros"`
    	PreviousTimestampMicros string      `json:"previousTimestampMicros"`
    	Params                  interface{} `json:"params"`
    }
    
    // HelloAnalytics handles Firebase Mobile Analytics log events.
    func HelloAnalytics(ctx context.Context, e AnalyticsEvent) error {
    	meta, err := metadata.[FromContext](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/functions/latest/metadata.html#cloud_google_com_go_functions_metadata_Metadata_FromContext)(ctx)
    	if err != nil {
    		return fmt.Errorf("metadata.FromContext: %w", err)
    	}
    	log.Printf("Function triggered by Google Analytics event: %v", meta.[Resource](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/functions/latest/metadata.html#cloud_google_com_go_functions_metadata_Resource))
    	log.Printf("%+v", e)
    	return nil
    }
    

### Node.js

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * Background Function triggered by a Google Analytics for Firebase log event.
     *
     * @param {!Object} event The Cloud Functions event.
     */
    exports.helloAnalytics = event => {
      const {resource} = event;
      console.log(`Function triggered by the following event: ${resource}`);
    
      const [analyticsEvent] = event.data.eventDim;
      console.log(`Name: ${analyticsEvent.name}`);
      console.log(`Timestamp: ${new Date(analyticsEvent.timestampMicros / 1000)}`);
    
      const userObj = event.data.userDim;
      console.log(`Device Model: ${userObj.deviceInfo.deviceModel}`);
      console.log(`Location: ${userObj.geoInfo.city}, ${userObj.geoInfo.country}`);
    };

### PHP

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\CloudFunctions\CloudEvent;
    
    function firebaseAnalytics(CloudEvent $cloudevent): void
    {
        $log = fopen(getenv('LOGGER_OUTPUT') ?: 'php://stderr', 'wb');
    
        $data = $cloudevent->getData();
    
        fwrite($log, 'Function triggered by the following event:' . $data['resource'] . PHP_EOL);
    
        $analyticsEvent = $data['eventDim'][0];
        $unixTime = $analyticsEvent['timestampMicros'] / 1000;
    
        fwrite($log, 'Name: ' . $analyticsEvent['name'] . PHP_EOL);
        fwrite($log, 'Timestamp: ' . gmdate("Y-m-d\TH:i:s\Z", $unixTime) . PHP_EOL);
    
        $userObj = $data['userDim'];
        fwrite($log, sprintf(
            'Location: %s, %s' . PHP_EOL,
            $userObj['geoInfo']['city'],
            $userObj['geoInfo']['country']
        ));
    
        fwrite($log, 'Device Model: %s' . $userObj['deviceInfo']['deviceModel'] . PHP_EOL);
    }

### Python

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from datetime import datetime
    
    def hello_analytics(data, context):
        """Triggered by a Google Analytics for Firebase log event.
        Args:
               data (dict): The event payload.
               context (google.cloud.functions.Context): Metadata for the event.
        """
        trigger_resource = context.resource
        print(f"Function triggered by the following event: {trigger_resource}")
    
        event = data["eventDim"][0]
        print(f'Name: {event["name"]}')
    
        event_timestamp = int(event["timestampMicros"][:-6])
        print(f"Timestamp: {datetime.utcfromtimestamp(event_timestamp)}")
    
        user_obj = data["userDim"]
        print(f'Device Model: {user_obj["deviceInfo"]["deviceModel"]}')
    
        geo_info = user_obj["geoInfo"]
        print(f'Location: {geo_info["city"]}, {geo_info["country"]}')
    
    

### Ruby

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "functions_framework"
    
    # Triggered by a Google Analytics for Firebase log event.
    FunctionsFramework.cloud_event "hello_analytics" do |event|
      # Event-triggered Ruby functions receive a CloudEvents::Event::V1 object.
      # See https://cloudevents.github.io/sdk-ruby/latest/CloudEvents/Event/V1.html
      # The Analytics event payload can be obtained from the `data` field.
      payload = event.data
    
      logger.info "Function triggered by the following event: #{event.source}"
    
      event = payload["eventDim"].first
      logger.info "Name: #{event['name']}"
    
      event_timestamp = Time.at(event["timestampMicros"].to_i / 1_000_000).utc
      logger.info "Timestamp: #{event_timestamp.strftime '%Y-%m-%dT%H:%M:%SZ'}"
    
      user_obj = payload["userDim"]
      logger.info "Device Model: #{user_obj['deviceInfo']['deviceModel']}"
    
      geo_info = user_obj["geoInfo"]
      logger.info "Location: #{geo_info['city']}, #{geo_info['country']}"
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudfunctions). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
