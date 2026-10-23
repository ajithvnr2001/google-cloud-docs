---
url: https://docs.cloud.google.com/spanner/docs/full-text-search/top-k-pattern-matching/
title: Perform efficient top-k retrieval \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:53:29.674833+00:00
---

# Perform efficient top-k retrieval  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/full-text-search/top-k-pattern-matching/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Guides ](https://docs.cloud.google.com/spanner/docs/create-query-database-console)



Send feedback 

#  Perform efficient top-k retrieval Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This feature is available with the Spanner Enterprise edition and Enterprise Plus edition. For more information, see the [Spanner editions overview](https://docs.cloud.google.com/spanner/docs/editions-overview). 

Many applications query a database to populate a single page in their applications. In such applications, the application doesn't need all of the matches, but only the top-k matches based on index sort order. Search indexes can implement this type of search very efficiently. This page describes how to create and search an index that has top-k matching.

## Create search indexes for top-k matches

To configure a search index for top-k matching, use `ORDER BY` to order the search index by a specific column. Queries need to have an `ORDER BY` clause that exactly matches the search index sort order (including ascending versus descending direction) and a `LIMIT` clause that requests the query to stop after finding k-matching rows.

You can also implement pagination using these clauses. For more information, see [Paginate search queries](https://docs.cloud.google.com/spanner/docs/full-text-search/paginate-search-results).

For some use cases, it might make sense to maintain multiple search indexes sorted by different columns. Like [partitioning](https://docs.cloud.google.com/spanner/docs/full-text-search/partition-search-index), it's a trade-off between storage and write cost versus query latency.

For example, consider a table that uses the following schema:

###  GoogleSQL 
    
    
    CREATE TABLE Albums (
      AlbumId STRING(MAX) NOT NULL,
      RecordTimestamp INT64 NOT NULL,
      ReleaseTimestamp INT64 NOT NULL,
      ListenTimestamp INT64 NOT NULL,
      AlbumTitle STRING(MAX),
      AlbumTitle_Tokens TOKENLIST AS (TOKENIZE_FULLTEXT(AlbumTitle)) HIDDEN
    ) PRIMARY KEY(AlbumId);
    
    CREATE SEARCH INDEX AlbumsRecordTimestampIndex
    ON Albums(AlbumTitle_Tokens, SingerId_Tokens)
    STORING (ListenTimestamp)
    ORDER BY RecordTimestamp DESC
    
    CREATE SEARCH INDEX AlbumsReleaseTimestampIndex
    ON Albums(AlbumTitle_Tokens)
    STORING (ListenTimestamp)
    ORDER BY ReleaseTimestamp DESC
    

###  PostgreSQL 
    
    
    CREATE TABLE albums (
      albumid character varying NOT NULL,
      recordtimestamp bigint NOT NULL,
      releasetimestamp bigint NOT NULL,
      listentimestamp bigint NOT NULL,
      albumtitle character varying,
      albumtitle_tokens spanner.tokenlist
          GENERATED ALWAYS AS (spanner.tokenize_fulltext(albumtitle)) VIRTUAL HIDDEN,
    PRIMARY KEY(albumid));
    
    CREATE SEARCH INDEX albumsrecordtimestampindex
    ON Albums(albumtitle_tokens, singerid_tokens)
    INCLUDE (listentimestamp)
    ORDER BY recordtimestamp DESC
    
    CREATE SEARCH INDEX albumsreleasetimestampindex
    ON Albums(albumtitle_tokens)
    INCLUDE (listentimestamp)
    ORDER BY releasetimestamp DESC
    

## Query search indexes for top-k matches

As stated previously, queries need to have an `ORDER BY` clause that exactly matches the search index sort order (including ascending versus descending direction) and a `LIMIT` clause that requests the query to stop after finding k-matching rows.

The following list analyzes the efficiency of some common queries.

  * This query is very efficient. It selects the `AlbumsRecordTimestampIndex` index. Even if there are many albums with the word "happy", the query only scans a small number of rows:

###  GoogleSQL 
        
        SELECT AlbumId
        FROM Albums
        WHERE SEARCH(AlbumTitle_Tokens, 'happy')
        ORDER BY RecordTimestamp DESC
        LIMIT 10
        

###  PostgreSQL 
        
        SELECT albumid
        FROM albums
        WHERE spanner.search(albumtitle_tokens, 'happy')
        ORDER BY recordtimestamp DESC
        LIMIT 10
        

  * The same query, requesting sort order by `ReleaseTimestamp` in descending order, uses the `AlbumsReleaseTimestampIndex` index and is equally efficient:

###  GoogleSQL 
        
        SELECT AlbumId
        FROM Albums
        WHERE SEARCH(AlbumTitle_Tokens, 'happy')
        ORDER BY ReleaseTimestamp DESC
        LIMIT 10
        

###  PostgreSQL 
        
        SELECT albumid
        FROM albums
        WHERE spanner.search(albumtitle_tokens, 'happy')
        ORDER BY releasetimestamp DESC
        LIMIT 10
        

  * A query that requests sort order by `ListenTimestamp` doesn't execute a top-k query efficiently. It has to fetch all matching albums, sort them by `ListenTimestamp,` and return the top 10. Such a query uses more resources if there's a large number of documents that contain the term "happy".

###  GoogleSQL 
        
        SELECT AlbumId
        FROM Albums
        WHERE SEARCH(AlbumTitle_Tokens, 'happy')
        ORDER BY ListenTimestamp DESC
        LIMIT 10
        

###  PostgreSQL 
        
        SELECT albumid
        FROM albums
        WHERE spanner.search(albumtitle_tokens, 'happy')
        ORDER BY listentimestamp DESC
        LIMIT 10
        

  * Similarly, a query doesn't run efficiently if it requests that results are ordered using the `RecordTimestamp` column in ascending order. It scans all rows with the word "happy", despite having a `LIMIT`.

###  GoogleSQL 
        
        SELECT AlbumId
        FROM Albums
        WHERE SEARCH(AlbumTitle_Tokens, 'happy')
        ORDER BY RecordTimestamp ASC
        LIMIT 10
        

###  PostgreSQL 
        
        SELECT albumid
        FROM albums
        WHERE spanner.search(albumtitle_tokens, 'happy')
        ORDER BY recordtimestamp ASC
        LIMIT 10
        




## What's next

  * Learn about [full-text search queries](https://docs.cloud.google.com/spanner/docs/full-text-search/query-overview).
  * Learn how to [rank search results](https://docs.cloud.google.com/spanner/docs/full-text-search/ranked-search).
  * Learn how to [paginate search results](https://docs.cloud.google.com/spanner/docs/full-text-search/paginate-search-results).
  * Learn how to [mix full-text and non-text queries](https://docs.cloud.google.com/spanner/docs/full-text-search/mix-full-text-and-non-text-queries).
  * Learn how to [search multiple columns](https://docs.cloud.google.com/spanner/docs/full-text-search/search-multiple-columns).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
