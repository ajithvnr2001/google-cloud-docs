---
url: https://docs.cloud.google.com/sql/docs/sqlserver/connect-connectors/
title: Connect using Cloud SQL Language Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:29:18.180195+00:00
---

# Connect using Cloud SQL Language Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/connect-connectors/

  * [ Guides ](https://docs.cloud.google.com/sql/docs/sqlserver/features)



#  Connect using Cloud SQL Language Connectors Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/connect-connectors "View this page for the MySQL database engine") | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/connect-connectors "View this page for the PostgreSQL database engine") | SQL Server

The Cloud SQL Connectors are libraries that provide encryption and Identity and Access Management (IAM)-based authorization when connecting to a Cloud SQL instance. They can't provide a network path to a Cloud SQL instance if one is not already present.

Other ways to connect to a Cloud SQL instance include [using a database client](https://docs.cloud.google.com/sql/docs/sqlserver/connect-admin-ip) or the [Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/sqlserver/sql-proxy). See the [About connection options](https://docs.cloud.google.com/sql/docs/sqlserver/connect-overview) page for more information about connecting to a Cloud SQL instance.

This page discusses the following Cloud SQL Connectors:

  * The Cloud SQL Java Connector 
  * The Cloud SQL Python Connector [(Open in Colab)](https://colab.research.google.com/github/GoogleCloudPlatform/cloud-sql-python-connector/blob/main/samples/notebooks/sqlserver_python_connector.ipynb)
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


For more information about creating instances, see [Create instances](https://docs.cloud.google.com/sql/docs/sqlserver/create-instance).

For more information about configuring the default user, see [Set the password for the default user account](https://docs.cloud.google.com/sql/docs/sqlserver/create-manage-users#user-root).

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



For examples of this library being used in the context of an application, check out these [sample applications](https://docs.cloud.google.com/sql/docs/sqlserver/manage-connections#java).

### Authenticate

This library uses [Application Default Credentials](https://developers.google.com/identity/protocols/application-default-credentials) to authenticate the connection to the Cloud SQL server.

To activate credentials locally, use the following [gcloud](https://cloud.google.com/sdk/gcloud/) command:
    
    
        gcloud auth application-default login
        

### Connect with Intellij

In order to [connect IntelliJ](https://jetbrains.com/help/idea/connecting-to-a-database.html#mysql) to your Cloud SQL instance, you will need to add the library as a jar with dependencies in the **Additional Files** section on the driver settings page. For example, prebuilt fat jars can be found on the [Cloud SQL Java Connector Releases](https://github.com/GoogleCloudPlatform/cloud-sql-jdbc-socket-factory/releases) page for this purpose.

### Python

The Cloud SQL Python Connector is a library that can be used alongside a database driver to allow users with sufficient permissions to connect to a Cloud SQL database without having to manually allowlist IPs or manage SSL certificates.

For interactive examples of using the Cloud SQL Python Connector, open the [Cloud SQL Python Connector notebook](https://colab.research.google.com/github/GoogleCloudPlatform/cloud-sql-python-connector/blob/main/samples/notebooks/sqlserver_python_connector.ipynb).

The driver that SQL Server supports is [pytds](https://github.com/denisenkom/pytds).

### Install

To install the latest release of the Cloud SQL Python Connector, use the `pip install` command and specify the `pytds` driver for your database:
    
    
        pip install "cloud-sql-python-connector[pytds]"
        

### Authenticate

This library uses [Application Default Credentials](https://developers.google.com/identity/protocols/application-default-credentials) to authenticate the connection to the Cloud SQL server.

To activate credentials locally, use the following [gcloud](https://cloud.google.com/sdk/gcloud/) command:
    
    
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

To see this snippet in the context of a web application, view [the README on GitHub](https://github.com/GoogleCloudPlatform/java-docs-samples/blob/master/cloud-sql/sqlserver/servlet/README.md).
    
    
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
      private static final String DB_USER = System.getenv("DB_USER");
      private static final String DB_PASS = System.getenv("DB_PASS");
      private static final String DB_NAME = System.getenv("DB_NAME");
    
      public static DataSource createConnectionPool() {
        // The configuration object specifies behaviors for the connection pool.
        HikariConfig config = new HikariConfig();
    
        // The following is equivalent to setting the config options below:
        // jdbc:sqlserver://;user=<DB_USER>;password=<DB_PASS>;databaseName=<DB_NAME>;
        // socketFactoryClass=com.google.cloud.sql.sqlserver.SocketFactory;
        // socketFactoryConstructorArg=<INSTANCE_CONNECTION_NAME>
    
        // See the link below for more info on building a JDBC URL for the Cloud SQL JDBC Socket Factory
        // https://github.com/GoogleCloudPlatform/cloud-sql-jdbc-socket-factory#creating-the-jdbc-url
    
        // Configure which instance and what database user to connect with.
        config
            .setDataSourceClassName("com.microsoft.sqlserver.jdbc.SQLServerDataSource");
        config.setUsername(DB_USER); // e.g. "root", "sqlserver"
        config.setPassword(DB_PASS); // e.g. "my-password"
        config.addDataSourceProperty("databaseName", DB_NAME);
    
        config.addDataSourceProperty("socketFactoryClass",
            "com.google.cloud.sql.sqlserver.SocketFactory");
        config.addDataSourceProperty("socketFactoryConstructorArg", INSTANCE_CONNECTION_NAME);
    
        // The Java Connector provides SSL encryption, so it should be disabled
        // at the driver level.
        config.addDataSourceProperty("encrypt", "false");
    
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

**Note:** If you set `encrypt=true` and `trustServerCertificate = false or blank`, you need to include the `CA file` for the instance. If you use Cloud SQL Auth Proxy, `hostNameInCertificate` must not be blank. 

### Python

See [ How to use this Connector](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector#how-to-use-this-connector) for detailed instructions on using the library. View example connection test code on GitHub.
    
    
    import os
    
    from google.cloud.sql.connector import Connector, IPTypes
    import pytds
    
    import sqlalchemy
    
    
    def connect_with_connector() -> sqlalchemy.engine.base.Engine:
        """
        Initializes a connection pool for a Cloud SQL instance of SQL Server.
    
        Uses the Cloud SQL Python Connector package.
        """
        # Note: Saving credentials in environment variables is convenient, but not
        # secure - consider a more secure solution such as
        # Cloud Secret Manager (https://cloud.google.com/secret-manager) to help
        # keep secrets safe.
    
        instance_connection_name = os.environ[
            "INSTANCE_CONNECTION_NAME"
        ]  # e.g. 'project:region:instance'
        db_user = os.environ.get("DB_USER", "")  # e.g. 'my-db-user'
        db_pass = os.environ["DB_PASS"]  # e.g. 'my-db-password'
        db_name = os.environ["DB_NAME"]  # e.g. 'my-database'
    
        ip_type = IPTypes.PRIVATE if os.environ.get("PRIVATE_IP") else IPTypes.PUBLIC
    
        # initialize Cloud SQL Python Connector object
        connector = Connector(ip_type=ip_type, refresh_strategy="LAZY")
    
        connect_args = {}
        # If your SQL Server instance requires SSL, you need to download the CA
        # certificate for your instance and include cafile={path to downloaded
        # certificate} and validate_host=False. This is a workaround for a known issue.
        if os.environ.get("DB_ROOT_CERT"):  # e.g. '/path/to/my/server-ca.pem'
            connect_args = {
                "cafile": os.environ["DB_ROOT_CERT"],
                "validate_host": False,
            }
    
        def getconn() -> pytds.Connection:
            conn = connector.connect(
                instance_connection_name,
                "pytds",
                user=db_user,
                password=db_pass,
                db=db_name,
                **connect_args
            )
            return conn
    
        pool = sqlalchemy.create_engine(
            "mssql+pytds://",
            creator=getconn,
            # ...
        )
        return pool
    
    

**Note:** If your instance requires SSL to connect, for `Pytds` to work, you need to include the `CA file` for the instance. If you also use Cloud SQL Auth Proxy, `validate_host` must be set to `False`. 

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
    	mssql "github.com/denisenkom/go-mssqldb"
    )
    
    type csqlDialer struct {
    	dialer     *cloudsqlconn.[Dialer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudsqlconn/latest/index.html#cloud_google_com_go_cloudsqlconn_Dialer)
    	connName   string
    	usePrivate bool
    }
    
    // DialContext adheres to the mssql.Dialer interface.
    func (c *csqlDialer) DialContext(ctx context.Context, network, addr string) (net.Conn, error) {
    	var opts []cloudsqlconn.[DialOption](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudsqlconn/latest/index.html#cloud_google_com_go_cloudsqlconn_DialOption)
    	if c.usePrivate {
    		opts = append(opts, cloudsqlconn.[WithPrivateIP](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudsqlconn/latest/index.html#cloud_google_com_go_cloudsqlconn_DialOption_WithPrivateIP)())
    	}
    	return c.dialer.[Dial](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudsqlconn/latest/index.html#cloud_google_com_go_cloudsqlconn_Dialer_Dial)(ctx, c.connName, opts...)
    }
    
    func connectWithConnector() (*sql.DB, error) {
    	mustGetenv := func(k string) string {
    		v := os.Getenv(k)
    		if v == "" {
    			log.Fatalf("Fatal Error in connect_connector.go: %s environment variable not set.\n", k)
    		}
    		return v
    	}
    	// Note: Saving credentials in environment variables is convenient, but not
    	// secure - consider a more secure solution such as
    	// Cloud Secret Manager (https://cloud.google.com/secret-manager) to help
    	// keep secrets safe.
    	var (
    		dbUser                 = mustGetenv("DB_USER")                  // e.g. 'my-db-user'
    		dbPwd                  = mustGetenv("DB_PASS")                  // e.g. 'my-db-password'
    		dbName                 = mustGetenv("DB_NAME")                  // e.g. 'my-database'
    		instanceConnectionName = mustGetenv("INSTANCE_CONNECTION_NAME") // e.g. 'project:region:instance'
    		usePrivate             = os.Getenv("PRIVATE_IP")
    	)
    
    	dbURI := fmt.Sprintf("user id=%s;password=%s;database=%s;", dbUser, dbPwd, dbName)
    	c, err := mssql.NewConnector(dbURI)
    	if err != nil {
    		return nil, fmt.Errorf("mssql.NewConnector: %w", err)
    	}
    	// WithLazyRefresh() Option is used to perform refresh
    	// when needed, rather than on a scheduled interval.
    	// This is recommended for serverless environments to
    	// avoid background refreshes from throttling CPU.
    	dialer, err := cloudsqlconn.[NewDialer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudsqlconn/latest/index.html#cloud_google_com_go_cloudsqlconn_Dialer_NewDialer)(context.Background(), cloudsqlconn.[WithLazyRefresh](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudsqlconn/latest/index.html#cloud_google_com_go_cloudsqlconn_Option_WithLazyRefresh)())
    	if err != nil {
    		return nil, fmt.Errorf("cloudsqlconn.NewDailer: %w", err)
    	}
    	c.[Dialer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudsqlconn/latest/index.html#cloud_google_com_go_cloudsqlconn_Dialer) = &csqlDialer{
    		dialer:     dialer,
    		connName:   instanceConnectionName,
    		usePrivate: usePrivate != "",
    	}
    
    	dbPool := sql.OpenDB(c)
    	if err != nil {
    		return nil, fmt.Errorf("sql.Open: %w", err)
    	}
    	return dbPool, nil
    }
    

**Note:** If your instance requires SSL to connect, for `Pytds` to work, you need to include the `CA file` for the instance. If you also use Cloud SQL Auth Proxy, `validate_host` must be set to `False`. 

### Node.js

For detailed instructions on using the library, see [ Usage](https://github.com/GoogleCloudPlatform/cloud-sql-nodejs-connector#usage).
    
    
    const {Connection} = require('tedious');
    const {Connector} = require('@google-cloud/cloud-sql-connector');
    
    // In case the PRIVATE_IP environment variable is defined then we set
    // the ipType=PRIVATE for the new connector instance, otherwise defaults
    // to public ip type.
    const getIpType = () =>
      process.env.PRIVATE_IP === '1' || process.env.PRIVATE_IP === 'true'
        ? 'PRIVATE'
        : 'PUBLIC';
    
    // connectWithConnector initializes a TCP connection
    // to a Cloud SQL instance of SQL Server.
    const connectWithConnector = async config => {
      // Note: Saving credentials in environment variables is convenient, but not
      // secure - consider a more secure solution such as
      // Cloud Secret Manager (https://cloud.google.com/secret-manager) to help
      // keep secrets safe.
      const connector = new Connector();
      const clientOpts = await connector.getTediousOptions({
        instanceConnectionName: process.env.INSTANCE_CONNECTION_NAME,
        ipType: getIpType(),
      });
      const dbConfig = {
        // Please note that the `server` property here is not used and is only
        // defined due to a bug in the tedious driver
        // (ref: https://github.com/tediousjs/tedious/issues/1541)
        // With that in mind, do not try to change this value since it will have no
        // impact in how the connector works, this sample will be updated to remove
        // this property declaration as soon as the tedious driver bug is fixed
        server: '0.0.0.0', // e.g. '127.0.0.1'
        authentication: {
          type: 'default',
          options: {
            userName: process.env.DB_USER, // e.g. 'my-db-user'
            password: process.env.DB_PASS, // e.g. 'my-db-password'
          },
        },
        options: {
          ...clientOpts,
          // Please note that the `port` property here is not used and is only
          // defined due to a bug in the tedious driver
          // (ref: https://github.com/tediousjs/tedious/issues/1541)
          // With that in mind, do not try to change this value since it will have
          // no impact in how the connector works, this sample will be updated to
          // remove this property declaration as soon as the tedious driver bug is
          // fixed
          port: 9999,
          database: process.env.DB_NAME, // e.g. 'my-database'
          useColumnNames: true,
        },
        // ... Specify additional properties here.
        ...config,
      };
    
      // Establish a connection to the database.
      return new Connection(dbConfig);
    };

## Enforce

By using [connector enforcement](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1/instances#ConnectorEnforcement), you can enforce using only the Cloud SQL Auth Proxy or Cloud SQL Language Connectors to connect to Cloud SQL instances. With connector enforcement, Cloud SQL rejects direct connections to the database.

If you're using a [Private Service Connect-enabled instance](https://docs.cloud.google.com/sql/docs/sqlserver/about-private-service-connect), then there's a limitation. If the instance has connector enforcement enabled, then you can't create read replicas for the instance. Similarly, if the instance has read replicas, then you can't enable connector enforcement for the instance.

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

For additional help with connection issues, see the [Troubleshoot](https://docs.cloud.google.com/sql/docs/sqlserver/troubleshooting#connectivity) and [Debug connection issues](https://docs.cloud.google.com/sql/docs/sqlserver/debugging-connectivity) pages.

## What's next

  * See the [Cloud SQL Java Connector home page on GitHub](https://github.com/GoogleCloudPlatform/cloud-sql-jdbc-socket-factory).
  * See the [Cloud SQL Python Connector home page on GitHub](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector).
  * Learn more about the [Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/sqlserver/sql-proxy).
  * Learn more about [IAM](https://docs.cloud.google.com/iam/docs/overview).
  * Learn about [options for support](https://docs.cloud.google.com/sql/docs/support).



Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
