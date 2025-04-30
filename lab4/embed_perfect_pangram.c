#include <Python.h>

int main() {
    Py_Initialize();

    PyObject *pName = PyUnicode_DecodeFSDefault("util_perfect_pangram");
    PyObject *pModule = PyImport_Import(pName);
    Py_DECREF(pName);

    if (pModule != NULL) {
        PyObject *pFunc = PyObject_GetAttrString(pModule, "perfect_pangram");

        if (pFunc && PyCallable_Check(pFunc)) {
            PyObject *pArgs = PyTuple_Pack(1, PyUnicode_FromString("Blowzy night-frumps vex'd Jack Q."));
            PyObject *pValue = PyObject_CallObject(pFunc, pArgs);
            Py_DECREF(pArgs);

            if (pValue != NULL) {
                if (PyObject_IsTrue(pValue)) {
                    printf("It's a perfect pangram.\n");
                } else {
                    printf("Not a perfect pangram.\n");
                }
                Py_DECREF(pValue);
            } else {
                PyErr_Print();
            }
        } else {
            PyErr_Print();
            fprintf(stderr, "Cannot find function 'perfect_pangram'\n");
        }

        Py_XDECREF(pFunc);
        Py_DECREF(pModule);
    } else {
        PyErr_Print();
        fprintf(stderr, "Failed to load module 'util_perfect_pangram'\n");
    }

    Py_Finalize();
    return 0;
}
