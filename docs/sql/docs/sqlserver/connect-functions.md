---
url: https://docs.cloud.google.com/sql/docs/sqlserver/connect-functions/
title: Connect from Cloud Run functions \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:30:26.619922+00:00
---

# Connect from Cloud Run functions  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/connect-functions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/sqlserver/features)



Send feedback 

#  Connect from Cloud Run functions Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/connect-functions "View this page for the MySQL database engine") | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/connect-functions "View this page for the PostgreSQL database engine") | SQL Server

This page contains information and examples for connecting to a Cloud SQL instance from a service running in Cloud Run functions. 

**For step-by-step instructions on running a Cloud Run functions sample web application connected to Cloud SQL,** see the [quickstart for connecting from Cloud Run functions](https://docs.cloud.google.com/sql/docs/sqlserver/connect-instance-cloud-functions).

Cloud SQL is a fully-managed database service that helps you set up, maintain, manage, and administer your relational databases in the cloud.

[Cloud Run functions](https://docs.cloud.google.com/functions/docs/concepts/overview) is a lightweight compute solution for developers to create single-purpose, standalone functions that respond to Cloud events without the need to manage a server or runtime environment.

## Set up a Cloud SQL instance

  1. Enable the Cloud SQL Admin API in the Google Cloud project that you are connecting from, if you haven't already done so: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=sqladmin&redirect=https%3A//console.cloud.google.com)

  2. [Create a Cloud SQL for SQL Server instance](https://docs.cloud.google.com/sql/docs/sqlserver/create-instance). We recommend that you choose a Cloud SQL [ instance location](https://docs.cloud.google.com/sql/docs/sqlserver/locations) in the same region as your Cloud Run functions service for better latency, to avoid some networking costs, and to reduce cross region failure risks. 

By default, Cloud SQL assigns a public IP address to a new instance. You also have the option to assign a private IP address. For more information about the connectivity options for both, see the [ Connecting Overview](https://docs.cloud.google.com/sql/docs/sqlserver/connect-overview) page.

  3. When you create the instance, you can choose the [ server certificate (CA) hierarchy](https://docs.cloud.google.com/sql/docs/mysql/authorize-ssl#ca-hierarchies) for the instance and then configure the hierarchy as the `serverCaMode` for the instance. You must select the per-instance CA option (`GOOGLE_MANAGED_INTERNAL_CA`) as the server CA mode for instances that you want to connect to from web applications. 



## Configure Cloud Run functions

The steps to configure Cloud Run functions depend on the type of IP address that you assigned to your Cloud SQL instance. 

### Public IP (default)

Cloud Run functions supports connecting to Cloud SQL for SQL Server over public IP using the [Go, Java and Python connectors](https://docs.cloud.google.com/sql/docs/sqlserver/connect-connectors). 

To configure Cloud Run functions to enable connections to a Cloud SQL instance: 

  * Confirm that the instance created above has a public IP address. You can confirm this on the **Overview** page for the instance in the [Google Cloud console](https://console.cloud.google.com/sql). If you need to add a public IP address, see [Configure public IP](https://docs.cloud.google.com/sql/docs/sqlserver/configure-ip). 
  * Get the instance's INSTANCE_CONNECTION_NAME. This value is available: 
    * On the **Overview** page for the instance, in the [Google Cloud console](https://console.cloud.google.com/sql), or
    * By running the following command: `gcloud sql instances describe [INSTANCE_NAME]`
  * [ Configure the service account](https://docs.cloud.google.com/functions/docs/securing/function-identity) for your function. If the authorizing service account belongs to a different project from the Cloud SQL instance, then you must enable the Cloud SQL Admin API, and add the `Cloud SQL Client` [IAM role](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql) to both projects.
  * Confirm that the service account has this role so that the account can connect to Cloud SQL.
  * If you're using [ Cloud Run functions and not Cloud Run functions (1st gen)](https://docs.cloud.google.com/functions/docs/concepts/version-comparison), the following are required (also see [ Configure Cloud Run](https://docs.cloud.google.com/sql/docs/sqlserver/connect-run#configure)): 
    1. Initially deploy your function.  
When you first begin creating a Cloud Run function in the Google Cloud console, the underlying Cloud Run service hasn't been created yet. You can't configure a Cloud SQL connection until that service is created (by deploying the Cloud Run function). 
    2. In the Google Cloud console, in the upper right of the **Function details** page, under **Powered by Cloud Run** , click the link to access the underlying Cloud Run service.
    3. On the Cloud Run **Service details** page, select the **Edit and deploy new revision** tab. 
    4. Follow the [standard steps](https://docs.cloud.google.com/sql/docs/sqlserver/connect-run#create-deploy) (as in the case of any configuration change) for setting a new configuration for a Cloud SQL connection.   
This creates a new Cloud Run revision, and subsequent revisions automatically receive this Cloud SQL connection, unless you explicitly change it.



### Private IP

If the authorizing service account belongs to a different project than the one containing the Cloud SQL instance, do the following: 

  * In both projects, enable the Cloud SQL Admin API.
  * For the service account in the project that contains the Cloud SQL instance, add the [IAM permissions](https://docs.cloud.google.com/sql/docs/mysql/roles-and-permissions#serverless-roles-permissions).

A Serverless VPC Access connector uses private IP addresses to handle communication to your VPC network. To connect directly with private IP addresses, you must do the following: 
  1. Make sure that the Cloud SQL instance created previously has a private IP address. If you need to add one, see [Configure private IP](https://docs.cloud.google.com/sql/docs/sqlserver/configure-private-ip) for instructions.
  2. [Create](https://docs.cloud.google.com/vpc/docs/configure-serverless-vpc-access#creating_a_connector) a Serverless VPC Access connector in the same VPC network as your Cloud SQL instance. Note the following conditions:
     * Unless you're using [ Shared VPC](https://docs.cloud.google.com/vpc/docs/configure-serverless-vpc-access#shared-vpc), your connector must be in the same project and region as the resource that uses it, but it can send traffic to resources in different regions.
     * Serverless VPC Access supports communication to VPC networks connected using [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn) and [VPC Network Peering](https://docs.cloud.google.com/vpc/docs/using-vpc-peering).
     * Serverless VPC Access doesn't support [legacy networks](https://docs.cloud.google.com/vpc/docs/legacy).
  3. Configure Cloud Run functions to use the connector.
  4. Connect using your instance's private IP address and port `1433`.



## Connect to Cloud SQL

After you configure Cloud Run functions, you can connect to your Cloud SQL instance.

### Public IP (default)

For public IP paths, Cloud Run functions provides encryption and connects using the Cloud SQL connectors. 

### Connect with Cloud SQL connectors

The [Cloud SQL connectors](https://docs.cloud.google.com/sql/docs/sqlserver/connect-connectors) are language specific libraries that provide encryption and IAM-based authorization when connecting to a Cloud SQL instance. 

### Python

To see this snippet in the context of a web application, view [the README on GitHub](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/master/cloud-sql/sql-server/sqlalchemy/README.md).
    
    
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
    
    

### Java

To see this snippet in the context of a web application, view [the README on GitHub](https://github.com/GoogleCloudPlatform/java-docs-samples/blob/master/cloud-sql/sqlserver/servlet/README.md).

Note: 

  * CLOUD_SQL_CONNECTION_NAME should be represented as <MY-PROJECT>:<INSTANCE-REGION>:<INSTANCE-NAME>
  * See the JDBC socket factory version requirements for the pom.xml file [ here ](https://github.com/GoogleCloudPlatform/cloud-sql-jdbc-socket-factory/blob/main/docs/jdbc.md). 


    
    
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

### Go

To see this snippet in the context of a web application, view [the README on GitHub](https://github.com/GoogleCloudPlatform/golang-samples/tree/master/cloudsql/sqlserver/database-sql/README.md).
    
    
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
    

### Node.js

To see this snippet in the context of a web application, view [the README on GitHub](https://github.com/GoogleCloudPlatform/nodejs-docs-samples/blob/main/cloud-sql/sqlserver/tedious/README.md).
    
    
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

### Private IP

For private IP paths, your application connects directly to your instance through a VPC network. This method uses TCP to connect directly to the Cloud SQL instance without using the Cloud SQL Auth Proxy. 

### Connect with TCP

Connect using the private IP address of your Cloud SQL instance as the host and port `1433`.

### Python

To see this snippet in the context of a web application, view [the README on GitHub](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/master/cloud-sql/sql-server/sqlalchemy/README.md).
    
    
    import os
    
    import sqlalchemy
    
    
    def connect_tcp_socket() -> sqlalchemy.engine.base.Engine:
        """Initializes a TCP connection pool for a Cloud SQL instance of SQL Server."""
        # Note: Saving credentials in environment variables is convenient, but not
        # secure - consider a more secure solution such as
        # Cloud Secret Manager (https://cloud.google.com/secret-manager) to help
        # keep secrets safe.
        db_host = os.environ[
            "INSTANCE_HOST"
        ]  # e.g. '127.0.0.1' ('172.17.0.1' if deployed to GAE Flex)
        db_user = os.environ["DB_USER"]  # e.g. 'my-db-user'
        db_pass = os.environ["DB_PASS"]  # e.g. 'my-db-password'
        db_name = os.environ["DB_NAME"]  # e.g. 'my-database'
        db_port = os.environ["DB_PORT"]  # e.g. 1433
    
        pool = sqlalchemy.create_engine(
            # Equivalent URL:
            # mssql+pytds://<db_user>:<db_pass>@<db_host>:<db_port>/<db_name>
            sqlalchemy.engine.url.URL.create(
                drivername="mssql+pytds",
                username=db_user,
                password=db_pass,
                database=db_name,
                host=db_host,
                port=db_port,
            ),
            # ...
        )
    
        return pool
    
    

### Java

To see this snippet in the context of a web application, view [the README on GitHub](https://github.com/GoogleCloudPlatform/java-docs-samples/blob/master/cloud-sql/sqlserver/servlet/README.md).

Note: 

  * CLOUD_SQL_CONNECTION_NAME should be represented as <MY-PROJECT>:<INSTANCE-REGION>:<INSTANCE-NAME>
  * Using the argument ipTypes=PRIVATE will force the SocketFactory to connect with an instance's associated private IP
  * See the [JDBC socket factory version requirements for the pom.xml file](https://github.com/GoogleCloudPlatform/cloud-sql-jdbc-socket-factory/blob/main/docs/jdbc.md). 


    
    
    import com.zaxxer.hikari.HikariConfig;
    import com.zaxxer.hikari.HikariDataSource;
    import javax.sql.DataSource;
    
    public class TcpConnectionPoolFactory extends ConnectionPoolFactory {
    
      // Note: Saving credentials in environment variables is convenient, but not
      // secure - consider a more secure solution such as
      // Cloud Secret Manager (https://cloud.google.com/secret-manager) to help
      // keep secrets safe.
      private static final String DB_USER = System.getenv("DB_USER");
      private static final String DB_PASS = System.getenv("DB_PASS");
      private static final String DB_NAME = System.getenv("DB_NAME");
    
      private static final String INSTANCE_HOST = System.getenv("INSTANCE_HOST");
      private static final String DB_PORT = System.getenv("DB_PORT");
    
    
      public static DataSource createConnectionPool() {
        // The configuration object specifies behaviors for the connection pool.
        HikariConfig config = new HikariConfig();
    
        // Configure which instance and what database user to connect with.
        config.setJdbcUrl(
            String.format("jdbc:sqlserver://%s:%s;databaseName=%s", INSTANCE_HOST, DB_PORT, DB_NAME));
        config.setUsername(DB_USER); // e.g. "root", "sqlserver"
        config.setPassword(DB_PASS); // e.g. "my-password"
    
    
        // ... Specify additional connection properties here.
        // ...
    
        // Initialize the connection pool using the configuration object.
        return new HikariDataSource(config);
      }
    }

### Node.js

To see this snippet in the context of a web application, view [the README on GitHub](https://github.com/GoogleCloudPlatform/nodejs-docs-samples/blob/master/cloud-sql/sqlserver/mssql/README.md).
    
    
    const mssql = require('mssql');
    
    // createTcpPool initializes a TCP connection pool for a Cloud SQL
    // instance of SQL Server.
    const createTcpPool = async config => {
      // Note: Saving credentials in environment variables is convenient, but not
      // secure - consider a more secure solution such as
      // Cloud Secret Manager (https://cloud.google.com/secret-manager) to help
      // keep secrets safe.
      const dbConfig = {
        server: process.env.INSTANCE_HOST, // e.g. '127.0.0.1'
        port: parseInt(process.env.DB_PORT), // e.g. 1433
        user: process.env.DB_USER, // e.g. 'my-db-user'
        password: process.env.DB_PASS, // e.g. 'my-db-password'
        database: process.env.DB_NAME, // e.g. 'my-database'
        options: {
          trustServerCertificate: true,
        },
        // ... Specify additional properties here.
        ...config,
      };
      // Establish a connection to the database.
      return mssql.connect(dbConfig);
    };

### Go

To see this snippet in the context of a web application, view [the README on GitHub](https://github.com/GoogleCloudPlatform/golang-samples/tree/master/cloudsql/sqlserver/database-sql/README.md).
    
    
    package cloudsql
    
    import (
    	"database/sql"
    	"fmt"
    	"log"
    	"os"
    	"strings"
    
    	_ "github.com/denisenkom/go-mssqldb"
    )
    
    // connectTCPSocket initializes a TCP connection pool for a Cloud SQL
    // instance of SQL Server.
    func connectTCPSocket() (*sql.DB, error) {
    	mustGetenv := func(k string) string {
    		v := os.Getenv(k)
    		if v == "" {
    			log.Fatalf("Fatal Error in connect_tcp.go: %s environment variable not set.\n", k)
    		}
    		return v
    	}
    	// Note: Saving credentials in environment variables is convenient, but not
    	// secure - consider a more secure solution such as
    	// Cloud Secret Manager (https://cloud.google.com/secret-manager) to help
    	// keep secrets safe.
    	var (
    		dbUser    = mustGetenv("DB_USER")       // e.g. 'my-db-user'
    		dbPwd     = mustGetenv("DB_PASS")       // e.g. 'my-db-password'
    		dbTCPHost = mustGetenv("INSTANCE_HOST") // e.g. '127.0.0.1' ('172.17.0.1' if deployed to GAE Flex)
    		dbPort    = mustGetenv("DB_PORT")       // e.g. '1433'
    		dbName    = mustGetenv("DB_NAME")       // e.g. 'my-database'
    	)
    
    	dbURI := fmt.Sprintf("server=%s;user id=%s;password=%s;port=%s;database=%s;",
    		dbTCPHost, dbUser, dbPwd, dbPort, dbName)
    
    
    	// dbPool is the pool of database connections.
    	dbPool, err := sql.Open("sqlserver", dbURI)
    	if err != nil {
    		return nil, fmt.Errorf("sql.Open: %w", err)
    	}
    
    	// ...
    
    	return dbPool, nil
    }
    

### PHP

To see this snippet in the context of a web application, view [the README on GitHub](https://github.com/GoogleCloudPlatform/php-docs-samples/tree/main/cloud_sql/sqlserver/pdo/README.md).
    
    
    namespace Google\Cloud\Samples\CloudSQL\SQLServer;
    
    use PDO;
    use PDOException;
    use RuntimeException;
    use TypeError;
    
    class DatabaseTcp
    {
        public static function initTcpDatabaseConnection(): PDO
        {
            try {
                // Note: Saving credentials in environment variables is convenient, but not
                // secure - consider a more secure solution such as
                // Cloud Secret Manager (https://cloud.google.com/secret-manager) to help
                // keep secrets safe.
                $username = getenv('DB_USER'); // e.g. 'your_db_user'
                $password = getenv('DB_PASS'); // e.g. 'your_db_password'
                $dbName = getenv('DB_NAME'); // e.g. 'your_db_name'
                $instanceHost = getenv('INSTANCE_HOST'); // e.g. '127.0.0.1' ('172.17.0.1' for GAE Flex)
    
                // Connect using TCP
                $dsn = sprintf(
                    'sqlsrv:server=%s;Database=%s',
                    $instanceHost,
                    $dbName
                );
    
                // Connect to the database
                $conn = new PDO(
                    $dsn,
                    $username,
                    $password,
                    # ...
                );
            } catch (TypeError $e) {
                throw new RuntimeException(
                    sprintf(
                        'Invalid or missing configuration! Make sure you have set ' .
                            '$username, $password, $dbName, and $instanceHost (for TCP mode). ' .
                            'The PHP error was %s',
                        $e->getMessage()
                    ),
                    $e->getCode(),
                    $e
                );
            } catch (PDOException $e) {
                throw new RuntimeException(
                    sprintf(
                        'Could not connect to the Cloud SQL Database. Check that ' .
                            'your username and password are correct, that the Cloud SQL ' .
                            'proxy is running, and that the database exists and is ready ' .
                            'for use. For more assistance, refer to %s. The PDO error was %s',
                        'https://cloud.google.com/sql/docs/sqlserver/connect-external-app',
                        $e->getMessage()
                    ),
                    (int) $e->getCode(),
                    $e
                );
            }
    
            return $conn;
        }
    }

## Best practices and other information

You can use the [Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/sqlserver/sql-proxy) when testing your application locally. See the [quickstart for using the Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/mysql/connect-instance-auth-proxy) for detailed instructions.

### Connection Pools

Connections to underlying databases may be dropped, either by the database server itself, or by the infrastructure underlying Cloud Run functions. We recommend using a client library that supports connection pools that automatically reconnect broken client connections. Additionally, we recommend using a globally scoped connection pool to increase the likelihood that your function reuses the same connection for subsequent invocations of the function, and closes the connection naturally when the instance is evicted (auto-scaled down). For more detailed examples on how to use connection pools, see [Managing database connections](https://docs.cloud.google.com/sql/docs/sqlserver/manage-connections). 

### Connection Limits

Cloud SQL imposes a maximum limit on concurrent connections, and these limits may vary depending on the database engine chosen (see [Cloud SQL Quotas and Limits](https://docs.cloud.google.com/sql/docs/quotas#fixed-limits)).

It's recommended to use a connection pool with Cloud Run functions but it is important to set the maximum number of connections to 1.

Note: Cloud Run functions limits concurrent executions to one per instance. You never have a situation where a single function instance is processing two requests at the same time. In most situations, only a single database connection is needed.

Where possible, you should take care to only initialize a connection pool for functions that need access to your database. Some connection pools will create connections preemptively, which can consume excess resources and count towards your connection limits. For this reason, it's recommended to use [ Lazy Initialization](https://docs.cloud.google.com/functions/docs/bestpractices/tips#do_lazy_initialization_of_global_variables) to delay the creation of a connection pool until needed, and only include the connection pool in functions where it's used.

For more detailed examples on how to limit the number of connections, see [Managing database connections](https://docs.cloud.google.com/sql/docs/sqlserver/manage-connections#count).

### API Quota Limits

Cloud Run functions provides a mechanism that connects using the Cloud SQL Auth Proxy, which uses the Cloud SQL Admin API. [ API quota limits](https://console.cloud.google.com/iam-admin/quotas?service=sqladmin.googleapis.com) apply to the Cloud SQL Auth Proxy. The Cloud SQL Admin API quota used is approximately two times the number of Cloud SQL instances configured times the total number of functions deployed. You can [set the number of max concurrent invocations](https://docs.cloud.google.com/functions/quotas#additional_quotas_for_background_functions) to modify the expected API quota consumed. Cloud Run functions also imposes [rate limits](https://docs.cloud.google.com/functions/quotas#rate_limits) on the number of API calls allowed per 100 seconds.

## What's next

  * Learn more about [Cloud Run functions](https://docs.cloud.google.com/functions/docs).
  * Learn more about [deploying Cloud Run functions](https://docs.cloud.google.com/functions/docs/deploy).
  * Learn more about [specifying triggers for Cloud Run functions](https://docs.cloud.google.com/functions/docs/calling).
  * Learn more about [configuring Cloud Run functions](https://docs.cloud.google.com/functions/docs/configuring).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
