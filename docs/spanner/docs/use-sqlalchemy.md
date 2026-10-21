---
url: https://docs.cloud.google.com/spanner/docs/use-sqlalchemy/
title: Integrate Spanner with SQLAlchemy ORM (GoogleSQL dialect) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:01:37.722023+00:00
---

# Integrate Spanner with SQLAlchemy ORM (GoogleSQL dialect)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/use-sqlalchemy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Guides ](https://docs.cloud.google.com/spanner/docs/create-query-database-console)



Send feedback 

#  Integrate Spanner with SQLAlchemy ORM (GoogleSQL dialect) Stay organized with collections  Save and categorize content based on your preferences. 

[SQLAlchemy](https://www.sqlalchemy.org/) is a Python SQL toolkit and Object Relational Mapper.

The [Spanner dialect for SQLAlchemy](https://github.com/googleapis/google-cloud-python/tree/main/packages/sqlalchemy-spanner) lets SQLAlchemy users to use Spanner databases. The dialect is built on top of the [Spanner API](https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-spanner/google/cloud/spanner_dbapi), which is designed in accordance with [PEP-249](https://www.python.org/dev/peps/pep-0249/), and is compatible with SQLAlchemy versions between [1.1.13](https://pypi.org/project/SQLAlchemy/1.1.13/) and [1.3.23](https://pypi.org/project/SQLAlchemy/1.3.23/), and [2.0](https://pypi.org/project/SQLAlchemy/2.0.0/).

**PostgreSQL interface note:** To use [PostgreSQL interface for Spanner](https://docs.cloud.google.com/spanner/docs/postgresql-interface) with SQLAlchemy, see [Integrate Spanner with SQLAlchemy 2 ORM (PostgreSQL-dialect)](https://docs.cloud.google.com/spanner/docs/use-sqlalchemy-pg). 

## Set up the Spanner dialect for SQLAlchemy

To set up the Spanner dialect for SQLAlchemy in your application, install the [`sqlalchemy-spanner package`](https://pypi.org/project/sqlalchemy-spanner/).
    
    
    pip3 install sqlalchemy-spanner
    

Alternatively, you can install from source.
    
    
    git clone https://github.com/googleapis/google-cloud-python.git
    cd google-cloud-python/packages/sqlalchemy-spanner
    python setup.py install
    

As authentication for the Spanner dialect for SQLAlchemy, provide the [service account JSON credentials](https://docs.cloud.google.com/docs/authentication/getting-started) file location in the `GOOGLE_APPLICATION_CREDENTIALS` environment variable. Otherwise, the dialect can also use the default credentials set in the gcloud CLI application.

## Use the Spanner dialect for SQLAlchemy

For more information about the available features, limitations of the dialect, recommendations on how to use the dialect, and for code samples, please consult the [reference documentation](https://github.com/googleapis/google-cloud-python/blob/main/packages/sqlalchemy-spanner/README.rst) on GitHub.

## What's next

  * Check out the [code examples](https://github.com/googleapis/google-cloud-python/blob/main/packages/sqlalchemy-spanner/samples/snippets.py) on how to use the Spanner dialect for SQLAlchemy.
  * View the repository for the Spanner dialect for SQLAlchemy on [GitHub](https://github.com/googleapis/google-cloud-python/tree/main/packages/sqlalchemy-spanner).
  * File a [GitHub issue](https://github.com/googleapis/google-cloud-python/issues) to report a bug or ask a question about the Spanner dialect for SQLAlchemy.
  * Learn more about [SQLAlchemy](https://www.sqlalchemy.org/).
  * Learn more about [PyPI](https://pypi.org/).
  * Learn about authorization and authentication credentials in [Getting started with authentication](https://docs.cloud.google.com/docs/authentication/getting-started).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
