pyrocksdb
=========

Python bindings for RocksDB.

This project is under development, and more features are coming soon.

Quick Install
-------------

Quick install for debian/ubuntu like linux distributions.


```
git clone https://github.com/twmht/python-rocksdb.git --recursive -b pybind11
cd python-rocksdb
python setup.py install
```

Quick Usage Guide
-----------------

```python
import pyrocksdb
db = pyrocksdb.DB()
opts = pyrocksdb.Options()
# for multi-thread
opts.IncreaseParallelism()
opts.OptimizeLevelStyleCompaction()
opts.create_if_missing = True
db.open(opts, '/path/to/db')
# put
opts = pyrocksdb.WriteOptions()
db.put(opts, "key1", "value1")
# get
opts = pyrocksdb.ReadOptions()
blob = db.get(opts, "key1")
print (blob.data) # value1
print (blob.status.ok()) # true
#delete
opts = pyrocksdb.WriteOptions()
db.delete(opts, "key1")
db.close()
```
