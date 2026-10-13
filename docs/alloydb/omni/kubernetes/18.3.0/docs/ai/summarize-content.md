---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/ai/summarize-content/
title: Summarize content \u00a0|\u00a0 AlloyDB Omni using the container orchestrator: 18.3.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:01:17.080129+00:00
---

# Summarize content  |  AlloyDB Omni using the container orchestrator: 18.3.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/ai/summarize-content/

This page documents AlloyDB Omni version **18.3.0** using the **container orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Container orchestrator: 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/overview)



Send feedback 

#  Summarize content Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.3.0keyboard_arrow_down

  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/ai/summarize-content)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/summarize-content)



**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Note:** This experimental launch is a Pre-GA offering.

The `ai.summarize` function utilizes large language models (LLMs) like Gemini to rephrase and reorganize input text into its most essential form. This function captures the core thesis of a document while preserving the original authorial tone and nuance. Using this function, you can extract key findings and conclusions from massive datasets without manual review, and control output length by specifying constraints like word counts or sentence limits in the prompt. You can also use batch processing or cursor-based snapshots to process millions of rows asynchronously.

The AlloyDB AI content summarization function supports various use cases, including but not limited to the following:

  * Meeting transcripts: summarize conversational text to focus on decisions and action items.
  * Technical documentation: condense complex methodology, results, and implications into high-level overviews.
  * Customer support logs: aggregate multiple user reviews or support tickets into a single unified summary of common issues.



## Before you begin

Make sure that you meet the following requirements before you use the `ai.summarize` function.

### Enable the extension

Make sure that you have the latest version of the `google_ml_integration.enable_preview_ai_functions` extension (version 1.5.7 or higher) installed with Preview functionality enabled.

To enable the `google_ml_integration.enable_preview_ai_functions` flag in AlloyDB Omni, you use the `SET` command. This flag controls access to preview AI functions like `ai.summarize`.

  1. Make sure that your `google_ml_integration extension` is version 1.5.7 or higher. You can check the version by running the following:
         
         SELECT extversion FROM pg_extension WHERE extname = 'google_ml_integration';
         

If you need to upgrade to a version that includes these preview functions, call the following:
         
         CALL google_ml.upgrade_to_preview_version();
         

  2. Enable the flag for the current session or for the entire database. To enable the flag for your current session, execute the following:
         
         SET google_ml_integration.enable_preview_ai_functions = 'on';
         

This change doesn't require a database restart. The default value of this flag is `off`.




### Create an example table

To follow the summarization function examples in this document, create a table and populate it with the following movie reviews.
    
    
    CREATE TABLE movie_reviews (
        id INT PRIMARY KEY,
        movie_id INT,
        review TEXT
    );
    
    INSERT INTO movie_reviews (id, movie_id, review) VALUES
    (1, 1, 'The Midnight Echo represents a masterclass in atmospheric tension. The cinematography captures the isolation of the frozen tundra perfectly while the lead actor delivers a superb performance. Although the pacing slows down significantly in the second act, the final twist remains unexpected. This is a truly remarkable experience.'),
    (2, 1, 'Neon Velocity delivers high octane action but lacks the narrative depth required to make the stakes feel real. The visual effects are undeniably stunning, creating a vibrant cyberpunk world that pops off the screen. However, the dialogue feels cliched and the secondary characters are thin. This film is a shallow blockbuster.'),
    
    -- more rows are present in this table
    

## Summarize a single string

To process a single block of text, use the scalar version of `ai.summarize`.
    
    
    SELECT ai.summarize(
      prompt => 'TEXT_CONTENT',
      model_id => 'MODEL_ID' -- Optional
    );
    

Run the following example query to provide a concise summary of movie reviews:
    
    
    SELECT ai.summarize(review) FROM movie_reviews;
    

The following is the example output:
    
    
     id |                         summary
    ----+-----------------------------------------------------------
      1 | "Atmospheric thriller with a haunting performance and shocking twist."
      2 | "Visually stunning cyberpunk action film lacks narrative depth."
    ...
    

## Summarize in batches

To process multiple records efficiently, use the array-based version.
    
    
    SELECT ai.summarize(
      prompts => TEXT[],
      batch_size => INT, -- Optional. The default is 10.
      model_id => VARCHAR(100) -- Optional. The default value is gemini-2.5-flash-lite.
    );
    

The following example shows how to use the array-based version of the `ai.summarize` function to efficiently process multiple text records in a single call.
    
    
    WITH summarized_results AS (
    SELECT
      ARRAY_AGG(id ORDER BY id) as ids,
      ai.summarize(
        prompts => array_agg( 'Please summarize this in max 10 words, review : ' || review
          ORDER BY id),
        batch_size => 15) as summaries
    FROM movie_reviews
    ),
    correlated_results AS (
        SELECT ids[i] as ID, summaries[i] as summary
        FROM summarized_results,
        generate_series(1, array_length(ids, 1)) AS i
    )
    SELECT movie_reviews.id, correlated_results.summary as summary
    FROM movie_reviews
    JOIN correlated_results ON movie_reviews.id = correlated_results.id
    ORDER BY movie_reviews.id DESC ;
    

The following is the example output:
    
    
     id | summary
    ---+----------------------------------------------------------------------------
      1 | "Masterclass in tension, haunting performance with a twist."
      2 | "High octane action, stunning visuals, shallow blockbuster."
      3 | "Gentle, moving exploration of  emotional honesty."
    

## Summarize using cursors

You can use cursors to efficiently handle potentially large sets of reviews, feeding them into an AI function and then processing the results one by one to store them back in the database.

The following example shows how to use cursors with the `ai.summarize` function to efficiently process rows from the `movie_reviews` table, generate a summary for each review, and store these summaries in a new table called `review_summaries`. This cursor-based approach is useful for handling large datasets that might be too large to process in a single batch or fit into memory all at once.

The `input_cursor` parameter takes a `REFCURSOR`. This means you need to provide a cursor name, which acts like a pointer to the results of a SQL query. The `ai.summarize` function then fetches data from this cursor to use as input for the summarization.
    
    
    CREATE OR REPLACE FUNCTION ai.summarize(
      prompt TEXT,
      input_cursor REFCURSOR,
      batch_size INT DEFAULT NULL,
      model_id VARCHAR(100) DEFAULT NULL)
    RETURNS REFCURSOR
    

The following example creates a table `review_summaries` (if needed), then it iterates through movie reviews, generates a concise summary for each using an AI function, and stores the summaries linked to their original review IDs in the table.
    
    
    -- Create a table to store the results
    CREATE TABLE IF NOT EXISTS review_summaries (
        review_id INT, 
        summary_text TEXT
    );
    
    DO $$
    DECLARE
        -- Use descriptive cursor and variable names
        review_cursor   REFCURSOR;
        result_record   RECORD;
        cursor_response  REFCURSOR;
        id_array        INT[];
        idx             INT := 1; 
    BEGIN
        -- 1. Open cursor for the input text
        OPEN review_cursor FOR 
            SELECT review AS prompt FROM movie_reviews ORDER BY id;
    
        -- 2. Call the AI summarize function
        cursor_response := ai.summarize(
            prompt       => 'Please summarize the following review in max 10 words: ',
            input_cursor => review_cursor
        );
    
        -- 3. Map IDs into an array to maintain relational integrity during the loop
        SELECT ARRAY_AGG(id ORDER BY id) INTO id_array FROM movie_reviews;
    
        -- 4. Iterate through AI results and insert into the results table
        LOOP
            FETCH cursor_response INTO result_record;
            EXIT WHEN NOT FOUND;
    
            INSERT INTO review_summaries (review_id, summary_text)
            VALUES (id_array[idx], result_record.output);
    
            idx := idx + 1;
        END LOOP;
    
        -- 5. Clean up cursors
        CLOSE review_cursor;
        CLOSE cursor_response;
    END;
    $$;
    
    -- Verify results
    SELECT * FROM review_summaries;
    

The following is the example output:
    
    
     review_id | summary_text
    -----------+---------------------------------------------------------------------------
             1 | "Masterclass in atmospheric tension with haunting performance, devastating twist."
             2 | "High octane action, stunning visuals, but shallow blockbuster."
             3 | "Gentle, moving exploration of grief with poetic screenplay."
    

## Aggregate summarization across rows

The `ai.agg_summarize` function operates across multiple rows in a column. It aggregates values into a unified prompt to generate a single summary for the entire group.

The following SQL query uses the `ai.agg_summarize` aggregate function to generate a single, unified summary for every `movie_id` based on all reviews in the `movie_reviews` table.
    
    
    select ai.agg_summarize(review) from movie_reviews group by movie_id;
    

Unlike `ai.summarize`, which summarizes each row individually, `ai.agg_summarize` combines the text from multiple rows into a single input to produce one consolidated summary for the entire group of rows.

The following is the example output:
    
    
    agg_summarize
    "The Midnight Echo is a masterclass in atmospheric tension, featuring haunting performances and stunning cinematography, though its pacing falters in the second act before a final twist. Neon Velocity offers stunning visual effects and high-octane action within a vibrant cyberpunk world, but suffers from shallow narrative depth, cliched dialogue, and underdeveloped characters. Garden of Whispers is a gentle, moving, and emotionally honest exploration of and life, characterized by poetic screenwriting and natural performances. Shadow Protocol ambitiously attempts to reinvent the spy thriller with a non-linear narrative and precise action, but ultimately confuses the audience and presents a derivative central mystery. The Last Alchemist uniquely blends historical drama with subtle fantasy, boasting meticulous production design and electric chemistry between its protagonists."
    

## What's next

  * [Evaluate sentiment](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/ai/evaluate-sentiment).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
