---
url: https://docs.cloud.google.com/bare-metal/docs/bms-rename-storage/
title: Rename a storage volume \u00a0|\u00a0 Bare Metal Solution \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:19:23.264242+00:00
---

# Rename a storage volume  |  Bare Metal Solution  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bare-metal/docs/bms-rename-storage/

The availability of Bare Metal Solution is transitioning to a specialized, allowlist-only model. If you are an existing customer, please contact your Google account team to explore the value of migrating to new [Oracle and Google Cloud strategic partnership offerings](https://docs.cloud.google.com/bare-metal/docs/explore-oracle-partnership-offerings). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Bare Metal ](https://docs.cloud.google.com/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/bare-metal/docs/bms-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Rename a storage volume

To rename a storage volume, follow these steps:

###  Console 

  1. In the Google Cloud console, go to the [**Compute Engine** > **Bare Metal Solution** > **Volumes**](https://console.cloud.google.com/compute/bareMetalSolution/volumes) page.
  2. Click the storage volume name.
  3. On the **Volume details** page, in the **Name** field, click edit**Edit name**.
  4. On the **Editing name** page, enter a new name.
  5. Click **Save**.
  6. To view your changes, refresh the page.



###  gcloud 

To rename a storage volume, use the `gcloud bms volumes rename` command.
    
    
    gcloud bms volumes rename VOLUME_NAME --new-name=NEW_NAME --project=PROJECT_ID --region=REGION
    

Replace the following:

  * VOLUME_NAME: Current name of the storage volume.
  * NEW_NAME: New name of the storage volume.
  * PROJECT_ID: Your project ID.
  * REGION: The location of the storage volume.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
