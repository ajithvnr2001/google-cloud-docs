---
url: https://docs.cloud.google.com/firestore/docs/samples/firestore-solution-sharded-counter-increment/
title: Incrementing a Firestore document field while using shards \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:25:35.471146+00:00
---

# Incrementing a Firestore document field while using shards  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/docs/samples/firestore-solution-sharded-counter-increment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore ](https://docs.cloud.google.com/firestore/docs)
  * [ Samples ](https://docs.cloud.google.com/firestore/docs/samples)



#  Incrementing a Firestore document field while using shards Stay organized with collections  Save and categorize content based on your preferences. 

Incrementing a Firestore document field while using shards

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Support frequent and distributed counters](https://docs.cloud.google.com/firestore/native/docs/solutions/counters)



## Code sample

### C#

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /// <summary>
    /// Increment a randomly picked shard by 1.
    /// </summary>
    /// <param name="docRef">The document reference <see cref="DocumentReference"/></param>
    /// <returns>The <see cref="Task"/></returns>
    private static async Task IncrementCounterAsync(DocumentReference docRef, int numOfShards)
    {
        int documentId;
        lock (s_randLock)
        {
            documentId = s_rand.Next(numOfShards);
        }
        var shardRef = docRef.Collection("shards").Document(documentId.ToString());
        await shardRef.UpdateAsync("count", FieldValue.Increment(1));
    }

### Go

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // incrementCounter increments a randomly picked shard.
    func (c *Counter) incrementCounter(ctx context.Context, docRef *firestore.DocumentRef) (*firestore.WriteResult, error) {
    	docID := strconv.Itoa(rand.Intn(c.numShards))
    
    	shardRef := docRef.Collection("shards").Doc(docID)
    	return shardRef.Update(ctx, []firestore.Update{
    		{Path: "Count", Value: firestore.Increment(1)},
    	})
    }
    

### PHP

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    $ref = $db->collection('samples/php/distributedCounters');
    $numShards = 0;
    $docCollection = $ref->documents();
    foreach ($docCollection as $doc) {
        $numShards++;
    }
    $shardIdx = random_int(0, max(1, $numShards) - 1);
    $doc = $ref->document((string) $shardIdx);
    $doc->update([
        ['path' => 'Cnt', 'value' => FieldValue::increment(1)]
    ]);

### Python

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def increment_counter(self, doc_ref):
        """Increment a randomly picked shard."""
        doc_id = random.randint(0, self._num_shards - 1)
    
        shard_ref = doc_ref.collection("shards").document(str(doc_id))
        return shard_ref.update({"count": firestore.Increment(1)})
    

### Ruby

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # project_id = "Your Google Cloud Project ID"
    # num_shards = "Number of shards for distributed counter"
    # collection_path = "shards"
    
    require "google/cloud/firestore"
    
    firestore = Google::Cloud::[Firestore](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore-admin/latest/Google-Cloud-Firestore.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore/latest/Google-Cloud-Firestore.html) project_id: project_id
    
    # Select a shard of the counter at random
    shard_id = rand 0...num_shards
    shard_ref = firestore.doc "#{collection_path}/#{shard_id}"
    
    # increment counter
    shard_ref.update({ count: firestore.[field_increment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore/latest/Google-Cloud-Firestore-Client.html)(1) })
    
    puts "Counter incremented."

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=firestore). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
