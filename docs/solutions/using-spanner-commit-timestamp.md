---
url: https://docs.cloud.google.com/solutions/using-spanner-commit-timestamp/
title: Create a change log with JDBC using the Spanner commit timestamp feature \u00a0|\u00a0 Solutions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:46:17.651616+00:00
---

# Create a change log with JDBC using the Spanner commit timestamp feature  |  Solutions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/solutions/using-spanner-commit-timestamp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Solutions ](https://docs.cloud.google.com/solutions)



Send feedback 

#  Create a change log with JDBC using the Spanner commit timestamp feature Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to use the [commit timestamp feature](https://docs.cloud.google.com/spanner/docs/commit-timestamp) to track the date and time when changes are made to your database records. When you have a large database with many transactions that change records and you want to capture changes made to the datasets, the commit timestamp feature simplifies this task.

Through a series of code samples, this document shows you how to rewrite existing data manipulation language (DML) to create a change log. The document extends [Using Cloud Spanner commit timestamps to create a change log with Go](https://docs.cloud.google.com/community/tutorials/cloud-spanner-commit-timestamp-change-log) by demonstrating the methods using Java and JDBC. The logic is represented in SQL rather than as Spanner client objects.

**Note:** An alternative to the solutions proposed on this page is Spanner change streams. Spanner change streams watch and stream out a Spanner database's data changes to other services. For more information, see [About change streams](https://docs.cloud.google.com/spanner/docs/change-streams).

## How the tables work

Assume you have a facts table called `msgs` and a history table called `msg_history`. Each time the facts table gets modified, you want to concurrently save a record in the `msg_history` table. You can use the contents of the history table later for other uses—for example, for auditing or as an event source.

The `msgs` table holds the facts, represented by a transaction ID (`id`) and the message (`msg`). The data definition language (DDL) statement that you use to create the table looks like the following:
    
    
    CREATE TABLE msgs (
        id INT64,
        msg STRING(MAX),
    ) PRIMARY KEY (id)
    

The `msg_history` table holds the transaction history. The following DDL creates the history table. The column `ts` stores the commit timestamp.
    
    
    CREATE TABLE msgs_history (
        id INT64,
        ts TIMESTAMP OPTIONS (allow_commit_timestamp=true),
        previous_msg STRING(MAX)
    ) PRIMARY KEY (ts, id)
    

### The examples

Instead of writing only to the facts table, you must do the operation to the history table in the same transaction. Spanner's JDBC driver supports declaration of the start and end of a transaction, which is a standard JDBC operation.

#### Step 1: Rewrite the insert operations

The first step is to rewrite the `insert` operations from the following form:
    
    
    insert into msgs (id, msg) values (1, 'a real msg')
    

  * Change the inserts to look like the following:
        
        insert into msgs_history (id, previous_msg, ts) values (1, Null, PENDING_COMMIT_TIMESTAMP());
        insert into msgs (id, msg) values (1, 'a real msg');
        

Here's the Java code:
        
        // insert into history
        stmt.executeUpdate(
            "insert into msgs_history (id, previous_msg, ts)"
                + " values (1, Null, PENDING_COMMIT_TIMESTAMP())");
        // insert into real table
        stmt.executeUpdate("insert into msgs (id, msg)" + " values (1, 'a real msg')");
        conn.commit();
        




#### Step 2: Rewrite the update operations

Next, you rewrite the `update` operations from the following form:
    
    
    update msgs set msg = 'new message' where id = 1
    

  * Change the updates to look like the following:
        
        insert msgs_history (id, previous_msg, ts) values ((select id from msgs where id =1 ), (select msg from msgs where id = 1), PENDING_COMMIT_TIMESTAMP());
        update msgs set msg = 'new message' where id = 1;
        

Here's the Java code:
        
        // insert into historystmt.executeUpdate(
            "insert msgs_history (id, previous_msg, ts)"
                + " values  ((select id from msgs where id =1),"
                + " (select msg from msgs where id = 1), PENDING_COMMIT_TIMESTAMP())");
        // update into fact table
        stmt.executeUpdate("update msgs set msg = 'new message' where id = 1");
        conn.commit();
        




#### Step 3: Rewrite the delete operations

Finally, you rewrite the `delete` operations from the following form:
    
    
    delete from msgs where id = 1
    

  * Change the deletes to look like the following:
        
        insert msgs_history (id, previous_msg, ts) values ((select id from msgs where id =1 ), (select msg from msgs where id = 1), PENDING_COMMIT_TIMESTAMP());
        delete from msgs where id = 1;
        

Here's the Java code:
        
        // insert into history
        stmt.executeUpdate(
            "insert msgs_history (id, previous_msg, ts)"
                + " values  ((select id from msgs where id =1),"
                + " (select msg from msgs where id = 1), PENDING_COMMIT_TIMESTAMP()) ");
        // delete from real table
        stmt.executeUpdate("delete from msgs where id = 1");
        conn.commit();
        




### Using the history table

  * Access the change history as follows:
        
        select id,msg,current_timestamp() as ts
        from msgs where id = 1
        union all
        select id,previous_msg, ts as msg
        from msgs_history where id = 1 order by ts desc
        

The results look similar to the following:
        
        id    msg             ts
        1     new message     2020-02-07T07:44:10.24833726Z
        1     a real msg      2020-01-14T10:07:20.137935Z
        1                     2020-01-14T10:07:20.070374Z
        




## What's next

  * Read more about the [Spanner commit timestamp feature](https://docs.cloud.google.com/spanner/docs/commit-timestamp).
  * Learn more about [Spanner change streams](https://docs.cloud.google.com/spanner/docs/change-streams).
  * Explore reference architectures, diagrams, and best practices about Google Cloud. Take a look at our [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
