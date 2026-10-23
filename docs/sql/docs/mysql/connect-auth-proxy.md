---
url: https://docs.cloud.google.com/sql/docs/mysql/connect-auth-proxy/
title: Connect using the Cloud SQL Auth Proxy \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:11:49.060416+00:00
---

# Connect using the Cloud SQL Auth Proxy  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/connect-auth-proxy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Connect using the Cloud SQL Auth Proxy Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/connect-auth-proxy "View this page for the PostgreSQL database engine") | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/connect-auth-proxy "View this page for the SQL Server database engine")

This page describes how to connect to your Cloud SQL instance using the Cloud SQL Auth Proxy.

For more information about how the Cloud SQL Auth Proxy works, see [About the Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/mysql/sql-proxy).

## Overview

Using the [Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/mysql/sql-proxy) is the recommended method for connecting to a Cloud SQL instance. The Cloud SQL Auth Proxy:

  * Works with both public and private IP endpoints
  * Validates connections using credentials for a user or service account
  * Wraps the connection in a SSL/TLS layer that's authorized for a Cloud SQL instance



Some Google Cloud services and applications use the Cloud SQL Auth Proxy to provide connections for public IP paths with encryption and authorization, including: 

  * [App Engine standard environment](https://docs.cloud.google.com/sql/docs/mysql/connect-app-engine-standard)
  * [App Engine flexible environment](https://docs.cloud.google.com/sql/docs/mysql/connect-app-engine-flexible)
  * [Cloud Run](https://docs.cloud.google.com/sql/docs/mysql/connect-run)



Applications running in [ Google Kubernetes Engine](https://docs.cloud.google.com/sql/docs/mysql/connect-kubernetes-engine#proxy) can connect using the Cloud SQL Auth Proxy.

**Note:** For connecting from Google Kubernetes Engine, we recommend running the Cloud SQL Auth Proxy in a `sidecar` pattern, as an [ additional container](https://docs.cloud.google.com/sql/docs/mysql/connect-kubernetes-engine#run_the_as_a_sidecar) that shares a pod with your application. Also see the related [ quickstart](https://docs.cloud.google.com/sql/docs/mysql/connect-instance-kubernetes).

See the [Quickstart for using the Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/mysql/connect-instance-auth-proxy) for a basic introduction to its usage.

You can also connect, with or without the Cloud SQL Auth Proxy, using a mysql client [from a local machine or Compute Engine](https://docs.cloud.google.com/sql/docs/mysql/connect-admin-ip).

## Before you begin

Before you can connect to a Cloud SQL instance, do the following:

  1.      * For a user or service account, make sure the account has the Cloud SQL Client role. This role contains the `cloudsql.instances.connect` permission, which authorizes a principal to connect to all Cloud SQL instances in a project. 

[ Go to the IAM page](https://console.cloud.google.com/iam-admin/iam)

     * You can optionally include an [IAM condition](https://docs.cloud.google.com/sql/docs/mysql/project-access-control#allow_users_to_connect_to_specific_instances) in the IAM policy binding that grants the account permission to connect only to one specific Cloud SQL instance. 
  2. Enable the Cloud SQL Admin API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=sqladmin)

  3. Install and initialize the [gcloud CLI](https://docs.cloud.google.com/sdk/docs/install).
  4. Optional. Install the Cloud SQL Auth Proxy Docker client.



## Download the Cloud SQL Auth Proxy

Before you begin, you must determine your machine's architecture.

If running on Linux or Mac, you can find this by running the following command:
    
    
      uname -a
      

### Linux 64-bit

  1. Download the Cloud SQL Auth Proxy: 
         
         curl -o cloud-sql-proxy https://storage.googleapis.com/cloud-sql-connectors/cloud-sql-proxy/v2.26.3/cloud-sql-proxy.linux.amd64

  2. Make the Cloud SQL Auth Proxy executable: 
         
         chmod +x cloud-sql-proxy




### Linux 32-bit

  1. Download the Cloud SQL Auth Proxy: 
         
         curl -o cloud-sql-proxy https://storage.googleapis.com/cloud-sql-connectors/cloud-sql-proxy/v2.26.3/cloud-sql-proxy.linux.386

  2. If the `curl` command is not found, run `sudo apt install curl` and repeat the download command.
  3. Make the Cloud SQL Auth Proxy executable: 
         
         chmod +x cloud-sql-proxy




### macOS 64-bit

  1. Download the Cloud SQL Auth Proxy: 
         
         curl -o cloud-sql-proxy https://storage.googleapis.com/cloud-sql-connectors/cloud-sql-proxy/v2.26.3/cloud-sql-proxy.darwin.amd64

  2. Make the Cloud SQL Auth Proxy executable: 
         
         chmod +x cloud-sql-proxy




### Mac M1

  1. Download the Cloud SQL Auth Proxy: 
         
         curl -o cloud-sql-proxy https://storage.googleapis.com/cloud-sql-connectors/cloud-sql-proxy/v2.26.3/cloud-sql-proxy.darwin.arm64
           

  2. Make the Cloud SQL Auth Proxy executable: 
         
         chmod +x cloud-sql-proxy
           




### Windows 64-bit

Right-click <https://storage.googleapis.com/cloud-sql-connectors/cloud-sql-proxy/v2.26.3/cloud-sql-proxy.x64.exe> and select **Save Link As** to download the Cloud SQL Auth Proxy. Rename the file to `cloud-sql-proxy.exe`. 

### Windows 32-bit

Right-click <https://storage.googleapis.com/cloud-sql-connectors/cloud-sql-proxy/v2.26.3/cloud-sql-proxy.x86.exe> and select **Save Link As** to download the Cloud SQL Auth Proxy. Rename the file to `cloud-sql-proxy.exe`. 

### Cloud SQL Auth Proxy Docker image

The Cloud SQL Auth Proxy has different container images, such as `distroless`, `alpine`, and `buster`. The default Cloud SQL Auth Proxy container image uses [`distroless`](https://github.com/GoogleContainerTools/distroless), which contains no shell. If you need a shell or related tools, then download an image based on `alpine` or `buster`. For more information, see [Cloud SQL Auth Proxy Container Images](https://github.com/GoogleCloudPlatform/cloudsql-proxy#container-images).

You can pull the latest image to your local machine using Docker by using the following command:
    
    
    docker pull gcr.io/cloud-sql-connectors/cloud-sql-proxy:2.26.3
    

**Note** : The Cloud SQL Auth Proxy uses a repository that supports the `gcr.io` domain but serves images from Artifact Registry. For more information, see [Transition from Container Registry](https://docs.cloud.google.com/artifact-registry/docs/transition/transition-from-gcr). 

### Other OS

For other operating systems not included here, you can [compile the Cloud SQL Auth Proxy from source](http://github.com/GoogleCloudPlatform/cloudsql-proxy). 

## Start the Cloud SQL Auth Proxy

Depending on your language and environment, you can start the Cloud SQL Auth Proxy using TCP sockets, Unix sockets, or the Cloud SQL Auth Proxy Docker image. The Cloud SQL Auth Proxy binary connects to one or more Cloud SQL instances specified on the command line, and opens a local connection as either TCP or a Unix socket. Other applications and services, such as your application code or database management client tools, can connect to Cloud SQL instances through those TCP or Unix socket connections.

**Warning:** Be careful when binding the Cloud SQL Auth Proxy to an external interface. Anyone with access to that interface/port will be authorized to connect to your instance.

### TCP sockets

For TCP connections, the Cloud SQL Auth Proxy listens on `localhost`(`127.0.0.1`) by default. So, when you specify `--port PORT_NUMBER` for an instance, the local connection is at `127.0.0.1:PORT_NUMBER`.

Alternatively, you can specify a different address for the local connection. For example, here's how to make the Cloud SQL Auth Proxy listen at `0.0.0.0:1234` for the local connection:
    
    
    ./cloud-sql-proxy --address 0.0.0.0 --port 1234 INSTANCE_CONNECTION_NAME

  1. Copy your INSTANCE_CONNECTION_NAME. This can be found on the **Overview** page for your instance in the [Google Cloud console](https://console.cloud.google.com/sql) or by running the following command:
         
         gcloud sql instances describe INSTANCE_NAME --format='value(connectionName)'

For example: myproject:myregion:myinstance.

  2. If the instance has both public and private IP configured, and you want the Cloud SQL Auth Proxy to use the [private IP](https://docs.cloud.google.com/sql/docs/mysql/configure-private-ip) address, you must provide the following option when you start the Cloud SQL Auth Proxy: 
         
         --private-ip

  3. If you are using a service account to authenticate the Cloud SQL Auth Proxy, note the location on your client machine of the private key file that was created when you created the service account.
  4. Start the Cloud SQL Auth Proxy. 

Some possible Cloud SQL Auth Proxy invocation strings:

     * Using Cloud SDK authentication: 
           
           ./cloud-sql-proxy --port 3306 INSTANCE_CONNECTION_NAME

The specified port must not already be in use, for example, by a local database server. 
     * Using a service account and explicitly including the name of the instance connection (recommended for production environments): 
           
           ./cloud-sql-proxy \
           --credentials-file PATH_TO_KEY_FILE INSTANCE_CONNECTION_NAME &

For more information about Cloud SQL Auth Proxy options, see [Options for authenticating the Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/mysql/connect-auth-proxy#authentication-options). 




### Unix sockets

**Note:** The Cloud SQL Auth Proxy currently does not support Unix sockets on Windows, so this option is only available for Linux and macOS platforms. 

The Cloud SQL Auth Proxy can listen on a Unix socket, which is a Posix standard mechanism for using a folder to manage communication between two processes running on the same host. Advantages to using Unix sockets are improved security and lower latency, however, you cannot access a Unix socket from an external machine.

To create and use a Unix socket, the target directory must exist and both the Cloud SQL Auth Proxy and application must have read and write access to it.

  1. Copy your INSTANCE_CONNECTION_NAME. This can be found on the **Overview** page for your instance in the [Google Cloud console](https://console.cloud.google.com/sql) or by running the following command:
         
         gcloud sql instances describe INSTANCE_NAME --format='value(connectionName)'

For example: myproject:myregion:myinstance.

  2. Create the directory where the Cloud SQL Auth Proxy sockets will live: 
         
         sudo mkdir /cloudsql; sudo chmod 777 /cloudsql

  3. If you are using a service account to authenticate the Cloud SQL Auth Proxy, note the location on your client machine of the private key file that was created when you created the service account.
  4. Open a new Cloud Shell terminal window and start the Cloud SQL Auth Proxy. 

Some possible Cloud SQL Auth Proxy invocation strings:

     * Using Google Cloud SDK authentication: 
           
           ./cloud-sql-proxy --unix-socket /cloudsql INSTANCE_CONNECTION_NAME &

     * Using a service account: 
           
           ./cloud-sql-proxy --unix-socket /cloudsql
             --credentials-file PATH_TO_KEY_FILE INSTANCE_CONNECTION_NAME &

Start the Cloud SQL Auth Proxy in its own Cloud Shell terminal so you can monitor its output without it mixing with the output from other programs.

For more information about Cloud SQL Auth Proxy options, see [Options for authenticating the Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/mysql/connect-auth-proxy#authentication-options). **NOTE:** When using a unix socket to connect to Cloud SQL using the Cloud SQL Auth Proxy, make sure the socket filename's length does not surpass the system's limit. It depends on the system, but it's usually between 91-108 characters. On Linux, the length is usually defined as 108, and you can use the following command to check: 
    
    cat /usr/include/linux/un.h | grep "define UNIX_PATH_MAX"




### Docker

To run the Cloud SQL Auth Proxy in a Docker container, use the Cloud SQL Auth Proxy Docker image available from the [Google Container Registry](https://docs.cloud.google.com/container-registry). 

You can start the Cloud SQL Auth Proxy using either TCP sockets or Unix sockets, with the commands shown below. The options use an INSTANCE_CONNECTION_NAME as the connection string to identify a Cloud SQL instance. You can find the INSTANCE_CONNECTION_NAME on the **Overview** page for your instance in the [Google Cloud console](https://console.cloud.google.com/sql) or by running the following command:
    
    
    gcloud sql instances describe INSTANCE_NAME

For example: `myproject:myregion:myinstance`.

Note: The Cloud SQL Auth Proxy doesn't support listening on Unix domain sockets on Windows.

Depending on your language and environment, you can start the Cloud SQL Auth Proxy using either TCP sockets or Unix sockets. Unix sockets aren't supported for applications written in the Java programming language or for the Windows environment.

### Using TCP sockets
    
    
    docker run -d \
      -v PATH_TO_KEY_FILE:/path/to/service-account-key.json \
      -p 127.0.0.1:3306:3306 \
      gcr.io/cloud-sql-connectors/cloud-sql-proxy:2.26.3 \
      --address 0.0.0.0 --port 3306 \
      --credentials-file /path/to/service-account-key.json INSTANCE_CONNECTION_NAME

If you're using the credentials provided by your Compute Engine instance, don't include the `--credentials-file` parameter and the `-v PATH_TO_KEY_FILE:/path/to/service-account-key.json` line. 

Always specify the `127.0.0.1` prefix in `-p` so that the Cloud SQL Auth Proxy isn't exposed outside the local host. The `--address 0.0.0.0` flag is required to make the port accessible from outside of the Docker container. 

### Using Unix sockets
    
    
    docker run -d -v /cloudsql:/cloudsql \
      -v PATH_TO_KEY_FILE:/path/to/service-account-key.json \
      gcr.io/cloud-sql-connectors/cloud-sql-proxy:2.26.3 \
      --unix-socket /cloudsql \
      --credentials-file /path/to/service-account-key.json INSTANCE_CONNECTION_NAME

If you're using the credentials provided by your Compute Engine instance, don't include the `--credentials-file` parameter and the `-v PATH_TO_KEY_FILE:/path/to/service-account-key.json` line. 

If you're using a container-optimized image, use a writable directory in place of `/cloudsql`, for example: 
    
    
    -v /mnt/stateful_partition/cloudsql:/cloudsql

You can specify more than one instance, separated by spaces. You can also use [Compute Engine metadata](https://docs.cloud.google.com/compute/docs/metadata) to dynamically determine the instances to connect to. [Learn more about the Cloud SQL Auth Proxy parameters.](https://docs.cloud.google.com/sql/docs/mysql/sql-proxy#proxy-startup-options)

## Connect with the mysql client

  1. Download the MySQL Community Server for your platform from the [MySQL Community Server download page](http://dev.mysql.com/downloads/mysql/).   
The Community Server includes the MySQL client. 
  2. Install the Community Server, following the directions on the download page. 



For more information about installing MySQL, see [Installing and Upgrading MySQL](https://dev.mysql.com/doc/refman/8.4/en/installing.html).

The connection string you use depends on whether you started the Cloud SQL Auth Proxy using a TCP socket or a UNIX socket or Docker.

**Important:** Starting in Cloud SQL for MySQL 8.4, the `mysql_native_password` authentication plugin is deprecated and new database users are created with the `caching_sha2_password` plugin. To connect using the Cloud SQL Auth Proxy and the `caching_sha2_password` plugin over a TCP socket connection, add the `--get-server-public-key` flag. UNIX socket connections using the Cloud SQL Auth Proxy with the `caching_sha2_password` plugin are not supported. 

### TCP sockets

  1. Start the mysql client: 
         
         mysql -u USERNAME -p --host 127.0.0.1

If you're connecting to a MySQL 8.4 instance, then use the following command: 
         
         mysql -u USERNAME -p --host 127.0.0.1 --get-server-public-key

When you connect using TCP sockets, the Cloud SQL Auth Proxy is accessed through `127.0.0.1`.

  2. If prompted, enter the password.
  3. The mysql prompt appears. 



### Using Unix sockets

  1. Start the mysql client: 
         
         mysql -u USERNAME -p -S /cloudsql/INSTANCE_CONNECTION_NAME --get-server-public-key

  2. Enter the password.
  3. The mysql prompt appears. 



Need help? For help troubleshooting the proxy, see [Troubleshooting Cloud SQL Auth Proxy connections](https://docs.cloud.google.com/sql/docs/mysql/connect-auth-proxy#troubleshooting), or see our [Cloud SQL Support](https://docs.cloud.google.com/sql/docs/mysql/getting-support) page. 

## Connect with an application

You can connect to the Cloud SQL Auth Proxy from any language that enables you to connect to a Unix or TCP socket. Below are some code snippets from complete examples on GitHub to help you understand how they work together in your application.

#### Connecting with TCP

Cloud SQL Auth Proxy invocation statement:
    
    
    ./cloud-sql-proxy INSTANCE_CONNECTION_NAME &

### Python

To see this snippet in the context of a web application, view [the README on GitHub](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/cloud-sql/mysql/sqlalchemy/README.md).
    
    
    import os
    
    import sqlalchemy
    
    
    def connect_tcp_socket() -> sqlalchemy.engine.base.Engine:
        """Initializes a TCP connection pool for a Cloud SQL instance of MySQL."""
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
        db_port = os.environ["DB_PORT"]  # e.g. 3306
    
        pool = sqlalchemy.create_engine(
            # Equivalent URL:
            # mysql+pymysql://<db_user>:<db_pass>@<db_host>:<db_port>/<db_name>
            sqlalchemy.engine.url.URL.create(
                drivername="mysql+pymysql",
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

To see this snippet in the context of a web application, view [the README on GitHub](https://github.com/GoogleCloudPlatform/java-docs-samples/blob/master/cloud-sql/mysql/servlet/README.md). 

Note: 

  * INSTANCE_CONNECTION_NAME should be represented as <MY-PROJECT>:<INSTANCE-REGION>:<INSTANCE-NAME>
  * Using the argument ipTypes=PRIVATE will force the SocketFactory to connect with an instance's associated private IP
  * See the [JDBC socket factory version requirements for the pom.xml file](https://github.com/GoogleCloudPlatform/cloud-sql-jdbc-socket-factory/blob/main/docs/jdbc.md). 


    
    
    import com.zaxxer.hikari.HikariConfig;
    import com.zaxxer.hikari.HikariDataSource;
    import javax.sql.DataSource;
    
    public class TcpConnectionPoolFactory extends ConnectionPoolFactory {
    
      // Saving credentials in environment variables is convenient, but not secure - consider a more
      // secure solution such as https://cloud.google.com/secret-manager/ to help keep secrets safe.
      private static final String DB_USER = System.getenv("DB_USER");
      private static final String DB_PASS = System.getenv("DB_PASS");
      private static final String DB_NAME = System.getenv("DB_NAME");
    
      private static final String INSTANCE_HOST = System.getenv("INSTANCE_HOST");
      private static final String DB_PORT = System.getenv("DB_PORT");
    
    
      public static DataSource createConnectionPool() {
        // The configuration object specifies behaviors for the connection pool.
        HikariConfig config = new HikariConfig();
    
        // The following URL is equivalent to setting the config options below:
        // jdbc:mysql://<INSTANCE_HOST>:<DB_PORT>/<DB_NAME>?user=<DB_USER>&password=<DB_PASS>
        // See the link below for more info on building a JDBC URL for the Cloud SQL JDBC Socket Factory
        // https://github.com/GoogleCloudPlatform/cloud-sql-jdbc-socket-factory#creating-the-jdbc-url
    
        // Configure which instance and what database user to connect with.
        config.setJdbcUrl(String.format("jdbc:mysql://%s:%s/%s", INSTANCE_HOST, DB_PORT, DB_NAME));
        config.setUsername(DB_USER); // e.g. "root", "mysql"
        config.setPassword(DB_PASS); // e.g. "my-password"
    
    
        // ... Specify additional connection properties here.
        // ...
    
        // Initialize the connection pool using the configuration object.
        return new HikariDataSource(config);
      }
    }

### Node.js

To see this snippet in the context of a web application, view [the README on GitHub](https://github.com/GoogleCloudPlatform/nodejs-docs-samples/tree/master/cloud-sql/mysql/mysql/README.md).
    
    
    const mysql = require('promise-mysql');
    const fs = require('fs');
    
    // createTcpPool initializes a TCP connection pool for a Cloud SQL
    // instance of MySQL.
    const createTcpPool = async config => {
      // Note: Saving credentials in environment variables is convenient, but not
      // secure - consider a more secure solution such as
      // Cloud Secret Manager (https://cloud.google.com/secret-manager) to help
      // keep secrets safe.
      const dbConfig = {
        host: process.env.INSTANCE_HOST, // e.g. '127.0.0.1'
        port: process.env.DB_PORT, // e.g. '3306'
        user: process.env.DB_USER, // e.g. 'my-db-user'
        password: process.env.DB_PASS, // e.g. 'my-db-password'
        database: process.env.DB_NAME, // e.g. 'my-database'
        // ... Specify additional properties here.
        ...config,
      };
      // Establish a connection to the database.
      return mysql.createPool(dbConfig);
    };

### Go

To see this snippet in the context of a web application, view [the README on GitHub](https://github.com/GoogleCloudPlatform/golang-samples/tree/master/cloudsql/mysql/database-sql/README.md).
    
    
    package cloudsql
    
    import (
    	"crypto/tls"
    	"crypto/x509"
    	"database/sql"
    	"errors"
    	"fmt"
    	"log"
    	"os"
    
    	"github.com/go-sql-driver/mysql"
    )
    
    // connectTCPSocket initializes a TCP connection pool for a Cloud SQL
    // instance of MySQL.
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
    		dbName    = mustGetenv("DB_NAME")       // e.g. 'my-database'
    		dbPort    = mustGetenv("DB_PORT")       // e.g. '3306'
    		dbTCPHost = mustGetenv("INSTANCE_HOST") // e.g. '127.0.0.1' ('172.17.0.1' if deployed to GAE Flex)
    	)
    
    	dbURI := fmt.Sprintf("%s:%s@tcp(%s:%s)/%s?parseTime=true",
    		dbUser, dbPwd, dbTCPHost, dbPort, dbName)
    
    
    	// dbPool is the pool of database connections.
    	dbPool, err := sql.Open("mysql", dbURI)
    	if err != nil {
    		return nil, fmt.Errorf("sql.Open: %w", err)
    	}
    
    	// ...
    
    	return dbPool, nil
    }
    

### C#

To see this snippet in the context of a web application, view [the README on GitHub](https://github.com/GoogleCloudPlatform/dotnet-docs-samples/blob/master/cloud-sql/mysql/README.md).
    
    
    using MySql.Data.MySqlClient;
    using System;
    
    namespace CloudSql
    {
        public class MySqlTcp
        {
            public static MySqlConnectionStringBuilder NewMysqlTCPConnectionString()
            {
                // Equivalent connection string:
                // "Uid=<DB_USER>;Pwd=<DB_PASS>;Host=<INSTANCE_HOST>;Database=<DB_NAME>;"
                var connectionString = new MySqlConnectionStringBuilder()
                {
                    // Note: Saving credentials in environment variables is convenient, but not
                    // secure - consider a more secure solution such as
                    // Cloud Secret Manager (https://cloud.google.com/secret-manager) to help
                    // keep secrets safe.
                    Server = Environment.GetEnvironmentVariable("INSTANCE_HOST"),   // e.g. '127.0.0.1'
                    // Set Host to 'cloudsql' when deploying to App Engine Flexible environment
                    UserID = Environment.GetEnvironmentVariable("DB_USER"),   // e.g. 'my-db-user'
                    Password = Environment.GetEnvironmentVariable("DB_PASS"), // e.g. 'my-db-password'
                    Database = Environment.GetEnvironmentVariable("DB_NAME"), // e.g. 'my-database'
    
                    // The Cloud SQL proxy provides encryption between the proxy and instance.
                    SslMode = MySqlSslMode.Disabled,
                };
                connectionString.Pooling = true;
                // Specify additional properties here.
                return connectionString;
    
            }
        }
    }

### Ruby

To see this snippet in the context of a web application, view [the README on GitHub](https://github.com/GoogleCloudPlatform/ruby-docs-samples/tree/master/cloud-sql/mysql/activerecord/README.md).
    
    
    tcp: &tcp
      adapter: mysql2
      # Configure additional properties here
      # Note: Saving credentials in environment variables is convenient, but not
      # secure - consider a more secure solution such as
      # Cloud Secret Manager (https://cloud.google.com/secret-manager) to help
      # keep secrets safe.
      username: <%= ENV["DB_USER"] %>  # e.g. "my-database-user"
      password: <%= ENV["DB_PASS"] %> # e.g. "my-database-password"
      database: <%= ENV.fetch("DB_NAME") { "vote_development" } %>
      host: "<%= ENV.fetch("INSTANCE_HOST") { "127.0.0.1" }%>" # '172.17.0.1' if deployed to GAE Flex
      port: <%= ENV.fetch("DB_PORT") { 3306 }%>

### PHP

To see this snippet in the context of a web application, view [the README on GitHub](https://github.com/GoogleCloudPlatform/php-docs-samples/tree/main/cloud_sql/mysql/pdo/README.md).
    
    
    namespace Google\Cloud\Samples\CloudSQL\MySQL;
    
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
                $dsn = sprintf('mysql:dbname=%s;host=%s', $dbName, $instanceHost);
    
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
                        'https://cloud.google.com/sql/docs/mysql/connect-external-app',
                        $e->getMessage()
                    ),
                    $e->getCode(),
                    $e
                );
            }
    
            return $conn;
        }
    }

#### Connecting with Unix sockets

Cloud SQL Auth Proxy invocation statement:
    
    
    ./cloud-sql-proxy --unix-socket /cloudsql INSTANCE_CONNECTION_NAME &
    

### Python

To see this snippet in the context of a web application, view [the README on GitHub](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/cloud-sql/mysql/sqlalchemy/README.md).
    
    
    import os
    
    import sqlalchemy
    
    
    def connect_unix_socket() -> sqlalchemy.engine.base.Engine:
        """Initializes a Unix socket connection pool for a Cloud SQL instance of MySQL."""
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
            # mysql+pymysql://<db_user>:<db_pass>@/<db_name>?unix_socket=<socket_path>/<cloud_sql_instance_name>
            sqlalchemy.engine.url.URL.create(
                drivername="mysql+pymysql",
                username=db_user,
                password=db_pass,
                database=db_name,
                query={"unix_socket": unix_socket_path},
            ),
            # ...
        )
        return pool
    
    

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

To see this snippet in the context of a web application, view [the README on GitHub](https://github.com/GoogleCloudPlatform/nodejs-docs-samples/tree/master/cloud-sql/mysql/mysql/README.md).
    
    
    const mysql = require('promise-mysql');
    
    // createUnixSocketPool initializes a Unix socket connection pool for
    // a Cloud SQL instance of MySQL.
    const createUnixSocketPool = async config => {
      // Note: Saving credentials in environment variables is convenient, but not
      // secure - consider a more secure solution such as
      // Cloud Secret Manager (https://cloud.google.com/secret-manager) to help
      // keep secrets safe.
      return mysql.createPool({
        user: process.env.DB_USER, // e.g. 'my-db-user'
        password: process.env.DB_PASS, // e.g. 'my-db-password'
        database: process.env.DB_NAME, // e.g. 'my-database'
        socketPath: process.env.INSTANCE_UNIX_SOCKET, // e.g. '/cloudsql/project:region:instance'
        // Specify additional properties here.
        ...config,
      });
    };

### C#

To see this snippet in the context of a web application, view [the README on GitHub](https://github.com/GoogleCloudPlatform/dotnet-docs-samples/blob/master/cloud-sql/mysql/README.md).
    
    
    using MySql.Data.MySqlClient;
    using System;
    
    namespace CloudSql
    {
        public class MySqlUnix
        {
            public static MySqlConnectionStringBuilder NewMysqlUnixSocketConnectionString()
            {
                // Equivalent connection string:
                // "Server=<INSTANCE_UNIX_SOCKET>;Uid=<DB_USER>;Pwd=<DB_PASS>;Database=<DB_NAME>;Protocol=unix"
                var connectionString = new MySqlConnectionStringBuilder()
                {
                    // The Cloud SQL proxy provides encryption between the proxy and instance.
                    SslMode = MySqlSslMode.Disabled,
    
                    // Note: Saving credentials in environment variables is convenient, but not
                    // secure - consider a more secure solution such as
                    // Cloud Secret Manager (https://cloud.google.com/secret-manager) to help
                    // keep secrets safe.
                    Server = Environment.GetEnvironmentVariable("INSTANCE_UNIX_SOCKET"), // e.g. '/cloudsql/project:region:instance'
                    UserID = Environment.GetEnvironmentVariable("DB_USER"),   // e.g. 'my-db-user
                    Password = Environment.GetEnvironmentVariable("DB_PASS"), // e.g. 'my-db-password'
                    Database = Environment.GetEnvironmentVariable("DB_NAME"), // e.g. 'my-database'
                    ConnectionProtocol = MySqlConnectionProtocol.UnixSocket
                };
                connectionString.Pooling = true;
                // Specify additional properties here.
                return connectionString;
            }
        }
    }

### Go

To see this snippet in the context of a web application, view [the README on GitHub](https://github.com/GoogleCloudPlatform/golang-samples/tree/master/cloudsql/mysql/database-sql/README.md).
    
    
    package cloudsql
    
    import (
    	"database/sql"
    	"fmt"
    	"log"
    	"os"
    
    	_ "github.com/go-sql-driver/mysql"
    )
    
    // connectUnixSocket initializes a Unix socket connection pool for
    // a Cloud SQL instance of MySQL.
    func connectUnixSocket() (*sql.DB, error) {
    	mustGetenv := func(k string) string {
    		v := os.Getenv(k)
    		if v == "" {
    			log.Fatalf("Fatal Error in connect_unix.go: %s environment variable not set.", k)
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
    		dbName         = mustGetenv("DB_NAME")              // e.g. 'my-database'
    		unixSocketPath = mustGetenv("INSTANCE_UNIX_SOCKET") // e.g. '/cloudsql/project:region:instance'
    	)
    
    	dbURI := fmt.Sprintf("%s:%s@unix(%s)/%s?parseTime=true",
    		dbUser, dbPwd, unixSocketPath, dbName)
    
    	// dbPool is the pool of database connections.
    	dbPool, err := sql.Open("mysql", dbURI)
    	if err != nil {
    		return nil, fmt.Errorf("sql.Open: %w", err)
    	}
    
    	// ...
    
    	return dbPool, nil
    }
    

### Ruby

To see this snippet in the context of a web application, view [the README on GitHub](https://github.com/GoogleCloudPlatform/ruby-docs-samples/tree/master/cloud-sql/mysql/activerecord/README.md).
    
    
    unix: &unix
      adapter: mysql2
      # Configure additional properties here.
      # Note: Saving credentials in environment variables is convenient, but not
      # secure - consider a more secure solution such as
      # Cloud Secret Manager (https://cloud.google.com/secret-manager) to help
      # keep secrets safe.
      username: <%= ENV["DB_USER"] %>  # e.g. "my-database-user"
      password: <%= ENV["DB_PASS"] %> # e.g. "my-database-password"
      database: <%= ENV.fetch("DB_NAME") { "vote_development" } %>
      # Specify the Unix socket path as host
      socket: "<%= ENV["INSTANCE_UNIX_SOCKET"] %>"

### PHP

To see this snippet in the context of a web application, view [the README on GitHub](https://github.com/GoogleCloudPlatform/php-docs-samples/tree/main/cloud_sql/mysql/pdo/README.md).
    
    
    namespace Google\Cloud\Samples\CloudSQL\MySQL;
    
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
                    'mysql:dbname=%s;unix_socket=%s',
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
                        'https://cloud.google.com/sql/docs/mysql/connect-external-app',
                        $e->getMessage()
                    ),
                    (int) $e->getCode(),
                    $e
                );
            }
    
            return $conn;
        }
    }

## Additional topics

### Cloud SQL Auth Proxy command-line arguments

The examples above cover the most common use cases, but the Cloud SQL Auth Proxy also has other configuration options that can be set with command-line arguments. For help on command-line arguments, use the `--help` flag to view the latest documentation:
    
    
    ./cloud-sql-proxy --help

See the [README on the Cloud SQL Auth Proxy GitHub repository](https://github.com/GoogleCloudPlatform/cloudsql-proxy/blob/master/README.md) for additional examples of how to use Cloud SQL Auth Proxy command-line options.

### Options for authenticating the Cloud SQL Auth Proxy

When you authenticate the Cloud SQL Auth Proxy, you enable it to access Google Cloud on behalf of your application, using a set of Google credentials. This is separate from database user authentication. 

All of these options use an INSTANCE_CONNECTION_NAME as the connection string to identify a Cloud SQL instance. You can find the INSTANCE_CONNECTION_NAME on the **Overview** page for your instance in the [Google Cloud console](https://console.cloud.google.com/sql). or by running the following command:

`gcloud sql instances describe --project PROJECT_ID INSTANCE_CONNECTION_NAME`.

For example: `gcloud sql instances describe --project myproject myinstance` .

Some of these options use a JSON credentials file that includes the RSA private key for the account. For instructions on creating a JSON credentials file for a service account, see [Creating a service account](https://docs.cloud.google.com/sql/docs/mysql/connect-auth-proxy#create-service-account). 

The Cloud SQL Auth Proxy provides several alternatives for authentication, depending on your environment. The Cloud SQL Auth Proxy checks for each of the following items, in the following order, using the first one it finds to attempt to authenticate: 

  1. #### Credentials supplied by the credentials-file flag.

Use a [service account](https://docs.cloud.google.com/sql/docs/mysql/connect-auth-proxy#create-service-account) to create and download the associated JSON file, and set the `--credentials-file` flag to the path of the file when you start the Cloud SQL Auth Proxy. The service account must have the [required permissions](https://docs.cloud.google.com/sql/docs/mysql/roles-and-permissions#proxy-roles-permissions) for the Cloud SQL instance. 

To use this option on the command-line, invoke the `cloud-sql-proxy` command with the `--credentials-file` flag set to the path and filename of a JSON credential file. The path can be absolute, or relative to the current working directory. For example: 
         
         ./cloud-sql-proxy --credentials-file PATH_TO_KEY_FILE \
         INSTANCE_CONNECTION_NAME
           

For detailed instructions about adding IAM roles to a service account, see [Granting Roles to Service Accounts](https://docs.cloud.google.com/iam/docs/granting-roles-to-service-accounts). 

For more information about the roles Cloud SQL supports, see [IAM roles for Cloud SQL](https://docs.cloud.google.com/sql/docs/mysql/iam-roles). 

  2. #### Credentials supplied by an access token.

[Create an access token](https://developers.google.com/oauthplayground/) and invoke the `cloud-sql-proxy` command with the `--token` flag set to an OAuth 2.0 access token. For example: 
         
         ./cloud-sql-proxy --token ACCESS_TOKEN \
         INSTANCE_CONNECTION_NAME
           

  3. #### Credentials supplied by an environment variable.

This option is similar to using the `--credentials-file` flag, except you specify the JSON credential file you set in the `GOOGLE_APPLICATION_CREDENTIALS` environment variable instead of using the `--credentials-file` command-line argument. 
  4. #### Credentials from an authenticated [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) client.

If you have installed the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) and have authenticated with your personal account, the Cloud SQL Auth Proxy can use the same account credentials. This method is especially helpful for getting a development environment up and running.

To enable the Cloud SQL Auth Proxy to use your gcloud CLI credentials, use the following command to authenticate the gcloud CLI:
         
         gcloud auth application-default login

  5. #### Credentials associated with the Compute Engine instance.

If you are connecting to Cloud SQL from a Compute Engine instance, the Cloud SQL Auth Proxy can use the service account associated with the Compute Engine instance. If the service account has the [required permissions](https://docs.cloud.google.com/sql/docs/mysql/roles-and-permissions#proxy-roles-permissions) for the Cloud SQL instance, the Cloud SQL Auth Proxy authenticates successfully. 

If the Compute Engine instance is in the same project as the Cloud SQL instance, the default service account for the Compute Engine instance has the necessary permissions for authenticating the Cloud SQL Auth Proxy. If the two instances are in different projects, you must add the Compute Engine instance's service account to the project containing the Cloud SQL instance. 
  6. #### Environment's default service account

If the Cloud SQL Auth Proxy cannot find credentials in any of the places covered earlier, it follows the logic documented in [Setting Up Authentication for Server to Server Production Applications](https://docs.cloud.google.com/docs/authentication/production). Some environment (such as Compute Engine, App Engine, and others) provide a default service account that your application can use to authenticate by default. If you use a default service account, it must have the permissions outlined in [roles and permissions](https://docs.cloud.google.com/sql/docs/mysql/roles-and-permissions#proxy-roles-permissions) For more information about Google Cloud's approach to authentication, see [Authentication overview](https://docs.cloud.google.com/docs/authentication). 



### Create a service account

If you are connecting from Compute Engine, make sure your VM has the proper `scope` to connect using the Cloud SQL Admin API. 

[ Configure the service account](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances#changeserviceaccountandscopes) to have either of the following access scopes: 

  * https://www.googleapis.com/auth/sqlservice.admin
  * https://www.googleapis.com/auth/cloud-platform



  1. In the Google Cloud console, go to the **Service accounts** page. 

[Go to Service accounts](https://console.cloud.google.com/iam-admin/serviceaccounts/)

  2. Select the project that contains your Cloud SQL instance. 
  3. Click **Create service account**. 
  4. In the **Service account name** field, enter a descriptive name for the service account. 
  5. Change the **Service account ID** to a unique, recognizable value and then click **Create and continue**. 
  6. Click the **Select a role** field and select one of the following roles: 
     * **Cloud SQL > Cloud SQL Client**
     * **Cloud SQL > Cloud SQL Editor**
     * **Cloud SQL > Cloud SQL Admin**

**Note:** To create a service account with the required permissions, you must have `resourcemanager.projects.setIamPolicy` permission. This permission is included in the Project Owner, Project IAM Admin, and Organization Administrator roles.  
You must also have enabled the Cloud SQL Admin API. If you are using the legacy project roles (Viewer, Editor, Owner), the service account must have at least the Editor role.

  7. Click **Done** to finish creating the service account.
  8. Click the action menu for your new service account and then select **Manage keys**. 
  9. Click the **Add key** drop-down menu and then click **Create new key**. 
  10. Confirm that the key type is JSON and then click **Create**. 

The private key file is downloaded to your machine. You can move it to another location. Keep the key file secure. 




### Use the Cloud SQL Auth Proxy with private IP

To connect to a Cloud SQL instance using private IP, the Cloud SQL Auth Proxy must be on a resource with access to the same VPC network as the instance.

The Cloud SQL Auth Proxy uses IP to establish a connection with your Cloud SQL instance. By default, the Cloud SQL Auth Proxy attempts to connect using a public IPv4 address.

If your Cloud SQL instance has only private IP or the instance has both public and private IP configured, and you want the Cloud SQL Auth Proxy to use the private IP address, then you must provide the following option when you start the Cloud SQL Auth Proxy:
    
    
    --private-ip
    

### Use the Cloud SQL Auth Proxy to connect to a write endpoint

You can use the Cloud SQL Auth Proxy to connect to a Cloud SQL primary instance that's configured with a write endpoint. A write endpoint is a global domain name service (DNS) name that you can use for connections instead of an IP address for [advanced disaster recovery (DR)](https://docs.cloud.google.com/sql/docs/mysql/intro-to-cloud-sql-disaster-recovery#advanced-dr) such as performing a replica failover or a switchover operation. If a replica failover or switchover operation occurs for the primary instance, then the Cloud SQL Auth Proxy detects changes to the DNS record automatically.

For more information on how to use the Cloud SQL Auth Proxy to connect to a write endpoint, see [Connect database clients to instances using the Cloud SQL Auth Proxy or Cloud SQL Language Connectors](https://docs.cloud.google.com/sql/docs/mysql/connect-to-instance-using-write-endpoint#connect-with-proxy-or-connectors).

### Use the Cloud SQL Auth Proxy with instances that have Private Service Connect enabled

You can use the Cloud SQL Auth Proxy to connect to a Cloud SQL instance with Private Service Connect enabled.

The Cloud SQL Auth Proxy is a connector that provides secure access to this instance without a need for authorized networks or for configuring SSL.

To allow Cloud SQL Auth Proxy client connections, you must set up a [DNS record](https://docs.cloud.google.com/dns/docs/records-overview) which matches the recommended [DNS name](https://docs.cloud.google.com/sql/docs/mysql/configure-private-service-connect#configure-dns) that's provided for the instance. The DNS record is a mapping between a DNS resource and a domain name.

For more information about using the Cloud SQL Auth Proxy to connect to instances with Private Service Connect enabled, see [Connect using the Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/mysql/configure-private-service-connect#connect-cloud-sql-auth-proxy).

### Required configurations for using the Cloud SQL Auth Proxy with MySQL 8.4 and later

When you connect to MySQL 8.4 and later with the Cloud SQL Auth Proxy, you must configure your application database client to use the MySQL configuration setting `allowPublicKeyRetrieval=true`.

For example, if you are using the `mysql` client, then use `--get-server-public-key` flag:
    
    
    mysql -u username -p --get-server-public-key
    

If you are using the Java programming language, then configure the following:
    
    
    config.setJdbcUrl("jdbc:mysql://" + dbHost + ":" + dbPort + "/" + dbName);
    config.addDataSourceProperty("allowPublicKeyRetrieval", "true");
    

### Create a database user account for the Cloud SQL Auth Proxy

When you connect to your instance using the Cloud SQL Auth Proxy, you provide a user account to log in to the instance. You can use any database user account for this purpose. However, because the Cloud SQL Auth Proxy always connects from a hostname that cannot be accessed except by the Cloud SQL Auth Proxy, you can create a user account that can be used only by the Cloud SQL Auth Proxy. The advantage of doing this is that you can specify this account without a password without compromising the security of your instance or your data.

To create a user account that can only be used with the Cloud SQL Auth Proxy, specify the hostname as `'cloudsqlproxy~[IP_ADDRESS]'`. You can also use the IP address wildcard, which would result in `'cloudsqlproxy~%'`. The full user account name would be:
    
    
    '[USER_NAME]'@'cloudsqlproxy~%'
    

or
    
    
    '[USER_NAME]'@'cloudsqlproxy~[IP_ADDRESS]'
    

For help with creating a user, see [Creating and Managing Users](https://docs.cloud.google.com/sql/docs/mysql/create-manage-users). For information about how Cloud SQL works with user accounts, see [Users](https://docs.cloud.google.com/sql/docs/mysql/users).

### Run the Cloud SQL Auth Proxy in a separate process

Running the Cloud SQL Auth Proxy in a separate Cloud Shell terminal process can be useful, to avoid mixing its console output with output from other programs. Use the syntax shown below to invoke the Cloud SQL Auth Proxy in a separate process.

### Linux

On Linux or macOS, use a trailing `&` on the command line to launch the Cloud SQL Auth Proxy in a separate process:
    
    
    ./cloud-sql-proxy INSTANCE_CONNECTION_NAME
      --credentials-file PATH_TO_KEY_FILE &
    

### Windows

In Windows PowerShell, use the `Start-Process` command to launch the Cloud SQL Auth Proxy in a separate process:
    
    
    Start-Process --filepath "cloud-sql-proxy.exe"
      --ArgumentList "
      --credentials-file PATH_TO_KEY_FILEINSTANCE_CONNECTION_NAME"
    

### Run the Cloud SQL Auth Proxy in a Docker container

To run the Cloud SQL Auth Proxy in a Docker container, use the Cloud SQL Auth Proxy Docker image available from the [Google Container Registry](https://docs.cloud.google.com/container-registry). You can install the Cloud SQL Auth Proxy Docker image using the following command:
    
    
    docker pull gcr.io/cloud-sql-connectors/cloud-sql-proxy:2.26.3
    

You can start the Cloud SQL Auth Proxy using either TCP sockets or Unix sockets, with the commands shown below. **Note:** Unix sockets aren't supported for applications written in the Java programming language or for the Windows environment. 

### TCP sockets
    
    
    docker run -d \
      -v PATH_TO_KEY_FILE:/path/to/service-account-key.json \
      -p 127.0.0.1:3306:3306 \
      gcr.io/cloud-sql-connectors/cloud-sql-proxy:2.26.3 \
      --address 0.0.0.0 --port 3306 \
      --credentials-file /path/to/service-account-key.json \
      INSTANCE_CONNECTION_NAME

Always specify the `127.0.0.1` prefix in `-p` so that the Cloud SQL Auth Proxy isn't exposed outside the local host. The `--address 0.0.0.0` flag is required to make the port accessible from outside of the Docker container. 

### Unix sockets
    
    
    docker run -d \
      -v /cloudsql:/cloudsql \
      -v PATH_TO_KEY_FILE:/path/to/service-account-key.json \
      gcr.io/cloud-sql-connectors/cloud-sql-proxy:2.26.3 \
      --unix-socket /cloudsql \
      --credentials-file /path/to/service-account-key.json \
      INSTANCE_CONNECTION_NAME

If you're using a container-optimized image, use a writable directory in place of `/cloudsql`, for example: 
    
    
    -v /mnt/stateful_partition/cloudsql:/cloudsql

If you're using the credentials provided by your Compute Engine instance, don't include the `--credentials-file` parameter and the `-v PATH_TO_KEY_FILE:/path/to/service-account-key.json` line.

### Running the Cloud SQL Auth Proxy as a service

Running the Cloud SQL Auth Proxy as a background service is an option for local development and production workloads. In development, when you need to access your Cloud SQL instance, you can start the service in the background and stop it when you're finished.

For production workloads, the Cloud SQL Auth Proxy doesn't currently provide built-in support for running as a Windows service, but third-party service managers can be used to run it as a service. For example, you can use [NSSM](http://nssm.cc/) to configure the Cloud SQL Auth Proxy as a Windows service, and NSSM monitors the Cloud SQL Auth Proxy and restarts it automatically if it stops responding. See the [NSSM documentation](http://nssm.cc/usage) for more information.

**Note:** If you run the Cloud SQL Auth Proxy as a service, keep in mind that it uses a secure connection to communicate with Cloud SQL instances, but connections from your application to the Cloud SQL Auth Proxy are not encrypted. For this reason, ensure that only trusted users are able to access the address and port that the Cloud SQL Auth Proxy is listening on.

### Enforce the use of Cloud SQL connectors

You can enforce the use of the Cloud SQL Auth Proxy or Cloud SQL Language Connectors in Cloud SQL instance connections using [ConnectorEnforcement](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances#ConnectorEnforcement).

If you're using a [Private Service Connect-enabled instance](https://docs.cloud.google.com/sql/docs/mysql/about-private-service-connect), then there's a limitation. If the instance has connector enforcement enabled, then you can't create read replicas for the instance. Similarly, if the instance has read replicas, then you can't enable connector enforcement for the instance.

### gcloud

The following command enforces the use of Cloud SQL connectors.
    
    
        gcloud sql instances patch INSTANCE_NAME \
        --connector-enforcement REQUIRED
      

To disable the enforcement, use the following line of code: `--connector-enforcement NOT_REQUIRED` The update doesn't trigger a restart.

### REST v1

The following command enforces the use of Cloud SQL connectors.

Before using any of the request data, make the following replacements: 

  * project-id: The project ID.
  * instance-id: The instance ID.



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id

Request JSON body: 
    
    
    {
      "settings": {                     
        "connectorEnforcement": "REQUIRED"    
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
         "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id"

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
        -Uri "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-16T02:32:12.281Z",
      "operationType": "UPDATE",
      "name": "operation-id",
      "targetId": "instance-id",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/project-id/operations/operation-id",
      "targetProject": "project-id"
    }
    

To disable the enforcement, use `"connectorEnforcement": "NOT_REQUIRED"` instead. The update does not trigger a restart.

### REST v1beta4

The following command enforces the use of Cloud SQL connectors.

Before using any of the request data, make the following replacements: 

  * project-id: The project ID.
  * instance-id: The instance ID.



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id

Request JSON body: 
    
    
    {
      "settings": {
        "connectorEnforcement": "REQUIRED"
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
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id"

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
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-16T02:32:12.281Z",
      "operationType": "UPDATE",
      "name": "operation-id",
      "targetId": "instance-id",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/operations/operation-id",
      "targetProject": "project-id"
    }
    

To disable the enforcement, use `"connectorEnforcement": "NOT_REQUIRED"` instead. The update does not trigger a restart.

## Tips for working with Cloud SQL Auth Proxy

### Invoke the Cloud SQL Auth Proxy

All of the sample proxy invocations start the Cloud SQL Auth Proxy in the background, so a prompt is returned. Reserve that Cloud Shell terminal for the Cloud SQL Auth Proxy, to avoid having its output mixed with the output from other programs. Also, the output from the Cloud SQL Auth Proxy can help you diagnose connection problems, so it can be helpful to capture in a log file. If you do not start the Cloud SQL Auth Proxy in the background, the output goes to stdout unless redirected.

You do not have to use `/cloudsql` as the directory for the Cloud SQL Auth Proxy sockets. (That directory name was chosen to minimize differences with App Engine connection strings.) If you change the directory name, however, keep the overall length to a minimum; it is incorporated in a longer string that has a length limit imposed by the operating system. It depends on the system, but it's usually between 91-108 characters. On Linux, the length is usually defined as 108, and you can use the following command to check:   

    
    
    cat /usr/include/linux/un.h | grep "define UNIX_PATH_MAX"

### Use the Cloud SQL Auth Proxy to connect to multiple instances

You can use one local Cloud SQL Auth Proxy client to connect to multiple Cloud SQL instances. The way you do this depends on whether you are using Unix sockets or TCP.

#### Unix sockets

To connect the Cloud SQL Auth Proxy to multiple instances, you provide each instance connection name as an argument to the Cloud SQL Auth Proxy, in a space-separated list. The Cloud SQL Auth Proxy connects to each instance when it starts.

You connect to each instance using its socket, in the specified directory.

For example:
    
    
          ./cloud-sql-proxy --unix-socket /cloudsql \
          myProject:us-central1:myInstance myProject:us-central1:myInstance2 &
          mysql -u myUser -S /cloudsql/myProject:us-central1:myInstance2
      

#### TCP sockets

When you connect using TCP, you specify a port on your machine for the Cloud SQL Auth Proxy to listen on for each Cloud SQL instance. When connecting to multiple Cloud SQL instances, each port specified must be unique and available for use on your machine.

For example:
    
    
        # Start the Cloud SQL Auth Proxy to connect to two different Cloud SQL instances.
        # Give the Cloud SQL Auth Proxy a unique port on your machine to use for each Cloud SQL instance.
    
        ./cloud-sql-proxy "myProject:us-central1:myInstance?port=3306" \
        "myProject:us-central1:myInstance2?port=1234"
    
        # Connect to "myInstance" using port 3306 on your machine:
        mysql -u myInstanceUser --host 127.0.0.1  --port 3306
    
        # Connect to "myInstance2" using port 1234 on your machine:
        mysql -u myInstance2User --host 127.0.0.1  --port 1234
      

## Troubleshoot Cloud SQL Auth Proxy connections

The Cloud SQL Auth Proxy Docker image is based on a specific version of the Cloud SQL Auth Proxy. When a new version of the Cloud SQL Auth Proxy becomes available, pull the new version of the Cloud SQL Auth Proxy Docker image to keep your environment up to date. You can see the current version of the Cloud SQL Auth Proxy by checking the [ Cloud SQL Auth Proxy GitHub releases page](https://github.com/GoogleCloudPlatform/cloudsql-proxy/releases). 

If you are having trouble connecting to your Cloud SQL instance using the Cloud SQL Auth Proxy, here are a few things to try to find what's causing the problem.

  * Check the Cloud SQL Auth Proxy output.

Often, the Cloud SQL Auth Proxy output can help you determine the source of the problem and how to solve it. Pipe the output to a file, or watch the Cloud Shell terminal where you started the Cloud SQL Auth Proxy.

  * If you are getting a `403 notAuthorized` error, and you are using a service account to authenticate the Cloud SQL Auth Proxy, make sure the service account has the correct [permissions](https://docs.cloud.google.com/sql/docs/mysql/roles-and-permissions).

You can check the service account by searching for its ID on the [IAM page](https://console.cloud.google.com/iam-admin). It must have the `cloudsql.instances.connect` permission. The `Cloud SQL Admin`, `Client` and `Editor` predefined roles have this permission.

  * If you are connecting from App Engine and are getting a `403 notAuthorized` error, check the `app.yaml` value `cloud_sql_instances` for a misspelled or incorrect instance connection name. Instance connection names are always in the format `PROJECT:REGION:INSTANCE`.

Also, check that the App Engine service account (for example, $PROJECT_ID@appspot.gserviceaccount.com) has the Cloud SQL Client IAM role.

If the App Engine service lives in one project (project A) and the database lives in another (project B), this error means the App Engine service account has not been given the Cloud SQL Client IAM role in the project with the database (project B).

  * Make sure to enable the Cloud SQL Admin API.

If it is not, you see output like `Error 403: Access Not Configured` in your Cloud SQL Auth Proxy logs.

  * If you are including multiple instances in your instances list, make sure you are using a comma as a delimiter, with no spaces. If you are using TCP, make sure you are specifying different ports for each instance.

  * If you are connecting using UNIX sockets, confirm that the sockets were created by listing the directory you provided when you started the Cloud SQL Auth Proxy.

  * If you have an outbound firewall policy, make sure it allows connections to port 3307 on the target Cloud SQL instance.

**Note:** The Cloud SQL Auth Proxy uses 3307 to connect to the Cloud SQL Auth Proxy server. Port `3306` is the default port for the MySQL protocol over a direct TCP connection (not using the Cloud SQL Auth Proxy).
  * You can confirm that the Cloud SQL Auth Proxy started correctly by looking in the logs under the **Operations > Logging > Logs explorer** section of the Google Cloud console. A successful operation looks like the following:
        
        2021/06/14 15:47:56 Listening on /cloudsql/$PROJECT_ID:$REGION:$INSTANCE_NAME/3306 for $PROJECT_ID:$REGION:$INSTANCE_NAME
        2021/06/14 15:47:56 Ready for new connections
        

  * Quota issues: When the Cloud SQL Admin API quota is breached, the Cloud SQL Auth Proxy starts up with the following error message:
        
        There was a problem when parsing a instance configuration but ignoring due
        to the configuration. Error: googleapi: Error 429: Quota exceeded for quota
        metric 'Queries' and limit 'Queries per minute per user' of service
        'sqladmin.googleapis.com' for consumer 'project_number:$PROJECT_ID.,
        rateLimitExceeded
        

Once an application connects to the proxy, the proxy reports the following error:
        
        failed to refresh the ephemeral certificate for $INSTANCE_CONNECTION_NAME:
        googleapi: Error 429: Quota exceeded for quota metric 'Queries' and limit
        'Queries per minute per user' of service 'sqladmin.googleapis.com' for
        consumer 'project_number:$PROJECT_ID., rateLimitExceeded
        

Solution: Either identify the source of the quota problem, for example, an application is misusing the connector and unnecessarily creating new connections, or contact support to request an increase to the Cloud SQL Admin API quota. If the quota error appears on startup, you must re-deploy the application to restart the proxy. If the quota error appears after startup, a re-deploy is unnecessary.




## What's next

  * Learn more about the [Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/mysql/sql-proxy).
  * Learn more about [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs/overview).
  * Learn more about [Service Accounts](https://docs.cloud.google.com/iam/docs/understanding-service-accounts).
  * Learn about the [two levels of access control](https://docs.cloud.google.com/sql/docs/mysql/instance-access-control) for Cloud SQL instances.
  * Create [users](https://docs.cloud.google.com/sql/docs/mysql/create-manage-users) and [databases](https://docs.cloud.google.com/sql/docs/mysql/create-manage-databases).
  * Learn about [ connecting to your instance from your application](https://docs.cloud.google.com/sql/docs/mysql/instance-access-control#instanceaccess).
  * Learn about [MySQL Client](https://dev.mysql.com/doc/refman/8.4/en/mysql.html).
  * Learn about [options for support](https://docs.cloud.google.com/sql/docs/support).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
