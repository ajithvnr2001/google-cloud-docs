---
url: https://docs.cloud.google.com/datastream/docs/create-connection-profiles/
title: Create connection profiles \u00a0|\u00a0 Datastream \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:34.355151+00:00
---

# Create connection profiles  |  Datastream  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/create-connection-profiles/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Guides ](https://docs.cloud.google.com/datastream/docs/how-to)



Send feedback 

#  Create connection profiles Stay organized with collections  Save and categorize content based on your preferences. 

Before you create a stream in Datastream, you configure connection profiles that store reusable authentication and network connectivity settings for resources in the same region.

You can create source connection profiles for Oracle, MySQL, PostgreSQL, SQL Server, MongoDB, Spanner, Salesforce, Salesforce Marketing Cloud, ServiceNow, Microsoft Dataverse, or Workday. For destinations, you can create connection profiles for BigQuery datasets or a Cloud Storage bucket.

## Before you begin

  * Make sure that you've set up your source database for replication. For information about steps required for each supported source type, see [Configure sources](https://docs.cloud.google.com/datastream/docs/sources).
  * Find out what steps might be required to set up your selected destination. For more information, see [Configure destinations](https://docs.cloud.google.com/datastream/docs/sources).



## Create a connection profile for Oracle database

  1. Go to the **Connection profiles** page in the Google Cloud Console.

[Go to the Connection profiles page](https://console.cloud.google.com/datastream/connection-profiles)

  2. Click **CREATE PROFILE**.

  3. In the **Create a connection profile** page, click the **Oracle** profile type.

  4. Use the following table to populate the fields of the **Define connection settings** section of the **Create Oracle profile** page:

Field| Description  
---|---  
Connection profile name| Enter the display name of the connection profile to the source Oracle database. This is used in the connection profile list as well as when an existing connection profile is selected in the creation of a stream.  
Connection profile ID| Datastream populates this field automatically based on the connection profile name that you enter. You can keep the ID that's auto-generated or change it.  
Region| Select the region where the connection profile is stored. Connection profiles, like all resources, are saved in a region, and a stream can only use connection profiles that are stored in the same region as the stream. Region selection doesn't impact whether Datastream can connect to the source or the destination, but can impact availability if the region experiences downtime.  
Hostname or IP| Enter a hostname or IP address that Datastream can use to connect to the source Oracle database.If you're using private connectivity to communicate with the source database, then specify the private (internal) IP address for the source database. If you're using a reverse proxy for private connectivity, then use the IP address of the proxy.For other connectivity methods, such as IP allowlisting, provide the public IP address.  
Port| Enter the port number that's reserved for the source database (The default port is typically **1521**.).  
Username| Enter the username of the account for the source database (for example, `ROOT`). This is the Datastream user that you created for the database.For more information about creating this user, see [Configure your source Oracle database](https://docs.cloud.google.com/datastream/docs/configure-your-source-oracle-database#configuresourcedatabase).  
Select Secret Manager password|  Select this option if you want to authenticate with a secret rather than enter the password manually. When select this option, two dropdowns appear: 
     * **Secret** : you can select a secret from the list (if available), enter it manually, or create a new secret:
To enter a secret manually: 
       1. Click **Enter secret manually**. The **Add a secret by resource ID** dialog appears.
       2. Copy and paste your secret resource identifier from Secret Manager. The secret resource ID can have the following format:
          * `projects/PROJECT_NUMBER/secrets/SECRET_NAME` (latest version)
          * `projects/PROJECT_NUMBER/secrets/SECRET_NAME/versions/VERSION_NUMBER` (specific version)
       3. Click the **Add secret** button.
To create a new secret: 
       1. Click **Create new secret**. The **Secret details** side panel opens.
       2. Under **Name** , enter a name for the secret (for example, `my-secret`). A secret name can contain uppercase and lowercase letters, numerals, hyphens, and underscores. The maximum allowed length for a name is 255 characters. The name that you create is added as part of the secret resource identifier.
       3. Optional: To also add a secret version when creating the initial secret, in the **Secret value** field, enter a value for the secret (for example, `abcd1234`). The secret value can be in any format but must not be larger than 64 KiB. You can also upload a text file containing the secret value using the **Upload file** option.
       4. Click the **Create secret** button.
     * **Secret version** : enter the version of the secret that you want to use:
       * When you provide the secret resource identifier, the **Use latest version** checkbox appears. You can select it to use the most up-to-date version of your secret resource.
       * Alternatively, you can expand the **Secret version** drop-down, and select the version from the list, if available.
       * If you want to use a different version of the secret, follow these steps:
         1. Click **Add new version**.
         2. In the **Secret value** field, enter a value for the secret. Alternatively, you can upload a file containing the secret value.
         3. Click the **Add new version** button.  
Enter password manually| Alternatively, you can enter the password of the account for the source database manually.  
System identifier (SID)| Enter the service that ensures that the source Oracle database is protected and monitored. For Oracle databases, the database service is typically **ORCL**. For pluggable databases, SID is the pluggable database name.  
Enable ASM access for binary reader| Select this checkbox, if you store your Oracle logs in Automatic Storage Management (ASM). This checkbox only applies to the binary log reader CDC method ([Preview](https://cloud.google.com/products/#product-launch-stages)). If you select it, you need to fill in the connection details for your ASM instance, including the ASM service name. The user account for the ASM connection must have the `SYSASM` privilege. For more information about the available CDC methods, see [Work with Oracle database redo log files](https://docs.cloud.google.com/datastream/docs/work-with-oracle-database-redo-log-files).  
  5. Optionally, use labels to organize your Datastream resources.

     1. To create a label, click **ADD LABEL** , and then enter the key-value pair for the label.
     2. To remove the label, click the **trashcan** icon to the right of the row that contains the label.
  6. In the **Define connection settings** section, click **CONTINUE**. The **Secure your connection to your source** page is active.

  7. From the **Encryption type** menu, select one of the following:

Encryption type| Description  
---|---  
None| Datastream connects to the source database without encryption.  
Server-only| When Datastream connects to the source database, Datastream authenticates the source, ensuring that it is connecting to the correct host securely. This prevents person-in-the-middle attacks. For server-only authentication, the source doesn't authenticate Datastream. To use server-only authentication, you must provide the x509 PEM-encoded certificate of the certificate authority (CA) that signed the source's certificate. Make sure you use a single certificate, Datastream doesn't support certificate chains.  
  8. In the **Secure your connection to your source** section, click **CONTINUE**. The **Define connectivity method** section of the **Create Oracle profile** page is active.

  9. From the **Connectivity method** drop-down menu, select a network connectivity method. This method defines how Datastream connects to the source database. Current network connectivity methods include:

     1. IP allowlisting: This method works by configuring the source database server to accept connections from Datastream. If you select this network connectivity method, then configure your source database to allow incoming connections from the Datastream public IP addresses for the region that you specified for the connection profile.
     2. Forward-SSH tunnel: This method establishes secure, encrypted connectivity between Datastream and the source database, using an SSH tunnel to either a tunnel server or to the database server. If you select this network connectivity method, then: 
        1. Enter the hostname or IP address, and port of the tunnel host server.
        2. Enter the username of the account for the tunnel host server.
        3. Select the authentication method for the SSH tunnel. If you select **Password** as the method, then enter the password of the account for the bastion host VM. If you select **Private/Public key pair** as the method, then provide a [private key](https://docs.cloud.google.com/datastream/docs/network-connectivity-options#sshkeys).
        4. Configure your tunnel host to allow incoming connections from the Datastream public IP addresses for the region that you specified for the connection profile.
     3. Private connectivity: this method lets you establish secure connectivity between Datastream and the source database, internally within Google Cloud, or with external sources connected over VPN or Interconnect. This communication happens through a Private Service Connect interface or a VPC peering connection.

If you select this network connectivity method, and you have created a private connectivity configuration, then select it from the list of configurations. This type of configuration contains information that Datastream uses to communicate with the source database over a private network.

If you haven't created a private connectivity configuration, create one by clicking **CREATE PRIVATE CONNECTIVITY CONFIGURATION** at the bottom of the drop-down list, and then perform the same steps as in [Create a private connectivity configuration](https://docs.cloud.google.com/datastream/docs/create-a-private-connectivity-configuration#create-the-configuration).

**Note:** You can use private connectivity to connect Datastream to any supported source. However, when you use VPC peering, transitive peering isn't supported. If the network that Datastream is peered with isn't the network where your source is hosted, you're using a fully managed database (for example, Cloud SQL), or if Datastream doesn't run in the region where your source exists, then a NAT VM is required.   
  
For more information, see [VPC peering](https://docs.cloud.google.com/datastream/docs/vpc-peering).
  10. In the **Define connectivity method** section, click **CONTINUE**. The **Test connection profile** section of the **Create Oracle profile** page is active.

  11. Click **RUN TEST** to verify that Datastream can communicate with the source.

If the test fails, then it indicates which part of the process had an issue. Refer to the [Diagnose issues](https://docs.cloud.google.com/datastream/docs/diagnose-issues) page for troubleshooting steps. Necessary changes can be made and then re-tested on the **Create Oracle profile** page.

Navigate to the part of the flow in question to correct the issue, and then retest.

**Note:** The connection profile can be created even if the test fails, but you should fix any issues associated with the connection profile before using the connection profile in a stream.
  12. Click **CREATE**.




## Create a connection profile for MySQL database

  1. Go to the **Connection profiles** page in the Google Cloud Console.

[Go to the Connection profiles page](https://console.cloud.google.com/datastream/connection-profiles)

  2. Click **CREATE PROFILE**.

  3. In the **Create a connection profile** page, click the **MySQL** profile type.

  4. Use the following table to populate the fields of the **Define connection settings** section of the **Create MySQL profile** page:

Field| Description  
---|---  
Connection profile name| Enter the display name of the connection profile to the source MySQL database. This is used in the connection profile list as well as when an existing connection profile is selected in the creation of a stream.  
Connection profile ID| Datastream populates this field automatically based on the connection profile name that you enter. You can keep the ID that's auto-generated or change it.  
Region| Select the region where the connection profile is stored. Connection profiles, like all resources, are saved in a region, and a stream can only use connection profiles that are stored in the same region as the stream. Region selection doesn't impact whether Datastream can connect to the source or the destination, but can impact availability if the region experiences downtime.  
Hostname or IP| Enter a hostname or IP address that Datastream can use to connect to the source MySQL database. If you're using private connectivity to communicate with the source database, then specify the private (internal) IP address for the source database. If you're using a reverse proxy for private connectivity, then use the IP address of the proxy.For other connectivity methods, such as IP allowlisting or Forward-SSH, provide the public IP address.  
Port| Enter the port number that's reserved for the source database (The default port is typically **3306**.).  
Username| Enter the username of the account for the source database (for example, `root`). This is the Datastream user that you created for the database.For more information about creating this user, see [Configure a source MySQL database](https://docs.cloud.google.com/datastream/docs/configure-your-source-mysql-database).  
Select Secret Manager password|  Select this option if you want to authenticate with a secret rather than enter the password manually. When select this option, two dropdowns appear: 
     * **Secret** : you can select a secret from the list (if available), enter it manually, or create a new secret:
To enter a secret manually: 
       1. Click **Enter secret manually**. The **Add a secret by resource ID** dialog appears.
       2. Copy and paste your secret resource identifier from Secret Manager. The secret resource ID can have the following format:
          * `projects/PROJECT_NUMBER/secrets/SECRET_NAME` (latest version)
          * `projects/PROJECT_NUMBER/secrets/SECRET_NAME/versions/VERSION_NUMBER` (specific version)
          * Click **Add secret**.
To create a new secret: 
       1. Click **Create new secret**. The **Secret details** side panel opens.
       2. Under **Name** , enter a name for the secret (for example, `my-secret`). A secret name can contain uppercase and lowercase letters, numerals, hyphens, and underscores. The maximum allowed length for a name is 255 characters. The name that you create is added as part of the secret resource identifier.
       3. Optional: To also add a secret version when creating the initial secret, in the **Secret value** field, enter a value for the secret (for example, `abcd1234`). The secret value can be in any format but must not be larger than 64 KiB. You can also upload a text file containing the secret value using the **Upload file** option.
       4. Click the **Create secret** button.
     * **Secret version** : enter the version of the secret that you want to use:
       * When you provide the secret resource identifier, the **Use latest version** checkbox appears. You can select it to use the most up-to-date version of your secret resource.
       * Alternatively, you can expand the **Secret version** drop-down, and select the version from the list, if available.
       * If you want to use a different version of the secret, follow these steps:
         1. Click **Add new version**.
         2. In the **Secret value** field, enter a value for the secret. Alternatively, you can upload a file containing the secret value.
       * Click the **Add new version** button.  
Enter password manually| Alternatively, you can enter the password of the account for the source database manually.  
  5. Optionally, use labels to organize your Datastream resources.

     1. To create a label, click **ADD LABEL** , and then enter the key-value pair for the label.
     2. To remove the label, click the **trashcan** icon to the right of the row that contains the label.
  6. In the **Define connection settings** section, click **CONTINUE**. The **Secure your connection to your source** page is active.

  7. From the **Encryption type** menu, select one of the following:

Encryption type| Description  
---|---  
None| Datastream connects to the source database without encryption.  
Server-only| When Datastream connects to the source database, Datastream authenticates the source, ensuring that it is connecting to the correct host securely. This prevents person-in-the-middle attacks. For server-only authentication, the source doesn't authenticate Datastream. To use server-only authentication, you must provide the x509 PEM-encoded certificate of the certificate authority (CA) that signed the source's certificate. Make sure you use a single certificate, Datastream doesn't support certificate chains. For more information about creating certificates and keys for your database server, see [Creating SSL and RSA Certificates and Keys](https://dev.mysql.com/doc/refman/5.7/en/creating-ssl-rsa-files.html).  
Server-client| When Datastream connects to the source, Datastream authenticates the source and the source authenticates Datastream. Server-client authentication provides the strongest security. However, if you don't want to provide the client certificate and private key when you create the connection profile, you can still use server-only authentication. To use server-client authentication, you must provide the following items when you create the source connection profile:
     * The certificate of the CA that signed the source database server's certificate (the CA certificate).
     * The certificate used by the instance to authenticate against the source database server (the client certificate).
     * The private key associated with the client certificate (the client key).
For more information about creating certificates and keys for your database server, see [Creating SSL and RSA Certificates and Keys](https://dev.mysql.com/doc/refman/5.7/en/creating-ssl-rsa-files.html).  
  8. In the **Secure your connection to your source** section, click **CONTINUE**. The **Define connectivity method** section of the **Create MySQL profile** page is active.

  9. From the **Connectivity method** drop-down menu, select a network connectivity method. This method defines how Datastream connects to the source database. Current network connectivity methods include:

     1. IP allowlisting: This method works by configuring the source database server to accept connections from Datastream. If you select this network connectivity method, then configure your source database to allow incoming connections from the Datastream public IP addresses for the region that you specified for the connection profile.
     2. Forward-SSH tunnel: This method establishes secure, encrypted connectivity between Datastream and the source database, using an SSH tunnel to either a tunnel server or to the database server. If you select this network connectivity method, then: 
        1. Enter the hostname or IP address, and port of the tunnel host server.
        2. Enter the username of the account for the tunnel host server.
        3. Select the authentication method for the SSH tunnel. If you select **Password** as the method, then enter the password of the account for the bastion host VM. If you select **Private/Public key pair** as the method, then provide a [private key](https://docs.cloud.google.com/datastream/docs/network-connectivity-options#sshkeys).
        4. Configure your tunnel host to allow incoming connections from the Datastream public IP addresses for the region that you specified for the connection profile.
     3. Private connectivity: this method lets you establish secure connectivity between Datastream and the source database, internally within Google Cloud, or with external sources connected over VPN or Interconnect. This communication happens through a Private Service Connect interface or a VPC peering connection.

If you select this network connectivity method, and you have created a private connectivity configuration, then select it from the list of configurations. This type of configuration contains information that Datastream uses to communicate with the source database over a private network.

If you haven't created a private connectivity configuration, create one by clicking **CREATE PRIVATE CONNECTIVITY CONFIGURATION** at the bottom of the drop-down list, and then perform the same steps as in [Create a private connectivity configuration](https://docs.cloud.google.com/datastream/docs/create-a-private-connectivity-configuration#create-the-configuration).

**Note:** You can use private connectivity to connect Datastream to any supported source. However, when you use VPC peering, transitive peering isn't supported. If the network that Datastream is peered with isn't the network where your source is hosted, you're using a fully managed database (for example, Cloud SQL), or if Datastream doesn't run in the region where your source exists, then a NAT VM is required.   
  
For more information, see [VPC peering](https://docs.cloud.google.com/datastream/docs/vpc-peering).
  10. In the **Define connectivity method** section, click **CONTINUE**. The **Test connection profile** section of the **Create MySQL profile** page is active.

  11. Click **RUN TEST** to verify that Datastream can communicate with the source.

If the test fails, then it indicates which part of the process had an issue. Refer to the [Diagnose issues](https://docs.cloud.google.com/datastream/docs/diagnose-issues) page for troubleshooting steps. You can make the necessary changes and then re-test the connection profile.

Navigate to the part of the flow in question to correct the issue, and then retest.

**Note:** The connection profile can be created even if the test fails, but you should fix any issues associated with the connection profile before using the connection profile in a stream.
  12. Click **CREATE**.




## Create a connection profile for PostgreSQL database

  1. Go to the **Connection profiles** page in the Google Cloud Console.

[Go to the Connection profiles page](https://console.cloud.google.com/datastream/connection-profiles)

  2. Click **CREATE PROFILE**.

  3. In the **Create a connection profile** page, click the **PostgreSQL** profile type.

  4. Use the following table to populate the fields of the **Define connection settings** section of the **Create PostgreSQL profile** page:

Field| Description  
---|---  
Connection profile name| Enter the display name of the connection profile to the source PostgreSQL database. This is used in the connection profile list as well as when an existing connection profile is selected in the creation of a stream.  
Connection profile ID| Datastream populates this field automatically based on the connection profile name that you enter. You can keep the ID that's auto-generated or change it.  
Region| Select the region where the connection profile is stored. Connection profiles, like all resources, are saved in a region, and a stream can only use connection profiles that are stored in the same region as the stream. Region selection doesn't impact whether Datastream can connect to the source or the destination, but can impact availability if the region experiences downtime.  
Hostname or IP| Enter a hostname or IP address that Datastream can use to connect to the source PostgreSQL database. If you're using private connectivity to communicate with the source database, then specify the private (internal) IP address for the source database. If you're using a reverse proxy for private connectivity, then use the IP address of the proxy.For other connectivity methods, such as IP allowlisting or Forward-SSH, provide the public IP address.  
Port| Enter the port number that's reserved for the source database (The default port for PostgreSQL is typically **5432**.).  
Username| Enter the username of the account for the source database (for example, `root`). This is the Datastream user that you created for the database.For more information about creating this user, see [Configure your source PostgreSQL database](https://docs.cloud.google.com/datastream/docs/configure-your-source-postgresql-database).  
Select Secret Manager password|  Select this option if you want to authenticate with a secret rather than enter the password manually. When select this option, two dropdowns appear: 
     * **Secret** : you can select a secret from the list (if available), enter it manually, or create a new secret:
To enter a secret manually: 
       1. Click **Enter secret manually**. The **Add a secret by resource ID** dialog appears.
       2. Copy and paste your secret resource identifier from Secret Manager. The secret resource ID can have the following format:
          * `projects/PROJECT_NUMBER/secrets/SECRET_NAME` (latest version)
          * `projects/PROJECT_NUMBER/secrets/SECRET_NAME/versions/VERSION_NUMBER` (specific version)
       3. Click the **Add secret** button.
To create a new secret: 
       1. Click **Create new secret**. The **Secret details** side panel opens.
       2. Under **Name** , enter a name for the secret (for example, `my-secret`). A secret name can contain uppercase and lowercase letters, numerals, hyphens, and underscores. The maximum allowed length for a name is 255 characters. The name that you create is added as part of the secret resource identifier.
       3. Optional: To also add a secret version when creating the initial secret, in the **Secret value** field, enter a value for the secret (for example, `abcd1234`). The secret value can be in any format but must not be larger than 64 KiB. You can also upload a text file containing the secret value using the **Upload file** option.
       4. Click the **Create secret** button.
     * **Secret version** : enter the version of the secret that you want to use:
       * When you provide the secret resource identifier, the **Use latest version** checkbox appears. You can select it to use the most up-to-date version of your secret resource.
       * Alternatively, you can expand the **Secret version** drop-down, and select the version from the list, if available.
       * If you want to use a different version of the secret, follow these steps:
         1. Click **Add new version**.
         2. In the **Secret value** field, enter a value for the secret. Alternatively, you can upload a file containing the secret value.
         3. Click the **Add new version** button.  
Enter password manually| Alternatively, you can enter the password of the account for the source database manually.  
Database| Enter the name that identifies the database instance. For PostgreSQL databases, this is typically `postgres`.  
  5. Optionally, use labels to organize your Datastream resources.

     1. To create a label, click **ADD LABEL** , and then enter the key-value pair for the label.
     2. To remove the label, click the **trashcan** icon to the right of the row that contains the label.
  6. Click **CONTINUE**. The **Secure your connection to your source** page is active.

  7. From the **Encryption type** menu, select one of the following:

Encryption type| Description  
---|---  
None| Datastream connects to the source database without encryption.  
Server-only| When Datastream connects to the source database, Datastream authenticates the source, ensuring that it is connecting to the correct host securely. This prevents person-in-the-middle attacks. For server-only authentication, the source doesn't authenticate Datastream. To use server-only authentication, you must provide the x509 PEM-encoded certificate of the certificate authority (CA) that signed the source's certificate. Make sure you use a single certificate, Datastream doesn't support certificate chains.  
Server-client| When Datastream connects to the source, Datastream authenticates the source and the source authenticates Datastream. Server-client authentication provides the strongest security. However, if you don't want to provide the client certificate and private key when you create the connection profile, you can still use server-only authentication. To use server-client authentication, you must provide the following items when you create the source connection profile:
     * The certificate of the CA that signed the source database server's certificate (the CA certificate).
     * The certificate used by the instance to authenticate against the source database server (the client certificate).
     * The private key associated with the client certificate (the client key).  
  8. Click **CONTINUE**. The **Define connectivity method** section of the **Create PostgreSQL profile** page is active.

  9. From the **Connectivity method** drop-down menu, select a network connectivity method. This method defines how Datastream connects to the source database. Current network connectivity methods include:

     1. IP allowlisting: this method works by configuring the source database server to accept connections from Datastream. If you select this network connectivity method, then configure your source database to allow incoming connections from the Datastream public IP addresses for the region that you specified for the connection profile.
     2. Forward-SSH tunnel: this method establishes secure, encrypted connectivity between Datastream and the source database, using an SSH tunnel to either a tunnel server or to the database server. If you select this network connectivity method, then: 
        1. Enter the hostname or IP address, and port of the tunnel host server.
        2. Enter the username of the account for the tunnel host server.
        3. Select the authentication method for the SSH tunnel. If you select **Password** as the method, then enter the password of the account for the bastion host VM. If you select **Private/Public key pair** as the method, then provide a [private key](https://docs.cloud.google.com/datastream/docs/network-connectivity-options#sshkeys).
        4. Configure your tunnel host to allow incoming connections from the Datastream public IP addresses for the region that you specified for the connection profile.
     3. Private connectivity: this method lets you establish secure connectivity between Datastream and the source database, internally within Google Cloud, or with external sources connected over VPN or Interconnect. This communication happens through a Private Service Connect interface or a VPC peering connection.

If you select this network connectivity method, and you have created a private connectivity configuration, then select it from the list of configurations. This type of configuration contains information that Datastream uses to communicate with the source database over a private network.

If you haven't created a private connectivity configuration, create one by clicking **CREATE PRIVATE CONNECTIVITY CONFIGURATION** at the bottom of the drop-down list, and then perform the same steps as in [Create a private connectivity configuration](https://docs.cloud.google.com/datastream/docs/create-a-private-connectivity-configuration#create-the-configuration).

**Note:** You can use private connectivity to connect Datastream to any supported source. However, when you use VPC peering, transitive peering isn't supported. If the network that Datastream is peered with isn't the network where your source is hosted, you're using a fully managed database (for example, Cloud SQL), or if Datastream doesn't run in the region where your source exists, then a NAT VM is required.   
  
For more information, see [VPC peering](https://docs.cloud.google.com/datastream/docs/vpc-peering).
  10. In the **Define connectivity method** section, click **CONTINUE**. The **Test connection profile** section of the **Create PostgreSQL profile** page is active.

  11. Click **RUN TEST** to verify that Datastream can communicate with the source.

If the test fails, then it indicates which part of the process had an issue. Refer to the [Diagnose issues](https://docs.cloud.google.com/datastream/docs/diagnose-issues) page for troubleshooting steps. You can make the necessary changes and then re-test the connection profile.

Navigate to the part of the flow in question to correct the issue, and then retest.

**Note:** The connection profile can be created even if the test fails, but you should fix any issues associated with the connection profile before using the connection profile in a stream.
  12. Click **CREATE**.




## Create a connection profile for SQL Server database

  1. Go to the **Connection profiles** page in the Google Cloud Console.

[Go to the Connection profiles page](https://console.cloud.google.com/datastream/connection-profiles)

  2. Click **CREATE PROFILE**.

  3. In the **Create a connection profile** page, click the **SQL Server** profile type.

  4. Use the following table to populate the fields of the **Define connection settings** section of the **Create SQL Server profile** page:

Field| Description  
---|---  
Connection profile name| Enter the display name of the connection profile to the source SQL Server database. This is used in the connection profile list as well as when an existing connection profile is selected in the creation of a stream.  
Connection profile ID| Datastream populates this field automatically based on the connection profile name that you enter. You can keep the ID that's auto-generated or change it.  
Region| Select the region where the connection profile is stored. Connection profiles, like all resources, are saved in a region, and a stream can only use connection profiles that are stored in the same region as the stream. Region selection doesn't impact whether Datastream can connect to the source or the destination, but can impact availability if the region experiences downtime.  
Hostname or IP| Enter a hostname or IP address that Datastream can use to connect to the source SQL Server database. If you're using private connectivity to communicate with the source database, then specify the private (internal) IP address for the source database. For IP allowlisting, provide the public IP address. If you're using a reverse proxy for private connectivity, then use the IP address of the proxy.  
Port| Enter the port number that's reserved for the source database (The default port is typically **1433**.).  
Username| Enter the username of the account for the source database (for example, `root`). This is the Datastream user that you created for the database. For Azure SQL databases, you might need to enter the full username, along with the domain name.For more information about creating this user, see [Configure your source SQL Server database](https://docs.cloud.google.com/datastream/docs/configure-your-source-sql-server-database).  
Select Secret Manager password|  Select this option if you want to authenticate with a secret rather than enter the password manually. When select this option, two dropdowns appear: 
     * **Secret** : you can select a secret from the list (if available), enter it manually, or create a new secret:
To enter a secret manually: 
       1. Click **Enter secret manually**. The **Add a secret by resource ID** dialog appears.
       2. Copy and paste your secret resource identifier from Secret Manager. The secret resource ID can have the following format:
          * `projects/PROJECT_NUMBER/secrets/SECRET_NAME` (latest version)
          * `projects/PROJECT_NUMBER/secrets/SECRET_NAME/versions/VERSION_NUMBER` (specific version)
       3. Click the **Add secret** button.
To create a new secret: 
       1. Click **Create new secret**. The **Secret details** side panel opens.
       2. Under **Name** , enter a name for the secret (for example, `my-secret`). A secret name can contain uppercase and lowercase letters, numerals, hyphens, and underscores. The maximum allowed length for a name is 255 characters. The name that you create is added as part of the secret resource identifier.
       3. Optional: To also add a secret version when creating the initial secret, in the **Secret value** field, enter a value for the secret (for example, `abcd1234`). The secret value can be in any format but must not be larger than 64 KiB. You can also upload a text file containing the secret value using the **Upload file** option.
       4. Click the **Create secret** button.
     * **Secret version** : enter the version of the secret that you want to use:
       * When you provide the secret resource identifier, the **Use latest version** checkbox appears. You can select it to use the most up-to-date version of your secret resource.
       * Alternatively, you can expand the **Secret version** drop-down, and select the version from the list, if available.
       * If you want to use a different version of the secret, follow these steps:
         1. Click **Add new version**.
         2. In the **Secret value** field, enter a value for the secret. Alternatively, you can upload a file containing the secret value.
         3. Click the **Add new version** button.  
Enter password manually| Alternatively, you can enter the password of the account for the source database manually.  
Database| Enter the name that identifies the database instance.  
  5. Optionally, use labels to organize your Datastream resources.

     1. To create a label, click **ADD LABEL** , and then enter the key-value pair for the label.
     2. To remove the label, click the **trashcan** icon to the right of the row that contains the label.
  6. Click **Continue**.

  7. In the **Define connectivity method** section, from the **Connectivity method** drop-down menu, select a network connectivity method. This method defines how Datastream connects to the source database. Network connectivity methods include:

     1. **IP allowlisting** : This method works by configuring the source database server to accept connections from Datastream. If you select this network connectivity method, then configure your source database to allow incoming connections from the Datastream public IP addresses for the region that you specified for the connection profile.
     2. **Forward-SSH tunnel** : This method creates a secure, encrypted connection between the source database and Datastream. To set up this connectivity method, you need an SSH server that has access to the source database. If you select this network connectivity method, then: 
        1. Enter the hostname or IP address, and the port of the tunnel host server.
        2. Enter the username of the account for the tunnel host server.
        3. Select the authentication method for the SSH tunnel. If you select **Private/Public key pair** as the method, then provide a [private key](https://docs.cloud.google.com/datastream/docs/network-connectivity-options#generate_private_and_public_keys). If you select **Password** as the method, then enter the password of the account for the bastion host VM.
        4. You might also need to allowlist the Datastream external IP addresses on the SSH tunnel server.
     3. Private connectivity: this method lets you establish secure connectivity between Datastream and the source database, internally within Google Cloud, or with external sources connected over VPN or Interconnect. This communication happens through a Private Service Connect interface or a VPC peering connection.

If you select this network connectivity method, and you have created a private connectivity configuration, then select it from the list of configurations. This type of configuration contains information that Datastream uses to communicate with the source database over a private network.

If you haven't created a private connectivity configuration, create one by clicking **CREATE PRIVATE CONNECTIVITY CONFIGURATION** at the bottom of the drop-down list, and then perform the same steps as in [Create a private connectivity configuration](https://docs.cloud.google.com/datastream/docs/create-a-private-connectivity-configuration#create-the-configuration).

**Note:** You can use private connectivity to connect Datastream to any supported source. However, when you use VPC peering, transitive peering isn't supported. If the network that Datastream is peered with isn't the network where your source is hosted, you're using a fully managed database (for example, Cloud SQL), or if Datastream doesn't run in the region where your source exists, then a NAT VM is required.   
  
For more information, see [VPC peering](https://docs.cloud.google.com/datastream/docs/vpc-peering).
  8. Click **CONTINUE**. The **Test connection profile** section of the **Create SQL Server profile** page is active.

  9. Click **RUN TEST** to verify that Datastream can communicate with the source.

If the test fails, then it indicates which part of the process had an issue. Refer to the [Diagnose issues](https://docs.cloud.google.com/datastream/docs/diagnose-issues#sqlserver-errors) page for troubleshooting steps. You can make the necessary changes and then re-test the connection profile.

Navigate to the part of the flow in question to correct the issue, and then retest.

**Note:** The connection profile can be created even if the test fails, but you should fix any issues associated with the connection profile before using the connection profile in a stream.
  10. Click **CREATE**.




## Create a connection profile for a Salesforce org

  1. Go to the **Connection profiles** page in the Google Cloud Console.

[Go to the Connection profiles page](https://console.cloud.google.com/datastream/connection-profiles)

  2. Click **CREATE PROFILE**.

  3. In the **Create a connection profile** page, click the **Salesforce** profile type.

  4. Use the following table to populate the fields of the **Define connection settings** section of the **Create Salesforce profile** page:

Field| Description  
---|---  
Connection profile name| Enter the display name of the connection profile to the source Salesforce org. This is used in the connection profile list as well as when an existing connection profile is selected in the creation of a stream.  
Connection profile ID| Datastream populates this field automatically based on the connection profile name that you enter. You can keep the ID that's auto-generated or change it.  
Region| Select the region where the connection profile is stored. Connection profiles, like all resources, are saved in a region, and a stream can only use connection profiles that are stored in the same region as the stream. Region selection doesn't impact whether Datastream can connect to the source or the destination, but can impact availability if the region experiences downtime.  
  5. In the **Connection details** section, enter the URL address for your Salesforce domain. You can find your domain URL by going to Salesforce and clicking **Setup > Company settings > My domain**. The URL is under **My domain details**. It usually has the following format: `domain-name.my.salesforce.com`.

  6. Under **Authentication method** , select your authentication method:

     * **OAuth 2.0 client credentials authentication** : if you select this option, you need to indicate your client identifier and the client secret. For the client secret, you can either provide the secret resource ID and version from [Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview), for example `projects/my-project/locations/us-central1/secrets/salesforce-secret/versions/1`, or enter the raw value of the secret.

For more information about how to get the client ID and client secret, see [Configure a source Salesforce org](https://docs.cloud.google.com/datastream/docs/configure-salesforce-org#create-connected-app).

     * **Username/password authentication** : if you select this option, you need to enter your Salesforce account username and your password.

       * For the username, enter the name that you use to sign in to Salesforce. If you're already signed in to your Salesforce org, you can find your username by opening your account settings page and clicking **Personal information**. The name is under **Username**.
       * For the password, you can either provide the secret resource ID and version from [Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview), for example `projects/my-project/locations/us-central1/secrets/salesforce-secret/versions/1`, or provide the raw value of your password.

In the **Security token** section, provide your token secret resource ID and version from [Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview), for example `projects/my-project/locations/us-central1/secrets/salesforce-secret/versions/1` or enter the raw value of the security token, for example `C08120F510542FFB1C3640F57AF19E2D5D700556A25F7D665C3B428407709D8C`.

  7. Optionally, use labels to organize your Datastream resources.

     1. To create a label, click **ADD LABEL** , and then enter the key-value pair for the label.
     2. To remove the label, click the **trashcan** icon to the right of the row that contains the label.
  8. Click **Continue**.

  9. In the **Review connectivity method** section, review the Datastream regional IP addresses listed, and make sure that you configured your Salesforce org to accept incoming connections from these addresses. For more information about how to configure your Salesforce instance, see [Configure a Salesforce org](https://docs.cloud.google.com/datastream/docs/configure-salesforce-org).

  10. Click **CONTINUE**. The **Test connection profile** section of the **Create Salesforce profile** page is active.

  11. Click **RUN TEST** to verify that Datastream can communicate with the source.

If the test fails, then it indicates which part of the process had an issue. Refer to the [Diagnose issues](https://docs.cloud.google.com/datastream/docs/diagnose-issues#salesforce-errors) page for troubleshooting steps. You can make the necessary changes and then re-test the connection profile.

Navigate to the part of the flow in question to correct the issue, and then retest.

**Note:** The connection profile can be created even if the test fails, but you should fix any issues associated with the connection profile before using the connection profile in a stream.
  12. Click **CREATE**.




## Create a connection profile for a Dataverse environment

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

  1. Go to the **Connection profiles** page in the Google Cloud Console.

[Go to the Connection profiles page](https://console.cloud.google.com/datastream/connection-profiles)

  2. Click **Create profile**.

  3. In the **Create a connection profile** page, click the **Dataverse** profile type.

  4. Use the following table to populate the fields of the **Define connection settings** section of the **Create Dataverse profile** page:

Field| Description  
---|---  
Connection profile name| Enter the display name of the connection profile to the source Dataverse. This is used in the connection profile list as well as when an existing connection profile is selected in the creation of a stream.  
Connection profile ID| Datastream populates this field automatically based on the connection profile name that you enter. You can keep the ID that's auto-generated or change it.  
Region| Select the region where the connection profile is stored. Connection profiles, like all resources, are saved in a region, and a stream can only use connection profiles that are stored in the same region as the stream. Region selection doesn't impact whether Datastream can connect to the source or the destination, but can impact availability if the region experiences downtime.  
Environment URL| Enter the URL for your Dataverse environment, for example, `myorg.crm4.dynamics.com`.  
Tenant ID| Enter the Azure Active Directory tenant identifier associated with your Dataverse environment. This identifies the Azure AD instance used for authentication.  
Client ID| Enter the application client identifier of the Azure AD application registered for connecting to Dataverse. This application must be configured with the necessary API permissions.  
Client secret| Enter the secret key or value generated for the Azure AD application. This secret is used, along with the client ID, to authenticate the application and establish the connection.  
  5. In the **Define connectivity method** section, click **Continue**. The **Test connection profile** section of the **Create Dataverse profile** page is active.

  6. Click **Run test** to verify that Datastream can communicate with the source.

If the test fails, then it indicates which part of the process had an issue. Refer to the [Diagnose issues](https://docs.cloud.google.com/datastream/docs/diagnose-issues) page for troubleshooting steps. Necessary changes can be made and then re-tested on the **Create Dataverse profile** page.

Navigate to the part of the flow in question to correct the issue, and then retest.

**Note:** The connection profile can be created even if the test fails, but you should fix any issues associated with the connection profile before using the connection profile in a stream.
  7. Click **CREATE**.




## Create a connection profile for a Salesforce Marketing Cloud instance

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

  1. Go to the **Connection profiles** page in the Google Cloud Console.

[Go to the Connection profiles page](https://console.cloud.google.com/datastream/connection-profiles)

  2. Click **Create profile**.

  3. In the **Create a connection profile** page, click the **Salesforce Marketing Cloud** profile type.

  4. Use the following table to populate the fields of the **Define connection settings** section of the **Create Salesforce Marketing Cloud profile** page:

Field| Description  
---|---  
Connection profile name| Enter the display name of the connection profile to the source Salesforce Marketing Cloud instance. This is used in the connection profile list as well as when an existing connection profile is selected in the creation of a stream.  
Connection profile ID| Datastream populates this field automatically based on the connection profile name that you enter. You can keep the ID that's auto-generated or change it.  
Region| Select the region where the connection profile is stored. Connection profiles, like all resources, are saved in a region, and a stream can only use connection profiles that are stored in the same region as the stream. Region selection doesn't impact whether Datastream can connect to the source or the destination, but can impact availability if the region experiences downtime.  
Subdomain| Enter the subdomain for your Salesforce Marketing Cloud instance. For more information about how to get the subdomain name, see [Configure a Salesforce Marketing Cloud instance](https://docs.cloud.google.com/datastream/docs/configure-salesforce-marketing-cloud#configure-sfmc).  
Client ID| Enter the client ID for your Salesforce Marketing Cloud instance. For more information about how to get the client identifier, see [Configure a Salesforce Marketing Cloud instance](https://docs.cloud.google.com/datastream/docs/configure-salesforce-marketing-cloud#configure-sfmc).  
Client secret| Either provide the secret resource ID and version from [Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview), or enter the raw value of the client secret from your Salesforce Marketing Cloud instance.  
  5. Optionally, use labels to organize your Datastream resources.

     1. To create a label, click **ADD LABEL** , and then enter the key-value pair for the label.
     2. To remove the label, click the **trashcan** icon to the right of the row that contains the label.
  6. Click **CONTINUE**. The **Test connection profile** section of the **Create Salesforce Marketing Cloud profile** page is active.

  7. Click **RUN TEST** to verify that Datastream can communicate with the source.

If the test fails, then it indicates which part of the process had an issue. Refer to the [Diagnose issues](https://docs.cloud.google.com/datastream/docs/diagnose-issues) page for troubleshooting steps. You can make the necessary changes and then re-test the connection profile.

Navigate to the part of the flow in question to correct the issue, and then retest.

**Note:** The connection profile can be created even if the test fails, but you should fix any issues associated with the connection profile before using the connection profile in a stream.
  8. Click **CREATE**.




## Create a connection profile for a ServiceNow instance

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

  1. Go to the **Connection profiles** page in the Google Cloud Console.

[Go to the Connection profiles page](https://console.cloud.google.com/datastream/connection-profiles)

  2. Click **CREATE PROFILE**.

  3. In the **Create a connection profile** page, click the **ServiceNow** profile type.

  4. Use the following table to populate the fields of the **Define connection settings** section of the **Create ServiceNow profile** page:

Field | Description  
---|---  
Connection profile name | Enter the display name of the connection profile to the source ServiceNow instance. Datastream uses this in the connection profile list and when you select an existing connection profile while creating a stream.  
Connection profile ID | Datastream populates this field automatically based on the connection profile name that you enter. You can keep the ID that's auto-generated or change it.  
Region | Select the region where you want to store the connection profile. You save connection profiles, like all resources, in a region, and a stream can only use connection profiles that reside in the same region as the stream.  
Instance | Enter the URL address for your ServiceNow instance. It usually has the following format: `company.service-now.com`.  
Login method | Select your authentication method: 
     * **Connected app credentials** : if you select this option, you need to fill in the **Client ID** field and the **Client secret** section. For the client secret, you can either provide the secret resource ID and version from [Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview), or enter the raw value of the secret.
     * **User credentials** : if you select this option, you need to enter your ServiceNow account username and your password. For the password, you can either provide the secret resource ID and version from [Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview), or provide the raw value of the password that you created when you configured your integration user in ServiceNow. For more information, see [Configure an integration user](https://docs.cloud.google.com/datastream/docs/configure-servicenow#configure-user).  
  5. Optionally, use labels to organize your Datastream resources.

     1. To create a label, click **ADD LABEL** , and then enter the key-value pair for the label.
     2. To remove the label, click the **trashcan** icon to the right of the row that contains the label.
  6. Click **CONTINUE**.

  7. In the **Review connectivity method** section, review the Datastream regional IP addresses listed, and make sure that you configured your ServiceNow instance to accept incoming connections from these addresses. For more information about how to configure your ServiceNow instance, see [Configure a ServiceNow instance](https://docs.cloud.google.com/datastream/docs/configure-servicenow).

  8. Click **CONTINUE**. The **Test connection profile** section of the **Create ServiceNow profile** page is active.

  9. Click **RUN TEST** to verify that Datastream can communicate with the source.

  10. Click **CREATE**.




## Create a connection profile for a MongoDB database

  1. Go to the **Connection profiles** page in the Google Cloud Console.

[Go to the Connection profiles page](https://console.cloud.google.com/datastream/connection-profiles)

  2. Click **CREATE PROFILE**.

  3. In the **Create a connection profile** page, click the **MongoDB** profile type.

  4. In the **Define connection settings** section, specify the following information: 

Field| Description  
---|---  
Connection profile name| Enter the display name of the connection profile to the source MongoDB database. This is used in the connection profile list as well as when an existing connection profile is selected in the creation of a stream.  
Connection profile ID| Datastream populates this field automatically based on the connection profile name that you enter. You can keep the ID that's auto-generated or change it.  
Region| Select the region where the connection profile is stored. Connection profiles, like all resources, are saved in a region, and a stream can only use connection profiles that are stored in the same region as the stream. Region selection doesn't impact whether Datastream can connect to the source or the destination, but can impact availability if the region experiences downtime.  
Connection string format| Specify the format that you want to use to connect to your MongoDB source:
     * **SRV connection format** : a connection string with a hostname that corresponds to a domain name service (DNS) SRV record. For more information, see the [MongoDB documentation](https://www.mongodb.com/docs/manual/reference/connection-string/#srv-connection-format).
     * **Standard connection string format** : the standard format of the MongoDB connection URI used to connect to a self-hosted MongoDB standalone deployment, replica set, or sharded cluster. For more information, see the [MongoDB documentation](https://www.mongodb.com/docs/manual/reference/connection-string/#standard-connection-string-format). When you select this option, you then need to select one of the supported MongoDB topologies: 
       * **Sharded cluster** : a MongoDB sharded cluster consists of shards, mongos and config servers. MongoDB shards data at the collection level, distributing the collection data across the shards in the cluster.
       * **Replica set** : a replica set in MongoDB is a group of `mongod` processes that maintain the same dataset. Replica sets provide redundancy and high availability, and are the basis for all production deployments. When you select this option, you need to provide a replica set name.  
Hostname| Enter a hostname that Datastream can use to connect to the source MongoDB database. If you're using the standard connection string format, you can add hostnames of all machines in the replica set.If you're using private connectivity to communicate with the source database, then specify the private (internal) IP address for the source database. If you're using a reverse proxy for private connectivity, then use the IP address of the proxy.For other connectivity methods, such as IP allowlisting, provide the public IP address.  
Port| For the **Standard connection string format** only. Enter the port number that's reserved for the source database (the default port for MongoDB is typically 27017). You can add ports of all machines in the replica set when using the standard connection format.  
Username| Enter the username of the account for the source database (for example, `ROOT`). This is the Datastream user that you created for the database.For more information about creating this user, see [Configure your source MongoDB database](https://docs.cloud.google.com/datastream/docs/configure-mongodb).  
Select password from Secret Manager|  Select this option if you want to authenticate with a secret rather than enter the password manually. When select this option, two dropdowns appear: 
     * **Secret** : you can select a secret from the list (if available), enter it manually, or create a new secret:
To enter a secret manually: 
       1. Click **Enter secret manually**. The **Add a secret by resource ID** dialog appears.
       2. Copy and paste your secret resource identifier from Secret Manager. The secret resource ID can have the following format:
          * `projects/PROJECT_NUMBER/secrets/SECRET_NAME` (latest version)
          * `projects/PROJECT_NUMBER/secrets/SECRET_NAME/versions/VERSION_NUMBER` (specific version)
       3. Click the **Add secret** button.
To create a new secret: 
       1. Click **Create new secret**. The **Secret details** side panel opens.
       2. Under **Name** , enter a name for the secret (for example, `my-secret`). A secret name can contain uppercase and lowercase letters, numerals, hyphens, and underscores. The maximum allowed length for a name is 255 characters. The name that you create is added as part of the secret resource identifier.
       3. Optional: To also add a secret version when creating the initial secret, in the **Secret value** field, enter a value for the secret (for example, `abcd1234`). The secret value can be in any format but must not be larger than 64 KiB. You can also upload a text file containing the secret value using the **Upload file** option.
       4. Click the **Create secret** button.
     * **Secret version** : enter the version of the secret that you want to use:
       * When you provide the secret resource identifier, the **Use latest version** checkbox appears. You can select it to use the most up-to-date version of your secret resource.
       * Alternatively, you can expand the **Secret version** drop-down, and select the version from the list, if available.
       * If you want to use a different version of the secret, follow these steps:
         1. Click **Add new version**.
         2. In the **Secret value** field, enter a value for the secret. Alternatively, you can upload a file containing the secret value.
         3. Click the **Add new version** button.  
Enter password manually| Alternatively, you can enter the password of the account for the source database manually.  
  5. Optionally, use labels to organize your Datastream resources.

     1. To create a label, click **ADD LABEL** , and then enter the key-value pair for the label.
     2. To remove the label, click the **trashcan** icon to the right of the row that contains the label.
  6. Click **Continue**.

  7. From the **Encryption type** menu, select one of the following: 

Encryption type| Description  
---|---  
None| Datastream connects to the source database without encryption.  
Server-only| When Datastream connects to the source database, Datastream authenticates the source, ensuring that it is connecting to the correct host securely. This prevents person-in-the-middle attacks. For server-only authentication, the source doesn't authenticate Datastream. To use server-only authentication, you must provide the x509 PEM-encoded certificate of the certificate authority (CA) that signed the source's certificate. Make sure you use a single certificate, Datastream doesn't support certificate chains.  
Server-client| When Datastream connects to the source, Datastream authenticates the source and the source authenticates Datastream.  
  
Server-client authentication provides the strongest security. However, if you don't want to provide the client certificate and private key when you create the connection profile, you can still use server-only authentication.

To use server-client authentication, you must provide the following items when you create the source connection profile:

     * The certificate of the CA that signed the source database server's certificate (the CA certificate).
     * The certificate used by the instance to authenticate against the source database server (the client certificate).
     * The private key associated with the client certificate (the client key).
  8. In the **Define connectivity method** section, from the **Connectivity method** drop-down menu, select a network connectivity method. This method defines how Datastream connects to the source database. Network connectivity methods include:

     1. **IP allowlisting** : This method works by configuring the source database server to accept connections from Datastream. If you select this network connectivity method, then configure your source database to allow incoming connections from the Datastream public IP addresses for the region that you specified for the connection profile.
     2. **Forward-SSH tunnel** : This method creates a secure, encrypted connection between the source database and Datastream. To set up this connectivity method, you need an SSH server that has access to the source database. If you select this network connectivity method, then: 
        1. Enter the SSH server hostname or IP address, and the port of the tunnel host server.
        2. Enter the username of the account for the tunnel host server.
        3. Select the authentication method for the SSH tunnel. If you select **Private/Public key pair** as the method, then provide a [private key](https://docs.cloud.google.com/datastream/docs/network-connectivity-options#generate_private_and_public_keys). If you select **Password** as the method, then enter the password of the account for the bastion host VM.
        4. You might also need to allowlist the Datastream external IP addresses on the SSH tunnel server.
     3. Private connectivity: this method lets you establish secure connectivity between Datastream and the source database, internally within Google Cloud, or with external sources connected over VPN or Interconnect. This communication happens through a Private Service Connect interface or a VPC peering connection.

If you select this network connectivity method, and you have created a private connectivity configuration, then select it from the list of configurations. This type of configuration contains information that Datastream uses to communicate with the source database over a private network.

If you haven't created a private connectivity configuration, create one by clicking **CREATE PRIVATE CONNECTIVITY CONFIGURATION** at the bottom of the drop-down list, and then perform the same steps as in [Create a private connectivity configuration](https://docs.cloud.google.com/datastream/docs/create-a-private-connectivity-configuration#create-the-configuration).

**Note:** You can use private connectivity to connect Datastream to any supported source. However, when you use VPC peering, transitive peering isn't supported. If the network that Datastream is peered with isn't the network where your source is hosted, you're using a fully managed database (for example, Cloud SQL), or if Datastream doesn't run in the region where your source exists, then a NAT VM is required.   
  
For more information, see [VPC peering](https://docs.cloud.google.com/datastream/docs/vpc-peering).
  9. Click **CONTINUE**. The **Test connection profile** section of the **Create MongoDB profile** page is active.

  10. Click **RUN TEST** to verify that Datastream can communicate with the source.

If the test fails, then it indicates which part of the process had an issue. Refer to the [Diagnose issues](https://docs.cloud.google.com/datastream/docs/diagnose-issues#mongodb-errors) page for troubleshooting steps. You can make the necessary changes and then re-test the connection profile.

Navigate to the part of the flow in question to correct the issue, and then retest.

**Note:** The connection profile can be created even if the test fails, but you should fix any issues associated with the connection profile before using the connection profile in a stream.
  11. Click **CREATE**.




## Create a connection profile for a Spanner database

  1. Go to the **Connection profiles** page in the Google Cloud Console.

[Go to the Connection profiles page](https://console.cloud.google.com/datastream/connection-profiles)

  2. Click **CREATE PROFILE**.

  3. In the **Create a connection profile** page, click the **Spanner** profile type.

  4. Use the following table to populate the fields of the **Define connection settings** section of the **Create Spanner profile** page:

Field| Description  
---|---  
Connection profile name| Enter the display name of the connection profile to the source Spanner database.  
Connection profile ID| Datastream populates this field automatically based on the connection profile name that you enter.  
Region| Select the region where the connection profile is stored.  
Database| Enter the full database path, including the project, instance, and database information. It should have the following format: `projects/PROJECT_ID/instances/INSTANCE_ID/databases/DATABASE_ID`.  
  5. Optionally, use labels to organize your Datastream resources.

     1. To create a label, click **ADD LABEL** , and then enter the key-value pair for the label.
     2. To remove the label, click the **trashcan** icon to the right of the row that contains the label.
  6. Click **CONTINUE**. The **Test connection profile** section of the **Create Spanner profile** page is active.

  7. Click **RUN TEST** to verify that Datastream can communicate with the source.

If the test fails, review the error and make any necessary changes before re-testing.

  8. Click **CREATE**.




## Create a connection profile for a Workday instance

  1. Go to the **Connection profiles** page in the Google Cloud Console.

[Go to the Connection profiles page](https://console.cloud.google.com/datastream/connection-profiles)

  2. Click **CREATE PROFILE**.

  3. In the **Create a connection profile** page, click the **Workday** profile type.

  4. Use the following table to populate the fields of the **Define connection settings** section:

Field| Description  
---|---  
Connection profile name| Enter the display name of the connection profile to the source Workday instance.  
Connection profile ID| Datastream populates this field automatically based on the name you enter. You can keep the auto-generated ID or change it.  
Region| Select the region where the connection profile is stored. A stream can only use connection profiles stored in the same region.  
Host| Enter the hostname of your Workday instance, for example `wd5-impl.workday.com`. The hostname is usually derived from your instance login URL. For more information, see [Configure a Workday instance for data replication](https://docs.cloud.google.com/datastream/docs/configure-workday).  
Tenant| Enter the short name or alias of your Workday tenant, for example `google`. This value identifies your specific environment within the Workday host. For more information, see [Configure a Workday instance for data replication](https://docs.cloud.google.com/datastream/docs/configure-workday).  
Client ID| Enter the Client ID retrieved during the API client registration in Workday. For more information, see [Configure a Workday instance for data replication](https://docs.cloud.google.com/datastream/docs/configure-workday).  
Client secret| Enter the client secret associated with your API client. You can enter the raw value or select a secret from the Secret Manager.  
Refresh token| Enter the refresh token generated for your Integration System User. For better security, we recommend storing this value in Secret Manager. For more information, see [Configure a Workday instance for data replication](https://docs.cloud.google.com/datastream/docs/configure-workday).  
  5. Optionally, use labels to organize your Datastream resources.

     1. To create a label, click **ADD LABEL** , and then enter the key-value pair for the label.
     2. To remove the label, click the **trashcan** icon to the right of the row that contains the label.
  6. Click **CONTINUE**.

  7. In the **Review connectivity method** section, review the Datastream regional IP addresses listed. Ensure your Workday organization is configured to accept incoming connections from these addresses.

  8. Click **CONTINUE**. The **Test connection profile** section is active.

  9. Click **RUN TEST** to verify that Datastream can communicate with the source Workday instance.

  10. Click **CREATE**.




## Create a connection profile for BigQuery

**Note:** These instructions also apply to the Apache Iceberg tables destination.

  1. Go to the **Connection profiles** page in the Google Cloud Console.

[Go to the Connection profiles page](https://console.cloud.google.com/datastream/connection-profiles)

  2. Click **CREATE PROFILE**.

  3. In the **Create a connection profile** page, click the **BigQuery** profile type.

  4. Use the following table to populate the fields of the **Create BigQuery profile** page:

Field| Description  
---|---  
Connection profile name| Enter the display name of the connection profile to the destination datasets in BigQuery. This is used in the connection profile list as well as when an existing connection profile is selected in the creation of a stream.  
Connection profile ID| Keep the auto-generated value that's populated in this field.  
Region| Select the region where the connection profile is stored. Connection profiles, like all resources, are saved in a region, and a stream can only use connection profiles that are stored in the same region as the stream. Region selection doesn't impact whether Datastream can connect to the source or the destination, but can impact availability if the region experiences downtime. Although the region that you select for your connection profile is independent of the location type that you selected for your BigQuery destination dataset, we recommend keeping all resources for the stream in the same region as your source data for cost and performance optimization.  
  5. Optionally, use labels to organize your Datastream resources.

     1. To create a label, click **ADD LABEL** , and then enter the key-value pair for the label.
     2. To remove the label, click the **trashcan** icon to the right of the row that contains the label.
  6. Click **CREATE**.




## Create a connection profile for Cloud Storage

  1. Go to the **Connection profiles** page in the Google Cloud Console.

[Go to the Connection profiles page](https://console.cloud.google.com/datastream/connection-profiles)

  2. Click **CREATE PROFILE**.

  3. In the **Create a connection profile** page, click the **Cloud Storage** profile type.

  4. Use the following table to populate the fields of the **Create Cloud Storage profile** page:

Field| Description  
---|---  
Connection profile name| Enter the display name of the connection profile to the destination bucket in Cloud Storage. This is used in the connection profile list as well as when an existing connection profile is selected in the creation of a stream.  
Connection profile ID| Keep the auto-generated value that's populated in this field.  
Region| Select the region where the connection profile is stored. Connection profiles, like all resources, are saved in a region, and a stream can only use connection profiles that are stored in the same region as the stream. Region selection doesn't impact whether Datastream can connect to the source or the destination, but can impact availability if the region experiences downtime.  
Bucket name| Click **BROWSE** to create or select the destination bucket in Cloud Storage into which Datastream will transfer data from the source database. If you select an existing bucket, then complete the following steps:
     1. Click the **Search** icon (which appears as a magnifying glass).
     2. In the **Search by name** field, enter the first few characters of the name of the bucket that you want to select. Datastream filters the list of buckets to reflect what you enter in the field.
     3. Select the bucket that you want to use as your destination.
     4. Click **SELECT**. Your bucket appears in the **Bucket name** field.
Alternatively, you can click the **Create new bucket** icon (which appears as a briefcase) to [create a bucket](https://docs.cloud.google.com/storage/docs/creating-buckets).   
  5. Optionally, in the **Connection profile path prefix** field, you can provide a prefix for the path that will be appended to the bucket name when Datastream transfers data to the destination.

**Note:** Any path that you enter in this field must start with a slash (`/`).
  6. Optionally, use labels to organize your Datastream resources.

     1. To create a label, click **ADD LABEL** , and then enter the key-value pair for the label.
     2. To remove the label, click the **trashcan** icon to the right of the row that contains the label.
  7. Click **CREATE**.




After creating connection profiles, you can [view high-level and detailed information](https://docs.cloud.google.com/datastream/docs/view-connection-profiles) about them.

## What's next

  * Learn how to [modify connection profiles](https://docs.cloud.google.com/datastream/docs/modify-connection-profiles).
  * Learn how to [view connection profiles](https://docs.cloud.google.com/datastream/docs/view-connection-profiles).
  * Find out how to [delete connection profiles](https://docs.cloud.google.com/datastream/docs/delete-a-connection-profile).
  * Learn more about how Datastream works with [Dataverse sources](https://docs.cloud.google.com/datastream/docs/sources-dataverse).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
