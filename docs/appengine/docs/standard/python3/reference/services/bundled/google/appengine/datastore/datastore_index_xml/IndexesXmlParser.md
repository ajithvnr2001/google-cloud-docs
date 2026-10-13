---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_index_xml/IndexesXmlParser/
title: google.appengine.datastore.datastore_index_xml.IndexesXmlParser \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:03:58.970613+00:00
---

# google.appengine.datastore.datastore_index_xml.IndexesXmlParser  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_index_xml/IndexesXmlParser/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.datastore.datastore_index_xml.IndexesXmlParser Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_index_xml.py#L80-L175) Provides logic for walking down XML tree and pulling data. Inherits From: [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)

## Methods

### `Parse`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_index_xml.py#L83-L109)
    
    
    Parse(
        xml_str
    )
    

Parses XML string and returns object representation of relevant info. | Args  
---  
  
`xml_str` |  The XML string.   
  
Returns  
---  
An `IndexDefinitions` object containing the result of parsing the XML.   
  
Raises  
---  
  
`ValidationError` |  In case of malformed XML or illegal inputs.   
  
### `ProcessIndexNode`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_index_xml.py#L111-L175)
    
    
    ProcessIndexNode(
        node
    )
    

Processes XML `<datastore-index>` nodes into `Index` objects.

The following information is parsed out:

  * `kind`: Specifies the kind of entities to index.
  * `ancestor`: `True` if the index supports queries that filter by `ancestor-key` to constraint results to a single entity group.
  * `property`: Represents the entity properties to index, with a name and direction attribute.



Args  
---  
  
`node` |  `<datastore-index>` XML node in `datastore-indexes.xml`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
