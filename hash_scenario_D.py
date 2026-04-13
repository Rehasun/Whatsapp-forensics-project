#!/usr/bin/env python
# coding: utf-8

# In[2]:


import hashlib
import os

def hash_file(filepath):
    sha256 = hashlib.sha256()
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            sha256.update(chunk)
    return sha256.hexdigest()

evidence_root = "C:\\evidence_D\\after_backup\\WhatsApp\\Databases"

for root, dirs, files in os.walk(evidence_root):
    for filename in files:
        filepath = os.path.join(root, filename)
        print(hash_file(filepath), filepath)


# In[ ]:




