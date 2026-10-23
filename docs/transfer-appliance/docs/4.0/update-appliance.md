---
url: https://docs.cloud.google.com/transfer-appliance/docs/4.0/update-appliance/
title: Update appliance details \u00a0|\u00a0 Transfer Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:25.413685+00:00
---

# Update appliance details  |  Transfer Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/transfer-appliance/docs/4.0/update-appliance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Transfer Appliance ](https://docs.cloud.google.com/transfer-appliance/docs)
  * [ Guides ](https://docs.cloud.google.com/transfer-appliance/docs/4.0/procedure-guide)



Send feedback 

#  Update appliance details Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** If the edit button is missing or you are unable to edit any of the following details, contact the Transfer Appliance Team at [data-support@google.com](mailto:data-support@google.com) for assistance.

## Destination bucket for offline data transfer

**Note:** Offline transfer destination can be updated only before upload starts at Google.

  * Go to [appliances page](https://console.cloud.google.com/appliances) and navigate to a specific appliance by clicking its ID.
  * Find "Offline transfer destination in Cloud Storage" on the page which displays the current destination.
  * Click the edit button next to the current destination. When prompted, enter a new destination bucket name and click "Save".
  * [Clean up permissions](https://docs.cloud.google.com/transfer-appliance/docs/4.0/cleanup#revoke-bucket-service-account) granted on the previous destination bucket
  * [Grant permissions](https://docs.cloud.google.com/transfer-appliance/docs/4.0/procedure-guide#project-setup-and-key-download) on the new destination bucket by going through the `Authorize service accounts` step



## Destination bucket for online data transfer

**Note:** Online transfer destination can be updated only before order preparation starts at Google.

  * Go to [appliances page](https://console.cloud.google.com/appliances) and navigate to a specific appliance by clicking its ID.
  * Find "Online transfer destination in Cloud Storage" on the page which displays the current destination.
  * Click the edit button next to the current destination. When prompted, enter a new destination bucket name and click "Save".
  * [Clean up permissions](https://docs.cloud.google.com/transfer-appliance/docs/4.0/cleanup#revoke-bucket-service-account) granted on the previous destination bucket
  * [Grant permissions](https://docs.cloud.google.com/transfer-appliance/docs/4.0/procedure-guide#project-setup-and-key-download) on the new destination bucket by going through the `Authorize service accounts` step



## Display name

  * Go to [appliances page](https://console.cloud.google.com/appliances) and navigate to a specific appliance by clicking its ID.
  * Find "Display name" on the page which displays the current name.
  * Click the edit button next to the current display name. When prompted, enter a new display name and click "Save".



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
