---
url: https://docs.cloud.google.com/appengine/migration-center/standard/python/memcache-to-memorystore/
title: Migrating Memcache to Memorystore \u00a0|\u00a0 App Engine migration center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:56:39.875344+00:00
---

# Migrating Memcache to Memorystore  |  App Engine migration center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/migration-center/standard/python/memcache-to-memorystore/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Migration center ](https://docs.cloud.google.com/appengine/migration-center)
  * [ Guides ](https://docs.cloud.google.com/appengine/migration-center/standard/services/migrating-services)



Send feedback 

#  Migrating Memcache to Memorystore Stay organized with collections  Save and categorize content based on your preferences. 

High performance scalable Python web applications often use a distributed in-memory data cache instead of robust persistent storage for some tasks.

The App Engine solution for this is [Memcache](https://docs.cloud.google.com/appengine/docs/standard/services/memcache), a distributed in-memory datastore that is used as a cache for specific tasks.

When migrating off legacy bundled services, the recommended replacement for App Engine Memcache is [Memorystore](https://docs.cloud.google.com/memorystore), a fully-managed cloud-based caching service that supports open source caching engines, Redis and Memcached. This guide covers using [Memorystore for Redis](https://docs.cloud.google.com/memorystore/docs/redis/redis-overview), which can build application caches that provide sub-millisecond data access.

If your Python app uses Memcache to only reduce latency for `ndb` or Cloud NDB requests, you can use [Cloud NDB's built-in support for Redis](https://docs.cloud.google.com/appengine/migration-center/standard/python/migrate-to-cloud-ndb#setup_redis_db), instead of Memcache or Memorystore for Redis.

Before getting started, make sure your app will stay within the [Memorystore for Redis quotas](https://docs.cloud.google.com/memorystore/docs/redis/quotas).

**Note:** Unlike Memcache, **Memorystore for Redis does not provide a free tier**. See [Memorystore pricing](https://cloud.google.com/memorystore/pricing) and [quotas and limits](https://docs.cloud.google.com/memorystore/docs/redis/quotas) for details.

## When to use a memory cache for Python apps

In your Python apps, session data, user preferences, and other data returned by queries for web pages are good candidates for caching. In general, if a frequently run query returns a set of results that do not need to appear in your app immediately, you can cache the results. Subsequent requests can check the cache and only query the database if the results are absent or have expired.

If you store a value only in Memorystore without backing it up in persistent storage, be sure that your application behaves acceptably if the value expires and is removed from the cache. For example, if the sudden absence of a user's session data would cause the session to malfunction, that data should probably be stored in the database in addition to Memorystore.

## Before you begin

If you have not done so already, set up your [Python development environment](https://docs.cloud.google.com/python/docs/setup) to use a Python version that is compatible with Google Cloud, and install testing tools for creating isolated Python environments.

### Understanding Memorystore permissions

Every interaction with a Google Cloud service needs to be authorized. For example, to interact with a Redis database hosted by Memorystore, your app needs to supply the credentials of an account that is authorized to access Memorystore.

By default, your app supplies the credentials of the App Engine default [service account](https://docs.cloud.google.com/appengine/docs/standard/configure-service-accounts), which is authorized to access databases in the same project as your app.

If any of the following conditions are true, you need to use an alternative authentication technique that explicitly provides credentials:

  * Your app and the Memorystore database are in different Google Cloud projects.

  * You have changed the roles assigned to the default App Engine service account.




For information about alternative authentication techniques, see [Setting up Authentication for Server to Server Production Applications](https://docs.cloud.google.com/docs/authentication#service-accounts).

## Overview of the migration process

To use Memorystore instead of Memcache in your Python app:

  1. Set up Memorystore for Redis, which requires you to create a Redis instance on Memorystore and create a Serverless VPC Access that your app uses to communicate with the Redis instance. The order of creating these two independent entities is not strict and can be set up in any order. The instructions in this guide show setting up Serverless VPC Access first.

  2. Install a client library for Redis and use Redis commands to cache data.

Memorystore for Redis is compatible with [any client library for Redis](https://redis.io/clients).

This guide describes using the [`redis-py`](https://pypi.org/project/redis/) client library to send Redis commands from your app.

  3. Test your updates.

  4. Deploy your app to App Engine.




## Setting up Memorystore for Redis

To set up Memorystore for Redis:

  1. [Connect your App Engine to a VPC network](https://docs.cloud.google.com/appengine/docs/standard/connecting-vpc). Your app can only communicate with Memorystore through a VPC connector.

Be sure to add the VPC connection information to your `app.yaml` file as described in [Configuring your app use the connector](https://docs.cloud.google.com/appengine/docs/standard/connecting-vpc#configuring).

  2. Note the IP address and port number of the Redis instance you create. You will use this information when you create a Redis client in your code.

  3. [Create a Redis instance](https://docs.cloud.google.com/memorystore/docs/redis/creating-managing-instances#creating_a_redis_instance_on_a_vpc_network) in Memorystore.

When prompted to select a region for your Redis instance, select the [same region in which your App Engine app is located](https://docs.cloud.google.com/appengine/docs/standard/locations).




## Installing dependencies

To use the `redis-py` client library:

  1. Update the `app.yaml` file. Follow the instructions for your version of Python:

###  Python 2 

For Python 2 apps, add the latest versions of `grpcio` and `setuptools` libraries.

The following is an example `app.yaml` file:
         
         runtime: python27
         threadsafe: yes
         api_version: 1
         
         libraries:
         - name: grpcio
           version: latest
         - name: setuptools
           version: latest
         

###  Python 3 

For Python 3 apps, specify the `runtime` element in your `app.yaml` file with a supported Python 3 version. For example:
         
         runtime: python310 # or another support version
         

The Python 3 runtime installs libraries automatically, so you do not need to specify built-in libraries from the previous Python 2 runtime. If your Python 3 app is using other legacy bundled services when migrating, you can continue to specify the necessary built-in libraries. Otherwise, you can delete the unnecessary lines in your `app.yaml` file.

  2. Update the `requirements.txt` file. Follow the instructions for your version of Python:

###  Python 2 

Add the Cloud Client Libraries for Memorystore for Redis to your list of dependencies in the `requirements.txt` file.
         
         redis
         

Run `pip install -t lib -r requirements.txt` to update the list of available libraries for your app.

###  Python 3 

Add the Cloud Client Libraries for Memorystore for Redis to your list of dependencies in the `requirements.txt` file.
         
         redis
         

App Engine automatically installs these dependencies during app deployment in the Python 3 runtime, so delete the `lib` folder if one exists.

  3. For Python 2 apps, if your app is using built-in or copied libraries specified in the `lib` directory, you must specify those paths in the `appengine_config.py` file, located in the same folder as your `app.yaml` file:
         
         import pkg_resources
         from google.appengine.ext import vendor
         
         # Set PATH to your libraries folder.
         PATH = 'lib'
         # Add libraries installed in the PATH folder.
         vendor.add(PATH)
         # Add libraries to pkg_resources working set to find the distribution.
         pkg_resources.working_set.add_entry(PATH)
         




## Creating a Redis client

To interact with a Redis database, your code needs to create a Redis client to manage the connection to your Redis database. The following sections describe creating a Redis client using the redis-py client library.

### Specifying environment variables

The redis-py client library uses two environment variables to assemble the URL for your Redis database:

  * A variable to identify the IP address of the Redis database you created in Memorystore.
  * A variable to identify the port number of the Redis database you created in Memorystore.



We recommend you define these variables in your app's `app.yaml` file instead of defining them directly in your code. This makes it easier to run your app in different environments, such as a local environment and App Engine.

For example, add the following lines to your `app.yaml` file:
    
    
     env_variables:
          REDISHOST: '10.112.12.112'
          REDISPORT: '6379'
    

### Importing redis-py and creating the client

After you define the `REDISHOST` and `REDISPORT` environment variables, use the following lines to import the `redis-py` library and create a client:
    
    
      import redis
    
      redis_host = os.environ.get('REDISHOST', 'localhost')
      redis_port = int(os.environ.get('REDISPORT', 6379))
      redis_client = redis.Redis(host=redis_host, port=redis_port)
    

If you've used an older version of `redis-py` for other apps, you might have used the `StrictClient` class instead of `Client`. However, `redis-py` now [recommends](https://pypi.org/project/redis/#client-classes-redis-and-strictredis) `Client` instead of `StrictClient`.

## Using Redis commands to store and retrieve data in the cache

While the Memorystore Redis database [supports most Redis commands](https://docs.cloud.google.com/memorystore/docs/redis/product-constraints), you only need to use a few commands to store and retrieve data from the cache. The following table suggests Redis commands you can use to cache data. To see how to call these commands from your app, view your client library's documentation.

Note that for Python 2 apps, while Memcache provides asynchronous alternatives for many of its commands, the `redis-py` client library doesn't always provide equivalent asynchronous methods. If you require all interactions with the cache to be asynchronous, [other Redis client libraries for Python](https://redis.io/clients#python) are available.

Task | Redis command  
---|---  
Create an entry in the data cache and  
set an expiration time for the entry | [SETNX](https://redis.io/commands/setnx)  
[MSETNX](https://redis.io/commands/msetnx)  
Retrieve data from the cache | [GET](https://redis.io/commands/get)  
[MGET](https://redis.io/commands/mget)  
Replace existing cache values | [SET](https://redis.io/commands/set)  
[MSET](https://redis.io/commands/mset)  
Increment or decrement numeric cache values | [INCR](https://redis.io/commands/incr)  
[INCRBY](https://redis.io/commands/incrby)  
[DECR](https://redis.io/commands/decr)  
[DECRBY](https://redis.io/commands/decrby)  
Delete entries from the cache | [DEL](https://redis.io/commands/del)  
[UNLINK](https://redis.io/commands/unlink)  
Support concurrent interactions with the cache ([compare and set](https://docs.cloud.google.com/appengine/docs/standard/services/memcache?tab=python#compare_and_set))  | See details about [Redis transactions](https://redis.io/topics/transactions). Note that the `redis-py` client library requires all transactions to occur in a [pipeline](https://github.com/andymccurdy/redis-py#pipelines).   
  
## Testing your updates

When you test your app locally, consider running a local instance of Redis to avoid interacting with production data (Memorystore doesn't provide an emulator). To install and run Redis locally, follow the directions in the [Redis documentation](http://redis.io/topics/quickstart). Note that it currently isn't possible to run Redis locally on Windows.

For more information about testing Python apps, see [Using the local development server](https://docs.cloud.google.com/appengine/docs/standard/tools/using-local-server).

## Deploying your app

Once your app is running in the local development server without errors:

  1. [Test the app on App Engine](https://docs.cloud.google.com/appengine/docs/standard/testing-and-deploying-your-app#testing-on-app-engine).

  2. If the app runs without errors, [use traffic splitting](https://docs.cloud.google.com/appengine/docs/standard/splitting-traffic) to slowly ramp up traffic for your updated app. Monitor the app closely for any database issues before routing more traffic to the updated app.




## What's next

  * For a hands-on tutorial, see the [Migrate from App Engine Memcache to Memorystore for Redis codelab](https://codelabs.developers.google.com/codelabs/cloud-gae-python-migrate-13-memorystore).
  * See [Memorystore for Redis](https://docs.cloud.google.com/memorystore/docs/redis/redis-overview) documentation for more details.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
