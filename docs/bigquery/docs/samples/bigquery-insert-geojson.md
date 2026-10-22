---
url: https://docs.cloud.google.com/bigquery/docs/samples/bigquery-insert-geojson/
title: Insert GeoJSON data \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:17:11.375250+00:00
---

# Insert GeoJSON data  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/samples/bigquery-insert-geojson/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Samples ](https://docs.cloud.google.com/bigquery/docs/samples)



#  Insert GeoJSON data Stay organized with collections  Save and categorize content based on your preferences. 

Streaming insert into GEOGRAPHY column with GeoJSON data.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Work with geospatial data](https://docs.cloud.google.com/bigquery/docs/geospatial-data)



## Code sample

### Python

Before trying this sample, follow the Python setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/bigquery/latest). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    import geojson
    from google.cloud import [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest)
    
    bigquery_client = [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest).[Client](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html)()
    
    # This example uses a table containing a column named "geo" with the
    # GEOGRAPHY data type.
    table_id = "my-project.my_dataset.my_table"
    
    # Use the python-geojson library to generate GeoJSON of a line from LAX to
    # JFK airports. Alternatively, you may define GeoJSON data directly, but it
    # must be converted to a string before loading it into BigQuery.
    my_geography = geojson.LineString([(-118.4085, 33.9416), (-73.7781, 40.6413)])
    rows = [
        # Convert GeoJSON data into a string.
        {"geo": geojson.dumps(my_geography)}
    ]
    
    #  table already exists and has a column
    # named "geo" with data type GEOGRAPHY.
    errors = bigquery_client.[insert_rows_json](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html#google_cloud_bigquery_client_Client_insert_rows_json)(table_id, rows)
    if errors:
        raise RuntimeError(f"row insert failed: {errors}")
    else:
        print(f"wrote 1 row to {table_id}")

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-bigquery/latest/Google/Cloud/Bigquery.html). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    require "google/cloud/bigquery"
    require "rgeo"
    require "rgeo/geo_json"
    
    def insert_geojson dataset_id = "your_dataset_id", table_id = "your_table_id"
      bigquery = Google::Cloud::[Bigquery](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-data_policies-v1beta1/latest/Google-Cloud-Bigquery.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery/latest/Google-Cloud-Bigquery.html)
      dataset  = bigquery.dataset dataset_id
      table    = dataset.table table_id
    
      # Use the RGeo library to generate GeoJSON of a line from LAX to
      # JFK airports. Alternatively, you may define GeoJSON data directly, but it
      # must be converted to a string before loading it into BigQuery.
      factory = RGeo::Geographic.spherical_factory
      my_line = factory.line_string([factory.point(-118.4085, 33.9416), factory.point(-73.7781, 40.6413)])
      row_data = [
        # Convert GeoJSON data into a string.
        { geo: RGeo::GeoJSON.encode(my_line).to_json }
      ]
    
      # Table already exists and has a column named "geo" with data type GEOGRAPHY.
      response = table.insert row_data
    
      if response.success?
        puts "Inserted GeoJSON row successfully"
      else
        puts "GeoJSON row insert failed: #{response.error_rows.[first](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-SplitCapacityCommitmentResponse.html)&.errors}"
      end
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigquery). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
