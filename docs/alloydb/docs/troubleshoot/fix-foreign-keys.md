---
url: https://docs.cloud.google.com/alloydb/docs/troubleshoot/fix-foreign-keys/
title: Find and fix foreign key violations \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:46:40.778962+00:00
---

# Find and fix foreign key violations  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/troubleshoot/fix-foreign-keys/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Find and fix foreign key violations Stay organized with collections  Save and categorize content based on your preferences. 

To check for a foreign key where the corresponding primary key is missing, run the following command:

### Code Sample
    
    
      WITH q AS (
          SELECT conrelid::regclass AS fk_table, 
                confrelid::regclass AS pk_table, 
                format('(%s)',(select string_agg(format('fk.%I', attname), ', ') 
                    FROM pg_attribute a 
                    JOIN unnest(conkey) ia(nr) ON ia.nr = a.attnum
                  WHERE attrelid = conrelid)) AS fk_fields, 
                format('(%s)',(select string_agg(format('pk.%I', attname), ', ') 
                    FROM pg_attribute a 
                    JOIN unnest(confkey) ia(nr) ON ia.nr = a.attnum
                  WHERE attrelid = confrelid)) AS pk_fields, 
                pg_get_constraintdef(oid)
            FROM pg_constraint
          WHERE contype='f'
      )
      SELECT format(
      $sql$
      DO $$ BEGIN RAISE NOTICE 'checking Foreign Key %3$s%1$s ==> %4$s%2$s'; END;$$;
      SELECT %1$s, %2$s 
        FROM %3$s AS fk
        LEFT JOIN %4$s AS pk ON %1$s = %2$s 
        WHERE %2$s IS NULL
          AND  %1$s IS NOT NULL  /* any NULL on FK side bypasses FK constraint by design */
      /* use limit for testing, or detecting that "there is a problem in this table */
      --  LIMIT 10
      $sql$, fk_fields, pk_fields, fk_table, pk_table
      )
        FROM q
      \gexec
      

The output of the script will be similar to the following. If there is no output, there are no violations and you have successfully rebuilt your index.

### Output
    
    
      id  | pk_id 
      ----+-------
          |     4
      (1 row)
      

In the above output, the first column shows the primary key columns, in this example, a column named `id`. The second column is the referencing column for the foreign key. This means there is a row, `pk_id=4`, for which a parent primary key doesn't exist. You can decide if these keys are valid and if they are not, you can delete them.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
