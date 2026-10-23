---
url: https://docs.cloud.google.com/sql/docs/sqlserver/samples/cloud-sql-sqlserver-databasesql-connect-connector/
title: Create a connection using the Cloud SQL Go Connector \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:18:50.030700+00:00
---

# Create a connection using the Cloud SQL Go Connector  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/samples/cloud-sql-sqlserver-databasesql-connect-connector/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Samples ](https://docs.cloud.google.com/sql/docs/sqlserver/samples)



#  Create a connection using the Cloud SQL Go Connector Stay organized with collections  Save and categorize content based on your preferences. 

Open a connection to Cloud SQL for SQL Server by using the Cloud SQL Go Connector.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Connect from App Engine flexible environment](https://docs.cloud.google.com/sql/docs/sqlserver/connect-app-engine-flexible)
  * [Connect from App Engine standard environment](https://docs.cloud.google.com/sql/docs/sqlserver/connect-app-engine-standard)
  * [Connect from Cloud Run](https://docs.cloud.google.com/sql/docs/sqlserver/connect-run)
  * [Connect from Cloud Run functions](https://docs.cloud.google.com/sql/docs/sqlserver/connect-functions)
  * [Connect using Cloud SQL Language Connectors](https://docs.cloud.google.com/sql/docs/sqlserver/connect-connectors)



## Code sample

### Go

To authenticate to Cloud SQL for SQL Server, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudsqlforsqlserver). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
