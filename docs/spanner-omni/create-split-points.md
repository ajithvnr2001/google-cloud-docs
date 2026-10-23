---
url: https://docs.cloud.google.com/spanner-omni/create-split-points/
title: Create and manage Spanner Omni database split points \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:32:20.424722+00:00
---

# Create and manage Spanner Omni database split points  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner-omni/create-split-points/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner Omni ](https://docs.cloud.google.com/spanner-omni)
  * [ Guides ](https://docs.cloud.google.com/spanner-omni/overview)



Send feedback 

#  Create and manage Spanner Omni database split points Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to create and manage splits in your Spanner Omni database to prepare for increased traffic. This process is mostly identical to [creating and managing Spanner split points](https://docs.cloud.google.com/spanner/docs/create-manage-split-points), with the following distinctions:

  * To _add_ manual splits to your Spanner Omni database, use the following command:
        
        spanner databases splits add DATABASE_ID \
        --splits-file=FILE_PATH \
        [--split-expiration-time=DATE]
        

Replace the following:

    * DATABASE_ID: the database identifier—for example, `MY_DATABASE`.

    * FILE_PATH: the path to the file containing the [split point definitions](https://docs.cloud.google.com/spanner/docs/create-manage-split-points#gcloud)—for example, `/home/user/project/spanner/manual_splits.txt`.

    * DATE: optional, the date after which the splits expire. Accepts [timestamp values](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/data-types#timestamp_type) and relative time values—for example, `2072-09-27T12:30:00.45Z` or `now+7d`.

  * To _view_ the manual split points in your Spanner Omni database, use the following command:
        
        spanner sql \
        --database DATABASE_ID --execute \
        "SELECT * \
        FROM SPANNER_SYS.USER_SPLIT_POINTS"
        




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
