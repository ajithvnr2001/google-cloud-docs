---
url: https://docs.cloud.google.com/datastream/docs/view-connection-profiles/
title: View connection profiles \u00a0|\u00a0 Datastream \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:50:55.318376+00:00
---

# View connection profiles  |  Datastream  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/view-connection-profiles/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Guides ](https://docs.cloud.google.com/datastream/docs/how-to)



Send feedback 

#  View connection profiles Stay organized with collections  Save and categorize content based on your preferences. 

In this page, you learn how to view high-level and detailed information about connection profiles.

To view information about a connection profile, do the following:

  1. Go to the **Connection profiles** page in the Google Cloud Console.

[Go to the Connection profiles page](https://console.cloud.google.com/datastream/connection-profiles)

  2. Click the connection profile for which you want to see detailed information. This information appears on the **Connection profile details** page.




## View high-level information

High-level information about a connection profile includes:

  * The name, ID, and type of the connection profile.
  * The password secret ID and version, if the profile authenticates with Secret Manager.
  * Whether the connection profile is assigned to streams.
  * How many streams are using the connection profile.
  * Details about how Datastream can connect to the profile.
  * When the connection profile was created or last updated.
  * The region where the connection profile is established.
  * Any labels added to the connection profile. 



## View detailed information

In addition to viewing high-level information about a connection profile, you can click a connection profile to see additional information, including:

  * The connectivity method that Datastream uses to connect to the source or destination.
  * The Datastream IP addresses for the region where the connection profile is stored. You can use these IP addresses to configure your source or destination database to allow incoming or outgoing connections for them.

**Note:** The IP addresses are shown only for public connectivity methods, such as IP allowlisting or forward-SSH tunnel.
  * For Cloud Storage connection profiles, a link that contains the name of your bucket and the folder of the bucket into which Datastream transfers schemas, tables, and data from the source database.

  * The streams that are using the connection profile.




## What's next

  * Learn how to [modify connection profiles](https://docs.cloud.google.com/datastream/docs/modify-connection-profiles).
  * Find out how to [delete connection profiles](https://docs.cloud.google.com/datastream/docs/delete-a-connection-profile).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
