---
url: https://docs.cloud.google.com/migrate/kf/docs/2.7/how-to/deploying-spring-cloud-config/
title: Deploy Spring Cloud Config \u00a0|\u00a0 Kf 2.7 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:14:05.514667+00:00
---

# Deploy Spring Cloud Config  |  Kf 2.7  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/kf/docs/2.7/how-to/deploying-spring-cloud-config/

Version 2.7

Available versions

[2.11 - Latest version](https://docs.cloud.google.com/migrate/kf/docs/2.11)  
[2.10](https://docs.cloud.google.com/migrate/kf/docs/2.10)  
[2.9](https://docs.cloud.google.com/migrate/kf/docs/2.9)  
[2.8 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.8)  
[2.7 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.7)  
[2.6 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.6)  
[2.5 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.5)  
[2.4 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.4)  
[2.3 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.3)  
[2.2 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.2)  
[2.1 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.1)  


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Kf ](https://docs.cloud.google.com/migrate/kf/docs)
  * [ 2.7 ](https://docs.cloud.google.com/migrate/kf/docs/2.7)
  * [ Guides ](https://docs.cloud.google.com/migrate/kf/docs/2.7/getting-started)



Send feedback 

#  Deploy Spring Cloud Config Stay organized with collections  Save and categorize content based on your preferences. 

This document shows how to deploy Spring Cloud Config in a Kf cluster.

[Spring Cloud Config](https://cloud.spring.io/spring-cloud-config/reference/html/) provides a way to decouple application code from its runtime configuration. The Spring Cloud Config configuration server can read configuration files from Git repositories, the local filesystem, [HashiCorp Vault servers](https://www.vaultproject.io/), or [Cloud Foundry CredHub](https://docs.cloudfoundry.org/credhub/). Once the configuration server has read the configuration, it can format and serve that configuration as YAML, [Java Properties](https://docs.oracle.com/cd/E23095_01/Platform.93/ATGProgGuide/html/s0204propertiesfileformat01.html), or JSON over HTTP.

## Before you begin

You will need a cluster with Kf installed and access to the Kf CLI.

Additionally, you will need the following software:

  * **`git`** : Git is required to clone a repository.



## Download the Spring Cloud Config configuration server

To download the configuration server source:

  1. Open a terminal.
  2. Clone the source for the configuration server:
         
         git clone --depth 1 "https://github.com/google/kf"




## Configure and deploy a configuration server

To update the settings for the instance:

  1. Change directory to `spring-cloud-config-server`:
         
         cd kf/spring-cloud-config-server

  2. Open `manifest.yaml`.

  3. Change the `GIT_URI` environment variable to the URI of your Git configuration server.

  4. Optionally, change the name of the application in the manifest.

  5. Optionally, [configure additional properties or alternative property sources](https://cloud.spring.io/spring-cloud-config/reference/html/#_environment_repository) by editing `src/main/resources/application.properties`.

  6. Deploy the configuration server without an external route. If you changed the name of the application in the manifest, update it here:
         
         kf push --no-route spring-cloud-config


**Note:** The default configuration is not production ready. The `README.md` file contains additional steps to take if you want to deploy the application to production.

## Bind applications to the configuration server

You can create a [user provided service](https://docs.cloud.google.com/migrate/kf/docs/2.7/concepts/user-provided-services) to bind the deployed configuration server to other Kf applications in the same cluster or namespace.

How you configure them will depend on the library you use:

### PCF applications

Existing PCF applications that use [Pivotal's Spring Cloud Services client library](https://github.com/pivotal-cf/spring-cloud-services-starters) can be bound using the following method:

  1. Create a user provided service named config-server. This step only has to be done once per configuration server:
         
         kf cups config-server -p '{"uri":"http://spring-cloud-config"}' -t configuration

**Note:** If you want to use a configuration server in a different space, change the URI [to include the space](https://docs.cloud.google.com/migrate/kf/docs/2.7/concepts/service-discovery#how_to_use_service_discovery_with).
  2. For each application that needs get credentials, run:
         
         kf bind-service application-name config-server
         kf restart application-name

This will create an entry into the `VCAP_SERVICES` environment variable for the configuration server.




### Other applications

Applications that can connect directly to a Spring Cloud Config configuration server should be configured to access it using its cluster internal URI:
    
    
    http://spring-cloud-config
    

**Note:** If you want to use a configuration server in a different space, change the URI [to include the space name](https://docs.cloud.google.com/migrate/kf/docs/2.7/concepts/service-discovery#how_to_use_service_discovery_with).

  * For Spring applications that use the [Spring Cloud Config client library](https://cloud.spring.io/spring-cloud-config/multi/multi__spring_cloud_config_client.html) can set the `spring.cloud.config.uri` property in the appropriate location for your application. This is usually an `application.properties` or `application.yaml` file.
  * For other frameworks, see your library's reference information.



## Delete the configuration server

To remove a configuration server:

  1. Remove all bindings to the configuration server running the following commands for each bound application:
         
         kf unbind-service application-name config-server
         kf restart application-name

  2. Remove the service entry for the configuration server:
         
         kf delete-service config-server

  3. Delete the configuration server application:
         
         kf delete spring-cloud-config




## What's next

  * Read more about the [types of configuration sources](https://cloud.spring.io/spring-cloud-config/reference/html/#_environment_repository) Spring Cloud Config supports.
  * Learn about [the structure of the `VCAP_SERVICES` environment variable](https://docs.cloud.google.com/migrate/kf/docs/2.7/how-to/app-runtime#vcapservices) to understand how it can be used for service discovery.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
