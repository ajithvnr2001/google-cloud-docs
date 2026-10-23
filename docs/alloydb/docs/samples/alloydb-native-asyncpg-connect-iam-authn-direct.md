---
url: https://docs.cloud.google.com/alloydb/docs/samples/alloydb-native-asyncpg-connect-iam-authn-direct/
title: Connect with IAM database authentication and asyncpg \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:42:54.735110+00:00
---

# Connect with IAM database authentication and asyncpg  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/samples/alloydb-native-asyncpg-connect-iam-authn-direct/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Samples ](https://docs.cloud.google.com/alloydb/docs/samples)



#  Connect with IAM database authentication and asyncpg Stay organized with collections  Save and categorize content based on your preferences. 

This snippet demonstrates how to create a secure, asynchronous connection pool using the Python asyncpg driver. It connects to an instance using IAM database authentication, which provides an automatically refreshed OAuth2 access token as the password.

## Code sample

### Python

To authenticate to AlloyDB, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import asyncpg
    
    import google.auth
    from google.auth.transport.requests import Request
    
        # initialize Google Auth credentials
        credentials, _ = google.auth.default(
            scopes=["https://www.googleapis.com/auth/cloud-platform"]
        )
    
        def get_authentication_token() -> str:
            """Get OAuth2 access token to be used for IAM database authentication"""
            # refresh credentials if expired
            if not credentials.valid:
                request = Request()
                credentials.refresh(request)
            return credentials.token
    
        # ... inside of async context (function)
        async with asyncpg.create_pool(
            user=user,  # your IAM db user, e.g. service-account@project-id.iam
            password=get_authentication_token,  # callable to get fresh OAuth2 token
            host=ip_address,  # your AlloyDB instance IP address
            port=5432,
            database=db,  # your database name
            # Because this connection uses an OAuth2 token as a password, you must
            # require SSL, or better, enforce all clients speak SSL on the server
            # side. This ensures the OAuth2 token is not inadvertantly leaked.
            ssl="require",
        ) as pool:
            # acquire connection from native asyncpg connection pool
            async with pool.acquire() as conn:
                time = await conn.fetchrow("SELECT NOW()")
                print("Current time is ", time[0])

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=alloydbforpostgresql). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
