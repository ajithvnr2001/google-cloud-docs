---
url: https://docs.cloud.google.com/sql/docs/mysql/admin-tools/
title: Connect from other MySQL tools \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:50:14.478250+00:00
---

# Connect from other MySQL tools  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/admin-tools/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Connect from other MySQL tools Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | PostgreSQL | SQL Server

This page describes several common database administration and reporting tools that you can use to connect to your Cloud SQL instances. 

## Overview

Database administration and reporting tools provide varying degrees of support for managing your database. Select a tool based on the type of administration and reporting that you need to do. For example, if you need to connect to one database and issue a few SQL commands, consider using the MySQL client. See [Connecting MySQL Client Using IP Addresses](https://docs.cloud.google.com/sql/docs/mysql/connect-admin-ip). If you need to design or manage many databases simultaneously, then use one of the visual-based tools discussed here. 

We discuss a limited number of tools in this page. If your tool is not discussed, it's likely that you can successfully connect by following the steps for a similar tool. 

## Connect with MySQL Workbench

This section shows how to connect to your Cloud SQL instance database with [MySQL Workbench](http://www.mysql.com/products/workbench/). 

Note: Add your MySQL Workbench machine's IP address as an [authorized network](https://docs.cloud.google.com/sql/docs/mysql/authorize-networks) for your Cloud SQL instance.

  1. In the MySQL Workbench home view, click **New Connection**.
  2. In the **Setup new connection** form, provide a **Connection Name** , **Hostname** , **Username** , and **Default Schema** , if applicable, as show in Figure 1. 

![The Setup New Connection, Parameters in MySQL Workbench.](https://docs.cloud.google.com/static/sql/images/mysql-workbench-01.png)Figure 1: New connection in MySQL Workbench **Setup New Connection** form.

  3. Click **Test Connection**. You are prompted for a password. 
  4. Optionally, click **Advanced** , and fill in the information for connecting with SSL as shown in Figure 2. Be sure to select **Use SSL if available** and specify an **SSL CA File** , an **SSL CERT File** , and an **SSL key File**. [Learn more](https://docs.cloud.google.com/sql/docs/mysql/authorize-ssl) about using SSL certificates with Cloud SQL. 

![The Setup New Connection, Advanced in MySQL Workbench.](https://docs.cloud.google.com/static/sql/images/mysql-workbench-02.png)Figure 2: Specifying advanced options in the MySQL Workbench **Setup New Connection** form.

  5. Click **Test Connection** to make sure all the advanced parameters are set correctly. 
  6. Click **Close**. 
  7. Connect with the connection you created. 
  8. Once connected, you can test if you're using SSL by executing the following SQL statement: 
         
         SHOW STATUS like 'ssl_cipher';

![Testing if connection is over SSL.](https://docs.cloud.google.com/static/sql/images/mysql-workbench-03.png)Figure 3: Testing if the MySQL Workbench connection uses SSL.




Back to top

## Connect with Toad for MySQL

This section shows how to connect to your Cloud SQL instance database with [ Toad for MySQL](http://www.toadworld.com/products#mysql). 

  1. In Toad for MySQL, create a new connection.
  2. In the **New MySQL Connection** form, fill in the following information: 
     * **User** : The name of a user in your MySQL database.
     * **Password** : The password for the specified user. 
     * **Host** : The IP address of your instance. For more information, see [ Configuring Application Access Control](http://www.mysql.com/products/workbench/). If you've mapped the IP address to the hostname of your local server, you can use that in this field. 
     * **Database** : The database instance to connect to. 

![The Create New Connection dialog box in Toad for Mac.](https://docs.cloud.google.com/static/sql/images/toad-01.png)Figure 4: The Create New Connection dialog box in Toad for Mac

  3. Click **Test Connection** to confirm that the connection information is correct. 
  4. Click **OK** to start the connection. 
  5. In the **Enter Password** dialog box, enter the password for the user. This dialog box appears because we did not choose **Save password (encrypted)** in the **Create New Connection** dialog box. 



### Configure Toad to use SSL

In Figure 5, a **Create New Connection** dialog box is shown with information for connecting with SSL. All versions of Toad might not support connecting with SSL. 

![The Create New Connection dialog box in Toad for Windows.](https://docs.cloud.google.com/static/sql/images/toad-02.png)Figure 5: The Create New Connection dialog box in Toad for Windows

Once connected, you can test if you're using SSL by executing the following SQL statement and verifying that the `ssl_cipher` value is not empty: 
    
    
    SHOW STATUS like 'ssl_cipher';

Back to top

## Connect with SQuirrel SQL

This section shows how to connect to your Cloud SQL instance database with [SQuirrel SQL](http://www.squirrelsql.org/). 

  1. In the SQuirrel SQL client, select the **Aliases** panel to make it active. 
  2. In the **Aliases** menu, select **New Alias**. 
  3. Fill out the information, as shown in Figure 6. Be sure to select the MySQL Driver and provide values for <instance-ip>, <database>, and <user-name>. 

**Note:** The connection URL for using SSL is of the form: `jdbc:mysql://<instance-ip>:3306/<database>?verifyServerCertificate=true&useSSL=true&requireSSL=true`. However, to use SSL, you must specify truststore files created from the CA certificate, the client certificate, and the client key you obtained when you created an SSL certificate. For more information, see Configuring a SQuirrel SQL connection to use SSL.

![New alias in SQuirrel SQL.](https://docs.cloud.google.com/static/sql/images/squirrel-sql-01.png)Figure 6: Configuring a SQuirrel SQL connection to MySQL.

  4. Click **Test** to test the connection. You are prompted for a password. 
  5. Click **OK** to save the alias. 
  6. In the **Aliases** panel, right-click the alias you created and select **Connect**. 



### Configure SQuirrel SQL to use SSL

This section assumes that you've created an SSL certificate (see [Configuring SSL for an instance](https://docs.cloud.google.com/sql/docs/mysql/configure-ssl-instance)) and you have three files: 

  * A CA certificate file, for example, **ca-cert.pem**.
  * A client public key certificate file, for example, **client-cert.pem**.
  * A client private key file, for example, **client-key.pem**.



Use these files as described in [Connecting Securely Using SSL](http://dev.mysql.com/doc/connector-j/en/connector-j-reference-using-ssl.html) in the MySQL Reference Manual to create keystore and truststore files. You need to specify the keystore and truststore files when you start SQuirrel SQL. One way to do this is to edit the script that launches the SQuirrel SQL application as follows: 
    
    
    $JAVACMD -Djavax.net.ssl.keyStore=<path-to-keystore> \
             -Djavax.net.ssl.keyStorePassword=<keystore-password> \
             -Djavax.net.ssl.trustStore=<path-to-truststore> \
             -Djavax.net.ssl.trustStorePassword=<truststore-password> \
             [existing launch parameters]
    

After you've started SQuirrel SQL with the valid keystore and truststore information, you can connect with: 
    
    
    jdbc:mysql://<instance-ip>:3306/<database>?verifyServerCertificate=true&useSSL=true&requireSSL=true
    

Once connected, you can test if you're using SSL by executing the following SQL statement and verifying that the `ssl_cipher` value is not empty: 
    
    
    SHOW STATUS like 'ssl_cipher';

Back to top

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
