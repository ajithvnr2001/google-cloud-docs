---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.users.User
title: Class User (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:51:11.502248+00:00
---

# Class User (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.users.User

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Class User (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public final class User implements Serializable, Comparable<User>

`User` represents a specific user, represented by the combination of an email address and a specific Google Apps domain (which we call an `authDomain`). For normal Google login, `authDomain` will be set to "gmail.com".

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > User

## Implements

[Serializable](https://docs.oracle.com/javase/8/docs/api/java/io/Serializable.html), [Comparable<User>](https://docs.oracle.com/javase/8/docs/api/java/lang/Comparable<com/google/appengine/api/users/User>.html)

## Inherited Members

[Object.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#clone--)

[Object.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-)

[Object.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#finalize--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#hashCode--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.toString()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#toString--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

## Constructors 

### User(String email, @Nullable String authDomain, @Nullable String userId, String federatedIdentity)
    
    
    public User(String email, @Nullable String authDomain, @Nullable String userId, String federatedIdentity)

Creates a new User with a federated identity.

**Parameters**  
---  
**Name** | **Description**  
`email` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
an optional field holding the user's email.  
`authDomain` | `[Nullable String](https://docs.oracle.com/javase/8/docs/api/java/lang/@org/jspecify/annotations/Nullable%20String.html)`  
the URL of the identity provider. Could be null.  
`userId` | `[Nullable String](https://docs.oracle.com/javase/8/docs/api/java/lang/@org/jspecify/annotations/Nullable%20String.html)`  
a unique id for this user. Could be null.  
`federatedIdentity` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
a not `null` asserted federated identity.  
  
### User(String email, String authDomain)
    
    
    public User(String email, String authDomain)

Creates a new User.

**Parameters**  
---  
**Name** | **Description**  
`email` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
a not `null` email address.  
`authDomain` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
a not `null` domain name into which this user has authenticated, or "gmail.com" for normal Google authentication.  
  
### User(String email, String authDomain, @Nullable String userId)
    
    
    public User(String email, String authDomain, @Nullable String userId)

Creates a new User.

**Parameters**  
---  
**Name** | **Description**  
`email` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
a not `null` email address.  
`authDomain` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
a not `null` domain name into which this user has authenticated, or "gmail.com" for normal Google authentication.  
`userId` | `[Nullable String](https://docs.oracle.com/javase/8/docs/api/java/lang/@org/jspecify/annotations/Nullable%20String.html)`  
a possibly-null string uniquely identifying the specified user.  
  
## Methods 

### compareTo(User user)
    
    
    public int compareTo(User user)

**Parameter**  
---  
**Name** | **Description**  
`user` | `[User](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.users.User)`  
  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### equals(@Nullable Object object)
    
    
    public boolean equals(@Nullable Object object)

**Parameter**  
---  
**Name** | **Description**  
`object` | `[Nullable Object](https://docs.oracle.com/javase/8/docs/api/java/lang/@org/jspecify/annotations/Nullable%20Object.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[Object.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-)

### getAuthDomain()
    
    
    public String getAuthDomain()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getEmail()
    
    
    public String getEmail()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getFederatedIdentity()
    
    
    public String getFederatedIdentity()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getNickname()
    
    
    public String getNickname()

Return this user's nickname.

The nickname will be a unique, human readable identifier for this user with respect to this application. It will be an email address for some users, but not all.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getUserId()
    
    
    public @Nullable String getUserId()

Returns an opaque string that uniquely identifies the user represented by this `User` object.

May be null if this `User` object was created explicitly and no user ID was supplied.

**Returns**  
---  
**Type** | **Description**  
`[Nullable String](https://docs.oracle.com/javase/8/docs/api/java/lang/@org/jspecify/annotations/Nullable%20String.html)` |   
  
### hashCode()
    
    
    public int hashCode()

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[Object.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#hashCode--)

### toString()
    
    
    public String toString()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
**Overrides**

[Object.toString()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#toString--)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
