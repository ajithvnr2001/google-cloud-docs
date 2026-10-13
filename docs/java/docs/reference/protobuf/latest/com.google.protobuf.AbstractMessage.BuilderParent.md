---
url: https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.BuilderParent
title: Interface AbstractMessage.BuilderParent (3.19.4) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:58:08.094388+00:00
---

# Interface AbstractMessage.BuilderParent (3.19.4)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.BuilderParent

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface AbstractMessage.BuilderParent (3.19.4) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    protected static interface AbstractMessage.BuilderParent

Interface for the parent of a Builder that allows the builder to communicate invalidations back to the parent for use when using nested builders.

## Methods 

### markDirty()
    
    
    public abstract void markDirty()

A builder becomes dirty whenever a field is modified -- including fields in nested builders \-- and becomes clean when build() is called. Thus, when a builder becomes dirty, all its parents become dirty as well, and when it becomes clean, all its children become clean. The dirtiness state is used to invalidate certain cached values.

To this end, a builder calls markDirty() on its parent whenever it transitions from clean to dirty. The parent must propagate this call to its own parent, unless it was already dirty, in which case the grandparent must necessarily already be dirty as well. The parent can only transition back to "clean" after calling build() on all children.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-10-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-30 UTC."],[],[]] 
