---
url: https://docs.cloud.google.com/ruby/docs/reference/activerecord-spanner-adapter/latest/
title: Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:58:22.602992+00:00
---

# Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/activerecord-spanner-adapter/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.2.0 (latest) ](https://docs.cloud.google.com/ruby/docs/reference/activerecord-spanner-adapter/latest/)
  * [ 2.1.0 ](https://docs.cloud.google.com/ruby/docs/reference/activerecord-spanner-adapter/2.1.0/)
  * [ 2.0.0 ](https://docs.cloud.google.com/ruby/docs/reference/activerecord-spanner-adapter/2.0.0/)



# ActiveRecord Cloud Spanner Adapter

[Google Cloud Spanner](https://cloud.google.com/spanner) adapter for ActiveRecord.

![rubocop](https://github.com/googleapis/ruby-spanner-activerecord/workflows/rubocop/badge.svg)

**This adapter only supports GoogleSQL-dialect Spanner databases. PostgreSQL-dialect databases are not supported. You can use the standard PostgreSQL ActiveRecord adapter in[combination with PGAdapter](https://github.com/GoogleCloudPlatform/pgadapter/blob/-/samples/ruby/activerecord) for Spanner PostgreSQL-dialect databases.**

This project provides a Spanner adapter for ActiveRecord. It supports the following versions:

  * ActiveRecord 7.0.x with Ruby 3.1 and higher.
  * ActiveRecord 7.1.x with Ruby 3.1 and higher.
  * ActiveRecord 7.2.x with Ruby 3.1 and higher.
  * ActiveRecord 8.0.x with Ruby 3.2 and higher.



Known limitations are listed in the Limitations section. Please report any problems that you might encounter by [creating a new issue](https://github.com/googleapis/ruby-spanner-activerecord/issues/new).

## Installation

Add this line to your application's Gemfile:
    
    
    gem 'activerecord-spanner-adapter'

If you would like to use latest adapter version from github then specify
    
    
    gem 'activerecord-spanner-adapter', :git => 'git@github.com:googleapis/ruby-spanner-activerecord.git'

And then execute:
    
    
    $ bundle
    

## Usage

### Migrations

**Use DDL batching when executing migrations for the best possible performance.**

Executing multiple schema changes on Spanner can take a long time. It is therefore strongly recommended that you limit the number of schema change operations. You can do this by using DDL batching in your migrations. See [the migrations examples](https://docs.cloud.google.com/ruby/docs/reference/activerecord-spanner-adapter/latest/examples/snippets/migrations) for how to do this.

### Database Connection

In Rails application `config/database.yml`, make the change as the following:
    
    
    development:
      adapter: "spanner"
      project: "<google project name>"
      instance: "<google instance name>"
      credentials: "<google credentails file path>"
      database: "app-dev"
    

## Examples

To get started with Rails, read the tutorial under [examples/rails/README.md](https://docs.cloud.google.com/ruby/docs/reference/activerecord-spanner-adapter/latest/README "examples/rails/README.md").

You can also find a list of short self-contained code examples that show how to use ActiveRecord with Spanner under the directory [examples/snippets](https://docs.cloud.google.com/ruby/docs/reference/activerecord-spanner-adapter/latest/examples/snippets). Each example is directly runnable without the need to setup a Spanner database, as all samples will automatically start a Spanner emulator in a Docker container and execute the sample code against that emulator. All samples can be executed by navigating to the sample directory on your local machine and then executing the command `bundle exec rake run`. Example:
    
    
    cd ruby-spanner-activerecord/examples/snippets/quickstart
    bundle exec rake run
    

**NOTE** : You do need to have [Docker](https://docs.docker.com/get-docker/) installed on your local system to run these examples.

Some noteworthy examples in the snippets directory:

  * [quickstart](https://docs.cloud.google.com/ruby/docs/reference/activerecord-spanner-adapter/latest/examples/snippets/quickstart): A simple application that shows how to create and query a simple database containing two tables.
  * [migrations](https://docs.cloud.google.com/ruby/docs/reference/activerecord-spanner-adapter/latest/examples/snippets/migrations): Shows a best-practice for executing migrations on Spanner.
  * [auto-generated-primary-key](https://docs.cloud.google.com/ruby/docs/reference/activerecord-spanner-adapter/latest/examples/snippets/auto-generated-primary-key): Shows how to use IDENTITY columns for primary keys.
  * [bit-reversed-sequences](https://docs.cloud.google.com/ruby/docs/reference/activerecord-spanner-adapter/latest/examples/snippets/bit-reversed-sequence): Shows how to use bit-reversed sequences for primary keys.
  * [read-write-transactions](https://docs.cloud.google.com/ruby/docs/reference/activerecord-spanner-adapter/latest/examples/snippets/read-write-transactions): Shows how to execute transactions on Spanner.
  * [read-only-transactions](https://docs.cloud.google.com/ruby/docs/reference/activerecord-spanner-adapter/latest/examples/snippets/read-only-transactions): Shows how to execute read-only transactions on Spanner.
  * [bulk-insert](https://docs.cloud.google.com/ruby/docs/reference/activerecord-spanner-adapter/latest/examples/snippets/bulk-insert): Shows the best way to insert a large number of new records.
  * [mutations](https://docs.cloud.google.com/ruby/docs/reference/activerecord-spanner-adapter/latest/examples/snippets/mutations): Shows how you can use [mutations instead of DML](https://cloud.google.com/spanner/docs/dml-versus-mutations) for inserting, updating and deleting data in a Spanner database. Mutations can have a significant performance advantage compared to DML statements, but do not allow read-your-writes semantics during a transaction.
  * [array-data-type](https://docs.cloud.google.com/ruby/docs/reference/activerecord-spanner-adapter/latest/examples/snippets/array-data-type): Shows how to work with `ARRAY` data types.
  * [interleaved-tables](https://docs.cloud.google.com/ruby/docs/reference/activerecord-spanner-adapter/latest/examples/snippets/interleaved-tables-before-7.1): Shows how to work with [Interleaved Tables](https://cloud.google.com/spanner/docs/schema-and-data-model#create-interleaved-tables).



## Limitations

Limitation | Comment | Resolution  
---|---|---  
Interleaved tables require composite primary keys | Spanner requires composite primary keys for interleaved tables. See [this example](https://docs.cloud.google.com/ruby/docs/reference/activerecord-spanner-adapter/latest/README "this example") for an example on how to use interleaved tables with ActiveRecord | Use composite primary keys.  
Lack of sequential IDs | Spanner uses either bit-reversed IDENTITY columns or sequences to generated primary keys to avoid [hotspotting](https://cloud.google.com/spanner/docs/schema-design#uuid_primary_key) so you SHOULD NOT rely on IDs being sorted | Use either IDENTITY columns or bit-reversed sequences to automatically generate primary keys.  
Table without Primary Key | Spanner support does not support tables without a primary key. | Always define a primary key for your table.  
Table names CANNOT have spaces within them whether back-ticked or not | Spanner DOES NOT support tables with spaces in them for example `Entity ID` | Ensure that your table names don't contain spaces.  
Table names CANNOT have punctuation marks and MUST contain valid UTF-8 | Spanner DOES NOT support punctuation marks e.g. periods ".", question marks "?" in table names | Ensure that your table names don't contain punctuation marks.  
Index with fields length [add_index](https://apidock.com/rails/v5.2.3/ActiveRecord/ConnectionAdapters/SchemaStatements/add_index) | Spanner does not support index with fields length | Ensure that your database definition does not include index definitions with field lengths.  
Only GoogleSQL-dialect databases | Spanner supports both GoogleSQL- and PostgreSQL-dialect databases. This adapter only supports GoogleSQL-dialect databases. You can use the [PostgreSQL ActiveRecord provider in combination with PGAdapter](https://github.com/GoogleCloudPlatform/pgadapter/tree/postgresql-dialect/samples/ruby/activerecord) for Spanner PostgreSQL databases. |   
`rails dbconsole` is not supported. | The `rails dbconsole` is not supported for Spanner databases. |   
  
## Contributing

Bug reports and pull requests are welcome on GitHub at <https://github.com/googleapis/ruby-spanner-activerecord>. This project is intended to be a safe, welcoming space for collaboration, and contributors are expected to adhere to the [Contributor Covenant](http://contributor-covenant.org) code of conduct.

## License

The gem is available as open source under the terms of the [MIT License](https://opensource.org/licenses/MIT).

## Code of Conduct

Everyone interacting in the Activerecord::Spanner project’s codebases, issue trackers, chat rooms and mailing lists is expected to follow the [code of conduct](https://github.com/googleapis/ruby-spanner-activerecord/blob/main/CODE_OF_CONDUCT.md).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
