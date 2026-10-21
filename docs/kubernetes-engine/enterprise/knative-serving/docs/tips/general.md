---
url: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/tips/general/
title: General development tips \u00a0|\u00a0 Knative serving \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:21:27.077750+00:00
---

# General development tips  |  Knative serving  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/tips/general/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Knative serving ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/architecture-overview)



Send feedback 

#  General development tips Stay organized with collections  Save and categorize content based on your preferences. 

This guide provides best practices for designing, implementing, testing, and deploying a Knative serving service. For more tips, see [Migrating an Existing Service](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/migrating).

## Writing effective services

This section describes general best practices for designing and implementing a Knative serving service.

### Avoiding background activities

When an application running on Knative serving finishes handling a request, the container instance's access to CPU will be disabled or severely limited. Therefore, you should not start background threads or routines that run outside the scope of the request handlers.

Running background threads can result in unexpected behavior because any subsequent request to the same container instance resumes any suspended background activity.

Background activity is anything that happens after your HTTP response has been delivered. Review your code to make sure all asynchronous operations finish before you deliver your response.

If you suspect there may be background activity in your service that is not readily apparent you can check your logs: look for anything that is logged after the entry for the HTTP request.

### Deleting temporary files

In the Cloud Run environment disk storage is an in-memory filesystem. Files written to disk consume memory otherwise available to your service, and can persist between invocations. Failing to delete these files can eventually lead to an out-of-memory error and a subsequent cold start.

## Optimizing performance

This section describes best practices for optimizing performance.

### Starting services quickly

Because container instances are scaled as needed, a typical method is to initialize the execution environment completely. This kind of initialization is called "cold start". If a client request triggers a cold start, the container instance startup results in additional latency.

The startup routine consists of:

  * Starting the service 
    * Starting the container
    * Running the [entrypoint](https://docs.docker.com/engine/reference/builder/#entrypoint) command to start your server.
  * Checking for the open service port.



Optimizing for service startup speed minimizes the latency that delays a container instance from serving requests.

### Using dependencies wisely

If you use a dynamic language with dependent libraries, such as importing modules in Node.js, the load time for those modules adds latency during a cold start. Reduce startup latency in these ways:

  * Minimize the number and size of dependencies to build a lean service.
  * Lazily load code that is infrequently used, if your language supports it.
  * Use code-loading optimizations such as PHP's [composer autoloader optimization](https://getcomposer.org/doc/articles/autoloader-optimization.md).



### Using global variables

In Knative serving, you cannot assume that service state is preserved between requests. However, Knative serving does reuse individual container instances to serve ongoing traffic, so you can declare a variable in global scope to allow its value to be reused in subsequent invocations. Whether any individual request receives the benefit of this reuse cannot be known ahead of time.

You can also cache objects in memory if they are expensive to recreate on each service request. Moving this from the request logic to global scope results in better performance.

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

### Performing lazy initialization of global variables

The initialization of global variables always occurs during startup, which increases cold start time. Use lazy initialization for infrequently used objects to defer the time cost and decrease cold start times.

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

## Optimizing concurrency

Knative serving instances can serve multiple requests simultaneously, "concurrently", up to a [configurable maximum concurrency](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/concurrency). This is different from Cloud Run functions, which uses `concurrency = 1`.

You should keep the default maximum concurrency setting unless your code has specific concurrency requirements.

### Tuning concurrency for your service

The number of concurrent requests that each container instance can serve can be limited by the technology stack and the use of shared resources such as variables and database connections.

To optimize your service for maximum stable concurrency:

  1. Optimize your service performance.
  2. Set your expected level of concurrency support in any code-level concurrency configuration. Not all technology stacks require such a setting.
  3. Deploy your service.
  4. Set Knative serving concurrency for your service equal or less than any code-level configuration. If there is no code-level configuration, use your expected concurrency.
  5. Use [load testing](https://en.wikipedia.org/wiki/Load_testing) tools that support a configurable concurrency. You need to confirm that your service remains stable under expected load and concurrency.
  6. If the service does poorly, go to step 1 to improve the service or step 2 to reduce the concurrency. If the service does well, go back to step 2 and increase the concurrency.



Continue iterating until you find the maximum stable concurrency.

### Matching memory to concurrency

Each request your service handles requires some amount of additional memory. So, when you adjust concurrency up or down, make sure you adjust your memory limit as well.

### Avoiding mutable global state

If you want to leverage mutable global state in a concurrent context, take extra steps in your code to ensure this is done safely. Minimize contention by limiting global variables to one-time initialization and reuse as described above under Performance.

If you use mutable global variables in a service that serves multiple requests at the same time, make sure to use locks or mutexes to prevent race conditions.

## Container security

Many general purpose software security practices apply to containerized applications. There are some practices that are either specific to containers or that align with the philosophy and architecture of containers.

To improve container security:

  * Use actively maintained and secure base images such as Google [base images](https://docs.cloud.google.com/software-supply-chain-security/docs/base-images) or Docker Hub's [official images](https://hub.docker.com/search?q=&type=image&image_filter=official).

**Note:** As of November 1, 2020, Docker Hub [ rate limits](https://www.docker.com/blog/scaling-docker-to-serve-millions-more-developers-network-egress/) apply to unauthenticated or authenticated pull requests on the Docker Free plan. To avoid disruptions and have greater control over your software supply chain, you can migrate your dependencies to [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/docker/migrate-external-containers).

  * Apply security updates to your services by regularly rebuilding container images and redeploying your services.

  * Include in the container only what is necessary to run your service. Extra code, packages, and tools are potential security vulnerabilities. See above for the related performance impact.

  * Implement a [deterministic build process](https://en.wikipedia.org/wiki/Reproducible_builds) that includes specific software and library versions. This prevents unverified code from being included in your container.

  * Set your container to run as a user other than `root` with the [Dockerfile `USER` statement](https://docs.docker.com/engine/reference/builder/#user). Some container images may already have a specific user configured.




### Automating security scanning

Enable [vulnerability scanning](https://docs.cloud.google.com/artifact-analysis/docs/scanning-types#automated) for security scanning of container images stored in [Artifact Registry](https://docs.cloud.google.com/artifact-registry).

You can also use [Binary Authorization](https://docs.cloud.google.com/binary-authorization/docs/configure-policy-gke) to ensure only secure container images are deployed.

### Building minimal container images

Large container images likely increase security vulnerabilities because they contain more than what the code needs.

On Knative serving, the size of your container image _does not affect_ cold start or request processing time and does not count towards the [available memory](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/configuring/memory-limits) of your container.

To build a minimal container, consider working from a lean base image such as:

  * [alpine](https://hub.docker.com/_/alpine)
  * [scratch](https://hub.docker.com/_/scratch)



[Ubuntu](https://hub.docker.com/_/ubuntu) is larger in size, but is a commonly used base image with a more complete out-of-box server environment.

If your service has a tool-heavy build process consider using [multi-stage builds](https://docs.docker.com/develop/develop-images/multistage-build/#use-multi-stage-builds) to keep your container light at run time.

These resources provide further information on creating lean container images:

  * [Kubernetes best practices: How and why to build small container images](https://cloud.google.com/blog/products/gcp/kubernetes-best-practices-how-and-why-to-build-small-container-images)
  * [7 best practices for building containers](https://cloud.google.com/blog/products/gcp/7-best-practices-for-building-containers)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
