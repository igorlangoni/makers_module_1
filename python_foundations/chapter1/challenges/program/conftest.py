# Adds the `lib` directory to the import path
import sys, os
current_path = os.path.dirname(os.path.abspath(__file__))
lib_path = os.path.join(current_path, 'lib')
sys.path.append(lib_path)
