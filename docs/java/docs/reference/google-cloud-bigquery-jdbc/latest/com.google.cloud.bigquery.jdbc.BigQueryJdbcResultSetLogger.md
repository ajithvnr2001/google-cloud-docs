---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery-jdbc/latest/com.google.cloud.bigquery.jdbc.BigQueryJdbcResultSetLogger
title: Class BigQueryJdbcResultSetLogger (1.6.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:23:30.075988+00:00
---

# Class BigQueryJdbcResultSetLogger (1.6.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery-jdbc/latest/com.google.cloud.bigquery.jdbc.BigQueryJdbcResultSetLogger

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class BigQueryJdbcResultSetLogger (1.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.6.0 (latest)  1.2.0  1.1.0  1.0.0 
    
    
    public class BigQueryJdbcResultSetLogger extends BigQueryJdbcCustomLogger

Specialized high-performance logger for ResultSet and its related classes. Avoids expensive stack trace walking (caller inference) on hot-path logging calls.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [java.util.logging.Logger](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Logger.html) > [BigQueryJdbcCustomLogger](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery-jdbc/latest/com.google.cloud.bigquery.jdbc.BigQueryJdbcCustomLogger) > BigQueryJdbcResultSetLogger

## Inherited Members

[BigQueryJdbcCustomLogger.fine(String)](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery-jdbc/latest/com.google.cloud.bigquery.jdbc.BigQueryJdbcCustomLogger#com_google_cloud_bigquery_jdbc_BigQueryJdbcCustomLogger_fine_java_lang_String_)

[BigQueryJdbcCustomLogger.fine(Supplier<String>)](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery-jdbc/latest/com.google.cloud.bigquery.jdbc.BigQueryJdbcCustomLogger#com_google_cloud_bigquery_jdbc_BigQueryJdbcCustomLogger_fine_java_util_function_Supplier_java_lang_String__)

[BigQueryJdbcCustomLogger.finer(String)](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery-jdbc/latest/com.google.cloud.bigquery.jdbc.BigQueryJdbcCustomLogger#com_google_cloud_bigquery_jdbc_BigQueryJdbcCustomLogger_finer_java_lang_String_)

[BigQueryJdbcCustomLogger.finest(String)](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery-jdbc/latest/com.google.cloud.bigquery.jdbc.BigQueryJdbcCustomLogger#com_google_cloud_bigquery_jdbc_BigQueryJdbcCustomLogger_finest_java_lang_String_)

[BigQueryJdbcCustomLogger.finest(Supplier<String>)](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery-jdbc/latest/com.google.cloud.bigquery.jdbc.BigQueryJdbcCustomLogger#com_google_cloud_bigquery_jdbc_BigQueryJdbcCustomLogger_finest_java_util_function_Supplier_java_lang_String__)

[BigQueryJdbcCustomLogger.severe(String,Throwable)](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery-jdbc/latest/com.google.cloud.bigquery.jdbc.BigQueryJdbcCustomLogger#com_google_cloud_bigquery_jdbc_BigQueryJdbcCustomLogger_severe_java_lang_String_java_lang_Throwable_)

[BigQueryJdbcCustomLogger.severe(String,Throwable,Object)](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery-jdbc/latest/com.google.cloud.bigquery.jdbc.BigQueryJdbcCustomLogger#com_google_cloud_bigquery_jdbc_BigQueryJdbcCustomLogger_severe_java_lang_String_java_lang_Throwable_java_lang_Object____)

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

[Logger.addHandler(Handler)](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Logger.html#addHandler-java.util.logging.Handler-)

[Logger.config(String)](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Logger.html#config-java.lang.String-)

[Logger.config(Supplier<String>)](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Logger.html#config-java.util.function.Supplier<java.lang.String>-)

[Logger.entering(String,String)](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Logger.html#entering-java.lang.String-java.lang.String-)

[Logger.entering(String,String,Object)](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Logger.html#entering-java.lang.String-java.lang.String-java.lang.Object-)

[Logger.entering(String,String,Object[])](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Logger.html#entering-java.lang.String-java.lang.String-java.lang.Object\[\]-)

[Logger.exiting(String,String)](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Logger.html#exiting-java.lang.String-java.lang.String-)

[Logger.exiting(String,String,Object)](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Logger.html#exiting-java.lang.String-java.lang.String-java.lang.Object-)

[Logger.finer(Supplier<String>)](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Logger.html#finer-java.util.function.Supplier<java.lang.String>-)

[Logger.getAnonymousLogger()](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Logger.html#getAnonymousLogger--)

[Logger.getAnonymousLogger(String)](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Logger.html#getAnonymousLogger-java.lang.String-)

[Logger.getFilter()](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Logger.html#getFilter--)

[Logger.getGlobal()](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Logger.html#getGlobal--)

[Logger.getHandlers()](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Logger.html#getHandlers--)

[Logger.getLevel()](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Logger.html#getLevel--)

[Logger.getLogger(String)](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Logger.html#getLogger-java.lang.String-)

[Logger.getLogger(String,String)](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Logger.html#getLogger-java.lang.String-java.lang.String-)

[Logger.getName()](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Logger.html#getName--)

[Logger.getParent()](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Logger.html#getParent--)

[Logger.getResourceBundle()](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Logger.html#getResourceBundle--)

[Logger.getResourceBundleName()](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Logger.html#getResourceBundleName--)

[Logger.getUseParentHandlers()](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Logger.html#getUseParentHandlers--)

[Logger.info(String)](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Logger.html#info-java.lang.String-)

[Logger.info(Supplier<String>)](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Logger.html#info-java.util.function.Supplier<java.lang.String>-)

[Logger.isLoggable(Level)](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Logger.html#isLoggable-java.util.logging.Level-)

[Logger.log(Level,String)](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Logger.html#log-java.util.logging.Level-java.lang.String-)

[Logger.log(Level,String,Object)](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Logger.html#log-java.util.logging.Level-java.lang.String-java.lang.Object-)

[Logger.log(Level,String,Object[])](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Logger.html#log-java.util.logging.Level-java.lang.String-java.lang.Object\[\]-)

[Logger.log(Level,String,Throwable)](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Logger.html#log-java.util.logging.Level-java.lang.String-java.lang.Throwable-)

[Logger.log(Level,Throwable,Supplier<String>)](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Logger.html#log-java.util.logging.Level-java.lang.Throwable-java.util.function.Supplier<java.lang.String>-)

[Logger.log(Level,Supplier<String>)](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Logger.html#log-java.util.logging.Level-java.util.function.Supplier<java.lang.String>-)

[Logger.log(LogRecord)](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Logger.html#log-java.util.logging.LogRecord-)

[Logger.logp(Level,String,String,String)](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Logger.html#logp-java.util.logging.Level-java.lang.String-java.lang.String-java.lang.String-)

[Logger.logp(Level,String,String,String,Object)](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Logger.html#logp-java.util.logging.Level-java.lang.String-java.lang.String-java.lang.String-java.lang.Object-)

[Logger.logp(Level,String,String,String,Object[])](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Logger.html#logp-java.util.logging.Level-java.lang.String-java.lang.String-java.lang.String-java.lang.Object\[\]-)

[Logger.logp(Level,String,String,String,Throwable)](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Logger.html#logp-java.util.logging.Level-java.lang.String-java.lang.String-java.lang.String-java.lang.Throwable-)

[Logger.logp(Level,String,String,Throwable,Supplier<String>)](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Logger.html#logp-java.util.logging.Level-java.lang.String-java.lang.String-java.lang.Throwable-java.util.function.Supplier<java.lang.String>-)

[Logger.logp(Level,String,String,Supplier<String>)](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Logger.html#logp-java.util.logging.Level-java.lang.String-java.lang.String-java.util.function.Supplier<java.lang.String>-)

[Logger.logrb(Level,String,String,String,String)](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Logger.html#logrb-java.util.logging.Level-java.lang.String-java.lang.String-java.lang.String-java.lang.String-)

[Logger.logrb(Level,String,String,String,String,Object)](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Logger.html#logrb-java.util.logging.Level-java.lang.String-java.lang.String-java.lang.String-java.lang.String-java.lang.Object-)

[Logger.logrb(Level,String,String,String,String,Object[])](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Logger.html#logrb-java.util.logging.Level-java.lang.String-java.lang.String-java.lang.String-java.lang.String-java.lang.Object\[\]-)

[Logger.logrb(Level,String,String,String,String,Throwable)](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Logger.html#logrb-java.util.logging.Level-java.lang.String-java.lang.String-java.lang.String-java.lang.String-java.lang.Throwable-)

[Logger.logrb(Level,String,String,ResourceBundle,String,Object)](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Logger.html#logrb-java.util.logging.Level-java.lang.String-java.lang.String-java.util.ResourceBundle-java.lang.String-java.lang.Object...-)

[Logger.logrb(Level,String,String,ResourceBundle,String,Throwable)](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Logger.html#logrb-java.util.logging.Level-java.lang.String-java.lang.String-java.util.ResourceBundle-java.lang.String-java.lang.Throwable-)

[Logger.removeHandler(Handler)](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Logger.html#removeHandler-java.util.logging.Handler-)

[Logger.setFilter(Filter)](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Logger.html#setFilter-java.util.logging.Filter-)

[Logger.setLevel(Level)](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Logger.html#setLevel-java.util.logging.Level-)

[Logger.setParent(Logger)](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Logger.html#setParent-java.util.logging.Logger-)

[Logger.setResourceBundle(ResourceBundle)](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Logger.html#setResourceBundle-java.util.ResourceBundle-)

[Logger.setUseParentHandlers(boolean)](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Logger.html#setUseParentHandlers-boolean-)

[Logger.severe(String)](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Logger.html#severe-java.lang.String-)

[Logger.severe(Supplier<String>)](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Logger.html#severe-java.util.function.Supplier<java.lang.String>-)

[Logger.throwing(String,String,Throwable)](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Logger.html#throwing-java.lang.String-java.lang.String-java.lang.Throwable-)

[Logger.warning(String)](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Logger.html#warning-java.lang.String-)

[Logger.warning(Supplier<String>)](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Logger.html#warning-java.util.function.Supplier<java.lang.String>-)

## Static Methods 

### getLogger(Class<?> clazz)
    
    
    public static BigQueryJdbcResultSetLogger getLogger(Class<?> clazz)

**Parameter**  
---  
**Name** | **Description**  
`clazz` | `[Class](https://docs.oracle.com/javase/8/docs/api/java/lang/Class.html)<?>`  
  
**Returns**  
---  
**Type** | **Description**  
`[BigQueryJdbcResultSetLogger](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery-jdbc/latest/com.google.cloud.bigquery.jdbc.BigQueryJdbcResultSetLogger)` |   
  
### getLogger(Class<?> clazz, String connectionId)
    
    
    public static BigQueryJdbcResultSetLogger getLogger(Class<?> clazz, String connectionId)

**Parameters**  
---  
**Name** | **Description**  
`clazz` | `[Class](https://docs.oracle.com/javase/8/docs/api/java/lang/Class.html)<?>`  
  
`connectionId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BigQueryJdbcResultSetLogger](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery-jdbc/latest/com.google.cloud.bigquery.jdbc.BigQueryJdbcResultSetLogger)` |   
  
## Constructors 

### BigQueryJdbcResultSetLogger(Class<?> clazz)
    
    
    public BigQueryJdbcResultSetLogger(Class<?> clazz)

**Parameter**  
---  
**Name** | **Description**  
`clazz` | `[Class](https://docs.oracle.com/javase/8/docs/api/java/lang/Class.html)<?>`  
  
  
### BigQueryJdbcResultSetLogger(Class<?> clazz, String connectionId)
    
    
    public BigQueryJdbcResultSetLogger(Class<?> clazz, String connectionId)

**Parameters**  
---  
**Name** | **Description**  
`clazz` | `[Class](https://docs.oracle.com/javase/8/docs/api/java/lang/Class.html)<?>`  
  
`connectionId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
  
## Methods 

### fine(String msg)
    
    
    public void fine(String msg)

**Parameter**  
---  
**Name** | **Description**  
`msg` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Overrides**

[BigQueryJdbcCustomLogger.fine(String msg)](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery-jdbc/latest/com.google.cloud.bigquery.jdbc.BigQueryJdbcCustomLogger#com_google_cloud_bigquery_jdbc_BigQueryJdbcCustomLogger_fine_java_lang_String_)

### fine(Supplier<String> msgSupplier)
    
    
    public void fine(Supplier<String> msgSupplier)

**Parameter**  
---  
**Name** | **Description**  
`msgSupplier` | `[Supplier](https://docs.oracle.com/javase/8/docs/api/java/util/function/Supplier.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
  
**Overrides**

[BigQueryJdbcCustomLogger.fine(Supplier<String> msgSupplier)](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery-jdbc/latest/com.google.cloud.bigquery.jdbc.BigQueryJdbcCustomLogger#com_google_cloud_bigquery_jdbc_BigQueryJdbcCustomLogger_fine_java_util_function_Supplier_java_lang_String__)

### fineTrace(String methodName, String msg)
    
    
    public void fineTrace(String methodName, String msg)

Log a message at Level.FINE with predefined class name and method name.

**Parameters**  
---  
**Name** | **Description**  
`methodName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`msg` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
  
### fineTrace(String methodName, Supplier<String> msgSupplier)
    
    
    public void fineTrace(String methodName, Supplier<String> msgSupplier)

Log a lazy message at Level.FINE with predefined class name and method name.

**Parameters**  
---  
**Name** | **Description**  
`methodName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`msgSupplier` | `[Supplier](https://docs.oracle.com/javase/8/docs/api/java/util/function/Supplier.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
  
  
### finer(String msg)
    
    
    public void finer(String msg)

**Parameter**  
---  
**Name** | **Description**  
`msg` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Overrides**

[BigQueryJdbcCustomLogger.finer(String msg)](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery-jdbc/latest/com.google.cloud.bigquery.jdbc.BigQueryJdbcCustomLogger#com_google_cloud_bigquery_jdbc_BigQueryJdbcCustomLogger_finer_java_lang_String_)

### finer(Supplier<String> msgSupplier)
    
    
    public void finer(Supplier<String> msgSupplier)

**Parameter**  
---  
**Name** | **Description**  
`msgSupplier` | `[Supplier](https://docs.oracle.com/javase/8/docs/api/java/util/function/Supplier.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
  
**Overrides**

[Logger.finer(Supplier<String>)](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Logger.html#finer-java.util.function.Supplier<java.lang.String>-)

### finerTrace(String methodName, String msg)
    
    
    public void finerTrace(String methodName, String msg)

Log a message at Level.FINER with predefined class name and method name.

**Parameters**  
---  
**Name** | **Description**  
`methodName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`msg` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
  
### finerTrace(String methodName, Supplier<String> msgSupplier)
    
    
    public void finerTrace(String methodName, Supplier<String> msgSupplier)

Log a lazy message at Level.FINER with predefined class name and method name.

**Parameters**  
---  
**Name** | **Description**  
`methodName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`msgSupplier` | `[Supplier](https://docs.oracle.com/javase/8/docs/api/java/util/function/Supplier.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
  
  
### finest(String msg)
    
    
    public void finest(String msg)

**Parameter**  
---  
**Name** | **Description**  
`msg` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Overrides**

[BigQueryJdbcCustomLogger.finest(String msg)](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery-jdbc/latest/com.google.cloud.bigquery.jdbc.BigQueryJdbcCustomLogger#com_google_cloud_bigquery_jdbc_BigQueryJdbcCustomLogger_finest_java_lang_String_)

### finest(Supplier<String> msgSupplier)
    
    
    public void finest(Supplier<String> msgSupplier)

**Parameter**  
---  
**Name** | **Description**  
`msgSupplier` | `[Supplier](https://docs.oracle.com/javase/8/docs/api/java/util/function/Supplier.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
  
**Overrides**

[BigQueryJdbcCustomLogger.finest(Supplier<String> msgSupplier)](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery-jdbc/latest/com.google.cloud.bigquery.jdbc.BigQueryJdbcCustomLogger#com_google_cloud_bigquery_jdbc_BigQueryJdbcCustomLogger_finest_java_util_function_Supplier_java_lang_String__)

### finestTrace(String methodName)
    
    
    public void finestTrace(String methodName)

Log a message at Level.FINEST with predefined class name, method name and messageto avoid stack trace parsing on the hot-path.

**Parameter**  
---  
**Name** | **Description**  
`methodName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
  
### finestTrace(String methodName, String msg)
    
    
    public void finestTrace(String methodName, String msg)

Log a message at Level.FINEST with predefined class name and method name to avoid stack trace parsing on the hot-path.

**Parameters**  
---  
**Name** | **Description**  
`methodName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`msg` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
  
### finestTrace(String methodName, Supplier<String> msgSupplier)
    
    
    public void finestTrace(String methodName, Supplier<String> msgSupplier)

Log a lazy message at Level.FINEST with predefined class name and method name.

**Parameters**  
---  
**Name** | **Description**  
`methodName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`msgSupplier` | `[Supplier](https://docs.oracle.com/javase/8/docs/api/java/util/function/Supplier.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
  
  
### getArrowArrayLogger()
    
    
    public BigQueryJdbcResultSetLogger getArrowArrayLogger()

**Returns**  
---  
**Type** | **Description**  
`[BigQueryJdbcResultSetLogger](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery-jdbc/latest/com.google.cloud.bigquery.jdbc.BigQueryJdbcResultSetLogger)` |   
  
### getArrowStructLogger()
    
    
    public BigQueryJdbcResultSetLogger getArrowStructLogger()

**Returns**  
---  
**Type** | **Description**  
`[BigQueryJdbcResultSetLogger](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery-jdbc/latest/com.google.cloud.bigquery.jdbc.BigQueryJdbcResultSetLogger)` |   
  
### getConnectionId()
    
    
    public String getConnectionId()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getJsonArrayLogger()
    
    
    public BigQueryJdbcResultSetLogger getJsonArrayLogger()

**Returns**  
---  
**Type** | **Description**  
`[BigQueryJdbcResultSetLogger](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery-jdbc/latest/com.google.cloud.bigquery.jdbc.BigQueryJdbcResultSetLogger)` |   
  
### getJsonStructLogger()
    
    
    public BigQueryJdbcResultSetLogger getJsonStructLogger()

**Returns**  
---  
**Type** | **Description**  
`[BigQueryJdbcResultSetLogger](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery-jdbc/latest/com.google.cloud.bigquery.jdbc.BigQueryJdbcResultSetLogger)` |   
  
### log(LogRecord record)
    
    
    public void log(LogRecord record)

**Parameter**  
---  
**Name** | **Description**  
`record` | `[LogRecord](https://docs.oracle.com/javase/8/docs/api/java/util/logging/LogRecord.html)`  
  
**Overrides**

[Logger.log(LogRecord)](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Logger.html#log-java.util.logging.LogRecord-)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
