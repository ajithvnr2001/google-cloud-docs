---
url: https://docs.cloud.google.com/sql/docs/mysql/samples/cloud-sql-mysql-pdo-connection/
title: MySQL PDO connection \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:12:22.606705+00:00
---

# MySQL PDO connection  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/samples/cloud-sql-mysql-pdo-connection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Samples ](https://docs.cloud.google.com/sql/docs/mysql/samples)



#  MySQL PDO connection Stay organized with collections  Save and categorize content based on your preferences. 

Run a SQL INSERT statement to open and close a connection to Cloud SQL for MySQL by using the PHP Data Objects (PDO) extension.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Manage database connections](https://docs.cloud.google.com/sql/docs/mysql/manage-connections)



## Code sample

### PHP

To authenticate to Cloud SQL for MySQL, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Use prepared statements to guard against SQL injection.
    $sql = 'INSERT INTO votes (time_cast, candidate) VALUES (NOW(), :voteValue)';
    
    try {
        $statement = $conn->prepare($sql);
        $statement->bindParam('voteValue', $value);
    
        $res = $statement->execute();
    } catch (PDOException $e) {
        throw new RuntimeException(
            'Could not insert vote into database. The PDO exception was ' .
            $e->getMessage(),
            $e->getCode(),
            $e
        );
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudsqlformysql). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
