---
url: https://docs.cloud.google.com/sql/docs/mysql/samples/cloud-sql-mysql-databasesql-connect-tcp-sslcerts/
title: Configure SSL certificates for TCP connection by using Go \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:30:02.402352+00:00
---

# Configure SSL certificates for TCP connection by using Go  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/samples/cloud-sql-mysql-databasesql-connect-tcp-sslcerts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Samples ](https://docs.cloud.google.com/sql/docs/mysql/samples)



#  Configure SSL certificates for TCP connection by using Go Stay organized with collections  Save and categorize content based on your preferences. 

Configure SSL (Secure Sockets Layer) certificates for a TCP connection to Cloud SQL for MySQL by using Go's database/sql package.

## Code sample

### Go

To authenticate to Cloud SQL for MySQL, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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
    
    	// (OPTIONAL) Configure SSL certificates
    	// For deployments that connect directly to a Cloud SQL instance without
    	// using the Cloud SQL Proxy, configuring SSL certificates will ensure the
    	// connection is encrypted.
    	if dbRootCert, ok := os.LookupEnv("DB_ROOT_CERT"); ok { // e.g., '/path/to/my/server-ca.pem'
    		var (
    			dbCert = mustGetenv("DB_CERT") // e.g. '/path/to/my/client-cert.pem'
    			dbKey  = mustGetenv("DB_KEY")  // e.g. '/path/to/my/client-key.pem'
    		)
    		pool := x509.NewCertPool()
    		pem, err := os.ReadFile(dbRootCert)
    		if err != nil {
    			return nil, err
    		}
    		if ok := pool.AppendCertsFromPEM(pem); !ok {
    			return nil, errors.New("unable to append root cert to pool")
    		}
    		cert, err := tls.LoadX509KeyPair(dbCert, dbKey)
    		if err != nil {
    			return nil, err
    		}
    		mysql.RegisterTLSConfig("cloudsql", &tls.Config{
    			RootCAs:      pool,
    			Certificates: []tls.Certificate{cert},
    			// InsecureSkipVerify and a custom VerifyPeerCertificate function is
    			// required to handle Cloud SQL's custom certificates.
    			// As an alternative it's also possible to inspect the server
    			// certificate and extract the SAN field and use that a ServerName
    			// while removing InsecureSkipVerify and VerifyPeerCertificate.
    			InsecureSkipVerify:    true,
    			VerifyPeerCertificate: verifyPeerCertFunc(pool),
    		})
    		dbURI += "&tls=cloudsql"
    	}
    
    	// dbPool is the pool of database connections.
    	dbPool, err := sql.Open("mysql", dbURI)
    	if err != nil {
    		return nil, fmt.Errorf("sql.Open: %w", err)
    	}
    
    	// ...
    
    	return dbPool, nil
    }
    
    
    // verifyPeerCertFunc returns a function that verifies the peer certificate is
    // in the cert pool.
    func verifyPeerCertFunc(pool *x509.CertPool) func([][]byte, [][]*x509.Certificate) error {
    	return func(rawCerts [][]byte, _ [][]*x509.Certificate) error {
    		if len(rawCerts) == 0 {
    			return errors.New("no certificates available to verify")
    		}
    
    		cert, err := x509.ParseCertificate(rawCerts[0])
    		if err != nil {
    			return err
    		}
    
    		opts := x509.VerifyOptions{Roots: pool}
    		if _, err = cert.Verify(opts); err != nil {
    			return err
    		}
    		return nil
    	}
    }
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudsqlformysql). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
