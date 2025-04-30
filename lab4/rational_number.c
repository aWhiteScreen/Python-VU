#include <Python.h>

typedef struct {
    PyObject_HEAD
    int numerator;
    int denominator;
} RationalObject;

static PyTypeObject RationalType;

static PyObject* Rational_new(PyTypeObject* type, PyObject* args, PyObject* kwds) {
    RationalObject* self;
    self = (RationalObject*)type->tp_alloc(type, 0);
    if (self != NULL) {
        self->numerator = 0;
        self->denominator = 1;
    }
    return (PyObject*)self;
}

static int Rational_init(RationalObject* self, PyObject* args, PyObject* kwds) {
    int num, denom;
    if (!PyArg_ParseTuple(args, "ii", &num, &denom)) {
        return -1;
    }
    if (denom == 0) {
        PyErr_SetString(PyExc_ZeroDivisionError, "Denominator cannot be zero.");
        return -1;
    }
    self->numerator = num;
    self->denominator = denom;
    return 0;
}

static PyObject* Rational_str(RationalObject* self) {
    return PyUnicode_FromFormat("%d/%d", self->numerator, self->denominator);
}

static PyObject* Rational_add(PyObject* a, PyObject* b) {
    if (!PyObject_TypeCheck(a, &RationalType) || !PyObject_TypeCheck(b, &RationalType)) {
        Py_RETURN_NOTIMPLEMENTED;
    }

    RationalObject* r1 = (RationalObject*)a;
    RationalObject* r2 = (RationalObject*)b;

    int num = r1->numerator * r2->denominator + r2->numerator * r1->denominator;
    int denom = r1->denominator * r2->denominator;

    return PyObject_CallFunction((PyObject*)&RationalType, "ii", num, denom);
}

static PyNumberMethods Rational_as_number = {
    .nb_add = Rational_add,
};

static PyTypeObject RationalType = {
    PyVarObject_HEAD_INIT(NULL, 0)
    .tp_name = "rational.Rational",
    .tp_doc = "Rational number represented as numerator/denominator",
    .tp_basicsize = sizeof(RationalObject),
    .tp_itemsize = 0,
    .tp_flags = Py_TPFLAGS_DEFAULT,
    .tp_new = Rational_new,
    .tp_init = (initproc)Rational_init,
    .tp_str = (reprfunc)Rational_str,
    .tp_as_number = &Rational_as_number,
};

static PyModuleDef rationalmodule = {
    PyModuleDef_HEAD_INIT,
    "rational",
    "Module that defines a Rational number type.",
    -1,
    NULL, NULL, NULL, NULL, NULL
};

PyMODINIT_FUNC PyInit_rational(void) {
    PyObject* m;
    if (PyType_Ready(&RationalType) < 0)
        return NULL;

    m = PyModule_Create(&rationalmodule);
    if (m == NULL)
        return NULL;

    Py_INCREF(&RationalType);
    if (PyModule_AddObject(m, "Rational", (PyObject*)&RationalType) < 0) {
        Py_DECREF(&RationalType);
        Py_DECREF(m);
        return NULL;
    }

    return m;
}
