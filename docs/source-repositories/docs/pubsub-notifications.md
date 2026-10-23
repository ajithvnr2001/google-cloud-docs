---
url: https://docs.cloud.google.com/source-repositories/docs/pubsub-notifications/
title: Notifications for Cloud Source Repositories \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:31:56.248455+00:00
---

# Notifications for Cloud Source Repositories  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/source-repositories/docs/pubsub-notifications/

Effective June 17, 2024, Cloud Source Repositories isn't available to new customers. For alternative source hosting options, [Secure Source Manager](https://cloud.google.com/secure-source-manager/docs) is a regionally deployed, single tenant, managed source code repository hosted on Google Cloud.

If your organization hasn't previously used Cloud Source Repositories, you can't enable the API or use Cloud Source Repositories. New projects not connected to an organization can't enable the Cloud Source Repositories API. Organizations that have used Cloud Source Repositories prior to June 17, 2024 are not affected by this change.

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Source Repositories ](https://docs.cloud.google.com/source-repositories/docs)
  * [ Guides ](https://docs.cloud.google.com/source-repositories/docs/create-code-repository)



Send feedback 

#  Notifications for Cloud Source Repositories Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Source Repositories publishes messages about your repository to named resources called topics. Apps subscribed to Pub/Sub topics can receive these messages. For example, when your repository state changes, you can receive an alert. Additionally, you can configure roles and permissions for your Pub/Sub topics to control how users interact with the Pub/Sub events that your repository generates.

This page provides an overview of Pub/Sub notifications for Cloud Source Repositories. To learn how to set up and use Pub/Sub notifications, see [Configuring Pub/Sub notifications](https://docs.cloud.google.com/source-repositories/docs/configuring-notifications).

## Scope

You can configure Cloud Source Repositories to publish events to a Pub/Sub topic. You can set the scope of this configuration to be your entire Google Cloud project or an individual repository.

After it is configured, Cloud Source Repositories publishes messages to the specified Pub/Sub topic using your service account. You must first give the service account permissions to publish to the topic. If you have audit logging enabled for Pub/Sub, this service account is shown as the caller of the Pub/Sub APIs.

## Permissions

Configuring Cloud Source Repositories to publish messages requires the following:

  * A project or a repository that is watched for events. If a project is specified, all repositories under that project are watched.
  * A Pub/Sub topic that Cloud Source Repositories publishes messages to.
  * A service account to access the Pub/Sub topic.
  * A message format (such as JSON or Protocol Buffers).



When you configure Cloud Source Repositories for Pub/Sub, you must have these permissions:

  * `source.repos.updateRepo` on the specified repository or `source.repos.updateProjectConfig` on the specified project
  * `iam.serviceAccounts.actAs` on the specified service account



After the Pub/Sub topic is registered, the specified service account must have `pubsub.topics.publish` permission to publish a message.

## Event types

Pub/Sub can notify you when a user creates a repository, deletes a repository, or pushes a commit to a repository. Each event is a specific event type. The following table lists the types and their corresponding definitions.

Event type | Description  
---|---  
CreateRepo | Occurs when a user creates a repository.  
RefUpdate | Occurs when a user executes a git push command.  
DeleteRepo | Occurs when a user deletes a repository.  
  
## Notification format

You can configure Pub/Sub to use one of two formats for notifications:

  * JSON
  * Protocol Buffers



## Notification data

Each Pub/Sub notification contains the following information about an event:

Field name | Description  
---|---  
name | Name of the repository.  
url | The URL of the repository.  
eventTime | The time at which the change occurred.  
refUpdateEvent | Information about the specific change.  
createRepoEvent | Indicates if a user created a repository.  
deleteRepoEvent | Indicates if a user deleted a repository.  
  
If the notification is for a `git push` command, the notification containing the `refUpdateEvent` field contains the following information:

Field name | Description  
---|---  
email | The email address of the user who made the change.  
refUpdates | Information about the commit.  
**Note:** If mirroring repositories to Cloud Source Repositories, the email address in Pub/Sub notifications always appears as `gerritcodereview@google.com`.

The `refUpdates` field contains the following details about the `git push` command:

Field name | Description  
---|---  
refName | The name of the branch.  
updateType | The type of update. For more information, see Update types.  
oldId | The previous commit ID for the repository.  
newId | The new ID for the repository.  
  
## Update types

A `git push` event can have one of four update types. You can find the type in the `updateType` field of the notification.

Update type | Description  
---|---  
CREATE | Occurs when the command creates a new reference.  
UPDATE_FAST_FORWARD | Occurs when the command updates an object.  
UPDATE_NON_FAST_FORWARD | Occurs when the command uses the `-f` flag, such as `git push -f`.  
DELETE | Occurs when the command deletes a reference.  
  
## Notification example

The following is an example of the data contained in a Pub/Sub notification. This notification uses the JSON format.
    
    
      {
        "name": "projects/test-project/repos/pubsub-test",
        "url": "[URL_PATH]",
        "eventTime": "2018-02-21T21:23:25.566175Z",
        "refUpdateEvent": {
          "email": "someone@somecompany.com",
          "refUpdates": {
            "refs/heads/master": {
              "refName": "refs/heads/master",
              "updateType": "UPDATE_FAST_FORWARD",
              "oldId": "c7a28dd5de3403cc384a025834c9fce2886fe763",
              "newId": "f00768887da8de62061210295914a0a8a2a38226"
            }
          }
        }
      }
    

## Cross-project setup example

You can configure Cloud Source Repositories to publish a message to a topic in a different project. In this case, you must create a service account in the same project where your repository resides. In the project that contains the Pub/Sub topic, give the role `roles/pubsub.publisher` to this service account. When you configure Cloud Source Repositories with this account and this Pub/Sub topic, the event messages for your repository appear in the topic in the other project.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
