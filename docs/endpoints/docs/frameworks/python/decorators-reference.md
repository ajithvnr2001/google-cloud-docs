---
url: https://docs.cloud.google.com/endpoints/docs/frameworks/python/decorators-reference/
title: Decorators \u00a0|\u00a0 Cloud Endpoints Frameworks for App Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:46:04.585572+00:00
---

# Decorators  |  Cloud Endpoints Frameworks for App Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/frameworks/python/decorators-reference/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ Endpoints Frameworks ](https://docs.cloud.google.com/endpoints/docs/frameworks/about-cloud-endpoints-frameworks)
  * [ Reference ](https://docs.cloud.google.com/endpoints/docs/frameworks/ref-endpoints-logs)



Send feedback 

#  Decorators Stay organized with collections  Save and categorize content based on your preferences. 

The Cloud Endpoints Frameworks for Python decorators describe API configuration, methods, parameters, and other vital details that define the properties and behavior of the Endpoint.

This page describes the available decorators in detail. For information about using the decorators to create your API, see the following:

  * [Creating the API](https://docs.cloud.google.com/endpoints/docs/frameworks/python/create_api)
  * [Creating an API implemented with multiple classes](https://docs.cloud.google.com/endpoints/docs/frameworks/python/create-multi-class-api)



## Defining the API (`@endpoints.api`)

You can supply several arguments to `@endpoints.api` to define your API. The following table describes the available arguments:

@endpoints.api Arguments | Description | Example  
---|---|---  
`allowed_client_ids` | Required if your API uses authentication. List of client IDs for clients allowed to request tokens. For more information, see Allowed client IDs and audiences. | `allowed_client_ids=['1-web-apps.apps.googleusercontent.com','2-android-apps.apps.googleusercontent.com', endpoints.API_EXPLORER_CLIENT_ID`]  
`api_key_required` | Optional. Used to restrict access to requests that supply an [API key](https://docs.cloud.google.com/endpoints/docs/frameworks/python/restricting-api-access-with-api-keys-frameworks). | `api_key_required=True`  
`audiences` | Required if your API requires authentication and if you are supporting Android clients. For Google ID tokens, this can be a list of client IDs on behalf of which tokens are requested. If the tokens are issued by third-party authentication providers, such as Auth0, this needs to be a dictionary mapping from auth issuer names to audience lists. For more information, see Allowed client IDs and audiences. | `audiences=['1-web-apps.apps.googleusercontent.com']` or `audiences={"auth0": ["aud-1.auth0.com", "aud-2.auth0.com"]}`  
`base_path` | Optional. Used to serve your API from the specified path. If you specify this argument, you must also change the `handlers` section in your `app.yaml` file. | See [Serving your API from a different path](https://docs.cloud.google.com/endpoints/docs/frameworks/python/api_server#serve_from_different_path).  
`canonical_name` | Optional. Used to specify a different or more readable name for the API _in the client library_. This name is used to generate names in the client library; the backend API continues to use the value specified in the `name` property.For example, if your API has the `name` set to **dfaanalytics** , you could use this property to specify a canonical name of **DFA Group Analytics** ; the generated client classes would then contain the name `DfaGroupAnalytics`.You should include the relevant spaces between the names as shown; these are replaced by the appropriate camel casing or underscores. | `canonical_name='DFA Analytics'`  
`description` | A short description of the API. This is exposed in the discovery service to describe your API, and might optionally also be used to generate documentation as described in [Generating client libraries](https://docs.cloud.google.com/endpoints/docs/frameworks/python/gen_clients). | `description='Sample API for a simple game'`  
`documentation` | Optional. The URL where users can find documentation about this version of the API. This is surfaced in the API Explorer "Learn More" highlight at the top of the API Explorer page to allow users to learn about your service. | `documentation='http://link_to/docs'`  
`hostname` | The host name of your App Engine application. The [Endpoints Frameworks command-line tool](https://docs.cloud.google.com/endpoints/docs/frameworks/python/endpoints_tool) uses the value that you specify here when it generates a Discovery document or an OpenAPI document. If you don't specify the host name here, you must specify the host name in the `application` field of your [`app.yaml`](https://docs.cloud.google.com/appengine/docs/standard/python/config/appref) file or specify your project ID when you deploy your App Engine application. | `hostname='your_app_id.appspot.com'`  
`issuers` | Optional. The custom JWT issuer configurations. This should be a dictionary mapping from issuer names to `endpoints.Issuer` objects. | `issuers={"auth0": endpoints.Issuer("https://test.auth0.com", "https://test.auth0.com/.well-known/jwks.json")}`  
`name` | Required. The name of the API, which is used as the prefix for all of the API's methods and paths. The `name` value:

  * _Must_ begin with a lowercase letter.
  * _Must_ match the regular expression `[a-z]+[A-Za-z0-9]`; that is, the rest of the name can consist of uppercase and lowercase letters or numbers.

To deploy multiple APIs as part of a single service, all API names must match the regular expression `[a-z][a-z0-9]{0,39}` that is, the name must start with a lowercase letter, the rest of the characters must be either lowercase letters or numbers, and the maximum length is 40 characters. | `name='yourApi'` or `name='yourapi'`  
`limit_definitions` | Optional. Used to define quotas for your API. See limit_definitions for more information. |   
`owner_domain` | Optional. The domain name of the entity that owns the API. Used together with `owner_name` to provides hints to properly name the client library when it is generated for this API. (The package path is the reverse of the `owner_domain` and `package_path` if supplied. The default is to use `appid.apppost.com` | `owner_domain='your-company.com'`  
`owner_name` | Optional. The name of the entity that owns the API. Used together with `owner_domain` to provides hints to properly name the client library when it is generated for this API. | `owner_name='Your-Company'`  
`package_path` | Optional. Is used to further scope The "package" this API belongs to, with values separated by `/` specifying logical groupings of APIs.For example, specifying `cloud/platform` results in the client library path set to `cloud/platform/<ApiName>` and client library package set to `cloud.plaform.<ApiName>`. | `package_path='cloud/platform'`  
`scopes` | If not supplied, the default is the email scope (`https://www.googleapis.com/auth/userinfo.email`), which is required for OAuth. You can override this to specify more [OAuth 2.0 scopes](https://docs.cloud.google.com/appengine/docs/python/oauth) if you wish. You can also override the scopes specified here for a particular API method by specifying different scopes in the `@endpoints.method` decorator. However, if you do define more than one scope, note that the scope check passes if the token is minted for _any_ of the specified scopes. To require multiple scopes, specify a single string with a space between each scope. | `scopes=['ss0', 'ss1 and_ss2']`  
`title` | Optional. The text displayed in API Explorer as the title of your API, and exposed in the discovery and the directory services. | `title='My Backend API'`  
`version` | Required. Specifies your Cloud Endpoints version. This value appears in your API's path. If you specify a version string compatible with the [SemVer standard](https://semver.org/spec/v2.0.0.html), only the major version number appears in your API's path when you deploy your API. For example, an API called `echo` with version `2.1.0` would have a path similar to `/echo/v2`. If you update the `echo` API to version `2.2.0` and deploy a backwards-compatible change, the path remains `/echo/v2`. This allows you to update the API version number when you make a backwards-compatible change without breaking existing paths for your clients. But if you update the `echo` API to version `3.0.0` (because you are deploying a breaking change), the path is changed to `/echo/v3`. | `version='v1'` or `version='2.1.0'`  
  
### `limit_definitions`

**Beta**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

To define [quotas](https://docs.cloud.google.com/endpoints/docs/frameworks/quotas-overview) for your API, you specify the optional `limit_definitions` argument to `@endpoints.api`. To configure a quota, you must also:

  * Install version 2.4.5 or later of the Endpoints Frameworks library.
  * Add the `metric_costs` argument to the method decorator for each method that you want to apply a quota to.



See [Configuring quotas](https://docs.cloud.google.com/endpoints/docs/frameworks/quotas-configure) for all the steps required to set up a quota.

You specify a list of one or more `LimitDefinition` instances, similar to the following:
    
    
    quota_limits = [
                  endpoints.LimitDefinition(
                    "name",
                    "Display name",
                    limit)
    ]
    

Each `LimitDefinition` instance must have the following values:

**Element** | **Description**  
---|---  
name | The name for the API request counter. Typically, this is the type of request (for example, “read-requests” or “write-requests”) that uniquely identifies the quota.  
Display name | The text displayed to identify the quota on the **Quotas** tab on the **Endpoints** > **Services** page. This text is also displayed to consumers of your API on the **Quotas** page of IAM & admin and API & Services. The display name must be a maximum of 40 characters. For readability purposes, the text “per minute per project” is automatically appended to the display name on the Quotas pages. To maintain consistency with the display names of Google services listed on the Quotas pages that consumers of your API see, we recommend the following for the display name: 

  * Use "Requests" when you only have one metric.
  * When you have multiple metrics, each should describe the type of request and contain the word “requests” (for example “Read requests” or “Write requests”).
  * Use "Quota units" instead of "Requests" when any of the costs for this quota is greater than 1.

  
limit | An integer value that is the maximum number of requests per minute per consumer project for the quota.  
  
#### Example
    
    
    quota_limits = [
      endpoints.LimitDefinition('read-requests', 'Read Requests', 1000),
      endpoints.LimitDefinition('list-requests', 'List Requests', 100),
      endpoints.LimitDefinition('write-requests', 'Write Requests', 50)
    ]
    
    @endpoints.api(name='bookstore',
                   version='v1',
                   limit_definitions=quota_limits)

### Allowed client IDs and audiences

For OAuth2 authentication, an OAuth2 token is issued to a specific client ID, which means that this client ID can be used for restricting access to your APIs. When you register Android applications in the Google Cloud console, you create a client ID for it. This client ID is the one requesting an OAuth2 token from Google for authentication purposes. When the backend API is protected by auth, an OAuth2 access token is sent and opened by Endpoints Frameworks for App Engine, the client ID is extracted from the token, and then the ID is compared to the backend's declared acceptable client ID list (the `allowed_client_ids` list).

The `allowed_client_ids` list should consist of all the client IDs you have obtained through the [Google Cloud console](https://console.cloud.google.com/) for your web, [Android](https://docs.cloud.google.com/endpoints/docs/frameworks/python/consume_android), and other client apps. This means that the clients must be known at API build-time. If you specify an empty list, _no_ clients can access the API.

Note that in each API method where you want to check for proper authentication, you must call `endpoints.get_current_user()`. See [Authenticating users](https://docs.cloud.google.com/endpoints/docs/frameworks/python/authenticating-users) for more information.

If you use the `allowed_client_ids` argument and you want to test authenticated calls to your API by using the API Explorer, you must supply its client ID in the list of `allowed_client_ids` by specifying the constant `endpoints.API_EXPLORER_CLIENT_ID`. Notice that if `allowed_client_ids` contains only `endpoints.API_EXPLORER_CLIENT_ID`, and you deploy your API, your API is still publicly discoverable and publicly accessible in the API Explorer.

**Note:** If you don't use the `allowed_client_ids` argument, you don't need to supply the API Explorer client ID.

#### About audiences

**Note:** The `audiences` argument is currently used _only for Android clients_.

The `allowed_client_ids` list _protects the backend API_ from unauthorized clients. But further protection is needed to _protect the clients_ , so that their authentication token works only for the intended backend API. For Android clients, this mechanism is the `audiences` argument, in which you specify the client ID of the backend API.

Note that when you create a Google Cloud console project, a default client ID is automatically created and named for use by the project. When you upload your backend API into App Engine, it uses that client ID. This is the web client ID mentioned in API [auth](https://docs.cloud.google.com/endpoints/docs/frameworks/python/auth).

#### Third-party authentication token issuer

If your application accepts authentication tokens that aren't Google ID tokens and are issued by third-party issuers, you need to properly set `audiences` and `issuers` arguments in `@endpoints.api` to provide the information about the third-party issuers. For example:
    
    
    @endpoints.api(
            audiences={'auth0': ['aud-1.auth0.com', 'aud-2.auth0.com']},
            issuers={'auth0': endpoints.Issuer('https://test.auth0.com',
                                               'https://test.auth0.com/.well-known/jwks.json')})
    class GreetingApi(remote.Service):
    

## Defining an API method (`@endpoints.method`)

You can set the `audiences`, `scopes`, and `allowed_client_ids` settings for the entire API by using `@endpoints.api`, or for a method, by using `@endpoints.method`. If these settings are specified at both the API and the method level, the method setting overrides.

To create a method in your API, decorate the corresponding Python method with `@endpoints.method`, supplying arguments to configure the use of the method. For example, you specify which request and response `Message` classes to use.

**Important:** Certain query parameters are reserved and cannot be used in an API method. For a list of these, see [Standard query parameters](https://developers.google.com/drive/web/query-parameters)

The available arguments are listed in the following table:

`@endpoints.method` Arguments | Description | Example  
---|---|---  
`allowed_client_ids` | This setting overrides the equivalent attribute specified in `@endpoints.api`. For more information, see Allowed client IDs and audiences. | `['1-web-apps.apps.googleusercontent.com', '2-android-apps.apps.googleusercontent.com']`  
`api_key_required` | Optional. Used to restrict access to requests that supply an [API key](https://docs.cloud.google.com/endpoints/docs/frameworks/python/restricting-api-access-with-api-keys-frameworks). | `api_key_required=True`  
`audiences` | Overrides the equivalent argument specified in `@endpoints.api`. For more information, see Allowed client IDs and audiences. | `['1-web-apps.apps.googleusercontent.com']`  
`metric_costs` | Optional. Indicates that the method has a quota limit. This is a dictionary with the following key:value pairs: 

  * **name:** A name that you specified in the limit_definitions argument to the API decorator.
  * **cost:** An integer that specifies the cost for each request. The cost allows methods to consume at different rates from the same quota. For example, if a quota has a limit of 1000 and a cost of 1, the calling application can make 1000 requests per minute before going over the limit. With a cost of 2 for the same quota, a calling application can make only 500 requests per minute before going over the limit.

| `metric_costs={'read-requests': 1}`  
`http_method` | The HTTP method to use. If you don't set this, `'POST'` is used by default. | `'GET'`  
`name` | An alternative name for this method. The `name` value:

  * _Must_ begin with lowercase.
  * _Must_ match the regular expression `[a-z]+[A-Za-z0-9]*`.

| `'yourApi'`  
`path` | The URI path to access this method. If you don't set this, the name of the Python method is used. If you plan to [add API management](https://docs.cloud.google.com/endpoints/docs/frameworks/python/adding-api-management), don't include a trailing slash in the path. | `'yourapi/path'`  
`Request Message` class | The [Google Protocol RPC](https://docs.cloud.google.com/appengine/docs/python/tools/protorpc) `Request Message` class to be used in the method call. Alternatively, you can supply the name of the class. | `YourRequestClass`  
`Response Message` class | The [Google Protocol RPC](https://docs.cloud.google.com/appengine/docs/python/tools/protorpc) `Response Message` class to be used in the method call. Alternatively, you can supply the name of the class. | `YourResponseClass`  
  
## Using `ResourceContainer` for path or query string arguments

If the request contains path or query string arguments, you cannot use a simple `Message` class as described in [Create the API](https://docs.cloud.google.com/endpoints/docs/frameworks/python/create_api#creating_the_api). Instead, you must use a `ResourceContainer` class, as follows:

  1. Define a `Message` class that has all the arguments that are passed in the request body. If there aren't any arguments in the request body, you don't need to define a `Message` class: simply use `message_types.VoidMessage`.) For example:
         
         class Greeting(messages.Message):
             """Greeting that stores a message."""
         
             message = messages.StringField(1)

  2. Define a `ResourceContainer` with the `Message` class that you defined in the previous step as the first parameter. Specify the path and query string arguments in the subsequent parameters. For example:
         
         MULTIPLY_RESOURCE = endpoints.ResourceContainer(
             Greeting,
             times=messages.IntegerField(2, variant=messages.Variant.INT32, required=True),

where the first argument is the `Message` class for the data in the request body and `times` is a number expected in the path or query string accompanying the request.

  3. Supply the `ResourceContainer` to the method handling the request, in the first parameter replacing the request `Message` class that would otherwise be supplied in that location. This snippet shows both the `ResourceContainer` and the `endpoints.method`:
         
         # This ResourceContainer is similar to the one used for get_greeting, but
         # this one also contains a request body in the form of a Greeting message.
         MULTIPLY_RESOURCE = endpoints.ResourceContainer(
             Greeting,
             times=messages.IntegerField(2, variant=messages.Variant.INT32, required=True),
         )
         
         @endpoints.method(
             # This method accepts a request body containing a Greeting message
             # and a URL parameter specifying how many times to multiply the
             # message.
             MULTIPLY_RESOURCE,
             # This method returns a Greeting message.
             Greeting,
             path="greetings/multiply/{times}",
             http_method="POST",
             name="greetings.multiply",
         )
         def multiply_greeting(self, request):
             return Greeting(message=request.message * request.times)
         

  4. Add the `path` parameter as shown, to include your API.

  5. If your `ResourceContainer` has a required argument, a client request must include it either in a query string (for example, `yourApi?times=2`), or the URL path (for example, `yourApi/2`). However, in order for your API to receive an argument value by using the URL path, you must also add the argument name to the API path as shown for the `{times}` argument in `path='yourApi/{times}`.




## What's next

  * [Creating the API](https://docs.cloud.google.com/endpoints/docs/frameworks/python/create_api)
  * [Creating an API implemented with multiple classes](https://docs.cloud.google.com/endpoints/docs/frameworks/python/create-multi-class-api)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
