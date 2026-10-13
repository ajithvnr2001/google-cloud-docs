---
url: https://docs.cloud.google.com/ruby/docs/setup/
title: Setting up a Ruby development environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:58:22.051499+00:00
---

# Setting up a Ruby development environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/setup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Guides ](https://docs.cloud.google.com/ruby/docs/setup)



Send feedback 

#  Setting up a Ruby development environment Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial shows how to prepare your local machine for [Ruby](https://www.ruby-lang.org/) development, including developing Ruby apps that run on Google Cloud. Follow this tutorial to install Ruby and relevant tools.

Read [Quickstart for Ruby and Google Cloud](https://docs.cloud.google.com/ruby/getting-started/hello-world) to get an overview of Ruby and learn ways to run Ruby apps on Google Cloud.

## Objectives

  * Install Ruby.
  * Install Bundler.
  * Install an editor (optional).
  * Install the Google Cloud CLI.
  * Install the Cloud Client Libraries for Ruby.
  * Set up authentication.



## Install Ruby

Ruby's installation instructions vary by operating system. Follow the guide for the operating system you're using on your local development machine. This tutorial applies to stable and non-end-of-life (EOL) Ruby versions listed on [Ruby-lang](https://www.ruby-lang.org/en/downloads/).

### macOS

We recommend using [`rbenv`](https://github.com/rbenv/rbenv) to manage your Ruby installations on macOS. `rbenv` manages multiple Ruby version installations on your machine and a rbenv plugin named [`ruby-build`](https://github.com/rbenv/ruby-build#readme) adds support to `rbenv` to install a specified version of Ruby.

While macOS includes a version of Ruby by default, it's best to perform a separate install of the latest versions of Ruby to stay up-to-date and avoid conflicts with the operating system's use of its default version.

  1. Install [XCode](https://itunes.apple.com/us/app/xcode/id497799835?mt=12).
  2. Install [XCode's command line tools](https://developer.apple.com/library/content/technotes/tn2339/_index.html) by using the following command in a terminal:
         
         xcode-select --install
         

  3. Install `homebrew` by following the instructions on the [homebrew homepage](https://brew.sh/).

  4. Install `rbenv` by using `homebrew`, following the instructions in the [rbenv readme](https://github.com/rbenv/rbenv#installation). The homebrew installation includes the `ruby-build` plugin.




Learn more about [using rbenv](https://github.com/rbenv/ruby-build#usage) and `ruby-build` to install different versions of Ruby.

### Linux

We recommend using [`rbenv`](https://github.com/rbenv/rbenv) to manage your Ruby installations on Linux distributions. `rbenv` manages multiple Ruby version installations on your machine and a `rbenv` plugin named [`ruby-build`](https://github.com/rbenv/ruby-build#readme) adds support to `rbenv` to install a specified version of Ruby.

  1. Install `rbenv` on your Linux distribution by using the [`rbenv` readme](https://github.com/rbenv/rbenv#installation).

  2. Install the `ruby-build` plugin for `rbenv` by using the instructions in the [`ruby-build` readme](https://github.com/rbenv/ruby-build#installation).




Learn more about [using `rbenv`](https://github.com/rbenv/ruby-build#usage) and `ruby-build` to install different versions of Ruby.

### Windows

For Windows, we recommend one of the following:

  * [RubyInstaller](https://rubyinstaller.org/)
  * [Install a Windows subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10).



## Install Bundler

[Bundler](https://bundler.io/) is a Ruby gem that manages project gem dependencies defined in a file named `Gemfile`. The Ruby samples in Google Cloud's documentation use `Gemfile` files to specify required gems and versions.

  1. Install Bundler.
         
         gem install bundler
         

  2. Install `gem` dependencies defined in the `Gemfile`.
         
         bundle install
         

  3. Run your Ruby project only using gems defined in your `Gemfile`.
         
         bundle exec ruby app.rb
         




Learn more about creating a `Gemfile` by reading [Bundler documentation](http://bundler.io/v1.16/man/gemfile.5.html).

## Install an editor

Popular editors (in no particular order) used to develop Ruby apps include, but aren't limited to:

  * [Sublime Text](https://www.sublimetext.com/) by Jon Skinner
  * [Atom](https://atom.io/) by GitHub
  * [RubyMine](https://www.jetbrains.com/ruby/) by JetBrains
  * [Vim](http://www.vim.org/) by Vim the editor



These editors (sometimes with the help of plugins) give you everything from syntax highlighting, intelli-sense, and code completion to fully integrated debugging capabilities, maximizing your Ruby development efficacy.

## Install the gcloud CLI

The [gcloud CLI](https://docs.cloud.google.com/sdk) is a set of tools for Google Cloud. It contains `gcloud` and `bq`, which you can use to access Compute Engine, Cloud Storage, BigQuery, and other products and services from the command line. You can run these tools interactively or in your automated scripts.

As an example, here is a simple command that deploys a Ruby web app to the App Engine flexible environment. After deployment, App Engine attempts to start the app with `bundle exec ruby app.rb -p 8080`: 
    
    
    gcloud app deploy
    

Learn how to [deploy a Ruby on Rails](https://docs.cloud.google.com/ruby/rails) app to the App Engine flexible environment. 

## Install the Cloud Client Library for Ruby

The [Cloud Client Library for Ruby](https://googleapis.github.io/google-cloud-ruby/docs) is the idiomatic way for Ruby developers to integrate with Google Cloud services. You can install the package for an individual API, such as Cloud Storage for example:
    
    
    gem install google-cloud-storage
    

You can also use Bundler and add the gem to your `Gemfile` dependencies, for example:
    
    
    bundle add google-cloud-storage
    

## Set up authentication

To use the Cloud Client Libraries in a local development environment, set up Application Default Credentials.

If you're using a local shell, then create local authentication credentials for your user account: 
    
    
    gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using client libraries](https://docs.cloud.google.com/docs/authentication/client-libraries).

## What's next

  * Browse the [documentation for Google Cloud products](https://docs.cloud.google.com/products).

  * Learn to [deploy Ruby on Rails to Google App Engine flexible environment](https://docs.cloud.google.com/ruby/rails). 

  * Clone the [Ruby samples repository from GitHub](https://github.com/GoogleCloudPlatform/ruby-docs-samples).

  * Explore [Ruby tutorials submitted by the community](https://docs.cloud.google.com/community/tutorials?q=%ruby%22).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
