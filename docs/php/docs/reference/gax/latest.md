---
url: https://docs.cloud.google.com/php/docs/reference/gax/latest/
title: Google API Core for PHP \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:29:51.849311+00:00
---

# Google API Core for PHP  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/gax/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google API Core for PHP Stay organized with collections  Save and categorize content based on your preferences. 

1.51.0 (latest)  1.46.0  1.43.0  1.42.5  1.40.0  1.38.2  1.36.1  1.35.1 

[![Latest Stable Version](https://poser.pugx.org/google/gax/v/stable)](https://packagist.org/packages/google/gax) [![Packagist](https://img.shields.io/packagist/dm/google/gax.svg)](https://packagist.org/packages/google/gax)

**NOTE:** This repository is part of [Google Cloud PHP](https://github.com/googleapis/google-cloud-php). Any support requests, bug reports, or development contributions should be directed to that project.

Google API Core for PHP (gax-php) is a set of modules which aids the development of APIs for clients based on [gRPC](http://grpc.io) and Google API conventions.

Application code will rarely need to use most of the classes within this library directly, but code generated automatically from the API definition files in [Google APIs](https://github.com/googleapis/googleapis/) can use services such as page streaming and retry to provide a more convenient and idiomatic API surface to callers.

## PHP Versions

gax-php currently requires PHP 8.2 or higher.

## Contributing

Contributions to this library are always welcome and highly encouraged.

See the [CONTRIBUTING](https://github.com/googleapis/gax-php/blob/main/.github/CONTRIBUTING.md) documentation for more information on how to get started.

## Versioning

This library follows [Semantic Versioning](http://semver.org/).

This library is considered GA (generally available). As such, it will not introduce backwards-incompatible changes in any minor or patch releases. We will address issues and requests with the highest priority.

## Repository Structure

All code lives under the src/ directory. Handwritten code lives in the src/ApiCore directory and is contained in the `Google\ApiCore` namespace.

Generated classes for protobuf common types and LongRunning client live under the src/ directory, in the appropriate directory and namespace.

Code in the metadata/ directory is provided to support generated protobuf classes, and should not be used directly.

## Development Set-Up

These steps describe the dependencies to install for Linux, and equivalents can be found for Mac or Windows.

  1. Install dependencies.
         
         > cd ~/
         > sudo apt-get install php php-dev libcurl3-openssl-dev php-pear php-bcmath php-xml
         > curl -sS https://getcomposer.org/installer | php
         > sudo pecl install protobuf
         

  2. Set up this repo.
         
         > cd /path/to/gax-php
         > composer install
         

  3. Run tests.
         
         > vendor/bin/phpunit
         

For Showcase Conformance testing and client generation, see [tests/Conformance/README.md](https://docs.cloud.google.com/php/docs/reference/gax/latest/tests/Conformance/README).

  4. Run static analysis tools
         
         > phpstan -c phpstan.neon.dist
         




## License

BSD - See [LICENSE](https://github.com/googleapis/gax-php/blob/main/LICENSE) for more information.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
