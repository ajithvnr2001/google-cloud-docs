---
url: https://docs.cloud.google.com/firestore/docs/samples/firestore-solution-sharded-counter-custom-type/
title: Create custom shard and counter types for Firestore distributed counters \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:58:57.560755+00:00
---

# Create custom shard and counter types for Firestore distributed counters  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/docs/samples/firestore-solution-sharded-counter-custom-type/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore ](https://docs.cloud.google.com/firestore/docs)
  * [ Samples ](https://docs.cloud.google.com/firestore/docs/samples)



#  Create custom shard and counter types for Firestore distributed counters Stay organized with collections  Save and categorize content based on your preferences. 

Create custom shard and counter types for Firestore distributed counters

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Support frequent and distributed counters](https://docs.cloud.google.com/firestore/native/docs/solutions/counters)



## Code sample

### C#

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /// <summary>
    /// Shard is a document that contains the count.
    /// </summary>
    [FirestoreData]
    public class Shard
    {
        [FirestoreProperty(name: "count")]
        public int Count { get; set; }
    }

### Go

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"math/rand"
    	"strconv"
    
    	"cloud.google.com/go/firestore"
    	"google.golang.org/api/iterator"
    )
    
    // Counter is a collection of documents (shards)
    // to realize counter with high frequency.
    type Counter struct {
    	numShards int
    }
    
    // Shard is a single counter, which is used in a group
    // of other shards within Counter.
    type Shard struct {
    	Count int
    }
    

### Python

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import random
    
    from google.cloud import firestore
    
    
    class Shard:
        """
        A shard is a distributed counter. Each shard can support being incremented
        once per second. Multiple shards are needed within a Counter to allow
        more frequent incrementing.
        """
    
        def __init__(self):
            self._count = 0
    
        def to_dict(self):
            return {"count": self._count}
    
    
    class Counter:
        """
        A counter stores a collection of shards which are
        summed to return a total count. This allows for more
        frequent incrementing than a single document.
        """
    
        def __init__(self, num_shards):
            self._num_shards = num_shards
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=firestore). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
