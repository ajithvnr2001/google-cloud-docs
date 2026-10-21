---
url: https://docs.cloud.google.com/functions/1stgendocs/concepts/java-logging/
title: Java Logging \u00a0|\u00a0 Cloud Run functions (1st gen) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:29:29.642746+00:00
---

# Java Logging  |  Cloud Run functions (1st gen)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/1stgendocs/concepts/java-logging/

If you are creating a new function, see the [Console Quickstart](https://cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. The content on this page only applies to existing legacy functions created with the Cloud Functions v1 API. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ 1st generation ](https://docs.cloud.google.com/functions/1stgendocs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/functions/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Java Logging

In the Java runtime, any output to `STDOUT` or `STDERR` is propagated to [Cloud Logging](https://docs.cloud.google.com/functions/1stgendocs/monitoring/logging). However, granular log severity level is not propagated. Use the standard [Java Logging API (JUL)](https://docs.oracle.com/javase/10/core/java-logging-overview.htm/) to log messages and propagate the correct log severity levels to Cloud Logging.

If you use a different logging framework, such as [SLF4J](http://www.slf4j.org/), [Log4j 2](https://logging.apache.org/log4j/2.x/), or [Apache Commons Logging](https://commons.apache.org/proper/commons-logging/), you can propagate the correct log severity level in one of the following ways:

  * Format the log messages in the [Structured Logging JSON format](https://docs.cloud.google.com/logging/docs/structured-logging) so that the severity level is propagated to Cloud Logging.
  * Use a bridge/adapter to send log messages to the Java Logging API, which already propagates the log messages in the correct format. If you take this approach, make sure there is not an existing adapter that already routes from the Java Logging API to the logging framework.



If your function uses different libraries and the libraries use different logging frameworks, then you'll need to configure each of the logging frameworks used. The following sections cover some of the various options.

## Spring Cloud Run function

If you use Spring Cloud Run function with the Spring Cloud Run functions Google Cloud Adapter, you can output the log in the right format using the [Spring Cloud's Google Cloud Logging Starter](https://github.com/GoogleCloudPlatform/spring-cloud-gcp/tree/main/spring-cloud-gcp-samples/spring-cloud-gcp-logging-sample) and the [`CONSOLE_JSON` appender](https://github.com/GoogleCloudPlatform/spring-cloud-gcp/blob/main/spring-cloud-gcp-logging/src/main/resources/com/google/cloud/spring/logging/logback-json-appender.xml) to output the log in the JSON format. Spring uses SLF4J and Logback by default—but you can also route SLF4J logs to the Java Logging API. See the SLF4J section for details.

## Java Logging API (JUL)

All supported Cloud Run functions [Java environments](https://docs.cloud.google.com/functions/1stgendocs/runtime-support#java) include Java Logging with a JSON handler that outputs the log in the correct format. Some Java frameworks may add additional components to bridge JUL to a different logging framework (such as [jul-to-slf4j bridge](http://www.slf4j.org/legacy.html#jul-to-slf4j) or [Log4j JDK Logging Adapter](https://logging.apache.org/log4j/2.0/log4j-jul.html)), in which case those log messages will no longer be formatted correctly. If your log messages do not have correct severity levels, make sure those bridges are removed.

## SLF4J

[SLF4J](http://www.slf4j.org/) can write logs to the Java Logging API by using the `slf4j-jdk14` logging framework binding. See the [SLF4J documentation](http://www.slf4j.org/docs.html) for details. Make sure you don't have the `jul-to-slf4j` bridge.

## Logback

[Logback](http://logback.qos.ch/) does not have an appender that routes log messages to the Java Logging API. However, Logback is usually used with the SFL4J API, so you can switch the SLF4J logger implementation to the Java Logging API.

## Log4j 2

[Log4j 2](https://logging.apache.org/log4j/2.x/) does not have a direct adapter that routes log messages to the Java Logging API. If you are using Log4j 2, then you need to first route messages to SLF4J using the [Log4J 2 to SLF4J Adapter](https://logging.apache.org/log4j/log4j-2.2/log4j-to-slf4j/index.html), then configure SLF4J to use the Java Logging API implementation. Make sure you do not have the Log4j JDK Logging Adapter.

## Apache Commons Logging (JCL)

[Apache Commons Logging](https://commons.apache.org/proper/commons-logging/) has a Java Logging API adapter. Configure Commons Logging to use the [Jdk14Logger](http://commons.apache.org/proper/commons-logging/apidocs/org/apache/commons/logging/impl/Jdk14Logger.html). See the [Apache Commons Logging configuration](http://commons.apache.org/proper/commons-logging/guide.html#Configuration) page for more information.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
