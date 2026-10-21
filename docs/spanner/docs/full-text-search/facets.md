---
url: https://docs.cloud.google.com/spanner/docs/full-text-search/facets/
title: Perform a search using facets \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:01:39.153471+00:00
---

# Perform a search using facets  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/full-text-search/facets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Guides ](https://docs.cloud.google.com/spanner/docs/create-query-database-console)



Send feedback 

#  Perform a search using facets Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This feature is available with the Spanner Enterprise edition and Enterprise Plus edition. For more information, see the [Spanner editions overview](https://docs.cloud.google.com/spanner/docs/editions-overview). 

This page describes how to use facets for a [full-text search](https://docs.cloud.google.com/spanner/docs/full-text-search). As part of interactive filtering, a facet is a potential filter value, and the count of matches for that filter. On websites with this capability, when you enter a search phrase, you get a list of results in the navigation menu, and there's a list of facets that you can use to narrow the search results, along with the number of results that fit into each category.

For example, if you use the query "foo" to search for albums, you might get hundreds of results. If there's a facet of genres, you could select by genres like "rock (250)," "r&b (50)," or "pop (150)".

In Spanner full-text search, you can use standard SQL expressions and full-text search functions for both filtering and filtered counting. You don't need to use special syntax to use facets.

## Add facets to use for full-text searches

The following example creates a table for albums and tokenizes the title for each album. This table is used for examples on this page.

###  GoogleSQL 
    
    
    CREATE TABLE Albums (
      AlbumId INT64 NOT NULL,
      Title STRING(MAX),
      Rating INT64,
      Genres ARRAY<STRING(MAX)>,
      Likes INT64 NOT NULL,
      Title_Tokens TOKENLIST AS (TOKENIZE_FULLTEXT(Title)) HIDDEN,
    ) PRIMARY KEY(AlbumId);
    

###  PostgreSQL 
    
    
    CREATE TABLE albums (
      albumid bigint NOT NULL,
      title text,
      rating bigint,
      genres text[],
      likes bigint NOT NULL,
      title_tokens spanner.TOKENLIST GENERATED ALWAYS AS (spanner.TOKENIZE_FULLTEXT(Title)) VIRTUAL HIDDEN,
    PRIMARY KEY(albumid));
    

Create a search index on `Title_Tokens`. Optionally, you can store `Title`, `Genres` and `Rating` in the search index to avoid a backjoin to the base table while computing facets.

###  GoogleSQL 
    
    
    CREATE SEARCH INDEX AlbumsIndex
    ON Albums (Title_Tokens)
    STORING (Title, Genres, Rating)
    ORDER BY Likes DESC;
    

###  PostgreSQL 
    
    
    CREATE SEARCH INDEX albumsindex
    ON albums (title_tokens)
    INCLUDE (title, genres, rating)
    ORDER BY likes DESC
    

For this example, insert the following data into the table.

###  GoogleSQL 
    
    
    INSERT INTO Albums (AlbumId, Title, Rating, Genres, Likes) VALUES
    (1, "The Foo Strike Again", 5, ["Rock", "Alternative"], 600),
    (2, "Who are the Who?", 5, ["Progressive", "Indie"], 200),
    (3, "No Foo For You", 4, ["Metal", "Alternative"], 50)
    

###  PostgreSQL 
    
    
    INSERT INTO albums (albumid, title, rating, genres, likes) VALUES
    (1, 'The Foo Strike Again', 5,'{"Rock", "Alternative"}', 600),
    (2, 'Who are the Who?', 5,'{"Progressive", "Indie"}', 200),
    (3, 'No Foo For You', 4,'{"Metal", "Alternative"}', 50)
    

## Retrieve count values for a single facet

This example shows how to perform a facet count on a Rating facet. It performs a text search for "foo" within the Title_Tokens column of the Albums table.

###  GoogleSQL 
    
    
    SELECT Rating, COUNT(*) AS result_count
    FROM Albums
    WHERE SEARCH(Title_Tokens, "foo")
    GROUP BY Rating
    ORDER BY Rating DESC
    
    | Rating | result_count |
    |--------|--------------|
    | 5      | 1            |
    | 4      | 1            |
    

###  PostgreSQL 
    
    
    SELECT rating, COUNT(*) AS result_count
    FROM albums
    WHERE spanner.SEARCH(title_tokens, 'foo')
    GROUP BY rating
    ORDER BY rating DESC;
    
    | rating | result_count |
    |--------|--------------|
    | 5      | 1            |
    | 4      | 1            |
    

## Retrieve count values for multiple facets

This example shows the steps for performing facet counting on multiple facets. It performs the following:

  1. Retrieve the initial search results: it performs a text search for "foo" within the `Title_Tokens` column of the `Albums` table.
  2. Calculate facet counts: it then computes counts for the `Rating` and `Genres` facets.



###  GoogleSQL 
    
    
    WITH search_results AS (
      SELECT AlbumId, Title, Genres, Rating, Likes
      FROM Albums
      WHERE SEARCH(Title_Tokens, "foo")
      ORDER BY Likes DESC, AlbumId
      LIMIT 10000
    )
    
    SELECT
    -- Result set #1: First page of search results
    ARRAY(
      SELECT AS STRUCT *
      FROM search_results
      ORDER BY Likes DESC, AlbumId
      LIMIT 50
    ) as result_page,
    -- Result set #2: Number of results by rating
    ARRAY(
      SELECT AS STRUCT Rating, COUNT(*) as result_count
      FROM search_results
      GROUP BY Rating
      ORDER BY result_count DESC, Rating DESC
    ) as rating_counts,
    -- Result set #3: Number of results for top 5 genres
    ARRAY(
      SELECT AS STRUCT genre, COUNT(*) as result_count
      FROM search_results
      JOIN UNNEST(Genres) genre
      GROUP BY genre
      ORDER BY result_count DESC, genre
      LIMIT 5
    ) as genres_counts
    

###  PostgreSQL 
    
    
    WITH search_results AS (
      SELECT albumid, title, genres, rating, likes
      FROM albums
      WHERE spanner.SEARCH(title_tokens, 'foo')
      ORDER BY likes DESC, albumid
      LIMIT 10000
    )
    
    -- The pattern ARRAY(SELECT TO_JSONB ...) enables returning multiple nested
    -- result sets in the same query.
    SELECT
      -- Result set #1: First page of search results
      ARRAY(
      SELECT JSONB_BUILD_OBJECT(
        'albumid', albumid,
        'title', title,
        'genres', genres,
        'rating', rating,
        'likes', likes
        )
      FROM search_results
      ORDER BY likes DESC, albumid
      LIMIT 50
    ) as result_page,
    -- Result set #2: Number of results by rating
    ARRAY(
      SELECT JSONB_BUILD_OBJECT(
        'rating', rating,
        'result_count', COUNT(*)
        )
      FROM search_results
      GROUP BY rating
      ORDER BY COUNT(*) DESC, rating DESC
    ) as rating_counts,
    -- Result set #3: Number of results for top 5 genres
    ARRAY(
      SELECT JSONB_BUILD_OBJECT(
        'genre', genre,
        'result_count', COUNT(*)
        )
      FROM
        search_results,
        UNNEST(genres) AS genre
      GROUP BY genre
      ORDER BY COUNT(*) DESC, genre
      LIMIT 5
    ) as genres_counts
    

Specifically, this example does the following:

  * `WITH search_results AS (...)` gathers a large set of initial search results to use for the first page of results and facet calculations.
  * `SEARCH(Title_Tokens, "foo")` is the primary search query.
  * `LIMIT 10000` limits the cost of the search by reducing the result set to 10,000. For very broad searches that might return millions of results, calculating exact facet counts on the entire dataset can be expensive. By limiting search results, the query can quickly provide approximate (lower bound) facet counts. This means the counts reflect at least that many results, but there might be more matching results beyond the 10,000 limit.
  * The `result_page` subquery produces the first page of search results displayed to the user. It selects only the top 50 records from `search_results`, ordered by `Likes` and `AlbumId`. This is what the user initially sees.
  * the `rating_counts` subquery calculates the facet counts for `Rating`. It groups all the records in `search_results` by their `Rating` and counts how many results fall into each rating category.
  * The `genres_counts` subquery calculates the facet counts for `Genres`. As it's an array, join with `UNNEST(Genres)` to treat each genre within the array as a separate row for counting.



## Retrieve subsequent pages

When you query for successive pages after the initial facet query, you can reuse the facet counts returned from the first page.

For more information on how to paginate, see [Use key-based pagination](https://docs.cloud.google.com/spanner/docs/full-text-search/paginate-search-results#use_key-based_pagination).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
