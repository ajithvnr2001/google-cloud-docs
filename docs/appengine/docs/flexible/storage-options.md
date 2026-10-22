---
url: https://docs.cloud.google.com/appengine/docs/flexible/storage-options/
title: Understanding data and file storage \u00a0|\u00a0 App Engine flexible environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:44:33.734302+00:00
---

# Understanding data and file storage  |  App Engine flexible environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/flexible/storage-options/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Flexible environment ](https://docs.cloud.google.com/appengine/docs/flexible)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Understanding data and file storage Stay organized with collections  Save and categorize content based on your preferences. 

To store data and files on App Engine, you can use Google Cloud services or any other storage service that is supported by your language and is accessible from your App Engine instance. Third-party databases can be hosted on [Compute Engine](https://docs.cloud.google.com/compute), hosted on another cloud provider, hosted on premises, or managed by a third-party vendor.

## Google Cloud storage services

For App Engine apps running in the flexible environment, we recommend one of the following Google Cloud storage services:

  * [Firestore in Datastore mode](https://docs.cloud.google.com/appengine/docs/flexible/using-firestore-in-datastore-mode) to store data in a NoSQL database. Note that Firestore in Datastore mode is available for all runtimes except the .NET runtime. 
  * [Cloud SQL for MySQL](https://docs.cloud.google.com/sql/docs/mysql/connect-app-engine-flexible) to store data in a MySQL database.
  * [Cloud SQL for PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/connect-app-engine-flexible) to store data in a PostgreSQL database.
  * [Cloud Storage](https://docs.cloud.google.com/appengine/docs/flexible/using-cloud-storage) to read and write files in the runtime environment, as well as [store and serve static files](https://docs.cloud.google.com/appengine/docs/flexible/serving-static-files), such as movies or images or other static content.



See a complete list of the Google Cloud storage products on the [Cloud Storage Products page](https://cloud.google.com/products/storage/).

## Hosting on Compute Engine

App Engine instances are part of the same [private internal network](https://docs.cloud.google.com/vpc/docs/vpc#app-engine-comm) as Compute Engine instances. Your App Engine app can communicate with services hosted on Compute Engine within the same project without going through the public internet. In many cases, your app connects to the service using the instance's internal IP address without needing to assign the database an external, public IP address. If desired, you can assign a public IP address to allow the database to be accessed from outside of Google Cloud.

Many popular third-party databases such as Redis, MongoDB, PostgreSQL, Cassandra, Hadoop, and Microsoft SQL Server can be quickly deployed to Compute Engine by using the [Google Cloud Marketplace](https://docs.cloud.google.com/marketplace). See the following guides for details about deploying [MySQL](https://docs.cloud.google.com/solutions/setup-mysql) or [PostgreSQL](https://docs.cloud.google.com/solutions/setup-postgres). 

## Other cloud providers

App Engine apps can connect to external databases that are hosted on other public clouds as long as those database servers and your firewall are configured properly to accept connections. Your App Engine app connects over the Internet using that external service's public IP address.

## Databases managed by a third-party vendor

There are many vendors offering managed database services such as [mLab](https://docs.cloud.google.com/mongodb) for MongoDB, Redis Labs offers hosted [Redis caching](https://redislabs.com/redis-enterprise/cloud/). These vendors handle hosting, configuration, and maintenance of databases. App Engine can connect to these external services over the Internet, in the same way as other public clouds by using that service's public IP address.

## On premises

If you have existing on-premises databases that you want to make accessible to your App Engine app, you can either configure your internal network and firewall to give the database a public IP address or connect using a VPN.

Setting up [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn) allows your App Engine app to access your on-premises network without directly exposing the database server to the public internet. Because App Engine and Compute Engine use the same networking infrastructure, you can use the VPN connection to establish a connection between the App Engine app and your on-premises database using the database server's internal IP address.

## Production considerations

App Engine can be configured to automatically scale your application [horizontally](https://wikipedia.org/wiki/Scalability#Horizontal_and_vertical_scaling) based on various metrics. Unlike web applications, databases often require non-trivial changes to respond to scale. In production applications, App Engine can quickly overwhelm a database during traffic spikes. You should take the anticipated average traffic load and load during spikes into consideration when configuring and deploying databases.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
