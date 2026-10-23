---
url: https://docs.cloud.google.com/firestore/docs/samples/firestore-solution-sharded-counter-get/
title: Getting a Firestore document while using shards \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:09:01.820411+00:00
---

# Getting a Firestore document while using shards  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/docs/samples/firestore-solution-sharded-counter-get/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore ](https://docs.cloud.google.com/firestore/docs)
  * [ Samples ](https://docs.cloud.google.com/firestore/docs/samples)



#  Getting a Firestore document while using shards Stay organized with collections  Save and categorize content based on your preferences. 

Getting a Firestore document while using shards

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Support frequent and distributed counters](https://docs.cloud.google.com/firestore/native/docs/solutions/counters)



## Code sample

### C#

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /// <summary>
    /// Get total count across all shards.
    /// </summary>
    /// <param name="docRef">The document reference <see cref="DocumentReference"/></param>
    /// <returns>The <see cref="int"/></returns>
    private static async Task<int> GetCountAsync(DocumentReference docRef)
    {
        var snapshotList = await docRef.Collection("shards").GetSnapshotAsync();
        return snapshotList.Sum(shard => shard.GetValue<int>("count"));
    }

### Go

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // getCount returns a total count across all shards.
    func (c *Counter) getCount(ctx context.Context, docRef *firestore.DocumentRef) (int64, error) {
    	var total int64
    	shards := docRef.Collection("shards").Documents(ctx)
    	for {
    		doc, err := shards.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			return 0, fmt.Errorf("Next: %w", err)
    		}
    
    		vTotal := doc.Data()["Count"]
    		shardCount, ok := vTotal.(int64)
    		if !ok {
    			return 0, fmt.Errorf("firestore: invalid dataType %T, want int64", vTotal)
    		}
    		total += shardCount
    	}
    	return total, nil
    }
    

### PHP

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    $result = 0;
    $docCollection = $db->collection('samples/php/distributedCounters')->documents();
    foreach ($docCollection as $doc) {
        $result += $doc->data()['Cnt'];
    }

### Python

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def get_count(self, doc_ref):
        """Return a total count across all shards."""
        total = 0
        shards = doc_ref.collection("shards").list_documents()
        for shard in shards:
            total += shard.get().to_dict().get("count", 0)
        return total
    

### Ruby

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # project_id = "Your Google Cloud Project ID"
    # collection_path = "shards"
    
    require "google/cloud/firestore"
    
    firestore = Google::Cloud::[Firestore](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore-admin/latest/Google-Cloud-Firestore.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore/latest/Google-Cloud-Firestore.html) project_id: project_id
    
    shards_ref = firestore.[col_group](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore/latest/Google-Cloud-Firestore-Client.html) collection_path
    
    count = 0
    shards_ref.get do |doc_ref|
      count += doc_ref[:count]
    end
    
    puts "Count value is #{count}."

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=firestore). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
