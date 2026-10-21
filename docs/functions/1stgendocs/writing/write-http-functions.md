---
url: https://docs.cloud.google.com/functions/1stgendocs/writing/write-http-functions/
title: Write HTTP functions \u00a0|\u00a0 Cloud Run functions (1st gen) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:29:32.705104+00:00
---

# Write HTTP functions  |  Cloud Run functions (1st gen)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/1stgendocs/writing/write-http-functions/

If you are creating a new function, see the [Console Quickstart](https://cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. The content on this page only applies to existing legacy functions created with the Cloud Functions v1 API. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ 1st generation ](https://docs.cloud.google.com/functions/1stgendocs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/functions/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Write HTTP functions

In Cloud Run functions, you use HTTP functions when you want to invoke a function via an HTTP(S) request. To allow for HTTP semantics, HTTP function signatures accept HTTP-specific arguments.

## Implementation

The following example shows a basic HTTP function source file for each runtime. See [Source directory structure](https://docs.cloud.google.com/functions/1stgendocs/writing#directory-structure) for information about where to locate your source code.

###  Node.js 
    
    
    const functions = require('@google-cloud/functions-framework');
    
    // Register an HTTP function with the Functions Framework
    functions.http('myHttpFunction', (req, res) => {
      // Your code here
    
      // Send an HTTP response
      res.send('OK');
    });
    

In Node.js, you register an HTTP handler function with the [Functions Framework for Node.js](https://github.com/GoogleCloudPlatform/functions-framework-nodejs). Your HTTP handler function must be an [Express middleware function](https://expressjs.com/en/guide/writing-middleware.html) that accepts the [request](https://expressjs.com/en/4x/api.html#req) and [response](https://expressjs.com/en/4x/api.html#res) arguments and sends an HTTP response.

Cloud Run functions automatically parses the request body for you based on the request's `Content-Type` header using [`body-parser`](https://expressjs.com/en/resources/middleware/body-parser.html), so you can access the `req.body` and `req.rawBody` objects in your HTTP handler.

The [function entry point](https://docs.cloud.google.com/functions/1stgendocs/writing#entry-point) is the name with which the handler is registered with the Functions Framework. In this example, the entry point is `myHttpFunction`.

###  Python 
    
    
    import functions_framework
    
    # Register an HTTP function with the Functions Framework
    @functions_framework.http
    def my_http_function(request):
      # Your code here
    
      # Return an HTTP response
      return 'OK'
    

In Python, you register an HTTP handler function with the [Functions Framework for Python](https://github.com/GoogleCloudPlatform/functions-framework-python). Your HTTP handler function must accept a [Flask request](https://flask.palletsprojects.com/api/#flask.Request) object as an argument and return [a value that Flask can convert into an HTTP response object](https://flask.palletsprojects.com/en/2.3.x/quickstart/#about-responses).

The [function entry point](https://docs.cloud.google.com/functions/1stgendocs/writing#entry-point) is the name of the handler function registered with the Functions Framework. In this example, the entry point is `my_http_function`.

###  Go 
    
    
    package myhttpfunction
    
    import (
        "fmt"
        "net/http"
    
        "github.com/GoogleCloudPlatform/functions-framework-go/functions"
    )
    
    func init() {
        // Register an HTTP function with the Functions Framework
        functions.HTTP("MyHTTPFunction", myHTTPFunction)
    }
    
    // Function myHTTPFunction is an HTTP handler
    func myHTTPFunction(w http.ResponseWriter, r *http.Request) {
        // Your code here
    
        // Send an HTTP response
        fmt.Fprintln(w, "OK")
    }
    

In Go, you register an HTTP handler function with the [Functions Framework for Go](https://github.com/GoogleCloudPlatform/functions-framework-go) in your `init()` function. Your HTTP handler function must use the standard [`http.HandlerFunc`](https://pkg.go.dev/net/http#HandlerFunc) interface to send an HTTP response.

The [function entry point](https://docs.cloud.google.com/functions/1stgendocs/writing#entry-point) is the name with which the handler is registered with the Functions Framework. In this example, the entry point is `MyHTTPFunction`.

Your HTTP handler function must implement the standard [`http.HandlerFunc`](https://pkg.go.dev/net/http#HandlerFunc) interface. It accepts an [http.ResponseWriter](https://pkg.go.dev/net/http#ResponseWriter) interface that your function uses to create a reply to the request, and a pointer to an [http.Request](https://pkg.go.dev/net/http#Request) struct containing the details of the inbound HTTP request.

###  Java 
    
    
    package myhttpfunction;
    
    import com.google.cloud.functions.HttpFunction;
    import com.google.cloud.functions.HttpRequest;
    import com.google.cloud.functions.HttpResponse;
    
    // Define a class that implements the HttpFunction interface
    public class MyHttpFunction implements HttpFunction {
      // Implement the service() method to handle HTTP requests
      @Override
      public void service(HttpRequest request, HttpResponse response) throws Exception {
        // Your code here
    
        // Send an HTTP response
        response.getWriter().write("OK");
      }
    }
    

In Java, you use the [Functions Framework Java API](https://javadoc.io/doc/com.google.cloud.functions/functions-framework-api/) to implement an HTTP handler class with the [`HttpFunction`](https://javadoc.io/doc/com.google.cloud.functions/functions-framework-api/latest/com/google/cloud/functions/HttpFunction.html) interface. The `service()` method must send an HTTP response.

The [function entry point](https://docs.cloud.google.com/functions/1stgendocs/writing#entry-point) is the fully-qualified name of the HTTP handler class, including the package name. In this example, the entry point is `myhttpfunction.MyHttpFunction`.

Your `service` method receives an [`HttpRequest`](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpRequest) object describing the inbound HTTP request, and an [`HttpResponse`](https://cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpResponse) object that your function populates with a response message. 

###  C# 
    
    
    using Google.Cloud.Functions.Framework;
    using Microsoft.AspNetCore.Http;
    using System.Threading.Tasks;
    
    namespace MyProject
    {
        // Define a class that implements the IHttpFunction interface
        public class MyHttpFunction : IHttpFunction
        {
            // Implement the HandleAsync() method to handle HTTP requests
            public async Task HandleAsync(HttpContext context)
            {
                // Your code here
    
                // Send an HTTP response
                await context.Response.WriteAsync("OK");
            }
        }
    }
    

In .NET runtimes, you use the [Functions Framework for .NET](https://github.com/GoogleCloudPlatform/functions-framework-dotnet) to implement an HTTP handler class with the [`IHttpFunction`](https://github.com/GoogleCloudPlatform/functions-framework-dotnet/blob/main/src/Google.Cloud.Functions.Framework/IHttpFunction.cs) interface. The `HandleAsync()` method accepts a standard ASP.NET [`HttpContext`](https://docs.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.http.httpcontext) object as an argument and must send an HTTP response.

The [function entry point](https://docs.cloud.google.com/functions/1stgendocs/writing#entry-point) is the fully-qualified name of the HTTP handler class, including the namespace. In this example, the entry point is `MyProject.MyHttpFunction`.

###  Ruby 
    
    
    require "functions_framework"
    
    # Register an HTTP function with the Functions Framework
    FunctionsFramework.http "my_http_function" do |request|
      # Your code here
    
      # Return an HTTP response
      "OK"
    end
    

In Ruby, you register an HTTP handler function with the [Functions Framework for Ruby](https://googlecloudplatform.github.io/functions-framework-ruby). Your HTTP handler function must accept a [Rack request](https://rubydoc.info/gems/rack/Rack/Request) object as an argument and return [a value that can be used as an HTTP response](https://googlecloudplatform.github.io/functions-framework-ruby/v1.1.0/file.writing-functions.html#response-types).

The [function entry point](https://docs.cloud.google.com/functions/1stgendocs/writing#entry-point) is the name with which the handler is registered with the Functions Framework. In this example, the entry point is `my_http_function`.

###  PHP 
    
    
    <?php
    
    use Google\CloudFunctions\FunctionsFramework;
    use Psr\Http\Message\ServerRequestInterface;
    
    // Register an HTTP function with the Functions Framework
    FunctionsFramework::http('myHttpFunction', 'myHttpHandler');
    
    // Define your HTTP handler
    function myHttpHandler(ServerRequestInterface $request): string
    {
        // Your code here
    
        // Return an HTTP response
        return 'OK';
    }
    

In PHP, you register an HTTP handler function with the [Functions Framework for PHP](https://github.com/GoogleCloudPlatform/functions-framework-php). Your HTTP handler function must accept an argument that implements the PSR-7 [`ServerRequestInterface`](https://www.php-fig.org/psr/psr-7/#321-psrhttpmessageserverrequestinterface) interface, and must return an HTTP response as either a string or an object that implements the PSR-7 [`ResponseInterface`](https://www.php-fig.org/psr/psr-7/#33-psrhttpmessageresponseinterface) interface.

The [function entry point](https://docs.cloud.google.com/functions/1stgendocs/writing#entry-point) is the name with which the handler is registered with the Functions Framework. In this example, the entry point is `myHttpFunction`.

## HTTP requests and responses

HTTP functions accept the HTTP request methods listed on the page [HTTP triggers](https://docs.cloud.google.com/functions/1stgendocs/calling/http). Your HTTP handler can inspect the request method and perform different actions based on the method.

Your function must send an HTTP response. If the function creates background tasks (such as with threads, futures, JavaScript `Promise` objects, callbacks, or system processes), you must terminate or otherwise resolve these tasks before sending an HTTP response. Any tasks not terminated before the HTTP response is sent might not be completed, and might cause undefined behavior.

See [HTTP triggers](https://docs.cloud.google.com/functions/1stgendocs/calling/http) for more information about HTTP functions and associated options.

## Handling CORS

[Cross-Origin Resource Sharing (CORS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) is a way to let applications running on one domain access resources from another domain. For example, you might need to let your domain make requests to the Cloud Run functions domain to access your function.

If CORS is not set up properly, you might see errors like the following:
    
    
    XMLHttpRequest cannot load https://YOUR_FUNCTION_URL.
    No 'Access-Control-Allow-Origin' header is present on the requested resource.
    Origin 'https://YOUR_DOMAIN' is therefore not allowed access.
    

To allow cross-origin requests to your function, set the [`Access-Control-Allow-Origin`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Origin) header as appropriate on your HTTP response. For [preflighted cross-origin requests](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS#preflighted_requests), you must respond to the preflight `OPTIONS` request with a `204` response code and additional headers.

###  Node.js 
    
    
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

###  Python 
    
    
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
    
    

###  Go 
    
    
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
    

###  Java 
    
    
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

###  C# 
    
    
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

###  Ruby 
    
    
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

###  PHP 
    
    
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

### CORS limitations

For preflighted cross-origin requests, preflight `OPTIONS` requests are sent without an `Authorization` header, so they will be rejected on all HTTP functions that require authentication. Because the preflight requests fail, the main requests will also fail. To work around this limitation, use one of the following options:

  * [Allow unauthenticated invocations](https://docs.cloud.google.com/functions/1stgendocs/securing/managing-access-iam#allowing_unauthenticated_http_function_invocation) of your function.
  * Host your web app and Cloud Run functions on the same domain to avoid CORS. You can do this by [integrating Firebase Hosting with Cloud Run functions](https://firebase.google.com/docs/hosting/functions).



## Next steps

  * Learn more about [HTTP triggers](https://docs.cloud.google.com/functions/1stgendocs/calling/http).
  * Learn how to [deploy a Cloud Run function](https://docs.cloud.google.com/functions/1stgendocs/deploy).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
