---
url: https://docs.cloud.google.com/iam/docs/reference/libraries/
title: IAM client libraries \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:53:21.161925+00:00
---

# IAM client libraries  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/reference/libraries/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  IAM client libraries Stay organized with collections  Save and categorize content based on your preferences. 

The APIs for Identity and Access Management (IAM) are built on HTTP and JSON, so any standard HTTP client can send requests to it and parse the responses.

However, the Google API Client Libraries provide better language integration, improved security, and support for authentication. The client libraries are available in a number of programming languages; they handle all communication with IAM.

Many Google Cloud services also offer Google Cloud Client Libraries, which you can use to manage the allow policies for each service's resources. The Google Cloud Client Libraries offer the same benefits as the Google API Client Libraries, along with a more idiomatic API for each programming language. To learn more, see [Client libraries explained](https://docs.cloud.google.com/apis/docs/client-libraries-explained).

## IAM v1 API

Use the IAM v1 API to manage custom roles, service accounts, and service account keys.

To grant and revoke access to a specific resource, use the `getIamPolicy` and `setIamPolicy` methods in that resource's API to update its allow policy. For a list of resource types that accept allow policies, see [Resource types that accept allow policies](https://docs.cloud.google.com/iam/docs/resource-types-with-policies).

To manage deny policies, use the IAM v2 API.

### Install the client library

### C++

To install the C++ client library, follow the instructions in [Setting up a C++ development environment](https://docs.cloud.google.com/cpp/docs/setup).

### C#

For more information, see [Setting up a C# development environment](https://docs.cloud.google.com/dotnet/docs/setup).
    
    
    install-package Google.Apis.Iam.v1

### Go

For more information, see [Setting up a Go development environment](https://docs.cloud.google.com/go/docs/setup).
    
    
    go get google.golang.org/api/iam/v1

### Java

For more information, see [Setting up a Java development environment](https://docs.cloud.google.com/java/docs/setup).

If you are using Maven, add this to your `pom.xml` file.
    
    
    <dependency>
      <groupId>com.google.apis</groupId>
      <artifactId>google-api-services-iam</artifactId>
      <version>v1-rev20240118-2.0.0</version>
    </dependency>

### Node.js

For more information, see [Setting up a Node.js development environment](https://docs.cloud.google.com/nodejs/docs/setup).
    
    
    npm install googleapis

### PHP

For more information, see [Using PHP on Google Cloud](https://docs.cloud.google.com/php/docs).

Add the library as a dependency to your `composer.json` file:
    
    
    "require": {
      "google/apiclient": "^2.0"
    }

Alternatively, you can [download the package locally](https://github.com/googleapis/google-api-php-client#download-the-release).

### Python

For more information, see [Setting up a Python development environment](https://docs.cloud.google.com/python/docs/setup).
    
    
    pip install --upgrade google-api-python-client

### Ruby

For more information, see [Setting up a Ruby development environment](https://docs.cloud.google.com/ruby/docs/setup).
    
    
    gem install google-api-client

### Additional resources

### C++

For more information about how to use this client library, see the following resources: 

  * API reference documentation: [C++ IAM client library reference](https://cloud.google.com/cpp/docs/reference/iam/latest)
  * Source code: [C++ IAM client library source code](https://github.com/googleapis/google-cloud-cpp/tree/main/google/cloud/iam)
  * Issue tracker: [Google Cloud Client Library for C++ issue tracker](https://github.com/googleapis/google-cloud-cpp/issues)
  * Stack Overflow: [Stack Overflow for IAM in C++](https://stackoverflow.com/search?q=%5Bgoogle-iam%5D+%5Bc%2B%2B%5D)



### C#

For more information about how to use this client library, see the following resources: 

  * API reference documentation: [C# IAM client library reference](https://googleapis.dev/dotnet/Google.Apis.Iam.v1/latest/api/Google.Apis.Iam.v1.html)
  * Source code: [C# IAM client library source code](https://github.com/googleapis/google-api-dotnet-client/tree/master/Src/Generated/Google.Apis.Iam.v1)
  * Issue tracker: [Google API Client Library for C# issue tracker](https://github.com/googleapis/google-api-dotnet-client/issues)
  * Stack Overflow: [Stack Overflow for IAM in C#](https://stackoverflow.com/search?q=%5Bgoogle-iam%5D+%5Bc%23%5D)



### Go

For more information about how to use this client library, see the following resources: 

  * API reference documentation: [Go IAM client library reference](https://pkg.go.dev/google.golang.org/api/iam/v1)
  * Source code: [Go IAM client library source code](https://github.com/googleapis/google-api-go-client/tree/master/iam/v1)
  * Issue tracker: [Google API Client Library for Go issue tracker](https://github.com/googleapis/google-api-go-client)
  * Stack Overflow: [Stack Overflow for IAM in Go](https://stackoverflow.com/search?q=%5Bgoogle-iam%5D+%5Bgo%5D)



### Java

For more information about how to use this client library, see the following resources: 

  * API reference documentation: [IAM client library for Java reference](https://cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/overview)
  * Source code: 
    * [IAM client library for Java source code](https://github.com/googleapis/google-api-java-client-services/tree/master/clients/google-api-services-iam/v1)
    * [Google API Client Library for Java](https://github.com/googleapis/google-api-java-client)
  * Issue tracker: [Google API Client Library for Java issue tracker](https://github.com/googleapis/google-api-java-client/issues)
  * Stack Overflow: [Stack Overflow for IAM in Java](https://stackoverflow.com/search?q=%5Bgoogle-iam%5D+%5Bjava%5D)



### Node.js

For more information about how to use this client library, see the following resources: 

  * API reference documentation: [Node.js IAM client library reference](https://googleapis.dev/nodejs/googleapis/latest/iam/index.html)
  * Source code: [Node.js IAM client library source code](https://github.com/googleapis/google-api-nodejs-client/tree/master/src/apis/iam)
  * Issue tracker: [Google API Client Library for Node.js issue tracker](https://github.com/googleapis/google-api-nodejs-client)
  * Stack Overflow: [Stack Overflow for IAM in Node.js](https://stackoverflow.com/search?q=%5Bgoogle-iam%5D+%5Bnode.js%5D)



### PHP

For more information about how to use this client library, see the following resources: 

  * Source code: 
    * [PHP IAM client library source code](https://github.com/googleapis/google-api-php-client-services/tree/master/src/Iam)
    * [Google API Client Library for PHP](https://github.com/googleapis/google-api-php-client)
  * Issue tracker: [Google API Client Library for PHP issue tracker](https://github.com/googleapis/google-api-php-client)
  * Stack Overflow: [Stack Overflow for IAM in PHP](https://stackoverflow.com/search?q=%5Bgoogle-iam%5D+%5Bphp%5D)



### Python

For more information about how to use this client library, see the following resources: 

  * API reference documentation: [Python IAM client library reference](http://googleapis.github.io/google-api-python-client/docs/dyn/iam_v1.html)
  * Source code: [Google API Client Library for Python](https://github.com/googleapis/google-api-python-client)
  * Issue tracker: [Google API Client Library for Python issue tracker](https://github.com/googleapis/google-api-python-client)
  * Stack Overflow: [Stack Overflow for IAM in Python](https://stackoverflow.com/search?q=%5Bgoogle-iam%5D+%5Bpython%5D)



### Ruby

For more information about how to use this client library, see the following resources: 

  * API reference documentation: [Ruby IAM client library reference](https://googleapis.dev/ruby/google-api-client/latest/Google/Apis/IamV1.html)
  * Source code: [Google API Client Library for Ruby](https://github.com/googleapis/google-api-ruby-client)
  * Issue tracker: [Google API Client Library for Ruby issue tracker](https://github.com/googleapis/google-api-ruby-client)
  * Stack Overflow: [Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-iam%5D+%5Bruby%5D)



## IAM v2 API

Use the IAM v2 API to manage [deny policies](https://docs.cloud.google.com/iam/docs/deny-overview).

To manage custom roles, service accounts, and service account keys, use the IAM v1 API.

### Install the client library

### C++

To install the C++ client library, follow the instructions in [Setting up a C++ development environment](https://docs.cloud.google.com/cpp/docs/setup).

### C#

For more information, see [Setting up a C# development environment](https://docs.cloud.google.com/dotnet/docs/setup).
    
    
    install-package Google.Cloud.Iam.V2

### Go

For more information, see [Setting up a Go development environment](https://docs.cloud.google.com/go/docs/setup).
    
    
    go get cloud.google.com/go/iam

### Java

For more information, see [Setting up a Java development environment](https://docs.cloud.google.com/java/docs/setup).

If you are using Maven, add this to your `pom.xml` file.
    
    
    <dependency>
      <groupId>com.google.cloud</groupId>
      <artifactId>google-iam-policy</artifactId>
      <scope>compile</scope>
    </dependency>

### Node.js

For more information, see [Setting up a Node.js development environment](https://docs.cloud.google.com/nodejs/docs/setup).
    
    
    npm install @google-cloud/iam

### PHP

For more information, see [Using PHP on Google Cloud](https://docs.cloud.google.com/php/docs).

Install the component with [Composer](https://getcomposer.org/):
    
    
    composer require google/cloud-iam

### Python

For more information, see [Setting up a Python development environment](https://docs.cloud.google.com/python/docs/setup).
    
    
    pip install --upgrade google-cloud-iam

### Ruby

For more information, see [Setting up a Ruby development environment](https://docs.cloud.google.com/ruby/docs/setup).
    
    
    gem install google-iam-v2

### Additional resources

### C++

For more information about how to use this client library, see the following resources: 

  * API reference documentation: [C++ IAM client library reference](https://cloud.google.com/cpp/docs/reference/iam/latest)
  * Source code: [C++ IAM client library source code](https://github.com/googleapis/google-cloud-cpp/tree/main/google/cloud/iam)
  * Issue tracker: [Google Cloud Client Library for C++ issue tracker](https://github.com/googleapis/google-cloud-cpp/issues)
  * Stack Overflow: [Stack Overflow for IAM in C++](https://stackoverflow.com/search?q=%5Bgoogle-iam%5D+%5Bc%2B%2B%5D)



### C#

For more information about how to use this client library, see the following resources: 

  * API reference documentation: [.NET IAM v2 client library reference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V2/latest)
  * Source code: [.NET IAM v2 client library source code](https://github.com/googleapis/google-cloud-dotnet/tree/main/apis/Google.Cloud.Iam.V2/Google.Cloud.Iam.V2)
  * Issue tracker: [Cloud Client Libraries for .NET issue tracker](https://github.com/googleapis/google-cloud-dotnet/issues)
  * Stack Overflow: [Stack Overflow for IAM in C#](https://stackoverflow.com/search?q=%5Bgoogle-iam%5D+%5Bc%23%5D)



### Go

For more information about how to use this client library, see the following resources: 

  * API reference documentation: [Go IAM v2 client library reference](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/iam/latest/apiv2)
  * Source code: [Go IAM v2 client library source code](https://github.com/googleapis/google-cloud-go/tree/main/iam/apiv2)
  * Issue tracker: [Cloud Client Libraries for Go issue tracker](https://github.com/googleapis/google-cloud-go/issues)
  * Stack Overflow: [Stack Overflow for IAM in Go](https://stackoverflow.com/search?q=%5Bgoogle-iam%5D+%5Bgo%5D)



### Java

For more information about how to use this client library, see the following resources: 

  * API reference documentation: [IAM v2 client library for Java reference](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v2)
  * Source code: [IAM v2 client library for Java source code](https://github.com/googleapis/java-iam)
  * Issue tracker: [Cloud Client Libraries for Java issue tracker](https://github.com/googleapis/java-iam/issues)
  * Stack Overflow: [Stack Overflow for IAM in Java](https://stackoverflow.com/search?q=%5Bgoogle-iam%5D+%5Bjava%5D)



### Node.js

For more information about how to use this client library, see the following resources: 

  * API reference documentation: [Node.js IAM v2 client library reference](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest)
  * Source code: [Cloud Client Libraries for Node.js source code](https://github.com/googleapis/google-cloud-node/tree/main/packages/google-iam/src/v2)
  * Issue tracker: [Cloud Client Libraries for Node.js issue tracker](https://github.com/googleapis/google-cloud-node/issues)
  * Stack Overflow: [Stack Overflow for IAM in Node.js](https://stackoverflow.com/search?q=%5Bgoogle-iam%5D+%5Bnode.js%5D)



### PHP

For more information about how to use this client library, see the following resources: 

  * API reference documentation: [PHP IAM v2 client library reference](https://docs.cloud.google.com/php/docs/reference/cloud-iam/latest)
  * Source code: [Cloud Client Libraries for PHP source code](https://github.com/googleapis/google-cloud-php/tree/main/Iam)
  * Issue tracker: [Cloud Client Libraries for PHP issue tracker](https://github.com/googleapis/google-cloud-php/issues)
  * Stack Overflow: [Stack Overflow for IAM in PHP](https://stackoverflow.com/search?q=%5Bgoogle-iam%5D+%5Bphp%5D)



### Python

For more information about how to use this client library, see the following resources: 

  * API reference documentation: [Python IAM v2 client library reference](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.services.policies)
  * Source code: [Cloud Client Libraries for Python source code](https://github.com/googleapis/python-iam)
  * Issue tracker: [Cloud Client Libraries for Python issue tracker](https://github.com/googleapis/python-iam/issues)
  * Stack Overflow: [Stack Overflow for IAM in Python](https://stackoverflow.com/search?q=%5Bgoogle-iam%5D+%5Bpython%5D)



### Ruby

For more information about how to use this client library, see the following resources: 

  * API reference documentation: [Ruby IAM v2 client library reference](https://googleapis.dev/ruby/google-iam-v2/latest/index.html)
  * Source code: [Cloud Client Libraries for Ruby source code](https://github.com/googleapis/google-cloud-ruby/tree/main/google-iam-v2)
  * Issue tracker: [Cloud Client Libraries for Ruby issue tracker](https://github.com/googleapis/google-cloud-ruby/issues)
  * Stack Overflow: [Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-iam%5D+%5Bruby%5D)



## Service Account Credentials API

Use the Service Account Credentials API to create short-lived, limited-privilege credentials for service accounts.

### Install the client library

### C++

To install the C++ client library, follow the instructions in [Setting up a C++ development environment](https://docs.cloud.google.com/cpp/docs/setup).

### C#

For more information, see [Setting up a C# development environment](https://docs.cloud.google.com/dotnet/docs/setup).
    
    
    install-package Google.Apis.IAMCredentials.v1

### Go

For more information, see [Setting up a Go development environment](https://docs.cloud.google.com/go/docs/setup).
    
    
    go get google.golang.org/api/iamcredentials/v1

### Java

For more information, see [Setting up a Java development environment](https://docs.cloud.google.com/java/docs/setup).

If you are using Maven, add this to your `pom.xml` file.
    
    
    <dependency>
      <groupId>com.google.apis</groupId>
      <artifactId>google-api-services-iamcredentials</artifactId>
      <version>v1-rev20211203-2.0.0</version>
    </dependency>

### Node.js

For more information, see [Setting up a Node.js development environment](https://docs.cloud.google.com/nodejs/docs/setup).
    
    
    npm install googleapis

### PHP

For more information, see [Using PHP on Google Cloud](https://docs.cloud.google.com/php/docs).

Add the library as a dependency to your `composer.json` file:
    
    
    "require": {
      "google/apiclient": "^2.0"
    }

Alternatively, you can [download the package locally](https://github.com/googleapis/google-api-php-client#download-the-release). 

### Python

For more information, see [Setting up a Python development environment](https://docs.cloud.google.com/python/docs/setup).
    
    
    pip install --upgrade google-cloud-iam

### Ruby

For more information, see [Setting up a Ruby development environment](https://docs.cloud.google.com/ruby/docs/setup).
    
    
    gem install google-api-client

### Additional resources

### C++

For more information about how to use this client library, see the following resources: 

  * API reference documentation: [C++ IAM client library reference](https://cloud.google.com/cpp/docs/reference/iam/latest)
  * Source code: [C++ IAM client library source code](https://github.com/googleapis/google-cloud-cpp/tree/main/google/cloud/iam)
  * Issue tracker: [Google Cloud Client Library for C++ issue tracker](https://github.com/googleapis/google-cloud-cpp/issues)
  * Stack Overflow: [Stack Overflow for IAM in C++](https://stackoverflow.com/search?q=%5Bgoogle-iam%5D+%5Bc%2B%2B%5D)



### C#

For more information about how to use this client library, see the following resources: 

  * API reference documentation: [C# Service Account Credentials client library reference](https://googleapis.dev/dotnet/Google.Apis.IAMCredentials.v1/latest/api/Google.Apis.IAMCredentials.v1.html)
  * Source code: [C# Service Account Credentials client library source code](https://github.com/googleapis/google-api-dotnet-client/tree/master/Src/Generated/Google.Apis.IAMCredentials.v1)
  * Issue tracker: [Google API Client Library for C# issue tracker](https://github.com/googleapis/google-api-dotnet-client/issues)
  * Stack Overflow: [Stack Overflow for IAM in C#](https://stackoverflow.com/search?q=%5Bgoogle-iam%5D+%5Bc%23%5D)



### Go

For more information about how to use this client library, see the following resources: 

  * API reference documentation: [Go Service Account Credentials client library reference](https://pkg.go.dev/google.golang.org/api/iamcredentials/v1)
  * Source code: [Go Service Account Credentials client library source code](https://github.com/googleapis/google-api-go-client/tree/master/iamcredentials/v1)
  * Issue tracker: [Google API Client Library for Go issue tracker](https://github.com/googleapis/google-api-go-client)
  * Stack Overflow: [Stack Overflow for IAM in Go](https://stackoverflow.com/search?q=%5Bgoogle-iam%5D+%5Bgo%5D)



### Java

For more information about how to use this client library, see the following resources: 

  * API reference documentation: [Service Account Credentials client library for Java reference](https://cloud.google.com/java/docs/reference/google-cloud-iamcredentials/latest/overview)
  * Source code: 
    * [Service Account Credentials client library for Java source code](https://github.com/googleapis/google-api-java-client-services/tree/master/clients/google-api-services-iamcredentials/v1)
    * [Google API Client Library for Java](https://github.com/googleapis/google-api-java-client)
  * Issue tracker: [Google API Client Library for Java issue tracker](https://github.com/googleapis/google-api-java-client/issues)
  * Stack Overflow: [Stack Overflow for IAM in Java](https://stackoverflow.com/search?q=%5Bgoogle-iam%5D+%5Bjava%5D)



### Node.js

For more information about how to use this client library, see the following resources: 

  * API reference documentation: [Node.js IAM client library reference](https://googleapis.dev/nodejs/googleapis/latest/iamcredentials/index.html)
  * Source code: [Node.js Service Account Credentials client library source code](https://github.com/googleapis/google-api-nodejs-client/tree/master/src/apis/iamcredentials)
  * Issue tracker: [Google API Client Library for Node.js issue tracker](https://github.com/googleapis/google-api-nodejs-client)
  * Stack Overflow: [Stack Overflow for IAM in Node.js](https://stackoverflow.com/search?q=%5Bgoogle-iam%5D+%5Bnode.js%5D)



### PHP

For more information about how to use this client library, see the following resources: 

  * Source code: 
    * [PHP Service Account Credentials client library source code](https://github.com/googleapis/google-api-php-client-services/tree/master/src/IAMCredentials)
    * [Google API Client Library for PHP](https://github.com/googleapis/google-api-php-client)
  * Issue tracker: [Google API Client Library for PHP issue tracker](https://github.com/googleapis/google-api-php-client)
  * Stack Overflow: [Stack Overflow for IAM in PHP](https://stackoverflow.com/search?q=%5Bgoogle-iam%5D+%5Bphp%5D)



### Python

For more information about how to use this client library, see the following resources: 

  * API reference documentation: [Python Service Account Credentials client library reference](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.services.iam_credentials)
  * Source code: [Cloud Client Libraries for Python](https://github.com/googleapis/python-iam)
  * Issue tracker: [Google API Client Library for Python issue tracker](https://github.com/googleapis/python-iam)
  * Stack Overflow: [Stack Overflow for IAM in Python](https://stackoverflow.com/search?q=%5Bgoogle-iam%5D+%5Bpython%5D)



### Ruby

For more information about how to use this client library, see the following resources: 

  * API documentation reference: [Ruby Service Account Credentials client library reference](https://googleapis.dev/ruby/google-api-client/latest/Google/Apis/IamcredentialsV1.html)
  * Source code: [Google API Client Library for Ruby](https://github.com/googleapis/google-api-ruby-client)
  * Issue tracker: [Google API Client Library for Ruby issue tracker](https://github.com/googleapis/google-api-ruby-client)
  * Stack Overflow: [Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-iam%5D+%5Bruby%5D)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
