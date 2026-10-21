---
url: https://docs.cloud.google.com/memorystore/docs/redis/connect-redis-instance-cloud-run/
title: Connect to a Redis instance from a Cloud Run service \u00a0|\u00a0 Memorystore for Redis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:53:15.559135+00:00
---

# Connect to a Redis instance from a Cloud Run service  |  Memorystore for Redis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/redis/connect-redis-instance-cloud-run/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis ](https://docs.cloud.google.com/memorystore/docs/redis)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/redis/redis-overview)



Send feedback 

#  Connect to a Redis instance from a Cloud Run service Stay organized with collections  Save and categorize content based on your preferences. 

You can connect to a Redis instance from Cloud Run by using [Direct VPC egress](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc).

**Important** : We recommend that you use Direct VPC egress because it offers lower latency, higher throughput, and lower costs by eliminating the need for managed connector instances.

You can also connect to a Redis instance from Cloud Run by using [Serverless VPC Access](https://docs.cloud.google.com/vpc/docs/configure-serverless-vpc-access). To use a Serverless VPC Access connector, see [VPC with connectors](https://docs.cloud.google.com/run/docs/configuring/vpc-connectors).

## Setup

If you have already installed the Google Cloud CLI and have created a Redis instance, you can skip these steps.

  1. [Install the gcloud CLI](https://cloud.google.com/sdk/docs/) and initialize:
         
         gcloud init
         

  2. Follow the [Quickstart Guide](https://docs.cloud.google.com/memorystore/docs/redis/create-instance-gcloud) to create a Redis instance. Take note of the zone, IP address, and port of the Redis instance.




## Prepare VPC network egress for configuration

To connect to your Redis instance, your Cloud Run service must have access to the Redis instance's authorized VPC network.

To find the name of this network, run the following command:
    
    
        gcloud redis instances describe INSTANCE_ID --region REGION --format "value(authorizedNetwork)"
    

Make a note of the network name.

## Sample application

This sample HTTP server application establishes a connection to a Redis instance from a Cloud Run service.

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
    Werkzeug==3.1.8; python_version >= '3.9'

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

## Deploying the application to Cloud Run

To deploy the application:

  1. Copy the `Dockerfile` into the source directory:
         
         cp cloud_run_deployment/Dockerfile .
         

  2. Build a container image using Cloud Build by running the following command:
         
         gcloud artifacts repositories create --location REPO_REGION --repository-format=docker REPO_ID
         gcloud builds submit --pack image=REPO_REGION-docker.pkg.dev/PROJECT_ID/REPO_ID/visit-counter:v1
         

  3. Deploy the container to Cloud Run by running the following command:
         
         gcloud run deploy \
           --image REPO_REGION-docker.pkg.dev/PROJECT_ID/REPO_ID/visit-counter:v1 \
           --allow-unauthenticated \
           --region REGION \
           --network NETWORK \
           --subnet SUBNET \
           --set-env-vars REDISHOST=REDIS_IP,REDISPORT=REDIS_PORT
         

where:

     * `REPO_REGION` is the region of the repository.
     * `REPO_ID` is the repository name containing the application image.
     * `PROJECT_ID` is your Google Cloud project's ID.
     * `REGION` is the region where your Redis instance is located.
     * `NETWORK` is the name of the authorized VPC network that your Redis instance is attached to.
     * `SUBNET` is the name of your subnet. The subnet must be `/26` or larger. Direct VPC egress supports IPv4 ranges [RFC 1918](https://tools.ietf.org/html/rfc1918#section-3), [RFC 6598](https://tools.ietf.org/html/rfc6598#section-7), and Class E.
     * `REDIS_IP` and `REDIS_PORT` are the IP address and port number of your Redis instance.



After the deployment successfully completes, the command line displays your Cloud Run service's URL. Visit this URL in a web browser (or use a tool like `curl`) and see the count on your Redis instance increase each time the service is visited.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
