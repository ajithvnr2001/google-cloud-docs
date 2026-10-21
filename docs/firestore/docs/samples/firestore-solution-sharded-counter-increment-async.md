---
url: https://docs.cloud.google.com/firestore/docs/samples/firestore-solution-sharded-counter-increment-async/
title: Incrementing a Firestore document field while using shards (async) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:58:56.953286+00:00
---

# Incrementing a Firestore document field while using shards (async)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/docs/samples/firestore-solution-sharded-counter-increment-async/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore ](https://docs.cloud.google.com/firestore/docs)
  * [ Samples ](https://docs.cloud.google.com/firestore/docs/samples)



#  Incrementing a Firestore document field while using shards (async) Stay organized with collections  Save and categorize content based on your preferences. 

Incrementing a Firestore document field while using shards (async).

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Support frequent and distributed counters](https://docs.cloud.google.com/firestore/native/docs/solutions/counters)



## Code sample

### Python

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    async def increment_counter(self, doc_ref):
        """Increment a randomly picked shard."""
        doc_id = random.randint(0, self._num_shards - 1)
    
        shard_ref = doc_ref.collection("shards").document(str(doc_id))
        return await shard_ref.update({"count": firestore.Increment(1)})
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=firestore). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
