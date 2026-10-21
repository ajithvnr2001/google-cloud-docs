---
url: https://docs.cloud.google.com/looker/docs/db-config-cloudera-impala/
title: Cloudera Impala 3.1+ and Cloudera Impala with Native Driver \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:25:15.114377+00:00
---

# Cloudera Impala 3.1+ and Cloudera Impala with Native Driver  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/db-config-cloudera-impala/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Cloudera Impala 3.1+ and Cloudera Impala with Native Driver Stay organized with collections  Save and categorize content based on your preferences. 

Connect your Cloudera Impala databases to Looker to visualize and analyze your data. You can configure these connections for various Impala dialects. Looker supports Cloudera Impala versions 3.1 and later, including standard and native driver configurations. Connections to older Impala dialects lacking a version number or native driver are not supported; queries to these will return an error.

## Dialects that use these instructions

Looker connects to the following Impala databases:

  * Cloudera Impala 3.1+
  * Cloudera Impala 3.1+ with Native Driver
  * Cloudera Impala with Native Driver

**Note:** Looker does not support connections to the Impala dialect called _Cloudera Impala_ (with no version number and without a native driver). Queries on connections to the _Cloudera Impala_ dialect will return an error.

## Encrypting network traffic

It is a best practice to encrypt network traffic between the Looker application and your database. Consider one of the options that are described on the [Enabling secure database access](https://docs.cloud.google.com/looker/docs/enabling-secure-db-access) documentation page.

## Configuring Looker to connect to Cloudera Impala

Looker connects to databases through a JDBC connection. For Impala databases, Looker connects by default to the server that is running the `impalad` daemon on port 21050. For more information, see the [Configuring Impala to work with JDBC](https://www.cloudera.com/documentation/enterprise/latest/topics/impala_jdbc.html) section of the documentation on the Cloudera website.

In the **Admin** section of Looker, select **Connections** , and then click **Add Connection**.

The Looker connection configuration depends on the security that is being used:

  * A cluster not using Kerberos or user authentication
  * A cluster requiring LDAP authentication
  * A cluster secured with Kerberos, but not using Apache Sentry



### Connecting to a cluster without Kerberos or user authentication

To configure a connection that isn't using Kerberos or user authentication, follow these steps:

  1. On the **Connection Settings** page, leave the **Username** and **Password** fields blank. (The `*` next to the field names implies that these fields are required, but they are not.)
  2. In the **Additional JDBC parameters** field, enter `;auth=noSasl`.



#### Verifying the connection string

To verify the JDBC connection string in the log files, in the Looker **Admin** panel, click **Log** in the left menu. Then filter the log on a term such as `jdbc` or `noSasl`. The log line may look something like this:
    
    
    jdbc connect using: jdbc:hive2://<HOSTNAME>/<DATABASE_NAME>;auth=noSasl
    

For more information about configuring Impala databases to work with JDBC, see the [documentation on the external Cloudera website](https://www.cloudera.com/content/cloudera/en/documentation/core/latest/topics/impala_jdbc.html#jdbc_connect_unique_1).

### Connecting to a cluster requiring LDAP authentication

For a cluster that requires LDAP authentication, including a cluster with Apache Sentry and Kerberos, on the **Connection Settings** page, enter a **Username** and **Password** with access to the schemas Looker will access.

### Connecting to a cluster secured with Kerberos, but not using Apache Sentry

**Note:** The Looker analyst team may need to assist in configuring this connection correctly.

Usually, Kerberos authentication with Cloudera environments is handled through [Apache Sentry](https://sentry.incubator.apache.org/). See the [Cloudera documentation](https://www.cloudera.com/content/www/en-us/documentation/enterprise/latest/topics/sg_sentry_service_config.html) for more details.

If you want to configure Looker to connect directly to Impala databases using Kerberos authentication, follow the steps on this page.

#### Setting up the Kerberos client configuration

First, verify that the required software is installed and necessary files are present on the Looker machine.

##### Kerberos client

Verify that the Kerberos client is installed on the Looker machine by trying to run `kinit`. If the Kerberos client is not installed, install the Kerberos client's binaries.

For example, on Red Hat/CentOS, run the following command:
    
    
    sudo yum install krb5-workstation krb5-libs krb5-auth-dialog
    

##### Java 8

Java 8 must be installed on the Looker machine and in the `PATH` and `JAVA_HOME` of the Looker user. If necessary, install it locally in the `looker` directory.

##### Java Cryptography Extension

  1. Download and install the Java Cryptography Extension (JCE) for Java 8 from [the Oracle website](https://www.oracle.com/technetwork/java/javase/downloads/jce8-download-2133166.html).

     * Locate the `jre/lib/security` directory for the Java installation.
     * Remove the following JAR files from this directory: `local_policy.jar` and `US_export_policy.jar`.
     * Replace these two files with the JAR files included in the JCE Unlimited Strength Jurisdiction Policy Files download.

It may be possible to use versions of Java prior to Java 8 with the JCE installed, but this is not recommended.

  2. Update `JAVA_HOME` and `PATH` in `~looker/.bash_profile` to point to the correct installation of Java and `source ~/.bash_profile` or log out and in again.

  3. Verify the Java version with `java -version`.

  4. Verify the `JAVA_HOME` environment variable with `echo $JAVA_HOME`.




##### `gss-jaas.conf`

Create a `gss-jaas.conf` file in the `looker` directory with these contents:
    
    
    com.sun.security.jgss.initiate {
        com.sun.security.auth.module.Krb5LoginModule required
        useTicketCache=true
        doNotPrompt=true;
    };
    

If necessary for testing, `debug=true` can be added to this file like this:
    
    
    com.sun.security.jgss.initiate {
        com.sun.security.auth.module.Krb5LoginModule required
        useTicketCache=true
        doNotPrompt=true
        debug=true;
    };
    

##### `krb5.conf`

The server that is running Looker should also have a valid `krb5.conf` file. By default, this file is in `/etc/krb5.conf`. If it is in another location, that must be indicated in the environment (`KRB5_CONFIG` in the shell environment).

You may need to copy this from another Kerberos client machine.

##### `lookerstart.cfg`

Point to the `gss-jaas.conf` and `krb5.conf` files by making a file in the `looker` directory (the same directory that contains the `looker` startup script) called `lookerstart.cfg` that contains the following lines:
    
    
      JAVAARGS="-Djava.security.auth.login.config=/path/to/gss-jaas.conf -Djavax.security.auth.useSubjectCredsOnly=false -Djava.security.krb5.conf=/etc/krb5.conf"
      LOOKERARGS=""
    

If the `krb5.conf` file is not at `/etc/krb5.conf` then it will also be necessary to add this variable:
    
    
      -Djava.security.krb5.conf=/path/to/krb5.conf
    

For debugging, add these variables:
    
    
      -Dsun.security.jgss.debug=true -Dsun.security.krb5.debug=true
    

Then restart Looker with `./looker restart`.

#### Authenticating with Kerberos

##### User authentication

  1. If `krb5.conf` is not in `/etc/`, then use the environment variable `KRB5_CONFIG` to indicate its location.

  2. Run the command `klist` to make sure there is a valid ticket in the Kerberos ticket cache.

  3. If there is no ticket, run `kinit username@REALM` or `kinit username` to create the ticket.

  4. The account that is used with Looker will likely be headless, so you can get a keytab file from Kerberos to store the credential for long-term use. Use a command like `kinit -k -t looker_user.keytab username@REALM` to get the Kerberos ticket.




##### Automatically renewing the ticket

Set up a cron job that runs every so often to keep an active ticket in the Kerberos ticket cache. How often this should run depends on the configuration of the cluster. `klist` should give an indication of how soon tickets expire.

## Creating the Looker connection to your database

In the **Admin** section of Looker, select **Connections** , and then click **Add Connection**.

Fill out the connection details as follows (see the [Connecting Looker to your database](https://docs.cloud.google.com/looker/docs/connecting-to-your-db) documentation page for more information):

  * **Name** : The name of the connection. This is how the connection will be referred to in the LookML model.
  * **Dialect** : **Cloudera Impala 3.1+** , **Cloudera Impala 3.1+ with Native Driver** , or **Cloudera Impala with Native Driver**.

**Note:** If you are on a [Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-overview) instance and you don't see your dialect listed in the **Dialect** menu, see the [Looker (Google Cloud core) documentation](https://docs.cloud.google.com/looker/docs/looker-core-dialects#supported_dialects_for) to verify that the dialect is supported for Looker (Google Cloud core) instances.
  * **Host** : Hostname.

  * **Port** : Database port (21050 by default).

  * **Database** : The default schema/database that will be modeled. When no database is specified for a table, this will be assumed.

  * **Username** : Leave this blank.

  * **Password** : Leave this blank.

  * **Enable PDTs** : Use this toggle to enable [persistent derived tables](https://docs.cloud.google.com/looker/docs/derived-tables#persistent-derived-tables). When PDTs are enabled, the **Connection** window reveals additional PDT settings and the [**PDT Overrides**](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#pdt-overrides) section.

  * **Temp Database** : A temporary schema/database for storing PDTs. This must be created beforehand.

  * **Additional JDBC parameters** : Add any additional JDBC parameters. See the Supported JDBC parameters section on this page for a list of supported parameters.

  * **SSL** : Check to use SSL connections. If your SSL certificate is not issued by a widely recognized Certificate Authority and you are using a custom certificate, you will need to:

    * Copy the certificate file to the Looker server. This is only available for customer-hosted Looker deployments.
    * Add the following parameters to the **Additional JDBC parameters** field:


    
    
      sslTrustStore=/path/to/your/trust_store.jks;trustStorePassword=yourpassword
    

> See [the Cloudera documentation](https://www.cloudera.com/content/cloudera/en/documentation/core/latest/topics/sg_hive_encryption.html#concept_rqh_sff_cm_unique_) for more details about how to form the correct JDBC strings for Impala databases.

  * **Database Time Zone** : The time zone of data stored in your database. Usually this can be left blank or set to **UTC**.



It is a best practice to have the server name (`impala.company.com` in this example) be the canonical name for the server and its IP address's reverse DNS lookup results in that name. However, the server name should be whatever is listed in the Kerberos domain controller:
    
    
      nslookup servername  # get canonical server name and IP address
    
      nslookup ipaddress  # get the canonical name back
    

Sometimes the server name is set to be the hostname, and not the fully qualified domain name. In this case it may be necessary to modify the `/etc/hosts` and `/etc/nsswitch.conf` files to make sure that reverse lookups resolve as intended.

Test the connection to make sure that it is configured correctly.

#### Debugging

  * [Cloudera's documentation about debugging Impala authentication issues.](https://www.cloudera.com/content/www/en-us/documentation/enterprise/latest/topics/cm_sg_sec_troubleshooting.html)
  * When you add debugging to the configuration, the extra debugging information will wind up in `looker/logs/looker.log`.



#### Resources

  * [Enabling Kerberos authentication for Impala (Cloudera documentation)](https://www.cloudera.com/content/www/en-us/documentation/enterprise/latest/topics/impala_kerberos.html)
  * [kinit man page](https://linux.die.net/man/1/kinit)
  * [klist man page](https://linux.die.net/man/1/klist)
  * [gss-jaas.conf documentation](https://docs.oracle.com/javase/8/docs/technotes/guides/security/jgss/tutorials/LoginConfigFile.html)
  * [Krb5LoginModule documentation](https://docs.oracle.com/javase/8/docs/jre/api/security/jaas/spec/com/sun/security/auth/module/Krb5LoginModule.html)



## Permissions for PDTs

The user connecting to the scratch schema for [persistent derived tables (PDTs)](https://docs.cloud.google.com/looker/docs/derived-tables#persistent_derived_table) must have read/write permissions.

## Supported JDBC parameters

For Cloudera Impala, Looker supports the following JDBC parameters in the [**Additional JDBC parameters**](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#additional_jdbc_parameters) field for the connection. See the documentation for your database for information on these parameters.

  * `AllowSelfSignedCerts`
  * `auth`
  * `AuthMech`
  * `CAIssuedCertNamesMismatch`
  * `httpPath`
  * `KrbHostFQDN`
  * `KrbRealm`
  * `KrbServiceName`
  * `principal`
  * `PWD`
  * `SocketTimeout`
  * `SSL`
  * `transportMode`
  * `UID`
  * `UseNativeQuery`
  * `UseSasl`



## Feature support

For Looker to support some features, your database dialect must also support them.

### Cloudera Impala with Native Driver

Cloudera Impala with Native Driver supports the following features as of Looker 26.20:

Feature | Supported?  
---|---  
Looker (Google Cloud core)|   
Symmetric aggregates|   
Derived tables|   
Persistent SQL derived tables|   
Persistent native derived tables|   
Stable views|   
Query killing|   
SQL-based pivots|   
Time zones|   
SSL|   
Subtotals|   
JDBC additional params|   
Case-sensitive|   
Location type|   
List type|   
Percentile|   
Distinct percentile|   
SQL Runner Show Processes|   
SQL Runner Describe Table|   
SQL Runner Show Indexes|   
SQL Runner Select 10|   
SQL Runner Count|   
SQL Explain|   
OAuth 2.0 credentials|   
Context comments|   
Connection pooling|   
HLL sketches|   
Aggregate awareness|   
Incremental PDTs|   
Milliseconds|   
Microseconds|   
Materialized views|   
Period-over-period measures|   
Approximate count distinct|   
In-database analytic models|   
Custom calendars|   
  
### Cloudera Impala 3.1+

Cloudera Impala 3.1+ supports the following features as of Looker 26.20:

Feature | Supported?  
---|---  
Looker (Google Cloud core)|   
Symmetric aggregates|   
Derived tables|   
Persistent SQL derived tables|   
Persistent native derived tables|   
Stable views|   
Query killing|   
SQL-based pivots|   
Time zones|   
SSL|   
Subtotals|   
JDBC additional params|   
Case-sensitive|   
Location type|   
List type|   
Percentile|   
Distinct percentile|   
SQL Runner Show Processes|   
SQL Runner Describe Table|   
SQL Runner Show Indexes|   
SQL Runner Select 10|   
SQL Runner Count|   
SQL Explain|   
OAuth 2.0 credentials|   
Context comments|   
Connection pooling|   
HLL sketches|   
Aggregate awareness|   
Incremental PDTs|   
Milliseconds|   
Microseconds|   
Materialized views|   
Period-over-period measures|   
Approximate count distinct|   
In-database analytic models|   
Custom calendars|   
  
### Cloudera Impala 3.1+ with Native Driver

Cloudera Impala 3.1+ with Native Driver supports the following features as of Looker 26.20:

Feature | Supported?  
---|---  
Looker (Google Cloud core)|   
Symmetric aggregates|   
Derived tables|   
Persistent SQL derived tables|   
Persistent native derived tables|   
Stable views|   
Query killing|   
SQL-based pivots|   
Time zones|   
SSL|   
Subtotals|   
JDBC additional params|   
Case-sensitive|   
Location type|   
List type|   
Percentile|   
Distinct percentile|   
SQL Runner Show Processes|   
SQL Runner Describe Table|   
SQL Runner Show Indexes|   
SQL Runner Select 10|   
SQL Runner Count|   
SQL Explain|   
OAuth 2.0 credentials|   
Context comments|   
Connection pooling|   
HLL sketches|   
Aggregate awareness|   
Incremental PDTs|   
Milliseconds|   
Microseconds|   
Materialized views|   
Period-over-period measures|   
Approximate count distinct|   
In-database analytic models|   
Custom calendars|   
  
## Next steps

After you have connected your database to Looker, [configure sign-in options for your users](https://docs.cloud.google.com/looker/docs/getting-started-with-users).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
