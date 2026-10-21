---
url: https://docs.cloud.google.com/sql/docs/sqlserver/connect-run/
title: Connect from Cloud Run \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:29:34.917127+00:00
---

# Connect from Cloud Run  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/connect-run/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/sqlserver/features)



Send feedback 

#  Connect from Cloud Run Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/connect-run "View this page for the MySQL database engine") | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/connect-run "View this page for the PostgreSQL database engine") | SQL Server

This page contains information and examples for connecting to a Cloud SQL instance from a service running in Cloud Run. 

**For step-by-step instructions on running a Cloud Run sample web application connected to Cloud SQL,** see the [quickstart for connecting from Cloud Run](https://docs.cloud.google.com/sql/docs/sqlserver/connect-instance-cloud-run).

Cloud SQL is a fully-managed database service that helps you set up, maintain, manage, and administer your relational databases in the cloud.

[Cloud Run](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run) is a managed compute platform that lets you run containers directly on top of Google Cloud infrastructure.

## Set up a Cloud SQL instance

  1. Enable the Cloud SQL Admin API in the Google Cloud project that you are connecting from, if you haven't already done so: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=sqladmin&redirect=https%3A//console.cloud.google.com)

  2. [Create a Cloud SQL for SQL Server instance](https://docs.cloud.google.com/sql/docs/sqlserver/create-instance). We recommend that you choose a Cloud SQL [ instance location](https://docs.cloud.google.com/sql/docs/sqlserver/locations) in the same region as your Cloud Run service for better latency, to avoid some networking costs, and to reduce cross region failure risks. 

By default, Cloud SQL assigns a public IP address to a new instance. You also have the option to assign a private IP address. For more information about the connectivity options for both, see the [ Connecting Overview](https://docs.cloud.google.com/sql/docs/sqlserver/connect-overview) page.

  3. When you create the instance, you can choose the [ server certificate (CA) hierarchy](https://docs.cloud.google.com/sql/docs/mysql/authorize-ssl#ca-hierarchies) for the instance and then configure the hierarchy as the `serverCaMode` for the instance. You must select the per-instance CA option (`GOOGLE_MANAGED_INTERNAL_CA`) as the server CA mode for instances that you want to connect to from web applications. 



## Configure Cloud Run

The steps to configure Cloud Run depend on the type of IP address that you assigned to your Cloud SQL instance. If you route all egress traffic through Direct VPC egress or a Serverless VPC Access connector, use a private IP address. For a comparison of the two egress methods, see [Compare Direct VPC egress with VPC connectors](https://docs.cloud.google.com/run/docs/configuring/connecting-vpc). 

### Public IP (default)

Cloud Run supports connecting to Cloud SQL for SQL Server over public IP using the [Go, Java and Python connectors](https://docs.cloud.google.com/sql/docs/sqlserver/connect-connectors). 

  * Make sure that the instance has a public IP address. You can verify this on the **Overview** page for your instance in the [Google Cloud console](https://console.cloud.google.com/sql). If you need to add one, see the [Configuring public IP page](https://docs.cloud.google.com/sql/docs/sqlserver/configure-ip) for instructions.
  * Get the INSTANCE_CONNECTION_NAME for your instance. You can find this value on the **Overview** page for your instance in the [Google Cloud console](https://console.cloud.google.com/sql) or by running the following `[gcloud sql instances describe](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/describe)` command: 
        
        gcloud sql instances describe INSTANCE_NAME
           

Replace INSTANCE_NAME with the name of your Cloud SQL instance.
  * Get the CLOUD_RUN_SERVICE_ACCOUNT_NAME for your Cloud Run service. You can find this value on the **IAM** page of the project that's hosting the Cloud Run service in the [Google Cloud console](https://console.cloud.google.com/iam-admin/serviceaccounts) or by running the following `[gcloud run services describe](https://docs.cloud.google.com/sdk/gcloud/reference/run/services/describe)` command in the project that's hosting the Cloud Run service: 
        
        gcloud run services describe CLOUD_RUN_SERVICE_NAME
        --region CLOUD_RUN_SERVICE_REGION --format="value(spec.template.spec.serviceAccountName)"
           

Replace the following variables: 
    * CLOUD_RUN_SERVICE_NAME: the name of your Cloud Run service
    * CLOUD_RUN_SERVICE_REGION: the region of your Cloud Run service
  * [ Configure the service account](https://docs.cloud.google.com/run/docs/configuring/services/service-identity) for your Cloud Run service. To connect to Cloud SQL, make sure that the service account has the `Cloud SQL Client` [IAM role](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql).
**Note:** If the authorizing service account belongs to a different project than the one containing the Cloud SQL instance, you must 
    * Enable the Cloud SQL Admin API in both the projects.
    * Add the IAM permissions for the service account in the project containing the Cloud SQL instance.
  * If you're adding a Cloud SQL connection to a new service, you need to have your service [containerized](https://cloud.google.com/discover/what-are-containerized-applications) and uploaded to the Container Registry or Artifact Registry. If you don't already have a connection, then see these instructions about [building and deploying](https://docs.cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-service) a container image. 
  * If you're connecting to instances that are configured with the shared certificate authority (CA) (`GOOGLE_MANAGED_CAS_CA`) option or the customer-managed CA (`CUSTOMER_MANAGED_CAS_CA`) option as the [server CA mode](https://docs.cloud.google.com/sql/docs/sqlserver/authorize-ssl#ca-hierarchies), then select the second generation execution environment when you [select the execution environment for the service](https://docs.cloud.google.com/run/docs/about-execution-environments#choose). Both server CA mode options require you to connect to the instance with the Cloud SQL Auth Proxy v2.

If your service runs in a first generation execution environment, then you can connect only to Cloud SQL instances that are configured with the per-instance certificate authority (CA) option (`GOOGLE_MANAGED_INTERNAL_CA`) as the server CA mode. The first generation execution environment of Cloud Run embeds the Cloud SQL Auth Proxy v1. For more information about connection requirements to Cloud SQL for the Cloud SQL Auth Proxy, see [Requirements for using the Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/sqlserver/sql-proxy#requirements).




Like any configuration change, setting a new configuration for the Cloud SQL connection leads to the creation of a new Cloud Run revision. Subsequent revisions will also automatically get this Cloud SQL connection unless you make explicit updates to change it.

### Console

  1. [Go to Cloud Run](https://console.cloud.google.com/run/services)

  2. Start configuring the service. To add Cloud SQL connections to an existing service, do the following:

     1. From the **Services** list, click the service name you want.
     2. Click **Edit & deploy new revision**.
  3. Enable connecting to a Cloud SQL instance: **Note:** If your application is written in Java you can skip this step, since you do this in the Java Cloud SQL Connector.
     1. Click **Container(s)** and then **Settings**.
     2. Scroll to **Cloud SQL connections**.
     3. Click **Add connection**.
     4. Click **Enable the Cloud SQL Admin** button if you haven't enabled the Cloud SQL Admin API yet.

![Add a Cloud SQL connection](https://docs.cloud.google.com/static/run/docs/images/cloudsql-connection.png)

     * If you're adding a connection to a Cloud SQL instance in your project, then select the Cloud SQL instance you want from the menu. 
     * If you're using a Cloud SQL instance from another project, then select **custom connection string** in the menu and enter the full instance connection name in the format PROJECT-ID:REGION:INSTANCE-ID. 
     * To delete a connection, hold your cursor to the right of the connection to display the delete **Delete** icon, and click it. 
**Note:** For more information about adding Cloud SQL connections to a service that you're creating, see [Deploying a new service](https://docs.cloud.google.com/run/docs/deploying#service).
  4. Click **Create** or **Deploy**.




### Command line

Before using any of the following commands, make the following replacements:

  * IMAGE with the image you're deploying
  * SERVICE_NAME with the name of your Cloud Run service
  * INSTANCE_CONNECTION_NAME with the instance connection name of your Cloud SQL instance, or a comma delimited list of connection names. 

If you're deploying a new container, use the following command:
        
        gcloud run deploy \
          --image=IMAGE \
          --add-cloudsql-instances=INSTANCE_CONNECTION_NAME

If you're updating an existing service, use the following command: 
        
        gcloud run services update SERVICE_NAME \
          --add-cloudsql-instances=INSTANCE_CONNECTION_NAME




### Terraform

The following code creates a base Cloud Run container, with a connected Cloud SQL instance.
    
    
    resource "google_cloud_run_v2_service" "default" {
      name     = "cloudrun-service"
      location = "us-central1"
    
      deletion_protection = false # set to "true" in production
    
      template {
        containers {
          image = "us-docker.pkg.dev/cloudrun/container/hello:latest" # Image to deploy
    
          volume_mounts {
            name       = "cloudsql"
            mount_path = "/cloudsql"
          }
        }
        volumes {
          name = "cloudsql"
          cloud_sql_instance {
            instances = [google_sql_database_instance.default.connection_name]
          }
        }
      }
      client     = "terraform"
      depends_on = [google_project_service.secretmanager_api, google_project_service.cloudrun_api, google_project_service.sqladmin_api]
    }

  


  1. Apply the changes by entering `terraform apply`. 
  2. To verify the changes were made, click the name of the [Cloud Run](https://console.cloud.google.com/run/services) service, then in the **Containers** tab, locate the **Cloud SQL connections** setting. 



### Private IP

If the authorizing service account belongs to a different project than the one containing the Cloud SQL instance, do the following: 

  * In both projects, enable the Cloud SQL Admin API.
  * For the service account in the project that contains the Cloud SQL instance, add the [IAM permissions](https://docs.cloud.google.com/sql/docs/mysql/roles-and-permissions#serverless-roles-permissions).

Direct VPC egress and connectors use private IP addresses to handle communication to your VPC network. To connect directly with private IP addresses using one of these egress methods, do the following: 
  1. Make sure that the Cloud SQL instance created previously has a private IP address. To add an internal IP address, see [Configure private IP](https://docs.cloud.google.com/sql/docs/sqlserver/configure-private-ip).
  2. [Configure your egress method](https://docs.cloud.google.com/run/docs/configuring/connecting-vpc) to connect to the same VPC network as your Cloud SQL instance. Note the following conditions:
     * Direct VPC egress and Serverless VPC Access both support communication to VPC networks connected using [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn) and [VPC Network Peering](https://docs.cloud.google.com/vpc/docs/using-vpc-peering).
     * Direct VPC egress and Serverless VPC Access don't support [legacy networks](https://docs.cloud.google.com/vpc/docs/legacy).
     * Unless you're using [ Shared VPC](https://docs.cloud.google.com/vpc/docs/configure-serverless-vpc-access#shared-vpc), a connector must share the same project and region as the resource that uses it, although the connector can send traffic to resources in different regions.
  3. Connect using your instance's private IP address and port `1433`.



## Connect to Cloud SQL

After you configure Cloud Run, you can connect to your Cloud SQL instance.

### Public IP (default)

**Warning** : If you're using a first generation execution environment for your Cloud Run service, then you can connect only to a Cloud SQL instance that's configured with the [per-instance certificate authority (CA)](https://docs.cloud.google.com/sql/sqlserver/authorize-ssl#ca-hierarchies) option (`GOOGLE_MANAGED_INTERNAL_CA`) as its server CA mode. The first generation execution environment of Cloud Run embeds the Cloud SQL Auth Proxy v1. For more information about connection requirements to Cloud SQL for the Cloud SQL Auth Proxy, see [Requirements for using the Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/sqlserver/sql-proxy#requirements). 

For public IP paths, Cloud Run provides encryption and connects using the Cloud SQL connectors. 

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

### Use Secret Manager

Google recommends that you use [Secret Manager](https://docs.cloud.google.com/secret-manager) to store sensitive information such as SQL credentials. You can [pass secrets as environment variables or mount as a volume](https://docs.cloud.google.com/run/docs/configuring/secrets) with Cloud Run.

After [creating a secret](https://docs.cloud.google.com/secret-manager/docs/creating-and-accessing-secrets#create) in Secret Manager, update an existing service, with the following command:

### Command line
    
    
    gcloud run services update SERVICE_NAME \
      --add-cloudsql-instances=INSTANCE_CONNECTION_NAME
      --update-env-vars=INSTANCE_CONNECTION_NAME=INSTANCE_CONNECTION_NAME_SECRET \
      --update-secrets=DB_USER=DB_USER_SECRET:latest \
      --update-secrets=DB_PASS=DB_PASS_SECRET:latest \
      --update-secrets=DB_NAME=DB_NAME_SECRET:latest

### Terraform

The following creates secret resources to securely hold the database user, password, and name values using `google_secret_manager_secret` and `google_secret_manager_secret_version`. Note that you must update the project compute service account to have access to each secret.
    
    
    # Create dbuser secret
    resource "google_secret_manager_secret" "dbuser" {
      secret_id = "dbusersecret"
      replication {
        auto {}
      }
      depends_on = [google_project_service.secretmanager_api]
    }
    
    # Attaches secret data for dbuser secret
    resource "google_secret_manager_secret_version" "dbuser_data" {
      secret      = google_secret_manager_secret.dbuser.id
      secret_data = "secret-data" # Stores secret as a plain txt in state
    }
    
    # Update service account for dbuser secret
    resource "google_secret_manager_secret_iam_member" "secretaccess_compute_dbuser" {
      secret_id = google_secret_manager_secret.dbuser.id
      role      = "roles/secretmanager.secretAccessor"
      member    = "serviceAccount:${data.google_project.project.number}-compute@developer.gserviceaccount.com" # Project's compute service account
    }
    

  

    
    
    # Create dbpass secret
    resource "google_secret_manager_secret" "dbpass" {
      secret_id = "dbpasssecret"
      replication {
        auto {}
      }
      depends_on = [google_project_service.secretmanager_api]
    }
    
    # Attaches secret data for dbpass secret
    resource "google_secret_manager_secret_version" "dbpass_data" {
      secret      = google_secret_manager_secret.dbpass.id
      secret_data = "secret-data" # Stores secret as a plain txt in state
    }
    
    # Update service account for dbpass secret
    resource "google_secret_manager_secret_iam_member" "secretaccess_compute_dbpass" {
      secret_id = google_secret_manager_secret.dbpass.id
      role      = "roles/secretmanager.secretAccessor"
      member    = "serviceAccount:${data.google_project.project.number}-compute@developer.gserviceaccount.com" # Project's compute service account
    }
    

  

    
    
    # Create dbname secret
    resource "google_secret_manager_secret" "dbname" {
      secret_id = "dbnamesecret"
      replication {
        auto {}
      }
      depends_on = [google_project_service.secretmanager_api]
    }
    
    # Attaches secret data for dbname secret
    resource "google_secret_manager_secret_version" "dbname_data" {
      secret      = google_secret_manager_secret.dbname.id
      secret_data = "secret-data" # Stores secret as a plain txt in state
    }
    
    # Update service account for dbname secret
    resource "google_secret_manager_secret_iam_member" "secretaccess_compute_dbname" {
      secret_id = google_secret_manager_secret.dbname.id
      role      = "roles/secretmanager.secretAccessor"
      member    = "serviceAccount:${data.google_project.project.number}-compute@developer.gserviceaccount.com" # Project's compute service account
    }
    

Update the main Cloud Run resource to include the new secrets.
    
    
    resource "google_cloud_run_v2_service" "default" {
      name     = "cloudrun-service"
      location = "us-central1"
    
      deletion_protection = false # set to "true" in production
    
      template {
        containers {
    ** image = "us-docker.pkg.dev/cloudrun/container/hello:latest" # Image to deploy**
    ******# Sets a environment variable for instance connection name**
    ** env {**
    ** name  = "INSTANCE_CONNECTION_NAME"**
    ** value = google_sql_database_instance.default.connection_name**
    **}**
    **# Sets a secret environment variable for database user secret**
    ** env {**
    ** name = "DB_USER"**
    ** value_source {**
    ** secret_key_ref {**
    ** secret  = google_secret_manager_secret.dbuser.secret_id # secret name**
    ** version = "latest"                                      # secret version number or 'latest'**
    **}**
    **}**
    **}**
    **# Sets a secret environment variable for database password secret**
    ** env {**
    ** name = "DB_PASS"**
    ** value_source {**
    ** secret_key_ref {**
    ** secret  = google_secret_manager_secret.dbpass.secret_id # secret name**
    ** version = "latest"                                      # secret version number or 'latest'**
    **}**
    **}**
    **}**
    **# Sets a secret environment variable for database name secret**
    ** env {**
    ** name = "DB_NAME"**
    ** value_source {**
    ** secret_key_ref {**
    ** secret  = google_secret_manager_secret.dbname.secret_id # secret name**
    ** version = "latest"                                      # secret version number or 'latest'**
    **}**
            }
          }
    
          volume_mounts {
            name       = "cloudsql"
            mount_path = "/cloudsql"
          }
        }
        volumes {
          name = "cloudsql"
          cloud_sql_instance {
            instances = [google_sql_database_instance.default.connection_name]
          }
        }
      }
      client     = "terraform"
      depends_on = [google_project_service.secretmanager_api, google_project_service.cloudrun_api, google_project_service.sqladmin_api]
    }

Apply the changes by entering `terraform apply`.

The example command uses the secret version, latest; however, Google recommends [pinning the secret](https://docs.cloud.google.com/secret-manager/docs/best-practices#administration) to a specific version, SECRET_NAME:v1.

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
    

### Ruby

To see this snippet in the context of a web application, view [the README on GitHub](https://github.com/GoogleCloudPlatform/ruby-docs-samples/tree/master/cloud-sql/sqlserver/activerecord/README.md).
    
    
    tcp: &tcp
      adapter: sqlserver
      # Configure additional properties here.
      # Note: Saving credentials in environment variables is convenient, but not
      # secure - consider a more secure solution such as
      # Cloud Secret Manager (https://cloud.google.com/secret-manager) to help
      # keep secrets safe.
      username: <%= ENV["DB_USER"] %>  # e.g. "my-database-user"
      password: <%= ENV["DB_PASS"] %> # e.g. "my-database-password"
      database: <%= ENV.fetch("DB_NAME") { "vote_development" } %>
      host: <%= ENV.fetch("INSTANCE_HOST") { "127.0.0.1" }%> # '172.17.0.1' if deployed to GAE Flex
      port: <%= ENV.fetch("DB_PORT") { 1433 }%> 

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

You can also test using the [Cloud SQL Proxy via a docker container](https://docs.cloud.google.com/sql/docs/sqlserver/connect-docker). 

### Connection Limits

Both the MySQL and PostgreSQL editions of Cloud SQL impose a maximum limit on concurrent connections, and these limits may vary depending on the database engine chosen (see the [Cloud SQL Quotas and Limits](https://docs.cloud.google.com/sql/docs/quotas#fixed-limits) page).

Cloud Run container instances are limited to 100 connections to a Cloud SQL database. Each instance of a Cloud Run service or job can have 100 connections to the database, and as this service or job scales, the total number of connections per deployment can grow.

You can limit the maximum number of connections used per instance by using a connection pool. For more detailed examples on how to limit the number of connections, see the [ Managing database connections](https://docs.cloud.google.com/sql/docs/sqlserver/manage-connections#count) page.

### API Quota Limits

Cloud Run provides a mechanism that connects using the Cloud SQL Auth Proxy, which uses the Cloud SQL Admin API. [ API quota limits](https://console.cloud.google.com/iam-admin/quotas?service=sqladmin.googleapis.com) apply to the Cloud SQL Auth Proxy. The Cloud SQL Admin API quota used is approximately two times the number of Cloud SQL instances configured by the number of Cloud Run instances of a particular service deployed at any one time. You can [cap or increase the number of Cloud Run instances](https://docs.cloud.google.com/run/docs/configuring/max-instances) to modify the expected API quota consumed.

## What's next

  * Learn more about [Cloud Run](https://docs.cloud.google.com/run/docs).
  * Learn more about [building and deploying](https://docs.cloud.google.com/run/docs/quickstarts/build-and-deploy) container images. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
