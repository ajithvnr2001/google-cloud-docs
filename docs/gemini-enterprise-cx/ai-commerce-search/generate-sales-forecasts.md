---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/generate-sales-forecasts/
title: Generate sales forecasts from ecommerce data \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:39:05.800453+00:00
---

# Generate sales forecasts from ecommerce data  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/generate-sales-forecasts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  Generate sales forecasts from ecommerce data Stay organized with collections  Save and categorize content based on your preferences. 

The page provides guidance for getting predictions from Vertex AI, based on retail [data exported into BigQuery](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/export-data-into-bq). We provide several SQL code blocks to help you transform retail product and user event data into a format that Vertex AI can use. These code blocks are followed by procedures for the Vertex AI console to create a dataset, train a model, and then generate a forecast.

## Before you begin

Before you can generate sales forecasts using your retail data, you must:

  * Have your retail data uploaded using AI Commerce Search. For more information, see:

    * [Import catalog information](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/upload-catalog)
    * [Record real-time user events](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/record-events)
    * [Import historical user events](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/import-user-events)
  * Export your retail data from AI Commerce Search into BigQuery. This leaves you with a product table and a user event table in BigQuery, which you can use in the following procedures. For more information, see [Export your data into BigQuery](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/export-data-into-bq).

Alternatively, if your product and user event data is already in BigQuery, in AI Commerce Search format, you can use that data to generate sales forecasts from retail data. In this case you don't need to upload your retail data and export it to BigQuery. For more information about the format, see [Product schema](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/catalog#schema) and [About user events](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/user-events).

  * Make sure that you've been granted the `roles/aiplatform.user` IAM role, so you can do the procedures using the Vertex AI console.




## Create an aggregated sales table

The SQL code in this section transforms the user event table into an aggregated sales table. This means that for each product in the user event table that was sold at least once, the sales quantity for the product is aggregated over a weekly period. In addition, the SQL code does the following:

  * For any product in the user event table, if any timestamps are missing between the first sale of the product in the table and the last sale of any product in the table, each of the missing timestamps is backfilled with a new row with zero sales. This is to eliminate gaps in sales history.

  * If there is not at least one product in the user event table that has at least 20 timestamps, a product from the table is chosen at random and is backfilled with enough rows (each with zero sales) to reach 20 timestamps. This is to accommodate the Vertex AI requirement of having at least 20 timestamps when training a model.




To create an aggregated sales table:

  1. Replace the variables in the following SQL example code as follows:

     * **starting_day_of_week**. The day that the week starts on. Valid values: `MONDAY`, `TUESDAY`, `WEDNESDAY`, `THURSDAY`, `FRIDAY`, `SATURDAY`, `SUNDAY`.

     * **rdm_user_event_table**. The project, dataset, and table IDs of the user event table that you exported to BigQuery. The format is `project_id.dataset_id.table_id`.

     * **rdm_product_table**. The project, dataset, and table IDs of the product table that you exported to BigQuery. The format is `project_id.dataset_id.table_id`. 

     * **aggregated_sales_table**. The project, dataset, and table IDs in BigQuery for the new aggregated sales table. Use the same project ID as the product and user event tables. Use the ID of an existing dataset. Specify a table ID, but don't use the ID of an existing table unless you want to overwrite it. The format is `project_id.dataset_id.table_id`.

####  SQL code sample 
    
    DECLARE max_date DATE;
    
      SET max_date = (SELECT LAST_DAY(DATETIME(max(event_time)),
      WEEK(STARTING_DAY_OF_WEEK)) FROM `RDM_USER_EVENT_TABLE`);
    
      CREATE OR REPLACE TABLE `AGGREGATED_SALES_TABLE` AS
      WITH flatten_sku AS
      (
        SELECT * EXCEPT(quantity, product), COALESCE(quantity, 1) as quantity,
        product.id as sku FROM
        (
          SELECT * EXCEPT(product_details),
          FROM `RDM_USER_EVENT_TABLE`,
          UNNEST(product_details) AS product_detail
        )
        WHERE product IS NOT NULL
      ),
    
      aggregate_by_type as
      (
          SELECT event_type, sum(quantity) as quantity, sku,
          LAST_DAY(DATETIME(event_time), WEEK(STARTING_DAY_OF_WEEK)) as
          last_day_of_week
          from flatten_sku group by event_type, sku, last_day_of_week
      ),
    
      sales_table as
      (
          SELECT quantity, sku, last_day_of_week FROM aggregate_by_type where
          event_type = 'purchase-complete'
      ),
    
      sales_table_with_known_products as
      (
          SELECT * EXCEPT (product_table_sku) FROM
          (
              SELECT s.*, p.id as product_table_sku FROM sales_table as s LEFT JOIN
              `RDM_PRODUCT_TABLE` as p
              ON s.sku = p.id
          )
          WHERE product_table_sku is NOT NULL
      ),
    
      fill_gap as
      (
          SELECT sku, sale_date as last_day_of_week, 0 as quantity
          FROM
          (
              SELECT sku, GENERATE_DATE_ARRAY(min_date, max_date, INTERVAL 7 DAY)
              date_range FROM
              (
                  SELECT sku , MIN(last_day_of_week) as min_date FROM
                  sales_table_with_known_products GROUP BY sku
              )
          ),
          UNNEST(date_range) sale_date
      ),
    
      sales_table_backfill as
      (
          SELECT fill_gap.sku, fill_gap.last_day_of_week, coalesce(original.quantity,
          fill_gap.quantity) as quantity
          FROM
          fill_gap LEFT JOIN sales_table_with_known_products original
          ON fill_gap.sku = original.sku and fill_gap.last_day_of_week =
          original.last_day_of_week
      ),
    
      one_sku_extend_history as
      (
          SELECT sku, GENERATE_DATE_ARRAY(IF(min_date < DATE_SUB(max_date, INTERVAL
          140 DAY), min_date, DATE_SUB(max_date, INTERVAL 140 DAY)), max_date,
          INTERVAL 7 DAY) date_range FROM
          (
              SELECT sku , MIN(last_day_of_week) as min_date FROM sales_table_backfill
              GROUP BY sku LIMIT 1
          )
      ),
    
      one_sku_extend_history2 as
      (
          SELECT backfill.sku, backfill.sale_date as last_day_of_week,
          coalesce(original.quantity, backfill.sale_quantity) as quantity
          FROM
          (
              SELECT sku, sale_date, 0 as sale_quantity
              FROM one_sku_extend_history,
                  UNNEST(date_range) sale_date
          ) backfill
          LEFT JOIN sales_table_backfill original
          ON backfill.sku = original.sku and backfill.sale_date =
          original.last_day_of_week
      ),
    
      sales_table_extend_history as
      (
          SELECT quantity, sku, last_day_of_week
          FROM sales_table_backfill
          WHERE sku not in
          (select sku from one_sku_extend_history)
          UNION ALL
          SELECT quantity, sku, last_day_of_week
          FROM
          one_sku_extend_history2
      ),
    
      other_event_table as
      (
          SELECT sku, last_day_of_week,
          SUM(category_page_view_quantity) as category_page_view_quantity,
          SUM(search_quantity) as search_quantity,
          SUM(detail_page_view_quantity) as detail_page_view_quantity,
          SUM(add_to_cart_quantity) as add_to_cart_quantity
          FROM
          (
              SELECT sku, last_day_of_week,
              CASE
                  WHEN event_type = 'category-page-view' THEN quantity
              END as category_page_view_quantity,
              CASE
                  WHEN event_type = 'search' THEN quantity
              END as search_quantity,
              CASE
                  WHEN event_type = 'detail-page-view' THEN quantity
              END as detail_page_view_quantity,
              CASE
                  WHEN event_type = 'add-to-cart' THEN quantity
              END as add_to_cart_quantity,
              FROM aggregate_by_type WHERE event_type != 'purchase-complete'
          ) GROUP BY sku, last_day_of_week
      )
    
      SELECT t1.*, t2.category_page_view_quantity, t2.search_quantity,
      t2.detail_page_view_quantity, t2.add_to_cart_quantity
      FROM sales_table_extend_history as t1 left join other_event_table as t2
      ON t1.sku = t2.sku AND t1.last_day_of_week = t2.last_day_of_week
      

  2. Copy the SQL code sample.

  3. Open the BigQuery page in the Google Cloud console.

[Go to the BigQuery page](https://console.cloud.google.com/bigquery)

  4. If it's not already selected, select the project that contains your product and user event tables.

  5. In the **Editor** pane, paste the SQL code sample.

  6. Click play_circle **Run** and wait for the query to finish running.




Your new aggregated sales table is written to the location in BigQuery that you set using the **aggregated_sales_table** variable.

## Process the product table

The SQL code in this section acts on the product table that you exported to BigQuery, removing the repeated and struct fields and unnesting the **price_info** field into its child fields. This is required because Vertex AI does not accept lists or nested structures. The result is the processed product table.

To process the product table:

  1. Replace the variables in the following SQL example code as follows:

     * **rdm_product_table**. The project, dataset, and table IDs for the product table that you exported to BigQuery. The format is `project_id.dataset_id.table_id`.

     * **processed_product_table**. The project, dataset, and table IDs in BigQuery for the new processed product table. Use the same project ID as the product and user event tables. Use the ID of an existing dataset. Specify a table ID, but don't use the ID of an existing table unless you want to overwrite it. The format is `project_id.dataset_id.table_id`.
    
    CREATE OR REPLACE TABLE `PROCESSED_PRODUCT_TABLE` AS
    SELECT * EXCEPT (id, attributes, price_info, rating, expire_time,
    available_time, fulfillment_info, images, audience, color_info, promotions,
    publish_time, retrievable_fields, categories, brands, conditions, sizes,
    collection_member_ids, tags, materials, patterns),
    id as sku,
    price_info.price as price_info_price,
    price_info.currency_code as price_info_currency_code,
    price_info.cost as price_info_cost,
    FROM `RDM_PRODUCT_TABLE`

  2. Copy the SQL code sample.

  3. Open the BigQuery page in the Google Cloud console.

[Go to the BigQuery page](https://console.cloud.google.com/bigquery)

  4. If it's not already selected, select the project that contains your product and user event tables.

  5. In the **Editor** pane, paste the SQL code sample.

  6. Click play_circle **Run** and wait for the query to finish running.




Your new processed product table is written to the location in BigQuery that you set using the **processed_product_table** variable.

## Create an events prediction table

The SQL code in this section extracts each SKU that was sold at least once in the user events table. The code creates an events prediction table containing all of the extracted SKUs across all timestamps in the future. The future timestamps are an array of continuous weekly timestamps, starting from the final week in the user event table + 1 week and ending at the final week in the user event table + **future_length** weeks. You set the **future_length** value to the number of weeks into the future that you want the model to predict. Each row in the events prediction table can be uniquely identified by a SKU and a timestamp.

To create an events prediction table:

  1. Replace the variables in the following SQL example code as follows:

     * **starting_day_of_week**. The day that the week starts on. Valid values: `MONDAY`, `TUESDAY`, `WEDNESDAY`, `THURSDAY`, `FRIDAY`, `SATURDAY`, `SUNDAY`.

     * **rdm_user_event_table**. The project, dataset, and table IDs for the user event table that you exported to BigQuery. The format is `project_id.dataset_id.table_id`.

     * **events_prediction_table**. The project, dataset, and table IDs in BigQuery for the new events prediction table. Use the same project ID as the product and user event tables. Use the ID of an existing dataset. Specify a table ID, but don't use the ID of an existing table unless you want to overwrite it. The format is `project_id.dataset_id.table_id`.

     * **rdm_product_table**. The project, dataset, and table IDs for the product table that you exported to BigQuery. The format is `project_id.dataset_id.table_id`.

     * **future_length**. The number of weeks into the future, after the final week in the user event table, that the model will predict.

####  SQL code sample 
    
    DECLARE max_date DATE;
    
      SET max_date = (SELECT LAST_DAY(DATETIME(max(event_time)),
      WEEK(STARTING_DAY_OF_WEEK)) FROM `RDM_USER_EVENT_TABLE`);
    
      CREATE OR REPLACE TABLE `EVENTS_PREDICTION_TABLE` AS
      WITH purchase_events as
      (
      SELECT * EXCEPT (product_details, product),
      order_item.product.id as sku
      FROM `RDM_USER_EVENT_TABLE`,
      UNNEST(product_details) as order_item
      WHERE event_type = 'purchase-complete'
      ),
    
      known_products_in_purchase_events as
      (
          SELECT sku FROM
          (
              SELECT s.sku, p.id as product_table_sku
              FROM (SELECT DISTINCT(sku) FROM purchase_events) as s
              LEFT JOIN `RDM_PRODUCT_TABLE` as p
              ON s.sku = p.id
          )
          WHERE product_table_sku is NOT NULL
      ),
    
      sales_table_future as
      (
          SELECT sku, future_date as last_day_of_week, NULL as quantity FROM
          (
              SELECT sku, GENERATE_DATE_ARRAY(DATE_ADD(max_date, INTERVAL 1 WEEK),
              DATE_ADD(max_date, INTERVAL FUTURE_LENGTH WEEK), INTERVAL 1
              WEEK)
              date_range
              FROM known_products_in_purchase_events
          ), UNNEST(date_range) future_date
      )
      SELECT * FROM sales_table_future
      

  2. Copy the SQL code sample.

  3. Open the BigQuery page in the Google Cloud console.

[Go to the BigQuery page](https://console.cloud.google.com/bigquery)

  4. If it's not already selected, select the project that contains your product and user event tables.

  5. In the **Editor** pane, paste the SQL code sample.

  6. Click play_circle **Run** and wait for the query to finish running.




Your new events prediction table is written to the location in BigQuery that you set using the **events_prediction_table** variable.

## Create a Vertex AI training table

The SQL code in this section joins the aggregated sales table with the processed product table. The result is a Vertex AI training table, which Vertex AI uses for model training.

To create a Vertex AI training table:

  1. Replace the variables in the following SQL example code as follows:

     * **vertex_ai_training_table**. The project, dataset, and table IDs in BigQuery for the new Vertex AI training table. Use the same project ID as the product and user event tables. Use the ID of an existing dataset. Specify a table ID, but don't use the ID of an existing table unless you want to overwrite it. The format is `project_id.dataset_id.table_id`.

     * **aggregated_sales_table**. The project, dataset, and table IDs in BigQuery of the aggregated sales table, which you created in Create an aggregated sales table.

     * **processed_product_table**. The project, dataset, and table IDs in BigQuery for the processed product table, which you created in Process the product table.
    
    CREATE OR REPLACE TABLE `VERTEX_AI_TRAINING_TABLE` AS
    SELECT t1.*, t2.* EXCEPT(sku) FROM `AGGREGATED_SALES_TABLE` AS t1
    LEFT
    JOIN `PROCESSED_PRODUCT_TABLE` AS t2 ON t1.sku = t2.sku

  2. Copy the SQL code sample.

  3. Open the BigQuery page in the Google Cloud console.

[Go to the BigQuery page](https://console.cloud.google.com/bigquery)

  4. If it's not already selected, select the project that contains your product and user event tables.

  5. In the **Editor** pane, paste the SQL code sample.

  6. Click play_circle **Run** and wait for the query to finish running.




Your new Vertex AI training table is written to the location in BigQuery that you set using the **vertex_ai_training_table** variable.

## Create a Vertex AI prediction table

The SQL code in this section appends the events prediction table to the aggregated sales table, then joins it with the processed product table. The result is the Vertex AI prediction table, which is used to create a forecast.

To create a Vertex AI prediction table:

  1. Replace the variables in the following SQL example code as follows:

     * **vertex_ai_prediction_table**. The project, dataset, and table IDs in BigQuery for the new Vertex AI prediction table. Use the same project ID and dataset ID that you used for the product and user event tables. Don't use the ID of an existing table unless you want to overwrite it. The format is `project_id.dataset_id.table_id`.

     * **aggregated_sales_table**. The project, dataset, and table IDs in BigQuery for the aggregated sales table, which you created in Create an aggregated sales table.

     * **processed_product_table**. The project, dataset, and table IDs in BigQuery for the processed product table, which you created in Process the product table.

     * **events_prediction_table**. The project, dataset, and table IDs in BigQuery for the events prediction table, which you created in Create an events prediction table.
    
    CREATE OR REPLACE TABLE `VERTEX_AI_PREDICTION_TABLE` AS
    WITH append_predict_to_history AS (
      SELECT add_to_cart_quantity, category_page_view_quantity,
      detail_page_view_quantity, last_day_of_week, quantity, search_quantity, sku
      FROM `AGGREGATED_SALES_TABLE` UNION ALL SELECT NULL AS
      add_to_cart_quantity, NULL AS category_page_view_quantity, NULL AS
      detail_page_view_quantity, last_day_of_week, NULL AS quantity, NULL AS
      search_quantity, sku FROM `EVENTS_PREDICTION_TABLE`
    )
    SELECT t1.*, t2.* EXCEPT(sku) FROM append_predict_to_history AS t1 LEFT JOIN
    `PROCESSED_PRODUCT_TABLE` AS t2 ON t1.sku = t2.sku

  2. Copy the SQL code sample.

  3. Open the BigQuery page in the Google Cloud console.

[Go to the BigQuery page](https://console.cloud.google.com/bigquery)

  4. If it's not already selected, select the project that contains your product and user event tables.

  5. In the **Editor** pane, paste the SQL code sample.

  6. Click play_circle **Run** and wait for the query to finish running.




Your new Vertex AI prediction table is written to the location in BigQuery that you set using the **vertex_ai_prediction_table** variable.

## Create a Vertex AI dataset

This section shows you how to create a Vertex AI dataset that you can use to train a forecast model. For more information, see [Create a dataset for training forecast models](https://cloud.google.com/vertex-ai/docs/tabular-data/forecasting/create-dataset) in the Vertex AI documentation.

To create a Vertex AI dataset:

  1. In the Google Cloud console, in the Vertex AI section, go to the **Dataset** page.

[Go to the Datasets page](https://console.cloud.google.com/vertex-ai/datasets)

  2. Click **Create** to open the **Create dataset** page.

  3. In the **Dataset name** field, enter a name for your new dataset.

  4. Select the **Tabular** tab.

  5. Select the **Forecasting** objective.

  6. In the **Region** list, select the region that you used when you created a dataset to export your retail data into BigQuery. If you selected **us** when you created your BigQuery dataset, you can select any region in the United States. Likewise, if you selected **eu** when you created your BigQuery dataset, you can select any region in the European Union. For more information, see [Export your data into BigQuery](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/export-data-into-bq).

  7. Click **Create** to create your empty dataset, and advance to the **Source** tab.

  8. Select **Select a table or view from BigQuery**.

  9. Under **Select a table or view from BigQuery** , enter the project, dataset, and table IDs for the Vertex AI training table that you created in Create a Vertex AI training table. The format is `project_id.dataset_id.table_id`.

  10. Click **Continue**.

Your data source is associated with your dataset.

  11. On the **Analyze** tab, select **sku** in the **Series identifier column** list and **last_day_of_week** in the **Timestamp column** list.

  12. Click **Train new model** to advance to the **Train new model** page. For instructions for training your model, go to Train a forecast model.




## Train a forecast model

This section shows you how to train a forecast model using the dataset that you created in Create a Vertex AI dataset. For more information, see [Train a forecast model](https://cloud.google.com/vertex-ai/docs/tabular-data/forecasting/train-model) in the Vertex AI documentation.

### Before you begin

Before you can train a forecast model, you must create a Vertex AI dataset.

### Train a model

  1. In the **Training method** page, select the model training method. For information about training methods, see [Train a model](https://docs.cloud.google.com/vertex-ai/docs/tabular-data/forecasting/train-model#train_a_model) in the Vertex AI documentation.

Click **Continue**.

  2. In the **Model details** page, configure as follows:

     1. Select **Train new model** if it's not already selected.

     2. Enter a name for your new model.

     3. Select **quantity (INTEGER)** from the **Target column** list.

     4. Select **Weekly** from the **Data granularity** list.

     5. Enter your **Context window** and **Forecast horizon**.

The **Forecast horizon** determines how far into the future the model forecasts the target value for each row of prediction data. The **Forecast horizon** is specified in units of **Data granularity**.

The **Context window** sets how far back the model looks during training (and for forecasts). In other words, for each training datapoint, the context window determines how far back the model looks for predictive patterns. If you don't specify a **Context window** , it defaults to the value set for **Forecast horizon**. The **Context window** is specified in units of **Data granularity**.

For more information, see [Considerations for setting the context window and forecast horizon](https://cloud.google.com/vertex-ai/docs/datasets/bp-tabular#context-window) in the Vertex AI documentation.

     6. Click **Continue**.

  3. In the **Training options** page, configure as follows. Note that when a arrow_drop_down drop-down arrow is grey, or when there is no drop-down arrow, that value cannot be changed.

     1. Select a **Transformation** value for the columns in the **Column name** list as follows:

        * If the **BigQuery type** value is **Float** , **Integer** , or **Numeric** , set the **Transformation** value to **Numeric**.

        * If the **BigQuery type** value is **String** or **Boolean** , set the **Transformation** value to **Categorical**.

        * If the **BigQuery type** value is **Date** , set the **Transformation** value to **Timestamp**.

     2. Select a **Feature type** value for the columns in the **Column name** list as follows:

        * For **add_to_cart_quantity** , **category_page_view_quantity** , **detail_page_view_quantity** , and **search_quantity** , set the **Feature type** value to **Covariate**.

        * Of the remaining columns, for those that can be changed, set the **Feature type** to **Attribute**.

     3. Select an **Available at forecast** value for the columns in the **Column type** list as follows:

        * For **add_to_cart_quantity** , **category_page_view_quantity** , **detail_page_view_quantity** , and **search_quantity** , set the **Availability at forecast** value to **Not available**.

        * Of the remaining columns, for those that can be changed, set the **Feature type** value to **Available**.

     4. Click **Continue**.

  4. In the **Compute and pricing** page, enter the maximum number of hours that you want your model to train for. This setting helps you put a cap on training costs. The actual time elapsed can be longer than this value because there are other operations involved in creating a new model. For information about the amount of time that can be needed to train high-quality models, see [Train a model](https://docs.cloud.google.com/vertex-ai/docs/tabular-data/forecasting/train-model#train_a_model) in the Vertex AI documentation.

  5. Click **Start training**.

Model training can take many hours, depending on the size and complexity of your data and your training budget, if you specified one. You can close this tab and return to it later. You receive an email when your model has completed training. If you want to monitor the progress of the model training, see Monitor the progress of your training.




### Monitor the progress of your training

  1. In the Google Cloud console, in the Vertex AI section, go to the **Training** page.

[Go to the Training page](https://console.cloud.google.com/vertex-ai/training/training-pipelines)

  2. If it's not already selected, select the **Training pipelines** tab. The model you are training should be in the list. Training is finished when the status changes from **Training** to **Finished**.




## Create a forecast

This page shows you how to create a forecast using the forecast model that you trained in Train a forecast model.

### Before you begin

Before you can create a forecast, you must train a forecast model.

### Make a batch prediction request to your model

  1. In the Google Cloud console console, under the Vertex AI section, go to the **Batch predictions** page.

[Go to the Batch predictions page](https://console.cloud.google.com/vertex-ai/batch-predictions)

  2. Click **Create** to open the **New batch prediction** window and complete the following steps:

     1. Enter a name for the batch prediction.

     2. In the **Model name** list, select the model that you trained in Train a forecast model.

     3. In the **Version** list, select the version of the model.

     4. Under **Select source** :

        1. Select **BigQuery table** if it's not already selected.

        2. Enter the project, dataset, and table IDs in BigQuery for the Vertex AI prediction table that you created in Create a Vertex AI prediction table. The format is `project_id.dataset_id.table_id`.

     5. Under **Batch prediction output** :

        1. In the **Output format** list, select **BigQuery table**.

        2. Enter project and dataset IDs in BigQuery for the batch prediction output table that you are creating. Use the same project ID and dataset ID that you used for the product and user event tables. The format is `project_id.dataset_id.`

     6. Click **Create**. The **Batch predictions** page appears.

The prediction is finished when the status changes from **Pending** to **Finished**. You also receive an email when your batch prediction is finished. The output of your batch prediction request is returned in the dataset in the BigQuery project that you specified. The name of your new output table is "predictions_" appended with the timestamp of when the prediction job started. For more information about retrieving and interpreting your forecast results, see [Retrieve batch prediction results](https://cloud.google.com/vertex-ai/docs/tabular-data/forecasting/get-predictions#retrieve_batch_prediction_results) and [Interpret forecast results](https://cloud.google.com/vertex-ai/docs/tabular-data/forecasting/get-predictions#interpret_forecast_results) in the Vertex AI documentation.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
