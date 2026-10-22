---
url: https://docs.cloud.google.com/endpoints/docs/frameworks/about-cloud-endpoints-frameworks/
title: Cloud Endpoints Frameworks for App Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:53:43.838553+00:00
---

# Cloud Endpoints Frameworks for App Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/frameworks/about-cloud-endpoints-frameworks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ Endpoints Frameworks ](https://docs.cloud.google.com/endpoints/docs/frameworks/about-cloud-endpoints-frameworks)



Send feedback 

#  Cloud Endpoints Frameworks Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Endpoints Frameworks is a [web framework](https://wikipedia.org/wiki/Web_framework) for the App Engine standard [Python 2.7 and Java 8 runtime environments](https://docs.cloud.google.com/appengine/docs/standard/runtimes). Cloud Endpoints Frameworks provides the tools and libraries that allow you to generate REST APIs and client libraries for your application.

**Note:** Endpoints Frameworks doesn't support the PHP, Go, or Node.js runtimes.

Like other web frameworks, Endpoints Frameworks handles the low-level communication details of HTTP requests and responses for your application. When a client sends a request to your API, Endpoints Frameworks routes the request's URL to the function or method in your code that processes the request. Endpoints Frameworks converts the return value to JSON and sends the response. You add metadata (by using annotations in Java and decorators in Python) to your source code. The metadata defines the [surface](https://docs.cloud.google.com/endpoints/docs/frameworks/glossary#surface) of the REST APIs for your application.

### Java
    
    
    @ApiMethod(name = "echo")
    public Message echo(Message message, @Named("n") @Nullable Integer n) {
      return doEcho(message, n);
    }

In the example code, the [annotations](https://docs.cloud.google.com/endpoints/docs/frameworks/java/annotate-code) begin with the `@` character.

### Python
    
    
    @endpoints.method(
        # This method takes a ResourceContainer defined above.
        ECHO_RESOURCE,
        # This method returns an Echo message.
        EchoResponse,
        path="echo",
        http_method="POST",
        name="echo",
    )
    def echo(self, request):
        output_message = " ".join([request.message] * request.n)
        return EchoResponse(message=output_message)

In the example code, the [decorators](https://docs.cloud.google.com/endpoints/docs/frameworks/python/create_api) begin with the `@` character.

With Endpoints Frameworks, you don't have to deploy a third-party web server (such as Apache Tomcat or Gunicorn) with your application. You annotate or decorate the code and deploy your application as you normally would to the [App Engine standard environment](https://docs.cloud.google.com/appengine/docs/standard).

## API management

The [Extensible Service Proxy (ESP)](https://docs.cloud.google.com/endpoints/docs/frameworks/glossary#extensible_service_proxy) provides API management features for Endpoints for OpenAPI and Endpoints for gRPC. ESP runs in a container alongside each instance of your backend.

Because the App Engine standard environment didn't support multi-container deployments when Endpoints Frameworks was under development, Endpoints Frameworks doesn't use ESP. Instead, Endpoints Frameworks includes a built-in [API gateway](https://wikipedia.org/wiki/API_management) that provides API management features that are comparable to the features that ESP provides for Endpoints for OpenAPI and Endpoints for gRPC.

Endpoints Frameworks intercepts all requests and performs any necessary checks (such as authentication) before forwarding the request to the API backend. When the backend responds, Endpoints Frameworks gathers and reports telemetry. You can view metrics for your API on the **Endpoints Services** page in the Google Cloud console.

You can use Endpoints Frameworks with or without API management functionality. Use of Endpoints Frameworks without API management functionality is offered at no charge. API management functionality is charged according to the [Endpoints pricing page](https://cloud.google.com/endpoints/pricing).

## Limitations

  * Endpoints Frameworks is supported only on the App Engine standard Python 2.7 and Java 8 runtime environments.
  * Endpoints Frameworks doesn't support the Node.js, PHP, and Go runtime environments on the App Engine standard environment.
  * Endpoints Frameworks doesn't support the App Engine flexible environment.
  * Endpoints Frameworks doesn't support Cloud Run functions, Compute Engine, and Google Kubernetes Engine.



## What's next

  * To learn more about the differences between ESP and Endpoints Frameworks, see [Comparing Extensible Service Proxy and Endpoints Frameworks](https://docs.cloud.google.com/endpoints/docs/frameworks/frameworks-extensible-service-proxy#endpoints_frameworks).

  * For information on the language-specific libraries and tools, see the following:

    * [About Endpoints Frameworks for Java](https://docs.cloud.google.com/endpoints/docs/frameworks/java/about-cloud-endpoints-frameworks)
    * [About Endpoints Frameworks for Python](https://docs.cloud.google.com/endpoints/docs/frameworks/python/about-cloud-endpoints-frameworks)
  * To learn how to configure, deploy, and send requests to a sample API, see the following:

    * [Getting started with Endpoints Frameworks for Java](https://docs.cloud.google.com/endpoints/docs/frameworks/java/get-started-frameworks-java)
    * [Getting started with Endpoints Frameworks for Python](https://docs.cloud.google.com/endpoints/docs/frameworks/python/get-started-frameworks-python)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
