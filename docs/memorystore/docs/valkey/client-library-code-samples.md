---
url: https://docs.cloud.google.com/memorystore/docs/valkey/client-library-code-samples/
title: Client library code samples \u00a0|\u00a0 Memorystore for Valkey \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:43:16.374802+00:00
---

# Client library code samples  |  Memorystore for Valkey  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/valkey/client-library-code-samples/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Valkey ](https://docs.cloud.google.com/memorystore/docs/valkey)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/valkey/product-overview)



Send feedback 

#  Client library code samples Stay organized with collections  Save and categorize content based on your preferences. 

This page provides code samples for Memorystore for Valkey instances that have both the [Cluster Mode Enabled and Cluster Mode Disabled modes](https://docs.cloud.google.com/memorystore/docs/valkey/cluster-mode-enabled-and-disabled).

## Code samples for Cluster Mode Enabled

Memorystore for Valkey is compatible with all of the Memorystore for Redis Cluster client code samples:

  * Memorystore for Redis Cluster [Client library code samples](https://docs.cloud.google.com/memorystore/docs/cluster/client-library-code-samples)
  * Memorystore for Redis Cluster [Client library connection code samples](https://docs.cloud.google.com/memorystore/docs/cluster/client-library-connection)



### About Valkey GLIDE

Valkey General Language Independent Driver for the Enterprise (GLIDE) is an open-source client library, and it supports all Valkey commands.

You can use [Valkey GLIDE](https://valkey.io/valkey-glide/) to connect your applications to Memorystore for Valkey instances. Valkey GLIDE is designed for reliability, optimized performance, and [high-availability](https://docs.cloud.google.com/memorystore/docs/valkey/ha-and-replicas).

To help ensure consistency in application development and operations, Valkey GLIDE is implemented using a core driver framework, written in [Rust](https://www.rust-lang.org/), with language-specific extensions. This design ensures consistency in features across languages and reduces complexity.

Valkey GLIDE supports Valkey [versions 7.2, 8.0, 9.0, and 9.1](https://docs.cloud.google.com/memorystore/docs/valkey/supported-versions). It's available for the following languages:

  * [C#](https://github.com/valkey-io/valkey-glide-csharp)
  * [Go](https://github.com/valkey-io/valkey-glide/tree/main/go)
  * [Java](https://github.com/valkey-io/valkey-glide/tree/main/java)
  * [Node.js](https://github.com/valkey-io/valkey-glide/tree/main/node)
  * [Python](https://github.com/valkey-io/valkey-glide/tree/main/python)



### Other Valkey OSS client libraries

In addition to Valkey GLIDE, Memorystore for Valkey is compatible with the following Valkey OSS client libraries:

  * [iovalkey](https://github.com/valkey-io/iovalkey)
  * [phpredis](https://github.com/phpredis/phpredis)
  * [predis](https://github.com/predis/predis)
  * [redisson](https://github.com/redisson/redisson)
  * [valkey-go](https://github.com/valkey-io/valkey-go)
  * [valkey-java](https://github.com/valkey-io/valkey-java)
  * [valkey-py](https://github.com/valkey-io/valkey-py)
  * [valkey-swift](https://github.com/valkey-io/valkey-swift)



### Systems and services

You can use [Spring Boot](https://spring.io/projects/spring-boot), [PostgreSQL](https://www.postgresql.org/), and Memorystore for Valkey to create the following systems and services:

  * [Session management system](https://github.com/GoogleCloudPlatform/memorystore-samples/tree/main/session): session management is a crucial part of modern web applications, ensuring that user interactions remain consistent and secure across multiple requests. By using a caching layer, your application can manage user sessions efficiently while reducing the load on your database and ensuring scalability.
  * [Scalable leaderboard system](https://github.com/GoogleCloudPlatform/memorystore-samples/tree/main/leaderboard): leaderboards are a useful way to display ranking data in applications. By using a caching layer, you can deliver real-time leaderboard rankings while reducing your database load.
  * [High-performance caching service](https://github.com/GoogleCloudPlatform/memorystore-samples/tree/main/caching): modern applications need to deliver fast, responsive user experiences at scale. By building this caching service, you can reduce both latency and your database load.



## Code samples for Cluster Mode Disabled

Memorystore for Valkey Cluster Mode Disabled is compatible with all Redis and Valkey OSS client libraries listed in Code samples for Cluster Mode Enabled.

When you use a Cluster Mode Disabled instance in Memorystore for Valkey, complete the following actions:

  * Instead of the `RedisCluster` or `ValkeyCluster` client object that the library provides, use the Redis or Valkey client object.
  * Create a writer client by using the primary endpoint IP address.
  * Create a reader client by using the reader endpoint IP address.




### redis-py

We recommend using [redis-py](https://github.com/redis/redis-py), versions 5.1 and later.
    
    
    import redis
    primaryEndpoint = PRIMARY_ENDPOINT_IP
    readerEndpoint = READER_ENDPOINT_IP
    
    primary_client = redis.Redis(host=primaryEndpoint, port=6379, db=0, decode_responses=True)
    reader_client = redis.Redis(host=readerEndpoint, port=6379, db=0, decode_responses=True)
    
    primary_client.set("key","value")
    print(reader_client.get("key"))
    

### go-redis

We recommend using [go-redis](https://github.com/redis/go-redis), versions 9.11.0 and later.
    
    
    package main
    
    import (
    "context"
    "fmt"
    "github.com/redis/go-redis/v9"
    )
    
    func main() {
    primary_endpoint := PRIMARY_ENDPOINT_IP
    reader_endpoint := READER_ENDPOINT_IP
    
    primary_client := redis.NewClient(&redis.Options{
      Addr:     primary_endpoint,
      Password: "", // no password set
      DB:       0,  // use default DB
    })
    
    reader_client := redis.NewClient(&redis.Options{
      Addr:     reader_endpoint,
      Password: "", // no password set
      DB:       0,  // use default DB
    })
    
    ctx := context.Background()
    
    err := primary_client.Set(ctx, "foo", "bar", 0).Err()
    if err != nil {
      panic(err)
    }
    
    val, err := reader_client.Get(ctx, "foo").Result()
    if err != nil {
      panic(err)
    }
    fmt.Println("foo", val)
    }
    
    

### Jedis

We recommend using [Jedis](https://github.com/redis/jedis), versions 4.4.0 and later.
    
    
    
    package org.example;
    
    import java.io.*;
    import java.time.LocalDateTime;
    import java.lang.Thread;
    import java.util.HashMap;
    import java.util.Map;
    
    import redis.clients.jedis.HostAndPort;
    import redis.clients.jedis.JedisPoolConfig;
    import redis.clients.jedis.Jedis;
    import redis.clients.jedis.JedisPool;
    
    public class Main
    {
    public static void main( String[] args )
    {
      primaryEndpoint = PRIMARY_ENDPOINT_IP
    
      JedisPool pool = new JedisPool(primaryEndpoint, 6379);
    
      try (Jedis jedis = pool.getResource()) {
        jedis.set("foo", "bar");
        System.out.println(jedis.get("foo")); // prints bar
    
        Map hash = new HashMap<>();;
        hash.put("name", "John");
        hash.put("surname", "Smith");
        hash.put("company", "Redis");
        hash.put("age", "29");
        jedis.hset("user-session:123", hash);
        System.out.println(jedis.hgetAll("user-session:123"));
        // Prints: {name=John, surname=Smith, company=Redis, age=29}
      } catch (Exception e) {
        System.out.println("Error setting or getting  key: " + e.getMessage());
      }
    }
    }
    

### Node.js

We recommend using [Node.js](https://github.com/redis/node-redis), versions 24.4.1 and later.
    
    
    import { createClient } from 'redis';
    import * as fs from 'fs';
    
    const primaryEndpoint = PRIMARY_ENDPOINT_IP
    
    const primary_endpoint_url ='redis://primaryEndpoint:6379'
    
    const client = createClient({
    url: primary_endpoint_url
    });
    
    await client.connect();
    await client.set(key, value);
    const retval = await client.get(key);
    console.log(retval)
    
    

### Code sample for both IAM authentication and in-transit encryption

This section gives an example of how to authenticate and connect to a Memorystore for Valkey instance by using both [IAM authentication](https://docs.cloud.google.com/memorystore/docs/valkey/about-iam-auth) and [in-transit encryption](https://docs.cloud.google.com/memorystore/docs/valkey/about-in-transit-encryption) with various client libraries.

### redis-py

We recommend using [redis-py](https://github.com/redis/redis-py), versions 5.1 and later.
    
    
    from google.cloud import iam_credentials_v1
    from redis.backoff import ConstantBackoff
    from redis.retry import Retry
    from redis.exceptions import (
    ConnectionError,
    AuthenticationWrongNumberOfArgsError,
    AuthenticationError
    )
    from redis.utils import (str_if_bytes)
    
    import redis
    
    service_account="projects/-/serviceAccounts/<TO-DO-1: your service account that used to authenticate to Valkey>""
    
    host=<TO-DO-2: your Redis Cluster discovery endpoint ip>
    ssl_ca_certs=<TO-DO-3, your trusted server ca file name>
    
    def generate_access_token():
      # Create a client
      client = iam_credentials_v1.IAMCredentialsClient()
    
      # Initialize request argument(s)
      request = iam_credentials_v1.GenerateAccessTokenRequest(
          name=service_account,
          scope=['https://www.googleapis.com/auth/cloud-platform'],
      )
    
      # Make the request
      response = client.generate_access_token(request=request)
      print(str(response.access_token))
    
      # Handle the response
      return str(response.access_token)
    
    class ValkeyTokenProvider(redis.CredentialProvider):
    
        # Generated IAM tokens are valid for 15 minutes
        def get_credentials(self):
            token= generate_access_token()
            return "default",token
    
    creds_provider = ValkeyTokenProvider()
    client = redis.Redis(host=host, port=6379, credential_provider=creds_provider, ssl=True, ssl_ca_certs=caFilePath)
    client.set('foo',"bar")
    print(client.get('foo'))
    
    

### Go

We recommend using [Go](https://go.dev/), versions 1.24.5 and later.
    
    
    package main
    
    import (
      "context"
      "crypto/tls"
      "crypto/x509"
      "flag"
      "fmt"
      "io/ioutil"
      "log"
      "sync"
      "time"
    
      credentials "google.golang.org/genproto/googleapis/iam/credentials/v1"
    
      "github.com/golang/protobuf/ptypes"
      "github.com/redis/go-redis/v9"
      "google.golang.org/api/option"
      gtransport "google.golang.org/api/transport/grpc"
    )
    
    var (
      svcAccount               = flag.String("a", "projects/-/serviceAccounts/example-service-account@example-project.iam.gserviceaccount.com", "service account email")
      lifetime                 = flag.Duration("d", time.Hour, "lifetime of token")
      refreshDuration          = flag.Duration("r", 5*time.Minute, "token refresh duration")
      checkTokenExpiryInterval = flag.Duration("e", 10*time.Second, "check token expiry interval")
      lastRefreshInstant       = time.Time{}
      errLastSeen              = error(nil)
      token                    = ""
      mu                       = sync.RWMutex{}
      err                      = error(nil)
    )
    
    func retrieveToken() (string, error) {
      ctx := context.Background()
      conn, err := gtransport.Dial(ctx,
        option.WithEndpoint("iamcredentials.googleapis.com:443"),
        option.WithScopes("https://www.googleapis.com/auth/cloud-platform"))
    
      if err != nil {
        log.Printf("Failed to dial API, error: %v", err)
        return token, err
      }
      client := credentials.NewIAMCredentialsClient(conn)
      req := credentials.GenerateAccessTokenRequest{
        Name:     *svcAccount,
        Scope:    []string{"https://www.googleapis.com/auth/cloud-platform"},
        Lifetime: ptypes.DurationProto(*lifetime),
      }
      rsp, err := client.GenerateAccessToken(ctx, &req)
      if err != nil {
        log.Printf("Failed to call GenerateAccessToken with request: %v, error: %v", req, err)
        return token, err
      }
      return rsp.AccessToken, nil
    }
    
    func refreshTokenLoop() {
      if *refreshDuration > *lifetime {
        log.Fatal("Refresh should not happen after token is already expired.")
      }
      for {
        mu.RLock()
        lastRefreshTime := lastRefreshInstant
        mu.RUnlock()
        if time.Now().After(lastRefreshTime.Add(*refreshDuration)) {
          var err error
          retrievedToken, err := retrieveToken()
          mu.Lock()
          token = retrievedToken
          if err != nil {
            errLastSeen = err
          } else {
            lastRefreshInstant = time.Now()
          }
          mu.Unlock()
        }
        time.Sleep(*checkTokenExpiryInterval)
      }
    }
    
    func retrieveTokenFunc() (string, string) {
      mu.RLock()
      defer mu.RUnlock()
      if time.Now().After(lastRefreshInstant.Add(*refreshDuration)) {
        log.Printf("Token is expired. last refresh instant: %v, refresh duration: %v, error that was last seen: %v", lastRefreshInstant, *refreshDuration, errLastSeen)
        return "", ""
      }
      username := "default"
      password := token
      return username, password
    }
    
    func main() {
      caFilePath := CA_FILE_PATH
      clusterDicEpAddr := PRIMARY_ENDPOINT_IP_ADDRESS_AND_PORT
      caCert, err := ioutil.ReadFile(caFilePath)
      if err != nil {
        log.Fatal(err)
      }
      caCertPool := x509.NewCertPool()
      caCertPool.AppendCertsFromPEM(caCert)
      token, err = retrieveToken()
      if err != nil {
        log.Fatal("Cannot retrieve IAM token to authenticate to the cluster, error: %v", err)
      }
      token, err = retrieveToken()
      fmt.Printf("token : %v", token)
      if err != nil {
        log.Fatal("Cannot retrieve IAM token to authenticate to the cluster, error: %v", err)
      }
      lastRefreshInstant = time.Now()
      go refreshTokenLoop()
    
      client := redis.NewClient(&redis.Options{
        Addr:                clusterDicEpAddr,
        CredentialsProvider: retrieveTokenFunc,
        TLSConfig: &tls.Config{
          RootCAs: caCertPool,
        },
      })
    
      ctx := context.Background()
      err = client.Set(ctx, "foo", "bar", 0).Err()
      if err != nil {
        log.Fatal(err)
      }
      val, err := client.Get(ctx, "foo").Result()
      if err != nil {
        log.Fatal(err)
      }
      fmt.Printf("\nGot the value for key: key, which is %s \n", val)
    }
    
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
