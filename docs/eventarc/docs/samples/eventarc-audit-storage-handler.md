---
url: https://docs.cloud.google.com/eventarc/docs/samples/eventarc-audit-storage-handler/
title: Create an event handler that receives and processes a Cloud Audit Log event with Cloud Storage data \u00a0|\u00a0 Eventarc \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:01:36.328496+00:00
---

# Create an event handler that receives and processes a Cloud Audit Log event with Cloud Storage data  |  Eventarc  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/eventarc/docs/samples/eventarc-audit-storage-handler/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Eventarc ](https://docs.cloud.google.com/eventarc/docs)
  * [ Samples ](https://docs.cloud.google.com/eventarc/docs/samples)



#  Create an event handler that receives and processes a Cloud Audit Log event with Cloud Storage data Stay organized with collections  Save and categorize content based on your preferences. 

Creates an event handler that receives an incoming Cloud Audit Log event within an HTTP POST request as a CloudEvent.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Develop event receivers](https://docs.cloud.google.com/eventarc/standard/docs/run/event-receivers)
  * [Tutorial: Debug routing events to Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/debugging-events-cloud-run)



## Code sample

### C#

To authenticate to Eventarc, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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
    

### Go

To authenticate to Eventarc, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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
    

### Java

To authenticate to Eventarc, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

To authenticate to Eventarc, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

### Python

To authenticate to Eventarc, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    @app.route("/", methods=["POST"])
    def index():
        # Create a CloudEvent object from the incoming request
        event = from_http(request.headers, request.data)
        # Gets the GCS bucket name from the CloudEvent
        # Example: "storage.googleapis.com/projects/_/buckets/my-bucket"
        bucket = event.get("subject")
    
        print(f"Detected change in Cloud Storage bucket: {bucket}")
        return (f"Detected change in Cloud Storage bucket: {bucket}", 200)
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=eventarc). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
