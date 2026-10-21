---
url: https://docs.cloud.google.com/logging/docs/samples/logging-quickstart/
title: Logging quickstart \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:36:52.037789+00:00
---

# Logging quickstart  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/samples/logging-quickstart/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Samples ](https://docs.cloud.google.com/logging/docs/samples)



#  Logging quickstart Stay organized with collections  Save and categorize content based on your preferences. 

Demonstration of how to write a log entry.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Logging client libraries](https://docs.cloud.google.com/logging/docs/reference/libraries)



## Code sample

### C#

To learn how to install and use the client library for Logging, see [Logging client libraries](https://docs.cloud.google.com/logging/docs/reference/libraries). 

To authenticate to Logging, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using System;
    // Imports the Google Cloud Logging client library
    using [Google.Cloud.Logging.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/latest/Google.Cloud.Logging.V2.html);
    using [Google.Cloud.Logging.Type](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.Type/latest/Google.Cloud.Logging.Type.html);
    using System.Collections.Generic;
    using [Google.Api](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.html);
    
    namespace GoogleCloudSamples
    {
        public class QuickStart
        {
            public static void Main(string[] args)
            {
                // Your Google Cloud Platform project ID.
                string projectId = "YOUR-PROJECT-ID";
    
                // Instantiates a client.
                var client = [LoggingServiceV2Client](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/latest/Google.Cloud.Logging.V2.LoggingServiceV2Client.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/latest/Google.Cloud.Logging.V2.LoggingServiceV2Client.html#Google_Cloud_Logging_V2_LoggingServiceV2Client_Create)();
    
                // Prepare new log entry.
                [LogEntry](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/latest/Google.Cloud.Logging.V2.LogEntry.html) logEntry = new [LogEntry](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/latest/Google.Cloud.Logging.V2.LogEntry.html)();
                string logId = "my-log";
                [LogName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/latest/Google.Cloud.Logging.V2.LogName.html) logName = new [LogName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/latest/Google.Cloud.Logging.V2.LogName.html)(projectId, logId);
                logEntry.[LogNameAsLogName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/latest/Google.Cloud.Logging.V2.LogEntry.html#Google_Cloud_Logging_V2_LogEntry_LogNameAsLogName) = logName;
                logEntry.[Severity](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/latest/Google.Cloud.Logging.V2.LogEntry.html#Google_Cloud_Logging_V2_LogEntry_Severity) = [LogSeverity](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.Type/latest/Google.Cloud.Logging.Type.LogSeverity.html).[Info](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.Type/latest/Google.Cloud.Logging.Type.LogSeverity.html#Google_Cloud_Logging_Type_LogSeverity_Info);
    
                // Create log entry message.
                string message = "Hello World!";
                string messageId = DateTime.Now.Millisecond.ToString();
                Type myType = typeof(QuickStart);
                string entrySeverity = logEntry.[Severity](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/latest/Google.Cloud.Logging.V2.LogEntry.html#Google_Cloud_Logging_V2_LogEntry_Severity).ToString().ToUpper();
                logEntry.[TextPayload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/latest/Google.Cloud.Logging.V2.LogEntry.html#Google_Cloud_Logging_V2_LogEntry_TextPayload) =
                    $"{messageId} {entrySeverity} {myType.Namespace}.LoggingSample - {message}";
    
                // Set the resource type to control which GCP resource the log entry belongs to.
                // See the list of resource types at:
                // https://cloud.google.com/logging/docs/api/v2/resource-list
                // This sample uses resource type 'global' causing log entries to appear in the 
                // "Global" resource list of the Developers Console Logs Viewer:
                //  https://console.cloud.google.com/logs/viewer
                [MonitoredResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.MonitoredResource.html) resource = new [MonitoredResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.MonitoredResource.html)
                {
                    Type = "global"
                };
    
                // Create dictionary object to add custom labels to the log entry.
                IDictionary<string, string> entryLabels = new Dictionary<string, string>();
                entryLabels.[Add](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Requests.Parameters.ParameterCollection.html#Google_Apis_Requests_Parameters_ParameterCollection_Add_System_String_System_String_)("size", "large");
                entryLabels.[Add](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Requests.Parameters.ParameterCollection.html#Google_Apis_Requests_Parameters_ParameterCollection_Add_System_String_System_String_)("color", "red");
    
                // Add log entry to collection for writing. Multiple log entries can be added.
                IEnumerable<LogEntry> logEntries = new [LogEntry](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/latest/Google.Cloud.Logging.V2.LogEntry.html)[] { logEntry };
    
                // Write new log entry.
                client.WriteLogEntries(logName, resource, entryLabels, logEntries);
    
                Console.WriteLine("Log Entry created.");
            }
        }
    }
    

### Go

To learn how to install and use the client library for Logging, see [Logging client libraries](https://docs.cloud.google.com/logging/docs/reference/libraries). 

To authenticate to Logging, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Sample logging-quickstart writes a log entry to Cloud Logging.
    package main
    
    import (
    	"context"
    	"fmt"
    	"log"
    
    	"cloud.google.com/go/logging"
    )
    
    func main() {
    	ctx := context.Background()
    
    	// Sets your Google Cloud Platform project ID.
    	projectID := "YOUR_PROJECT_ID"
    
    	// Creates a client.
    	client, err := logging.NewClient(ctx, projectID)
    	if err != nil {
    		log.Fatalf("Failed to create client: %v", err)
    	}
    
    	// Sets the name of the log to write to.
    	logName := "my-log"
    
    	// Selects the log to write to.
    	logger := client.Logger(logName)
    
    	// Sets the data to log.
    	text := "Hello, world!"
    
    	// Adds an entry to the log buffer.
    	logger.[Log](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/logging/latest/index.html#cloud_google_com_go_logging_Logger_Log)(logging.[Entry](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/logging/latest/index.html#cloud_google_com_go_logging_Entry){Payload: text})
    
    	// Closes the client and flushes the buffer to the Cloud Logging
    	// service.
    	if err := client.Close(); err != nil {
    		log.Fatalf("Failed to close client: %v", err)
    	}
    
    	fmt.Printf("Logged: %v\n", text)
    }
    

### Java

To learn how to install and use the client library for Logging, see [Logging client libraries](https://docs.cloud.google.com/logging/docs/reference/libraries). 

To authenticate to Logging, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.[MonitoredResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.MonitoredResource.html);
    import com.google.cloud.logging.[LogEntry](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LogEntry.html);
    import com.google.cloud.logging.[Logging](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.html);
    import com.google.cloud.logging.[LoggingOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LoggingOptions.html);
    import com.google.cloud.logging.[Payload](https://docs.cloud.google.com/java/docs/reference/google-cloud-apigee-connect/latest/com.google.cloud.apigeeconnect.v1.Payload.html).StringPayload;
    import com.google.cloud.logging.[Severity](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.Severity.html);
    import java.util.Collections;
    
    /**
     * This sample demonstrates writing logs using the Cloud Logging API. The library also offers a
     * java.util.logging Handler `com.google.cloud.logging.LoggingHandler` Logback integration is also
     * available :
     * https://github.com/googleapis/google-cloud-java/tree/master/google-cloud-clients/google-cloud-contrib/google-cloud-logging-logback
     * Using the java.util.logging handler / Logback appender should be preferred to using the API
     * directly.
     */
    public class QuickstartSample {
    
      /** Expects a new or existing Cloud log name as the first argument. */
      public static void main([String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html)... args) throws Exception {
        // The name of the log to write to
        [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) logName = args[0]; // "my-log";
        [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) textPayload = "Hello, world!";
    
        // Instantiates a client
        try ([Logging](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.html) logging = [LoggingOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LoggingOptions.html).getDefaultInstance().getService()) {
    
          [LogEntry](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LogEntry.html) entry =
              [LogEntry](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LogEntry.html).newBuilder(StringPayload.of(textPayload))
                  .setSeverity([Severity](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.Severity.html).ERROR)
                  .setLogName(logName)
                  .setResource([MonitoredResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.MonitoredResource.html).newBuilder("global").build())
                  .build();
    
          // Writes the log entry asynchronously
          logging.write(Collections.singleton(entry));
    
          // Optional - flush any pending log entries just before Logging is closed
          logging.flush();
        }
        System.out.printf("Logged: %s%n", textPayload);
      }
    }

### PHP

To learn how to install and use the client library for Logging, see [Logging client libraries](https://docs.cloud.google.com/logging/docs/reference/libraries). 

To authenticate to Logging, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # Includes the autoloader for libraries installed with composer
    require __DIR__ . '/vendor/autoload.php';
    
    # Imports the Google Cloud client library
    use Google\Cloud\Logging\LoggingClient;
    
    # Your Google Cloud Platform project ID
    $projectId = 'YOUR_PROJECT_ID';
    
    # Instantiates a client
    $logging = new LoggingClient([
        'projectId' => $projectId
    ]);
    
    # Selects the log to write to
    $logger = $logging->logger('my-log');
    
    # The data to log
    $text = 'Hello, world!';
    
    # Creates and writes the log entry
    $entry = $logger->entry($text);
    $logger->write($entry);
    
    echo 'Logged ' . $text;

### Python

To learn how to install and use the client library for Logging, see [Logging client libraries](https://docs.cloud.google.com/logging/docs/reference/libraries). 

To authenticate to Logging, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # Imports the Google Cloud client library
    from google.cloud import logging
    
    # Instantiates a client
    logging_client = logging.[Client](https://docs.cloud.google.com/python/docs/reference/logging/latest/google.cloud.logging_v2.client.Client.html)()
    
    # The name of the log to write to
    log_name = "my-log"
    # Selects the log to write to
    logger = logging_client.[logger](https://docs.cloud.google.com/python/docs/reference/logging/latest/google.cloud.logging_v2.client.Client.html#google_cloud_logging_v2_client_Client_logger)(log_name)
    
    # The data to log
    text = "Hello, world!"
    
    # Writes the log entry
    logger.log_text(text)
    
    print("Logged: {}".format(text))

### Ruby

To learn how to install and use the client library for Logging, see [Logging client libraries](https://docs.cloud.google.com/logging/docs/reference/libraries). 

To authenticate to Logging, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # Imports the Google Cloud client library
    require "google/cloud/logging"
    
    # Instantiates a client
    logging = Google::Cloud::[Logging](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-logging/latest/Google-Cloud-Logging.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-logging/latest/Google-Cloud-Logging.html)
    
    # Prepares a log entry
    entry = logging.[entry](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-logging/latest/Google-Cloud-Logging-Project.html)
    # payload = "The data you want to log"
    entry.[payload](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-logging/latest/Google-Cloud-Logging-Entry.html) = payload
    # log_name = "The name of the log to write to"
    entry.log_name = log_name
    # The resource associated with the data
    entry.resource.type = "global"
    
    # Writes the log entry
    logging.write_entries entry
    
    puts "Logged #{entry.[payload](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-logging/latest/Google-Cloud-Logging-Entry.html)}"

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudlogging). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
