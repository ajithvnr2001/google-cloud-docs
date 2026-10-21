---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.tools.compilation.DatastoreCallbacksProcessor
title: Class DatastoreCallbacksProcessor (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:05:41.149991+00:00
---

# Class DatastoreCallbacksProcessor (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.tools.compilation.DatastoreCallbacksProcessor

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Class DatastoreCallbacksProcessor (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public class DatastoreCallbacksProcessor extends AbstractProcessor

Processes datastore callback annotations ( [PrePut](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PrePut), [PostPut](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PostPut), [PreDelete](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PreDelete), [PostDelete](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PostDelete), [PreGet](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PreGet), [com.google.appengine.api.datastore.PostLoad](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PostLoad), [PreQuery](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PreQuery)) and generates a config file that the Datastore API can load at runtime. Each line of the config file is of the format:   
kind.callback_type=comma-separated list of methods  
where 'kind' is the kind of the entity to which the config on that line applies, 'callback_type' is one of PrePut, PostPut, PreDelete, PostDelete, and each entry in the comma-separated list of methods is a colon-delimited fully-qualified classname:method name tuple. So for example, if the dev wants a method named 'prePutCallback1' belonging to class 'com.example.MyCallbacks and a method named 'prePutCallback2' belonging to the same class to be invoked before any entity of kind 'yar' is put, the config file will look like this: 

> yar.PrePut=com.example.MyCallbacks:prePutCallback1,com.example.MyCallbacks:prePutCallback2

Note that it is possible to have a line which refers to all kinds by omitting the kind name: 

> .PreDelete=com.example.MyCallbacks:preDeleteCallback1

Each type of callback has its own signature requirements for the methods it annotates. If any of these signature requirements are violated the processor will produce an error. See the javadoc for the annotations for more information about the callback-specific signature requirements.

Processor Options:

  * debug - turns on debug statements



## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractProcessor](https://docs.oracle.com/javase/8/docs/api/javax/annotation/processing/AbstractProcessor.html) > DatastoreCallbacksProcessor

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

[AbstractProcessor.getCompletions(Element,AnnotationMirror,ExecutableElement,String)](https://docs.oracle.com/javase/8/docs/api/javax/annotation/processing/AbstractProcessor.html#getCompletions-javax.lang.model.element.Element-javax.lang.model.element.AnnotationMirror-javax.lang.model.element.ExecutableElement-java.lang.String-)

[AbstractProcessor.getSupportedAnnotationTypes()](https://docs.oracle.com/javase/8/docs/api/javax/annotation/processing/AbstractProcessor.html#getSupportedAnnotationTypes--)

[AbstractProcessor.getSupportedOptions()](https://docs.oracle.com/javase/8/docs/api/javax/annotation/processing/AbstractProcessor.html#getSupportedOptions--)

[AbstractProcessor.getSupportedSourceVersion()](https://docs.oracle.com/javase/8/docs/api/javax/annotation/processing/AbstractProcessor.html#getSupportedSourceVersion--)

[AbstractProcessor.init(ProcessingEnvironment)](https://docs.oracle.com/javase/8/docs/api/javax/annotation/processing/AbstractProcessor.html#init-javax.annotation.processing.ProcessingEnvironment-)

[AbstractProcessor.isInitialized()](https://docs.oracle.com/javase/8/docs/api/javax/annotation/processing/AbstractProcessor.html#isInitialized--)

[AbstractProcessor.process(Set<? extends TypeElement>,RoundEnvironment)](https://docs.oracle.com/javase/8/docs/api/javax/annotation/processing/AbstractProcessor.html#process-java.util.Set<?%20extends%20javax.lang.model.element.TypeElement>-javax.annotation.processing.RoundEnvironment-)

## Constructors 

### DatastoreCallbacksProcessor()
    
    
    public DatastoreCallbacksProcessor()

## Methods 

### getSupportedSourceVersion()
    
    
    public SourceVersion getSupportedSourceVersion()

**Returns**  
---  
**Type** | **Description**  
`[SourceVersion](https://docs.oracle.com/javase/8/docs/api/javax/lang/model/SourceVersion.html)` |   
**Overrides**

[AbstractProcessor.getSupportedSourceVersion()](https://docs.oracle.com/javase/8/docs/api/javax/annotation/processing/AbstractProcessor.html#getSupportedSourceVersion--)

### process(Set<? extends TypeElement> annotations, RoundEnvironment roundEnv)
    
    
    public boolean process(Set<? extends TypeElement> annotations, RoundEnvironment roundEnv)

**Parameters**  
---  
**Name** | **Description**  
`annotations` | `[Set](https://docs.oracle.com/javase/8/docs/api/java/util/Set.html)<? extends javax.lang.model.element.TypeElement>`  
  
`roundEnv` | `[RoundEnvironment](https://docs.oracle.com/javase/8/docs/api/javax/annotation/processing/RoundEnvironment.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[AbstractProcessor.process(Set<? extends TypeElement>,RoundEnvironment)](https://docs.oracle.com/javase/8/docs/api/javax/annotation/processing/AbstractProcessor.html#process-java.util.Set<?%20extends%20javax.lang.model.element.TypeElement>-javax.annotation.processing.RoundEnvironment-)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
