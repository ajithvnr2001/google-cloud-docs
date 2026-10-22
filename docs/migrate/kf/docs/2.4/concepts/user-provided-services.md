---
url: https://docs.cloud.google.com/migrate/kf/docs/2.4/concepts/user-provided-services/
title: User-Provided Services \u00a0|\u00a0 Kf 2.4 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:12:37.920865+00:00
---

# User-Provided Services  |  Kf 2.4  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/kf/docs/2.4/concepts/user-provided-services/

Version 2.4

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
  * [ 2.4 ](https://docs.cloud.google.com/migrate/kf/docs/2.4)
  * [ Guides ](https://docs.cloud.google.com/migrate/kf/docs/2.4/getting-started)



Send feedback 

#  User-Provided Services Stay organized with collections  Save and categorize content based on your preferences. 

Users can leverage services that aren't available in the marketplace by creating user-provided service instances. Once created, user-provided service instances behave like service instances created through the [marketplace](https://docs.cloud.google.com/migrate/kf/docs/2.4/cli/kf-marketplace). Creating, listing, updating, deleting, binding, and unbinding user-provided services are all supported in Kf.

# Create a user-provided service instance

The alias for `kf create-user-provided-service` is `kf cups`.

The name given to a user-provided service must be unique across all service instances in a Space, including services created through a service broker.

## Deliver service credentials to an App

A user-provided service instance can be used to deliver credentials to an App. For example, a database admin can have a set of credentials for an existing database managed outside of Kf, and these credentials include the URL, port, username, and password used to connect to the database.

The admin can create a user-provided service with the credentials and the developer can bind the service instance to the App. This allows the credentials to be shared without ever leaving the platform. Binding a service instance to an App has the same effect regardless of whether the service is a user-provided service or a marketplace service.

The App is configured with the credentials provided by the user, and the App runtime environment variable [`VCAP_SERVICES`](https://docs.cloud.google.com/migrate/kf/docs/2.4/how-to/app-runtime##vcapservices) is populated with information about all of the bound services to that App.

A user-provided service can be created with credentials and/or a list of tags.
    
    
    kf cups my-db -p '{"username":"admin", "password":"test123", "some-int-val": 1, "some-bool": true}' -t "comma, separated, tags"

This will create the user-provided service instance `my-db` with the provided credentials and tags. The credentials passed in to the `-p` flag must be valid JSON (either inline or loaded from a file path).

To deliver the credentials to one or more Apps, the user can run `kf bind-service`.

Suppose we have an App with one bound service, the user-provided service `my-db` defined above. The `VCAP_SERVICES` environment variable for that App will have the following contents:
    
    
    {
      "user-provided": [
        {
          "name": "my-db",
          "instance_name": "my-db",
          "label": "user-provided",
          "tags": [
            "comma",
            "separated",
            "tags"
          ],
          "credentials": {
            "username": "admin",
            "password": "test123",
            "some-int-val": 1,
            "some-bool": true
          }
        }
      ]
    }
    

# Update a user-provided service instance

The alias for `kf update-user-provided-service` is `kf uups`.

A user-provided service can be updated with the `uups` command. New credentials and/or tags passed in completely overwrite existing ones. For example, if the user created the user-provided service `my-db` above, called `kf bind-service` to bind the service to an App, then ran the command.
    
    
    kf uups my-db -p '{"username":"admin", "password":"new-pw", "new-key": "new-val"}'

The updated credentials will only be reflected on the App after the user unbinds and rebinds the service to the App. No restart or restage of the App is required. The updated `VCAP_SERVICES` environment variable will have the following contents:
    
    
    {
      "user-provided": [
        {
          "name": "my-db",
          "instance_name": "my-db",
          "label": "user-provided",
          "tags": [
            "comma",
            "separated",
            "tags"
          ],
          "credentials": {
            "username": "admin",
            "password": "new-pw",
            "new-key": "new-val"
          }
        }
      ]
    }
    

The new credentials overwrite the old credentials, and the tags are unchanged because they were not specified in the update command.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
