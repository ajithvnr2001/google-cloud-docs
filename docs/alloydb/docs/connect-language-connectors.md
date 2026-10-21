---
url: https://docs.cloud.google.com/alloydb/docs/connect-language-connectors/
title: Connect using the AlloyDB Language Connectors \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:45:54.578698+00:00
---

# Connect using the AlloyDB Language Connectors  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/connect-language-connectors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Connect using the AlloyDB Language Connectors Stay organized with collections  Save and categorize content based on your preferences. 

To simplify establishing secure connections from your application to an AlloyDB for PostgreSQL cluster, you can use the AlloyDB Language Connectors. These client libraries provide the following capabilities:

  * Automated mTLS connections
  * Identity and Access Management (IAM)-based authorization support
  * Automated IAM authentication



AlloyDB Language Connectors can't provide a network path to an AlloyDB cluster if a network path isn't already present.

For more information about AlloyDB Language Connectors, see [AlloyDB Language Connectors overview](https://docs.cloud.google.com/alloydb/docs/language-connectors-overview).

This page discusses the following AlloyDB Language Connectors:

  * The AlloyDB Java Connector
  * The AlloyDB Go Connector
  * The AlloyDB Python Connector



## Before you begin

  1. Enable the AlloyDB API.

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=alloydb.googleapis.com)

  2. Create an AlloyDB instance and configure the default user.

For more information about creating an instance, see [Create a primary instance](https://docs.cloud.google.com/alloydb/docs/instance-primary-create).

For more information about user roles, see [Predefined AlloyDB IAM roles](https://docs.cloud.google.com/alloydb/docs/reference/iam-roles-permissions#roles).

  3. Configure the following IAM roles required to connect to an AlloyDB instance:

     * AlloyDB Client (`roles/alloydb.client`)
     * Service Usage Consumer (`roles/serviceusage.serviceUsageConsumer`)

For more information about which roles and permissions are required, see [Manage IAM authentication](https://docs.cloud.google.com/alloydb/docs/database-users/manage-iam-auth).




## Install the AlloyDB Language Connectors

### Java

The AlloyDB Java Connector is a library that provides IAM-based authorization and encryption when connecting to an AlloyDB instance. If you're using Spring Boot, see the [Spring Boot AlloyDB starter](https://googlecloudplatform.github.io/spring-cloud-gcp/5.3.0/reference/html/alloydb.html).

### Installation

For Maven, you can install the AlloyDB Java Connector by adding the following to your project's `pom.xml`:
    
    
    <!-- Add the connector with the latest version -->
    <dependency>
      <groupId>com.google.cloud</groupId>
      <artifactId>alloydb-jdbc-connector</artifactId>
      <version>1.12.1</version>
    </dependency>
    
    <!-- Add the driver with the latest version -->
    <dependency>
      <groupId>org.postgresql</groupId>
      <artifactId>postgresql</artifactId>
      <version>42.7.5</version>
    </dependency>
    
    <!-- Add HikariCP with the latest version -->
    <dependency>
      <groupId>com.zaxxer</groupId>
      <artifactId>HikariCP</artifactId>
      <version>5.1.0</version>
    </dependency>
    

For Gradle, you can install the AlloyDB Java Connector by including the following in your project's `build.gradle`:
    
    
    // Add connector with the latest version
    implementation group: 'com.google.cloud.alloydb', name: 'alloydb-jdbc-connector', version: '1.12.1'
    
    // Add driver with the latest version
    implementation group: 'org.postgresql', name: 'postgresql', version: '42.7.5'
    
    // Add HikariCP with the latest version
    implementation group: 'com.zaxxer', name: 'HikariCP', version: '5.1.0'
    

### Python (pg8000)

The AlloyDB Python Connector works with the `pg8000` (synchronous) and `asyncpg` (asynchronous) database drivers to let principals with sufficient permissions connect to an AlloyDB database without manually allowlisting IP addresses.

### Installation

You can install the AlloyDB Python Connector library with `pip install`.

If you're using `pg8000`, run the following command:
    
    
    pip install "google-cloud-alloydb-connector[pg8000]" sqlalchemy

### Python (asyncpg)

The AlloyDB Python Connector works with the `pg8000` (synchronous) and `asyncpg` (asynchronous) database drivers to let principals with sufficient permissions connect to an AlloyDB database without manually allowlisting IP addresses.

### Installation

You can install the AlloyDB Python Connector library with `pip install`.

If you're using `asyncpg`, run the following command:
    
    
    pip install "google-cloud-alloydb-connector[asyncpg]" "sqlalchemy[asyncio]"

For more information about async driver usage, see [Async Driver Usage](https://github.com/GoogleCloudPlatform/alloydb-python-connector#async-driver-usage).

### Go (pgx)

The AlloyDB Go Connector is an AlloyDB connector designed for use with the Go language.

### Installation

You can install the AlloyDB Go Connector with `go get`.

If you're using `pgx`, run the following commands:
    
    
    go get github.com/jackc/pgx/v5
    go get cloud.google.com/go/alloydbconn

### Go (database/sql)

The AlloyDB Go Connector is an AlloyDB connector designed for use with the Go language.

### Installation

You can install the AlloyDB Go Connector with `go get`.

If you're using `database/sql`, run the following command:
    
    
    go get cloud.google.com/go/alloydbconn

## Configure the AlloyDB Language Connectors

### Java

To use the AlloyDB Java Connector to connect to your AlloyDB cluster, configure it using the following steps.

To use this snippet in the context of a web application, view [the README on GitHub](https://github.com/GoogleCloudPlatform/alloydb-java-connector/). 
    
    
    import com.zaxxer.hikari.HikariConfig;
    import com.zaxxer.hikari.HikariDataSource;
    
    public class AlloyDbJdbcConnectorDataSourceFactory {
    
      public static final String ALLOYDB_DB = System.getenv("ALLOYDB_DB");
      public static final String ALLOYDB_USER = System.getenv("ALLOYDB_USER");
      public static final String ALLOYDB_PASS = System.getenv("ALLOYDB_PASS");
      public static final String ALLOYDB_INSTANCE_NAME = System.getenv("ALLOYDB_INSTANCE_NAME");
    
      static HikariDataSource createDataSource() {
        HikariConfig config = new HikariConfig();
    
        config.setJdbcUrl(String.format("jdbc:postgresql:///%s", ALLOYDB_DB));
        config.setUsername(ALLOYDB_USER); // e.g., "postgres"
        config.setPassword(ALLOYDB_PASS); // e.g., "secret-password"
        config.addDataSourceProperty("socketFactory", "com.google.cloud.alloydb.SocketFactory");
        // e.g., "projects/my-project/locations/us-central1/clusters/my-cluster/instances/my-instance"
        config.addDataSourceProperty("alloydbInstanceName", ALLOYDB_INSTANCE_NAME);
    
        return new HikariDataSource(config);
      }
    }

**Use public IP**

If you're using public IP to connect to your AlloyDB cluster, then include the following:
    
    
    config.addDataSourceProperty("alloydbIpType", "PUBLIC");
    

**Use Private Service Connect**

If you're using Private Service Connect to connect to your AlloyDB instance, then include the following:
    
    
    config.addDataSourceProperty("alloydbIpType", "PSC");
    

**Automatic IAM authentication**

By default, AlloyDB Language Connectors use built-in authentication. You can use [automatic IAM authentication](https://docs.cloud.google.com/alloydb/docs/database-users/manage-iam-auth) with the AlloyDB Java Connector. To enable it, include the following:
    
    
    config.addDataSourceProperty("alloydbEnableIAMAuth", "true");
    

### Python (pg8000)

To use the AlloyDB Python Connector to connect to your AlloyDB cluster, configure the connector using the following steps, if you're using `pg8000`.

To use this snippet in the context of a web application, view [the README on GitHub](https://github.com/GoogleCloudPlatform/alloydb-python-connector/). 
    
    
    import sqlalchemy
    
    from google.cloud.alloydbconnector import Connector
    
    
    def create_sqlalchemy_engine(
        inst_uri: str,
        user: str,
        password: str,
        db: str,
        refresh_strategy: str = "background",
    ) -> tuple[sqlalchemy.engine.Engine, Connector]:
        """Creates a connection pool for an AlloyDB instance and returns the pool
        and the connector. Callers are responsible for closing the pool and the
        connector.
    
        A sample invocation looks like:
    
            engine, connector = create_sqlalchemy_engine(
                inst_uri,
                user,
                password,
                db,
            )
            with engine.connect() as conn:
                time = conn.execute(sqlalchemy.text("SELECT NOW()")).fetchone()
                conn.commit()
                curr_time = time[0]
                # do something with query result
                connector.close()
    
        Args:
            instance_uri (str):
                The instance URI specifies the instance relative to the project,
                region, and cluster. For example:
                "projects/my-project/locations/us-central1/clusters/my-cluster/instances/my-instance"
            user (str):
                The database user name, e.g., postgres
            password (str):
                The database user's password, e.g., secret-password
            db (str):
                The name of the database, e.g., mydb
            refresh_strategy (Optional[str]):
                Refresh strategy for the AlloyDB Connector. Can be one of "lazy"
                or "background". For serverless environments use "lazy" to avoid
                errors resulting from CPU being throttled.
        """
        connector = Connector(refresh_strategy=refresh_strategy)
    
        # create SQLAlchemy connection pool
        engine = sqlalchemy.create_engine(
            "postgresql+pg8000://",
            creator=lambda: connector.connect(
                inst_uri,
                "pg8000",
                user=user,
                password=password,
                db=db,
            ),
        )
        engine.dialect.description_encoding = None
        return engine, connector
    
    

**Use public IP**

If you're using public IP to connect to your AlloyDB cluster, then replace your connection function with the following:
    
    
      def getconn() -> pg8000.dbapi.Connection:
          conn: pg8000.dbapi.Connection = connector.connect(
              inst_uri,
              "pg8000",
              user=user,
              password=password,
              db=db,
              # use ip_type to specify public IP
              ip_type=IPTypes.PUBLIC,
          )
          return conn
    

**Use Private Service Connect**

If you're using Private Service Connect to connect to your AlloyDB instance, then include the following:
    
    
      def getconn() -> pg8000.dbapi.Connection:
          conn: pg8000.dbapi.Connection = connector.connect(
              inst_uri,
              "pg8000",
              user=user,
              password=password,
              db=db,
              # use ip_type to specify PSC
              ip_type=IPTypes.PSC,
            )
          return conn
    

**Automatic IAM authentication**

By default, AlloyDB Language Connectors use built-in authentication. You can use [automatic IAM authentication](https://docs.cloud.google.com/alloydb/docs/database-users/manage-iam-auth) with the AlloyDB Python Connector. To enable it, replace your connection function with the following:
    
    
      def getconn() -> pg8000.dbapi.Connection:
          conn: pg8000.dbapi.Connection = connector.connect(
              inst_uri,
              "pg8000",
              user=user,
              password=password,
              db=db,
              # use enable_iam_auth to enable IAM authentication
              enable_iam_auth=True,
          )
          return conn
    

### Python (asyncpg)

To use the AlloyDB Python Connector to connect to your AlloyDB cluster, configure the connector using the following steps, if you're using `asyncpg`.

To use this snippet in the context of a web application, view [the README on GitHub](https://github.com/GoogleCloudPlatform/alloydb-python-connector/). 
    
    
    import asyncpg
    import sqlalchemy
    import sqlalchemy.ext.asyncio
    
    from google.cloud.alloydbconnector import AsyncConnector
    
    
    async def create_sqlalchemy_engine(
        inst_uri: str,
        user: str,
        password: str,
        db: str,
        refresh_strategy: str = "background",
    ) -> tuple[sqlalchemy.ext.asyncio.engine.AsyncEngine, AsyncConnector]:
        """Creates a connection pool for an AlloyDB instance and returns the pool
        and the connector. Callers are responsible for closing the pool and the
        connector.
    
        A sample invocation looks like:
    
            engine, connector = await create_sqlalchemy_engine(
                inst_uri,
                user,
                password,
                db,
            )
            async with engine.connect() as conn:
                time = await conn.execute(sqlalchemy.text("SELECT NOW()")).fetchone()
                curr_time = time[0]
                # do something with query result
                await connector.close()
    
        Args:
            instance_uri (str):
                The instance URI specifies the instance relative to the project,
                region, and cluster. For example:
                "projects/my-project/locations/us-central1/clusters/my-cluster/instances/my-instance"
            user (str):
                The database user name, e.g., postgres
            password (str):
                The database user's password, e.g., secret-password
            db (str):
                The name of the database, e.g., mydb
            refresh_strategy (Optional[str]):
                Refresh strategy for the AlloyDB Connector. Can be one of "lazy"
                or "background". For serverless environments use "lazy" to avoid
                errors resulting from CPU being throttled.
        """
        connector = AsyncConnector(refresh_strategy=refresh_strategy)
    
        # create SQLAlchemy connection pool
        engine = sqlalchemy.ext.asyncio.create_async_engine(
            "postgresql+asyncpg://",
            async_creator=lambda: connector.connect(
                inst_uri,
                "asyncpg",
                user=user,
                password=password,
                db=db,
            ),
            execution_options={"isolation_level": "AUTOCOMMIT"},
        )
        return engine, connector
    
    

**Use public IP**

If you're using public IP to connect to your AlloyDB cluster, then replace your connection function with the following:
    
    
      async def getconn() -> asyncpg.Connection:
        conn: asyncpg.Connection = await connector.connect(
            inst_uri,
            "asyncpg",
            user=user,
            password=password,
            db=db,
            # use ip_type to specify public IP
            ip_type=IPTypes.PUBLIC,
        )
        return conn
    

**Use Private Service Connect**

If you're using Private Service Connect to connect to your AlloyDB instance, then include the following:
    
    
        async def getconn() -> asyncpg.Connection:
          conn: asyncpg.Connection = await connector.connect(
              inst_uri,
              "asyncpg",
              user=user,
              password=password,
              db=db,
              # use ip_type to specify PSC
              ip_type=IPTypes.PSC,
          )
          return conn
    

**Automatic IAM authentication**

By default, AlloyDB Language Connectors use built-in authentication. You can use [automatic IAM authentication](https://docs.cloud.google.com/alloydb/docs/database-users/manage-iam-auth) with the AlloyDB Python Connector. To enable it, replace your connection function with the following:
    
    
      async def getconn() -> asyncpg.Connection:
        conn: asyncpg.Connection = await connector.connect(
            inst_uri,
            "asyncpg",
            user=user,
            password=password,
            db=db,
            # use enable_iam_auth to enable IAM authentication
            enable_iam_auth=True,
        )
        return conn
    

### Go (pgx)

To use the AlloyDB Go Connector to connect to your AlloyDB cluster, configure the connector using the following steps, if you're using `pgx`.

To use this snippet in the context of a web application, view [the README on GitHub](https://github.com/GoogleCloudPlatform/alloydb-go-connector/). 
    
    
    import (
    	"context"
    	"fmt"
    	"net"
    
    	"cloud.google.com/go/alloydbconn"
    	"github.com/jackc/pgx/v5/pgxpool"
    )
    
    // connectPgx establishes a connection to your database using pgxpool and the
    // AlloyDB Go Connector (aka alloydbconn.Dialer)
    //
    // The function takes an instance URI, a username, a password, and a database
    // name. Usage looks like this:
    //
    //	pool, cleanup, err := connectPgx(
    //	  context.Background(),
    //	  "projects/myproject/locations/us-central1/clusters/mycluster/instances/myinstance",
    //	  "postgres",
    //	  "secretpassword",
    //	  "mydb",
    //	)
    //
    // In addition to a *pgxpool.Pool type, the function returns a cleanup function
    // that should be called when you're done with the database connection.
    func connectPgx(
    	ctx context.Context, instURI, user, pass, dbname string,
    	opts ...alloydbconn.[Option](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/alloydbconn/latest/index.html#cloud_google_com_go_alloydbconn_Option),
    ) (*pgxpool.Pool, func() error, error) {
    	// First initialize the dialer. alloydbconn.NewDialer accepts additional
    	// options to configure credentials, timeouts, etc.
    	//
    	// For details, see:
    	// https://pkg.go.dev/cloud.google.com/go/alloydbconn#Option
    	d, err := alloydbconn.[NewDialer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/alloydbconn/latest/index.html#cloud_google_com_go_alloydbconn_Dialer_NewDialer)(ctx, opts...)
    	if err != nil {
    		noop := func() error { return nil }
    		return nil, noop, fmt.Errorf("failed to init Dialer: %v", err)
    	}
    	// The cleanup function will stop the dialer's background refresh
    	// goroutines. Call it when you're done with your database connection to
    	// avoid a goroutine leak.
    	cleanup := func() error { return d.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/alloydbconn/latest/index.html#cloud_google_com_go_alloydbconn_Dialer_Close)() }
    
    	dsn := fmt.Sprintf(
    		// sslmode is disabled, because the Dialer will handle the SSL
    		// connection instead.
    		"user=%s password=%s dbname=%s sslmode=disable",
    		user, pass, dbname,
    	)
    
    	// Prefer pgxpool for applications.
    	// For more information, see:
    	// https://github.com/jackc/pgx/wiki/Getting-started-with-pgx#using-a-connection-pool
    	config, err := pgxpool.ParseConfig(dsn)
    	if err != nil {
    		return nil, cleanup, fmt.Errorf("failed to parse pgx config: %v", err)
    	}
    
    	// Tell pgx to use alloydbconn.Dialer to connect to the instance.
    	config.ConnConfig.DialFunc = func(ctx context.Context, _ string, _ string) (net.Conn, error) {
    		return d.[Dial](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/alloydbconn/latest/index.html#cloud_google_com_go_alloydbconn_Dialer_Dial)(ctx, instURI)
    	}
    
    	// Establish the connection.
    	pool, connErr := pgxpool.NewWithConfig(ctx, config)
    	if connErr != nil {
    		return nil, cleanup, fmt.Errorf("failed to connect: %s", connErr)
    	}
    
    	return pool, cleanup, nil
    }
    

**Use public IP**

If you're using public IP to connect to your AlloyDB cluster, then replace your `d.Dial` function with the following:
    
    
    d.Dial(ctx, instURI, alloydbconn.WithPublicIP())
    

**Use Private Service Connect**

If you're using Private Service Connect to connect to your AlloyDB instance, then include the following:
    
    
      d.Dial(ctx, instURI, alloydbconn.WithPSC())
    

**Automatic IAM authentication**

By default, AlloyDB Language Connectors use built-in authentication. You can use [automatic IAM authentication](https://docs.cloud.google.com/alloydb/docs/database-users/manage-iam-auth) with the AlloyDB Go Connector. To enable it, replace the `alloydbconn.NewDialer` function with the following:
    
    
    d, err := alloydbconn.NewDialer(ctx, alloydbconn.WithIAMAuthN())
    

**Disable built-in telemetry**

The `WithOptOutOfBuiltInTelemetry` option disables the internal metric export. By default, the Dialer reports on its internal operations to the `alloydb.googleapis.com` system metric prefix. These metrics help AlloyDB improve performance and identify client connectivity problems. This option is useful for applications that operate in environments where outbound metric exporting is restricted. To disable this telemetry, provide the following option when initializing a Dialer:
    
    
      d.Dial(ctx, instURI, alloydbconn.WithOptOutOfBuiltInTelemetry())
    

### Go (database/sql)

To use the AlloyDB Go Connector to connect to your AlloyDB cluster, configure the connector using the following steps, if you're using `database/sql`.

To use this snippet in the context of a web application, view [the README on GitHub](https://github.com/GoogleCloudPlatform/alloydb-go-connector/). 
    
    
    import (
    	"database/sql"
    	"fmt"
    
    	"cloud.google.com/go/alloydbconn"
    	"cloud.google.com/go/alloydbconn/driver/postgres"
    )
    
    // connectDatabaseSQL establishes a connection to your database using the Go
    // standard library's database/sql package and using the AlloyDB Go Connector
    // (aka alloydbconn.Dialer)
    //
    // The function takes an instance URI, a username, a password, and a database
    // name. Usage looks like this:
    //
    //	db, cleanup, err := connectDatabaseSQL(
    //	  "projects/myproject/locations/us-central1/clusters/mycluster/instances/myinstance",
    //	  "postgres",
    //	  "secretpassword",
    //	  "mydb",
    //	)
    //
    // In addition to a *db.SQL type, the function returns a cleanup function that
    // should be called when you're done with the database connection.
    func connectDatabaseSQL(
    	instURI, user, pass, dbname string,
    	opts ...alloydbconn.[Option](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/alloydbconn/latest/index.html#cloud_google_com_go_alloydbconn_Option),
    ) (*sql.DB, func() error, error) {
    	// First, register the AlloyDB driver. Note, the driver's name is arbitrary
    	// and must only match what you use below in sql.Open. Also,
    	// postgres.RegisterDriver accepts options to configure credentials, timeouts,
    	// etc.
    	//
    	// For details, see:
    	// https://pkg.go.dev/cloud.google.com/go/alloydbconn#Option
    	//
    	// The cleanup function will stop the dialer's background refresh
    	// goroutines. Call it when you're done with your database connection to
    	// avoid a goroutine leak.
    	cleanup, err := postgres.[RegisterDriver](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/alloydbconn/latest/driver/postgres.html#cloud_google_com_go_alloydbconn_driver_postgres_RegisterDriver)("alloydb", opts...)
    	if err != nil {
    		return nil, cleanup, err
    	}
    
    	db, err := sql.Open(
    		"alloydb",
    		fmt.Sprintf(
    			// sslmode is disabled, because the Dialer will handle the SSL
    			// connection instead.
    			"host=%s user=%s password=%s dbname=%s sslmode=disable",
    			instURI, user, pass, dbname,
    		),
    	)
    	return db, cleanup, err
    }
    

**Use public IP**

If you're using public IP to connect to your AlloyDB cluster, then replace your `RegisterDriver` function with the following:
    
    
    cleanup, err := postgres.RegisterDriver(
      "alloydb",
      alloydbconn.WithDefaultDialOptions(alloydbconn.WithPublicIP()),
    )
    

**Use Private Service Connect**

If you're using Private Service Connect to connect to your AlloyDB instance, then include the following:
    
    
    cleanup, err := postgres.RegisterDriver(
      "alloydb",
      alloydbconn.WithDefaultDialOptions(alloydbconn.WithPSC()),
    )
    

**Automatic IAM authentication**

By default, AlloyDB Language Connectors use built-in authentication. You can use [automatic IAM authentication](https://docs.cloud.google.com/alloydb/docs/database-users/manage-iam-auth) with the AlloyDB Go Connector. To enable it, replace your `RegisterDriver` function with the following:
    
    
    cleanup, err := postgres.RegisterDriver(
      "alloydb",
      alloydbconn.WithIAMAuthN(),
    )
    

**Disable built-in telemetry**

The `WithOptOutOfBuiltInTelemetry` option disables the internal metric export. By default, the Dialer reports on its internal operations to the `alloydb.googleapis.com` system metric prefix. These metrics help AlloyDB improve performance and identify client connectivity problems. This option is useful for applications that operate in environments where outbound metric exporting is restricted. To disable this telemetry, provide the following option when initializing a Dialer:
    
    
    cleanup, err := postgres.RegisterDriver(
      "alloydb",
      alloydbconn.WithOptOutOfBuiltInTelemetry(),
    )
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
