---
url: https://docs.cloud.google.com/functions/docs/samples/functions-concepts-after-timeout/
title: Execution after timeout \u00a0|\u00a0 Cloud Run functions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:51:58.693274+00:00
---

# Execution after timeout  |  Cloud Run functions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/docs/samples/functions-concepts-after-timeout/

If you are creating a new function, see the [Console Quickstart](https://docs.cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ Samples ](https://docs.cloud.google.com/functions/docs/samples)



#  Execution after timeout Stay organized with collections  Save and categorize content based on your preferences. 

Sample that demonstrates code that should (but won't) execute after a GCF call times out.

## Code sample

### Go

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Package tips contains tips for writing Cloud Functions in Go.
    package tips
    
    import (
    	"fmt"
    	"log"
    	"net/http"
    	"time"
    
    	"github.com/GoogleCloudPlatform/functions-framework-go/functions"
    )
    
    func init() {
    	functions.HTTP("Timeout", Timeout)
    }
    
    // Timeout sleeps for 2 minutes and may time out before finishing.
    func Timeout(w http.ResponseWriter, r *http.Request) {
    	log.Println("Function execution started...")
    	time.Sleep(2 * time.Minute)
    	log.Println("Function completed!")
    	fmt.Fprintln(w, "Function completed!")
    }
    

### Java

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    package functions;
    
    import com.google.cloud.functions.HttpFunction;
    import com.google.cloud.functions.HttpRequest;
    import com.google.cloud.functions.HttpResponse;
    import java.io.BufferedWriter;
    import java.io.IOException;
    import java.util.concurrent.TimeUnit;
    import java.util.logging.Logger;
    
    public class AfterTimeout implements HttpFunction {
      private static final Logger logger = Logger.getLogger(AfterTimeout.class.getName());
    
      // Simple function to return "Hello World"
      @Override
      public void service(HttpRequest request, HttpResponse response)
          throws IOException, InterruptedException {
        logger.info("Function running...");
        TimeUnit.MINUTES.sleep(2);
    
        // May not execute if function's timeout is <2 minutes
        logger.info("Function completed!");
        BufferedWriter writer = response.getWriter();
        writer.write("Function completed!");
      }
    }

### Node.js

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const functions = require('@google-cloud/functions-framework');
    
    /**
     * HTTP Cloud Function that may not completely
     * execute due to function execution timeout
     *
     * @param {Object} req Cloud Function request context.
     * @param {Object} res Cloud Function response context.
     */
    functions.http('afterTimeout', (req, res) => {
      setTimeout(() => {
        // May not execute if function's timeout is <2 minutes
        console.log('Function running...');
        res.end();
      }, 120000); // 2 minute delay
    });

### Python

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import time
    
    import functions_framework
    
    
    @functions_framework.http
    def timeout(request):
        print("Function running...")
        time.sleep(120)
    
        # May not execute if function's timeout is <2 minutes
        print("Function completed!")
        return "Function completed!"
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudfunctions). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
