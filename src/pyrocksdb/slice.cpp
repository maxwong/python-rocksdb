#include <pybind11/pybind11.h>
#include "pyrocksdb.hpp"

namespace py = pybind11;

void init_slice(py::module & m) {
  py::class_<rocksdb::Slice>(m, "Slice")
    .def(py::init<>());
}

