---
url: https://docs.cloud.google.com/cortex/docs/v6/optional-step-external-datasets/
title: Configure external datasets \u00a0|\u00a0 Google Cloud Cortex Framework \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:10:18.482932+00:00
---

# Configure external datasets  |  Google Cloud Cortex Framework  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cortex/docs/v6/optional-step-external-datasets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Google Cloud Cortex Framework ](https://docs.cloud.google.com/cortex/docs)
  * [ Version 6 Guides ](https://docs.cloud.google.com/cortex/docs/v6/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure external datasets

This page describes an optional step to configure external datasets for the Cortex Framework Data Foundation deployment. Some advanced use cases might require external datasets to complement an enterprise system of record. In addition to external exchanges consumed from [BigQuery sharing (formerly Analytics Hub)](https://docs.cloud.google.com/bigquery/docs/analytics-hub-introduction), some datasets might need custom or tailored methods to ingest data and join them with the reporting models.

To enable the following external datasets, set `k9.deployDataset` to `True` if you want Dataset to be deployed.

Configure the Directed Acyclic Graphs (DAGs) for the supported external datasets following these steps:

  1. **Holiday Calendar:** This DAG retrieves the special dates from [PyPi Holidays](https://pypi.org/project/holidays/).

**Note:** If using sample data, keep default values.
     1. Adjust the list of countries, the list of years, as well as other DAG parameters to retrieve holidays in [`holiday_calendar.ini`](https://github.com/GoogleCloudPlatform/cortex-data-foundation/blob/main/src/k9/src/holiday_calendar/holiday_calendar.ini).
  2. **Trends** : This DAG retrieves _Interest Over Time_ for a specific set of terms from [Google Search trends](https://trends.google.com/trends/). The terms can be configured in [`trends.ini`](https://github.com/GoogleCloudPlatform/cortex-data-foundation/blob/main/src/k9/src/trends/trends.ini).

     1. After an initial run, adjust the `start_date` to `'today 7-d'` in [`trends.ini`](https://github.com/GoogleCloudPlatform/cortex-data-foundation/blob/main/src/k9/src/trends/trends.ini).
     2. Get familiarized with the results coming from the different terms to tune parameters.
     3. We recommend partitioning large lists to multiple copies of this DAG running at different times.
     4. For more information about the underlying library being used, see [Pytrends](https://pypi.org/project/pytrends/).
  3. **Weather** : By default, this DAG uses the publicly available test dataset [`BigQuery-public-data.geo_openstreetmap.planet_layers`](https://console.cloud.google.com/bigquery/analytics-hub/exchanges\(analyticshub:search\)?queryText=open%20street%20map). The query also relies on an NOAA dataset only available through Sharing: [`noaa_global_forecast_system`](https://console.cloud.google.com/bigquery/analytics-hub/exchanges\(analyticshub:search\)?queryText=noaa%20global%20forecast).

**This dataset needs to be created in the same region as the other datasets prior to executing deployment**. If the datasets aren't available in your region, you can continue with the following instructions to transfer the data into the chosen region:

     1. Go to the [**Sharing (Analytics Hub)**](https://console.cloud.google.com/bigquery/analytics-hub) page.
     2. Click **Search listings**.
     3. Search for **NOAA Global Forecast System**.
     4. Click **Subscribe**.
     5. When prompted, keep `noaa_global_forecast_system` as the name of the dataset. If needed, adjust the name of the dataset and table in the FROM clauses in `weather_daily.sql`.
     6. Repeat the listing search for Dataset `OpenStreetMap Public Dataset`.
     7. Adjust the `FROM` clauses containing: `BigQuery-public-data.geo_openstreetmap.planet_layers` in `postcode.sql`.
  4. **Sustainability and ESG insights** : Cortex Framework combines SAP supplier performance data with advanced ESG insights to compare delivery performance, sustainability and risks more holistically across global operations. For more information, see the [Dun & Bradstreet data source](https://docs.cloud.google.com/cortex/docs/v6/dun-and-bradstreet).




## General considerations

  * [Sharing](https://docs.cloud.google.com/bigquery/docs/analytics-hub-introduction) is only supported in EU and US locations, and some datasets, such as NOAA Global Forecast, are only offered in a single multi location.

If you are targeting a location different from the one available for the required dataset, we recommended to create a [scheduled query](https://docs.cloud.google.com/bigquery/docs/scheduling-queries) to copy the new records from the Sharing linked dataset followed by a [transfer service](https://docs.cloud.google.com/bigquery/docs/dts-introduction) to copy those new records into a dataset located in the same location or region as the rest of your deployment. You then need to adjust the SQL files.

  * Before copying these DAGs to Managed Airflow, add the required python modules [as dependencies](https://docs.cloud.google.com/composer/docs/how-to/using/installing-python-dependencies#options_for_managing_python_packages):
        
        Required modules:
        pytrends~=4.9.2
        holidays
        




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
