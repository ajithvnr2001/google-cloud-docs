---
url: https://docs.cloud.google.com/appengine/migration-center/standard/python/migrate-to-cloud-ndb/
title: Migrate to Cloud NDB \u00a0|\u00a0 App Engine migration center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:49:12.919787+00:00
---

# Migrate to Cloud NDB  |  App Engine migration center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/migration-center/standard/python/migrate-to-cloud-ndb/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Migration center ](https://docs.cloud.google.com/appengine/migration-center)
  * [ Guides ](https://docs.cloud.google.com/appengine/migration-center/standard/services/migrating-services)



Send feedback 

#  Migrate to Cloud NDB Stay organized with collections  Save and categorize content based on your preferences. 

### App Engine locations

App Engine is _regional_ , which means the infrastructure that runs your apps is located in a specific region, and Google manages it so that it is available redundantly across [all of the zones within that region](https://docs.cloud.google.com/docs/geography-and-regions).

Meeting your latency, availability, or durability requirements are primary factors for selecting the region where your apps are run. You can generally select the region nearest to your app's users, but you should consider [the locations where App Engine is available](https://cloud.google.com/about/locations/#region) as well as the [locations](https://cloud.google.com/about/locations/#region) of the other Google Cloud products and services that your app uses. Using services across multiple locations can affect your app's latency as well as its [pricing](https://cloud.google.com/appengine/pricing).

You cannot change an app's region after you set it.

**Note:** Two locations, which are called `europe-west` and `us-central` in App Engine commands and in the Google Cloud console, are called `europe-west1` and `us-central1`, respectively, elsewhere in Google documentation.

If you already created an App Engine application, you can view its region by doing one of the following:

  * Run the `gcloud app describe` command.

  * Open the [App Engine Dashboard in the Google Cloud console](https://console.cloud.google.com/appengine). The region appears near the top of the page.




OK

Cloud NDB is a client library for Python that replaces App Engine NDB. App Engine NDB enables apps to store and query data in Datastore databases. Cloud NDB enables Python 3 apps to store and query data in the same databases, however the product that manages those databases has changed from Datastore to [Firestore in Datastore mode](https://docs.cloud.google.com/datastore/docs). Although the Cloud NDB library can access any data created with App Engine NDB, some structured data types stored using Cloud NDB cannot be accessed with App Engine NDB. For that reason, migrating to Cloud NDB should be considered irreversible.

Cloud NDB is intended to replace the features in App Engine NDB, so it won't support new features of Firestore in Datastore mode. We recommend that new apps use the [Datastore mode client library](https://docs.cloud.google.com/datastore/docs/reference/libraries) instead of Cloud NDB.

For more information about Cloud NDB, see the following pages on GitHub:

  * [Cloud NDB documentation](https://googleapis.dev/python/python-ndb/latest/index.html)

  * [Cloud NDB source code](https://github.com/googleapis/python-ndb/tree/main/google/cloud/ndb)




## Comparison of App Engine NDB and Cloud NDB

Similarities:

  * Cloud NDB supports almost all of the features supported by App Engine NDB with only minor differences in method syntax.



Differences:

  * App Engine NDB APIs that rely on legacy App Engine runtime-specific services have either been updated or removed from Cloud NDB.

  * New features in Python 3 and Django eliminate the need for `google.appengine.ext.ndb.django_middleware`. Write your own middleware with just a few lines of code.

  * App Engine NDB required apps and the Datastore database to be in the same Google Cloud project, with App Engine providing credentials automatically. Cloud NDB can access Datastore mode databases in any project, as long as you authenticate your client properly. This is consistent with other Google Cloud APIs and client libraries.

  * Cloud NDB doesn't use the App Engine Memcache service to cache data.

Instead, Cloud NDB caches data in a Redis in-memory datastore managed by [Memorystore](https://docs.cloud.google.com/memorystore/docs/redis/redis-overview), [Redis](https://docs.redis.com/latest/rc/databases/create-database/), or other systems. While only Redis datastores are supported, Cloud NDB has generalized and defined caching in the abstract `GlobalCache` interface, which can support additional concrete implementations.

To access Memorystore for Redis, your app needs to use Serverless VPC Access.

Neither Memorystore for Redis nor Serverless VPC Access provide a free tier, and these products may not be available in your app's region. See Before you start migrating for more information.




The full list of differences is available in the [migration notes for the Cloud NDB GitHub project](https://github.com/googleapis/python-ndb/blob/main/MIGRATION_NOTES.md).

Code samples:

  * Basic database operations [using App Engine NDB](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/main/appengine/standard/ndb/overview/main.py)

  * Basic database operations [using Cloud NDB](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/main/appengine/standard/migration/ndb/overview/main.py)




## Before you migrate

Before you start migrating:

  1. If you have not done so already, set up your [Python development environment](https://docs.cloud.google.com/python/docs/setup) to use a Python version that is compatible with Google Cloud, and install testing tools for creating isolated Python environments.

  2. Determine if you need to cache data.

  3. If you need to cache data, make sure your app's region is supported by Serverless VPC Access and Memorystore for Redis.

  4. Understand Datastore mode permissions.




### Determine if you need to cache data

If your app needs to cache data, understand that Memorystore for Redis and Serverless VPC Access don't have a free tier and don't support all Google Cloud regions.

In general:

  * If your app frequently reads the same data, caching could decrease latency.

  * The more requests your app serves, the bigger impact caching could have.




To see how much you rely on cached data, view the Memcache dashboard to see the ratio of cache hits to misses. If the ratio is high, using a data cache is likely to have a big impact on reducing your app's latency.

[Go to App Engine Memcache](https://console.cloud.google.com/appengine/memcache)

For information about pricing see [Memorystore Pricing](https://cloud.google.com/memorystore/docs/pricing) and [Serverless VPC Access Pricing](https://cloud.google.com/vpc/pricing#serverless-vpc-pricing).

### Confirm the region

If you need to cache data, make sure your app's region is supported by Memorystore for Redis and Serverless VPC Access:

  1. View the region of your app, which appears near the top of the App Engine Dashboard in the Google Cloud console.

[Go to App Engine](https://console.cloud.google.com/appengine)

The region appears near the top of the page, just below your app's URL.

  2. Confirm that your app is in one the [regions supported by Serverless VPC Access](https://docs.cloud.google.com/vpc/docs/configure-serverless-vpc-access#supported_regions).

  3. Confirm that your that your app is in one the regions supported by Memorystore for Redis by visiting the Create connector page and viewing the regions in the **Regions** list.

[Go to Serverless VPC Access](https://console.cloud.google.com/networking/connectors/add)




If your app is not in a region that is supported by Memorystore for Redis and Serverless VPC Access:

  1. Create a Google Cloud project.

  2. Create a new App Engine app in the project and select a supported region.

  3. Create the Google Cloud services that your app uses in the new project.

Alternatively, you can update your app to use the existing services in your old project, but pricing and resource use may be different when you use services in a different project and region. Refer to the documentation for each service for more information.

  4. Deploy your app to the new project.




### Understand Datastore mode permissions

Every interaction with a Google Cloud service needs to be authorized. For example, to store or query data in a Datastore mode database, your app needs to supply the credentials of an account that is authorized to access the database.

By default, your app supplies the credentials of the App Engine default [service account](https://docs.cloud.google.com/appengine/docs/standard/configure-service-accounts), which is authorized to access databases in the same project as your app.

You will need to use an alternative authentication technique that explicitly provides credentials if any of the following conditions are true:

  * Your app and the Datastore mode database are in different Google Cloud projects.

  * You have changed the roles assigned to the default App Engine service account.




For information about alternative authentication techniques, see [Setting up Authentication for Server to Server Production Applications](https://docs.cloud.google.com/docs/authentication#service-accounts).

## Overview of the migration process

To migrate to Cloud NDB:

  1. Update your Python app:

     1. Install the Cloud NDB client library.

     2. Update import statements to import modules from Cloud NDB.

     3. Add code that creates a Cloud NDB client. The client can read your app's environment variables and use the data to authenticate with Datastore mode.

     4. Add code that uses the client's runtime context to keep caching and transactions separate between threads.

     5. Remove or update code that uses methods and properties that are no longer supported.

  2. Enable caching.

  3. Test your updates.

  4. Deploy your app to App Engine.

As with any change you make to your app, consider [using traffic splitting](https://docs.cloud.google.com/appengine/docs/standard/splitting-traffic) to slowly ramp up traffic. Monitor the app closely for any database issues before routing more traffic to the updated app.




## Update your Python app

To migrate your app to Cloud NDB, install the client library and update your code.

### Install the Cloud NDB library for Python apps

To install the Cloud NDB client library in your App Engine Python app:

  1. Update the [`app.yaml`](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml) file. Specify the `runtime` element with a supported Python version. For example, your `app.yaml` file might look as follows:
         
         runtime: python310 # or another supported version
         

The Python runtime installs libraries automatically, so you don't need to specify built-in libraries. If your Python app is using other legacy bundled services when migrating, leave the `app.yaml` file as is.

  2. Update the `requirements.txt` file. Add the Cloud Client Libraries for Cloud NDB to your list of dependencies in the [`requirements.txt` file](https://pip.pypa.io/en/latest/user_guide/#requirements-files).
         
         google-cloud-ndb
         

App Engine automatically installs these dependencies during [app deployment](https://docs.cloud.google.com/appengine/docs/standard/testing-and-deploying-your-app#deploying_your_application), so delete the `lib` folder if one exists.




### Update import statements

The location of the NDB module has moved to [`google.cloud.ndb`](https://googleapis.dev/python/python-ndb/latest/). Update your app's import statements as shown in the following table:

Remove | Replace with  
---|---  
`from google.appengine.ext import ndb` | `from google.cloud import ndb`  
  
### Create a Cloud NDB Client

As with other client libraries that are based on Google Cloud APIs, the first step in using Cloud NDB is to create a [`Client` object](https://googleapis.dev/python/python-ndb/latest/client.html). The client contains credentials and other data needed to connect to Datastore mode. For example:
    
    
    from google.cloud import ndb
    
    client = ndb.Client()
    

In the default authorization scenario described previously, the Cloud NDB client contains credentials from App Engine's default service account, which is authorized to interact with Datastore mode. If you aren't working in this default scenario, see [Application Default Credentials (ADC)](https://docs.cloud.google.com/docs/authentication/application-default-credentials) for information on how to provide credentials.

### Use the client's runtime context

In addition to providing the credentials needed to interact with Datastore mode, the Cloud NDB client contains the [`context()`](https://googleapis.dev/python/python-ndb/latest/client.html#google.cloud.ndb.client.Client.context) method which returns a runtime context. The runtime context isolates caching and transaction requests from other concurrent Datastore mode interactions.

All interactions with Datastore mode need to occur within an NDB runtime context. Since creating a model definition does not interact with Datastore mode, you can define your model class before creating a Cloud NDB client and retrieving a runtime context, and then use the runtime context in the request handler to get data from the database.

For example:
    
    
    from google.cloud import ndb
    
    
    class Book(ndb.Model):
        title = ndb.StringProperty()
    
    
    client = ndb.Client()
    
    
    def list_books():
        with client.context():
            books = Book.query()
            for book in books:
                print(book.to_dict())

### Multithreaded apps

The runtime context that the Cloud NDB client returns only applies to a single thread. If your app uses multiple threads for a single request, you need to retrieve a separate runtime context for each thread that will use the Cloud NDB library.

### Use a runtime context with WSGI frameworks

If your web app uses a WSGI framework, you can automatically create a new runtime context for every request by creating a middleware object that retrieves the runtime context, and then wrapping the app in the middleware object.

In the following example of using middleware with Flask:

  * The `middleware` method creates a WSGI middleware object within the runtime context of the NDB client.

  * The Flask app is wrapped in the middleware object.

  * Flask will then pass each request through the middleware object, which retrieves a new NDB runtime context for each request.



    
    
    from flask import Flask
    
    from google.cloud import ndb
    
    
    client = ndb.Client()
    
    
    def ndb_wsgi_middleware(wsgi_app):
        def middleware(environ, start_response):
            with client.context():
                return wsgi_app(environ, start_response)
    
        return middleware
    
    
    app = Flask(__name__)
    app.wsgi_app = ndb_wsgi_middleware(app.wsgi_app)  # Wrap the app in middleware.
    
    
    class Book(ndb.Model):
        title = ndb.StringProperty()
    
    
    @app.route("/")
    def list_books():
        books = Book.query()
        return str([book.to_dict() for book in books])

### Use a runtime context with Django

The Django middleware provided by the App Engine NDB library isn't supported by the Cloud NDB library. If you used this middleware (`google.appengine.ext.ndb.django_middleware`) in your app, follow these steps to update your app:

  1. Use Django's middleware system to create a new runtime context for every request.

In the following example:

     * The `ndb_django_middleware` method creates a Cloud NDB client.

     * The `middleware` method creates a middleware object within the runtime context of the NDB client.
    
    from google.cloud import ndb
    
    
    # Once this middleware is activated in Django settings, NDB calls inside Django
    # views will be executed in context, with a separate context for each request.
    def ndb_django_middleware(get_response):
        client = ndb.Client()
    
        def middleware(request):
            with client.context():
                return get_response(request)
    
        return middleware

  2. In the Django settings.py file, update the [`MIDDLEWARE` setting](https://docs.djangoproject.com/en/stable/ref/settings/#std:setting-MIDDLEWARE) so it lists the new middleware you created instead of `google.appengine.ext.ndb.NdbDjangoMiddleware`.




Django will now pass each request through the middleware object you listed in the `MIDDLEWARE` setting, and this object will retrieve a new NDB runtime context for each request.

## Update code for removed or changed NDB APIs

NDB APIs that rely on App Engine-specific APIs and services have either been updated or removed from the Cloud NDB library.

You will need to update your code if it uses any of the following NDB APIs:

  * `google.appengine.ext.ndb.Model` and model properties
  * `google.appengine.ext.ndb.Key`
  * `google.appengine.ext.ndb.query.QueryOptions` and `PropertyOrder`
  * `google.appengine.ext.ndb.utils`
  * `google.appengine.api.namespacemanager`
  * `google.appengine.api.ext.ndb.tasklets`
  * `google.appengine.api.datastore_errors`



### Models and Model properties

The following methods from `google.appengine.ext.ndb.Model` are not available in the Cloud NDB library because they use App Engine-specific APIs that are no longer available.

Removed API | Replacement  
---|---  
`Model.get_indexes` and   
`Model.get_indexes_async` | None  
`Model._deserialize` and   
`Model._serialize` | None  
`Model.make_connection` | None  
  
The following table describes the specific [`google.appengine.ext.ndb.Model`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/ndb/Model) properties that have changed in the Cloud NDB library:

Property | Change  
---|---  
`TextProperty` |  [ `google.cloud.ndb.TextProperty`](https://googleapis.dev/python/python-ndb/latest/model.html#google.cloud.ndb.model.TextProperty) cannot be indexed. If you try to set `google.cloud.ndb.TextProperty.indexed`, a `NotImplementedError` will be raised.   
`StringProperty` |  [`StringProperty`](https://googleapis.dev/python/python-ndb/latest/model.html#google.cloud.ndb.model.StringProperty) is always indexed. If you try to set `google.cloud.ndb.StringProperty.indexed`, a `NotImplementedError` will be raised.   
All properties with `name` or `kind` arguments in the constructor.  |  `name` or `kind` must be `str` data types, since `unicode` was replaced by `str` in Python 3.   
  
The classes and methods in the following table are no longer available, because they use App Engine-specific resources that are no longer available.

Removed API | Replacement  
---|---  
`google.appengine.ext.ndb.msgprop.MessageProperty` and   
`google.appengine.ext.ndb.msgprop.EnumProperty` |  None If you try to create these objects, a `NotImplementedError` will be raised.  
`google.appengine.ext.ndb.model.Property`:  
`_db_get_value`  
`_db_set_value`  
`_db_set_compressed_meaning`  
`_db_set_uncompressed_meaning`  
`__creation_counter_global` |  None These methods rely on Datastore mode protocol buffers that have changed.  
`Model.make_connection` | None  
  
### Keys

The following methods from `google.appengine.ext.ndb.Key` are not available in the Cloud NDB library. These methods were used to pass keys to and from the DB API, which is no longer supported (DB is the predecessor of App Engine NDB).

Removed API | Replacement  
---|---  
`Key.from_old_key` and   
`Key.to_old_key` |  None   
  
In addition, note the following changes:

App Engine NDB | Cloud NDB  
---|---  
Kinds and string IDs must be less than 500 bytes  |  Kinds and string IDs must be less than 1500 bytes.   
`Key.app()` returns the project ID you specified when you created the key.  |  The value returned by [ `google.cloud.ndb.Key.app()`](https://googleapis.dev/python/python-ndb/latest/key.html#google.cloud.ndb.key.Key.app) may differ from the original ID passed into the constructor. This is because prefixed app IDs like **s~example** are legacy identifiers from App Engine. They have been replaced by equivalent project IDs, such as **example**.   
  
### Queries

Like App Engine NDB, Cloud NDB provides a `QueryOptions` class ([`google.cloud.ndb.query.QueryOptions`](https://googleapis.dev/python/python-ndb/latest/query.html#google.cloud.ndb.query.QueryOptions)) that lets you reuse a specific set of query options instead of redefining them for each query. However, `QueryOptions` in Cloud NDB doesn't inherit from `google.appengine.datastore.datastore_rpc.Configuration` and therefore doesn't support `...datastore_rpc.Configuration` methods.

In addition, `google.appengine.datastore.datastore_query.Order` has been replaced with [`google.cloud.ndb.query.PropertyOrder`](https://googleapis.dev/python/python-ndb/latest/query.html#google.cloud.ndb.query.PropertyOrder). Similar to `Order`, the `PropertyOrder` class lets you specify the sort order across multiple queries. The `PropertyOrder` constructor is the same as the constructor for `Order`. Only the name of the class has changed.

Removed API | Replacement  
---|---  
from `google.appengine.datastore.datastore_rpc.Configuration`:  
`deadline(value)`  
`on_completion(value)`  
`read_policy(value)`  
`force_writes(value)`  
`max_entity_groups_per_rpc(value)`  
`max_allocate_ids_keys(value)`  
`max_rpc_bytes(value)`  
`max_get_keys(value)`  
`max_put_entities(value)`  
`max_delete_keys(value)` See the [source code](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_rpc) for a description of these methods. | None  
`google.appengine.ext.ndb.Order`  
For example:  
`order=Order(-Account.birthday, Account.name)` | `google.cloud.ndb.PropertyOrder`  
For example:  
`google.cloud.ndb.PropertyOrder(-Account.birthday, Account.name)`  
  
### Utils

The `ndb.utils` module (`google.appengine.ext.ndb.utils`) is no longer available. Most of the methods in that module were internal to App Engine NDB, some methods have been discarded due to implementation differences in the new ndb, while other methods have been made obsolete by new Python 3 features.

For example, the positional decorator in the old `utils` module declared that only the first _n_ arguments of a function or method may be positional. However, Python 3 can do this using [keyword-only arguments](https://www.python.org/dev/peps/pep-3102/). What used to be written as:
    
    
    @utils.positional(2)
    def function1(arg1, arg2, arg3=None, arg4=None)
      pass
    

Can be written like this in Python 3:
    
    
    def function1(arg1, arg2, *, arg3=None, arg4=None)
      pass
    

### Namespaces

Namespaces enable a [multitenant application](https://docs.cloud.google.com/datastore/docs/concepts/multitenancy) to use separate silos of data for each tenant while still using the same Datastore mode database. That is, each tenant stores data under its own namespace.

Instead of using the App Engine-specific `google.appengine.api.namespacemanager`, you specify a default namespace when you create a Cloud NDB client and then use the default namespace by calling Cloud NDB methods within the client's runtime context. This follows the same pattern as other Google Cloud APIs that support namespaces.

Removed API | Replacement  
---|---  
`google.appengine.api.namespace_manager.namespace_manager.set_namespace(str)` and   
`google.appengine.api.namespacemanager.getnamespace()` | 
    
    
    client=google.cloud.ndb.Client(namespace="my namespace")
    
    with client.context() as context:
        key = ndb.Key("SomeKind", "SomeId")
           

or 
    
    
    key-non-default-namespace=ndb.Key("SomeKind," "AnotherId",
    namespace="non-default-nspace")  
  
All other `google.appengine.api.namespacemanager` methods | None  
  
### Tasklets

[Tasklets](https://googleapis.dev/python/python-ndb/latest/tasklets.html) can now use a standard Python `return` statement to return a result instead of raising an NDB `Return` exception. For example:

App Engine NDB library | Cloud NDB library  
---|---  
      
    
            @ndb.tasklet
            def get_cart():
              cart = yield
            CartItem.query().fetch_async()
              raise Return(cart)
           

| 
    
    
            @ndb.tasklet
            def get_cart():
              cart = yield
            CartItem.query().fetch_async()
              return cart
              
  
Note that you can still return results in Cloud NDB by raising a `Return` exception, but it's not recommended.

In addition, the following `Tasklets` methods and subclasses are no longer available, mainly because of changes in how an NDB context is created and used in Cloud NDB library.

Removed API | Replacement  
---|---  
from `google.appengine.api.ext.ndb.tasklets`:  
`add_flow_exception`  
`make_context`  
`make_default_context`  
`set_context` | None  
from `google.appengine.api.ext.ndb.tasklets`:  
`QueueFuture`  
`ReducedFuture`  
`SerialQueueFuture` | None  
  
### Exceptions

While the [`google.cloud.ndb.exceptions` module](https://googleapis.dev/python/python-ndb/latest/exceptions.html) in the Cloud NDB library contains many of the same exceptions from the App Engine NDB library, not all of the old exceptions are available in the new library. The following table lists the exceptions that are no longer available:

Removed API | Replacement  
---|---  
from `google.appengine.api.datastore_errors`:  
`BadKeyError`  
`BadPropertyError`  
`CommittedButStillApplying`  
`EntityNotFoundError`  
`InternalError`  
`NeedIndexError`  
`QueryNotFoundError`  
`ReferencePropertyResolveError`  
`Timeout`  
`TransactionFailedError`  
`TransactionNotFoundError` | `google.cloud.ndb.exceptions`  
  
## Enable data caching

Cloud NDB can cache data in a Redis in-memory datastore managed by [Memorystore](https://docs.cloud.google.com/memorystore/docs/redis/redis-overview), [Redis](https://docs.redis.com/latest/rc/databases/create-database/), or other systems. This guide describes how to use Memorystore for Redis to cache data:

  1. Set up Serverless VPC Access.

  2. Set up Memorystore for Redis.

  3. Add the Redis connection URL to your app.

  4. Create a RedisCache object.




### Set up Serverless VPC Access

Your app can only communicate with Memorystore through a Serverless VPC Access connector. To set up a Serverless VPC Access connector:

  1. [Create a Serverless VPC Access connector](https://docs.cloud.google.com/vpc/docs/configure-serverless-vpc-access#creating_a_connector).

  2. [Configure your app to use the connector](https://docs.cloud.google.com/appengine/docs/standard/connecting-vpc#configuring).




### Set up Memorystore for Redis

To set up Memorystore for Redis:

  1. [Create a Redis instance](https://docs.cloud.google.com/memorystore/docs/redis/creating-managing-instances) in Memorystore. When you're creating the instance:

     * Under **Region** , select the same region in which your App Engine app is located.

     * Under **Authorized network** , select the same network that your Serverless VPC Access connector is using.

  2. Note the IP address and port number of the Redis instance you create. You will use this information when you enable data caching for Cloud NDB.

Be sure to use the **`gcloud beta`** command to deploy your app updates. Only the beta command can update your app to use a VPC connector.




### Add the Redis connection URL

You can connect to the Redis cache by adding the `REDIS_CACHE_URL` environment variable to your app's `app.yaml` file. The value of `REDIS_CACHE_URL` takes the following form:

`redis://IP address for your instance:port`

For example, you can add the following lines to your app's `app.yaml` file:
    
    
         env_variables:
          REDIS_CACHE_URL: redis://10.0.0.3:6379
    

### Create and use a Redis cache object

If you've set `REDIS_CACHE_URL` as an environment variable, you can create a RedisCache object with a single line of code, then use the cache by passing it to `Client.context()` when you set up the runtime context:
    
    
    client = ndb.Client()
    global_cache = ndb.RedisCache.from_environment()
    
    with client.context(global_cache=global_cache):
      books = Book.query()
      for book in books:
          print(book.to_dict())
    

If you don't set `REDIS_CACHE_URL` as an environment variable, you'll need to construct a Redis client and pass the client to the `ndb.RedisCache()` constructor. For example:

`global_cache = ndb.RedisCache(redis.StrictRedis(host=IP-address, port=redis_port))`

Note that you don't need to declare a dependency on the Redis client library, since the Cloud NDB library already depends on the Redis client library.

Refer to the [Memorystore sample application](https://docs.cloud.google.com/memorystore/docs/redis/connect-redis-instance-standard#sample_application) for an example of constructing a Redis client.

## Test your updates

To set up a test database and run your app locally before deploying it to App Engine:

  1. [Run the Datastore mode local emulator](https://docs.cloud.google.com/datastore/docs/tools/datastore-emulator) to store and retrieve data.

Make sure to follow the [instructions for setting environment variables](https://docs.cloud.google.com/datastore/docs/tools/datastore-emulator#setting_environment_variables) so your app connects to the emulator instead of the production Datastore mode environment.

You can also [import data into the emulator](https://docs.cloud.google.com/datastore/docs/tools/emulator-export-import) if you want to start your test with data pre-loaded into the database.

  2. [Use the local development server](https://docs.cloud.google.com/appengine/docs/standard/tools/using-local-server) to run your app.

To make sure the `GOOGLE_CLOUD_PROJECT` environment variable is set correctly during local development, initialize `dev_appserver` using the following parameter: 
         
         --application=PROJECT_ID

Replace PROJECT_ID with your Google Cloud project ID. You can find your project ID by running the `gcloud config list project` command or looking at your project page in the Google Cloud console.




## Deploy your app

Once your app is running in the local development server without errors:

  1. [Test the app on App Engine](https://docs.cloud.google.com/appengine/docs/standard/testing-and-deploying-your-app#testing-on-app-engine).

  2. If the app runs without errors, [use traffic splitting](https://docs.cloud.google.com/appengine/docs/standard/splitting-traffic) to slowly ramp up traffic for your updated app. Monitor the app closely for any database issues before routing more traffic to the updated app.




## What's next

  * For a tutorial, see the [Migrate from App Engine ndb to Cloud NDB codelab](https://codelabs.developers.google.com/codelabs/cloud-gae-python-migrate-2-cloudndb).
  * For more details, see the [Cloud NDB](https://googleapis.dev/python/python-ndb/latest/index.html) documentation.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
