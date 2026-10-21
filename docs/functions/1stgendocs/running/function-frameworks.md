---
url: https://docs.cloud.google.com/functions/1stgendocs/running/function-frameworks/
title: Run functions with Functions Framework \u00a0|\u00a0 Cloud Run functions (1st gen) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:29:33.268046+00:00
---

# Run functions with Functions Framework  |  Cloud Run functions (1st gen)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/1stgendocs/running/function-frameworks/

If you are creating a new function, see the [Console Quickstart](https://cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. The content on this page only applies to existing legacy functions created with the Cloud Functions v1 API. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ 1st generation ](https://docs.cloud.google.com/functions/1stgendocs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/functions/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Run functions with Functions Framework

Cloud Run functions uses the open-source [Functions Framework](https://docs.cloud.google.com/functions/1stgendocs/functions-framework) libraries to wrap your deployed functions in a persistent HTTP application.

The Functions Framework can also run on any other platform that supports the language itself, including your local machine, on-premises servers, [Compute Engine](https://cloud.google.com/products/compute), and [Cloud Run](https://docs.cloud.google.com/run).

**Note:** if you're interested in building locally runnable _containers_ , see [Using the Functions Emulator](https://docs.cloud.google.com/functions/1stgendocs/running/functions-emulator).

## Install dependencies

In your function's directory, install the Functions Framework library for your language:

See the [Java Functions Framework library](https://github.com/GoogleCloudPlatform/functions-framework-java) for more information.

###  Node.js 

**Note:** This library is automatically included when deploying your function if you do not specify it in your function's dependencies. 
    
    
    npm install --save-dev @google-cloud/functions-framework

###  Python 

**Note:** This library is automatically included when deploying your function if you do not specify it in your function's dependencies. 
    
    
    pip install functions-framework

###  Go 

**Note:** This library is automatically included when deploying your function if you do not specify it in your function's dependencies. 
    
    
    go install github.com/GoogleCloudPlatform/functions-framework-go/funcframework

###  Java 

**Note:** This library is automatically included when deploying your function if you do not specify it in your function's dependencies. 

#### Maven

If you're using [Maven](http://maven.apache.org/install.html), add the following to your `pom.xml` file:
    
    
    <dependency>
      <groupId>com.google.cloud.functions</groupId>
      <artifactId>functions-framework-api</artifactId>
      <version>1.1.0</version>
      <scope>provided</scope>
    </dependency>

#### Gradle

If you're using [Gradle](https://gradle.org/), add the following to your `build.gradle` file:
    
    
    dependencies {
      // Every function needs this dependency to get the Functions Framework API.
      compileOnly 'com.google.cloud.functions:functions-framework-api:1.1.0'
    
      // To run function locally using Functions Framework's local invoker
      invoker 'com.google.cloud.functions.invoker:java-function-invoker:1.3.1'
    }

###  C# 

The commands below use .NET Templates to create a new .NET Cloud Run function codebase with the [.NET Functions Framework library](https://github.com/GoogleCloudPlatform/functions-framework-dotnet) as a dependency:
    
    
    # HTTP functions
    dotnet new gcf-http
    
    # CloudEvent functions
    dotnet new gcf-event

###  Ruby 

In Ruby the Functions Framework **must** be added to your function's dependencies in order to deploy it to Cloud Run functions:
    
    
    bundle add functions_framework

###  PHP 

**Note:** This library is automatically included when deploying your function if you do not specify it in your function's dependencies. 
    
    
    composer require google/cloud-functions-framework

## Configure the Functions Framework

Before running a function using the Functions Framework, you'll first need to specify both the type and the name of the function you want to run. These attributes can be specified as either command-line interface (CLI) flag or as environment variables.

#### Supported function types

The Functions Framework supports all three types of functions supported by Cloud Run functions 1st gen. All language runtimes support `http` and one of either `event` or `cloudevent`.

Function type | Signature type | Description | Supporting Runtimes  
---|---|---|---  
[HTTP-triggered functions](https://docs.cloud.google.com/functions/1stgendocs/writing/write-http-functions) |  `http` |  Functions that receive and respond to HTTP requests.  |  All runtimes   
[Background functions](https://docs.cloud.google.com/functions/1stgendocs/writing/write-event-driven-functions#background-functions) |  `event` |  Cloud Run functions-specific event format  |  [Node.js](https://docs.cloud.google.com/functions/1stgendocs/concepts/nodejs-runtime), [Python](https://docs.cloud.google.com/functions/1stgendocs/concepts/python-runtime), [Go](https://docs.cloud.google.com/functions/1stgendocs/concepts/go-runtime), [Java](https://docs.cloud.google.com/functions/1stgendocs/concepts/java-runtime)  
[CloudEvent functions](https://docs.cloud.google.com/functions/1stgendocs/writing/write-event-driven-functions#cloudevent-functions) |  `cloudevent` |  Industry-standard event format  |  [.NET](https://docs.cloud.google.com/functions/1stgendocs/concepts/dotnet-runtime), [Ruby](https://docs.cloud.google.com/functions/1stgendocs/concepts/ruby-runtime), [PHP](https://docs.cloud.google.com/functions/1stgendocs/concepts/php-runtime)  
  
#### Specify which function to run

Before running a function with the Functions Framework, you must first specify which function within your code should be run. For most languages, you can do this by specifying the target function's method name as shown in the tables below. (Exceptions to this rule such as [Java](https://docs.cloud.google.com/functions/1stgendocs/concepts/java-runtime) and [.NET](https://docs.cloud.google.com/functions/1stgendocs/concepts/dotnet-runtime) are also shown below.)

#### Per-language instructions

See the table below for a list of configuration options supported by each language.

###  Node.js 

CLI Argument  |  Environment Variable  |  Description   
---|---|---  
`--port` |  `PORT` |  The port to listen for requests on. (Default: `8080`)   
`--target` |  `FUNCTION_TARGET` |  The name of the `export`ed function to be invoked. (Default: `function`)   
`--signature-type` |  `FUNCTION_SIGNATURE_TYPE` |  The signature type used by your function. Can be one of `http` (the default), `event`, or `cloudevent`.   
  
###  Python 

CLI Argument  |  Environment Variable  |  Description   
---|---|---  
`--port` |  `PORT` |  The port to listen for requests on. (Default: `8080`)   
`--target` |  `FUNCTION_TARGET` |  The name of the `export`ed function to be invoked. (Default: `function`)   
`--signature-type` |  `FUNCTION_SIGNATURE_TYPE` |  The signature type used by your function. Can be one of `http` (the default), `event`, or `cloudevent`.   
  
###  Go 

Environment Variable  |  Description   
---|---  
`PORT` |  The port to listen for requests on. (Default: `8080`)   
**Note:** the Go Functions Framework automatically detects your function's signature type. 

###  Java 

Argument Name  |  Environment Variable  |  Description   
---|---|---  
`run.port` |  `PORT` |  The port to listen for requests on. (Default: `8080`)   
`run.functionTarget` |  `FUNCTION_TARGET` |  The name of the `export`ed function to be invoked. (Default: `function`)   
**Note:** the Java Functions Framework automatically detects your function's signature type. 

###  C# 

CLI Argument  |  Environment Variable  |  Description   
---|---|---  
`--port` |  `PORT` |  The port to listen for requests on. (Default: `8080`)   
`--target` (or only argument)  |  `FUNCTION_TARGET` |  The _classname_ of the function to be invoked. (Default: `function`)   
**Note:** the .NET Functions Framework automatically detects your function's signature type. 

###  Ruby 

CLI Argument  |  Environment Variable  |  Description   
---|---|---  
`--port` |  `PORT` |  The port to listen for requests on. (Default: `8080`)   
`--target` |  `FUNCTION_TARGET` |  The name of the `export`ed function to be invoked. (Default: `function`)   
  
###  PHP 

Environment Variable  |  Description   
---|---  
`FUNCTION_TARGET` |  The name of the function to be invoked. (Default: `function`)   
`FUNCTION_SIGNATURE_TYPE` |  The signature type used by your function. Can be one of `http` (the default), `event`, or `cloudevent`.   
  
Follow the instructions below to configure and run the Functions Framework:

###  Node.js 

The Node.js Functions Framework allows you to specify your function's name and signature type as command line arguments or [environment variables](https://github.com/GoogleCloudPlatform/functions-framework-nodejs/#configure-the-functions-framework).

**Note:** command-line arguments take precedence over environment variables when running the Node.js Functions Framework.

You can also specify these values in the `package.json` buildfile by adding a `start` script with the required CLI arguments as shown in the example below.
    
    
    "scripts": {
      "start": "npx functions-framework --target=YOUR_FUNCTION_NAME [--signature-type=YOUR_SIGNATURE_TYPE]"
    }

The same can be done using environment variables:
    
    
    "scripts": {
      "start": "FUNCTION_TARGET=YOUR_FUNCTION_NAME FUNCTION_SIGNATURE_TYPE=YOUR_SIGNATURE_TYPE npx functions-framework"
    }

Replace YOUR_FUNCTION_NAME with the method name of your function, and YOUR_SIGNATURE_TYPE (if applicable) with the signature type of your function as shown in the table above. 

###  Python 

The Python Functions Framework allows you to specify your function's name and signature type as command line arguments or [environment variables](https://github.com/GoogleCloudPlatform/functions-framework-python/#configure-the-functions-framework). Command-line arguments must be specified when you run the framework.

**Note:** command-line arguments take precedence over environment variables when running the Python Functions Framework.

###  Go 

The Go Functions Framework uses `funcframework.RegisterHTTPFunctionContext` to specify the function target and signature type.

###  Java 

The Java Functions Framework accepts configuration data from three different sources, in the following priority order (most specific to least specific):

  * Command-line arguments
  * Buildfiles
  * Environment variables



### Command-line arguments

#### Maven

You can specify the function you want to run by adding the following command-line interface (CLI) flag to your `mvn` commands:
    
    
    -Drun.functionTarget=YOUR_FUNCTION_NAME

You can also specify the target port by adding the following CLI flag in a similar manner:
    
    
    -Drun.port=12345

#### Gradle

Gradle's CLI flags are nearly identical to Maven's. The only change Gradle makes is to swap the leading `-D` in each flag for a `-P` as shown in the example below:
    
    
    # Maven version
    **-D** run.functionTarget=...
    
    # Gradle version
    **-P** run.functionTarget=...

### Buildfiles

You can also specify the function you want to run in your project's buildfile. While Maven and Gradle have similar CLI flags, their buildfile clauses differ significantly.

#### Maven

Maven buildfiles are named `pom.xml`. Add the following clause to this file to specify a target function:
    
    
    <plugin>
      <groupId>com.google.cloud.functions</groupId>
      <artifactId>function-maven-plugin</artifactId>
      <version>0.11.0</version>
      <configuration>
        <functionTarget>functions.HelloWorld</functionTarget>
      </configuration>
    </plugin>

Replace `<functionTarget>` with the class name of your function. (For example, a function in package `functions` with class name `HelloCloudFunctions` would have a class name of `functions.HelloCloudFunctions`. This is relative to the parent build file \- either `pom.xml` or `build.gradle`).

#### Gradle

Gradle buildfiles are named `build.gradle`. Add the following clause to this file to specify a target function:
    
    
    // Register a "runFunction" task to run the function locally
    tasks.register("runFunction", JavaExec) {
      main = 'com.google.cloud.functions.invoker.runner.Invoker'
      classpath(configurations.invoker)
      inputs.files(configurations.runtimeClasspath, sourceSets.main.output)
      args(
        '--target', project.findProperty('run.functionTarget') ?: '',
        '--port', project.findProperty('run.port') ?: 8080
      )
      doFirst {
        args('--classpath', files(configurations.runtimeClasspath, sourceSets.main.output).asPath)
      }
    }

###  C# 

If you create your project using `dotnet new` and one of the templates specified above, the .NET Functions Framework will automatically detect your function.

If your project contains multiple functions, see the Running the Framework section for information on how to run a specific function. 

###  Ruby 

The Ruby Functions Framework allows you to specify your function's name and signature type as command line arguments or [environment variables](https://googlecloudplatform.github.io/functions-framework-ruby/v0.9.0/file.running-a-functions-server.html#configuring-the-server). Command-line arguments must be specified when you run the framework.

**Note:** command-line arguments take precedence over environment variables when running the Ruby Functions Framework. 

###  PHP 

The PHP Functions Framework allows you to specify [environment variables](https://github.com/GoogleCloudPlatform/functions-framework-php#configure-the-functions-framework) as command line arguments.

You can also specify these values in the `composer.json` buildfile by adding a `start` script as shown in the example below.
    
    
    "scripts": {
       "start": [
           "Composer\\Config::disableProcessTimeout",
           "FUNCTION_TARGET=YOUR_FUNCTION_NAME php -S localhost:${PORT:-8080} vendor/bin/router.php"
        ]
    }

Replace YOUR_FUNCTION_NAME with the name of your function, and YOUR_SIGNATURE_TYPE (if applicable) with the signature type of your function as shown in the table above. 

## Run the Functions Framework

Use the following command to run your function with the Functions Framework. By default, your function will be accessible at `localhost:8080` unless you explicitly specify a `PORT` value.

###  Node.js 
    
    
    npm start

###  Python 

Using command line arguments: 
    
    
    functions-framework --target=YOUR_FUNCTION_NAME

Using environment variables: 
    
    
    FUNCTION_TARGET=YOUR_FUNCTION_NAME functions-framework

Replace YOUR_FUNCTION_NAME with your function's method name. 

###  Go 

**Note:** First create a `cmd/main.go` file as described on the [Functions Framework for Go](https://github.com/GoogleCloudPlatform/functions-framework-go#quickstart-hello-world-on-your-local-machine) site.
    
    
    cd cmd
    go build
    ./cmd

Using environment variables: 
    
    
    cd cmd
    go build
    PORT=8080 ./cmd

###  Java 

#### Maven

Use the following command to run a function specified in `pom.xml`: 
    
    
    mvn function:run

Use the following command to run a function specified in a command-line argument: 
    
    
    mvn function:run -Drun.functionTarget=YOUR_FUNCTION_NAME

Use the following command to run a function specified as an environment variable: 
    
    
    FUNCTION_TARGET=YOUR_FUNCTION_NAME mvn function:run

Replace YOUR_FUNCTION_NAME with your function's classname.

#### Gradle

Use the following command to run a function specified in `build.gradle`:
    
    
    ./gradlew runFunction

Use the following command to run a function specified in a command-line argument: 
    
    
    ./gradlew runFunction -Prun.functionTarget=YOUR_FUNCTION_NAME

Use the following command to run a function specified as an environment variable: 
    
    
    FUNCTION_TARGET=YOUR_FUNCTION_NAME ./gradlew runFunction

Replace YOUR_FUNCTION_NAME with your function's classname. 

###  C# 

Use the following command to run your function when exactly one function is present in the current .NET project. (This is the default structure for template-created projects.) 
    
    
    dotnet run

**Note:** the .NET runtime detects functions by searching for classes that implement one of the Functions Framework interfaces (`IHttpFunction` or `ICloudEventFunction`).

If your .NET project contains multiple functions, use the following command to run a specific function. Replace YOUR_FUNCTION_CLASSNAME with your function's classname, including the namespace. 
    
    
    dotnet run YOUR_FUNCTION_CLASSNAME

If you want to run multiple functions simultaneously, you'll need to run multiple Functions Framework instances. To avoid conflicts between running framework instances, each instance should use a different `PORT` value. The following command shows how to run a function with a `PORT` value of `8080`.

Using command line arguments: 
    
    
    dotnet run --target YOUR_FUNCTION_CLASSNAME --port 8080

Using environment variables: 
    
    
    FUNCTION_TARGET=YOUR_FUNCTION_CLASSNAME PORT=8080 dotnet run

###  Ruby 

Using command line arguments: 
    
    
    bundle exec functions-framework-ruby --target YOUR_FUNCTION_NAME

Using environment variables: 
    
    
    FUNCTION_TARGET=YOUR_FUNCTION_NAME bundle exec functions-framework-ruby

Replace YOUR_FUNCTION_NAME with your function's method name. 

###  PHP 
    
    
    export FUNCTION_TARGET=YOUR_FUNCTION_NAME
    php -S localhost:8080 vendor/bin/router.php

Replace YOUR_FUNCTION_NAME with your function's name. 

## Call your function

See the [calling local functions](https://docs.cloud.google.com/functions/1stgendocs/running/calling) page for instructions on how to interact with your locally-running function.

## Clean up

Once you're finished running your function, stop the running framework instance by pressing Control+C.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
