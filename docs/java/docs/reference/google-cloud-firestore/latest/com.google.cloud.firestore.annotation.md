---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.annotation
title: Package com.google.cloud.firestore.annotation (3.49.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:11:49.540591+00:00
---

# Package com.google.cloud.firestore.annotation (3.49.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.annotation

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Package com.google.cloud.firestore.annotation (3.49.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.49.0 (latest)  3.45.0  3.44.0  3.43.1  3.41.0  3.38.0  3.37.0  3.36.0  3.35.1  3.33.4  3.32.2  3.31.9  3.30.11  3.28.0  3.27.2  3.26.5  3.25.1  3.24.3  3.22.0  3.21.4  3.20.0  3.17.0  3.16.3  3.15.7  3.14.4  3.13.2  3.12.1  3.11.0  3.10.0  3.9.6  3.8.2  3.7.10  3.6.0  3.5.0  3.4.2  3.3.0  3.2.0  3.1.0  3.0.21 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-firestore/google-cloud-firestore/src/main/java/com/google/cloud/firestore/annotation)  
---  
  
## This package is not the recommended entry point to using this client library!

For this library, we recommend using [com.google.cloud.firestore](https://cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore) for new applications.

## Interfaces

Interface |  Description  
---|---  
[com.google.cloud.firestore.annotation.DocumentId](https://cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.annotation.DocumentId) |  Annotation used to mark a POJO property to be automatically populated with the document's ID when the POJO is created from a Cloud Firestore document (for example, via DocumentSnapshot#toObject). Any of the following will throw a runtime exception:  
[com.google.cloud.firestore.annotation.Exclude](https://cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.annotation.Exclude) |  Marks a field as excluded from the Database.  
[com.google.cloud.firestore.annotation.IgnoreExtraProperties](https://cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.annotation.IgnoreExtraProperties) |  Properties that don't map to class fields are ignored when serializing to a class annotated with this annotation.  
[com.google.cloud.firestore.annotation.PropertyName](https://cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.annotation.PropertyName) |  Marks a field to be renamed when serialized.  
[com.google.cloud.firestore.annotation.ServerTimestamp](https://cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.annotation.ServerTimestamp) |  Annotation used to mark a timestamp field as being populated via Server Timestamps. If a POJO being written contains null for a @ServerTimestamp annotated field, it will be replaced with a server-generated timestamp.  
[com.google.cloud.firestore.annotation.ThrowOnExtraProperties](https://cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.annotation.ThrowOnExtraProperties) |  Properties that don't map to class fields when serializing to a class annotated with this annotation cause an exception to be thrown.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
