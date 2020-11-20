
import pickle

pkl_filename = 'pickle_model.pkl'
with open(pkl_filename, 'rb') as file:
    pickle_model = pickle.load(file)

res = pickle_model.predict([[5.7, 3.2, 1.1, 3.6]])
print(res)




from os.path import join, abspath, dirname
base_path = dirname(dirname(abspath(__file__)))
os.environ['PATH'] = '%s%s' % (
    os.environ['PATH'],
    join(base_path, 'Library', 'bin'),
)