---
url: https://docs.cloud.google.com/appengine/docs/standard/services/users/
title: Users API for legacy bundled services \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:38:14.626398+00:00
---

# Users API for legacy bundled services  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/services/users/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Users API for legacy bundled services Stay organized with collections  Save and categorize content based on your preferences. 

### Region ID

The `REGION_ID` is an abbreviated code that Google assigns based on the region you select when you create your app. The code does not correspond to a country or province, even though some region IDs may appear similar to commonly used country and province codes. For apps created after February 2020, `REGION_ID.r` is included in App Engine URLs. For existing apps created before this date, the region ID is optional in the URL.

Learn more [about region IDs](https://docs.cloud.google.com/appengine/docs/standard/python/how-requests-are-routed#region-id). 

OK

Go Java PHP Python

The Users API allows an application to:

  * Detect whether the current user has signed in.
  * Redirect the user to the appropriate sign-in page to sign in.
  * Request that your application user create a new Google account if they don't have one already.



While a user is signed in to the application, the app can access the user's email address, as well as a unique user ID. The app can also detect whether the current user is an administrator (also called "admin user"), making it easy to implement admin-only areas of the app. 

**Note:** An _admin_ user is any user that has the Viewer, Editor, Owner, or App Engine Admin [role](https://docs.cloud.google.com/appengine/docs/standard/roles). For more information on setting user roles, see [Roles that Grant Access to App Engine](https://docs.cloud.google.com/appengine/docs/standard/access-control).

## User authentication

The following example greets a user who has signed in to the app with a personalized message and a link to sign out. If the user is not signed in, the app offers a link to the sign-in page for Google Accounts.

First, import the [`google.appengine.api.users`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/users) module.
    
    
    from google.appengine.api import users
    

Then use it to get information about the user:
    
    
    user = users.get_current_user()
    if user:
        nickname = user.nickname()
        logout_url = users.create_logout_url('/')
        greeting = 'Welcome, {}! (<a href="{}">sign out</a>)'.format(
            nickname, logout_url)
    else:
        login_url = users.create_login_url('/')
        greeting = '<a href="{}">Sign in</a>'.format(login_url)

### Enforcing sign in and admin access with app.yaml

If you have pages that require the user to be signed in order to access, you can enforce this in your `app.yaml` file. If a user accesses a URL configured to require sign-in and the user is not signed in, App Engine redirects the user to the appropriate Google sign-in page, then directs the user back to your app's URL after signing in or registering successfully.

The handler configuration can also require that the user be a registered administrator for the application; that is, the user must have the Viewer, Editor, Owner, or App Engine Admin [role](https://docs.cloud.google.com/appengine/docs/standard/roles). This makes it easy to build administrator-only sections of the site, without having to implement a separate authorization mechanism. 

To learn how to configure authentication for URLs, see how to require login or administrator status in the [`app.yaml` reference](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml#handlers_login).

## Authentication options

Your app can authenticate users using one of these options:

  * A Google Account
  * An account on your Google Workspace domain



### Choosing an authentication option

After you create your app, you can choose the authentication option you want to use. By default, your app will use Google Accounts for authentication. To choose another option, such as Google Workspace domain, go to the [settings](https://console.cloud.google.com/appengine/settings) page for your project in the Google Cloud console and click **Edit**. In the _Google authentication_ dropdown menu, select the desired authentication type, and then click **Save**.

## Signing in and out

An application can detect whether a user has signed in to the app with your app's chosen authentication option. If the user is not signed in, the app can direct the user to Google Accounts to sign in or create a new Google account. The app gets the URL for the sign-in page by calling a method of the Users API. The app can display this URL as a link, or it can issue an HTTP redirect to the URL when the user visits a page that requires authentication.

If your app uses Google Accounts or Google Workspace for authentication, the name of your application appears on the sign-in page when the user signs in to your application. The name shown is the application name that you specified when registering the application. You can change this name in the **Application name** field of the Google Cloud console [Credentials](https://console.cloud.google.com/apis/credentials/consent) page.

Once the user has signed in or created a Google account, the user is redirected back to your application. The app provides the redirect URL to the method that generates the sign-in URL.

The Users API includes a method to generate a URL for signing out of the app. The sign-out URL de-authenticates the user from the app, then redirects back to the app's URL without displaying anything.

A user is not signed in to an application until they are prompted to do so by the app and enter their account's email address and password. This is true even if the user has signed in to other applications using their Google Account.

## Accessing account information

While a user is signed in to an app, the app can access the account's email address for every request the user makes to the app. The app can also access a user ID that identifies the user uniquely, even if the user changes the email address for their account.

The app can also determine whether the current user is an administrator for the app. An _admin_ user is any user that has the Viewer, Editor, Owner, or App Engine Admin [role](https://docs.cloud.google.com/appengine/docs/standard/roles). You can use this feature to build administrative features for the app, even if you don't authenticate other users. The Go, Java, PHP and Python APIs make it easy to configure URLs as "administrator only".

**Note:** Every user has the same user ID for all App Engine applications. If your app uses the user ID in public data, such as by including it in a URL parameter, you should use a hash algorithm with a "salt" value added to obscure the ID. Exposing raw IDs could allow someone to associate a user's activity in one app with that in another, or get the user's email address by coercing the user to sign in to another app.

## Users and the Datastore

The Users service API can return the current user's information as a User object. Although User objects can be stored as a property value in the datastore, we strongly recommend that you avoid doing so because this includes the email address along with the user's unique ID. If a user changes their email address and you compare their old, stored `User` to the new `User` value, they won't match. Instead, consider using the `User` _user ID value_ as the user's stable unique identifier.

## Google accounts and the development server

The development server simulates the Google Accounts system using a fake sign-in screen. When your application calls the Users API to get the URL for the sign-in screen, the API returns a special development server URL that prompts for an email address, but no password. You can type any email address into this prompt, and the app will behave as if you are signed in with an account with that address.

The fake sign-in screen also includes a checkbox that indicates whether the fake account is an administrator; that is, whether the account has the Viewer, Editor, Owner, or App Engine Admin [role](https://docs.cloud.google.com/appengine/docs/standard/roles). If you check this box, the app will behave as if you are signed in using an administrator account.

Similarly, the Users API returns a sign-out URL that cancels the fake sign-in.

The unique ID for a User object in the development server is calculated from the email address. Two unique email addresses always represent two unique users in the development server.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
