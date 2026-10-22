---
url: https://docs.cloud.google.com/datastream/docs/configure-mongodb-atlas-psc/
title: Configure MongoDB Atlas using Private Service Connect interfaces \u00a0|\u00a0 Datastream \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:15.910287+00:00
---

# Configure MongoDB Atlas using Private Service Connect interfaces  |  Datastream  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/configure-mongodb-atlas-psc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Guides ](https://docs.cloud.google.com/datastream/docs/how-to)



Send feedback 

#  Configure MongoDB Atlas using Private Service Connect interfaces Stay organized with collections  Save and categorize content based on your preferences. 

You can stream change data capture (CDC) updates from a MongoDB Atlas database over a private network by using Private Service Connect interfaces in Datastream. To prepare your source, you create a MongoDB database user, set up private network connectivity between Datastream and MongoDB Atlas, and create a connection profile. This configuration doesn't provide high availability. If a MongoDB node fails the connection profile test, you must manually update the IP address in the Datastream connection profile.

## Configure a MongoDB database user

To use Datastream with a MongoDB Atlas instance, you first need to create a database user and grant them access privileges:

  1. In the [MongoDB Atlas dashboard](https://www.mongodb.com/products/platform/cloud), under **Security** , click **Database access**.
  2. Click **New database user** and select the password authentication method for your user.
  3. Enter the username and password for your Datastream user.
  4. Under **Database user privileges** , select **Grant specific user privileges**.
  5. Under **Specific privileges** , add the following role: 
     * `readAnyDatabase`
  6. Click **Add user**.



## Set up network configuration

Connect your Virtual Private Cloud networks across Datastream and MongoDB Atlas.

  1. Identify the central Virtual Private Cloud network in your Google Cloud project. Ensure that the IP address ranges of this network don't overlap with the IP address ranges of your Datastream or MongoDB Atlas networks.
  2. [Create a private connectivity configuration](https://docs.cloud.google.com/datastream/docs/psc-interfaces) to peer your Datastream network with your central Google Cloud Virtual Private Cloud network.
  3. Set up a network peering connection in MongoDB Atlas to peer your central Google Cloud Virtual Private Cloud network with your MongoDB Atlas network. Provide your project ID, the network name, subnet name, and endpoint name. For more information, see [Set up a private endpoint for a dedicated cluster](https://www.mongodb.com/docs/atlas/security-cluster-private-endpoint/) in MongoDB documentation.



## Create the connection profile

After you configure your network, create a Datastream connection profile.

  1. Go to the **Connection profiles** page in the Google Cloud Console.

[Go to the Connection profiles page](https://console.cloud.google.com/datastream/connection-profiles)

  2. Click **Create profile** and select **MongoDB**.

  3. In the **Hostname** field, enter the IP address of the endpoint in the **Connected endpoints** section from the **Private Service Connect** page in Google Cloud.

[Go to the Private Service Connect](https://console.cloud.google.com/net-services/psc)

  4. In the **Port** field, enter `27017`.

  5. Enter the username and password for your database user.

  6. Add the `tls` and `tls_allow_invalid_hostnames` labels and set their values to `true`. For more information about setting labels, see [Create a connection profile for a MongoDB database](https://docs.cloud.google.com/datastream/docs/create-connection-profiles#cp4mongodb).

  7. Select **Private connectivity** as your connectivity method.

  8. Select the private connectivity configuration that you created.

  9. Click **Create** to save the connection profile.

  10. Run a test to verify connection to your database.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
