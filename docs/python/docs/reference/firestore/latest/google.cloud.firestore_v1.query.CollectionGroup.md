---
url: https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.query.CollectionGroup
title: Class CollectionGroup (2.34.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:07:36.881118+00:00
---

# Class CollectionGroup (2.34.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.query.CollectionGroup

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class CollectionGroup (2.34.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.34.0 (latest)  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.1  2.27.0  2.26.0  2.23.0  2.22.0  2.21.0  2.20.2  2.19.0  2.18.0  2.17.2  2.16.1  2.15.0  2.14.0  2.13.1  2.12.0  2.11.1  2.10.1  2.9.1  2.8.0  2.7.3  2.6.1  2.5.3  2.4.0  2.3.4  2.2.0  2.1.3  2.0.2  1.9.2  1.8.1  1.7.0  1.6.2  1.5.0  1.4.0  1.3.0 
    
    
    CollectionGroup(
        parent,
        projection=None,
        field_filters=(),
        orders=(),
        limit=None,
        limit_to_last=False,
        offset=None,
        start_at=None,
        end_at=None,
        all_descendants=True,
        recursive=False,
    )

Represents a Collection Group in the Firestore API.

This is a specialization of `.Query` that includes all documents in the database that are contained in a collection or subcollection of the given parent.

## Parameter  
  
---  
**Name** | **Description**  
`parent` |  `[CollectionReference](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.collection.CollectionReference)`   
The collection that this query applies to.  
  
## Methods 

### get_partitions
    
    
    get_partitions(
        partition_count,
        retry: retries.Retry | object | None = _MethodDefault._DEFAULT_VALUE,
        timeout: float | None = None,
        *,
        read_time: Optional[datetime.datetime] = None
    ) -> Generator[QueryPartition, None, None]

Partition a query for parallelization.

Partitions a query by returning partition cursors that can be used to run the query in parallel. The returned partition cursors are split points that can be used as starting/end points for the query results.

**Parameters**  
---  
**Name** | **Description**  
`partition_count` |  `int`   
The desired maximum number of partition points. The number must be strictly positive. The actual number of partitions returned may be fewer.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried. Defaults to a system-specified policy.  
`timeout` |  `float`   
The timeout for this request. Defaults to a system-specified value.  
`read_time` |  `Optional[datetime.datetime]`   
If set, reads documents as they were at the given time. This must be a microsecond precision timestamp within the past one hour, or if Point-in-Time Recovery is enabled, can additionally be a whole minute timestamp within the past 7 days. For the most accurate results, use UTC timezone.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
