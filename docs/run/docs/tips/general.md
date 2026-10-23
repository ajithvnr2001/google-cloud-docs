---
url: https://docs.cloud.google.com/run/docs/tips/general/
title: General development tips \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:58:11.951520+00:00
---

# General development tips  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/tips/general/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  General development tips Stay organized with collections  Save and categorize content based on your preferences. 

Designing Cloud Run services with recommended practices lets you optimize runtime efficiency, minimize container startup latency, and scale predictably across workloads. These design, concurrency, and security strategies help you build resilient and cost-effective services. If you are moving an existing web service to Cloud Run, see [Migrating an existing service](https://docs.cloud.google.com/run/docs/migrating).

## Write effective services

This section describes general best practices for designing and implementing a Cloud Run service.

### Background activity

Background activity is anything that happens after your HTTP response has been delivered. To determine whether there is background activity in your service that is not readily apparent, check your logs for anything that is logged after the entry for the HTTP request.

#### Configure instance-based billing to use background activities

If you want to support background activities in your Cloud Run service, set your Cloud Run service to [instance-based billing](https://docs.cloud.google.com/run/docs/configuring/billing-settings) so you can run background activities outside of requests and still have CPU access.

#### Avoid background activities if using request-based billing

If you need to set your service to [request-based billing](https://docs.cloud.google.com/run/docs/configuring/billing-settings), when the Cloud Run service finishes handling a request, the instance's access to CPU will be disabled or severely limited. You shouldn't start background threads or routines that run outside the scope of the request handlers if you use this type of billing.

Review your code to make sure all asynchronous operations finish before you deliver your response.

Running background threads with request-based billing enabled can result in unexpected behavior because any subsequent request to the same container instance resumes any suspended background activity.

### Delete temporary files

In the Cloud Run environment, disk storage is an in-memory filesystem. Files written to disk consume memory otherwise available to your service, and can persist between invocations. Failing to delete these files can eventually lead to an out-of-memory error and a subsequent slow container startup times.

### Report errors

Handle all exceptions and do not let your service crash on errors. A crash leads to a slow container startup while traffic is queued for a replacement instance.

See the [Error reporting guide](https://docs.cloud.google.com/run/docs/error-reporting) for information on how to properly report errors.

## Optimize performance

This section describes best practices for optimizing performance.

### Start containers quickly

Because instances are [scaled as needed](https://docs.cloud.google.com/run/docs/about-instance-autoscaling), their startup time has impact on the latency of your service. Cloud Run de-couples instance startup and request processing, so in some cases a request must wait for a new instance to start before the request is processed. This commonly happens when a service scales from zero.

The startup routine consists of:

  * Downloading the container image (using Cloud Run's container image streaming technology)
  * Starting the container by running the [entrypoint](https://docs.cloud.google.com/run/docs/configuring/services/containers#configure-entrypoint) command.
  * Waiting for the container to start listening on the [configured port](https://docs.cloud.google.com/run/docs/configuring/services/containers#configure-port).



Optimizing for container startup speed minimizes the request processing latency.

### Use startup CPU boost to reduce startup latency

You can [enable startup CPU boost](https://docs.cloud.google.com/run/docs/configuring/services/cpu#startup-boost) to temporarily increase CPU allocation during instance startup in order to reduce startup latency.

### Use minimum instances to reduce container startup times

You can configure [minimum instances](https://docs.cloud.google.com/run/docs/configuring/min-instances) and [concurrency](https://docs.cloud.google.com/run/docs/configuring/concurrency) to minimize container startup times. For example, using a minimum instances of 1 means that your service is ready to receive up to the number of concurrent requests configured for your service without needing to start a new instance. When using minimum instances, avoid using system exits that will shut down an instance and potentially increase cold starts.

Note that a request waiting for an instance to start will be kept pending in a queue as follows:

Requests will pend for up to 3.5 times average startup time of container instances of this service, or 10 seconds, whichever is greater.

### Use dependencies wisely

If you use a dynamic language with dependent libraries, such as importing modules in Node.js, the load time for those modules adds to the startup latency.

Reduce startup latency in these ways:

  * Minimize the number and size of dependencies to build a lean service.
  * Lazily load code that is infrequently used, if your language supports it.
  * Use code-loading optimizations such as PHP's [composer autoloader optimization](https://getcomposer.org/doc/articles/autoloader-optimization.md).



### Use global variables

In Cloud Run, you cannot assume that service state is preserved between requests. However, Cloud Run does reuse individual instances to serve ongoing traffic, so you can declare a variable in global scope to allow its value to be reused in subsequent invocations. Whether any individual request receives the benefit of this reuse cannot be known ahead of time.

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

### Perform lazy initialization of global variables

The initialization of global variables always occurs during startup, which increases container startup time. Use lazy initialization for infrequently used objects to defer the time cost and decrease container startup times.

One drawback of lazy initialization is an increased latency for first requests to new instances. This can cause overscaling and dropped requests when you deploy a new revision of a service that is actively handling many requests.

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

### Use a different execution environment

You may experience faster startup times by using a [different execution environment](https://docs.cloud.google.com/run/docs/about-execution-environments).

## Optimize concurrency

Cloud Run instances can serve multiple requests simultaneously, "concurrently", up to a [configurable maximum concurrency](https://docs.cloud.google.com/run/docs/about-concurrency).

Cloud Run automatically adjusts the concurrency up to the configured maximum.

The default maximum concurrency of 80 is a good fit for many container images. However, you should:

  * Lower it if your container is not able to process many concurrent requests.
  * Increase it if your container is able to handle a large volume of requests.



### Tune concurrency for your service

The number of concurrent requests that each instance can serve can be limited by the technology stack and the use of shared resources such as variables and database connections.

To optimize your service for maximum stable concurrency:

  1. Optimize your service performance.
  2. Set your expected level of concurrency support in any code-level concurrency configuration. Not all technology stacks require such a setting.
  3. Deploy your service.
  4. Set Cloud Run concurrency for your service equal or less than any code-level configuration. If there is no code-level configuration, use your expected concurrency.
  5. Use [load testing](https://en.wikipedia.org/wiki/Load_testing) tools that support a configurable concurrency. You need to confirm that your service remains stable under expected load and concurrency.
  6. If the service does poorly, go to step 1 to improve the service or step 2 to reduce the concurrency. If the service does well, go back to step 2 and increase the concurrency.



Continue iterating until you find the maximum stable concurrency.

### Match memory to concurrency

Each request your service handles requires some amount of additional memory. So, when you adjust concurrency up or down, make sure you adjust your memory limit as well.

### Avoid mutable global state

If you want to leverage mutable global state in a concurrent context, take extra steps in your code to ensure this is done safely. Minimize contention by limiting global variables to one-time initialization and reuse as described above under Performance.

If you use mutable global variables in a service that serves multiple requests at the same time, make sure to use locks or mutexes to prevent race conditions.

### Throughput versus latency versus cost tradeoffs

Tuning the maximum concurrent requests setting can help balance the tradeoff between throughput, latency, and cost for your service.

In general, a lower maximum concurrent requests setting results in lower latency and lower throughput per instance. With lower maximimum concurrent requests, fewer requests compete for resources inside each instance and each request achieves better performance. But because each instance can serve fewer requests at once, the per instance throughput is lower and the service needs more instances to serve the same traffic.

In the opposite direction, a higher maximum concurrent requests setting generally results in higher latency and higher throughput per instance. Requests might need to wait for access to resources like CPU, GPU, and memory bandwidth inside the instance, which leads to increased latency. But each instance can process more requests at once such that the service needs less instances overall to process the same traffic.

### Cost considerations

[Cloud Run pricing](https://cloud.google.com/run/pricing) is per instance time. If you set [instance-based billing](https://docs.cloud.google.com/run/docs/configuring/billing-settings#pricing-impact), the instance time is the total lifetime of each instance. If you set request-based billing, the instance time is the time each instance spends processing at least one request.

The impact of maximum concurrent requests on billing depends on your traffic pattern. Lowering maximum concurrent requests _can_ result in a lower bill _if_ the lower setting leads to

  * Decreased latency
  * Instances completing their work faster
  * Instances shutting down faster even if more total instances are required



But the opposite is also possible: lowering maximum concurrent requests can _increase_ billing if the increase in number of instances is not outweighed by the reduction in time that each instance is running, due to the improved latency.

The best way to optimize billing is through [load testing](https://docs.cloud.google.com/run/docs/about-load-testing) using different maximum concurrent requests settings to identify the setting that results in the lowest billable instance time, as seen in the [`container/billable_instance_time` monitoring metric](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#gcp-run).

## Container security

Many general purpose software security practices apply to containerized services. There are some practices that are either specific to containers or that align with the philosophy and architecture of containers.

To improve container security:

  * Use actively maintained and secure base images such as Google [base images](https://docs.cloud.google.com/software-supply-chain-security/docs/base-images) or Docker Hub's [official images](https://hub.docker.com/search?q=&type=image&image_filter=official).

**Note:** As of November 1, 2020, Docker Hub [ rate limits](https://www.docker.com/blog/scaling-docker-to-serve-millions-more-developers-network-egress/) apply to unauthenticated or authenticated pull requests on the Docker Free plan. To avoid disruptions and have greater control over your software supply chain, you can migrate your dependencies to [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/docker/migrate-external-containers).

  * Apply security updates to your services by regularly rebuilding container images and redeploying your services.

  * Include in the container only what is necessary to run your service. Extra code, packages, and tools are potential security vulnerabilities. See above for the related performance impact.

  * Implement a [deterministic build process](https://en.wikipedia.org/wiki/Reproducible_builds) that includes specific software and library versions. This prevents unverified code from being included in your container.

  * Set your container to run as a user other than `root` with the [Dockerfile `USER` statement](https://docs.docker.com/engine/reference/builder/#user). Some container images may already have a specific user configured.

  * Prevent the use of Preview features by using [custom organization policies](https://docs.cloud.google.com/run/docs/securing/custom-constraints#prevent-launch-stage).




### Automate security scanning

Enable [vulnerability scanning](https://docs.cloud.google.com/artifact-analysis/docs/scanning-types#automated) for security scanning of container images stored in [Artifact Registry](https://docs.cloud.google.com/artifact-registry).

### Build minimal container images

Large container images likely increase security vulnerabilities because they contain more than what the code needs.

Because of Cloud Run's container image streaming technology, the size of your container image _does not affect_ container startup times or request processing time. The container image size also does not count towards the [available memory](https://docs.cloud.google.com/run/docs/configuring/services/memory-limits) of your container.

To build a minimal container, consider working from a lean base image such as:

  * [alpine](https://hub.docker.com/_/alpine)
  * [scratch](https://hub.docker.com/_/scratch)



[Ubuntu](https://hub.docker.com/_/ubuntu) is larger in size, but is a commonly used base image with a more complete out-of-box server environment.

If your service has a tool-heavy build process consider using [multi-stage builds](https://docs.docker.com/develop/develop-images/multistage-build/#use-multi-stage-builds) to keep your container light at run time.

These resources provide further information on creating lean container images:

  * [Kubernetes best practices: How and why to build small container images](https://cloud.google.com/blog/products/containers-kubernetes/kubernetes-best-practices-how-and-why-to-build-small-container-images)
  * [7 best practices for building containers](https://cloud.google.com/blog/products/containers-kubernetes/7-best-practices-for-building-containers)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
