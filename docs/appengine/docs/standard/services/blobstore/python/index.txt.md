---
url: https://docs.cloud.google.com/appengine/docs/standard/services/blobstore/python/index.txt
title: https://docs.cloud.google.com/appengine/docs/standard/services/blobstore/python/index.txt
method: scrapling+scrapegraph
fetched_at: 2026-10-16T09:30:59.677700+00:00
---

# https://docs.cloud.google.com/appengine/docs/standard/services/blobstore/python/index.txt

> Source: https://docs.cloud.google.com/appengine/docs/standard/services/blobstore/python/index.txt

// [START making_asynchronous_requests_1] upload_url = blobstore.create_upload_url('/upload') slow_operation() self.response.out.write("""""" % upload_url) // [END making_asynchronous_requests_1] // [START making_asynchronous_requests_2] upload_url_rpc = blobstore.create_upload_url_async('/upload') slow_operation() upload_url = upload_url_rpc.get_result() self.response.out.write("""""" % upload_url) // [END making_asynchronous_requests_2] // [START writing_files_to_the_Blobstore] from google.appengine.api import files # Create the file file_name = files.blobstore.create(mime_type='application/octet-stream') # Open the file and write to it with files.open(file_name, 'a') as f: f.write('data') # Finalize the file. Do this before attempting to read it. files.finalize(file_name) # Get the file's blob key blob_key = files.blobstore.get_blob_key(file_name) // [END writing_files_to_the_Blobstore] 
