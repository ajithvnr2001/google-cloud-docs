---
url: https://docs.cloud.google.com/functions/docs/samples/functions-helloworld-http/
title: HTTP Hello World \u00a0|\u00a0 Cloud Run functions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:51:53.865355+00:00
---

# HTTP Hello World  |  Cloud Run functions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/docs/samples/functions-helloworld-http/

If you are creating a new function, see the [Console Quickstart](https://docs.cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ Samples ](https://docs.cloud.google.com/functions/docs/samples)



#  HTTP Hello World Stay organized with collections  Save and categorize content based on your preferences. 

HTTP function responds with "Hello, world!"

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Functions best practices](https://docs.cloud.google.com/run/docs/tips/functions-best-practices)
  * [Quickstart: Create and deploy a HTTP Cloud Run function by using Node.js (1st gen)](https://docs.cloud.google.com/functions/1stgendocs/create-deploy-http-nodejs-1st-gen)
  * [Quickstart: Create and deploy an HTTP Cloud Run function by using Go](https://docs.cloud.google.com/functions/1stgendocs/create-deploy-http-go-1st-gen)
  * [Quickstart: Create and deploy an HTTP Cloud Run function by using Python](https://docs.cloud.google.com/functions/1stgendocs/create-deploy-http-python-1st-gen)
  * [Quickstart: Create and deploy an HTTP Cloud Run function by using Ruby](https://docs.cloud.google.com/functions/1stgendocs/create-deploy-http-ruby-1st-gen)
  * [Specify dependencies in Node.js](https://docs.cloud.google.com/functions/1stgendocs/writing/specifying-dependencies-nodejs)
  * [Specify dependencies in Node.js](https://docs.cloud.google.com/run/docs/runtimes/nodejs-dependencies)
  * [Tips & Tricks](https://docs.cloud.google.com/functions/1stgendocs/bestpractices/tips)



## Code sample

### C#

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using Google.Cloud.Functions.Framework;
    using Microsoft.AspNetCore.Http;
    using Microsoft.Extensions.Logging;
    using System.IO;
    using System.Text.Json;
    using System.Threading.Tasks;
    
    namespace HelloHttp;
    
    public class Function : IHttpFunction
    {
        private readonly ILogger _logger;
    
        public Function(ILogger<Function> logger) =>
            _logger = logger;
    
        public async Task HandleAsync(HttpContext context)
        {
            HttpRequest request = context.Request;
            // Check URL parameters for "name" field
            // "world" is the default value
            string name = ((string) request.Query["name"]) ?? "world";
    
            // If there's a body, parse it as JSON and check for "name" field.
            using TextReader reader = new StreamReader(request.Body);
            string text = await reader.ReadToEndAsync();
            if (text.Length > 0)
            {
                try
                {
                    JsonElement json = JsonSerializer.Deserialize<JsonElement>(text);
                    if (json.TryGetProperty("name", out JsonElement nameElement) &&
                        nameElement.ValueKind == JsonValueKind.String)
                    {
                        name = nameElement.GetString();
                    }
                }
                catch (JsonException parseException)
                {
                    _logger.LogError(parseException, "Error parsing JSON request");
                }
            }
    
            await context.Response.WriteAsync($"Hello {name}!", context.RequestAborted);
        }
    }

### Go

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Package helloworld provides a set of Cloud Functions samples.
    package helloworld
    
    import (
    	"encoding/json"
    	"fmt"
    	"html"
    	"net/http"
    
    	"github.com/GoogleCloudPlatform/functions-framework-go/functions"
    )
    
    func init() {
    	functions.HTTP("HelloHTTP", HelloHTTP)
    }
    
    // HelloHTTP is an HTTP Cloud Function with a request parameter.
    func HelloHTTP(w http.ResponseWriter, r *http.Request) {
    	var d struct {
    		Name string `json:"name"`
    	}
    	if err := json.NewDecoder(r.Body).Decode(&d); err != nil {
    		fmt.Fprint(w, "Hello, World!")
    		return
    	}
    	if d.Name == "" {
    		fmt.Fprint(w, "Hello, World!")
    		return
    	}
    	fmt.Fprintf(w, "Hello, %s!", html.EscapeString(d.Name))
    }
    

### Java

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.functions.HttpFunction;
    import com.google.cloud.functions.HttpRequest;
    import com.google.cloud.functions.HttpResponse;
    import com.google.gson.Gson;
    import com.google.gson.JsonElement;
    import com.google.gson.JsonObject;
    import com.google.gson.JsonParseException;
    import java.io.IOException;
    import java.io.PrintWriter;
    import java.util.logging.Logger;
    
    public class HelloHttp implements HttpFunction {
      private static final Logger logger = Logger.getLogger(HelloHttp.class.getName());
    
      private static final Gson gson = new Gson();
    
      @Override
      public void service(HttpRequest request, HttpResponse response)
          throws IOException {
        // Check URL parameters for "name" field
        // "world" is the default value
        String name = request.getFirstQueryParameter("name").orElse("world");
    
        // Parse JSON request and check for "name" field
        try {
          JsonElement requestParsed = gson.fromJson(request.getReader(), JsonElement.class);
          JsonObject requestJson = null;
    
          if (requestParsed != null && requestParsed.isJsonObject()) {
            requestJson = requestParsed.getAsJsonObject();
          }
    
          if (requestJson != null && requestJson.has("name")) {
            name = requestJson.get("name").getAsString();
          }
        } catch (JsonParseException e) {
          logger.severe("Error parsing JSON: " + e.getMessage());
        }
    
        var writer = new PrintWriter(response.getWriter());
        writer.printf("Hello %s!", name);
      }
    }

### Node.js

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const functions = require('@google-cloud/functions-framework');
    const escapeHtml = require('escape-html');
    
    /**
     * Responds to an HTTP request using data from the request body parsed according
     * to the "content-type" header.
     *
     * @param {Object} req Cloud Function request context.
     * @param {Object} res Cloud Function response context.
     */
    functions.http('helloHttp', (req, res) => {
      const name =
        (req.query && req.query.name) || (req.body && req.body.name) || 'World';
    
      res.send(`Hello ${escapeHtml(name)}!`);
    });

### PHP

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    <?php
    
    use Google\CloudFunctions\FunctionsFramework;
    use Psr\Http\Message\ServerRequestInterface;
    
    // Register the function with Functions Framework.
    // This enables omitting the `FUNCTIONS_SIGNATURE_TYPE=http` environment
    // variable when deploying. The `FUNCTION_TARGET` environment variable should
    // match the first parameter.
    FunctionsFramework::http('helloHttp', 'helloHttp');
    
    function helloHttp(ServerRequestInterface $request): string
    {
        $name = 'World';
        $body = $request->getBody()->getContents();
        if (!empty($body)) {
            $json = json_decode($body, true);
            if (json_last_error() != JSON_ERROR_NONE) {
                throw new RuntimeException(sprintf(
                    'Could not parse body: %s',
                    json_last_error_msg()
                ));
            }
            $name = $json['name'] ?? $name;
        }
        $queryString = $request->getQueryParams();
        $name = $queryString['name'] ?? $name;
    
        return sprintf('Hello, %s!', htmlspecialchars($name));
    }
    

### Python

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import functions_framework
    
    
    from markupsafe import escape
    
    @functions_framework.http
    def hello_http(request):
        """HTTP Cloud Function.
        Args:
            request (flask.Request): The request object.
            <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
        Returns:
            The response text, or any set of values that can be turned into a
            Response object using `make_response`
            <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
        """
        request_json = request.get_json(silent=True)
        request_args = request.args
    
        if request_json and "name" in request_json:
            name = request_json["name"]
        elif request_args and "name" in request_args:
            name = request_args["name"]
        else:
            name = "World"
        return f"Hello {escape(name)}!"
    
    

### Ruby

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "functions_framework"
    require "cgi/escape"
    require "json"
    
    FunctionsFramework.http "hello_http" do |request|
      # The request parameter is a Rack::Request object.
      # See https://www.rubydoc.info/gems/rack/Rack/Request
      name = request.params["name"] ||
             begin
               request.body.rewind
               JSON.parse(request.body.read)["name"]
             rescue StandardError
               nil
             end ||
             "World"
      # Return the response body as a string.
      # You can also return a Rack::Response object, a Rack response array, or
      # a hash which will be JSON-encoded into a response.
      "Hello #{CGI.escape_html name}!"
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudfunctions). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
