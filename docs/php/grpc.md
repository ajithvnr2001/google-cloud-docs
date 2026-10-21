---
url: https://docs.cloud.google.com/php/grpc/
title: Install gRPC for PHP \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:34:49.872672+00:00
---

# Install gRPC for PHP  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/grpc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Install gRPC for PHP Stay organized with collections  Save and categorize content based on your preferences. 

gRPC is a modern, open-source, high-performance remote procedure call framework. If you want to use PHP client libraries for gRPC-enabled APIs, you must install gRPC for PHP. This tutorial explains how to install and enable gRPC.

## Objectives

  * Install the gRPC extension for PHP.
  * Enable the gRPC extension for PHP.



## Requirements

  * PHP 7.0 or later
  * [PECL](https://pecl.php.net/) (unless you build from source)
  * [Composer](https://getcomposer.org/)



Note: Windows users can [download and enable DLLs](https://pecl.php.net/package/gRPC) from PECL.

## Installing PECL

### Ubuntu / Debian
    
    
    sudo apt-get install autoconf zlib1g-dev php-dev php-pear
    

If using PHP 7.4+, PHP must have been installed with the `--with-pear` flag.

### CentOS / RHEL 7
    
    
    sudo rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
    sudo rpm -Uvh https://mirror.webtatic.com/yum/el7/webtatic-release.rpm
    sudo yum install php-devel php-pear gcc zlib-devel
    

### macOS
    
    
    curl -O https://pear.php.net/go-pear.phar
    sudo php -d detect_unicode=0 go-pear.phar
    

### Windows

Windows does not require PECL.

## Installing the gRPC extension

### Using PECL
    
    
    sudo pecl install grpc
    

This compiles and installs the gRPC PHP extension into the standard PHP extension directory.

**Note** : For users on CentOS/RHEL 6, unfortunately this step won't work. Follow the instructions under the **Build from source** tab to compile the extension from source.

### Build from source

Follow these instructions to compile the gRPC core library and PHP extension from source.

  1. Clone the gRPC repository from GitHub.
         
         git clone https://github.com/grpc/grpc
         

  2. Build and install the gRPC C core library.
         
         cd grpc
         git submodule update --init
         make
         sudo make install
         

It can take a few minutes to download and execute the library. If you have git version 1.8.4 or greater, you can speed up the `git submodule update --init` command by adding the `--depth=1` flag.

  3. Compile the gRPC PHP extension.
         
         cd src/php/ext/grpc
         phpize
         ./configure
         make
         sudo make install
         




#### Windows

Windows users can download the pre-compiled gRPC directly from the [PECL website](https://pecl.php.net/package/grpc).

Read the [PHP documentation for installing extensions](https://www.php.net/manual/en/install.pecl.windows.php) on Windows.

### Enable the gRPC extension in php.ini

#### Linux / macOS

Add this line anywhere in your `php.ini` file, for example, `/etc/php7/cli/php.ini`. You can find this file by running `php --ini`.
    
    
    extension=grpc.so
    

#### Windows

Add this line anywhere in your `php.ini` file, for example, `C:\Program Files\PHP\7.3\php.ini`.
    
    
    extension=php_grpc.dll
    

### Add gRPC as a Composer dependency

Use Composer to add the `grpc/grpc` package to your PHP project:
    
    
    composer require "grpc/grpc:^1.38"
    

## Installing the protobuf runtime library

You can choose from two protobuf runtime libraries. The APIs they offer are identical. The C implementation performs better than the PHP (native) implementation, while the native implementation installs easier than the C implementation.

### C implementation

For better performance with gRPC, enable the protobuf C-extension.

**Linux / macOS**

Install the `protobuf.so` extension by using PECL.
    
    
    sudo pecl install protobuf
    

Now add this line to your `php.ini` file, for example, `/etc/php5/cli/php.ini`.
    
    
    extension=protobuf.so
    

**Windows**

Download the pre-compiled protobuf extension directly from the [PECL website](https://pecl.php.net/package/protobuf).

Now add this line to your `php.ini` file, for example, `C:\Program Files\PHP\7.3\php.ini`.
    
    
    extension=php_protobuf.dll
    

### PHP implementation

For easier installation, require the `google/protobuf` package by using Composer.
    
    
    composer require "google/protobuf:^3.17"
    

## What's next

Now that you've installed gRPC and the gRPC PHP extension, try out gRPC-enabled APIs such as [Google Cloud Spanner](https://cloud.google.com/php/docs/reference/cloud-spanner/latest).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-04 UTC."],[],[]] 
