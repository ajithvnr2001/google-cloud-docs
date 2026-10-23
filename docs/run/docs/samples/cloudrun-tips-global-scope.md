---
url: https://docs.cloud.google.com/run/docs/samples/cloudrun-tips-global-scope/
title: Using global scoped variables \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:45:23.876668+00:00
---

# Using global scoped variables  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/samples/cloudrun-tips-global-scope/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Samples ](https://docs.cloud.google.com/run/docs/samples)



#  Using global scoped variables Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrate how to minimize the memory footprint of reusable variables by leveraging global scope.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [General development tips](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/tips/general)
  * [General development tips](https://docs.cloud.google.com/run/docs/tips/general)



## Code sample

### Go

To authenticate to Cloud Run, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

To authenticate to Cloud Run, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

To authenticate to Cloud Run, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

### Python

To authenticate to Cloud Run, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudrun). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
