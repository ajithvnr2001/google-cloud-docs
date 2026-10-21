---
url: https://docs.cloud.google.com/functions/docs/samples/functions-tips-scopes/
title: Global versus function scope \u00a0|\u00a0 Cloud Run functions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:21:21.543405+00:00
---

# Global versus function scope  |  Cloud Run functions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/docs/samples/functions-tips-scopes/

If you are creating a new function, see the [Console Quickstart](https://docs.cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ Samples ](https://docs.cloud.google.com/functions/docs/samples)



#  Global versus function scope Stay organized with collections  Save and categorize content based on your preferences. 

Creates a heavy object only once per function instance, and shares it across all function invocations reaching the given instance.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Cloud Functions execution environment](https://docs.cloud.google.com/functions/1stgendocs/concepts/execution-environment)
  * [Functions best practices](https://docs.cloud.google.com/run/docs/tips/functions-best-practices)
  * [Tips & Tricks](https://docs.cloud.google.com/functions/1stgendocs/bestpractices/tips)



## Code sample

### C#

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

### Go

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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
    

### Java

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

### Node.js

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

### PHP

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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
    

### Python

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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
    
    

### Ruby

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudfunctions). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
