---
url: https://docs.cloud.google.com/functions/docs/samples/functions-concepts-stateless/
title: Statelessness \u00a0|\u00a0 Cloud Run functions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:51:51.059192+00:00
---

# Statelessness  |  Cloud Run functions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/docs/samples/functions-concepts-stateless/

If you are creating a new function, see the [Console Quickstart](https://docs.cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ Samples ](https://docs.cloud.google.com/functions/docs/samples)



#  Statelessness Stay organized with collections  Save and categorize content based on your preferences. 

An example of what variable state function instances do (and don't) store.

## Code sample

### C#

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using Google.Cloud.Functions.Framework;
    using Microsoft.AspNetCore.Http;
    using System.Threading;
    using System.Threading.Tasks;
    
    namespace ExecutionCount;
    
    public class Function : IHttpFunction
    {
        // Note that this variable must be static, because a new instance is
        // created for each request. An alternative approach would be to use
        // dependency injection with a singleton resource injected into the function
        // constructor.
        private static int _count;
    
        public async Task HandleAsync(HttpContext context)
        {
            // Note: the total function invocation count across
            // all servers may not be equal to this value!
            int currentCount = Interlocked.Increment(ref _count);
            await context.Response.WriteAsync($"Server execution count: {currentCount}", context.RequestAborted);
        }
    }

### Go

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Package http provides a set of HTTP Cloud Functions samples.
    package http
    
    import (
    	"fmt"
    	"net/http"
    
    	"github.com/GoogleCloudPlatform/functions-framework-go/functions"
    )
    
    // count is a global variable, but only shared within a function instance.
    var count = 0
    
    func init() {
    	functions.HTTP("ExecutionCount", ExecutionCount)
    }
    
    // ExecutionCount is an HTTP Cloud Function that counts how many times it
    // is executed within a specific instance.
    func ExecutionCount(w http.ResponseWriter, r *http.Request) {
    	count++
    
    	// Note: the total function invocation count across
    	// all instances may not be equal to this value!
    	fmt.Fprintf(w, "Instance execution count: %d", count)
    }
    

### Java

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.functions.HttpFunction;
    import com.google.cloud.functions.HttpRequest;
    import com.google.cloud.functions.HttpResponse;
    import java.io.BufferedWriter;
    import java.io.IOException;
    import java.util.concurrent.atomic.AtomicInteger;
    
    public class ExecutionCount implements HttpFunction {
    
      private final AtomicInteger count = new AtomicInteger(0);
    
      @Override
      public void service(HttpRequest request, HttpResponse response)
          throws IOException {
        count.getAndIncrement();
    
        // Note: the total function invocation count across
        // all instances may not be equal to this value!
        BufferedWriter writer = response.getWriter();
        writer.write("Instance execution count: " + count);
      }
    }

### Node.js

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const functions = require('@google-cloud/functions-framework');
    
    // Global variable, but only shared within function instance.
    let count = 0;
    
    /**
     * HTTP Cloud Function that counts how many times
     * it is executed within a specific instance.
     *
     * @param {Object} req Cloud Function request context.
     * @param {Object} res Cloud Function response context.
     */
    functions.http('executionCount', (req, res) => {
      count++;
    
      // Note: the total function invocation count across
      // all instances may not be equal to this value!
      res.send(`Instance execution count: ${count}`);
    });

### Python

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import functions_framework
    
    
    # Global variable, modified within the function by using the global keyword.
    count = 0
    
    
    @functions_framework.http
    def statelessness(request):
        """
        HTTP Cloud Function that counts how many times it is executed
        within a specific instance.
        Args:
            request (flask.Request): The request object.
            <http://flask.pocoo.org/docs/1.0/api/#flask.Request>
        Returns:
            The response text, or any set of values that can be turned into a
            Response object using `make_response`
            <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>.
        """
        global count
        count += 1
    
        # Note: the total function invocation count across
        # all instances may not be equal to this value!
        return f"Instance execution count: {count}"
    
    

### Ruby

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "functions_framework"
    
    # Global variable, but scoped only within one function instance.
    $count = 0
    
    FunctionsFramework.http "execution_count" do |_request|
      $count += 1
    
      # NOTE: the total function invocation count across all instances
      # may not be equal to this value!
      "Instance execution count: #{$count}"
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudfunctions). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
