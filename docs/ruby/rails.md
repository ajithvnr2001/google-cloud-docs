---
url: https://docs.cloud.google.com/ruby/rails/
title: Running Rails on Google Cloud \u00a0|\u00a0 Ruby \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:03:25.993965+00:00
---

# Running Rails on Google Cloud  |  Ruby  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/rails/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Guides ](https://docs.cloud.google.com/ruby/docs/setup)



Send feedback 

#  Running Rails on Google Cloud Stay organized with collections  Save and categorize content based on your preferences. 

It's easy to get started developing Ruby on Rails apps that run on Google Cloud. Because the apps you create run on the same infrastructure that powers all of Google's products, you can be confident that they can scale to serve all of your users, whether there are a few or millions of them.

## Hosting platforms

These are some of the available options for deploying Rails on Google Cloud:

Rails deployment option | Get started  
---|---  
Cloud Run | 

  * [Rails on Cloud Run](https://docs.cloud.google.com/ruby/rails/run)
  * [Deploy a Ruby app in a container image to Cloud Run](https://docs.cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-ruby-service)

  
App Engine flexible environment | [Rails on App Engine flexible environment](https://docs.cloud.google.com/ruby/rails/appengine)  
Google Kubernetes Engine (GKE) | [Ruby on GKE](https://docs.cloud.google.com/ruby/tutorials/bookshelf-on-kubernetes-engine)  
Compute Engine | [Ruby in Compute Engine](https://docs.cloud.google.com/ruby/tutorials/bookshelf-on-compute-engine)  
  
For more details on the differences between these platforms, see [App Hosting options on Google Cloud](https://cloud.google.com/hosting-options).

## Databases

### Relational databases

[Rails Active Record](http://guides.rubyonrails.org/active_record_basics.html) works best with a traditional SQL database. If you are starting a new project, [Cloud SQL](https://docs.cloud.google.com/sql) is a good choice. With a few clicks you can create a MySQL or PostgreSQL database that is fully managed and scaled by Google, with no management on your end. Review the [Using Cloud SQL for MySQL with Rails 5](https://docs.cloud.google.com/ruby/rails/using-cloudsql-mysql) tutorial or the [Using Cloud SQL for PostgreSQL with Rails 5](https://docs.cloud.google.com/ruby/rails/using-cloudsql-postgres).

### NoSQL databases

In many situations, there are compelling reasons to use a NoSQL database, for example, scalability or suitability for your data model. Although using Rails models with a NoSQL database can be challenging, it is possible with some limitations. For example, you can express many types of database joins in Rails, but joins aren't supported by Datastore or other NoSQL databases such as MongoDB. You can learn more by reviewing our Rails [Bookshelf tutorial using Datastore](https://docs.cloud.google.com/ruby/getting-started/using-cloud-datastore), which uses Datastore as its non-relational database. For a managed, massively-scalable NoSQL solution, consider [Datastore](https://docs.cloud.google.com/datastore), which is a non-relational database that often scales better than a SQL solution.

If you choose to use MongoDB, you can deploy it by using [Google Cloud Marketplace](https://docs.cloud.google.com/marketplace/solution/click-to-deploy-images/mongodb) and do your own management, or you can use the managed MongoDB hosting service provided by [mLab](https://www.mongodb.com/atlas/database).

## Caches

To install Memcached on Compute Engine, you can use [Cloud Marketplace](https://docs.cloud.google.com/marketplace/solution/bitnami-launchpad/memcached?q=memcache). To install Memcached on either Compute Engine or GKE , you can use the [Memcached Docker image](https://hub.docker.com/_/memcached/). Similarly, you can install Redis by using [Cloud Marketplace](https://docs.cloud.google.com/marketplace/solution/click-to-deploy-images/redis) or the [Redis docker image](https://hub.docker.com/_/redis/).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
