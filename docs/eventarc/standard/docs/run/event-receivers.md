---
url: https://docs.cloud.google.com/eventarc/standard/docs/run/event-receivers/
title: Develop event receivers \u00a0|\u00a0 Eventarc Standard \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:01:17.580354+00:00
---

# Develop event receivers  |  Eventarc Standard  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/eventarc/standard/docs/run/event-receivers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Eventarc ](https://docs.cloud.google.com/eventarc/docs)
  * [ Standard ](https://docs.cloud.google.com/eventarc/standard/docs)
  * [ Guides ](https://docs.cloud.google.com/eventarc/standard/docs/overview)



Send feedback 

#  Develop event receivers Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/eventarc/standard/docs/overview)

This page shows you how to create and deploy an event receiver service. The target service receives HTTP requests containing the event in the [CloudEvents format](https://docs.cloud.google.com/eventarc/docs/event-format).

Event providers (sources) can provide the following event types:

  * [Directly from a Google Cloud source](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#directly-from-a-google-cloud-source)
  * [Using Cloud Audit Logs](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs)



## Event receiver response

Your receiver service should send an HTTP `2xx` response to signal a successful event receipt to the router. The router treats all other HTTP responses as delivery failures and will resend the event.

## Open source repository

The structure of the HTTP body for all events are available on the [CloudEvents GitHub repository](https://github.com/googleapis/google-cloudevents). 

The repository contains the following to help you understand and use CloudEvents data in your programming language: 

  * Google Protocol Buffers for CloudEvents data payloads
  * Generated JSON schemas
  * A public JSON schema catalog



Links to client libraries are also included. 

## Use a CloudEvents SDK library

You can develop event receiver services using the CloudEvents SDK library, which is available for the following languages:

  * [C#](https://github.com/cloudevents/sdk-csharp)
  * [Go](https://github.com/cloudevents/sdk-go)
  * [Java](https://github.com/cloudevents/sdk-java)
  * [JavaScript](https://github.com/cloudevents/sdk-javascript)
  * [Python](https://github.com/cloudevents/sdk-python)
  * [Ruby](https://github.com/cloudevents/sdk-ruby)



These libraries are open source and make it easier to transform your HTTP request into a language-idiomatic CloudEvents object.

## Sample receiver source code

###  Cloud Audit Logs 

The sample code shows you how to read Cloud Storage events using Cloud Audit Logs in a service deployed to Cloud Run.

### Python
    
    
    @app.route("/", methods=["POST"])
    def index():
        # Create a CloudEvent object from the incoming request
        event = from_http(request.headers, request.data)
        # Gets the GCS bucket name from the CloudEvent
        # Example: "storage.googleapis.com/projects/_/buckets/my-bucket"
        bucket = event.get("subject")
    
        print(f"Detected change in Cloud Storage bucket: {bucket}")
        return (f"Detected change in Cloud Storage bucket: {bucket}", 200)
    
    

### Java
    
    
    import io.cloudevents.CloudEvent;
    import io.cloudevents.rw.CloudEventRWException;
    import io.cloudevents.spring.http.CloudEventHttpUtils;
    import org.springframework.http.HttpHeaders;
    import org.springframework.http.HttpStatus;
    import org.springframework.http.ResponseEntity;
    import org.springframework.web.bind.annotation.RequestBody;
    import org.springframework.web.bind.annotation.RequestHeader;
    import org.springframework.web.bind.annotation.RequestMapping;
    import org.springframework.web.bind.annotation.RequestMethod;
    import org.springframework.web.bind.annotation.RestController;
    
    @RestController
    public class EventController {
    
      @RequestMapping(value = "/", method = RequestMethod.POST, consumes = "application/json")
      public ResponseEntity<String> receiveMessage(
          @RequestBody String body, @RequestHeader HttpHeaders headers) {
        CloudEvent event;
        try {
          event =
              CloudEventHttpUtils.fromHttp(headers)
                  .withData(headers.getContentType().toString(), body.getBytes())
                  .build();
        } catch (CloudEventRWException e) {
          return new ResponseEntity<>(e.getMessage(), HttpStatus.BAD_REQUEST);
        }
    
        String ceSubject = event.getSubject();
        String msg = "Detected change in Cloud Storage bucket: " + ceSubject;
        System.out.println(msg);
        return new ResponseEntity<>(msg, HttpStatus.OK);
      }
    }

### Node.js
    
    
    const express = require('express');
    const app = express();
    
    app.use(express.json());
    app.post('/', (req, res) => {
      if (!req.header('ce-subject')) {
        return res
          .status(400)
          .send('Bad Request: missing required header: ce-subject');
      }
    
      console.log(
        `Detected change in Cloud Storage bucket: ${req.header('ce-subject')}`
      );
      return res
        .status(200)
        .send(
          `Detected change in Cloud Storage bucket: ${req.header('ce-subject')}`
        );
    });
    
    module.exports = app;

### Go
    
    
    // Processes CloudEvents containing Cloud Audit Logs for Cloud Storage
    package main
    
    import (
    	"fmt"
    	"log"
    	"net/http"
    	"os"
    
    	cloudevent "github.com/cloudevents/sdk-go/v2"
    )
    
    // HelloEventsStorage receives and processes a Cloud Audit Log event with Cloud Storage data.
    func HelloEventsStorage(w http.ResponseWriter, r *http.Request) {
    	if r.Method != http.MethodPost {
    		http.Error(w, "Expected HTTP POST request with CloudEvent payload", http.StatusMethodNotAllowed)
    		return
    	}
    
    	event, err := cloudevent.NewEventFromHTTPRequest(r)
    	if err != nil {
    		log.Printf("cloudevent.NewEventFromHTTPRequest: %v", err)
    		http.Error(w, "Failed to create CloudEvent from request.", http.StatusBadRequest)
    		return
    	}
    	s := fmt.Sprintf("Detected change in Cloud Storage bucket: %s", event.Subject())
    	fmt.Fprintln(w, s)
    }
    

### C#
    
    
    using Microsoft.AspNetCore.Builder;
    using Microsoft.AspNetCore.Hosting;
    using Microsoft.AspNetCore.Http;
    using [Microsoft.Extensions.DependencyInjection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Microsoft.Extensions.DependencyInjection.html);
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
                    logger.LogInformation("Handling HTTP POST");
    
                    var ceSubject = context.Request.Headers["ce-subject"];
                    logger.LogInformation($"ce-subject: {ceSubject}");
    
                    if (string.IsNullOrEmpty(ceSubject))
                    {
                        context.Response.StatusCode = 400;
                        await context.Response.WriteAsync("Bad Request: expected header Ce-Subject");
                        return;
                    }
    
                    await context.Response.WriteAsync($"GCS CloudEvent type: {ceSubject}");
                });
            });
        }
    }
    

###  Pub/Sub 

The sample code shows you how to read Pub/Sub events in a service deployed to Cloud Run.

### Python
    
    
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
    
    

### Java
    
    
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

### Go
    
    
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
    

### C#
    
    
    using CloudNative.CloudEvents;
    using CloudNative.CloudEvents.AspNetCore;
    using Google.Events.Protobuf.Cloud.PubSub.V1;
    using Microsoft.AspNetCore.Builder;
    using Microsoft.AspNetCore.Hosting;
    using Microsoft.AspNetCore.Http;
    using [Microsoft.Extensions.DependencyInjection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Microsoft.Extensions.DependencyInjection.html);
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
    

## What's next

  * [Event providers and destinations](https://docs.cloud.google.com/eventarc/standard/docs/event-providers-targets)
  * [Event routes](https://docs.cloud.google.com/eventarc/standard/docs/run/event-routing-options)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
