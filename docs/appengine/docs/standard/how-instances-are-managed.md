---
url: https://docs.cloud.google.com/appengine/docs/standard/how-instances-are-managed/
title: How instances are managed \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:47:43.610389+00:00
---

# How instances are managed  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/how-instances-are-managed/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  How instances are managed Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** For new projects you create after March 2025, App Engine sets the automatic scaling maximum instances default for standard environment deployments to 20. This change doesn't impact existing apps. To override the default, specify a new [`max_instances`](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml#scaling_elements) value in your `app.yaml` file, and deploy a new version or redeploy over an existing version.

Instances are the basic building blocks of App Engine, providing all the resources needed to successfully host your application. At any given time, your application can be running on one or many instances with requests being spread across all of them. Each instance includes a security layer to ensure that instances cannot inadvertently affect each other.

App Engine can automatically create and shut down instances as traffic fluctuates, or you can specify a number of instances to run regardless of the amount of traffic. To determine how and when new instances are created, you specify a _scaling type_ for your app. The scaling settings are applied at the App Engine version level as part of the [app.yaml](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml#scaling_elements) file.

## Scaling types

App Engine supports the following _scaling types_ , which controls how and when instances are created:

  * Automatic (default)
  * Basic
  * Manual



You specify the scaling type in your app's [`app.yaml`](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml#scaling_elements). By default, your app uses automatic scaling, which means App Engine will manage the number of idle instances.

Automatic scaling
    Automatic scaling creates instances based on request rate, response latencies, and other application metrics. You can specify thresholds for each of these metrics, as well as a minimum number instances to keep running at all times by configuring the [`automatic_scaling`](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml#scaling_elements) element.

Basic Scaling
    Basic scaling creates instances when your application receives requests. Each instance will be shut down when the application becomes idle. Basic scaling is ideal for work that is intermittent or driven by user activity.

Manual scaling
    Manual scaling specifies the number of instances that continuously run regardless of the load level. This allows tasks such as complex initializations and applications that rely on the state of the memory over time.
This table compares the performance features of the three scaling types: Feature | Automatic scaling | Basic scaling | Manual scaling  
---|---|---|---  
Request timeout |  10 minutes for HTTP requests and task queue tasks. If your app doesn't return a request within this time limit, App Engine interrupts the request handler and [emits an error](https://docs.cloud.google.com/appengine/docs/standard/how-requests-are-handled#specifying_a_request_deadline) for your code to handle.  |  24 hours for HTTP requests and task queue tasks. If your app doesn't return a request within this time limit, App Engine interrupts the request handler and [emits an error](https://docs.cloud.google.com/appengine/docs/standard/how-requests-are-handled#specifying_a_request_deadline) for your code to handle. A basic-scaled instance can choose to handle `/_ah/start` and execute a program or script for many hours without returning an HTTP response code. | Same as basic scaling.  
Background threads (Java only) | Not allowed | Allowed | Allowed  
Residence | Instances are shut down based on usage patterns. |  Instances are shut down based on the `idle_timeout` parameter. If an instance has been idle, for example it has not received a request for more than `idle_timeout`, then the instance is shut down.  |  Instances remain in memory and state is preserved across requests. When instances are stopped, an `/_ah/stop` request appears in the logs.   
  
If there is an `/_ah/stop` handler or a registered shutdown hook ( [Java](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.LifecycleManager#com_google_appengine_api_LifecycleManager_setShutdownHook_com_google_appengine_api_LifecycleManager_ShutdownHook_), [Python](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/runtime/set_shutdown_hook)), it has 30 seconds to complete before shutdown occurs.   
Startup and shutdown |  Instances are created on demand to handle requests and automatically turned down when idle.  |  Instances are created on demand to handle requests and automatically shut down when idle, based on the `idle_timeout` configuration parameter. An instance that is [manually stopped](https://docs.cloud.google.com/appengine/docs/standard/how-instances-are-managed#instance_states) has 30 seconds to finish handling requests before it is forcibly terminated.  |  Instances are sent a start request automatically by App Engine in the form of an empty GET request to `/_ah/start`. As with basic scaling, an instance that is [manually stopped](https://docs.cloud.google.com/appengine/docs/standard/how-instances-are-managed#instance_states) has 30 seconds to finish handling requests before it is forcibly terminated.   
Instance addressability | Instances are anonymous. |  Instance "i" of version "v" of service "s" is addressable at the URL: `https://i-dot-v-dot-s-dot-app_id.REGION_ID.r.appspot.com`. If you have set up a [ wildcard subdomain mapping](https://docs.cloud.google.com/appengine/docs/standard/mapping-custom-domains) for a custom domain, you can also address a service or any of its instances via a URL of the form `https://s.domain.com` or `https://i.s.domain.com`. You can reliably cache state in each instance and retrieve it in subsequent requests.  | Same as basic scaling.  
Scaling |  App Engine scales the number of instances automatically in response to processing volume. This scaling factors in the `automatic_scaling` settings that are provided on a per-version basis in the configuration file.  |  A service with basic scaling is configured by setting the maximum number of instances in the `max_instances` parameter of the `basic_scaling` setting. The number of live instances scales with the processing volume.  |  You configure the number of instances of each version in that service's configuration file. The number of instances usually corresponds to the size of a dataset being held in memory or the desired throughput for offline work.   
  
## Scaling dynamic instances

App Engine applications that use basic or automatic scaling are powered by any number of dynamic instances at a given time, depending on the volume of incoming requests. As requests for your application increase, the number of dynamic instances may increase as well.

### Apps with basic scaling

If you use basic scaling, App Engine attempts to keep your cost low, even though that may result in higher latency as the volume of incoming requests increases.

When none of the existing instances are available to serve an incoming request, App Engine starts a new instance. Even after starting a new instance, some requests may need to be queued until the new instance completes its [startup process](https://docs.cloud.google.com/appengine/docs/standard/how-instances-are-managed#startup). If you require the lowest latency possible consider using automatic scaling, which creates new instances preemptively to minimize latency.

### Apps with automatic scaling

If you use automatic scaling, each instance in your app has its own queue for incoming requests. Before the queues become long enough to have a noticeable effect on your app's latency, App Engine automatically creates one or more new instances to handle the increasing load.

**Note:** If your service is infrequently used, App Engine standard environment scales to zero instances. To reduce the impact of cold-start latency for infrequently used services, you can change the configuration to allow a minimum of one instance to always be active or enable [warmup requests](https://docs.cloud.google.com/appengine/docs/standard/configuring-warmup-requests).

You can configure the settings for automatic scaling to achieve a trade-off between the performance you want and the cost you can incur. The following table describes these settings.

Automatic scaling settings | Description  
---|---  
[Target CPU utilization](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml#automatic_scaling_target_cpu_utilization) | Sets the CPU utilization ratio threshold to specify the CPU usage threshold at which more instances will be started to handle traffic.  
[Target throughput utilization](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml#automatic_scaling_target_throughput_utilization) | Sets the throughput threshold for the number of concurrent requests after which more instances will be started to handle traffic.  
[Max concurrent requests](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml#max_concurrent_requests) | Sets the max concurrent requests an instance can accept before the scheduler spawns a new instance.  
  
Watch the App Engine [Scheduler settings](https://www.youtube.com/watch?v=eUXUY7QFfAI) video to see the effects of these settings.

### Scaling down

When request volumes decrease, App Engine reduces the number of instances. This downward scaling helps ensure that all of your application's current instances are being used for optimal efficiency and cost effectiveness.

When an application is not being used at all, App Engine turns off its associated dynamic instances, but readily reloads them as soon as they are needed. Reloading instances can result in loading requests and additional latency for users.

You can specify a minimum number of idle instances. Setting an appropriate number of idle instances for your application based on request volume allows your application to serve every request with little latency, unless you are experiencing abnormally high request volume.

#### Scaling down in automatic scaling

If your app uses automatic scaling, it takes approximately 15 minutes of inactivity for the idle instances to start shutting down. To keep one or more idle instances running, set the value of [`min_idle_instances`](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml#scaling_elements) to `1` or higher.

### Scaling and batches of requests

If you are sending batches of requests to your services, for example, to a task queue for processing, a large number of instances will be created quickly. We recommend controlling this by rate limiting the number of request sent per second, if possible. For example, if you use Google Tasks, you can [control the rate](https://docs.cloud.google.com/tasks/docs/configuring-queues#rate) at which tasks are pushed.

## Instance life cycle

### Instance states

An instance of an auto-scaled service is always running. However, an instance of a manual or basic scaled service can be either running or stopped. All instances of the same service and version share the same state. You change the state of your instances by managing your versions. You can:

  * Use the [Versions page](https://console.cloud.google.com/appengine/versions) in the Google Cloud console
  * Use `[gcloud app versions start](https://docs.cloud.google.com/sdk/gcloud/reference/app/versions/start)` and `[gcloud app versions stop](https://docs.cloud.google.com/sdk/gcloud/reference/app/versions/stop)` commands



### Startup

Each service instance is created in response to a start request, which is an empty HTTP `GET` request to `/_ah/start`. App Engine sends this request to bring an instance into existence; users cannot send a request to `/_ah/start`. Manual and basic scaling instances must respond to the start request before they can handle another request. The start request can be used for two purposes:

  * To start a program that runs indefinitely, without accepting further requests.
  * To initialize an instance before it receives additional traffic.



Manual, basic, and automatically scaling instances startup differently. When you start a manual scaling instance, App Engine immediately sends a `/_ah/start` request to each instance. When you start an instance of a basic scaling service, App Engine allows it to accept traffic, but the `/_ah/start` request is not sent to an instance until it receives its first user request. Multiple basic scaling instances are only started as necessary, in order to handle increased traffic. Automatically scaling instances do not receive any `/_ah/start` request.

When an instance responds to the `/_ah/start` request with an HTTP status code of `200–299` or `404`, it is considered to have successfully started and can handle additional requests. Otherwise, App Engine terminates the instance. Manual scaling instances are restarted immediately, while basic scaling instances are restarted only when needed for serving traffic.

### Shutdown

The shutdown process might be triggered by a variety of planned and unplanned events, such as:

  * There are too many instances and not enough app requests (traffic).
  * You manually stop an instance.
  * You deploy an updated version to the service.
  * The instance exceeds the maximum memory for its configured [`instance_class`](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml#instance_class).
  * Your application runs out of Instance Hours quota.
  * Your instance is moved to a different machine, either because the current machine that is running the instance is restarted, or App Engine moved your instance to improve load distribution.



One of the benefits App Engine standard environment's "pay for only what you need" platform as described earlier in Scaling Down is that the system autoscales the number of instances down to zero when there is no traffic. This helps make App Engine a cost-effective solution for small applications that don't receive continuous requests. When an instance needs to be shut down, new incoming requests are routed to other instances (if any) and requests that are currently being processed are given time to complete.

App Engine normally sends a `STOP` (`SIGTERM`) signal to the app container. Your app does not need to respond to this event, but it can use this to perform any necessary clean-up actions before the container is shut down. Under normal conditions, the system waits up to 2 seconds for the app to stop and then sends a `KILL` (`SIGKILL`) signal. If your app does not catch the `SIGTERM` signal, the instance is immediately shut down.

Some instance shutdown log messages you might see include:
    
    
    [start] Quitting on terminated signal
    [INFO] Handling signal: term
    [INFO] Worker exiting (pid: 21)
    [INFO] Worker exiting (pid: 24)
    [INFO] Shutting down: Master
    [start] Start program failed: termination triggered by nginx exit
    

These log messages do not indicate any error condition but are indications of the normal instance shut down process. Note that `[start]` and `Start` in the logs refer to a platform process named `start` and has nothing to do with starting an instance or an app.

### Loading requests

When App Engine creates a new instance for your application, the instance must first load any libraries and resources required to handle the request. This happens during the first request to the instance, called a _Loading Request_. During a loading request, your application undergoes initialization which causes the request to take longer.

The following best practices allow you to reduce the duration of loading requests:

  * Load only the code needed for startup.
  * Access the disk as little as possible.
  * In some cases, loading code from a zip or jar file is faster than loading from many separate files.



### Warmup requests

Warmup requests are a specific type of loading request that load application code into an instance ahead of time, before any live requests are made. Manual or basic scaling instances do not receive an `/_ah/warmup` request.

To learn more about how to use warmup requests, see [Configuring warmup requests](https://docs.cloud.google.com/appengine/docs/standard/configuring-warmup-requests).

## Instance uptime

App Engine attempts to keep manual and basic scaling instances running indefinitely. However, at this time there is no guaranteed uptime for manual and basic scaling instances.

## NTP with App Engine standard environment

The App Engine standard environment has network time protocol (NTP) services which use Google NTP servers. However, the NTP service is not editable.

## Manage services

Depending on the scaling type of your instance, you can manage services and versions in the Google Cloud console or Google Cloud CLI.

### Stop a version

Each version in App Engine runs within one or more instances, depending on how much traffic you configured it to handle.

Click the tab for instructions on using the tool of your choice:

###  Console 

To stop or disable a version for your service:

  1. Go to the App Engine **Versions** page in the Google Cloud console:

[Go to Versions](https://console.cloud.google.com/appengine/versions)

  2. Select a version from the table, and click **Stop**.




###  gcloud 

Run the following:
    
    
      gcloud app versions stop --service=SERVICE VERSION
    

Replace:

  * SERVICE with the name of your service.
  * VERSION with the version name of your service.



### Delete a service

Each service can be configured to use different runtimes and to operate with different performance settings. You can't delete the default service. Deleting a service also deletes all of its accompanying versions in your project.

Click the tab for instructions on using the tool of your choice:

###  Console 

To delete a service:

  1. Go to the App Engine **Services** page in the Google Cloud console:

[Go to Services](https://console.cloud.google.com/appengine/services)

  2. Select a service from the table, and click **Delete**.




###  gcloud 

Run the following:
    
    
      gcloud app services delete SERVICE
    

Replace:

  * SERVICE with the name of your service.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
