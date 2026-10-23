---
url: https://docs.cloud.google.com/firestore/docs/samples/firestore-solution-sharded-counter-create/
title: Create a Firestore sharded counter \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:08:51.396519+00:00
---

# Create a Firestore sharded counter  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/docs/samples/firestore-solution-sharded-counter-create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore ](https://docs.cloud.google.com/firestore/docs)
  * [ Samples ](https://docs.cloud.google.com/firestore/docs/samples)



#  Create a Firestore sharded counter Stay organized with collections  Save and categorize content based on your preferences. 

Create a Firestore sharded counter

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Support frequent and distributed counters](https://docs.cloud.google.com/firestore/native/docs/solutions/counters)



## Code sample

### C#

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /// <summary>
    /// Create a given number of shards as a
    /// subcollection of specified document.
    /// </summary>
    /// <param name="docRef">The document reference <see cref="DocumentReference"/></param>
    private static async Task CreateCounterAsync(DocumentReference docRef, int numOfShards)
    {
        CollectionReference colRef = docRef.Collection("shards");
        var tasks = new List<Task>();
        // Initialize each shard with Count=0
        for (var i = 0; i < numOfShards; i++)
        {
            tasks.Add(colRef.Document(i.ToString()).SetAsync(new Shard() { Count = 0 }));
        }
        await Task.WhenAll(tasks);
    }

### Go

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // initCounter creates a given number of shards as
    // subcollection of specified document.
    func (c *Counter) initCounter(ctx context.Context, docRef *firestore.DocumentRef) error {
    	colRef := docRef.Collection("shards")
    
    	// Initialize each shard with count=0
    	for num := 0; num < c.numShards; num++ {
    		shard := Shard{0}
    
    		if _, err := colRef.Doc(strconv.Itoa(num)).Set(ctx, shard); err != nil {
    			return fmt.Errorf("Set: %w", err)
    		}
    	}
    	return nil
    }
    

### PHP

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    $numShards = 10;
    $ref = $db->collection('samples/php/distributedCounters');
    for ($i = 0; $i < $numShards; $i++) {
        $doc = $ref->document((string) $i);
        $doc->set(['Cnt' => 0]);
    }

### Python

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def init_counter(self, doc_ref):
        """
        Create a given number of shards as
        subcollection of specified document.
        """
        col_ref = doc_ref.collection("shards")
    
        # Initialize each shard with count=0
        for num in range(self._num_shards):
            shard = Shard()
            col_ref.document(str(num)).set(shard.to_dict())
    

### Ruby

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # project_id = "Your Google Cloud Project ID"
    # num_shards = "Number of shards for distributed counter"
    # collection_path = "shards"
    
    require "google/cloud/firestore"
    
    firestore = Google::Cloud::[Firestore](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore-admin/latest/Google-Cloud-Firestore.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore/latest/Google-Cloud-Firestore.html) project_id: project_id
    
    shards_ref = firestore.col collection_path
    
    # Initialize each shard with count=0
    num_shards.times do |i|
      shards_ref.doc(i).set({ count: 0 })
    end
    
    puts "Distributed counter shards collection created."

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=firestore). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
