---
url: https://docs.cloud.google.com/datastream/docs/delete-a-private-connectivity-configuration/
title: Delete a private connectivity configuration \u00a0|\u00a0 Datastream \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:50:55.988044+00:00
---

# Delete a private connectivity configuration  |  Datastream  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/delete-a-private-connectivity-configuration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Guides ](https://docs.cloud.google.com/datastream/docs/how-to)



Send feedback 

#  Delete a private connectivity configuration Stay organized with collections  Save and categorize content based on your preferences. 

If you no longer need a private connectivity configuration, then delete it. 

If a private connectivity configuration is assigned to any connection profiles, then you can't delete the configuration. To delete it, you must first [delete each connection profile](https://docs.cloud.google.com/datastream/docs/delete-a-connection-profile) that's associated with the configuration. To see which connection profiles are using the private connectivity configuration, you can [view detailed information about the configuration](https://docs.cloud.google.com/datastream/docs/view-a-private-connectivity-configuration#view-detailed-information).

## Delete a configuration

  1. Go to the **Private connectivity configurations** page in the Google Cloud Console.

[Go to the Private connectivity configurations page](https://console.cloud.google.com/datastream/private-connections)

  2. Click the configuration that you want to delete.

  3. In the **Private connectivity configuration details** page, verify that the configuration isn't being used by any connection profiles. If it is, then [delete the profiles](https://docs.cloud.google.com/datastream/docs/delete-a-connection-profile).

  4. Click **DELETE**.

  5. In the dialog, click **DELETE**.

It takes a few minutes for your private connectivity configuration to be deleted. Background resources first need to be deleted before the configuration can be deleted.



## What's next

  * Learn about the [Private Service Connect interfaces](https://docs.cloud.google.com/datastream/docs/psc-interfaces) private connectivity method.
  * Learn about the [VPC peering](https://docs.cloud.google.com/datastream/docs/vpc-peering) private connectivity method.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
