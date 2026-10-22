---
url: https://docs.cloud.google.com/endpoints/docs/frameworks/python/restricting-api-access-with-api-keys-frameworks/
title: Restricting API access with API keys \u00a0|\u00a0 Cloud Endpoints Frameworks for App Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:53:24.948373+00:00
---

# Restricting API access with API keys  |  Cloud Endpoints Frameworks for App Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/frameworks/python/restricting-api-access-with-api-keys-frameworks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ Endpoints Frameworks ](https://docs.cloud.google.com/endpoints/docs/frameworks/about-cloud-endpoints-frameworks)



Send feedback 

#  Restricting API access with API keys Stay organized with collections  Save and categorize content based on your preferences. 

You can use [API keys](https://docs.cloud.google.com/endpoints/docs/frameworks/python/when-why-api-key) to restrict access to specific API methods or all methods in an API. This page describes how to restrict API access to those clients that have an API key and also shows how to create an API key. 

If you set an API key requirement in your API, requests to the protected method, class, or API are rejected unless they have a key generated in your project or within other projects belonging to developers with whom you have [granted access to enable your API](https://docs.cloud.google.com/endpoints/docs/frameworks/control-api-callers). The project that the API key was created in is not logged and is not added to the request header. You can, however, view the Google Cloud project that a client is associated with on the **Endpoints Services** page, as described in [Filter for a specific consumer project](https://docs.cloud.google.com/endpoints/docs/frameworks/monitoring-your-api#filter_for_a_specific_consumer_project).

For information on which Google Cloud project an API key should be created in, see Sharing APIs protected by API key.

## Restricting access to all API methods

To require an API key for all calls into the API, add `api_key_required=True` to your [API decorator](https://docs.cloud.google.com/endpoints/docs/frameworks/python/decorators-reference#defining_the_api_endpointsapi). For example:
    
    
    @endpoints.api(name='echo', version='v1', api_key_required=True)
    class EchoApi(remote.Service):
    #...
    

## Restricting access to specific API methods

To require an API key for all calls to a specific API method, add `api_key_required=True` to your [API method decorator](https://docs.cloud.google.com/endpoints/docs/frameworks/python/decorators-reference#defining_an_api_method_endpointsmethod). For example:
    
    
    endpoints.method(
      # This method takes an Echo message.
      ECHO_RESOURCE,
      # This method returns an Echo message.
      EchoResponse,
      path='echo',
      http_method='POST',
      name='echo_api_key',
      api_key_required=True)
    def echo_api_key(self, request):
      output_content = '\n'.join([request.content] * request.n)
      return EchoResponse(content=output_content)
    

## Removing API key restriction for a method

To turn off API key validation for an API or API method, remove `api_key_required=True` (Python) or `apiKeyRequired = AnnotationBoolean.TRUE` (Java) from your API or method decorator or annotation. Then recompile and re-deploy.

## Calling an API using an API key

If an API or API method requires an API key, supply the key using a query parameter named `key`, as shown in this cURL example:
    
    
    curl \
        -H "Content-Type: application/json" \
        -X POST \
        -d '{"message": "echo"}' \
        "${HOST}/_ah/api/echo/v1/echo_api_key?key=${API_KEY}"
    

where `HOST` and `API_KEY` are variables containing your API host name and API key, respectively. Replace `echo` with the name of your API, and `v1` with the version of your API.

## Sharing APIs protected by API key

API keys are associated with the Google Cloud project in which they have been created. If you have decided to require an API key for your API, the Google Cloud project that the API key gets created in depends on the answers to the following questions:

  * Do you need to distinguish between the callers of your API so that you can use Endpoints features such as [quotas](https://docs.cloud.google.com/endpoints/docs/frameworks/quotas-overview)? 
  * Do all the callers of your API have their own Google Cloud projects?
  * Do you need to set up different [API key restrictions](https://docs.cloud.google.com/docs/authentication/api-keys#api_key_restrictions)? 



You can use the following decision tree as a guide for deciding which Google Cloud project to create the API key in.

![API key decision tree](https://docs.cloud.google.com/static/endpoints/docs/images/api_key_decision_tree.png)

### Grant permission to enable the API

When you need to distinguish between callers of your API, and each caller has their own Google Cloud project, you can grant principals permission to enable the API in their own Google Cloud project. This way, users of your API can create their own API key for use with your API.

For example, suppose your team has created an API for internal use by various client programs in your company, and each client program has their own Google Cloud project. To distinguish between callers of your API, the API key for each caller must be created in a different Google Cloud project. You can grant your coworkers permission to enable the API in the Google Cloud project that the client program is associated with.

To let users create their own API key:

  1. In the Google Cloud project in which your API is configured, grant each user the [permission to enable your API](https://docs.cloud.google.com/endpoints/docs/frameworks/control-api-callers). 
  2. Contact the users, and let them know that they can [enable your API](https://docs.cloud.google.com/endpoints/docs/frameworks/enable-api) in their own Google Cloud project and [ create an API key](https://docs.cloud.google.com/docs/authentication/api-keys#creating_an_api_key). 



### Create a separate Google Cloud project for each caller

When you need to distinguish between callers of your API, and not all of the callers have Google Cloud projects, you can create a separate Google Cloud project and API key for each caller. Before creating the projects, give some thought to the project names so that you can easily identify the caller associated with the project.

For example, suppose you have external customers of your API, and you have no idea how the client programs that call your API were created. Perhaps some of the clients use Google Cloud services and have a Google Cloud project, and perhaps some don't. To distinguish between the callers, you must create a separate Google Cloud project and API key for each caller.

To create a separate Google Cloud project and API key for each caller:

  1. Create a separate project for each caller.
  2. In each project, [enable your API](https://docs.cloud.google.com/endpoints/docs/frameworks/enable-api) and [ create an API key](https://docs.cloud.google.com/docs/authentication/api-keys#creating_an_api_key).
  3. Give the API key to each caller.



### Create an API key for each caller

When you don't need to distinguish between callers of your API, but you want to add API key restrictions, you can create a separate API key for each caller in the same project.

To create an API key for each caller in the same project:

  1. In either the project that your API is configured in, or a project that your [API is enabled in](https://docs.cloud.google.com/endpoints/docs/frameworks/enable-api), create an API key for each customer that has the [API key restrictions](https://docs.cloud.google.com/docs/authentication/api-keys#api_key_restrictions) that you need.
  2. Give the API key to each caller.



### Create one API key for all callers

When you don't need to distinguish between callers of your API, and you don't need to add API restrictions, but you still want to require an API key (to prevent anonymous access, for example), you can create one API key for all callers to use.

To create one API key for all callers: 

  1. In either the project that your API is configured in, or a project that your [API is enabled in](https://docs.cloud.google.com/endpoints/docs/frameworks/enable-api), create an API key for all callers that has the [API key restrictions](https://docs.cloud.google.com/docs/authentication/api-keys#api_key_restrictions) that you need.
  2. Give the same API key to every caller.



## What's next

  * [Securing an API key](https://docs.cloud.google.com/docs/authentication/api-keys#securing_an_api_key)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
