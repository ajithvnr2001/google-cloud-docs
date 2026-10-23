---
url: https://docs.cloud.google.com/sql/docs/postgres/connect-build/
title: Connect from Cloud Build \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:18:32.981030+00:00
---

# Connect from Cloud Build  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/connect-build/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/postgres/features)



Send feedback 

#  Connect from Cloud Build Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/connect-build "View this page for the MySQL database engine") | PostgreSQL | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/connect-build "View this page for the SQL Server database engine")

This page contains information and examples for connecting to a Cloud SQL instance from a service running in Cloud Build. 

Cloud SQL is a fully-managed database service that helps you set up, maintain, manage, and administer your relational databases in the cloud.

[Cloud Build](https://docs.cloud.google.com/build/docs/overview) is a service that executes your builds on Google Cloud infrastructure.

## Set up a Cloud SQL instance

  1. Enable the Cloud SQL Admin API in the Google Cloud project that you are connecting from, if you haven't already done so: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=sqladmin&redirect=https%3A//console.cloud.google.com)

  2. [Create a Cloud SQL for PostgreSQL instance](https://docs.cloud.google.com/sql/docs/postgres/create-instance). We recommend that you choose a Cloud SQL [ instance location](https://docs.cloud.google.com/sql/docs/postgres/locations) in the same region as your Cloud Build service for better latency, to avoid some networking costs, and to reduce cross region failure risks. 

By default, Cloud SQL assigns a public IP address to a new instance. You also have the option to assign a private IP address. For more information about the connectivity options for both, see the [ Connecting Overview](https://docs.cloud.google.com/sql/docs/postgres/connect-overview) page.

  3. When you create the instance, you can choose the [ server certificate (CA) hierarchy](https://docs.cloud.google.com/sql/docs/mysql/authorize-ssl#ca-hierarchies) for the instance and then configure the hierarchy as the `serverCaMode` for the instance. You must select the per-instance CA option (`GOOGLE_MANAGED_INTERNAL_CA`) as the server CA mode for instances that you want to connect to from web applications. 



## Set up an Artifact Registry Repository

  1. If you haven't already done so, then enable the Artifact Registry API in the Google Cloud project that you are connecting from: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=artifactregistry&redirect=https%3A//console.cloud.google.com)

  2. [Create a Docker Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos). To improve latency, reduce the risk of cross-region failure, and avoid additional networking costs, we recommend that you choose an Artifact Registry [location](https://docs.cloud.google.com/artifact-registry/docs/repositories/repo-locations) in the same region as your Cloud Run service. 



## Configure Cloud Build

The steps to configure Cloud Build depend on the type of IP address that you assigned to your Cloud SQL instance. 

### Public IP (default)

Make sure your [ Cloud Build service account](https://docs.cloud.google.com/build/docs/cloud-build-service-account) has the [IAM roles and permissions required to connect to the Cloud SQL instance](https://docs.cloud.google.com/sql/docs/mysql/project-access-control#roles). The Cloud Build service account is listed on the Google Cloud console [IAM](https://console.cloud.google.com/iam-admin) page as the **Principal** `[YOUR-PROJECT-NUMBER]@cloudbuild.gserviceaccount.com`.

To view this service account in the Google Cloud console, select the **Include Google-provided role grants** checkbox.

Your Cloud Build service account needs the `Cloud SQL Client` [IAM role](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql).

If the Cloud Build service account belongs to a different project than the Cloud SQL instance, then the Cloud SQL Admin API and the role need to be added for both projects.

### Private IP

To connect to your Cloud SQL instance over private IP, Cloud Build must be in the same VPC network as your Cloud SQL instance. To configure this: 

  1. Set up a private connection between the [VPC network of your Cloud SQL instance and the service producer network](https://docs.cloud.google.com/build/docs/private-pools/set-up-private-pool-environment#setup-private-connection).
  2. Create a [Cloud Build private pool](https://docs.cloud.google.com/build/docs/private-pools/create-manage-private-pools#creating_a_new_private_pool).



Once configured, your application will be able to connect directly using your instance's private IP address and port `5432` when your build is run in the pool.

## Connect to Cloud SQL

After you configure Cloud Build, you can connect to your Cloud SQL instance.

### Public IP (default)

For public IP paths, Cloud Build supports both Unix and TCP sockets. 

### Connect with TCP

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

### Connect with Unix sockets

Once correctly configured, you can connect your service to your Cloud SQL instance's Unix domain socket accessed on the environment's filesystem at the following path: `/cloudsql/INSTANCE_CONNECTION_NAME`.

The INSTANCE_CONNECTION_NAME uses the format `project:region:instance-id`. You can find it on the **Overview** page for your instance in the [Google Cloud console](https://console.cloud.google.com/sql) or by running the following command:

`gcloud sql instances describe [INSTANCE_NAME]`

These connections are automatically encrypted without any additional configuration.

The code samples shown below are extracts from more complete examples on the GitHub site. Click `View on GitHub` to see more.

**Note:** The PostgreSQL standard requires a `.s.PGSQL.5432` suffix in the socket path. Some libraries apply this suffix automatically, but others require you to specify the socket path as follows: 
    
    
    /cloudsql/INSTANCE_CONNECTION_NAME/.s.PGSQL.5432

**Warning:** Linux-based operating systems have a maximum socket path length of 108 characters. If the total length of the path exceeds this length, you cannot connect with a socket from Cloud Build. 

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

You can use the Cloud SQL Auth Proxy in a Cloud Build step to allow connections to your database. This configuration: 

  1. Builds your container and pushes it to Artifact Registry.
  2. Builds a second container, copying in the Cloud SQL Auth Proxy binary.
     * Containers built by Cloud Build don't need to be pushed to any registry and are [discarded on build completion](https://docs.cloud.google.com/build/docs/build-config-file-schema#images).
  3. Using the second container, starts the Cloud SQL Auth Proxy and runs any migration commands.


    
    
    steps:
      - id: install-proxy
        name: gcr.io/cloud-builders/wget
        entrypoint: sh
        args:
          - -c
          - |
            wget -O /workspace/cloud-sql-proxy https://storage.googleapis.com/cloud-sql-connectors/cloud-sql-proxy/2.26.3
            chmod +x /workspace/cloud-sql-proxy
    
     - id: migrate
        waitFor: ['install-proxy']
        name: YOUR_CONTAINER_IMAGE_NAME
        entrypoint: sh
        env:
          - "DATABASE_NAME=${_DATABASE_NAME}"
          - "DATABASE_USER=${_DATABASE_USER}"
          - "DATABASE_PORT=${_DATABASE_PORT}"
          - "INSTANCE_CONNECTION_NAME=${_INSTANCE_CONNECTION_NAME}"
        secretEnv:
          - DATABASE_PASS
        args:
          - "-c"
          - |
            /workspace/cloud-sql-proxy ${_INSTANCE_CONNECTION_NAME} --port ${_DATABASE_PORT} & sleep 2;
            # Cloud SQL Proxy is now up and running, add your own logic below to connect
            python migrate.py # For example
    
      options:
        dynamic_substitutions: true
    
      substitutions:
        _DATABASE_USER: myuser
        _DATABASE_NAME: mydatabase
        _INSTANCE_CONNECTION_NAME: ${PROJECT_ID}:us-central1:myinstance
        _DATABASE_PORT: '5432'
        _DATABASE_PASSWORD_KEY: database_password
        _AR_REPO_REGION: us-central1
        _AR_REPO_NAME: my-docker-repo
        _IMAGE_NAME: ${_AR_REPO_REGION}-docker.pkg.dev/${PROJECT_ID}/${_AR_REPO_NAME}/sample-sql-proxy
    
      availableSecrets:
        secretManager:
          - versionName: projects/$PROJECT_ID/secrets/${_DATABASE_PASSWORD_KEY}/versions/latest
            env: "DATABASE_PASS"

The Cloud Build code sample shows how you might run a hypothetical `migrate.py` script after deploying the previous sample app to update its Cloud SQL database using the Cloud SQL Auth Proxy and Cloud Build. To run this Cloud Build code sample the setup steps required are: 

  1. Create a folder name `sql-proxy`
  2. Create a `Dockerfile` file in the `sql-proxy` folder with the following single line of code for its file contents: 
         
         FROM gcr.io/gcp-runtimes/ubuntu_20_0_4
             

  3. Create a `cloudbuild.yaml` file in the `sql-proxy` folder.
  4. Update the `cloudbuild.yaml` file: 
     1. Copy the previous sample Cloud Build code and paste it into the `cloudbuild.yaml` file.
     2. Replace the following placeholder values with the values used in your project: 
        * `mydatabase`
        * `myuser`
        * `myinstance`
  5. Create a secret named `database_password` in [Secret Manager](https://console.cloud.google.com/security/secret-manager/). 
     * In order for the Cloud Build service account to access this secret, you have to grant it the [Secret Manager Secret Accessor](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager) role in [IAM](https://console.cloud.google.com/iam-admin/iam). See [Using secrets from Secret Manager](https://docs.cloud.google.com/build/docs/securing-builds/use-secrets) for more information. 
  6. Create a **migrate.py** script file in the `sql-proxy` folder. 
     * The script can reference the following environment variables and the secret created in the `cloudbuild.yaml` file using the following examples: 
       * `os.getenv('DATABASE_NAME')`
       * `os.getenv('DATABASE_USER')`
       * `os.getenv('DATABASE_PASS')`
       * `os.getenv('INSTANCE_CONNECTION_NAME')`
     * To reference the same variables from a Bash script (for example: `migrate.sh`) use the following examples: 
       * `$DATABASE_NAME`
       * `$DATABASE_USER`
       * `$DATABASE_PASS`
       * `$INSTANCE_CONNECTION_NAME`
  7. Run the following [`gcloud builds submit`](https://docs.cloud.google.com/sdk/gcloud/reference/builds/submit) command to build a container with the Cloud SQL Auth Proxy, start the Cloud SQL Auth Proxy, and run the `migrate.py` script: 
         
         gcloud builds submit --config cloudbuild.yaml
             




### Private IP

For private IP paths, your application connects directly to your instance through private pools. This method uses TCP to connect directly to the Cloud SQL instance without using the Cloud SQL Auth Proxy. 

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

You can then create a Cloud Build step to run your code directly. 
    
    
    steps:
      - id: "docker-build"
        name: "gcr.io/cloud-builders/docker"
        args: ["build", "-t", "${_IMAGE_NAME}", "sql-private-pool/."]
    
      - id: "docker-push"
        name: "gcr.io/cloud-builders/docker"
        args: ["push", "${_IMAGE_NAME}"]
    
      - id: "migration"
        name: "${_IMAGE_NAME}"
        dir: sql-private-pool
        env:
          - "DATABASE_NAME=mydatabase"
          - "DATABASE_USER=myuser"
          - "DATABASE_HOST=${_DATABASE_HOST}"
          - "DATABASE_TYPE=${_DATABASE_TYPE}"
        secretEnv:
          - DATABASE_PASS
        entrypoint: python   # for example
        args: ["migrate.py"] # for example
    
    options:
      pool:
        name: projects/$PROJECT_ID/locations/us-central1/workerPools/private-pool
      dynamicSubstitutions: true
    
    substitutions:
      _DATABASE_PASSWORD_KEY: database_password
      _DATABASE_TYPE: postgres
      _AR_REPO_REGION: us-central1
      _AR_REPO_NAME: my-docker-repo
      _IMAGE_NAME: ${_AR_REPO_REGION}-docker.pkg.dev/${PROJECT_ID}/${_AR_REPO_NAME}/sample-private-pool
    
    availableSecrets:
      secretManager:
        - versionName: projects/$PROJECT_ID/secrets/${_DATABASE_PASSWORD_KEY}/versions/latest
          env: DATABASE_PASS

The Cloud Build code sample above shows how you might run a hypothetical **migrate** script after deploying the sample app above to update its Cloud SQL database using Cloud Build. To run this Cloud Build code sample the setup steps required are: 

  1. Create a folder name `sql-private-pool`
  2. Create a `Dockerfile` file in the `sql-private-pool` folder with the following single line of code for its file contents: 
         
         FROM gcr.io/gcp-runtimes/ubuntu_20_0_4

  3. Create a `cloudbuild.yaml` file in the `sql-private-pool` folder.
  4. Update the `cloudbuild.yaml` file: 
     1. Copy the sample Cloud Build code above and paste it into the `cloudbuild.yaml` file.
     2. Replace the following placeholder values with the values used in your project: 
        * `mydatabase`
        * `myuser`
        * `databasehost`, in the form `host:port`.
  5. Create a secret named `database_password` in [Secret Manager](https://console.cloud.google.com/security/secret-manager/). 
     * In order for the Cloud Build service account to access this secret, you will have to grant it the [Secret Manager Secret Accessor](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager) role in [IAM](https://console.cloud.google.com/iam-admin/iam). See [Using secrets from Secret Manager](https://docs.cloud.google.com/build/docs/securing-builds/use-secrets) for more information. 
  6. Create a **migrate.py** script file in the `sql-proxy` folder. 
     * The script can reference the following environment variables and the secret created in the `cloudbuild.yaml` file using the following examples: 
       * `os.getenv('DATABASE_NAME')`
       * `os.getenv('DATABASE_USER')`
       * `os.getenv('DATABASE_PASS')`
       * `os.getenv('DATABASE_HOST')`
     * To reference the same variables from a Bash script (for example: `migrate.sh`) use the following examples: 
       * `$DATABASE_NAME`
       * `$DATABASE_USER`
       * `$DATABASE_PASS`
       * `$DATABASE_HOST`
  7. Run the following [`gcloud builds submit`](https://docs.cloud.google.com/sdk/gcloud/reference/builds/submit) command to build a container with the Cloud SQL Auth Proxy, start the Cloud SQL Auth Proxy, and run the `migrate.py` script: 
         
         gcloud builds submit --config cloudbuild.yaml




## Best practices and other information

You can use the [Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/postgres/sql-proxy) when testing your application locally. See the [quickstart for using the Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/mysql/connect-instance-auth-proxy) for detailed instructions.

You can also test using the [Cloud SQL Proxy via a docker container](https://docs.cloud.google.com/sql/docs/postgres/connect-docker). 

### Database schema migrations

By configuring Cloud Build to connect to Cloud SQL, you can run database schema migration tasks in Cloud Build using the same code you would deploy to any other serverless platform.

### Using Secret Manager

You can use [Secret Manager](https://docs.cloud.google.com/build/docs/securing-builds/use-secrets) to include sensitive information in your builds. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
