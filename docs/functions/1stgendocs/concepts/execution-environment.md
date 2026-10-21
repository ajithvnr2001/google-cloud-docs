---
url: https://docs.cloud.google.com/functions/1stgendocs/concepts/execution-environment/
title: Cloud Functions execution environment \u00a0|\u00a0 Cloud Run functions (1st gen) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:29:28.403363+00:00
---

# Cloud Functions execution environment  |  Cloud Run functions (1st gen)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/1stgendocs/concepts/execution-environment/

If you are creating a new function, see the [Console Quickstart](https://cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. The content on this page only applies to existing legacy functions created with the Cloud Functions v1 API. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ 1st generation ](https://docs.cloud.google.com/functions/1stgendocs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/functions/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Cloud Functions execution environment

Cloud Run functions run in a fully-managed serverless environment where Google handles infrastructure, operating systems, and runtime environments. Each function runs in its own isolated secure execution context, scales automatically, and has a lifecycle independent from other functions.

## Runtimes

Cloud Run functions supports multiple language runtimes. Each contains a standard set of [system packages](https://docs.cloud.google.com/functions/docs/reference/system-packages), as well as the tools and libraries needed for that language. You'll need the **Runtime ID** value if you're deploying functions [from the command line](https://docs.cloud.google.com/functions/docs/deploying/filesystem) or through [Terraform](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloudfunctions_function).

Security and maintenance updates are made available to all 1st and 2nd gen execution environments. These updates are applied automatically or manually, depending on the environment and how you've configured it. For more information about execution environment updates, see [Secure your Cloud Run function](https://docs.cloud.google.com/functions/docs/securing#updating).

### Node.js

Runtime | Generation | Environment | Runtime ID | Runtime image  
---|---|---|---|---  
Node.js 26   
(Preview) | 2nd gen | Ubuntu 24.04 | nodejs26 |  [us-central1-docker.pkg.dev/serverless-runtimes/google-24-full/runtimes/nodejs26](http://us-central1-docker.pkg.dev/serverless-runtimes/google-24-full/runtimes/nodejs26)  
Node.js 24 | 2nd gen | Ubuntu 24.04 | nodejs24 |  [us-central1-docker.pkg.dev/serverless-runtimes/google-24-full/runtimes/nodejs24](http://us-central1-docker.pkg.dev/serverless-runtimes/google-24-full/runtimes/nodejs24)  
Node.js 22 | 1st gen, 2nd gen | Ubuntu 22.04 | nodejs22 |  [us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/nodejs22](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/nodejs22)  
Node.js 20 | 1st gen, 2nd gen | Ubuntu 22.04 | nodejs20 |  [us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/nodejs20](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/nodejs20)  
Node.js 18 | 1st gen, 2nd gen | Ubuntu 22.04 | nodejs18 |  [us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/nodejs18](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/nodejs18)  
Node.js 16 | 1st gen, 2nd gen | Ubuntu 18.04 | nodejs16 |  [us-central1-docker.pkg.dev/serverless-runtimes/google-18-full/runtimes/nodejs16](http://us-central1-docker.pkg.dev/serverless-runtimes/google-18-full/runtimes/nodejs16)  
Node.js 14 | 1st gen, 2nd gen | Ubuntu 18.04 | nodejs14 |  [us-central1-docker.pkg.dev/serverless-runtimes/google-18-full/runtimes/nodejs14](http://us-central1-docker.pkg.dev/serverless-runtimes/google-18-full/runtimes/nodejs14)  
Node.js 12 | 1st gen, 2nd gen | Ubuntu 18.04 | nodejs12 |  [us-central1-docker.pkg.dev/serverless-runtimes/google-18-full/runtimes/nodejs12](http://us-central1-docker.pkg.dev/serverless-runtimes/google-18-full/runtimes/nodejs12)  
Node.js 10 | 1st gen, 2nd gen | Ubuntu 18.04 | nodejs10 |  [us-central1-docker.pkg.dev/serverless-runtimes/google-18-full/runtimes/nodejs10](http://us-central1-docker.pkg.dev/serverless-runtimes/google-18-full/runtimes/nodejs10)  
Node.js 8 | 1st gen, 2nd gen | Ubuntu 18.04 | nodejs8 |  Decommissioned   
Node.js 6 | 1st gen, 2nd gen | Ubuntu 18.04 | nodejs6 |  Decommissioned   
  
### Python

Runtime | Generation | Environment | Runtime ID | Runtime image  
---|---|---|---|---  
Python 3.14 | 2nd gen | Ubuntu 24.04 | python314 |  [us-central1-docker.pkg.dev/serverless-runtimes/google-24-full/runtimes/python314](http://us-central1-docker.pkg.dev/serverless-runtimes/google-24-full/runtimes/python314)  
Python 3.13 | 2nd gen | Ubuntu 22.04 | python313 |  [us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/python313](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/python313)  
Python 3.12 | 1st gen, 2nd gen | Ubuntu 22.04 | python312 |  [us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/python312](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/python312)  
Python 3.11 | 1st gen, 2nd gen | Ubuntu 22.04 | python311 |  [us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/python311](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/python311) | Python 3.10 | 1st gen, 2nd gen | Ubuntu 22.04 | python310 |  [us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/python310](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/python310)  
Python 3.9 | 1st gen, 2nd gen | Ubuntu 18.04 | python39 |  [us-central1-docker.pkg.dev/serverless-runtimes/google-18-full/runtimes/python39](http://us-central1-docker.pkg.dev/serverless-runtimes/google-18-full/runtimes/python39)  
Python 3.8 | 1st gen, 2nd gen | Ubuntu 18.04 | python38 |  [us-central1-docker.pkg.dev/serverless-runtimes/google-18-full/runtimes/python38](http://us-central1-docker.pkg.dev/serverless-runtimes/google-18-full/runtimes/python38)  
Python 3.7 | 1st gen | Ubuntu 18.04 | python37 |  [us-central1-docker.pkg.dev/serverless-runtimes/google-18-full/runtimes/python37](http://us-central1-docker.pkg.dev/serverless-runtimes/google-18-full/runtimes/python37)  
  
###  Go 

Runtime | Generation | Environment | Runtime ID | Runtime image  
---|---|---|---|---  
Go 1.27 | 2nd gen | Ubuntu 24.04 | go127 |  [us-central1-docker.pkg.dev/serverless-runtimes/google-24-full/runtimes/go127](http://us-central1-docker.pkg.dev/serverless-runtimes/google-24-full/runtimes/go127)  
Go 1.26 | 2nd gen | Ubuntu 24.04 | go126 |  [us-central1-docker.pkg.dev/serverless-runtimes/google-24-full/runtimes/go126](http://us-central1-docker.pkg.dev/serverless-runtimes/google-24-full/runtimes/go126)  
Go 1.25 | 2nd gen | Ubuntu 22.04 | go125 |  [us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/go125](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/go125)  
Go 1.24 | 2nd gen | Ubuntu 22.04 | go124 |  [us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/go124](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/go124)  
Go 1.23 | 2nd gen | Ubuntu 22.04 | go123 |  [us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/go123](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/go123)  
Go 1.22 | 2nd gen | Ubuntu 22.04 | go122 |  [us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/go122](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/go122)  
Go 1.21 | 1st gen, 2nd gen | Ubuntu 22.04 | go121 |  [us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/go121](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/go121)  
Go 1.20 | 1st gen, 2nd gen | Ubuntu 22.04 | go120 |  [us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/go120](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/go120)  
Go 1.19 | 1st gen, 2nd gen | Ubuntu 22.04 | go119 |  [us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/go119](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/go119)  
Go 1.18 | 1st gen, 2nd gen | Ubuntu 22.04 | go118 |  [us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/go118](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/go118)  
Go 1.16 | 1st gen, 2nd gen | Ubuntu 18.04 | go116 |  [us-central1-docker.pkg.dev/serverless-runtimes/google-18-full/runtimes/go116](http://us-central1-docker.pkg.dev/serverless-runtimes/google-18-full/runtimes/go116)  
Go 1.13 | 1st gen, 2nd gen | Ubuntu 18.04 | go113 |  [us-central1-docker.pkg.dev/serverless-runtimes/google-18-full/runtimes/go113](http://us-central1-docker.pkg.dev/serverless-runtimes/google-18-full/runtimes/go113)  
Go 1.11 | 1st gen, 2nd gen | Ubuntu 18.04 | go111 |  Decommissioned   
**Note:** Go's [release policy](https://go.dev/doc/devel/release#policy) states that each major Go release is supported until there are two newer major releases. Key dates might not be available until newer versions of Go are made publicly available. 

###  Java 

Runtime | Generation | Environment | Runtime ID | Runtime image  
---|---|---|---|---  
Java 25 | 2nd gen | Ubuntu 24.04 | java25 |  [us-central1-docker.pkg.dev/serverless-runtimes/google-24-full/runtimes/java25](http://us-central1-docker.pkg.dev/serverless-runtimes/google-24-full/runtimes/java25)  
Java 21 | 2nd gen | Ubuntu 22.04 | java21 |  [us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/java21](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/java21)  
Java 17 | 1st gen, 2nd gen | Ubuntu 22.04 | java17 |  [us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/java17](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/java17)  
Java 11 | 1st gen, 2nd gen | Ubuntu 18.04 | java11 |  [us-central1-docker.pkg.dev/serverless-runtimes/google-18-full/runtimes/java11](http://us-central1-docker.pkg.dev/serverless-runtimes/google-18-full/runtimes/java11)  
  
### Ruby

Runtime | Generation | Environment | Runtime ID | Runtime image  
---|---|---|---|---  
Ruby 4.0 | 2nd gen | Ubuntu 24.04 | ruby40 |  [us-central1-docker.pkg.dev/serverless-runtimes/google-24-full/runtimes/ruby40](http://us-central1-docker.pkg.dev/serverless-runtimes/google-24-full/runtimes/ruby40)  
Ruby 3.4 | 2nd gen | Ubuntu 22.04 | ruby34 |  [us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/ruby34](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/ruby34)  
Ruby 3.3 | 1st gen, 2nd gen | Ubuntu 22.04 | ruby33 |  [us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/ruby33](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/ruby33)  
Ruby 3.2 | 1st gen, 2nd gen | Ubuntu 22.04 | ruby32 |  [us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/ruby32](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/ruby32)  
Ruby 3.0 | 1st gen, 2nd gen | Ubuntu 18.04 | ruby30 |  [us-central1-docker.pkg.dev/serverless-runtimes/google-18-full/runtimes/ruby30](http://us-central1-docker.pkg.dev/serverless-runtimes/google-18-full/runtimes/ruby30)  
Ruby 2.7 | 1st gen, 2nd gen | Ubuntu 18.04 | ruby27 |  [us-central1-docker.pkg.dev/serverless-runtimes/google-18-full/runtimes/ruby27](http://us-central1-docker.pkg.dev/serverless-runtimes/google-18-full/runtimes/ruby27)  
Ruby 2.6 | 1st gen, 2nd gen | Ubuntu 18.04 | ruby26 |  [us-central1-docker.pkg.dev/serverless-runtimes/google-18-full/runtimes/ruby26](http://us-central1-docker.pkg.dev/serverless-runtimes/google-18-full/runtimes/ruby26)  
  
### PHP

Runtime | Environment | Generation | Runtime ID | Runtime image  
---|---|---|---|---  
PHP 8.5 | 2nd gen | Ubuntu 24.04 | php85 |  [us-central1-docker.pkg.dev/serverless-runtimes/google-24-full/runtimes/php85](http://us-central1-docker.pkg.dev/serverless-runtimes/google-24-full/runtimes/php85)  
PHP 8.4 | 2nd gen | Ubuntu 22.04 | php84 |  [us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/php84](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/php84)  
PHP 8.3 | 2nd gen | Ubuntu 22.04 | php83 |  [us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/php83](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/php83)  
PHP 8.2 | 1st gen, 2nd gen | Ubuntu 22.04 | php82 |  [us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/php82](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/php82)  
PHP 8.1 | 1st gen, 2nd gen | Ubuntu 18.04 | php81 |  [us-central1-docker.pkg.dev/serverless-runtimes/google-18-full/runtimes/php81](http://us-central1-docker.pkg.dev/serverless-runtimes/google-18-full/runtimes/php81)  
PHP 7.4 | 1st gen, 2nd gen | Ubuntu 18.04 | php74 |  [us-central1-docker.pkg.dev/serverless-runtimes/google-18-full/runtimes/php74](http://us-central1-docker.pkg.dev/serverless-runtimes/google-18-full/runtimes/php74)  
  
### .NET Core

Runtime | Generation | Environment | Runtime ID | Runtime image  
---|---|---|---|---  
.NET Core 10 | 2nd gen | Ubuntu 24.04 | dotnet10 |  [us-central1-docker.pkg.dev/serverless-runtimes/google-24-full/runtimes/dotnet10](http://us-central1-docker.pkg.dev/serverless-runtimes/google-24-full/runtimes/dotnet10)  
.NET Core 8 | 2nd gen | Ubuntu 22.04 | dotnet8 |  [us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/dotnet8](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/dotnet8)  
.NET Core 6 | 1st gen, 2nd gen | Ubuntu 22.04 | dotnet6 |  [us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/dotnet6](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/dotnet6)  
.NET Core 3 | 1st gen, 2nd gen | Ubuntu 18.04 | dotnet3 |  [us-central1-docker.pkg.dev/serverless-runtimes/google-18-full/runtimes/dotnet3](http://us-central1-docker.pkg.dev/serverless-runtimes/google-18-full/runtimes/dotnet3)  
  
## Auto-scaling behavior

Cloud Run functions implements the serverless paradigm, in which you run your code without worrying about the underlying infrastructure, such as servers or virtual machines. Once deployed, your functions are automatically managed and scaled.

Cloud Run functions handles incoming requests by assigning them to _instances_ of your function. Depending on the volume of requests, as well as the number of existing function instances, Cloud Run functions may assign a request to an existing instance or create a new one.

In cases where inbound request volume exceeds the number of existing instances, Cloud Run functions may start multiple new instances to handle requests. This automatic scaling behavior allows Cloud Run functions to handle many requests in parallel, each using a different instance of your function.

**Note:** An extremely rapid increase in inbound traffic can intermittently cause some requests to fail with an HTTP code of 500. This is because the requests time out in the pending queue while waiting for new instances to be created. Configuring your workload so that it ramps traffic up gradually over the course of a minute can help with this issue. Also see [Troubleshooting Cloud Functions](https://docs.cloud.google.com/functions/docs/troubleshooting#scalability) for more information.

In some cases, unbounded scaling might be undesirable. To address this, Cloud Run functions allows you to configure a [maximum number of instances](https://docs.cloud.google.com/functions/docs/configuring/max-instances) that can coexist at any given time for a particular function.

### Statelessness

To enable automatic management and scaling of your functions, functions must be _stateless_ —one function invocation must not rely on in-memory state set by a previous invocation. Invocations might be handled by different function instances, which do not share global variables, memory, file systems, or other state.

**Note:** Though it must not be relied upon, in-memory state can often be reused as a performance optimization; see the recommendation in [Tips and Tricks](https://docs.cloud.google.com/functions/docs/bestpractices/tips#use_global_variables_to_reuse_objects_in_future_invocations) for details.

If you need to share state across function invocations, your function should use a service such as [Memorystore](https://docs.cloud.google.com/memorystore), [Datastore](https://docs.cloud.google.com/datastore), [Firestore](https://firebase.google.com/products/firestore/), or [Cloud Storage](https://docs.cloud.google.com/storage) to persist data. See [Google Cloud databases](https://cloud.google.com/products/databases) and [Google Cloud storage products](https://cloud.google.com/products/storage) for more information about database and storage options provided by Google Cloud.

### Concurrency

#### Cloud Run functions (2nd gen)

Cloud Run functions (2nd gen) supports handling multiple concurrent requests on a single function instance. This can be helpful in preventing cold starts since an already warmed instance can process multiple requests simultaneously, thereby reducing overall latency. For details, see [Concurrency](https://docs.cloud.google.com/functions/docs/configuring/concurrency).

#### Cloud Run functions (1st gen)

In Cloud Run functions (1st gen), each instance of a function handles only one concurrent request at a time. This means that while your code is processing one request, there is no possibility of a second request being routed to the same instance. Thus the original request can use the full amount of resources (memory and CPU) that you allocate.

Because concurrent requests in Cloud Run functions (1st gen) are processed by different function instances, they do not share variables or local memory. See Statelessness and Function instance lifespan for more information.

### Cold starts

A new function instance is started in two cases:

  * When you deploy your function.

  * When a new function instance is automatically created to scale up to the load, or occasionally to replace an existing instance.




Starting a new function instance involves loading the runtime and your code. Requests that include function instance startup, called _cold starts_ , can be slower than requests routed to existing function instances. If your function receives steady load, however, then the number of cold starts is typically negligible unless your function frequently crashes and requires restarting of the function environment.

If your function code throws an uncaught exception or crashes the current process, the function instance might be restarted. This can lead to more cold starts, resulting in higher latency, so we recommend catching exceptions and otherwise avoiding termination of the current process.

**Note:** In 1st gen, the amount of memory granted to a function impacts the CPU allocation, which in turn can have an impact on cold start time (see [pricing](https://cloud.google.com/functions/pricing#compute_time)). While this is also true in 2nd gen by default, in 2nd gen you have the option of configuring [CPU allocation](https://docs.cloud.google.com/functions/docs/configuring/memory#set-vcpu) separate from memory.

If your function is latency-sensitive, consider setting a [minimum number of instances](https://docs.cloud.google.com/functions/docs/configuring/min-instances) to avoid cold starts.

### Function instance lifespan

Function instances are typically resilient and reused by subsequent function invocations, unless the number of instances is being scaled down due to lack of ongoing traffic or your function crashes. This means that when one function execution ends, another function invocation can be handled by the same function instance.

**Note:** As a performance optimization, you can cache state across invocations in global scope where possible. However, your function must not rely on this cached state as there is no guarantee that the next invocation will reach the same function instance - see Statelessness.

## Function scope versus global scope

A single function invocation results in execution of only the body of the function declared as the entry point. The global scope of your function source code is only executed on cold starts, and not on instances that have already been initialized.

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

You can use global variables as a performance optimization, but you must not rely on state set in the global scope by previous function invocations - see Statelessness for more information.

You can assume that for each function instance, the global scope has been executed exactly once before your function code is invoked. However, you must not depend on the total number of or timing of global scope executions, as they might vary depending on auto-scaling activity.

## Function execution timeline

A function has access to its allocated resources (memory and CPU) only for the duration of function execution. Code run outside of the execution period is not guaranteed to execute, and it can be stopped at any time. Therefore, you should always signal the end of your function execution correctly and avoid running any code beyond it. See [HTTP Functions](https://docs.cloud.google.com/functions/docs/writing/http), [Background Functions](https://docs.cloud.google.com/functions/docs/writing/background#terminating_background_functions), and [CloudEvent Functions](https://docs.cloud.google.com/functions/docs/writing/cloudevents#terminating_cloudevent_functions) for guidance.

Function execution is also subject to the timeout duration of the function. See [Function timeout](https://docs.cloud.google.com/functions/docs/configuring/timeout) for more information.

Take into account the execution timeline when initializing your application. Background tasks should not be created in global scope during initialization, as they would execute outside of the duration of a request.

## Execution guarantees

Your functions are typically invoked once for each incoming event. However, Cloud Run functions does not guarantee a single invocation in all cases because of differences in error scenarios.

The maximum or minimum number of times your function could be invoked for a single event depends on the type of your function:

  * HTTP functions are invoked at _most_ once. This is because of the synchronous nature of HTTP calls, and it means that any error that occurs during function invocation will be returned without retrying. The caller of an HTTP function is expected to handle errors and retry if needed.

  * Event-driven functions are invoked at _least_ once. This is because of the asynchronous nature of events, in which there is no caller that waits for the response. The system might, in rare circumstances, invoke an event-driven function more than once in order to ensure delivery of the event. If an event-driven function invocation fails with an error, the function will not be invoked again unless [retries on failure](https://docs.cloud.google.com/functions/docs/bestpractices/retries) are enabled for that function.




To make sure that your function behaves correctly on retried execution attempts, you should make it _idempotent_ by implementing it so that the desired results (and side effects) are produced even if an event is delivered multiple times. In the case of HTTP functions, this also means returning the desired value even if the caller retries calls to the HTTP function endpoint. See [Retrying Event-Driven Functions](https://docs.cloud.google.com/functions/docs/bestpractices/retries#make_retryable_event-driven_functions_idempotent) for more information on how to make your function idempotent.

## Memory and file system

Each function has a certain amount of memory allocated for its use. You can configure the amount of memory at deployment - see [Configure memory](https://docs.cloud.google.com/functions/1stgendocs/configuring/memory) for more information.

The function execution environment includes an in-memory file system that contains the source files and directories deployed with your function (see [Structuring source code](https://docs.cloud.google.com/functions/docs/writing#structuring_source_code)). The directory containing your source files is read-only, but the rest of the file system is writeable (except for files used by the operating system). Use of the file system counts towards a function's memory usage.

Your function can interact with the file system using standard methods in each programming language.

**Note:** In the Cloud Run functions execution environment, the root directory of your function source code is the current working directory (`.`), with the exception of Go runtimes, where the root directory of your function source code is beneath the current working directory at `./serverless_function_source_code`.

## Network

Your function can access the public internet using standard methods in each programming language, whether through built-in libraries offered by the runtime or third-party libraries you include as dependencies.

Try to reuse network connections across function invocations. However, note that a connection that remains unused for 10 minutes might be closed by the system, and further attempts to use a closed connection will result in a "connection reset" error. Your code should either use a library that handles closed connections well, or handle them explicitly if using low-level networking constructs.

## Function isolation

Every deployed function is isolated from all other functions—even those deployed from the same source file. In particular, they do not share memory, global variables, file systems, or other state.

To share data across deployed functions, you can use services such as [Memorystore](https://docs.cloud.google.com/memorystore), [Datastore](https://docs.cloud.google.com/datastore), [Firestore](https://firebase.google.com/products/firestore/), or [Cloud Storage](https://docs.cloud.google.com/storage). Alternatively, you can invoke one function from another using their appropriate triggers and passing along the necessary data. For example, make an HTTP request to the endpoint of an HTTP function or publish a message to a Pub/Sub topic to trigger a Pub/Sub function.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
