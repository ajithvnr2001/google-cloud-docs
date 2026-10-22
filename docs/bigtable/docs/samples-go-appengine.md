---
url: https://docs.cloud.google.com/bigtable/docs/samples-go-appengine/
title: Example: Go App Engine Application \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:53:34.575958+00:00
---

# Example: Go App Engine Application  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/samples-go-appengine/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Example: Go App Engine Application

This example is an [App Engine](https://docs.cloud.google.com/appengine) application, written in Go, that provides a web interface that uses Bigtable to track the number of visits from your Google account. It runs locally in a Docker container or in the cloud in App Engine's [flexible environment](https://docs.cloud.google.com/appengine/docs/flexible). The code for this application is in the GitHub repository [GoogleCloudPlatform/golang-samples](https://github.com/GoogleCloudPlatform/golang-samples), in the directory `bigtable/usercounter`.

**Warning:** This application does not provide any access control for your data. Shut down the application when you are done testing.

## Overview of the code sample

When the code sample is launched, it creates an administrative client for Bigtable. It then uses the client to check the user-specified Bigtable instance for a table named `user-visit-counter`, with a single column family named `emails`. If necessary, it creates the table and column family:
    
    
    adminClient, err := bigtable.NewAdminClient(ctx, project, instance)
    if err != nil {
    	log.Fatalf("Unable to create a table admin client. %v", err)
    }
    tables, err := adminClient.Tables(ctx)
    if err != nil {
    	log.Fatalf("Unable to fetch table list. %v", err)
    }
    if !sliceContains(tables, tableName) {
    	if err := adminClient.CreateTable(ctx, tableName); err != nil {
    		log.Fatalf("Unable to create table: %v. %v", tableName, err)
    	}
    }
    tblInfo, err := adminClient.TableInfo(ctx, tableName)
    if err != nil {
    	log.Fatalf("Unable to read info for table: %v. %v", tableName, err)
    }
    if !sliceContains(tblInfo.Families, familyName) {
    	if err := adminClient.CreateColumnFamily(ctx, tableName, familyName); err != nil {
    		log.Fatalf("Unable to create column family: %v. %v", familyName, err)
    	}
    }
    adminClient.Close()

The code sample then creates a single Bigtable client that is used for all subsequent reads and writes:
    
    
    client, err = bigtable.NewClient(ctx, project, instance)
    if err != nil {
    	log.Fatalf("Unable to create data operations client. %v", err)
    }

Finally, the code sample adds an HTTP handler to the root of the App Engine server. On each request, the handler prompts the user to log in if necessary. It then tracks the user's visit by performing an `Increment` operation on the row for the user's email address:
    
    
    tbl := client.Open(tableName)
    rmw := bigtable.NewReadModifyWrite()
    rmw.Increment(familyName, u.Email, 1)
    row, err := tbl.ApplyReadModifyWrite(ctx, u.Email, rmw)
    if err != nil {
    	return &appError{err, "Error applying ReadModifyWrite to row: " + u.Email, http.StatusInternalServerError}
    }

After incrementing the row, the handler displays an HTML page showing the total number of visits by the current user.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
