import importlib
import inspect
import IPython
import openmdao.api as om

def get_object_from_reference(reference):
    split = reference.split('.')
    right = []
    module = None
    while split:
        try:
            module = importlib.import_module('.'.join(split))
            break
        except ModuleNotFoundError:
            right.append(split.pop())
    if module:
        for entry in reversed(right):
            module = getattr(module, entry)
    return module

def show_source_code(reference):

    obj = inspect.getsource(get_object_from_reference(reference))

    return IPython.display.Code(obj, language='python')
