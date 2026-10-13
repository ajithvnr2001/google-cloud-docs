---
url: https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/
title: Google BigQuery for PHP \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:55:30.566000+00:00
---

# Google BigQuery for PHP  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google BigQuery for PHP Stay organized with collections  Save and categorize content based on your preferences. 

1.39.3 (latest)  1.38.0  1.37.0  1.36.0  1.35.2  1.34.7  1.33.1  1.32.0  1.31.1  1.30.3  1.29.0  1.28.3  1.27.0  1.26.1  1.25.1  1.24.2  1.23.10 

> Idiomatic PHP client for [Google BigQuery](https://cloud.google.com/bigquery/).

[![Latest Stable Version](https://poser.pugx.org/google/cloud-bigquery/v/stable)](https://packagist.org/packages/google/cloud-bigquery) [![Packagist](https://img.shields.io/packagist/dm/google/cloud-bigquery.svg)](https://packagist.org/packages/google/cloud-bigquery)

  * [API Documentation](https://cloud.google.com/php/docs/reference/cloud-bigquery/latest)



**NOTE:** This repository is part of [Google Cloud PHP](https://github.com/googleapis/google-cloud-php). Any support requests, bug reports, or development contributions should be directed to that project.

Allows you to create, manage, share and query data.

### Installation

To begin, install the preferred dependency manager for PHP, [Composer](https://getcomposer.org/).

Now install this component:
    
    
    $ composer require google/cloud-bigquery
    

### Authentication

Please see our [Authentication guide](https://github.com/googleapis/google-cloud-php/blob/main/AUTHENTICATION.md) for more information on authenticating your client. Once authenticated, you'll be ready to start making requests.

### Sample
    
    
    require 'vendor/autoload.php';
    
    use Google\Cloud\BigQuery\BigQueryClient;
    
    $bigQuery = new BigQueryClient();
    
    // Get an instance of a previously created table.
    $dataset = $bigQuery->dataset('my_dataset');
    $table = $dataset->table('my_table');
    
    // Begin a job to import data from a CSV file into the table.
    $loadJobConfig = $table->load(
        fopen('/data/my_data.csv', 'r')
    );
    $job = $table->runJob($loadJobConfig);
    
    // Run a query and inspect the results.
    $queryJobConfig = $bigQuery->query(
        'SELECT * FROM `my_project.my_dataset.my_table`'
    );
    $queryResults = $bigQuery->runQuery($queryJobConfig);
    
    foreach ($queryResults as $row) {
        print_r($row);
    }
    

### Debugging

Please see our [Debugging guide](https://github.com/googleapis/google-cloud-php/blob/main/DEBUG.md) for more information about the debugging tools.

### Version

This component is considered GA (generally available). As such, it will not introduce backwards-incompatible changes in any minor or patch releases. We will address issues and requests with the highest priority.

### Next Steps

  1. Understand the [official documentation](https://cloud.google.com/bigquery/docs).
  2. Take a look at [in-depth usage samples](https://github.com/GoogleCloudPlatform/php-docs-samples/tree/master/bigquery).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
