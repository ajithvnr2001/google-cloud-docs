---
url: https://docs.cloud.google.com/appengine/docs/flexible/troubleshooter/latency/
title: Troubleshoot elevated latency in App Engine apps \u00a0|\u00a0 App Engine flexible environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:14:18.083288+00:00
---

# Troubleshoot elevated latency in App Engine apps  |  App Engine flexible environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/flexible/troubleshooter/latency/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Flexible environment ](https://docs.cloud.google.com/appengine/docs/flexible)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Troubleshoot elevated latency in App Engine apps Stay organized with collections  Save and categorize content based on your preferences. 

In many cases, elevated latency in your application eventually results in [5xx server errors](https://tools.ietf.org/html/rfc7231#section-6.6). Because the root cause of both the error and the latency spikes might be the same, apply the following strategies for troubleshooting latency issues:

  1. Scope the latency issue
  2. Identify the cause
  3. Troubleshoot



## Scope the latency issue

Define the scope of the issue by asking the following questions:

  * Which applications, services, and versions does this issue impact?
  * Which specific endpoints on the service does this issue impact?
  * Does this impact all clients globally, or a specific subset of clients?
  * What is the start and end time of the incident? Consider specifying the timezone.
  * What are the specific errors?
  * What is the observed latency delta, which is usually specified as an increase at a specific percentile? For example, latency increased by 2 seconds at the 90th percentile.
  * How did you measure the latency? In particular, did you measure it at the client, or is it visible in Cloud Logging or in the Cloud Monitoring latency data that the App Engine serving infrastructure provides?
  * What are the dependencies of your service, and do any of them experience incidents?
  * Did you make any recent code, configuration, or workload changes that triggered this issue?



A service might have its own custom monitoring and logging that you can use to further narrow down the scope of the issue. Defining the scope of the problem will guide you towards the likely root cause and determine your next troubleshooting steps.

## Identify the cause

Determine which component in the request path is mostly likely to be causing the latency or errors. The main components in the request path are as follows:

Client --> Internet --> Google Front End (GFE) --> App Engine serving infrastructure --> Service instance

If the previous information doesn't point you to the source of the failure, apply the following strategies while reviewing your service instance's health and performance:

  1. Monitor the App Engine request logs. If you see HTTP status code errors or elevated latency in those logs, the issue likely lies in the instance that runs your service.

  2. If the number of service instances hasn't scaled up to match traffic levels, your instances might be overloaded, resulting in elevated errors and latency.

  3. If you see elevated errors or latency in [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview), the problem might be from the upstream of the load balancer, which records the App Engine metrics. In most cases, this points to a problem in the service instances.

  4. If you see elevated latency or errors in monitoring metrics but not in the request logs, it either indicates a load balancing failure, or a severe instance failure that's preventing the load balancer from routing requests. To distinguish between these cases, look at the request logs before the incident starts. If the request logs show increasing latency before failure, the application instances were beginning to fail before the load balancer stopped routing requests to them.




## Troubleshoot

This section describes troubleshooting strategies for elevated latency issues from the following components in the request path:

  1. Internet
  2. Google Front End (GFE)
  3. App Engine serving infrastructure
  4. Application instance
  5. Application dependencies



### Internet

Your application might encounter latency issues due to poor connectivity or lower bandwidth.

#### Poor internet connectivity

To determine if the issue is poor internet connectivity, run the following command on your client:
    
    
    $ curl -s -o /dev/null -w '%{time_connect}\n' <hostname>
    

The value for `time_connect` represents the latency of the client's connection to the nearest [Google Front End](https://docs.cloud.google.com/security/infrastructure/design#google_front_end_service). For slow connections, troubleshoot further using [`traceroute`](https://docs.cloud.google.com/vpc/docs/vpc#traceroute) to determine which hop on the network causes the delay.

Run tests from clients in different geographical locations. App Engine automatically routes requests to the closest Google data center, which varies based on the client's location.

#### Low bandwidth

The application might be responding quickly; however, network bottlenecks delay the App Engine serving infrastructure from sending packets across the network quickly, slowing down responses.

### Google Front End (GFE)

Your application might encounter latency issues due to incorrect routing, parallel requests sent from HTTP/2 clients, or termination of SSL connections.

#### Map a client IP to a geographical region

Google resolves the App Engine application's hostname to the closest GFE to the client, based on the client IP address it uses in the DNS lookup. If the client's DNS resolver isn't using the [EDNS0 protocol](https://landing.google.com/sre/sre-book/chapters/load-balancing-frontend/), Google might not route the client requests to the closest GFE.

#### HTTP/2 head-of-line blocking

HTTP/2 clients sending multiple requests in parallel might see elevated latency due to head-of-line blocking at the GFE. To resolve this issue, the clients must use the [QUIC protocol](https://blog.cloudflare.com/the-road-to-quic/).

#### SSL termination for custom domains

The GFE might terminate the SSL connection. If you're using a custom domain instead of an `appspot.com` domain, SSL termination requires an extra hop. This might add latency for applications running in some regions. For more information, see [Mapping custom domains](https://docs.cloud.google.com/appengine/docs/flexible/mapping-custom-domains).

### App Engine serving infrastructure

You might see elevated latency in your application due to service-wide incidents or autoscaling.

#### Service-wide incidents

Google posts details of a severe service-wide in the [Service Health](https://status.cloud.google.com/products/kchyUtnkMHJWaAva8aYc/history) dashboard. However, Google does rollouts gradually, so a service-wide incident is unlikely to affect all your instances at once.

#### Autoscaling

Elevated latency or errors can result from the following autoscaling scenarios:

  * Scale up traffic too fast: App Engine autoscaling might not scale your instances as fast as traffic increases, leading to temporary overloading. Typically, overloading occurs when traffic is generated by a computer program instead of end users. To resolve this issue, throttle the system that generates the traffic.

  * Spikes in traffic: spikes in traffic might cause elevated latency in cases where an autoscaled service needs to scale up more quickly than is possible, without affecting latency. End user traffic doesn't usually cause frequent traffic spikes. If you see traffic spikes, then you should investigate the cause. If a batch system is running at intervals, you might be able to smooth out the traffic or use different scaling settings.

  * Autoscaler settings: the autoscaler can be configured based on the scaling characteristics of your service. The scaling parameters might become non-optimal during the following scenarios: 

    * App Engine flexible environment services scale based on CPU utilization. Your application might become I/O bound during an incident resulting in overloading instances with a high number of requests, because CPU-based scaling does not occur. 



We recommend that you benchmark performance with the default scaling settings, and then run a new benchmark after each change to these settings.

##### Deployments

Elevated latency shortly after a deployment indicates that you haven't sufficiently scaled up before migrating traffic. Newer instances might not have warmed up local caches, and they serve more slowly than older instances.

To avoid latency spikes, don't deploy an App Engine service using the same version name as an existing version of the service. If you reuse an existing version name, you won't be able to slowly migrate traffic to the new version. Requests might be slower because App Engine restarts every instance within a short period of time. You also have to redeploy if you want to revert to the previous version.

### Application instance

This section describes the common strategies you can apply to your application instances, and source code to optimize performance and reduce latency.

#### Application code

Issues in application code can be challenging to debug, particularly if they are intermittent or not reproducible.

To resolve issues, do the following:

  * For diagnosing your issues, we recommend instrumenting your application using [logging](https://docs.cloud.google.com/logging/docs), [monitoring](https://docs.cloud.google.com/monitoring/docs), and [tracing](https://docs.cloud.google.com/trace/docs). You can also use [Cloud Profiler](https://docs.cloud.google.com/profiler/docs).

  * Try to reproduce the issue in a local development environment which might allow you to run language-specific debugging tools that might not be possible to run within App Engine.

  * You can SSH to an instance and gather a thread dump to see the current state of your application. Reproduce the problem in a load test or by running the application locally. You can increase the instance size to see if this resolves the problem. For example, increased RAM might resolve issues for applications experiencing delays due to garbage collection. 

  * To better understand how your application fails and what bottlenecks occur, load test your application until failure. Set a maximum instance count, and then gradually increase load until the application fails.

  * If the latency issue correlates with deployment of a new version of your application code, roll back to determine whether the new version caused the incident. However, if you deploy continuously, then the frequent deployments make it hard to determine whether or not the deployment caused the incident based on time of onset.

  * Your application might store configuration settings within the Datastore or elsewhere. Create a timeline of configuration changes to determine whether any of these line up with the onset of elevated latency.




#### Workload change

A workload change might cause elevated latency. Some monitoring metrics that indicate workload changes include [`qps`](https://docs.cloud.google.com/appengine/docs/flexible/flexible-for-standard-users#dropping_requests_when_overloaded), API usage, and latency. Check also for changes in request and response sizes.

#### Health check failures

The App Engine flexible environment load balancer stops routing requests to instances that fail health checks. This might increase load on other instances, potentially resulting in a cascading failure. The Nginx logs show instances that fail health checks. Analyze your logs and monitoring to determine why the instance is unhealthy, or [configure health checks](https://docs.cloud.google.com/appengine/docs/flexible/how-instances-are-managed#health_checking) to be less sensitive to transient failures. There is a short delay before the load balancer stops routing traffic to an unhealthy instance. This delay might cause an error spike if the [load balancer cannot retry requests](https://docs.cloud.google.com/load-balancing/docs/https#timeouts_and_retries).

#### Memory pressure

If monitoring shows either a saw-tooth pattern in memory usage, or a drop in memory usage that correlates to deployments, a memory leak might be the cause of performance issues. A memory leak might also cause frequent garbage collection that leads to higher latency. If you aren't able to trace this issue to a problem in the code, try provisioning larger instances with more memory.

#### Resource leak

If an instance of your application shows rising latency that correlates with instance age, then you might have a resource leak that causes performance issues. The latency drops after a deployment is complete. For example, a data structure that gets slower over time due to higher CPU usage might cause any CPU-bound workload to get slower.

#### Code optimization

To reduce latency on App Engine, optimize code by using the following methods:

  * **Offline work** : use [Cloud Tasks](https://docs.cloud.google.com/tasks/docs) to prevent user requests from blocking the application waiting for completion of work, such as sending mail.

  * **Asynchronous API calls** : ensure that your code isn't blocked waiting for an API call to complete.

  * **Batch API calls** : the batch version of API calls is usually faster than sending individual calls.

  * **Denormalize data models** : reduce the latency of calls made to the data persistence layer by denormalizing your data models.




### Application dependencies

Monitor dependencies of your application to detect if latency spikes correlate with a dependency failure.

A workload change and an increase in traffic might cause a dependency's latency to increase.

#### Non-scaling dependency

If your application's dependency doesn't scale as the number of App Engine instances scales up, the dependency might overload when traffic increases. An example of a dependency that might not scale is a SQL database. A higher number of application instances leads to a higher number of database connections, which might cause a cascading failure by preventing the database from starting up. To resolve this issue, do the following:

  1. Deploy a new default version that doesn't connect to the database.
  2. Shut down the previous default version.
  3. Deploy a new non-default version that connects to the database.
  4. Slowly migrate traffic to the new version.



As a preventive measure, design your application to drop requests to the dependency using [adaptive throttling](https://landing.google.com/sre/book/chapters/handling-overload.html).

#### Caching layer failure

To speed up requests, use multiple caching layers, such as edge caching, Memcache, and in-instance memory. A failure in one of these caching layers might cause a sudden latency increase. For example, a Memcache flush might cause more requests to go to a slower Datastore.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
