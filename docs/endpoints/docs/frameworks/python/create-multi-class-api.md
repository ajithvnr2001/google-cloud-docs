---
url: https://docs.cloud.google.com/endpoints/docs/frameworks/python/create-multi-class-api/
title: Creating an API implemented with multiple classes \u00a0|\u00a0 Cloud Endpoints Frameworks for App Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:53:35.653057+00:00
---

# Creating an API implemented with multiple classes  |  Cloud Endpoints Frameworks for App Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/frameworks/python/create-multi-class-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ Endpoints Frameworks ](https://docs.cloud.google.com/endpoints/docs/frameworks/about-cloud-endpoints-frameworks)



Send feedback 

#  Creating an API implemented with multiple classes Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to decorate your code to create an API implemented in multiple classes. If you implemented your API using only one class, see [Creating the API](https://docs.cloud.google.com/endpoints/docs/frameworks/python/create_api). See [Decorators](https://docs.cloud.google.com/endpoints/docs/frameworks/python/decorators-reference) for detailed information about all the available decorators.
    
    
    api_collection = endpoints.api(name="library", version="v1.0")
    
    
    @api_collection.api_class(resource_name="shelves")
    class Shelves(remote.Service):
        @endpoints.method(Request, Response)
        def list(self, request):
            return Response()
    
    
    @api_collection.api_class(resource_name="books", path="books")
    class Books(remote.Service):
        @endpoints.method(Request, Response, path="bookmark")
        def get_bookmark(self, request):
            return Response()
    
        @endpoints.method(Request, Response)
        def best_sellers_list(self, request):
            return Response()
    
    

Replace `api_collection` with any name you want, so long as you use the same name for each class in the API. You must precede each class in the API with the decorator as shown in the preceding snippet.

### About the `resource_name` argument

The optional `resource_name` argument for `api_class` is the name of the class that you want to expose in the API; this is the name that shows up in the API Explorer, prepended to any methods exposed in the class.

### About the `path` argument

The optional `path` argument for `api_class` specifies the relative location at which the class methods appear in the URL. In the preceding example, a `path` isn't specified for the class `Shelves`, so its methods are accessible under the root, `/_ah/api/library/v1`. For example, the `list` method is accessible from the path `/_ah/api/library/v1/list`.

If you specify a `path` argument for a class, the specified path is appended to the root. In the preceding example, the `path` argument `books` is specified for the class `Books`, so its methods are accessible under `/_ah/api/library/v1/books`. For example, the `best_sellers_list` method is accessible from the path `/_ah/api/library/v1/books/best_sellers_list`.

The `path` argument is optional for methods. If you don't specify a `path`, the method name is used. Any paths specified for methods are appended to the class path. In the preceding example, `bookmark` is specified as the `path` for the `get_bookmark` method. The `get_bookmark` method is accessible from the path `/_ah/api/library/v1/books/bookmark`.

You can override the class `path` argument by specifying a method `path` argument that begins with `/`. For example, assume that the `get_bookmark` method in the `Books` class has the following path:
    
    
    @endpoints.method(Request, Response, path='/bookmark')
    def get_bookmark(self, request):
      return Response()
    

The leading slash changes the path for the `get_bookmark` method to `/_ah/api/library/v1/bookmark`.

### Serving a multi-class API

In your [endpoints.api_server](https://docs.cloud.google.com/endpoints/docs/frameworks/python/api_server) code that creates the API server, you supply the name you assigned for your `api_class` collection. For example, where the collection name is `api_collection` you would create the server as follows:
    
    
    api = endpoints.api_server([api_collection])

## What's next

  * [Creating the API](https://docs.cloud.google.com/endpoints/docs/frameworks/python/create_api)
  * [Decorators](https://docs.cloud.google.com/endpoints/docs/frameworks/python/decorators-reference)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
