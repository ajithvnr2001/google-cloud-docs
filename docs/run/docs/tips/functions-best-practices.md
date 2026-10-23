---
url: https://docs.cloud.google.com/run/docs/tips/functions-best-practices/
title: Functions best practices \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:51:08.055501+00:00
---

# Functions best practices  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/tips/functions-best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Functions best practices Stay organized with collections  Save and categorize content based on your preferences. 

This document describes best practices for designing, implementing, testing, and deploying Cloud Run functions.

**Note:** Several of the recommendations in this document center around what is known as a _cold start_. Functions are stateless, and the execution environment is often initialized from scratch, which is called a cold start. Cold starts can take significant amounts of time to complete. It is best practice to avoid unnecessary cold starts, and to streamline the cold start process to whatever extent possible (for example, by avoiding unnecessary dependencies).

## Correctness

This section describes general best practices for designing and implementing Cloud Run functions.

### Write idempotent functions

Your functions should produce the same result even if they are called multiple times. This lets you retry an invocation if the previous invocation fails part way through your code. For more information, see [retrying event-driven functions](https://docs.cloud.google.com/run/docs/tips/function-retries). 

### Ensure HTTP functions send an HTTP response

If your function is [HTTP-triggered](https://docs.cloud.google.com/run/docs/write-http-functions), remember to send an HTTP response, as shown below. Failing to do so can result in your function executing until timeout. If this occurs, you will be charged for the entire timeout time. [Timeouts may also cause unpredictable behavior](https://docs.cloud.google.com/run/docs/configuring/request-timeout) or cold starts on subsequent invocations, resulting in unpredictable behavior or additional latency.

###  Node.js 
    
    
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
    ** const name =**
        (req.query && req.query.name) || (req.body && req.body.name) || 'World';
    
      res.send(`Hello ${escapeHtml(name)}!`);
    });

###  Python 
    
    
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
    ** name = request_json["name"]**
        elif request_args and "name" in request_args:
            name = request_args["name"]
        else:
            name = "World"
        return f"Hello {escape(name)}!"
    

###  Go 
    
    
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
    
    **// HelloHTTP is an HTTP Cloud Function with a request parameter.**
    func HelloHTTP(w http.ResponseWriter, r *http.Request) {
    	var d struct {
    		Name string `json:"name"`
    **}**
    	if err := json.NewDecoder(r.Body).Decode(&d); err != nil {
    		fmt.Fprint(w, "Hello, World!")
    ** return**
    	}
    	if d.Name == "" {
    		fmt.Fprint(w, "Hello, World!")
    		return
    	}
    	fmt.Fprintf(w, "Hello, %s!", html.EscapeString(d.Name))
    }

###  Java 
    
    
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
    ** writer.printf("Hello %s!", name);**
      }
    }

###  C# 
    
    
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
    
    ** await context.Response.WriteAsync($"Hello {name}!", context.RequestAborted);**
        }
    }

###  Ruby 
    
    
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
    ** end ||**
             "World"
      # Return the response body as a string.
      # You can also return a Rack::Response object, a Rack response array, or
      # a hash which will be JSON-encoded into a response.
      "Hello #{CGI.escape_html name}!"
    end

###  PHP 
    
    
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
    **json_last_error_msg()**
                ));
            }
            $name = $json['name'] ?? $name;
        }
        $queryString = $request->getQueryParams();
        $name = $queryString['name'] ?? $name;
    
        return sprintf('Hello, %s!', htmlspecialchars($name));
    }

### Do not start background activities

Background activity is anything that happens after your function has terminated. A function invocation finishes once the function returns or otherwise signals completion, such as by calling the `callback` argument in Node.js event-driven functions. Any code run after graceful termination cannot access the CPU and will not make any progress.

**Note:** If a Node.js event-driven function returns a Promise, Cloud Run functions ensures that the Promise is settled before terminating.

In addition, when a subsequent invocation is executed in the same environment, your background activity resumes, interfering with the new invocation. This may lead to unexpected behavior and errors that are hard to diagnose. Accessing the network after a function terminates usually leads to connections being reset (`ECONNRESET` error code).

Background activity can often be detected in logs from individual invocations, by finding anything that is logged after the line saying that the invocation finished. Background activity can sometimes be buried deeper in the code, especially when asynchronous operations such as callbacks or timers are present. Review your code to make sure all asynchronous operations finish before you terminate the function.

### Always delete temporary files

Local disk storage in the temporary directory is an in-memory filesystem. Files that you write consume memory available to your function, and sometimes persist between invocations. Failing to explicitly delete these files may eventually lead to an out-of-memory error and a subsequent cold start.

You can see the memory used by an individual function by selecting it in the [list of functions](https://console.cloud.google.com/functions/list) in the Google Cloud console and choosing the _Memory usage_ plot.

If you need access to long term storage, consider using Cloud Run volume mounts with [Cloud Storage](https://docs.cloud.google.com/run/docs/configuring/services/cloud-storage-volume-mounts) or [NFS volumes](https://docs.cloud.google.com/run/docs/configuring/services/nfs-volume-mounts).

You can reduce memory requirements when processing larger files using pipelining. For example, you can process a file on Cloud Storage by creating a read stream, passing it through a stream-based process, and writing the output stream directly to Cloud Storage.

### Functions Framework

To ensure that the same dependencies are installed consistently across environments, we recommend that you include the Functions Framework library in your package manager and pin the dependency to a specific version of Functions Framework.

To do this, include your preferred version in the relevant lock file (for example, `package-lock.json` for Node.js, or `requirements.txt` for Python).

If Functions Framework is not explicitly listed as a dependency, it will automatically be added during the build process using the latest available version.

## Tools

This section provides guidelines on how to use tools to implement, test, and interact with Cloud Run functions.

### Local development

Function deployment takes a bit of time, so it is often faster to test the code of your function locally.

Developers can use the [Functions Framework](https://docs.cloud.google.com/run/docs/write-functions) for local testing. 

### Error reporting

In languages that use exception handling, do not throw uncaught exceptions, because they force cold starts in future invocations.

### Do not manually exit

Manually exiting can cause unexpected behavior. Please use the following language-specific idioms instead:

###  Node.js 

Do not use `process.exit()`. HTTP functions should send a response with `res.status(200).send(message)`, and event-driven functions will exit once they return (either implicitly or explicitly). 

###  Python 

Do not use `sys.exit()`. HTTP functions should explicitly return a response as a string, and event-driven functions will exit once they return a value (either implicitly or explicitly). 

###  Go 

Do not use `os.Exit()`. HTTP functions should explicitly return a response as a string, and event-driven functions will exit once they return a value (either implicitly or explicitly). 

###  Java 

Do not use `System.exit()`. HTTP functions should send a response with `response.getWriter().write(message)`, and event-driven functions will exit once they return (either implicitly or explicitly). 

###  C# 

Do not use `System.Environment.Exit()`. HTTP functions should send a response with `context.Response.WriteAsync(message)`, and event-driven functions will exit once they return (either implicitly or explicitly). 

###  Ruby 

Do not use `exit()` or `abort()`. HTTP functions should explicitly return a response as a string, and event-driven functions will exit once they return a value (either implicitly or explicitly). 

###  PHP 

Do not use `exit()` or `die()`. HTTP functions should explicitly return a response as a string, and event-driven functions will exit once they return a value (either implicitly or explicitly). 

### Use Sendgrid to send emails

Cloud Run functions does not allow outbound connections on port 25, so you cannot make non-secure connections to an SMTP server. The recommended way to send emails is to use a third party service such as [SendGrid](https://sendgrid.com/). You can find other options for sending email in the [Sending Email from an Instance](https://cloud.google.com/compute/docs/tutorials/sending-mail) tutorial for Google Compute Engine.

## Performance

This section describes best practices for optimizing performance.

### Avoid low concurrency

Because cold starts are expensive, being able to reuse recently started instances during a spike is a great optimization to handle load. Limiting concurrency limits how existing instances can be leveraged, therefore incurring more cold starts.

[Increasing concurrency](https://cloud.google.com/run/docs/about-concurrency) helps defer multiple requests per instance, making spikes of load easier to handle. **Note:** As efficiency increases and their required number is reduced, individual function instances may use more memory to hold requests and require more CPU to process them.

### Use dependencies wisely

Because functions are stateless, the execution environment is often initialized from scratch (during what is known as a _cold start_). When a cold start occurs, the global context of the function is evaluated.

If your functions import modules, the load time for those modules can add to the invocation latency during a cold start. You can reduce this latency, as well as the time needed to deploy your function, by loading dependencies correctly and not loading dependencies your function doesn't use.

### Use global variables to reuse objects in future invocations

There is no guarantee that the state of a Cloud Run function will be preserved for future invocations. However, Cloud Run functions often recycles the execution environment of a previous invocation. If you declare a variable in global scope, its value can be reused in subsequent invocations without having to be recomputed.

This way you can cache objects that may be expensive to recreate on each function invocation. Moving such objects from the function body to global scope may result in significant performance improvements. The following example creates a heavy object only once per function instance, and shares it across all function invocations reaching the given instance:

###  Node.js 
    
    
    const functions = require('@google-cloud/functions-framework');
    
    // TODO(developer): Define your own computations
    const {lightComputation, heavyComputation} = require('./computations');
    
    // Global (instance-wide) scope
    // This computation runs once (at instance cold-start)
    const instanceVar = heavyComputation();
    
    /**
     * HTTP function that declares a variable.
     *
     * @param {Object} req request context.
     * @param {Object} res response context.
     */
    functions.http('scopeDemo', (req, res) => {
      // Per-function scope
      // This computation runs every time this function is called
      const functionVar = lightComputation();
    
      res.send(`Per instance: ${instanceVar}, per function: ${functionVar}`);
    });

###  Python 
    
    
    import time
    
    import functions_framework
    
    
    # Placeholder
    def heavy_computation():
        return time.time()
    
    
    # Placeholder
    def light_computation():
        return time.time()
    
    
    # Global (instance-wide) scope
    # This computation runs at instance cold-start
    instance_var = heavy_computation()
    
    
    @functions_framework.http
    def scope_demo(request):
        """
        HTTP Cloud Function that declares a variable.
        Args:
            request (flask.Request): The request object.
            <http://flask.pocoo.org/docs/1.0/api/#flask.Request>
        Returns:
            The response text, or any set of values that can be turned into a
            Response object using `make_response`
            <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>.
        """
    
        # Per-function scope
        # This computation runs every time this function is called
        function_var = light_computation()
        return f"Instance: {instance_var}; function: {function_var}"
    
    

###  Go 
    
    
    // h is in the global (instance-wide) scope.
    var h string
    
    // init runs during package initialization. So, this will only run during an
    // an instance's cold start.
    func init() {
    	h = heavyComputation()
    	functions.HTTP("ScopeDemo", ScopeDemo)
    }
    
    // ScopeDemo is an example of using globally and locally
    // scoped variables in a function.
    func ScopeDemo(w http.ResponseWriter, r *http.Request) {
    	l := lightComputation()
    	fmt.Fprintf(w, "Global: %q, Local: %q", h, l)
    }
    

###  Java 
    
    
    import com.google.cloud.functions.HttpFunction;
    import com.google.cloud.functions.HttpRequest;
    import com.google.cloud.functions.HttpResponse;
    import java.io.IOException;
    import java.io.PrintWriter;
    import java.util.Arrays;
    
    public class Scopes implements HttpFunction {
      // Global (instance-wide) scope
      // This computation runs at instance cold-start.
      // Warning: Class variables used in functions code must be thread-safe.
      private static final int INSTANCE_VAR = heavyComputation();
    
      @Override
      public void service(HttpRequest request, HttpResponse response)
          throws IOException {
        // Per-function scope
        // This computation runs every time this function is called
        int functionVar = lightComputation();
    
        var writer = new PrintWriter(response.getWriter());
        writer.printf("Instance: %s; function: %s", INSTANCE_VAR, functionVar);
      }
    
      private static int lightComputation() {
        int[] numbers = new int[] { 1, 2, 3, 4, 5, 6, 7, 8, 9 };
        return Arrays.stream(numbers).sum();
      }
    
      private static int heavyComputation() {
        int[] numbers = new int[] { 1, 2, 3, 4, 5, 6, 7, 8, 9 };
        return Arrays.stream(numbers).reduce((t, x) -> t * x).getAsInt();
      }
    }

###  C# 
    
    
    using Google.Cloud.Functions.Framework;
    using Microsoft.AspNetCore.Http;
    using System.Linq;
    using System.Threading.Tasks;
    
    namespace Scopes;
    
    public class Function : IHttpFunction
    {
        // Global (server-wide) scope.
        // This computation runs at server cold-start.
        // Warning: Class variables used in functions code must be thread-safe.
        private static readonly int GlobalVariable = HeavyComputation();
    
        // Note that one instance of this class (Function) is created per invocation,
        // so calling HeavyComputation in the constructor would not have the same
        // benefit.
    
        public async Task HandleAsync(HttpContext context)
        {
            // Per-function-invocation scope.
            // This computation runs every time this function is called.
            int functionVariable = LightComputation();
    
            await context.Response.WriteAsync(
                $"Global: {GlobalVariable}; function: {functionVariable}",
                context.RequestAborted);
        }
    
        private static int LightComputation()
        {
            int[] numbers = { 1, 2, 3, 4, 5, 6, 7, 8, 9 };
            return numbers.Sum();
        }
    
        private static int HeavyComputation()
        {
            int[] numbers = { 1, 2, 3, 4, 5, 6, 7, 8, 9 };
            return numbers.Aggregate((current, next) => current * next);
        }
    }

###  Ruby 
    
    
    # Global (instance-wide) scope.
    # This block runs on cold start, before any function is invoked.
    #
    # Note: It is usually best to run global initialization in an on_startup block
    # instead at the top level of the Ruby file. This is because top-level code
    # could be executed to verify the function during deployment, whereas an
    # on_startup block is run only when an actual function instance is starting up.
    FunctionsFramework.on_startup do
      instance_data = perform_heavy_computation
    
      # To pass data into function invocations, the best practice is to set a
      # key-value pair using the Ruby Function Framework's built-in "set_global"
      # method. Functions can call the "global" method to retrieve the data by key.
      # (You can also use Ruby global variables or "toplevel" local variables, but
      # they can make it difficult to isolate global data for testing.)
      set_global :my_instance_data, instance_data
    end
    
    FunctionsFramework.http "tips_scopes" do |_request|
      # Per-function scope.
      # This method is called every time this function is called.
      invocation_data = perform_light_computation
    
      # Retrieve the data computed by the on_startup block.
      instance_data = global :my_instance_data
    
      "instance: #{instance_data}; function: #{invocation_data}"
    end

###  PHP 
    
    
    use Psr\Http\Message\ServerRequestInterface;
    
    function scopeDemo(ServerRequestInterface $request): string
    {
        // Heavy computations should be cached between invocations.
        // The PHP runtime does NOT preserve variables between invocations, so we
        // must write their values to a file or otherwise cache them.
        // (All writable directories in Cloud Functions are in-memory, so
        // file-based caching operations are typically fast.)
        // You can also use PSR-6 caching libraries for this task:
        // https://packagist.org/providers/psr/cache-implementation
        $cachePath = sys_get_temp_dir() . '/cached_value.txt';
    
        $response = '';
        if (file_exists($cachePath)) {
            // Read cached value from file, using file locking to prevent race
            // conditions between function executions.
            $response .= 'Reading cached value.' . PHP_EOL;
            $fh = fopen($cachePath, 'r');
            flock($fh, LOCK_EX);
            $instanceVar = stream_get_contents($fh);
            flock($fh, LOCK_UN);
        } else {
            // Compute cached value + write to file, using file locking to prevent
            // race conditions between function executions.
            $response .= 'Cache empty, computing value.' . PHP_EOL;
            $instanceVar = _heavyComputation();
            file_put_contents($cachePath, $instanceVar, LOCK_EX);
        }
    
        // Lighter computations can re-run on each function invocation.
        $functionVar = _lightComputation();
    
        $response .= 'Per instance: ' . $instanceVar . PHP_EOL;
        $response .= 'Per function: ' . $functionVar . PHP_EOL;
    
        return $response;
    }
    

It is particularly important to cache network connections, library references, and API client objects in global scope. See [Networking best practices](https://docs.cloud.google.com/run/docs/configuring/networking-best-practices) for examples. **Note:** Background tasks should not be performed outside of the duration of a request. If you need to initialize a global variable with the result from an expensive background task, perform the task during your function's execution and store its result before sending a response.

### Reduce cold starts by setting a minimum number of instances

By default, Cloud Run functions scales the number of instances based on the number of incoming requests. You can change this default behavior by setting a minimum number of instances that Cloud Run functions must keep ready to serve requests. Setting a minimum number of instances reduces cold starts of your application. We recommend setting a minimum number of instances, and completing initialization at load time, if your application is latency-sensitive.

To learn how to set a minimum number of instances, see [Using minimum instances](https://docs.cloud.google.com/run/docs/configuring/min-instances).

### Notes about cold start and initialization

Global initialization happens at load time. Without it, the first request would need to complete initialization and load modules, thereby incurring higher latency.

However, global initialization also has an impact on cold starts. To minimize this impact, initialize only what is needed for the first request, to keep the first request's latency as low as possible.

This is especially important if you configured min instances as described above for a latency-sensitive function. In that scenario, completing initialization at load time and caching useful data ensures that the first request doesn't need to do it and is served with low latency.

If you initialize variables in global scope, depending on the language, long initialization times can result in two behaviors: \- for some combination of languages and async libraries, the function framework can run asynchronously and return immediately, causing code to continue running in the background, which could cause issues such as not being able to access the CPU. To avoid this, you should block on module initialization as described below. This also ensures that requests are not served until the initialization is complete. \- on the other hand, if the initialization is synchronous, the long initialization time will cause longer cold starts, which could be an issue especially with low concurrency functions during spikes of load.

**Note:** if you chose to use longer cold start times and min_instances, we also recommend that you use high concurrency in order to better support spikes of traffic.

#### Example of prewarming an async node.js library

Node.js with Firestore is an example of async node.js library. In order to take advantage of min_instances, the following code completes loading and initialization at load time, blocking on the module loading.

TLA is used, which means ES6 is required, using an `.mjs` extension for the node.js code or adding `type: module` to the package.json file.
    
    
    {
      "main": "main.js",
      "type": "module",
      "dependencies": {
        "@google-cloud/firestore": "^7.10.0",
        "@google-cloud/functions-framework": "^3.4.5"
      }
    }

### Node.js
    
    
    import Firestore from '@google-cloud/firestore';
    import * as functions from '@google-cloud/functions-framework';
    
    const firestore = new Firestore({preferRest: true});
    
    // Pre-warm firestore connection pool, and preload our global config
    // document in cache. In order to ensure no other request comes in,
    // block the module loading with a synchronous global request:
    const config = await firestore.collection('collection').doc('config').get();
    
    functions.http('fetch', (req, res) => {
    
    // Do something with config and firestore client, which are now preloaded
    // and will execute at lower latency.
    });

#### Examples of global initialization

###  Node.js 
    
    
    const functions = require('@google-cloud/functions-framework');
    
    // Always initialized (at cold-start)
    const nonLazyGlobal = fileWideComputation();
    
    // Declared at cold-start, but only initialized if/when the function executes
    let lazyGlobal;
    
    /**
     * HTTP function that uses lazy-initialized globals
     *
     * @param {Object} req request context.
     * @param {Object} res response context.
     */
    functions.http('lazyGlobals', (req, res) => {
      // This value is initialized only if (and when) the function is called
      lazyGlobal = lazyGlobal || functionSpecificComputation();
    
      res.send(`Lazy global: ${lazyGlobal}, non-lazy global: ${nonLazyGlobal}`);
    });

###  Python 
    
    
    import functions_framework
    
    # Always initialized (at cold-start)
    non_lazy_global = file_wide_computation()
    
    # Declared at cold-start, but only initialized if/when the function executes
    lazy_global = None
    
    
    @functions_framework.http
    def lazy_globals(request):
        """
        HTTP Cloud Function that uses lazily-initialized globals.
        Args:
            request (flask.Request): The request object.
            <http://flask.pocoo.org/docs/1.0/api/#flask.Request>
        Returns:
            The response text, or any set of values that can be turned into a
            Response object using `make_response`
            <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>.
        """
        global lazy_global, non_lazy_global  # noqa: F824
    
        # This value is initialized only if (and when) the function is called
        if not lazy_global:
            lazy_global = function_specific_computation()
    
        return f"Lazy: {lazy_global}, non-lazy: {non_lazy_global}."
    
    

###  Go 
    
    
    // Package tips contains tips for writing Cloud Functions in Go.
    package tips
    
    import (
    	"context"
    	"log"
    	"net/http"
    	"sync"
    
    	"cloud.google.com/go/storage"
    	"github.com/GoogleCloudPlatform/functions-framework-go/functions"
    )
    
    // client is lazily initialized by LazyGlobal.
    var client *storage.Client
    var clientOnce sync.Once
    
    func init() {
    	functions.HTTP("LazyGlobal", LazyGlobal)
    }
    
    // LazyGlobal is an example of lazily initializing a Google Cloud Storage client.
    func LazyGlobal(w http.ResponseWriter, r *http.Request) {
    	// You may wish to add different checks to see if the client is needed for
    	// this request.
    	clientOnce.Do(func() {
    		// Pre-declare an err variable to avoid shadowing client.
    		var err error
    		client, err = storage.NewClient(context.Background())
    		if err != nil {
    			http.[Error](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_MultiRangeDownloader_Error)(w, "Internal error", http.StatusInternalServerError)
    			log.Printf("storage.NewClient: %v", err)
    			return
    		}
    	})
    	// Use client.
    }
    

###  Java 
    
    
    import com.google.cloud.functions.HttpFunction;
    import com.google.cloud.functions.HttpRequest;
    import com.google.cloud.functions.HttpResponse;
    import java.io.IOException;
    import java.io.PrintWriter;
    import java.util.Arrays;
    
    public class LazyFields implements HttpFunction {
      // Always initialized (at cold-start)
      // Warning: Class variables used in Servlet classes must be thread-safe,
      // or else might introduce race conditions in your code.
      private static final int NON_LAZY_GLOBAL = fileWideComputation();
    
      // Declared at cold-start, but only initialized if/when the function executes
      // Uses the "initialization-on-demand holder" idiom
      // More information: https://en.wikipedia.org/wiki/Initialization-on-demand_holder_idiom
      private static class LazyGlobalHolder {
        // Making the default constructor private prohibits instantiation of this class
        private LazyGlobalHolder() {}
    
        // This value is initialized only if (and when) the getLazyGlobal() function below is called
        private static final Integer INSTANCE = functionSpecificComputation();
    
        private static Integer getInstance() {
          return LazyGlobalHolder.INSTANCE;
        }
      }
    
      @Override
      public void service(HttpRequest request, HttpResponse response)
          throws IOException {
        Integer lazyGlobal = LazyGlobalHolder.getInstance();
    
        var writer = new PrintWriter(response.getWriter());
        writer.printf("Lazy global: %s; non-lazy global: %s%n", lazyGlobal, NON_LAZY_GLOBAL);
      }
    
      private static int functionSpecificComputation() {
        int[] numbers = new int[] {1, 2, 3, 4, 5, 6, 7, 8, 9};
        return Arrays.stream(numbers).sum();
      }
    
      private static int fileWideComputation() {
        int[] numbers = new int[] {1, 2, 3, 4, 5, 6, 7, 8, 9};
        return Arrays.stream(numbers).reduce((t, x) -> t * x).getAsInt();
      }
    }

###  C# 
    
    
    using Google.Cloud.Functions.Framework;
    using Microsoft.AspNetCore.Http;
    using System;
    using System.Linq;
    using System.Threading;
    using System.Threading.Tasks;
    
    namespace LazyFields;
    
    public class Function : IHttpFunction
    {
        // This computation runs at server cold-start.
        // Warning: Class variables used in functions code must be thread-safe.
        private static readonly int NonLazyGlobal = FileWideComputation();
    
        // This variable is initialized at server cold-start, but the
        // computation is only performed when the function needs the result.
        private static readonly Lazy<int> LazyGlobal = new Lazy<int>(
            FunctionSpecificComputation,
            LazyThreadSafetyMode.ExecutionAndPublication);
    
        public async Task HandleAsync(HttpContext context)
        {
            // In a more complex function, there might be some paths that use LazyGlobal.Value,
            // and others that don't. The computation is only performed when necessary, and
            // only once per server.
            await context.Response.WriteAsync(
                $"Lazy global: {LazyGlobal.Value}; non-lazy global: {NonLazyGlobal}",
                context.RequestAborted);
        }
    
        private static int FunctionSpecificComputation()
        {
            int[] numbers = { 1, 2, 3, 4, 5, 6, 7, 8, 9 };
            return numbers.Sum();
        }
    
        private static int FileWideComputation()
        {
            int[] numbers = { 1, 2, 3, 4, 5, 6, 7, 8, 9 };
            return numbers.Aggregate((current, next) => current * next);
        }
    }

###  Ruby 
    
    
    FunctionsFramework.on_startup do
      # This method is called when the function is initialized, not on each
      # invocation.
    
      # Declare and set non_lazy_global
      set_global :non_lazy_global, file_wide_computation
    
      # Declare, but do not set, lazy_global
      set_global :lazy_global do
        function_specific_computation
      end
    end
    
    FunctionsFramework.http "tips_lazy" do |_request|
      # This method is called every time this function is called.
    
      "Lazy: #{global :lazy_global}; non_lazy: #{global :non_lazy_global}"
    end

###  PHP 

PHP functions cannot preserve variables between requests. The scopes sample above uses lazy loading to cache global variable values in a file. 

This is particularly important if you define several functions in a single file, and different functions use different variables. Unless you use lazy initialization, you may waste resources on variables that are initialized but never used.

**Note:** this technique can also be used when importing dependencies in Node.js and Python, albeit at the expense of code readability.

### Additional resources

Find out more about optimizing performance in the "Google Cloud Performance Atlas" video [Cloud Run functions Cold Boot Time](https://www.youtube.com/watch?v=IOXrwFqR6kY).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
