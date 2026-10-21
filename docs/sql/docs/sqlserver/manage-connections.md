---
url: https://docs.cloud.google.com/sql/docs/sqlserver/manage-connections/
title: Manage database connections \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:28:53.623671+00:00
---

# Manage database connections  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/manage-connections/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/sqlserver/features)



Send feedback 

#  Manage database connections Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/manage-connections "View this page for the MySQL database engine") | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/manage-connections "View this page for the PostgreSQL database engine") | SQL Server

This page provides best practices and language-specific code samples to help you create applications that use Cloud SQL database connections effectively.

These samples are excerpts from a complete web application available to you on GitHub. Learn more.

**For step-by-step instructions on running a sample web application connected to Cloud SQL,** follow the link for your environment:

  * [Quickstart for connecting from your local computer](https://docs.cloud.google.com/sql/docs/sqlserver/connect-instance-local-computer)
  * [Quickstart for connecting from Compute Engine](https://docs.cloud.google.com/sql/docs/sqlserver/connect-instance-compute-engine)
  * [Quickstart for connecting from Cloud Run](https://docs.cloud.google.com/sql/docs/sqlserver/connect-instance-cloud-run)
  * [Quickstart for connecting from Cloud Run functions](https://docs.cloud.google.com/sql/docs/sqlserver/connect-instance-cloud-functions)
  * [Quickstart for connecting from Google Kubernetes Engine](https://docs.cloud.google.com/sql/docs/postgres/connect-instance-kubernetes)



## Connection pools

A connection pool is a cache of database connections that are shared and reused to improve connection latency and performance. When your application needs a database connection, it borrows one from its pool temporarily; when the application is finished with the connection, it returns the connection to the pool, where it can be reused the next time the application needs a database connection.

## Open and close connections

When you use a connection pool, you must open and close connections properly, so that your connections are always returned to the pool when you are done with them. Unreturned or "leaked" connections are not reused, which wastes resources and can cause performance bottlenecks for your application.

### Python
    
    
    # Preparing a statement before hand can help protect against injections.
    stmt = sqlalchemy.text(
        "INSERT INTO votes (time_cast, candidate) VALUES (:time_cast, :candidate)"
    )
    try:
        # Using a with statement ensures that the connection is always released
        # back into the pool at the end of statement (even if an error occurs)
        with db.connect() as conn:
            conn.execute(stmt, parameters={"time_cast": time_cast, "candidate": team})
            conn.commit()
    except Exception as e:
        # If something goes wrong, handle the error in this section. This might
        # involve retrying or adjusting parameters depending on the situation.
        # ...

### Java
    
    
    // Using a try-with-resources statement ensures that the connection is always released back
    // into the pool at the end of the statement (even if an error occurs)
    try (Connection conn = pool.getConnection()) {
    
      // PreparedStatements can be more efficient and project against injections.
      PreparedStatement voteStmt = conn.prepareStatement(
          "INSERT INTO votes (time_cast, candidate) VALUES (?, ?);");
      voteStmt.setTimestamp(1, now);
      voteStmt.setString(2, team);
    
      // Finally, execute the statement. If it fails, an error will be thrown.
      voteStmt.execute();
    
    } catch (SQLException ex) {
      // If something goes wrong, handle the error in this section. This might involve retrying or
      // adjusting parameters depending on the situation.
      // ...
    }

### Node.js
    
    
    try {
      const stmt =
        'INSERT INTO votes (time_cast, candidate) VALUES (@timestamp, @team)';
      // Using a prepared statement protects against SQL injection attacks.
      // When prepare is called, a single connection is acquired from the connection pool
      // and all subsequent executions are executed exclusively on this connection.
      const ps = new mssql.PreparedStatement(pool);
      ps.input('timestamp', mssql.DateTime);
      ps.input('team', mssql.VarChar(6));
      await ps.prepare(stmt);
      await ps.execute({
        timestamp: timestamp,
        team: team,
      });
      await ps.unprepare();
    } catch (err) {
      // If something goes wrong, handle the error in this section. This might
      // involve retrying or adjusting parameters depending on the situation.
      // ...
    }

### C#
    
    
    using Microsoft.Data.SqlClient;
    using System;
    
    namespace CloudSql
    {
        public class SqlServerTcp
        {
            public static SqlConnectionStringBuilder NewSqlServerTCPConnectionString()
            {
                // Equivalent connection string:
                // "User Id=<DB_USER>;Password=<DB_PASS>;Server=<INSTANCE_HOST>;Database=<DB_NAME>;"
                var connectionString = new SqlConnectionStringBuilder()
                {
                    // Note: Saving credentials in environment variables is convenient, but not
                    // secure - consider a more secure solution such as
                    // Cloud Secret Manager (https://cloud.google.com/secret-manager) to help
                    // keep secrets safe.
                    DataSource = Environment.GetEnvironmentVariable("INSTANCE_HOST"), // e.g. '127.0.0.1'
                    // Set Host to 'cloudsql' when deploying to App Engine Flexible environment
                    UserID = Environment.GetEnvironmentVariable("DB_USER"),         // e.g. 'my-db-user'
                    Password = Environment.GetEnvironmentVariable("DB_PASS"),       // e.g. 'my-db-password'
                    InitialCatalog = Environment.GetEnvironmentVariable("DB_NAME"), // e.g. 'my-database'
    
                    // The Cloud SQL proxy provides encryption between the proxy and instance
                    Encrypt = false,
                };
                connectionString.Pooling = true;
                // Specify additional properties here.
                return connectionString;
            }
        }
    }

### Go
    
    
    insertVote := "INSERT INTO votes (candidate, created_at) VALUES (@TEAM, GETDATE())"
    _, err := db.Exec(insertVote, sql.Named("TEAM", team))

### Ruby
    
    
    @vote = Vote.new candidate: candidate
    
    # ActiveRecord creates and executes your SQL and automatically
    # handles the opening and closing of the database connection.
    if @vote.save
      render json: "Vote successfully cast for \"#{@vote.candidate}\" at #{@vote.time_cast} PST!"
    else
      render json: @vote.errors, status: :unprocessable_entity
    end

### PHP
    
    
    // Use prepared statements to guard against SQL injection.
    $sql = 'INSERT INTO votes (time_cast, candidate) VALUES (GETDATE(), :voteValue)';
    
    try {
        $statement = $conn->prepare($sql);
        $statement->bindParam('voteValue', $value);
    
        $res = $statement->execute();
    } catch (PDOException $e) {
        throw new RuntimeException(
            'Could not insert vote into database. The PDO exception was ' .
            $e->getMessage(),
            $e->getCode(),
            $e
        );
    }

**Note:** Most PHP applications are not long-running. They start at the beginning of request processing and shut down when request processing ends. Database connections are closed when the application shuts down.

## Connection count

Every database connection uses client and server-side resources. In addition, Cloud SQL imposes overall connection limits that cannot be exceeded. Creating and using fewer connections reduces overhead and helps you stay under the connection limit.

### Python
    
    
    # Pool size is the maximum number of permanent connections to keep.
    pool_size=5,
    # Temporarily exceeds the set pool_size if no connections are available.
    max_overflow=2,
    # The total number of concurrent connections for your application will be
    # a total of pool_size and max_overflow.

### Java
    
    
    // maximumPoolSize limits the total number of concurrent connections this pool will keep. Ideal
    // values for this setting are highly variable on app design, infrastructure, and database.
    config.setMaximumPoolSize(5);
    // minimumIdle is the minimum number of idle connections Hikari maintains in the pool.
    // Additional connections will be established to meet this value unless the pool is full.
    config.setMinimumIdle(5);

### Node.js
    
    
      // 'max' limits the total number of concurrent connections this pool will keep. Ideal
      // values for this setting are highly variable on app design, infrastructure, and database.
      (config.pool.max = 5);
    // 'min' is the minimum number of idle connections maintained in the pool.
    // Additional connections will be established to meet this value unless the pool is full.
    config.pool.min = 1;

### C#
    
    
    // MaximumPoolSize sets maximum number of connections allowed in the pool.
    connectionString.MaxPoolSize = 5;
    // MinimumPoolSize sets the minimum number of connections in the pool.
    connectionString.MinPoolSize = 0;
    

### Go
    
    
    // Set maximum number of connections in idle connection pool.
    db.SetMaxIdleConns(5)
    
    // Set maximum number of open connections to the database.
    db.SetMaxOpenConns(7)

### Ruby
    
    
    # 'pool' is the maximum number of permanent connections to keep.
    pool: 5

### PHP

[PDO](https://www.php.net/manual/en/book.pdo.php) currently doesn't offer any functionality to configure connection limits.

## Exponential backoff

If your application attempts to connect to the database and does not succeed, the database could be temporarily unavailable. In this case, sending repeated connection requests wastes resources. It is preferable to wait before sending additional connection requests in order to allow the database to become accessible again. Using an exponential backoff or other delay mechanism achieves this goal.

This retry only makes sense when first connecting, or when first grabbing a connection from the pool. If errors happen in the middle of a transaction, the _application_ must do the retrying, and it must retry from the beginning of a transaction. So even if your pool is configured properly, the application might still see errors if connections are lost.

### Python
    
    
    # SQLAlchemy automatically uses delays between failed connection attempts,
    # but provides no arguments for configuration.

### Java
    
    
    // Hikari automatically delays between failed connection attempts, eventually reaching a
    // maximum delay of `connectionTimeout / 2` between attempts.

### Node.js
    
    
    // The node-mssql module uses a built-in retry strategy which does not implement backoff.
    // 'createRetryIntervalMillis' is the number of milliseconds to wait in between retries.
    config.pool.createRetryIntervalMillis = 200;

### C#
    
    
    Policy
        .Handle<SqlException>()
        .WaitAndRetry(new[]
        {
            TimeSpan.FromSeconds(1),
            TimeSpan.FromSeconds(2),
            TimeSpan.FromSeconds(5)
        })
        .Execute(() => connection.Open());
    

### Go

The [database/sql](http://go-database-sql.org/) package currently doesn't offer any functionality to configure exponential backoff.

### Ruby
    
    
    # ActiveRecord automatically uses delays between failed connection attempts,
    # but provides no arguments for configuration.

### PHP

[PDO](https://www.php.net/manual/en/book.pdo.php) currently doesn't offer any functionality to configure exponential backoff.

## Connection timeout

There are many reasons why a connection attempt might not succeed. Network communication is never guaranteed, and the database might be temporarily unable to respond. Make sure your application handles broken or unsuccessful connections gracefully.

### Python
    
    
    # 'pool_timeout' is the maximum number of seconds to wait when retrieving a
    # new connection from the pool. After the specified amount of time, an
    # exception will be thrown.
    pool_timeout=30,  # 30 seconds

### Java
    
    
    // setConnectionTimeout is the maximum number of milliseconds to wait for a connection checkout.
    // Any attempt to retrieve a connection from this pool that exceeds the set limit will throw an
    // SQLException.
    config.setConnectionTimeout(10000); // 10 seconds
    // idleTimeout is the maximum amount of time a connection can sit in the pool. Connections that
    // sit idle for this many milliseconds are retried if minimumIdle is exceeded.
    config.setIdleTimeout(600000); // 10 minutes

### Node.js
    
    
    // 'connectionTimeout` is the maximum number of milliseconds to wait trying to establish an
    // initial connection. After the specified amount of time, an exception will be thrown.
    config.connectionTimeout = 30000;
    // 'acquireTimeoutMillis' is the number of milliseconds before a timeout occurs when acquiring a
    // connection from the pool.
    config.pool.acquireTimeoutMillis = 30000;
    // 'idleTimeoutMillis' is the number of milliseconds a connection must sit idle in the pool
    // and not be checked out before it is automatically closed
    (config.pool.idleTimeoutMillis = 600000),

### C#
    
    
    // ConnectionTimeout sets the time to wait (in seconds) while
    // trying to establish a connection before terminating the attempt.
    connectionString.ConnectTimeout = 15;
    

### Go

The [database/sql](http://go-database-sql.org/) package currently doesn't offer any functionality to configure connection timeout. Timeout is configured at the driver level.

### Ruby
    
    
    # 'timeout' is the maximum number of seconds to wait when retrieving a
    # new connection from the pool. After the specified amount of time, an
    # ActiveRecord::ConnectionTimeoutError will be raised.
    timeout: 5000

### PHP
    
    
    // Here we set the connection timeout to five seconds and ask PDO to
    // throw an exception if any errors occur.
    [
        PDO::ATTR_TIMEOUT => 5,
        PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    ]

## Connection duration

Limiting a connection's lifetime can help prevent abandoned connections from accumulating. You can use the connection pool to limit your connection lifetimes.

### Python
    
    
    # 'pool_recycle' is the maximum number of seconds a connection can persist.
    # Connections that live longer than the specified amount of time will be
    # re-established
    pool_recycle=1800,  # 30 minutes

### Java
    
    
    // maxLifetime is the maximum possible lifetime of a connection in the pool. Connections that
    // live longer than this many milliseconds will be closed and reestablished between uses. This
    // value should be several minutes shorter than the database's timeout value to avoid unexpected
    // terminations.
    config.setMaxLifetime(1800000); // 30 minutes

### Node.js

The '[node-mssql](https://github.com/tediousjs/node-mssql)' Node.js library currently doesn't offer any functionality to control the duration of a connection.

### C#
    
    
    // ADO.NET connection pooler removes a connection
    // from the pool after it's been idle for approximately
    // 4-8 minutes, or if the pooler detects that the
    // connection with the server no longer exists.
    

### Go
    
    
    // Set Maximum time (in seconds) that a connection can remain open.
    db.SetConnMaxLifetime(1800 * time.Second)

### Ruby

[ActiveRecord](https://github.com/rails/rails/tree/master/activerecord) currently doesn't offer any functionality to control the duration of a connection.

### PHP

[PDO](https://www.php.net/manual/en/book.pdo.php) currently doesn't offer any functionality to control the duration of a connection.

## View the complete application

To see the complete application, click the link below.

### Python

View the [complete application](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/cloud-sql/sql-server/sqlalchemy/README.md) for the Python programming language.

### Node.js

View the [complete application](https://github.com/GoogleCloudPlatform/nodejs-docs-samples/blob/master/cloud-sql/sqlserver/mssql/README.md) for the Node.js programming language.

### C#

View the [complete application](https://github.com/GoogleCloudPlatform/dotnet-docs-samples/blob/master/cloud-sql/sql-server/README.md) for the C# programming language.

### Go

View the [complete application](https://github.com/GoogleCloudPlatform/golang-samples/blob/master/cloudsql/sqlserver/database-sql/README.md) for the Go programming language.

### PHP

View the [complete application](https://github.com/GoogleCloudPlatform/php-docs-samples/tree/main/cloud_sql/sqlserver/pdo) for the PHP programming language.

## What's next

  * Learn more about [Private IP](https://docs.cloud.google.com/sql/docs/sqlserver/private-ip).
  * Learn about [quotas and limits](https://docs.cloud.google.com/sql/docs/sqlserver/quotas) for Cloud SQL and App Engine.
  * Learn about [best practices](https://docs.cloud.google.com/sql/docs/sqlserver/best-practices) for working with Cloud SQL. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
