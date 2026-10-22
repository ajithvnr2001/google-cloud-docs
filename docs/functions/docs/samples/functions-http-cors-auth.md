---
url: https://docs.cloud.google.com/functions/docs/samples/functions-http-cors-auth/
title: HTTP Auth with CORS \u00a0|\u00a0 Cloud Run functions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:51:21.039346+00:00
---

# HTTP Auth with CORS  |  Cloud Run functions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/docs/samples/functions-http-cors-auth/

If you are creating a new function, see the [Console Quickstart](https://docs.cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ Samples ](https://docs.cloud.google.com/functions/docs/samples)



#  HTTP Auth with CORS Stay organized with collections  Save and categorize content based on your preferences. 

HTTP function that supports CORS requests with credentials.

## Code sample

### Go

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Package http provides a set of HTTP Cloud Functions samples.
    package http
    
    import (
    	"fmt"
    	"net/http"
    
    	"github.com/GoogleCloudPlatform/functions-framework-go/functions"
    )
    
    // CORSEnabledFunctionAuth is an example of setting CORS headers with
    // authentication enabled.
    // For more information about CORS and CORS preflight requests, see
    // https://developer.mozilla.org/en-US/docs/Glossary/Preflight_request.
    func CORSEnabledFunctionAuth(w http.ResponseWriter, r *http.Request) {
    	// Set CORS headers for the preflight request
    	if r.Method == http.MethodOptions {
    		w.Header().Set("Access-Control-Allow-Credentials", "true")
    		w.Header().Set("Access-Control-Allow-Headers", "Authorization")
    		w.Header().Set("Access-Control-Allow-Methods", "POST")
    		w.Header().Set("Access-Control-Allow-Origin", "https://example.com")
    		w.Header().Set("Access-Control-Max-Age", "3600")
    		w.WriteHeader(http.StatusNoContent)
    		return
    	}
    	// Set CORS headers for the main request.
    	w.Header().Set("Access-Control-Allow-Credentials", "true")
    	w.Header().Set("Access-Control-Allow-Origin", "https://example.com")
    	fmt.Fprint(w, "Hello World!")
    }
    
    func init() {
    	functions.HTTP("CORSEnabledFunctionAuth", CORSEnabledFunctionAuth)
    }
    

### Java

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.functions.HttpFunction;
    import com.google.cloud.functions.HttpRequest;
    import com.google.cloud.functions.HttpResponse;
    import java.io.BufferedWriter;
    import java.io.IOException;
    import java.net.HttpURLConnection;
    
    public class CorsEnabledAuth implements HttpFunction {
      // corsEnabledAuth is an example of setting CORS headers.
      // For more information about CORS and CORS preflight requests, see
      // https://developer.mozilla.org/en-US/docs/Glossary/Preflight_request.
      @Override
      public void service(HttpRequest request, HttpResponse response)
          throws IOException {
        // Set CORS headers
        //   Allows GETs from origin https://mydomain.com
        //   with the Authorization header present
        response.appendHeader("Access-Control-Allow-Origin", "https://mydomain.com");
        response.appendHeader("Access-Control-Allow-Credentials", "true");
    
        if ("OPTIONS".equals(request.getMethod())) {
          response.appendHeader("Access-Control-Allow-Methods", "GET");
          response.appendHeader("Access-Control-Allow-Headers", "Authorization");
          response.appendHeader("Access-Control-Max-Age", "3600");
          response.setStatusCode(HttpURLConnection.HTTP_NO_CONTENT);
          return;
        }
    
        // Handle the main request
        BufferedWriter writer = response.getWriter();
        writer.write("CORS headers set successfully!");
      }
    }

### Node.js

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const functions = require('@google-cloud/functions-framework');
    
    /**
     * HTTP function that supports CORS requests with credentials.
     *
     * @param {Object} req Cloud Function request context.
     * @param {Object} res Cloud Function response context.
     */
    functions.http('corsEnabledFunctionAuth', (req, res) => {
      // Set CORS headers for preflight requests
      // Allows GETs from origin https://mydomain.com with Authorization header
    
      res.set('Access-Control-Allow-Origin', 'https://mydomain.com');
      res.set('Access-Control-Allow-Credentials', 'true');
    
      if (req.method === 'OPTIONS') {
        // Send response to OPTIONS requests
        res.set('Access-Control-Allow-Methods', 'GET');
        res.set('Access-Control-Allow-Headers', 'Authorization');
        res.set('Access-Control-Max-Age', '3600');
        res.status(204).send('');
      } else {
        res.send('Hello World!');
      }
    });

### Python

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import functions_framework
    
    @functions_framework.http
    def cors_enabled_function_auth(request):
        # For more information about CORS and CORS preflight requests, see
        # https://developer.mozilla.org/en-US/docs/Glossary/Preflight_request
        # for more information.
    
        # Set CORS headers for preflight requests
        if request.method == "OPTIONS":
            # Allows GET requests from origin https://mydomain.com with
            # Authorization header
            headers = {
                "Access-Control-Allow-Origin": "https://mydomain.com",
                "Access-Control-Allow-Methods": "GET",
                "Access-Control-Allow-Headers": "Authorization",
                "Access-Control-Max-Age": "3600",
                "Access-Control-Allow-Credentials": "true",
            }
            return ("", 204, headers)
    
        # Set CORS headers for main requests
        headers = {
            "Access-Control-Allow-Origin": "https://mydomain.com",
            "Access-Control-Allow-Credentials": "true",
        }
    
        return ("Hello World!", 200, headers)
    
    

### Ruby

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    FunctionsFramework.http "cors_enabled_function_auth" do |request|
      # For more information about CORS and CORS preflight requests, see
      # https://developer.mozilla.org/en-US/docs/Glossary/Preflight_request
      # for more information.
    
      # Set CORS headers for preflight requests
      if request.options?
        # Allows GET requests from origin https://mydomain.com with
        # Authorization header
        headers = {
          "Access-Control-Allow-Origin"      => "https://mydomain.com",
          "Access-Control-Allow-Methods"     => "GET",
          "Access-Control-Allow-Headers"     => "Authorization",
          "Access-Control-Max-Age"           => "3600",
          "Access-Control-Allow-Credentials" => "true"
        }
        [204, headers, []]
      else
        # Set CORS headers for main requests
        headers = {
          "Access-Control-Allow-Origin"      => "https://mydomain.com",
          "Access-Control-Allow-Credentials" => "true"
        }
    
        [200, headers, ["Hello World!"]]
      end
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudfunctions). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
