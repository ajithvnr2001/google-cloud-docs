---
url: https://docs.cloud.google.com/functions/docs/samples/functions-http-content/
title: HTTP request body \u00a0|\u00a0 Cloud Run functions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:03:37.013642+00:00
---

# HTTP request body  |  Cloud Run functions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/docs/samples/functions-http-content/

If you are creating a new function, see the [Console Quickstart](https://docs.cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ Samples ](https://docs.cloud.google.com/functions/docs/samples)



#  HTTP request body Stay organized with collections  Save and categorize content based on your preferences. 

Parses a request body.

## Code sample

### C#

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using Google.Cloud.Functions.Framework;
    using Microsoft.AspNetCore.Http;
    using Microsoft.Extensions.Primitives;
    using System;
    using System.IO;
    using System.Net;
    using System.Net.Mime;
    using System.Text;
    using System.Text.Json;
    using System.Threading.Tasks;
    
    namespace ParseContentType;
    
    public class Function : IHttpFunction
    {
        public async Task HandleAsync(HttpContext context)
        {
            HttpRequest request = context.Request;
            HttpResponse response = context.Response;
    
            string name = null;
            ContentType contentType = new ContentType(request.ContentType);
    
            switch (contentType.MediaType)
            {
                case "application/json":
                {
                    // '{"name":"John"}'
                    using TextReader reader = new StreamReader(request.Body);
                    string json = await reader.ReadToEndAsync();
                    JsonElement body = JsonSerializer.Deserialize<JsonElement>(json);
                    if (body.TryGetProperty("name", out JsonElement property) && property.ValueKind == JsonValueKind.String)
                    {
                        name = property.GetString();
                    }
                    break;
                }
                case "application/octet-stream":
                {
                    // 'John', encoded to bytes using UTF-8, then encoded as base64
                    using TextReader reader = new StreamReader(request.Body);
                    string base64 = await reader.ReadToEndAsync();
                    byte[] data = Convert.FromBase64String(base64);
                    name = Encoding.UTF8.GetString(data);
                    break;
                }
                case "text/plain":
                {
                    // 'John'
                    using TextReader reader = new StreamReader(request.Body);
                    name = await reader.ReadLineAsync();
                    break;
                }
                case "application/x-www-form-urlencoded":
                {
                    // 'name=John' in the body of a POST request (not the URL)
                    if (request.Form.TryGetValue("name", out StringValues value))
                    {
                        name = value;
                    }
                    break;
                }
            }
            if (name is object)
            {
                await response.WriteAsync($"Hello {name}!", context.RequestAborted);
            }
            else
            {
                // Unrecognized content type, or the name wasn't in the content
                // (e.g. JSON without a "name" property)
                response.StatusCode = (int) HttpStatusCode.BadRequest;
            }
        }
    }

### Go

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Package http provides a set of HTTP Cloud Functions samples.
    package http
    
    import (
    	"encoding/json"
    	"fmt"
    	"html"
    	"io"
    	"log"
    	"net/http"
    
    	"github.com/GoogleCloudPlatform/functions-framework-go/functions"
    )
    
    func init() {
    	// Register an HTTP function with the Functions Framework
    	functions.HTTP("HelloContentType", HelloContentType)
    }
    
    // HelloContentType is an HTTP Cloud function.
    // It uses the Content-Type header to identify the request payload format.
    func HelloContentType(w http.ResponseWriter, r *http.Request) {
    	var name string
    
    	switch r.Header.Get("Content-Type") {
    	case "application/json":
    		var d struct {
    			Name string `json:"name"`
    		}
    		err := json.NewDecoder(r.Body).Decode(&d)
    		if err != nil {
    			log.Printf("error parsing application/json: %v", err)
    		} else {
    			name = d.Name
    		}
    	case "application/octet-stream":
    		body, err := io.ReadAll(r.Body)
    		if err != nil {
    			log.Printf("error parsing application/octet-stream: %v", err)
    		} else {
    			name = string(body)
    		}
    	case "text/plain":
    		body, err := io.ReadAll(r.Body)
    		if err != nil {
    			log.Printf("error parsing text/plain: %v", err)
    		} else {
    			name = string(body)
    		}
    	case "application/x-www-form-urlencoded":
    		if err := r.ParseForm(); err != nil {
    			log.Printf("error parsing application/x-www-form-urlencoded: %v", err)
    		} else {
    			name = r.FormValue("name")
    		}
    	}
    
    	if name == "" {
    		name = "World"
    	}
    
    	fmt.Fprintf(w, "Hello, %s!", html.EscapeString(name))
    }
    

### Java

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.functions.HttpFunction;
    import com.google.cloud.functions.HttpRequest;
    import com.google.cloud.functions.HttpResponse;
    import com.google.gson.Gson;
    import com.google.gson.JsonObject;
    import java.io.IOException;
    import java.io.PrintWriter;
    import java.net.HttpURLConnection;
    import java.nio.charset.StandardCharsets;
    import java.util.Base64;
    import java.util.Optional;
    
    public class ParseContentType implements HttpFunction {
    
      // Use GSON (https://github.com/google/gson) to parse JSON content.
      private static final Gson gson = new Gson();
    
      // Responds to an HTTP request using data from the request body parsed according to the
      // "content-type" header.
      @Override
      public void service(HttpRequest request, HttpResponse response)
          throws IOException {
        String name = null;
    
        // Default values avoid null issues (with switch/case) and exceptions from get() (optionals)
        String contentType = request.getContentType().orElse("");
    
        switch (contentType) {
          case "application/json":
            // '{"name":"John"}'
            JsonObject body = gson.fromJson(request.getReader(), JsonObject.class);
            if (body.has("name")) {
              name = body.get("name").getAsString();
            }
            break;
          case "application/octet-stream":
            // 'John', stored in a Buffer
            name = new String(Base64.getDecoder().decode(request.getInputStream().readAllBytes()),
                StandardCharsets.UTF_8);
            break;
          case "text/plain":
            // 'John'
            name = request.getReader().readLine();
            break;
          case "application/x-www-form-urlencoded":
            // 'name=John' in the body of a POST request (not the URL)
            Optional<String> nameParam = request.getFirstQueryParameter("name");
            if (nameParam.isPresent()) {
              name = nameParam.get();
            }
            break;
          default:
            // Invalid or missing "Content-Type" header
            response.setStatusCode(HttpURLConnection.HTTP_UNSUPPORTED_TYPE);
            return;
        }
    
        // Verify that a name was provided
        if (name == null) {
          response.setStatusCode(HttpURLConnection.HTTP_BAD_REQUEST);
        }
    
        // Respond with a name
        var writer = new PrintWriter(response.getWriter());
        writer.printf("Hello %s!", name);
      }
    }

### Node.js

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const escapeHtml = require('escape-html');
    const functions = require('@google-cloud/functions-framework');
    
    /**
     * Responds to an HTTP request using data from the request body parsed according
     * to the "content-type" header.
     *
     * @param {Object} req Cloud Function request context.
     * @param {Object} res Cloud Function response context.
     */
    functions.http('helloContent', (req, res) => {
      let name;
    
      switch (req.get('content-type')) {
        // '{"name":"John"}'
        case 'application/json':
          ({name} = req.body);
          break;
    
        // 'John', stored in a Buffer
        case 'application/octet-stream':
          name = req.body.toString(); // Convert buffer to a string
          break;
    
        // 'John'
        case 'text/plain':
          name = req.body;
          break;
    
        // 'name=John' in the body of a POST request (not the URL)
        case 'application/x-www-form-urlencoded':
          ({name} = req.body);
          break;
      }
    
      res.status(200).send(`Hello ${escapeHtml(name || 'World')}!`);
    });

### PHP

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Psr\Http\Message\ServerRequestInterface;
    
    function helloContent(ServerRequestInterface $request): string
    {
        $name = 'World';
        $body = $request->getBody()->getContents();
        switch ($request->getHeaderLine('content-type')) {
            // '{"name":"John"}'
            case 'application/json':
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
                break;
                // 'John', stored in a stream
            case 'application/octet-stream':
                $name = $body;
                break;
                // 'John'
            case 'text/plain':
                $name = $body;
                break;
                // 'name=John' in the body of a POST request (not the URL)
            case 'application/x-www-form-urlencoded':
                parse_str($body, $data);
                $name = $data['name'] ?? $name;
                break;
        }
    
        return sprintf('Hello %s!', htmlspecialchars($name));
    }
    

### Python

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import functions_framework
    
    
    from markupsafe import escape
    
    @functions_framework.http
    def hello_content(request):
        """Responds to an HTTP request using data from the request body parsed
        according to the "content-type" header.
        Args:
            request (flask.Request): The request object.
            <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
        Returns:
            The response text, or any set of values that can be turned into a
            Response object using `make_response`
            <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
        """
        content_type = request.headers["content-type"]
        if content_type == "application/json":
            request_json = request.get_json(silent=True)
            if request_json and "name" in request_json:
                name = request_json["name"]
            else:
                raise ValueError("JSON is invalid, or missing a 'name' property")
        elif content_type == "application/octet-stream":
            name = request.data
        elif content_type == "text/plain":
            name = request.data
        elif content_type == "application/x-www-form-urlencoded":
            name = request.form.get("name")
        else:
            raise ValueError(f"Unknown content type: {content_type}")
        return f"Hello {escape(name)}!"
    
    

### Ruby

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "functions_framework"
    require "json"
    
    FunctionsFramework.http "http_content" do |request|
      # The request parameter is a Rack::Request object.
      # See https://www.rubydoc.info/gems/rack/Rack/Request
      content_type = request.content_type
      case content_type
      # '{"name":"John"}'
      when "application/json"
        name = JSON.parse(request.body.read.to_s)["name"] rescue nil
      # "John", stored in a Buffer
      when "application/octet-stream"
        name = request.body.read.to_s # Convert buffer to a string
      # "John"
      when "text/plain"
        name = request.body.read.to_s
      # "name=John" in the body of a POST request (not the URL)
      when "application/x-www-form-urlencoded"
        name = request.params["name"] rescue nil
      end
    
      name ||= "World"
    
      # Return the response body as a string.
      # You can also return a Rack::Response object, a Rack response array, or
      # a hash which will be JSON-encoded into a response.
      "Hello #{name}!"
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudfunctions). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
