---
url: https://docs.cloud.google.com/bigtable/docs/samples-go-hello/
title: Go hello world \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:29:07.539493+00:00
---

# Go hello world  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/samples-go-hello/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Go hello world

This example is a very simple "hello world" application, written in Go, that illustrates how to:

  * Set up authentication
  * Connect to a Bigtable instance.
  * Create a new table.
  * Write data to the table.
  * Read the data back.
  * Delete the table.



## Set up authentication

To use the Go samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  3. If you're using a local shell, then create local authentication credentials for your user account: 
         
         gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 




For more information, see [ Set up authentication for a local development environment](https://docs.cloud.google.com/bigtable/docs/authentication#local-development). 

## Running the sample

This example uses the [Cloud Bigtable package](https://godoc.org/cloud.google.com/go/bigtable) of the [Google Cloud Client Library for Go](https://github.com/GoogleCloudPlatform/google-cloud-go) to communicate with Bigtable.

To run this sample program, follow the [instructions for the sample on GitHub](https://github.com/GoogleCloudPlatform/golang-samples/tree/master/bigtable/helloworld).

## Using the Cloud Client Library with Bigtable

The sample application connects to Bigtable and demonstrates some simple operations.

### Importing the client library

The sample uses the following imports: 
    
    
    import (
    	"context"
    	"flag"
    	"fmt"
    	"log"
    
    	"cloud.google.com/go/bigtable"
    )
    

### Connecting to Bigtable to manage tables

To manage tables, connect to Bigtable using [`bigtable.NewAdminClient()`](https://godoc.org/cloud.google.com/go/bigtable#NewAdminClient).
    
    
    adminClient, err := bigtable.NewAdminClient(ctx, *project, *instance)
    if err != nil {
    	log.Fatalf("Could not create admin client: %v", err)
    }

### Creating a table

Create a table with [`AdminClient.CreateTable()`](https://godoc.org/cloud.google.com/go/bigtable#AdminClient.CreateTable), then get information about the table with [`AdminClient.TableInfo()`](https://godoc.org/cloud.google.com/go/bigtable#AdminClient.TableInfo). Create a column family with [`AdminClient.CreateColumnFamily()`](https://godoc.org/cloud.google.com/go/bigtable#AdminClient.CreateColumnFamily).

**Note:** Columns that are related to one another are typically grouped into a column family. For more information about column families, see the [Bigtable storage model](https://docs.cloud.google.com/bigtable/docs/overview#storage-model).
    
    
    tables, err := adminClient.Tables(ctx)
    if err != nil {
    	log.Fatalf("Could not fetch table list: %v", err)
    }
    
    if !sliceContains(tables, tableName) {
    	log.Printf("Creating table %s", tableName)
    	if err := adminClient.CreateTable(ctx, tableName); err != nil {
    		log.Fatalf("Could not create table %s: %v", tableName, err)
    	}
    }
    
    tblInfo, err := adminClient.TableInfo(ctx, tableName)
    if err != nil {
    	log.Fatalf("Could not read info for table %s: %v", tableName, err)
    }
    
    if !sliceContains(tblInfo.Families, columnFamilyName) {
    	if err := adminClient.CreateColumnFamily(ctx, tableName, columnFamilyName); err != nil {
    		log.Fatalf("Could not create column family %s: %v", columnFamilyName, err)
    	}
    }

### Connecting to Bigtable to manage data

To manage data, connect to Bigtable using [`bigtable.NewClient()`](https://godoc.org/cloud.google.com/go/bigtable#NewClient).
    
    
    client, err := bigtable.NewClient(ctx, *project, *instance)
    if err != nil {
    	log.Fatalf("Could not create data operations client: %v", err)
    }

### Writing rows to a table

Open the table you want to write to. Use [`bigtable.NewMutation()`](https://godoc.org/cloud.google.com/go/bigtable#NewMutation) to create a mutation on a single row, then use [`Mutation.Set()`](https://godoc.org/cloud.google.com/go/bigtable#Mutation.Set) to set values in the row. Generate a unique row key for each row. Repeat these steps to create multiple mutations. Finally, use [`Table.ApplyBulk()`](https://godoc.org/cloud.google.com/go/bigtable#Table.ApplyBulk) to apply all of the mutations to your table.
    
    
    tbl := client.Open(tableName)
    muts := make([]*bigtable.Mutation, len(greetings))
    rowKeys := make([]string, len(greetings))
    
    log.Printf("Writing greeting rows to table")
    for i, greeting := range greetings {
    	muts[i] = bigtable.NewMutation()
    	muts[i].Set(columnFamilyName, columnName, bigtable.Now(), []byte(greeting))
    
    	// Each row has a unique row key.
    	//
    	// Note: This example uses sequential numeric IDs for simplicity, but
    	// this can result in poor performance in a production application.
    	// Since rows are stored in sorted order by key, sequential keys can
    	// result in poor distribution of operations across nodes.
    	//
    	// For more information about how to design a Bigtable schema for the
    	// best performance, see the documentation:
    	//
    	//     https://cloud.google.com/bigtable/docs/schema-design
    	rowKeys[i] = fmt.Sprintf("%s%d", columnName, i)
    }
    
    rowErrs, err := tbl.ApplyBulk(ctx, rowKeys, muts)
    if err != nil {
    	log.Fatalf("Could not apply bulk row mutation: %v", err)
    }
    if rowErrs != nil {
    	for _, rowErr := range rowErrs {
    		log.Printf("Error writing row: %v", rowErr)
    	}
    	log.Fatalf("Could not write some rows")
    }

### Reading a row by its key

Get a row directly using its key with [`Table.ReadRow()`](https://godoc.org/cloud.google.com/go/bigtable#Table.ReadRow).
    
    
    log.Printf("Getting a single greeting by row key:")
    row, err := tbl.ReadRow(ctx, rowKeys[0], bigtable.RowFilter(bigtable.ColumnFilter(columnName)))
    if err != nil {
    	log.Fatalf("Could not read row with key %s: %v", rowKeys[0], err)
    }
    log.Printf("\t%s = %s\n", rowKeys[0], string(row[columnFamilyName][0].Value))

### Scanning all table rows

Use [`Table.ReadRows()`](https://godoc.org/cloud.google.com/go/bigtable#Table.ReadRows) to scan all of the rows in a table. Close the data client when you are done using it.
    
    
    log.Printf("Reading all greeting rows:")
    err = tbl.ReadRows(ctx, bigtable.PrefixRange(columnName), func(row bigtable.Row) bool {
    	item := row[columnFamilyName][0]
    	log.Printf("\t%s = %s\n", item.Row, string(item.Value))
    	return true
    }, bigtable.RowFilter(bigtable.ColumnFilter(columnName)))
    
    if err = client.Close(); err != nil {
    	log.Fatalf("Could not close data operations client: %v", err)
    }

### Deleting a table

Delete a table with [`AdminClient.DeleteTable()`](https://godoc.org/cloud.google.com/go/bigtable#AdminClient.DeleteTable). Close the admin client when you are done using it.
    
    
    log.Printf("Deleting the table")
    if err = adminClient.DeleteTable(ctx, tableName); err != nil {
    	log.Fatalf("Could not delete table %s: %v", tableName, err)
    }
    
    if err = adminClient.Close(); err != nil {
    	log.Fatalf("Could not close admin client: %v", err)
    }

## Putting it all together

Here is the full example without comments.
    
    
    package main
    
    import (
    	"context"
    	"flag"
    	"fmt"
    	"log"
    
    	"cloud.google.com/go/bigtable"
    )
    
    
    const (
    	tableName        = "Hello-Bigtable"
    	columnFamilyName = "cf1"
    	columnName       = "greeting"
    )
    
    var greetings = []string{"Hello World!", "Hello Cloud Bigtable!", "Hello Go!"}
    
    func sliceContains(list []string, target string) bool {
    	for _, s := range list {
    		if s == target {
    			return true
    		}
    	}
    	return false
    }
    
    func main() {
    	project := flag.String("project", "", "The Google Cloud Platform project ID. Required.")
    	instance := flag.String("instance", "", "The Google Cloud Bigtable instance ID. Required.")
    	flag.Parse()
    
    	for _, f := range []string{"project", "instance"} {
    		if flag.Lookup(f).[Value](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/apiv2/bigtablepb.html#cloud_google_com_go_bigtable_apiv2_bigtablepb_Value).String() == "" {
    			log.Fatalf("The %s flag is required.", f)
    		}
    	}
    
    	ctx := context.Background()
    
    	adminClient, err := bigtable.[NewAdminClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_AdminClient_NewAdminClient)(ctx, *project, *instance)
    	if err != nil {
    		log.Fatalf("Could not create admin client: %v", err)
    	}
    
    	tables, err := adminClient.[Tables](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_AdminClient_Tables)(ctx)
    	if err != nil {
    		log.Fatalf("Could not fetch table list: %v", err)
    	}
    
    	if !sliceContains(tables, tableName) {
    		log.Printf("Creating table %s", tableName)
    		if err := adminClient.CreateTable(ctx, tableName); err != nil {
    			log.Fatalf("Could not create table %s: %v", tableName, err)
    		}
    	}
    
    	tblInfo, err := adminClient.TableInfo(ctx, tableName)
    	if err != nil {
    		log.Fatalf("Could not read info for table %s: %v", tableName, err)
    	}
    
    	if !sliceContains(tblInfo.Families, columnFamilyName) {
    		if err := adminClient.[CreateColumnFamily](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_AdminClient_CreateColumnFamily)(ctx, tableName, columnFamilyName); err != nil {
    			log.Fatalf("Could not create column family %s: %v", columnFamilyName, err)
    		}
    	}
    
    	client, err := bigtable.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_Client_NewClient)(ctx, *project, *instance)
    	if err != nil {
    		log.Fatalf("Could not create data operations client: %v", err)
    	}
    
    	tbl := client.[Open](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_Client_Open)(tableName)
    	muts := make([]*bigtable.Mutation, len(greetings))
    	rowKeys := make([]string, len(greetings))
    
    	log.Printf("Writing greeting rows to table")
    	for i, greeting := range greetings {
    		muts[i] = bigtable.[NewMutation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_Mutation_NewMutation)()
    		muts[i].[Set](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_Mutation_Set)(columnFamilyName, columnName, bigtable.[Now](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_Timestamp_Now)(), []byte(greeting))
    
    		rowKeys[i] = fmt.Sprintf("%s%d", columnName, i)
    	}
    
    	rowErrs, err := tbl.ApplyBulk(ctx, rowKeys, muts)
    	if err != nil {
    		log.Fatalf("Could not apply bulk row mutation: %v", err)
    	}
    	if rowErrs != nil {
    		for _, rowErr := range rowErrs {
    			log.Printf("Error writing row: %v", rowErr)
    		}
    		log.Fatalf("Could not write some rows")
    	}
    
    	log.Printf("Getting a single greeting by row key:")
    	row, err := tbl.ReadRow(ctx, rowKeys[0], bigtable.RowFilter(bigtable.[ColumnFilter](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_Filter_ColumnFilter)(columnName)))
    	if err != nil {
    		log.Fatalf("Could not read row with key %s: %v", rowKeys[0], err)
    	}
    	log.Printf("\t%s = %s\n", rowKeys[0], string(row[columnFamilyName][0].[Value](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/apiv2/bigtablepb.html#cloud_google_com_go_bigtable_apiv2_bigtablepb_Value)))
    
    	log.Printf("Reading all greeting rows:")
    	err = tbl.ReadRows(ctx, bigtable.[PrefixRange](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_RowRange_PrefixRange)(columnName), func(row bigtable.Row) bool {
    		item := row[columnFamilyName][0]
    		log.Printf("\t%s = %s\n", item.Row, string(item.[Value](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/apiv2/bigtablepb.html#cloud_google_com_go_bigtable_apiv2_bigtablepb_Value)))
    		return true
    	}, bigtable.RowFilter(bigtable.[ColumnFilter](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_Filter_ColumnFilter)(columnName)))
    
    	if err = client.Close(); err != nil {
    		log.Fatalf("Could not close data operations client: %v", err)
    	}
    
    	log.Printf("Deleting the table")
    	if err = adminClient.DeleteTable(ctx, tableName); err != nil {
    		log.Fatalf("Could not delete table %s: %v", tableName, err)
    	}
    
    	if err = adminClient.Close(); err != nil {
    		log.Fatalf("Could not close admin client: %v", err)
    	}
    }

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
