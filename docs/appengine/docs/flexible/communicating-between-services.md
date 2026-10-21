---
url: https://docs.cloud.google.com/appengine/docs/flexible/communicating-between-services/
title: Communicating between your services \u00a0|\u00a0 App Engine flexible environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:40:09.547550+00:00
---

# Communicating between your services  |  App Engine flexible environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/flexible/communicating-between-services/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Flexible environment ](https://docs.cloud.google.com/appengine/docs/flexible)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Communicating between your services Stay organized with collections  Save and categorize content based on your preferences. 

### Region ID

The `REGION_ID` is an abbreviated code that Google assigns based on the region you select when you create your app. The code does not correspond to a country or province, even though some region IDs may appear similar to commonly used country and province codes. For apps created after February 2020, `REGION_ID.r` is included in App Engine URLs. For existing apps created before this date, the region ID is optional in the URL.

Learn more [about region IDs](https://docs.cloud.google.com/appengine/docs/flexible/python/how-requests-are-routed#region-id). 

OK

You can use various methods to communicate between your App Engine services or with other services, including Google Cloud services and external applications.

The simplest approach for communicating with your App Engine service is to send targeted HTTP requests, where the URL includes the name or ID of a resource. For example, you can include the ID of a service or version that you want to target, in addition to the corresponding Google Cloud project ID:
    
    
    https://VERSION-dot-SERVICE-dot-PROJECT_ID.REGION_ID.r.appspot.com
    

Note that the combined length of `VERSION-dot-SERVICE-dot-PROJECT_ID`, where `VERSION` is the name of your version, `SERVICE ` is the name of your service, and `PROJECT_ID` is your project ID, cannot be longer than 63 characters and cannot start or end with a hyphen. If the combined length is longer than 63 characters, you might see Error `DNS address could not be found. `

Learn more about requests in App Engine:

  * [How requests are handled](https://docs.cloud.google.com/appengine/docs/flexible/how-requests-are-handled): Learn how your application receives requests and sends responses.
  * [How requests are routed](https://docs.cloud.google.com/appengine/docs/flexible/how-requests-are-routed): Learn how to target your services, including how to define HTTPS URLs.
  * Learn how to authorize the requests between your services and other Google Cloud services: 
    * [Provide credentials for Application Default Credentials](https://docs.cloud.google.com/docs/authentication/provide-credentials-adc)
    * [Using user-managed service accounts](https://docs.cloud.google.com/appengine/docs/flexible/user-managed-service-accounts)



Your App Engine services can also communicate using [Pub/Sub](https://docs.cloud.google.com/appengine/docs/flexible/writing-and-responding-to-pub-sub-messages), which provides reliable asynchronous many-to-many messaging between processes, including App Engine. These processes can be individual instances of your application, services, or even external applications.

To share data across databases and your App Engine app or some other external application, see [Understanding Data and File Storage](https://docs.cloud.google.com/appengine/docs/flexible/storage-options).

## Private Communication

### Communication between services in the same project

You can allow an App Engine flexible service to communicate with another App Engine service in the same project without having to expose the destination service to the public internet.

  1. Configure the destination service's [ingress settings](https://docs.cloud.google.com/appengine/docs/flexible/ingress-settings) to allow "internal" traffic only.

  2. Ensure the source app version is not deployed to a Shared VPC network located in a different project.




### Communication between services in different projects

You can have private access between Google Cloud projects when apps running in projects belong to a Shared VPC network that is configured to invoke an app running in the Shared VPC network's host project.

To use this pattern, follow the previous steps for communicating between services in the same project. In the flexible environment, [deploy](https://docs.cloud.google.com/appengine/docs/flexible/using-shared-vpc) each client version to the same Shared VPC network. 

Other methods of communication between projects using internal access are not possible in App Engine.

## Reserved URL paths

It is not possible to use the following URL paths:

  * Paths ending with `/eventlog`
  * Paths starting with `/_ah/`
  * Some paths ending with `z`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
