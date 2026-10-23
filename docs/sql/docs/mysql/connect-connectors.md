---
url: https://docs.cloud.google.com/sql/docs/mysql/connect-connectors/
title: Connect using Cloud SQL Language Connectors \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:20:01.304590+00:00
---

# Connect using Cloud SQL Language Connectors  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/connect-connectors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Connect using Cloud SQL Language Connectors Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/connect-connectors "View this page for the PostgreSQL database engine") | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/connect-connectors "View this page for the SQL Server database engine")

The Cloud SQL Connectors are libraries that provide encryption and Identity and Access Management (IAM)-based authorization when connecting to a Cloud SQL instance. They can't provide a network path to a Cloud SQL instance if one is not already present.

Other ways to connect to a Cloud SQL instance include [using a database client](https://docs.cloud.google.com/sql/docs/mysql/connect-admin-ip) or the [Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/mysql/sql-proxy). See the [About connection options](https://docs.cloud.google.com/sql/docs/mysql/connect-overview) page for more information about connecting to a Cloud SQL instance.

This page discusses the following Cloud SQL Connectors:

  * The Cloud SQL Java Connector 
  * The Cloud SQL Python Connector [(Open in Colab)](https://colab.research.google.com/github/GoogleCloudPlatform/cloud-sql-python-connector/blob/main/samples/notebooks/mysql_python_connector.ipynb)
  * The Cloud SQL Go Connector
  * The Cloud SQL Node.js Connector



## Benefits

Using a Cloud SQL connector provides the following benefits:

  * **IAM authorization:** Uses IAM permissions to control who or what can connect to your Cloud SQL instances.
  * **Convenience:** Removes the requirement to manage SSL certificates, configure firewall rules, or enable authorized networks.



## Before you begin

  * Enable the Cloud SQL Admin API. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=sqladmin&redirect=https%3A//console.cloud.google.com)

  * Create a Cloud SQL instance, including configuring the default user.  


For more information about creating instances, see [Create instances](https://docs.cloud.google.com/sql/docs/mysql/create-instance).

For more information about configuring the default user, see [Set the password for the default user account](https://docs.cloud.google.com/sql/docs/mysql/create-manage-users#user-root).

  * Configure the [roles and permissions](https://docs.cloud.google.com/sql/docs/mysql/roles-and-permissions) required to connect to a Cloud SQL instance. **Note:** If the authorizing IAM principal belongs to a different project than the one that contains the Cloud SQL instance, then you must do the following: 
    * Enable the Cloud SQL Admin API in both the projects.
    * Add the IAM permissions for the IAM principal in the project that contains the Cloud SQL instance.



## Setup

### Java

The Cloud SQL Java Connector is a library that provides IAM-based authorization and encryption when connecting to a Cloud SQL instance. It can _not_ provide a network path to a Cloud SQL instance if one is not already present.

### Install

For instructions on building and using the drivers for JDBC and R2DBC with the Cloud SQL Java Connector, see the following links:

  * JDBC: [Connecting to Cloud SQL using JDBC](https://github.com/GoogleCloudPlatform/cloud-sql-jdbc-socket-factory/blob/main/docs/jdbc.md).
  * R2DBC: [Connecting to Cloud SQL using R2DBC](https://github.com/GoogleCloudPlatform/cloud-sql-jdbc-socket-factory/blob/main/docs/r2dbc.md).



For examples of this library being used in the context of an application, check out these [sample applications](https://docs.cloud.google.com/sql/docs/mysql/manage-connections#java).

### Authenticate

This library uses [Application Default Credentials](https://developers.google.com/identity/protocols/application-default-credentials) to authenticate the connection to the Cloud SQL server.

To activate credentials locally, use the following [gcloud](https://docs.cloud.google.com/sdk/gcloud) command:
    
    
        gcloud auth application-default login
        

### Connect with Intellij

In order to [connect IntelliJ](https://jetbrains.com/help/idea/connecting-to-a-database.html#mysql) to your Cloud SQL instance, you will need to add the library as a jar with dependencies in the **Additional Files** section on the driver settings page. For example, prebuilt fat jars can be found on the [Cloud SQL Java Connector Releases](https://github.com/GoogleCloudPlatform/cloud-sql-jdbc-socket-factory/releases) page for this purpose.

### Python

The Cloud SQL Python Connector is a library that can be used alongside a database driver to allow users with sufficient permissions to connect to a Cloud SQL database without having to manually allowlist IPs or manage SSL certificates.

For interactive examples of using the Cloud SQL Python Connector, open the [Cloud SQL Python Connector notebook](https://colab.research.google.com/github/GoogleCloudPlatform/cloud-sql-python-connector/blob/main/samples/notebooks/mysql_python_connector.ipynb).

The driver that MySQL supports is [pymysql](https://github.com/PyMySQL/PyMySQL).

### Install

To install the latest release of the Cloud SQL Python Connector, use the `pip install` command and specify the `pymysql` driver for your database:
    
    
        pip install "cloud-sql-python-connector[pymysql]"
        

### Authenticate

This library uses [Application Default Credentials](https://developers.google.com/identity/protocols/application-default-credentials) to authenticate the connection to the Cloud SQL server.

To activate credentials locally, use the following [gcloud](https://docs.cloud.google.com/sdk/gcloud) command:
    
    
        gcloud auth application-default login
        

### Go

The Cloud SQL Go connector is a Cloud SQL connector designed for use with the Go language. For improved security, this connector uses robust, manually authenticated TLS 1.3 encryption between the client connector and the server-side proxy, independent of the database protocol.

### Install

You can install this repo with `go get`:
    
    
        go get cloud.google.com/go/cloudsqlconn
        

### Node.js

The Node.js Connector is a library designed for use with the Node.js runtime that allows you to connect securely to your Cloud SQL instance.

### Install

You can install the library with `npm install`:
    
    
        npm install @google-cloud/cloud-sql-connector
        

## Use

### Java

To see this snippet in the context of a web application, view [the README on GitHub](https://github.com/GoogleCloudPlatform/java-docs-samples/blob/master/cloud-sql/mysql/servlet/README.md).
    
    
    import com.zaxxer.hikari.HikariConfig;
    import com.zaxxer.hikari.HikariDataSource;
    import javax.sql.DataSource;
    
    public class ConnectorConnectionPoolFactory extends ConnectionPoolFactory {
    
      // Note: Saving credentials in environment variables is convenient, but not
      // secure - consider a more secure solution such as
      // Cloud Secret Manager (https://cloud.google.com/secret-manager) to help
      // keep secrets safe.
      private static final String INSTANCE_CONNECTION_NAME =
          System.getenv("INSTANCE_CONNECTION_NAME");
      private static final String INSTANCE_UNIX_SOCKET = System.getenv("INSTANCE_UNIX_SOCKET");
      private static final String DB_USER = System.getenv("DB_USER");
      private static final String DB_PASS = System.getenv("DB_PASS");
      private static final String DB_NAME = System.getenv("DB_NAME");
    
      public static DataSource createConnectionPool() {
        // The configuration object specifies behaviors for the connection pool.
        HikariConfig config = new HikariConfig();
    
        // The following URL is equivalent to setting the config options below:
        // jdbc:mysql:///<DB_NAME>?cloudSqlInstance=<INSTANCE_CONNECTION_NAME>&
        // socketFactory=com.google.cloud.sql.mysql.SocketFactory&user=<DB_USER>&password=<DB_PASS>
        // See the link below for more info on building a JDBC URL for the Cloud SQL JDBC Socket Factory
        // https://github.com/GoogleCloudPlatform/cloud-sql-jdbc-socket-factory#creating-the-jdbc-url
    
        // Configure which instance and what database user to connect with.
        config.setJdbcUrl(String.format("jdbc:mysql:///%s", DB_NAME));
        config.setUsername(DB_USER); // e.g. "root", "mysql"
        config.setPassword(DB_PASS); // e.g. "my-password"
    
        config.addDataSourceProperty("socketFactory", "com.google.cloud.sql.mysql.SocketFactory");
        config.addDataSourceProperty("cloudSqlInstance", INSTANCE_CONNECTION_NAME);
    
    
        // The ipTypes argument can be used to specify a comma delimited list of preferred IP types
        // for connecting to a Cloud SQL instance. The argument ipTypes=PRIVATE will force the
        // SocketFactory to connect with an instance's associated private IP.
        config.addDataSourceProperty("ipTypes", "PUBLIC,PRIVATE");
    
        // cloudSqlRefreshStrategy set to "lazy" is used to perform a
        // refresh when needed, rather than on a scheduled interval.
        // This is recommended for serverless environments to
        // avoid background refreshes from throttling CPU.
        config.addDataSourceProperty("cloudSqlRefreshStrategy", "lazy");
    
        // ... Specify additional connection properties here.
        // ...
    
        // Initialize the connection pool using the configuration object.
        return new HikariDataSource(config);
      }
    }

### Python

See [ How to use this Connector](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector#how-to-use-this-connector) for detailed instructions on using the library. View example connection test code on GitHub.
    
    
    import os
    
    from google.cloud.sql.connector import Connector, IPTypes
    import pymysql
    
    import sqlalchemy
    
    
    def connect_with_connector() -> sqlalchemy.engine.base.Engine:
        """
        Initializes a connection pool for a Cloud SQL instance of MySQL.
    
        Uses the Cloud SQL Python Connector package.
        """
        # Note: Saving credentials in environment variables is convenient, but not
        # secure - consider a more secure solution such as
        # Cloud Secret Manager (https://cloud.google.com/secret-manager) to help
        # keep secrets safe.
    
        instance_connection_name = os.environ[
            "INSTANCE_CONNECTION_NAME"
        ]  # e.g. 'project:region:instance'
        db_user = os.environ["DB_USER"]  # e.g. 'my-db-user'
        db_pass = os.environ["DB_PASS"]  # e.g. 'my-db-password'
        db_name = os.environ["DB_NAME"]  # e.g. 'my-database'
    
        ip_type = IPTypes.PRIVATE if os.environ.get("PRIVATE_IP") else IPTypes.PUBLIC
    
        # initialize Cloud SQL Python Connector object
        connector = Connector(ip_type=ip_type, refresh_strategy="LAZY")
    
        def getconn() -> pymysql.connections.Connection:
            conn: pymysql.connections.Connection = connector.connect(
                instance_connection_name,
                "pymysql",
                user=db_user,
                password=db_pass,
                db=db_name,
            )
            return conn
    
        pool = sqlalchemy.create_engine(
            "mysql+pymysql://",
            creator=getconn,
            # ...
        )
        return pool
    
    

### Go

See [ Usage](https://github.com/GoogleCloudPlatform/cloud-sql-go-connector#usage) for detailed instructions on using the library. View example connection test code on GitHub.
    
    
    package cloudsql
    
    import (
    	"context"
    	"database/sql"
    	"fmt"
    	"log"
    	"net"
    	"os"
    
    	"cloud.google.com/go/cloudsqlconn"
    	"github.com/go-sql-driver/mysql"
    )
    
    func connectWithConnector() (*sql.DB, error) {
    	mustGetenv := func(k string) string {
    		v := os.Getenv(k)
    		if v == "" {
    			log.Fatalf("Fatal Error in connect_connector.go: %s environment variable not set.", k)
    		}
    		return v
    	}
    	// Note: Saving credentials in environment variables is convenient, but not
    	// secure - consider a more secure solution such as
    	// Cloud Secret Manager (https://cloud.google.com/secret-manager) to help
    	// keep passwords and other secrets safe.
    	var (
    		dbUser                 = mustGetenv("DB_USER")                  // e.g. 'my-db-user'
    		dbPwd                  = mustGetenv("DB_PASS")                  // e.g. 'my-db-password'
    		dbName                 = mustGetenv("DB_NAME")                  // e.g. 'my-database'
    		instanceConnectionName = mustGetenv("INSTANCE_CONNECTION_NAME") // e.g. 'project:region:instance'
    		usePrivate             = os.Getenv("PRIVATE_IP")
    	)
    
    	// WithLazyRefresh() Option is used to perform refresh
    	// when needed, rather than on a scheduled interval.
    	// This is recommended for serverless environments to
    	// avoid background refreshes from throttling CPU.
    	d, err := cloudsqlconn.[NewDialer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudsqlconn/latest/index.html#cloud_google_com_go_cloudsqlconn_Dialer_NewDialer)(context.Background(), cloudsqlconn.[WithLazyRefresh](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudsqlconn/latest/index.html#cloud_google_com_go_cloudsqlconn_Option_WithLazyRefresh)())
    	if err != nil {
    		return nil, fmt.Errorf("cloudsqlconn.NewDialer: %w", err)
    	}
    	var opts []cloudsqlconn.[DialOption](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudsqlconn/latest/index.html#cloud_google_com_go_cloudsqlconn_DialOption)
    	if usePrivate != "" {
    		opts = append(opts, cloudsqlconn.[WithPrivateIP](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudsqlconn/latest/index.html#cloud_google_com_go_cloudsqlconn_DialOption_WithPrivateIP)())
    	}
    	mysql.RegisterDialContext("cloudsqlconn",
    		func(ctx context.Context, addr string) (net.Conn, error) {
    			return d.[Dial](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudsqlconn/latest/index.html#cloud_google_com_go_cloudsqlconn_Dialer_Dial)(ctx, instanceConnectionName, opts...)
    		})
    
    	dbURI := fmt.Sprintf("%s:%s@cloudsqlconn(localhost:3306)/%s?parseTime=true",
    		dbUser, dbPwd, dbName)
    
    	dbPool, err := sql.Open("mysql", dbURI)
    	if err != nil {
    		return nil, fmt.Errorf("sql.Open: %w", err)
    	}
    	return dbPool, nil
    }
    

### Node.js

For detailed instructions on using the library, see [ Usage](https://github.com/GoogleCloudPlatform/cloud-sql-nodejs-connector#usage).
    
    
    const mysql = require('mysql2/promise');
    const {Connector} = require('@google-cloud/cloud-sql-connector');
    
    // In case the PRIVATE_IP environment variable is defined then we set
    // the ipType=PRIVATE for the new connector instance, otherwise defaults
    // to public ip type.
    const getIpType = () =>
      process.env.PRIVATE_IP === '1' || process.env.PRIVATE_IP === 'true'
        ? 'PRIVATE'
        : 'PUBLIC';
    
    // connectWithConnector initializes a connection pool for a Cloud SQL instance
    // of MySQL using the Cloud SQL Node.js Connector.
    const connectWithConnector = async config => {
      // Note: Saving credentials in environment variables is convenient, but not
      // secure - consider a more secure solution such as
      // Cloud Secret Manager (https://cloud.google.com/secret-manager) to help
      // keep secrets safe.
      const connector = new Connector();
      const clientOpts = await connector.getOptions({
        instanceConnectionName: process.env.INSTANCE_CONNECTION_NAME,
        ipType: getIpType(),
      });
      const dbConfig = {
        ...clientOpts,
        user: process.env.DB_USER, // e.g. 'my-db-user'
        password: process.env.DB_PASS, // e.g. 'my-db-password'
        database: process.env.DB_NAME, // e.g. 'my-database'
        // ... Specify additional properties here.
        ...config,
      };
      // Establish a connection to the database.
      return mysql.createPool(dbConfig);
    };

## Enforce

By using [connector enforcement](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances#ConnectorEnforcement), you can enforce using only the Cloud SQL Auth Proxy or Cloud SQL Language Connectors to connect to Cloud SQL instances. With connector enforcement, Cloud SQL rejects direct connections to the database.

If you're using a [Private Service Connect-enabled instance](https://docs.cloud.google.com/sql/docs/mysql/about-private-service-connect), then there's a limitation. If the instance has connector enforcement enabled, then you can't create read replicas for the instance. Similarly, if the instance has read replicas, then you can't enable connector enforcement for the instance.

### gcloud

To enforce using only the Cloud SQL Auth Proxy or Cloud SQL Language Connectors to connect to an instance, use the [`gcloud sql instances patch`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/patch) command:
    
    
    gcloud sql instances patch INSTANCE_NAME \
    --connector-enforcement=REQUIRED

Replace `INSTANCE_NAME` with the name of your Cloud SQL instance.

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that contains the instance
  * INSTANCE_NAME: the name of your Cloud SQL instance

**Note:** By setting the value of the `connectorEnforcement` parameter to `REQUIRED`, all connections must use the Cloud SQL Language Connectors, including the Cloud SQL Auth Proxy and the Java, Python, Go, and Node.js connectors.

HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_NAME

Request JSON body: 
    
    
    {
      "kind": "sql#instance",
      "name": INSTANCE_NAME,
      "project": PROJECT_ID,
      "settings": {
      "connectorEnforcement": "REQUIRED",
      "kind": "sql#settings"
      }
    }

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_NAME"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_NAME" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_NAME",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-16T02:32:12.281Z",
      "operationType": "UPDATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_NAME",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

## Troubleshoot

### Driver versions

Make sure you are using the latest version of the Cloud SQL Connectors and your database driver to avoid incompatibilities. Some older versions of drivers are not supported.

### Connection paths

The Cloud SQL Connectors provide authorization for connections, but they don't provide new paths to connectivity. For example, in order to connect to a Cloud SQL instance using a Private IP address, your application must already have VPC access.

### Debug connection issues

For additional help with connection issues, see the [Troubleshoot](https://docs.cloud.google.com/sql/docs/mysql/troubleshooting#connectivity) and [Debug connection issues](https://docs.cloud.google.com/sql/docs/mysql/debugging-connectivity) pages.

## What's next

  * See the [Cloud SQL Java Connector home page on GitHub](https://github.com/GoogleCloudPlatform/cloud-sql-jdbc-socket-factory).
  * See the [Cloud SQL Python Connector home page on GitHub](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector).
  * Learn more about the [Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/mysql/sql-proxy).
  * Learn more about [IAM](https://docs.cloud.google.com/iam/docs/overview).
  * Learn about [options for support](https://docs.cloud.google.com/sql/docs/support).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
