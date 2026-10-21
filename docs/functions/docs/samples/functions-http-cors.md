---
url: https://docs.cloud.google.com/functions/docs/samples/functions-http-cors/
title: HTTP CORS \u00a0|\u00a0 Cloud Run functions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:03:36.306299+00:00
---

# HTTP CORS  |  Cloud Run functions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/docs/samples/functions-http-cors/

If you are creating a new function, see the [Console Quickstart](https://docs.cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ Samples ](https://docs.cloud.google.com/functions/docs/samples)



#  HTTP CORS Stay organized with collections  Save and categorize content based on your preferences. 

Shows how to make CORS-enabled requests with Cloud Functions.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Write Cloud Run functions](https://docs.cloud.google.com/run/docs/write-functions)
  * [Write HTTP functions](https://docs.cloud.google.com/functions/1stgendocs/writing/write-http-functions)



## Code sample

### C#

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using Google.Cloud.Functions.Framework;
    using Microsoft.AspNetCore.Http;
    using System.Net;
    using System.Threading.Tasks;
    
    namespace Cors;
    
    // For more information about CORS and CORS preflight requests, see
    // https://developer.mozilla.org/en-US/docs/Glossary/Preflight_request.
    public class Function : IHttpFunction
    {
        public async Task HandleAsync(HttpContext context)
        {
            HttpRequest request = context.Request;
            HttpResponse response = context.Response;
    
            // Set CORS headers
            //   Allows GETs from any origin with the Content-Type
            //   header and caches preflight response for 3600s
    
            response.Headers.Append("Access-Control-Allow-Origin", "*");
            if (HttpMethods.IsOptions(request.Method))
            {
                response.Headers.Append("Access-Control-Allow-Methods", "GET");
                response.Headers.Append("Access-Control-Allow-Headers", "Content-Type");
                response.Headers.Append("Access-Control-Max-Age", "3600");
                response.StatusCode = (int) HttpStatusCode.NoContent;
                return;
            }
    
            await response.WriteAsync("CORS headers set successfully!", context.RequestAborted);
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
    
    // CORSEnabledFunction is an example of setting CORS headers.
    // For more information about CORS and CORS preflight requests, see
    // https://developer.mozilla.org/en-US/docs/Glossary/Preflight_request.
    func CORSEnabledFunction(w http.ResponseWriter, r *http.Request) {
    	// Set CORS headers for the preflight request
    	if r.Method == http.MethodOptions {
    		w.Header().Set("Access-Control-Allow-Origin", "*")
    		w.Header().Set("Access-Control-Allow-Methods", "POST")
    		w.Header().Set("Access-Control-Allow-Headers", "Content-Type")
    		w.Header().Set("Access-Control-Max-Age", "3600")
    		w.WriteHeader(http.StatusNoContent)
    		return
    	}
    	// Set CORS headers for the main request.
    	w.Header().Set("Access-Control-Allow-Origin", "*")
    	fmt.Fprint(w, "Hello, World!")
    }
    
    func init() {
    	functions.HTTP("CORSEnabledFunction", CORSEnabledFunction)
    }
    

### Java

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.functions.HttpFunction;
    import com.google.cloud.functions.HttpRequest;
    import com.google.cloud.functions.HttpResponse;
    import java.io.BufferedWriter;
    import java.io.IOException;
    import java.net.HttpURLConnection;
    
    public class CorsEnabled implements HttpFunction {
      // corsEnabled is an example of setting CORS headers.
      // For more information about CORS and CORS preflight requests, see
      // https://developer.mozilla.org/en-US/docs/Glossary/Preflight_request.
      @Override
      public void service(HttpRequest request, HttpResponse response)
          throws IOException {
        // Set CORS headers
        //   Allows GETs from any origin with the Content-Type
        //   header and caches preflight response for 3600s
        response.appendHeader("Access-Control-Allow-Origin", "*");
    
        if ("OPTIONS".equals(request.getMethod())) {
          response.appendHeader("Access-Control-Allow-Methods", "GET");
          response.appendHeader("Access-Control-Allow-Headers", "Content-Type");
          response.appendHeader("Access-Control-Max-Age", "3600");
          response.setStatusCode(HttpURLConnection.HTTP_NO_CONTENT);
          return;
        }
    
        // Handle the main request.
        BufferedWriter writer = response.getWriter();
        writer.write("CORS headers set successfully!");
      }
    }

### Node.js

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const functions = require('@google-cloud/functions-framework');
    
    /**
     * HTTP function that supports CORS requests.
     *
     * @param {Object} req Cloud Function request context.
     * @param {Object} res Cloud Function response context.
     */
    functions.http('corsEnabledFunction', (req, res) => {
      // Set CORS headers for preflight requests
      // Allows GETs from any origin with the Content-Type header
      // and caches preflight response for 3600s
    
      res.set('Access-Control-Allow-Origin', '*');
    
      if (req.method === 'OPTIONS') {
        // Send response to OPTIONS requests
        res.set('Access-Control-Allow-Methods', 'GET');
        res.set('Access-Control-Allow-Headers', 'Content-Type');
        res.set('Access-Control-Max-Age', '3600');
        res.status(204).send('');
      } else {
        res.send('Hello World!');
      }
    });

### PHP

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Psr\Http\Message\ResponseInterface;
    use Psr\Http\Message\ServerRequestInterface;
    use GuzzleHttp\Psr7\Response;
    
    function corsEnabledFunction(ServerRequestInterface $request): ResponseInterface
    {
        // Set CORS headers for preflight requests
        // Allows GETs from any origin with the Content-Type header
        // and caches preflight response for 3600s
        $headers = ['Access-Control-Allow-Origin' => '*'];
    
        if ($request->getMethod() === 'OPTIONS') {
            // Send response to OPTIONS requests
            $headers = array_merge($headers, [
                'Access-Control-Allow-Methods' => 'GET',
                'Access-Control-Allow-Headers' => 'Content-Type',
                'Access-Control-Max-Age' => '3600'
            ]);
            return new Response(204, $headers, '');
        } else {
            return new Response(200, $headers, 'Hello World!');
        }
    }
    

### Python

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import functions_framework
    
    @functions_framework.http
    def cors_enabled_function(request):
        # For more information about CORS and CORS preflight requests, see:
        # https://developer.mozilla.org/en-US/docs/Glossary/Preflight_request
    
        # Set CORS headers for the preflight request
        if request.method == "OPTIONS":
            # Allows GET requests from any origin with the Content-Type
            # header and caches preflight response for an 3600s
            headers = {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "GET",
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Max-Age": "3600",
            }
    
            return ("", 204, headers)
    
        # Set CORS headers for the main request
        headers = {"Access-Control-Allow-Origin": "*"}
    
        return ("Hello World!", 200, headers)
    
    

### Ruby

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    FunctionsFramework.http "cors_enabled_function" do |request|
      # For more information about CORS and CORS preflight requests, see
      # https://developer.mozilla.org/en-US/docs/Glossary/Preflight_request
      # for more information.
    
      # Set CORS headers for the preflight request
      if request.options?
        # Allows GET requests from any origin with the Content-Type
        # header and caches preflight response for an 3600s
        headers = {
          "Access-Control-Allow-Origin"  => "*",
          "Access-Control-Allow-Methods" => "GET",
          "Access-Control-Allow-Headers" => "Content-Type",
          "Access-Control-Max-Age"       => "3600"
        }
        [204, headers, []]
      else
        # Set CORS headers for the main request
        headers = {
          "Access-Control-Allow-Origin" => "*"
        }
    
        [200, headers, ["Hello World!"]]
      end
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudfunctions). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
