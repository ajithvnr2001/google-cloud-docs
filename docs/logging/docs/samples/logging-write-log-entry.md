---
url: https://docs.cloud.google.com/logging/docs/samples/logging-write-log-entry/
title: Write structured logs \u00a0|\u00a0 Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:36:51.608913+00:00
---

# Write structured logs  |  Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/samples/logging-write-log-entry/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Samples ](https://docs.cloud.google.com/logging/docs/samples)



#  Write structured logs Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates how to write a log entry.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Using .NET logging frameworks or calling the API](https://docs.cloud.google.com/logging/docs/integrate/dotnet)



## Code sample

### C#

To learn how to install and use the client library for Logging, see [Logging client libraries](https://docs.cloud.google.com/logging/docs/reference/libraries). 

To authenticate to Logging, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    private void WriteLogEntry(string logId)
    {
        var client = LoggingServiceV2Client.Create();
        LogName logName = new LogName(s_projectId, logId);
        var jsonPayload = new Struct()
        {
            Fields =
            {
                { "name", Value.ForString("King Arthur") },
                { "quest", Value.ForString("Find the Holy Grail") },
                { "favorite_color", Value.ForString("Blue") }
            }
        };
        LogEntry logEntry = new LogEntry
        {
            LogNameAsLogName = logName,
            Severity = LogSeverity.Info,
            JsonPayload = jsonPayload
        };
        MonitoredResource resource = new MonitoredResource { Type = "global" };
        IDictionary<string, string> entryLabels = new Dictionary<string, string>
        {
            { "size", "large" },
            { "color", "blue" }
        };
        client.WriteLogEntries(logName, resource, entryLabels,
            new[] { logEntry }, _retryAWhile);
        Console.WriteLine($"Created log entry in log-id: {logId}.");
    }
    

### Go

To learn how to install and use the client library for Logging, see [Logging client libraries](https://docs.cloud.google.com/logging/docs/reference/libraries). 

To authenticate to Logging, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"log"
    
    	"cloud.google.com/go/logging"
    )
    
    func structuredWrite(projectID string) {
    	ctx := context.Background()
    	client, err := logging.NewClient(ctx, projectID)
    	if err != nil {
    		log.Fatalf("Failed to create logging client: %v", err)
    	}
    	defer client.Close()
    	const name = "log-example"
    	logger := client.Logger(name)
    	defer logger.[Flush](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/logging/latest/index.html#cloud_google_com_go_logging_Logger_Flush)() // Ensure the entry is written.
    
    	logger.[Log](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/logging/latest/index.html#cloud_google_com_go_logging_Logger_Log)(logging.[Entry](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/logging/latest/index.html#cloud_google_com_go_logging_Entry){
    		// Log anything that can be marshaled to JSON.
    		Payload: struct{ Anything string }{
    			Anything: "The payload can be any type!",
    		},
    		Severity: logging.[Debug](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/logging/latest/index.html#cloud_google_com_go_logging_Default_Debug_Info_Notice_Warning_Error_Critical_Alert_Emergency),
    	})
    }
    

### Java

To learn how to install and use the client library for Logging, see [Logging client libraries](https://docs.cloud.google.com/logging/docs/reference/libraries). 

To authenticate to Logging, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.[MonitoredResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.MonitoredResource.html);
    import com.google.cloud.logging.[LogEntry](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LogEntry.html);
    import com.google.cloud.logging.[Logging](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.html);
    import com.google.cloud.logging.[LoggingOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LoggingOptions.html);
    import com.google.cloud.logging.[Payload](https://docs.cloud.google.com/java/docs/reference/google-cloud-apigee-connect/latest/com.google.cloud.apigeeconnect.v1.Payload.html).JsonPayload;
    import com.google.cloud.logging.[Severity](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.Severity.html);
    import com.google.common.collect.ImmutableMap;
    import java.util.Collections;
    import java.util.Map;
    
    public class WriteLogEntry {
    
      public static void main([String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html)[] args) throws Exception {
        // TODO(developer): Optionally provide the logname as an argument
        [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) logName = args.length > 0 ? args[0] : "test-log";
    
        // Instantiates a client
        try ([Logging](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.html) logging = [LoggingOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LoggingOptions.html).getDefaultInstance().getService()) {
          Map<String, String> payload =
              ImmutableMap.of(
                  "name", "King Arthur", "quest", "Find the Holy Grail", "favorite_color", "Blue");
          [LogEntry](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LogEntry.html) entry =
              [LogEntry](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LogEntry.html).newBuilder(JsonPayload.of(payload))
                  .setSeverity([Severity](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.Severity.html).INFO)
                  .setLogName(logName)
                  .setResource([MonitoredResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.MonitoredResource.html).newBuilder("global").build())
                  .build();
    
          // Writes the log entry asynchronously
          logging.write(Collections.singleton(entry));
    
          // Optional - flush any pending log entries just before Logging is closed
          logging.flush();
        }
        System.out.printf("Wrote to %s\n", logName);
      }
    }

### PHP

To learn how to install and use the client library for Logging, see [Logging client libraries](https://docs.cloud.google.com/logging/docs/reference/libraries). 

To authenticate to Logging, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Logging\LoggingClient;
    use Google\Cloud\Logging\Logger;
    
    /** Write a log message via the Stackdriver Logging API.
     *
     * @param string $projectId The Google project ID.
     * @param string $loggerName The name of the logger.
     * @param string $message The log message.
     */
    function write_log($projectId, $loggerName, $message)
    {
        $logging = new LoggingClient(['projectId' => $projectId]);
        $logger = $logging->logger($loggerName, [
            'resource' => [
                'type' => 'gcs_bucket',
                'labels' => [
                    'bucket_name' => 'my_bucket'
                ]
            ]
        ]);
        $entry = $logger->entry($message, [
            'severity' => Logger::INFO
        ]);
        $logger->write($entry);
        printf("Wrote a log to a logger '%s'." . PHP_EOL, $loggerName);
    }

### Python

To learn how to install and use the client library for Logging, see [Logging client libraries](https://docs.cloud.google.com/logging/docs/reference/libraries). 

To authenticate to Logging, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def write_entry():
        """Demonstrates how to write log entries to Google Cloud using Python's standard logging library."""
        logging_client = google.cloud.logging.Client()
    
        # By default, logs route to projects/[PROJECT_ID]/logs/python
        # unless overridden by GCP or custom handlers.
        logging_client.setup_logging(log_level=logging.INFO)
    
        # Make a simple text log
        logging.info("Hello, world!")
    
        # Simple text log with severity.
        logging.warning("Goodbye, world!")
    
        # Prepare your structured data as a dictionary.
        json_log = {
            "name": "King Arthur",
            "quest": "Find the Holy Grail",
            "favorite_color": "Blue",
        }
    
        logging.info("This is a JSON log.", extra={"json_fields": json_log})
    
        # wait for threads to finish working on the background.
        time.sleep(5)
    
    

### Ruby

To learn how to install and use the client library for Logging, see [Logging client libraries](https://docs.cloud.google.com/logging/docs/reference/libraries). 

To authenticate to Logging, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/logging"
    
    logging = Google::Cloud::[Logging](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-logging/latest/Google-Cloud-Logging.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-logging/latest/Google-Cloud-Logging.html)
    
    entry = logging.[entry](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-logging/latest/Google-Cloud-Logging-Project.html)
    # payload = "The data you want to log"
    entry.[payload](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-logging/latest/Google-Cloud-Logging-Entry.html) = payload
    # log_name = "The name of the log to write to"
    entry.log_name = log_name
    entry.severity = :NOTICE
    entry.resource.type = "gae_app"
    entry.resource.labels[:module_id] = "default"
    entry.resource.labels[:version_id] = "20160101t163030"
    
    logging.write_entries entry
    puts "Wrote payload: #{entry.[payload](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-logging/latest/Google-Cloud-Logging-Entry.html)} to log: #{entry.log_name}"

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudlogging). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
