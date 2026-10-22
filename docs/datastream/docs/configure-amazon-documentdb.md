---
url: https://docs.cloud.google.com/datastream/docs/configure-amazon-documentdb/
title: Configure an Amazon DocumentDB database for CDC \u00a0|\u00a0 Datastream \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:17.650887+00:00
---

# Configure an Amazon DocumentDB database for CDC  |  Datastream  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/configure-amazon-documentdb/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Guides ](https://docs.cloud.google.com/datastream/docs/how-to)



Send feedback 

#  Configure an Amazon DocumentDB database for CDC Stay organized with collections  Save and categorize content based on your preferences. 

Datastream lets you stream change data capture (CDC) updates from an Amazon DocumentDB (with MongoDB compatibility) database to a [supported destination](https://docs.cloud.google.com/datastream/docs/destinations), such as BigQuery or Cloud Storage. To prepare your cluster in an Amazon Virtual Private Cloud, you enable change streams, set up a bastion host SSH tunnel, and configure SSL/TLS encryption. Datastream doesn't support Amazon DocumentDB Elastic Clusters.

## Enable change streams

Datastream uses change streams to capture and replicate changes from your Amazon DocumentDB database.

To enable change streams for the specific databases or collections that you want to replicate, see [Enabling change streams](https://docs.aws.amazon.com/documentdb/latest/developerguide/change_streams.html#change_streams-enabling) in the Amazon DocumentDB documentation.

## Set up a bastion host for the SSH tunnel

To connect to your Amazon DocumentDB cluster from Datastream, set up a bastion host:

  1. In AWS, launch a lightweight Amazon Elastic Compute Cloud (EC2) instance to serve as a bastion host. Configure the security group of the instance to allow SSH connections (port 22) from Datastream.
  2. Allow network traffic from the Datastream public IP addresses for your region. To locate the regional IP addresses to allowlist, see [IP allowlists and regions](https://docs.cloud.google.com/datastream/docs/ip-allowlists-and-regions).

Alternatively, you can find the IP addresses to allowlist on the bastion host for your region when you create the MongoDB connection profile in the Google Cloud console:

     1. Go to the **Connection profiles** page in the Google Cloud Console.

[Go to the Connection profiles page](https://console.cloud.google.com/datastream/connection-profiles)

     1. Start creating a **MongoDB** connection profile.
     2. Expand the **Define connectivity method** section and locate the list of Datastream public IP addresses for your region.
  3. To authenticate the SSH tunnel session from Datastream, configure a user account on your EC2 instance with either a password or an SSH private key (recommended). If you use a private key, add the public key to the `~/.ssh/authorized_keys` file on your bastion host. For more information, see [Forward SSH tunnel](https://docs.cloud.google.com/datastream/docs/ssh-tunnel).




## Encrypt your connection using SSL/TLS

To establish a secure connection, Datastream requires a certificate authority (CA) certificate to verify the Amazon DocumentDB server.

  1. Download the CA certificate (`.pem` file) for your Amazon DocumentDB cluster from AWS. For more information, see the [Amazon DocumentDB documentation](https://docs.aws.amazon.com/documentdb/latest/developerguide/security.encryption.ssl.html). 
     1. When you create your connection profile in Datastream, in the **Secure your connection to your source** section, select **Server-only** as the encryption type.
  2. Upload or enter the `.pem` certificate in the **Source CA certificate** section.
  3. Complete the remaining steps to create your connection profile. For more information, see [Create connection profiles ](https://docs.cloud.google.com/datastream/docs/create-connection-profiles).



## What's next

  * Learn more about how Datastream works with [MongoDB sources](https://docs.cloud.google.com/datastream/docs/sources-mongodb).
  * Learn how to [create a connection profile](https://docs.cloud.google.com/datastream/docs/create-connection-profiles).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
