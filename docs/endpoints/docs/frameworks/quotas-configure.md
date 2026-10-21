---
url: https://docs.cloud.google.com/endpoints/docs/frameworks/quotas-configure/
title: Configuring quotas \u00a0|\u00a0 Cloud Endpoints Frameworks for App Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:38:16.968708+00:00
---

# Configuring quotas  |  Cloud Endpoints Frameworks for App Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/frameworks/quotas-configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ Endpoints Frameworks ](https://docs.cloud.google.com/endpoints/docs/frameworks/about-cloud-endpoints-frameworks)



Send feedback 

#  Configuring quotas Stay organized with collections  Save and categorize content based on your preferences. 

**Beta**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes how to configure quotas for your API in Cloud Endpoints Frameworks. For an overview of the functionality provided by quotas, see [About quotas](https://docs.cloud.google.com/endpoints/docs/frameworks/quotas-overview).

### Java

The following procedure assumes that you have already:

  * [Written and annotated the code](https://docs.cloud.google.com/endpoints/docs/frameworks/java/annotate-code) for your API.
  * [Added API management](https://docs.cloud.google.com/endpoints/docs/frameworks/java/adding-api-management).
  * [Deployed your API](https://docs.cloud.google.com/endpoints/docs/frameworks/java/test-deploy).
  * Configured your API to use an API key. This is needed so that Endpoints Frameworks can identify the Google Cloud project that the calling application is associated with. See [Sharing APIs protected by API key](https://docs.cloud.google.com/endpoints/docs/frameworks/java/restricting-api-access-with-api-keys-frameworks#sharing_apis_protected_by_api_key) for more information.



To configure quotas on your API:

  1. In the file that contains the [API-scoped annotations](https://docs.cloud.google.com/endpoints/docs/frameworks/java/annotations), add the following to your @Api annotation:
         
         limitDefinitions = {
               @ApiLimitMetric(
                 name = "YOUR_METRIC_NAME",
                 displayName = "YOUR_METRIC_DISPLAY_NAME",
                 limit = YOUR_QUOTA_LIMIT)
         }
         

     * Replace `YOUR_METRIC_NAME` with a name that describes the API requests counter.
     * Replace `YOUR_METRIC_DISPLAY_NAME` with the text that is displayed on **Endpoints** > **Services** > **Quotas** page to identify the quota.
     * Replace `YOUR_QUOTA_LIMIT` with an integer value. This is the number of requests that an application associated with a consumer's Google Cloud project can make in a minute. For example:
           
           @Api(
                 name = "echo",
                 version = "v1",
                 namespace =
                   @ApiNamespace(
                     ownerDomain = "echo.example.com",
                     ownerName = "echo.example.com",
                     packagePath = ""
                   ),
                 limitDefinitions = {
                   @ApiLimitMetric(
                     name = "read-requests",
                     displayName = "Read requests",
                     limit = 1000),
                   @ApiLimitMetric(
                     name = "list-requests",
                     displayName = "List requests",
                     limit = 100),
                   @ApiLimitMetric(
                     name = "write-requests",
                     displayName = "Write requests",
                     limit = 50),
                 }
             )
           

  2. For each method that you want to apply a quota to, add the following to the `@ApiMethod` annotation:
         
         metricCosts = {
                      @ApiMetricCost(
                        name ="YOUR_METRIC_NAME",
                        cost = YOUR_COST)
         }
         

     * Replace `YOUR_METRIC_NAME` with a name that you specified in the `limitDefinitions` parameter in the `@Api` annotation.
     * Replace `YOUR_COST` with an integer value that specifies the cost for each request.

For example:
           
           @ApiMethod(name = "echo",
                        metricCosts = {
                          @ApiMetricCost(
                            name = "read-requests",
                            cost = 1)
                        })
             public Message echo(Message message, @Named("n") @Nullable Integer n) {
               // ...function code here...
             }
           

  3. [Deploy the API](https://docs.cloud.google.com/endpoints/docs/frameworks/java/test-deploy).




See the following for more information on the annotations used in quotas:

  * [`@ApiLimitMetric`](https://docs.cloud.google.com/endpoints/docs/frameworks/java/annotations#apilimitmetric)
  * [`@ApiMethod`: Method-scoped annotations](https://docs.cloud.google.com/endpoints/docs/frameworks/java/annotations#apimethod_method-scoped_annotations)



### Python

The following procedure assumes that you have already:

  * Installed version 2.4.5 or later of the Endpoints Frameworks library.
  * [Created your API](https://docs.cloud.google.com/endpoints/docs/frameworks/python/create_api).
  * [Created a web server](https://docs.cloud.google.com/endpoints/docs/frameworks/python/api_server).
  * [Added API management](https://docs.cloud.google.com/endpoints/docs/frameworks/python/adding-api-management).
  * [Deployed your API](https://docs.cloud.google.com/endpoints/docs/frameworks/python/test-deploy).
  * Configured your API to use an API key. This is needed so that Endpoints Frameworks can identify the Google Cloud project that the calling application is associated with. See [Sharing APIs protected by API key](https://docs.cloud.google.com/endpoints/docs/frameworks/python/restricting-api-access-with-api-keys-frameworks#sharing_apis_protected_by_api_key) for more information.



To configure quotas on your API:

  1. In the file that contains the [API decorator](https://docs.cloud.google.com/endpoints/docs/frameworks/python/decorators-reference#defining_the_api_endpointsapi), create a list of `LimitDefinition` instances, similar to the following:
         
         quota_limits = [
           endpoints.LimitDefinition(
             "YOUR_METRIC_NAME",
             "YOUR_METRIC_DISPLAY_NAME",
             limit)
         ]
         

     * Replace `YOUR_METRIC_NAME` with a name that describes the API requests counter.
     * Replace `YOUR_METRIC_DISPLAY_NAME` with the text that is displayed on **Endpoints** > **Services** > **Quotas** page to identify the quota.
     * Replace `limit` with an integer value. This is the number of requests that an application associated with a consumer's Google Cloud project can make in a minute. For example:
           
           quota_limits = [
               endpoints.LimitDefinition('read-requests', 'Read Requests', 1000),
               endpoints.LimitDefinition('list-requests', 'List Requests', 100),
               endpoints.LimitDefinition('write-requests', 'Write Requests', 50),
             ]
           

  2. Add your quota to the API decorator by assigning it to the `limit_definitions` argument. For example:
         
         @endpoints.api(name='bookstore',
                          version='v1',
                          limit_definitions=quota_limits)
         

  3. For each method that you want to apply a quota to, assign a dictionary to the `METRIC_COSTS` argument of the [method decorator](https://docs.cloud.google.com/endpoints/docs/frameworks/python/decorators-reference#defining_an_api_method_endpointsmethod). The key must be a name that you specified in the `limit_definitions` argument to the API decorator, and the value is an integer that specifies the cost for each request. For example:
         
         @endpoints.method(path='shelves/{shelf}',
                             http_method='GET',
                             metric_costs={'read-requests': 1})
           def get_shelf(self, request):
           # ...function code here...
         

  4. [Deploy the API](https://docs.cloud.google.com/endpoints/docs/frameworks/python/test-deploy).




See the following for more information on the decorators used in quotas:

  * [`limit_definitions`](https://docs.cloud.google.com/endpoints/docs/frameworks/python/decorators-reference#limit_definitions)
  * [Defining an API method (`@endpoints.method`)](https://docs.cloud.google.com/endpoints/docs/frameworks/python/decorators-reference#defining_an_api_method_endpointsmethod)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
