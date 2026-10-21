---
url: https://docs.cloud.google.com/eventarc/docs/samples/eventarc-pubsub-handler/
title: Create an event handler that receives and processes a Pub/Sub message event \u00a0|\u00a0 Eventarc \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:01:53.262254+00:00
---

# Create an event handler that receives and processes a Pub/Sub message event  |  Eventarc  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/eventarc/docs/samples/eventarc-pubsub-handler/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Eventarc ](https://docs.cloud.google.com/eventarc/docs)
  * [ Samples ](https://docs.cloud.google.com/eventarc/docs/samples)



#  Create an event handler that receives and processes a Pub/Sub message event Stay organized with collections  Save and categorize content based on your preferences. 

Creates an event handler that receives and processes a Pub/Sub message event.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Develop event receivers](https://docs.cloud.google.com/eventarc/standard/docs/run/event-receivers)



## Code sample

### C#

To authenticate to Eventarc, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using CloudNative.CloudEvents;
    using CloudNative.CloudEvents.AspNetCore;
    using Google.Events.Protobuf.Cloud.PubSub.V1;
    using Microsoft.AspNetCore.Builder;
    using Microsoft.AspNetCore.Hosting;
    using Microsoft.AspNetCore.Http;
    using [Microsoft.Extensions.DependencyInjection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Billing.Budgets.V1Beta1/latest/Microsoft.Extensions.DependencyInjection.html);
    using Microsoft.Extensions.Hosting;
    using Microsoft.Extensions.Logging;
    
    public class Startup
    {
        public void ConfigureServices(IServiceCollection services)
        {
        }
    
        public void Configure(IApplicationBuilder app, IWebHostEnvironment env, ILogger<Startup> logger)
        {
            if (env.IsDevelopment())
            {
                app.UseDeveloperExceptionPage();
            }
    
            logger.LogInformation("Service is starting...");
    
            app.UseRouting();
    
            app.UseEndpoints(endpoints =>
            {
                endpoints.MapPost("/", async context =>
                {
                    var formatter = CloudEventFormatterAttribute.CreateFormatter(typeof(MessagePublishedData));
                    var cloudEvent = await context.Request.ToCloudEventAsync(formatter);
                    logger.LogInformation("Received CloudEvent\n" + GetEventLog(cloudEvent));
    
                    var messagePublishedData = (MessagePublishedData) cloudEvent.Data;
                    var pubSubMessage = messagePublishedData.Message;
                    if (pubSubMessage == null)
                    {
                        context.Response.StatusCode = 400;
                        await context.Response.WriteAsync("Bad request: Invalid Pub/Sub message format");
                        return;
                    }
    
                    var data = pubSubMessage.Data;
                    logger.LogInformation($"Data: {data.ToBase64()}");
    
                    var name = data.ToStringUtf8();
                    logger.LogInformation($"Extracted name: {name}");
    
                    var id = context.Request.Headers["ce-id"];
                    await context.Response.WriteAsync($"Hello {name}! ID: {id}");
                });
            });
        }
    
        private string GetEventLog(CloudEvent cloudEvent)
        {
            return $"ID: {cloudEvent.Id}\n"
                + $"Source: {cloudEvent.Source}\n"
                + $"Type: {cloudEvent.Type}\n"
                + $"Subject: {cloudEvent.Subject}\n"
                + $"DataSchema: {cloudEvent.DataSchema}\n"
                + $"DataContentType: {cloudEvent.DataContentType}\n"
                + $"Time: {cloudEvent.Time?.UtcDateTime:yyyy-MM-dd'T'HH:mm:ss.fff'Z'}\n"
                + $"SpecVersion: {cloudEvent.SpecVersion}\n"
                + $"Data: {cloudEvent.Data}";
        }
    }
    

### Go

To authenticate to Eventarc, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Sample pubsub is a Cloud Run service which handles Pub/Sub messages.
    package main
    
    import (
    	"encoding/json"
    	"fmt"
    	"log"
    	"net/http"
    	"os"
    )
    
    // PubSubMessage is the payload of a Pub/Sub event.
    // See the documentation for more details:
    // https://cloud.google.com/pubsub/docs/reference/rest/v1/PubsubMessage
    type PubSubMessage struct {
    	Message struct {
    		Data []byte `json:"data,omitempty"`
    		ID   string `json:"id"`
    	} `json:"message"`
    	Subscription string `json:"subscription"`
    }
    
    // HelloEventsPubSub receives and processes a Pub/Sub push message.
    func HelloEventsPubSub(w http.ResponseWriter, r *http.Request) {
    	var e PubSubMessage
    	if err := json.NewDecoder(r.Body).Decode(&e); err != nil {
    		http.Error(w, "Bad HTTP Request", http.StatusBadRequest)
    		log.Printf("Bad HTTP Request: %v", http.StatusBadRequest)
    		return
    	}
    	name := string(e.Message.Data)
    	if name == "" {
    		name = "World"
    	}
    	s := fmt.Sprintf("Hello, %s! ID: %s", name, string(r.Header.Get("Ce-Id")))
    	log.Print(s)
    	fmt.Fprintln(w, s)
    }
    

### Java

To authenticate to Eventarc, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.example.cloudrun.eventpojos.PubSubBody;
    import java.util.Base64;
    import java.util.Map;
    import org.apache.commons.lang3.StringUtils;
    import org.springframework.http.HttpStatus;
    import org.springframework.http.ResponseEntity;
    import org.springframework.web.bind.annotation.RequestBody;
    import org.springframework.web.bind.annotation.RequestHeader;
    import org.springframework.web.bind.annotation.RequestMapping;
    import org.springframework.web.bind.annotation.RequestMethod;
    import org.springframework.web.bind.annotation.RestController;
    
    @RestController
    public class EventController {
      @RequestMapping(value = "/", method = RequestMethod.POST)
      public ResponseEntity<String> receiveMessage(
          @RequestBody PubSubBody body, @RequestHeader Map<String, String> headers) {
        // Get PubSub message from request body.
        PubSubBody.PubSubMessage message = body.getMessage();
        if (message == null) {
          String msg = "No Pub/Sub message received.";
          System.out.println(msg);
          return new ResponseEntity<>(msg, HttpStatus.BAD_REQUEST);
        }
    
        String data = message.getData();
        if (data == null || data.isEmpty()) {
          String msg = "Invalid Pub/Sub message format.";
          System.out.println(msg);
          return new ResponseEntity<>(msg, HttpStatus.BAD_REQUEST);
        }
    
        String name =
            !StringUtils.isEmpty(data) ? new String(Base64.getDecoder().decode(data)) : "World";
        String ceId = headers.getOrDefault("ce-id", "");
        String msg = String.format("Hello, %s! ID: %s", name, ceId);
        System.out.println(msg);
        return new ResponseEntity<>(msg, HttpStatus.OK);
      }
    }

### Node.js

To authenticate to Eventarc, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const express = require('express');
    const {
      toMessagePublishedData,
    } = require('@google/events/cloud/pubsub/v1/MessagePublishedData');
    const app = express();
    
    app.use(express.json());
    app.post('/', (req, res) => {
      if (!req.body) {
        const errorMessage = 'no Pub/Sub message received';
        res.status(400).send(`Bad Request: ${errorMessage}`);
        console.log(`Bad Request: ${errorMessage}`);
        return;
      }
      if (!req.body.message) {
        const errorMessage = 'invalid Pub/Sub message format';
        res.status(400).send(`Bad Request: ${errorMessage}`);
        console.log(`Bad Request: ${errorMessage}`);
        return;
      }
      // Cast to MessagePublishedEvent for IDE autocompletion
      const pubSubMessage = toMessagePublishedData(req.body);
      const name =
        pubSubMessage.message && pubSubMessage.message.data
          ? Buffer.from(pubSubMessage.message.data, 'base64').toString().trim()
          : 'World';
    
      const result = `Hello, ${name}! ID: ${req.get('ce-id') || ''}`;
      console.log(result);
      res.send(result);
    });
    
    module.exports = app;

### Python

To authenticate to Eventarc, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    @app.route("/", methods=["POST"])
    def index():
        data = request.get_json()
        if not data:
            msg = "no Pub/Sub message received"
            print(f"error: {msg}")
            return f"Bad Request: {msg}", 400
    
        if not isinstance(data, dict) or "message" not in data:
            msg = "invalid Pub/Sub message format"
            print(f"error: {msg}")
            return f"Bad Request: {msg}", 400
    
        pubsub_message = data["message"]
    
        name = "World"
        if isinstance(pubsub_message, dict) and "data" in pubsub_message:
            name = base64.b64decode(pubsub_message["data"]).decode("utf-8").strip()
    
        resp = f"Hello, {name}! ID: {request.headers.get('ce-id')}"
        print(resp)
    
        return (resp, 200)
    
    

### Ruby

To authenticate to Eventarc, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    post "/" do
      request.body.rewind # in case someone already read it
    
      body = JSON.parse request.body.read
      data = Base64.decode64 body["message"]["data"]
      if data.empty?
        data = "World"
      end
      id = request.env["HTTP_CE_ID"]
      if request.has_header? "ce-id"
        id = request.get_header "ce-id"
      end
    
      result = "Hello #{data}! ID: #{id}"
      puts result
      result
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=eventarc). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
