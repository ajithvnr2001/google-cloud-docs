---
url: https://docs.cloud.google.com/functions/docs/samples/functions-memorystore-redis/
title: Memorystore for Redis \u00a0|\u00a0 Cloud Run functions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:03:12.476083+00:00
---

# Memorystore for Redis  |  Cloud Run functions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/docs/samples/functions-memorystore-redis/

If you are creating a new function, see the [Console Quickstart](https://docs.cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ Samples ](https://docs.cloud.google.com/functions/docs/samples)



#  Memorystore for Redis Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates a Cloud Function that connects to a managed Redis instance.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Connect to a Redis instance from Cloud Run functions](https://docs.cloud.google.com/memorystore/docs/redis/connect-redis-instance-functions)



## Code sample

### Go

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Package visitcount provides a Cloud Function that connects
    // to a managed Redis instance.
    package visitcount
    
    import (
    	"errors"
    	"fmt"
    	"log"
    	"net/http"
    	"os"
    
    	"github.com/GoogleCloudPlatform/functions-framework-go/functions"
    	"github.com/gomodule/redigo/redis"
    )
    
    var redisPool *redis.Pool
    
    func init() {
    	// Register the HTTP handler with the Functions Framework
    	functions.HTTP("VisitCount", visitCount)
    }
    
    // initializeRedis initializes and returns a connection pool
    func initializeRedis() (*redis.Pool, error) {
    	redisHost := os.Getenv("REDISHOST")
    	if redisHost == "" {
    		return nil, errors.New("REDISHOST must be set")
    	}
    	redisPort := os.Getenv("REDISPORT")
    	if redisPort == "" {
    		return nil, errors.New("REDISPORT must be set")
    	}
    	redisAddr := fmt.Sprintf("%s:%s", redisHost, redisPort)
    
    	const maxConnections = 10
    	return &redis.Pool{
    		MaxIdle: maxConnections,
    		Dial: func() (redis.Conn, error) {
    			c, err := redis.Dial("tcp", redisAddr)
    			if err != nil {
    				return nil, fmt.Errorf("redis.Dial: %w", err)
    			}
    			return c, err
    		},
    	}, nil
    }
    
    // visitCount increments the visit count on the Redis instance
    // and prints the current count in the HTTP response.
    func visitCount(w http.ResponseWriter, r *http.Request) {
    	// Initialize connection pool on first invocation
    	if redisPool == nil {
    		// Pre-declare err to avoid shadowing redisPool
    		var err error
    		redisPool, err = initializeRedis()
    		if err != nil {
    			log.Printf("initializeRedis: %v", err)
    			http.Error(w, "Error initializing connection pool", http.StatusInternalServerError)
    			return
    		}
    	}
    
    	conn := redisPool.Get()
    	defer conn.Close()
    
    	counter, err := redis.Int(conn.Do("INCR", "visits"))
    	if err != nil {
    		log.Printf("redis.Int: %v", err)
    		http.Error(w, "Error incrementing visit count", http.StatusInternalServerError)
    		return
    	}
    	fmt.Fprintf(w, "Visit count: %d", counter)
    }
    

### Node.js

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const functions = require('@google-cloud/functions-framework');
    const redis = require('redis');
    
    const REDISHOST = process.env.REDISHOST || 'localhost';
    const REDISPORT = process.env.REDISPORT || 6379;
    
    const redisClient = redis.createClient({
      socket: {
        host: REDISHOST,
        port: REDISPORT,
      },
    });
    redisClient.on('error', err => console.error('ERR:REDIS:', err));
    redisClient.connect();
    
    functions.http('visitCount', async (req, res) => {
      try {
        const response = await redisClient.incr('visits');
        res.writeHead(200, {'Content-Type': 'text/plain'});
        res.end(`Visit count: ${response}`);
      } catch (err) {
        console.log(err);
        res.status(500).send(err.message);
      }
    });
    

### Python

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import os
    
    import functions_framework
    import redis
    
    redis_host = os.environ.get("REDISHOST", "localhost")
    redis_port = int(os.environ.get("REDISPORT", 6379))
    redis_client = redis.StrictRedis(host=redis_host, port=redis_port)
    
    
    @functions_framework.http
    def visit_count(request):
        value = redis_client.incr("visits", 1)
        return f"Visit count: {value}"
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudfunctions). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
