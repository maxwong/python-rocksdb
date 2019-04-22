import pyrocksdb
import tempfile
import pytest


@pytest.fixture(scope='module')
def db():
    db = pyrocksdb.DB()
    opts = pyrocksdb.Options()
    opts.IncreaseParallelism()
    opts.OptimizeLevelStyleCompaction()
    opts.create_if_missing = True
    tmp = tempfile.TemporaryDirectory()
    s = db.open(opts, tmp.name)
    assert s.ok()
    yield db
    db.close()


def test_put_get(db):
    opts = pyrocksdb.WriteOptions()
    s = db.put(opts, "key1", "value1")
    assert s.ok()
    opts = pyrocksdb.ReadOptions()
    blob = db.get(opts, "key1")
    assert blob.status.ok()
    assert blob.data == 'value1'

def test_delete(db):
    opts = pyrocksdb.WriteOptions()
    s = db.put(opts, "key1", "value1")
    assert s.ok()
    opts = pyrocksdb.ReadOptions()
    blob = db.get(opts, "key1")
    assert blob.status.ok()
    assert blob.data == 'value1'
    opts = pyrocksdb.WriteOptions()
    s = db.delete(opts, "key1")
    assert s.ok()
    opts = pyrocksdb.ReadOptions()
    blob = db.get(opts, "key1")
    assert not blob.status.ok()

def test_iterator(db):
    opts = pyrocksdb.WriteOptions()
    s = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
    for k, v in s.items():
        db.put(opts, k, v)

    opts = pyrocksdb.ReadOptions()
    it = db.iterator(opts)
    it.seek_to_first()
    assert it.valid()
    for k, v in s.items():
        assert it.key().data() == k
        assert it.value().data() == v
        it.next()

    assert not it.valid()


