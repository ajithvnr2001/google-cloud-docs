---
url: https://docs.cloud.google.com/datastream/docs/modify-connection-profiles/
title: Modify connection profiles \u00a0|\u00a0 Datastream \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:50:55.361629+00:00
---

# Modify connection profiles  |  Datastream  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/modify-connection-profiles/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Guides ](https://docs.cloud.google.com/datastream/docs/how-to)



Send feedback 

#  Modify connection profiles Stay organized with collections  Save and categorize content based on your preferences. 

After viewing high-level and detailed information about a connection profile, you can modify it.

## Modify a connection profile

  1. Go to the **Connection profiles** page in the Google Cloud Console.

[Go to the Connection profiles page](https://console.cloud.google.com/datastream/connection-profiles)

  2. Click the connection profile that you want to modify.

  3. On the **Connection profile details** page, click **EDIT**.

  4. Modify the connection settings, secret or password, encryption type, or connectivity method for the connection profile.

If you're modifying a connection profile to a source, then test your modifications to ensure that Datastream can communicate with the source.

When you do this, a dialog appears, prompting you for the secret or password of the account for the source. Datastream uses the username of the account that appears in the window and the secret or password that you supply to verify that Datastream can establish a connection to the source.

For more information about the connection settings, connectivity method, or account for the source connection profile, see [Create connection profiles](https://docs.cloud.google.com/datastream/docs/create-connection-profiles).

  5. After making your changes, click **SAVE**.




After creating and viewing high-level and detailed information about connection profiles for a source database and a destination, and making any necessary changes to the profiles, you can use them to [create a stream](https://docs.cloud.google.com/datastream/docs/create-a-stream).

## What's next

  * Learn how to [view connection profiles](https://docs.cloud.google.com/datastream/docs/view-connection-profiles).
  * Find out how to [delete connection profiles](https://docs.cloud.google.com/datastream/docs/delete-a-connection-profile).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
