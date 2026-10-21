---
url: https://docs.cloud.google.com/run/docs/samples/cloudrun-tips-global-lazy/
title: Lazy variable initialization \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:15:36.951626+00:00
---

# Lazy variable initialization  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/samples/cloudrun-tips-global-lazy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Samples ](https://docs.cloud.google.com/run/docs/samples)



#  Lazy variable initialization Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrate the use of lazy initialization of values for cases where memory allocation and response latency impacting operations are not commonly needed by the Cloud Run service.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [General development tips](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/tips/general)
  * [General development tips](https://docs.cloud.google.com/run/docs/tips/general)



## Code sample

### Go

To authenticate to Cloud Run, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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
    

### Java

To authenticate to Cloud Run, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

### Node.js

To authenticate to Cloud Run, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

### Python

To authenticate to Cloud Run, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudrun). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
