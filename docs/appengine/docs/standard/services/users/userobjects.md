---
url: https://docs.cloud.google.com/appengine/docs/standard/services/users/userobjects/
title: User objects \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:47:58.056978+00:00
---

# User objects  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/services/users/userobjects/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  User objects Stay organized with collections  Save and categorize content based on your preferences. 

Go Java PHP Python

An instance of the [`User`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/db/UserProperty/data_type) class represents a user. User instances are unique and comparable. If two instances are equal, then they represent the same user.

The application can access the User instance for the current user by calling the [`users.get_current_user()`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/users/GetCurrentUser) function.
    
    
    user = users.get_current_user()
    

You can use the [`users.get_current_user()`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/users/GetCurrentUser) function no matter which authentication option your app uses.

A User instance can be also constructed from an email address:
    
    
    user = users.User("Albert.Johnson@example.com")

Or, if you have a `federated_identity`, you can use it to create a User instance:
    
    
    user = users.User(federated_identity="http://example.com/id/ajohnson")

If the User constructor is called with an email address that does not correspond with a valid Google account, the object will be created but it will not correspond with a real Google account. This will be the case even if someone creates a Google account with the given email address after the object is stored. A User value with an email address that does not represent a Google account at the time it is created will never match a User value that represents a real user.

When running under the development web server, all User objects are assumed to represent valid Google accounts when stored in the (simulated) datastore.

The User object for a valid user can provide a unique ID value for the user that stays the same even if the user changes her email address. The [`user_id()`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/db/UserProperty/data_type#user_id) method returns this ID, a `str` value.

The User object has the same form no matter which method of authentication your app uses.

## Using user values with Datastore

The user ID is stable; you can use it in a key name or as a string property. Therefore, when using user values, you want to store the user ID (and perhaps the last-seen mail address to communicate with the user by mail). The example below shows how to compare the current user to a user ID:
    
    
    class ModelWithUser(ndb.Model):
        user_id = ndb.StringProperty()
        color = ndb.StringProperty()
    
        @classmethod
        def get_by_user(cls, user):
            return cls.query().filter(cls.user_id == user.user_id()).get()

We strongly recommend that you do not store a `UserProperty`, because it includes the email address along with the user's unique ID. If a user changes their email address and you compare their old, stored `User` to the new `User` value, they won't match. Instead, consider using the `User` _user ID value_ as the user's stable unique identifier.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
