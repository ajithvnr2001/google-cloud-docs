---
url: https://docs.cloud.google.com/appengine/docs/standard/services/multitenancy/multitenancy/
title: Implementing multitenancy using Namespaces \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:44:03.874893+00:00
---

# Implementing multitenancy using Namespaces  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/services/multitenancy/multitenancy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Implementing multitenancy using Namespaces Stay organized with collections  Save and categorize content based on your preferences. 

Go Java PHP Python

The Namespaces API allows you to easily enable [multitenancy](https://docs.cloud.google.com/appengine/docs/standard/services/multitenancy) in your application, simply by selecting a namespace string for each tenant in `appengine_config.py` using the `namespace_manager` package. 

## Setting the current namespace

You can get, set, and validate namespaces using the `namespace_manager` package. The namespace manager allows you to set a current namespace for [namespace-enabled APIs](https://docs.cloud.google.com/appengine/docs/standard/services/multitenancy#App_Engine_APIs_that_use_namespaces). You set a current namespace up-front in `appengine_config.py` and the Datastore and memcache automatically use that namespace.

Most App Engine developers will use their Google Workspace (formerly G Suite) domain as the current namespace. Google Workspace lets you deploy your app to any domain that you own, so you can easily use this mechanism to configure different namespaces for different domains. Then, you can use those separate namespaces to segregate data across the domains. For more information, see [Mapping Custom Domains](https://docs.cloud.google.com/appengine/docs/standard/mapping-custom-domains).

The following code sample shows you how to set the current namespace to the Google Workspace domain that was used to map the URL. Notably, this string will be the same for all URLs mapped via the same Google Workspace domain.

To set a namespace in Python, use the App Engine configuration system `appengine_config.py` in your application's root directory. The following simple example demonstrates how to use your Google Workspace domain as the current namespace:
    
    
    from google.appengine.api import namespace_manager
    
    # Called only if the current namespace is not set.
    def namespace_manager_default_namespace_for_request():
        # The returned string will be used as the Google Apps domain.
        return namespace_manager.google_apps_namespace()
    

If you do not specify a value for `namespace`, the namespace is set to an empty string. The `namespace` string is arbitrary, but also limited to a maximum of 100 alphanumeric characters, periods, underscores, and hyphens. More explicitly, namespace strings must match the regular expression `[0-9A-Za-z._-]{0,100}`.

By convention, all namespaces starting with "`_`" (underscore) are reserved for system use. This system namespace rule is not enforced, but you could easily encounter undefined negative consequences if you do not follow it.

## Avoiding data leaks

One of the risks commonly associated with multitenant apps is the danger that data will leak across namespaces. Unintended data leaks can arise from many sources, including:

  * Using namespaces with App Engine APIs that do not yet support namespaces. For example, Blobstore does not support namespaces. If you use Namespaces with Blobstore, you need to avoid using Blobstore queries for end user requests, or Blobstore keys from untrusted sources.
  * Using an external storage medium (instead of memcache and Datastore), via `URL Fetch` or some other mechanism, without providing a compartmentalization scheme for namespaces.
  * Setting a namespace based on a user's email domain. In most cases, you don't want all email addresses of a domain to access a namespace. Using the email domain also prevents your application from using a namespace until the user is logged in.



## Deploying namespaces

The following sections describe how to deploy namespaces with other App Engine tools and APIs.

### Creating namespaces on a per user basis

Some applications need to create namespaces on a per-user basis. If you want to compartmentalize data at the user level for logged-in users, consider using [`User.user_id()`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/users) , which returns a unique, permanent ID for the user. The following code sample demonstrates how to use the Users API for this purpose:
    
    
    from google.appengine.api import users
    
    def namespace_manager_default_namespace_for_request():
        # assumes the user is logged in.
        return users.get_current_user().user_id()
    

Typically, apps that create namespaces on a per-user basis also provide specific landing pages to different users. In these cases, the application needs to provide a URL scheme dictating which landing page to display to a user.

### Using namespaces with the Datastore

By default, the Datastore uses the current namespace setting in the namespace manager for Datastore requests. The API applies this current namespace to [`Key`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/datastore/Key) or [`Query`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/datastore/Query) objects when they are created. Therefore, you need to be careful if an application stores `Key` or `Query` objects in serialized forms, since the namespace is preserved in those serializations.

If you are using deserialized `Key` and `Query` objects, make sure that they behave as intended. Most simple applications that use Datastore (`put`/`query`/`get`) without using other storage mechanisms will work as expected by setting the current namespace before calling any Datastore API.

**Note:** An application that reads Keys, or other namespace-aware objects, from untrusted sources (like the web browser client) introduces security vulnerabilities. Applications that rely on keys from untrusted sources must incorporate a security layer verifying that the current user is authorized to access the requested namespace.

`Query` and `Key` objects demonstrate the following, unique behaviors with regard to namespaces:

  * `Query` and `Key` objects inherit the current namespace when constructed, unless you set an explicit namespace.
  * When an application creates a new `Key` from an ancestor, the new `Key` inherits the namespace of the ancestor.



### Using namespaces with Memcache

By default, memcache uses the current namespace from the namespace manager for memcache requests. In most cases, you do not need to explicitly set a namespace in the memcache, and doing so could introduce unexpected bugs.

However, there are some unique instances where it is appropriate to explicitly set a namespace in the memcache. For example, your application might have common data shared across all namespaces (such as a table containing country codes).

**Warning:** If you explicitly set a namespace in the memcache, it will ignore the current settings from the namespace manager.

Using the Python API for memcache, you can get the current namespace from the namespace manager or set it explicitly when you create the memcache service. The example below sets the namespace explicitly when you store a value in memcache:
    
    
      // Store an entry to the memcache explicitly
    memcache.add("key", data, namespace='abc')

### Using namespaces with the Task Queue

By default, [push queues](https://docs.cloud.google.com/appengine/docs/standard/services/taskqueue/push) use the current namespace as set in the namespace manager at the time the task was created. In most cases, you do not need to explicitly set a namespace in the task queue, and doing so could introduce unexpected bugs.

**Warning:** Tasks in [pull queues](https://docs.cloud.google.com/appengine/docs/standard/services/taskqueue) do not provide any namespace functionality. If you use namespaces with pull queues, you need to ensure that namespaces are saved in the payload and restored as needed by the application.

Task names are shared across all namespaces. You cannot create two tasks of the same name, even if they use different namespaces. If you wish to use the same task name for many namespaces, you can simply append each namespace to the task name.

When a new task calls the task queue [`add()`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/taskqueue/Queue#add) method, the task queue copies the current namespace and (if applicable) the Google Workspace domain from the namespace manager. When the task is executed, the current namespace and Google Workspace namespace are restored.

If the current namespace is not set in the originating request (in other words, if `get_namespace()` returns `''`), you can use `set_namespace()` to set the current namespace for the task. 

There are some unique instances where it is appropriate to explicitly set a namespace for a task that works across all namespaces. For example, you might create a task that aggregates usage statistics across all namespaces. You could then explicitly set the namespace of the task. 

### Using namespaces with the Blobstore

The Blobstore is not segmented by namespace. To preserve a namespace in Blobstore, you need to access Blobstore via a storage medium that is aware of the namespace (currently only memcache, Datastore, and task queue). For example, if a blob's `Key` is stored in a Datastore entity, you can access it with a Datastore `Key` or `Query` that is aware of the namespace.

If the application is accessing Blobstore via keys stored in namespace-aware storage, the Blobstore itself does not need to be segmented by namespace. Applications must avoid blob leaks between namespaces by:

  * Not using `BlobInfo.gql()` for end-user requests. You can use BlobInfo queries for administrative requests (such as generating reports about all the applications blobs), but using it for end-user requests may result in data leaks because all BlobInfo records are not compartmentalized by namespace.
  * Not using Blobstore keys from untrusted sources.



### Setting namespaces for Datastore Queries

In the Google Cloud console, you can [set the namespace for Datastore queries](https://console.cloud.google.com/project/_/datastore/query).

If you don't want to use the default, select the namespace you want to use from the drop-down.

### Using namespaces with the Bulk Loader

The bulk loader supports a `--namespace=NAMESPACE` flag that allows you to specify the namespace to use. Each namespace is handled separately and, if you want to access all namespaces, you will need to iterate through them.

### Using namespaces with Search

When you create a new instance of `Index`, it is assigned to the current namespace by default:
    
    
    # set the current namespace
    namespace_manager.set_namespace("aSpace")
    index = search.Index(name="myIndex")
    # index namespace is now fixed to "aSpace"
    

You can also assign a namespace explicitly in the constructor:
    
    
    index = search.Index(name="myIndex", namespace="aSpace")
    

Once you've created an index spec, its namespace cannot be changed:
    
    
    # change the current namespace
    namespace_manager.set_namespace("anotherSpace")
    # the namespaceof 'index' is still "aSpace" because it was bound at create time
    index.search('hello')
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
