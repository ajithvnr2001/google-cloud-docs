---
url: https://docs.cloud.google.com/appengine/docs/the-appengine-environments/
title: Choose an App Engine environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:17:33.321685+00:00
---

# Choose an App Engine environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/the-appengine-environments/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Choose an App Engine environment Stay organized with collections  Save and categorize content based on your preferences. 

**Important:** For new Google Cloud users, we recommend using [Cloud Run](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run) as the preferred alternative over App Engine. Cloud Run is a fully managed, modern application hosting platform that provides access to advanced capabilities, such as GPUs, at lower prices. We recommend that you [evaluate Cloud Run](https://docs.cloud.google.com/appengine/migration-center/run/compare-gae-with-run) for your upcoming projects, or use Cloud Run for modernizing your existing applications.

You can run your applications in App Engine by using the [App Engine flexible environment](https://docs.cloud.google.com/appengine/docs/flexible) or the [App Engine standard environment](https://docs.cloud.google.com/appengine/docs/standard). You can also choose to simultaneously use both environments for your application and allow your services to take advantage of each environment's individual benefits.

## App Engine environments

App Engine is well suited to applications that are designed using a [microservice](https://wikipedia.org/wiki/Microservices) architecture, especially if you decide to utilize both environments. Use the following sections to learn and understand which environment best meets your application's needs.

### When to choose the standard environment

Application instances run in a [sandbox](https://en.wikipedia.org/wiki/Sandbox_\(computer_security\)), using the runtime environment of a supported language listed below. 

Applications that need to deal with rapid scaling. 

The standard environment is optimal for applications with the following characteristics: 

  * Intended to **run for free or at very low cost** , where you pay only for what you need and when you need it. For example, your application can scale to 0 instances when there is no traffic. 
  * Experiences **sudden and extreme spikes of traffic** which require immediate scaling. 



### When to choose the flexible environment

Application instances run within Docker containers on Compute Engine virtual machines (VM). 

Applications that receive consistent traffic, experience regular traffic fluctuations, or meet the parameters for scaling up and down gradually. 

The flexible environment is optimal for applications with the following characteristics: 

  * Runs in a Docker container that includes a custom runtime or source code written in **other programming languages**. 
  * Uses or depends on frameworks that include **native code**. 
  * Accesses the resources or services of your Google Cloud project that reside in the **Compute Engine network**. 



## Compare high-level features

The following table summarizes the differences between the two environments:

Feature | Standard environment | Flexible environment  
---|---|---  
Instance startup time | Seconds | Minutes  
Maximum request timeout |  Depends on the [ runtime and type of scaling.](https://docs.cloud.google.com/appengine/docs/standard/how-instances-are-managed#timeout) | 60 minutes  
Background threads | Yes, with restrictions | Yes  
Background processes | No | Yes  
SSH debugging | No | Yes  
Scaling | Manual, Basic, Automatic | Manual, Automatic  
Scale to zero | Yes | No, minimum 1 instance  
Writing to local disk |  Read and write access to the `/tmp` directory.  | Yes, ephemeral (disk initialized on each VM startup)  
Modifying the runtime | No | Yes (through Dockerfile)  
Deployment time | Seconds | Minutes  
Automatic in-place security patches | Yes | Yes (excludes container image runtime)  
Access to Google Cloud APIs & Services such as [Cloud Storage](https://docs.cloud.google.com/storage/docs), [Cloud SQL](https://docs.cloud.google.com/sql/docs), [Memorystore](https://docs.cloud.google.com/memorystore/docs), [Google Tasks](https://docs.cloud.google.com/tasks/docs) and others.  | Yes | Yes  
WebSockets | No | Yes  
Supports installing third-party binaries |  Yes  | Yes  
Location | [Locations](https://docs.cloud.google.com/appengine/docs/standard/locations) for the standard environment | [Locations](https://docs.cloud.google.com/appengine/docs/flexible/locations) for the flexible environment  
Pricing |  Based on [instance hours](https://docs.cloud.google.com/appengine/pricing#standard_instance_pricing) |  Based on usage of [vCPU, memory, and persistent disks](https://docs.cloud.google.com/appengine/pricing#app-engine-flexible-environment-pricing)  
  
Also see the in-depth [comparison of the environments](https://docs.cloud.google.com/appengine/docs/flexible/flexible-for-standard-users).

## Compare App Engine and Cloud Run

To compare features and learn how to migrate to Cloud Run, see [Compare App Engine and Cloud Run](https://docs.cloud.google.com/appengine/migration-center/run/compare-gae-with-run).

## Compare the flexible environment to Compute Engine

The App Engine flexible environment has the following differences to Compute Engine:

  * The flexible environment VM instances are restarted on a weekly basis. During restarts, Google's management services apply any necessary operating system and security updates.

  * You always have root access to Compute Engine VM instances. By default, SSH access to the VM instances in the flexible environment is disabled. If you choose, you can enable root access to your app's VM instances.

  * Code deployments can take longer as container images are built by using the Cloud Build service.

  * The geographical region of a flexible environment VM instance is determined by the location that you specify for the [App Engine application](https://docs.cloud.google.com/appengine/docs/flexible/locations) of your Google Cloud project. Google's management services ensures that the VM instances are co-located for optimal performance.




## Migrate from the standard environment to the flexible environment

If you have an application in the standard environment, you might want to move some services to the flexible environment. For guidance, see the recommendations for in the [comparison of the environments](https://docs.cloud.google.com/appengine/docs/flexible/flexible-for-standard-users).

To migrate specific services for Python, Java, Go, and PHP, see [Migrate services from the standard environment to the flexible environment](https://docs.cloud.google.com/appengine/docs/flexible/migrating).

##  Try it for yourself 

If you're new to Google Cloud, create an account to evaluate how Ruby standard environment performs in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

[ Try Ruby standard environment free ](https://console.cloud.google.com/freetrial)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
