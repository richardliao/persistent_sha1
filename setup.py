from distutils.core import setup, Extension

module_sha1 = Extension("persistentsha1",
                    sources = ["shamodule.c"])

setup (name = "persistentsha1",
       version = "1.0",
       description = "This is a persistent sha1 package",
       author = "Richard Liao",
       author_email = "richard.liao.i@gmail.com",
       url = "https://github.com/richardliao/persisten_sha1",
       license = "BSD",
       long_description = """This is a persistent sha1 package, based on shamodule.c from python 2.4.6.""",
       ext_modules = [module_sha1])
