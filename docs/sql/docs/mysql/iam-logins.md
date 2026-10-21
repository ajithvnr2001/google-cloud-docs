---
url: https://docs.cloud.google.com/sql/docs/mysql/iam-logins/
title: Log in using IAM database authentication \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:29:27.367905+00:00
---

# Log in using IAM database authentication  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/iam-logins/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Log in using IAM database authentication Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/iam-logins "View this page for the PostgreSQL database engine") | SQL Server

This page describes how users and service accounts can log in to Cloud SQL databases using Cloud SQL IAM database authentication. For more information, see [IAM authentication](https://docs.cloud.google.com/sql/docs/mysql/iam-authentication).

## Before you begin

  * Configure the instance to use IAM database authentication. For more information, see [Configure new instances for IAM database authentication](https://docs.cloud.google.com/sql/docs/mysql/create-edit-iam-instances#configure-iam-db-instance).
  * Add an IAM user, service account, or group to the database. For more information, see [Add an IAM user or service account to the database](https://docs.cloud.google.com/sql/docs/mysql/add-manage-iam-users#creating-a-database-user) and [Add a group to the database](https://docs.cloud.google.com/sql/docs/mysql/add-manage-iam-users#add-iam-group-db).
  * Add the [`roles/cloudsql.instanceUser`](https://docs.cloud.google.com/sql/docs/mysql/iam-roles) IAM role to your IAM user, service account, or group. It's a predefined role that contains the necessary Cloud SQL IAM `cloudsql.instances.login` permission. You need this permission to login to a database instance with IAM database authentication. For more information, see [Roles and permissions](https://docs.cloud.google.com/sql/docs/mysql/roles-and-permissions#introduction).
  * If you're using the Cloud SQL Auth Proxy, then add the [`roles/cloudsql.client`](https://docs.cloud.google.com/sql/docs/mysql/iam-roles) IAM role to your IAM user, service account, or group. It's a predefined role that contains the necessary Cloud SQL IAM `cloudsql.instances.connect` permission. You need this permission to login to a database instance with the Cloud SQL Auth Proxy. For more information, see the following: 
    * [Roles and permissions](https://docs.cloud.google.com/sql/docs/mysql/roles-and-permissions#introduction)
    * [Install Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/mysql/sql-proxy)
  * When an IAM user is added to a database, by default the new database user has no privileges to any database. To provide the user with the required database privileges, you can [assign database roles while you add the IAM account](https://docs.cloud.google.com/sql/docs/mysql/add-manage-iam-users#add-db-roles) to the instance, [assign database roles while you update the IAM account](https://docs.cloud.google.com/sql/docs/mysql/add-manage-iam-users#update-revoke-db-roles) on the instance, or you can use the `GRANT` command to grant privileges to the [individual IAM account](https://docs.cloud.google.com/sql/docs/mysql/add-manage-iam-users#grant-db-privileges) or [IAM group](https://docs.cloud.google.com/sql/docs/mysql/\(/sql/docs/mysql/add-manage-iam-users#grant-db-priv-to-group\)).
  * If you're using IAM group authentication, then the IAM user or service account must be a member of a group that has been granted an IAM role or permissions to log in to the Cloud SQL instance. Cloud SQL creates an account after the user or service account logs in to the instance for the first time.



## Log in with automatic IAM database authentication

You can configure a Cloud SQL connector to automatically handle authentication to the Cloud SQL instance on behalf of a user or an application. Connectors include the Cloud SQL Auth Proxy, the Go connector, the Java connector, and the Python connector, all of which support automatic IAM database authentication. When using a Cloud SQL connector with automatic IAM database authentication, the IAM account that you use to start the connector must be the same account that authenticates to the database.

**Note:** You must allow outgoing (or egress) TCP connections to ports `443` and `3307`.

  * Cloud SQL Connectors call APIs through the `sqladmin.googleapis.com` domain name. This domain name doesn't have a fixed IP address. Therefore, you must allow all egress TCP connections on port `443`. (Port `443` is the standard HTTPS port. Whenever you go to a website or make an API request, the secure connection goes through port `443` of the IP address to which the website or endpoint resolves.)
  * While Cloud SQL Connectors can listen on any port, they create outgoing (or egress) connections to your Cloud SQL instance only on port `3307`. If your client machine has an outbound firewall policy, then make sure it allows outgoing connections to port `3307` on your Cloud SQL instance's IP address. For more information, see [Options for authenticating Cloud SQL Connectors](https://docs.cloud.google.com/sql/docs/mysql/connect-auth-proxy#authentication-options).



To log in using automatic IAM database authentication:

###  Cloud SQL Auth Proxy 

**Important:** If you use the `cloud_sql_proxy` binary or the `--enable_iam_login` flag to start the Cloud SQL Auth Proxy, then you are using v1 of the Cloud SQL Auth Proxy. Migrate to v2, `cloud-sql-proxy`, and use the `--auto-iam-authn` flag for IAM database authentication. For more information about migrating to v2, see [Migrating from v1 to v2](https://github.com/GoogleCloudPlatform/cloud-sql-proxy/blob/main/migration-guide.md).

  1. Authenticate to Google Cloud.

**User**

Authenticate to Google Cloud using Application Default Credentials (ADC).

Use the [`gcloud auth application-default login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/application-default/login) command. For more information, see [Set up Application Default Credentials](https://docs.cloud.google.com/docs/authentication/provide-credentials-adc).

**Service account**

To authenticate to Google Cloud using ADC with a service account, you can use service account impersonation or set up a service account key. If you want to authenticate with service account impersonation, replace SERVICE_ACCOUNT_EMAIL_ADDRESS, and run the following command:
         
         gcloud auth application-default login --impersonate-service-account SERVICE_ACCOUNT_EMAIL_ADDRESS

For more information, see [Set up Application Default Credentials](https://docs.cloud.google.com/docs/authentication/provide-credentials-adc).

  2. Start the Cloud SQL Auth Proxy with the `--auto-iam-authn` flag Replace INSTANCE_CONNECTION_NAME with the connection string used to identify the Cloud SQL instance. If you are using a port other than the default MySQL port, then specify the port number. For more information on how to find and construct this string, see [Options for authenticating the Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/mysql/connect-auth-proxy#authentication-options).
         
         ./cloud-sql-proxy --auto-iam-authn INSTANCE_CONNECTION_NAME

For more information on how to start the proxy, see [Start the Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/mysql/connect-auth-proxy#start-proxy).

**Warning:** If you run the Cloud SQL Auth Proxy as a service, keep in mind that it requests the access tokens on behalf of your applications. For this reason, ensure that only trusted users are able to access the address and port or the Unix socket that the Cloud SQL Auth Proxy is listening on.
  3. When you are ready to connect to the instance by using the Cloud SQL Auth Proxy, log in with the `mysql` client. Replace the following:

     * HOSTNAME: IP address used by the Cloud SQL Auth Proxy. By default, the Cloud SQL Auth Proxy uses the localhost address of `127.0.0.1`, but you can assign a different IP address when you start the Cloud SQL Auth Proxy.
     * USERNAME: For an IAM user account, this is the user's email address, without the `@` symbol or domain name. For example, for `test-user@example.com`, enter `test-user`. For a service account, this is the service account's email address without the `@_project-id_.iam.gserviceaccount.com` suffix.
     * PORT_NUMBER: Optional. If you specified a different port in the instance connection string, then specify that port number.

Run the following command:
    
    mysql --host=HOSTNAME \
    --user=USERNAME \
    --port=PORT_NUMBER

For more information on how to connect to the Cloud SQL Auth Proxy, see [Connect with the mysql client](https://docs.cloud.google.com/sql/docs/mysql/connect-auth-proxy#connect-to-proxy).




###  Go 
    
    
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
    
    func connectWithConnectorIAMAuthN() (*sql.DB, error) {
    	mustGetenv := func(k string) string {
    		v := os.Getenv(k)
    		if v == "" {
    			log.Fatalf("Warning: %s environment variable not set.", k)
    		}
    		return v
    	}
    	// Note: Saving credentials in environment variables is convenient, but not
    	// secure - consider a more secure solution such as
    	// Cloud Secret Manager (https://cloud.google.com/secret-manager) to help
    	// keep secrets safe.
    	var (
    		dbUser                 = mustGetenv("DB_IAM_USER")              // e.g. 'service-account-name'
    		dbName                 = mustGetenv("DB_NAME")                  // e.g. 'my-database'
    		instanceConnectionName = mustGetenv("INSTANCE_CONNECTION_NAME") // e.g. 'project:region:instance'
    		usePrivate             = os.Getenv("PRIVATE_IP")
    	)
    
    	// WithLazyRefresh() Option is used to perform refresh
    	// when needed, rather than on a scheduled interval.
    	// This is recommended for serverless environments to
    	// avoid background refreshes from throttling CPU.
    	d, err := cloudsqlconn.[NewDialer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudsqlconn/latest/index.html#cloud_google_com_go_cloudsqlconn_Dialer_NewDialer)(
    		context.Background(),
    		cloudsqlconn.[WithIAMAuthN](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudsqlconn/latest/index.html#cloud_google_com_go_cloudsqlconn_Option_WithIAMAuthN)(),
    		cloudsqlconn.[WithLazyRefresh](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudsqlconn/latest/index.html#cloud_google_com_go_cloudsqlconn_Option_WithLazyRefresh)(),
    	)
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
    
    	dbURI := fmt.Sprintf("%s:empty@cloudsqlconn(localhost:3306)/%s?parseTime=true",
    		dbUser, dbName)
    
    	dbPool, err := sql.Open("mysql", dbURI)
    	if err != nil {
    		return nil, fmt.Errorf("sql.Open: %w", err)
    	}
    	return dbPool, nil
    }
    

###  Java JDBC 
    
    
    import com.zaxxer.hikari.HikariConfig;
    import com.zaxxer.hikari.HikariDataSource;
    import javax.sql.DataSource;
    
    public class ConnectorIamAuthnConnectionPoolFactory extends ConnectionPoolFactory {
    
      // Note: Saving credentials in environment variables is convenient, but not
      // secure - consider a more secure solution such as
      // Cloud Secret Manager (https://cloud.google.com/secret-manager) to help
      // keep secrets safe.
      private static final String INSTANCE_CONNECTION_NAME =
          System.getenv("INSTANCE_CONNECTION_NAME");
      private static final String INSTANCE_UNIX_SOCKET = System.getenv("INSTANCE_UNIX_SOCKET");
      private static final String DB_IAM_USER = System.getenv("DB_IAM_USER");
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
    
        config.addDataSourceProperty("socketFactory", "com.google.cloud.sql.mysql.SocketFactory");
        config.addDataSourceProperty("cloudSqlInstance", INSTANCE_CONNECTION_NAME);
    
        // If connecting using automatic database authentication, follow the instructions for
        // connecting using the connector, but set the DB_IAM_USER value to an IAM user or
        // service account that has been given access to the database.
        // See https://cloud.google.com/sql/docs/postgres/iam-logins for more details.
        config.addDataSourceProperty("enableIamAuth", "true");
        config.addDataSourceProperty("user", DB_IAM_USER);
        // Explicitly set sslmode to disable to prevent driver from hanging.
        // The Java Connector will handle SSL so it is unneccesary to enable it at the driver level.
        config.addDataSourceProperty("sslmode", "disable");
    
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

###  Java R2DBC 
    
    
    // Set up ConnectionFactoryOptions
    ConnectionFactoryOptions options =
        ConnectionFactoryOptions.builder()
            .option(DRIVER, "gcp")
            .option(PROTOCOL, "mysql")
            .option(USER, DB_USER)
            .option(DATABASE, DB_NAME)
            .option(HOST, CONNECTION_NAME)
            .option(IP_TYPES, IP_TYPE)
            .option(ENABLE_IAM_AUTH, true)
            .build();
    
    // Initialize connection pool
    ConnectionFactory connectionFactory = ConnectionFactories.get(options);
    ConnectionPoolConfiguration configuration =
        ConnectionPoolConfiguration.builder(connectionFactory).build();
    
    this.connectionPool = new ConnectionPool(configuration);

###  Node.js 
    
    
    const mysql = require('mysql2/promise');
    const {Connector} = require('@google-cloud/cloud-sql-connector');
    
    // In case the PRIVATE_IP environment variable is defined then we set
    // the ipType=PRIVATE for the new connector instance, otherwise defaults
    // to public ip type.
    const getIpType = () =>
      process.env.PRIVATE_IP === '1' || process.env.PRIVATE_IP === 'true'
        ? 'PRIVATE'
        : 'PUBLIC';
    
    // connectWithConnectorAutoIAMAuthn initializes a connection pool for a Cloud SQL instance
    // of MySQL using the Cloud SQL Node.js Connector.
    const connectWithConnectorAutoIAMAuthn = async config => {
      // Note: Saving credentials in environment variables is convenient, but not
      // secure - consider a more secure solution such as
      // Cloud Secret Manager (https://cloud.google.com/secret-manager) to help
      // keep secrets safe.
      const connector = new Connector();
      const clientOpts = await connector.getOptions({
        instanceConnectionName: process.env.INSTANCE_CONNECTION_NAME,
        ipType: getIpType(),
        authType: 'IAM',
      });
      const dbConfig = {
        ...clientOpts,
        user: process.env.IAM_DB_USER, // e.g. 'service-account-name'
        database: process.env.DB_NAME, // e.g. 'my-database'
        // ... Specify additional properties here.
        ...config,
      };
      // Establish a connection to the database.
      return mysql.createPool(dbConfig);
    };

###  Python 
    
    
    import os
    
    from google.cloud.sql.connector import Connector, IPTypes
    import pymysql
    
    import sqlalchemy
    
    
    def connect_with_connector_auto_iam_authn() -> sqlalchemy.engine.base.Engine:
        """
        Initializes a connection pool for a Cloud SQL instance of MySQL.
    
        Uses the Cloud SQL Python Connector with Automatic IAM Database Authentication.
        """
        # Note: Saving credentials in environment variables is convenient, but not
        # secure - consider a more secure solution such as
        # Cloud Secret Manager (https://cloud.google.com/secret-manager) to help
        # keep secrets safe.
        instance_connection_name = os.environ[
            "INSTANCE_CONNECTION_NAME"
        ]  # e.g. 'project:region:instance'
        db_iam_user = os.environ["DB_IAM_USER"]  # e.g. 'service-account-name'
        db_name = os.environ["DB_NAME"]  # e.g. 'my-database'
    
        ip_type = IPTypes.PRIVATE if os.environ.get("PRIVATE_IP") else IPTypes.PUBLIC
    
        # initialize Cloud SQL Python Connector object
        connector = Connector(refresh_strategy="LAZY")
    
        def getconn() -> pymysql.connections.Connection:
            conn: pymysql.connections.Connection = connector.connect(
                instance_connection_name,
                "pymysql",
                user=db_iam_user,
                db=db_name,
                enable_iam_auth=True,
                ip_type=ip_type,
            )
            return conn
    
        # The Cloud SQL Python Connector can be used with SQLAlchemy
        # using the 'creator' argument to 'create_engine'
        pool = sqlalchemy.create_engine(
            "mysql+pymysql://",
            creator=getconn,
            # ...
        )
        return pool
    
    

To open an interactive example for Cloud SQL Python Connector, click [here](https://colab.research.google.com/github/GoogleCloudPlatform/cloud-sql-python-connector/blob/main/samples/notebooks/postgres_python_connector.ipynb#scrollTo=GCsS4f5UCYUa).

## Log in with manual IAM database authentication

**Note:** If you plan to use the Cloud SQL Auth Proxy, the Go connector, the Java connector, or the Python connector, then see [Log in with automatic IAM database authentication](https://docs.cloud.google.com/sql/docs/mysql/iam-logins#log-in-with-automatic).

A user or an application can authenticate to the database using IAM by manually requesting an access token from Google Cloud and presenting it to the database. Using the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud), you can explicitly request an [OAuth 2.0](https://developers.google.com/identity/protocols/oauth2) token with the Cloud SQL Admin API scope that is used to log in to the database. When you log in as a database user with manual IAM database authentication, you use your email address as the username and the access token as the password. You can use this method with either a direct connection to the database or with a Cloud SQL connector.

In this procedure, you authenticate to Google Cloud, request an access token, and then connect to the database by passing in the token as the password for the IAM database user. Use these steps to connect without the [Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/sql-proxy).

For these steps, you must:

  * Use the [\--enable-cleartext-plugin](https://dev.mysql.com/doc/refman/8.0/en/mysql-command-options.html#option_mysql_enable-cleartext-plugin) `mysql` option.
  * If you are connecting to an instance with public IP, authorize external access to the instance. For more information, see [Authorize your machine's IP address for public IP](https://docs.cloud.google.com/sql/docs/mysql/authorize-networks#console).
  * If you are connecting to an instance with private IP, run the command within the Virtual Private Cloud (VPC) network.
  * Use the [`gcloud sql generate-login-token`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/generate-login-token) command to generate your authentication token.



To log in using manual IAM database authentication:

###  gcloud 

  1. Authenticate to Google Cloud.

**User**

Authenticate to IAM using [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login). For more information, see [Authenticate for the gcloud CLI](https://docs.cloud.google.com/sdk/docs/authenticate#user-accounts).

**Service account**

Authenticate to IAM using [`gcloud auth activate-service-account`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/activate-service-account). For more information, see [Authenticate for the gcloud CLI](https://docs.cloud.google.com/sdk/docs/authenticate#user-accounts).

  2. Request the access token, and log in with a client.

**Warning:** You can use your OAuth 2.0 token to make authenticated requests on your behalf. Make sure to keep it secure, and be careful where you store it. 

Replace the following:

     * HOSTNAME: The IP address of the instance, either the public IP address or private IP address. 
     * USERNAME: For an IAM user account, this is the user's email address, without the `@` symbol or domain name. For example, for `test-user@example.com`, enter `test-user`. For a service account, this is the service account's email address without the `@_project-id_.iam.gserviceaccount.com` suffix. 
    
    export MYSQL_PWD=`gcloud sql generate-login-token` \
     mysql --enable-cleartext-plugin \
     --ssl-mode=REQUIRED \
     --host=HOSTNAME \
     --user=USERNAME
     

If [`ssl_mode`](https://docs.cloud.google.com/sql/docs/mysql/configure-ssl-instance#enforcing-ssl) on your Cloud SQL instance is configured to `TRUSTED_CLIENT_CERTIFICATE_REQUIRED`, then include a client certificate and client key when you log in. In addition, to let the client verify the server's identity for mutual authentication, specify the server certificate `server-ca.pem`. For example:
    
    export MYSQL_PWD=`gcloud sql generate-login-token` \
     mysql --enable-cleartext-plugin \
     --ssl-mode=VERIFY_CA \
     --ssl-ca=server-ca.pem \
     --ssl-cert=client-cert.pem \
     --ssl-key=client-key.pem \
     --host=HOSTNAME \
     --user=USERNAME
     

For information on how to create a client certificate and key, see [Client certificates](https://docs.cloud.google.com/sql/docs/mysql/configure-ssl-instance#client-certs). 

**Note:** The OAuth 2.0 token can't be entered or pasted directly into a password field, because that token is longer than the field's maximum size. Use an environment variable to pass the authentication token to the command. The provided command is for Unix/Linux environments. If you use Microsoft Windows, substitute Windows environment variable settings.



## What's next

  * Learn more about [IAM database authentication](https://docs.cloud.google.com/sql/docs/mysql/iam-authentication).
  * Learn how to [enable and view login information in audit logs](https://docs.cloud.google.com/sql/docs/mysql/add-manage-iam-users#viewing-login-audit-logs).
  * Learn how to [create users and service accounts that use Cloud SQL IAM database authentication](https://docs.cloud.google.com/sql/docs/mysql/add-manage-iam-users#creating-a-database-user). 
  * Learn how to [add an IAM policy binding to a user or service account](https://docs.cloud.google.com/sql/docs/mysql/add-manage-iam-users#add-policy-binding). 
  * Learn how to [manage users and service accounts for IAM database authentication](https://docs.cloud.google.com/sql/docs/mysql/add-manage-iam-users).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
