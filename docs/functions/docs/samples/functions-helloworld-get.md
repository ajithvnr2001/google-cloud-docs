---
url: https://docs.cloud.google.com/functions/docs/samples/functions-helloworld-get/
title: HTTP Hello World - Get \u00a0|\u00a0 Cloud Run functions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:03:36.204348+00:00
---

# HTTP Hello World - Get  |  Cloud Run functions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/docs/samples/functions-helloworld-get/

If you are creating a new function, see the [Console Quickstart](https://docs.cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ Samples ](https://docs.cloud.google.com/functions/docs/samples)



#  HTTP Hello World - Get Stay organized with collections  Save and categorize content based on your preferences. 

Function that prints "Hello world!" in response to a GET request.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [HTTP Tutorial](https://docs.cloud.google.com/functions/1stgendocs/tutorials/http-1st-gen)
  * [JVM Languages](https://docs.cloud.google.com/functions/1stgendocs/concepts/jvm-langs)
  * [Quickstart: Create and deploy an HTTP Cloud Run function by using Java](https://docs.cloud.google.com/functions/1stgendocs/create-deploy-http-java-1st-gen)
  * [Quickstart: Deploy a Cloud Run function using the gcloud CLI](https://docs.cloud.google.com/run/docs/quickstarts/functions/deploy-functions-gcloud)



## Code sample

### C#

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using Google.Cloud.Functions.Framework;
    using Microsoft.AspNetCore.Http;
    using System.Threading.Tasks;
    
    namespace HelloWorld;
    
    public class Function : IHttpFunction
    {
        public async Task HandleAsync(HttpContext context)
        {
            await context.Response.WriteAsync("Hello World!", context.RequestAborted);
        }
    }

### Go

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Package helloworld provides a set of Cloud Functions samples.
    package helloworld
    
    import (
    	"fmt"
    	"net/http"
    
    	"github.com/GoogleCloudPlatform/functions-framework-go/functions"
    )
    
    func init() {
    	functions.HTTP("HelloGet", helloGet)
    }
    
    // helloGet is an HTTP Cloud Function.
    func helloGet(w http.ResponseWriter, r *http.Request) {
    	fmt.Fprint(w, "Hello, World!")
    }
    

### Java

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    package functions;
    
    import com.google.cloud.functions.HttpFunction;
    import com.google.cloud.functions.HttpRequest;
    import com.google.cloud.functions.HttpResponse;
    import java.io.BufferedWriter;
    import java.io.IOException;
    
    public class HelloWorld implements HttpFunction {
      // Simple function to return "Hello World"
      @Override
      public void service(HttpRequest request, HttpResponse response)
          throws IOException {
        BufferedWriter writer = response.getWriter();
        writer.write("Hello World!");
      }
    }

### Kotlin
    
    
    import com.google.cloud.functions.HttpFunction
    import com.google.cloud.functions.HttpRequest
    import com.google.cloud.functions.HttpResponse
    import java.io.IOException
    import java.util.logging.Logger
    
    class HelloWorld : HttpFunction {
        // Simple function to return "Hello World"
        @Throws(IOException::class)
        override fun service(request: HttpRequest, response: HttpResponse) {
            response.writer.write("Hello World!")
        }
    }

### Node.js

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const functions = require('@google-cloud/functions-framework');
    
    // Register an HTTP function with the Functions Framework that will be executed
    // when you make an HTTP request to the deployed function's endpoint.
    functions.http('helloGET', (req, res) => {
      res.send('Hello World!');
    });

### PHP

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Psr\Http\Message\ServerRequestInterface;
    
    function helloGet(ServerRequestInterface $request): string
    {
        return 'Hello, World!' . PHP_EOL;
    }
    

### Python

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import functions_framework
    
    @functions_framework.http
    def hello_get(request):
        """HTTP Cloud Function.
        Args:
            request (flask.Request): The request object.
            <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
        Returns:
            The response text, or any set of values that can be turned into a
            Response object using `make_response`
            <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
        Note:
            For more information on how Flask integrates with Cloud
            Functions, see the `Writing HTTP functions` page.
            <https://cloud.google.com/functions/docs/writing/http#http_frameworks>
        """
        return "Hello World!"
    
    

### Ruby

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "functions_framework"
    
    FunctionsFramework.http "hello_get" do |_request|
      # The request parameter is a Rack::Request object.
      # See https://www.rubydoc.info/gems/rack/Rack/Request
    
      # Return the response body as a string.
      # You can also return a Rack::Response object, a Rack response array, or
      # a hash which will be JSON-encoded into a response.
      "Hello World!"
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudfunctions). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
