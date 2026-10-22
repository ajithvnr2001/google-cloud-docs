---
url: https://docs.cloud.google.com/artifact-registry/docs/java/troubleshoot/
title: Troubleshoot Java package issues \u00a0|\u00a0 Artifact Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:18:42.312604+00:00
---

# Troubleshoot Java package issues  |  Artifact Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/java/troubleshoot/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-registry/docs/overview)



Send feedback 

#  Troubleshoot Java package issues Stay organized with collections  Save and categorize content based on your preferences. 

Learn about troubleshooting steps that you might find helpful if you run into problems managing java packages in Artifact Registry.

### Can't resolve a dependency stored in Artifact Registry

Maven resolves some dependencies before applying a wagon defined in `pom.xml`, including:

  * References in a child Maven project to a parent project using the `<parent>` element.
  * Plugin dependencies stored in Artifact Registry.



If your project needs to resolve these dependencies, you must use the [core extensions](https://maven.apache.org/docs/3.3.1/release-notes.html) mechanism to ensure that Maven can locate parent POM files and plugins.

In your project, create the file `${maven.projectBasedir}/.mvn/extensions.xml` with the following content. The `<extension>` element defines the wagon.
    
    
    <extensions xmlns="http://maven.apache.org/EXTENSIONS/1.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://maven.apache.org/EXTENSIONS/1.0.0 http://maven.apache.org/xsd/core-extensions-1.0.0.xsd">
      <extension>
        <groupId>com.google.cloud.artifactregistry</groupId>
        <artifactId>artifactregistry-maven-wagon</artifactId>
        <version>2.2.5</version>
      </extension>
    </extensions>
    

### Can't upload non-unique snapshots to a snapshot repository

You can upload snapshot versions that do not exist in an Artifact Registry snapshot repository, but you cannot overwrite a version that already exists in the repository.

Non-unique snapshots are a feature of Maven 2. Maven 3 always adds a timestamp to snapshot version numbers so that every snapshot version is unique.

Artifact Registry only supports non-unique snapshot versions in repositories with a snapshot version policy. By default snapshot repositories only accept unique snapshot versions. You can only set a version policy when you create the repository.

To find out the version policy settings for a repository, run the following command:
    
    
    gcloud artifacts repositories describe REPOSITORY \
        [--project=PROJECT] \
        [--location=LOCATION]
    

Where

  * REPOSITORY is the ID of the repository. If you configured a [default](https://docs.cloud.google.com/artifact-registry/docs/gcloud-defaults) Artifact Registry repository, it is used when this flag is omitted from the command.
  * PROJECT is the project ID. If this flag is omitted, the current or [default project](https://docs.cloud.google.com/artifact-registry/docs/gcloud-defaults#project) is used.
  * LOCATION is the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) for the repository.



The output of the command includes information about the version policy under `mavenConfig`. In the following example, the repository has a snapshot version policy and snapshots cannot overwrite identical versions in the repository.
    
    
    Encryption: Google-managed key
    createTime: '2021-09-23T19:39:10.897404Z'
    format: MAVEN
    mavenConfig:
     allowSnapshotOverwrites: false
     versionPolicy: SNAPSHOT
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
