---
url: https://docs.cloud.google.com/functions/docs/samples/functions-log-helloworld/
title: Write logs \u00a0|\u00a0 Cloud Run functions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:51:19.712368+00:00
---

# Write logs  |  Cloud Run functions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/docs/samples/functions-log-helloworld/

If you are creating a new function, see the [Console Quickstart](https://docs.cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ Samples ](https://docs.cloud.google.com/functions/docs/samples)



#  Write logs Stay organized with collections  Save and categorize content based on your preferences. 

Writes a Cloud Functions log entry.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [View and write Cloud Run function logs](https://docs.cloud.google.com/functions/1stgendocs/monitoring/logging)



## Code sample

### C#

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using Google.Cloud.Functions.Framework;
    using Microsoft.AspNetCore.Http;
    using Microsoft.Extensions.Logging;
    using System;
    using System.Threading.Tasks;
    
    namespace LogHelloWorld;
    
    public class Function : IHttpFunction
    {
        private readonly ILogger _logger;
    
        public Function(ILogger<Function> logger) =>
            _logger = logger;
    
        public async Task HandleAsync(HttpContext context)
        {
            Console.WriteLine("I am a log to stdout!");
            Console.Error.WriteLine("I am a log to stderr!");
    
            _logger.LogInformation("I am an info log!");
            _logger.LogWarning("I am a warning log!");
    
            await context.Response.WriteAsync("Messages successfully logged!", context.RequestAborted);
        }
    }

### Go

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Package helloworld provides a set of Cloud Functions samples.
    package helloworld
    
    import (
    	"fmt"
    	"log"
    	"net/http"
    
    	"github.com/GoogleCloudPlatform/functions-framework-go/functions"
    )
    
    func init() {
    	functions.HTTP("HelloLogging", HelloLogging)
    }
    
    // HelloLogging logs messages.
    func HelloLogging(w http.ResponseWriter, r *http.Request) {
    	log.Println("This is stderr")
    	fmt.Println("This is stdout")
    
    	// Structured logging can be used to set severity levels.
    	// See https://cloud.google.com/logging/docs/structured-logging.
    	fmt.Println(`{"message": "This has ERROR severity", "severity": "error"}`)
    
    	// cloud.google.com/go/logging can optionally be used for additional options.
    }
    

### Java

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.functions.HttpFunction;
    import com.google.cloud.functions.HttpRequest;
    import com.google.cloud.functions.HttpResponse;
    import java.io.BufferedWriter;
    import java.io.IOException;
    import java.util.logging.Logger;
    
    public class LogHelloWorld implements HttpFunction {
    
      private static final Logger logger = Logger.getLogger(LogHelloWorld.class.getName());
    
      @Override
      public void service(HttpRequest request, HttpResponse response)
          throws IOException {
        System.out.println("I am a log to stdout!");
        System.err.println("I am a log to stderr!");
    
        logger.info("I am an info log!");
        logger.warning("I am a warning log!");
    
        BufferedWriter writer = response.getWriter();
        writer.write("Messages successfully logged!");
      }
    }

### Node.js

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const functions = require('@google-cloud/functions-framework');
    
    functions.http('helloWorld', (req, res) => {
      console.log('I am a log entry!');
      console.error('I am an error!');
      res.end();
    });

### PHP

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Psr\Http\Message\ServerRequestInterface;
    
    function helloLogging(ServerRequestInterface $request): string
    {
        // Code running in Google Cloud Functions itself writes log entries to
        // Cloud Logging. (Default log severity level is INFO.)
        $log = fopen('php://stderr', 'wb');
        fwrite($log, "Log entry from fwrite().\n");
    
        // You can also specify a severity level explicitly using structured logs.
        // See this page for a list of log severity values:
        //   https://cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#LogSeverity
        fwrite($log, json_encode([
          'message' => 'Structured log with error severity',
          'severity' => 'error'
        ]) . PHP_EOL);
    
        // This will log to standard error, which will appear in Cloud Logging
        error_log('error_log logs in Cloud Functions!');
    
        // This will log an error message and immediately terminate the function execution
        // trigger_error('fatal errors are logged!');
    
        // For HTTP functions, this is added to the HTTP response
        // For CloudEvent functions, this does nothing
        var_dump('var_dump goes to HTTP response for HTTP functions');
    
        // You can also dump variables using var_export() and forward
        // the resulting string to Cloud Logging via an fwrite() call.
        $entry = var_export('var_export output can be captured.', true);
        fwrite($log, $entry);
    
        // Functions must return a String or PSR-7 Response object
        return '';
    }
    

### Python

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def hello_world(data, context):
        """Background Cloud Function.
        Args:
             data (dict): The dictionary with data specific to the given event.
             context (google.cloud.functions.Context): The event metadata.
        """
        print("Hello, stdout!")
    
    

### Ruby

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "functions_framework"
    
    FunctionsFramework.http "log-helloworld" do |_request|
      # Any output sent to either stdout or stderr will be captured and written to
      # the function's logs.
      puts "Hello, stdout!"
      warn "Hello, stderr!"
    
      # Return the response body as a string.
      "Hello, world!"
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudfunctions). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
