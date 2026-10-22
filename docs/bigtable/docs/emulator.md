---
url: https://docs.cloud.google.com/bigtable/docs/emulator/
title: Test using the emulator \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:37:09.704881+00:00
---

# Test using the emulator  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/emulator/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Test using the emulator

The [Google Cloud CLI](https://docs.cloud.google.com/sdk) provides a local, in-memory emulator for Bigtable, which you can use to test your application. Because the emulator stores data only in memory, it won't persist data across runs. It is intended to help you use Bigtable for local development and testing, not for production deployments.

You can use the emulator with all Cloud Bigtable client libraries.

The emulator does not provide administrative APIs to create or manage instances and clusters. After the emulator starts up, you can connect to it using any project and instance name to create tables and read or write data. The emulator doesn't support a secure connection.

**Note:** You can't use the emulator in the HBase shell.

## Install and run the emulator

The two most common ways to run the emulator are by using the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud/reference/beta/emulators/bigtable) and [Docker](https://www.docker.com). Choose the way that is appropriate for your application development and test workflow.

### Set up authentication

In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

### gcloud CLI

  1. Update your gcloud CLI installation to get the latest features:
         
         gcloud components update beta
         

  2. Run the following command to start the emulator:
         
         gcloud beta emulators bigtable start
         

If the emulator is not installed already, you will be prompted to download and install the binary for the emulator.

The emulator prints the host and port number where it is running.

By default, the emulator chooses `localhost:8086`. To bind the emulator to a specific host and port, use the optional `--host-port` flag, replacing HOST and PORT:
         
         gcloud beta emulators bigtable start --host-port=HOST:PORT
         

The following is an example:
         
         gcloud beta emulators bigtable start --host-port=localhost:8086
         

**Note:** If you want to run multiple emulators, make sure that when you are starting the emulator, you specify the host and port explicitly.
  3. Type Control-C to stop the emulator.




### Docker

  1. Make sure [Docker](https://www.docker.com/products/docker-desktop) is installed on your system and available on the system path.

  2. Start the emulator:
         
         docker run -p 127.0.0.1:8086:8086 --rm -ti google/cloud-sdk gcloud beta emulators bigtable start --host-port=0.0.0.0:8086
         

This command runs the emulator and maps the ports in the container to the same ports on your local host.




You can also use the emulator as part of your existing Docker Compose configuration (`.yaml`) file. For more information about Docker Compose, see [Docker Compose Overview](https://docs.docker.com/compose/).

## Use the client libraries with the emulator

Set the `BIGTABLE_EMULATOR_HOST` environment variable to use the client libraries with the emulator:

### Linux / macOS
    
    
      export BIGTABLE_EMULATOR_HOST=localhost:8086
    

### Windows
    
    
      set BIGTABLE_EMULATOR_HOST=localhost:8086
    

When your application starts, the client library automatically checks for `BIGTABLE_EMULATOR_HOST` and connects to the emulator if it is running.

Once `BIGTABLE_EMULATOR_HOST` is set, you can test the emulator by following the [hello world samples](https://docs.cloud.google.com/bigtable/docs/samples-python-hello).

To stop the emulator, type Control-C, then unset `BIGTABLE_EMULATOR_HOST` with the following command:
    
    
        unset BIGTABLE_EMULATOR_HOST
    

### Java wrapper for the emulator

The Java wrapper bundles the built-in Bigtable emulator and provides a Java interface to write tests.

For more information about using the Java wrapper, see the [GitHub repository](https://github.com/googleapis/google-cloud-java/tree/main/java-bigtable/google-cloud-bigtable-emulator).

The following documentation provides more information about the emulator Java packages:

  * [com.google.cloud.bigtable.emulator.core](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.emulator.core)
  * [com.google.cloud.bigtable.emulator.v2](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.emulator.v2)



## Filters

The emulator supports all filters, except the [`Sink`](https://docs.cloud.google.com/bigtable/docs/using-filters#sink) limiting filter.

Issues related to the Bigtable emulator are tracked in the [google-cloud-go](https://github.com/googleapis/google-cloud-go/labels/api%3A%20bigtable) GitHub repository, where you can file bug reports and feature requests or comment on existing issues.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
