---
url: https://docs.cloud.google.com/datastream/docs/ip-allowlists/
title: IP allowlists \u00a0|\u00a0 Datastream \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:50:55.462649+00:00
---

# IP allowlists  |  Datastream  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/ip-allowlists/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Guides ](https://docs.cloud.google.com/datastream/docs/how-to)



Send feedback 

#  IP allowlists Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to use the IP allowlists connectivity method so that Datastream can transfer data from a source database to a destination.

Public IP connectivity is most appropriate when the source database is external to Google Cloud and has an externally accessible IPv4 address and TCP port.

## Set up IP allowlists

If your source database is external to Google Cloud, then add the Datastream public IP addresses as an inbound firewall rule on the source network:

  1. Open your source database machine's network firewall rules.

  2. Create an inbound rule.

  3. Set the IP address of the source database to Datastream's [IP addresses](https://docs.cloud.google.com/datastream/docs/ip-allowlists-and-regions).

  4. Set the protocol to `TCP`.

  5. Set the port associated with the `TCP` protocol. The default values are:

     * `1521` for an Oracle database
     * `3306`for a MySQL database
     * `5432`for a PostgreSQL database
     * `1433` for a SQL Server database
     * `27017` for a MongoDB database
  6. Save the firewall rule, and then exit.




## What's next

  * Learn how about other network [connectivity methods](https://docs.cloud.google.com/datastream/docs/network-connectivity-options).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
