---
url: https://docs.cloud.google.com/appengine/docs/standard/communicating-between-services/
title: Communicating between your services \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:44:29.705678+00:00
---

# Communicating between your services  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/communicating-between-services/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Communicating between your services Stay organized with collections  Save and categorize content based on your preferences. 

### Region ID

The `REGION_ID` is an abbreviated code that Google assigns based on the region you select when you create your app. The code does not correspond to a country or province, even though some region IDs may appear similar to commonly used country and province codes. For apps created after February 2020, `REGION_ID.r` is included in App Engine URLs. For existing apps created before this date, the region ID is optional in the URL.

Learn more [about region IDs](https://docs.cloud.google.com/appengine/docs/standard/python/how-requests-are-routed#region-id). 

OK

You can use various methods to communicate between your App Engine services or with other services, including Google Cloud services and external applications.

The simplest approach for communicating with your App Engine service is to send targeted HTTP requests, where the URL includes the name or ID of a resource. For example, you can include the ID of a service or version that you want to target, in addition to the corresponding Google Cloud project ID:
    
    
    https://VERSION-dot-SERVICE-dot-PROJECT_ID.REGION_ID.r.appspot.com
    

Note that the combined length of `VERSION-dot-SERVICE-dot-PROJECT_ID`, where `VERSION` is the name of your version, `SERVICE ` is the name of your service, and `PROJECT_ID` is your project ID, cannot be longer than 63 characters and cannot start or end with a hyphen. If the combined length is longer than 63 characters, you might see Error `DNS address could not be found. `

Learn more about requests in App Engine:

  * [How requests are handled](https://docs.cloud.google.com/appengine/docs/standard/how-requests-are-handled): Learn how your application receives requests and sends responses.
  * [How requests are routed](https://docs.cloud.google.com/appengine/docs/standard/how-requests-are-routed): Learn how to target your services, including how to define HTTPS URLs.
  * Learn how to authorize the requests between your services and other Google Cloud services: 
    * [Provide credentials for Application Default Credentials](https://docs.cloud.google.com/docs/authentication/provide-credentials-adc)
    * [Using user-managed service accounts](https://docs.cloud.google.com/appengine/docs/standard/user-managed-service-accounts)



Your App Engine services can also communicate using [Pub/Sub](https://docs.cloud.google.com/pubsub/docs), which provides reliable asynchronous many-to-many messaging between processes, including App Engine. These processes can be individual instances of your application, services, or even external applications.

To share data across databases and your App Engine app or some other external application, see [Understanding Data and File Storage](https://docs.cloud.google.com/appengine/docs/standard/storage-options).

If you use the legacy bundled services, you can also pass requests between services and from services to external endpoints using the [URL Fetch](https://docs.cloud.google.com/appengine/docs/legacy/standard/python/issue-requests) API.

Additionally, services in the standard environment that reside within the same Google Cloud project can also use one of the App Engine APIs for the following tasks:

  * Share a single [memcache](https://docs.cloud.google.com/appengine/docs/legacy/standard/python/memcache) instance.
  * Collaborate by assigning work between services through [Task Queues](https://docs.cloud.google.com/appengine/docs/legacy/standard/python/taskqueue).



## Private Communication

### Communication between services in the same project

You can allow an App Engine standard service to communicate with another App Engine service in the same project without having to expose the destination service to the public internet.

To allow communication between services in the same project:

  1. Configure ingress controls by adjusting the destination service's [ingress settings](https://docs.cloud.google.com/appengine/docs/standard/ingress-settings) to allow "internal" traffic only.

The "internal" setting allows requests from the project's VPC networks only. This includes App Engine resources from a client app on the same network when egress traffic is routed over a connector. All other traffic from the internet or other Google Cloud projects, including other App Engine services, is blocked.

**Note:** The "internal" traffic setting blocks all traffic from additional Google Cloud services that do not use the VPC network, such as URLFetch, Cloud Tasks, and Pub/Sub, even within the same project.
  2. Route the traffic over a [Serverless VPC Access connector](https://docs.cloud.google.com/vpc/docs/configure-serverless-vpc-access#appengine):

     1. For each App Engine version sending private traffic to other app endpoints, attach the version to a Serverless VPC Access connector belonging to one of the Google Cloud project's own networks, not a Shared VPC network.

     2. Ensure Private Google Access is enabled for the subnet used by the Serverless VPC Access connector.

     3. Configure one of the following:

        * Configure client requests to use the `private.googleapis.com` IP range by adding a DNS entry for the destination hostname. Follow [DNS configuration](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#config-domain) to add the DNS hostname, but be sure to configure the private zone to be for `appspot.com` rather than `googleapis.com`. Also ensure that traffic is directed to the destination app's `appspot.com` address, not a custom domain. Your app can only be reached on the `private.googleapis.com` IP range using this `appspot.com` domain.

        * Configure the client app to [send](https://docs.cloud.google.com/appengine/docs/standard/connecting-vpc#manage) `all-traffic` through the Serverless VPC Access connector, instead of configuring requests to use the `private.googleapis.com` IP range.




### Communication between services in different projects

You can have private access between Google Cloud projects when apps running in projects belong to a Shared VPC network that is configured to invoke an app running in the Shared VPC network's host project.

To use this pattern, follow the previous steps for communicating between services in the same project. In the standard environment, attach each client version to a Serverless VPC Access connector on the Shared VPC network. 

Other methods of communication between projects using internal access are not possible in App Engine.

## Reserved URL paths

It is not possible to use the following URL paths:

  * Paths ending with `/eventlog`
  * Paths starting with `/_ah/`
  * Some paths ending with `z`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
