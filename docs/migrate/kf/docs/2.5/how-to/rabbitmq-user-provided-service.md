---
url: https://docs.cloud.google.com/migrate/kf/docs/2.5/how-to/rabbitmq-user-provided-service/
title: Setting Up RabbitMQ as a User-Provided Service \u00a0|\u00a0 Kf 2.5 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:36:54.459902+00:00
---

# Setting Up RabbitMQ as a User-Provided Service  |  Kf 2.5  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/kf/docs/2.5/how-to/rabbitmq-user-provided-service/

Version 2.5

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
  * [ 2.5 ](https://docs.cloud.google.com/migrate/kf/docs/2.5)
  * [ Guides ](https://docs.cloud.google.com/migrate/kf/docs/2.5/documentation)



Send feedback 

#  Setting Up RabbitMQ as a User-Provided Service Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** You can leverage services that aren't listed in the marketplace by creating user-provided service instances that an App can bind to. Learn more about [user-provided services](https://docs.cloud.google.com/migrate/kf/docs/2.5/concepts/user-provided-services).

This document guides you through binding your App to a RabbitMQ instance not listed in the Kf marketplace (including [RabbitMQ click to deploy on Marketplace](https://console.cloud.google.com/marketplace/product/click-to-deploy-images/rabbitmq) with the Spring Cloud Foundry Connector. This results in the RabbitMQ credentials being injected into your App, just like binding to services provisioned through marketplace plans.

# Before you begin

  * Ensure you have RabbitMQ installed and accessible by your Kf cluster.
  * Ensure RabbitMQ has already been set up for your App.
  * Ensure you have targeted the Space running your App.



# Create the user-provided instance

For Kf to successfully bind an App to your RabbitMQ instance, the minimum environment variable is the URI (for example `amqp://username:password@host:port/vhost?query`). Additional key-value pairs may be included if desired. The [RabbitMQ documentation](https://www.rabbitmq.com/uri-spec.html) can help with creating a URI string. The following example should be sufficient for basic deployments.
    
    
    kf cups service-instance-name -p '{"uri":"amqp://username:password@rabbitmq-host:5672"}' -t "rabbitmq"

# Bind your App

Now that the user-provided service has been created, you can bind your App to the instance name:
    
    
    kf bind-service application-name service-instance-name

Restart your App to for the changes to take effect:
    
    
    kf restart application-name

You can confirm the new environment variables being provided to your App:
    
    
    kf vcap-services application-name

# Update the user-provided instance

If there are changes to the environment (for example password or host update in the URI, or the addition of new key-value pairs) that need to be passed on to any App bound to it, you can update the user-provided instance.
    
    
    kf uups service-instance-name -p '{"uri":"new-uri", "some-new-key": "some-new-value"}'

# Related documents

  * [VCAP_SERVICES](https://docs.cloud.google.com/migrate/kf/docs/2.5/how-to/app-runtime#vcapservices)
  * [Unbind service](https://docs.cloud.google.com/migrate/kf/docs/2.5/cli/kf-unbind-service)
  * [Delete service](https://docs.cloud.google.com/migrate/kf/docs/2.5/cli/kf-delete-service)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
