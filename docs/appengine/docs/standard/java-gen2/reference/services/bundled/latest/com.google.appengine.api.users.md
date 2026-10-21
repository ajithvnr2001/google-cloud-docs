---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.users
title: Package com.google.appengine.api.users (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T23:25:26.362970+00:00
---

# Package com.google.appengine.api.users (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.users

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Package com.google.appengine.api.users (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 

Provides facilities to check if a user has authenticated, retrieve their email address, and check if they are an administrator for this application. It can also be used to construct a URL for users to login or logout.

As an example, your application might, in a JSP file, have code like this:
    
    
     <%
       UserService userService = UserServiceFactory.getUserService();
       if (!userService.isUserLoggedIn()) {
     %>
        Please {@code [">log in](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/<%=userService.createLoginURL\()>}
     <% } else { %>
        Welcome, <%= userService.getCurrentUser().getNickname(); %>!
          {@code (["](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/<%=userservice.createlogouturl\()>log out>)}
     <%
       }
     %>>

See Also: [com.google.appengine.api.users.UserService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.users.UserService), [The Users Java API in the _Google App Engine Developer's Guide_](http://cloud.google.com/appengine/docs/java/users/).

## Classes 

### [IUserServiceFactoryProvider](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.users.IUserServiceFactoryProvider)

Creates `IUserServiceFactory` implementations.

**Note:** This class is not intended for end users.

### [User](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.users.User)

`User` represents a specific user, represented by the combination of an email address and a specific Google Apps domain (which we call an `authDomain`). For normal Google login, `authDomain` will be set to "gmail.com".

### [UserServiceFactory](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.users.UserServiceFactory)

Creates a UserService.

## Interfaces 

### [IUserServiceFactory](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.users.IUserServiceFactory)

This interface should be implemented by providers of the [UserService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.users.UserService) and registered with [com.google.appengine.spi.ServiceFactoryFactory](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.spi.ServiceFactoryFactory).

### [UserService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.users.UserService)

The UserService provides information useful for forcing a user to log in or out, and retrieving information about the user who is currently logged-in.

## Exceptions 

### [UserServiceFailureException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.users.UserServiceFailureException)

`UserServiceFailureException` is thrown when any unknown error occurs while communicating with the user service.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
