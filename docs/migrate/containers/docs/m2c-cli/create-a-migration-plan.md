---
url: https://docs.cloud.google.com/migrate/containers/docs/m2c-cli/create-a-migration-plan/
title: Create a migration plan \u00a0|\u00a0 Migrate to Containers \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:17:22.310470+00:00
---

# Create a migration plan  |  Migrate to Containers  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/containers/docs/m2c-cli/create-a-migration-plan/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Containers ](https://docs.cloud.google.com/migrate/containers/docs)
  * [ Guides ](https://docs.cloud.google.com/migrate/containers/docs/getting-started)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

#  Create a migration plan 

After creating a copy of the source machine's file system on your local machine, the next step is to analyze the file system to prepare a migration plan. The migration plan can then be used to generate migration artifacts.

This page describes the steps required to prepare a migration plan for different workloads.

## Create a migration plan for a Linux VM container

To perform the analysis, run the following command:
    
    
    ./m2c analyze \
      -s PATH_TO_COPIED_FILESYSTEM \
      -p linux-vm-container \
      -o ANALYSIS_OUTPUT_PATH \
      [ -r skip_size_checks=SKIP_SIZE_CHECKS  ] \
      [ -r big_files_threshold_mb=SIZE_IN_MB ]
    

Replace the following:

  * PATH_TO_COPIED_FILESYSTEM: the path to copied file system directory.
  * ANALYSIS_OUTPUT_PATH: the path to the folder where you want the analysis output to be created.
  * SKIP_SIZE_CHECKS: this is an optional parameter. By default, this is set to `false` and Migrate to Containers CLI checks the image layers to ensure that the size doesn't exceed 15 GB. If the total size of the image layers exceeds 15 GB, then the artifact generation fails and Migrate to Containers CLI displays an error message. To skip this size check, set this parameter to `true`.
  * SIZE_IN_MB: this is an optional parameter. Specify a file size threshold, in MB, to check for files that exceed a specific size. If Migrate to Containers CLI detects a file with a size that exceeds the specified size threshold, then Migrate to Containers CLI adds a comment in the generated migration plan with a suggestion to exclude the detected file from the container image.



After the analysis is complete, a new directory is created in the specified output path which contains the migration plan, `config.yaml`.

## Create a migration plan for Tomcat workloads

For Tomcat app components, this process requires the `catalina-home` and `catalina-base` paths as inputs.

To retrieve these values, check the running Tomcat server process:
    
    
    ps aux | grep catalina
    

To perform the analysis, run the following command:
    
    
    ./m2c analyze \
      -s PATH_TO_COPIED_FILESYSTEM \
      -p tomcat-container \
      -o ANALYSIS_OUTPUT_PATH \
      -r catalina-home=PATH_TO_CATALINA_HOME \
      -r catalina-base=PATH_TO_CATALINA_BASE \
      -r java-version=JAVA_VERSION
    

Replace the following:

  * PATH_TO_COPIED_FILESYSTEM: the path to copied file system directory
  * ANALYSIS_OUTPUT_PATH: the path to the folder where you want the analysis output to be created
  * PATH_TO_CATALINA_HOME: path to the root of the Tomcat installation
  * PATH_TO_CATALINA_BASE: path to the root of the runtime configuration of the Tomcat instance that you're migrating. Multiple bases should be separated using colon
  * JAVA_VERSION: Java version of the container in `X.Y` format. The default Java version is `11.0`.



After the analysis is complete, a new directory is created in the specified output path which contains the migration plan, `config.yaml`.

## Create a migration plan for WebSphere workloads

### Optional: Set up the binaryAppScanner.jar

**Note:** If you want to migrate Liberty workloads and maintain their Java environment, you don't need to set up the `binaryAppScanner.jar`.

If you want to migrate WebSphere traditional workloads, or perform a migration between different Java environments, you can set up the `binaryAppScanner.jar`. Migrate to Containers CLI automates the use of the `binaryAppScanner.jar` to generate new WebSphere configurations and facilitate Java runtime modernization.

To set up the `binaryAppScanner.jar`:

  1. Download the installer file, `binaryAppScannerInstaller.jar`, from [IBM Support](https://www.ibm.com/support/pages/migration-toolkit-application-binaries). You must accept the license agreement as part of the download.

  2. Extract the `binaryAppScanner.jar` file and accept the license agreement:
         
         java -jar binaryAppScannerInstaller.jar --acceptLicense --verbose INSTALL_LOCATION
         

Replace the following:

     * INSTALL_LOCATION: the target directory for extraction. For example, if you specify `/tmp` as the target directory, after the installation is complete, `binaryAppScanner.jar` is available at `/tmp/wamt/binaryAppScanner.jar`.



### Perform the analysis

To perform the analysis, run the following command:
    
    
    ./m2c analyze \
      -s PATH_TO_COPIED_FILESYSTEM \
      -p websphere-container \
      -o ANALYSIS_OUTPUT_PATH \
      -r websphere-profile=WEBSPHERE_PROFILE \
      -r websphere-home=WEBSPHERE_HOME \
      -r websphere-java-home=WEBSPHERE_JAVA_HOME \
      -r target-profile=TARGET_PROFILE \
      -r target-version=TARGET_VERSION \
      -r target-edition=TARGET_EDITION \
      -r target-se=TARGET_SE \
      -r target-ee=TARGET_EE \
      -r target-vendor=TARGET_VENDOR \
      -r target-base-image=TARGET_BASE_IMAGE \
      --volume PATH_TO_BINARYAPPSCANNER:/binaryAppScanner.jar
    

Replace the following:

  * PATH_TO_COPIED_FILESYSTEM: the path to copied file system directory.
  * ANALYSIS_OUTPUT_PATH: the path to the folder where you want the analysis output to be created.
  * WEBSPHERE_PROFILE: this is an optional parameter. Specify the WebSphere profile used in the source VM. Format: [Liberty|Traditional].
  * WEBSPHERE_HOME: this is an optional parameter. Specify the path to the application server installation in the source VM.
  * WEBSPHERE_JAVA_HOME: this is an optional parameter. Specify the path to the Java installation in the source VM.
  * TARGET_PROFILE: this is an optional parameter. Specify the WebSphere profile to use in the target container. Format: [Liberty|Traditional]. Defaults to the source profile.
  * TARGET_VERSION: this is an optional parameter. Specify the WebSphere version to use in the target container. Defaults to the source version.
  * TARGET_EDITION: this is an optional parameter. Specify the WebSphere edition to use in the target container. Format: [Base|Core|Open|ND]. Defaults to the source edition.
  * TARGET_SE: this is an optional parameter. Specify the Java SE version to use in the target container. Format: [SE8|SE11|SE17]. Defaults to the source Java SE.
  * TARGET_EE: this is an optional parameter. Specify the Java EE or Jakarta EE version to use in the target container. Format: [EE7|EE8|EE9|EE10]. Defaults to the source Java EE or Jakarta EE.
  * TARGET_VENDOR: this is an optional parameter. Specify the Java vendor to use in the target container. Format: [IBM Corporation|Oracle Corporation]. Defaults to the source Java vendor.
  * TARGET_BASE_IMAGE: this is an optional parameter. Specify a base image to use for the target container.
  * PATH_TO_BINARYAPPSCANNER: this is an optional parameter. Specify the path to the `binaryAppScanner.jar` file on your local machine.



After the analysis is complete, a new directory is created in the specified output path which contains the migration plan, `config.yaml`.

## Create a migration plan for WebSphere traditional workloads

**Important:** The `websphere-traditional` plugin is now deprecated. For existing customers, this plugin is still supported till December 2023, after which it will no longer be available. If you're new to WebSphere workload modernization, then use the `websphere-container` plugin with the Migrate to Containers CLI instead.

### Set up the binaryAppScanner.jar

Download the latest version of the `binaryAppScanner.jar` file.

If you've already installed the `binaryAppScanner.jar` file, check the current version:
    
    
    java -jar binaryAppScanner.jar --version

Then, compare your current version to the version shown in the IBM license that appears when you click **Migration Toolkit for Application Binaries** to download the file. If they differ, download the latest version of the `binaryAppScanner.jar` file.

Migrate to Containers CLI automates the use of the `binaryAppScanner.jar`, available as part of the [IBM WebSphere Application Server Migration Toolkit for Application Binaries](https://www.ibm.com/support/pages/migration-toolkit-application-binaries), to extract configuration information and files for WebSphere Application Server applications in the source VM.

Before you can perform a migration, you must accept the license agreement and download the [IBM WebSphere Application Server Migration Toolkit for Application Binaries](https://www.ibm.com/support/pages/migration-toolkit-application-binaries), and then extract the `binaryAppScanner.jar` file.

To set up `binaryAppScanner.jar`:

  1. Download the installer file, `binaryAppScannerInstaller.jar`, from [IBM Support](https://www.ibm.com/support/pages/migration-toolkit-application-binaries). You must accept the license agreement as part of the download.

  2. Run the following command to extract the `binaryAppScanner.jar` file and to accept the License Agreement:
         
         java -jar binaryAppScannerInstaller.jar --acceptLicense --verbose
         

  3. Specify the target directory for the extraction. For example, if you specify `/tmp` as the target directory, after the installation is complete, `binaryAppScanner.jar` is available at `/tmp/wamt/binaryAppScanner.jar`.




### Retrieve `WAS_HOME`

The `WAS_HOME` environment variable specifies where WebSphere Application Server traditional is installed, such as `/opt/IBM/WebSphere/AppServer/`. Migrate to Containers CLI uses this value to correctly locate and analyze the WebSphere traditional configuration.

To retrieve this value, check the running WebSphere Application Server traditional process:
    
    
    ps aux | grep WAS_HOME
    

### Run the analysis

To perform the analysis, run the following command:
    
    
    ./m2c analyze \
      -s PATH_TO_COPIED_FILESYSTEM \
      -p websphere-traditional-container -o ANALYSIS_OUTPUT_PATH \
      -r was-home=PATH_TO_WAS_HOME \
      --volume PATH_TO_BINARYAPPSCANNER:/binaryAppScanner.jar
    

Replace the following:

  * PATH_TO_COPIED_FILESYSTEM: the path to copied file system directory.
  * ANALYSIS_OUTPUT_PATH: the path to the folder where you want the analysis output to be created.
  * PATH_TO_WAS_HOME: path to the WebSphere Application Server traditional installation.
  * PATH_TO_BINARYAPPSCANNER: path to the `binaryAppScanner.jar` file. For example, if you specified `/tmp` as your target directory, then `binaryAppScanner.jar` is available at `/tmp/wamt/binaryAppScanner.jar`.



After the analysis is complete, a new directory is created in the specified output path which contains the migration plan, `config.yaml`.

## Create a migration plan for JBoss workloads

For JBoss app components, creating a migration plan requires the `JBOSS_HOME` variable as an input.

To retrieve this value, check the running JBoss server process:
    
    
    ps aux | grep jboss.home.dir
    

To perform the analysis, run the following command:
    
    
    ./m2c analyze \
      -s PATH_TO_COPIED_FILESYSTEM \
      -p jboss-container \
      -o ANALYSIS_OUTPUT_PATH \
      -r jboss-home=PATH_TO_JBOSS_HOME
    

Replace the following:

  * PATH_TO_COPIED_FILESYSTEM: the path to copied file system directory
  * ANALYSIS_OUTPUT_PATH: the path to the folder where you want the analysis output to be created
  * PATH_TO_JBOSS_HOME: path to the JBoss installation



After the analysis is complete, a new directory is created in the specified output path which contains the migration plan, `config.yaml`.

## Create a migration plan for Apache workloads

To perform the analysis, run the following command:
    
    
    ./m2c analyze \
      -s PATH_TO_COPIED_FILESYSTEM \
      -p apache-container \
      -o ANALYSIS_OUTPUT_PATH
    

Replace the following:

  * PATH_TO_COPIED_FILESYSTEM: the path to copied file system directory
  * ANALYSIS_OUTPUT_PATH: the path to the folder where you want the analysis output to be created



After the analysis is complete, a new directory is created in the specified output path which contains the migration plan, `config.yaml`.

## Create a migration plan for WordPress workloads

To perform the analysis, run the following command:
    
    
    ./m2c analyze \
      -s PATH_TO_COPIED_FILESYSTEM \
      -p wordpress-container \
      -o ANALYSIS_OUTPUT_PATH
    

Replace the following:

  * PATH_TO_COPIED_FILESYSTEM: the path to copied file system directory
  * ANALYSIS_OUTPUT_PATH: the path to the folder where you want the analysis output to be created



After the analysis is complete, a new directory is created in the specified output path which contains the migration plan, `config.yaml`.

## Create a migration plan for Windows IIS services

To perform the analysis, run the following command:
    
    
    ./m2c analyze -s PATH_TO_IMAGE -p windows-iis-container -o ANALYSIS_OUTPUT_PATH
    

Replace the following:

  * PATH_TO_IMAGE: the path to source machine disk image. You can specify more than one disk image at a time using multiple `-s` flags. For example, `-s PATH_TO_IMAGE_1 -s PATH_TO_IMAGE_2...-s PATH_TO_IMAGE_N`.
  * ANALYSIS_OUTPUT_PATH: the path to the folder where you want the analysis output to be created.



After the analysis is complete, a new directory is created in the specified output path which contains the migration plan, `config.yaml`.

## What's next

  * Learn how to customize the migration plan for the following: 
    * [Linux VMs](https://docs.cloud.google.com/migrate/containers/docs/m2c-cli/linux/customizing-a-migration-plan)
    * [Tomcat](https://docs.cloud.google.com/migrate/containers/docs/m2c-cli/tomcat/tomcat-customizing-a-migration-plan)
    * [WebSphere Liberty](https://docs.cloud.google.com/migrate/containers/docs/m2c-cli/websphere/websphere-customizing-a-migration)
    * [WebSphere traditional](https://docs.cloud.google.com/migrate/containers/docs/m2c-cli/websphere-traditional/websphere-traditional-customizing-a-migration)
    * [JBoss](https://docs.cloud.google.com/migrate/containers/docs/m2c-cli/jboss/jboss-customizing-a-migration-plan)
    * [Apache](https://docs.cloud.google.com/migrate/containers/docs/m2c-cli/apache/apache-customizing-a-migration-plan)
    * [WordPress](https://docs.cloud.google.com/migrate/containers/docs/m2c-cli/wordpress/wordpress-customizing-a-migration-plan)
    * [Windows IIS services](https://docs.cloud.google.com/migrate/containers/docs/m2c-cli/windows/windows-customizing-a-migration-plan)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
