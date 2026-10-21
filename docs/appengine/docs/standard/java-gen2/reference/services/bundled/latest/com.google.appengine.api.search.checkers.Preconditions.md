---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.checkers.Preconditions
title: Class Preconditions (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:52:57.906779+00:00
---

# Class Preconditions (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.checkers.Preconditions

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Class Preconditions (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public final class Preconditions

Simple static methods to be called at the start of your own methods to verify correct arguments and state. This allows constructs such as
    
    
     if (count <= 0)="" {="" throw="" new="" illegalargumentexception("must="" be="" positive:="" "="" +="" count);="" }="">

to be replaced with the more compact
    
    
         checkArgument(count > 0, "must be positive: %s", count);

Note that the sense of the expression is inverted; with `Preconditions` you declare what you expect to be _true_ , just as you do with an [`assert`](http://java.sun.com/j2se/1.5.0/docs/guide/language/assert.html) or a JUnit `assertTrue` call.

**Note:** This class is a copy of a very old version of Guava's Preconditions. Please use the current Guava version instead. See Also: "<https://google.github.io/guava/releases/21.0/api/docs/com/google/common/base/Preconditions.html>"

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > Preconditions

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

## Static Methods 

### <T>checkNotNull(T reference, @Nullable Object errorMessage)
    
    
    public static T <T>checkNotNull(T reference, @Nullable Object errorMessage)

Ensures that an object reference passed as a parameter to the calling method is not null.

**Parameters**  
---  
**Name** | **Description**  
`reference` | `T`  
an object reference  
`errorMessage` | `[Nullable Object](https://docs.oracle.com/javase/8/docs/api/java/lang/@org/jspecify/annotations/Nullable%20Object.html)`  
the exception message to use if the check fails; will be converted to a string using String#valueOf(Object)  
**Returns**  
---  
**Type** | **Description**  
`T` | the non-null reference that was validated  
  
### checkArgument(boolean expression, @Nullable Object errorMessage)
    
    
    public static void checkArgument(boolean expression, @Nullable Object errorMessage)

Ensures the truth of an expression involving one or more parameters to the calling method.

**Parameters**  
---  
**Name** | **Description**  
`expression` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
a boolean expression  
`errorMessage` | `[Nullable Object](https://docs.oracle.com/javase/8/docs/api/java/lang/@org/jspecify/annotations/Nullable%20Object.html)`  
the exception message to use if the check fails; will be converted to a string using String#valueOf(Object) if not null (a null will not be converted).  
  
### checkArgument(boolean expression, @Nullable String errorMessageTemplate, @Nullable Object[] errorMessageArgs)
    
    
    public static void checkArgument(boolean expression, @Nullable String errorMessageTemplate, @Nullable Object[] errorMessageArgs)

Ensures the truth of an expression involving one or more parameters to the calling method.

**Parameters**  
---  
**Name** | **Description**  
`expression` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
a boolean expression  
`errorMessageTemplate` | `[Nullable String](https://docs.oracle.com/javase/8/docs/api/java/lang/@org/jspecify/annotations/Nullable%20String.html)`  
a template for the exception message should the check fail. The message is formed using String#format(String, Object...). if not null (a null will not be converted).  
`errorMessageArgs` | `[Nullable Object](https://docs.oracle.com/javase/8/docs/api/java/lang/@org/jspecify/annotations/Nullable%20Object.html)[]`  
the arguments to be substituted into the message template.  
  
### checkState(boolean expression, @Nullable String errorMessage)
    
    
    public static void checkState(boolean expression, @Nullable String errorMessage)

Ensures the truth of an expression involving the state of the calling instance.

**Parameters**  
---  
**Name** | **Description**  
`expression` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
a boolean expression  
`errorMessage` | `[Nullable String](https://docs.oracle.com/javase/8/docs/api/java/lang/@org/jspecify/annotations/Nullable%20String.html)`  
the exception message to use if the check fails; will be converted to a string using String#valueOf(Object) if not null (a null will not be converted).  
  
### checkState(boolean expression, @Nullable String errorMessageTemplate, @Nullable Object[] errorMessageArgs)
    
    
    public static void checkState(boolean expression, @Nullable String errorMessageTemplate, @Nullable Object[] errorMessageArgs)

Ensures the truth of an expression involving the state of the calling instance.

**Parameters**  
---  
**Name** | **Description**  
`expression` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
a boolean expression  
`errorMessageTemplate` | `[Nullable String](https://docs.oracle.com/javase/8/docs/api/java/lang/@org/jspecify/annotations/Nullable%20String.html)`  
a template for the exception message should the check fail. The message is formed using String#format(String, Object...). if not null (a null will not be converted).  
`errorMessageArgs` | `[Nullable Object](https://docs.oracle.com/javase/8/docs/api/java/lang/@org/jspecify/annotations/Nullable%20Object.html)[]`  
the arguments to be substituted into the message template.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
