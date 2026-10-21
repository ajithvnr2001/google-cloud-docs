---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_stub_index/GenerateIndexFromHistory/
title: google.appengine.datastore.datastore_stub_index.GenerateIndexFromHistory \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T12:42:52.087000+00:00
---

# google.appengine.datastore.datastore_stub_index.GenerateIndexFromHistory  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_stub_index/GenerateIndexFromHistory/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.datastore.datastore_stub_index.GenerateIndexFromHistory Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_stub_index.py#L185-L217) Generate most of the text for index.yaml from the query history.
    
    
    google.appengine.datastore.datastore_stub_index.GenerateIndexFromHistory(
        query_history, all_indexes=None, manual_indexes=None
    )
    

| 

## Args  
  
---  
  
`query_history` |  Query history, a dict mapping datastore_pb.Query to a count of the number of times that query has been issued.   
`all_indexes` |  Optional datastore_index.IndexDefinitions instance representing all the indexes found in the input file. May be None.   
`manual_indexes` |  Optional datastore_index.IndexDefinitions instance containing indexes for which we should not generate output. May be None.   
  
## Returns  
  
---  
A string representation that can safely be appended to an existing index.yaml file. Returns the empty string if it would generate no output.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
