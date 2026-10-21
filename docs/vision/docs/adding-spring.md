---
url: https://docs.cloud.google.com/vision/docs/adding-spring/
title: Using Vision with Spring framework \u00a0|\u00a0 Cloud Vision API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:01:22.846854+00:00
---

# Using Vision with Spring framework  |  Cloud Vision API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision/docs/adding-spring/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Vision API ](https://docs.cloud.google.com/vision/docs)
  * [ Guides ](https://docs.cloud.google.com/vision/docs/features-list)



Send feedback 

#  Using Vision with Spring framework Stay organized with collections  Save and categorize content based on your preferences. 

[Spring Cloud Google Cloud](https://spring.io/projects/spring-cloud-gcp) offers convenient libraries to interface with the Vision API from a Spring application. These libraries include [Auto-Configuration and helper classes](https://docs.spring.io/spring-boot/docs/current/reference/html/using-boot-auto-configuration.html) and Spring Boot Template classes to allow developers to get started with the Vision API quickly.

If you're already familiar with the [Spring Framework](https://spring.io/projects/spring-framework), then Spring Cloud Vision can make it easier to work with the Vision API in your application and reduce the amount of code that you need to write.

This page explains how to add Spring Cloud Vision to a Java application. For detailed information about the module, see the [Spring Cloud Vision reference](https://googlecloudplatform.github.io/spring-cloud-gcp/4.1.3/reference/html/index.html#cloud-vision).

## Dependency setup

To begin using this library, add the `spring-cloud-gcp-starter-vision` artifact to your project.

Maven coordinates, using Spring Cloud Google Cloud BOM:
    
    
    <dependencyManagement>
      <dependencies>
        <dependency>
          <groupId>org.springframework.cloud</groupId>
          <artifactId>spring-cloud-gcp-dependencies</artifactId>
          <version>1.2.8.RELEASE</version>
          <type>pom</type>
          <scope>import</scope>
        </dependency>
        <dependency>
          <groupId>org.springframework.boot</groupId>
          <artifactId>spring-boot-dependencies</artifactId>
          <version>${spring.version}</version>
          <type>pom</type>
          <scope>import</scope>
        </dependency>
      </dependencies>
    </dependencyManagement>
    
    
    <dependency>
      <groupId>org.springframework.cloud</groupId>
      <artifactId>spring-cloud-gcp-starter-vision</artifactId>
    </dependency>

For more information, see the instructions for [setting up a Java development environment](https://docs.cloud.google.com/java/docs/setup). You do not need to install the Google Cloud Client Library for Java; the Spring Boot starter installs the client library automatically.

## Image analysis

After configuring the Spring Cloud Google Cloud Vision dependencies on your classpath, you can immediately begin processing your images by getting an instance of `CloudVisionTemplate` using [Spring dependency injection](https://docs.spring.io/spring-boot/docs/current/reference/html/using-boot-spring-beans-and-dependency-injection.html).
    
    
    @Autowired private CloudVisionTemplate cloudVisionTemplate;

The `CloudVisionTemplate` is a wrapper around the Vision API Client Libraries and lets you process images easily through the Vision API. For more information about the `CloudVisionTemplate` features, see the [Cloud Vision template reference page](https://googlecloudplatform.github.io/spring-cloud-gcp/4.1.3/reference/html/index.html#cloud-vision).

The following sections contain code samples for common use cases of the `CloudVisionTemplate`. All code snippets come from the [Spring and Cloud Vision sample application](https://github.com/GoogleCloudPlatform/java-docs-samples/tree/master/vision/spring-framework).

### Getting the classification labels for an image

The code below extracts the classification labels for an image, providing you with general descriptions of image content.
    
    
    AnnotateImageResponse response =
        this.cloudVisionTemplate.analyzeImage(
            this.resourceLoader.getResource(imageUrl), Type.LABEL_DETECTION);
    
    Map<String, Float> imageLabels =
        response.getLabelAnnotationsList().stream()
            .collect(
                Collectors.toMap(
                    EntityAnnotation::getDescription,
                    EntityAnnotation::getScore,
                    (u, v) -> {
                      throw new IllegalStateException(String.format("Duplicate key %s", u));
                    },
                    LinkedHashMap::new));

### Extracting the Text In an Image

The code sample below describes another common operation of extracting the text from an image.
    
    
    String textFromImage =
        this.cloudVisionTemplate.extractTextFromImage(this.resourceLoader.getResource(imageUrl));
    return "Text from image: " + textFromImage;

## What's next

  * [Get started with Spring Cloud Google Cloud](https://googlecloudplatform.github.io/spring-cloud-gcp/4.1.3/reference/html/index.html#getting-started).
  * Learn more about [using Spring Cloud Vision in your applications](https://googlecloudplatform.github.io/spring-cloud-gcp/4.1.3/reference/html/index.html#cloud-vision).
  * [File a GitHub issue](https://github.com/GoogleCloudPlatform/spring-cloud-gcp/issues) to report a bug or ask a question about the module.
  * Get more information about [Spring Framework support on Google Cloud](https://docs.cloud.google.com/java/docs/reference/spring).
  * Try a codelab to [deploy and run an application that uses Spring Cloud Google Cloud](https://codelabs.developers.google.com/spring/).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
