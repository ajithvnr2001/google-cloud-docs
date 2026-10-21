---
url: https://docs.cloud.google.com/looker/docs/best-practices/connecting-a-ms-sql-named-instance/
title: Connecting an MS-SQL named instance \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:11:32.598295+00:00
---

# Connecting an MS-SQL named instance  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/best-practices/connecting-a-ms-sql-named-instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Best Practices ](https://docs.cloud.google.com/looker/docs/best-practices/home)



Send feedback 

#  Connecting an MS-SQL named instance Stay organized with collections  Save and categorize content based on your preferences. 

Microsoft SQL Server (MS-SQL) has a feature called [**named instances**](https://serverfault.com/a/80771). This feature lets you run multiple databases on the same host (or clustered hosts) with separate settings. Each database instance runs on its own port. However, when using MS-SQL–aware clients running on Windows, you can connect by name instead of by port number. For example, if your hostname is `dbserver` and your instance is named `proddb`, you would connect using the hostname `dbserver\proddb`. 

## How MS-SQL named instances connect

  1. Your client contacts the host, named on the default MS-SQL port (1433). 
  2. MS-SQL responds with the named instance's port. 
  3. The client then connects to that port. 



Looker will be unable to find the port number of a named instance in this way. Once Looker connects to a port, it expects to be able to run queries and will not connect with any other port. 

## How to connect an MS-SQL named instance with Looker

MS-SQL chooses a random port at startup. For Looker to connect to an MS-SQL named instance, you will need to find the port the named instance is running on:

  * The article [SQL Server — Finding TCP Port Number SQL Instance Is Listening On](http://sqlandme.com/2013/05/01/sql-server-finding-tcp-port-number-sql-instance-is-listening-on/) details the method for finding the port. Although the article is from 2012, the procedure is similar across the various versions of MS-SQL. 
  * Once you've found the port, you can enter the port name in the [`Host:Port`](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#host:port) field in Looker's database connection configuration. For example, if the port is `61499` and the host is named `dbserver`, the connection in Looker will look like this: 
        
        host: dbserver
          port: 61499

> _**NOTE:** The database hostname will **not** take the form `dbserver\proddb`, as it would if you were connecting by the instance name._

  * it is important to note that MS-SQL may choose a different port for the named instance whenever the server is rebooted. This could require MS-SQL to change firewall rules and reconfigure Looker to use the new port. To avoid ports changing, you can choose to assign a static port to your named instance; see [How to Assign a Static Port to a SQL Server Named Instance — and Avoid a Common Pitfall](https://www.heelpbook.net/2015/how-to-assign-static-port-to-a-sql-server-named-instance/) for details on the process.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
