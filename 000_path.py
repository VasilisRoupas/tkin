#1
# from pathlib import Path
# print(Path.cwd())
# path = Path.cwd()
# print(path)
# print(path.__class__)
# print(path.__class__.__name__)

#2
# import os
# print(os.getcwd())
# path = os.getcwd()
# print(path)
# print(path.__class__)
# print(path.__class__.__name__)

#3
# import pathlib
# print(pathlib.Path().absolute())
# path = pathlib.Path().absolute()
# print(path)
# print(path.__class__)
# print(path.__class__.__name__)

#4
# import os
# print(os.path.basename(__file__))
# print(os.path.dirname(__file__))
# filename = os.path.basename(__file__)
# print(filename)
# print(filename.__class__)
# print(filename.__class__.__name__)
# path = os.path.dirname(__file__)
# print(path)
# print(path.__class__)
# print(path.__class__.__name__)

#5
import os
print(os.path.abspath(__file__))
print(os.path.dirname(os.path.abspath(__file__)))
filename = os.path.abspath(__file__)
print(filename)
print(filename.__class__)
print(filename.__class__.__name__)
path = os.path.dirname(__file__)
print(os.path.dirname(os.path.abspath(__file__)))
print(path.__class__)
print(path.__class__.__name__)
