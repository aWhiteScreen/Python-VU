#include <Python.h>
#include <string.h>
#include <ctype.h>


static PyObject* PangramError;

static PyObject* perfect_pangram(PyObject* self, PyObject* args) {
    const char* text;
    if (!PyArg_ParseTuple(args, "s", &text))
    {
        PyErr_SetString(PangramError, "Expected a string.");
        return NULL;
    }

    int letters[26] = {0};
    int i;
    for (i = 0; text[i]; i++) {
        if (isalpha(text[i])) {
            int index = tolower(text[i]) - 'a';
            letters[index]++;
        }
    }

    for (i = 0; i < 26; i++) {
        if (letters[i] != 1)
            Py_RETURN_FALSE;
    }

    Py_RETURN_TRUE;
}

static PyMethodDef PangramMethods[] = {
    {"perfect_pangram", perfect_pangram, METH_VARARGS, "Checks if the text is a perfect pangram."},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef pangrammodule = {
    PyModuleDef_HEAD_INIT,
    "perfect_pangram",
    "Module for checking perfect pangrams.",
    -1,
    PangramMethods
};

PyMODINIT_FUNC PyInit_perfect_pangram(void) {
    PyObject* module = PyModule_Create(&pangrammodule);

    PangramError = PyErr_NewException("perfect_pangram.PangramError", NULL, NULL);
    Py_INCREF(PangramError);
    PyModule_AddObject(module, "PangramError", PangramError);

    return module;
}
