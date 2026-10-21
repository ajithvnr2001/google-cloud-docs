---
url: https://docs.cloud.google.com/functions/1stgendocs/monitoring/logging/
title: View and write Cloud Run function logs \u00a0|\u00a0 Cloud Run functions (1st gen) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:29:42.642820+00:00
---

# View and write Cloud Run function logs  |  Cloud Run functions (1st gen)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/1stgendocs/monitoring/logging/

If you are creating a new function, see the [Console Quickstart](https://cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. The content on this page only applies to existing legacy functions created with the Cloud Functions v1 API. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ 1st generation ](https://docs.cloud.google.com/functions/1stgendocs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/functions/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# View and write Cloud Run function logs

## Writing runtime logs

Cloud Run functions includes simple runtime logging by default. Logs written to `stdout` or `stderr` will appear automatically in the [Google Cloud console](https://console.cloud.google.com/project/_/logs?service=cloudfunctions.googleapis.com). For more advanced logging, use the Cloud Logging client libraries.

**Note:** There is typically a slight delay between when log entries are created and when they show up in Cloud Logging.

As a default, the log payload is a simple text string, as shown in the following snippets. The string is stored in the `textPayload` field of the log entry.

###  Node.js 
    
    
    const functions = require('@google-cloud/functions-framework');
    
    functions.http('helloWorld', (req, res) => {
      console.log('I am a log entry!');
      console.error('I am an error!');
      res.end();
    });

Most log entries do not have an associated log level. These include: 

  * Logs emitted using `console.log()`, `console.info()` , `console.warn()` or `console.error()`
  * Logs written directly to `stdout` or `stderr`



Internal system messages have the `DEBUG` log level. 

###  Python 
    
    
    def hello_world(data, context):
        """Background Cloud Function.
        Args:
             data (dict): The dictionary with data specific to the given event.
             context (google.cloud.functions.Context): The event metadata.
        """
        print("Hello, stdout!")
    
    

  * Logs to standard output or standard error do not have an associated log level.
  * Internal system messages have the `DEBUG` log level.



###  Go 
    
    
    // Package helloworld provides a set of Cloud Functions samples.
    package helloworld
    
    import (
    	"fmt"
    	"log"
    	"net/http"
    
    	"github.com/GoogleCloudPlatform/functions-framework-go/functions"
    )
    
    func init() {
    	functions.HTTP("HelloLogging", HelloLogging)
    }
    
    // HelloLogging logs messages.
    func HelloLogging(w http.ResponseWriter, r *http.Request) {
    	log.Println("This is stderr")
    	fmt.Println("This is stdout")
    
    	// Structured logging can be used to set severity levels.
    	// See https://cloud.google.com/logging/docs/structured-logging.
    	fmt.Println(`{"message": "This has ERROR severity", "severity": "error"}`)
    
    	// cloud.google.com/go/logging can optionally be used for additional options.
    }
    

  * Logs to `stdout` or `stderr` do not have an associated log level.
  * Internal system messages have the `DEBUG` log level.



###  Java 
    
    
    import com.google.cloud.functions.HttpFunction;
    import com.google.cloud.functions.HttpRequest;
    import com.google.cloud.functions.HttpResponse;
    import java.io.BufferedWriter;
    import java.io.IOException;
    import java.util.logging.Logger;
    
    public class LogHelloWorld implements HttpFunction {
    
      private static final Logger logger = Logger.getLogger(LogHelloWorld.class.getName());
    
      @Override
      public void service(HttpRequest request, HttpResponse response)
          throws IOException {
        System.out.println("I am a log to stdout!");
        System.err.println("I am a log to stderr!");
    
        logger.info("I am an info log!");
        logger.warning("I am a warning log!");
    
        BufferedWriter writer = response.getWriter();
        writer.write("Messages successfully logged!");
      }
    }

  * Logs to `stdout` or `stderr` do not have an associated log level.
  * Internal system messages have the `DEBUG` log level.



###  C# 
    
    
    using Google.Cloud.Functions.Framework;
    using Microsoft.AspNetCore.Http;
    using Microsoft.Extensions.Logging;
    using System;
    using System.Threading.Tasks;
    
    namespace LogHelloWorld;
    
    public class Function : IHttpFunction
    {
        private readonly ILogger _logger;
    
        public Function(ILogger<Function> logger) =>
            _logger = logger;
    
        public async Task HandleAsync(HttpContext context)
        {
            Console.WriteLine("I am a log to stdout!");
            Console.Error.WriteLine("I am a log to stderr!");
    
            _logger.LogInformation("I am an info log!");
            _logger.LogWarning("I am a warning log!");
    
            await context.Response.WriteAsync("Messages successfully logged!", context.RequestAborted);
        }
    }

  * Text written to `stdout` (for example, via `Console.WriteLine`) and `stderr` (for example, via `Console.Error.WriteLine`) do not have a log level.
  * ASP.NET Core logging levels are mapped to Cloud Logging levels as follows: 
    * `LogLevel.Trace` and `LogLevel.Debug map` to Cloud Logging `DEBUG`.
    * `LogLevel.Information` maps to Cloud Logging `INFO`.
    * `LogLevel.Warning` maps to Cloud Logging `WARNING`.
    * `LogLevel.Error` maps to Cloud Logging `ERROR`.
    * `LogLevel.Critical` maps to Cloud Logging `CRITICAL`.



###  Ruby 
    
    
    require "functions_framework"
    
    FunctionsFramework.http "log-helloworld" do |_request|
      # Any output sent to either stdout or stderr will be captured and written to
      # the function's logs.
      puts "Hello, stdout!"
      warn "Hello, stderr!"
    
      # Return the response body as a string.
      "Hello, world!"
    end

Log entries do not have an associated log level.

###  PHP 
    
    
    use Psr\Http\Message\ServerRequestInterface;
    
    function helloLogging(ServerRequestInterface $request): string
    {
        // Code running in Google Cloud Functions itself writes log entries to
        // Cloud Logging. (Default log severity level is INFO.)
        $log = fopen('php://stderr', 'wb');
        fwrite($log, "Log entry from fwrite().\n");
    
        // You can also specify a severity level explicitly using structured logs.
        // See this page for a list of log severity values:
        //   https://cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#LogSeverity
        fwrite($log, json_encode([
          'message' => 'Structured log with error severity',
          'severity' => 'error'
        ]) . PHP_EOL);
    
        // This will log to standard error, which will appear in Cloud Logging
        error_log('error_log logs in Cloud Functions!');
    
        // This will log an error message and immediately terminate the function execution
        // trigger_error('fatal errors are logged!');
    
        // For HTTP functions, this is added to the HTTP response
        // For CloudEvent functions, this does nothing
        var_dump('var_dump goes to HTTP response for HTTP functions');
    
        // You can also dump variables using var_export() and forward
        // the resulting string to Cloud Logging via an fwrite() call.
        $entry = var_export('var_export output can be captured.', true);
        fwrite($log, $entry);
    
        // Functions must return a String or PSR-7 Response object
        return '';
    }

### Writing structured logs

The default text logs described above do not have an associated log level. If you want to include log levels or other specific fields in your log entries, you can write logs to `stdout` or `stderr` in the form of a single line of serialized JSON. This line is picked up and parsed by Cloud Run functions and is placed into the `jsonPayload` field instead of `textPayload`. The snippets below demonstrate writing such structured logs.

**Note:** These snippets were originally written for Cloud Run. They are equally applicable to Cloud Run functions.

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

Structured logging support is available in Python 3.8 and later. 
    
    
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
    
    
    // Build structured log messages as an object.
    Object globalLogFields = null;
    
    // Add log correlation to nest all log messages beneath request log in Log Viewer.
    // TODO(developer): delete this code if you're creating a Cloud
    //                  Function and it is *NOT* triggered by HTTP.
    String traceHeader = req.headers("x-cloud-trace-context");
    if (traceHeader != null && project != null) {
      String trace = traceHeader.split("/")[0];
      globalLogFields =
          kv(
              "logging.googleapis.com/trace",
              String.format("projects/%s/traces/%s", project, trace));
    }
    // -- End log correlation code --
    
    // Create a structured log entry using key value pairs.
    // For instantiating the "logger" variable, see
    // https://cloud.google.com/run/docs/logging#run_manual_logging-java
    logger.error(
        "This is the default display field.",
        kv("component", "arbitrary-property"),
        kv("severity", "NOTICE"),
        globalLogFields);
    
    
    <configuration>
      <appender name="jsonConsoleAppender" class="ch.qos.logback.core.ConsoleAppender">
        <encoder class="net.logstash.logback.encoder.LogstashEncoder">
          <!-- Ignore default logging fields -->
          <fieldNames>
            <timestamp>[ignore]</timestamp>
            <version>[ignore]</version>
            <logger>[ignore]</logger>
            <thread>[ignore]</thread>
            <level>[ignore]</level>
            <levelValue>[ignore]</levelValue>
          </fieldNames>
        </encoder>
      </appender>
      <root level="INFO">
        <appender-ref ref="jsonConsoleAppender"/>
      </root>
    </configuration>
    

### Processing special JSON fields in messages

When you provide structured data as a JSON dictionary, some special fields are stripped from the `jsonPayload` and are written to the corresponding field in the generated [`LogEntry`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry), as described in the documentation for [special fields](https://docs.cloud.google.com/logging/docs/agent/configuration#special-fields).

For example, if your JSON includes a `severity` property, it is removed from the `jsonPayload` and appears instead as the log entry's `severity`. The `message` property is used as the main display text of the log entry if present.

### Writing logs using client libraries

[Cloud Logging client libraries](https://docs.cloud.google.com/logging/docs/reference/libraries) provide an alternative way to write logs. With these libraries you can use the standard logging mechanisms of your programming language and integrate with various supported logging frameworks. Client libraries also simplify population of the special JSON fields by automatically capturing some information and providing interfaces to appropriately populate the fields.

You can use client libraries to write logs with the Cloud Logging API synchronously or asynchronously. Some client libraries also support writing structured logs directly to `stdout` or `stderr`. Note that if you write logs asynchronously, unexpected function termination [might result in lost log entries](https://docs.cloud.google.com/functions/1stgendocs/troubleshooting#missing-logs). Also note that synchronous logging with the Logging API increases function execution time because it requires waiting for API calls to be completed.

## Viewing runtime logs

This section describes your options for viewing runtime logs.

### Using the command-line tool

Logs for Cloud Run functions are viewable in the Cloud Logging UI, and using the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud).

To view logs with the gcloud CLI, use the [`gcloud functions logs read`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/logs/read) command:
    
    
    gcloud functions logs read

To view the logs for a specific function, provide the function name as an argument:
    
    
    gcloud functions logs read FUNCTION_NAME

Use the following to view the logs for a specific execution:
    
    
    gcloud functions logs read FUNCTION_NAME --execution-id EXECUTION_ID

For the full range of log viewing options, see the documentation for [`gcloud functions logs read`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/logs/read).

### Using the Logging dashboard

You can also view runtime logs for Cloud Run functions in the [Google Cloud console](https://console.cloud.google.com/logs/query).

### Using the Logging API

Runtime logs can also be written and retrieved through the Cloud Logging API. The [Cloud Logging client libraries](https://docs.cloud.google.com/logging/docs/reference/libraries) provide an idiomatic interface to the Logging API:

###  Node.js 

For more information, see the [Node.js Client Library reference](https://docs.cloud.google.com/nodejs/docs/reference/logging/latest). 
    
    
    // Imports the Google Cloud client library
    const {Logging} = require('[@google-cloud/logging](https://docs.cloud.google.com/nodejs/docs/reference/logging/latest/overview.html)');
    
    // Creates a client
    const logging = new [Logging](https://docs.cloud.google.com/nodejs/docs/reference/logging/latest/logging/logging.html)();
    
    /**
     * TODO(developer): Uncomment the following line to run the code.
     */
    // const logName = 'Name of the log from which to list entries, e.g. my-log';
    
    const log = logging.log(logName);
    
    async function printEntryMetadata() {
      // List the most recent entries for a given log
      // See https://googleapis.dev/nodejs/logging/latest/Logging.html#getEntries
      const [entries] = await log.getEntries();
      console.log('Logs:');
      entries.forEach(entry => {
        const metadata = entry.metadata;
        console.log(`${metadata.timestamp}:`, metadata[metadata.payload]);
      });
    }
    printEntryMetadata();

###  Python 

For more information, see the [ Python Client Library reference](https://docs.cloud.google.com/python/docs/reference/logging/latest). 
    
    
    def list_entries(logger_name):
        """Lists the most recent entries for a given logger."""
        logging_client = logging.Client()
        logger = logging_client.logger(logger_name)
    
        print("Listing entries for logger {}:".format(logger.name))
    
        for entry in logger.list_entries():
            timestamp = entry.timestamp.isoformat()
            print("* {}: {}".format(timestamp, entry.payload))
    
    

###  Go 

For more information, see the [Go Client Library reference](https://godoc.org/cloud.google.com/go/logging). 
    
    
    import (
    	"context"
    	"fmt"
    	"log"
    	"time"
    
    	"cloud.google.com/go/logging"
    	"cloud.google.com/go/logging/logadmin"
    	"google.golang.org/api/iterator"
    )
    
    func getEntries(projectID string) ([]*logging.[Entry](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/logging/latest/index.html#cloud_google_com_go_logging_Entry), error) {
    	ctx := context.Background()
    	adminClient, err := logadmin.NewClient(ctx, projectID)
    	if err != nil {
    		log.Fatalf("Failed to create logadmin client: %v", err)
    	}
    	defer adminClient.Close()
    
    	var entries []*logging.[Entry](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/logging/latest/index.html#cloud_google_com_go_logging_Entry)
    	const name = "log-example"
    	lastHour := time.Now().Add(-1 * time.Hour).Format(time.RFC3339)
    
    	iter := adminClient.Entries(ctx,
    		// Only get entries from the "log-example" log within the last hour.
    		logadmin.Filter(fmt.Sprintf(`logName = "projects/%s/logs/%s" AND timestamp > "%s"`, projectID, name, lastHour)),
    		// Get most recent entries first.
    		logadmin.NewestFirst(),
    	)
    
    	// Fetch the most recent 20 entries.
    	for len(entries) < 20 {
    		entry, err := iter.Next()
    		if err == iterator.Done {
    			return entries, nil
    		}
    		if err != nil {
    			return nil, err
    		}
    		entries = append(entries, entry)
    	}
    	return entries, nil
    }
    

###  Java 

For more information, see the [ Java Client Library reference](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/overview). 
    
    
    import com.google.api.gax.paging.[Page](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.paging.Page.html);
    import com.google.cloud.logging.[LogEntry](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LogEntry.html);
    import com.google.cloud.logging.[Logging](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.html);
    import com.google.cloud.logging.[Logging](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.html).[EntryListOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.EntryListOption.html);
    import com.google.cloud.logging.[LoggingOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LoggingOptions.html);
    import java.text.DateFormat;
    import java.text.SimpleDateFormat;
    import java.util.Calendar;
    import java.util.TimeZone;
    
    public class ListLogEntries {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace the variable value with valid log name before running the sample
        // or provide it as an argument.
        String logName = args.length > 0 ? args[0] : "test-log";
    
        try ([Logging](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.html) logging = [LoggingOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LoggingOptions.html).[getDefaultInstance](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LoggingOptions.html#com_google_cloud_logging_LoggingOptions_getDefaultInstance__)().getService()) {
    
          // When composing a filter, using indexed fields, such as timestamp, resource.type, logName
          // and
          // others can help accelerate the results
          // Full list of indexed fields here:
          // https://cloud.google.com/logging/docs/view/advanced-queries#finding-quickly
          // This sample restrict the results to only last minute to minimize number of API calls
          Calendar calendar = Calendar.getInstance(TimeZone.getTimeZone("UTC"));
          calendar.add(Calendar.MINUTE, -1);
          DateFormat rfc3339 = new SimpleDateFormat("yyyy-MM-dd'T'HH:mm:ss.SSS'Z'");
          String logFilter =
              "logName=projects/"
                  + logging.[getOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.testing.RemoteLoggingHelper.html#com_google_cloud_logging_testing_RemoteLoggingHelper_getOptions__)().getProjectId()
                  + "/logs/"
                  + logName
                  + " AND timestamp>=\""
                  + rfc3339.format(calendar.getTime())
                  + "\"";
    
          // List all log entries
          Page<LogEntry> entries = logging.listLogEntries([EntryListOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.EntryListOption.html).filter(logFilter));
          while (entries != null) {
            for ([LogEntry](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LogEntry.html) logEntry : entries.iterateAll()) {
              System.out.println(logEntry);
            }
            entries = entries.getNextPage();
          }
        }
      }
    }

###  C# 
    
    
    private void ListLogEntries(string logId)
    {
        var client = LoggingServiceV2Client.Create();
        LogName logName = new LogName(s_projectId, logId);
        ProjectName projectName = new ProjectName(s_projectId);
        var results = client.ListLogEntries(Enumerable.Repeat(projectName, 1), $"logName={logName.ToString()}",
            "timestamp desc", callSettings: _retryAWhile);
        foreach (var row in results)
        {
            Console.WriteLine($"{row.TextPayload.Trim()}");
        }
    }

###  Ruby 
    
    
    require "google/cloud/logging"
    
    # log_name = "my_log_name"
    logging = Google::Cloud::[Logging](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-logging-v2/latest/Google-Cloud-Logging.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-logging/latest/Google-Cloud-Logging.html)
    entries = logging.entries filter: "logName:#{log_name}",
                              max:    1000,
                              order:  "timestamp desc"
    
    entries.each do |entry|
      puts "[#{entry.timestamp}] #{entry.log_name} #{entry.[payload](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-logging/latest/Google-Cloud-Logging-Entry.html).inspect}"
    end

###  PHP 
    
    
    use Google\Cloud\Logging\LoggingClient;
    
    /**
     * Print the timestamp and entry for the project and logger.
     *
     * @param string $projectId The Google project ID.
     * @param string $loggerName The name of the logger.
     */
    function list_entries($projectId, $loggerName)
    {
        $logging = new LoggingClient(['projectId' => $projectId]);
        $loggerFullName = sprintf('projects/%s/logs/%s', $projectId, $loggerName);
        $oneDayAgo = date(\DateTime::RFC3339, strtotime('-24 hours'));
        $filter = sprintf(
            'logName = "%s" AND timestamp >= "%s"',
            $loggerFullName,
            $oneDayAgo
        );
        $options = [
            'filter' => $filter,
        ];
        $entries = $logging->entries($options);
    
        // Print the entries
        foreach ($entries as $entry) {
            /* @var $entry \Google\Cloud\Logging\Entry */
            $entryInfo = $entry->info();
            if (isset($entryInfo['textPayload'])) {
                $entryText = $entryInfo['textPayload'];
            } else {
                $entryPayload = [];
                foreach ($entryInfo['jsonPayload'] as $key => $value) {
                    $entryPayload[] = "$key: $value";
                }
                $entryText = '{' . implode(', ', $entryPayload) . '}';
            }
            printf('%s : %s' . PHP_EOL, $entryInfo['timestamp'], $entryText);
        }
    }

For additional logging options for Java, see [Java Logging](https://docs.cloud.google.com/functions/1stgendocs/concepts/java-logging).

**Note:** To write or access Cloud Run functions logs, a principal must also have the appropriate logging permissions. See the Cloud Logging [Access control guide](https://docs.cloud.google.com/logging/docs/access-control) for more information.

## Responding to runtime logs

You can respond to Cloud Logging events by forwarding their logs to a Cloud Run function. For more information, see the [Second-Party Triggers with Cloud Logging](https://docs.cloud.google.com/functions/1stgendocs/calling/logging) page.

## Viewing build image logs

You can also see the logs for the [build image](https://docs.cloud.google.com/functions/1stgendocs/building) step of the deployment process. Follow the link for more information.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-19 UTC."],[],[]] 
