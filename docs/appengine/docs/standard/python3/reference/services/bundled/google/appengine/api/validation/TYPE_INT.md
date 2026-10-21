---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/TYPE_INT/
title: google.appengine.api.validation.TYPE_INT \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:16:12.406756+00:00
---

# google.appengine.api.validation.TYPE_INT  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/TYPE_INT/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.validation.TYPE_INT Stay organized with collections  Save and categorize content based on your preferences. 

Verifies property is of expected type.
    
    
    google.appengine.api.validation.TYPE_INT(
        value, key='???'
    )
    

Can optionally convert value if it is not of the expected type.

It is possible to specify a required field of a specific type in shorthand by merely providing the type. This method is slightly less efficient than providing an explicit type but is not significant unless parsing a large amount of information:
    
    
      class Person(Validated):
        ATTRIBUTES = {'name': unicode,
                      'age': int,
                      }
    

However, in most instances it is best to use the type constants:
    
    
      class Person(Validated):
        ATTRIBUTES = {'name': TypeUnicode,
                      'age': TypeInt,
                      }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
