---
url: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/logging/
title: Logging and viewing logs in Knative serving \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:03:57.505764+00:00
---

# Logging and viewing logs in Knative serving  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Knative serving ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/architecture-overview)



Send feedback 

#  Logging and viewing logs in Knative serving Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the logs available when using Knative serving, and how to view and write logs.

Knative serving has two types of logs:

  * Request logs: logs of requests sent to Knative serving services. These logs are created automatically.
  * Container logs: logs emitted from the container instances, typically from your own code, written to supported locations as described in Writing container logs.



## Enabling logs

For Google Cloud logs are automatically sent to [Cloud Logging](https://docs.cloud.google.com/logging/docs). For Google Distributed Cloud, [you must first enable logs](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/how-to/application-logging-monitoring#enabling_and_for_user_applications).

## Viewing logs

You can view logs for your service in a couple of ways:

  * Use the Knative serving page in the Google Cloud console
  * Use Cloud Logging Logs Explorer in the Google Cloud console.



Both of these viewing methods examine the same logs stored in Cloud Logging, but the Cloud Logging Logs Explorer provides more details and more filtering capabilities.

### Viewing logs in Knative serving

To view logs in the Knative serving page:

  1. [Go to Knative serving](https://console.cloud.google.com/kubernetes/run)

  2. Click the desired service in the displayed list.

  3. Click the **LOGS** tab to get the request and container logs for all revisions of this service. You can filter by log severity level.




### Viewing logs in Cloud Logging

To view your Knative serving logs in the Cloud Logging Logs Explorer:

  1. Go to the Logs Explorer page in the Google Cloud console.

  2. Select an existing Google Cloud project at the top of the page, or create a new project.

  3. Using the drop-down menus, select the resource: **Kubernetes Container**.




For more information, see [Using the Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface).

### Viewing logs in Cloud Code

To view your logs in [Cloud Code](https://docs.cloud.google.com/code/docs), read the [IntelliJ](https://docs.cloud.google.com/code/docs/intellij/viewing-cloud-run-logs) and [Visual Studio Code](https://docs.cloud.google.com/code/docs/vscode/logging#cloud_run_logs) guides.

### Reading logs programmatically

If you want to read the logs programmatically, you can use one of these methods:

  * Use a [log sink to Pub/Sub and a script to pull from Pub/Sub](https://docs.cloud.google.com/logging/docs/export).
  * Call the Logging API through the [Client Libraries](https://docs.cloud.google.com/logging/docs/reference/libraries) for your programming language.
  * Call the [Logging API REST endpoints](https://docs.cloud.google.com/logging/docs/reference/v2/rest) directly.



## Writing container logs

When you write logs from your service, they will be picked up automatically by Cloud Logging so long as the logs are written to any of these locations:

  * [Standard output (`stdout`) or standard error (`stderr`) streams](https://en.wikipedia.org/wiki/Standard_streams)
  * syslog (`/dev/log`)
  * Logs written using [Cloud Logging client libraries](https://docs.cloud.google.com/logging/docs/reference/libraries), which are available for many popular languages



Most developers are expected to write logs using standard output and standard error.

The container logs written to these supported locations are automatically associated with the Knative serving service, revision, and location.

### Using simple text vs structured JSON in logs

When you write logs, you can send a simple text string or send a single line of serialized JSON, also called "structured" data. This is picked up and parsed by Cloud Logging and is placed into `jsonPayload`. In contrast, the simple text message is placed in `textPayload`.

### Writing structured logs

The following snippet shows how to write structured log entries. It also shows how to correlate log messages with the corresponding request log.

###  Node.js 
    
    
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
    

###  Python 
    
    
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

###  Go 

The structure for each log entry is provided by an `Entry` type: 
    
    
    // Entry defines a log entry.
    type Entry struct {
    	Message  string `json:"message"`
    	Severity string `json:"severity,omitempty"`
    	Trace    string `json:"logging.googleapis.com/trace,omitempty"`
    
    	// Logs Explorer allows filtering and display of this as `jsonPayload.component`.
    	Component string `json:"component,omitempty"`
    }
    
    // String renders an entry structure to the JSON format expected by Cloud Logging.
    func (e Entry) String() string {
    	if e.Severity == "" {
    		e.Severity = "INFO"
    	}
    	out, err := json.Marshal(e)
    	if err != nil {
    		log.Printf("json.Marshal: %v", err)
    	}
    	return string(out)
    }
    

When an Entry struct is logged, the `String` method is called to marshal it to the JSON format expected by Cloud Logging: 
    
    
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
    

###  Java 

Enable JSON logging with [Logback](http://logback.qos.ch/) and [SLF4J](http://www.slf4j.org/) by enabling the [Logstash JSON Encoder](https://github.com/logstash/logstash-logback-encoder) in your `logback.xml` configuration. 
    
    
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
    
    
    <configuration>
      <appender name="CLOUD" class="com.google.cloud.logging.logback.LoggingAppender">
        <!-- Optional : filter logs at or above a level -->
        <filter class="ch.qos.logback.classic.filter.ThresholdFilter">
          <level>INFO</level>
        </filter>
        <log>application.log</log> <!-- Optional : default java.log -->
        <resourceType>gae_app</resourceType> <!-- Optional : default: auto-detected, fallback: global -->
        <enhancer>com.example.logging.logback.enhancers.ExampleEnhancer</enhancer> <!-- Optional -->
        <flushLevel>WARN</flushLevel> <!-- Optional : default ERROR -->
        <!-- Redirect logs to stdout in JSON format for Cloud Run to capture -->
        <redirectToStdout>true</redirectToStdout>
      </appender>
      <root level="INFO">
        <appender-ref ref="CLOUD"/>
      </root>
    </configuration>
    

### Special JSON fields in messages

When you provide a structured log as a JSON dictionary, some special fields are stripped from the `jsonPayload` and are written to the corresponding field in the generated [LogEntry](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) as described in the documentation for [special fields](https://docs.cloud.google.com/logging/docs/agent/configuration#special-fields).

For example, if your JSON includes a `severity` property, it is removed from the `jsonPayload` and appears instead as the log entry's `severity`. The `message` property is used as the main display text of the log entry if present. For more on special properties read the Logging Resource section below.

### Correlating your container logs with a request log

In the Logs Explorer, logs correlated by the same `trace` are viewable in "parent-child" format: when you click on the triangle icon at the left of the request log entry, the container logs related to that request show up nested under the request log.

Container logs are not automatically correlated to request logs unless you use a [Cloud Logging client library](https://docs.cloud.google.com/logging/docs/reference/libraries). To correlate container logs with request logs without using a client library, you can use a structured JSON log line that contains a `logging.googleapis.com/trace` field with the trace identifier extracted from the `X-Cloud-Trace-Context` header as shown in the above sample for structured logging.

## Controlling request log resource usage

Request logs are created automatically. Although you cannot control the amount of request logs directly from Knative serving, you can make use of the [logs exclusion](https://docs.cloud.google.com/logging/docs/routing/overview#exclusions) feature from Cloud Logging.

## A note about logging agents

If you've used Cloud Logging with certain Google Cloud products, such as Compute Engine, you may have used Cloud Logging logging agents. Knative serving does not use logging agents because it has built-in support for log collection.

## Logging resource

Clicking on a log entry in the Logs Explorer opens up a JSON formatted log entry so you can drill down to the details you want.

All of the fields in a log entry, such as timestamps, severity, and `httpRequest` are standard, and are described in the documentation for a [log entry](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry).

However, there are some labels or resource labels that are special to Knative serving. These are listed here with sample contents:
    
    
    {
     httpRequest: {…}
     insertId:  "5c82b3d1000ece0000000000"
     labels: {
      instanceId:  "00bf4bf00000fb59c906a00000c9e29c2c4e06dce91500000000056008d2b6460f163c0057b97b2345f2725fb2423ee5f0bafd36df887fdb1122371563cf1ff453717282afe000001"
     }
     logName:  "projects/my-project/logs/kubernetes-engine/enterprise/knative-serving/.googleapis.com%2Frequests"
     receiveTimestamp:  "2019-03-08T18:26:25.981686167Z"
     resource: {
      labels: {
       configuration_name:  "myservice"
       location:  "us-central1"
       project_id:  "my-project"
       revision_name:  "myservice-00002"
       service_name:  "myservice"
      }
      type:  "cloud_run_revision"
     }
     severity:  "INFO"
     timestamp:  "2019-03-08T18:26:25.970397Z"
    }
    

Field | Values and notes  
---|---  
`instanceId` | The container instance that handled the request.  
`logName` | Identifies the log, for example, request log, standard error, standard output, etc.  
`configuration_name` | The Configuration resource that created the revision that served the request.  
`location` | Identifies the GCP location of the service.  
`project_id` | The project the service is deployed to.  
`revision_name` | The revision that served the request.  
`service_name` | The service that served the request.  
`type` | `cloud_run_revision`. The Knative serving resource type.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
