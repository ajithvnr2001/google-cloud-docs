---
url: https://docs.cloud.google.com/endpoints/docs/openapi/lifecycle-management/
title: API lifecycle management \u00a0|\u00a0 Cloud Endpoints with OpenAPI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:00:44.428662+00:00
---

# API lifecycle management  |  Cloud Endpoints with OpenAPI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/openapi/lifecycle-management/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ OpenAPI ](https://docs.cloud.google.com/endpoints/docs/openapi)



Send feedback 

#  API lifecycle management Stay organized with collections  Save and categorize content based on your preferences. 

OpenAPI | gRPC

This page describes the Cloud Endpoints API versioning features and provides best practices for versioning and staging your Endpoints API. The information on this page is applicable for APIs using the [OpenAPI specification](https://github.com/OAI/OpenAPI-Specification). For APIs using Cloud Endpoints Frameworks for App Engine standard environment, see [Handling API versioning: Java](https://docs.cloud.google.com/endpoints/docs/frameworks/java/handling-api-versioning) or [Handling API versioning: Python](https://docs.cloud.google.com/endpoints/docs/frameworks/python/handling-api-versioning).

We recommend that you follow the same basic principles that Google uses for API versioning and service staging:

  * Include the following in your OpenAPI configuration file before you deploy the initial version:

    * Set the version number in the `info.version` field. We recommend that you use a version string which includes a major version and a minor version, for example, `1.0`.
    * Set the `basePath` field to include the major version number. We recommend that you use a base path formatted as the letter `v` followed by major version number, for example, `/v1`.
  * When you need to make a backwards-compatible change, such as adding a new method, increment the minor version number (1.2, 1.3, etc.) in the `info.version` field and redeploy. See [Versioning an API](https://docs.cloud.google.com/endpoints/docs/openapi/versioning-an-api) for details.

  * When you need to make a change to an existing method that breaks client code, make a copy of your OpenAPI configuration file, and make the following changes:

    * Increment the major version number (2.0, 3.0, etc.) in the `info.version` field.
    * Increment the major version number (/v2, /v3, etc.) in the `basePath` field.

Deploy both versions of your OpenAPI configuration files and redeploy the backend, which now has both versions of the method. See [Versioning an API](https://docs.cloud.google.com/endpoints/docs/openapi/versioning-an-api) for details.

  * Implement all major API versions in a single backend. This recommendation:

    * Simplifies routing because requests to a specific version are based on the path, as in the previous example.
    * Simplifies configuration and deployment. You use the same Google Cloud project and backend for all major versions of the API, and you deploy all versions of your API at the same time.
    * Keeps your costs down by avoiding running superfluous backends.
  * Stage your API in a separate Google Cloud project before you deploy to your production Google Cloud project. See Staging services for details.




The use of major and minor version numbers in Endpoints corresponds to the definitions in [Semantic versioning](http://semver.org/). Although Endpoints doesn't require that you increment the patch version number in your OpenAPI configuration file and deploy the configuration when you deploy a bug fix in your backend code, you can choose to do so if you like.

## Cloud Endpoints API versioning features

The [Extensible Service Proxy (ESP)](https://docs.cloud.google.com/endpoints/docs/openapi/about-cloud-endpoints) has the ability to manage multiple major versions of your API concurrently in a single Google Cloud project and backend as long as the APIs don't have overlapping paths. For example:
    
    
    http://echo-api.endpoints.my-project.cloud.goog/v1/echo
    http://echo-api.endpoints.my-project.cloud.goog/v2/echo
    

This lets your customers pick which version they want to use and control when they migrate to the new version. The ESP tags each request with the version number before routing the request to the applicable method in the backend. Because each request is tagged with a version number:

  * The graphs and logs in **Endpoints** > **Services** display requests from each major API version and the aggregate total across all versions. You can filter your view to a specific version. This gives you a clear idea of how much traffic each version is getting. The logs can even tell you which clients are using which version.

  * When you redeploy your API with a minor version number update, subsequent activity is labeled with the new version number in the graphs and logs. This provides you with a labeled history of your deployments.

  * When you remove a version of an API, the graphs and logs continue to display data in the time range that the API was active.




## API lifecycle example

This section describes a typical evolution of a service.

**Version 1**

You initially deploy version 1 of My Awesome Echo API service. The API is served from `my-api.endpoints.my‐awesomeproject.cloud.goog/v1/echo`. In the graphs and logs in **Endpoints** > **Services** , you see all traffic at `1.0`.

**Version 1.1**

Your customers request a new feature, so you add a new method. In your OpenAPI configuration file, you add the new method and increment the `info.version` field to `1.1`. You increment the minor version number because this change doesn't break client code. You deploy and test your change in a staging environment to ensure it works.

Next, you deploy the OpenAPI configuration and the API backend to the production environment. The API is still served from `my-api.endpoints.my‐awesomeproject.cloud.goog/v1/echo`, but now callers can make requests to the new method. Because you didn't change the interface to the old methods, your customers don't need to change and redeploy their clients; clients can continue to send requests to the old method the same as before.

In **Endpoints** > **Services** , the traffic served is now at version `1.1`. If you select an earlier time range to display, it displays the previous version in the graphs and logs, which provides a labeled history of your deployments.

**Version 2.0**

Over time, you realize that you need to make a backwards-incompatible change to an existing method. Because it's important that you don't break your customers' client code, you decide to maintain two versions of the API. You leave the old method as it is, and implement the new version of the method. You create another OpenAPI configuration file for version 2.0, and configure the new version to be served from `my-api.endpoints.my‐awesomeproject.cloud.goog/v2/echo`. Your original OpenAPI configuration file still points to the old version of the method, while the new OpenAPI configuration file points to the new version of the method.

You deploy both version 1 and version 2 OpenAPI configuration files at the same time, and redeploy the backend, which now contains both versions of the method. (See [Versioning an API](https://docs.cloud.google.com/endpoints/docs/openapi/versioning-an-api) for details.)

After you deploy, **Endpoints** > **Services** shows that you are serving two versions of your API, and you can see how much traffic each version is getting. Your v1 clients can continue to call `/v1`, but they can also call `/v2` to use the new version of the method. How you handle versioning in your backend code depends on the API framework you are using. For an example using servlets, see [Endpoints & Java with multiple versions sample](https://github.com/GoogleCloudPlatform/java-docs-samples/tree/master/endpoints/multiple-versions).

**Disabling version 1**

In time, as your clients migrate and you see that all traffic to v1 has stopped, you can stop serving it. To remove version 1 of your API, deploy only the version 2 OpenAPI configuration file and redeploy the backend. You can now safely remove the code that implemented version 1 from your backend. **Endpoints** > **Services** retains the historical data from version 1.x.

## Staging services

As a best practice, we recommend that you stage updates to your Endpoints service so that you can test your service before it reaches your customers. We also recommend that you create a separate Google Cloud project for staging your service, so that it is isolated from production. For example, Google quotas are generally shared by resources within a project. Thus, if you put the staging service in the same project as the production service, an errant for loop, for example, could cause an outage in your production service.

We recommend that you devise a Google Cloud project name that clearly indicates it is for staging. A common naming strategy is to use the same name as your production Google Cloud project name, but with `-staging` at the end. You might also want to put `-prod` on production projects to make it clear that the project holds production services.

Service names on Google Cloud must be unique. Because you specify the name of the service in the OpenAPI configuration file, you need to either maintain separate API configuration files for the staging and production projects, or use one set of API configuration files and devise a process where you change the service name to match the name of the project that you are deploying to.

## What's next

  * [Endpoints & Java with multiple versions sample](https://github.com/GoogleCloudPlatform/java-docs-samples/tree/master/endpoints/multiple-versions)
  * [Planning your Google Cloud projects](https://docs.cloud.google.com/endpoints/docs/openapi/planning-cloud-projects)
  * [Versioning an API](https://docs.cloud.google.com/endpoints/docs/openapi/versioning-an-api)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
