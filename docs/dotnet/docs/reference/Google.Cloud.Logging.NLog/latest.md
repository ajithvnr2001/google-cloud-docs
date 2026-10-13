---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.NLog/latest/
title: Google.Cloud.Logging.NLog \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:06:33.427816+00:00
---

# Google.Cloud.Logging.NLog  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.NLog/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google.Cloud.Logging.NLog Stay organized with collections  Save and categorize content based on your preferences. 

6.1.0 (latest)  6.0.0  5.2.0  5.1.0  5.0.0  4.0.0  3.3.0 

`Google.Cloud.Logging.NLog` is a .NET client library to integrate [Google Stackdriver Logging](https://cloud.google.com/logging/) with [NLog](http://nlog-project.org/).

Note: This documentation is for version `6.1.0` of the library. Some samples may not work with other versions.

## Installation

Install the `Google.Cloud.Logging.NLog` package from NuGet. Add it to your project in the normal way (for example by right-clicking on the project in Visual Studio and choosing "Manage NuGet Packages...").

## Authentication

When running on Google Cloud, no action needs to be taken to authenticate.

Otherwise, the simplest way of authenticating your API calls is to set up Application Default Credentials. The credentials will automatically be used to authenticate. See [Set up Application Default Credentials](https://cloud.google.com/docs/authentication/provide-credentials-adc) for more details.

## Getting started

## Console app

Create an `nlog` configuration file (`nlog.xml`):
    
    
    <?xml version="1.0" encoding="utf-8" ?>
    <nlog xmlns="http://www.nlog-project.org/schemas/NLog.xsd"
          xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
    
      <extensions>
        <add assembly="Google.Cloud.Logging.NLog" />
      </extensions>
      
      <targets async="true">
        <target name="stackdriver" xsi:type="GoogleStackdriver" projectId="PROJECT_ID" logId="LOG_ID">
          <!-- Potentially additional configuration -->
        </target>
        <target name="console" xsi:type="Console" />
      </targets>
    
      <rules>
        <logger name="*" minlevel="Info" writeTo="stackdriver" />
        <logger name="*" minlevel="Info" writeTo="console" />
      </rules>
      
    </nlog>
    

Edit the file replacing `PROJECT_ID` with your Google Cloud Project ID, and `LOG_ID` with an identifier for your application.

Ensure the file is copied to the output directory. For example, in your project file you might include:
    
    
    <None Update="nlog.xml" CopyToOutputDirectory="Always" />
    

Use this file to configure NLog and then log as normal:
    
    
    // Configure nlog to use Google Stackdriver logging from the XML configuration file.
    LogManager.Setup().LoadConfigurationFromFile("nlog.xml", optional: false);
    
    // Acquire a logger for this class
    Logger logger = LogManager.GetCurrentClassLogger();
    // Log some information. This log entry will be sent to Google Stackdriver Logging.
    logger.Info("An exciting log entry!");
    
    // Flush buffered log entries before program exit; then shutdown the logger before program exit.
    LogManager.Flush(TimeSpan.FromSeconds(15));
    LogManager.Shutdown();
    

If executing on [Google App Engine (GAE)](https://cloud.google.com/appengine/), [Google Kubernetes Engine (GKE)](https://cloud.google.com/kubernetes-engine/), or [Google Compute Engine (GCE)](https://cloud.google.com/compute/), then the `projectId="PROJECT_ID"` configuration setting can be omitted; it will be auto-detected from the platform at run-time.

## Configuration options

  * `ProjectId` \- Google Cloud project ID where logs will be sent to. Can be omitted if executing on on [Google App Engine (GAE)](https://cloud.google.com/appengine/) or [Google Compute Engine (GCE)](https://cloud.google.com/compute/)
  * `LogId` \- Name of log under the resource type (Default = "Default")
  * `DisableResourceTypeDetection` \- Defaults to false. Setting this to true disables automatic resource type detection based on platform detection.
  * `ResourceType` \- Resource type for logs. Must be one of the supported types listed in the [cloud logging documentation](https://cloud.google.com/logging/docs/api/v2/resource-list). This is not needed if resource type detection is successful. If resource type detection fails or is disabled, and this is not set, the resource type in log entries is set to "global".
  * `ResourceLabel` \- Used to specify extra labels as shown in the [Monitoring Resource Types](https://cloud.google.com/logging/docs/api/v2/resource-list) list.
  * `ContextProperty` \- Allows custom labels to be added to the log entries as extra metadata.
  * `CredentialFile` \- Credentials using a JSON file, instead of using the application default credentials
  * `CredentialJson` \- Credentials using raw JSON input, instead of using the application default credentials
  * `CredentialType` \- Specifies the type of credential being used (Default = "service_account"). The value must be a valid type as defined on [JsonCredentialParameters](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.JsonCredentialParameters); possible values include "service_account", "authorized_user", "external_account", and "impersonated_service_account".
  * `IncludeCallSite` \- Include `LogEntrySourceLocation` extracted from NLog callsite. (This only includes the function name.)
  * `IncludeCallSiteStackTrace` \- Include `LogEntrySourceLocation` extracted from NLog callsite. (This also includes file name and line number.)
  * `IncludeEventProperties` \- Includes structured logging properties from NLog `LogEventInfo.Properties`.
  * `IncludeMdlc` \- Include async thread context properties from NLog MappedDiagnosticsLogicalContext
  * `SendJsonPayload` \- Use the `jsonPayload` property in log entries instead of `textPayload`. When this is enabled, properties are set within the payload instead of as custom labels
  * `ServiceContextName` \- Configures the "service" in "serviceContext" when sending a JSON payload. (Defaults to the `AppDomain.FriendlyName` of the running code.)
  * `ServiceContextVersion` \- Configures the "version" in "serviceContext" when sending a JSON payload. (Defaults to the `FileVersion` of the entry assembly.)
  * `EnableJsonLayout` \- Uses NLog's native JSON layout to format JSON payloads, completely replacing the default layout.
  * `JsonConverter` or `JsonConverterTypeName`/`JsonConverterMethodName` \- Configures a custom conversion for individual values within a JSON payload.
  * `TraceId` \- The trace ID to associate to log entries. Ex: `06796866738c859f2f19b7cfb3214824`. See [Google Logging V2 LogEntry reference docs](https://cloud.google.com/logging/docs/reference/v2/rpc/google.logging.v2#google.logging.v2.LogEntry) for more information.
  * `SpanId` \- The span ID within the trace associated with the log entry. Trace API v2 uses a 16-character hexadecimal encoding of an 8-byte array, ex: `000000000000004a`. See [Google Logging V2 LogEntry reference docs](https://cloud.google.com/logging/docs/reference/v2/rpc/google.logging.v2#google.logging.v2.LogEntry) for more information.
  * `TraceSampled` \- The sampling decision of the trace associated with the log entry. See [Google Logging V2 LogEntry reference docs](https://cloud.google.com/logging/docs/reference/v2/rpc/google.logging.v2#google.logging.v2.LogEntry) for more information.



## Sending JsonPayload

Enabling `SendJsonPayload` will capture structured logging properties in JSON format (instead of saving them as resource labels).
    
    
    <?xml version="1.0" encoding="utf-8" ?>
    <nlog xmlns="http://www.nlog-project.org/schemas/NLog.xsd"
          xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
    
      <extensions>
        <add assembly="Google.Cloud.Logging.NLog" />
      </extensions>
      
      <targets async="true">
        <target name="stackdriver" xsi:type="GoogleStackdriver" projectId="PROJECT_ID" logId="LOG_ID" includeEventProperties="true" sendJsonPayload="true">
          <contextproperty name="exception" layout="${exception:format=tostring}" />  <!-- Optional and repeatable -->
        </target>
        <target name="console" xsi:type="Console" />
      </targets>
    
      <rules>
        <logger name="*" minlevel="Info" writeTo="stackdriver" />
        <logger name="*" minlevel="Info" writeTo="console" />
      </rules>
      
    </nlog>
    

## Custom JsonPayload

Enabling `EnableJsonLayout` will override the standard JSON format, and instead depend on the output from NLog JsonLayout. This will completely replace the JSON payload, but has a performance penalty because of additional parsing.
    
    
    <?xml version="1.0" encoding="utf-8" ?>
    <nlog xmlns="http://www.nlog-project.org/schemas/NLog.xsd"
          xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
    
      <extensions>
        <add assembly="Google.Cloud.Logging.NLog" />
      </extensions>
      
      <targets async="true">
        <target type="GoogleStackdriver" name="stackdriver"
                projectId="PROJECT_ID" logId="LOG_ID" resourceType="container" sendJsonPayload="true" enableJsonLayout="true">
          <layout xsi:type="JsonLayout" includeAllProperties="true">
            <attribute name="someProp" layout="prop" />
            <attribute name="nestedProp" encode="false">
              <layout type='JsonLayout'>
                <attribute name='insideNested1' layout='hello nested1!' />
                <attribute name='insideNested2' layout='hello nested2!' />
                <attribute name="nestedNestedProp" encode="false">
                  <layout type='JsonLayout'>
                    <attribute name='insideNestedNested1' layout='hello NestedNested1!' />
                    <attribute name='insideNestedNested2' layout='hello NestedNested2!' />
                  </layout>
                </attribute>
              </layout>
            </attribute>
          </layout>
        </target>
        <target name="console" xsi:type="Console" />
      </targets>
    
      <rules>
        <logger name="*" minlevel="Info" writeTo="stackdriver" />
        <logger name="*" minlevel="Info" writeTo="console" />
      </rules>
      
    </nlog>
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-05 UTC."],[],[]] 
