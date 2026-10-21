---
url: https://docs.cloud.google.com/functions/1stgendocs/monitoring/error-reporting/
title: Report runtime function errors (1st gen) \u00a0|\u00a0 Cloud Run functions (1st gen) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:29:42.878860+00:00
---

# Report runtime function errors (1st gen)  |  Cloud Run functions (1st gen)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/1stgendocs/monitoring/error-reporting/

If you are creating a new function, see the [Console Quickstart](https://cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. The content on this page only applies to existing legacy functions created with the Cloud Functions v1 API. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ 1st generation ](https://docs.cloud.google.com/functions/1stgendocs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/functions/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Report runtime function errors (1st gen)

You should handle and report runtime errors that occur in Cloud Run functions. Uncaught exceptions or executions that crash the process can result in [cold starts](https://docs.cloud.google.com/functions/1stgendocs/concepts/execution-environment#cold-starts), which you should generally try to minimize.

The recommended way for a function to signal an error depends on the function type:

  * HTTP functions should return appropriate HTTP status codes which denote an error. See [HTTP Functions](https://docs.cloud.google.com/functions/1stgendocs/writing/write-http-functions) for more information.

  * Event-driven functions should log and return an error message. See [Write event-driven functions](https://docs.cloud.google.com/functions/1stgendocs/writing/write-event-driven-functions) for more information.




If errors are appropriately handled, then function instances that encounter errors can remain active and available to serve requests.

## Emit errors to Error Reporting

You can emit an error from a Cloud Run function to [Error Reporting](https://cloud.google.com/error-reporting/docs) as shown in the following:

###  Node.js 
    
    
    // These WILL be reported to Error Reporting
    throw new Error('I failed you'); // Will cause a cold start if not caught

###  Python 
    
    
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
    
    

###  Go 
    
    
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
    

###  Java 
    
    
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

If you would like more fine-grained error reporting, you can use the [Error Reporting client libraries](https://docs.cloud.google.com/error-reporting/docs/reference/libraries).

You can view the reported errors in [Error Reporting](https://console.cloud.google.com/errors) in the Google Cloud console. You can also see the errors reported from a particular function when you select it from the [list of functions](https://console.cloud.google.com/functions) in the Google Cloud console.

Uncaught exceptions produced by your function will appear in Error Reporting. Note that some types of uncaught exceptions (such as those thrown asynchronously) will cause a [cold start](https://docs.cloud.google.com/functions/1stgendocs/concepts/execution-environment#cold-starts) to occur upon a future function invocation. This increases the amount of time your function will take to run.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
