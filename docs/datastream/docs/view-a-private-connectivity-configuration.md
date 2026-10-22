---
url: https://docs.cloud.google.com/datastream/docs/view-a-private-connectivity-configuration/
title: View a private connectivity configuration \u00a0|\u00a0 Datastream \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:42:00.917482+00:00
---

# View a private connectivity configuration  |  Datastream  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/view-a-private-connectivity-configuration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Guides ](https://docs.cloud.google.com/datastream/docs/how-to)



Send feedback 

#  View a private connectivity configuration Stay organized with collections  Save and categorize content based on your preferences. 

In this section, you learn how to view high-level and detailed information about a private connectivity configuration.

## View high-level information

High-level information about a private connectivity configuration includes:

  * The name of the private connectivity configuration.
  * The status of the configuration (`Active` or `Inactive`). If the status is `Active`, then the number of connection profiles to which the configuration is assigned appears.
  * When the configuration was created.
  * The region where the configuration is established.
  * The private connectivity method that was used: Private Service Connect interface or VPC peering.



## View detailed information

In addition to viewing high-level information about a private connectivity configuration, you can click a configuration to see additional information, including:

  * The ID of the private connectivity configuration.
  * Additional information about the connection profiles that use the private connectivity configuration. You assign the configuration to connection profiles when you [create the profiles](https://docs.cloud.google.com/datastream/docs/create-connection-profiles).
  * For VPC peering private connectivity configurations: 
    * A link to the VPC network.
    * The subnet on your VPC network that's assigned to this configuration.
  * For Private Service Connect interface private connectivity configurations: 
    * A link to the network attachment used.



To view a private connectivity configuration in the Google Cloud console, perform the following steps:

  1. Go to the **Private connectivity configurations** page in the Google Cloud Console.

[Go to the Private connectivity configurations page](https://console.cloud.google.com/datastream/private-connections)

  2. Click the configuration for which you want to see detailed information. This information appears on the **Private connectivity configuration details** page.




After viewing high-level and detailed information about a private connectivity configuration, you can use the configuration to [create a connection profile](https://docs.cloud.google.com/datastream/docs/create-connection-profiles).

## What's next

  * Learn about the [Private Service Connect interfaces](https://docs.cloud.google.com/datastream/docs/psc-interfaces) private connectivity method.
  * Learn about the [VPC peering](https://docs.cloud.google.com/datastream/docs/vpc-peering) private connectivity method.
  * Find out how to [delete a private connectivity configuration](https://docs.cloud.google.com/datastream/docs/delete-a-private-connectivity-configuration).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
