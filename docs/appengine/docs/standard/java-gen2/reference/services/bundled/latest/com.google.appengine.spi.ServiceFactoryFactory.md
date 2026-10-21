---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.spi.ServiceFactoryFactory
title: Class ServiceFactoryFactory (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:38:15.865422+00:00
---

# Class ServiceFactoryFactory (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.spi.ServiceFactoryFactory

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Class ServiceFactoryFactory (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public final class ServiceFactoryFactory

**This class is not intended for end users.**

Provide factory instances for AppEngine APIs. Each API will have an associated [FactoryProvider](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.spi.FactoryProvider) registered with this class. N.B. _Once <xref uid="com.google.appengine.spi.ServiceFactoryFactory._

To construct the runtime mapping, this class first uses `java.util.ServiceLoader` to find all registered [FactoryProvider](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.spi.FactoryProvider) entities using the `ClassLoader` of `ServiceFactoryFactory`. Finally, the explicitly registered providers <xref uid="com.google.appengine.spi.ServiceFactoryFactory._register(com.google.appengine.spi.FactoryProvider <I>)" data-throw-if-not-resolved="false">#register(FactoryProvider) are merged in._

__

__

_If`ServiceLoader` locates multiple providers for a given factory interface, the ambiguity can be resolved by using the [ServiceProvider#precedence](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.spi.ServiceProvider#com_google_appengine_spi_ServiceProvider_precedence_) annotation property (higher precedence wins; _the google implementations all have precedence Integer.MIN_VALUE_). An exception is raised if the ambiguity cannot be resolved. Note that explicit registration (<xref uid="com.google.appengine.spi.ServiceFactoryFactory._register(com.google.appengine.spi.FactoryProvider <I>)" data-throw-if-not-resolved="false">#register(FactoryProvider)) always takes precedence (it does not honor the [ServiceProvider#precedence](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.spi.ServiceProvider#com_google_appengine_spi_ServiceProvider_precedence_) annotation property).__

____

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > ServiceFactoryFactory

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

## Static Fields 

### USE_THREAD_CONTEXT_CLASSLOADER_PROPERTY
    
    
    public static final String USE_THREAD_CONTEXT_CLASSLOADER_PROPERTY

If this system property is set to "true" the thread context classloader is used (if non-null) when looking up API service implementations. Otherwise the class loader of this class is used.

**Field Value**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
## Static Methods 

### <I>register(FactoryProvider<I> p)
    
    
    public static synchronized void <I>register(FactoryProvider<I> p)

Explicitly register a provider. This does not take the precedence (see FactoryProvider#getPrecedence()) of the provider into consideration; subsequent registrations will always override previous ones.

**Parameter**  
---  
**Name** | **Description**  
`p` | `[FactoryProvider](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.spi.FactoryProvider)<I>`  
The provider to register  
  
### <T>getFactory(Class<T> base)
    
    
    public static T <T>getFactory(Class<T> base)

Used by AppEngine service factories. Returns an instance of the factory implementing the interface provide by `base`. Since there must always be a provider registered for a given base, an error will be raised if no appropriate registration is found.

**Parameter**  
---  
**Name** | **Description**  
`base` | `[Class](https://docs.oracle.com/javase/8/docs/api/java/lang/Class.html)<T>`  
The returned factory must extend this class.  
**Returns**  
---  
**Type** | **Description**  
`T` |   
  
## Constructors 

### ServiceFactoryFactory()
    
    
    public ServiceFactoryFactory()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
