---
url: https://docs.cloud.google.com/functions/docs/samples/functions-helloworld-error/
title: Hello World error \u00a0|\u00a0 Cloud Run functions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:03:05.130560+00:00
---

# Hello World error  |  Cloud Run functions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/docs/samples/functions-helloworld-error/

If you are creating a new function, see the [Console Quickstart](https://docs.cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ Samples ](https://docs.cloud.google.com/functions/docs/samples)



#  Hello World error Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates how to report an error.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Report runtime function errors (1st gen)](https://docs.cloud.google.com/functions/1stgendocs/monitoring/error-reporting)



## Code sample

### Go

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    package tips
    
    import (
    	"fmt"
    	"net/http"
    	"os"
    
    	"github.com/GoogleCloudPlatform/functions-framework-go/functions"
    )
    
    func init() {
    	functions.HTTP("HTTPError", HTTPError)
    }
    
    // HTTPError describes how errors are handled in an HTTP function.
    func HTTPError(w http.ResponseWriter, r *http.Request) {
    	// An error response code is NOT reported to Error Reporting.
    	// http.Error(w, "An error occurred", http.StatusInternalServerError)
    
    	// Printing to stdout and stderr is NOT reported to Error Reporting.
    	fmt.Println("An error occurred (stdout)")
    	fmt.Fprintln(os.Stderr, "An error occurred (stderr)")
    
    	// Calling log.Fatal sets a non-zero exit code and is NOT reported to Error
    	// Reporting.
    	// log.Fatal("An error occurred (log.Fatal)")
    
    	// Panics are reported to Error Reporting.
    	panic("An error occurred (panic)")
    }
    

### Java

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.functions.HttpFunction;
    import com.google.cloud.functions.HttpRequest;
    import com.google.cloud.functions.HttpResponse;
    import java.io.IOException;
    import java.util.logging.Logger;
    
    public class HelloError implements HttpFunction {
    
      private static final Logger logger = Logger.getLogger(HelloError.class.getName());
    
      @Override
      public void service(HttpRequest request, HttpResponse response)
          throws IOException {
        // These will NOT be reported to Error Reporting
        System.err.println("I failed you");
        logger.severe("I failed you");
    
        // This WILL be reported to Error Reporting
        throw new RuntimeException("I failed you");
      }
    }

### Node.js

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // These WILL be reported to Error Reporting
    throw new Error('I failed you'); // Will cause a cold start if not caught

### Python

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    @functions_framework.http
    def hello_error_1(request):
        # This WILL be reported to Error Reporting,
        # and WILL NOT show up in logs or
        # terminate the function.
        from google.cloud import error_reporting
    
        client = error_reporting.[Client](https://docs.cloud.google.com/python/docs/reference/clouderrorreporting/latest/google.cloud.error_reporting.client.Client.html)()
    
        try:
            raise RuntimeError("I failed you")
        except RuntimeError:
            [client](https://docs.cloud.google.com/python/docs/reference/clouderrorreporting/latest/google.cloud.error_reporting.client.html).[report_exception](https://docs.cloud.google.com/python/docs/reference/clouderrorreporting/latest/google.cloud.error_reporting.client.Client.html#google_cloud_error_reporting_client_Client_report_exception)()
    
        # This WILL be reported to Error Reporting,
        # and WILL terminate the function
        raise RuntimeError("I failed you")
    
    
    @functions_framework.http
    def hello_error_2(request):
        # These errors WILL NOT be reported to Error
        # Reporting, but will show up in logs.
        import logging
        import sys
    
        print(RuntimeError("I failed you (print to stdout)"))
        logging.warning(RuntimeError("I failed you (logging.warning)"))
        logging.error(RuntimeError("I failed you (logging.error)"))
        sys.stderr.write("I failed you (sys.stderr.write)\n")
    
        # This is considered a successful execution and WILL NOT be reported
        # to Error Reporting, but the status code (500) WILL be logged.
        from flask import abort
    
        return abort(500)
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudfunctions). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
