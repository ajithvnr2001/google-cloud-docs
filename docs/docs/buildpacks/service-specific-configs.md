---
url: https://docs.cloud.google.com/docs/buildpacks/service-specific-configs/
title: Configure Cloud Run and Cloud Run functions services \u00a0|\u00a0 Buildpacks \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:06:07.009699+00:00
---

# Configure Cloud Run and Cloud Run functions services  |  Buildpacks  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/buildpacks/service-specific-configs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Buildpacks ](https://docs.cloud.google.com/docs/buildpacks)
  * [ Guides ](https://docs.cloud.google.com/docs/buildpacks/overview)



Send feedback 

#  Configure Cloud Run and Cloud Run functions services Stay organized with collections  Save and categorize content based on your preferences. 

Use the following environment variables to configure the behavior of your services when deployed to either Cloud Run or Cloud Run functions.

[Learn how to set these environment variable in your container image](https://docs.cloud.google.com/docs/buildpacks/set-environment-variables).

For configuration details about a specific language, see:

  * [Go](https://docs.cloud.google.com/docs/buildpacks/go)
  * [Java](https://docs.cloud.google.com/docs/buildpacks/java)
  * [Node.js](https://docs.cloud.google.com/docs/buildpacks/nodejs)
  * [Python](https://docs.cloud.google.com/docs/buildpacks/python)
  * [Ruby](https://docs.cloud.google.com/docs/buildpacks/ruby)
  * [PHP](https://docs.cloud.google.com/docs/buildpacks/php)



## Cloud Run and Cloud Run functions environment variables

The following configurations support building services for both applications and functions. For more Cloud Run functions environment variables, see additional Cloud Run functions environment variables.

### `GOOGLE_ENTRYPOINT`

Specifies the command that is run when your container is executed. This is equivalent to [entrypoint](https://docs.docker.com/engine/reference/builder/#entrypoint) in a Dockerfile.

Examples:

###  Cloud Run source deploy 

  * Java: `java -jar target/myjar.jar`
  * PHP: `php -S 0.0.0.0:8080 index.php`
  * Python:



**Preview — Default entrypoint for Cloud Run source deploys**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The Python buildpack sets the default entrypoint for [Cloud Run source deployments](https://docs.cloud.google.com/run/docs/deploying-source-code). For Python version 3.13 and later, the Python buildpack sets the entrypoint based on the web service configuration in your `requirements.txt` file. If you don't specify a web server or framework in the `requirements.txt` file, or use Python version 3.12 and earlier, the Python buildpack sets the default entrypoint to `gunicorn -b :8080 main:app`. For more information, see [Building a Python application](https://docs.cloud.google.com/docs/buildpacks/python#run-source-deploys).

###  All other deployments 

  * Java: `java -jar target/myjar.jar`
  * PHP: `php -S 0.0.0.0:8080 index.php`
  * Python: `gunicorn -b :8080 main:app`



### `GOOGLE_RUNTIME`

Forces the runtime to opt-in. If the runtime buildpack image appears in multiple groups, the buildpack image in the first group is used across all groups.

Node.js example: Specifying `nodejs` forces the Node.js runtime buildpack to opt-in.

### `GOOGLE_RUNTIME_VERSION`

Specifies the version of your runtime to install. For .NET, specifies the .NET SDK version.

Examples:

  * Go: `1.25.1`
  * Java: `25`
  * Node.js: `24.1.0`
  * .NET: `10.0.101`



### `GOOGLE_BUILDABLE`

For Go, Java, Dart, and .NET runtimes: Specifies path to a buildable unit.

Go example: Specifying `./maindir` builds the package rooted at `maindir`.

### `GOOGLE_BUILD_ARGS`

For Java (Maven and Gradle) and .NET runtimes: Appends arguments to the build command.

Java example: Specifying `-Pprod` runs `mvn clean package ... -Pprod`.

### `GOOGLE_MAVEN_BUILD_ARGS`

For Java runtimes using the Maven plugin: Overrides the default Maven command with the build command that you specify.

When `GOOGLE_MAVEN_BUILD_ARGS` is not specified, the following command is run by default:
    
    
    mvn clean package --batch-mode -DskipTests -Dhttp.keepAlive=false
    

Example: Specifying `GOOGLE_MAVEN_BUILD_ARGS="clean package:` runs the `mvn clean package` command.

### `GOOGLE_GRADLE_BUILD_ARGS`

For Java runtimes using the Gradle plugin: Overrides the default Gradle command with the build command that you specify.

When `GOOGLE_GRADLE_BUILD_ARGS` is not specified, the following command is run by default:
    
    
    gradle clean assemble -x test --build-cache
    

Example: Specifying `GOOGLE_GRADLE_BUILD_ARGS="clean assemble"` runs the `gradle clean assemble` command.

### `GOOGLE_DEVMODE`

For [Skaffold](https://skaffold.dev): Enables the development mode buildpacks. Use live local development to trigger automatic container rebuilds for changes to your source code. You must install Skaffold and run `skaffold dev`.

  * Supported values: `true`, `True`, `1`



### `GOOGLE_CLEAR_SOURCE`

For functions and Go or Java applications: Clears source after the application is built. If the application depends on static files, such as Go templates, setting this variable may cause the application to misbehave.

Supported values: `true`, `True`, or `1`

## Additional Cloud Run functions environment variables

The following configurations are only available for source code built as functions that use [Functions Framework](https://cloud.google.com/functions/docs/functions-framework) and Cloud Run functions. For more information about these configuration option, see the [contract](https://github.com/GoogleCloudPlatform/functions-framework).

### `GOOGLE_FUNCTION_TARGET`

  * Specifies the name of the exported function to be invoked in response to requests.
  * **Example:** `myFunction` will cause the Functions Framework to invoke the function of the same name.



### `GOOGLE_FUNCTION_SIGNATURE_TYPE`

  * Specifies the signature used by the function.
  * **Example:** `http`, `event`, or `cloudevent`.



### `GOOGLE_FUNCTION_SOURCE`

  * Specifies the name of the directory or file containing the function source, depending on the language.
  * _(Only applicable to some languages, please see the language-specific[documentation](https://github.com/GoogleCloudPlatform/functions-framework#languages).)_
  * **Example:** `function.py` for Python.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
