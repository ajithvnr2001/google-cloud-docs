---
url: https://docs.cloud.google.com/endpoints/docs/frameworks/python/create_api/
title: Creating the API using Cloud Endpoints Frameworks for Python \u00a0|\u00a0 Cloud Endpoints Frameworks for App Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:01:53.829386+00:00
---

# Creating the API using Cloud Endpoints Frameworks for Python  |  Cloud Endpoints Frameworks for App Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/frameworks/python/create_api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ Endpoints Frameworks ](https://docs.cloud.google.com/endpoints/docs/frameworks/about-cloud-endpoints-frameworks)



Send feedback 

#  Creating the API using Cloud Endpoints Frameworks for Python Stay organized with collections  Save and categorize content based on your preferences. 

An API is a remote procedure call (RPC) service that provides remote methods accessible to external clients. Each backend API consists of an RPC service class that subclasses the [`ProtoRPC remote.Service`](https://docs.cloud.google.com/appengine/docs/python/tools/protorpc) class, and one or more methods. When you define a method, you must also define [`Message` classes](https://docs.cloud.google.com/appengine/docs/python/tools/protorpc#Working_with_Messages) for the requests coming into that method and the responses returned by it. A `Message` class performs a mapping function so the incoming data can be extracted and supplied to the service method properly, or supplied properly to the outgoing response.

**Note:** The `Message` classes aren't part of the exposed API, so clients don't need to know about them.

If a request has path or query string arguments, you use a [`ResourceContainer`](https://docs.cloud.google.com/endpoints/docs/frameworks/python/decorators-reference#using_resourcecontainer_for_path_or_query_string_arguments) class for the mapping, instead of a simple `Message` class.

Finally, you need to decorate the API service class and class methods, and you need to define `Message` classes for the requests and responses.

## Creating the API

The following procedure shows how to decorate your code to create an API implemented in a single class. If you have a multi-class API, see [Creating an API implemented with multiple classes](https://docs.cloud.google.com/endpoints/docs/frameworks/python/create-multi-class-api). See [Decorators](https://docs.cloud.google.com/endpoints/docs/frameworks/python/decorators-reference) for detailed information about all the available decorators.

To create an API:

  1. Add the following required imports:
         
         import endpoints
         from endpoints import message_types
         from endpoints import messages
         from endpoints import remote

  2. Define a subclass of `remote.Service` and decorate it with `@endpoints.api`:
         
         @endpoints.api(name="echo", version="v1")
         class EchoApi(remote.Service):

Notice that your API name and the name of your service class don't need to be the same. The version number applies to the version of the API. The value that you enter becomes part of the path in the URL to your API. For more information on versions, see [Handling API versioning](https://docs.cloud.google.com/endpoints/docs/frameworks/python/handling-api-versioning).

  3. Determine what data your method expects from the request and what data is returned, and create a [`Message` class](https://docs.cloud.google.com/appengine/docs/python/tools/protorpc#Working_with_Messages) for the request body and response body:
         
         class EchoRequest(messages.Message):
             message = messages.StringField(1)
         
         
         class EchoResponse(messages.Message):
             """A proto Message that contains a simple string field."""
         
             message = messages.StringField(1)
         
         
         ECHO_RESOURCE = endpoints.ResourceContainer(
             EchoRequest, n=messages.IntegerField(2, default=1)
         )

Note that if no arguments appear in the request body, such as in a `GET` request, you can omit the `Message` class for the request and simply use the value `message_types.VoidMessage`.

If your request has path or query string arguments, replace your `Message` class with an appropriate `ResourceContainer`.

For complete information on forming and using `Message` classes, see the documentation for the [Google Protocol RPC](https://docs.cloud.google.com/appengine/docs/python/tools/protorpc) response and request `Message` classes.

  4. Create the method for your API, and decorate it with `@endpoints.method`:
         
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

If your request has path or query string data, replace the request message type with an appropriate [`ResourceContainer`](https://docs.cloud.google.com/endpoints/docs/frameworks/python/decorators-reference#using_resourcecontainer_for_path_or_query_string_arguments).

  5. Add the code to serve your API, as described in [Creating a web server](https://docs.cloud.google.com/endpoints/docs/frameworks/python/api_server).




## What's next

  * [Creating an API implemented with multiple classes](https://docs.cloud.google.com/endpoints/docs/frameworks/python/create-multi-class-api)
  * [Decorators](https://docs.cloud.google.com/endpoints/docs/frameworks/python/decorators-reference)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
