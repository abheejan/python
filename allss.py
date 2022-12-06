Python 3.10.8 (tags/v3.10.8:aaaf517, Oct 11 2022, 16:50:30) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
sentence = "the cat sat on the mat with the rat cat and rat were playing in the mat and the cat was happy with rat on the mat"

sentence
'the cat sat on the mat with the rat cat and rat were playing in the mat and the cat was happy with rat on the mat'
from collections import Counter
print(dict(Counter(sentence)))
{'t': 18, 'h': 9, 'e': 8, ' ': 26, 'c': 3, 'a': 15, 's': 2, 'o': 2, 'n': 6, 'm': 3, 'w': 4, 'i': 4, 'r': 4, 'd': 2, 'p': 3, 'l': 1, 'y': 2, 'g': 1}
from datetime import datetime
import time
dir(datetime)
['__add__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__radd__', '__reduce__', '__reduce_ex__', '__repr__', '__rsub__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', 'astimezone', 'combine', 'ctime', 'date', 'day', 'dst', 'fold', 'fromisocalendar', 'fromisoformat', 'fromordinal', 'fromtimestamp', 'hour', 'isocalendar', 'isoformat', 'isoweekday', 'max', 'microsecond', 'min', 'minute', 'month', 'now', 'replace', 'resolution', 'second', 'strftime', 'strptime', 'time', 'timestamp', 'timetuple', 'timetz', 'today', 'toordinal', 'tzinfo', 'tzname', 'utcfromtimestamp', 'utcnow', 'utcoffset', 'utctimetuple', 'weekday', 'year']
print ("time.ctime() : ",time.ctime())
time.ctime() :  Tue Dec  6 08:12:16 2022
hrfromnow = (time.time() + 60 * 60)
print ("time.ctime() + 1hr : ",time.ctime(hrfromnow))
time.ctime() + 1hr :  Tue Dec  6 09:12:55 2022
print(datetime)
<class 'datetime.datetime'>
print(datetime.today)
<built-in method today of type object at 0x00007FFC62158CD0>
datetime.today
<built-in method today of type object at 0x00007FFC62158CD0>
>>> print ("time.ctime() : ",time.ctime())
time.ctime() :  Tue Dec  6 08:15:41 2022
>>> print(datetime.today())
2022-12-06 08:16:27.515904
>>> import sys
>>> dir(sys)
['__breakpointhook__', '__displayhook__', '__doc__', '__excepthook__', '__interactivehook__', '__loader__', '__name__', '__package__', '__spec__', '__stderr__', '__stdin__', '__stdout__', '__unraisablehook__', '_base_executable', '_clear_type_cache', '_current_exceptions', '_current_frames', '_deactivate_opcache', '_debugmallocstats', '_enablelegacywindowsfsencoding', '_framework', '_getframe', '_git', '_home', '_xoptions', 'addaudithook', 'api_version', 'argv', 'audit', 'base_exec_prefix', 'base_prefix', 'breakpointhook', 'builtin_module_names', 'byteorder', 'call_tracing', 'copyright', 'displayhook', 'dllhandle', 'dont_write_bytecode', 'exc_info', 'excepthook', 'exec_prefix', 'executable', 'exit', 'flags', 'float_info', 'float_repr_style', 'get_asyncgen_hooks', 'get_coroutine_origin_tracking_depth', 'get_int_max_str_digits', 'getallocatedblocks', 'getdefaultencoding', 'getfilesystemencodeerrors', 'getfilesystemencoding', 'getprofile', 'getrecursionlimit', 'getrefcount', 'getsizeof', 'getswitchinterval', 'gettrace', 'getwindowsversion', 'hash_info', 'hexversion', 'implementation', 'int_info', 'intern', 'is_finalizing', 'maxsize', 'maxunicode', 'meta_path', 'modules', 'orig_argv', 'path', 'path_hooks', 'path_importer_cache', 'platform', 'platlibdir', 'prefix', 'pycache_prefix', 'set_asyncgen_hooks', 'set_coroutine_origin_tracking_depth', 'set_int_max_str_digits', 'setprofile', 'setrecursionlimit', 'setswitchinterval', 'settrace', 'stderr', 'stdin', 'stdlib_module_names', 'stdout', 'thread_info', 'unraisablehook', 'version', 'version_info', 'warnoptions', 'winver']
>>> sys.path()
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    sys.path()
TypeError: 'list' object is not callable
>>> sys.path
['', 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\idlelib', 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\python310.zip', 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\DLLs', 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib', 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310', 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages']
