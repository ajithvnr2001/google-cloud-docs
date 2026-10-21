---
url: https://docs.cloud.google.com/memorystore/docs/redis/connect-redis-instance-flex/
title: Connect to a Redis instance from an App Engine flexible environment application \u00a0|\u00a0 Memorystore for Redis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:33:52.678923+00:00
---

# Connect to a Redis instance from an App Engine flexible environment application  |  Memorystore for Redis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/redis/connect-redis-instance-flex/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis ](https://docs.cloud.google.com/memorystore/docs/redis)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/redis/redis-overview)



Send feedback 

#  Connect to a Redis instance from an App Engine flexible environment application Stay organized with collections  Save and categorize content based on your preferences. 

App Engine applications must be on the same authorized network as the Redis instance in order to access it.

## Setup

If you have already installed the Google Cloud CLI and have created a Redis instance, you can skip these steps.

  1. [Install the gcloud CLI](https://cloud.google.com/sdk/docs/) and initialize:
         
         gcloud init
         

  2. Follow the [Quickstart Guide](https://docs.cloud.google.com/memorystore/docs/redis/create-instance-gcloud) to create a Redis instance. Take note of the zone, IP address, and port of the Redis instance.




## Sample application

This sample HTTP server application establishes a connection to a Redis instance from an App Engine flexible environment instance.

Clone the repository for your chosen programming language and navigate to the folder that contains the sample code:

### Go
    
    
    git clone https://github.com/GoogleCloudPlatform/golang-samples
    cd golang-samples/memorystore/redis
    

### Java
    
    
    git clone https://github.com/GoogleCloudPlatform/java-docs-samples
    cd java-docs-samples/memorystore/redis
    

### Node.js
    
    
    git clone https://github.com/GoogleCloudPlatform/nodejs-docs-samples
    cd nodejs-docs-samples/memorystore/redis
    

### Python
    
    
    git clone https://github.com/GoogleCloudPlatform/python-docs-samples
    cd python-docs-samples/memorystore/redis
    

This sample application increments a Redis counter every time the `/` endpoint is accessed.

### Go

This application uses the [`github.com/gomodule/redigo/redis`](https://godoc.org/github.com/gomodule/redigo/redis) client. Install it by running the following command:
    
    
    go get github.com/gomodule/redigo/redis@latest
    

Example application:
    
    
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

This application is Jetty 3.1 servlet-based.

It uses the [Jedis](https://github.com/xetorthio/jedis) library:
    
    
    <dependency>
      <groupId>redis.clients</groupId>
      <artifactId>jedis</artifactId>
      <version>5.1.0</version>
    </dependency>

The `AppServletContextListener` class is used to create a long-lived Redis connection pool:
    
    
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

The `VisitCounterServlet` class is a web servlet that increments a Redis counter:
    
    
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

This application uses the [`redis`](https://www.npmjs.com/package/redis) module. This is a sample `package.json` file:
    
    
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
    
    

Sample application code:
    
    
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

### Python

This application uses [Flask](https://flask.palletsprojects.com/en/1.1.x/) for web serving and the [`redis-py`](https://redis-py.readthedocs.io/en/latest/) package to communicate with the Redis instance.
    
    
    Flask==3.1.3; python_version >= '3.9'
    gunicorn==23.0.0
    redis==6.0.0
    Werkzeug==3.1.9; python_version >= '3.10'

Sample application code:
    
    
    import logging
    import os
    
    from flask import Flask
    import redis
    
    app = Flask(__name__)
    
    redis_host = os.environ.get("REDISHOST", "localhost")
    redis_port = int(os.environ.get("REDISPORT", 6379))
    redis_client = redis.StrictRedis(host=redis_host, port=redis_port)
    
    
    @app.route("/")
    def index():
        value = redis_client.incr("counter", 1)
        return f"Visitor number: {value}"
    
    
    @app.errorhandler(500)
    def server_error(e):
        logging.exception("An error occurred during a request.")
        return (
            """
        An internal error occurred: <pre>{}</pre>
        See logs for full stacktrace.
        """.format(
                e
            ),
            500,
        )
    
    
    if __name__ == "__main__":
        # This is used when running locally. Gunicorn is used to run the
        # application on Google App Engine and Cloud Run.
        # See entrypoint in app.yaml or Dockerfile.
        app.run(host="127.0.0.1", port=8080, debug=True)

## Preparing the application for deployment

To access the Redis instance, the App Engine instance must be deployed on the same authorized network as the Redis instance, and you must provide your Redis instance's connection details. You can find your Redis instance's authorized network, IP address, and port by running the following command:
    
    
     gcloud redis instances describe [INSTANCE_ID] --region [REGION]
    

  1. Create an [App Engine application](https://console.cloud.google.com/projectselector/appengine/create).

**Note:** You can also use an existing App Engine application.
  2. Update the app's configuration to specify the IP address, port, and network of your Redis instance:

### Go

Update the `gae_flex_deployment/app.yaml` file:
         
         runtime: go
         env: flex
         
         # Update with Redis instance details
         env_variables:
           REDISHOST: '<REDIS_IP>'
           REDISPORT: '6379'
         
         # Update with Redis instance network name
         network:
           name: default
         
         runtime_config:
           operating_system: "ubuntu22"
           runtime_version: "1.25"

See [Configuring your App with app.yaml](https://docs.cloud.google.com/appengine/docs/flexible/go/configuring-your-app-with-app-yaml) for more details.

### Java

Update the `gae_flex_deployment/app.yaml` file to specify your Redis instance's network:
         
         runtime: java
         env: flex
         
         # Update with Redis instance network name
         network:
           name: default

And update the `src/main/resources/application.properties` file with your Redis instance's IP address and port:
         
         redis.host=REDIS_HOST_IP
         redis.port=6379

For more information about configuring your app, see [Configuring your App with app.yaml](https://docs.cloud.google.com/appengine/docs/flexible/java/configuring-your-app-with-app-yaml).

### Node.js

Update the `gae_flex_deployment/app.yaml` file:
         
         runtime: nodejs
         env: flex
         
         # Update with Redis instance details
         env_variables:
           REDISHOST: '<REDIS_IP>'
           REDISPORT: '6379'
         
         # Update with Redis instance network name
         network:
           name: default

See [Configuring your App with app.yaml](https://docs.cloud.google.com/appengine/docs/flexible/nodejs/configuring-your-app-with-app-yaml) for more details.

### Python

Update the `gae_flex_deployment/app.yaml` file:
         
         runtime: python
         env: flex
         entrypoint: gunicorn -b :$PORT main:app
         
         runtime_config:
           python_version: 3
         
         # Update with Redis instance IP and port
         env_variables:
           REDISHOST: '<REDIS_IP>'
           REDISPORT: '6379'
         
         # Update with Redis instance network name
         network:
           name: default

See [Configuring your App with app.yaml](https://docs.cloud.google.com/appengine/docs/flexible/python/configuring-your-app-with-app-yaml) for more details.




## Deploying the application to the App Engine flexible environment

To deploy the application:

  1. Copy necessary configuration files into the source directory:

### Go

Copy the `app.yaml` file into the source directory:
         
         cp gae_flex_deployment/app.yaml .
         

### Java

Copy the `app.yaml` file into the source directory:
         
         mkdir -p src/main/appengine
         cp gae_flex_deployment/app.yaml src/main/appengine/
         

### Node.js

Copy the `app.yaml` file into the source directory:
         
         cp gae_flex_deployment/app.yaml .
         

### Python

Copy the `app.yaml` file into the source directory:
         
         cp gae_flex_deployment/app.yaml .
         

  2. Run the deploy command:

### Go
         
         gcloud app deploy
         

This might take a few minutes.

### Java
         
         mvn appengine:deploy
         

This might take a few minutes.

### Node.js
         
         gcloud app deploy
         

This might take a few minutes.

### Python
         
         gcloud app deploy
         

This might take a few minutes.




After the deployment is complete, visit your app at the following URL, replacing `[PROJECT_ID]` with your Google Cloud project ID:
    
    
    https://[PROJECT_ID].appspot.com
    

The count on your Redis instance increases each time the app is visited.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
