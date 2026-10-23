---
url: https://docs.cloud.google.com/appengine/docs/standard/services/ndb/polymodelclass/
title: PolyModel Class \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:18:18.665865+00:00
---

# PolyModel Class  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/services/ndb/polymodelclass/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  PolyModel Class Stay organized with collections  Save and categorize content based on your preferences. 

Go Java PHP Python

The `PolyModel` class lets an application define models that support polymorphic queries, in a more flexible way than the standard `Model` class. A query produced from a `PolyModel` derived class can have results that are instances of the class _or_ any of its subclasses. 

It is defined in `google.appengine.ext.ndb.polymodel`. The following example shows the flexibility provided by the PolyModel class. 
    
    
    from google.appengine.ext import ndb
    from google.appengine.ext.ndb import polymodel
    
    class Contact(polymodel.PolyModel):
      phone_number = ndb.PhoneNumberProperty()
      address = ndb.PostalAddressProperty()
    
    class Person(Contact):
      first_name = ndb.StringProperty()
      last_name = ndb.StringProperty()
      mobile_number = ndb.PhoneNumberProperty()
    
    class Company(Contact):
      name = ndb.StringProperty()
      fax_number = ndb.PhoneNumberProperty()
    
    p = Person(phone_number='1-206-555-9234',
               address='123 First Ave., Seattle, WA, 98101',
               first_name='Alfred',
               last_name='Smith',
               mobile_number='1-206-555-0117')
    p.put()
    
    c = Company(phone_number='1-503-555-9123',
                address='P.O. Box 98765, Salem, OR, 97301',
                name='Data Solutions, LLC',
                fax_number='1-503-555-6622')
    c.put()
    
    for contact in Contact.query():
      print 'Phone: %s\nAddress: %s\n\n' % (contact.phone_number, contact.address)

`Contact.query()` returns `Person` and `Company` instances; if `Contact` derived from `Model` instead of from `PolyModel`, each class would have a different `kind` and `Contact.query()` would not return instances of proper subclasses of `Contact`. 

If you wish to retrieve only `Person` instances, use `Person.query()`. You could also use `Contact.query(Contact.class_ == 'Person')`. 

In addition to the regular Model methods, PolyModel has some interesting class methods: 

  * `_get_kind()`: the name of the root class; e.g. `Person._get_kind() == 'Contact'`. The root class, Contact in this example, may override this method to use a different name as the kind used in the datastore (for the entire hierarchy rooted here). 
  * `_class_name()`: the name of the current class; e.g. `Person._class_name() == 'Person'`. A leaf class, Person in our example, may override this method to use a different name as the class name and in the class key. A non-leaf class may also override this method, but beware: its subclasses should also override it, or else they will all use the same class name, and you will soon be very confused. 
  * `_class_key()`: a list of class names giving the hierarchy. For example, `Person._class_key() == ['Contact', 'Person']`. For deeper hierarchies, this will include all bases between `PolyModel` and the current class, including the latter, but excluding PolyModel itself. This is the same as the value of the `class_` property. Its datastore name is 'class'. 



Since the class name is used in the `class_` property and this property is used to distinguish between the subclasses, the class names (as returned by `_class_name()`) should be unique among those subclasses. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
