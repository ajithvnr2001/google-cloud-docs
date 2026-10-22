---
url: https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/cache-ontap-volumes/prepopulate-flexcache-volume/
title: Prepopulate a FlexCache volume \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:17:26.452800+00:00
---

# Prepopulate a FlexCache volume  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/cache-ontap-volumes/prepopulate-flexcache-volume/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Prepopulate a FlexCache volume Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to prepopulate a [FlexCache volume](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/cache-ontap-volumes/overview#about_flexcache).

You can configure a job to prepopulate the cache, as mentioned in [Cache prepopulation](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/cache-ontap-volumes/overview#cache_prepopulation).

### Considerations

  * Prepopulation is supported only for existing FlexCache volumes.

  * An initiated prepopulation starts a one-time job. Once this job is completed, the subsequent changes made to the source aren't continuously prepopulated in the cache. To update the cache, you must either start a new prepopulation job or allow clients to fetch the outdated files by accessing the cache.




Use the following instructions to start a prepopulation job using the Google Cloud CLI or ONTAP-mode.

### gcloud

To start a prepopulation job:
    
    
    gcloud beta netapp volumes update VOLUME_NAME --location=LOCATION \
      --cache-pre-populate=path-list=PATH_LIST1#PATH_LIST2,exclude-path-list=EXCLUDE_PATH_LIST1#EXCLUDE_PATH_LIST2,recursion=RECURSION

Replace the following information:

  * `VOLUME_NAME`: the name of the volume. This name must be unique per location.

  * `LOCATION`: the location for the FlexCache volume.

  * `PATH_LIST`: Optional: a list of file or directory paths to prepopulate. Use # sign to separate multiple paths.

The following example shows you how to add multiple file or directory paths:
        
        path-list=PATH_LIST1#PATH_LIST2
        

  * `EXCLUDE_PATH_LIST`: Optional: a list of file or directory paths to exclude when prepopulating `PATH_LIST`. Use # sign to separate multiple paths.

The following example shows you how to exclude multiple file or directory paths:
        
        path-list=EXCLUDE_PATH_LIST1#EXCLUDE_PATH_LIST2
        

  * `RECURSION`: Optional: a boolean flag that indicates whether the folders specified in `PATH_LIST` and `EXCLUDE_PATH_LIST` should be included or excluded recursively. By default, this is set to `false`.




To check the status of a prepopulation job whether it's still running or completed, [look up the FlexCache volume](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/cache-ontap-volumes/manage-flexcache-volume#view_flexcache_volume_details) details. The `CachePrePopulateState` field within the `cacheParameters` output shows the current state.

### ONTAP-mode

For more information, see [Prepopulate ONTAP FlexCache volumes](https://docs.netapp.com/us-en/ontap/flexcache/prepopulate-volume-task.html) in the ONTAP documentation.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
