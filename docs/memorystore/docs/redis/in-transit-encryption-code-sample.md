---
url: https://docs.cloud.google.com/memorystore/docs/redis/in-transit-encryption-code-sample/
title: In-transit encryption client library code sample \u00a0|\u00a0 Memorystore for Redis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:33:53.102873+00:00
---

# In-transit encryption client library code sample  |  Memorystore for Redis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/redis/in-transit-encryption-code-sample/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis ](https://docs.cloud.google.com/memorystore/docs/redis)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/redis/redis-overview)



Send feedback 

#  In-transit encryption client library code sample Stay organized with collections  Save and categorize content based on your preferences. 

This code sample shows a [go-redis client library](https://github.com/redis/go-redis) configuration for connecting to a Memorystore for Redis instance that has [in-transit encryption](https://docs.cloud.google.com/memorystore/docs/redis/about-in-transit-encryption) enabled.

## Connect to an instance

The following sample provides an example of how to instantiate a client, load an in-transit encryption Certificate Authority, and how to set up a connection pool.

### Go
    
    
    import (
    	"context"
    	"crypto/tls"
    	"crypto/x509"
    	"errors"
    	"fmt"
    	"io"
    	"time"
    
    	memorystore "cloud.google.com/go/redis/apiv1"
    	redispb "cloud.google.com/go/redis/apiv1/redispb"
    	"github.com/go-redis/redis/v8"
    )
    
    // ConnectToDatabase demonstrates how to use go-redis library to connect to a
    // Memorystore Redis instance.
    func ConnectToDatabase(w io.Writer, projectID, location, instanceID string) error {
    
    	// Instantiate a Redis administrative client
    	ctx := context.Background()
    	adminClient, err := memorystore.NewCloudRedisClient(ctx)
    	if err != nil {
    		return err
    	}
    	defer adminClient.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/redis/latest/apiv1.html#cloud_google_com_go_redis_apiv1_CloudRedisClient_Close)()
    
    	req := &redispb.GetInstanceRequest{
    		Name: fmt.Sprintf("projects/%s/locations/%s/instances/%s", projectID, location, instanceID),
    	}
    
    	instance, err := adminClient.GetInstance(ctx, req)
    	if err != nil {
    		return err
    	}
    
    	fmt.Fprintln(w, instance)
    
    	// Load CA cert
    	caCerts := instance.GetServerCaCerts()
    	if len(caCerts) == 0 {
    		return errors.New("memorystore: no server CA certs for instance")
    	}
    
    	caCertPool := x509.NewCertPool()
    	caCertPool.AppendCertsFromPEM([]byte(caCerts[0].Cert))
    
    	// Setup Redis Connection pool
    	client := redis.NewClient(&redis.Options{
    		Addr:         fmt.Sprintf("%s:%d", instance.Host, instance.Port),
    		Password:     "PASSWORD",
    		PoolSize:     1,
    		MinIdleConns: 1,
    		PoolTimeout:  0,
    		IdleTimeout:  20 * time.Second,
    		DialTimeout:  2 * time.Second,
    		TLSConfig: &tls.Config{
    			RootCAs: caCertPool,
    		},
    	})
    
    	p, err := client.Ping(ctx).Result()
    	if err != nil {
    		return err
    	}
    	fmt.Fprintf(w, "Response:\n%s", p)
    
    	return nil
    }
    

## What's next

  * Learn more about [in-transit encryption](https://docs.cloud.google.com/memorystore/docs/redis/about-in-transit-encryption).
  * Learn how to [enable in-transit encryption](https://docs.cloud.google.com/memorystore/docs/redis/manage-in-transit-encryption) on an instance.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
