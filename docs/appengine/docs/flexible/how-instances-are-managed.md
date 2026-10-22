---
url: https://docs.cloud.google.com/appengine/docs/flexible/how-instances-are-managed/
title: How instances are managed \u00a0|\u00a0 App Engine flexible environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:30:32.319537+00:00
---

# How instances are managed  |  App Engine flexible environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/flexible/how-instances-are-managed/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Flexible environment ](https://docs.cloud.google.com/appengine/docs/flexible)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  How instances are managed Stay organized with collections  Save and categorize content based on your preferences. 

Instances are the computing units that App Engine uses to automatically scale your [application](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine). At any given time, your application can be running on one instance or many instances, with requests being spread across all of them.

Your instances with manual scaling should run indefinitely, but there is no uptime guarantee as instances can get early termination due to failures or restart for the updates. Hardware or software failures that cause early termination or frequent restarts can occur without warning and can take considerable time to resolve.

All flexible instances may be restarted on a weekly basis if there are updates available. This schedule is not guaranteed. During restarts, critical, backwards-compatible updates are automatically rolled out to the underlying operating system. Your application's image will remain the same across restarts.

## Health checking

App Engine sends periodic health check requests to confirm that an instance is running, and to check that an instance is fully started and ready to accept incoming requests. By default, these health checks are enabled and are known as **split health checks**. An instance that receives a health check must answer the health check within a specified time interval.

If you need to extend the default behavior of split health checks to your application, you can customize the [`app.yaml`](https://docs.cloud.google.com/appengine/docs/flexible/reference/app-yaml#updated_health_checks) file to configure two types of health checks:

  * **Liveness checks** detect that a VM instance and its container are running. When a VM instance fails the liveness check, the instance is restarted automatically. Liveness checks can fail due to the configured thresholds and time intervals, or due to the container crashing.
  * **Readiness checks** detect that a VM instance is ready to accept incoming requests. If a VM instance fails the readiness check, it means that the VM instance has not finished its startup and is not ready to receive requests. When the VM instance passes the readiness check and has completed its startup, it is added to the pool of available instances.



Learn more about split health check behaviors in the [Migrating to Split Health Checks](https://docs.cloud.google.com/appengine/docs/flexible/migrating-to-split-health-checks) guide.

As the instance goes through these health checks, the [App Engine logs](https://console.cloud.google.com/logs/query) can indicate that the instance is in any of the following states:

  * **Healthy**. The instance received the health check requests and is processing the requests. A healthy status indicates that the instance has more than 820 MB of available disk space and should respond to a health check with an HTTP status code of `200`.
  * **Unhealthy**. The instance refused the health check requests and failed to respond to a specified number of consecutive health check requests. App Engine continues to send health check requests and restarts the instance if an unhealthy instance continues to fail to respond to a predetermined number of consecutive health checks.
  * **Lameduck**. The instance is scheduled to be shut down or restarted. During shutdowns, the instance finishes up ongoing requests, and refuses new requests. The app returns a `503` code to indicate that the instance is unable to handle requests. Before an instance shuts down or restarts, the shutdown script has a limited time period to run, and cannot be configured to be shorter or longer.
  * **App Lameduck**. The instance is preparing to serve traffic. The app returns a `503` code to indicate that the instance is unable to handle requests. When a VM instance has completed startup and is ready to serve traffic, the instance will become healthy and process requests. If a VM instance does not start up in time, the instance changes to unhealthy and gets removed.



Both lameduck and app lameduck behaviors are part of a normal process that the VM instance goes through.

## Monitoring resource usage

The Instances page of the [Google Cloud console](https://console.cloud.google.com/appengine/instances) provides visibility into how your instances are performing. You can see the memory and CPU usage of each instance, uptime, number of requests, and other statistics. You can also manually initiate the shutdown process for any instance.

## NTP with App Engine flexible environment

The App Engine flexible environment has network time protocol (NTP) services which use Google NTP servers. However, the NTP services in the flexible environment is not editable.

## Instance location

Instances are automatically located by geographical region according to the [project settings](https://docs.cloud.google.com/appengine/docs/flexible/managing-projects-apps-billing).

## Instance scaling

While an application is running, incoming requests are routed to an existing or new instance of the appropriate service/version. Each active version must have at least one instance running, and the scaling type of a service/version controls how additional instances are created. You specify the scaling type in your app's [`app.yaml`](https://docs.cloud.google.com/appengine/docs/flexible/reference/app-yaml#services). By default, your app uses automatic scaling, which means App Engine will manage the number of idle instances.

Automatic scaling
    Automatic scaling creates instances based on request rate, response latencies, and other application metrics. You can specify thresholds for each of these metrics, as well as a minimum number instances to keep running at all times by configuring the [`automatic_scaling`](https://docs.cloud.google.com/appengine/docs/flexible/reference/app-yaml#automatic_scaling) element.

Manual scaling
    Manual scaling specifies the number of instances that continuously run regardless of the load level. This allows tasks such as complex initializations and applications that rely on the state of the memory over time.

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
