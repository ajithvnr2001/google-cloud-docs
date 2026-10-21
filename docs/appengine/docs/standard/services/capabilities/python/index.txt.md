---
url: https://docs.cloud.google.com/appengine/docs/standard/services/capabilities/python/index.txt
title: https://docs.cloud.google.com/appengine/docs/standard/services/capabilities/python/index.txt
method: crawl4ai+scrapegraph (scrapling: scrapling thin content (735 chars), fallback to crawl4ai)
fetched_at: 2026-10-14T08:59:27.248663+00:00
---

# https://docs.cloud.google.com/appengine/docs/standard/services/capabilities/python/index.txt

> Source: https://docs.cloud.google.com/appengine/docs/standard/services/capabilities/python/index.txt


    // [START image_resize]
    from google.appengine.api import capabilities
    
    def StoreUploadedProfileImage(self):
        uploaded_image = self.request.get('img')
        # If the images API is unavailable, we'll just skip the resize.
        if capabilities.CapabilitySet('images').is_enabled():
            uploaded_image = images.resize(uploaded_image, 64, 64)
        store(uploaded_image)
    // [END image_resize]
    
    // [START intro]
    from google.appengine.ext import db
    
    def RenderHTMLForm(self):
        if not db.WRITE_CAPABILITY.is_enabled():
            # Datastore is in read-only mode.
    // [END intro]
    
