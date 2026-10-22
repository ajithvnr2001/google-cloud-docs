---
url: https://docs.cloud.google.com/appengine/docs/flexible/troubleshooting/
title: Troubleshoot App Engine errors \u00a0|\u00a0 App Engine flexible environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:30:31.707675+00:00
---

# Troubleshoot App Engine errors  |  App Engine flexible environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/flexible/troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Flexible environment ](https://docs.cloud.google.com/appengine/docs/flexible)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Troubleshoot App Engine errors Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the troubleshooting process for errors you might encounter while using App Engine. For information about incidents affecting Google Cloud services, refer to the [Google Cloud Service Health Dashboard](https://status.cloud.google.com/summary) and [All incidents reported for App Engine](https://status.cloud.google.com/products/kchyUtnkMHJWaAva8aYc/history).

See the following pages for guidance on how to resolve issues related to your app:

  * [Troubleshoot deployment issues](https://docs.cloud.google.com/appengine/docs/flexible/troubleshooter/deployment)
  * [Troubleshoot serving issues](https://docs.cloud.google.com/appengine/docs/flexible/troubleshooter/serving)
  * [Troubleshoot elevated latency in your app](https://docs.cloud.google.com/appengine/docs/flexible/troubleshooter/latency)
  * [App Engine connectivity strategies](https://docs.cloud.google.com/appengine/docs/flexible/troubleshooter/connectivity)



## App Engine troubleshooting strategies

The following sections explain how you can apply general troubleshooting strategies to resolve your error. If you continue to encounter errors even after following the steps in the troubleshooting guides, see What's next.

### Output good logs using Cloud Logging

Troubleshooting your app running on App Engine is easier if you have good application logs for debugging. Ensure your application writes logs in a way that [correlates request logs with the application logs](https://docs.cloud.google.com/appengine/docs/flexible/writing-application-logs#correlate_logs).

With correlated logs you can identify the request that needs further analysis, find the request trace, and analyze the root cause of the issue. For more information on writing logs, see [Write application logs](https://docs.cloud.google.com/appengine/docs/flexible/writing-application-logs#writing_app_logs).

### Resolve unexpected latency

If you encounter issues with latency, do the following:

  1. Check if the latency is affecting all requests to your service or only a small percentage. The [App Engine latency dashboard](https://docs.cloud.google.com/appengine/docs/flexible/monitoring-and-alerting-latency#checking_the_latency_dashboard) shows 50th, 95th, and 99th percentile latency.

If you have high latency on all three of these metrics, you have high latency for at least 50% of your requests. If you only see high latency in the 99th percentile graph, you have high latency in 1% of your requests.

  2. Identify the request with high latency to understand the source of latency. You can use Cloud Trace or Cloud Logging to understand how long a particular request has taken. For more information, see [Understanding app latency](https://docs.cloud.google.com/appengine/docs/flexible/monitoring-and-alerting-latency#understanding_app_latency).

To identify requests with high latency using Cloud Logging, apply the `traceSampled=true` filter to correlate logs in Cloud Logging with traces in Cloud Trace. For more information, see [Integrate with Cloud Logging](https://docs.cloud.google.com/trace/docs/trace-log-integration).

  3. Try the following steps to fix latency issues, and improve service performance:

     * Adjust your [CPU, memory, and disk resources](https://docs.cloud.google.com/appengine/docs/flexible/reference/app-yaml#services).

     * Adjust [scaling settings](https://docs.cloud.google.com/appengine/docs/flexible/how-instances-are-managed#instance_scaling).

     * Consider using [Profiler](https://docs.cloud.google.com/appengine/docs/flexible/cloud-profiler).

     * Modify your source code.




For more information on how to troubleshoot elevated latency issues, see [Troubleshoot elevated latency in your app](https://docs.cloud.google.com/appengine/docs/flexible/troubleshooter/latency).

### Resolve issues with connectivity

By default, your App Engine service is accessible on the public internet, however, you can modify the service to have more restrictions on ingress and egress network connectivity.

You can restrict ingress connections with the ingress settings, or through App Engine firewall rules. If you have trouble connecting to your App Engine service from VPC networks or internet resources, check the following:

  * [Ingress settings](https://docs.cloud.google.com/appengine/docs/flexible/ingress-settings)
  * [App Engine firewall](https://docs.cloud.google.com/appengine/docs/flexible/understanding-firewalls)



To resolve other connectivity issues, do the following:

  * Set an instance into [debug mode](https://docs.cloud.google.com/appengine/docs/flexible/debugging-an-instance), and SSH to the instance while it continues to take live traffic. After connecting to the instance, you can debug the instance using common command line tools.

  * Check the [firewall rules on your VPC network](https://docs.cloud.google.com/firewall/docs/firewalls) to make sure traffic isn't blocked.

  * Check if you have [disabled the external IP](https://docs.cloud.google.com/appengine/docs/flexible/disable-external-ip).




For more information on how to troubleshoot connectivity issues, see [App Engine connectivity strategies](https://docs.cloud.google.com/appengine/docs/flexible/troubleshooter/connectivity).

### What's next

If you can't find a solution to your problem in the App Engine documentation, follow these steps:

  * Open a support case by contacting [Cloud Customer Care](https://cloud.google.com/support-hub).
  * Get support from the community by [asking questions on StackOverflow](https://stackoverflow.com/questions/tagged/google-app-engine), or search for similar issues using the `google-app-engine` tag.
  * Open bugs or feature requests by using the [public issue tracker](https://docs.cloud.google.com/support/docs/issue-trackers).



For more information, see [App Engine community](https://docs.cloud.google.com/appengine/docs/flexible/community).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
