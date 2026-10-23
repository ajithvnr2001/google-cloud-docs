---
url: https://docs.cloud.google.com/functions/docs/samples/functions-http-method/
title: HTTP method types \u00a0|\u00a0 Cloud Run functions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:03:34.965903+00:00
---

# HTTP method types  |  Cloud Run functions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/docs/samples/functions-http-method/

If you are creating a new function, see the [Console Quickstart](https://docs.cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ Samples ](https://docs.cloud.google.com/functions/docs/samples)



#  HTTP method types Stay organized with collections  Save and categorize content based on your preferences. 

Shows how to handle HTTP method types (such as GET, PUT, and POST) in Cloud Functions.

## Code sample

### C#

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using Google.Cloud.Functions.Framework;
    using Microsoft.AspNetCore.Http;
    using System.Net;
    using System.Threading.Tasks;
    
    namespace HttpRequestMethod;
    
    public class Function : IHttpFunction
    {
        public async Task HandleAsync(HttpContext context)
        {
            HttpResponse response = context.Response;
            switch (context.Request.Method)
            {
                case "GET":
                    response.StatusCode = (int) HttpStatusCode.OK;
                    await response.WriteAsync("Hello world!", context.RequestAborted);
                    break;
                case "PUT":
                    response.StatusCode = (int) HttpStatusCode.Forbidden;
                    await response.WriteAsync("Forbidden!", context.RequestAborted);
                    break;
                default:
                    response.StatusCode = (int) HttpStatusCode.MethodNotAllowed;
                    await response.WriteAsync("Something blew up!", context.RequestAborted);
                    break;
            }
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
    
    func init() {
    	// Register an HTTP function with the Functions Framework
    	functions.HTTP("HelloHTTPMethod", HelloHTTPMethod)
    }
    
    // HelloHTTPMethod is an HTTP Cloud function.
    // It uses the request method to differentiate the response.
    func HelloHTTPMethod(w http.ResponseWriter, r *http.Request) {
    	switch r.Method {
    	case http.MethodGet:
    		fmt.Fprint(w, "Hello World!")
    	case http.MethodPut:
    		http.Error(w, "403 - Forbidden", http.StatusForbidden)
    	default:
    		http.Error(w, "405 - Method Not Allowed", http.StatusMethodNotAllowed)
    	}
    }
    

### Java

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.functions.HttpFunction;
    import com.google.cloud.functions.HttpRequest;
    import com.google.cloud.functions.HttpResponse;
    import java.io.BufferedWriter;
    import java.io.IOException;
    import java.net.HttpURLConnection;
    
    public class HttpMethod implements HttpFunction {
      @Override
      public void service(HttpRequest request, HttpResponse response)
          throws IOException {
    
        BufferedWriter writer = response.getWriter();
    
        switch (request.getMethod()) {
          case "GET":
            response.setStatusCode(HttpURLConnection.HTTP_OK);
            writer.write("Hello world!");
            break;
          case "PUT":
            response.setStatusCode(HttpURLConnection.HTTP_FORBIDDEN);
            writer.write("Forbidden!");
            break;
          default:
            response.setStatusCode(HttpURLConnection.HTTP_BAD_METHOD);
            writer.write("Something blew up!");
            break;
        }
      }
    }

### Node.js

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const functions = require('@google-cloud/functions-framework');
    
    /**
     * Responds to a GET request with "Hello World!". Forbids a PUT request.
     *
     * @example
     * gcloud functions call helloHttp
     *
     * @param {Object} req Cloud Function request context.
     * @param {Object} res Cloud Function response context.
     */
    functions.http('helloHttp', (req, res) => {
      switch (req.method) {
        case 'GET':
          res.status(200).send('Hello World!');
          break;
        case 'PUT':
          res.status(403).send('Forbidden!');
          break;
        default:
          res.status(405).send({error: 'Something blew up!'});
          break;
      }
    });

### PHP

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Psr\Http\Message\ResponseInterface;
    use Psr\Http\Message\ServerRequestInterface;
    use GuzzleHttp\Psr7\Response;
    
    function httpMethod(ServerRequestInterface $request): ResponseInterface
    {
        switch ($request->getMethod()) {
            case 'GET':
                // Example: read request
                return new Response(
                    200, // OK
                    [],
                    'Hello, World!' . PHP_EOL
                );
                break;
            case 'PUT':
                // Example: write request to a read-only resource
                return new Response(
                    403, // Permission denied
                    [],
                    'Forbidden!' . PHP_EOL
                );
                break;
            default:
                // Example: request type not supported by the application
                $json_payload = json_encode([
                    'error' => 'something blew up!'
                ]);
                return new Response(
                    405, // Method not allowed
                    ['Content-Type' => 'application/json'],
                    $json_payload
                );
                break;
        }
    }
    

### Python

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import functions_framework
    
    @functions_framework.http
    def hello_method(request):
        """Responds to a GET request with "Hello world!". Forbids a PUT request.
        Args:
            request (flask.Request): The request object.
            <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
        Returns:
            The response text, or any set of values that can be turned into a
            Response object using `make_response`
            <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
        """
        from flask import abort
    
        if request.method == "GET":
            return "Hello World!"
        elif request.method == "PUT":
            return abort(403)
        else:
            return abort(405)
    
    

### Ruby

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "functions_framework"
    require "json"
    
    FunctionsFramework.http "http_method" do |request|
      # The request parameter is a Rack::Request object.
      # See https://www.rubydoc.info/gems/rack/Rack/Request
      case request.request_method
      when "GET"
        status = 200
        body = "Hello World!"
      when "PUT"
        status = 403
        body = "Forbidden!"
      else
        status = 405
        body = '{"error":"Something blew up!"}'
      end
    
      # Return the response body as a Rack::Response object.
      ::Rack::Response.new body, status
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudfunctions). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
