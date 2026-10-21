---
url: https://docs.cloud.google.com/sql/docs/sqlserver/samples/cloud-sql-sqlserver-databasesql-connect-tcp-sslcerts/
title: Configure SSL certificates for TCP connection by using Go \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:30:52.428559+00:00
---

# Configure SSL certificates for TCP connection by using Go  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/samples/cloud-sql-sqlserver-databasesql-connect-tcp-sslcerts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Samples ](https://docs.cloud.google.com/sql/docs/sqlserver/samples)



#  Configure SSL certificates for TCP connection by using Go Stay organized with collections  Save and categorize content based on your preferences. 

Configure SSL (Secure Sockets Layer) certificates for a TCP connection to Cloud SQL for SQL Server by using Go's database/sql package.

## Code sample

### Go

To authenticate to Cloud SQL for SQL Server, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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
    
    	// (OPTIONAL) Configure SSL certificates
    	// For deployments that connect directly to a Cloud SQL instance without
    	// using the Cloud SQL Proxy, configuring SSL certificates will ensure the
    	// connection is encrypted.
    	if dbRootCert, ok := os.LookupEnv("DB_ROOT_CERT"); ok { // e.g., '/path/to/my/server-ca.pem'
    		// Get connection host name to be matched with host name in SSL certificate.
    		var instanceConnectionName = mustGetenv("INSTANCE_CONNECTION_NAME")
    		// Expected format of INSTANCE_CONNECTION_NAME is project_id:region:instance_name
    		hostNameParts := strings.Split(instanceConnectionName, ":")
    		if len(hostNameParts) != 3 {
    			log.Fatalf("Invalid format for INSTANCE_CONNECTION_NAME environment variable, got = %q", instanceConnectionName)
    		}
    		// Specify encrypted connection, host name and certificate.
    		dbURI += fmt.Sprintf("encrypt=true;hostnameincertificate=%s:%s;certificate=%s;",
    			hostNameParts[0], hostNameParts[2], dbRootCert)
    	}
    
    	// dbPool is the pool of database connections.
    	dbPool, err := sql.Open("sqlserver", dbURI)
    	if err != nil {
    		return nil, fmt.Errorf("sql.Open: %w", err)
    	}
    
    	// ...
    
    	return dbPool, nil
    }
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudsqlforsqlserver). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
