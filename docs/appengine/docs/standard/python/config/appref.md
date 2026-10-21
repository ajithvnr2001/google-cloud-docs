---
url: https://docs.cloud.google.com/appengine/docs/standard/python/config/appref/
title: App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T21:26:49.315612+00:00
---

# App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python/config/appref/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  App Engine standard environment Stay organized with collections  Save and categorize content based on your preferences. 

The App Engine standard environment is based on container instances running on Google's infrastructure. Containers are preconfigured with one of several available runtimes.

The standard environment makes it easy to build and deploy an application that runs reliably even under heavy load and with large amounts of data.

Applications run in a secure, sandboxed environment, allowing the standard environment to distribute requests across multiple servers and scale servers to meet traffic demands. Your application runs within its own secure, reliable environment that is independent of the hardware, operating system, or physical location of the server.

## Standard environment languages and runtimes

The standard environment supports the following languages:

[ Go ](https://docs.cloud.google.com/appengine/docs/standard/go/runtime)

[ Java ](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/runtime)

[ Node.js ](https://docs.cloud.google.com/appengine/docs/standard/nodejs/runtime)

[ PHP ](https://docs.cloud.google.com/appengine/docs/standard/php-gen2/runtime)

[ Python ](https://docs.cloud.google.com/appengine/docs/standard/python3/runtime)

[ Ruby ](https://docs.cloud.google.com/appengine/docs/standard/ruby/runtime)

## Instance classes

The _instance class_ determines the amount of memory and CPU available to each instance, the amount of [free quota](https://docs.cloud.google.com/appengine/docs/standard/quotas#Instances), and the [cost per hour](https://cloud.google.com/appengine/pricing#standard_instance_pricing) after your app exceeds the free quota.

For all runtime generations, the memory limit includes the memory your app uses along with the memory that the runtime itself needs to run your app. The Java runtimes use more memory to run your app than other runtimes.

To override the default instance class, use the [`instance_class` setting](https://docs.cloud.google.com/appengine/docs/standard/python3/config/appref#instance_class) in your app's `app.yaml` file.

Instance Class | Memory Limit | CPU Limit | Supported Scaling Types  
---|---|---|---  
F1 (default) | 384 MB | 600 MHz | automatic  
F2 | 768 MB | 1.2 GHz | automatic  
F4 | 1536 MB | 2.4 GHz | automatic  
F4_1G | 3072 MB | 2.4 GHz | automatic  
B1 | 384 MB | 600 MHz | manual, basic  
B2 (default) | 768 MB | 1.2 GHz | manual, basic  
B4 | 1536 MB | 2.4 GHz | manual, basic  
B4_1G | 3072 MB | 2.4 GHz | manual, basic  
B8 | 3072 MB | 4.8 GHz | manual, basic  
  
The CPU values and limits reported in the instance class table don't reflect a fixed clock speed in the CPU. Instead, they represent the instance's allocated relative compute power or performance tier on the [shared-core](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n1-shared-core) instance type.

System tools might report the total physical memory of the underlying host machine. This is different from the instance's enforced memory limit, which is the maximum memory available to the instance's isolated sandbox environment. Exceeding this "Memory Limit", not the host's total RAM, might cause performance issues.

**Important:** When you [view your bill](https://docs.cloud.google.com/billing/docs/how-to/reports), you will not see the names of the individual instance classes in your billing line items. Instead, you see instance hours from the "B" classes reported as "Backend Instances", and instance hours from the "F" classes reported as "Frontend Instances". The bill will apply the appropriate multiple of instance hours for each instance class you use. For example, if you use an F4 instance for one hour, you see "Frontend Instance" billing for four instance hours at the F1 rate. 

## Quotas and limits

The standard environment gives you 1 GiB of data storage and traffic for free, which can be increased by enabling paid applications. However, some features impose limits unrelated to quotas to protect the stability of the system. For more details on quotas, including how you can edit them to suit your needs, see [Quotas](https://docs.cloud.google.com/appengine/docs/standard/quotas).

##  Try it for yourself 

If you're new to Google Cloud, create an account to evaluate how App Engine performs in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

[ Try App Engine free ](https://console.cloud.google.com/freetrial)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
