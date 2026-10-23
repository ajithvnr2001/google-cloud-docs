---
url: https://docs.cloud.google.com/sql/docs/postgres/connect-app-engine-standard/
title: Connect from App Engine standard environment \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:12:15.090906+00:00
---

# Connect from App Engine standard environment  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/connect-app-engine-standard/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/postgres/features)



Send feedback 

#  Connect from App Engine standard environment Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/connect-app-engine-standard "View this page for the MySQL database engine") | PostgreSQL | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/connect-app-engine-standard "View this page for the SQL Server database engine")

This page contains information and examples for connecting to a Cloud SQL instance from a service running in the App Engine standard environment.

Cloud SQL is a fully-managed database service that helps you set up, maintain, manage, and administer your relational databases in the cloud.

App Engine is a fully managed, serverless platform for developing and hosting web applications at scale. You can choose from several popular languages, libraries, and frameworks to develop your apps, then let App Engine take care of provisioning servers and scaling your app instances based on demand.

## Set up a Cloud SQL instance

  1. Enable the Cloud SQL Admin API in the Google Cloud project that you are connecting from, if you haven't already done so: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=sqladmin&redirect=https%3A//console.cloud.google.com)

  2. [Create a Cloud SQL for PostgreSQL instance](https://docs.cloud.google.com/sql/docs/postgres/create-instance). We recommend that you choose a Cloud SQL [ instance location](https://docs.cloud.google.com/sql/docs/postgres/locations) in the same region as your App Engine standard environment service for better latency, to avoid some networking costs, and to reduce cross region failure risks. 

By default, Cloud SQL assigns a public IP address to a new instance. You also have the option to assign a private IP address. For more information about the connectivity options for both, see the [ Connecting Overview](https://docs.cloud.google.com/sql/docs/postgres/connect-overview) page.

  3. When you create the instance, you can choose the [ server certificate (CA) hierarchy](https://docs.cloud.google.com/sql/docs/mysql/authorize-ssl#ca-hierarchies) for the instance and then configure the hierarchy as the `serverCaMode` for the instance. You must select the per-instance CA option (`GOOGLE_MANAGED_INTERNAL_CA`) as the server CA mode for instances that you want to connect to from App Engine standard environment web applications. 



## Configure App Engine standard environment

The steps to configure App Engine standard environment depend on the type of IP address that you assigned to your Cloud SQL instance. 

### Public IP (default)

To configure App Engine standard environment to enable connections to a Cloud SQL instance using public IP: 

  * Make sure that the instance has a public IP address. You can verify this on the **Overview** page for your instance in the [Google Cloud console](https://console.cloud.google.com/sql). If you need to add one, see the [Configuring public IP page](https://docs.cloud.google.com/sql/docs/postgres/configure-ip) for instructions.
  * Get the INSTANCE_CONNECTION_NAME for your instance. You can find this value on the **Overview** page for your instance in the [Google Cloud console](https://console.cloud.google.com/sql) or by running the following `[gcloud sql instances describe](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/describe)` command: 
        
        gcloud sql instances describe INSTANCE_NAME
           

Replace INSTANCE_NAME with the name of your Cloud SQL instance.
Replace the INSTANCE_NAME variable with the name of your instance. 
  * Ensure that the service account your app is using to authenticate calls to Cloud SQL has the `Cloud SQL Client` [IAM role](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql).

For detailed instructions on adding IAM roles to a service account, see [Granting Roles to Service Accounts](https://docs.cloud.google.com/iam/docs/granting-roles-to-service-accounts).




The [default App Engine service account](https://docs.cloud.google.com/appengine/docs/standard/configure-service-accounts#default-service-account) is automatically created when you use App Engine. The service account identity is in the format `PROJECT_ID@appspot.gserviceaccount.com`.

If the authorizing service account belongs to a different project than the Cloud SQL instance, the Cloud SQL Admin API and IAM permissions will need to be added for both projects.

### Private IP

If the authorizing service account belongs to a different project than the one containing the Cloud SQL instance, do the following: 

  * In both projects, enable the Cloud SQL Admin API.
  * For the service account in the project that contains the Cloud SQL instance, add the [IAM permissions](https://docs.cloud.google.com/sql/docs/mysql/roles-and-permissions#serverless-roles-permissions).

A Serverless VPC Access connector uses private IP addresses to handle communication to your VPC network. To connect directly with private IP addresses, you must do the following: 
  1. Make sure that the Cloud SQL instance created previously has a private IP address. If you need to add one, see [Configure private IP](https://docs.cloud.google.com/sql/docs/postgres/configure-private-ip) for instructions.
  2. [Create](https://docs.cloud.google.com/vpc/docs/configure-serverless-vpc-access#creating_a_connector) a Serverless VPC Access connector in the same VPC network as your Cloud SQL instance. Note the following conditions:
     * Unless you're using [ Shared VPC](https://docs.cloud.google.com/vpc/docs/configure-serverless-vpc-access#shared-vpc), your connector must be in the same project and region as the resource that uses it, but it can send traffic to resources in different regions.
     * Serverless VPC Access supports communication to VPC networks connected using [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn) and [VPC Network Peering](https://docs.cloud.google.com/vpc/docs/using-vpc-peering).
     * Serverless VPC Access doesn't support [legacy networks](https://docs.cloud.google.com/vpc/docs/legacy).
  3. Configure App Engine standard environment to use the connector.
  4. Connect using your instance's private IP address and port `5432`.



## Connect to Cloud SQL

After you configure App Engine standard environment, you can connect to your Cloud SQL instance.

### Public IP (default)

For public IP paths, App Engine standard environment can be set up to use the [Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/postgres/sql-proxy) for encryption in two ways: 

  * Through Unix sockets
  * By using a Cloud SQL connector



### Connect with Unix sockets

Once correctly configured, you can connect your service to your Cloud SQL instance's Unix domain socket accessed on the environment's filesystem at the following path: `/cloudsql/INSTANCE_CONNECTION_NAME`.

The INSTANCE_CONNECTION_NAME uses the format `project:region:instance-id`. You can find it on the **Overview** page for your instance in the [Google Cloud console](https://console.cloud.google.com/sql) or by running the following command:

`gcloud sql instances describe [INSTANCE_NAME]`

These connections are automatically encrypted without any additional configuration.

The code samples shown below are extracts from more complete examples on the GitHub site. Click `View on GitHub` to see more.

**Note:** The PostgreSQL standard requires a `.s.PGSQL.5432` suffix in the socket path. Some libraries apply this suffix automatically, but others require you to specify the socket path as follows: 
    
    
    /cloudsql/INSTANCE_CONNECTION_NAME/.s.PGSQL.5432

**Warning:** Linux-based operating systems have a maximum socket path length of 108 characters. If the total length of the path exceeds this length, you cannot connect with a socket from App Engine standard environment. 

### Python

To see this snippet in the context of a web application, view [the README on GitHub](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/master/cloud-sql/postgres/sqlalchemy/README.md).
    
    
    import os
    
    import sqlalchemy
    
    
    def connect_unix_socket() -> sqlalchemy.engine.base.Engine:
        """Initializes a Unix socket connection pool for a Cloud SQL instance of Postgres."""
        # Note: Saving credentials in environment variables is convenient, but not
        # secure - consider a more secure solution such as
        # Cloud Secret Manager (https://cloud.google.com/secret-manager) to help
        # keep secrets safe.
        db_user = os.environ["DB_USER"]  # e.g. 'my-database-user'
        db_pass = os.environ["DB_PASS"]  # e.g. 'my-database-password'
        db_name = os.environ["DB_NAME"]  # e.g. 'my-database'
        unix_socket_path = os.environ[
            "INSTANCE_UNIX_SOCKET"
        ]  # e.g. '/cloudsql/project:region:instance'
    
        pool = sqlalchemy.create_engine(
            # Equivalent URL:
            # postgresql+pg8000://<db_user>:<db_pass>@/<db_name>
            #                         ?unix_sock=<INSTANCE_UNIX_SOCKET>/.s.PGSQL.5432
            # Note: Some drivers require the `unix_sock` query parameter to use a different key.
            # For example, 'psycopg2' uses the path set to `host` in order to connect successfully.
            sqlalchemy.engine.url.URL.create(
                drivername="postgresql+pg8000",
                username=db_user,
                password=db_pass,
                database=db_name,
                query={"unix_sock": f"{unix_socket_path}/.s.PGSQL.5432"},
            ),
            # ...
        )
        return pool
    
    

### Java

To see this snippet in the context of a web application, view [the README on GitHub](https://github.com/GoogleCloudPlatform/java-docs-samples/blob/master/cloud-sql/postgres/servlet/README.md).
    
    
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
        // jdbc:postgresql:///<DB_NAME>?cloudSqlInstance=<INSTANCE_CONNECTION_NAME>&
        // socketFactory=com.google.cloud.sql.postgres.SocketFactory&user=<DB_USER>&password=<DB_PASS>
        // See the link below for more info on building a JDBC URL for the Cloud SQL JDBC Socket Factory
        // https://github.com/GoogleCloudPlatform/cloud-sql-jdbc-socket-factory#creating-the-jdbc-url
    
        // Configure which instance and what database user to connect with.
        config.setJdbcUrl(String.format("jdbc:postgresql:///%s", DB_NAME));
        config.setUsername(DB_USER); // e.g. "root", _postgres"
        config.setPassword(DB_PASS); // e.g. "my-password"
    
        config.addDataSourceProperty("socketFactory", "com.google.cloud.sql.postgres.SocketFactory");
        config.addDataSourceProperty("cloudSqlInstance", INSTANCE_CONNECTION_NAME);
    
        // Unix sockets are not natively supported in Java, so it is necessary to use the Cloud SQL
        // Java Connector to connect. When setting INSTANCE_UNIX_SOCKET, the connector will 
        // call an external package that will enable Unix socket connections.
        // Note: For Java users, the Cloud SQL Java Connector can provide authenticated connections
        // which is usually preferable to using the Cloud SQL Proxy with Unix sockets.
        // See https://github.com/GoogleCloudPlatform/cloud-sql-jdbc-socket-factory for details.
        if (INSTANCE_UNIX_SOCKET != null) {
          config.addDataSourceProperty("unixSocketPath", INSTANCE_UNIX_SOCKET);
        }
    
    
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

### Node.js

To see this snippet in the context of a web application, view [the README on GitHub](https://github.com/GoogleCloudPlatform/nodejs-docs-samples/blob/master/cloud-sql/postgres/knex/README.md).
    
    
    const Knex = require('knex');
    
    // createUnixSocketPool initializes a Unix socket connection pool for
    // a Cloud SQL instance of Postgres.
    const createUnixSocketPool = async config => {
      // Note: Saving credentials in environment variables is convenient, but not
      // secure - consider a more secure solution such as
      // Cloud Secret Manager (https://cloud.google.com/secret-manager) to help
      // keep secrets safe.
      return Knex({
        client: 'pg',
        connection: {
          user: process.env.DB_USER, // e.g. 'my-user'
          password: process.env.DB_PASS, // e.g. 'my-user-password'
          database: process.env.DB_NAME, // e.g. 'my-database'
          host: process.env.INSTANCE_UNIX_SOCKET, // e.g. '/cloudsql/project:region:instance'
        },
        // ... Specify additional properties here.
        ...config,
      });
    };

### C#

To see this snippet in the context of a web application, view [the README on GitHub](https://github.com/GoogleCloudPlatform/dotnet-docs-samples/blob/master/cloud-sql/postgres/README.md).
    
    
    using Npgsql;
    using System;
    
    namespace CloudSql
    {
        public class PostgreSqlUnix
        {
            public static NpgsqlConnectionStringBuilder NewPostgreSqlUnixSocketConnectionString()
            {
                // Equivalent connection string:
                // "Server=<INSTANCE_UNIX_SOCKET>;Uid=<DB_USER>;Pwd=<DB_PASS>;Database=<DB_NAME>"
                var connectionString = new NpgsqlConnectionStringBuilder()
                {
                    // The Cloud SQL proxy provides encryption between the proxy and instance.
                    SslMode = SslMode.Disable,
    
                    // Note: Saving credentials in environment variables is convenient, but not
                    // secure - consider a more secure solution such as
                    // Cloud Secret Manager (https://cloud.google.com/secret-manager) to help
                    // keep secrets safe.
                    Host = Environment.GetEnvironmentVariable("INSTANCE_UNIX_SOCKET"), // e.g. '/cloudsql/project:region:instance'
                    Username = Environment.GetEnvironmentVariable("DB_USER"), // e.g. 'my-db-user
                    Password = Environment.GetEnvironmentVariable("DB_PASS"), // e.g. 'my-db-password'
                    Database = Environment.GetEnvironmentVariable("DB_NAME"), // e.g. 'my-database'
                };
                connectionString.Pooling = true;
                // Specify additional properties here.
                return connectionString;
            }
        }
    }

### Go

To see this snippet in the context of a web application, view [the README on GitHub](https://github.com/GoogleCloudPlatform/golang-samples/tree/master/cloudsql/postgres/database-sql/README.md).
    
    
    package cloudsql
    
    import (
    	"database/sql"
    	"fmt"
    	"log"
    	"os"
    
    	// Note: If connecting using the App Engine Flex Go runtime, use
    	// "github.com/jackc/pgx/stdlib" instead, since v5 requires
    	// Go modules which are not supported by App Engine Flex.
    	_ "github.com/jackc/pgx/v5/stdlib"
    )
    
    // connectUnixSocket initializes a Unix socket connection pool for
    // a Cloud SQL instance of Postgres.
    func connectUnixSocket() (*sql.DB, error) {
    	mustGetenv := func(k string) string {
    		v := os.Getenv(k)
    		if v == "" {
    			log.Fatalf("Fatal Error in connect_unix.go: %s environment variable not set.\n", k)
    		}
    		return v
    	}
    	// Note: Saving credentials in environment variables is convenient, but not
    	// secure - consider a more secure solution such as
    	// Cloud Secret Manager (https://cloud.google.com/secret-manager) to help
    	// keep secrets safe.
    	var (
    		dbUser         = mustGetenv("DB_USER")              // e.g. 'my-db-user'
    		dbPwd          = mustGetenv("DB_PASS")              // e.g. 'my-db-password'
    		unixSocketPath = mustGetenv("INSTANCE_UNIX_SOCKET") // e.g. '/cloudsql/project:region:instance'
    		dbName         = mustGetenv("DB_NAME")              // e.g. 'my-database'
    	)
    
    	dbURI := fmt.Sprintf("user=%s password=%s database=%s host=%s",
    		dbUser, dbPwd, dbName, unixSocketPath)
    
    	// dbPool is the pool of database connections.
    	dbPool, err := sql.Open("pgx", dbURI)
    	if err != nil {
    		return nil, fmt.Errorf("sql.Open: %w", err)
    	}
    
    	// ...
    
    	return dbPool, nil
    }
    

### Ruby

To see this snippet in the context of a web application, view [the README on GitHub](https://github.com/GoogleCloudPlatform/ruby-docs-samples/tree/master/cloud-sql/postgres/activerecord/README.md).
    
    
    unix: &unix
      adapter: postgresql
      # Configure additional properties here.
      # Note: Saving credentials in environment variables is convenient, but not
      # secure - consider a more secure solution such as
      # Cloud Secret Manager (https://cloud.google.com/secret-manager) to help
      # keep secrets safe.
      username: <%= ENV["DB_USER"] %>  # e.g. "my-database-user"
      password: <%= ENV["DB_PASS"] %> # e.g. "my-database-password"
      database: <%= ENV.fetch("DB_NAME") { "vote_development" } %>
      # Specify the Unix socket path as host
      host: "<%= ENV["INSTANCE_UNIX_SOCKET"] %>"

### PHP

To see this snippet in the context of a web application, view [the README on GitHub](https://github.com/GoogleCloudPlatform/php-docs-samples/tree/main/cloud_sql/postgres/pdo/README.md).
    
    
    namespace Google\Cloud\Samples\CloudSQL\Postgres;
    
    use PDO;
    use PDOException;
    use RuntimeException;
    use TypeError;
    
    class DatabaseUnix
    {
        public static function initUnixDatabaseConnection(): PDO
        {
            try {
                // Note: Saving credentials in environment variables is convenient, but not
                // secure - consider a more secure solution such as
                // Cloud Secret Manager (https://cloud.google.com/secret-manager) to help
                // keep secrets safe.
                $username = getenv('DB_USER'); // e.g. 'your_db_user'
                $password = getenv('DB_PASS'); // e.g. 'your_db_password'
                $dbName = getenv('DB_NAME'); // e.g. 'your_db_name'
                $instanceUnixSocket = getenv('INSTANCE_UNIX_SOCKET'); // e.g. '/cloudsql/project:region:instance'
    
                // Connect using UNIX sockets
                $dsn = sprintf(
                    'pgsql:dbname=%s;host=%s',
                    $dbName,
                    $instanceUnixSocket
                );
    
                // Connect to the database.
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
                            '$username, $password, $dbName, ' .
                            'and $instanceUnixSocket (for UNIX socket mode). ' .
                            'The PHP error was %s',
                        $e->getMessage()
                    ),
                    (int) $e->getCode(),
                    $e
                );
            } catch (PDOException $e) {
                throw new RuntimeException(
                    sprintf(
                        'Could not connect to the Cloud SQL Database. Check that ' .
                            'your username and password are correct, that the Cloud SQL ' .
                            'proxy is running, and that the database exists and is ready ' .
                            'for use. For more assistance, refer to %s. The PDO error was %s',
                        'https://cloud.google.com/sql/docs/postgres/connect-external-app',
                        $e->getMessage()
                    ),
                    (int) $e->getCode(),
                    $e
                );
            }
    
            return $conn;
        }
    }

### Connect with Cloud SQL connectors

The [Cloud SQL connectors](https://docs.cloud.google.com/sql/docs/postgres/connect-connectors) are language specific libraries that provide encryption and IAM-based authorization when connecting to a Cloud SQL instance. 

### Python

To see this snippet in the context of a web application, view [the README on GitHub](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/master/cloud-sql/postgres/sqlalchemy/README.md).
    
    
    import os
    
    from google.cloud.sql.connector import Connector, IPTypes
    import pg8000
    
    import sqlalchemy
    
    
    def connect_with_connector() -> sqlalchemy.engine.base.Engine:
        """
        Initializes a connection pool for a Cloud SQL instance of Postgres.
    
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
        connector = Connector(refresh_strategy="LAZY")
    
        def getconn() -> pg8000.dbapi.Connection:
            conn: pg8000.dbapi.Connection = connector.connect(
                instance_connection_name,
                "pg8000",
                user=db_user,
                password=db_pass,
                db=db_name,
                ip_type=ip_type,
            )
            return conn
    
        # The Cloud SQL Python Connector can be used with SQLAlchemy
        # using the 'creator' argument to 'create_engine'
        pool = sqlalchemy.create_engine(
            "postgresql+pg8000://",
            creator=getconn,
            # ...
        )
        return pool
    
    

### Java

To see this snippet in the context of a web application, view [the README on GitHub](https://github.com/GoogleCloudPlatform/java-docs-samples/blob/master/cloud-sql/postgres/servlet/README.md).

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
      private static final String INSTANCE_UNIX_SOCKET = System.getenv("INSTANCE_UNIX_SOCKET");
      private static final String DB_USER = System.getenv("DB_USER");
      private static final String DB_PASS = System.getenv("DB_PASS");
      private static final String DB_NAME = System.getenv("DB_NAME");
    
      public static DataSource createConnectionPool() {
        // The configuration object specifies behaviors for the connection pool.
        HikariConfig config = new HikariConfig();
    
        // The following URL is equivalent to setting the config options below:
        // jdbc:postgresql:///<DB_NAME>?cloudSqlInstance=<INSTANCE_CONNECTION_NAME>&
        // socketFactory=com.google.cloud.sql.postgres.SocketFactory&user=<DB_USER>&password=<DB_PASS>
        // See the link below for more info on building a JDBC URL for the Cloud SQL JDBC Socket Factory
        // https://github.com/GoogleCloudPlatform/cloud-sql-jdbc-socket-factory#creating-the-jdbc-url
    
        // Configure which instance and what database user to connect with.
        config.setJdbcUrl(String.format("jdbc:postgresql:///%s", DB_NAME));
        config.setUsername(DB_USER); // e.g. "root", _postgres"
        config.setPassword(DB_PASS); // e.g. "my-password"
    
        config.addDataSourceProperty("socketFactory", "com.google.cloud.sql.postgres.SocketFactory");
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

### Go

To see this snippet in the context of a web application, view [the README on GitHub](https://github.com/GoogleCloudPlatform/golang-samples/tree/master/cloudsql/postgres/database-sql/README.md).
    
    
    package cloudsql
    
    import (
    	"context"
    	"database/sql"
    	"fmt"
    	"log"
    	"net"
    	"os"
    
    	"cloud.google.com/go/cloudsqlconn"
    	"github.com/jackc/pgx/v5"
    	"github.com/jackc/pgx/v5/stdlib"
    )
    
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
    	// keep passwords and other secrets safe.
    	var (
    		dbUser                 = mustGetenv("DB_USER")                  // e.g. 'my-db-user'
    		dbPwd                  = mustGetenv("DB_PASS")                  // e.g. 'my-db-password'
    		dbName                 = mustGetenv("DB_NAME")                  // e.g. 'my-database'
    		instanceConnectionName = mustGetenv("INSTANCE_CONNECTION_NAME") // e.g. 'project:region:instance'
    		usePrivate             = os.Getenv("PRIVATE_IP")
    	)
    
    	dsn := fmt.Sprintf("user=%s password=%s database=%s", dbUser, dbPwd, dbName)
    	config, err := pgx.ParseConfig(dsn)
    	if err != nil {
    		return nil, err
    	}
    	var opts []cloudsqlconn.[Option](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudsqlconn/latest/index.html#cloud_google_com_go_cloudsqlconn_Option)
    	if usePrivate != "" {
    		opts = append(opts, cloudsqlconn.[WithDefaultDialOptions](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudsqlconn/latest/index.html#cloud_google_com_go_cloudsqlconn_Option_WithDefaultDialOptions)(cloudsqlconn.[WithPrivateIP](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudsqlconn/latest/index.html#cloud_google_com_go_cloudsqlconn_DialOption_WithPrivateIP)()))
    	}
    	// WithLazyRefresh() Option is used to perform refresh
    	// when needed, rather than on a scheduled interval.
    	// This is recommended for serverless environments to
    	// avoid background refreshes from throttling CPU.
    	opts = append(opts, cloudsqlconn.[WithLazyRefresh](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudsqlconn/latest/index.html#cloud_google_com_go_cloudsqlconn_Option_WithLazyRefresh)())
    	d, err := cloudsqlconn.[NewDialer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudsqlconn/latest/index.html#cloud_google_com_go_cloudsqlconn_Dialer_NewDialer)(context.Background(), opts...)
    	if err != nil {
    		return nil, err
    	}
    	// Use the Cloud SQL connector to handle connecting to the instance.
    	// This approach does *NOT* require the Cloud SQL proxy.
    	config.DialFunc = func(ctx context.Context, network, instance string) (net.Conn, error) {
    		return d.[Dial](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudsqlconn/latest/index.html#cloud_google_com_go_cloudsqlconn_Dialer_Dial)(ctx, instanceConnectionName)
    	}
    	dbURI := stdlib.RegisterConnConfig(config)
    	dbPool, err := sql.Open("pgx", dbURI)
    	if err != nil {
    		return nil, fmt.Errorf("sql.Open: %w", err)
    	}
    	return dbPool, nil
    }
    

### Node.js

To see this snippet in the context of a web application, view [the README on GitHub](https://github.com/GoogleCloudPlatform/nodejs-docs-samples/blob/main/cloud-sql/postgres/knex/README.md).
    
    
    const Knex = require('knex');
    const {Connector} = require('@google-cloud/cloud-sql-connector');
    
    // In case the PRIVATE_IP environment variable is defined then we set
    // the ipType=PRIVATE for the new connector instance, otherwise defaults
    // to public ip type.
    const getIpType = () =>
      process.env.PRIVATE_IP === '1' || process.env.PRIVATE_IP === 'true'
        ? 'PRIVATE'
        : 'PUBLIC';
    
    // connectWithConnector initializes connection pool for a Cloud SQL instance
    // of Postgres using the Cloud SQL Node.js Connector.
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
        client: 'pg',
        connection: {
          ...clientOpts,
          user: process.env.DB_USER, // e.g. 'my-user'
          password: process.env.DB_PASS, // e.g. 'my-user-password'
          database: process.env.DB_NAME, // e.g. 'my-database'
        },
        // ... Specify additional properties here.
        ...config,
      };
      // Establish a connection to the database.
      return Knex(dbConfig);
    };

### Private IP

For private IP paths, your application connects directly to your instance through a VPC network. This method uses TCP to connect directly to the Cloud SQL instance without using the Cloud SQL Auth Proxy. 

### Connect with TCP

Connect using the private IP address of your Cloud SQL instance as the host and port `5432`.

### Python

To see this snippet in the context of a web application, view [the README on GitHub](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/master/cloud-sql/postgres/sqlalchemy/README.md).
    
    
    import os
    import ssl
    
    import sqlalchemy
    
    
    def connect_tcp_socket() -> sqlalchemy.engine.base.Engine:
        """Initializes a TCP connection pool for a Cloud SQL instance of Postgres."""
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
        db_port = os.environ["DB_PORT"]  # e.g. 5432
    
        pool = sqlalchemy.create_engine(
            # Equivalent URL:
            # postgresql+pg8000://<db_user>:<db_pass>@<db_host>:<db_port>/<db_name>
            sqlalchemy.engine.url.URL.create(
                drivername="postgresql+pg8000",
                username=db_user,
                password=db_pass,
                host=db_host,
                port=db_port,
                database=db_name,
            ),
            # ...
        )
        return pool
    
    

### Java

To see this snippet in the context of a web application, view [the README on GitHub](https://github.com/GoogleCloudPlatform/java-docs-samples/blob/master/cloud-sql/postgres/servlet/README.md).

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
    
        // The following URL is equivalent to setting the config options below:
        // jdbc:postgresql://<INSTANCE_HOST>:<DB_PORT>/<DB_NAME>?user=<DB_USER>&password=<DB_PASS>
        // See the link below for more info on building a JDBC URL for the Cloud SQL JDBC Socket Factory
        // https://github.com/GoogleCloudPlatform/cloud-sql-jdbc-socket-factory#creating-the-jdbc-url
    
        // Configure which instance and what database user to connect with.
        config.setJdbcUrl(String.format("jdbc:postgresql://%s:%s/%s", INSTANCE_HOST, DB_PORT, DB_NAME));
        config.setUsername(DB_USER); // e.g. "root", "postgres"
        config.setPassword(DB_PASS); // e.g. "my-password"
    
    
        // ... Specify additional connection properties here.
        // ...
    
        // Initialize the connection pool using the configuration object.
        return new HikariDataSource(config);
      }
    }

### Node.js

To see this snippet in the context of a web application, view [the README on GitHub](https://github.com/GoogleCloudPlatform/nodejs-docs-samples/blob/master/cloud-sql/postgres/knex/README.md).
    
    
    const Knex = require('knex');
    const fs = require('fs');
    
    // createTcpPool initializes a TCP connection pool for a Cloud SQL
    // instance of Postgres.
    const createTcpPool = async config => {
      // Note: Saving credentials in environment variables is convenient, but not
      // secure - consider a more secure solution such as
      // Cloud Secret Manager (https://cloud.google.com/secret-manager) to help
      // keep secrets safe.
      const dbConfig = {
        client: 'pg',
        connection: {
          host: process.env.INSTANCE_HOST, // e.g. '127.0.0.1'
          port: process.env.DB_PORT, // e.g. '5432'
          user: process.env.DB_USER, // e.g. 'my-user'
          password: process.env.DB_PASS, // e.g. 'my-user-password'
          database: process.env.DB_NAME, // e.g. 'my-database'
        },
        // ... Specify additional properties here.
        ...config,
      };
      // Establish a connection to the database.
      return Knex(dbConfig);
    };

### Go

To see this snippet in the context of a web application, view [the README on GitHub](https://github.com/GoogleCloudPlatform/golang-samples/tree/master/cloudsql/postgres/database-sql/README.md).
    
    
    package cloudsql
    
    import (
    	"database/sql"
    	"fmt"
    	"log"
    	"os"
    
    	// Note: If connecting using the App Engine Flex Go runtime, use
    	// "github.com/jackc/pgx/stdlib" instead, since v5 requires
    	// Go modules which are not supported by App Engine Flex.
    	_ "github.com/jackc/pgx/v5/stdlib"
    )
    
    // connectTCPSocket initializes a TCP connection pool for a Cloud SQL
    // instance of Postgres.
    func connectTCPSocket() (*sql.DB, error) {
    	mustGetenv := func(k string) string {
    		v := os.Getenv(k)
    		if v == "" {
    			log.Fatalf("Fatal Error in connect_tcp.go: %s environment variable not set.", k)
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
    		dbPort    = mustGetenv("DB_PORT")       // e.g. '5432'
    		dbName    = mustGetenv("DB_NAME")       // e.g. 'my-database'
    	)
    
    	dbURI := fmt.Sprintf("host=%s user=%s password=%s port=%s database=%s",
    		dbTCPHost, dbUser, dbPwd, dbPort, dbName)
    
    
    	// dbPool is the pool of database connections.
    	dbPool, err := sql.Open("pgx", dbURI)
    	if err != nil {
    		return nil, fmt.Errorf("sql.Open: %w", err)
    	}
    
    	// ...
    
    	return dbPool, nil
    }
    

### C#

To see this snippet in the context of a web application, view [the README on GitHub](https://github.com/GoogleCloudPlatform/dotnet-docs-samples/blob/master/cloud-sql/mysql/README.md).
    
    
    using Npgsql;
    using System;
    
    namespace CloudSql
    {
        public class PostgreSqlTcp
        {
            public static NpgsqlConnectionStringBuilder NewPostgreSqlTCPConnectionString()
            {
                // Equivalent connection string:
                // "Uid=<DB_USER>;Pwd=<DB_PASS>;Host=<INSTANCE_HOST>;Database=<DB_NAME>;"
                var connectionString = new NpgsqlConnectionStringBuilder()
                {
                    // Note: Saving credentials in environment variables is convenient, but not
                    // secure - consider a more secure solution such as
                    // Cloud Secret Manager (https://cloud.google.com/secret-manager) to help
                    // keep secrets safe.
                    Host = Environment.GetEnvironmentVariable("INSTANCE_HOST"),     // e.g. '127.0.0.1'
                    // Set Host to 'cloudsql' when deploying to App Engine Flexible environment
                    Username = Environment.GetEnvironmentVariable("DB_USER"), // e.g. 'my-db-user'
                    Password = Environment.GetEnvironmentVariable("DB_PASS"), // e.g. 'my-db-password'
                    Database = Environment.GetEnvironmentVariable("DB_NAME"), // e.g. 'my-database'
    
                    // The Cloud SQL proxy provides encryption between the proxy and instance.
                    SslMode = SslMode.Disable,
                };
                connectionString.Pooling = true;
                // Specify additional properties here.
                return connectionString;
            }
        }
    }

### Ruby

To see this snippet in the context of a web application, view [the README on GitHub](https://github.com/GoogleCloudPlatform/ruby-docs-samples/tree/master/cloud-sql/postgres/activerecord/README.md).
    
    
    tcp: &tcp
      adapter: postgresql
      # Configure additional properties here.
      # Note: Saving credentials in environment variables is convenient, but not
      # secure - consider a more secure solution such as
      # Cloud Secret Manager (https://cloud.google.com/secret-manager) to help
      # keep secrets safe.
      username: <%= ENV["DB_USER"] %>  # e.g. "my-database-user"
      password: <%= ENV["DB_PASS"] %> # e.g. "my-database-password"
      database: <%= ENV.fetch("DB_NAME") { "vote_development" } %>
      host: <%= ENV.fetch("INSTANCE_HOST") { "127.0.0.1" }%> # '172.17.0.1' if deployed to GAE Flex
      port: <%= ENV.fetch("DB_PORT") { 5432 }%>

### PHP

To see this snippet in the context of a web application, view [the README on GitHub](https://github.com/GoogleCloudPlatform/php-docs-samples/tree/main/cloud_sql/postgres/pdo/README.md).
    
    
    namespace Google\Cloud\Samples\CloudSQL\Postgres;
    
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
                $dsn = sprintf('pgsql:dbname=%s;host=%s', $dbName, $instanceHost);
    
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
                        'https://cloud.google.com/sql/docs/postgres/connect-external-app',
                        $e->getMessage()
                    ),
                    $e->getCode(),
                    $e
                );
            }
    
            return $conn;
        }
    }

## Best practices and other information

You can use the [Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/postgres/sql-proxy) when testing your application locally. See the [quickstart for using the Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/mysql/connect-instance-auth-proxy) for detailed instructions.

### Connection Pools

Connections to underlying databases may be dropped, either by the database server itself, or by the underlying infrastructure. To mitigate this, we recommend that you use a client library that supports [connection pools](https://docs.cloud.google.com/sql/docs/mysql/manage-connections#pools) and automatic reconnection. 

### Connection Limits

Each App Engine instance running in a standard environment cannot have more than _100 concurrent connections_ to an instance. For PHP 5.5 apps, the limit is _60 concurrent connections_. This limit applies per application instance. This means that each instance of the App Engine application can have that many connections to the database, and as it scales the total number of connections per deployment can grow. For more information, see [Scaling elements](https://docs.cloud.google.com/appengine/docs/standard/python/config/appref#scaling_elements). 

You can limit the maximum number of connections used per instance by using a connection pool. For more detailed examples on how to limit the number of connections, see the [ Managing database connections](https://docs.cloud.google.com/sql/docs/mysql/manage-connections#count) page.

App Engine applications are subject to request time limits depending on usage and environment. For more information, see how instances are managed in App Engine standard environment [ standard](https://docs.cloud.google.com/appengine/docs/standard/python/how-instances-are-managed#timeout) and[ flexible](https://docs.cloud.google.com/appengine/docs/flexible/python/how-instances-are-managed) environments. 

### API Quota Limits

App Engine provides a mechanism that connects using the Cloud SQL Auth Proxy, which uses the Cloud SQL Admin API. [ API quota limits](https://console.cloud.google.com/iam-admin/quotas?service=sqladmin.googleapis.com) apply to the Cloud SQL Auth Proxy. When the Cloud SQL Admin API starts, it uses a quota of two and an average of two per hour afterwards. The default quota is 180 per minute per user. App Engine applications are also subject to additional quotas and limits as discussed on the [ App Engine Quotas](https://docs.cloud.google.com/appengine/docs/quotas) page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
