---
url: https://docs.cloud.google.com/sql/docs/postgres/samples/cloud-sql-postgres-dotnet-ado-connection/
title: PostgreSQL ADO.NET connection \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:11:39.064433+00:00
---

# PostgreSQL ADO.NET connection  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/samples/cloud-sql-postgres-dotnet-ado-connection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Samples ](https://docs.cloud.google.com/sql/docs/postgres/samples)



#  PostgreSQL ADO.NET connection Stay organized with collections  Save and categorize content based on your preferences. 

Run a SQL INSERT statement to open and close a connection to Cloud SQL for PostgreSQL by using the ADO.NET System.Data.Common package.

## Code sample

### C#

To authenticate to Cloud SQL for PostgreSQL, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    insertTimestamp = DateTime.UtcNow;
    try
    {
        using(var connection = new NpgsqlConnection(_connectionString.ConnectionString))
        {    
            connection.OpenWithRetry();
            using (var insertVoteCommand = connection.CreateCommand())
            {
                insertVoteCommand.CommandText =
                    @"INSERT INTO votes (candidate, time_cast) VALUES (@candidate, @time_cast)";
                var candidate = insertVoteCommand.CreateParameter();
                candidate.ParameterName = "@candidate";
                candidate.DbType = DbType.String;
                candidate.Value = team;
                insertVoteCommand.Parameters.Add(candidate);
                var timeCast = insertVoteCommand.CreateParameter();
                timeCast.ParameterName = "@time_cast";
                timeCast.DbType = DbType.DateTime;
                timeCast.Value = insertTimestamp;
                insertVoteCommand.Parameters.Add(timeCast);
                await insertVoteCommand.ExecuteNonQueryAsync();
            }
        }
        return Content($"Vote successfully cast for '{team}' at time {insertTimestamp}!");
    }
    catch (Exception ex)
    {
        // If something goes wrong, handle the error in this
        // section. This might involve retrying or adjusting
        // parameters depending on the situation.
        return StatusCode((int)HttpStatusCode.InternalServerError, ex);
    }
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudsqlforpostgresql). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
