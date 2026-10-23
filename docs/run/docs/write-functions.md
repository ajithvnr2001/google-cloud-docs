---
url: https://docs.cloud.google.com/run/docs/write-functions/
title: Write Cloud Run functions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:58:19.157090+00:00
---

# Write Cloud Run functions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/write-functions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Write Cloud Run functions Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to write HTTP and event-driven Cloud Run functions with the Functions Framework.

## Functions Framework overview

When writing functions source code, you must use the [Functions Framework](https://github.com/GoogleCloudPlatform/functions-framework), an open source library for writing Cloud Run functions. With the Functions Framework, you can write lightweight functions that run in Cloud Run and in other environments, including your local development machine and Knative-based environments.

The Functions Framework lets you:

  * Invoke a Cloud Run function in response to a request.
  * Automatically unmarshal events conforming to the [CloudEvents](https://cloudevents.io/) specification, an industry-standard specification for describing event data in a common way.
  * Start a local development server for testing.



The Functions Framework provides an interface for building modular services. To use the Functions Framework in your source code, specify the following:

  * Function entry point
  * Signature type



### Function entry point

Your source code must define a function entry point, which is the code that runs when Cloud Run invokes your function. You specify this entry point when you deploy your function.

How you define the entry point depends on the language runtime you use. Some languages use a function as their entry point, while others use a class.

### Signature Type

When you write the source code of a function with the Functions Framework, you must specify one of the two signature types:

  * **HTTP functions**: Registers an HTTP handler function. Use an HTTP function when your function needs a URL endpoint and must respond to HTTP requests, such as for webhooks.
  * **Event-driven functions**, also known as _CloudEvents functions_ : Registers a CloudEvents handler function. Use an event-driven function when your function is triggered directly in response to events within your Google Cloud project, such as messages on a Pub/Sub topic or changes in a Cloud Storage bucket.



## Source directory structure

The Functions Framework is supported in a number of programming languages. The language runtime you choose and the type of function you want to write determines how to structure your code and implement your function.

For Cloud Run to locate your function definition, each language runtime has requirements for structuring your source code.

### Node.js

The basic directory structure for Node.js functions is as follows:
    
    
    .
    ├── index.js
    └── package.json
    

By default, Cloud Run attempts to load source code from a file named `index.js` at the root of your function directory. To specify a different main source file, use the `main` field in your `package.json` file.

Your `package.json` file must also include the [Functions Framework for Node.js](https://github.com/GoogleCloudPlatform/functions-framework-nodejs) as a dependency:
    
    
    {
      "main": "index.js",
      "dependencies": {
        "@google-cloud/functions-framework": "^3.0.0"
      },
      "type": "module"
    }
    

**Note:** You can add the Functions Framework dependency with [npm](https://www.npmjs.com/) by running `npm install @google-cloud/functions-framework`.

The code in your main file must define your function entry point and can import other code and Node.js modules. The main file can also define multiple function entry points that can be deployed separately.

See the [Node.js runtime overview](https://docs.cloud.google.com/run/docs/runtimes/nodejs) and the [Functions Framework for Node.js](https://github.com/GoogleCloudPlatform/functions-framework-nodejs) for more details.

### Python

The basic directory structure for Python functions is as follows:
    
    
    .
    ├── main.py
    └── requirements.txt
    

Cloud Run loads source code from a file named `main.py` at the root of your function directory. You must name your main file `main.py`.

Your `requirements.txt` file must include the [Functions Framework for Python](https://github.com/GoogleCloudPlatform/functions-framework-python) as a dependency:
    
    
    functions-framework==3.*
    

The code in your `main.py` file must define your function entry point and can import other code and external dependencies as normal. The `main.py` file can also define multiple function entry points that can be deployed separately.

See the [Python runtime overview](https://docs.cloud.google.com/run/docs/runtimes/python) and the [Functions Framework for Python](https://github.com/GoogleCloudPlatform/functions-framework-python) for more details.

### Go

The basic directory structure for Go functions is as follows:
    
    
    .
    ├── myfunction.go
    └── go.mod
    

Your function must be in a Go package at the root of your project. The package and its source files can have any name, except your function cannot be in `package main`. If you need a `main` package, for example for local testing, you can create one in a subdirectory:
    
    
    .
    ├── myfunction.go
    ├── go.mod
    └── cmd/
      └── main.go
    

Your `go.mod` file must include the [Functions Framework for Go](https://github.com/GoogleCloudPlatform/functions-framework-go) as a dependency:
    
    
    module example.com/my-module
    
    require (
      github.com/GoogleCloudPlatform/functions-framework-go v1.5.2
    )
    

**Note:** You can add the Functions Framework dependency by running `go get github.com/GoogleCloudPlatform/functions-framework-go`.

The code in your root package must define your function entry point and can import other code from subpackages and dependencies as normal. Your package can also define multiple function entry points that can be deployed separately.

**Note:** For an example of setting up a basic Cloud Run project in Go, see the [Functions Framework for Go Quickstart on GitHub](https://github.com/GoogleCloudPlatform/functions-framework-go#quickstart-hello-world-on-your-local-machine).

See the [Go runtime overview](https://docs.cloud.google.com/run/docs/runtimes/go) and the [Functions Framework for Go](https://github.com/GoogleCloudPlatform/functions-framework-go) for more details.

### Java

The basic directory structure for Java functions is as follows:
    
    
    .
    ├── pom.xml
    └── src/
      └── main/
          └── java/
              └── MyFunction.java
    

Your Java source files must be under the `src/main/java/` directory and can have any name. If your source files declare a package, add an extra directory under `src/main/java` with the name of the package:
    
    
    .
    ├── pom.xml
    └── src/
      └── main/
          └── java/
              └── mypackage/
                  └── MyFunction.java
    

We recommend putting associated tests under a `src/test/java/` subdirectory.

**Note:** If you're working with another JVM language (such as Groovy, Kotlin, or Scala), rename the `java` directories to language-appropriate names (such as `groovy`, `kotlin`, or `scala`).

Your `pom.xml` file must include the [Functions Framework for Java](https://github.com/GoogleCloudPlatform/functions-framework-java) as a dependency:
    
    
    ...
        <dependency>
          <groupId>com.google.cloud.functions</groupId>
          <artifactId>functions-framework-api</artifactId>
          <version>1.0.4</version>
        </dependency>
    ...
    

The code in your source files must define your function entry point and can import other code and external dependencies as normal. Your source files can also define multiple function entry points that can be deployed separately.

See the [Java runtime overview](https://docs.cloud.google.com/run/docs/runtimes/java) and the [Functions Framework for Java](https://github.com/GoogleCloudPlatform/functions-framework-java) for more details.

### .NET

The basic directory structure for .NET functions is as follows:
    
    
    .
    ├── MyFunction.cs
    └── MyProject.csproj
    

You can structure your projects as you would any other .NET source code. Your source files can have any name.

**Note:** The same pattern applies if you use F# or Visual Basic, but with appropriate file extensions (`.fs` and `.fsproj` for F#, `.vb` and `.vbproj` for Visual Basic).

Your project file must include the [Functions Framework for .NET](https://github.com/GoogleCloudPlatform/functions-framework-dotnet) as a dependency:
    
    
    ...
        <PackageReference Include="Google.Cloud.Functions.Hosting" Version="1.0.0" />
    ...
    

The code in your source files must define your function entry point and can import other code and external dependencies as normal. Your source files can also define multiple function entry points that can be deployed separately.

**Note:** For information about file structure in relation to functions that use multiple local .NET projects, see [Deploying a function with a local project dependency](https://github.com/GoogleCloudPlatform/functions-framework-dotnet/blob/main/docs/deployment.md#deploying-a-function-with-a-local-project-dependency).

See the [.NET runtime overview](https://docs.cloud.google.com/run/docs/runtimes/dotnet) and the [Functions Framework for .NET](https://github.com/GoogleCloudPlatform/functions-framework-dotnet) for more details.

### Ruby

The basic directory structure for Ruby functions is as follows:
    
    
    .
    ├── app.rb
    ├── Gemfile
    └── Gemfile.lock
    

Cloud Run loads source code from a file named `app.rb` at the root of your function directory. Your main file must be named `app.rb`.

Your `Gemfile` file must include the [Functions Framework for Ruby](https://github.com/GoogleCloudPlatform/functions-framework-ruby) as a dependency:
    
    
    source "https://rubygems.org"
    gem "functions_framework", "~> 1.0"
    

**Note:** You can add the Functions Framework dependency with [Bundler](https://bundler.io/) by running `bundle add functions_framework`.

The code in your `app.rb` file must define your function entry point and can import other code and external dependencies as normal. The `app.rb` file can also define multiple function entry points that can be deployed separately.

See the [Ruby runtime overview](https://docs.cloud.google.com/run/docs/runtimes/ruby) and the [Functions Framework for Ruby](https://github.com/GoogleCloudPlatform/functions-framework-ruby) for more details.

### PHP

The basic directory structure for PHP functions is as follows:
    
    
    .
    ├── index.php
    └── composer.json
    

Cloud Run loads source code from a file named `index.php` at the root of your function directory. You must name your main file `index.php`.

Your `composer.json` file must include the [Functions Framework for PHP](https://github.com/GoogleCloudPlatform/functions-framework-php) as a dependency:
    
    
    {
      "require": {
        "google/cloud-functions-framework": "^1.1"
      }
    }
    

**Note:** You can add the Functions Framework dependency with [Composer](https://getcomposer.org/) by running `composer require google/cloud-functions-framework`.

The code in your `index.php` file must define your function entry point and can import other code and external dependencies as normal. The `index.php` file can also define multiple function entry points that can be deployed separately.

See the [PHP runtime overview](https://docs.cloud.google.com/run/docs/runtimes/php) and the [Functions Framework for PHP](https://github.com/GoogleCloudPlatform/functions-framework-php) for more details.

If you group multiple functions into a single project, be aware that every function might end up sharing the same set of dependencies. However, some of the functions might not need all of the dependencies.

Where possible, we recommend splitting up large multi-function codebases and putting each function in its own top-level directory as shown in the preceding examples, with its own source and project configuration files. This approach minimizes the number of dependencies required for a particular function, which in turn reduces the amount of memory your function needs.

## Write HTTP functions

Write an HTTP function when you want to invoke a function through an HTTP(S) request. To allow for HTTP semantics, you use the Function Framework and specify the HTTP Function signature to accept HTTP-specific arguments.

The following example shows a basic HTTP function source file for each runtime. For a complete working example, see [Deploy a Cloud Run function using the Google Cloud CLI](https://docs.cloud.google.com/run/docs/quickstarts/functions/deploy-functions-gcloud). For For more information about where to locate your source code, see [Source directory structure](https://docs.cloud.google.com/run/docs/write-functions#directory_structure).

### Node.js

###  ES module 
    
    
    import { http } from '@google-cloud/functions-framework';
    // Register an HTTP function with the Functions Framework that executes
    // when you make an HTTP request to the deployed function's endpoint.
    http('helloGET', (req, res) => {
      res.send('Hello World!');
    });

Add the following dependencies in your `package.json` file:
    
    
    {
      "name": "nodejs-docs-samples-functions-hello-world-get",
      "version": "0.0.1",
      "private": true,
      "license": "Apache-2.0",
      "author": "Google Inc.",
      "repository": {
        "type": "git",
        "url": "https://github.com/GoogleCloudPlatform/nodejs-docs-samples.git"
      },
      "engines": {
        "node": ">=16.0.0"
      },
      "scripts": {
        "test": "c8 mocha -p -j 2 test/*.test.js --timeout=6000 --exit"
      },
      "dependencies": {
        "@google-cloud/functions-framework": "^3.1.0"
      },
      "devDependencies": {
        "c8": "^10.0.0",
        "gaxios": "^6.0.0",
        "mocha": "^10.0.0",
        "wait-port": "^1.0.4"
      }
    }

###  CommonJS module 
    
    
      const functions = require('@google-cloud/functions-framework');
    
      // Register an HTTP function with the Functions Framework
      functions.http('helloGET', (req, res) => {
        // Your code here
    
        // Send an HTTP response
        res.send('OK');
      });
    

Add the following dependencies in your `package.json` file:
    
    
      {
        "dependencies": {
          "@google-cloud/functions-framework": "^3.0.0"
        }
      }
    

In Node.js, you register an HTTP handler function with the [Functions Framework for Node.js](https://github.com/GoogleCloudPlatform/functions-framework-nodejs). Your HTTP handler function must be an [Express middleware function](https://expressjs.com/en/guide/writing-middleware.html) that accepts the [request](https://expressjs.com/en/4x/api.html#req) and [response](https://expressjs.com/en/4x/api.html#res) arguments and sends an HTTP response.

Cloud Run automatically parses the request body for you based on the request's `Content-Type` header using [`body-parser`](https://expressjs.com/en/resources/middleware/body-parser.html), so you can access the `req.body` and `req.rawBody` objects in your HTTP handler.

The [function entry point](https://docs.cloud.google.com/run/docs/write-functions#function_entry_point) is the name with which the handler is registered with the Functions Framework. In this example, the entry point is `helloGET`.

### Python
    
    
    import functions_framework
    
    # Register an HTTP function with the Functions Framework
    @functions_framework.http
    def my_http_function(request):
      # Your code here
    
      # Return an HTTP response
      return 'OK'
    

In Python, you register an HTTP handler function with the [Functions Framework for Python](https://github.com/GoogleCloudPlatform/functions-framework-python). Your HTTP handler function must accept a [Flask request](https://flask.palletsprojects.com/api/#flask.Request) object as an argument and return [a value that Flask can convert into an HTTP response object](https://flask.palletsprojects.com/en/2.3.x/quickstart/#about-responses).

The [function entry point](https://docs.cloud.google.com/run/docs/write-functions#function_entry_point) is the name with which the handler is registered with the Functions Framework. In this example, the entry point is `my_http_function`.

### Go
    
    
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

The [function entry point](https://docs.cloud.google.com/run/docs/write-functions#function_entry_point) is the name with which the handler is registered with the Functions Framework. In this example, the entry point is `MyHTTPFunction`.

Your HTTP handler function must implement the standard [`http.HandlerFunc`](https://pkg.go.dev/net/http#HandlerFunc) interface. It accepts an [http.ResponseWriter](https://pkg.go.dev/net/http#ResponseWriter) interface that your function uses to create a reply to the request, and a pointer to an [http.Request](https://pkg.go.dev/net/http#Request) struct containing the details of the inbound HTTP request.

### Java
    
    
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

The [function entry point](https://docs.cloud.google.com/run/docs/write-functions#function_entry_point) is the fully-qualified name of the HTTP handler class, including the package name. In this example, the entry point is `myhttpfunction.MyHttpFunction`.

Your `service` method receives an [`HttpRequest`](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpRequest) object describing the inbound HTTP request, and an [`HttpResponse`](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpResponse) object that your function populates with a response message.

### .NET
    
    
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

The [function entry point](https://docs.cloud.google.com/run/docs/write-functions#function_entry_point) is the fully-qualified name of the HTTP handler class, including the namespace. In this example, the entry point is `MyProject.MyHttpFunction`.

### Ruby
    
    
    require "functions_framework"
    
    # Register an HTTP function with the Functions Framework
    FunctionsFramework.http "my_http_function" do |request|
      # Your code here
    
      # Return an HTTP response
      "OK"
    end
    

In Ruby, you register an HTTP handler function with the [Functions Framework for Ruby](https://googlecloudplatform.github.io/functions-framework-ruby). Your HTTP handler function must accept a [Rack request](https://rubydoc.info/gems/rack/Rack/Request) object as an argument and return [a value that can be used as an HTTP response](https://googlecloudplatform.github.io/functions-framework-ruby/v1.1.0/file.writing-functions.html#response-types).

The [function entry point](https://docs.cloud.google.com/run/docs/write-functions#function_entry_point) is the name with which the handler is registered with the Functions Framework. In this example, the entry point is `my_http_function`.

### PHP
    
    
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

The [function entry point](https://docs.cloud.google.com/run/docs/write-functions#function_entry_point) is the name with which the handler is registered with the Functions Framework. In this example, the entry point is `myHttpFunction`.

### HTTP request and responses

When you register an HTTP handler function with the Functions Framework, your HTTP handler can inspect the request method and perform different actions based on the method.

When you configure an event provider to send HTTP requests to your Cloud Run function, your function sends an HTTP response. If the function creates background tasks (such as with threads, futures, JavaScript Promise objects, callbacks, or system processes), you must terminate or otherwise resolve these tasks before sending an HTTP response. Any tasks not terminated before the HTTP response is sent might not be completed, and might cause undefined behavior.

### Handle CORS

[Cross-Origin Resource Sharing (CORS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) is a way to let applications running on one domain access resources from another domain. For example, you might need to let your domain make requests to the Cloud Run functions domain to access your function.

To allow cross-origin requests to your function, set the [`Access-Control-Allow-Origin`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Origin) header as appropriate on your HTTP response. For [preflighted cross-origin requests](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS#preflighted_requests), you must respond to the preflight `OPTIONS` request with a `204` response code and additional headers.

### Node.js
    
    
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

### Python
    
    
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
    
    

### Go
    
    
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

### .NET
    
    
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

### Ruby
    
    
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

### PHP
    
    
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
    

If CORS is not set up properly, you might see errors like the following:
    
    
    XMLHttpRequest cannot load https://YOUR_FUNCTION_URL.
    No 'Access-Control-Allow-Origin' header is present on the requested resource.
    Origin 'https://YOUR_DOMAIN' is therefore not allowed access.
    

#### CORS limitations

For preflighted cross-origin requests, preflight OPTIONS requests are sent without an Authorization header, so they will be rejected on all HTTP functions that require authentication. Because the preflight requests fail, the main requests will also fail. To work around this limitation, use one of the following options:

  * [Allow public access](https://docs.cloud.google.com/run/docs/authenticating/public) of your function.
  * [Configure Identity-Aware Proxy](https://docs.cloud.google.com/run/docs/securing/identity-aware-proxy-cloud-run) for your function, which provides the Authorization header for preflight OPTIONS requests sent to Cloud Run functions.
  * Host your web app and Cloud Run on the same domain to avoid CORS. You can do this by [integrating Firebase Hosting with Cloud Run functions](https://firebase.google.com/docs/hosting/functions).



## Write event-driven functions

Write an event-driven function when you want a function to be triggered directly in response to events within your Google Cloud project, such as messages on a Pub/Sub topic or changes in a Cloud Storage bucket.

Event-driven functions are based on [CloudEvents](https://cloudevents.io/), an industry-standard specification for describing event data in a common way. You can learn more about the CloudEvents specification at the [CloudEvents GitHub repository](https://github.com/cloudevents/spec). The CloudEvents project also provides a set of [CloudEvents SDKs](https://github.com/cloudevents/spec#sdks) to help work with CloudEvents objects in your code.

The following example shows an event-driven function source file for each runtime. See [Source directory structure](https://docs.cloud.google.com/run/docs/write-functions#directory_structure) for information about where to locate your source code.

### Node.js

###  ES module 
    
    
      import { cloudEvent } from "@google-cloud/functions-framework";
      cloudEvent('myCloudEventFunction', cloudEvent => {
        // Your code here
        // Access the CloudEvent data payload using cloudEvent.data
      });
    

Add the following dependencies, including `"type": "module"` in your `package.json` file:
    
    
      {
        "dependencies": {
          "@google-cloud/functions-framework": "^3.0.0"
        },
        "type": "module"
      }
    

###  CommonJS module 
    
    
    const functions = require('@google-cloud/functions-framework');
    
    // Register a CloudEvent function with the Functions Framework
    functions.cloudEvent('myCloudEventFunction', cloudEvent => {
      // Your code here
      // Access the CloudEvent data payload using cloudEvent.data
    });
    

Add the following dependencies in your `package.json` file:
    
    
      {
        "dependencies": {
          "@google-cloud/functions-framework": "^3.0.0"
        }
      }
    

In Node.js, you register a CloudEvent handler function with the [Functions Framework for Node.js](https://github.com/GoogleCloudPlatform/functions-framework-nodejs). Your handler function must accept a [`CloudEvent`](https://cloudevents.github.io/sdk-javascript/classes/CloudEvent.html) object as an argument.

The function entry point is the name with which the handler is registered with the Functions Framework. In this example, the entry point is `myCloudEventFunction`.

### Python
    
    
    import functions_framework
    
    # Register a CloudEvent function with the Functions Framework
    @functions_framework.cloud_event
    def my_cloudevent_function(cloud_event):
      # Your code here
      # Access the CloudEvent data payload via cloud_event.data
    

In Python, you register a CloudEvent handler function with the [Functions Framework for Python](https://github.com/GoogleCloudPlatform/functions-framework-python). Your handler function must accept a [`CloudEvent`](https://github.com/cloudevents/sdk-python/blob/master/cloudevents/http/event.py) object as an argument.

The function entry point is the name of the handler function registered with the Functions Framework. In this example, the entry point is `my_cloudevent_function`.

### Go
    
    
    package mycloudeventfunction
    
    import (
        "context"
    
        "github.com/GoogleCloudPlatform/functions-framework-go/functions"
        "github.com/cloudevents/sdk-go/v2/event"
    )
    
    func init() {
        // Register a CloudEvent function with the Functions Framework
        functions.CloudEvent("MyCloudEventFunction", myCloudEventFunction)
    }
    
    // Function myCloudEventFunction accepts and handles a CloudEvent object
    func myCloudEventFunction(ctx context.Context, e event.Event) error {
        // Your code here
        // Access the CloudEvent data payload using e.Data() or e.DataAs(...)
    
        // Returning an error causes its message to be logged.
        // Example:
        err := myInternalFunction() // may return an error
        if err != nil {
            // Append error message to log
            return err
        }
    
        // Return nil if no error occurred
        return nil
    }
    

In Go, you register a CloudEvent handler function with the [Functions Framework for Go](https://github.com/GoogleCloudPlatform/functions-framework-go). Your handler function must accept a CloudEvents [`event.Event`](https://pkg.go.dev/github.com/cloudevents/sdk-go/v2@v2.9.0/event#Event) object as an argument.

The function entry point is the name with which the handler is registered with the Functions Framework. In this example, the entry point is `MyCloudEventFunction`.

### Java
    
    
    package mycloudeventfunction;
    
    import com.google.cloud.functions.CloudEventsFunction;
    import io.cloudevents.CloudEvent;
    
    // Define a class that implements the CloudEventsFunction interface
    public class MyCloudEventFunction implements CloudEventsFunction {
      // Implement the accept() method to handle CloudEvents
      @Override
      public void accept(CloudEvent event) {
        // Your code here
        // Access the CloudEvent data payload using event.getData()
        // To get the data payload as a JSON string, use:
        // new String(event.getData().toBytes())
      }
    }
    

In Java, you use the [Functions Framework Java API](https://javadoc.io/doc/com.google.cloud.functions/functions-framework-api/) to implement a CloudEvent handler class with the [`CloudEventsFunction`](https://javadoc.io/doc/com.google.cloud.functions/functions-framework-api/latest/com/google/cloud/functions/CloudEventsFunction.html) interface. The `accept()` method must accept a [`CloudEvent`](https://www.javadoc.io/doc/io.cloudevents/cloudevents-api/latest/io/cloudevents/CloudEvent.html) object as an argument and perform any processing on the event.

The function entry point is the fully-qualified name of the CloudEvent handler class, including the package name. In this example, the entry point is `mycloudeventfunction.MyCloudEventFunction`.

### .NET
    
    
    using CloudNative.CloudEvents;
    using Google.Cloud.Functions.Framework;
    using System.Threading;
    using System.Threading.Tasks;
    
    namespace MyProject
    {
      // Define a class that implements the ICloudEventFunction<T> interface
      public class MyCloudEventFunction : ICloudEventFunction<CloudEventDataType>
      {
          // Implement the HandleAsync() method to handle CloudEvents
          public Task HandleAsync(CloudEvent cloudEvent, CloudEventDataType data, CancellationToken cancellationToken)
          {
              // Your code here
              // The data argument represents the CloudEvent data payload
    
              // Signal function completion
              return Task.CompletedTask;
          }
      }
    }

In .NET runtimes, you use the [Functions Framework for .NET](https://github.com/GoogleCloudPlatform/functions-framework-dotnet) to implement a CloudEvent handler class with the [`ICloudEventFunction<T>`](https://github.com/GoogleCloudPlatform/functions-framework-dotnet/blob/main/src/Google.Cloud.Functions.Framework/ICloudEventFunction.cs) interface. The `HandleAsync()` method accepts a [`CloudEvent`](https://github.com/cloudevents/sdk-csharp/blob/main/src/CloudNative.CloudEvents/CloudEvent.cs) object and the associated CloudEvent data payload as arguments.

The type of the CloudEvent data payload argument, shown in the example code as `CloudEventDataType`, must correspond to the type of event the function handles. The [Google CloudEvents .NET library](https://github.com/googleapis/google-cloudevents-dotnet) provides data types for the various events supported by Google.

The function entry point is the fully-qualified name of the CloudEvent handler class, including the namespace. In this example, the entry point is `MyProject.MyCloudEventFunction`.

### Ruby
    
    
    require "functions_framework"
    
    # Register a CloudEvent function with the Functions Framework
    FunctionsFramework.cloud_event "my_cloudevent_function" do |cloud_event|
      # Your code here
      # Access the CloudEvent data payload via cloud_event.data
    end
    

In Ruby, you register a CloudEvent handler function with the [Functions Framework for Ruby](https://googlecloudplatform.github.io/functions-framework-ruby). Your handler function must accept a CloudEvents [`Event`](https://github.com/cloudevents/sdk-ruby/blob/main/lib/cloud_events/event/v1.rb) object as an argument.

The function entry point is the name with which the handler is registered with the Functions Framework. In this example, the entry point is `my_cloudevent_function`.

### PHP
    
    
    <?php
    
    use CloudEvents\V1\CloudEventInterface;
    use Google\CloudFunctions\FunctionsFramework;
    
    // Register a CloudEvent function with the Functions Framework
    FunctionsFramework::cloudEvent('myCloudEventFunction', 'myCloudEventHandler');
    
    // Define your CloudEvent handler
    function myCloudEventHandler(CloudEventInterface $event): void
    {
        // Your code here
        // Access the CloudEvent data payload using $event->getData()
    }
    

In PHP, you register a CloudEvent handler function with the [Functions Framework for PHP](https://github.com/GoogleCloudPlatform/functions-framework-php). Your handler function must accept an argument that conforms to the [`CloudEventInterface`](https://github.com/cloudevents/sdk-php/blob/master/src/V1/CloudEventInterface.php) interface.

The [function entry point](https://docs.cloud.google.com/run/docs/write-functions#function_entry_point) is the name with which the handler is registered with the Functions Framework. In this example, the entry point is `myCloudEventFunction`.

For event-driven functions, event data is passed to your function in the [CloudEvents format](https://docs.cloud.google.com/eventarc/docs/cloudevents), with a CloudEvent data payload corresponding to the event type that triggers your function. See [Function triggers](https://docs.cloud.google.com/run/docs/function-triggers) for information about supported triggers, event types, and associated event data formats.

The [Google Events](https://github.com/googleapis/google-cloudevents) repository contains resources for working with CloudEvents issued by Google.

### Function termination

Cloud Run considers event-driven function execution complete when the function returns. If the function creates background tasks (such as with threads, futures, JavaScript Promise objects, callbacks, or system processes), you must terminate or otherwise resolve these tasks before returning from your function. Any tasks not terminated before the function returns might not be completed, and might cause undefined behavior.

### Automatic retries

Event-driven functions can be configured to automatically retry failed invocations. See [Retrying event-driven functions](https://docs.cloud.google.com/eventarc/docs/retry-events) for more information.

## What's next

  * [Function triggers](https://docs.cloud.google.com/run/docs/function-triggers)
  * [Deploy a Cloud Run function](https://docs.cloud.google.com/run/docs/deploy-functions)
  * Learn about the [Functions Framework Contract](https://github.com/GoogleCloudPlatform/functions-framework)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
