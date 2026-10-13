---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.Log4Net/latest/
title: Google.Cloud.Logging.Log4Net \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:06:33.715277+00:00
---

# Google.Cloud.Logging.Log4Net  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.Log4Net/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google.Cloud.Logging.Log4Net Stay organized with collections  Save and categorize content based on your preferences. 

5.0.0 (latest)  4.4.0  4.3.0  4.2.0  4.1.0  4.0.0  3.3.0 

`Google.Cloud.Logging.Log4Net` is a .NET client library to integrate [Google Cloud Logging](https://cloud.google.com/logging/) with [log4net](https://logging.apache.org/log4net/).

Note: This documentation is for version `5.0.0` of the library. Some samples may not work with other versions.

## Installation

Install the `Google.Cloud.Logging.Log4Net` package from NuGet. Add it to your project in the normal way (for example by right-clicking on the project in Visual Studio and choosing "Manage NuGet Packages...").

## Authentication

When running on Google Cloud, no action needs to be taken to authenticate.

Otherwise, the simplest way of authenticating your API calls is to set up Application Default Credentials. The credentials will automatically be used to authenticate. See [Set up Application Default Credentials](https://cloud.google.com/docs/authentication/provide-credentials-adc) for more details.

Alternatively, credentials can be provided when configuring `GoogleStackdriverAppender`. See the [configuration guide](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.Log4Net/latest/configuration) for details, specifically the `CredentialFile` and `CredentialJson` options.

## Getting started

See the [configuration guide](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.Log4Net/latest/configuration) for details of all `GoogleStackdriverAppender` configuration options.

## ASP.NET

Add the log4net section to the `Web.config` file:
    
    
    <configuration>
      <configSections>
    
        <!-- Other configSection item -->
    
        <!-- Specify a configuration section for log4net -->
        <section name="log4net" type="log4net.Config.Log4NetConfigurationSectionHandler,log4net" />
      </configSections>
    
      <!-- The log4net configuration -->
      <log4net>
        <appender name="CloudLogger" type="Google.Cloud.Logging.Log4Net.GoogleStackdriverAppender,Google.Cloud.Logging.Log4Net">
          <layout type="log4net.Layout.PatternLayout">
            <conversionPattern value="%-4timestamp [%thread] %-5level %logger %ndc - %message" />
          </layout>
          <projectId value="PROJECT_ID" />
          <logId value="LOG_ID" />
          <disableResourceTypeDetection value="true" />
        </appender>
        <root>
          <level value="ALL" />
          <appender-ref ref="CloudLogger" />
        </root>
      </log4net>
    
      <!-- Other configuration items -->
    
    </configuration>
    

Edit the file replacing `PROJECT_ID` with your Google Cloud Project ID, and `LOG_ID` with an identifier for your application.
    
    
    // Load log4net configuration from Web.config
    log4net.Config.XmlConfigurator.Configure(LogManager.GetRepository(GetType().Assembly));
    

If executing on [Google App Engine (GAE)](https://cloud.google.com/appengine/), [Google Kubernetes Engine (GKE)](https://cloud.google.com/kubernetes-engine/), or [Google Compute Engine (GCE)](https://cloud.google.com/compute/), then the `<projectId value="PROJECT_ID" />` configuration setting can be omitted; it will be auto-detected from the platform at run-time.

## Console app

Create a `log4net` configuration file (`log4net.xml`):
    
    
    <?xml version="1.0" encoding="utf-8" ?>
    <log4net>
      <appender name="CloudLogger" type="Google.Cloud.Logging.Log4Net.GoogleStackdriverAppender,Google.Cloud.Logging.Log4Net">
        <layout type="log4net.Layout.PatternLayout">
          <conversionPattern value="%-4timestamp [%thread] %-5level %logger %ndc - %message" />
        </layout>
        <projectId value="PROJECT_ID" />
        <logId value="LOG_ID" />
        <disableResourceTypeDetection value="true" />
      </appender>
      <root>
        <level value="ALL" />
        <appender-ref ref="CloudLogger" />
      </root>
    </log4net>
    

Edit the file replacing `PROJECT_ID` with your Google Cloud Project ID, and `LOG_ID` with an identifier for your application.

Use this file to configure `log4net` and then log as normal:
    
    
    // Configure log4net to use Google Cloud Logging from the XML configuration file.
    XmlConfigurator.Configure(LogManager.GetRepository(GetType().Assembly), new FileInfo("log4net.xml"));
    
    // Retrieve a logger for this context.
    ILog log = LogManager.GetLogger(typeof(Program));
    // Log some information. This log entry will be sent to Google Cloud Logging.
    log.Info("An exciting log entry!");
    
    // Flush buffered log entries before program exit.
    // This is required because log entries are buffered locally before being sent to Google Cloud Logging.
    // LogManager.Flush() only works in the full .NET framework (not in .NET Core):
    bool flushCompleted = LogManager.Flush(10_000);
    // On .NET Core, the specific repository needs to be flushed:
    bool repositoryFlushCompleted = ((IFlushable)LogManager.GetRepository(GetType().Assembly)).Flush(10_000);
    

If executing on [Google App Engine (GAE)](https://cloud.google.com/appengine/), [Google Kubernetes Engine (GKE)](https://cloud.google.com/kubernetes-engine/), or [Google Compute Engine (GCE)](https://cloud.google.com/compute/), then the `<projectId value="PROJECT_ID" />` configuration setting can be omitted; it will be auto-detected from the platform at run-time.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-18 UTC."],[],[]] 
