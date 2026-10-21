---
url: https://docs.cloud.google.com/functions/1stgendocs/writing/write-event-driven-functions/
title: Write event-driven functions \u00a0|\u00a0 Cloud Run functions (1st gen) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:29:32.478453+00:00
---

# Write event-driven functions  |  Cloud Run functions (1st gen)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/1stgendocs/writing/write-event-driven-functions/

If you are creating a new function, see the [Console Quickstart](https://cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. The content on this page only applies to existing legacy functions created with the Cloud Functions v1 API. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ 1st generation ](https://docs.cloud.google.com/functions/1stgendocs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/functions/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Write event-driven functions

**Note:** This content applies only to Cloud Run functions (1st gen)—formerly Cloud Functions (1st gen). See [Write event-driven functions](https://docs.cloud.google.com/run/docs/write-functions#write-event-driven-functions) for the Cloud Run functions version of this document. 

In Cloud Run functions, you use event-driven functions when you want a function to be invoked automatically in response to an event that occurs in your cloud environment.

There are two ways to implement event-driven functions. Which way you use depends on your chosen language runtime:

  * For Node.js, Python, Go, and Java runtimes, use Background functions.
  * For .NET, Ruby, and PHP runtimes, use CloudEvent functions.



## CloudEvent functions

_CloudEvent functions_ are based on [CloudEvents](https://cloudevents.io/), an industry-standard specification for describing event data in a common way. You can learn more about the CloudEvents specification at the [CloudEvents GitHub repository](https://github.com/cloudevents/spec). The CloudEvents project also provides a set of [CloudEvents SDKs](https://github.com/cloudevents/spec#sdks) to help work with CloudEvents objects in your code.

The following example shows a basic CloudEvent function source file for each runtime. See [Source directory structure](https://docs.cloud.google.com/functions/1stgendocs/writing#directory-structure) for information about where to locate your source code.

###  C# 
    
    
    using CloudNative.CloudEvents;
    using Google.Cloud.Functions.Framework;
    using System.Threading;
    using System.Threading.Tasks;
    
    namespace MyProject
    {
        // Define a class that implements the ICloudEventFunction<T> interface
        public class MyCloudEventFunction : ICloudEventFunction<CloudEventDataType>
        {
            // Implement the HandleAsync() method to handle CloudEvents
            public Task HandleAsync(CloudEvent cloudEvent, CloudEventDataType data, CancellationToken cancellationToken)
            {
                // Your code here
                // The data argument represents the CloudEvent data payload
    
                // Signal function completion
                return Task.CompletedTask;
            }
        }
    }

In .NET runtimes, you use the [Functions Framework for .NET](https://github.com/GoogleCloudPlatform/functions-framework-dotnet) to implement a CloudEvent handler class with the [`ICloudEventFunction<T>`](https://github.com/GoogleCloudPlatform/functions-framework-dotnet/blob/main/src/Google.Cloud.Functions.Framework/ICloudEventFunction.cs) interface. The `HandleAsync()` method accepts a [`CloudEvent`](https://github.com/cloudevents/sdk-csharp/blob/main/src/CloudNative.CloudEvents/CloudEvent.cs) object and the associated CloudEvent data payload as arguments.

The type of the CloudEvent data payload argument, shown in the above example as `CloudEventDataType`, must correspond to the type of event the function handles. The [Google CloudEvents .NET library](https://github.com/googleapis/google-cloudevents-dotnet) provides data types for the various events supported by Google.

The [function entry point](https://docs.cloud.google.com/functions/1stgendocs/writing#entry-point) is the fully-qualified name of the CloudEvent handler class, including the namespace. In this example, the entry point is `MyProject.MyCloudEventFunction`.

###  Ruby 
    
    
    require "functions_framework"
    
    # Register a CloudEvent function with the Functions Framework
    FunctionsFramework.cloud_event "my_cloudevent_function" do |cloud_event|
      # Your code here
      # Access the CloudEvent data payload via cloud_event.data
    end
    

In Ruby, you register a CloudEvent handler function with the [Functions Framework for Ruby](https://googlecloudplatform.github.io/functions-framework-ruby). Your handler function must accept a CloudEvents [`Event`](https://github.com/cloudevents/sdk-ruby/blob/main/lib/cloud_events/event/v1.rb) object as an argument.

The [function entry point](https://docs.cloud.google.com/functions/1stgendocs/writing#entry-point) is the name with which the handler is registered with the Functions Framework. In this example, the entry point is `my_cloudevent_function`.

###  PHP 
    
    
    <?php
    
    use CloudEvents\V1\CloudEventInterface;
    use Google\CloudFunctions\FunctionsFramework;
    
    // Register a CloudEvent function with the Functions Framework
    FunctionsFramework::cloudEvent('myCloudEventFunction', 'myCloudEventHandler');
    
    // Define your CloudEvent handler
    function myCloudEventHandler(CloudEventInterface $event): void
    {
        // Your code here
        // Access the CloudEvent data payload via $event->getData()
    }
    

In PHP, you register a CloudEvent handler function with the [Functions Framework for PHP](https://github.com/GoogleCloudPlatform/functions-framework-php). Your handler function must accept an argument that conforms to the [`CloudEventInterface`](https://github.com/cloudevents/sdk-php/blob/master/src/V1/CloudEventInterface.php) interface.

The [function entry point](https://docs.cloud.google.com/functions/1stgendocs/writing#entry-point) is the name with which the handler is registered with the Functions Framework. In this example, the entry point is `myCloudEventFunction`.

For CloudEvent functions, event data is passed to your function in the [CloudEvents format](https://docs.cloud.google.com/eventarc/docs/cloudevents), with a CloudEvent data payload corresponding to the event type that triggers your function. See [Cloud Run functions triggers](https://docs.cloud.google.com/functions/1stgendocs/calling) for information about supported triggers, event types, and associated event data formats.

The [Google Events](https://github.com/googleapis/google-cloudevents) repository contains resources for working with CloudEvents issued by Google.

## Background functions

Event-driven functions in the Node.js, Python, Go, and Java runtimes expect different arguments from CloudEvent functions. This older style of event-driven function is called a _background function_.

The following example shows a basic background function source file for each runtime. See [Source directory structure](https://docs.cloud.google.com/functions/1stgendocs/writing#directory-structure) for information about where to locate your source code.

###  Node.js 
    
    
    // Define and export an event handler
    exports.myBackgroundFunction = (eventData, context, callback) => {
      // Your code here
      // The eventData argument represents the event data payload
    
      // Optionally signal function completion:
      callback();
    };
    

In Node.js, you define and export a function that handles event data. Cloud Run functions passes your handler function the following arguments:

  * `eventData`: An object representing the event data payload. Its format depends on the event type.
  * `context`: An object containing metadata about the event.
  * `callback`: An optional function you can call to signal completion. The first argument to this callback is interpreted as signaling an error. Pass no arguments or a `null` first argument to signal success.



The [function entry point](https://docs.cloud.google.com/functions/1stgendocs/writing#entry-point) is the name of the exported event handler. In this example, the entry point is `myBackgroundFunction`.

###  Python 
    
    
    # Define an event handler
    def my_background_function(event_data, context):
      # Your code here
      # The event_data argument represents the event data payload
    

In Python, you define a function that handles event data. Cloud Run functions passes your handler function the following arguments:

  * `event_data`: A dictionary representing the event data payload. Its format depends on the event type.
  * `context`: An object containing metadata about the event.



The [function entry point](https://docs.cloud.google.com/functions/1stgendocs/writing#entry-point) is the name of the handler function. In this example, the entry point is `my_background_function`.

###  Go 
    
    
    package mybackgroundfunction
    
    import (
        "context"
    )
    
    // Function MyBackgroundFunction accepts and handles event data
    func MyBackgroundFunction(ctx context.Context, e EventDataType) error {
        // Your code here
        // The argument e represents the event data payload
    
        // Return nil if no error occurred
        return nil
    }

In Go, you define an exported function that handles event data. Cloud Run functions passes your handler function the following arguments:

  * `ctx`: A `context.Context` object containing metadata about the event. You can retrieve the metadata using the [`cloud.google.com/go/functions/metadata`](https://pkg.go.dev/cloud.google.com/go/functions/metadata) package.
  * `e`: An object representing the event data payload. Its type, shown in the above example as `EventDataType`, must be a struct corresponding to the type of event the function handles. The event data payload is unmarshaled into the struct using [`json.Unmarshal()`](https://pkg.go.dev/encoding/json#Unmarshal).



The [function entry point](https://docs.cloud.google.com/functions/1stgendocs/writing#entry-point) is the name of the exported event handler. In this example, the entry point is `MyBackgroundFunction`.

###  Java 
    
    
    package mybackgroundfunction;
    
    import com.google.cloud.functions.BackgroundFunction;
    import com.google.cloud.functions.Context;
    
    // Define a class that implements the BackgroundFunction<T> interface
    public class MyBackgroundFunction implements BackgroundFunction<EventDataType> {
      // Implement the accept() method to handle events
      @Override
      public void accept(EventDataType eventData, Context context) {
        // Your code here
        // The eventData argument represents the event data payload
      }
    }

In Java, you use the [Functions Framework Java API](https://javadoc.io/doc/com.google.cloud.functions/functions-framework-api/) to implement an event handler class with the [`BackgroundFunction<T>`](https://javadoc.io/doc/com.google.cloud.functions/functions-framework-api/latest/com/google/cloud/functions/BackgroundFunction.html) interface. The `accept()` method accepts as arguments the event data payload and a [`Context`](https://javadoc.io/doc/com.google.cloud.functions/functions-framework-api/latest/com/google/cloud/functions/Context.html) object containing metadata about the event.

The type of the event data payload argument, shown in the above example as `EventDataType`, must correspond to the type of event the function handles. The event data payload is deserialized into an instance of this class using [`Gson.fromJson()`](https://www.javadoc.io/doc/com.google.code.gson/gson/latest/com.google.gson/com/google/gson/Gson.html#fromJson\(java.lang.String,java.lang.Class\)).

The [function entry point](https://docs.cloud.google.com/functions/1stgendocs/writing#entry-point) is the fully-qualified name of the event handler class, including the package name. In this example, the entry point is `mybackgroundfunction.MyBackgroundFunction`.

For background functions, the event data payload is passed directly to your function in a format corresponding to the event type that triggers your function. See [Triggers supported in Cloud Run functions (1st gen)](https://docs.cloud.google.com/functions/1stgendocs/calling#1st-gen-triggers) for information about supported triggers, event types, and associated event data formats.

## Function termination

Cloud Run functions considers event-driven function execution complete when the function returns. If the function creates background tasks (such as with threads, futures, JavaScript `Promise` objects, callbacks, or system processes), you must terminate or otherwise resolve these tasks before returning from your function. Any tasks not terminated before the function returns might not be completed, and might cause undefined behavior.

## Automatic retries

Event-driven functions can be configured to automatically retry failed invocations. See [Retrying event-driven functions](https://docs.cloud.google.com/functions/1stgendocs/bestpractices/retries) for more information.

## Next steps

  * Learn about [Cloud Run functions triggers](https://docs.cloud.google.com/functions/1stgendocs/calling).
  * Learn how to [deploy a Cloud Run function](https://docs.cloud.google.com/functions/1stgendocs/deploy).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
