---
url: https://docs.cloud.google.com/appengine/docs/flexible/flexible-for-standard-users/
title: App Engine flexible environment for users of App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:45:09.904547+00:00
---

# App Engine flexible environment for users of App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/flexible/flexible-for-standard-users/

  * [ Home ](https://docs.cloud.google.com/)
  * [ App Engine ](https://docs.cloud.google.com/appengine)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  App Engine flexible environment for users of App Engine standard environment Stay organized with collections  Save and categorize content based on your preferences. 

This guide provides an introduction to the flexible environment for those who are familiar with the standard environment. It explains the similarities and key differences between the environments and also provides general architectural recommendations for applications that use both environments.

For a mapping of services available in standard environment to their analogues in the flexible environment, see [Migrating Services from the Standard Environment to the Flexible Environment](https://docs.cloud.google.com/appengine/docs/flexible/migrating).

## Similarities and key differences

Both environments provide you with App Engine’s deployment, serving, and scaling infrastructure. The key differences are the way the environment executes your application, how your application accesses external services, how you run your application locally, and how your application scales. You can also refer to [choosing an environment](https://docs.cloud.google.com/appengine/docs/the-appengine-environments) for a high-level summary of these differences.

### Application execution

In the standard environment, your application runs on a lightweight instance inside of a sandbox. This sandbox restricts what your application can do. For example, the sandbox only allows your app to use a limited set of binary libraries, and your app cannot write to disk. The standard environment also limits the CPU and memory options available to your application. Because of these restrictions, most App Engine standard applications tend to be stateless web applications that respond to HTTP requests quickly.

In contrast, the flexible environment runs your application in Docker containers on [Google Compute Engine virtual machines (VMs)](https://docs.cloud.google.com/compute/docs/instances), which have fewer restrictions. For example, you can use any programming language of your choice, write to disk, use any library you'd like, and even run multiple processes. The flexible environment also allows you to choose any Compute Engine machine type for your instances so that your application has access to more memory and CPU.

### Accessing external services

In the standard environment, your application typically accesses services such as Datastore via the built-in google.appengine APIs. However, in the flexible environment, these APIs are no longer available. Instead, use the [Google Cloud client libraries](https://docs.cloud.google.com/sdk/cloud-client-libraries). These client libraries work everywhere, which means that your application is more portable. If needed, applications that run in the flexible environment can usually run on [Google Kubernetes Engine](https://docs.cloud.google.com/kubernetes-engine/docs) or [Compute Engine](https://docs.cloud.google.com/compute/docs) without heavy modification.

### Local development

In the standard environment, you typically run your application locally using the App Engine SDK. The SDK handles running your application and emulates the App Engine services. In the flexible environment, the SDK is no longer used to run your application. Instead, applications written for the flexible environment should be written like standard web applications that can run anywhere. As mentioned, the flexible environment just runs your application in a Docker container. This means that to test the application locally, you just run the application directly. For example, to run a Python application using Django, you would just run `python manage.py runserver`.

Another key difference is that flexible environment applications running locally use actual Cloud Platform services, such as Datastore. Use a separate project for testing locally and when available, use [emulators](https://docs.cloud.google.com/sdk/gcloud/reference/beta/emulators).

### Scaling characteristics

While both environments use App Engine’s automatic scaling infrastructure, the way in which they scale is different. The standard environment can scale from zero instances up to thousands very quickly. In contrast, the flexible environment must have at least one instance running for each active version and can take longer to scale out in response to traffic.

Standard environment uses a custom-designed autoscaling algorithm. Flexible environment uses the Compute Engine [Autoscaler](https://docs.cloud.google.com/compute/docs/autoscaler). Note that flexible environment does not support all of the autoscaling options that are available to Compute Engine. App Engine respects any Compute Engine VM reservations that you already have in a region that match your configuration. Having a VM reservation increases the likelihood that you will receive a resource allocation during a [temporary resource shortage](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-resource-availability).

Developers should test their application behavior under a range of conditions. For example, you should verify how autoscaling responds when a CPU-bound application becomes I/O-bound during periods when calls to remote services have elevated latency.

### Health checks

Standard environment does not use health checks to determine whether or not to send traffic to an instance. Flexible environment permits application developers to write their own health check handlers that will be used by the load balancer to determine whether or not to send traffic to an instance and whether or not it should be autohealed. Developers should be careful when adding logic to health checks. For example, if the health check makes a call to an external service then a temporary failure in that service can cause all instances to go unhealthy, possibly leading to a cascading failure.

### Dropping requests when overloaded

Applications can drop requests when overloaded as part of a strategy to avoid cascading failures. This capability is built into the traffic routing layer in the standard environment. We recommend that developers of very high QPS applications in the flexible environment build this capability to drop overload traffic into their applications by limiting the number of concurrent requests.

You can verify that your flexible environment application is not susceptible to this type of failure by creating a version with a limit to the maximum number of instances. Then steadily increase traffic until requests are dropped. You should ensure that your application is not failing health checks during overload.

For Java, Java apps using the [Jetty runtime](https://docs.cloud.google.com/appengine/docs/flexible/java/runtime) can configure the Quality of Service Filter to implement drop overload. You can set the maximum number of concurrent requests serviced by the apps, and the length of time that requests will be queued using this feature.

### Instance sizes

Flexible environment instances are permitted to have higher CPU and memory limits than is possible with standard environment instances. This allows flexible instances to run applications that are more memory and CPU intensive. However, it may increase the likelihood of concurrency bugs due to the increase in threads within a single instance.

Developers can [SSH to a flexible environment instance](https://docs.cloud.google.com/appengine/docs/flexible/debugging-an-instance) and obtain a thread dump to troubleshoot this type of problem.

For example, if you are using the Java runtime, you can run the following:
    
    
    $ ps auwwx | grep java
    $ sudo kill -3 
    $ sudo docker logs gaeapp

### Maximum request timeout

While the standard environment [request timeout](https://docs.cloud.google.com/appengine/docs/standard/how-instances-are-managed#timeout) varies with the selected scaling type, the flexible environment always imposes a [60 minute timeout](https://docs.cloud.google.com/appengine/docs/the-appengine-environments#comparing_high-level_features). To avoid leaving requests open for the full 60 minutes and potentially using up all threads on the web server:

  * When making calls to external services, specify a timeout.

  * Implement a servlet filter to stop requests that take an unacceptably long time, such as 60 seconds. Make sure your app can return to a consistent state after your filter stops a request.




### Thread management

**Note:** Thread management is only applicable for the Java runtime.

Standard environment Java runtimes before Java 8 could only use [threads that are created using the App Engine standard environment SDK](https://docs.cloud.google.com/appengine/docs/legacy/standard/java/runtime#threads). Developers that port an application from a first generation Java standard environment runtime to flexible environment must switch to using native thread libraries. Applications that require a very large number of threads might run more efficiently with thread pools than with explicit thread creation.

### Traffic migration

Standard environment provides a traffic migration feature that gradually moves traffic to a new version to minimize latency spikes. See the [Traffic Migration docs](https://docs.cloud.google.com/appengine/docs/flexible/migrating-traffic) for ways to ensure you avoid a latency spike when switching traffic to a new version.

### Single zone failures

Standard environment applications are single-homed, meaning that all instances of the application live in a single availability zone. In the event of a failure in that zone, the application starts new instances in a different zone in the same region and the load balancer routes traffic to the new instances. You will see a latency spike due to loading requests and also a Memcache flush.

Flexible environment applications use [Regional Managed Instance Groups](https://docs.cloud.google.com/compute/docs/instance-groups/distributing-instances-with-regional-instance-groups), meaning that instances are distributed among multiple availability zones within a region. In the event of a single zone failure, the load balancer stops routing traffic to that zone. If you have set autoscaling to run your instances as hot as possible, then you will see a brief period of overload before autoscaling creates more instances.

### Cost comparisons

Many factors are involved in a cost comparison between workloads running on standard and flexible environments. These include:

  * Price paid per MCycle.
  * CPU platform capabilities, which impacts work that can be done per MCycle
  * How hot you can run instances on each platform.
  * Cost of deployments, which may differ on each platform and can be significant if you are using Continuous Deployment for your application.
  * Runtime overhead.



You will need to run experiments to determine the cost of your workload on each platform. In flexible environment, you can use QPS per core as a proxy for the cost efficiency of your application when running experiments to determine whether a change has an impact on costs. Standard environment does not provide such a mechanism to get real-time metrics on the cost efficiency of your application. You have to make a change and wait for the daily billing cycle to complete.

## Microservices

The standard environment allows secure authentication between applications using the [`X-Appengine-Inbound-Appid`](https://docs.cloud.google.com/appengine/docs/legacy/standard/python/appidentity#asserting_identity_to_other_app_engine_apps) request header. Flexible environment does not have such a feature. The recommended approach for secure authentication between applications is to use [OAuth](https://developers.google.com/identity/protocols/OAuth2ServiceAccount).

## Deployment

Deployments in standard environment are generally faster than deployments in flexible environment. It is faster to scale up an existing version in flexible environment than to deploy a new version, because the network programming for a new version is normally the long pole in a flexible environment deployment. One strategy for doing quick rollbacks in flexible environment is to maintain a known good version scaled down to a single instance. You can then scale up that version and then route all traffic to it using Traffic Splitting.

### When to use the flexible environment

The flexible environment is intended to be complementary to the standard environment. If you have an existing application running in the standard environment, it’s not usually necessary to migrate the entire application to the flexible environment. Instead, identify the parts of your application that require more CPU, more RAM, a specialized third-party library or program, or that need to perform actions that aren’t possible in the standard environment. Once you’ve identified these parts of your application, create small App Engine services that use the flexible environment to handle just those parts. Your existing service running in the standard environment can call the other services using HTTP, Cloud Tasks, or Cloud Pub/Sub.

For example, if you have an existing web application running in the standard environment and you want to add a new feature to convert files to PDFs, you can write a separate microservice that runs in the flexible environment that just handles the conversion to PDF. This microservice can be a simple program consisting of just one or two request handlers. This microservice can install and use any available Linux program to aid in the conversion, such as [unoconv](http://dag.wiee.rs/home-made/unoconv/).

Your main application remains in the standard environment and can call this microservice directly via HTTP, or if you anticipate the conversion will take a long time, the application can use [Cloud Tasks](https://docs.cloud.google.com/tasks/docs) or [Pub/Sub](https://docs.cloud.google.com/pubsub/docs) to queue the requests.

## What's next

[Map the services your app uses in the standard environment to their analogues in the flexible environment](https://docs.cloud.google.com/appengine/docs/flexible/migrating).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
