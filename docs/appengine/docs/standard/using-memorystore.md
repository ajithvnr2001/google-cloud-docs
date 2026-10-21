---
url: https://docs.cloud.google.com/appengine/docs/standard/using-memorystore/
title: Caching data with Memorystore \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:47:43.268746+00:00
---

# Caching data with Memorystore  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/using-memorystore/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Caching data with Memorystore Stay organized with collections  Save and categorize content based on your preferences. 

High performance scalable web applications often use a distributed in-memory data cache in front of or in place of robust persistent storage for some tasks. We recommend using Memorystore for Redis as your caching service. Note that **Memorystore for Redis does not provide a free tier**. See [Memorystore Pricing](https://cloud.google.com/memorystore#pricing) for details.

Before getting started, make sure your app will stay within the [Memorystore for Redis quotas](https://docs.cloud.google.com/memorystore/docs/redis/quotas).

## When to use a memory cache

Session data, user preferences, and other data returned by queries for web pages are good candidates for caching. In general, if a frequently run query returns a set of results that do not need to appear in your app immediately, you can cache the results. Subsequent requests can check the cache and only query the database if the results are absent or have expired.

If you store a value only in Memorystore without backing it up in persistent storage, be sure that your application behaves acceptably if the value expires and is removed from the cache. For example, if the sudden absence of a user's session data would cause the session to malfunction, that data should probably be stored in the database in addition to Memorystore.

## Understanding Memorystore permissions

Every interaction with a Google Cloud service needs to be authorized. For example, to interact with a Redis database hosted by Memorystore, your app needs to supply the credentials of an account that is authorized to access Memorystore.

By default your app supplies the credentials of the App Engine default [service account](https://docs.cloud.google.com/iam/docs/service-accounts), which is authorized to access databases in the same project as your app.

If any of the following conditions are true, you need to use an alternative authentication technique that explicitly provides credentials:

  * Your app and the Memorystore database are in different Google Cloud projects.

  * You have changed the roles assigned to the default App Engine service account.




For information about alternative authentication techniques, see [Setting up Authentication for Server to Server Production Applications](https://docs.cloud.google.com/docs/authentication/production#auth-cloud-implicit-python).

## Overview of using Memorystore

To use Memorystore in your app:

  1. Set up Memorystore for Redis, which requires you to create a Redis instance on Memorystore and create a Serverless VPC Access that your app uses to communicate with the Redis instance.

  2. Install a client library for Redis and use Redis commands to cache data.

Memorystore for Redis is compatible with [any client library for Redis](https://redis.io/clients).

### Go

This guide describes using the [redigo](https://github.com/gomodule/redigo) client library to send Redis commands from your app.

### Java

This guide describes using the [Jedis](https://github.com/xetorthio/jedis) client library to send Redis commands from your app. For details about using Jedis, see the [Jedis wiki](https://github.com/xetorthio/jedis/wiki/Getting-started).

### Node.js

This guide describes using the [node_redis](http://redis.js.org/) client library to send Redis commands from your app.

### PHP

This guide describes using the [PHPRedis](https://pecl.php.net/package/redis) client library to send Redis commands from your app.

### Python

This guide describes using the [redis-py 3.0](https://pypi.org/project/redis/) client library to send Redis commands from your app.

### Ruby

This guide describes using the [redis-rb](https://github.com/redis/redis-rb) client library to send Redis commands from your app.

  3. Test your updates.

  4. Deploy your app to App Engine.




## Setting up Memorystore for Redis

To set up Memorystore for Redis:

  1. [Create a Redis instance](https://docs.cloud.google.com/memorystore/docs/redis/creating-managing-instances#creating_a_redis_instance_on_a_vpc_network) in Memorystore.

When prompted to select a region for your Redis instance, select the [same region in which your App Engine app is located](https://docs.cloud.google.com/appengine/docs/standard/locations).

  2. Note the IP address and port number of the Redis instance you create. You will use this information when you create a Redis client in your code.

  3. [Connect your App Engine to a VPC network](https://docs.cloud.google.com/appengine/docs/standard/connecting-vpc). Your app can only communicate with Memorystore through a VPC connector.

Be sure to add the VPC connection information to your `app.yaml` file as described in [Configuring your app use the connector](https://docs.cloud.google.com/appengine/docs/standard/connecting-vpc#configuring).




## Installing dependencies

### Go

To make the redigo client library available to your app when it runs in App Engine, add the library to your app's dependencies. For example, if you use a `go.mod` file to declare dependencies, add the following line to your `go.mod` file:

module github.com/GoogleCloudPlatform/golang-samples/tree/master/memorystore/redis

Learn more about [specifying dependencies](https://docs.cloud.google.com/appengine/docs/standard/go/specifying-dependencies) for your Go app.

### Java

To make the Jedis client library available to your app when it runs in App Engine, add the library to your app's dependencies. For example, if you use Maven add the following dependency in your `pom.xml` file: 
    
    
    <dependency>
      <groupId>redis.clients</groupId>
      <artifactId>jedis</artifactId>
      <version>5.1.0</version>
    </dependency>

### Node.js

To make the node_redis client library available to your app when it runs in App Engine, add the library to your app's `package.json` file.

For example: 
    
    
    {
      "name": "memorystore-redis",
      "description": "An example of using Memorystore(Redis) with Node.js",
      "version": "0.0.1",
      "private": true,
      "license": "Apache Version 2.0",
      "author": "Google Inc.",
      "engines": {
        "node": ">=20.0.0"
      },
      "dependencies": {
        "redis": "^4.0.0"
      }
    }
    
    

Learn more about [specifying dependencies](https://docs.cloud.google.com/appengine/docs/standard/nodejs/specifying-dependencies) for your Node.js app.

### PHP

To make the PHPRedis client library available to your app when it runs in App Engine, add the `redis.so` extension to your app's `php.ini` file. For example: 
    
    
    ; Enable the Redis extension on App Engine
    extension=redis.so
    

For more information about enabling PHP extensions in App Engine, see [Dynamically loadable extensions](https://docs.cloud.google.com/appengine/docs/standard/php-gen2/runtime#dynamically_loadable_extensions).

### Python

To make the redis-py client library available to your app when it runs in App Engine, add the following line to your app's [`requirements.txt`](https://pip.pypa.io/en/latest/user_guide/#requirements-files) file:
    
    
      redis
    

The App Engine Python 3 runtime will automatically upload all libraries your app's `requirements.txt` file when you [deploy the app](https://docs.cloud.google.com/appengine/docs/standard/testing-and-deploying-your-app#deploying_your_application).

For local development, we recommend that you install dependencies in a virtual environment such as [venv](https://packaging.python.org/key_projects/#venv).

### Ruby

To make the redis-rb client library available to your app when it runs in App Engine, add the library to your app's `Gemfile` file.
    
    
      source "https://cloud.google.com/memorystore"
    
      gem "redis-rb"
    

## Creating a Redis client

To interact with a Redis database, your code needs to create a Redis client to manage the connection to your Redis database. The following sections describe creating a Redis client using the Redis client library.

### Specifying environment variables

The Redis client library uses two environment variables to assemble the URL for your Redis database:

  * A variable to identify the IP address of the Redis database you created in Memorystore.
  * A variable to identify the port number of the Redis database you created in Memorystore.



We recommend you define these variables in your app's `app.yaml` file instead of defining them directly in your code. This makes it easier to run your app in different environments, such as a local environment and App Engine. Learn more about environment variables in the [`app.yaml` reference page](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml).

### Go

For example, add the following lines to your `app.yaml` file:
    
    
      env_variables:
           REDISHOST: '10.112.12.112'
           REDISPORT: '6379'
    

### Java

For example, add the following lines to your `app.yaml` file:
    
    
      env_variables:
           redis.host: '10.112.12.112'
           redis.port: '6379'
    

### Node.js

For example, add the following lines to your `app.yaml` file:
    
    
      env_variables:
           REDISHOST: '10.112.12.112'
           REDISPORT: '6379'
    

### PHP

For example, add the following lines to your `app.yaml` file:
    
    
      env_variables:
           REDIS_HOST: '10.112.12.112'
           REDIS_PORT: '6379'
    

### Python

For example, add the following lines to your `app.yaml` file:
    
    
      env_variables:
           REDISHOST: '10.112.12.112'
           REDISPORT: '6379'
    

### Ruby

For example, add the following lines to your `app.yaml` file:
    
    
      env_variables:
           REDISHOST: '10.112.12.112'
           REDISPORT: '6379'
    

### Importing Redis and creating the client

### Go

After you define the `REDISHOST` and `REDISPORT` environment variables, use the following lines to import the redigo library, create a connection pool, and then retrieve a Redis client from the pool:
    
    
    // Package main is a basic app that connects to a managed Redis instance.
    package main
    
    import (
    	"fmt"
    	"log"
    	"net/http"
    	"os"
    
    	"github.com/gomodule/redigo/redis"
    )
    
    var redisPool *redis.Pool
    
    func incrementHandler(w http.ResponseWriter, r *http.Request) {
    	conn := redisPool.Get()
    	defer conn.Close()
    
    	counter, err := redis.Int(conn.Do("INCR", "visits"))
    	if err != nil {
    		http.Error(w, "Error incrementing visitor counter", http.StatusInternalServerError)
    		return
    	}
    	fmt.Fprintf(w, "Visitor number: %d", counter)
    }
    
    func main() {
    	redisHost := os.Getenv("REDISHOST")
    	redisPort := os.Getenv("REDISPORT")
    	redisAddr := fmt.Sprintf("%s:%s", redisHost, redisPort)
    
    	const maxConnections = 10
    	redisPool = &redis.Pool{
    		MaxIdle: maxConnections,
    		Dial:    func() (redis.Conn, error) { return redis.Dial("tcp", redisAddr) },
    	}
    
    	http.HandleFunc("/", incrementHandler)
    
    	port := os.Getenv("PORT")
    	if port == "" {
    		port = "8080"
    	}
    	log.Printf("Listening on port %s", port)
    	if err := http.ListenAndServe(":"+port, nil); err != nil {
    		log.Fatal(err)
    	}
    }
    

### Java

When you use the Jedis library, we recommend that you create a [JedisPool](https://github.com/xetorthio/jedis/wiki/Getting-started#user-content-using-jedis-in-a-multithreaded-environment), and then use the pool to create a client. The following lines of code use the `redis.host` and `redis.port` environment variables you defined earlier to create a pool:
    
    
    package com.example.redis;
    
    import java.io.IOException;
    import java.util.Properties;
    import javax.servlet.ServletContextEvent;
    import javax.servlet.ServletContextListener;
    import javax.servlet.annotation.WebListener;
    import redis.clients.jedis.JedisPool;
    import redis.clients.jedis.JedisPoolConfig;
    
    @WebListener
    public class AppServletContextListener implements ServletContextListener {
    
      private Properties config = new Properties();
    
      private JedisPool createJedisPool() throws IOException {
        String host;
        Integer port;
        config.load(
            Thread.currentThread()
                .getContextClassLoader()
                .getResourceAsStream("application.properties"));
        host = config.getProperty("redis.host");
        port = Integer.valueOf(config.getProperty("redis.port", "6379"));
    
        JedisPoolConfig poolConfig = new JedisPoolConfig();
        // Default : 8, consider how many concurrent connections into Redis you will need under load
        poolConfig.setMaxTotal(128);
    
        return new JedisPool(poolConfig, host, port);
      }
    
      @Override
      public void contextDestroyed(ServletContextEvent event) {
        JedisPool jedisPool = (JedisPool) event.getServletContext().getAttribute("jedisPool");
        if (jedisPool != null) {
          jedisPool.destroy();
          event.getServletContext().setAttribute("jedisPool", null);
        }
      }
    
      // Run this before web application is started
      @Override
      public void contextInitialized(ServletContextEvent event) {
        JedisPool jedisPool = (JedisPool) event.getServletContext().getAttribute("jedisPool");
        if (jedisPool == null) {
          try {
            jedisPool = createJedisPool();
            event.getServletContext().setAttribute("jedisPool", jedisPool);
          } catch (IOException e) {
            // handle exception
          }
        }
      }
    }

To create a client from the pool, use the `JedisPool.getResource()` method. For example:
    
    
    package com.example.redis;
    
    import java.io.IOException;
    import java.net.SocketException;
    import javax.servlet.annotation.WebServlet;
    import javax.servlet.http.HttpServlet;
    import javax.servlet.http.HttpServletRequest;
    import javax.servlet.http.HttpServletResponse;
    import redis.clients.jedis.Jedis;
    import redis.clients.jedis.JedisPool;
    
    @WebServlet(name = "Track visits", value = "")
    public class VisitCounterServlet extends HttpServlet {
    
      @Override
      public void doGet(HttpServletRequest req, HttpServletResponse resp) throws IOException {
        try {
          JedisPool jedisPool = (JedisPool) req.getServletContext().getAttribute("jedisPool");
    
          if (jedisPool == null) {
            throw new SocketException("Error connecting to Jedis pool");
          }
          Long visits;
    
          try (Jedis jedis = jedisPool.getResource()) {
            visits = jedis.incr("visits");
          }
    
          resp.setStatus(HttpServletResponse.SC_OK);
          resp.getWriter().println("Visitor counter: " + String.valueOf(visits));
        } catch (Exception e) {
          resp.sendError(HttpServletResponse.SC_INTERNAL_SERVER_ERROR, e.getMessage());
        }
      }
    }

### Node.js

After you've defined the `REDISHOST` and `REDISPORT` environment variables, you can use the following lines to import the node_redis library and create a Redis client:
    
    
    'use strict';
    const http = require('http');
    const redis = require('redis');
    
    const REDISHOST = process.env.REDISHOST || 'localhost';
    const REDISPORT = process.env.REDISPORT || 6379;
    
    const client = redis.createClient({
      url: `redis://${REDISHOST}:${REDISPORT}`,
    });
    
    client.on('error', err => console.error('ERR:REDIS:', err));
    
    client
      .connect()
      .then(() => {
        console.log('Connected to Redis');
        http
          .createServer(async (req, res) => {
            try {
              const reply = await client.incr('visits');
              res.writeHead(200, {'Content-Type': 'text/plain'});
              res.end(`Visitor number: ${reply}\n`);
            } catch (err) {
              console.error(err);
              res.statusCode = 500;
              res.end(err.message);
            }
          })
          .listen(8080, () => {
            console.log('Server listening on port 8080');
          });
      })
      .catch(err => {
        console.error('Failed to connect to Redis:', err);
        throw err;
      });

### PHP

After you've defined the `REDIS_HOST` and `REDIS_PORT` environment variables, you can use the following lines to create a Redis client:
    
    
    <?php
    /**
     * Copyright 2019 Google Inc.
     *
     * Licensed under the Apache License, Version 2.0 (the "License");
     * you may not use this file except in compliance with the License.
     * You may obtain a copy of the License at
     *
     *     http://www.apache.org/licenses/LICENSE-2.0
     *
     * Unless required by applicable law or agreed to in writing, software
     * distributed under the License is distributed on an "AS IS" BASIS,
     * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
     * See the License for the specific language governing permissions and
     * limitations under the License.
     */
    
    // Only serve traffic from "/"
    switch (@parse_url($_SERVER['REQUEST_URI'])['path']) {
        case '/':
            break;
        default:
            http_response_code(404);
            exit('Not Found');
    }
    
    // Connect to Memorystore from App Engine.
    if (!$host = getenv('REDIS_HOST')) {
        throw new Exception('The REDIS_HOST environment variable is required');
    }
    
    # Memorystore Redis port defaults to 6379
    $port = getenv('REDIS_PORT') ?: '6379';
    
    try {
        $redis = new Redis();
        $redis->connect($host, $port);
    } catch (Exception $e) {
        return print('Error: ' . $e->getMessage());
    }
    
    $value = $redis->incr('counter');
    
    printf('Visitor number: %s', $value);
    

### Python

After you define the `REDISHOST` and `REDISPORT` environment variables, use the following lines to import the redis-py library and create a client:
    
    
      import redis
    
      redis_host = os.environ.get('REDISHOST', 'localhost')
      redis_port = int(os.environ.get('REDISPORT', 6379))
      redis_client = redis.Redis(host=redis_host, port=redis_port)
    

If you've used an older version of redis-py for other apps, you might have used the `StrictClient` class instead of `Client`. However, redis-py now [recommends](https://pypi.org/project/redis/#client-classes-redis-and-strictredis) `Client` instead of `StrictClient`.

### Ruby

No additional information for this runtime.

## Using Redis commands to store and retrieve data in the cache

While the Memorystore Redis database [supports most Redis commands](https://docs.cloud.google.com/memorystore/docs/redis/product-constraints), you only need to use a few commands to store and retrieve data from the cache. The following table suggests Redis commands you can use to cache data. To see how to call these commands from your app, view your client library's documentation.

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
Support concurrent interactions with the cache  | See details about [Redis transactions](https://redis.io/topics/transactions).   
  
For Python, the redis-py client library requires all transactions to occur in a [pipeline](https://github.com/andymccurdy/redis-py#pipelines).   
  
## Testing your updates

When you test your app locally, consider running a local instance of Redis to avoid interacting with production data (Memorystore doesn't provide an emulator). To install and run Redis locally, follow the directions in the [Redis documentation](http://redis.io/topics/quickstart). Note that it currently isn't possible to run Redis locally on Windows.

For more information about testing your apps, see [Testing and deploying your application](https://docs.cloud.google.com/appengine/docs/standard/testing-and-deploying-your-app).

## Deploying your app

Once your app is running in the local development server without errors:

  1. [Test the app on App Engine](https://docs.cloud.google.com/appengine/docs/standard/testing-and-deploying-your-app#testing-on-app-engine).

  2. If the app runs without errors, [use traffic splitting](https://docs.cloud.google.com/appengine/docs/standard/splitting-traffic) to slowly ramp up traffic for your updated app. Monitor the app closely for any database issues before routing more traffic to the updated app.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
