---
url: https://docs.cloud.google.com/run/docs/samples/cloudrun-manual-logging/
title: Write structured logs \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:58:35.326361+00:00
---

# Write structured logs  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/samples/cloudrun-manual-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Samples ](https://docs.cloud.google.com/run/docs/samples)



#  Write structured logs Stay organized with collections  Save and categorize content based on your preferences. 

Writes structured log entries with request log correlation using common libraries.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Logging and viewing logs in Cloud Run](https://docs.cloud.google.com/run/docs/logging)
  * [Logging and viewing logs in Knative serving](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/logging)
  * [View and write Cloud Run function logs](https://docs.cloud.google.com/functions/1stgendocs/monitoring/logging)
  * [Write and view logs](https://docs.cloud.google.com/appengine/docs/flexible/writing-application-logs)
  * [Write and view logs](https://docs.cloud.google.com/appengine/docs/standard/writing-application-logs)



## Code sample

### Go

To authenticate to Cloud Run, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    func init() {
    	// Disable log prefixes such as the default timestamp.
    	// Prefix text prevents the message from being parsed as JSON.
    	// A timestamp is added when shipping logs to Cloud Logging.
    	log.SetFlags(0)
    }
    
    func indexHandler(w http.ResponseWriter, r *http.Request) {
    	// Uncomment and populate this variable in your code:
    	// projectID = "The project ID of your Cloud Run service"
    
    	// Derive the traceID associated with the current request.
    	var trace string
    	if projectID != "" {
    		traceHeader := r.Header.Get("X-Cloud-Trace-Context")
    		traceParts := strings.Split(traceHeader, "/")
    		if len(traceParts) > 0 && len(traceParts[0]) > 0 {
    			trace = fmt.Sprintf("projects/%s/traces/%s", projectID, traceParts[0])
    		}
    	}
    
    	log.Println(Entry{
    		Severity:  "NOTICE",
    		Message:   "This is the default display field.",
    		Component: "arbitrary-property",
    		Trace:     trace,
    	})
    
    	fmt.Fprintln(w, "Hello Logger!")
    }
    

### Java

To authenticate to Cloud Run, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Add log correlation to nest all log messages beneath request log in Log Viewer.
    // TODO(developer): delete this code if you're creating a Cloud
    //                  Function and it is *NOT* triggered by HTTP.
    String traceHeader = req.headers("x-cloud-trace-context");
    if (traceHeader != null && project != null) {
      String trace = traceHeader.split("/")[0];
      MDC.put(
          "logging.googleapis.com/trace",
          String.format("projects/%s/traces/%s", project, trace));
    }
    // -- End log correlation code --
    
    // Create a structured log entry using MDC (Mapped Diagnostic Context) keys.
    // For instantiating the "logger" variable, see
    // https://cloud.google.com/run/docs/logging#run_manual_logging-java
    MDC.put("component", "arbitrary-property");
    
    logger.info("This is the default display field.");
    
    // Clear MDC at the end of the request to avoid resource leaks
    MDC.clear();

### Node.js

To authenticate to Cloud Run, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Uncomment and populate this variable in your code:
    // const project = 'The project ID of your function or Cloud Run service';
    
    // Build structured log messages as an object.
    const globalLogFields = {};
    
    // Add log correlation to nest all log messages beneath request log in Log Viewer.
    // (This only works for HTTP-based invocations where `req` is defined.)
    if (typeof req !== 'undefined') {
      const traceHeader = req.header('X-Cloud-Trace-Context');
      if (traceHeader && project) {
        const [trace] = traceHeader.split('/');
        globalLogFields['logging.googleapis.com/trace'] =
          `projects/${project}/traces/${trace}`;
      }
    }
    
    // Complete a structured log entry.
    const entry = Object.assign(
      {
        severity: 'NOTICE',
        message: 'This is the default display field.',
        // Log viewer accesses 'component' as 'jsonPayload.component'.
        component: 'arbitrary-property',
      },
      globalLogFields
    );
    
    // Serialize to a JSON string and output.
    console.log(JSON.stringify(entry));
    

### Python

To authenticate to Cloud Run, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # Uncomment and populate this variable in your code:
    # PROJECT = 'The project ID of your Cloud Run service';
    
    # Build structured log messages as an object.
    global_log_fields = {}
    
    # Add log correlation to nest all log messages.
    # This is only relevant in HTTP-based contexts, and is ignored elsewhere.
    # (In particular, non-HTTP-based Cloud Functions.)
    request_is_defined = "request" in globals() or "request" in locals()
    if request_is_defined and request:
        trace_header = request.headers.get("X-Cloud-Trace-Context")
    
        if trace_header and PROJECT:
            trace = trace_header.split("/")
            global_log_fields[
                "logging.googleapis.com/trace"
            ] = f"projects/{PROJECT}/traces/{trace[0]}"
    
    # Complete a structured log entry.
    entry = dict(
        severity="NOTICE",
        message="This is the default display field.",
        # Log viewer accesses 'component' as jsonPayload.component'.
        component="arbitrary-property",
        **global_log_fields,
    )
    
    print(json.dumps(entry))

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudrun). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
