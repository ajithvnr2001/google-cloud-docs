---
url: https://docs.cloud.google.com/appengine/docs/flexible/python/how-requests-are-routed/
title: How requests are routed \u00a0|\u00a0 App Engine flexible environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:02:25.824241+00:00
---

# How requests are routed  |  App Engine flexible environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/flexible/python/how-requests-are-routed/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Flexible environment ](https://docs.cloud.google.com/appengine/docs/flexible)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  How requests are routed Stay organized with collections  Save and categorize content based on your preferences. 

### Region ID

The `REGION_ID` is an abbreviated code that Google assigns based on the region you select when you create your app. The code does not correspond to a country or province, even though some region IDs may appear similar to commonly used country and province codes. For apps created after February 2020, `REGION_ID.r` is included in App Engine URLs. For existing apps created before this date, the region ID is optional in the URL.

Learn more [about region IDs](https://docs.cloud.google.com/appengine/docs/flexible/python/how-requests-are-routed#region-id). 

OK

Go Java Node.js PHP Python Ruby .NET Custom

This page describes how HTTP requests from users reach the appropriate version of a service. Requests can be routed in the following ways:

  * Routing with URLs
  * Routing with a dispatch file
  * Routing with Cloud Load Balancing



These options apply only to deployed apps. When you are testing locally, the routing behavior depends on the particular runtime and development environment that you're using.

## Routing with URLs

Once your app is running in App Engine, you can use the following URL to send HTTP requests to the app:

`https://PROJECT_ID.REGION_ID.r.appspot.com`

where `PROJECT_ID` is the ID of the Google Cloud project that contains the app.

This URL sends requests to your app's default service at the version that you have configured to receive traffic.

**Note:** We [recommend](http://googleonlinesecurity.blogspot.com/2014/08/https-as-ranking-signal_6.html) using the HTTPS protocol to send requests to your app. HTTPS requests sent to the `REGION_ID.r.appspot.com` must use the string "`-dot-`" to separate subdomains instead of "`.`". You can use the simple "`.`" URL notation with your own custom domains and with HTTP requests.

### URLs for services and versions

If you create more than one service in your app, each service has its own URL. Each version of a service also has its own URL, so you can deploy and test a new version before configuring that version to receive traffic.

The URLs for specific services and versions are in the following form:

`VERSION-dot-SERVICE-dot-PROJECT_ID.REGION_ID.r.appspot.com`

You can omit `VERSION-dot-` if you don't need to target a specific version.

To retrieve the IDs of your app's services and versions, you can use any of the following tools:

### Console

In the Google Cloud console, you can view the corresponding [Instances](https://console.cloud.google.com/appengine/instances), [Services](https://console.cloud.google.com/appengine/services), and [Versions](https://console.cloud.google.com/appengine/versions) pages.

### gcloud

Run the [`gcloud app instances list`](https://docs.cloud.google.com/sdk/gcloud/reference/app/instances/list) command to list the resource IDs within a specific Google Cloud project.

### API

To programmatically retrieve resource IDs, see the [`list` methods in the Admin API](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.ListInstancesRequest).

### Example URLs

Here are some examples of URLs for App Engine, showing both the `appspot.com` domain that App Engine assigns to your app and a custom domain, which you can [set up for your app](https://docs.cloud.google.com/appengine/docs/flexible/mapping-custom-domains).

  * Sends the request to an available instance of the `default` service:
    
        
        https://PROJECT_ID.REGION_ID.r.appspot.com
        https://CUSTOM_DOMAIN

Requests are received by any version that is configured for traffic in the `default` service.

  * Sends a request to an available instance of a specific service:
    
        
        https://SERVICE_ID-dot-PROJECT_ID.REGION_ID.r.appspot.com
        https://SERVICE_ID.CUSTOM_DOMAIN

Requests are received by any version that is configured for traffic in the targeted service. If the service that you are targeting does not exist, the request gets soft routed.

  * Sends a request to an available instance of a specific version in the
`default` service:
    
        
        https://VERSION_ID-dot-default-dot-PROJECT_ID.REGION_ID.r.appspot.com
        https://VERSION_ID.CUSTOM_DOMAIN

When a service is not targeted, requests are sent to the `default` service.




### Soft routing

If a request matches the `PROJECT_ID.REGION_ID.r.appspot.com` portion of the hostname, but includes a service, version, or instance name that does not exist, then the request is routed to the `default` service. Soft routing does not apply to custom domains; requests to them will return a HTTP `404` status code if the hostname is invalid.

### Targeted routing

The following URL patterns reach their target, if they exist. Requests that don't pass through Cloud Load Balancing are never intercepted and rerouted by the patterns that you have defined in your dispatch file:

  * **Sends the request to an available instance of a specific service and version:**
        
        https://VERSION-dot-SERVICE-dot-PROJECT_ID.REGION_ID.r.appspot.com
        https://VERSION_ID.SERVICE_ID.PROJECT_ID.CUSTOM_DOMAIN


**Note:** In the flexible environment, targeting an instance is not supported. It is not possible to send requests directly to a specific instance.

## Routing with a dispatch file

You can create a dispatch file to override App Engine's URL-based routing rules and define your own custom routing rules. With a dispatch file, you can send incoming requests to a specific service based on the path or hostname in the request URL.

### Creating a dispatch file

To create a dispatch file:

  1. Create a file named `dispatch.yaml` either in the root of your project directory, or in the root directory of your `default` service.

  2. Define routing rules in the file as described see the [`dispatch.yaml`](https://docs.cloud.google.com/appengine/docs/flexible/reference/dispatch-yaml) reference.




Note the following about the routing rules:

  * You can define up to 20 routing rules. Each rule must contain the `url` and `service` elements.
  * The rules must use HTTP URL patterns that include the "`.`" notation for separating subdomains. URLs defined with the HTTPS "`-dot-`" notation are not supported.
  * The rules also apply to the URLs that you define in your [`cron.yaml` file](https://docs.cloud.google.com/appengine/docs/flexible/scheduling-jobs-with-cron-yaml).



For example, you can create a dispatch file to route mobile requests like `https://simple-sample.uc.r.appspot.com/mobile/` to a mobile frontend, and route worker requests like `https://simple-sample.uc.r.appspot.com/work/` to a static backend:
    
    
    dispatch:
      # Send all mobile traffic to the mobile frontend.
      - url: "*/mobile/*"
        service: mobile-frontend
    
      # Send all work to the one static backend.
      - url: "*/work/*"
        service: static-backend
    

### Deploying the dispatch file

To deploy the dispatch file using `gcloud`, run the following command:
    
    
    gcloud app deploy dispatch.yaml
    

## Routing with Cloud Load Balancing

Cloud Load Balancing is a separate product that enables advanced network configurations for all of your applications running on Google Cloud.

[When HTTP(S) Load Balancing is enabled for serverless apps](https://docs.cloud.google.com/load-balancing/docs/negs/serverless-neg-concepts), you can:

  * Configure your serverless app to serve from a dedicated IPv4 or IPv6 IP address that is not shared with other services.

  * Reuse the same SSL certificates and private keys that you use for Compute Engine, Google Kubernetes Engine, and Cloud Storage. This eliminates the need to manage separate certificates for serverless apps.




If the Serverless NEG specifies a service, version, or a tag, the load balancer doesn't interfere or interact with routing rules in your `dispatch.yaml` file. The `dispatch.yaml` rules are not evaluated until a serverless NEG directs traffic to App Engine. Targeted routing fails when the Serverless NEG doesn't specify service, version, or a tag, and routing relies on the rules you specify in the `dispatch.yaml` file.

Note the following:

  * We recommend that you [use ingress controls](https://docs.cloud.google.com/appengine/docs/flexible/application-security#ingress_controls) so that your app only receives requests sent from the load balancer (and the VPC if you use it). Otherwise, users can use your app's App Engine URL to bypass the load balancer, Cloud Armor security policies, SSL certificates, and private keys that are passed through the load balancer.



### Inconsistent metrics when App Engine flexible environment uses Cloud Load Balancing

The App Engine flexible environment dashboard displays all metrics only for requests routed through a flexible environment managed backend. If you use App Engine flexible environment with Cloud Load Balancing, then certain metrics in the App Engine [metrics table](https://docs.cloud.google.com/monitoring/api/metrics_gcp_a_b#gcp-appengine) are reported as metrics from the [`loadbalancing`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_i_o#gcp-loadbalancing) table instead. For more information, see [HTTP(S) Load Balancing logging and monitoring](https://cloud.google.com/load-balancing/docs/https/https-logging-monitoring).

## Understand the Region ID in URLs

The `REGION_ID` is an abbreviated code that Google assigns based on the region you select when you create your app. The code does not correspond to a country or province, even though some region IDs may appear similar to commonly used country and province codes. For apps created after February 2020, `REGION_ID.r` is included in App Engine URLs. For existing apps created before this date, the region ID is optional in the URL.

You can use the following tools to see the region ID of your app:

### Console

In the Google Cloud console, you can view the URLs for your app's [Instances](https://console.cloud.google.com/appengine/instances), [Services](https://console.cloud.google.com/appengine/services), and [Versions](https://console.cloud.google.com/appengine/versions).

All of these URLs include the region ID.

### gcloud

When you deploy an app or service, the `gcloud app deploy` command displays the URL after the deployment succeeds. This URL includes the region ID.

To view the URL for a service that is already deployed:

  1. Enter the [`gcloud app versions list`](https://docs.cloud.google.com/sdk/gcloud/reference/app/versions/list) command to list the versions of a specific service. For example, to list the versions of the default service, enter `gcloud app versions list --service=default`.

  2. Enter the [`gcloud app versions describe`](https://docs.cloud.google.com/sdk/gcloud/reference/app/versions/describe) command. The output of that command includes the version URL with the app's region ID. For example, to describe version 20191023t101741 for the default service, enter `gcloud app versions describe 20191023t101741 --service=default`




## Domain name is included in the request data

The domain name used for the request is included in the request data that is passed to your app. Therefore, you can use the request data to control how your app responds based on the domain name in the request. For example, if you want to redirect to an official domain, you can code your app to check the `Host` request header and then respond accordingly based on the domain name.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
