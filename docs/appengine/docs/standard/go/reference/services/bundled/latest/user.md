---
url: https://docs.cloud.google.com/appengine/docs/standard/go/reference/services/bundled/latest/user/
title: Package google.golang.org/appengine/v2/user (v2.0.6) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:06:53.177577+00:00
---

# Package google.golang.org/appengine/v2/user (v2.0.6)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/go/reference/services/bundled/latest/user/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Package google.golang.org/appengine/v2/user (v2.0.6) Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** To get more information about this package, such as access to older versions, view [this package on pkg.go.dev](https://pkg.go.dev/google.golang.org/appengine/v2/user). 

Package user provides a client for App Engine's user authentication service.

## Functions 

### func IsAdmin 
    
    
    func IsAdmin(c [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context)) [bool](https://pkg.go.dev/builtin#bool)

IsAdmin returns true if the current user is signed in and is currently registered as an administrator of the application.

### func LoginURL 
    
    
    func LoginURL(c [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), dest [string](https://pkg.go.dev/builtin#string)) ([string](https://pkg.go.dev/builtin#string), [error](https://pkg.go.dev/builtin#error))

LoginURL returns a URL that, when visited, prompts the user to sign in, then redirects the user to the URL specified by dest.

### func LoginURLFederated 
    
    
    func LoginURLFederated(c [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), dest, identity [string](https://pkg.go.dev/builtin#string)) ([string](https://pkg.go.dev/builtin#string), [error](https://pkg.go.dev/builtin#error))

LoginURLFederated is like LoginURL but accepts a user's OpenID identifier.

### func LogoutURL 
    
    
    func LogoutURL(c [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), dest [string](https://pkg.go.dev/builtin#string)) ([string](https://pkg.go.dev/builtin#string), [error](https://pkg.go.dev/builtin#error))

LogoutURL returns a URL that, when visited, signs the user out, then redirects the user to the URL specified by dest.

### func OAuthConsumerKey 
    
    
    func OAuthConsumerKey(c [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context)) ([string](https://pkg.go.dev/builtin#string), [error](https://pkg.go.dev/builtin#error))

OAuthConsumerKey returns the OAuth consumer key provided with the current request. This method will return an error if the OAuth request was invalid.

## User
    
    
    type User struct {
    	Email      [string](https://pkg.go.dev/builtin#string)
    	AuthDomain [string](https://pkg.go.dev/builtin#string)
    	Admin      [bool](https://pkg.go.dev/builtin#bool)
    
    	// ID is the unique permanent ID of the user.
    	// It is populated if the Email is associated
    	// with a Google account, or empty otherwise.
    	ID [string](https://pkg.go.dev/builtin#string)
    
    	// ClientID is the ID of the pre-registered client so its identity can be verified.
    	// See https://developers.google.com/console/help/#generatingoauth2 for more information.
    	ClientID [string](https://pkg.go.dev/builtin#string)
    
    	FederatedIdentity [string](https://pkg.go.dev/builtin#string)
    	FederatedProvider [string](https://pkg.go.dev/builtin#string)
    }

User represents a user of the application.

### func Current 
    
    
    func Current(c [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context)) *User

Current returns the currently logged-in user, or nil if the user is not signed in.

### func CurrentOAuth 
    
    
    func CurrentOAuth(c [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), scopes [string](https://pkg.go.dev/builtin#string)) (*User, [error](https://pkg.go.dev/builtin#error))

CurrentOAuth returns the user associated with the OAuth consumer making this request. If the OAuth consumer did not make a valid OAuth request, or the scopes is non-empty and the current user does not have at least one of the scopes, this method will return an error.

### func (*User) String 
    
    
    func (u *User) String() [string](https://pkg.go.dev/builtin#string)

String returns a displayable name for the user.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-10-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-30 UTC."],[],[]] 
