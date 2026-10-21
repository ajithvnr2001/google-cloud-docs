---
url: https://docs.cloud.google.com/spanner/docs/use-active-record/
title: Using Active Record with Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:54:14.562678+00:00
---

# Using Active Record with Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/use-active-record/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Guides ](https://docs.cloud.google.com/spanner/docs/create-query-database-console)



Send feedback 

#  Using Active Record with Spanner Stay organized with collections  Save and categorize content based on your preferences. 

Ruby [Active Record](https://guides.rubyonrails.org/active_record_basics.html) is an Object-Relational Mapping (ORM) library bundled with [Ruby on Rails](https://rubyonrails.org/). Active Record provides an abstraction over the underlying database and includes capabilities such as automatically generating schema changes and managing schema version history.

The [Spanner support for Active Record](https://github.com/googleapis/ruby-spanner-activerecord) enables [Active Record](https://guides.rubyonrails.org/active_record_basics.html) users to use Spanner databases. With this support, Ruby applications can take advantage of Spanner's high availability and external consistency at scale through an ORM.

**PostgreSQL interface note:** The [PostgreSQL interface for Spanner](https://docs.cloud.google.com/spanner/docs/postgresql-interface) doesn't support Active Record. 

## Setting up the Spanner support for Active Record

To setup the Spanner support for Active Record in your application, edit the `Gemfile` of your Rails application and add the [activerecord-spanner-adapter](https://rubygems.org/gems/activerecord-spanner-adapter) gem.
    
    
    gem 'activerecord-spanner-adapter'
    

Next, run bundle to install the gem.
    
    
    bundle install
    

As authentication for the Spanner support for Active Record, the [service account JSON credentials](https://docs.cloud.google.com/docs/authentication/getting-started) file location should be provided in the `GOOGLE_APPLICATION_CREDENTIALS` environment variable. Otherwise, the Spanner support for Active Record can also use the default credentials set in the Google Cloud SDK `gcloud` application.

## Using the Spanner support for Active Record

For more information about the available features, limitations of the Spanner support for Active Record, recommendations on how to use it, and for code samples, please consult the [reference documentation](https://github.com/googleapis/ruby-spanner-activerecord#readme) on GitHub.

## What's next

  * Checkout the [code examples](https://github.com/googleapis/ruby-spanner-activerecord#examples) on how to use the Spanner support for Active Record.
  * View the repository for the Spanner support for Active Record on [GitHub](https://github.com/googleapis/ruby-spanner-activerecord).
  * File a [GitHub issue](https://github.com/googleapis/ruby-spanner-activerecord/issues) to report a bug or ask a question about the Spanner support for Active Record.
  * Learn more about [Active Record](https://guides.rubyonrails.org/active_record_basics.html).
  * Learn more about [Ruby Gems](https://rubygems.org/).
  * Learn about authorization and authentication credentials in [Getting started with authentication](https://docs.cloud.google.com/docs/authentication/getting-started).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
